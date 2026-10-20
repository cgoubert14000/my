#!/usr/bin/env bash
# Vinted Sniper — installation + lancement en une commande.
# Usage : ./run.sh [--port 9000] [--host 0.0.0.0] [--turbo] ...
set -euo pipefail
cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"
if ! command -v "$PYTHON" >/dev/null 2>&1; then
  if command -v python >/dev/null 2>&1; then
    PYTHON=python
  else
    echo "❌ Python 3.10+ est requis. Installez-le depuis https://www.python.org/downloads/"
    exit 1
  fi
fi

if [ ! -d .venv ]; then
  echo "📦 Création de l'environnement virtuel (.venv)…"
  "$PYTHON" -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

STAMP=".venv/.requirements.sha256"
if command -v sha256sum >/dev/null 2>&1; then
  CURRENT="$(sha256sum requirements.txt | cut -d' ' -f1)"
else
  CURRENT="$(shasum -a 256 requirements.txt | cut -d' ' -f1)"
fi
if [ ! -f "$STAMP" ] || [ "$(cat "$STAMP")" != "$CURRENT" ]; then
  echo "📥 Installation des dépendances…"
  python -m pip install --quiet --upgrade pip
  python -m pip install --quiet -r requirements.txt
  echo "$CURRENT" > "$STAMP"
fi

exec python main.py "$@"
