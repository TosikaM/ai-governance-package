# Deterministic Policy Snapshot Resolver Specification

**Module:** M4 Project Integration Kit  
**Status:** DRAFT  
**Version:** 0.1.0-draft  
**Owner Placeholder:** [ROLE: AI Governance Platform Architect]  
**Review Date:** [YYYY-MM-DD]  

---

## 1. Overview & Architectural Role

The **Deterministic Policy Snapshot Resolver** is the core calculation engine of the Enterprise AI Governance Package. It bridges abstract enterprise policies and concrete project CI/CD pipelines.

Every AI project maintains an `ai-project-manifest.yaml` in its repository root declaring its architecture, operational characteristics, risk tier, registered components, and governance version pins. The Resolver evaluates this manifest against the immutable Enterprise Baseline (61 controls) and any declared contextual overlays, applies approved exceptions, and outputs a versioned, cryptographically hashed `effective-policy-snapshot.json`.

```
+------------------------------------+
|     ai-project-manifest.yaml       |
|  - Archetype & characteristics    |
|  - Baseline & Overlay pins         |
|  - Active exception references     |
+------------------------------------+
                  |
                  v
+-------------------------------------------------------+
|             Deterministic Resolver Engine             |
|  1. Validate manifest against JSON schema             |
|  2. Select active baseline controls via predicates    |
|  3. Sequentially merge pinned overlays (Monotonic)    |
|  4. Detect conflicts -> UNRESOLVED_CONFLICT_HALT      |
|  5. Apply verified, unexpired exceptions              |
|  6. Calculate cryptographic SHA-256 digest            |
+-------------------------------------------------------+
                  |
                  v
+------------------------------------+
|   effective-policy-snapshot.json   |
|  - Pinned controls & parameters    |
|  - Enforced modes (blocking/review)|
|  - Required evidence artifacts     |
|  - SHA-256 integrity hash          |
+------------------------------------+
                  |
                  +----------> Pre-Commit Hooks
                  +----------> PR Verification Actions
                  +----------> CI/CD Deployment Gates
                  +----------> Runtime Interceptors
```

### Determinism Guarantee
The resolver is strictly pure and deterministic:
$$\text{Snapshot} = \mathcal{R}(\text{Manifest}, \text{Baseline}, \text{Overlays}, \text{Exceptions}, \text{Timestamp})$$
Given identical inputs, the resolver outputs bit-for-bit identical policy snapshots across developer workstations, CI/CD runners, and audit environments.

---

## 2. Formal Resolution Algorithm (Pseudocode)

```python
def resolve_effective_policy(
    manifest_path: str,
    baseline_dir: str,
    overlays_dir: str,
    exceptions_dir: str,
    as_of_date: str
) -> ResolvedSnapshot:
    """
    Executes deterministic resolution of effective governance policy.
    """
    # -------------------------------------------------------------------------
    # PHASE 1: MANIFEST INGESTION & VALIDATION
    # -------------------------------------------------------------------------
    manifest = load_yaml(manifest_path)
    validate_json_schema(manifest, "schemas/project-manifest.schema.json")
    
    project_id = manifest["project_id"]
    profile = manifest["ai_system_profile"]
    bindings = manifest["governance_bindings"]

    # -------------------------------------------------------------------------
    # PHASE 2: BASELINE CONTROL SELECTION
    # -------------------------------------------------------------------------
    baseline_controls = load_all_baseline_controls(baseline_dir)
    effective_controls = {}

    for control in baseline_controls:
        is_active = evaluate_applicability(control["applicability_condition"], profile)
        if is_active:
            effective_controls[control["id"]] = {
                "id": control["id"],
                "title": control["title"],
                "domain": control["domain"],
                "type": control["type"],
                "lifecycle_stages": control["lifecycle_stages"],
                "enforcement_points": control["enforcement_points"],
                "check_type": control["check_type"],
                "mode": control["mode"],  # advisory, review, blocking
                "parameters": deep_copy(control.get("parameters", {})),
                "evidence_required": deep_copy(control.get("evidence_required", [])),
                "exception_eligibility": deep_copy(control.get("exception_eligibility", {})),
                "reference_mappings": control.get("reference_mappings", []),
                "origin": "baseline",
                "applied_overlays": [],
                "active_exception": None
            }

    # -------------------------------------------------------------------------
    # PHASE 3: CONTEXTUAL OVERLAY MERGING (MONOTONIC ENVELOPE)
    # -------------------------------------------------------------------------
    overlay_pins = bindings.get("overlay_pins", [])
    
    for pin in overlay_pins:
        overlay = load_overlay(overlays_dir, pin["overlay_id"])
        validate_json_schema(overlay, "schemas/overlay.schema.json")
        verify_semver_compatibility(pin["version_pin"], overlay["baseline_compatibility"])

        for rule in overlay["rules"]:
            target_id = rule["target_control_id"]
            action = rule["action"]
            
            # If target control is not in baseline, check if overlay introduces it
            if target_id not in effective_controls:
                if action == "add_control":
                    effective_controls[target_id] = create_control_from_rule(rule, overlay["id"])
                    continue
                else:
                    # Target control was inactive due to predicate mismatch; rule does not apply
                    continue

            ctrl = effective_controls[target_id]
            ctrl["applied_overlays"].append(overlay["id"])

            # Rule Action: Tighten Numerical Parameter
            if action == "tighten_parameter":
                tightening = rule["parameter_tightening"]
                param_name = tightening["parameter_name"]
                new_val = tightening["new_value"]
                direction = tightening["direction"]

                if param_name not in ctrl["parameters"]:
                    raise ResolverError(f"Parameter '{param_name}' does not exist on control '{target_id}'")

                param_def = ctrl["parameters"][param_name]
                current_val = param_def.get("effective_value", param_def["default_value"])

                if direction == "lower_is_stricter":
                    param_def["effective_value"] = min(current_val, new_val)
                elif direction == "higher_is_stricter":
                    param_def["effective_value"] = max(current_val, new_val)
                elif direction == "strict_subset":
                    param_def["effective_value"] = list(set(current_val).intersection(set(new_val)))
                    if len(param_def["effective_value"]) == 0:
                        return trigger_conflict_halt(
                            conflict_type="EMPTY_SUBSET_INTERSECTION",
                            control_id=target_id,
                            parameter=param_name,
                            overlay=overlay["id"]
                        )
                else:
                    return trigger_conflict_halt(
                        conflict_type="UNKNOWN_MONOTONICITY_DIRECTION",
                        control_id=target_id,
                        parameter=param_name,
                        overlay=overlay["id"]
                    )

            # Rule Action: Upgrade Enforcement Mode
            elif action == "upgrade_mode":
                upgraded_mode = rule["upgraded_mode"]
                mode_ladder = {"advisory": 1, "review": 2, "blocking": 3}
                if mode_ladder[upgraded_mode] > mode_ladder[ctrl["mode"]]:
                    ctrl["mode"] = upgraded_mode

            # Rule Action: Require Additional Evidence
            elif action == "require_additional_evidence":
                existing_types = {e["artifact_type"] for e in ctrl["evidence_required"]}
                for ev in rule["additional_evidence"]:
                    if ev["artifact_type"] not in existing_types:
                        ctrl["evidence_required"].append(ev)
                        existing_types.add(ev["artifact_type"])

            # Rule Action: Restrict Exceptions
            elif action == "restrict_exception":
                restr = rule["restrict_exception"]
                if restr.get("disallow_exceptions") is True:
                    ctrl["exception_eligibility"]["eligible"] = false
                    ctrl["exception_eligibility"]["statutory_prohibition"] = true
                if "additional_mandatory_compensations" in restr:
                    comp_list = ctrl["exception_eligibility"].setdefault("minimum_compensating_controls", [])
                    comp_list.extend(restr["additional_mandatory_compensations"])

    # -------------------------------------------------------------------------
    # PHASE 4: TIME-LIMITED EXCEPTION BINDING
    # -------------------------------------------------------------------------
    active_exc_ids = bindings.get("active_exceptions", [])
    
    for exc_id in active_exc_ids:
        exc = load_exception(exceptions_dir, exc_id)
        validate_json_schema(exc, "schemas/exception.schema.json")

        # Invariant: Exception project_id must match manifest
        if exc["project_id"] != project_id:
            raise ResolverError(f"Exception {exc_id} belongs to project {exc['project_id']}, not {project_id}")

        # Invariant: Exception must be in APPROVED state
        if exc["status"] != "APPROVED":
            raise ResolverError(f"Exception {exc_id} is in status {exc['status']}, not APPROVED")

        # Invariant: Exception must not be expired
        if exc["expiration_date"] < as_of_date:
            raise ResolverError(f"Exception {exc_id} expired on {exc['expiration_date']} (as of {as_of_date})")

        # Invariant: Statutory legal obligations CANNOT be waived
        target_ctrl = effective_controls.get(exc["control_id"])
        if target_ctrl is None:
            continue

        if target_ctrl["exception_eligibility"].get("statutory_prohibition", False):
            raise ResolverError(
                f"ILLEGAL EXCEPTION: Control {target_ctrl['id']} carries statutory prohibition. "
                f"Internal exceptions cannot waive statutory law."
            )

        if exc["legal_statutory_certification"]["statutory_obligation_waived"] is True:
            raise ResolverError(f"ILLEGAL EXCEPTION: {exc_id} declares statutory_obligation_waived=true.")

        # Apply approved parameter variations
        for var in exc.get("parameter_variations", []):
            p_name = var["parameter_name"]
            if p_name in target_ctrl["parameters"]:
                target_ctrl["parameters"][p_name]["effective_value"] = var["requested_variance_value"]
                target_ctrl["parameters"][p_name]["exception_applied"] = exc_id

        # Attach compensating controls
        target_ctrl["active_exception"] = {
            "exception_id": exc_id,
            "expiration_date": exc_expiration_date,
            "compensating_controls": exc["compensating_controls"]
        }

    # -------------------------------------------------------------------------
    # PHASE 5: SERIALIZATION & INTEGRITY HASHING
    # -------------------------------------------------------------------------
    snapshot_payload = {
        "snapshot_schema_version": "1.0.0",
        "generated_at": current_iso_timestamp(),
        "as_of_date": as_of_date,
        "project_id": project_id,
        "manifest_hash": calculate_sha256(manifest_path),
        "baseline_version": bindings["baseline_version_pin"],
        "applied_overlays": overlay_pins,
        "total_active_controls": len(effective_controls),
        "controls": effective_controls
    }

    canonical_json = json.dumps(snapshot_payload, sort_keys=True, indent=2)
    integrity_hash = sha256_hex(canonical_json)
    snapshot_payload["snapshot_integrity_hash"] = integrity_hash

    return snapshot_payload
```

---

## 3. Predicate Evaluation Logic

Conditional controls declare an `applicability_condition` matching manifest properties:

| Predicate Operator | Evaluation Logic | Example Manifest Path |
|---|---|---|
| `always` | Always returns `true`. Universal baseline controls. | N/A |
| `is_true` | Returns `true` if target boolean property is `true`. | `ai_system_profile.declared_characteristics.executes_tools_or_code` |
| `is_false` | Returns `true` if target boolean property is `false`. | `ai_system_profile.declared_characteristics.operates_in_safety_critical_context` |
| `in` | Returns `true` if manifest string is present in target array. | `ai_system_profile.risk_tier in ["tier_2_moderate", "tier_3_high"]` |
| `intersects` | Returns `true` if manifest array shares at least one element with target array. | `ai_system_profile.data_classifications intersects ["restricted_pii", "regulated_health"]` |
| `equals` | Returns `true` if manifest property equals target value. | `ai_system_profile.archetype equals "autonomous_agent"` |

---

## 4. Conflict Handling & UNRESOLVED_CONFLICT_HALT

When two overlays declare contradictory requirements with no mathematical ordering relation (e.g., mutually exclusive data residency regions, incompatible retention periods with equal statutory rank):

1. The Resolver halts execution immediately with exit code `2`.
2. No `effective-policy-snapshot.json` is generated.
3. The Resolver emits a structured diagnostic conflict report:

```json
{
  "status": "UNRESOLVED_CONFLICT_HALT",
  "project_id": "customer-copilot",
  "timestamp": "2026-10-02T01:21:00Z",
  "conflict_details": {
    "control_id": "ORG-CTL-DAT-003",
    "parameter_name": "allowed_storage_regions",
    "competing_overlays": [
      {
        "overlay_id": "ORG-OVL-GEO-EU-001",
        "declared_value": ["eu-central-1", "eu-west-1"]
      },
      {
        "overlay_id": "ORG-OVL-GEO-US-001",
        "declared_value": ["us-east-1", "us-west-2"]
      }
    ],
    "mathematical_intersection": [],
    "reason": "Intersection yields empty set. Mutually exclusive data residency mandates."
  },
  "escalation": {
    "arbitration_body": "Enterprise AI Safety Review Board and Legal Counsel",
    "required_action": "Submit architectural variance or partition regional data pipelines."
  }
}
```

---

## 5. Downstream Consumer Integration

The resulting `effective-policy-snapshot.json` is committed into the repository or generated dynamically in CI/CD pipelines:
- **Pre-commit hooks:** Reads `snapshot.json` to verify developer prompt templates and secret scanners.
- **Pull Request Actions:** Compares PR diff against `snapshot.controls` to enforce blocking checks.
- **Model Registry Admission Gates:** Blocks model promotion if `eval_benchmark_report` does not satisfy snapshot parameters (e.g. `max_hallucination_rate`).
- **Runtime Gateway Sidecars:** Enforces real-time rate limits, toxicity thresholds, and token ceilings declared in the snapshot.
