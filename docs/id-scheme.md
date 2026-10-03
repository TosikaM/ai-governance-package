# Enterprise AI Governance Package: Identifier Scheme

**Status:** DRAFT  
**Baseline Version:** v0.1.0-draft  
**Organization Prefix:** `ORG`  
**Owner Placeholder:** [ROLE: AI Governance Platform Architect]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Principles of Permanent Identification

1. **Enterprise Namespacing:** Every machine-readable artifact is prefixed with the enterprise identifier `ORG` (or the customized organization prefix specified at initialization).
2. **Immutability:** Once an identifier is published in a tagged baseline release, its semantic definition is permanently bound. Identifiers **MUST NEVER** be renumbered or repurposed.
3. **Deprecation Without Erasure:** When a control or policy is superseded or retired, its identifier transitions to `DEPRECATED` or `RETIRED`. The ID is never reused.
4. **Machine-Parseable Regex:** All identifiers strictly conform to deterministic regular expressions to enable automated linting, schema validation, and Policy-as-Code compilation.

---

## 2. Core Taxonomy and Domain Codes

The enterprise baseline establishes 16 standardized three-letter domain codes covering the comprehensive governance lifecycle:

| Domain Code | Canonical Domain Name | Scope & Primary Objectives |
|---|---|---|
| `ACC` | Accountability & AI Inventory | Central registry, system ownership, RACI, algorithmic register |
| `USE` | Acceptable Use & Literacy | Permitted use-cases, shadow AI prevention, training & certification |
| `RSK` | Risk Classification & Impact | Risk tiers (1-4), AI impact assessment, fundamental rights impact |
| `DAT` | Data Quality, Privacy & Retention | Lineage, consent, residency, minimization, PII sanitization, retention |
| `SUP` | Supply Chain & Third-Party Models | Foundation model provenance, vendor risk, Model SBOM, upstream audits |
| `IPR` | Intellectual Property & Licensing | Training data rights, copyright indemnification, AI-generated code |
| `SEC` | AI Security & Attack Mitigation | Prompt injection, retrieval auth (RAG), jailbreaks, data exfiltration |
| `ROB` | Robustness, Evaluation & Testing | Benchmark evals, hallucination rate, adversarial testing, edge cases |
| `FAI` | Fairness, Bias & Accessibility | Demographic parity, accessibility (WCAG), vulnerable population impact |
| `TRN` | Transparency & Disclosure | Synthetic watermarking, user disclosure, explainability, system cards |
| `HUM` | Human Oversight & Redress | Human-in-the-loop (HITL), decision contestability, appeals process |
| `AGT` | Agent Autonomy & Guardrails | Tool-call authorization, least-privilege identity, kill switches, audit logs |
| `MON` | Monitoring, Drift & Incidents | Concept/data drift, latency, automated alerting, AI incident response |
| `CST` | Cost, Resource & Compute Limits | Token budgets, inference compute caps, GPU efficiency, finops |
| `REC` | Evidence Integrity & Audit Trails | Tamper-evident logging, cryptographic attestation, compliance ledger |
| `RET` | System Decommissioning & Retirement | Model unlearning, archive disposition, decommission checklist |

---

## 3. Identifier Structures & Regular Expressions

### 3.1 Principles (`ORG-PRIN-{DOMAIN}`)
Foundational ethical and governance commitments.
- **Syntax:** `^ORG-PRIN-[A-Z]{3}$`
- **Examples:**
  - `ORG-PRIN-ACC`: Accountability & Governance Integrity
  - `ORG-PRIN-SEC`: Safety, Security & Technical Robustness
  - `ORG-PRIN-AGT`: Agent Autonomy Boundaries & Verifiable Action Control

### 3.2 Policies (`ORG-POL-{DOMAIN}-{NUMBER}`)
Human-readable enterprise policy documents.
- **Syntax:** `^ORG-POL-[A-Z]{3}-[0-9]{3}$`
- **Examples:**
  - `ORG-POL-ACC-001`: Enterprise AI System Registration & Ownership Policy
  - `ORG-POL-SEC-001`: Artificial Intelligence Defensive Security & Vulnerability Policy
  - `ORG-POL-AGT-001`: Autonomous Tool Execution & Agent Authorization Policy

### 3.3 Controls (`ORG-CTL-{DOMAIN}-{NUMBER}`)
Atomic, machine-enforceable governance controls (Universal, Conditional, or Parameterized).
- **Syntax:** `^ORG-CTL-[A-Z]{3}-[0-9]{3}$`
- **Structure:**
  - `ORG`: Organization prefix
  - `CTL`: Control artifact type
  - `{DOMAIN}`: 3-letter domain code from Section 2
  - `{NUMBER}`: 3-digit zero-padded monotonic sequence (`001` to `999`)
- **Examples:**
  - `ORG-CTL-ACC-001`: Mandatory AI System Registration in Central Inventory
  - `ORG-CTL-SEC-002`: Agent Tool Call Schema Validation & Least-Privilege Execution
  - `ORG-CTL-ROB-003`: Pre-deployment Benchmark Evaluation & Hallucination Threshold

### 3.4 Overlays (`ORG-OVL-{CATEGORY}-{SUBJECT}-{NUMBER}`)
Jurisdictional, industry, risk tier, or archetype overlays that add or tighten requirements.
- **Syntax:** `^ORG-OVL-[A-Z]{3}-[A-Z0-9_-]+-[0-9]{3}$`
- **Categories:**
  - `GEO`: Geographic / Jurisdictional (e.g., `ORG-OVL-GEO-EU-001` for EU AI Act)
  - `SEC`: Sectoral / Industry (e.g., `ORG-OVL-SEC-FIN-001` for Financial Services)
  - `RSK`: Risk Tier Specific (e.g., `ORG-OVL-RSK-TIER3-001` for High Risk Systems)
  - `ARC`: Archetype / AI Type (e.g., `ORG-OVL-ARC-RAG-001` for RAG Architectures)
  - `CTR`: Contractual (e.g., `ORG-OVL-CTR-CLIENTA-001` for Specific Client Obligations)

### 3.5 Project Manifests (`ORG-MNF-{PROJECT_ID}-{VERSION}`)
Project declaration binding a repository to governance requirements.
- **Syntax:** `^ORG-MNF-[a-z0-9_-]+-v[0-9]+\.[0-9]+\.[0-9]+$`
- **Examples:**
  - `ORG-MNF-customer-copilot-v1.0.0`
  - `ORG-MNF-fraud-detection-v2.1.0`

### 3.6 Exceptions (`ORG-EXC-{YEAR}-{NUMBER}`)
Time-limited, approved deviations with compensatory controls.
- **Syntax:** `^ORG-EXC-[0-9]{4}-[0-9]{3,}$`
- **Structure:** Year of grant, followed by a monotonic sequence of at least 3 digits.
- **Examples:**
  - `ORG-EXC-2026-001`
  - `ORG-EXC-2026-042`

### 3.7 Evidence Records (`ORG-EVD-{DOMAIN}-{NUMBER}-{PROJECT_ID}-{DATE}-{SEQ}`)
Immutable attestations, automated evaluation reports, and sign-offs.
- **Syntax:** `^ORG-EVD-[A-Z]{3}-[0-9]{3}-[a-z0-9_-]+-[0-9]{8}-[0-9]{3}$`
- **Examples:**
  - `ORG-EVD-ROB-003-fraud-engine-20261001-001`
  - `ORG-EVD-SEC-002-support-agent-20261001-002`

---

## 4. Mapping from Phase A Provisional Identifiers

During Phase A (Design Consultation), initial identifiers were established in `runs/design-continuation.md`. The table below establishes their permanent canonical mapping under the `ORG-` scheme:

| Phase A Provisional ID | Canonical M0 Permanent ID | Classification | Artifact Type |
|---|---|---|---|
| `PRIN-GOV` | `ORG-PRIN-ACC` | Accountability & Governance Integrity | Ethical Principle |
| `PRIN-SEC` | `ORG-PRIN-SEC` | Safety, Security & Technical Robustness | Ethical Principle |
| `PRIN-TRN` | `ORG-PRIN-TRN` | Transparency, Explainability & Provenance | Ethical Principle |
| `PRIN-FAI` | `ORG-PRIN-FAI` | Fairness, Non-Discrimination & Societal Impact | Ethical Principle |
| `PRIN-DAT` | `ORG-PRIN-DAT` | Privacy, Data Stewardship & IP | Ethical Principle |
| `PRIN-HUM` | `ORG-PRIN-HUM` | Human Agency, Contestability & Redress | Ethical Principle |
| `CTL-GOV-001` | `ORG-CTL-ACC-001` | System Inventory Registration & Ownership Assignment | Universal Control |
| `CTL-SEC-002` | `ORG-CTL-SEC-002` | Agent Tool Execution Authorization & Least-Privilege Delegation | Conditional Control |
| `CTL-EVAL-003` | `ORG-CTL-ROB-003` | Pre-deployment Benchmark Evaluation & Hallucination Threshold | Parameterized Control |
| `OVL-REG-EU-001` | `ORG-OVL-GEO-EU-001` | EU AI Act High-Risk System Specialization Overlay | Jurisdictional Overlay |

---

## 5. Permanence & Deprecation Lifecycle Rules

```
                      +-------------------+
                      |      DRAFT        | (Authored in PR / feature branch)
                      +-------------------+
                                |
                                v
                      +-------------------+
                      |     PROPOSED      | (Submitted for Review Board evaluation)
                      +-------------------+
                                |
                                v
                      +-------------------+
                      |     APPROVED      | (Formal sign-off by ARB / Risk Committee)
                      +-------------------+
                                |
                                v
                      +-------------------+
                      |      ACTIVE       | (Included in tagged baseline release)
                      +-------------------+
                                |
                                v
                      +-------------------+
                      |    DEPRECATED     | (Successor specified; grace period active)
                      +-------------------+
                                |
                                v
                      +-------------------+
                      |     RETIRED       | (Tombstoned; never re-issued or deleted)
                      +-------------------+
```

- **Tombstoning:** When a control reaches `RETIRED`, its definition file remains in the repository with status `RETIRED`, recording the retirement date, rationale, and successor control ID.
- **Prohibition on ID Recycling:** A retired identifier (e.g., `ORG-CTL-SEC-002`) will never be reassigned to a different requirement, guaranteeing historical auditability across enterprise logs and evidence repositories.
