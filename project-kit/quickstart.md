# AI Governance Adoption Quickstart Guide

**Target Audience:** AI Project Leads, Machine Learning Engineers, MLOps / DevOps Leads  
**Package Baseline:** `v0.1.0-draft`  
**Status:** DRAFT  
**Owner Placeholder:** [ROLE: AI Governance Enablement Lead]  
**Review Date:** [YYYY-MM-DD]  

---

## 1. Overview

The Enterprise AI Governance Package provides a declarative, machine-readable framework to ensure AI systems deployed across the enterprise are safe, secure, compliant, and auditable.

Instead of navigating lengthy static compliance documents, your project declares its operational characteristics in a single YAML file (`ai-project-manifest.yaml`). The governance engine resolves these declarations against immutable enterprise baselines and contextual overlays, outputting an authoritative `effective-policy-snapshot.json` enforced automatically across your CI/CD pipelines.

---

## 2. 5-Step Project Integration Workflow

```
[Step 1: Declare Manifest]  -->  [Step 2: Pin Overlays]  -->  [Step 3: Resolve Policy Snapshot]
                                                                        |
                                                                        v
[Step 5: Exceptions & Audit] <-- [Step 4: Wire CI/CD Gates] <-----------+
```

### Step 1: Copy and Initialize `ai-project-manifest.yaml`

Copy the starter template from the integration kit into the root directory of your project repository:

```bash
cp project-kit/ai-project-manifest.template.yaml ai-project-manifest.yaml
```

Edit `ai-project-manifest.yaml` to declare your system's operational profile:
1. **Metadata:** Set `project_id`, `project_name`, repository URL, and designated owner contacts (`business_owner`, `technical_lead`, `risk_officer`).
2. **System Profile:** Select your `archetype` (`predictive_ml`, `generative_llm`, `rag_system`, `autonomous_agent`, or `hybrid`) and `risk_tier` (`tier_1_minimal` through `tier_4_unacceptable`).
3. **Declared Characteristics:** Accurately set binary flags under `declared_characteristics` (e.g. `executes_tools_or_code`, `processes_personal_data`, `interacts_directly_with_public`).

> [!IMPORTANT]
> Be truthful when declaring characteristics. CI/CD scanners and static analyzers independently inspect your code and models during pull requests; mismatches will halt pipeline admission.

---

### Step 2: Bind Governance Baseline and Contextual Overlays

In the `governance_bindings` section of your manifest, pin the approved baseline version and identify any applicable contextual overlays:

```yaml
governance_bindings:
  baseline_version_pin: "v0.1.0-draft"
  overlay_pins:
    # If deploying or marketing outputs in the EU:
    - overlay_id: "ORG-OVL-GEO-EU-001"
      version_pin: "0.1.0-draft"

    # If operating in financial services, banking, or credit allocation:
    - overlay_id: "ORG-OVL-SEC-FIN-001"
      version_pin: "0.1.0-draft"

    # If classified as Tier 3 High Risk:
    - overlay_id: "ORG-OVL-RSK-TIER3-001"
      version_pin: "0.1.0-draft"

    # If deploying autonomous agentic execution loops:
    - overlay_id: "ORG-OVL-ARC-AGENT-001"
      version_pin: "0.1.0-draft"

  active_exceptions: []
```

---

### Step 3: Generate the Effective Policy Snapshot

Run the Deterministic Resolver tool locally to compute your project's active governance obligations:

```bash
python project-kit/resolver/resolve.py \
    --manifest ai-project-manifest.yaml \
    --output effective-policy-snapshot.json
```

The resolver executes the following deterministic steps:
1. Ingests your manifest and validates it against `schemas/project-manifest.schema.json`.
2. Evaluates conditional control predicates against your declared characteristics, selecting the active subset of the 61 baseline controls.
3. Applies pinned overlays using the **monotonic merge algebra**: tightens numerical parameters, upgrades enforcement modes (e.g., advisory $\to$ blocking), and accumulates required evidence artifacts.
4. Generates a cryptographically hashed `effective-policy-snapshot.json`.

Inspect `effective-policy-snapshot.json` to review your active controls, effective parameters (e.g. `max_hallucination_rate`, `drift_psi_alert_threshold`), and required evidence artifacts.

---

### Step 4: Wire Automated Pipeline Enforcement Gates

Integrate the policy snapshot into your software delivery lifecycle:

- **Local Workstations (Pre-commit):** Run client-side linters to catch plain-text API secrets, prohibited dependencies, or missing manifest fields before committing.
- **Pull Requests (PR Checks):** Add a CI workflow step that runs `resolve.py --validate-only` to ensure PR changes have not invalidated manifest constraints or broken parameter thresholds.
- **Model Promotion Gates:** Before model weights or container images are promoted to production, admission controllers verify that all required evidence records declared in `snapshot.controls` exist in the compliance registry and are cryptographically signed.

```yaml
# Example CI/CD Workflow Step (Tool-Neutral)
- name: Verify AI Governance Policy Conformance
  run: |
    python project-kit/resolver/resolve.py --manifest ai-project-manifest.yaml --validate-only
    echo "Governance baseline and overlays verified successfully."
```

---

### Step 5: Manage Exceptions and Evidence Records

#### Requesting a Policy Variance
If operational constraints prevent immediate compliance with a specific control parameter (e.g., benchmark accuracy needs further fine-tuning):
1. Copy `project-kit/exception-request.template.yaml` to `exceptions/ORG-EXC-YYYY-XXX.yaml`.
2. Define compensating technical safeguards (e.g., mandatory secondary validator sidecars, human-in-the-loop review queues).
3. Submit the request to the Enterprise AI Safety Review Board for formal approval.
4. Once approved, add the exception ID to `governance_bindings.active_exceptions` in your manifest and re-run `resolve.py`.

> [!CAUTION]
> Internal exceptions **NEVER** waive statutory legal requirements (e.g., EU AI Act Article 50 public disclosure, ECOA credit adverse action explanation, or agent emergency kill switch). Any exception attempting to waive a statutory mandate will be rejected automatically by the resolver.

#### Producing Evidence Records
Before deployment, your build and evaluation jobs generate structured JSON evidence records matching `schemas/evidence-record.schema.json`. These include benchmark evaluation reports (`eval_benchmark_report`), accessibility audits, and security vulnerability scans. Evidence bundles are preserved in immutable audit storage in accordance with your retention schedule.

---

## 3. Getting Help and Escalation

- **AI Safety & Governance Review Board:** `ai-governance-board@internal.net`
- **Model Risk Management Intake:** `model-risk-intake@internal.net`
- **Policy Package Architecture Team:** `ai-platform-architecture@internal.net`
