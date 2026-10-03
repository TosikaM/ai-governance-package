# Antigravity AI Assistant Workspace Instructions & Context Loading

## Mandatory Action on Session Startup
Whenever this workspace is opened on any machine or by any user account, you MUST immediately review the master project context and chronological chat history file:
* **Master Context File:** [`PROJECT_CONTEXT_AND_CHAT_HISTORY.md`](file:///c:/ai-governance-package/PROJECT_CONTEXT_AND_CHAT_HISTORY.md)

---

## Core Project Mission & Architecture
This workspace contains the **Enterprise AI Governance Package** — an automated Policy-as-Code and CI/CD validation engine that plugs into any AI project to guarantee regulatory compliance, safety, and copyright clearance.

### Key Components
1. **16 Enterprise Policies:** [`baseline/policies/`](file:///c:/ai-governance-package/baseline/policies/) (`POL-SEC` for cybersecurity, `POL-IPR` for copyright/licensing, `POL-DAT` for data privacy, etc.).
2. **60 Baseline Controls:** [`baseline/controls/`](file:///c:/ai-governance-package/baseline/controls/) across 16 domains with ISO 42001, NIST AI RMF, and EU AI Act mappings.
3. **1-Minute Developer Kit:** [`project-kit/init.py`](file:///c:/ai-governance-package/project-kit/init.py) (auto-scaffolds `governance-cards/data-card.yaml` and `ai-project-manifest.yaml`).
4. **Automated PR & Code Gate:** [`plugins/pull-request/ai_code_review_gate.py`](file:///c:/ai-governance-package/plugins/pull-request/ai_code_review_gate.py) (blocks AGPL/GPL copyleft violations and unreviewed AI code).
5. **4 Autonomous Governance Agents:** [`agents/`](file:///c:/ai-governance-package/agents/) (Intake, Resolver, Enforcement, Monitoring).
6. **Multi-Industry Sample Projects:**
   * [`sample-ai-project/`](file:///c:/ai-governance-package/sample-ai-project/) (Baseline Customer Support AI)
   * [`sample-loan-approval-risk/`](file:///c:/ai-governance-package/sample-loan-approval-risk/) (Credit Underwriting - Demographic Disparity Failure & Fix)
   * [`sample-medical-triage-ai/`](file:///c:/ai-governance-package/sample-medical-triage-ai/) (Emergency Triage - Human Clinician Override Failure & Fix)
   * [`sample-financial-advisor/`](file:///c:/ai-governance-package/sample-financial-advisor/) (Wealth Management)
   * [`sample-hr-resume-screening/`](file:///c:/ai-governance-package/sample-hr-resume-screening/) (Recruiting Screener)
7. **Executive Management Presentation:** [`AI_Governance_Novice_Guide.html`](file:///c:/ai-governance-package/AI_Governance_Novice_Guide.html) (14-slide executive slide deck with PDF export, Dark/Light modes, and Q&A Appendix).

---

## User Interaction Guidelines & Tone
1. **Simple, Concise, and Precise:** The user values clean, plain-English answers without obtuse technical jargon.
2. **Always Link Files:** Always provide clickable links using github-style markdown `file:///` format with forward slashes.
3. **Continuous GitHub Sync:** Maintain synchronization with the remote repository:
   * Remote: `[Configured Enterprise Git Remote]`
   * Branch: `main`
