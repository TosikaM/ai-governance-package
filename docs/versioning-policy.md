# Enterprise AI Governance Package: Semantic Versioning Policy

**Status:** DRAFT  
**Baseline Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: AI Governance Platform Architect]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Scope & Semantic Foundation

This package adheres to [Semantic Versioning 2.0.0](https://semver.org/), adapted to govern the lifecycle of declarative policies, machine-readable control definitions, automated pipeline admission gates, and runtime guardrails.

Version identifiers follow the standard format:
```
v<MAJOR>.<MINOR>.<PATCH>[-<PRERELEASE>][+<BUILDMETADATA>]
```
Example: `v1.2.0`, `v0.1.0-draft`, `v2.0.0-rc.1`

---

## 2. Version Increment Rules for Governance Artifacts

Because governance policies directly dictate automated build breaks, PR rejections, and runtime admission blocks, breaking changes must be managed with extreme predictability.

| Component Level | Trigger Condition | Impact on Consuming Projects | Example Action |
|---|---|---|---|
| **MAJOR (vX.0.0)** | **Breaking Governance Change** | Causes previously passing pipelines, manifests, or systems to fail evaluation without configuration changes. | - Introducing a new `blocking` baseline control.<br>- Tightening an existing default parameter threshold.<br>- Upgrading a control mode from `advisory` to `blocking`.<br>- Incompatible schema modification (removing fields, tightening regex).<br>- Retiring a control or altering applicability predicates. |
| **MINOR (v0.X.0 / vX.Y.0)** | **Backwards-Compatible Enhancement** | Expands governance capabilities without breaking existing compliant builds. | - Adding a new `advisory` or `review` mode control.<br>- Introducing a new optional overlay (e.g., new sector overlay).<br>- Adding optional, backwards-compatible fields to schemas.<br>- Adding new reference mappings (e.g., ISO 42001 cross-walks).<br>- Releasing new reference plug-in templates or scripts. |
| **PATCH (vX.Y.Z)** | **Backwards-Compatible Defect Fix** | Non-semantic corrections and defect remediations. | - Correcting syntax errors or logic bugs in Policy-as-Code rules.<br>- Typo corrections in human-readable policy text.<br>- Updating documentation or external reference citations.<br>- Non-functional schema documentation and description updates. |

---

## 3. Prerelease & Draft State Designation

Until the Enterprise AI Safety & Governance Review Board formally approves the package, all artifacts carry a `-draft` or `-rc` prerelease tag.

- `v0.x.x-draft`: Development and iterative generation phase. Subject to change; intended for architectural review and sandbox prototyping.
- `v1.0.0-rc.X`: Release Candidate state submitted to the Governance Review Board.
- `v1.0.0`: The first officially approved enterprise baseline. All controls marked `APPROVED` and `ACTIVE`.

---

## 4. Overlay & Baseline Decoupling

To enable rapid compliance adaptation to changing laws (such as EU AI Act delegated acts or state-level AI mandates) without requiring an enterprise-wide baseline upgrade:

1. **Independent Overlay Versioning:** Each overlay in `overlays/` maintains an independent semantic version:
   ```yaml
   id: ORG-OVL-GEO-EU-001
   version: "1.3.0"
   baseline_compatibility: ">=1.0.0 <2.0.0"
   ```
2. **Compatibility Matrix:** An overlay declares its supported baseline version range using standard semver range expressions.
3. **Project Manifest Binding:** A consuming project explicitly pins both the baseline version and any applicable overlay versions in its `ai-project-manifest.yaml`.

---

## 5. Deprecation Lifecycle & Migration Windows

To protect active production projects from sudden breaking changes:

1. **Deprecation Notice Period:** Any control slated for modification or removal must be tagged as `DEPRECATED` in at least one MINOR release prior to removal in a MAJOR release.
2. **Grace Period:** A 90-day grace period is mandatory for project migration following the publication of a new MAJOR baseline release.
3. **Advisory Transition:** Controls scheduled to become `blocking` in the next MAJOR release are introduced as `advisory` in the preceding MINOR release, providing teams advance visibility of future gate failures.

---

## 6. Emergency Hotfix and Security Revocation Policy

In the event of a critical zero-day AI security vulnerability (e.g., active remote code execution via prompt injection) or an immediate statutory injunction:

1. The Governance Platform Architect and Chief Information Security Officer (CISO) may issue an **Emergency Out-of-Band Patch** (`vX.Y.Z+hotfix`).
2. Emergency runtime blocks are deployed via policy sidecars and admission controllers immediately, accompanied by an emergency notification broadcast to all registered AI System Owners.
3. A retroactive Architecture Review Board review must occur within 5 business days of any emergency intervention.
