import os
import re

# BEFORE GOVERNANCE (NON-COMPLIANT):
# 1. Hardcoded API Secret was present:
# OPENAI_API_KEY = "sk-proj-demo99887766554433221100aaabbbccc" # VIOLATION: POL-SEC-01
# 2. Automated rejections without human recruiter review (EU AI Act High-Risk Violation: POL-OVR-01)
# 3. Retaining candidate PII indefinitely (Data Privacy Violation: POL-RET-01)

# AFTER GOVERNANCE (REMEDIATED & COMPLIANT):
# 1. Credentials loaded securely from environment:
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# 2. Candidate schema explicitly tracks PII fields for governance data card
CANDIDATE_SCHEMA = {
    "first_name": str,
    "last_name": str,
    "email": str,
    "phone": str,
    "skills": list,
    "experience_years": float
}

def analyze_resume(candidate_data: dict) -> dict:
    """
    Parses resume text and calculates a preliminary match score.
    In accordance with High-Risk AI Governance rules (POL-OVR-01):
    - NO automated rejection is permitted.
    - Output is strictly advisory for human HR recruiters.
    """
    skills = candidate_data.get("skills", [])
    exp = candidate_data.get("experience_years", 0)
    score = min(100.0, (len(skills) * 15.0) + (exp * 8.0))
    
    return {
        "candidate_id": f"CAN-{candidate_data.get('email', 'anon').split('@')[0]}",
        "match_score": round(score, 2),
        "governance_status": "PENDING_HUMAN_REVIEW", # Human oversight enforced
        "advisory_notes": "Passed to HR recruiter for evaluation. Automated rejection disabled."
    }

if __name__ == "__main__":
    sample_applicant = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com",
        "phone": "+1-555-0199",
        "skills": ["Python", "Machine Learning", "Governance"],
        "experience_years": 4.5
    }
    result = analyze_resume(sample_applicant)
    print("Screening Result:", result)
