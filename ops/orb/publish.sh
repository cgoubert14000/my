#!/usr/bin/env bash
# Publie les rapports ORB (docs/reports/orb) dans la branche courante sans conflit : repart de la pointe distante,
# n'indexe que les fichiers de ce run (TAG) + latest_*, pousse en avance rapide (5 essais). Aucun secret n'est écrit.
set -u
cd "$(dirname "$0")/../.."
BRANCH="${GITHUB_REF_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
TAG="${ORB_RUN_TAG:-${GITHUB_RUN_ID:-}}"
git config user.name  >/dev/null 2>&1 || git config user.name "orb-bot"
git config user.email >/dev/null 2>&1 || git config user.email "actions@users.noreply.github.com"
git rebase --abort >/dev/null 2>&1 || true
collect() {
  [ -n "$TAG" ] && ls docs/reports/orb/*"$TAG"* docs/reports/orb/live/*"$TAG"* docs/reports/orb/live/*"$TAG"*/* 2>/dev/null
  find docs/reports/orb -maxdepth 1 -name 'latest_*' -mmin -30 2>/dev/null
}
for i in 1 2 3 4 5; do
  git fetch -q origin "$BRANCH" || { sleep 8; continue; }
  git reset -q --mixed "origin/$BRANCH"
  mapfile -t FILES < <(collect | sort -u)
  [ "${#FILES[@]}" -gt 0 ] && git add -f -- "${FILES[@]}" 2>/dev/null
  if git diff --cached --quiet; then echo "publish: nothing new"; exit 0; fi
  git commit -q -m "orb report $(date -u +%Y-%m-%dT%H:%M:%SZ) [skip ci]" || { echo "publish: commit failed"; exit 0; }
  if git push -q origin "HEAD:$BRANCH"; then echo "publish: pushed to $BRANCH ($(git rev-parse --short HEAD))"; exit 0; fi
  echo "publish: push rejected (attempt $i), retrying"; sleep 8
done
echo "publish: failed after 5 attempts"; exit 0
