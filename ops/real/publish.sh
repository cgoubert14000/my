#!/usr/bin/env bash
# Publie les fichiers de la session réelle (docs/reports/real, docs/reports/verify_chain_*) dans la branche courante.
# Appelé après chaque instantané (toutes les 2 min) et à la fin de la session. Aucun secret n'est écrit.
#
# Méthode sans conflit : on repart de la pointe distante (fetch + reset --mixed), on n'indexe QUE les fichiers de
# rapport locaux (les nôtres sont toujours les plus récents : latest_<chain>.*, history_<chain>_<run>.jsonl, journal de
# session) et on pousse en avance rapide. Un rebase classique entrait en conflit dès qu'une autre session avait
# modifié les mêmes fichiers (observé sur la session 38434686316).
set -u
cd "$(dirname "$0")/../.."
BRANCH="${GITHUB_REF_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
git config user.name  >/dev/null 2>&1 || git config user.name "real-market-bot"
git config user.email >/dev/null 2>&1 || git config user.email "actions@users.noreply.github.com"
# un rebase/merge resté en suspens (ancienne version du script) ne doit jamais bloquer la publication
git rebase --abort >/dev/null 2>&1 || true
git merge --abort  >/dev/null 2>&1 || true
# Seuls les fichiers de CETTE session sont indexés (jamais `add -A` : le clone du runner ne connaît pas les fichiers
# publiés entre-temps par d'autres sessions et les supprimerait).
TAG="${ARB_RUN_TAG:-${GITHUB_RUN_ID:-}}"
collect() {
  if [ -n "$TAG" ]; then
    ls docs/reports/real/*"$TAG"* 2>/dev/null
  else
    find docs/reports/real -type f -mmin -600 2>/dev/null
  fi
  # fichiers à nom stable : uniquement s'ils viennent d'être (ré)écrits par cette session
  find docs/reports/real -maxdepth 1 \( -name 'latest_*' -o -name 'sessions_*' -o -name 'observations_*' \) -mmin -15 2>/dev/null
  find docs/reports -maxdepth 1 -name 'verify_chain_*' -mmin -600 2>/dev/null
}
# tableau inter-sessions (lecture seule des rapports déjà écrits)
python3 scripts/sessions_summary.py "${ARB_CHAIN:-base}" >/dev/null 2>&1 || true
for i in 1 2 3 4 5; do
  git fetch -q origin "$BRANCH" || { sleep 8; continue; }
  git reset -q --mixed "origin/$BRANCH"
  mapfile -t FILES < <(collect | sort -u)
  [ "${#FILES[@]}" -gt 0 ] && git add -f -- "${FILES[@]}" 2>/dev/null
  if git diff --cached --quiet; then echo "publish: nothing new"; exit 0; fi
  git commit -q -m "real-market snapshot $(date -u +%Y-%m-%dT%H:%M:%SZ) [skip ci]" || { echo "publish: commit failed"; exit 0; }
  if git push -q origin "HEAD:$BRANCH"; then echo "publish: pushed to $BRANCH ($(git rev-parse --short HEAD))"; exit 0; fi
  echo "publish: push rejected (attempt $i), retrying from the new remote tip"
  sleep 8
done
echo "publish: failed after 5 attempts (will retry at next snapshot)"; exit 0
