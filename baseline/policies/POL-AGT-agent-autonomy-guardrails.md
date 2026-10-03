# Enterprise Policy on Autonomous Agent Identity, Permissions, Autonomy Limits, and Action Guardrails

**Policy Identifier:** `ORG-POL-AGT-001`  
**Associated Principle:** `ORG-PRIN-AGT` (Agent Autonomy Boundaries & Verifiable Action)  
**Status:** DRAFT  
**Effective Version:** v0.1.0-draft  
**Owner Placeholder:** [ROLE: Principal Agent Architect & Head of Identity & Access Management]  
**Approver Placeholder:** [ROLE: Enterprise AI Safety & Governance Review Board]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Purpose & Scope

This policy establishes strict architectural boundaries, security guardrails, identity models, autonomy limits, and emergency kill switches for all autonomous agents, multi-agent frameworks, tool-calling systems, and Model Context Protocol (MCP) integrations operating across the enterprise.

This policy applies to any software system wherein a machine learning model autonomously generates plans, selects tools, formats API requests, or executes workflows across internal or external environments.

---

## 2. Normative Requirements

### 2.1 Outside-the-Model Authorization Boundary
1. **Model Is Never the Policy Engine:** Authorization and access control decisions **MUST BE ENFORCED OUTSIDE THE MODEL** by deterministic Policy Enforcement Points (PEPs), API gateways, or runtime sidecars.
2. **Prohibition of Self-Authorization:** A model's generated plan, internal chain-of-thought, or textual claim of supervisor approval **DOES NOT CONSTITUTE AUTHORIZATION**. No tool execution may proceed based solely on the model asserting that an action is permitted.

### 2.2 Dedicated Agent Identity & Least-Privilege Delegation
1. **Machine-Only Service Identity:** Every autonomous agent must execute under a dedicated, cryptographically verifiable non-human service identity (e.g., SPIFFE ID, OAuth2 service principal, or mTLS certificate). Agents **MUST NOT** impersonate human end-users or share generic service accounts.
2. **Dual-Subject Authorization:** When an agent acts on behalf of a human user, the PEP must evaluate permissions against both the user's entitlements AND the agent's scoped capabilities (intersection of rights).
3. **No Unbounded Transitive Delegation:** An agent **MUST NOT** delegate broad or unconstrained credentials to sub-agents. Child agents inherit strictly reduced, time-limited, and task-scoped tokens.

### 2.3 Strict Tool-Call Schema Validation
1. **Pre-Approved Tool Registry:** Agents may only invoke tools, plugins, and MCP servers registered in the enterprise agent registry adhering to `schemas/project-manifest.schema.json`.
2. **Strict Schema Interception:** Before dispatching an outgoing tool call, a runtime PEP must intercept the payload and validate all arguments against the tool's registered JSON schema. Permissive typing (`any`, `object` without properties) is prohibited for state-modifying tools.
3. **Destructive Tool Approvals:** Tools classified as `destructive_write_requires_approval` (e.g., database writes, financial transfers, code deployment) require an out-of-band cryptographic human approval token before execution.

### 2.4 Autonomy Limits & Loop Termination
1. **Maximum Execution Depth:** Autonomous agent execution chains must be constrained by hard execution caps (default parameter: `max_execution_steps = 10` [provisional; requires Principal Agent Architect approval]).
2. **Runaway Loop Detection:** Agent runtimes must incorporate cyclic call detection; repeating identical tool calls or oscillating between error states must terminate execution automatically.

### 2.5 Out-of-Band Kill Switch & Action Logging
1. **Instantaneous Kill Switch:** Every agent deployment must support an out-of-band kill switch capable of instantly invalidating credentials, revoking tokens, and terminating execution threads without relying on model cooperation.
2. **Immutable Action Audit Trails:** All proposed agent tool calls, evaluated arguments, PEP authorization decisions, and tool response payloads must be captured in immutable, tamper-evident logs.

---

## 3. Separation of Automated Checks and Human Judgment

| Requirement | Verification Mechanism | Check Type | Enforcement Point | Mode |
|---|---|---|---|---|
| Outgoing Tool Call JSON Schema Validation | Interceptor validating payload against registered tool schema | Automated | Agent Runtime Interceptor / PEP | Blocking |
| Loop Depth & Cyclic Call Threshold Cap | Runtime step counter and cycle detector sidecar | Automated | Agent Runtime / Gateway | Blocking |
| Kill Switch Execution Latency Verification | Automated integration test verifying token revocation in < 1s | Automated | CI/CD Integration Test | Blocking |
| Classification of Tool Destructiveness (Read vs Write) | Architectural review of tool capabilities and side effects | Human Judgment | Tool Registry Intake Gate | Review |
| Autonomy Scope Expansion Approval | Governance review of expanded agent execution boundaries | Human Judgment | AI Review Board Gate | Review |

---

## 4. Roles & Responsibilities

- **Agent Framework Engineers:** Implement outside-the-model PEP interceptors, schema validation hooks, and execution depth limits.
- **Identity & Access Management (IAM) Lead:** Issues and monitors dedicated agent service principals and scoped credential exchanges.
- **System Technical Lead:** Registers all agent tools with complete JSON schemas in `ai-project-manifest.yaml`.
- **Security Operations Center (SOC):** Holds operational authority to trigger emergency agent kill switches.

---

## 5. Non-Conformance & Exceptions

An autonomous agent operating without an external PEP or lacking an operational kill switch will be terminated and quarantined immediately. Exceptions must be documented under `ORG-EXC` and require CISO and AI Review Board approval. Internal exceptions cannot waive statutory liabilities.

---

## 6. Authoritative Reference Mappings

- **OWASP Top 10 for LLM Applications (2025):** LLM06:2025 (Excessive Agency), LLM07:2025 (System Information Leakage).
- **NIST AI RMF 1.0 / NIST AI 600-1 (GenAI Profile):** MANAGE 2.1, MANAGE 2.3 (Autonomous agent boundaries, fail-safe isolation).
- **ISO/IEC 42001:2023:** Annex A.8.4 (Control of autonomous actions and operational boundaries).
