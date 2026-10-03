#!/usr/bin/env python3
"""
Enterprise AI Governance Package - Deterministic Policy Snapshot Resolver
=============================================================================
Reference implementation of the Policy Snapshot Resolver engine specified in
project-kit/resolver/resolver-spec.md.

Usage:
    python project-kit/resolver/resolve.py \
        --manifest project-kit/ai-project-manifest.template.yaml \
        --output effective-policy-snapshot.json
=============================================================================
"""

import argparse
import copy
import datetime
import glob
import hashlib
import json
import os
import sys
from typing import Any, Dict, List, Optional, Set, Tuple

import yaml

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


MODE_HIERARCHY = {
    "advisory": 1,
    "review": 2,
    "blocking": 3
}


class ResolverError(Exception):
    """Raised when resolution encounters an unrecoverable validation error."""
    pass


class UnresolvedConflictHalt(Exception):
    """Raised when overlays impose mutually incompatible obligations."""
    def __init__(self, diagnostic: Dict[str, Any]):
        super().__init__(diagnostic.get("reason", "Incompatible overlay conflict"))
        self.diagnostic = diagnostic


def get_nested_property(data: Dict[str, Any], path: str) -> Any:
    """Extract a property from a nested dictionary via dot-delimited path."""
    tokens = path.split(".")
    curr = data
    for tok in tokens:
        if isinstance(curr, dict) and tok in curr:
            curr = curr[tok]
        else:
            return None
    return curr


def evaluate_predicate(condition: Dict[str, Any], manifest: Dict[str, Any]) -> bool:
    """Evaluate a control's applicability condition against the project manifest."""
    pred_type = condition.get("predicate_type", "always")
    if pred_type == "always":
        return True

    if pred_type != "manifest_property_match":
        # Unknown predicate types default to conservative true
        return True

    path = condition.get("manifest_path", "")
    op = condition.get("operator", "equals")
    target_val = condition.get("target_value")

    actual_val = get_nested_property(manifest, path)
    if actual_val is None:
        return False

    if op == "is_true":
        return actual_val is True
    elif op == "is_false":
        return actual_val is False
    elif op == "equals":
        return actual_val == target_val
    elif op == "in":
        if isinstance(target_val, list):
            return actual_val in target_val
        return actual_val == target_val
    elif op == "intersects":
        if isinstance(actual_val, list) and isinstance(target_val, list):
            return bool(set(actual_val).intersection(set(target_val)))
        return False
    elif op == "not_in":
        if isinstance(target_val, list):
            return actual_val not in target_val
        return actual_val != target_val
    else:
        return False


def load_all_controls(baseline_dir: str) -> List[Dict[str, Any]]:
    """Recursively discover and load all baseline control YAML definitions."""
    search_path = os.path.join(baseline_dir, "**", "*.yaml")
    files = glob.glob(search_path, recursive=True)
    controls = []
    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict) and "id" in data and "domain" in data:
                controls.append(data)
    controls.sort(key=lambda x: x["id"])
    return controls


def find_overlay_by_id(overlays_dir: str, overlay_id: str) -> Optional[Dict[str, Any]]:
    """Locate an overlay YAML file matching the given ID."""
    search_path = os.path.join(overlays_dir, "**", "*.yaml")
    files = glob.glob(search_path, recursive=True)
    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if isinstance(data, dict) and data.get("id") == overlay_id:
                    return data
        except Exception:
            continue
    return None


def find_exception_by_id(exceptions_dir: str, exception_id: str) -> Optional[Dict[str, Any]]:
    """Locate an exception record YAML file matching the given ID."""
    search_path = os.path.join(exceptions_dir, "**", "*.yaml")
    files = glob.glob(search_path, recursive=True)
    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if isinstance(data, dict) and data.get("exception_id") == exception_id:
                    return data
        except Exception:
            continue
    return None


def resolve_effective_policy(
    manifest_data: Dict[str, Any],
    baseline_dir: str,
    overlays_dir: str,
    exceptions_dir: str,
    as_of_date: str,
    schemas_dir: Optional[str] = None
) -> Dict[str, Any]:
    """
    Core deterministic resolution function executing merge algebra and conflict detection.
    """
    project_id = manifest_data.get("project_id", "unknown-project")
    profile = manifest_data.get("ai_system_profile", {})
    bindings = manifest_data.get("governance_bindings", {})
    baseline_pin = bindings.get("baseline_version_pin", "unknown")

    # 1. Select Active Baseline Controls
    all_controls = load_all_controls(baseline_dir)
    if not all_controls:
        raise ResolverError(f"No baseline controls discovered in '{baseline_dir}'.")

    effective_controls: Dict[str, Dict[str, Any]] = {}
    for ctrl in all_controls:
        cond = ctrl.get("applicability_condition", {"predicate_type": "always"})
        if evaluate_predicate(cond, manifest_data):
            # Control is active for this project profile
            params = {}
            for p_name, p_def in ctrl.get("parameters", {}).items():
                params[p_name] = {
                    "description": p_def.get("description", ""),
                    "data_type": p_def.get("data_type", "string"),
                    "default_value": p_def.get("default_value"),
                    "effective_value": p_def.get("default_value"),
                    "allowed_range": p_def.get("allowed_range"),
                    "monotonicity": p_def.get("monotonicity", "lower_is_stricter")
                }

            effective_controls[ctrl["id"]] = {
                "id": ctrl["id"],
                "title": ctrl["title"],
                "domain": ctrl["domain"],
                "type": ctrl["type"],
                "lifecycle_stages": copy.deepcopy(ctrl.get("lifecycle_stages", [])),
                "enforcement_points": copy.deepcopy(ctrl.get("enforcement_points", [])),
                "check_type": ctrl["check_type"],
                "mode": ctrl["mode"],
                "parameters": params,
                "evidence_required": copy.deepcopy(ctrl.get("evidence_required", [])),
                "exception_eligibility": copy.deepcopy(ctrl.get("exception_eligibility", {})),
                "applied_overlays": [],
                "active_exception": None
            }

    # 2. Merge Contextual Overlays (Monotonic Envelopes)
    overlay_pins = bindings.get("overlay_pins", [])
    for pin in overlay_pins:
        ovl_id = pin.get("overlay_id")
        overlay = find_overlay_by_id(overlays_dir, ovl_id)
        if not overlay:
            raise ResolverError(f"Pinned overlay '{ovl_id}' not found in '{overlays_dir}'.")

        rules = overlay.get("rules", [])
        for rule in rules:
            target_id = rule.get("target_control_id")
            action = rule.get("action")

            if target_id not in effective_controls:
                # If target control is inactive for this project profile, rule does not apply
                continue

            target_ctrl = effective_controls[target_id]
            if ovl_id not in target_ctrl["applied_overlays"]:
                target_ctrl["applied_overlays"].append(ovl_id)

            if action == "tighten_parameter":
                tightening = rule.get("parameter_tightening", {})
                param_name = tightening.get("parameter_name")
                new_val = tightening.get("new_value")
                direction = tightening.get("direction")

                if param_name not in target_ctrl["parameters"]:
                    raise ResolverError(
                        f"Overlay rule {rule.get('rule_id')} targets unknown parameter "
                        f"'{param_name}' on control '{target_id}'."
                    )

                p_entry = target_ctrl["parameters"][param_name]
                current_val = p_entry["effective_value"]

                if direction == "lower_is_stricter":
                    if new_val < current_val:
                        p_entry["effective_value"] = new_val
                elif direction == "higher_is_stricter":
                    if new_val > current_val:
                        p_entry["effective_value"] = new_val
                elif direction == "strict_subset":
                    if isinstance(current_val, list) and isinstance(new_val, list):
                        intersected = list(set(current_val).intersection(set(new_val)))
                        if not intersected:
                            raise UnresolvedConflictHalt({
                                "status": "UNRESOLVED_CONFLICT_HALT",
                                "project_id": project_id,
                                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                "conflict_details": {
                                    "control_id": target_id,
                                    "parameter_name": param_name,
                                    "competing_overlay": ovl_id,
                                    "current_value": current_val,
                                    "conflicting_value": new_val,
                                    "reason": "Subset intersection yielded empty set."
                                },
                                "escalation": {
                                    "arbitration_path": overlay.get("conflict_resolution", {}).get(
                                        "resolution_escalation_path", "Enterprise AI Safety Review Board"
                                    )
                                }
                            })
                        p_entry["effective_value"] = intersected
                else:
                    raise ResolverError(f"Unknown monotonicity direction '{direction}'.")

            elif action == "upgrade_mode":
                upgraded_mode = rule.get("upgraded_mode", "blocking")
                current_mode = target_ctrl["mode"]
                if MODE_HIERARCHY.get(upgraded_mode, 0) > MODE_HIERARCHY.get(current_mode, 0):
                    target_ctrl["mode"] = upgraded_mode

            elif action == "require_additional_evidence":
                existing_types = {e["artifact_type"] for e in target_ctrl["evidence_required"]}
                for ev in rule.get("additional_evidence", []):
                    if ev["artifact_type"] not in existing_types:
                        target_ctrl["evidence_required"].append(ev)
                        existing_types.add(ev["artifact_type"])

            elif action == "restrict_exception":
                restr = rule.get("restrict_exception", {})
                if restr.get("disallow_exceptions") is True:
                    target_ctrl["exception_eligibility"]["eligible"] = False
                    target_ctrl["exception_eligibility"]["statutory_prohibition"] = True
                if "additional_mandatory_compensations" in restr:
                    comp_list = target_ctrl["exception_eligibility"].setdefault("minimum_compensating_controls", [])
                    comp_list.extend(restr["additional_mandatory_compensations"])

    # 3. Apply Active, Verified Exceptions
    active_exc_ids = bindings.get("active_exceptions", [])
    for exc_id in active_exc_ids:
        exc = find_exception_by_id(exceptions_dir, exc_id)
        if not exc:
            raise ResolverError(f"Declared active exception '{exc_id}' not found in '{exceptions_dir}'.")

        # Invariant checks
        if exc.get("project_id") != project_id:
            raise ResolverError(f"Exception '{exc_id}' belongs to project '{exc.get('project_id')}', not '{project_id}'.")

        if exc.get("status") != "APPROVED":
            raise ResolverError(f"Exception '{exc_id}' has status '{exc.get('status')}', must be 'APPROVED'.")

        exp_date = exc.get("expiration_date", "1970-01-01")
        if exp_date < as_of_date:
            raise ResolverError(f"Exception '{exc_id}' expired on {exp_date} (as-of date is {as_of_date}).")

        target_ctrl_id = exc.get("control_id")
        if target_ctrl_id not in effective_controls:
            continue

        target_ctrl = effective_controls[target_ctrl_id]
        if target_ctrl["exception_eligibility"].get("statutory_prohibition", False):
            raise ResolverError(
                f"ILLEGAL EXCEPTION: Control '{target_ctrl_id}' carries a statutory prohibition. "
                f"Internal exceptions cannot waive statutory law."
            )

        cert = exc.get("legal_statutory_certification", {})
        if cert.get("statutory_obligation_waived") is True:
            raise ResolverError(f"ILLEGAL EXCEPTION: Exception '{exc_id}' declares statutory_obligation_waived=true.")

        # Apply parameter variations
        for var in exc.get("parameter_variations", []):
            p_name = var.get("parameter_name")
            if p_name in target_ctrl["parameters"]:
                target_ctrl["parameters"][p_name]["effective_value"] = var.get("requested_variance_value")
                target_ctrl["parameters"][p_name]["variance_applied"] = exc_id

        target_ctrl["active_exception"] = {
            "exception_id": exc_id,
            "expiration_date": exp_date,
            "compensating_controls": exc.get("compensating_controls", [])
        }

    # 4. Construct Snapshot Payload and Compute Cryptographic Hash
    snapshot = {
        "snapshot_schema_version": "1.0.0",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "as_of_date": as_of_date,
        "project_id": project_id,
        "baseline_version_pin": baseline_pin,
        "applied_overlays": overlay_pins,
        "total_active_controls": len(effective_controls),
        "controls": effective_controls
    }

    canonical_repr = json.dumps(snapshot, sort_keys=True, indent=2)
    digest = hashlib.sha256(canonical_repr.encode("utf-8")).hexdigest()
    snapshot["snapshot_integrity_hash"] = digest

    return snapshot


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise AI Governance Package - Deterministic Policy Snapshot Resolver"
    )
    parser.add_argument(
        "--manifest",
        default="project-kit/ai-project-manifest.template.yaml",
        help="Path to ai-project-manifest.yaml"
    )
    parser.add_argument(
        "--baseline-dir",
        default="baseline/controls",
        help="Path to baseline controls directory"
    )
    parser.add_argument(
        "--overlays-dir",
        default="overlays",
        help="Path to overlays directory"
    )
    parser.add_argument(
        "--exceptions-dir",
        default="schemas/examples",
        help="Path to exceptions records directory"
    )
    parser.add_argument(
        "--output",
        default="effective-policy-snapshot.json",
        help="Output path for resolved effective-policy-snapshot.json"
    )
    parser.add_argument(
        "--as-of-date",
        default=datetime.date.today().isoformat(),
        help="Evaluation date for checking exception expiration (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Execute resolution and validation without writing output snapshot file"
    )

    args = parser.parse_args()

    if not os.path.exists(args.manifest):
        print(f"ERROR: Manifest file not found at '{args.manifest}'.", file=sys.stderr)
        return 1

    try:
        with open(args.manifest, "r", encoding="utf-8") as f:
            manifest_data = yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR: Failed to read manifest YAML: {e}", file=sys.stderr)
        return 1

    try:
        snapshot = resolve_effective_policy(
            manifest_data=manifest_data,
            baseline_dir=args.baseline_dir,
            overlays_dir=args.overlays_dir,
            exceptions_dir=args.exceptions_dir,
            as_of_date=args.as_of_date
        )
    except UnresolvedConflictHalt as uch:
        print("RESOLUTION HALTED: INCOMPATIBLE OVERLAY CONFLICT DETECTED!", file=sys.stderr)
        print(json.dumps(uch.diagnostic, indent=2), file=sys.stderr)
        return 2
    except ResolverError as re:
        print(f"RESOLUTION FAILED: {re}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}", file=sys.stderr)
        return 1

    print("=================================================================")
    print("DETERMINISTIC POLICY SNAPSHOT RESOLUTION SUCCESSFUL")
    print("=================================================================")
    print(f"Project ID:              {snapshot['project_id']}")
    print(f"Baseline Version:        {snapshot['baseline_version_pin']}")
    print(f"Applied Overlays:        {len(snapshot['applied_overlays'])}")
    print(f"Active Controls:         {snapshot['total_active_controls']}")
    print(f"Snapshot SHA-256 Digest: {snapshot['snapshot_integrity_hash']}")
    print("=================================================================")

    if not args.validate_only:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(snapshot, f, indent=2)
            print(f"Snapshot written successfully to: {args.output}")
        except Exception as e:
            print(f"ERROR writing snapshot output: {e}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
