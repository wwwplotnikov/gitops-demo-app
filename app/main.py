#!/usr/bin/env python3
"""
Крошечный веб-сервис для демонстрации GitOps.
Задача: отдавать свою версию (= тег образа = commit SHA),
чтобы наглядно видеть, какую версию ArgoCD выкатил в кластер.
"""
import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_VERSION = os.environ.get("APP_VERSION", "unknown")
PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self._json(200, {"status": "ok"})
        elif self.path == "/":
            self._json(200, {"service": "gitops-demo-app", "version": APP_VERSION})
        else:
            self._json(404, {"error": "not found"})

    def _json(self, code, payload):
        body = (json.dumps(payload) + "\n").encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"gitops-demo-app version={APP_VERSION} listening on :{PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
# trigger deploy
