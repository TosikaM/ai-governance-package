#!/usr/bin/env python3
"""
Enterprise AI Governance - Pre-Commit Secret Scanner (Advisory)
=============================================================================
Scans staged text files for accidental hardcoded AI API keys and secrets.
=============================================================================
"""

import re
import sys

SECRET_PATTERNS = [
    ("OpenAI API Key", re.compile(r"sk-[a-zA-Z0-9]{20,T3BlbkFJ[a-zA-Z0-9]{20,}")),
    ("Anthropic API Key", re.compile(r"sk-ant-[a-zA-Z0-9_\-]{30,}")),
    ("HuggingFace Token", re.compile(r"hf_[a-zA-Z0-9]{34,}")),
    ("Generic AI Gateway Bearer Token", re.compile(r"(?i)(ai_gateway_token|llm_api_key)\s*[:=]\s*['\"][a-zA-Z0-9_\-]{20,}['\"]"))
]


def scan_file(filepath: str) -> int:
    issues = 0
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line_no, line in enumerate(f, 1):
                for name, pat in SECRET_PATTERNS:
                    if pat.search(line):
                        print(f"ADVISORY WARNING: Potential {name} detected in {filepath}:{line_no}")
                        issues += 1
    except Exception:
        pass
    return issues


def main() -> int:
    files = sys.argv[1:]
    total_issues = 0
    for f in files:
        total_issues += scan_file(f)
    if total_issues > 0:
        print(f"\n[ADVISORY] Found {total_issues} potential AI credential leak(s).")
        print("Please use enterprise secret management or environment variables before pushing.")
        # Pre-commit advisory returns 1 to alert developer, but can be bypassed with --no-verify locally
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
