# Algorithmic Impact Assessment (AIIA) Template

**Document Identifier:** `ORG-AIIA-[YEAR]-[PROJECT_ID]`  
**Status:** DRAFT  
**System Name:** [System Name]  
**Project ID:** [project_id matching ai-project-manifest.yaml]  
**Assessor Placeholder:** [ROLE: AI Governance Assessor / Ethics Lead]  
**Review Board Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Initial Assessment Date:** [YYYY-MM-DD]  
**Last Review Date:** [YYYY-MM-DD]  
**Applicability:** Mandatory for all Tier 2 (Moderate Risk) and Tier 3 (High Risk) systems prior to production deployment (governed by [`ORG-CTL-RSK-002`](file:///c:/ai-governance-package/baseline/controls/risk-classification/CTL-RSK-002.yaml)).

---

## 1. System Overview & Business Purpose

### 1.1 Intended Use & Context
- **Business Objective:** [Describe the core business problem this AI system solves.]
- **Deployment Context:** [Specify where and how the system will operate: internal operations, customer-facing, automated processing, decision-support.]
- **System Archetype:** [Predictive ML / Generative LLM / RAG Knowledge System / Autonomous Agent / Hybrid]
- **Target Users & Affected Stakeholders:** [Identify internal operators, enterprise customers, vulnerable groups, or members of the general public affected by outputs.]

### 1.2 Out-of-Scope & Prohibited Uses
- **Explicit Exclusions:** [Detail operational domains or use cases where this system MUST NOT be used (e.g., employment screening, automated credit denial without human review).]
- **Misuse Scenarios:** [Detail foreseeable misuse modes (e.g., jailbreaks, prompt injection, extraction of training secrets).]

---

## 2. Fundamental Rights, Legal & Ethical Assessment

Evaluate the impact of system outputs across fundamental human rights and societal dimensions:

| Impact Dimension | Potential Impact | Severity (1-5) | Likelihood (1-5) | Proposed Mitigations |
|---|---|:---:|:---:|---|
| **Non-Discrimination & Fairness** | Risk of demographic disparity, proxy bias, or unfair treatment of protected classes. | [1-5] | [1-5] | [e.g., Disparate impact auditing (`ORG-CTL-FAI-001`), proxy variable removal.] |
| **Privacy & Data Protection** | Unauthorized ingestion, leakage, or memorization of Personally Identifiable Information (PII). | [1-5] | [1-5] | [e.g., Automated PII redaction (`ORG-CTL-DAT-002`), differential privacy.] |
| **Human Dignity & Autonomy** | Risk of user deception, manipulation, or erosion of meaningful human choice. | [1-5] | [1-5] | [e.g., Conspicuous disclosure (`ORG-CTL-TRN-001`), accessible redress channels.] |
| **Safety & Physical Integrity** | Potential for physical hazard, health impairment, or critical infrastructure disruption. | [1-5] | [1-5] | [e.g., Hardware interlocks, fail-safe kill switch (`ORG-CTL-AGT-004`).] |
| **Economic & Legal Rights** | Denial of benefits, housing, credit, or contractual entitlements. | [1-5] | [1-5] | [e.g., Mandatory HITL review (`ORG-CTL-HUM-001`), explainability (`ORG-CTL-TRN-003`).] |

---

## 3. Data Governance & Lineage Evaluation

- **Data Sources:** [Enumerate primary training datasets, vector corpora, or fine-tuning datasets.]
- **Consent & Legal Basis:** [State GDPR / statutory basis: consent, legitimate interest, contractual necessity.]
- **Copyright & Licensing:** [Confirm commercial use rights under [`ORG-CTL-IPR-001`](file:///c:/ai-governance-package/baseline/controls/intellectual-property/CTL-IPR-001.yaml); confirm absence of copyleft contamination.]
- **Data Quality & Representativeness:** [Detail dataset curation, label validation, and historical bias remediation.]
- **Retention & Minimization:** [Confirm alignment with retention schedule (`ORG-CTL-DAT-004`); specify purging schedule.]

---

## 4. Technical Robustness, Security & Performance

- **Benchmark Accuracy:** [Report baseline performance on domain evaluation harnesses (`ORG-CTL-ROB-001`).]
- **Hallucination & Error Bounds:** [Measured hallucination rate; state whether within ceiling (`ORG-CTL-ROB-003`).]
- **Adversarial Resilience:** [Summarize red-teaming or prompt injection testing outcomes (`ORG-CTL-SEC-001`, `004`).]
- **Cybersecurity & Vector Layer:** [Confirm Zero-Trust ACLs on vector embeddings (`ORG-CTL-SEC-002`).]
- **Autonomous Safeguards:** [If agentic: confirm outside-the-model PEP, step caps, and kill switch SLA (`ORG-CTL-AGT-001` to `004`).]

---

## 5. Human Oversight & Operational Governance

- **Oversight Paradigm:**
  - [ ] **Human-in-the-Loop (HITL):** Mandatory pre-action approval by human operator.
  - [ ] **Human-on-the-Loop (HOTL):** Continuous real-time monitoring with instantaneous stop authority.
  - [ ] **Human-in-Command (HIC):** System provides situational awareness; human decides and acts.
- **Automation Bias Controls:** [Measures to detect rubber-stamping or reviewer complacency (`ORG-CTL-HUM-004`).]
- **Contestability Workflow:** [Process by which affected individuals can contest automated decisions and obtain human review within 5 business days (`ORG-CTL-HUM-003`).]

---

## 6. Risk Scoring & Residual Risk Matrix

### Risk Calculation Formula
$$\text{Risk Score} = \text{Severity} \times \text{Likelihood} \quad (\text{Scale: } 1 - 25)$$

- **Inherent Risk Score:** [1-25] ([Low / Medium / High / Critical])
- **Residual Risk Score (Post-Mitigation):** [1-25] ([Low / Medium / High])

### Formal Risk Acceptance Gate
- [ ] **Approved without conditions:** Residual risk is Low.
- [ ] **Approved with mandatory conditions:** Residual risk is Medium; compensating controls attached.
- [ ] **Rejected / Escalated:** Residual risk is High or Critical; escalated to Executive Risk Committee.

---

## 7. Accountable Sign-Offs & Attestations

| Role | Name | Decision | Date | Signature / Reference |
|---|---|---|:---:|---|
| **System Technical Lead** | [Name] | [APPROVED / CONDITIONAL] | [YYYY-MM-DD] | `[ROLE: Lead AI Engineer]` |
| **Business Product Owner** | [Name] | [APPROVED / CONDITIONAL] | [YYYY-MM-DD] | `[ROLE: Business Product Owner]` |
| **Enterprise AI Risk Officer** | [Name] | [APPROVED / CONDITIONAL] | [YYYY-MM-DD] | `[ROLE: Enterprise AI Risk Lead]` |
| **Lead Legal Counsel (Regulatory AI)** | [Name] | [APPROVED / CONDITIONAL] | [YYYY-MM-DD] | `[ROLE: Legal Counsel - Regulatory AI]` |

> [!NOTE]
> Adopting this assessment template does not establish regulatory compliance or legal certification. Legal applicability requires qualified legal counsel review.
