# Enterprise AI Governance Package: Overlay Framework & Merge Engine Specification

**Status:** DRAFT  
**Baseline Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: AI Governance Platform Architect & Lead Regulatory Counsel]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Executive Summary & Purpose

The Enterprise AI Governance Package enforces an immutable baseline of universal, conditional, and parameterized controls. However, AI deployments operate across divergent legal jurisdictions (e.g., EU AI Act, US State Privacy Laws), highly regulated industry sectors (e.g., Financial Services, Healthcare), distinct risk profiles (Tiers 1–4), and technical architectures (e.g., autonomous agents vs. predictive tabular models).

The **Overlay Framework** provides a declarative, machine-readable mechanism to specialize and tighten governance requirements for specific contexts.

```
                    +-------------------------------------------------------+
                    |           Enterprise Baseline (61 Controls)           |
                    |    Immutable universal, conditional & parameterized   |
                    +-------------------------------------------------------+
                                                |
                                                v
                        +-----------------------------------------------+
                        |             Attached Overlays                 |
                        |  - Geography Overlay (e.g. EU AI Act)         |
                        |  - Sector Overlay (e.g. Banking / FinServ)    |
                        |  - Risk Tier Overlay (e.g. Tier 3 High Risk)  |
                        |  - Archetype Overlay (e.g. Autonomous Agents) |
                        +-----------------------------------------------+
                                                |
                                                v
                    +-------------------------------------------------------+
                    |             Deterministic Merge Engine                |
                    |  - Monotonicity Invariant: Add/Tighten Only           |
                    |  - Typed Directional Merging                          |
                    |  - Incompatible Conflict Detection                    |
                    +-------------------------------------------------------+
                                                |
                                                v
                    +-------------------------------------------------------+
                    |         Effective-Policy Snapshot (JSON)              |
                    |    The authoritative ruleset enforced at runtime      |
                    +-------------------------------------------------------+
```

---

## 2. Core Architectural Invariants

### 2.1 Monotonicity Invariant (Never Weaken)
Overlays **MUST NEVER** weaken, relax, or waive baseline controls. An overlay can only:
1. **Add new controls** not present in the baseline.
2. **Tighten numerical parameters** in a stricter direction.
3. **Upgrade enforcement modes** (e.g., from `advisory` to `blocking`).
4. **Require additional evidence artifacts** beyond baseline minimums.
5. **Restrict or eliminate exception eligibility** for specific controls.

Any overlay proposing to relax a baseline parameter, downgrade a blocking control to advisory, or eliminate required evidence is syntactically invalid and will be rejected by the resolver.

### 2.2 Independent Versioning & Decoupling
Overlays are versioned independently of the baseline package adhering to Semantic Versioning 2.0.0. Each overlay specifies a `baseline_compatibility` range expression (e.g., `>=0.1.0 <2.0.0`). Consuming projects pin exact overlay versions in their `ai-project-manifest.yaml`.

### 2.3 Legal Review Requirement
All regulatory overlays (jurisdictional or statutory mandates) carry an explicit `legal_review_status` field. Overlays cannot graduate from `DRAFT` to `APPROVED` without formal sign-off by qualified legal counsel.

---

## 3. Typed Merge Algebra & Deterministic Resolution

When a project attaches multiple overlays (e.g., an EU geographic overlay AND a Financial Services sectoral overlay), the resolver merges their obligations using typed, deterministic rules:

```
                            [Overlay Merge Process]
                                       |
                     +-----------------+-----------------+
                     |                                   |
           [Target Control Exists?]              [New Control Added?]
                     |                                   |
         +-----------+-----------+                       v
         |                       |             [Insert Control into Snapshot]
  [Mode Upgrade?]        [Parameter Change?]
         |                       |
         v                       v
  [Advisory -> Blocking]   [Apply Directional
   (Monotonic Upgrade)      Monotonic Envelope]
                                 |
                     +-----------+-----------+
                     |                       |
               [Ordered Set?]         [Incompatible?]
                     |                       |
                     v                       v
             [Tightened Value]     [UNRESOLVED_CONFLICT_HALT]
```

### 3.1 Numerical Parameters (Directional Monotonic Envelope)
Numerical parameters declare a `monotonicity` attribute in their control definition:
- `lower_is_stricter`: The effective parameter is the mathematical minimum of all declared values.
  $$\text{effective} = \min(\text{baseline}, \text{overlay}_1, \text{overlay}_2, \dots)$$
  *Example:* Hallucination rate ceiling. If baseline is `0.05` and an overlay declares `0.02`, effective is `0.02`.
- `higher_is_stricter`: The effective parameter is the mathematical maximum of all declared values.
  $$\text{effective} = \max(\text{baseline}, \text{overlay}_1, \text{overlay}_2, \dots)$$
  *Example:* Accuracy floor. If baseline is `0.85` and an overlay declares `0.92`, effective is `0.92`.

### 3.2 Discrete Sets & Enums (Strict Subset Narrowing)
For parameters consisting of allowed sets (e.g., allowed cloud regions):
- `strict_subset`: The effective set is the mathematical intersection of the baseline and overlay sets.
  $$\text{effective} = \text{baseline} \cap \text{overlay}_1 \cap \text{overlay}_2$$
  If the intersection yields the empty set ($\emptyset$), the resolver halts with an `UNRESOLVED_CONFLICT_HALT`.

### 3.3 Enforcement Modes (Monotonic Progression)
Control modes progress strictly along a monotonic escalation ladder:
$$\text{advisory} \longrightarrow \text{review} \longrightarrow \text{blocking}$$
- If any overlay upgrades a control from `advisory` to `blocking`, `blocking` wins.
- `blocking` is an absorbing state; no overlay may demote a control.

### 3.4 Evidence Requirements (Additive Union)
Evidence requirements merge via cumulative set union:
$$\text{effective\_evidence} = \text{baseline\_evidence} \cup \text{overlay\_evidence}$$
Projects must provide all evidence artifacts required by both baseline and all attached overlays.

### 3.5 Exception Eligibility (Restrictive Override)
- If baseline permits exceptions but an overlay marks `disallow_exceptions: true`, exceptions are forbidden for that project.
- Additional mandatory compensating controls declared in overlays are appended to the required compensation list.

---

## 4. Conflict Detection & The UNRESOLVED-CONFLICT State

### 4.1 Incompatible Obligations
When multiple overlays impose contradictory obligations with no defined mathematical ordering relation, the resolver **MUST NOT** guess or silently drop requirements. 

*Concrete Examples:*
- **Contradictory Retention Horizons:** A banking regulation mandates preserving transaction logs for `7 years`, while a local privacy statute mandates purging customer telemetry within `30 days`.
- **Exclusive Regional Boundaries:** An EU overlay restricts storage to `eu-central-1`, while a US healthcare overlay restricts storage to `us-east-1`.

### 4.2 Resolver Behavior: `UNRESOLVED_CONFLICT_HALT`
Upon encountering incompatible obligations:
1. The resolver immediately halts and sets system status to `UNRESOLVED_CONFLICT_HALT`.
2. The resolver outputs a machine-readable Conflict Diagnostic Report detailing:
   - Conflicting Overlay IDs (e.g., `ORG-OVL-GEO-EU-001` vs. `ORG-OVL-SEC-FIN-001`).
   - Target Control ID and Parameter Name.
   - Declared Incompatible Values.
   - Designated Escalation Routing Path.
3. Automated deployment controllers block admission until an authorized arbitration resolution or legal determination is applied.

---

## 5. Overlay Taxonomy & Skeletons

The package establishes four canonical overlay categories:

| Category | Identifier Pattern | Scope & Purpose | Canonical Example |
|---|---|---|---|
| **Geography** | `ORG-OVL-GEO-{JURIS}-{NUM}` | Legal statutes binding systems in specific nations or trading blocs. | `ORG-OVL-GEO-EU-001` (EU AI Act) |
| **Sector** | `ORG-OVL-SEC-{SECTOR}-{NUM}` | Industry regulations (financial, clinical, automotive, energy). | `ORG-OVL-SEC-FIN-001` (Financial Services) |
| **Risk Tier** | `ORG-OVL-RSK-{TIER}-{NUM}` | Tier-specific controls specializing baseline expectations. | `ORG-OVL-RSK-TIER3-001` (Tier 3 High Risk) |
| **AI Type** | `ORG-OVL-ARC-{ARCH}-{NUM}` | Architectural guardrails for specific AI paradigms. | `ORG-OVL-ARC-AGENT-001` (Autonomous Agents) |
