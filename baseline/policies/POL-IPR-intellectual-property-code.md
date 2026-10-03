# Enterprise Policy on Intellectual Property, Licensing, and AI-Generated Code

**Policy Identifier:** `ORG-POL-IPR-001`  
**Associated Principle:** `ORG-PRIN-IPR` (Intellectual Property & Licensing)  
**Status:** DRAFT  
**Effective Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: Intellectual Property Legal Counsel & Lead Software Architect]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Purpose & Scope

This policy governs intellectual property (IP) rights, open-source software licensing, copyright compliance, and the development lifecycle of software source code generated in whole or in part by Artificial Intelligence systems (AI-assisted coding tools, coding agents, and generative LLMs).

This policy applies to all proprietary software repositories, training datasets, vector database knowledge bases, and software engineering teams utilizing AI coding assistants.

---

## 2. Normative Requirements

### 2.1 Training Data & Knowledge Base Licensing
1. **Copyright Clearance:** Training datasets and retrieval corpus documents must have documented licenses permitting text-and-data mining (TDM), machine learning training, or vector indexing.
2. **Copyleft Ingestion Restrictions:** Code or documentation distributed under reciprocal copyleft licenses (e.g., GNU GPL, AGPL) **MUST NOT** be ingested into model fine-tuning corpora or internal commercial vector indices without explicit IP legal clearance.

### 2.2 Governance of AI-Generated Software Code
1. **Mandatory Human Accountability:** AI-generated software code is an engineering accelerator, not an author. All AI-generated code, infrastructure-as-code, and configuration files must be authored, understood, and peer-reviewed by an accountable enterprise human engineer prior to merge.
2. **Automated Snippet / Copyleft Matching:** Development workflows utilizing AI code generators must implement automated code similarity scanning (e.g., tool matching code against public GitHub repositories) to ensure models do not regurgitate licensed open-source code without attribution or in violation of reciprocal licenses.
3. **Mandatory Secret & Security Scanning:** Because generative coding tools frequently propose deprecated libraries or insecure idioms, 100% of AI-assisted pull requests must undergo automated Static Application Security Testing (SAST) and hardcoded secret detection prior to merge.
4. **No Direct Production Commits by Autonomous Agents:** Autonomous coding agents are strictly prohibited from pushing code directly to production or bypass-protected branches (`main`, `release/*`) without human peer review and automated CI verification.

### 2.3 Intellectual Property Ownership & Confidentiality
1. **Enterprise IP Ownership:** All prompts, model fine-tunings, embeddings, and software outputs produced on enterprise systems constitute proprietary work-for-hire owned exclusively by the enterprise.
2. **Provider Training Opt-Out:** Enterprise coding tools must be configured to prohibit third-party model providers from retaining, inspecting, or training on enterprise source code or telemetry.

---

## 3. Separation of Automated Checks and Human Judgment

| Requirement | Verification Mechanism | Check Type | Enforcement Point | Mode |
|---|---|---|---|---|
| Open Source License Scanning (SCA) | Dependency license checker (e.g., FOSSA / syft) | Automated | PR CI/CD Pipeline | Blocking |
| Code Match / Regurgitation Detection | Source code similarity & license scanner | Automated | PR CI/CD Pipeline | Blocking |
| SAST & Hardcoded Secret Scanning | GitLeaks / Semgrep / Static security analyzers | Automated | Pre-commit hook & PR gate | Blocking |
| Human Peer Review of AI-Generated PRs | Peer review approval by qualified software engineer | Human Judgment | Pull Request Review Gate | Blocking |
| Evaluation of Complex IP / Fair Use Questions | Formal legal review of dataset ingestion rights | Human Judgment | Legal Counsel Intake Gate | Review |

---

## 4. Roles & Responsibilities

- **Software Engineers:** Personally accountable for the correctness, safety, and license compliance of any code generated with AI assistance.
- **Peer Reviewers:** Must scrutinize AI-suggested code with the same rigor as human-authored code, validating edge-case handling and security posture.
- **Intellectual Property Counsel:** Provides binding determinations on dataset copyright, foundation model licensing, and commercial IP indemnification terms.
- **DevSecOps Engineering:** Maintains automated SAST, secret detection, and license compliance checks across all source code repositories.

---

## 5. Non-Conformance & Exceptions

Merging unvetted AI-generated code that introduces reciprocal copyleft contamination or critical vulnerabilities will trigger immediate code revert and branch protection audit. Exceptions must be recorded under `ORG-EXC` and require IP Legal Counsel sign-off. Internal exceptions cannot waive statutory copyright obligations.

---

## 6. Authoritative Reference Mappings

- **ISO/IEC 42001:2023:** Annex A.7.4 (Intellectual property rights in AI systems).
- **NIST AI RMF 1.0:** GOVERN 1.2, MANAGE 1.1 (Legal and regulatory compliance, IP risk management).
- **OWASP Top 10 for LLM Applications (2025):** LLM02:2025 (Sensitive Information Disclosure), LLM05:2025 (Improper Output Handling).
- **US Copyright Office Guidance (March 2023):** Copyright Registration Guidance for Works Containing AI-Generated Material (human authorship requirements).
