# Sample Project: HR Resume Screening System (High-Risk AI)

## Business Overview
This application assists HR talent acquisition teams by parsing candidate resumes, assessing skills, and ranking suitability for open positions.

## Why This is High-Risk (Tier 3)
Under the **EU AI Act (Annex III)**, AI systems used for recruitment and selection of natural persons are classified as **High-Risk AI**. They carry severe regulatory, legal, and reputational risk if unmanaged.

## What Was Caught as Non-Compliant (Before Governance)
1. **Accidental Hardcoded API Secret:** The OpenAI API key was pasted directly in `resume_scanner.py`.
2. **Missing Human-in-the-Loop Oversight:** The initial code attempted automated candidate rejections, violating `POL-OVR-01`.
3. **No Retention Limit on Personal Data:** Candidate resumes, emails, and phone numbers had no documented deletion schedule.

## How Governance Was Plugged In & Remediated (After Governance)
1. **Secret Remediated:** API keys moved to secure environment variables; pre-commit secret shield installed.
2. **Human Review Enforced:** System modified to output advisory scores only (`PENDING_HUMAN_REVIEW`), ensuring recruiters make all final hiring decisions.
3. **Cards & Policies Sealed:** Model Card created with 85% fairness parity ratio; Data Card configured with strict 1-year retention limit.
4. **Audit Report Generated:** Visual compliance audit report generated at `governance-compliance-report.html`.
