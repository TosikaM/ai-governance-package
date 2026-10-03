# Enterprise Policy on AI Accountability, Registration, and System Inventory

**Policy Identifier:** `ORG-POL-ACC-001`  
**Associated Principle:** `ORG-PRIN-ACC` (Accountability & AI Inventory)  
**Status:** DRAFT  
**Effective Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: Enterprise AI Governance Lead]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Purpose & Scope

This policy establishes mandatory operational accountability and centralized inventory registration for all Artificial Intelligence (AI) systems, machine learning models, retrieval-augmented generation (RAG) applications, and autonomous agents designed, procured, developed, or operated by the enterprise.

This policy applies across all business units, operating subsidiaries, engineering teams, and third-party vendors delivering AI software.

---

## 2. Normative Requirements

### 2.1 Mandatory Inventory Registration
1. **Pre-Training & Pre-Deployment Registration:** Every AI system must be registered in the Central AI Inventory Registry prior to the expenditure of production training compute, access to production datasets, or deployment to any staging or production environment.
2. **Permanent System Identifier:** Upon intake, the registry assigns a unique, immutable System Identifier (`SYS-ID`) formatted in accordance with the enterprise inventory taxonomy.
3. **Machine-Readable Declaration:** Every software repository containing AI code, pipeline definitions, or agent configurations must maintain an `ai-project-manifest.yaml` adhering to `schemas/project-manifest.schema.json` in its root directory.

### 2.2 Unambiguous Ownership Assignment
1. **Named Business Owner:** Every AI system must have an active, named Enterprise Business Owner accountable for business justification, ethical alignment, regulatory compliance, and risk acceptance.
2. **Named Technical Lead:** Every system must designate an active Technical Lead accountable for architecture, pipeline security, model evaluation, and runtime guardrails.
3. **Owner Transition:** If a designated owner or lead departs the organization or changes roles, successor ownership must be formally assigned and updated in the registry within `10 business days` [approximate, verify against enterprise HR policy]. Unowned systems are subject to automated staging freezes.

### 2.3 Algorithmic Transparency Record
1. Each registered system must document its primary AI archetype (`predictive_ml`, `generative_llm`, `rag_system`, `autonomous_agent`, or `hybrid`), intended purpose, operational boundaries, and known limitations.

---

## 3. Separation of Automated Checks and Human Judgment

| Requirement | Verification Mechanism | Check Type | Enforcement Point | Mode |
|---|---|---|---|---|
| Manifest File Presence (`ai-project-manifest.yaml`) | Automated static file check | Automated | Pre-commit hook & CI pipeline | Blocking |
| Manifest Schema Conformance | Validates against `schemas/project-manifest.schema.json` | Automated | CI build pipeline | Blocking |
| Active Registry Registration & `SYS-ID` Binding | API query against Central AI Registry | Automated | Deployment admission controller | Blocking |
| Authenticity of Business Owner & Commercial Purpose | Evaluation of business case and risk categorization | Human Judgment | AI Review Board Intake Gate | Review |
| Annual Ownership Re-certification | Confirmation of ongoing operational necessity | Human Judgment | Annual Governance Review | Review |

---

## 4. Roles & Responsibilities

- **Enterprise Business Owner:** Accountable for system business justification, risk acceptance, and regulatory defensibility.
- **Technical Lead:** Responsible for maintaining `ai-project-manifest.yaml`, registering the system, and ensuring pipeline admission gates pass.
- **AI Governance Registry Administrator:** Responsible for maintaining the central registry service, schema versions, and audit reporting.
- **Platform Engineering:** Responsible for enforcing automated admission blocks on unverified system IDs.

---

## 5. Non-Conformance & Exceptions

Systems lacking valid inventory registration or active ownership will be denied deployment admission by automated cluster controllers. Emergency deviations require an approved `ORG-EXC` record with compensating controls. Internal exceptions never waive statutory or regulatory disclosure obligations.

---

## 6. Authoritative Reference Mappings

- **NIST AI RMF 1.0:** GOVERN 1.1, GOVERN 1.2, GOVERN 2.1 (Inventory of AI systems, clear accountability roles).
- **ISO/IEC 42001:2023:** Clause 5.3 (Organizational roles, responsibilities and authorities), Clause 8.1 (Operational planning and control).
- **EU AI Act Regulation (EU) 2024/1689:** Article 49, Article 71 (EU database registration for high-risk AI systems; mapping to verify for exact delegated act formatting).
