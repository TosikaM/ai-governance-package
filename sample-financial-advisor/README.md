# Sample Project: Autonomous Financial & Portfolio Advisor (Agentic AI)

## Business Overview
This AI application analyzes wealth management portfolios, provides rebalancing recommendations, and triggers automated fund transfers via banking APIs.

## Why This is High-Risk (Tier 3 Autonomous Agent)
Because this AI system can execute real-world financial transactions (`execute_fund_transfer`), it is classified as an **Autonomous Agent System**. An unconstrained autonomous agent could trigger runaway fund transfers or execute unauthorized transactions if exploited via prompt injection.

## What Was Caught as Non-Compliant (Before Governance)
1. **Unconstrained Tool Execution:** The agent could trigger unlimited transfers with zero human confirmation.
2. **Missing Statutory Retention:** Transaction logs and customer prompts lacked a documented SEC/FINRA 7-year audit retention policy (`POL-RET-01`).
3. **No CI/CD PR Quality Gate:** The project had no automated pipeline barrier blocking merge if error rates or hallucination rates increased.

## How Governance Was Plugged In & Remediated (After Governance)
1. **Dual-Key Policy Interceptor:** Enforced dual-key authorization for transfers over $500.
2. **Autonomous Agent Overlay Bound:** Auto-bound `ORG-OVL-ARC-AGENT-001`, locking recursion depth <= 3 and human escalation.
3. **Data Card Configured:** SEC/FINRA 7-year statutory audit retention formally registered in `governance-cards/data-card.yaml`.
4. **Audit Report Generated:** Visual compliance audit report generated at `governance-compliance-report.html`.
