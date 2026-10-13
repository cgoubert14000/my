#!/usr/bin/env bash
# Publie les instantanés de la session réelle dans la branche courante (appelé après chaque snapshot).
# Aucun secret : les fichiers sont des rapports JSON/MD/CSV + le journal de session.
set -u
cd "$(dirname "$0")/../.."
BRANCH="${GITHUB_REF_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
git config user.name  >/dev/null 2>&1 || git config user.name "real-market-bot"
git config user.email >/dev/null 2>&1 || git config user.email "actions@users.noreply.github.com"
git add -f docs/reports/real docs/reports/verify_chain_*.md docs/reports/verify_chain_*.json 2>/dev/null || true
if git diff --cached --quiet; then echo "publish: nothing new"; exit 0; fi
git commit -q -m "real-market snapshot $(date -u +%Y-%m-%dT%H:%M:%SZ) [skip ci]" || exit 0
for i in 1 2 3 4 5; do
  if git pull --rebase -q origin "$BRANCH" && git push -q origin "HEAD:$BRANCH"; then echo "publish: pushed to $BRANCH"; exit 0; fi
  sleep 8
done
echo "publish: push failed (will retry at next snapshot)"; exit 0
