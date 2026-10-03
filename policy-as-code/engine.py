#!/usr/bin/env python3
"""
Enterprise AI Governance Package - Tool-Neutral Policy-as-Code Engine
=============================================================================
Evaluates declarative AI governance policy rules against project contexts,
manifests, evaluation reports, and runtime telemetry.

Usage:
    python policy-as-code/engine.py \
        --rules policy-as-code/rules/01-accountability-inventory.yaml \
        --context sample-context.json
=============================================================================
"""

import argparse
import glob
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional, Tuple

import yaml

SEMVER_REGEX = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(-[a-z0-9.]+)?$")
SHA256_REGEX = re.compile(r"^[a-fA-F0-9]{64}$")
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def get_nested_field(data: Dict[str, Any], path: str) -> Tuple[bool, Any]:
    """Retrieve field value from dot-delimited path, returning (found, value)."""
    tokens = path.split(".")
    curr = data
    for tok in tokens:
        if isinstance(curr, dict) and tok in curr:
            curr = curr[tok]
        elif isinstance(curr, list) and tok.isdigit():
            idx = int(tok)
            if 0 <= idx < len(curr):
                curr = curr[idx]
            else:
                return False, None
        else:
            return False, None
    return True, curr


def evaluate_assertion(assertion: Dict[str, Any], context: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Evaluates a single assertion against context data.
    Returns (passed, failure_detail).
    """
    field_path = assertion["field_path"]
    operator = assertion["operator"]
    expected = assertion.get("expected_value")
    failure_msg = assertion["failure_message"]

    found, actual = get_nested_field(context, field_path)

    if operator == "exists":
        if not found or actual is None:
            return False, f"{failure_msg} (Field '{field_path}' does not exist)"
        return True, ""

    if not found or actual is None:
        return False, f"{failure_msg} (Required field '{field_path}' is missing)"

    if operator == "not_empty":
        if actual == "" or actual == [] or actual == {}:
            return False, f"{failure_msg} (Field '{field_path}' is empty)"
        return True, ""

    elif operator == "equals":
        if actual != expected:
            return False, f"{failure_msg} (Expected '{expected}', found '{actual}')"
        return True, ""

    elif operator == "not_equals":
        if actual == expected:
            return False, f"{failure_msg} (Expected not '{expected}', found equal)"
        return True, ""

    elif operator == "less_than_or_equal":
        try:
            if float(actual) > float(expected):
                return False, f"{failure_msg} (Actual {actual} > threshold {expected})"
        except (ValueError, TypeError):
            return False, f"{failure_msg} (Could not compare non-numerical values '{actual}' and '{expected}')"
        return True, ""

    elif operator == "greater_than_or_equal":
        try:
            if float(actual) < float(expected):
                return False, f"{failure_msg} (Actual {actual} < threshold {expected})"
        except (ValueError, TypeError):
            return False, f"{failure_msg} (Could not compare non-numerical values '{actual}' and '{expected}')"
        return True, ""

    elif operator == "in":
        if isinstance(expected, list):
            if actual not in expected:
                return False, f"{failure_msg} (Value '{actual}' not in permitted set {expected})"
        else:
            if actual != expected:
                return False, f"{failure_msg} (Value '{actual}' != '{expected}')"
        return True, ""

    elif operator == "not_in":
        if isinstance(expected, list) and actual in expected:
            return False, f"{failure_msg} (Prohibited value '{actual}' present in {expected})"
        elif actual == expected:
            return False, f"{failure_msg} (Prohibited value '{actual}' matched expected)"
        return True, ""

    elif operator == "contains":
        if isinstance(actual, (list, str)) and expected not in actual:
            return False, f"{failure_msg} (Collection does not contain '{expected}')"
        return True, ""

    elif operator == "not_contains":
        if isinstance(actual, (list, str)) and expected in actual:
            return False, f"{failure_msg} (Prohibited element '{expected}' found in collection)"
        return True, ""

    elif operator == "regex_match":
        if not re.search(str(expected), str(actual)):
            return False, f"{failure_msg} (Value '{actual}' does not match pattern '{expected}')"
        return True, ""

    elif operator == "is_valid_email":
        if not EMAIL_REGEX.match(str(actual)):
            return False, f"{failure_msg} (Value '{actual}' is not a valid email address)"
        return True, ""

    elif operator == "is_valid_sha256":
        if not SHA256_REGEX.match(str(actual)):
            return False, f"{failure_msg} (Value '{actual}' is not a valid 64-character SHA-256 hexadecimal hash)"
        return True, ""

    elif operator == "is_valid_semver":
        if not SEMVER_REGEX.match(str(actual)):
            return False, f"{failure_msg} (Value '{actual}' is not a valid SemVer string)"
        return True, ""

    return False, f"Unknown operator '{operator}'"


def evaluate_rule(rule: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates all assertions in a rule against the provided context.
    Returns structured rule evaluation report.
    """
    rule_id = rule["rule_id"]
    target_ctrl = rule["target_control_id"]
    title = rule["title"]
    mode = rule["mode"]
    remediation = rule["remediation"]

    passed = True
    violations = []

    for assertion in rule["assertions"]:
        a_id = assertion["assertion_id"]
        a_passed, detail = evaluate_assertion(assertion, context)
        if not a_passed:
            passed = False
            violations.append({
                "assertion_id": a_id,
                "description": assertion["description"],
                "detail": detail
            })

    return {
        "rule_id": rule_id,
        "target_control_id": target_ctrl,
        "title": title,
        "mode": mode,
        "status": "PASS" if passed else "FAIL",
        "violations": violations,
        "remediation": remediation if not passed else None
    }


def evaluate_rule_file(rule_path: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Loads a rule YAML file and evaluates all constituent rules."""
    with open(rule_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    results = []
    for rule in data.get("rules", []):
        results.append(evaluate_rule(rule, context))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise AI Governance - Policy-as-Code Evaluation Engine"
    )
    parser.add_argument("--rules", required=True, help="Path to rule YAML file or directory")
    parser.add_argument("--context", required=True, help="Path to input context JSON or YAML file")
    parser.add_argument("--output", help="Optional output path for evaluation report JSON")

    args = parser.parse_args()

    # Load context
    with open(args.context, "r", encoding="utf-8") as f:
        if args.context.endswith(".yaml") or args.context.endswith(".yml"):
            context = yaml.safe_load(f)
        else:
            context = json.load(f)

    # Discover rules
    if os.path.isdir(args.rules):
        rule_files = glob.glob(os.path.join(args.rules, "**", "*.yaml"), recursive=True)
    else:
        rule_files = [args.rules]

    total_rules = 0
    passed_rules = 0
    failed_blocking = 0
    failed_advisory = 0
    all_results = []

    for rf in rule_files:
        try:
            results = evaluate_rule_file(rf, context)
            for res in results:
                total_rules += 1
                all_results.append(res)
                if res["status"] == "PASS":
                    passed_rules += 1
                else:
                    if res["mode"] == "blocking":
                        failed_blocking += 1
                    else:
                        failed_advisory += 1
        except Exception as e:
            print(f"ERROR evaluating '{rf}': {e}", file=sys.stderr)
            return 1

    report = {
        "summary": {
            "total_rules": total_rules,
            "passed": passed_rules,
            "failed_blocking": failed_blocking,
            "failed_advisory": failed_advisory,
            "verdict": "BLOCKED" if failed_blocking > 0 else "ADMITTED"
        },
        "results": all_results
    }

    print("=================================================================")
    print("POLICY-AS-CODE EVALUATION REPORT")
    print("=================================================================")
    print(f"Total Rules Checked:  {total_rules}")
    print(f"Passed:               {passed_rules}")
    print(f"Failed (Blocking):    {failed_blocking}")
    print(f"Failed (Advisory):    {failed_advisory}")
    print(f"Pipeline Verdict:     {report['summary']['verdict']}")
    print("=================================================================")

    if failed_blocking > 0:
        print("\nBLOCKING VIOLATIONS:")
        for res in all_results:
            if res["status"] == "FAIL" and res["mode"] == "blocking":
                print(f"\n[FAIL] {res['rule_id']} ({res['target_control_id']}): {res['title']}")
                for v in res["violations"]:
                    print(f"  - {v['detail']}")
                print(f"  Remediation: {res['remediation']}")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"\nDetailed report written to: {args.output}")

    return 2 if failed_blocking > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
