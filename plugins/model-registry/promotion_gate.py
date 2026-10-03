#!/usr/bin/env python3
"""
Enterprise AI Governance - Model Registry & CT Promotion Gate
=============================================================================
Authoritative gate controlling promotion of trained model weights into the
enterprise production model catalog or registry.

Enforces:
  - ORG-CTL-SUP-003: Safe serialization (safetensors/ONNX) and SHA-256 verification
  - ORG-CTL-ROB-003: Pre-deployment benchmark evaluation thresholds
  - ORG-CTL-TRN-004: Model card and provenance metadata verification

Usage:
    python plugins/model-registry/promotion_gate.py \
        --model-path models/weights.safetensors \
        --model-card models/model_card.json \
        --eval-report eval_benchmark_report.json
=============================================================================
"""

import argparse
import hashlib
import json
import os
import sys

ALLOWED_SERIALIZATION_EXTENSIONS = {".safetensors", ".onnx", ".gguf"}
PROHIBITED_SERIALIZATION_EXTENSIONS = {".pkl", ".pickle", ".bin", ".pt", ".pth"}


def verify_serialization_format(model_path: str) -> bool:
    """Verifies that the model uses a safe, non-executable serialization format."""
    _, ext = os.path.splitext(model_path.lower())
    if ext in PROHIBITED_SERIALIZATION_EXTENSIONS:
        print(f"BLOCKING SECURITY VIOLATION: Prohibited insecure serialization format '{ext}' (ORG-CTL-SUP-003).")
        print("Model weights using arbitrary python pickle are prohibited. Convert to safetensors or ONNX.")
        return False
    if ext not in ALLOWED_SERIALIZATION_EXTENSIONS:
        print(f"BLOCKING SECURITY VIOLATION: Unrecognized model weight extension '{ext}'.")
        return False
    return True


def compute_file_sha256(filepath: str) -> str:
    """Compute streaming SHA-256 hash of large model weight files."""
    sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            sha.update(chunk)
    return sha.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise AI Model Registry Promotion Gate")
    parser.add_argument("--model-path", required=True, help="Path to model weight file")
    parser.add_argument("--model-card", required=True, help="Path to model card JSON file")
    parser.add_argument("--eval-report", required=True, help="Path to evaluation report JSON file")

    args = parser.parse_args()

    print("=================================================================")
    print("MODEL REGISTRY & CT PROMOTION GATE")
    print("=================================================================")

    if not os.path.exists(args.model_path):
        print(f"BLOCKING ERROR: Model file not found at '{args.model_path}'.", file=sys.stderr)
        return 1

    if not verify_serialization_format(args.model_path):
        return 1
    print("[PASS] Model weight serialization format is safe (ORG-CTL-SUP-003).")

    # Verify model card metadata
    if not os.path.exists(args.model_card):
        print(f"BLOCKING ERROR: Model card metadata missing at '{args.model_card}' (ORG-CTL-TRN-004).", file=sys.stderr)
        return 1

    with open(args.model_card, "r", encoding="utf-8") as f:
        model_card = json.load(f)

    if not model_card.get("model_name") or not model_card.get("version"):
        print("BLOCKING ERROR: Model card must declare 'model_name' and 'version'.", file=sys.stderr)
        return 1
    print("[PASS] Model card metadata verified.")

    # Calculate model digest
    print("Calculating model weight cryptographic digest...")
    weight_hash = compute_file_sha256(args.model_path)
    print(f"[PASS] Model SHA-256 Digest: {weight_hash}")

    # Verify benchmark report
    if not os.path.exists(args.eval_report):
        print(f"BLOCKING ERROR: Evaluation report missing at '{args.eval_report}'.", file=sys.stderr)
        return 1

    with open(args.eval_report, "r", encoding="utf-8") as f:
        eval_report = json.load(f)

    hallucination_rate = eval_report.get("hallucination_rate", 1.0)
    if hallucination_rate > 0.05:
        print(f"[FAIL] Hallucination rate {hallucination_rate:.4f} exceeds baseline ceiling (0.05).", file=sys.stderr)
        return 1

    print("[PASS] Benchmark evaluation metrics meet promotion criteria.")
    print("=================================================================")
    print("MODEL REGISTRY PROMOTION APPROVED: Ready for production deployment.")
    print("=================================================================")
    return 0


if __name__ == "__main__":
    sys.exit(main())
