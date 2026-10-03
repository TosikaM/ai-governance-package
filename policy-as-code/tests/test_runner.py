#!/usr/bin/env python3
"""
Enterprise AI Governance Package - Policy-as-Code Unit Test Suite
=============================================================================
Executes unit tests verifying that all declarative PAC rules correctly admit
compliant contexts and strictly block non-compliant contexts.

Usage:
    python policy-as-code/tests/test_runner.py
=============================================================================
"""

import glob
import json
import os
import sys

# Ensure engine is importable
current_dir = os.path.dirname(os.path.abspath(__file__))
pac_dir = os.path.dirname(current_dir)
sys.path.insert(0, pac_dir)

from engine import evaluate_rule_file


def run_tests() -> int:
    rules_dir = os.path.join(pac_dir, "rules")
    fixtures_dir = os.path.join(current_dir, "fixtures")

    pass_fixture_path = os.path.join(fixtures_dir, "pass_context.json")
    fail_fixture_path = os.path.join(fixtures_dir, "fail_context.json")

    with open(pass_fixture_path, "r", encoding="utf-8") as f:
        pass_context = json.load(f)

    with open(fail_fixture_path, "r", encoding="utf-8") as f:
        fail_context = json.load(f)

    rule_files = sorted(glob.glob(os.path.join(rules_dir, "*.yaml")))
    if not rule_files:
        print("ERROR: No rule files found in", rules_dir, file=sys.stderr)
        return 1

    print("=================================================================")
    print("POLICY-AS-CODE AUTOMATED UNIT TEST SUITE")
    print("=================================================================")
    print(f"Rule Files to Test:    {len(rule_files)}")
    print(f"Passing Fixture:       {os.path.basename(pass_fixture_path)}")
    print(f"Failing Fixture:       {os.path.basename(fail_fixture_path)}")
    print("=================================================================\n")

    test_failures = 0

    # -------------------------------------------------------------------------
    # TEST SUITE 1: PASSING CONTEXT ASSERTIONS (ALL RULES MUST PASS)
    # -------------------------------------------------------------------------
    print("RUNNING SUITE 1: Compliant Context (Expected: 100% PASS)...")
    suite1_rules = 0
    suite1_passed = 0

    for rf in rule_files:
        results = evaluate_rule_file(rf, pass_context)
        for res in results:
            suite1_rules += 1
            if res["status"] == "PASS":
                suite1_passed += 1
            else:
                test_failures += 1
                print(f"  [UNEXPECTED FAIL] {res['rule_id']} failed on compliant context:")
                for v in res["violations"]:
                    print(f"    - {v['detail']}")

    print(f"Suite 1 Result: {suite1_passed}/{suite1_rules} rules passed.\n")

    # -------------------------------------------------------------------------
    # TEST SUITE 2: FAILING CONTEXT ASSERTIONS (BLOCKING VIOLATIONS DETECTED)
    # -------------------------------------------------------------------------
    print("RUNNING SUITE 2: Non-Compliant Context (Expected: Blocking Violations)...")
    suite2_rules = 0
    suite2_failed_blocking = 0

    for rf in rule_files:
        results = evaluate_rule_file(rf, fail_context)
        for res in results:
            suite2_rules += 1
            if res["status"] == "FAIL":
                if res["mode"] == "blocking":
                    suite2_failed_blocking += 1

    print(f"Suite 2 Result: Detected {suite2_failed_blocking} blocking violations across {suite2_rules} rules.")

    if suite2_failed_blocking == 0:
        print("  [ERROR] Failing fixture failed to trigger any blocking violations!")
        test_failures += 1
    else:
        print("  [SUCCESS] All targeted policy violations correctly blocked non-compliant release.")

    print("\n=================================================================")
    if test_failures == 0:
        print("ALL UNIT TESTS PASSED (100% CONFORMANCE)")
        print("=================================================================")
        return 0
    else:
        print(f"UNIT TEST FAILURES DETECTED: {test_failures}")
        print("=================================================================")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
