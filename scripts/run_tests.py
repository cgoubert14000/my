"""Run every automated test suite and write machine-readable + human-readable reports to docs/reports/.

  python scripts/run_tests.py            # forge (contracts) + pytest (backend) ; devnet tests run only if anvil is up
  python scripts/run_tests.py --no-forge # backend only

The runtime reads docs/reports/pytest_results.json and forge_tests.json at startup to set the maturity flags
`tests_passed`, `contract_tested`, `financial_math_validated` — a red suite therefore blocks live mode.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPORTS = ROOT / "docs" / "reports"
PY = sys.executable


def run(cmd: list[str], cwd: pathlib.Path, env: dict | None = None) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env={**os.environ, **(env or {})})
    return p.returncode, p.stdout + p.stderr


def forge_tests() -> dict:
    forge = shutil.which("forge") or str(pathlib.Path.home() / ".tools" / "bin" / "forge")
    if not pathlib.Path(forge).exists():
        return {"skipped": True, "reason": "forge not found (install Foundry)"}
    env = {}
    local_solc = pathlib.Path.home() / ".tools" / "bin" / "solc"
    if local_solc.exists():
        env = {"FOUNDRY_SOLC": str(local_solc), "FOUNDRY_OFFLINE": "true"}
    code, out = run([forge, "test", "--json"], ROOT / "contracts", env)
    suites: dict = {}
    try:
        # forge --json prints one JSON object (possibly after build logs); take the last line that parses
        for line in reversed(out.strip().splitlines()):
            try:
                suites = json.loads(line)
                break
            except json.JSONDecodeError:
                continue
    except Exception:  # noqa: BLE001
        suites = {}
    summary = {"ts": time.time(), "exit_code": code, "passed": 0, "failed": 0, "suites": {}}
    for path, suite in suites.items():
        name = path.split(":")[-1]
        res = {}
        for tname, t in suite.get("test_results", {}).items():
            ok = t.get("status") == "Success"
            summary["passed" if ok else "failed"] += 1
            gas = t.get("kind", {}).get("Unit", {}).get("gas") if isinstance(t.get("kind"), dict) else None
            res[tname] = {"ok": ok, "gas": gas, "runs": (t.get("kind", {}).get("Fuzz", {}) or {}).get("runs") if isinstance(t.get("kind"), dict) else None}
        summary["suites"][name] = res
    if not suites:
        summary["raw_tail"] = out[-2000:]
    return summary


def pytest_backend() -> dict:
    junit = REPORTS / "pytest_junit.xml"
    code, out = run([PY, "-m", "pytest", "tests", "-q", f"--junitxml={junit}"], ROOT / "backend")
    summary = {"ts": time.time(), "exit_code": code, "passed": 0, "failed": 0, "skipped": 0, "errors": 0, "tests": {}, "tail": out[-1500:]}
    if junit.exists():
        root = ET.parse(junit).getroot()
        for tc in root.iter("testcase"):
            name = f"{tc.get('classname')}::{tc.get('name')}"
            status = "passed"
            if tc.find("failure") is not None:
                status = "failed"
            elif tc.find("error") is not None:
                status = "error"
            elif tc.find("skipped") is not None:
                status = "skipped"
            summary["tests"][name] = {"status": status, "time": float(tc.get("time", 0))}
            summary[{"passed": "passed", "failed": "failed", "error": "errors", "skipped": "skipped"}[status]] += 1
    return summary


def markdown(forge: dict, py: dict) -> str:
    lines = [f"# Rapport d'exécution des tests — {time.strftime('%Y-%m-%d %H:%M:%S')}", ""]
    lines.append("## Contrats (Foundry)")
    if forge.get("skipped"):
        lines.append(f"- ignoré : {forge['reason']}")
    else:
        lines.append(f"- **{forge['passed']} réussis / {forge['failed']} échoués** (code de sortie {forge['exit_code']})")
        for suite, tests in forge.get("suites", {}).items():
            lines.append(f"- {suite} : {sum(1 for t in tests.values() if t['ok'])}/{len(tests)}")
            for name, t in sorted(tests.items()):
                extra = f" — gaz {t['gas']}" if t.get("gas") else (f" — {t['runs']} runs" if t.get("runs") else "")
                lines.append(f"  - {'✅' if t['ok'] else '❌'} {name}{extra}")
    lines += ["", "## Backend (pytest)", f"- **{py['passed']} réussis / {py['failed']} échoués / {py['skipped']} ignorés / {py['errors']} erreurs** (code de sortie {py['exit_code']})"]
    by_file: dict[str, list] = {}
    for name, t in py["tests"].items():
        by_file.setdefault(name.split("::")[0], []).append((name.split("::")[-1], t))
    for f, tests in sorted(by_file.items()):
        lines.append(f"- {f}")
        for n, t in tests:
            icon = {"passed": "✅", "failed": "❌", "error": "💥", "skipped": "⏭️"}[t["status"]]
            lines.append(f"  - {icon} {n} ({t['time']:.2f}s)")
    lines += ["", "Les tests `devnet` sont ignorés si anvil n'est pas démarré ; ils ont été exécutés ici si leur statut est ✅."]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-forge", action="store_true")
    a = ap.parse_args()
    REPORTS.mkdir(parents=True, exist_ok=True)
    forge = {"skipped": True, "reason": "--no-forge"} if a.no_forge else forge_tests()
    py = pytest_backend()
    (REPORTS / "forge_tests.json").write_text(json.dumps(forge, indent=1))
    (REPORTS / "pytest_results.json").write_text(json.dumps(py, indent=1))
    md = markdown(forge, py)
    (REPORTS / "tests_latest.md").write_text(md)
    print(md)
    ok = py["failed"] == 0 and py["errors"] == 0 and (forge.get("skipped") or forge["failed"] == 0)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
