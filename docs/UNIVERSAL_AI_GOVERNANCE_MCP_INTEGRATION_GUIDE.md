# Universal AI Governance Integration Guide: MCP, Generative AI & Cloud Storage

> **Document Version:** v1.0.0-enterprise  
> **Applicability:** Desktop AI Tools, Cloud Generative AI, GitHub, SharePoint, Local Machines, AWS S3, and Google Drive.

---

## 1. Executive Summary & Compatibility Matrix

The **Enterprise AI Governance Package** provides a universal **Policy-as-Code** and **Automated Audit Engine** that can be plugged into **any Generative AI interface** and **any storage repository**.

Depending on the tool, connection is established via:
1. **Native MCP (Model Context Protocol):** Standard JSON-RPC over `stdio` (Claude Desktop, Cursor, Windsurf, VS Code).
2. **OpenAPI 3.0 REST Actions:** Direct HTTP API / Custom GPT Actions (ChatGPT Cloud, ChatGPT Desktop, Custom LLM APIs).
3. **Storage Mount / Sync Connectors:** Local file system mapping, CLI sync, or webhooks (GitHub, SharePoint, AWS S3, Google Drive).

### Compatibility Matrix

| Category | Platform / Tool | Protocol | Connection Method |
|---|---|---|---|
| **Desktop AI** | **Claude Desktop** | Native MCP (`stdio`) | Config file: `claude_desktop_config.json` |
| **Desktop AI** | **Cursor / Windsurf** | Native MCP (`stdio`) | Config file: `.cursor/mcp.json` |
| **Desktop AI** | **Codex / VS Code** | Native MCP (`stdio`) | Extension: VS Code MCP Settings |
| **Desktop AI** | **ChatGPT Desktop** | OpenAPI / Local HTTP | Custom GPT Action or local bridge |
| **Desktop AI** | **Perplexity Desktop** | API / Custom Context | Perplexity Pro Collections + Prompts |
| **Cloud AI** | **ChatGPT Cloud (GPT-4o)** | OpenAPI 3.0 REST | Custom GPT Action using `docs/openapi.yaml` |
| **Cloud AI** | **Claude Cloud (Claude.ai)** | Project Knowledge / API | Claude Projects with policy artifacts |
| **Cloud AI** | **Perplexity Cloud** | Custom Collection / API | Perplexity Pro Collection with schema files |
| **Storage / Repo** | **GitHub Repositories** | GitHub Action CI/CD | `uses: your-org/ai-governance-package@main` |
| **Storage / Repo** | **Local Workstations** | Native File System | Direct path (`C:\projects\...` or `/path/...`) |
| **Storage / Repo** | **SharePoint (M365)** | OneDrive Local Mount | Synced SharePoint Document Library path |
| **Storage / Repo** | **AWS S3 Buckets** | AWS CLI Sync / Lambda | Staging sync or S3 event webhook |
| **Storage / Repo** | **Google Drive** | Google Drive for Desktop | Virtual Drive mount (`G:\My Drive\...`) |

---

## 2. Desktop Generative AI Tools: Step-by-Step

### 2.1 Claude Desktop
Claude Desktop supports native MCP out of the box.

* **Configuration File Location:**
  * **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
    *(Full path: `C:\Users\<Username>\AppData\Roaming\Claude\claude_desktop_config.json`)*
  * **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

* **Configuration:**
  ```json
  {
    "mcpServers": {
      "ai-governance": {
        "command": "python",
        "args": [
          "C:\\ai-governance-package\\mcp_server.py"
        ]
      }
    }
  }
  ```

* **Usage in Claude Desktop:**
  1. Restart Claude Desktop.
  2. Look for the **Hammer (🔨) icon** in the bottom-right corner.
  3. Prompt Claude:
     > *"Claude, inspect the repository at `C:\projects\loan-app` and tell me what governance policies apply."*

---

### 2.2 Cursor Desktop & Windsurf
Both Cursor and Windsurf support native MCP servers for IDE-level autonomous coding.

* **Configuration:**
  Create or edit `.cursor/mcp.json` in your workspace or global settings:
  ```json
  {
    "mcpServers": {
      "ai-governance": {
        "command": "python",
        "args": ["C:\\ai-governance-package\\mcp_server.py"]
      }
    }
  }
  ```

* **Usage in Cursor / Windsurf:**
  In Composer or Chat (`Ctrl + L` / `Cmd + L`), ask:
  > *"@ai-governance audit this repository and check if there are any AGPL copyleft licenses or secret leaks before I commit."*

---

### 2.3 Codex Desktop / VS Code
For VS Code users running Copilot, Codex, or Gemini extensions:

* **Configuration:**
  Install the **Model Context Protocol** VS Code extension, then open `settings.json`:
  ```json
  {
    "mcp.servers": {
      "ai-governance": {
        "command": "python",
        "args": ["C:\\ai-governance-package\\mcp_server.py"]
      }
    }
  }
  ```

---

### 2.4 ChatGPT Desktop
ChatGPT Desktop connects to tools via Custom GPT Actions or a local HTTP bridge.

* **Step 1: Start the Governance HTTP Server:**
  ```bash
  python C:\ai-governance-package\mcp_server.py --transport http --port 3335
  ```
* **Step 2: Connect to ChatGPT Desktop:**
  Use the Custom GPT created in [Section 3.1](#31-chatgpt-cloud-custom-gpts--chatgpt-plusenterprise) (see below). Because ChatGPT Desktop syncs with your OpenAI cloud account, the Custom GPT will be immediately available in your ChatGPT Desktop sidebar!

---

### 2.5 Perplexity Desktop
Perplexity connects to custom domain knowledge via **Perplexity Pro Collections**:

1. Open Perplexity Desktop $\rightarrow$ Click **Library** $\rightarrow$ Click **Collections** $\rightarrow$ **New Collection**.
2. Name it: `Enterprise AI Governance Engine`.
3. Set the System Prompt:
   > *"You are the Enterprise AI Governance Officer. You enforce the 16 enterprise safety policies, evaluate risk tiers, and provide guidance on resolving disparate impact, clinician override, and copyleft violations adhering to ISO 42001 and NIST AI RMF."*
4. Upload [`baseline/policies/`](file:///c:/ai-governance-package/baseline/policies/) markdown documents.

---

## 3. Cloud Generative AI Platforms: Step-by-Step

### 3.1 ChatGPT Cloud (Custom GPTs / ChatGPT Plus/Enterprise)

You can create an official **Enterprise AI Governance GPT** in ChatGPT Cloud that directly invokes your package via REST Actions.

* **Step 1: Start or Host the Server:**
  Run the server locally (with a tunnel like Cloudflare Tunnel / ngrok) or host it on Google Cloud Run / AWS:
  ```bash
  python C:\ai-governance-package\mcp_server.py --transport http --port 3335
  ```
  *(Schema URL: `http://localhost:3335/openapi.yaml` or your public domain URL).*

* **Step 2: Create Custom GPT:**
  1. Open [chatgpt.com](https://chatgpt.com) $\rightarrow$ Click your profile $\rightarrow$ **My GPTs** $\rightarrow$ **Create a GPT**.
  2. Under the **Configure** tab:
     * **Name:** `Enterprise AI Governance Officer`
     * **Description:** `Autonomous compliance auditor, policy-as-code validator, and safety gate.`
     * **Instructions:**
       > *"You are the Enterprise AI Governance Officer. When users ask you to inspect, audit, or onboard an AI codebase, invoke your actions to scan code, evaluate policies, check copyleft licenses, and provide remediation."*
  3. Scroll down to **Actions** $\rightarrow$ Click **Create new action**.
  4. Under **Schema**, paste the contents of [`docs/openapi.yaml`](file:///c:/ai-governance-package/docs/openapi.yaml).
  5. Under **Authentication**, select **None** (for internal network) or **API Key**.
  6. Click **Save** $\rightarrow$ **Publish (Only to me or Enterprise Workspace)**.

* **Step 3: Using in ChatGPT:**
  Prompt ChatGPT:
  > *"Run an audit on the project located at `C:\ai-governance-package\sample-loan-approval-risk` and give me the compliance summary."*

---

### 3.2 Claude Cloud (Claude.ai Web & Projects)

For organizations using Claude Team or Claude Enterprise on the web:

* **Step 1: Create a Claude Project:**
  1. Go to [claude.ai](https://claude.ai) $\rightarrow$ Click **Projects** $\rightarrow$ **Create Project**.
  2. Name: `Enterprise AI Governance`.
  3. Description: `Autonomous Policy-as-Code evaluation and AI safety architecture.`

* **Step 2: Add Project Knowledge:**
  1. Upload the following key artifacts from your repository into Project Knowledge:
     * All 16 policy files from [`baseline/policies/`](file:///c:/ai-governance-package/baseline/policies/)
     * The master context: [`PROJECT_CONTEXT_AND_CHAT_HISTORY.md`](file:///c:/ai-governance-package/PROJECT_CONTEXT_AND_CHAT_HISTORY.md)
     * The master guide: [`AI_Governance_Novice_Guide.html`](file:///c:/ai-governance-package/AI_Governance_Novice_Guide.html)
  2. Set Custom Instructions:
     > *"You are the Enterprise AI Governance Lead. Help developers craft manifests, explain controls, resolve demographic disparity, and audit code diffs for AGPL/GPL copyleft violations."*

---

### 3.3 Custom Cloud LLM APIs (OpenAI Assistants, Anthropic API, Gemini API)

If you are developing internal bots using the OpenAI, Anthropic, or Gemini SDKs, you can expose the 7 governance tools directly as function declarations:

```python
import json
from agents.mcp_server import TOOLS, handle_inspect, handle_audit

# Example for OpenAI Function Calling
openai_tools = [
    {
        "type": "function",
        "function": {
            "name": t["name"],
            "description": t["description"],
            "parameters": t["inputSchema"]
        }
    }
    for t in TOOLS
]

# Dispatching tool calls when the model returns a tool_call
def execute_tool(name, args):
    if name == "ai_governance_inspect":
        return handle_inspect(args.get("target_dir", "."))
    elif name == "ai_governance_audit":
        return handle_audit(args.get("target_dir", "."))
```

---

## 4. Connecting to Storage & Code Repositories

### 4.1 GitHub Repositories (Cloud PR Workflows)

To enforce AI governance automatically across every pull request on GitHub:

1. In any target repository on GitHub, create `.github/workflows/ai-governance.yml`:
   ```yaml
   name: Enterprise AI Governance Gate

   on:
     push:
       branches: [main, master]
     pull_request:
       branches: [main, master]

   jobs:
     governance-scan:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout Code
           uses: actions/checkout@v4

         - name: Run Enterprise AI Governance Audit
           uses: your-org/ai-governance-package@main
           with:
             action: 'audit'
             target-dir: '.'
             fail-on-violation: 'true'
   ```
2. **What happens:** Every PR automatically scans for API keys, AGPL/GPL code, and compliance violations. Non-compliant PRs are blocked from merging.

---

### 4.2 SharePoint Repositories (Microsoft 365)

Many enterprises store AI training data, model documentation, and prompts in SharePoint document libraries.

#### Method A: Local Folder Sync via OneDrive (Recommended)
1. Open your SharePoint document library in your browser (e.g. `https://yourcompany.sharepoint.com/sites/AIData`).
2. Click the **Sync** button in the SharePoint top toolbar.
3. Windows OneDrive will sync the library locally to:
   ```
   C:\Users\<Username>\<YourCompany>\AIData
   ```
4. Now, simply pass that local path to Claude, Cursor, or MCP:
   > *"Claude, inspect the AI data repository in `C:\Users\<Username>\<YourCompany>\AIData` and verify its data cards."*

#### Method B: Automated Python Microsoft Graph Sync Script
To sync SharePoint folders programmatically in CI/CD pipelines before running audits:
```python
# scripts/sync_sharepoint.py
import os, requests

def sync_sharepoint_folder(site_id, drive_id, local_dest):
    token = os.environ.get("MS_GRAPH_TOKEN")
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root/children"
    # Downloads files to local_dest, then triggers GovernanceAgent(local_dest).audit()
```

---

### 4.3 Local Developer Workstations
Developers can govern any local project on their machine instantly:

1. **Option 1 (Interactive CLI Wizard):**
   ```bash
   cd C:\path\to\any-ai-project
   python C:\ai-governance-package\project-kit\init.py
   ```
2. **Option 2 (Autonomous Agent 1-Liner):**
   ```bash
   python C:\ai-governance-package\agents\governance_agent.py auto-setup C:\path\to\any-ai-project
   ```

---

### 4.4 AWS S3 Buckets

AI models and training datasets are frequently hosted in AWS S3 buckets (`s3://company-ai-models/`).

#### Method A: AWS CLI Staging Sync
Sync S3 contents to a local or CI staging directory, then audit:
```bash
# 1. Sync bucket to staging
aws s3 sync s3://company-ai-models/model-v1 ./staging-model

# 2. Run Governance Audit via Agent
python C:\ai-governance-package\agents\governance_agent.py audit ./staging-model
```

#### Method B: AWS EventBridge / Lambda Automation
Configure an S3 Object Created Event trigger that invokes an AWS Lambda function running the governance engine container whenever new model weights or datasets are uploaded.

---

### 4.5 Google Drive

For teams storing models and datasets in Google Drive:

#### Method A: Google Drive for Desktop (Virtual Drive Mount)
1. Install **Google Drive for Desktop**.
2. Google Drive will appear as a virtual drive letter on Windows (typically `G:\My Drive\` or `G:\Shared drives\<DriveName>`).
3. Point your MCP client or agent directly at the path:
   > *"Claude, audit the AI project at `G:\Shared drives\AI-Projects\Medical-Assistant`."*

#### Method B: Google Drive API Pipeline
In CI/CD environments, use the Google Drive API (`gspread` or `google-api-python-client`) with a service account to pull documents into a staging directory before running `ai_governance_audit`.

---

## 5. Summary of the 7 Autonomous Tools Exposed

| Tool Name | Key Function | Input Arguments |
|---|---|---|
| **`ai_governance_inspect`** | Discovers code frameworks, PII, external tool executions, and leaked API keys. Infers risk tier. | `target_dir` |
| **`ai_governance_auto_setup`** | Fully scaffolds manifest, Model Card, Data Card, pre-commit hooks, and CI/CD gates in < 60s. | `target_dir` |
| **`ai_governance_audit`** | Evaluates project against all 16 policies and produces an interactive standalone HTML report. | `target_dir`, `generate_html`, `output_filename` |
| **`ai_governance_check_pr`** | Scans code diffs for reciprocal copyleft licenses (`GPL-3.0`, `AGPL-3.0`) and hardcoded secrets. | `target_dir` |
| **`ai_governance_resolve`** | Deterministic policy snapshot resolver generating SHA-256 sealed snapshots. | `manifest_path`, `output_path` |
| **`ai_governance_list_policies`** | Queries all 16 enterprise baseline policies with regulatory mappings to EU AI Act and ISO 42001. | `policy_id` (optional) |
| **`ai_governance_explain_control`** | Returns step-by-step developer remediation guidance for any control ID. | `control_id` |

---

## 6. Verification Checklist

1. **Verify stdio MCP (Claude Desktop / Cursor):**
   ```bash
   python mcp_server.py
   ```
2. **Verify REST / HTTP Server (ChatGPT / Cloud):**
   ```bash
   python mcp_server.py --transport http --port 3335
   curl http://localhost:3335/health
   curl http://localhost:3335/openapi.json
   ```
3. **Verify GitHub Action Gate:**
   ```bash
   python agents/governance_agent.py audit sample-ai-project
   ```
