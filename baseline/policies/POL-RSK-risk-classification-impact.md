# Enterprise Policy on AI Risk Classification and Impact Assessment

**Policy Identifier:** `ORG-POL-RSK-001`  
**Associated Principle:** `ORG-PRIN-RSK` (Risk Classification & Impact Assessment)  
**Status:** DRAFT  
**Effective Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: Enterprise AI Risk Officer]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Purpose & Scope

This policy establishes the mandatory enterprise risk taxonomy and Algorithmic Impact Assessment (AIIA) process for all AI systems. It ensures that system risks—including safety, legal, civil rights, privacy, and business continuity risks—are quantified, categorized, and mitigated commensurate with their potential impact.

This policy applies to all AI systems across all lifecycle phases from concept to production.

---

## 2. Normative Requirements

### 2.1 Enterprise 4-Tier Risk Classification Taxonomy
Every registered AI system must be classified into exactly one of four enterprise risk tiers, documented in its `ai-project-manifest.yaml`:

| Risk Tier | Definition & Characteristics | Governance & Control Posture |
|---|---|---|
| **Tier 1: Minimal Risk** | Systems with negligible societal, financial, or personal impact (e.g., developer code autocompletion with mandatory peer review, internal document search, spam filtering). | Baseline automated controls apply; self-certification by Technical Lead; periodic spot audits. |
| **Tier 2: Moderate Risk** | Systems with intermediate impact or public interaction without binding consequences (e.g., customer support conversational bots, marketing copy generation, internal operational forecasting). | Baseline automated controls + pre-deployment review; mandatory evaluation benchmarks; annual review. |
| **Tier 3: High Risk** | Systems influencing critical decisions (employment, creditworthiness, legal/contractual rights, healthcare assistance, educational access) or executing autonomous actions. | Full baseline + applicable regulatory overlays; mandatory comprehensive AIIA; independent ARB sign-off; continuous monitoring. |
| **Tier 4: Unacceptable Risk** | Systems posing intolerable safety, ethical, or legal risks (prohibited practices under `ORG-POL-USE-001`). | Prohibited. System intake rejected; automated deployment blocked. |

### 2.2 Mandatory AI Impact Assessment (AIIA)
1. **Completion Milestone:** An AIIA adhering to `templates/ai-impact-assessment.md` must be completed and approved prior to moving any Tier 2 or Tier 3 system to staging or production.
2. **Evaluation Scope:** The assessment must evaluate data provenance, model limitations, security posture, fairness/bias, human oversight adequacy, and potential adverse impacts on vulnerable populations.
3. **Approval Authority:** Tier 2 systems require approval by the Domain Risk Officer. Tier 3 systems require formal sign-off by the Enterprise AI Safety & Governance Review Board.

### 2.3 Reassessment on Material Change
An updated AIIA and risk review must be triggered whenever a material change occurs, including:
1. Replacement of the underlying foundation model or major version upgrade.
2. Expansion of system autonomy (e.g., granting write permissions to an agent previously restricted to read-only tools).
3. Ingestion of new data classifications (e.g., incorporating PII into a previously public corpus).
4. Expansion into new geographic jurisdictions or regulated business sectors.

---

## 3. Separation of Automated Checks and Human Judgment

| Requirement | Verification Mechanism | Check Type | Enforcement Point | Mode |
|---|---|---|---|---|
| Risk Tier Declaration in Manifest | Schema validation of `ai_system_profile.risk_tier` | Automated | CI build pipeline | Blocking |
| Tier 4 (Unacceptable Risk) Admission Block | Automated rule rejecting `tier_4_unacceptable` | Automated | CI / Admission Controller | Blocking |
| AIIA Document Attachment for Tier 2/3 | Verifies `ORG-EVD` record of approved AIIA | Automated | Deployment admission controller | Blocking |
| Substantive Rigor & Validity of Impact Assessment | Multi-disciplinary evaluation of residual harm | Human Judgment | AI Review Board Gate | Review |
| Determination of "Material Change" Threshold | Expert evaluation of algorithmic architectural changes | Human Judgment | Change Advisory Board (CAB) | Review |

---

## 4. Roles & Responsibilities

- **Technical Lead:** Authors the initial risk self-assessment and completes the technical sections of the AIIA.
- **Enterprise Business Owner:** Endorses the risk assessment and formally accepts residual risks.
- **Enterprise AI Risk Officer:** Independently validates the assigned risk tier and scrutinizes mitigation adequacy.
- **AI Safety & Governance Review Board:** Approves Tier 3 High-Risk deployments and resolves classification appeals.

---

## 5. Non-Conformance & Exceptions

Systems lacking a validated risk tier or an approved AIIA for Tier 2/3 cannot pass automated deployment admission. Internal exceptions never waive statutory high-risk assessment obligations (e.g., EU AI Act Fundamental Rights Impact Assessment under Article 27).

---

## 6. Authoritative Reference Mappings

- **NIST AI RMF 1.0:** GOVERN 1.1, MAP 1.1, MAP 2.1, MAP 3.1 (Categorizing AI systems, context mapping, risk characterization).
- **ISO/IEC 23894:2023:** Clause 6 (Risk assessment process for AI).
- **ISO/IEC 42001:2023:** Clause 6.1 (Actions to address risks and opportunities), Annex A.4 (AI impact assessment).
- **EU AI Act Regulation (EU) 2024/1689:** Article 6, Article 9 (Risk management system for high-risk AI), Article 27 (Fundamental rights impact assessment).
