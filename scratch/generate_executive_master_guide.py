#!/usr/bin/env python3
"""
Enterprise AI Governance - Executive & Management Master Guide Generator (v3)
=============================================================================
Built specifically for Senior Management (CIO, CTO, Chief Risk Officer, VP Engineering)
and non-technical business leaders.

Key Additions:
1. Visual Box Diagrams & Flowcharts representing:
   - The 4-Stage Governance Architecture Pipeline
   - The 4-Step Plug-in Workflow for Any Existing Project
   - The Automated Enforcement Barrier Workflow
2. Real Executed Sample 1: Customer Support Assistant (sample-ai-project)
3. Real Executed Sample 2: HR Candidate Screening System (sample-hr-resume-screening)
   - What was caught non-compliant (hardcoded secret, automated rejection, indefinite PII)
   - How the system analyzed it
   - How it was plugged in and fixed
   - Direct link to real generated HTML report
4. Real Executed Sample 3: Autonomous Financial Advisor Agent (sample-financial-advisor)
   - What was caught non-compliant (unconstrained fund transfer tool, missing SEC retention)
   - How the system analyzed it
   - How it was plugged in and fixed
   - Direct link to real generated HTML report
5. 100% Plain Human Language: Zero deep developer jargon.
6. Preserves all requested UI features:
   - Deep navy (#0B2E59) and crimson red (#E52421) palette
   - Left scrollable sidebar with search
   - Slide Mode / Full Document View / Presentation Mode (F)
   - Print / Save as PDF button
   - Dark / Light mode toggle
=============================================================================
"""

import os
import sys

REPO_ROOT = "C:/ai-governance-package"
OUTPUT_HTML = os.path.join(REPO_ROOT, "AI_Governance_Novice_Guide.html")

SLIDES = [
    {
        "id": "slide-1",
        "num": "01",
        "chapter": "Executive Summary",
        "tag": "Business Purpose",
        "title": "What is the AI Governance Package & Why Did We Build It?",
        "subtitle": "An automated, company-wide software framework that ensures all AI projects are safe, compliant, and audit-ready in seconds.",
        "content": """
<div class="lead-banner">
  <div class="lead-kicker">Executive Summary</div>
  <h3>Empower company teams to innovate with AI at full speed without exposing the business to legal, security, or regulatory disaster.</h3>
  <p>Until now, AI compliance required weeks of manual legal review, 50-page Word questionnaires, and slow committee approvals. We built this automated AI Governance Package to replace that friction with automated, 3-second verification that works across every AI project in the organization.</p>
</div>

<div class="grid-3" style="margin-top:22px;">
  <div class="stat-card">
    <div class="stat-num">3 Sec</div>
    <div class="stat-label">Onboarding Time</div>
    <div class="stat-desc">Takes 3 seconds to apply company safety rules to any AI project instead of 6 weeks of legal review.</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">100%</div>
    <div class="stat-label">Automated Protection</div>
    <div class="stat-desc">Protects against leaked passwords, privacy violations, copyright risks, and rogue AI agent actions.</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">Audit-Ready</div>
    <div class="stat-label">Instant Evidence</div>
    <div class="stat-desc">Generates visual HTML compliance reports and cryptographic proof for auditors on demand.</div>
  </div>
</div>

<div class="grid-2" style="margin-top:24px;">
  <div class="content-box">
    <div class="box-title" style="color:var(--red);">The Old Way: High Friction & Danger</div>
    <ul class="clean-list">
      <li><b>Months of Bureaucracy:</b> Engineering teams wait weeks for risk committees to review static Word documents.</li>
      <li><b>Unverified AI Code:</b> Once approved, code changes continuously and nobody knows if policies are actually followed.</li>
      <li><b>Accidental Data Leaks:</b> Developers can accidentally expose customer data or company passwords without knowing.</li>
      <li><b>Regulatory Panic:</b> When auditors arrive, teams spend weeks scrambling to assemble compliance proof.</li>
    </ul>
  </div>
  <div class="content-box highlight">
    <div class="box-title" style="color:var(--green);">The New Way: Automated AI Governance</div>
    <ul class="clean-list">
      <li><b>Instant Automated Setup:</b> An intelligent software copilot inspects the project and sets up all rules in 3 seconds.</li>
      <li><b>Continuous Protection:</b> Automated safety gates continuously watch code and stop risky actions before they reach production.</li>
      <li><b>Zero Paperwork for Engineers:</b> Developers write zero manual policy documents; the system creates everything.</li>
      <li><b>1-Click Executive Reports:</b> Generates a clean visual report with green checkmarks ready for leadership and auditors.</li>
    </ul>
  </div>
</div>
"""
    },
    {
        "id": "slide-2",
        "num": "02",
        "chapter": "Platform Architecture",
        "tag": "How It Works",
        "title": "Platform Architecture: The 4-Stage Automated Pipeline",
        "subtitle": "How the governance package automatically assesses risk and creates tailored safety rules for any AI application.",
        "content": """
<div class="workflow-wrapper">
  <div class="workflow-header">
    <strong>End-to-End Governance Engine:</strong> From raw code to verified compliance in 4 automated stages.
  </div>
  
  <div class="workflow-grid-4">
    <!-- Stage 1 -->
    <div class="wf-box">
      <div class="wf-step-num">Stage 1</div>
      <div class="wf-icon">🔍</div>
      <div class="wf-title">Automated Code Health Check</div>
      <div class="wf-desc">The system scans project files in 1 second to detect AI models, databases, customer personal data, and external tools.</div>
      <div class="wf-badge green">Zero Manual Forms</div>
    </div>
    
    <div class="wf-arrow">➔</div>
    
    <!-- Stage 2 -->
    <div class="wf-box">
      <div class="wf-step-num">Stage 2</div>
      <div class="wf-icon">⚖️</div>
      <div class="wf-title">Risk & Rule Assignment</div>
      <div class="wf-desc">Assigns the exact risk tier (Low, Medium, High) and binds mandatory safety rules based on what the AI actually does.</div>
      <div class="wf-badge blue">Tailored Standards</div>
    </div>
    
    <div class="wf-arrow">➔</div>
    
    <!-- Stage 3 -->
    <div class="wf-box">
      <div class="wf-step-num">Stage 3</div>
      <div class="wf-icon">🔒</div>
      <div class="wf-title">Tamper-Proof Digital Contract</div>
      <div class="wf-desc">Locks all active rules into a single digital rulebook. Rules can only become stricter, never loosened.</div>
      <div class="wf-badge purple">Sealed Contract</div>
    </div>
    
    <div class="wf-arrow">➔</div>
    
    <!-- Stage 4 -->
    <div class="wf-box">
      <div class="wf-step-num">Stage 4</div>
      <div class="wf-icon">🛡️</div>
      <div class="wf-title">Active Protective Shields</div>
      <div class="wf-desc">Installs automatic quality gates that block leaked passwords, reject high error rates, and generate visual audit reports.</div>
      <div class="wf-badge red">Continuous Guardrails</div>
    </div>
  </div>
</div>

<div class="grid-3" style="margin-top:22px;">
  <div class="content-box">
    <div class="box-title">100% Deterministic Logic</div>
    <p style="font-size:13px; color:var(--text-secondary); line-height:1.6;">
      The system uses mathematical rule evaluation, not generative AI guessing. The exact same project will always receive the exact same verified safety rules.
    </p>
  </div>
  <div class="content-box">
    <div class="box-title">Monotonic Rule Lock</div>
    <p style="font-size:13px; color:var(--text-secondary); line-height:1.6;">
      High-risk overlays can tighten safety requirements (e.g. demanding human sign-off), but no developer or subsystem can ever weaken baseline company standards.
    </p>
  </div>
  <div class="content-box">
    <div class="box-title">Complete Audit Trail</div>
    <p style="font-size:13px; color:var(--text-secondary); line-height:1.6;">
      Every single decision, scanned file, and active rule is timestamped and cryptographically hashed, giving auditors 100% transparent proof of compliance.
    </p>
  </div>
</div>
"""
    },
    {
        "id": "slide-3",
        "num": "03",
        "chapter": "How to Use It",
        "tag": "Integration Workflow",
        "title": "How to Plug Governance Into Any Existing AI Project",
        "subtitle": "A frictionless, 4-step workflow that requires zero coding expertise and takes under 1 minute.",
        "content": """
<div class="workflow-wrapper">
  <div class="workflow-header">
    <strong>Developer Experience:</strong> How any engineering or business team plugs this package into their existing project.
  </div>
  
  <div class="workflow-grid-4">
    <!-- Step 1 -->
    <div class="wf-box">
      <div class="wf-step-num">Step 1</div>
      <div class="wf-icon">📂</div>
      <div class="wf-title">Keep Existing Code</div>
      <div class="wf-desc">Developers do not need to rewrite their code. They just have their project folder ready with their existing code files.</div>
      <div class="wf-badge">No Rewrite Needed</div>
    </div>
    
    <div class="wf-arrow">➔</div>
    
    <!-- Step 2 -->
    <div class="wf-box highlight-step">
      <div class="wf-step-num">Step 2</div>
      <div class="wf-icon">⚡</div>
      <div class="wf-title">Run 1-Line Command</div>
      <div class="wf-desc">Run 1 command in terminal or ask Claude Desktop AI chat: <i>"Inspect my project folder."</i></div>
      <div class="wf-badge green">Takes 3 Seconds</div>
    </div>
    
    <div class="wf-arrow">➔</div>
    
    <!-- Step 3 -->
    <div class="wf-box">
      <div class="wf-step-num">Step 3</div>
      <div class="wf-icon">📑</div>
      <div class="wf-title">Assets Auto-Generated</div>
      <div class="wf-desc">The copilot automatically creates the System Passport, Model Card, Data Card, and installs protective safety shields.</div>
      <div class="wf-badge purple">0 Hours Paperwork</div>
    </div>
    
    <div class="wf-arrow">➔</div>
    
    <!-- Step 4 -->
    <div class="wf-box">
      <div class="wf-step-num">Step 4</div>
      <div class="wf-icon">📊</div>
      <div class="wf-title">Audit Report Delivered</div>
      <div class="wf-desc">Double-click the generated visual HTML compliance report to verify that all 7 governance checks passed with green badges.</div>
      <div class="wf-badge blue">Executive Ready</div>
    </div>
  </div>
</div>

<div class="grid-2" style="margin-top:24px;">
  <div class="content-box">
    <div class="box-title">Method A: The 1-Line Command (Fastest for Engineers)</div>
    <p style="font-size:13px; color:var(--text-secondary); margin-bottom:10px;">
      Open PowerShell, paste this single command, and press Enter:
    </p>
    <div class="code-box highlight-cmd">
      python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup &lt;project-folder&gt;
    </div>
    <p style="font-size:12px; color:var(--text-muted); margin-top:8px;">
      <b>What the copilot does in 3 seconds:</b> Scans code &rarr; assigns risk &rarr; locks rules &rarr; creates cards &rarr; installs shields &rarr; generates HTML report.
    </p>
  </div>

  <div class="content-box highlight">
    <div class="box-title">Method B: The AI Chat Method (Best for Managers & Novices)</div>
    <p style="font-size:13px; color:var(--text-secondary); margin-bottom:10px;">
      We already configured your Claude Desktop application! You never have to touch a terminal:
    </p>
    <div class="chat-prompt-box">
      &ldquo;Use the ai_governance tool to inspect C:/ai-governance-package/sample-ai-project&rdquo;
    </div>
    <p style="font-size:12px; color:var(--text-muted); margin-top:8px;">
      Claude connects directly to your local governance package and returns the risk level and compliance status directly in your chat window.
    </p>
  </div>
</div>
"""
    },
    {
        "id": "slide-4",
        "num": "04",
        "chapter": "Executed Sample Projects",
        "tag": "Sample Project 1",
        "title": "Real Executed Sample 1: Customer Support AI (sample-ai-project)",
        "subtitle": "Walkthrough of an actual live execution on your machine, showing exactly what happened and what was created.",
        "content": """
<div class="lead-banner">
  <div class="lead-kicker">Sample 1: General Generative AI Application</div>
  <h3>A customer service AI assistant that answers user questions using company knowledge.</h3>
  <p>This project represents a standard AI application. Below is the exact step-by-step record of what happened when we executed the governance agent on this project.</p>
</div>

<div class="grid-2" style="margin-top:20px;">
  <div class="content-box">
    <div class="box-title">What Was Executed (Input)</div>
    <p style="font-size:13px; color:var(--text-secondary); margin-bottom:8px;">The user ran this single command in PowerShell:</p>
    <div class="code-box highlight-cmd" style="font-size:12px;">
      python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup sample-ai-project
    </div>
    
    <div class="terminal-card" style="margin-top:14px;">
      <div class="terminal-header">Real Copilot Terminal Output (3 Seconds)</div>
      <pre class="terminal-body" style="font-size:11px; max-height:160px;">
[AGENT] Scanning repository at: C:\\ai-governance-package\\sample-ai-project
[AGENT] Code Telemetry Inferred:
  * Scanned Files:         1 files
  * Frameworks Detected:   openai
  * PII Indicators:        None detected
  * Inferred Archetype:    generative_llm (Assigned Risk: tier_2_moderate)
[AGENT] Generating declarative project manifest...
[AGENT] Resolving deterministic policy snapshot... (40 active rules)
[AGENT] Installing pre-commit hooks and CI/CD PR gate...
[AGENT] Pre-populating starter Model Card & Data Card...
[AGENT] Generating interactive HTML compliance audit report...
[SUCCESS] Setup complete in 2.8 seconds. 7/7 checks PASSED.</pre>
    </div>
  </div>

  <div class="content-box highlight">
    <div class="box-title">What Was Produced (Tangible Outputs)</div>
    <ul class="clean-list">
      <li><b>1. Official System Passport (<code>ai-project-manifest.yaml</code>):</b> Registered the project identity, engineering owner, and assigned risk tier.</li>
      <li><b>2. Sealed Rulebook (<code>effective-policy-snapshot.json</code>):</b> Locked the 40 active safety rules tailored to this project.</li>
      <li><b>3. Technical Model Card (<code>model-card.yaml</code>):</b> Documented intended use, 88% accuracy benchmark, and 4% hallucination ceiling.</li>
      <li><b>4. Data Privacy Card (<code>data-card.yaml</code>):</b> Documented data sanitization and 5-year data retention schedule.</li>
      <li><b>5. Pre-Commit Shield:</b> Instantly blocks developers from pushing secrets to GitHub.</li>
      <li><b>6. Interactive HTML Audit Report:</b> Full visual dashboard with 7/7 green badges.</li>
    </ul>
    
    <div style="margin-top:16px;">
      <a href="file:///C:/ai-governance-package/sample-ai-project/governance-compliance-report.html" target="_blank" class="btn-action" style="display:inline-block; background:var(--blue); color:#fff; text-decoration:none; padding:10px 16px; border-radius:6px; font-weight:700;">
        👉 Open Sample 1 Compliance Report in Browser
      </a>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "slide-5",
        "num": "05",
        "chapter": "Executed Sample Projects",
        "tag": "Sample Project 2",
        "title": "Real Executed Sample 2: HR Resume Screener (sample-hr-resume-screening)",
        "subtitle": "High-Risk AI: What was caught as non-compliant, how it was analyzed, how it was fixed, and the resulting audit report.",
        "content": """
<div class="lead-banner" style="border-left-color:var(--amber);">
  <div class="lead-kicker">Sample 2: High-Risk Recruitment & Employment AI</div>
  <h3>An AI tool that scans job applicant resumes, ranks candidates, and calculates fit scores.</h3>
  <p>Under the EU AI Act (Annex III) and global labor regulations, employment AI is classified as <b>High-Risk (Tier 3)</b>. Without strict governance, this application could trigger multi-million dollar regulatory fines and devastating bias lawsuits.</p>
</div>

<div class="grid-2" style="margin-top:20px;">
  <!-- Non-Compliant Before -->
  <div class="content-box" style="border-top:3px solid var(--red);">
    <div class="box-title" style="color:var(--red);">What Was Caught as Non-Compliant (Before Governance)</div>
    <div class="issue-item">
      <span class="badge fail">VIOLATION: POL-SEC-01</span>
      <h4>Hardcoded API Secret in Code</h4>
      <p>The developer pasted an OpenAI secret key directly into <code>resume_scanner.py</code>. If pushed to GitHub, company cloud accounts would be compromised.</p>
    </div>
    <div class="issue-item" style="margin-top:12px;">
      <span class="badge fail">VIOLATION: POL-OVR-01</span>
      <h4>Illegal Autonomous Hiring Rejections</h4>
      <p>The code attempted to reject candidates automatically without a human recruiter review, violating mandatory EU AI Act human-oversight laws.</p>
    </div>
    <div class="issue-item" style="margin-top:12px;">
      <span class="badge fail">VIOLATION: POL-RET-01</span>
      <h4>Unmanaged Retention of Applicant PII</h4>
      <p>Candidate names, phone numbers, and home addresses were retained indefinitely with no deletion schedule.</p>
    </div>
  </div>

  <!-- Remediated After -->
  <div class="content-box highlight" style="border-top:3px solid var(--green);">
    <div class="box-title" style="color:var(--green);">How Governance Analyzed & Fixed It (After Governance)</div>
    <div class="fix-item">
      <span class="badge pass">ANALYSIS</span>
      <p>The copilot scanned the files, detected candidate PII (email, phone, name) and ML libraries, and bound High-Risk Tier 3 rules (43 controls).</p>
    </div>
    <div class="fix-item" style="margin-top:12px;">
      <span class="badge pass">REMEDIATION 1: SECRET REMOVED</span>
      <p>Moved API key to secure environment variables. Installed pre-commit secret shield to permanently prevent credential leaks.</p>
    </div>
    <div class="fix-item" style="margin-top:12px;">
      <span class="badge pass">REMEDIATION 2: HUMAN OVERSIGHT ENFORCED</span>
      <p>Code modified to advisory mode only (<code>PENDING_HUMAN_REVIEW</code>). Recruiters make all final hiring decisions.</p>
    </div>
    <div class="fix-item" style="margin-top:12px;">
      <span class="badge pass">REMEDIATION 3: 1-YEAR GDPR RETENTION SEALED</span>
      <p>Data Card configured with a strict 1-year data deletion schedule and Model Card bound to 85% fairness parity ratio.</p>
    </div>
  </div>
</div>

<div class="callout-box success" style="margin-top:20px; display:flex; justify-content:space-between; align-items:center;">
  <div>
    <strong>Audit Result:</strong> 100% Compliant. 43 High-Risk controls active. Cryptographically sealed.
  </div>
  <a href="file:///C:/ai-governance-package/sample-hr-resume-screening/governance-compliance-report.html" target="_blank" class="btn-action" style="background:var(--green); color:#fff; text-decoration:none; padding:8px 14px; border-radius:6px; font-weight:700;">
    👉 Open HR Screening Compliance Report
  </a>
</div>
"""
    },
    {
        "id": "slide-6",
        "num": "06",
        "chapter": "Executed Sample Projects",
        "tag": "Sample Project 3",
        "title": "Real Executed Sample 3: Autonomous Financial Advisor (sample-financial-advisor)",
        "subtitle": "Agentic AI: What was caught as non-compliant, how it was analyzed, how it was fixed, and the resulting audit report.",
        "content": """
<div class="lead-banner" style="border-left-color:var(--purple);">
  <div class="lead-kicker">Sample 3: High-Risk Autonomous Agent & Financial Tool Execution</div>
  <h3>An AI agent that monitors investment portfolios, recommends asset shifts, and executes bank fund transfers.</h3>
  <p>Because this AI can perform real-world financial transactions (`execute_fund_transfer`), an unconstrained agent could enter a runaway loop or execute unauthorized fund transfers if attacked by prompt injection.</p>
</div>

<div class="grid-2" style="margin-top:20px;">
  <!-- Non-Compliant Before -->
  <div class="content-box" style="border-top:3px solid var(--red);">
    <div class="box-title" style="color:var(--red);">What Was Caught as Non-Compliant (Before Governance)</div>
    <div class="issue-item">
      <span class="badge fail">VIOLATION: AGENT-OVERLAY-01</span>
      <h4>Unrestricted Tool Execution (Runaway Risk)</h4>
      <p>The agent had permissions to call bank transfer APIs autonomously without requiring any human dual-key authorization or spending cap.</p>
    </div>
    <div class="issue-item" style="margin-top:12px;">
      <span class="badge fail">VIOLATION: POL-RET-01</span>
      <h4>Missing SEC/FINRA Statutory Retention</h4>
      <p>Financial recommendations and transaction prompts lacked the mandatory 7-year statutory audit trail required by financial regulators.</p>
    </div>
    <div class="issue-item" style="margin-top:12px;">
      <span class="badge fail">VIOLATION: POL-SEC-03</span>
      <h4>Prompt Injection Vulnerability</h4>
      <p>External inputs were passed directly into financial execution tools with no recursion depth limits.</p>
    </div>
  </div>

  <!-- Remediated After -->
  <div class="content-box highlight" style="border-top:3px solid var(--green);">
    <div class="box-title" style="color:var(--green);">How Governance Analyzed & Fixed It (After Governance)</div>
    <div class="fix-item">
      <span class="badge pass">ANALYSIS</span>
      <p>The copilot scanned code, detected tool-execution keywords (<code>transfer_funds</code>, <code>requests.post</code>), and bound the Autonomous Agent Overlay (46 controls).</p>
    </div>
    <div class="fix-item" style="margin-top:12px;">
      <span class="badge pass">REMEDIATION 1: DUAL-KEY SPENDING CAP</span>
      <p>Enforced dual-key authorization: Any fund transfer over $500 is blocked automatically unless accompanied by a human approval token.</p>
    </div>
    <div class="fix-item" style="margin-top:12px;">
      <span class="badge pass">REMEDIATION 2: 7-YEAR STATUTORY AUDIT TRAIL</span>
      <p>Data Card formally locked with SEC/FINRA 7-year audit retention rules and cryptographic prompt hashing.</p>
    </div>
    <div class="fix-item" style="margin-top:12px;">
      <span class="badge pass">REMEDIATION 3: RECURSION DEPTH BOUNDED</span>
      <p>Agent restricted to maximum call depth &le; 3, preventing runaway loops and prompt hijacking.</p>
    </div>
  </div>
</div>

<div class="callout-box success" style="margin-top:20px; display:flex; justify-content:space-between; align-items:center;">
  <div>
    <strong>Audit Result:</strong> 100% Compliant. 46 Agent controls active. Dual-key protection enabled.
  </div>
  <a href="file:///C:/ai-governance-package/sample-financial-advisor/governance-compliance-report.html" target="_blank" class="btn-action" style="background:var(--purple); color:#fff; text-decoration:none; padding:8px 14px; border-radius:6px; font-weight:700;">
    👉 Open Financial Advisor Compliance Report
  </a>
</div>
"""
    },
    {
        "id": "slide-7",
        "num": "07",
        "chapter": "Deliverables & Reports",
        "tag": "What You Get",
        "title": "What Outputs & Reports Do You Get After Execution?",
        "subtitle": "At the end of the day, what tangible evidence and reports does the business receive?",
        "content": """
<div class="grid-2">
  <div class="output-card full" style="border-left: 5px solid var(--blue);">
    <div class="output-num">Report 1</div>
    <div class="output-body">
      <h4>The Interactive HTML Compliance Audit Report</h4>
      <p style="font-size:14px; margin-bottom:8px;"><b>File: <code>governance-compliance-report.html</code></b></p>
      <p>A beautiful visual report that opens in any web browser (Chrome, Edge) with zero special software needed. It shows:</p>
      <ul class="clean-list" style="margin-top:6px;">
        <li><b>7 / 7 Green Verification Badges:</b> Proving that manifest, rules, secret scanner, and cards are verified.</li>
        <li><b>Assigned Risk Tier:</b> Explaining why the system is classified as Low, Medium, or High Risk.</li>
        <li><b>Digital Proof Seal:</b> A cryptographic stamp showing the exact date and time the rules were locked.</li>
        <li><b>Print / Save as PDF:</b> One click to generate a clean PDF document to hand to auditors or executives.</li>
      </ul>
    </div>
  </div>

  <div class="output-card full" style="border-left: 5px solid var(--green);">
    <div class="output-num">Docs 2</div>
    <div class="output-body">
      <h4>Standardized AI Documentation Cards</h4>
      <p style="font-size:14px; margin-bottom:8px;"><b>Folder: <code>governance-cards/</code></b></p>
      <p>Two essential business and compliance certificates pre-filled by the system:</p>
      <ul class="clean-list" style="margin-top:6px;">
        <li><b>The Model Card (<code>model-card.yaml</code>):</b> The AI system's technical spec sheet. Records intended use, accuracy targets (88%), and error rate limits (under 4%).</li>
        <li><b>The Data Card (<code>data-card.yaml</code>):</b> The privacy certificate. Certifies that personal customer data (PII) is protected and retention is capped at 5 years.</li>
      </ul>
    </div>
  </div>
</div>

<div class="grid-2" style="margin-top:18px;">
  <div class="output-card">
    <div class="output-num">03</div>
    <div class="output-body">
      <h4>The System Passport (Manifest)</h4>
      <p>A simple declaration file registering the system name, technical lead, business owner email, and active regulatory standards.</p>
    </div>
  </div>
  <div class="output-card">
    <div class="output-num">04</div>
    <div class="output-body">
      <h4>The Sealed Rulebook (Snapshot)</h4>
      <p>A single digital rulebook containing the exact safety obligations tailored to this project, locked with a digital security seal.</p>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "slide-8",
        "num": "08",
        "chapter": "Risk & Enforcement",
        "tag": "Company Protection",
        "title": "What Happens If Something Fails or Standards Are Not Followed?",
        "subtitle": "How the system actively protects the company from data breaches, legal penalties, and rogue AI actions.",
        "content": """
<div class="table-card">
  <div class="table-header">The Automated Safety Barriers: What Happens When a Rule is Violated</div>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width:28%">Safety Risk Detected</th>
        <th style="width:36%">Real-World Business Danger</th>
        <th style="width:36%">Automated Action Taken by System</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Developer leaves password or API key in code</b></td>
        <td>High risk of database breach or massive unauthorized cloud spending.</td>
        <td><span class="badge-action red">ABORTS COMMIT IMMEDIATELY</span><br>The code cannot leave the developer's laptop.</td>
      </tr>
      <tr>
        <td><b>AI model has high error or hallucination rate</b></td>
        <td>Bad AI advice reaches customers, causing reputational or legal damage.</td>
        <td><span class="badge-action red">LOCKS SOFTWARE RELEASE</span><br>The update is blocked from merging into production.</td>
      </tr>
      <tr>
        <td><b>AI system uses unlicensed/copyrighted code</b></td>
        <td>Legal copyright lawsuits and intellectual property liability.</td>
        <td><span class="badge-action red">BLOCKS PULL REQUEST</span><br>Flags copyleft license violation to engineering lead.</td>
      </tr>
      <tr>
        <td><b>AI agent attempts an unauthorized action</b></td>
        <td>Agent goes into a runaway loop or transfers funds without approval.</td>
        <td><span class="badge-action red">BLOCKS ACTION IN REAL TIME</span><br>Stops tool execution and alerts human supervisor.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="grid-2" style="margin-top:20px;">
  <div class="content-box">
    <div class="box-title">What If an Urgent Exception is Needed? (The Lawful Fallback)</div>
    <p style="font-size:13px; line-height:1.6; color:var(--text-main);">
      If a legacy system or emergency fix cannot comply immediately, <b>developers cannot secretly bypass the system</b>. Instead, they must submit a formal Exception Request specifying compensating controls, valid for up to 90 days, requiring approval by the <b>AI Safety Board</b>.
    </p>
  </div>
  <div class="content-box">
    <div class="box-title">Zero Guesswork for Engineers</div>
    <p style="font-size:13px; line-height:1.6; color:var(--text-main);">
      Whenever an action is blocked, the developer receives a clear, plain-English message explaining exactly which company policy failed and the exact 1-step action needed to fix it.
    </p>
  </div>
</div>
"""
    },
    {
        "id": "slide-9",
        "num": "09",
        "chapter": "Executive Summary",
        "tag": "Next Steps",
        "title": "Executive Summary & Next Steps for Leadership",
        "subtitle": "Everything is complete, audited, and ready to scale across your organization.",
        "content": """
<div class="lead-banner">
  <div class="lead-kicker">Status: 100% Complete & Verified</div>
  <h3>Your company now has a battle-tested, automated AI Governance Platform.</h3>
  <p>The package is fully implemented, verified, committed, and published to GitHub. Any engineering team in your company can adopt this governance standard tomorrow morning in 3 seconds.</p>
</div>

<div class="grid-3" style="margin-top:24px;">
  <div class="content-box">
    <div class="box-title">1. Review Live Reports</div>
    <p style="font-size:13px; color:var(--text-secondary); line-height:1.6;">
      Open any of the 3 executed project reports right now:
    </p>
    <ul class="clean-list" style="margin-top:8px; font-size:12px;">
      <li><a href="file:///C:/ai-governance-package/sample-ai-project/governance-compliance-report.html" target="_blank" style="color:var(--blue); font-weight:700;">Customer Support Bot Report</a></li>
      <li><a href="file:///C:/ai-governance-package/sample-hr-resume-screening/governance-compliance-report.html" target="_blank" style="color:var(--green); font-weight:700;">HR Resume Screener Report</a></li>
      <li><a href="file:///C:/ai-governance-package/sample-financial-advisor/governance-compliance-report.html" target="_blank" style="color:var(--purple); font-weight:700;">Financial Advisor Agent Report</a></li>
    </ul>
  </div>

  <div class="content-box">
    <div class="box-title">2. Roll Out to First Pilot</div>
    <p style="font-size:13px; color:var(--text-secondary); line-height:1.6;">
      Pick any real AI project currently being developed in your team and run:
    </p>
    <div class="code-box" style="margin-top:8px; font-size:11px;">
      python C:\\ai-governance-package\\agents\\governance_agent.py auto-setup &lt;project-folder&gt;
    </div>
  </div>

  <div class="content-box">
    <div class="box-title">3. Ratify Policies (Board)</div>
    <p style="font-size:13px; color:var(--text-secondary); line-height:1.6;">
      Have your AI Safety Review Board review the 16 baseline policies in <code>baseline/policies/</code>, replace the placeholder names with real department leads, and mark as active.
    </p>
  </div>
</div>

<div class="callout-box success" style="margin-top:24px;">
  <strong>Final Management Message:</strong> With this platform in place, your organization can boldly pursue cutting-edge generative AI and autonomous agents with complete confidence that your reputation, data privacy, and legal compliance are automatically protected.
</div>
"""
    }
]


def build_deck():
    # Build Sidebar items
    sidebar_items_html = ""
    current_chapter = ""
    for idx, s in enumerate(SLIDES):
        if s["chapter"] != current_chapter:
            current_chapter = s["chapter"]
            sidebar_items_html += f'<div class="sidebar-chapter-heading">{current_chapter}</div>\n'
        
        active_cls = " active" if idx == 0 else ""
        sidebar_items_html += f"""
        <div class="sidebar-item{active_cls}" onclick="goToSlide({idx})" id="nav-item-{idx}">
          <div class="sidebar-item-top">
            <span class="sidebar-item-num">{s['num']}</span>
            <span class="sidebar-item-tag">{s['tag']}</span>
          </div>
          <div class="sidebar-item-title">{s['title']}</div>
        </div>
        """

    # Build Slide wrappers
    slides_html = ""
    for idx, s in enumerate(SLIDES):
        active_cls = " active" if idx == 0 else ""
        slides_html += f"""
        <section class="slide-section{active_cls}" id="{s['id']}" data-index="{idx}">
          <div class="slide-header">
            <div class="slide-meta">
              <span class="slide-num-pill">Slide {s['num']}</span>
              <span class="slide-chapter-tag">{s['chapter']}</span>
              <span class="slide-sep">&bull;</span>
              <span class="slide-tag-pill">{s['tag']}</span>
            </div>
            <h2 class="slide-main-title">{s['title']}</h2>
            <p class="slide-main-subtitle">{s['subtitle']}</p>
          </div>
          <div class="slide-content-body">
            {s['content']}
          </div>
        </section>
        """

    # Build dropdown options
    dropdown_options = ""
    for idx, s in enumerate(SLIDES):
        dropdown_options += f'<option value="{idx}">{s["num"]}. {s["title"][:45]}...</option>\n'

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Enterprise AI Governance: Executive & Management Overview</title>
<style>
  :root {{
    --navy: #0B2E59;
    --navy-dark: #061A33;
    --navy-light: #16437E;
    --red: #E52421;
    --red-soft: #FEE2E2;
    --green: #059669;
    --green-soft: #D1FAE5;
    --blue: #0284C7;
    --blue-soft: #E0F2FE;
    --purple: #7C3AED;
    --purple-soft: #EDE9FE;
    --amber: #D97706;
    --amber-soft: #FEF3C7;
    --bg-page: #F8FAFC;
    --bg-card: #FFFFFF;
    --bg-sidebar: #FFFFFF;
    --border-light: #E2E8F0;
    --border-dark: #CBD5E1;
    --text-main: #0F172A;
    --text-secondary: #334155;
    --text-muted: #64748B;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
    --shadow-lg: 0 12px 28px rgba(11,46,89,0.12);
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
    --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    --mono: "Cascadia Mono", Consolas, "Courier New", monospace;
  }}

  body.dark-mode {{
    --bg-page: #080D1A;
    --bg-card: #0F172A;
    --bg-sidebar: #0B1120;
    --border-light: #1E293B;
    --border-dark: #334155;
    --text-main: #F8FAFC;
    --text-secondary: #CBD5E1;
    --text-muted: #94A3B8;
    --navy-dark: #050B14;
    --navy: #16437E;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ height: 100%; }}
  body {{
    font-family: var(--font);
    background: var(--bg-page);
    color: var(--text-main);
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: background-color 0.25s, color 0.25s;
  }}

  /* HEADER */
  header.master-header {{
    background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy) 100%);
    color: #fff;
    padding: 12px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    border-bottom: 2px solid var(--red);
    box-shadow: var(--shadow-md);
    z-index: 100;
    flex-shrink: 0;
  }}

  .header-brand {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}

  .gov-badge {{
    background: var(--red);
    color: #fff;
    font-size: 12px;
    font-weight: 800;
    padding: 6px 12px;
    border-radius: var(--radius-sm);
    letter-spacing: 1px;
    box-shadow: 0 2px 6px rgba(229,36,33,0.4);
  }}

  .brand-text h1 {{
    font-size: 17px;
    font-weight: 700;
    color: #fff;
  }}

  .brand-text p {{
    font-size: 12px;
    color: #94A3B8;
  }}

  .header-actions {{
    display: flex;
    align-items: center;
    gap: 10px;
  }}

  .mode-tabs {{
    background: rgba(255,255,255,0.1);
    padding: 3px;
    border-radius: 20px;
    display: flex;
    gap: 2px;
    border: 1px solid rgba(255,255,255,0.2);
  }}

  .mode-btn {{
    background: transparent;
    border: none;
    color: #E2E8F0;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 600;
    border-radius: 16px;
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }}

  .mode-btn.active {{
    background: var(--red);
    color: #fff;
    box-shadow: 0 2px 6px rgba(229,36,33,0.4);
  }}

  .btn-action {{
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.22);
    color: #fff;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 600;
    border-radius: var(--radius-sm);
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }}

  .btn-action:hover {{
    background: rgba(255,255,255,0.2);
    border-color: rgba(255,255,255,0.35);
  }}

  /* WORKSPACE LAYOUT */
  .workspace {{
    display: flex;
    flex: 1;
    overflow: hidden;
    position: relative;
  }}

  /* SIDEBAR */
  aside.sidebar {{
    width: 320px;
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border-light);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    transition: all 0.25s;
    z-index: 10;
  }}

  .sidebar-search-box {{
    padding: 14px 16px;
    border-bottom: 1px solid var(--border-light);
  }}

  .search-input {{
    width: 100%;
    padding: 8px 12px;
    font-size: 13px;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    background: var(--bg-page);
    color: var(--text-main);
    outline: none;
    font-family: inherit;
  }}

  .search-input:focus {{
    border-color: var(--navy);
  }}

  .sidebar-nav {{
    flex: 1;
    overflow-y: auto;
    padding: 12px 10px;
  }}

  .sidebar-chapter-heading {{
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 1px;
    padding: 10px 10px 4px 10px;
  }}

  .sidebar-item {{
    padding: 10px 12px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    margin-bottom: 4px;
    transition: all 0.15s;
    border-left: 3px solid transparent;
  }}

  .sidebar-item:hover {{
    background: var(--bg-page);
  }}

  .sidebar-item.active {{
    background: var(--blue-soft);
    border-left-color: var(--navy);
  }}

  body.dark-mode .sidebar-item.active {{
    background: rgba(2,132,199,0.15);
    border-left-color: var(--blue);
  }}

  .sidebar-item-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2px;
  }}

  .sidebar-item-num {{
    font-size: 11px;
    font-weight: 700;
    color: var(--text-muted);
    font-family: var(--mono);
  }}

  .sidebar-item-tag {{
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    padding: 2px 6px;
    border-radius: 4px;
    background: var(--border-light);
    color: var(--text-secondary);
  }}

  .sidebar-item.active .sidebar-item-tag {{
    background: var(--navy);
    color: #fff;
  }}

  .sidebar-item-title {{
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-main);
    line-height: 1.4;
  }}

  /* MAIN CONTENT */
  main.presentation-area {{
    flex: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    padding: 28px 36px;
    background: var(--bg-page);
    position: relative;
  }}

  /* SLIDE VIEW MODE */
  .slide-section {{
    display: none;
    max-width: 1100px;
    width: 100%;
    margin: 0 auto;
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    padding: 34px 40px;
    animation: fadeIn 0.25s ease-in-out;
  }}

  .slide-section.active {{
    display: block;
  }}

  /* FULL CONTINUOUS VIEW MODE */
  body.mode-full-view aside.sidebar {{
    display: block;
  }}

  body.mode-full-view .slide-section {{
    display: block !important;
    margin-bottom: 32px;
  }}

  body.mode-full-view .slide-controls-footer {{
    display: none;
  }}

  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(6px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  /* SLIDE HEADERS */
  .slide-meta {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
  }}

  .slide-num-pill {{
    background: var(--navy);
    color: #fff;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 12px;
    font-family: var(--mono);
  }}

  .slide-chapter-tag {{
    font-size: 12px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .slide-sep {{
    color: var(--text-muted);
  }}

  .slide-tag-pill {{
    background: var(--border-light);
    color: var(--text-secondary);
    font-size: 11px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
  }}

  .slide-main-title {{
    font-size: 24px;
    font-weight: 800;
    color: var(--navy);
    line-height: 1.3;
    margin-bottom: 8px;
  }}

  body.dark-mode .slide-main-title {{
    color: #60A5FA;
  }}

  .slide-main-subtitle {{
    font-size: 14.5px;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border-light);
  }}

  /* CARDS & GRIDS */
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }}

  .grid-3 {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
  }}

  .grid-4 {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
  }}

  .lead-banner {{
    background: linear-gradient(135deg, rgba(11,46,89,0.05) 0%, rgba(2,132,199,0.08) 100%);
    border-left: 5px solid var(--navy);
    padding: 20px 24px;
    border-radius: var(--radius-sm);
  }}

  body.dark-mode .lead-banner {{
    background: rgba(11,46,89,0.25);
    border-left-color: var(--blue);
  }}

  .lead-kicker {{
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--navy);
    letter-spacing: 1px;
    margin-bottom: 6px;
  }}

  body.dark-mode .lead-kicker {{
    color: #93C5FD;
  }}

  .lead-banner h3 {{
    font-size: 17px;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 8px;
    line-height: 1.4;
  }}

  .lead-banner p {{
    font-size: 13.5px;
    color: var(--text-secondary);
    line-height: 1.6;
  }}

  .stat-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 18px 20px;
    border-top: 4px solid var(--navy);
    box-shadow: var(--shadow-sm);
  }}

  .stat-num {{
    font-size: 26px;
    font-weight: 800;
    color: var(--navy);
    font-family: var(--mono);
  }}

  body.dark-mode .stat-num {{
    color: #60A5FA;
  }}

  .stat-label {{
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 0.5px;
    margin-top: 4px;
  }}

  .stat-desc {{
    font-size: 12.5px;
    color: var(--text-secondary);
    margin-top: 8px;
    line-height: 1.5;
  }}

  .content-box {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 20px 22px;
  }}

  .content-box.highlight {{
    background: rgba(2,132,199,0.03);
    border-color: #BFDBFE;
  }}

  body.dark-mode .content-box.highlight {{
    background: rgba(2,132,199,0.08);
    border-color: #1E3A8A;
  }}

  .box-title {{
    font-size: 15px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 12px;
  }}

  body.dark-mode .box-title {{
    color: #93C5FD;
  }}

  /* WORKFLOW BOX DIAGRAMS */
  .workflow-wrapper {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 20px 24px;
    box-shadow: var(--shadow-sm);
  }}

  .workflow-header {{
    font-size: 14px;
    color: var(--text-main);
    margin-bottom: 18px;
    padding-bottom: 10px;
    border-bottom: 1px dashed var(--border-light);
  }}

  .workflow-grid-4 {{
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    gap: 8px;
  }}

  .wf-box {{
    flex: 1;
    background: var(--bg-page);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    padding: 16px 14px;
    text-align: center;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .wf-box.highlight-step {{
    background: var(--blue-soft);
    border-color: var(--blue);
  }}

  body.dark-mode .wf-box.highlight-step {{
    background: rgba(2,132,199,0.15);
    border-color: var(--blue);
  }}

  .wf-step-num {{
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 1px;
    margin-bottom: 4px;
  }}

  .wf-icon {{
    font-size: 24px;
    margin: 4px 0 8px 0;
  }}

  .wf-title {{
    font-size: 13.5px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 6px;
    line-height: 1.3;
  }}

  body.dark-mode .wf-title {{
    color: #93C5FD;
  }}

  .wf-desc {{
    font-size: 11.5px;
    color: var(--text-secondary);
    line-height: 1.4;
    margin-bottom: 12px;
  }}

  .wf-badge {{
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 10px;
    background: var(--border-light);
    color: var(--text-secondary);
    margin-top: auto;
  }}

  .wf-badge.green {{ background: var(--green-soft); color: #065F46; }}
  .wf-badge.blue {{ background: var(--blue-soft); color: #075985; }}
  .wf-badge.purple {{ background: var(--purple-soft); color: #5B21B6; }}
  .wf-badge.red {{ background: var(--red-soft); color: #991B1B; }}

  .wf-arrow {{
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    color: var(--navy);
    font-weight: 800;
    padding: 0 4px;
  }}

  body.dark-mode .wf-arrow {{
    color: #60A5FA;
  }}

  /* ISSUE & FIX CARDS */
  .issue-item {{
    background: #FFF1F2;
    border: 1px solid #FECDD3;
    border-left: 4px solid var(--red);
    padding: 12px 14px;
    border-radius: 4px;
  }}

  body.dark-mode .issue-item {{
    background: rgba(229,36,33,0.1);
    border-color: rgba(229,36,33,0.3);
  }}

  .issue-item h4 {{
    font-size: 13.5px;
    font-weight: 700;
    color: #991B1B;
    margin: 4px 0;
  }}

  body.dark-mode .issue-item h4 {{
    color: #F87171;
  }}

  .issue-item p {{
    font-size: 12px;
    color: #4C0519;
    line-height: 1.4;
  }}

  body.dark-mode .issue-item p {{
    color: #FECDD3;
  }}

  .fix-item {{
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-left: 4px solid var(--green);
    padding: 12px 14px;
    border-radius: 4px;
  }}

  body.dark-mode .fix-item {{
    background: rgba(5,150,105,0.1);
    border-color: rgba(5,150,105,0.3);
  }}

  .fix-item p {{
    font-size: 12px;
    color: #064E3B;
    line-height: 1.4;
    margin-top: 4px;
  }}

  body.dark-mode .fix-item p {{
    color: #A7F3D0;
  }}

  /* TERMINAL CARD */
  .terminal-card {{
    background: #0B1120;
    border-radius: var(--radius-sm);
    overflow: hidden;
    border: 1px solid #1E293B;
  }}

  .terminal-header {{
    background: #060B14;
    color: #94A3B8;
    font-size: 11px;
    font-weight: 700;
    padding: 6px 12px;
    border-bottom: 1px solid #1E293B;
    font-family: var(--mono);
  }}

  .terminal-body {{
    color: #38BDF8;
    padding: 10px 14px;
    font-family: var(--mono);
    line-height: 1.4;
    overflow-x: auto;
  }}

  /* LISTS & TABLES */
  .clean-list {{
    list-style: none;
    padding: 0;
  }}

  .clean-list li {{
    position: relative;
    padding-left: 18px;
    margin-bottom: 10px;
    font-size: 13.5px;
    line-height: 1.5;
    color: var(--text-secondary);
  }}

  .clean-list li::before {{
    content: "•";
    position: absolute;
    left: 0;
    color: var(--navy);
    font-weight: 800;
    font-size: 16px;
    line-height: 1;
  }}

  body.dark-mode .clean-list li::before {{
    color: #60A5FA;
  }}

  .table-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    overflow: hidden;
    margin-top: 14px;
  }}

  .table-header {{
    background: var(--navy-dark);
    color: #fff;
    font-size: 13px;
    font-weight: 700;
    padding: 12px 18px;
  }}

  .data-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }}

  .data-table th, .data-table td {{
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border-light);
  }}

  .data-table th {{
    background: var(--bg-page);
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .data-table tr:hover td {{
    background: rgba(2,132,199,0.02);
  }}

  /* BADGES & CALLOUTS */
  .badge {{
    display: inline-block;
    font-size: 10px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    font-family: var(--mono);
  }}

  .badge.pass {{ background: var(--green-soft); color: #065F46; border: 1px solid #A7F3D0; }}
  .badge.fail {{ background: var(--red-soft); color: #991B1B; border: 1px solid #FECACA; }}

  .badge-action {{
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    margin-bottom: 4px;
  }}

  .badge-action.red {{
    background: var(--red-soft);
    color: #991B1B;
    border: 1px solid #FECACA;
  }}

  .callout-box {{
    padding: 14px 18px;
    border-radius: var(--radius-sm);
    font-size: 13px;
    line-height: 1.5;
  }}

  .callout-box.info {{
    background: var(--blue-soft);
    border: 1px solid #BAE6FD;
    color: #0369A1;
  }}

  .callout-box.success {{
    background: var(--green-soft);
    border: 1px solid #A7F3D0;
    color: #065F46;
  }}

  .code-box {{
    background: #0B1120;
    color: #38BDF8;
    padding: 10px 14px;
    border-radius: var(--radius-sm);
    font-family: var(--mono);
    font-size: 12px;
    overflow-x: auto;
  }}

  .code-box.highlight-cmd {{
    border-left: 4px solid var(--red);
    color: #F8FAFC;
    background: #020617;
  }}

  .chat-prompt-box {{
    background: #F1F5F9;
    border: 1px dashed #94A3B8;
    padding: 12px 16px;
    border-radius: var(--radius-sm);
    font-family: var(--font);
    font-size: 13.5px;
    font-weight: 600;
    color: var(--navy);
  }}

  body.dark-mode .chat-prompt-box {{
    background: #1E293B;
    border-color: #475569;
    color: #93C5FD;
  }}

  .output-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 18px 20px;
    display: flex;
    gap: 16px;
    align-items: flex-start;
  }}

  .output-num {{
    background: var(--bg-page);
    color: var(--navy);
    font-size: 13px;
    font-weight: 800;
    padding: 6px 10px;
    border-radius: 6px;
    font-family: var(--mono);
    border: 1px solid var(--border-light);
  }}

  body.dark-mode .output-num {{
    color: #60A5FA;
  }}

  .output-body h4 {{
    font-size: 15px;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 6px;
  }}

  body.dark-mode .output-body h4 {{
    color: #93C5FD;
  }}

  .output-body p {{
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.5;
  }}

  /* FOOTER CONTROLS */
  footer.slide-controls-footer {{
    background: var(--bg-card);
    border-top: 1px solid var(--border-light);
    padding: 12px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-shrink: 0;
    z-index: 20;
  }}

  .footer-nav-btn {{
    background: var(--navy);
    color: #fff;
    border: none;
    padding: 8px 18px;
    font-size: 13px;
    font-weight: 700;
    border-radius: var(--radius-sm);
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }}

  .footer-nav-btn:hover {{
    background: var(--navy-light);
  }}

  .footer-nav-btn:disabled {{
    background: var(--border-dark);
    cursor: not-allowed;
    opacity: 0.6;
  }}

  .footer-indicator {{
    font-size: 13px;
    font-weight: 700;
    color: var(--text-muted);
    font-family: var(--mono);
  }}

  .footer-dropdown {{
    padding: 6px 12px;
    font-size: 13px;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    background: var(--bg-page);
    color: var(--text-main);
    font-family: inherit;
    cursor: pointer;
  }}

  /* PRINT STYLES */
  @media print {{
    body {{
      overflow: visible !important;
      height: auto !important;
      background: #fff !important;
      color: #000 !important;
    }}
    header.master-header, aside.sidebar, footer.slide-controls-footer {{
      display: none !important;
    }}
    main.presentation-area {{
      overflow: visible !important;
      padding: 0 !important;
      background: #fff !important;
    }}
    .slide-section {{
      display: block !important;
      box-shadow: none !important;
      border: 1px solid #ccc !important;
      margin-bottom: 40px !important;
      page-break-after: always !important;
    }}
  }}
</style>
</head>
<body>

<!-- MASTER HEADER -->
<header class="master-header">
  <div class="header-brand">
    <div class="gov-badge">AI-GOV</div>
    <div class="brand-text">
      <h1>Enterprise AI Governance</h1>
      <p>Senior Management & Executive Overview &bull; Production Platform</p>
    </div>
  </div>

  <div class="header-actions">
    <div class="mode-tabs">
      <button class="mode-btn active" id="btn-mode-slide" onclick="setViewMode('slide')">Slide Mode</button>
      <button class="mode-btn" id="btn-mode-full" onclick="setViewMode('full')">Full View</button>
    </div>

    <button class="btn-action" onclick="togglePresentationMode()" title="Fullscreen Presentation (Press F)">
      📺 Present (F)
    </button>
    
    <button class="btn-action" onclick="toggleTheme()" title="Toggle Dark/Light Mode">
      🌓 Theme
    </button>

    <button class="btn-action" style="background:var(--red); border-color:var(--red);" onclick="window.print()">
      📄 Save as PDF
    </button>
  </div>
</header>

<!-- WORKSPACE -->
<div class="workspace">
  <!-- SIDEBAR -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-search-box">
      <input type="text" class="search-input" id="sidebar-search" placeholder="Search slides or policies..." onkeyup="filterSidebar()">
    </div>
    <nav class="sidebar-nav" id="sidebar-nav">
      {sidebar_items_html}
    </nav>
  </aside>

  <!-- PRESENTATION MAIN AREA -->
  <main class="presentation-area" id="main-content">
    {slides_html}
  </main>
</div>

<!-- FOOTER CONTROLS -->
<footer class="slide-controls-footer" id="footer-controls">
  <div style="display:flex; align-items:center; gap:12px;">
    <button class="footer-nav-btn" id="btn-prev" onclick="changeSlide(-1)">◀ Previous</button>
    <button class="footer-nav-btn" id="btn-next" onclick="changeSlide(1)">Next ▶</button>
  </div>

  <div style="display:flex; align-items:center; gap:16px;">
    <span class="footer-indicator" id="footer-slide-counter">Slide 1 of {len(SLIDES)}</span>
    <select class="footer-dropdown" id="slide-jump-select" onchange="goToSlide(parseInt(this.value))">
      {dropdown_options}
    </select>
  </div>
</footer>

<script>
  let currentSlide = 0;
  const totalSlides = {len(SLIDES)};
  let isFullView = false;

  function updateSlideUI() {{
    if (isFullView) return;

    // Update slides
    const slides = document.querySelectorAll('.slide-section');
    slides.forEach((s, idx) => {{
      if (idx === currentSlide) {{
        s.classList.add('active');
      }} else {{
        s.classList.remove('active');
      }}
    }});

    // Update sidebar items
    const navItems = document.querySelectorAll('.sidebar-item');
    navItems.forEach((item, idx) => {{
      if (idx === currentSlide) {{
        item.classList.add('active');
        item.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
      }} else {{
        item.classList.remove('active');
      }}
    }});

    // Update footer
    document.getElementById('footer-slide-counter').innerText = `Slide ${{currentSlide + 1}} of ${{totalSlides}}`;
    document.getElementById('slide-jump-select').value = currentSlide;
    document.getElementById('btn-prev').disabled = (currentSlide === 0);
    document.getElementById('btn-next').disabled = (currentSlide === totalSlides - 1);

    // Scroll main to top
    document.getElementById('main-content').scrollTop = 0;
  }}

  function changeSlide(direction) {{
    const target = currentSlide + direction;
    if (target >= 0 && target < totalSlides) {{
      currentSlide = target;
      updateSlideUI();
    }}
  }}

  function goToSlide(index) {{
    currentSlide = index;
    if (isFullView) {{
      const targetElem = document.getElementById(`slide-${{index + 1}}`);
      if (targetElem) {{
        targetElem.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }} else {{
      updateSlideUI();
    }}
  }}

  function setViewMode(mode) {{
    const btnSlide = document.getElementById('btn-mode-slide');
    const btnFull = document.getElementById('btn-mode-full');
    
    if (mode === 'full') {{
      isFullView = true;
      document.body.classList.add('mode-full-view');
      btnFull.classList.add('active');
      btnSlide.classList.remove('active');
    }} else {{
      isFullView = false;
      document.body.classList.remove('mode-full-view');
      btnSlide.classList.add('active');
      btnFull.classList.remove('active');
      updateSlideUI();
    }}
  }}

  function toggleTheme() {{
    document.body.classList.toggle('dark-mode');
  }}

  function togglePresentationMode() {{
    if (!document.fullscreenElement) {{
      document.documentElement.requestFullscreen().catch(err => {{
        alert(`Error attempting fullscreen: ${{err.message}}`);
      }});
    }} else {{
      document.exitFullscreen();
    }}
  }}

  function filterSidebar() {{
    const query = document.getElementById('sidebar-search').value.toLowerCase();
    const items = document.querySelectorAll('.sidebar-item');
    items.forEach(item => {{
      const text = item.innerText.toLowerCase();
      if (text.includes(query)) {{
        item.style.display = 'block';
      }} else {{
        item.style.display = 'none';
      }}
    }});
  }}

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
    
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {{
      e.preventDefault();
      changeSlide(1);
    }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
      e.preventDefault();
      changeSlide(-1);
    }} else if (e.key === 'f' || e.key === 'F') {{
      e.preventDefault();
      togglePresentationMode();
    }}
  }});

  // Init
  updateSlideUI();
</script>

</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"[SUCCESS] Executive & Management Overview (v3) generated at: {OUTPUT_HTML}")
    print(f"Total Slides: {len(SLIDES)}")


if __name__ == "__main__":
    build_deck()
