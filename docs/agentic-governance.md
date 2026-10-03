# Enterprise AI Governance: Autonomous Agentic Governance Guide

**Document Identifier:** `ORG-DOC-AGENTIC-001`  
**Status:** DRAFT  
**Baseline Version:** `v0.1.0-draft`  
**Owner Placeholder:** [ROLE: AI Governance Automation Architect]  
**Last Review Date:** [YYYY-MM-DD]  
**Next Review Date:** [YYYY-MM-DD]  

---

## 1. Vision: Zero-Touch, Agentic Governance

Traditional governance fails because it demands repetitive manual toil from software engineers and data scientists. 

The **Autonomous Governance Copilot** flips this dynamic: instead of forcing humans to read 61 controls, answer checklists, or manually draft YAML files, an intelligent agent **autonomously inspects the repository, infers characteristics, resolves policy snapshots, configures CI/CD barriers, and drafts documentation cards in seconds.**

```
+---------------------------------------------------------------------------------------------------+
|                               AUTONOMOUS GOVERNANCE AGENT WORKFLOW                                |
+---------------------+     +--------------------+     +-------------------+     +------------------+
| 1. Code Inspection  | --> | 2. Auto-Manifest   | --> | 3. Policy Snapshot| --> | 4. Auto-Gate &   |
|    (AST & Imports)  |     |    Generation      |     |    Resolution     |     |    Card Drafting |
+---------------------+     +--------------------+     +-------------------+     +------------------+
         |                            |                          |                         |
   Scans PyTorch,              Creates clean              Executes resolve.py        Installs CI PR
   LangChain, Chroma,          ai-project-                computes SHA-256           workflow & drafts
   PII keywords, tools         manifest.yaml              integrity hash             model/data cards
```

---

## 2. Using the Autonomous Governance Agent (`governance_agent.py`)

The primary CLI agent is located at [`agents/governance_agent.py`](file:///c:/ai-governance-package/agents/governance_agent.py). It runs standalone in pure Python without requiring heavyweight cloud dependencies or API keys.

### 2.1 The One-Command Autonomous Setup (`auto-setup`)
When a developer runs this command in any AI project repository:

```bash
python /path/to/ai-governance-package/agents/governance_agent.py auto-setup .
```

The agent executes the entire governance lifecycle autonomously:
1. **Codebase Scanning:** Inspects `requirements.txt`, `pyproject.toml`, `package.json`, and all Python/TypeScript files.
2. **Framework Detection:** Detects whether you are using LangChain, CrewAI, AutoGen, LlamaIndex, OpenAI, Hugging Face, PyTorch, or Scikit-Learn.
3. **Trait Inference:** Checks for personal data (PII keywords) and external tool executions (`subprocess`, SQL queries, API mutations).
4. **Manifest Generation:** Creates an exact, tailored [`ai-project-manifest.yaml`](file:///c:/ai-governance-package/project-kit/ai-project-manifest.template.yaml) with correct archetype and risk tier.
5. **Snapshot Resolution:** Runs the deterministic resolver and creates `effective-policy-snapshot.json`.
6. **Pipeline Gate Installation:** Copies `.pre-commit-config.yaml` and adds `.github/workflows/ai-governance-gate.yaml`.
7. **Card Synthesis:** Pre-populates starter `governance-cards/model-card.yaml` and `governance-cards/data-card.yaml`.

**Result:** The engineer simply runs `git add . && git commit -m 'feat: add AI governance'` and returns to coding. **Time elapsed: ~3 seconds.**

### 2.2 Inspection Mode (`inspect`)
To see what the agent detects about a repository without making changes:

```bash
python /path/to/ai-governance-package/agents/governance_agent.py inspect .
```

Outputs structured JSON describing inferred telemetry:
```json
{
  "archetype": "rag_knowledge",
  "risk_tier": "tier_2_moderate",
  "telemetry": {
    "frameworks": ["openai", "langchain", "chromadb"],
    "has_pii": true,
    "has_tools": false,
    "has_rag": true,
    "scanned_files": 42
  }
}
```

---

## 3. IDE Integration via Model Context Protocol (MCP)

For developers using **Cursor, Claude Code, Gemini CLI, or VS Code**, the package provides a native **MCP Server** at [`agents/mcp_server.py`](file:///c:/ai-governance-package/agents/mcp_server.py).

### How to Configure MCP in Your IDE

Add the server to your IDE's MCP configuration (e.g., `claude_desktop_config.json` or Cursor Settings):

```json
{
  "mcpServers": {
    "ai-governance": {
      "command": "python",
      "args": [
        "c:/ai-governance-package/agents/mcp_server.py"
      ]
    }
  }
}
```

### The Developer Experience in Chat / IDE

Once configured, the developer doesn't even need to open a terminal. They simply type in their IDE chat window:

> **Developer:** *"Hey, set up enterprise AI governance for this project."*  
> **Coding Assistant:** *Calls MCP tool `ai_governance_auto_setup`.*  
> **Coding Assistant:** *"I scanned your repository. You are building a RAG application using LangChain and ChromaDB with PII handling. I have automatically generated your project manifest, resolved the 42 applicable controls into `effective-policy-snapshot.json`, installed pre-commit secret scanning, and configured your GitHub Actions CI gate. Ready to commit!"*

---

## 4. Human-in-the-Loop Governance Safeguards

Even with full agentic automation, the platform enforces strict human accountability invariants:
1. **Agent Proposes, Human Commits:** The agent generates files in the developer's working tree; the developer or technical lead must commit them to Git.
2. **Review Board Ratification:** For Tier 3 High-Risk systems (e.g. credit decisions, biometrics), automated manifest generation sets risk tier to High, automatically requiring human review board sign-off prior to production cluster admission.
3. **Outside-the-Model Enforcement:** Autonomous agents running inside applications can never self-authorize; their actions remain strictly bounded by outside-the-model PEP proxies ([`plugins/agent-interceptor/agent_pep_proxy.py`](file:///c:/ai-governance-package/plugins/agent-interceptor/agent_pep_proxy.py)).

---
*Enterprise AI Governance Platform &bull; Baseline Version v0.1.0-draft &bull; Status: DRAFT*
