# Enterprise Policy on Human Oversight, Contestability, and Redress

**Policy Identifier:** `ORG-POL-HUM-001`  
**Associated Principle:** `ORG-PRIN-HUM` (Human Agency, Oversight & Contestability)  
**Status:** DRAFT  
**Effective Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: Head of Operations & Consumer Rights Lead]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Purpose & Scope

This policy mandates effective human oversight architectures across all Artificial Intelligence systems and guarantees accessible, verifiable mechanisms for individuals to contest automated decisions and obtain human review and redress.

This policy applies to all systems that inform, automate, or execute decisions impacting employees, customers, or third-party individuals.

---

## 2. Normative Requirements

### 2.1 Oversight Operational Models
Every AI system must designate and technically enforce its human oversight model in `ai-project-manifest.yaml`:
1. **Human-in-the-Loop (HITL):** A qualified human operator must review and explicitly approve the AI recommendation before any binding action, decision, or communication is committed. Mandatory for all Tier 3 High-Risk systems producing material legal or economic effects.
2. **Human-on-the-Loop (HOTL):** The system executes actions autonomously within bounded parameters, with real-time human monitoring and an immediate, non-disruptive capability to override, alter, or abort active executions.
3. **Human-in-Command (HIC):** System oversight is exercised at the strategic and operational level, with the technical ability to suspend, alter, or permanently terminate the entire AI system lifecycle.

### 2.2 Operator Competence & Prevention of Automation Bias
1. **Meaningful Authority:** Designated human overseers must possess the operational authority, technical competence, and sufficient time to scrutinize AI outputs rather than rubber-stamping algorithmic suggestions (automation bias mitigation).
2. **Audit of Override Frequency:** Enterprise monitoring must track human override and rejection rates. An override rate of zero in high-stakes workflows will trigger an immediate governance audit to investigate automation complacency.

### 2.3 Contestability & Human Redress Mechanisms
1. **Right to Contest:** Any individual subject to an automated or AI-assisted decision producing significant legal, economic, or contractual consequences must be provided a simple, accessible channel to contest the decision.
2. **Mandatory Human Review Pathway:** Contested decisions must be routed to a qualified human adjudicator who was not involved in the initial automated recommendation and who possesses full authority to reverse the automated outcome.
3. **Turnaround SLA:** Human review and formal response must be completed within `15 business days` [approximate; verify against enterprise consumer service and regulatory SLAs].

---

## 3. Separation of Automated Checks and Human Judgment

| Requirement | Verification Mechanism | Check Type | Enforcement Point | Mode |
|---|---|---|---|---|
| Oversight Model Declaration in Manifest | Validation of `oversight_model` field in manifest | Automated | CI build pipeline | Blocking |
| Programmatic Override & Stop Endpoint Existence | Integration test validating technical pause/override API | Automated | Integration Test Pipeline | Blocking |
| Audit Telemetry of Human Approvals | Telemetry verification that actions require signed reviewer token | Automated | Admission / Runtime Interceptor | Blocking |
| Human Operator Competence & Cognitive Workload | Operational assessment of operator workload and training | Human Judgment | Operational Readiness Review | Review |
| Substantive Fairness of Redress Adjudication | Case audit of contested decision outcomes and appeals | Human Judgment | Quarterly Compliance Audit | Review |

---

## 4. Roles & Responsibilities

- **System Technical Lead:** Implements operator review dashboards, override controls, and telemetry capture for human interventions.
- **Operations Managers:** Ensure designated human reviewers receive adequate training, manageable workloads, and clear decision criteria.
- **Customer Redress / Grievance Officers:** Manage the intake, investigation, and adjudication of contested AI decisions.
- **AI Safety & Governance Review Board:** Oversees override metrics and audits automation bias indicators.

---

## 5. Non-Conformance & Exceptions

A high-risk system deployed without an active human approval queue or omitting human redress pathways represents a severe governance breach requiring immediate system suspension. Exceptions must be recorded under `ORG-EXC` and signed by the Chief Operating Officer. Internal exceptions never waive statutory rights to human review (e.g., GDPR Article 22, EU AI Act Article 14).

---

## 6. Authoritative Reference Mappings

- **EU AI Act Regulation (EU) 2024/1689:** Article 14 (Human oversight of high-risk AI systems), Article 86 (Right to explanation of individual decision-making).
- **Regulation (EU) 2016/679 (GDPR):** Article 22 (Automated individual decision-making, including profiling; right to obtain human intervention).
- **NIST AI RMF 1.0:** GOVERN 1.2, MANAGE 2.2, MANAGE 2.4 (Human oversight, fallback procedures, redress).
- **ISO/IEC 42001:2023:** Annex A.5.4 (Human oversight).
