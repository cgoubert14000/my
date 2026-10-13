#!/usr/bin/env python
"""Serve docs/live/ + the latest real-market snapshots, refreshed from the Git branch every minute.

Useful when the machine serving the page cannot reach the blockchain itself (the data is produced elsewhere — e.g.
by the GitHub Actions job — and published to the branch). Nothing is generated here: files are copied verbatim
from `origin/<branch>`.

Usage: python scripts/live_mirror.py --branch arena/9aff96cd-my --port 8090 --every 60
"""
from __future__ import annotations

import argparse
import http.server
import pathlib
import shutil
import subprocess
import tempfile
import threading
import time

REPO = pathlib.Path(__file__).resolve().parents[1]


def sync(branch: str, out: pathlib.Path, log) -> None:
    subprocess.run(["git", "fetch", "-q", "origin", branch], cwd=REPO, check=False, timeout=120)
    ref = f"origin/{branch}"
    paths = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "docs/live", "docs/reports/real", "docs/reports"],
                           cwd=REPO, capture_output=True, text=True, timeout=60).stdout.split()
    n = 0
    for rel in paths:
        if not (rel.startswith("docs/live/") or rel.startswith("docs/reports/")):
            continue
        if rel.endswith(".csv") and "latest" not in rel:
            continue  # big files, not needed for the page
        data = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=REPO, capture_output=True, timeout=60).stdout
        dst = out / rel[len("docs/"):]
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists() or dst.read_bytes() != data:
            dst.write_bytes(data)
            n += 1
    head = subprocess.run(["git", "log", "-1", "--format=%h %cI %s", ref], cwd=REPO, capture_output=True, text=True, timeout=60).stdout.strip()
    log(f"sync {ref}: {n} file(s) updated — head {head}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", required=True)
    ap.add_argument("--port", type=int, default=8090)
    ap.add_argument("--every", type=float, default=60)
    args = ap.parse_args()
    out = pathlib.Path(tempfile.mkdtemp(prefix="arbbot-live-"))

    def log(m: str) -> None:
        print(time.strftime("%H:%M:%S"), m, flush=True)

    def loop() -> None:
        while True:
            try:
                sync(args.branch, out, log)
            except Exception as e:  # noqa: BLE001
                log(f"sync failed: {e!r}")
            time.sleep(args.every)

    threading.Thread(target=loop, daemon=True).start()
    (out / "index.html").write_text('<meta http-equiv="refresh" content="0; url=live/">')

    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(out), **k)

        def end_headers(self):
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

        def log_message(self, *a):  # quiet
            pass

    log(f"serving {out} on 0.0.0.0:{args.port} (branch {args.branch}, refresh every {args.every:.0f} s)")
    http.server.ThreadingHTTPServer(("0.0.0.0", args.port), H).serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
