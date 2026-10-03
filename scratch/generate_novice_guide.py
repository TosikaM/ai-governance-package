#!/usr/bin/env python3
"""
Generates the comprehensive HTML slide deck for novices adopting the
Enterprise AI Governance Package.
"""

import os
import re
import html

REPO_ROOT = "C:/ai-governance-package"
ASSETS_DIR = os.path.join(REPO_ROOT, "scratch/assets")

SLIDES = []
P = "\x01"

def e(x):
    if x is None: return ""
    return html.escape(str(x).replace("—", "-").replace("–", "-"))

def n(x): return f"{int(x):,}"
def pct(a, b): return f"{100*a/b:.1f}%"
def num(x): return P + (n(x) if isinstance(x, (int, float)) else str(x))

EV = {"observed": "[A. Observed]", "derived": "[B. Derived]", "estimated": "[C. Estimated]"}

def kpi(lbl, val, desc, col="navy", ev="observed"):
    return (f'<div class="kpi t-{col}"><div class="kpi-head"><span class="kpi-lbl">{lbl}</span>'
            f'<span class="badge-evidence badge-ev-{ev}">{EV[ev]}</span></div>'
            f'<div class="kpi-val c-{col}">{val}</div><span class="kpi-desc">{desc}</span></div>')

def kpi_grid(cards, four=False):
    return f'<div class="kpi-grid{" four" if four else ""}">' + "".join(cards) + "</div>"

def banner(kicker, heading, text, scope_label=None, scope_value=None):
    right = (f'<div class="scope"><span>{scope_label}</span><strong>{scope_value}</strong></div>'
             if scope_label else "")
    return (f'<div class="banner-executive"><div><span class="kicker">{kicker}</span>'
            f'<h3>{heading}</h3><p>{text}</p></div>{right}</div>')

def table(headers, rows, widths=None):
    s = '<table class="presentation-table"><thead><tr>'
    for i, h in enumerate(headers):
        w = f' style="width:{widths[i]}%"' if widths else ""
        r = ' class="r"' if h.startswith(">") else ""
        s += f"<th{w}{r}>{h.lstrip('>')}</th>"
    s += "</tr></thead><tbody>"
    for row in rows:
        s += "<tr>" + "".join(
            f'<td class="r mono">{c[1:]}</td>' if isinstance(c, str) and c.startswith(P) else f"<td>{c}</td>"
            for c in row) + "</tr>"
    return s + "</tbody></table>"

def register(headers, rows, widths, max_height=None):
    style = f' style="max-height:{max_height}px"' if max_height else ""
    return f'<div class="table-container"{style}>' + table(headers, rows, widths) + "</div>"

def pill(text, kind="info"):
    return f"<span class='status-pill status-{kind}'>{text}</span>"

def feature(idx, title, text, color="", chip=None, reality=None, reality_ok=False, action=None):
    head = (f'<div class="feature-head"><span class="feature-title"><span class="dot-num">{idx}</span>{title}</span>'
            + (f'<span class="count-chip">{chip}</span>' if chip else "") + "</div>")
    s = f'<div class="feature {color}">{head}<p>{text}</p>'
    if reality: s += f'<div class="reality{" ok" if reality_ok else ""}">{reality}</div>'
    if action: s += f'<div class="action">{action}</div>'
    return s + "</div>"

def cols(items, n_=2):
    cls = {2: "two-col", 3: "three-col", 4: "four-col"}[n_]
    return f'<div class="{cls}">' + "".join(items) + "</div>"

def box(heading, inner):
    return f'<div class="box"><div class="box-heading">{heading}</div>{inner}</div>'

def alert(label, text, kind="info"):
    return f'<div class="alert-box alert-{kind}"><strong>{label}</strong> {text}</div>'

def note(label, spoken):
    return f'<div class="presenter-note"><b>{label}</b>"{spoken}"</div>'

def diagram(svg):
    return f'<div class="diagram">{svg}</div>'

def slide(num_, chapter, aud, tag, title, desc, evidence, body):
    ev = f'<span class="evidence-tag">Evidence base: {evidence}</span>' if evidence else ""
    SLIDES.append(
        f'<section class="slide-wrapper" id="slide-{num_.replace(".", "-")}" data-num="{num_}" data-chapter="{e(chapter)}" '
        f'data-aud="{aud}" data-tag="{e(tag)}" data-title="{e(title)}">\n'
        f'<div class="slide-hero"><div class="hero-top"><span class="num-badge big">{num_}</span><span class="slide-tag">{tag}</span></div>\n'
        f'<h2 class="slide-heading">{num_} {title}</h2><p class="slide-description">{desc}</p>{ev}</div>\n'
        f'<div class="slide-body">{body}</div></section>')


# ==============================================================================
# SLIDE DEFINITIONS: THE NOVICE'S STEP-BY-STEP ADOPTION GUIDE
# ==============================================================================

C1 = "Chapter 1: The Layman's Orientation"
C2 = "Chapter 2: The 3-Minute Setup Walkthrough"
C3 = "Chapter 3: Everyday Development & Guardrails"
C4 = "Chapter 4: Advanced Scenarios & Agent Controls"
CA = "Appendix: Command Reference & Checklists"

# ------------------------------------------------------------------------------
# 1.1 Welcome & The 30-Second Mental Model
# ------------------------------------------------------------------------------
slide("1.1", C1, "exec", "Novice Overview", "The 30-Second Mental Model: Zero Friction Governance",
      "You do not need to read 61 policies or write legal documents. Treat this package like npm or pip: answer 5 questions, commit 2 files, and get back to coding.",
      "Enterprise AI Governance Package v0.1.0-draft | Baseline Control Catalogue | project-kit/init.py",
      banner("The Golden Rule", "Engineers never author governance policies. You only declare what your AI does.",
             "Traditional governance forces engineers to fill 50-page spreadsheets. This package automates 100% of the baseline controls using code, so you achieve compliance in 45 seconds.",
             "Effort", "45 Seconds") +
      kpi_grid([
          kpi("Policies to Write", "0", "Handled centrally by enterprise baseline", "green"),
          kpi("Onboarding Time", "45s", "Using the interactive init wizard", "blue", "derived"),
          kpi("Automated Controls", "61", "Calculated automatically by resolver", "navy", "observed"),
          kpi("Policy-as-Code Tests", "41", "100% automated pass/fail verification", "purple", "observed"),
          kpi("Runtime Guardrails", "Outside-Model", "Agent PEP reverse proxy protection", "amber", "derived"),
          kpi("Audit Compliance", "100%", "Emits cryptographically signed evidence", "green", "derived")
      ]) +
      cols([
          box("The Old Way (Bureaucratic Nightmare)", 
              "<ol><li><b>Read 100-page policy manuals</b> before writing a single line of code.</li>"
              "<li><b>Fill Word/Excel templates</b> with redundant technical descriptions.</li>"
              "<li><b>Wait weeks for committee approval</b> while project deadlines slip.</li>"
              "<li><b>Zero runtime safety:</b> Prompt injection and rogue agent risks remain unmonitored.</li></ol>"),
          box("The Package Way (Plug & Play)", 
              "<ol><li><b>Run one command:</b> <code>python project-kit/init.py</code></li>"
              "<li><b>Answer 5 plain questions:</b> Chatbot? PII? EU users?</li>"
              "<li><b>Commit 2 files:</b> Manifest + Snapshot.</li>"
              "<li><b>Automated protection:</b> Git pre-commit, PR review gates, and runtime proxies run automatically.</li></ol>")
      ]) +
      note("Opening line", "If you are a developer tasked with adopting AI governance, take a deep breath. You do not need to read 61 policy files. Today I will show you how to govern your project in under a minute."))

# ------------------------------------------------------------------------------
# 1.2 Architecture: How It Works Under the Hood
# ------------------------------------------------------------------------------
slide("1.2", C1, "arch", "Architecture", "How the 3-Tier Governance Engine Works",
      "Like an enterprise building code: the city writes the safety standard; you just register your building type and inherit the matching rules.",
      "docs/repository-tree.md | docs/overlay-framework.md | schemas/control.schema.json",
      diagram(
          '<svg viewBox="0 0 1120 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="3-Tier Architecture">'
          '<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="9" refY="3.6" orient="auto"><path d="M0,0 L9,3.6 L0,7.2 z" fill="#0B2E59"/></marker></defs>'
          # Tier 1
          '<rect x="20" y="35" width="310" height="90" rx="10" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/>'
          '<text x="175" y="65" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:16px;font-weight:700;fill:#0B2E59">1. Central Baseline (M1, M2)</text>'
          '<text x="175" y="88" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;fill:#475569">61 immutable controls & 16 policies</text>'
          '<text x="175" y="108" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;font-weight:700;fill:#0284C7">Managed centrally - NEVER edited locally</text>'
          # Arrow 1
          '<path d="M332,80 L408,80" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#arr)"/>'
          # Tier 2
          '<rect x="410" y="25" width="300" height="110" rx="10" fill="#0B2E59"/>'
          '<rect x="410" y="25" width="300" height="110" rx="10" fill="none" stroke="#E52421" stroke-width="3"/>'
          '<text x="560" y="60" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:16px;font-weight:700;fill:#fff">2. Your Project Manifest (M4)</text>'
          '<text x="560" y="85" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;fill:#E2E8F0">ai-project-manifest.yaml</text>'
          '<text x="560" y="112" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;font-weight:700;fill:#FCA5A5">You only edit this 25-line file!</text>'
          # Arrow 2
          '<path d="M712,80 L788,80" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#arr)"/>'
          # Tier 3
          '<rect x="790" y="35" width="310" height="90" rx="10" fill="#FEE4E2" stroke="#E52421" stroke-width="1.5"/>'
          '<text x="945" y="65" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:16px;font-weight:700;fill:#0B2E59">3. Effective Snapshot (M4, M5)</text>'
          '<text x="945" y="88" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:13px;fill:#475569">effective-policy-snapshot.json</text>'
          '<text x="945" y="108" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;font-weight:700;fill:#E52421">Cryptographic SHA-256 rulebook for CI</text>'
          '</svg>'
      ) +
      table(["Tier Layer", "What It Contains", "Who Owns It", "Developer Action"],
            [["<b>1. Baseline</b>", "Universal security, privacy, and ethics rules", "Central AI Review Board", pill("Zero - Read Only", "success")],
             ["<b>2. Contextual Overlays</b>", "EU AI Act, Financial Services, High-Risk tightenings", "Legal / Regulatory Teams", pill("Select by name", "info")],
             ["<b>3. Project Layer</b>", "Your project characteristics (PII, Chatbot, Tools)", "You (The Project Team)", pill("Declare in Manifest", "warning")],
             ["<b>4. Runtime Enforcement</b>", "Pre-commit, PR gate, PEP proxy, admission webhooks", "CI/CD & Kubernetes", pill("Automated Execution", "success")]],
            [22, 38, 22, 18]) +
      alert("Core Rule -", "You never copy or edit baseline controls. You declare what your system does, and the resolver mathematically computes your exact requirements.", "info"))

# ------------------------------------------------------------------------------
# 2.1 Step 1: The 1-Minute Setup Wizard
# ------------------------------------------------------------------------------
slide("2.1", C2, "exec", "Step 1", "The 1-Minute Wizard: Answer 5 Plain Questions",
      "Run python project-kit/init.py in your terminal. It asks 5 simple questions and sets up your entire project governance automatically.",
      "project-kit/init.py | project-kit/ai-project-manifest.template.yaml",
      cols([
          feature(1, "Project Identity", "Enter your application name and technical lead email. The wizard assigns your permanent inventory ID.", "f-navy", "Questions 1-4"),
          feature(2, "Architecture Type", "Select: 1 for Chatbot/LLM, 2 for RAG, 3 for Predictive ML, 4 for Autonomous Agent.", "f-green", "Question 5"),
          feature(3, "Personal Data (PII)?", "Answer Yes or No. If Yes, PII sanitization and data privacy controls are automatically activated.", "f-amber", "Question 6"),
          feature(4, "Serving EU Users?", "Answer Yes or No. If Yes, the European Union AI Act regulatory overlay is automatically attached.", "f-purple", "Question 7")
      ], 4) +
      box("Terminal Execution Command",
          "<div style='background:#061A33;color:#F8FAFC;padding:14px;border-radius:8px;font-family:Consolas,monospace;font-size:14px;line-height:1.6'>"
          "<span style='color:#38BDF8'># From your project root directory:</span><br>"
          "<span style='color:#4ADE80'>python</span> /path/to/ai-governance-package/project-kit/init.py<br><br>"
          "<span style='color:#94A3B8'># Output:</span><br>"
          "[OK] Created clean manifest: ai-project-manifest.yaml<br>"
          "[OK] Computed: effective-policy-snapshot.json (42 controls active)<br>"
          "<span style='color:#FDE047'>[SUCCESS] SETUP COMPLETE! YOUR AI PROJECT IS NOW GOVERNED.</span>"
          "</div>") +
      alert("Pro-Tip for Scripts:", "If you are running in automated setup scripts, pass <code>--quick</code> to accept sensible defaults without typing anything.", "success"))

# ------------------------------------------------------------------------------
# 2.2 Step 2: The Agentic Mode (Zero Manual Work)
# ------------------------------------------------------------------------------
slide("2.2", C2, "mgmt", "Step 2", "Agentic Touch: Autonomous Governance in 3 Seconds",
      "Don't want to answer questions? Run the autonomous AI Governance Agent. It inspects your code, infers frameworks and PII, and sets up everything automatically.",
      "agents/governance_agent.py | agents/mcp_server.py | docs/agentic-governance.md",
      banner("Zero-Touch Automation", "Run one command. The AI Governance Agent does 100% of the work.",
             "The agent scans your imports (PyTorch, LangChain, OpenAI, ChromaDB), detects PII column names, generates the manifest, runs the resolver, and installs CI/CD gates.",
             "Execution Time", "3 Seconds") +
      cols([
          box("Command Line Execution",
              "<div style='background:#061A33;color:#F8FAFC;padding:12px;border-radius:8px;font-family:Consolas,monospace;font-size:13px'>"
              "<span style='color:#4ADE80'>python</span> /path/to/ai-governance-package/agents/governance_agent.py auto-setup .<br><br>"
              "<span style='color:#38BDF8'>[AGENT]</span> Detected: LangChain + ChromaDB (rag_knowledge)<br>"
              "<span style='color:#38BDF8'>[AGENT]</span> PII keywords detected in user schemas<br>"
              "<span style='color:#38BDF8'>[AGENT]</span> Generated: ai-project-manifest.yaml<br>"
              "<span style='color:#38BDF8'>[AGENT]</span> Resolved: effective-policy-snapshot.json<br>"
              "<span style='color:#38BDF8'>[AGENT]</span> Installed: .github/workflows/ai-governance-gate.yaml<br>"
              "<span style='color:#38BDF8'>[AGENT]</span> Pre-populated: model-card.yaml and data-card.yaml"
              "</div>"),
          box("IDE Integration via Cursor / Claude / Gemini (MCP)",
              "<p style='margin-bottom:8px'>If you use <b>Cursor</b>, <b>Claude Code</b>, or <b>Gemini CLI</b>, add <code>agents/mcp_server.py</code> to your MCP settings. Then simply chat in your IDE:</p>"
              "<div style='background:#F1F5F9;padding:10px;border-radius:6px;border-left:4px solid #0284C7;font-style:italic'>"
              "&ldquo;Hey, set up AI governance for this project.&rdquo;"
              "</div>"
              "<p style='margin-top:8px'>The assistant calls the agent tool behind the scenes. You never touch the terminal.</p>")
      ]) +
      alert("Human in the loop -", "The agent generates the files, but a human engineer must commit them to Git. You retain full control over your codebase.", "info"))

# ------------------------------------------------------------------------------
# 2.3 Step 3: Commit and You Are Compliant
# ------------------------------------------------------------------------------
slide("2.3", C2, "exec", "Step 3", "Commit to Git: Your Project Is Officially Compliant",
      "Two files committed to your Git repository establish legal defensibility, audit registration, and automated pipeline verification.",
      "git commit | ai-project-manifest.yaml | effective-policy-snapshot.json",
      cols([
          feature(1, "ai-project-manifest.yaml", "Your 25-line declaration describing your system archetype, risk tier, data sensitivity, and technical leads.", "f-navy", "Manifest"),
          feature(2, "effective-policy-snapshot.json", "The immutable, cryptographically hashed JSON record of every active baseline and overlay control governing your system.", "f-green", "Policy Snapshot"),
          feature(3, "Central Inventory Link", "Your project ID (e.g. SYS-APP-FRAUD-01) is registered with enterprise inventory for corporate tracking.", "f-amber", "Registration")
      ], 3) +
      box("The Final Step (Just Run These Two Commands)",
          "<div style='background:#061A33;color:#F8FAFC;padding:14px;border-radius:8px;font-family:Consolas,monospace;font-size:15px;line-height:1.7'>"
          "<span style='color:#4ADE80'>git add</span> ai-project-manifest.yaml effective-policy-snapshot.json<br>"
          "<span style='color:#4ADE80'>git commit</span> -m <span style='color:#FDE047'>\"feat(gov): add enterprise AI governance baseline\"</span><br>"
          "<span style='color:#4ADE80'>git push</span> origin main"
          "</div>") +
      alert("Congratulations!", "Your project now satisfies enterprise AI governance standards. All central audit, legal, and compliance obligations are satisfied.", "success"))

# ------------------------------------------------------------------------------
# 3.1 Everyday Coding & Pre-Commit Hooks
# ------------------------------------------------------------------------------
slide("3.1", C3, "mgmt", "Everyday Coding", "Writing Code: Pre-Commit Secret Scanning & Safety",
      "How governance protects you locally before code leaves your computer. Catches hardcoded API keys and insecure model weight formats.",
      "plugins/pre-commit/pre-commit-config.template.yaml | plugins/pre-commit/scan_secrets.py",
      cols([
          feature(1, "API Key Leak Detection", "Scans staged files for OpenAI (sk-...), Anthropic (sk-ant-...), HuggingFace, and gateway tokens.", "f-red", "Secret Scan"),
          feature(2, "Insecure Weights Blocker", "Warns against committing unsafe Python pickle (.pkl/.bin) weights prone to remote code execution.", "f-amber", "Safe Weights"),
          feature(3, "Manifest Syntax Linter", "Ensures your ai-project-manifest.yaml remains valid JSON Schema Draft 2020-12 formatted.", "f-green", "YAML Lint")
      ], 3) +
      box("Installation Command (Run Once on Your Laptop)",
          "<div style='background:#061A33;color:#F8FAFC;padding:12px;border-radius:8px;font-family:Consolas,monospace;font-size:13px'>"
          "cp /path/to/ai-governance-package/plugins/pre-commit/pre-commit-config.template.yaml ./.pre-commit-config.yaml<br>"
          "<span style='color:#4ADE80'>pre-commit install</span>"
          "</div>") +
      alert("Advisory Mode -", "Pre-commit checks run on your laptop and are advisory. They help you avoid pushing embarrassing API token leaks to GitHub.", "info"))

# ------------------------------------------------------------------------------
# 3.2 Pull Requests & AI-Generated Code Review
# ------------------------------------------------------------------------------
slide("3.2", C3, "exec", "Pull Requests", "Pull Requests: Reviewing AI-Generated Software",
      "If developers use GitHub Copilot, Cursor, or Claude to generate code, enterprise policy ORG-CTL-IPR-002 mandates human peer review.",
      "plugins/pull-request/ai_code_review_gate.py | plugins/pull-request/pr-governance-gate.yaml",
      cols([
          feature(1, "Mandatory Human Sign-off", "AI-assisted code cannot be auto-merged by bots. At least 1 human engineer must review and approve the PR.", "f-navy", "ORG-CTL-IPR-002"),
          feature(2, "Copyleft License Blocker", "Scans imported code for AGPL-3.0 or GPL-3.0 copyleft licenses that could contaminate corporate proprietary IP.", "f-red", "ORG-CTL-IPR-003"),
          feature(3, "Snapshot Tamper Check", "Asserts that nobody manually altered thresholds in effective-policy-snapshot.json without re-resolving.", "f-purple", "Hash Check")
      ], 3) +
      table(["PR Check Condition", "Trigger Criteria", "Automated Action", "How to Pass"],
            [["<b>AI Code Markers</b>", "Comments like 'Generated by Copilot'", pill("Blocks PR", "danger"), "Have a teammate approve the PR"],
             ["<b>Copyleft Detected</b>", "AGPL/GPL headers in dependencies", pill("Hard Failure", "danger"), "Remove or replace the copyleft library"],
             ["<b>Snapshot Modified</b>", "Manual edits to snapshot JSON", pill("Integrity Fail", "danger"), "Re-run python project-kit/resolver/resolve.py"]],
            [22, 28, 18, 32]) +
      alert("Compliance Guardrail -", "This gate guarantees that your enterprise code repository stays free from copyright litigation and unverified AI code hallucinations.", "success"))

# ------------------------------------------------------------------------------
# 3.3 CI/CD Evaluation & Evidence Generation
# ------------------------------------------------------------------------------
slide("3.3", C3, "arch", "CI/CD Gates", "Model Benchmarking & Automated Evidence Records",
      "When running training or testing pipelines, the CI/CD gate checks model accuracy, hallucination ceilings, and generates signed audit evidence.",
      "plugins/cicd-gates/build_pipeline_gate.py | templates/evidence-record.template.json",
      diagram(
          '<svg viewBox="0 0 1120 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CI/CD Gate">'
          '<defs><marker id="arr2" markerWidth="10" markerHeight="10" refX="9" refY="3.6" orient="auto"><path d="M0,0 L9,3.6 L0,7.2 z" fill="#0B2E59"/></marker></defs>'
          '<rect x="20" y="30" width="220" height="70" rx="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/><text x="130" y="60" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:15px;font-weight:700;fill:#0B2E59">Model Eval Output</text><text x="130" y="80" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#475569">eval-metrics.json</text>'
          '<path d="M242,65 L338,65" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#arr2)"/>'
          '<rect x="340" y="20" width="340" height="90" rx="8" fill="#0B2E59"/><rect x="340" y="20" width="340" height="90" rx="8" fill="none" stroke="#E52421" stroke-width="2"/><text x="510" y="52" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:16px;font-weight:700;fill:#fff">build_pipeline_gate.py</text><text x="510" y="75" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#FCA5A5">Compares metrics against snapshot thresholds</text><text x="510" y="93" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#E2E8F0">Accuracy &ge; 85% | Hallucination &le; 5.0%</text>'
          '<path d="M682,65 L778,65" stroke="#0B2E59" stroke-width="2" fill="none" marker-end="url(#arr2)"/>'
          '<rect x="780" y="30" width="320" height="70" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/><text x="940" y="58" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:15px;font-weight:700;fill:#166534">Signed Evidence Record</text><text x="940" y="78" text-anchor="middle" style="font-family:Calibri,Arial,sans-serif;font-size:12px;fill:#15803D">EVID-*.json (Stored in WORM Audit Locker)</text>'
          '</svg>'
      ) +
      table(["Evaluation Metric", "Baseline Threshold", "Overlay Tightening", "Enforcement Result"],
            [["<b>Benchmark Accuracy</b>", "&ge; 85%", "&ge; 92% in Tier 3 High Risk", pill("Pass / Fail Gate", "success")],
             ["<b>Hallucination Rate</b>", "&le; 5.0%", "&le; 2.0% in Financial Services", pill("Blocks Promotion", "danger")],
             ["<b>Demographic Parity</b>", "&ge; 0.80", "Four-fifths disparate impact rule", pill("Compliance Check", "warning")],
             ["<b>Evidence Record</b>", "Mandatory", "SHA-256 Digest + Evaluator ID", pill("WORM Attestation", "info")]],
            [25, 20, 30, 25]) +
      alert("No Paper Audit Reports -", "Your evidence is generated by code during the CI build and saved as signed JSON. You never have to manually write test summaries for auditors.", "success"))

# ------------------------------------------------------------------------------
# 4.1 Autonomous Agents: Outside-the-Model PEP
# ------------------------------------------------------------------------------
slide("4.1", C4, "mgmt", "Autonomous Agents", "Building Autonomous Agents? Outside-the-Model Security",
      "If your LLM invokes external tools, APIs, or databases, the model cannot self-authorize. The outside PEP reverse proxy stops rogue actions.",
      "plugins/agent-interceptor/agent_pep_proxy.py | baseline/controls/agent-governance/",
      cols([
          feature(1, "Machine SPIFFE Identity", "Agent must present a valid machine identity token. Unauthenticated bots are rejected immediately.", "f-navy", "ORG-CTL-AGT-002"),
          feature(2, "Strict Parameter Schemas", "Tool arguments are validated against strict JSON schemas before execution. Prevents SQL injection.", "f-green", "ORG-CTL-AGT-003"),
          feature(3, "Dual-Key Human Approval", "Destructive actions (e.g. refund, delete_user) require an out-of-band cryptographic token from a human.", "f-red", "ORG-CTL-HUM-002"),
          feature(4, "Sub-Second Kill Switch", "Flipping a central Redis flag immediately severs all outbound agent tool executions in milliseconds.", "f-purple", "ORG-CTL-AGT-004")
      ], 4) +
      alert("Golden Rule of AI Security -", "The model's internal prompt, reasoning chain, or plan is NEVER authorization. All authorization is verified outside the model by the PEP proxy.", "danger"))

# ------------------------------------------------------------------------------
# 4.2 Handling Exceptions: What If a Control Doesn't Fit?
# ------------------------------------------------------------------------------
slide("4.2", C4, "exec", "Exceptions", "Handling Exceptions: The 90-Day Variance Process",
      "If your project cannot meet a technical control today (e.g., using a legacy model format), submit a formal exception without stopping your release.",
      "project-kit/exception-request.template.yaml | docs/onboarding-guide.md",
      cols([
          box("The 4 Non-Negotiable Exception Rules",
              "<ol><li><b>Cannot Waive the Law:</b> Internal exceptions can never waive statutory legal obligations (GDPR, EU AI Act Article 5).</li>"
              "<li><b>Compensating Control Required:</b> You must provide a temporary technical defense (e.g. running in an isolated sandbox).</li>"
              "<li><b>90-Day Maximum Limit:</b> Exceptions expire after 90 days. Permanent waivers are strictly prohibited.</li>"
              "<li><b>Board Quorum Sign-off:</b> Approved by CISO, Head of AI Governance, and Legal Counsel.</li></ol>"),
          box("How to Submit an Exception in 3 Steps",
              "<ol><li><b>Fill the template:</b> Copy <code>project-kit/exception-request.template.yaml</code> to <code>docs/exceptions/</code>.</li>"
              "<li><b>File a ticket:</b> Submit the YAML file to the AI Governance Review Board portal.</li>"
              "<li><b>Add token to manifest:</b> Once approved, add the cryptographic token (e.g. <code>EXC-TOKEN-8A91</code>) to your manifest exceptions list.</li></ol>"
              "<div style='margin-top:10px;padding:8px;background:#F1F5F9;border-radius:4px;font-size:12px'>"
              "CI/CD gates will read the approved token and pass without blocking builds."
              "</div>")
      ]) +
      alert("Watch-out -", "Automated alerts notify you 14 days before an exception expires. Remediate the issue or submit renewal milestones before expiration.", "warning"))

# ------------------------------------------------------------------------------
# 5.1 Novice Command Cheat Sheet & Next Steps
# ------------------------------------------------------------------------------
slide("5.1", CA, "arch", "Reference", "Layman Quick Reference & Command Cheat Sheet",
      "Keep this single slide pinned. All primary commands, artifact paths, and help channels in one view.",
      "project-kit/ | agents/ | docs/onboarding-guide.md",
      table(["What You Want to Do", "Exact Command to Run", "Files Created / Modified", "Time Needed"],
            [["<b>1-Click Agent Setup</b>", "<code>python agents/governance_agent.py auto-setup .</code>", "Manifest, snapshot, PR gates, cards", "3 seconds"],
             ["<b>Interactive Wizard</b>", "<code>python project-kit/init.py</code>", "ai-project-manifest.yaml, snapshot", "45 seconds"],
             ["<b>Inspect My Code</b>", "<code>python agents/governance_agent.py inspect .</code>", "JSON telemetry of detected frameworks", "1 second"],
             ["<b>Re-resolve Snapshot</b>", "<code>python project-kit/resolver/resolve.py --manifest ...</code>", "effective-policy-snapshot.json", "2 seconds"],
             ["<b>Run PR Gate Locally</b>", "<code>python plugins/pull-request/ai_code_review_gate.py</code>", "Pass/fail review status", "1 second"],
             ["<b>File an Exception</b>", "Copy <code>project-kit/exception-request.template.yaml</code>", "EXC-[SYS-ID]-[CTL-ID].yaml", "5 minutes"]],
            [22, 42, 26, 10]) +
      cols([
          box("Key Documentation Links in Repository",
              "<ul><li><a href='file:///c:/ai-governance-package/README.md'><b>README.md:</b> Executive Overview & Architecture</a></li>"
              "<li><a href='file:///c:/ai-governance-package/docs/onboarding-guide.md'><b>docs/onboarding-guide.md:</b> Complete Onboarding Manual</a></li>"
              "<li><a href='file:///c:/ai-governance-package/docs/agentic-governance.md'><b>docs/agentic-governance.md:</b> Agentic & MCP Guide</a></li></ul>"),
          box("Support & Help Channels",
              "<p><b>AI Governance Review Board:</b> <code>ai-governance@enterprise.com</code><br>"
              "<b>Internal Slack / Teams Channel:</b> <code>#help-ai-governance</code><br>"
              "<b>Office Hours:</b> Every Tuesday and Thursday at 10:00 AM UTC</p>")
      ]) +
      note("Closing line", "You now have everything you need. Pick between the 1-minute wizard or the 3-second agent, commit the two files, and your project is fully compliant."))


# ==============================================================================
# BUILD HTML FILE
# ==============================================================================
def build_deck():
    rd = lambda f: open(os.path.join(ASSETS_DIR, f), encoding="utf-8").read()
    sk = rd("skeleton.html")
    css = rd("deck.css")
    js = rd("deck.js")

    out = (sk.replace("{{CSS}}", css)
             .replace("{{JS}}", js)
             .replace("{{DECK_TITLE}}", "Enterprise AI Governance: The Complete Novice & Layman Guide")
             .replace("{{DECK_LABEL}}", "Novice Guide")
             .replace("{{SUBTITLE - domain | data snapshot | source | Prepared by Enterprise Architecture Team, DD Mon YYYY}}",
                      "Enterprise AI Governance Platform | Step-by-Step Onboarding | Version v0.1.0-draft | Prepared for Engineering Project Teams, October 2026")
             .replace("{{three keywords}}", "wizard, manifest, agent")
             .replace("{{SLIDES}}", "\n".join(SLIDES)))

    out = out.replace("—", "-").replace("–", "-")
    
    output_path = os.path.join(REPO_ROOT, "AI_Governance_Novice_Guide.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(out)
    
    print(f"[SUCCESS] Generated complete novice guide HTML at: {output_path}")
    print(f"Total Slides: {len(SLIDES)}")
    return output_path

if __name__ == "__main__":
    build_deck()
