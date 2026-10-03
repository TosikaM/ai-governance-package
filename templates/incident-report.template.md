# AI Safety & Security Incident Report (Post-Mortem)

**Incident Identifier:** `ORG-INC-[YEAR]-[SEQUENCE]`  
**Status:** DRAFT  
**Incident Severity:** [P1 - Critical / P2 - Major / P3 - Moderate / P4 - Minor]  
**Affected System Name:** [System Name]  
**Project ID:** [project_id matching ai-project-manifest.yaml]  
**Incident Date & Time:** [YYYY-MM-DD HH:MM UTC]  
**Incident Commander Placeholder:** [ROLE: AI Incident Response Commander]  
**Lead Investigator Placeholder:** [ROLE: AI Safety & Security Incident Lead]  
**Governed Control:** [`ORG-CTL-MON-004`](file:///c:/ai-governance-package/baseline/controls/monitoring-incidents/CTL-MON-004.yaml) (AI Incident Triage, Circuit Breaking, and RCA Reporting)

---

## 1. Executive Summary

- **Brief Synopsis:** [Concise 2-3 sentence overview of what occurred, how it was detected, and operational impact.]
- **Impact Classification:**
  - [ ] **Prompt Injection / Jailbreak Bypass:** Adversary bypassed safety guardrails.
  - [ ] **Data Leakage / PII Ingestion:** Confidential data exposed to unauthorized recipients.
  - [ ] **Hallucination / Misinformation:** False output caused customer detriment or material business error.
  - [ ] **Algorithmic Disparity / Discrimination:** Demographic disparity detected in live decisions.
  - [ ] **Runaway Agent Loop / Cost Spike:** Recursive tool-calling loop or token exhaustion.
  - [ ] **Service Degradation / Model Drift:** Unexpected latency spike or performance collapse.

---

## 2. Chronological Incident Timeline (UTC)

| Timestamp (UTC) | Phase | Event Description | Action Taken & Operator |
|---|---|---|---|
| `[YYYY-MM-DD 00:00]` | **Inception** | First anomalous input or trigger condition executed. | [System telemetry initiated anomalous trace.] |
| `[YYYY-MM-DD 00:05]` | **Detection** | Alert fired or user report logged. | [Alert fired to AI SRE on-call rotation.] |
| `[YYYY-MM-DD 00:12]` | **Triage** | Incident response team assembled; severity confirmed. | [Incident Commander declared P1 incident.] |
| `[YYYY-MM-DD 00:20]` | **Containment** | Emergency circuit breaker or kill switch tripped. | [Triggered ORG-CTL-AGT-004 kill switch; traffic halted.] |
| `[YYYY-MM-DD 01:15]` | **Mitigation** | Corrective filter or fallback model deployed. | [Factual grounding threshold tightened; sidecar updated.] |
| `[YYYY-MM-DD 02:00]` | **Restoration** | Production service restored under active monitoring. | [Production traffic re-admitted under 100% human review.] |

---

## 3. Blast Radius & Impact Assessment

- **Users Affected:** [Number of internal staff, enterprise customers, or public users exposed.]
- **Data Compromised:** [State whether PII, intellectual property, or confidential financials were exposed; specify volume.]
- **Financial & Operational Impact:** [Estimated cost of erroneous transactions, emergency response hours, or third-party API spend.]
- **Regulatory Reporting Obligations:**
  - EU AI Act Article 73 Serious Incident Reporting triggered: [YES / NO]
  - GDPR Article 33 72-Hour Supervisory Authority Notification required: [YES / NO]
  - Legal Counsel Notification Reference: `[ROLE: Lead Legal Counsel - Regulatory AI]`

---

## 4. Root Cause Analysis (5 Whys Methodology)

1. **Why did the failure occur?** [Direct trigger description.]
2. **Why was the trigger not intercepted?** [Why did the input guardrail or model filter miss the prompt?]
3. **Why did the evaluation harness not detect this vulnerability?** [Gap in benchmark test suite or edge cases.]
4. **Why did pipeline gates permit deployment?** [Gap in CI/CD thresholds or unpinned dependencies.]
5. **Why was the organizational process deficient?** [Systemic governance or architectural root cause.]

---

## 5. Corrective & Preventative Actions (CAPA)

| Action ID | Corrective Action Description | Target Control | Owner Placeholder | Due Date |
|---|---|---|---|:---:|
| **CAPA-01** | Update prompt injection heuristic regex list in gateway sidecar. | `ORG-CTL-SEC-001` | `[ROLE: AI Security Engineer]` | [YYYY-MM-DD] |
| **CAPA-02** | Add adversarial test cases to evaluation benchmark harness. | `ORG-CTL-ROB-001` | `[ROLE: AI Evaluation Lead]` | [YYYY-MM-DD] |
| **CAPA-03** | Tighten circuit breaker threshold to trigger at 3 consecutive anomalies. | `ORG-CTL-MON-004` | `[ROLE: AI Platform SRE Lead]` | [YYYY-MM-DD] |
| **CAPA-04** | Conduct formal post-mortem review with Enterprise Review Board. | `ORG-CTL-ACC-002` | `[ROLE: Enterprise AI Risk Lead]` | [YYYY-MM-DD] |

---

## 6. Incident Sign-Offs

| Role | Name | Decision | Date |
|---|---|:---:|:---:|
| **AI Incident Response Commander** | [Name] | [CLOSED] | [YYYY-MM-DD] |
| **Enterprise Chief Information Security Officer (CISO)** | [Name] | [APPROVED] | [YYYY-MM-DD] |
| **Lead Regulatory AI Legal Counsel** | [Name] | [APPROVED] | [YYYY-MM-DD] |
| **Enterprise Chief Risk Officer** | [Name] | [APPROVED] | [YYYY-MM-DD] |
