# Enterprise Policy on AI Model, Supplier, and Software Supply Chain Integrity

**Policy Identifier:** `ORG-POL-SUP-001`  
**Associated Principle:** `ORG-PRIN-SUP` (Model, Supplier & Supply Chain Integrity)  
**Status:** DRAFT  
**Effective Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: AI Supply Chain & Third-Party Risk Lead]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Purpose & Scope

This policy governs the procurement, ingestion, verification, and maintenance of third-party foundation models, open-source model weights, upstream AI software dependencies, and cloud-hosted AI API services across the enterprise.

This policy applies to all external software libraries, open-weights checkpoints, commercial API endpoints, container base images, and datasets acquired from external vendors or open-source repositories.

---

## 2. Normative Requirements

### 2.1 Third-Party Model & Vendor Due Diligence
1. **Commercial Model Evaluation:** Commercial foundation model providers must undergo third-party vendor risk assessment evaluating security certifications (SOC 2 Type II, ISO 27001), enterprise data handling terms (verifying enterprise inputs are never retained or used for foundation model training), and service level agreements (SLAs).
2. **Upstream Vulnerability & Outage Resiliency:** Critical systems relying on external model APIs must maintain documented fallback mechanisms or multi-provider routing to mitigate upstream outages or sudden model deprecation.

### 2.2 Model & Software Bill of Materials (SBOM / MBOM)
1. **Mandatory CycloneDX/SPDX SBOM:** Every software build deploying AI capabilities must automatically generate a Software Bill of Materials (SBOM) capturing all runtime dependencies, model runtime binaries, tokenizers, and framework versions.
2. **Model Bill of Materials (MBOM):** Teams deploying open-source model weights must maintain an MBOM capturing model family, exact architecture revision, training data references, license classification, and upstream source URL.

### 2.3 Cryptographic Integrity & Safe Serialization Formats
1. **Prohibition of Insecure Deserialization (`pickle`):** Machine learning models ingested into enterprise repositories or clusters **MUST NOT** utilize vulnerable serialization formats (such as arbitrary Python `pickle` or untrusted `.bin` files) capable of arbitrary code execution.
2. **Mandatory Safe Formats (`safetensors`):** Model weights must be distributed in memory-safe, non-executable serialization formats (e.g., Hugging Face `safetensors`, GGUF, or ONNX).
3. **Cryptographic SHA-256 Checksums:** All downloaded weights, tokenizers, and configuration files must have their SHA-256 hashes cryptographically verified against the vendor or repository publisher’s signed release manifest prior to storage in internal artifact registries.

---

## 3. Separation of Automated Checks and Human Judgment

| Requirement | Verification Mechanism | Check Type | Enforcement Point | Mode |
|---|---|---|---|---|
| Insecure Model Format Scanning (Pickle/Eval Detection) | Model file inspection tool (e.g., Fickling / static analyzer) | Automated | CI / Artifact Registry Ingestion | Blocking |
| SHA-256 Checksum Verification | Hash verification against signed manifest | Automated | Model download / container build | Blocking |
| Dependency Vulnerability (CVE) Scanning | Software composition analysis (SCA / CycloneDX scanner) | Automated | CI build pipeline | Blocking |
| Third-Party Vendor Data Processing Terms Review | Legal and procurement contract evaluation | Human Judgment | Vendor Intake Gate | Review |
| Assessment of Upstream Model Ethical Provenance | Evaluation of model safety reports and alignment audits | Human Judgment | AI Review Board Gate | Review |

---

## 4. Roles & Responsibilities

- **Procurement & Legal Counsel:** Ensures third-party AI vendor contracts contain zero-training and confidential enterprise indemnification clauses.
- **AI Supply Chain Security Engineer:** Configures model artifact scanning, enforces `safetensors` compliance, and oversees internal model registry admission.
- **System Technical Lead:** Declares all third-party components in `ai-project-manifest.yaml` and ensures SBOMs are continuously generated.
- **Enterprise CISO:** Monitors upstream AI supply chain advisories and directs emergency revocation of compromised foundation models.

---

## 5. Non-Conformance & Exceptions

Any unverified model weight file or unapproved third-party API endpoint detected in production builds will trigger automated pipeline termination. Exceptions must be recorded under `ORG-EXC` and require CISO approval. Internal exceptions cannot waive export control or vendor contractual liabilities.

---

## 6. Authoritative Reference Mappings

- **NIST AI RMF 1.0:** GOVERN 3.2, MANAGE 1.3 (AI supply chain risk management, third-party risk controls).
- **ISO/IEC 42001:2023:** Annex A.10 (Third-party and supplier relationships for AI systems).
- **OWASP Top 10 for LLM Applications (2025):** LLM03:2025 (Supply Chain Risks).
- **Executive Order 14110 / NIST SP 800-218:** Secure Software Development Framework (SSDF) applicable to AI.
