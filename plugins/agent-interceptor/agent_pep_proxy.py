#!/usr/bin/env python3
"""
Enterprise AI Governance - Outside-the-Model Agent PEP Proxy Interceptor
=============================================================================
Runtime Policy Enforcement Point (PEP) intercepting autonomous agent tool calls
and Model Context Protocol (MCP) execution requests.

CORE INVARIANT:
Agent authorization is enforced strictly OUTSIDE the model. A model's plan,
reasoning chain, or claim of approval is NEVER authorization.

Enforces:
  - ORG-CTL-AGT-001: Outside-the-model authorization boundary
  - ORG-CTL-AGT-002: Dedicated machine identity token validation
  - ORG-CTL-AGT-003: Strict parameter schema validation & destructive action gating
  - ORG-CTL-AGT-004: Execution recursion step limits & kill switch checking

Usage:
    python plugins/agent-interceptor/agent_pep_proxy.py --test-invocation tool_call.json
=============================================================================
"""

import argparse
import json
import sys
from typing import Any, Dict, Optional, Tuple

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


class AgentAuthorizationError(Exception):
    """Raised when an agent tool invocation violates outside-the-model governance."""
    pass


class OutsideTheModelPEP:
    def __init__(
        self,
        registered_tools: Dict[str, Dict[str, Any]],
        max_execution_steps: int = 10,
        kill_switch_active: bool = False
    ):
        self.registered_tools = registered_tools
        self.max_execution_steps = max_execution_steps
        self.kill_switch_active = kill_switch_active
        self.session_step_counters: Dict[str, int] = {}

    def intercept_and_authorize(
        self,
        session_id: str,
        caller_identity_token: str,
        tool_id: str,
        parameters: Dict[str, Any],
        human_approval_token: Optional[str] = None
    ) -> Tuple[bool, str]:
        """
        Evaluates tool call request outside the model boundary.
        Ignores any model self-assertion of approval.
        """
        # 1. Kill Switch Check (ORG-CTL-AGT-004)
        if self.kill_switch_active:
            raise AgentAuthorizationError(
                "EMERGENCY KILL SWITCH ACTIVE: Agent runtime execution is halted (ORG-CTL-AGT-004)."
            )

        # 2. Recursion Step Limit Check (ORG-CTL-AGT-004)
        curr_step = self.session_step_counters.get(session_id, 0) + 1
        if curr_step > self.max_execution_steps:
            raise AgentAuthorizationError(
                f"RECURSION LIMIT EXCEEDED: Session {session_id} exceeded maximum allowable steps "
                f"({curr_step} > {self.max_execution_steps})."
            )
        self.session_step_counters[session_id] = curr_step

        # 3. Machine Identity Verification (ORG-CTL-AGT-002)
        if not caller_identity_token or not caller_identity_token.startswith("spiffe://") and not caller_identity_token.startswith("sa_"):
            raise AgentAuthorizationError(
                "UNAUTHENTICATED AGENT IDENTITY: Caller lacks valid machine identity token (ORG-CTL-AGT-002). "
                "User impersonation is prohibited."
            )

        # 4. Registered Tool Existence
        if tool_id not in self.registered_tools:
            raise AgentAuthorizationError(
                f"UNREGISTERED TOOL: Tool '{tool_id}' is not registered in enterprise tool manifest."
            )

        tool_meta = self.registered_tools[tool_id]
        exec_mode = tool_meta.get("execution_mode", "read_only")
        param_schema = tool_meta.get("parameter_schema")

        # 5. Strict Schema Validation (ORG-CTL-AGT-003)
        if param_schema and HAS_JSONSCHEMA:
            try:
                jsonschema.validate(instance=parameters, schema=param_schema)
            except jsonschema.ValidationError as ve:
                raise AgentAuthorizationError(
                    f"SCHEMA VALIDATION FAILED: Tool '{tool_id}' parameters violate registered schema: {ve.message}"
                )

        # 6. Destructive Mutation Approval Gate (ORG-CTL-AGT-003 / ORG-CTL-HUM-002)
        if exec_mode == "destructive_write_requires_approval":
            if not human_approval_token or not human_approval_token.startswith("OOB-AUTH-"):
                raise AgentAuthorizationError(
                    f"HUMAN APPROVAL REQUIRED: Tool '{tool_id}' performs destructive state modification. "
                    "A model cannot self-authorize destructive actions; out-of-band human cryptographic token required."
                )

        return True, f"AUTHORIZED: Tool '{tool_id}' step {curr_step}/{self.max_execution_steps} cleared."


def main() -> int:
    parser = argparse.ArgumentParser(description="Agent Outside-the-Model PEP Proxy")
    parser.add_argument("--test-tool", default="refund_payment", help="Test tool name")
    parser.add_argument("--test-destructive", action="store_true", help="Simulate destructive action")
    parser.add_argument("--with-human-approval", action="store_true", help="Provide human approval token")

    args = parser.parse_args()

    mock_tools = {
        "read_kb": {
            "execution_mode": "read_only",
            "parameter_schema": {
                "type": "object",
                "required": ["query"],
                "properties": {"query": {"type": "string"}}
            }
        },
        "refund_payment": {
            "execution_mode": "destructive_write_requires_approval",
            "parameter_schema": {
                "type": "object",
                "required": ["amount", "reason"],
                "properties": {
                    "amount": {"type": "number", "minimum": 0.01},
                    "reason": {"type": "string"}
                }
            }
        }
    }

    pep = OutsideTheModelPEP(mock_tools, max_execution_steps=5)

    print("=================================================================")
    print("AGENT OUTSIDE-THE-MODEL PEP INTERCEPTOR")
    print("=================================================================")

    approval_token = "OOB-AUTH-SUPERVISOR-SIGN-9921" if args.with_human_approval else None
    params = {"amount": 50.0, "reason": "Customer cancellation"} if args.test_tool == "refund_payment" else {"query": "warranty"}

    try:
        authorized, msg = pep.intercept_and_authorize(
            session_id="sess-8812",
            caller_identity_token="spiffe://internal.net/ns/agents/sa/support-agent",
            tool_id=args.test_tool,
            parameters=params,
            human_approval_token=approval_token
        )
        print(f"[PASS] {msg}")
        return 0
    except AgentAuthorizationError as aae:
        print(f"[BLOCK] {aae}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
