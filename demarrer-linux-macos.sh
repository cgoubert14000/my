#!/usr/bin/env bash
# Vinted Sniper — lanceur Linux / macOS (aucune installation manuelle).
set -e
cd "$(dirname "$0")"

PY=""
for candidate in python3.12 python3.11 python3.10 python3 python; do
  if command -v "$candidate" >/dev/null 2>&1; then PY="$candidate"; break; fi
done
if [ -z "$PY" ]; then
  echo "Python 3.10+ est requis : https://www.python.org/downloads/"
  exit 1
fi

if [ ! -x ".venv/bin/python" ]; then
  echo "Première utilisation : installation (1 à 2 minutes)…"
  "$PY" -m venv .venv
  .venv/bin/python -m pip install --upgrade pip >/dev/null
  .venv/bin/python -m pip install -r requirements.txt
fi

echo "Dashboard : http://127.0.0.1:8000  (Ctrl+C pour arrêter)"
exec .venv/bin/python main.py
