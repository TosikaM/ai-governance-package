# Enterprise Policy on AI Acceptable Use, Shadow AI Prevention, and AI Literacy

**Policy Identifier:** `ORG-POL-USE-001`  
**Associated Principle:** `ORG-PRIN-USE` (Acceptable Use, Shadow AI & Literacy)  
**Status:** DRAFT  
**Effective Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: Chief Information Security Officer & Chief Learning Officer]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Purpose & Scope

This policy defines the acceptable, restricted, and expressly prohibited uses of Artificial Intelligence technologies, foundation model APIs, and autonomous agents across the enterprise. It mandates active measures to eliminate unapproved "Shadow AI" and establishes mandatory baseline AI literacy standards for all workforce members.

This policy binds all personnel (employees, contractors, consultants) and all automated systems executing workflows on enterprise infrastructure.

---

## 2. Normative Requirements

### 2.1 Expressly Prohibited AI Use Cases
Enterprise personnel and automated systems are strictly prohibited from developing, deploying, or utilizing AI systems for:
1. **Subliminal Manipulation & Exploitation:** Systems designed to distort human behavior to cause physical, psychological, or financial harm by exploiting vulnerabilities (age, disability, socio-economic distress).
2. **Social Scoring:** Evaluation or classification of individuals over time based on social behavior or personality traits leading to discriminatory or unjustified treatment.
3. **Unapproved Biometric Surveillance:** Real-time remote biometric identification in publicly accessible spaces without explicit legal authorization and ARB approval.
4. **Autonomous Lethal or Kinetic Actions:** Systems capable of directing kinetic or life-critical physical action without fail-safe human intervention.
5. **Deceptive Impersonation:** Creating synthetic media or conversational bots designed to deceive individuals into believing they are interacting with a specific human being without prior consent.

### 2.2 Prohibition of Shadow AI
1. **Unvetted Consumer Services:** Personnel **MUST NOT** input enterprise data, source code, customer records, or internal documentation into public, unvetted consumer AI portals (e.g., public web chat tools where terms permit provider training on user inputs).
2. **Approved Gateway Mandate:** All programmatic and interactive AI interactions must route through the enterprise-managed LLM Gateway or approved enterprise-tenanted SaaS tools configured with zero-data-retention and zero-training agreements.
3. **Endpoint & Network Inspection:** Enterprise workstations and networks shall maintain active egress inspection blocking unauthorized generative AI endpoints.

### 2.3 Mandatory AI Literacy & Training
1. **General Workforce Training:** All employees interacting with AI tools must complete annual baseline AI Literacy Training covering prompt risks, hallucination awareness, output verification, and data handling.
2. **Developer & Practitioner Certification:** Engineers building or deploying AI systems must complete specialized training covering security (prompt injection, jailbreaking), evaluation harnesses, and bias mitigation before gaining deployment repository access.

---

## 3. Separation of Automated Checks and Human Judgment

| Requirement | Verification Mechanism | Check Type | Enforcement Point | Mode |
|---|---|---|---|---|
| Egress Domain Filtering (Shadow AI) | Network proxy / Secure Web Gateway blocklist | Automated | Corporate Proxy / DNS Firewall | Blocking |
| Secret & Sensitive Data Leakage in Prompts | DLP scanning sidecar on outgoing gateway requests | Automated | Enterprise LLM Gateway | Blocking |
| Code Repository AI Tool Audit | Dependency scanning for unapproved AI API SDKs | Automated | PR CI/CD pipeline | Blocking |
| Assessment of Novel / Prohibited Use Cases | Ethical and regulatory review of system intent | Human Judgment | AI Review Board Intake Gate | Review |
| Annual Literacy Curriculum Quality & Relevance | Curriculum review against emerging AI threats | Human Judgment | Annual Learning Audit | Review |

---

## 4. Roles & Responsibilities

- **All Personnel:** Bound to utilize only authorized AI tools and verify all AI-assisted outputs for factual accuracy before reliance.
- **Enterprise CISO / Security Operations:** Enforces DNS/web filtering, DLP rules, and investigates Shadow AI detections.
- **Chief Learning Officer / HR:** Develops and tracks completion of mandatory AI literacy modules.
- **Technical Leads:** Ensure no unauthorized external AI SDKs or endpoints are introduced into production codebases.

---

## 5. Non-Conformance & Exceptions

Violations of acceptable use or deliberate exfiltration of proprietary data to unapproved tools will result in immediate revocation of AI access privileges and disciplinary review. Internal exceptions never waive statutory prohibitions (e.g., EU AI Act prohibited practices under Article 5).

---

## 6. Authoritative Reference Mappings

- **ISO/IEC 42001:2023:** Clause 7.2 (Competence and awareness), Annex A.5 (AI system impact on individuals and society).
- **NIST AI RMF 1.0:** GOVERN 2.2, GOVERN 2.3 (Workforce competencies, ethical principles in acceptable use).
- **EU AI Act Regulation (EU) 2024/1689:** Article 4 (AI literacy obligation for providers and deployers), Article 5 (Prohibited artificial intelligence practices).
- **OWASP Top 10 for LLM Applications (2025):** LLM02:2025 (Sensitive Information Disclosure).
