#!/usr/bin/env python3
"""
Enterprise AI Governance - Universal MCP & REST Server Entrypoint
=============================================================================
Top-level entrypoint for the AI Governance MCP & REST Server.

Compatible with:
  1. Desktop AI Tools:
     - Claude Desktop, Claude Code, Cursor, Windsurf, VS Code (via stdio MCP)
     - ChatGPT Desktop, Perplexity Desktop (via HTTP/REST Actions)
  2. Cloud Generative AI:
     - ChatGPT Cloud Custom GPTs (via OpenAPI REST Actions)
     - Claude Cloud, Perplexity Cloud, Custom LLM APIs (OpenAI, Anthropic, Gemini)
  3. Cloud Repositories & Storage:
     - GitHub, SharePoint, Local Machines, AWS S3, Google Drive

Usage with Claude Desktop / Cursor (stdio):
    python mcp_server.py

Usage for ChatGPT Actions / Cloud REST / Remote MCP (port 3335):
    python mcp_server.py --transport http --port 3335
=============================================================================
"""

import sys
import os
import json
import argparse
from pathlib import Path

# Add workspace root to sys.path
REPO_ROOT = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from agents.mcp_server import (
    main as run_stdio_server,
    handle_request,
    handle_inspect,
    handle_auto_setup,
    handle_audit,
    handle_check_pr,
    handle_resolve,
    handle_list_policies,
    handle_explain_control
)
import yaml


def run_http_server(port: int = 3335):
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class UniversalAIHandler(BaseHTTPRequestHandler):
        def _send_cors(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

        def do_OPTIONS(self):
            self.send_response(200)
            self._send_cors()
            self.end_headers()

        def do_GET(self):
            if self.path == "/health":
                resp = json.dumps({"status": "ok", "server": "enterprise-ai-governance-mcp"}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(resp)))
                self._send_cors()
                self.end_headers()
                self.wfile.write(resp)

            elif self.path in ["/openapi.json", "/openapi.yaml"]:
                openapi_path = REPO_ROOT / "docs" / "openapi.yaml"
                if openapi_path.exists():
                    with open(openapi_path, "r", encoding="utf-8") as f:
                        data = yaml.safe_load(f)
                    if self.path == "/openapi.json":
                        resp = json.dumps(data, indent=2).encode("utf-8")
                        content_type = "application/json"
                    else:
                        resp = yaml.dump(data).encode("utf-8")
                        content_type = "application/x-yaml"
                    self.send_response(200)
                    self.send_header("Content-Type", content_type)
                    self.send_header("Content-Length", str(len(resp)))
                    self._send_cors()
                    self.end_headers()
                    self.wfile.write(resp)
                else:
                    self.send_response(404)
                    self.end_headers()

            else:
                self.send_response(404)
                self.end_headers()

        def do_POST(self):
            content_len = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_len).decode("utf-8") if content_len > 0 else "{}"
            try:
                body = json.loads(raw_body) if raw_body.strip() else {}
            except Exception:
                body = {}

            try:
                # 1. REST Endpoint: Inspect
                if self.path == "/api/inspect":
                    res = handle_inspect(body.get("target_dir", "."))
                # 2. REST Endpoint: Auto-Setup
                elif self.path == "/api/auto-setup":
                    res = handle_auto_setup(body.get("target_dir", "."))
                # 3. REST Endpoint: Audit
                elif self.path == "/api/audit":
                    res = handle_audit(
                        target_dir=body.get("target_dir", "."),
                        generate_html=body.get("generate_html", True),
                        output_filename=body.get("output_filename", "governance-compliance-report.html")
                    )
                # 4. REST Endpoint: Check PR
                elif self.path == "/api/check-pr":
                    res = handle_check_pr(body.get("target_dir", "."))
                # 5. REST Endpoint: List Policies
                elif self.path == "/api/list-policies":
                    res = handle_list_policies(body.get("policy_id"))
                # 6. REST Endpoint: Explain Control
                elif self.path == "/api/explain-control":
                    res = handle_explain_control(body.get("control_id", ""))
                # 7. Standard MCP JSON-RPC protocol over HTTP
                else:
                    res = handle_request(body)

                resp_bytes = json.dumps(res, indent=2).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(resp_bytes)))
                self._send_cors()
                self.end_headers()
                self.wfile.write(resp_bytes)

            except Exception as e:
                err_resp = json.dumps({"status": "error", "message": str(e)}).encode("utf-8")
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(err_resp)))
                self._send_cors()
                self.end_headers()
                self.wfile.write(err_resp)

    httpd = HTTPServer(("0.0.0.0", port), UniversalAIHandler)
    print(f"\n[AI-GOVERNANCE] Universal Server online!")
    print(f"  * MCP Endpoint:     http://localhost:{port}/")
    print(f"  * Health Check:     http://localhost:{port}/health")
    print(f"  * OpenAPI Schema:   http://localhost:{port}/openapi.json")
    print(f"  * REST Actions:     http://localhost:{port}/api/[inspect|auto-setup|audit|check-pr|explain-control]")
    print(f"Press Ctrl+C to stop.\n")
    httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description="Universal AI Governance MCP & REST Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http", "sse"],
        default="stdio",
        help="Server transport: 'stdio' for Claude Desktop/Cursor, 'http'/'sse' for ChatGPT Actions & Cloud REST"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=3335,
        help="HTTP port when running with --transport http (default: 3335)"
    )
    args = parser.parse_args()

    if args.transport == "stdio":
        run_stdio_server()
    else:
        run_http_server(port=args.port)


if __name__ == "__main__":
    main()
