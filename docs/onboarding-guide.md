# Enterprise AI Governance: Comprehensive Project Onboarding Guide

**Document Identifier:** `ORG-DOC-ONBOARD-001`  
**Status:** DRAFT  
**Baseline Version:** `v0.1.0-draft`  
**Owner Placeholder:** [ROLE: AI Governance Enablement Lead]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

> [!WARNING]
> **COMPLIANCE DISCLAIMER**  
> Following this onboarding guide enables engineering teams to adopt the enterprise AI governance controls and integrate required pipeline and runtime barriers. However, completing onboarding does not constitute formal certification, legal sign-off, or regulatory indemnification. High-risk systems require explicit review and sign-off by the AI Safety & Governance Review Board.

---

## 1. Introduction & Target Audiences

This guide provides engineering teams, data scientists, product managers, and compliance assessors with an end-to-end operational manual for onboarding artificial intelligence systems into the enterprise governance ecosystem.

### Persona Mapping & Core Responsibilities

```
+---------------------------------------------------------------------------------------------------+
|                                  ONBOARDING ROLES & RESPONSIBILITIES                              |
+------------------------------------+--------------------------------------------------------------+
| Role / Persona                     | Primary Governance Tasks & Artifacts                         |
+------------------------------------+--------------------------------------------------------------+
| 1. Product Manager & Project Lead  | - Register system in Enterprise AI Inventory (ORG-CTL-ACC-001)|
|                                    | - Complete Algorithmic Impact Assessment (ORG-CTL-RSK-002)   |
|                                    | - Author project manifest (ai-project-manifest.yaml)         |
|                                    | - Submit and track policy exception requests                 |
+------------------------------------+--------------------------------------------------------------+
| 2. Data Scientist & ML Engineer    | - Author Data Cards (ORG-CTL-DAT-001, ORG-CTL-IPR-001)       |
|                                    | - Author Model Cards (ORG-CTL-TRN-004)                       |
|                                    | - Enforce safe serialization formats (ORG-CTL-SUP-003)       |
|                                    | - Verify evaluation benchmarks (accuracy, toxicity, bias)    |
+------------------------------------+--------------------------------------------------------------+
| 3. Software & Platform Engineer    | - Install pre-commit hooks & configure CI/CD PR gates        |
|                                    | - Deploy outside-the-model Agent PEP Proxies (ORG-CTL-AGT-002)|
|                                    | - Configure Admission Controllers and Gateway Sidecars       |
|                                    | - Emit automated, verifiable evidence records                |
+------------------------------------+--------------------------------------------------------------+
| 4. Security & Compliance Assessor  | - Conduct threat modeling & adversarial red-teaming          |
|                                    | - Review PII sanitization and data residency compliance      |
|                                    | - Audit residual risk and validate compensating controls     |
+------------------------------------+--------------------------------------------------------------+
```

---

## 2. End-to-End Onboarding Workflow

The onboarding lifecycle spans five sequential phases:

```
  Phase 1: Intake & Classification
     |
     v
  Phase 2: Manifest Declaration & Overlay Selection
     |
     v
  Phase 3: Policy Snapshot Resolution & Freezing
     |
     v
  Phase 4: Integrating Pipeline & Runtime Gates
     |
     v
  Phase 5: Producing Documentation Cards & Verifiable Evidence
```

---

### Phase 1: Intake, Registration & Risk Classification

Before writing code or provisioning cloud infrastructure, the Project Lead must register the initiative:

1. **Reserve Permanent System Identifier (`SYS-ID`):**
   - Access the Enterprise AI Inventory portal and register a new record.
   - Obtain a unique identifier formatted as `SYS-[BUSINESS_UNIT]-[SYSTEM_SLUG]` (e.g., `SYS-FIN-FRAUD-DETECTOR-01`, adhering to [`ORG-CTL-ACC-001`](file:///c:/ai-governance-package/baseline/controls/accountability-inventory/CTL-ACC-001.yaml)).
2. **Execute Initial Algorithmic Impact Assessment (AIIA):**
   - Copy [`templates/ai-impact-assessment.template.md`](file:///c:/ai-governance-package/templates/ai-impact-assessment.template.md) into your project documentation repository.
   - Detail the business objective, deployment context, human rights risk analysis, and out-of-scope system boundaries.
3. **Determine Risk Tier Classification (`ORG-CTL-RSK-001`):**
   - Use the classification matrix in [`baseline/policies/POL-RSK-risk-classification-impact.md`](file:///c:/ai-governance-package/baseline/policies/POL-RSK-risk-classification-impact.md) to assign a risk tier:
     - **Tier 1 (Minimal Risk):** Internal non-critical productivity tools, developer code assistance, offline document summarization.
     - **Tier 2 (Moderate Risk):** Customer-facing chatbots with human fallback, internal operational workflow triage, non-critical classification.
     - **Tier 3 (High Risk):** Credit decisions, employment screening, biometrics, safety-critical medical/industrial operations, autonomous transactions.
     - **Tier 4 (Unacceptable Risk):** Social scoring, real-time untargeted biometric surveillance, subliminal behavioral manipulation. **PROHIBITED FROM DEPLOYMENT** ([`ORG-CTL-USE-001`](file:///c:/ai-governance-package/baseline/controls/acceptable-use/CTL-USE-001.yaml)).

---

### Phase 2: Manifest Declaration & Overlay Selection

The system's operational parameters, architectural traits, and regulatory scope are codified in a declarative YAML manifest.

1. **Instantiate Manifest:**
   - Copy [`project-kit/ai-project-manifest.template.yaml`](file:///c:/ai-governance-package/project-kit/ai-project-manifest.template.yaml) into your project root as `ai-project-manifest.yaml`.
2. **Declare System Characteristics:**
   - Define exact metadata matching your inventory registration:
     ```yaml
     schema_version: "2020-12"
     project_id: "SYS-FIN-FRAUD-DETECTOR-01"
     project_name: "Real-Time Transaction Fraud Detection Model"
     baseline_version: "v0.1.0-draft"
     risk_tier: "tier_3_high"
     archetype: "predictive_tabular"  # or generative_llm, rag_knowledge, autonomous_agent
     ```
3. **Select Contextual Overlays:**
   - Review available overlays in [`overlays/`](file:///c:/ai-governance-package/overlays) and declare all matching regulatory jurisdictions, industry domains, and architectures:
     ```yaml
     overlays:
       geography:
         - overlay_id: "ORG-OVL-GEO-EU-001"
           version: "v0.1.0-draft"
       sector:
         - overlay_id: "ORG-OVL-SEC-FIN-001"
           version: "v0.1.0-draft"
       risk_tier:
         - overlay_id: "ORG-OVL-RSK-TIER3-001"
           version: "v0.1.0-draft"
     ```
4. **Declare Technical Capabilities:**
   - Set boolean operational flags accurately:
     ```yaml
     capabilities:
       executes_tools_or_agents: false
       processes_personal_data: true
       generates_user_facing_content: false
       makes_automated_decisions: true
     ```

---

### Phase 3: Policy Snapshot Resolution & Freezing

Projects never copy baseline controls directly. Instead, they run the deterministic resolver to compute an immutable policy snapshot.

1. **Execute Resolver Utility:**
   ```bash
   python /path/to/ai-governance-package/project-kit/resolver/resolve.py \
     --manifest ./ai-project-manifest.yaml \
     --baseline-dir /path/to/ai-governance-package/baseline/controls \
     --overlays-dir /path/to/ai-governance-package/overlays \
     --output ./effective-policy-snapshot.json
   ```
2. **Review Resolved Policy Output:**
   - Inspect `effective-policy-snapshot.json` to verify:
     - Applicable universal controls (e.g., `ORG-CTL-ACC-001`, `ORG-CTL-SEC-001`).
     - Triggered conditional controls (e.g., `ORG-CTL-DAT-002` triggered by `processes_personal_data: true`).
     - Monotonically tightened parameter values (e.g., minimum accuracy raised from 80% to 92% by Tier 3 overlay).
     - Computed canonical SHA-256 integrity hash:
       ```json
       "snapshot_integrity_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
       ```
3. **Handling Unresolved Conflicts (`UNRESOLVED_CONFLICT_HALT`):**
   - If two overlays introduce mutually contradictory obligations without a monotonic ordering, the resolver halts execution with status `UNRESOLVED_CONFLICT_HALT`.
   - The team must contact the AI Governance Platform Lead to arbitrate the conflicting overlay requirements before proceeding.
4. **Commit Snapshot to Source Control:**
   - Commit both `ai-project-manifest.yaml` and `effective-policy-snapshot.json` into your Git repository. All downstream CI/CD gates will enforce compliance against this committed snapshot.

---

### Phase 4: Integrating Pipeline & Runtime Plug-in Gates

Enforcement must occur at every stage of the software and model lifecycle.

```
Developer Workstation       Pull Request Gate        Build & Test CI/CD        Container Runtime
[pre-commit hook]    -->   [pr-governance-gate]  -->  [build_pipeline_gate] --> [admission_webhook]
(Advisory Lint/Scan)       (Authoritative Gate)       (Eval Thresholds/Hash)    (Signed Images Only)
```

#### 4.1 Local Developer Workstation (Advisory)
- Copy [`plugins/pre-commit/pre-commit-config.template.yaml`](file:///c:/ai-governance-package/plugins/pre-commit/pre-commit-config.template.yaml) to `.pre-commit-config.yaml`.
- Run `pre-commit install`.
- Local hooks will automatically check manifest YAML syntax, scan for exposed API keys (`plugins/pre-commit/scan_secrets.py`), and warn against insecure pickle weights.

#### 4.2 Pull Request / Merge Request Gate (Authoritative)
- Copy [`plugins/pull-request/pr-governance-gate.yaml`](file:///c:/ai-governance-package/plugins/pull-request/pr-governance-gate.yaml) into `.github/workflows/`.
- The PR gate will:
  - Verify manifest schema validity.
  - Re-run `resolve.py` and confirm that `effective-policy-snapshot.json` matches committed code.
  - Run [`plugins/pull-request/ai_code_review_gate.py`](file:///c:/ai-governance-package/plugins/pull-request/ai_code_review_gate.py) to ensure human peer review on AI-generated software (`ORG-CTL-IPR-002`) and scan for viral copyleft licenses (`ORG-CTL-IPR-003`).

#### 4.3 Build & Test CI/CD Barrier (Authoritative)
- Add [`plugins/cicd-gates/build_pipeline_gate.py`](file:///c:/ai-governance-package/plugins/cicd-gates/build_pipeline_gate.py) to your build pipeline:
  ```bash
  python plugins/cicd-gates/build_pipeline_gate.py \
    --snapshot ./effective-policy-snapshot.json \
    --metrics ./target/eval-metrics.json \
    --output-evidence ./evidence/eval-evidence.json
  ```
- The gate validates benchmark metrics against snapshot parameters:
  - Accuracy $\ge$ threshold (e.g., 90%).
  - Hallucination rate $\le$ ceiling (e.g., 5.0%).
  - Bias parity ratio $\ge 0.80$ (four-fifths rule).
- Fails build immediately if thresholds are violated. Emits signed JSON evidence record upon success.

#### 4.4 Model Registry Promotion Gate (Authoritative)
- When publishing model weights to the enterprise model registry (MLflow, Hugging Face Hub, S3, OCI):
  - Run [`plugins/model-registry/promotion_gate.py`](file:///c:/ai-governance-package/plugins/model-registry/promotion_gate.py).
  - Verifies model serialization is safe (`safetensors` or `ONNX`, blocking dangerous pickle files per `ORG-CTL-SUP-003`).
  - Computes SHA-256 weight digest and asserts presence of valid `model-card.yaml`.

#### 4.5 Runtime Admission Controller (Authoritative)
- For Kubernetes / container clusters:
  - Deploy [`plugins/admission-controller/admission_webhook.py`](file:///c:/ai-governance-package/plugins/admission-controller/admission_webhook.py).
  - Intercepts Pod deployment requests. Verifies container image Cosign digital signature (`ORG-CTL-REC-003`), validates snapshot hash annotations, and rejects any pod attempting to launch Tier 4 Unacceptable Risk systems.

#### 4.6 Outside-the-Model Agent PEP Proxy (Mandatory for Agentic Systems)
- If your system invokes tools, APIs, databases, or MCP servers:
  - **The model must never invoke external tools directly.**
  - Route all agent tool execution requests through [`plugins/agent-interceptor/agent_pep_proxy.py`](file:///c:/ai-governance-package/plugins/agent-interceptor/agent_pep_proxy.py).
  - The PEP proxy enforces:
    - SPIFFE machine identity validation (`ORG-CTL-AGT-002`).
    - Tool parameter JSON Schema validation (`ORG-CTL-AGT-003`).
    - Outside-the-model dual-key human approval tokens for destructive operations (`ORG-CTL-HUM-002`).
    - Maximum recursion depth limit ($\le 5$ turns).
    - Sub-second out-of-band kill switch execution (`ORG-CTL-AGT-004`).

---

### Phase 5: Producing Documentation Cards & Verifiable Evidence

Before final production sign-off, engineering teams must complete and commit standard documentation templates:

1. **Model Card (`ORG-CTL-TRN-004`):**
   - Instantiate [`templates/model-card.template.yaml`](file:///c:/ai-governance-package/templates/model-card.template.yaml).
   - Document architecture, training parameters, evaluation benchmark scores, and declared operational limitations.
2. **Data Card (`ORG-CTL-DAT-001`, `ORG-CTL-IPR-001`):**
   - Instantiate [`templates/data-card.template.yaml`](file:///c:/ai-governance-package/templates/data-card.template.yaml).
   - Document collection provenance, PII sanitization pipelines, copyright clearances, and retention schedules.
3. **AI Risk Register (`ORG-CTL-RSK-003`):**
   - Instantiate [`templates/risk-register-entry.template.yaml`](file:///c:/ai-governance-package/templates/risk-register-entry.template.yaml).
   - Document specific adversarial threat scenarios (prompt injection, model theft, data poisoning), inherent likelihood/impact scores, mapped baseline controls, and real-time monitoring thresholds.
4. **Verifiable Evidence Records (`ORG-CTL-REC-001`):**
   - Ensure all automated pipeline gates emit structured JSON evidence records matching [`schemas/evidence-record.schema.json`](file:///c:/ai-governance-package/schemas/evidence-record.schema.json).
   - Store evidence records in the designated enterprise WORM (Write Once, Read Many) evidence locker for audit retrieval.

---

## 3. Managing Variances and Policy Exceptions

If a project cannot meet a specific baseline or overlay requirement due to technical constraints or unique operational context, the project lead must submit a formal Exception Request.

### Strict Governance Rules for Exceptions

1. **Non-Waivable Legal Obligations:** Internal policy exceptions **CANNOT** waive statutory legal requirements (e.g., GDPR Article 22 human review, EU AI Act prohibited practices). Any exception request attempting to waive a statutory obligation is rejected immediately.
2. **Compensating Controls Required:** An exception is never a free pass. Every exception request must propose concrete, measurable compensating controls that mitigate the underlying risk to an acceptable level.
3. **Strict Time Limits:** Exceptions are granted for a maximum duration of **90 calendar days**. Permanent exceptions are prohibited.
4. **Formal Review Quorum:** Exceptions require formal sign-off by the AI Governance Platform Lead, CISO, and Legal Counsel.

### Exception Submission Workflow

```
[Project Lead]                                 [ARB Secretariat]                [Review Quorum]
       |                                                |                               |
       |-- 1. Complete exception-request.template.yaml ->|                               |
       |                                                |-- 2. Triage & Legal Review -->|
       |                                                |                               |-- 3. Deliberate
       |                                                |<-- 4. Record Decision --------|
       |<-- 5. Issue Exception Token or Rejection ------|
```

1. **Draft Exception Request:**
   - Copy [`project-kit/exception-request.template.yaml`](file:///c:/ai-governance-package/project-kit/exception-request.template.yaml) to `docs/exceptions/EXC-[SYS-ID]-[CTL-ID].yaml`.
   - Specify the exact control ID (e.g., `ORG-CTL-SUP-003`), business justification, proposed compensating controls, expiration date (within 90 days), and project lead attestation.
2. **Submit to AI Governance Review Board:**
   - File an Exception Ticket in the enterprise governance portal referencing the drafted YAML file.
3. **Board Deliberation & Outcome:**
   - **Approved:** A cryptographic exception token (`EXC-TOKEN-[HASH]`) is issued and recorded in the central exception registry. Update your `ai-project-manifest.yaml` under `exceptions:` to bypass automated CI/CD blocking for the duration of the token.
   - **Rejected:** The project must remediate the non-compliance before production deployment.
4. **Expiration & Re-certification:**
   - 14 days prior to expiration, automated alerts will notify the project lead. The team must either demonstrate compliance or submit a renewal request with updated remediation milestones.

---

## 4. Incident Response & System Retirement

### AI Safety & Security Incident Reporting (`ORG-CTL-MON-004`)

If an onboarded AI system experiences an adversarial attack, severe hallucination causing business harm, unauthorized data exfiltration, or rogue agent behavior:
1. **Initiate Incident Triage:**
   - Notify the Enterprise Security Operations Center (SOC) and AI Incident Response Team immediately.
   - For autonomous agents, trigger the instantaneous kill switch ([`plugins/agent-interceptor/agent_pep_proxy.py`](file:///c:/ai-governance-package/plugins/agent-interceptor/agent_pep_proxy.py)).
2. **Complete Incident Post-Mortem:**
   - Instantiate [`templates/incident-report.template.md`](file:///c:/ai-governance-package/templates/incident-report.template.md).
   - Document incident severity (P1 Critical to P4 Low), chronological timeline, blast radius, 5-Whys root cause analysis, and Corrective and Preventive Actions (CAPA).
   - Submit the post-mortem to the AI Safety Review Board within 5 business days of incident closure.

### System Decommissioning & Retirement (`ORG-CTL-RET-001` through `004`)

When phasing out a production AI model or agent service:
1. **Instantiate Retirement Checklist:**
   - Copy [`templates/retirement-checklist.template.md`](file:///c:/ai-governance-package/templates/retirement-checklist.template.md).
2. **Execute Mandatory Retirement Steps:**
   - Publish 90-day advance deprecation notice to API consumers (`ORG-CTL-RET-004`).
   - Configure HTTP 410 Gone tombstones on decommissioned endpoints.
   - Revoke SPIFFE machine credentials and IAM permissions (`ORG-CTL-RET-003`).
   - Drop vector database collections and flush semantic caches (`ORG-CTL-RET-003`).
   - Transfer model weights and audit records to WORM-compliant cold storage for the statutory retention period (`ORG-CTL-RET-002`).
   - Update central inventory status to `RETIRED` (`ORG-CTL-RET-001`).

---

## 5. Troubleshooting & Frequently Asked Questions (FAQ)

### Q1: My CI build failed with "Snapshot Integrity Hash Mismatch". What happened?
**Cause:** Someone manually edited `effective-policy-snapshot.json` or modified `ai-project-manifest.yaml` without re-running the resolver.  
**Resolution:** Re-execute `python project-kit/resolver/resolve.py --manifest ai-project-manifest.yaml --output effective-policy-snapshot.json`, review the diff, and commit the newly generated snapshot.

### Q2: How do I add a new tool or MCP server to my autonomous agent?
**Cause:** The outside-the-model PEP proxy rejects unregistered tool calls with `HTTP 403 Tool Not Authorized`.  
**Resolution:**
1. Author a JSON Schema defining the tool's parameter structure.
2. Update [`templates/agent-tool-registry.template.yaml`](file:///c:/ai-governance-package/templates/agent-tool-registry.template.yaml) with the new tool name, schema, and execution mode (`read_only` vs `destructive_write_requires_approval`).
3. Obtain security lead sign-off.
4. Register the tool in the agent PEP proxy configuration.

### Q3: The resolver halted with `UNRESOLVED_CONFLICT_HALT`. How do I proceed?
**Cause:** Two selected overlays specified contradictory parameters that cannot be resolved automatically (e.g., Overlay A mandates retention $\le 30$ days for privacy, while Overlay B mandates retention $\ge 90$ days for statutory financial auditing).  
**Resolution:** Contact the AI Governance Review Board. A joint legal and regulatory determination will be made to establish which obligation takes statutory precedence.

### Q4: We are using a hosted foundation model via API. Do we still need to provide a Model Card?
**Yes.** For hosted commercial models (e.g., Claude, GPT-4), populate [`templates/model-card.template.yaml`](file:///c:/ai-governance-package/templates/model-card.template.yaml) with vendor-published model card metadata, declare system prompt configurations, cite provider trust center URLs, and document your internal evaluation benchmarks.

---
*Enterprise AI Governance Platform &bull; Baseline Version v0.1.0-draft &bull; Status: DRAFT*
