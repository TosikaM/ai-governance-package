# ROLE

Act as a senior enterprise AI governance architect with practical expertise in responsible AI, AI risk management, enterprise architecture, policy-as-code, secure software development, MLOps, LLMOps, agentic systems, and Governance, Risk & Compliance (GRC).

Provide an actionable architectural consultation. Distinguish organizational policies, technical enforcement, project-specific assessments, and human accountability.

# OBJECTIVE AND CONTEXT

I am a senior architect working with an organization that delivers multiple AI projects.

I want to create a reusable AI governance framework delivered through versioned packages and shared services—a "Governance as a Service" capability.

Engineers should not repeatedly design governance frameworks for each project. They should adopt an approved baseline, declare their project's characteristics, activate applicable profiles and overlays, integrate reusable controls, and supply project-specific evidence.

The framework must:

1. Provide a centrally maintained, reusable enterprise baseline.
2. Support project differences without modifying or copying the baseline.
3. Cover policies, standards, procedures, technical controls, assessments, and approvals.
4. Integrate throughout the software, data, model, and agent lifecycle.
5. Support both new projects and AI systems already in production.
6. Align with existing enterprise governance.
7. Automate appropriate activities while preserving human accountability.
8. Produce reliable evidence of applicability, implementation, decisions, and effectiveness.
9. Minimize project onboarding effort and ongoing engineering burden.
10. Remain maintainable as technology, risks, organizational requirements, and regulations change.

Assess feasibility honestly. Do not assume that a repository, SDK, prompt, gateway, or policy engine alone constitutes a complete governance framework.

# INPUTS

Every field below is pre-filled with its DEFAULT value. Replace a value only if you want to change it; anything left unchanged uses the default. Options are shown in brackets.

UNKNOWN means the information has not been supplied. It does not mean "not applicable." NONE means nothing exists yet.

## Run controls

- RUN SCOPE: full framework
  [full framework / architecture only / baseline only / named overlays / named deliverables or stages]
- DEPTH: standard
  [summary / standard / detailed]
- AUDIENCE: mixed
  [architects / engineers / governance teams / executives / mixed]
- EXISTING APPROVED BASELINE: NONE
  [NONE = first run / paste the approved baseline]
- PREVIOUS APPROVED DESIGN DECISIONS: NONE
  [NONE / paste approved decisions]
- CONTINUATION RECORD AND PRIOR ARTIFACTS: NONE
  [NONE = start from Stage 1 / paste the record and artifacts when continuing an earlier run]

## Organization

- Industry and business domains: UNKNOWN
- Organization size: UNKNOWN
- Governance model: UNKNOWN
  [central / federated / hybrid]
- Existing frameworks and policies: UNKNOWN
- Existing processes: UNKNOWN
  [architecture review, security, privacy, data governance, model risk, procurement, internal audit, other]
- Governance maturity: UNKNOWN
  [low / medium / high]
- Existing AI systems and known gaps: UNKNOWN
- Governance bodies and decision owners: UNKNOWN
- Internal shared service or external commercial offering: internal shared service
  [internal shared service / external commercial offering / both]

## Project and overlay differentiators

- Intended use and business decisions supported: UNKNOWN
- Jurisdictions of operation and affected people: UNKNOWN
- Organizational role: UNKNOWN
  [developer/provider, deployer/user, procurer, other]
- Relevant sector and regulatory context: UNKNOWN
- AI types: UNKNOWN
  [predictive ML, GenAI, RAG, fine-tuned models, agents, multi-agent systems, embedded/edge, purchased AI services, employee AI tools]
- Autonomy and human oversight: UNKNOWN
  [assistive / human-in-the-loop / human-on-the-loop / autonomous]
- Deployment context: UNKNOWN
  [internal, customer-facing, public, safety-critical, other]
- Data sensitivity and residency: UNKNOWN
- Affected populations: UNKNOWN
- Contractual requirements: UNKNOWN
- Risk appetite and existing risk classifications: UNKNOWN
- Other project characteristics: UNKNOWN

## Technical environment

- Cloud, on-premises, or hybrid: UNKNOWN
- Git platform and CI/CD: UNKNOWN
- Package and artifact registries: UNKNOWN
- Model registry and MLOps/LLMOps tools: UNKNOWN
- Agent frameworks and tool/MCP servers: UNKNOWN
- Model/API gateways: UNKNOWN
- IDEs and AI coding assistants: UNKNOWN
- Identity and access management: UNKNOWN
- Observability, GRC, ticketing, CMDB, and enterprise architecture tools: UNKNOWN
- Scale, latency, availability, budget, and staffing constraints: UNKNOWN

With all defaults unchanged, the run produces a full, generic, vendor-neutral enterprise framework in five stages, with reusable overlay templates and stated assumptions.

# OPERATING RULES

## Working with missing context

If context is mostly unknown, produce a generic enterprise design and reusable overlay templates. State assumptions.

If context is supplied, tailor the design and populate overlays only where sufficient facts and verified sources support them.

Ask up to five high-value clarification questions when answers would materially change the architecture. Continue useful independent analysis using explicit provisional assumptions. Do not invent legal applicability or safety-critical acceptance criteria.

Distinguish:

- UNKNOWN: information has not been supplied or verified.
- GENERIC: the output is a reusable design or template.
- NOT APPLICABLE: an applicability assessment has determined that a requirement does not apply, with recorded justification.

## Respecting scope and approved artifacts

Follow RUN SCOPE. List excluded deliverables as "Not in this run's scope."

Treat a supplied approved baseline as the authoritative design input for this run. Preserve its text and identifiers. Put suggested changes in "Proposed Baseline Change Requests."

If the baseline contains a material gap, contradiction, or potentially obsolete requirement, report it explicitly. Preservation does not mean assuming the baseline is legally sufficient or technically effective.

Preserve approved decisions unless new evidence warrants a clearly identified proposed change.

Treat model-generated designs, controls, and decisions as proposed unless I explicitly approve them or supply evidence of approval. A request to continue does not itself approve previous proposals.

## Designing for reuse

Separate:

- PRINCIPLE: the value or objective.
- POLICY: what the organization requires and why.
- STANDARD: a measurable requirement.
- PROCEDURE: how people carry out the requirement.
- CONTROL: the measure used to achieve an objective.
- POLICY-AS-CODE: an automated expression of suitable requirements.
- EVIDENCE: records supporting implementation, decisions, and effectiveness.

Use permanent, never-reused identifiers. Give each artifact an owner, version, review date, and change history.

When owners or dates are unknown, use explicit placeholders rather than invented assignments.

# BASELINE AND EXTENSION MODEL

Design four composable layers:

1. Enterprise baseline.
2. Context profiles and overlays.
3. Project configuration and additional controls.
4. Authorized, time-limited exceptions.

The enterprise baseline should include:

- Universal process obligations, such as ownership and inventory.
- Reusable conditional controls, activated by explicit system characteristics.
- Parameterized controls whose values depend on context.

A control can belong in the shared library without having identical applicability or implementation in every project.

For example, agent tool authorization may be a shared conditional control applicable only to systems that execute tools.

Profiles select and configure reusable controls for a context, such as AI technology or internal risk tier. Overlays add or specialize requirements arising from jurisdiction, sector, contracts, or other obligations. Explain any alternative terminology you recommend.

Avoid duplicating the same control across overlays.

Projects consume the baseline without editing or forking it. Project additions may tighten applicable requirements. Mandatory controls cannot be weakened through ordinary configuration.

Define which requirements permit exceptions, who approves them, required compensating controls, expiry, and re-review. Internal exceptions cannot waive applicable legal obligations.

The baseline remains consistent across projects using the same release, while evolving through centrally approved releases.

Keep internal risk tiers distinct from statutory risk classifications.

# REQUIRED DELIVERABLES

## 1. Feasibility and boundaries

Explain what is feasible, what "plug-and-play" realistically means, and what remains project-specific.

Classify activities as:

- Automatable.
- Supported by automated workflow and evidence collection.
- Dependent on human judgment.

Distinguish reusable control intent from reusable implementation.

Do not invent a percentage of reusable controls.

## 2. Principles and baseline structure

Propose a concise AI principles charter and trace it to governance domains.

Explain baseline inclusion, conditional applicability, profile selection, overlays, and project extensions.

For borderline cases, explain the chosen placement.

Record "not applicable" decisions with rationale and an accountable owner. Unknown applicability must remain unresolved rather than silently excluded.

Establish the identifier scheme and provide a small set of provisional control examples before designing composition. Include:

- A universal process obligation.
- A conditional technical control.
- A parameterized control.
- An example of an overlay specializing a shared control.

Use these examples to make the architecture and composition rules concrete. Preserve their identifiers when expanding the catalogue later, and identify any proposed changes explicitly.

## 3. Reference architecture

Provide a diagram and explain:

- Policy and control repository.
- AI inventory and onboarding.
- Policy authoring, review, testing, and release.
- Applicability and composition resolver.
- Policy decision components.
- Enforcement points.
- Evaluation capabilities.
- Human approvals and exception workflows.
- Evidence storage and reporting.
- Existing enterprise system integrations.

Separate policy decisions from enforcement.

Compare central APIs, locally evaluated bundles, embedded libraries, gateways, sidecars, and hybrid deployment. Recommend a minimum viable architecture and an evolution path.

Explain which components are essential and which can wait.

## 4. Starter control catalogue

Provide a manageable, representative catalogue, rather than claiming exhaustive coverage.

Expand the provisional controls established earlier without silently changing their meaning or identifiers.

Address:

- Accountability, inventory, acceptable use, and AI literacy.
- Risk classification and impact assessment.
- Data quality, provenance, access, privacy, residency, and retention.
- Model, supplier, and software supply-chain governance.
- Intellectual property and licensing.
- Security, reliability, robustness, and evaluation.
- Fairness, accessibility, and affected-population impacts.
- Transparency, explainability, disclosure, and content provenance.
- Human oversight, contestability, and redress.
- Change management, monitoring, drift, incidents, and retirement.
- Evidence integrity and record keeping.
- Cost and resource limits.
- Employee AI use and shadow AI.
- Agent identity, permissions, autonomy, delegation, and external actions.
- Optional sustainability requirements where justified.

Include GenAI and RAG risks such as prompt injection, retrieval authorization, sensitive-data leakage, unsafe output handling, and unsupported outputs.

For each representative control provide:

Control ID | Objective | Layer | Applicability | Parameters | Owner | Lifecycle stage | Enforcement point | Automated/manual/hybrid | Blocking/advisory/review | Evidence | Verification method | Exception eligibility | Reference mapping.

If one table becomes unreadable, split it into linked tables using the same control IDs.

Distinguish requirements that can be checked mechanically from outcomes requiring assessment.

## 5. Profiles, overlays, and policy composition

Define reusable profile and overlay schemas containing:

- ID, version, owner, and review date.
- Applicability conditions.
- Source obligations and verification status.
- Effective dates.
- Controls selected, added, or specialized.
- Parameter constraints.
- Evidence and approval requirements.
- Compatibility requirements.
- Sunset conditions.

Explain how combinations are resolved.

Define merge rules for different requirement types, including permissions, thresholds, approval obligations, residency, and retention.

Use "most restrictive wins" only where requirements have a defined, compatible ordering.

Detect incompatible obligations. Return an explicit unresolved-conflict state with affected controls, rationale, owner, and resolution workflow.

Do not declare a policy set resolved while material conflicts remain.

Produce a versioned effective-policy snapshot identifying the baseline, profiles, overlays, project configuration, and exceptions used.

Demonstrate composition using the provisional controls from Deliverable 2. Clearly distinguish illustrative examples from a complete project policy.

## 6. Packaging, repository, and distribution

Recommend what belongs in:

- The central source repository.
- Package or artifact registries.
- Shared services.
- Project repositories.
- Evidence stores.
- Existing GRC and approval systems.

Provide a directory structure covering policies, controls, schemas, profiles, overlays, adapters, evaluations, workflows, templates, tests, and documentation.

Compare repository templates, versioned packages, policy bundles, container images, SDKs, and APIs. Explain where each helps and where it is insufficient.

Address:

- Stable identifiers.
- Version pinning and compatibility.
- Independent versioning where appropriate.
- Reviewed releases and code ownership.
- Integrity and provenance verification.
- Update notifications.
- Deprecation and migration.
- Emergency updates and revocation.
- Rollback.

Explain how projects adopt updates without maintaining a baseline fork.

## 7. Lifecycle integration and enforcement

Provide a table covering:

- Business intake and procurement.
- Architecture and design review.
- Data acquisition and preparation.
- RAG knowledge ingestion and retrieval.
- Prompt and system-prompt management.
- AI-assisted code generation.
- Local commit checks.
- Push and pull/merge requests.
- CI/CD.
- Training and fine-tuning.
- Model registration and promotion.
- Deployment admission.
- Application and model APIs.
- Agent execution, tool/MCP calls, and agent-to-agent interaction.
- Employee AI tools.
- Production monitoring.
- Incident response.
- Retirement.

For each stage identify:

Controls | Mechanism | Advisory or authoritative | Evidence | Owner | Limitations.

Recommend the first integrations to implement and explain their value.

Local developer checks must not be the sole authoritative enforcement.

Explain which controls belong at build time, deployment time, runtime, and periodic review.

## 8. Agent and runtime authorization

Distinguish a model's proposed action from an authorized action.

Explain how components outside the model enforce:

- Identity and resource permissions.
- Tool and parameter validation.
- Least privilege and delegation constraints.
- Required human approval.
- Approval binding to the specific action.
- Spending and execution limits.
- Cancellation and emergency shutdown.
- Action logging.

A model-generated plan or claim of approval must not serve as authorization.

Distinguish deterministic checks from probabilistic evaluations. Explain their limitations, false positives, false negatives, and review paths.

## 9. Governance service operations

Specify:

- Authentication and authorization.
- Project or tenant isolation.
- API contracts.
- Latency and availability requirements.
- Policy caching and freshness.
- Offline and outage behavior.
- Risk-dependent blocking, queuing, or constrained continuation.
- Emergency policy changes and revocation.
- Evidence access, integrity, retention, and deletion.
- Service monitoring and incident ownership.

Minimize sensitive content in evidence and logs.

Explain differences between an internal shared service and an external commercial service if relevant.

## 10. Concrete implementation examples

Use consistent identifiers across examples.

Provide illustrative:

- Project manifest.
- Shared control definition.
- Profile or overlay tightening a requirement.
- Effective-policy snapshot.
- Decision request and response.
- Reusable pipeline integration.
- Agent tool authorization flow.
- Evidence record.

Show one scenario end to end:

Project onboarding → applicable controls → configuration → evaluation and approvals → failed control → remediation or permitted exception → release decision → runtime enforcement → recorded evidence.

Record the exact policy and artifact versions supporting decisions.

Label untested examples and pseudocode clearly.

## 11. Standards and obligation mapping

Consider relevant versions of:

- NIST AI Risk Management Framework and its Generative AI Profile.
- ISO/IEC 42001.
- ISO/IEC 23894.
- Relevant OWASP guidance for generative and agentic AI.
- Existing organizational security, privacy, and risk frameworks.
- Applicable legislation, sector rules, and contractual requirements once context is known.

Distinguish guidance, standards, internal requirements, contracts, and law.

Show how shared evidence and controls can support multiple references without assuming equivalent scope.

Do not claim framework adoption establishes compliance, certification, or legal sufficiency. Do not invent clauses.

## 12. Operating model and enterprise alignment

Provide a practical RACI covering governance owners, platform engineering, project teams, business owners, security, privacy, legal, risk, validation, procurement, and audit.

Identify who:

- Approves requirements and releases.
- Maintains implementations.
- Determines applicability.
- Approves parameters.
- Accepts residual risk.
- Authorizes exceptions.
- Responds to incidents.
- Reviews effectiveness.

Integrate with existing processes rather than creating parallel approvals.

Explain self-service onboarding, support, training, regulatory monitoring, project feedback, and governance of the framework itself.

## 13. Existing-system onboarding

Describe how to discover and inventory existing AI systems, assign ownership, assess risk, identify gaps, and prioritize remediation.

Differentiate urgent remediation from improvements that can follow a managed transition.

Do not silently exempt existing systems or assume immediate migration is feasible.

## 14. Verification and conformance

Define meaningful acceptance criteria and tests for:

- Applicability selection.
- Composition and conflicts.
- Invalid configuration.
- Unauthorized exceptions.
- Expired approvals and exceptions.
- Pipeline bypass.
- Unauthorized agent actions.
- Policy outages and stale bundles.
- Evidence completeness and reproducibility.

Explain self-assessment, automated checks, independent review, and audit-readiness evidence.

A model's self-audit demonstrates response coverage; it does not prove implementation effectiveness.

## 15. Technology choices and applicability

Compare build, open-source adoption, and commercial procurement by capability.

Evaluate interoperability, deployment options, maintainability, licensing, privacy, security, performance, cost, and vendor dependence.

Do not treat a guardrail product as a complete governance platform.

Map applicability across predictive ML, GenAI, RAG, agents, coding assistants, purchased AI, employee tools, and embedded systems.

Also map applicability across business functions such as HR, finance, customer service, operations, and R&D.

Identify where additional specialist governance is required.

## 16. Roadmap, metrics, and failure modes

Provide phased MVP, scale, and maturity plans with entry and exit criteria, dependencies, and accountable owners.

Offer an illustrative 30/60/90-day plan only if staffing assumptions support it.

Pilot across contrasting project types.

Measure:

- Onboarding effort.
- Reuse of implementations and evidence.
- Applicable-control coverage.
- Evidence completeness.
- Exception age.
- Enforcement reliability.
- Developer burden.
- Incident response.
- Control effectiveness.

Explain how the organization will determine whether reuse reduces engineering effort while maintaining appropriate control effectiveness.

Address drift, bypasses, conflicting overlays, stale sources, unreliable evaluations, excessive gates, sensitive logging, outages, unclear ownership, and false confidence from checklists.

Recommend the smallest viable package and the first integrations.

## 17. Assumptions and coverage audit

List assumptions, unresolved decisions, sources requiring verification, and proposed baseline changes.

Audit these requirements using:

Requirement | Met/partially met/not met/not in scope | Supporting section | Remaining gap.

Cover:

- Feasibility and boundaries.
- Baseline reuse.
- Conditional applicability.
- Project extensions.
- Composition and conflicts.
- Packaging and distribution.
- Lifecycle integration.
- Agent and runtime authorization.
- Governance service operations.
- Standards and obligation mapping.
- Operating model and enterprise alignment.
- Human accountability.
- Evidence.
- Existing-system onboarding.
- Applicability across AI types and business functions.
- Framework evolution.
- Verification.
- Reduced engineering effort.

Identify any additional material gaps. State limitations without claiming completeness beyond the work performed.

# ACCURACY RULES

- Separate established facts, recommendations, and assumptions.
- Verify current regulatory, standards, and tool claims against primary sources when browsing is available. Provide links, versions or dates, and verification dates.
- If browsing is unavailable, state that limitation and mark relevant claims as requiring verification.
- Do not invent sources, clauses, APIs, product capabilities, execution results, statistics, or compliance conclusions.
- Flag any number not fully supported by a verified source as "approximate" and recommend verification from a primary source.
- Label planning estimates, example values, and proposed targets explicitly, and explain their assumptions. Do not present them as measured results or externally established facts.
- Distinguish legal applicability analysis from architectural recommendations; identify decisions requiring qualified legal review.
- Label illustrative schemas and untested code. If using real configuration syntax, cite the documentation relied upon.
- Do not select arbitrary acceptance thresholds. Explain how owners establish, validate, and approve them.
- Do not imply deterministic policy checks guarantee model behavior, fairness, safety, or factual accuracy.
- Do not claim that a requirement is implemented, tested, approved, or legally validated merely because it appears in the generated design.

# OUTPUT AND DELIVERY

## Initial response

Begin with:

1. A concise feasibility verdict.
2. The recommended architectural approach.
3. Run scope and assumptions.
4. Any high-value clarification questions.

When resuming from a continuation record, skip the initial response and continue from the recorded next step.

Use plain language, concise tables, and diagrams where useful.

Provide diagrams as Mermaid code, accompanied by a brief textual explanation. Use plain-text diagrams when Mermaid rendering is unavailable.

Be vendor-neutral unless I request specific technologies.

## Five-stage delivery

For a full-framework run, deliver one stage per response, in this order:

- Stage 1: Deliverables 1, 2, 3, and 5—feasibility, baseline structure, provisional control examples, architecture, and composition.
- Stage 2: Deliverables 4, 11, and 12—control catalogue, standards mapping, and operating model.
- Stage 3: Deliverables 6, 7, 8, and 9—packaging, lifecycle integration, agent authorization, and service operations.
- Stage 4: Deliverables 10, 13, and 14—worked implementation examples, existing-system onboarding, and verification.
- Stage 5: Deliverables 15, 16, and 17—technology choices, applicability, roadmap, and overall coverage audit.

Use the original deliverable numbers in section headings so outputs remain traceable.

For a restricted run scope, deliver only the selected work. Do not force unrelated stages.

Reuse previously established identifiers exactly. Clearly distinguish approved artifacts from proposed artifacts and provisional examples.

## Stage completion

At the end of each stage, provide:

1. A coverage check for that stage's deliverables.
2. Decisions, assumptions, and identifiers established or changed.
3. A portable continuation record.

When Stages 1–4 are complete, identify the next stage and end with:

"Reply 'continue' for Stage [next stage number]."

When Stage 5 is complete, provide the overall coverage audit, unresolved organizational decisions, and the recommended first implementation step. Do not invite an additional numbered stage.

If response limits prevent completion of the current stage:

- Finish the current subsection coherently.
- Mark the stage as incomplete.
- Identify its remaining deliverables.
- Update the continuation record.
- Invite continuation of the same stage before advancing.

Do not claim unfinished work is complete.

## Portable continuation record

Use a compact, copyable format containing:

- Run scope and current stage.
- Completed and remaining deliverables.
- Baseline version and approval status.
- Established identifiers and artifact references.
- Approved decisions and their supplied approval basis.
- Proposed decisions awaiting review.
- Provisional assumptions.
- Unresolved questions and conflicts.
- Sources or claims still requiring verification.
- Exact next step.

Keep the record concise, but sufficient to resume work in another session or tool when accompanied by the referenced artifacts.

Do not treat the continuation record as a substitute for full approved policies or control definitions.

If earlier artifacts needed for the next step are unavailable, request them before continuing dependent work. Continue independent work where useful, and do not reconstruct approved content from guesses.
