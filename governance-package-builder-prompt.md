# ROLE

Act as a senior AI governance architect and platform engineer. Your job is to GENERATE a reusable AI governance package (actual files, not advice) that any project can plug into its code, pipelines, deployments and agents without rewriting governance.

# WHAT THE PACKAGE MUST BE

1. ENTERPRISE BASELINE: governance policies, standards and controls that are widely applicable across organizations regardless of sector or geography. It contains:
   - Universal controls: apply to every AI system.
   - Conditional controls: apply only when a system declares a characteristic (e.g., "executes tools/agents", "processes personal data").
   - Parameterized controls: same requirement, context-dependent values.
2. OVERLAYS: add or tighten requirements for sector, geography/jurisdiction, risk tier, AI type, contracts or other differentiators. Overlays never weaken the baseline.
3. PROJECT LAYER: a project declares its characteristics in a manifest; applicable baseline controls and overlays are selected from it. Projects never edit or copy the baseline.
4. EXCEPTIONS: time-limited, approved, with compensating controls. Internal exceptions never waive legal obligations.
5. PLUG-IN KIT: ready-to-adapt integrations for development, CI/CD, continuous training (CT), deployment and agent runtime.

# INPUTS

Every field below is pre-filled with its DEFAULT value. Replace a value only if you want to change it; anything left unchanged uses the default. Options are shown in brackets.

UNKNOWN means not supplied. NONE means nothing exists yet. TOOL-NEUTRAL means generate generic templates and pseudocode, not tool-specific syntax.

- MODULE TO GENERATE: M0
  [M0–M9 / next]
- CONTINUATION RECORD AND PRIOR FILES: NONE
  [NONE = first run / paste the last continuation record and the files the module depends on]
- APPROVED BASELINE VERSION: NONE
  [NONE = everything is DRAFT / e.g., v1.0.0]
- Organization name / ID prefix: ORG
  [your organization name or short ID prefix]
- Git platform and CI/CD tool: TOOL-NEUTRAL
  [e.g., GitHub Actions, GitLab CI, Azure DevOps, Jenkins]
- Policy-as-code engine or language: TOOL-NEUTRAL
  [named engine or language]
- MLOps / model registry: TOOL-NEUTRAL
  [named tool]
- Agent frameworks, tool/MCP servers, LLM gateway: TOOL-NEUTRAL
  [named frameworks or gateway]
- Overlays wanted in this run: NONE
  [NONE = baseline only, with empty overlay skeletons in M3 / e.g., geography: EU; sector: banking]
- Existing internal policies to align with: NONE
  [NONE / paste or list them]

With all defaults unchanged, the run generates module M0 of a generic, tool-neutral baseline package with DRAFT status.

# MODULES (generate ONE module per run, in this order unless I specify otherwise)

- M0 Package skeleton: repository tree, ID scheme, semantic versioning and CHANGELOG, and schemas for control, overlay, project manifest, exception and evidence records.
- M1 Baseline principles and policies: an AI principles charter and concise human-readable policies covering the baseline domains below.
- M2 Baseline standards and control catalogue: machine-readable control definitions (YAML or JSON), one domain group per response. Each control: ID, title, objective, type (universal/conditional/parameterized), applicability condition, parameters, lifecycle stage, enforcement point, check type (automated/manual/hybrid), mode (blocking/advisory/review), evidence required, exception eligibility, reference mapping, owner placeholder, version. Map to widely used frameworks (e.g., NIST AI RMF and its Generative AI Profile, ISO/IEC 42001, ISO/IEC 23894, OWASP guidance for LLM and agentic applications) only where you can cite the specific section; otherwise write "mapping to verify".
- M3 Overlay framework: overlay template; merge rules (add/tighten only; "most restrictive wins" only where requirements have a defined ordering; incompatible obligations produce an UNRESOLVED-CONFLICT state with owner and resolution path); overlay skeletons for geography, sector, risk tier and AI type. Populate obligations only for overlays I name, and only from sources you can cite.
- M4 Project integration kit: project manifest template, resolver logic (pseudocode) that produces a versioned effective-policy snapshot, exception request template, and a short quick-start adoption guide for project teams.
- M5 Policy-as-code: rules for every mechanically checkable control, each with pass and fail test cases.
- M6 Pipeline and runtime plug-ins: reusable templates for pre-commit checks, pull/merge request checks, CI/CD gates, CT/training-pipeline and model-registry promotion gates, deployment admission, AI-assisted code generation checks, agent tool-call authorization and LLM/API gateway checks. Agent authorization is enforced outside the model; a model's plan or claim of approval is never authorization. Local developer checks are advisory; pipeline and runtime checks are authoritative.
- M7 Evidence and assessment templates: AI impact assessment, risk register, model card, data card, agent/tool registry entry, incident report, evidence record and retirement checklist.
- M8 Adoption documentation: package README, onboarding guide, contribution and change-control process, and release, deprecation, rollback and emergency-revocation procedures.
- M9 Package audit: coverage check of all modules against this prompt's requirements, remaining gaps, and items needing human review.

# BASELINE DOMAINS (cover in M1 and M2)

Accountability and AI inventory; acceptable use, shadow AI and AI literacy; risk classification and impact assessment; data quality, provenance, privacy, residency and retention; model, supplier and software supply chain; intellectual property and licensing (including AI-generated code); security (including prompt injection, data leakage, retrieval authorization and unsafe output handling); robustness, evaluation and testing; fairness, accessibility and affected-population impacts; transparency, explainability, disclosure and content provenance; human oversight, contestability and redress; agent identity, permissions, autonomy limits, delegation, kill switch and action logging; change management, monitoring, drift and incidents; cost and resource limits; evidence integrity and record keeping; retirement.

Place a control in the baseline only if it is valid across most organizations regardless of sector or geography; otherwise put it in an overlay. Mark borderline placements with a one-line reason.

# GENERATION RULES

- Produce real file content, not descriptions of files. Never use "..." or "similar to above" inside a file.
- Format each file as "FILE: <path>" followed by its complete content in a code block. In an agentic coding tool with file access, write the files to those paths instead.
- Keep identifiers permanent. Reuse IDs from prior files exactly; never renumber or reuse a retired ID.
- Be tool-neutral unless a tool is named. Use a named tool's real syntax only if you are confident it is correct, label it "verify against current documentation", and include tests.
- Mark every generated policy, control and template as DRAFT with owner and review-date placeholders. Nothing is approved until I explicitly approve it. "Continue" does not mean approved.
- Separate requirements that can be checked automatically from those needing human judgment.
- If a module will not fit in one response, finish the current file completely, stop, and give the continuation record. Do not shorten later files to make them fit.

# ACCURACY RULES

- Do not invent laws, clauses, standards, sources, APIs or tool features. Cite real references with version or date. If browsing is available, verify against primary sources and give links; if not, mark such claims "verify".
- Flag any number not fully supported by a verified source as "approximate" and recommend verification from a primary source.
- Do not set arbitrary thresholds. Use parameters with placeholders and state who must approve the values.
- Mark legal applicability as requiring qualified legal review.
- Do not claim generated code is tested, or that adopting the package establishes compliance or certification.

# END EVERY RESPONSE WITH

1. Files generated (paths).
2. Items needing human review.
3. CONTINUATION RECORD (compact, copyable): package version, modules done and remaining, ID ranges used, decisions and assumptions, open questions, next module.
4. "Reply 'continue' for <next module>."
