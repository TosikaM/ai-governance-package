# Enterprise AI Governance: Model Context Protocol (MCP) Setup Guide

> **Purpose:**  
> This guide explains how to connect the **Enterprise AI Governance Package** as an **MCP (Model Context Protocol) Server** to **Claude Desktop**, **Claude Code**, **Cursor**, **Windsurf**, and any **cloud repository on GitHub**.

---

## 1. Overview: What This MCP Connector Does

By plugging this MCP server into Claude or your cloud CI/CD pipelines, your AI assistants gain autonomous capabilities to govern, verify, and remediate any AI project in real-time.

### The 7 Autonomous MCP Tools Exposed:
| Tool Name | What It Does | Arguments |
|---|---|---|
| `ai_governance_inspect` | Scans codebase, detects LLM/RAG/Agent frameworks, PII, tool executions, leaked secrets, and infers risk tier. | `target_dir` (default: `.`) |
| `ai_governance_auto_setup` | 1-minute autonomous setup: generates manifest, scaffolds Model & Data Cards, installs pre-commit & GitHub Action gates, and seals snapshot. | `target_dir` (default: `.`) |
| `ai_governance_audit` | Runs a complete compliance audit against Policy-as-Code rules, checks 7 pipeline barriers, and generates an interactive HTML report. | `target_dir`, `generate_html`, `output_filename` |
| `ai_governance_check_pr` | Scans code for reciprocal copyleft licenses (AGPL/GPL-3.0), hardcoded API credentials, and unreviewed AI code. | `target_dir` (default: `.`) |
| `ai_governance_resolve` | Deterministic policy resolver: merges baseline policies + overlays into `effective-policy-snapshot.json` with SHA-256 seal. | `manifest_path`, `output_path` |
| `ai_governance_list_policies` | Lists all 16 enterprise baseline policies (`POL-ACC` through `POL-USE`) with regulatory mappings, or retrieves full text. | `policy_id` (optional, e.g. `POL-SEC`) |
| `ai_governance_explain_control` | Returns plain-English remediation guidance and sample code for any control (e.g., `CTL-FAI-001` disparate impact). | `control_id` (required) |

---

## 2. Connecting with Claude Desktop ("Next App Installation of Claude")

When you install Claude Desktop on your machine, connect this governance engine in 3 simple steps:

### Step 1: Open the Claude Desktop Configuration File
* **On Windows:**
  Press `Win + R`, paste the path below, and press Enter:
  ```
  %APPDATA%\Claude\claude_desktop_config.json
  ```
  *(Full Path: `C:\Users\<YourUsername>\AppData\Roaming\Claude\claude_desktop_config.json`)*

* **On macOS:**
  ```
  ~/Library/Application Support/Claude/claude_desktop_config.json
  ```

### Step 2: Add the AI Governance MCP Server
Open the file in Notepad or VS Code and add the following JSON configuration:

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

*(Note for macOS / Linux users: replace `C:\\ai-governance-package\\mcp_server.py` with `/path/to/ai-governance-package/mcp_server.py`)*

### Step 3: Restart Claude Desktop
1. Completely close Claude Desktop (right-click tray icon and select **Quit**).
2. Re-open Claude Desktop.
3. Look at the bottom-right of the prompt bar: you will see a **Hammer (🔨) icon** showing `ai-governance` with 7 tools loaded!

---

## 3. Example Prompts to Use in Claude Desktop

Once connected, you can converse with Claude naturally. Claude will autonomously invoke the tools:

* **To Inspect Any Repo:**
  > *"Claude, inspect the AI project at `C:\projects\loan-app` and tell me what frameworks, PII, and risk tier you detect."*

* **To Onboard a New AI Project:**
  > *"Claude, run autonomous governance setup on `C:\projects\customer-chatbot`. Generate the manifest, data cards, and CI/CD gates."*

* **To Audit Compliance:**
  > *"Claude, audit `C:\projects\loan-app` against our enterprise policies and tell me if any controls are failing."*

* **To Check a Pull Request:**
  > *"Claude, check `C:\projects\loan-app` to make sure there are no AGPL/GPL copyleft violations or leaked API keys before I merge."*

* **To Understand a Policy or Control:**
  > *"Claude, explain control `CTL-FAI-001` and tell our developers how to fix demographic bias in credit underwriting models."*

---

## 4. Connecting with Claude Code (CLI)

If you use Anthropic's **Claude Code** terminal CLI:

```bash
claude mcp add ai-governance python C:\ai-governance-package\mcp_server.py
```

To verify:
```bash
claude mcp list
```

---

## 5. Connecting with Cloud Repositories (GitHub, Codespaces, CI/CD)

Once this package is pushed to your GitHub repository (`https://github.com/your-org/ai-governance-package.git`), any cloud repository can connect using **three methods**:

### Method A: Reusable GitHub Action (Zero-Install in Target Repos)
In any AI application repository on GitHub, create `.github/workflows/ai-governance.yml`:

```yaml
name: Enterprise AI Governance Gate

on:
  pull_request:
    branches: [main, master]
  push:
    branches: [main, master]

jobs:
  governance-verification:
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
* **What happens:** Every pull request automatically runs the governance gate. If an engineer leaks an API key, links copyleft GPL code, or lacks required data cards, the PR merge button is locked automatically.

---

### Method B: In GitHub Codespaces or Cloud Dev Containers
If your team develops inside GitHub Codespaces or VS Code Remote Containers:

Add to `.devcontainer/devcontainer.json`:
```json
{
  "postCreateCommand": "pip install git+https://github.com/your-org/ai-governance-package.git",
  "customizations": {
    "vscode": {
      "settings": {
        "mcpServers": {
          "ai-governance": {
            "command": "ai-governance-mcp"
          }
        }
      }
    }
  }
}
```

---

### Method C: Running as a Remote Cloud Microservice (HTTP/SSE)
You can deploy this MCP server as a containerized microservice on Google Cloud Run, AWS ECS, or Azure Container Apps:

```bash
# Start remote HTTP/SSE MCP server on port 3335
python mcp_server.py --transport sse --port 3335
```

Cloud health check endpoint:
```bash
curl http://localhost:3335/health
# Returns: {"status": "ok", "server": "enterprise-ai-governance-mcp"}
```

Remote clients (like Claude or Cursor) can connect via `mcp-remote`:
```json
{
  "mcpServers": {
    "ai-governance-remote": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://governance.internal.company.com:3335/"]
    }
  }
}
```

---

## 6. Testing & Verifying Your MCP Server Locally

You can test the server anytime using Python:

```bash
# Test initialization and list of tools
python -c "
import subprocess, json
proc = subprocess.Popen(['python', 'mcp_server.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
proc.stdin.write(json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize'}) + '\n')
proc.stdin.flush()
print(proc.stdout.readline())
proc.kill()
"
```
Output:
```json
{"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}, "resources": {}, "prompts": {}}, "serverInfo": {"name": "enterprise-ai-governance-mcp", "version": "0.1.0"}}}
```
