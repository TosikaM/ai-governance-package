# AI Governance Framework Design: Portable Continuation Record

## 1. Run Metadata & Current Status
- **Run Scope:** Full framework
- **Depth:** Standard
- **Audience:** Mixed (Architects, Engineers, Governance Teams, Executives)
- **Current Stage Completed:** Stage 1
- **Deliverables Completed:**
  - Deliverable 1: Feasibility and boundaries
  - Deliverable 2: Principles and baseline structure
  - Deliverable 3: Reference architecture
  - Deliverable 5: Profiles, overlays, and policy composition
- **Remaining Deliverables:**
  - Stage 2: Deliverables 4 (Control catalogue), 11 (Standards mapping), 12 (Operating model)
  - Stage 3: Deliverables 6 (Packaging & repository), 7 (Lifecycle integration), 8 (Agent runtime authorization), 9 (Governance service operations)
  - Stage 4: Deliverables 10 (Concrete implementation examples), 13 (Existing-system onboarding), 14 (Verification & conformance)
  - Stage 5: Deliverables 15 (Technology choices), 16 (Roadmap & metrics), 17 (Assumptions & coverage audit)
- **Baseline Version:** `v1.0.0-PROPOSED`
- **Approval Status:** DRAFT / PROPOSED (Awaiting Enterprise Review Board approval)

## 2. Established Identifiers & Artifact References
- **Primary Design Artifact:** `design/stage-1.md`
- **Principle Identifiers:**
  - `PRIN-GOV`: Accountability & Governance Integrity
  - `PRIN-SEC`: Safety, Security & Technical Robustness
  - `PRIN-TRN`: Transparency, Explainability & Provenance
  - `PRIN-FAI`: Fairness, Non-Discrimination & Societal Impact
  - `PRIN-DAT`: Privacy, Data Stewardship & Intellectual Property
  - `PRIN-HUM`: Human Agency, Contestability & Redress
- **Provisional Control Identifiers:**
  - `CTL-GOV-001`: System Inventory Registration & Ownership Assignment (Layer 1 Universal Process)
  - `CTL-SEC-002`: Agent Tool Execution Authorization & Least-Privilege Delegation (Layer 1 Conditional Technical)
  - `CTL-EVAL-003`: Pre-deployment Benchmark Evaluation & Hallucination Control (Layer 1 Parameterized Technical)
- **Provisional Overlay Identifiers:**
  - `OVL-REG-EU-001`: EU AI Act High-Risk System Specialization (Layer 2 Regulatory Specialization of `CTL-EVAL-003`)
- **Schema Identifiers & Specifications:**
  - `profile.schema.yaml`: Context Profile Schema
  - `overlay.schema.yaml`: Regulatory & Sectoral Overlay Schema
  - `effective-policy-snapshot.json`: Effective-Policy Snapshot Schema

## 3. Approved Decisions
- **None:** First design run (`PREVIOUS APPROVED DESIGN DECISIONS: NONE`). All decisions remain proposed until approved by an authorized review body.

## 4. Proposed Decisions Awaiting Review
- **DEC-001-ARCH:** Decouple Policy Decision Points (PDP) from Policy Enforcement Points (PEP) using localized OPA/CEL bundle evaluation.
- **DEC-002-ARCH:** Establish a 4-layer composition model (Baseline $\rightarrow$ Profiles/Overlays $\rightarrow$ Project Configuration $\rightarrow$ Authorized Exceptions).
- **DEC-003-ARCH:** Enforce typed, deterministic merge rules (intersection for permissions, directional monotonic envelopes for numerical thresholds, cumulative union for approvals) rather than generic "most restrictive wins".
- **DEC-004-ARCH:** Treat missing context or unknown manifest declarations as `UNRESOLVED_APPLICABILITY` halting automated promotion gates, rather than silent exclusion.

## 5. Provisional Assumptions
- Organization operates an internal shared service delivering governance capabilities to multiple heterogeneous delivery teams.
- Delivery environment includes mixed AI modalities: predictive ML, Generative AI / RAG, and tool-executing autonomous agents.
- CI/CD automation is available (e.g., GitHub Actions, GitLab CI) and runtime utilizes container orchestration (e.g., Kubernetes).

## 6. Unresolved Questions & Conflicts
- **Clarification Q1:** Priority regulatory frameworks (e.g., EU AI Act, NIST AI RMF, ISO/IEC 42001, sector-specific mandates like HIPAA/FINRA).
- **Clarification Q2:** Specific enterprise tech stack platforms (Git/CI/CD, model gateways, cloud infrastructure).
- **Clarification Q3:** Standard enterprise GRC and CMDB integration targets (ServiceNow, Jira, Archer).
- **Clarification Q4:** AI portfolio risk appetite and distribution of autonomous agent use cases.
- **Clarification Q5:** Preferred operating model structure (centralized AI Review Board vs. federated governance champions).

## 7. Sources Requiring Verification
- EU AI Act Regulation (EU) 2024/1689 primary text and annexes regarding high-risk logging, human oversight, and post-market evaluation.
- NIST AI RMF 1.0 and Generative AI Profile (NIST AI 600-1) provisions.
- ISO/IEC 42001:2023 clauses on AI management systems.

## 8. Exact Next Step
Execute **Stage 2** of the design consultation:
- **Deliverable 4:** Starter Control Catalogue (covering 15+ governance domains, expanding provisional controls `CTL-GOV-001`, `CTL-SEC-002`, `CTL-EVAL-003`).
- **Deliverable 11:** Standards and Obligation Mapping (cross-mapping to NIST AI RMF, ISO/IEC 42001, EU AI Act, OWASP GenAI/LLM).
- **Deliverable 12:** Operating Model & Enterprise Alignment (practical RACI, intake, exception lifecycle, and review board structure).

---
*Reply 'continue' for Stage 2.*
