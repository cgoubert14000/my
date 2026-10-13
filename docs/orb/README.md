# ORB / OPR — Opening Range Breakout : backtest exhaustif + exécution temps réel

Système complet, indépendant du bot d'arbitrage, construit à partir de la stratégie décrite dans la vidéo
(« range d'ouverture de New York, cassure, retest FVG, RR 1/2/3, 900+ variantes en Python »), mais **vérifié** :
données réelles, coûts, validation hors échantillon, et un moteur temps réel qui exécute *exactement* le code testé.

> Statut d'honnêteté : les chiffres de la vidéo (« profit factor 1,75, > 2 avec filtres ») sont une affirmation
> marketing que nous **testons**, pas une vérité. Le rapport réel se trouve dans `docs/reports/orb/latest_XAUUSD.md`
> (produit par GitHub Actions sur les bougies Dukascopy). Aucun résultat n'est annoncé tant qu'il n'y figure pas.

## 1. Ce qui est fourni

| Composant | Fichier | Rôle |
|---|---|---|
| Stratégie | `orb/orbbot/strategy/orb.py` | Machine à états par séance : range, cassure (clôture ou FVG + retest), stop (borne opposée / milieu / structure), objectif RR, TP partiel + break-even, filtre EMA, 1 ou 2 trades/jour, heure limite, clôture 15:55 NY. **Le même objet sert au backtest et au temps réel.** |
| Variantes | `orb/orbbot/strategy/params.py` | Grille 3 × 2 × 3 × 3 × 3 × 2 × 2 × 2 = 1 296 combinaisons → **1 080 variantes distinctes** (le TP partiel n'a pas de sens avec RR 1). `VIDEO_CLAIM` = la variante annoncée (or, 30 min, FVG, RR 1). |
| Données | `orb/orbbot/data/dukascopy.py` | Bougies 1 min BID Dukascopy (flux public, gratuit), décodage LZMA auto-vérifié (ordre des colonnes, échelle), cache local `data/orb/` (jamais versionné). |
| Backtest | `orb/orbbot/backtest/` | Séances New York (heure d'été/hiver), EMA continues, exécution parallèle, métriques, **in-sample / out-of-sample 60/40, walk-forward annuel, bootstrap (IC 95 % du profit factor), sensibilité aux coûts, avertissement de biais de sélection**, verdict. |
| Temps réel | `orb/orbbot/live/` | Flux OANDA v20 (M1 clôturées, polling 5 s) ou rejeu ; courtier `PaperBroker` (fictif) ou `OandaBroker` (ordres au marché avec stop/objectif serveur, clôture partielle, déplacement du stop) ; politique de risque gelée ; kill switch ; journal JSONL + état. |
| Politique | `ops/orb/policy.json` | Risque 0,5 %/trade, perte max 2 R/jour, 2 trades/jour, 5 unités max, 6 pertes consécutives ⇒ suspension, `mode=paper`. Le bot ne la modifie jamais (empreinte SHA-256 journalisée). |
| Automatisation | `.github/workflows/orb-backtest.yml`, `orb-paper.yml` | Backtest réel à chaque modification de `ops/orb/backtest.json` ; séance paper quotidienne (13:15 UTC) si le secret `OANDA_TOKEN` existe. |
| Tests | `orb/tests/` | 25 tests exécutés : chaque règle de la stratégie sur des scénarios à résultat connu, décodage Dukascopy, heure d'été/hiver, grille parallèle = séquentielle, rapport, **rejeu temps réel == backtest**, politique, kill switch. |

## 2. Règles exactes de la stratégie (ce que le code fait, sans ambiguïté)

- Séance : bougies 1 min de 09:30 à 16:00 heure de New York (fuseau `America/New_York`, DST géré). Journées avec moins de 200 bougies ignorées.
- Range : plus haut / plus bas des bougies `[09:30, 09:30 + R)` avec R ∈ {5, 15, 30}.
- Cassure : clôture 1 min au-dessus du haut (achat) ou sous le bas (vente).
  - `close` : entrée **au marché à l'ouverture de la bougie suivante**.
  - `fvg` : après la cassure, première Fair Value Gap dans le sens du mouvement (haussière : `low[i] > high[i-2]`) ; **ordre limite au bord proche de la zone** ; si le prix reclôture dans le range avant qu'une FVG n'apparaisse, signal abandonné ; retest non survenu avant l'heure limite ⇒ annulé.
- Stop : `opposite` = autre borne du range ; `mid` = milieu du range ; `structure` = plus bas/haut de la bougie de cassure (`close`) ou bord éloigné de la FVG (`fvg`).
- Objectif : entrée ± RR × (entrée − stop), RR ∈ {1, 2, 3}. `partial` : 50 % à 1 R puis stop au point d'entrée, le reste à RR.
- Filtre `ma` : EMA 50 ou 200 sur les clôtures 1 min (série continue) ; achat seulement si clôture de cassure > EMA, vente si < EMA.
- `max_trades` 2 : un second signal est pris si le prix a reclôturé dans le range (même sens) ou dans l'autre sens.
- Heure limite d'entrée 11:30 ou 13:00 NY ; tout est fermé à 15:55 NY.
- Coûts : bougies BID ; achat à bid + spread, vente à bid ; slippage sur ordres au marché et stops (or : spread 0,30 $, slippage 0,05 $ ; EURUSD : 1,0 pip / 0,2 pip). Dans une même bougie, stop prioritaire sur l'objectif ; dans la bougie d'entrée d'un retest FVG seul le stop est vérifié (hypothèses défavorables).
- Résultats en **R** (multiple du risque initial) : indépendants de la taille du compte.

## 3. Lire le rapport (et ne pas se faire piéger)

`docs/reports/orb/backtest_<INSTRUMENT>_<run>.md` contient dans l'ordre :

1. **Verdict** : `FIABILITÉ NON DÉMONTRÉE` tant que la variante sélectionnée n'a pas ≥ 100 trades hors échantillon, un PF hors échantillon > 1, une borne basse d'IC 95 % > 1 **et** un walk-forward positif ; sinon `ROBUSTESSE PLAUSIBLE HORS ÉCHANTILLON — À CONFIRMER EN PAPER TRADING`. Jamais « rentable ».
2. La variante au meilleur PF **in-sample** et ce qu'elle donne **out-of-sample** (c'est la seule colonne qui compte).
3. Les 10 meilleures in-sample vues hors échantillon, la part de toutes les variantes avec PF OOS > 1, la corrélation de rang IS/OOS.
4. Walk-forward : chaque année, la meilleure variante des années précédentes appliquée en aveugle — ce qu'une sélection automatique aurait réellement produit.
5. La variante « vidéo » (or, 30 min, FVG, RR 1) avec IC bootstrap et détail par année.
6. Sensibilité aux coûts (spread × 1,5 et × 2).

Pour référence, la même grille sur une **marche aléatoire** (aucune information) donne : PF médian OOS ≈ 0,8, ≈ 20 % des variantes avec PF OOS > 1, meilleure in-sample PF 1,87 → OOS 0,88. C'est à cela qu'il faut comparer un « PF 1,75 » obtenu en choisissant la meilleure de 1 000 variantes.

## 4. Installation (Windows, PowerShell)

```powershell
cd C:\chemin\vers\my
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e "orb[dev]"
cd orb; python -m pytest tests -q; cd ..
```

## 5. Backtest sur données réelles

```powershell
# télécharge (cache data\orb) et teste 1 080 variantes sur l'or depuis 2022 ; rapport dans docs\reports\orb
orbbot backtest --instrument XAUUSD --start 2022-01-01 --grid full
orbbot backtest --instrument EURUSD --start 2022-01-01 --grid full
# grille réduite (32 variantes) pour un essai rapide
orbbot backtest --instrument XAUUSD --start 2024-01-01 --grid quick
# démonstration hors ligne sur données synthétiques (résultats sans valeur, étiquetés comme tels)
orbbot backtest --instrument XAUUSD --start 2024-01-01 --end 2024-06-30 --synthetic
```

Sur GitHub : modifier `run` dans `ops/orb/backtest.json`, pousser ; le workflow `orb-backtest` télécharge, calcule, publie `docs/reports/orb/backtest_*_<run_id>.{md,json}`, `trades_*.csv` et `latest_<INSTRUMENT>.md`.

## 6. Temps réel, 100 % automatique

Le moteur a besoin d'un flux de prix 1 min et d'un courtier. Choix retenu : **OANDA** (compte de démonstration gratuit,
API REST v20, or et forex, pas de MT5 requis). Étapes :

1. Créer un compte de démonstration OANDA (fxpractice), générer un jeton dans *Manage API Access*, noter l'identifiant de compte.
2. Sur le PC :
   ```powershell
   $env:OANDA_TOKEN = "votre-jeton"
   orbbot policy-check --policy ops\orb\policy.json
   orbbot live --policy ops\orb\policy.json --broker paper          # prix réels, exécution fictive, journal docs\reports\orb\live\
   $env:OANDA_ACCOUNT_ID = "101-004-XXXXXXX-001"
   orbbot live --policy ops\orb\policy.json --broker oanda          # ordres réels sur le compte de DÉMONSTRATION (mode oanda_practice requis dans la politique)
   orbbot live --policy ops\orb\policy.json --broker replay --replay-start 2025-09-01 --replay-end 2025-09-30   # rejeu local
   ```
3. Sur GitHub (sans PC allumé) : ajouter le secret `OANDA_TOKEN` → le workflow `orb-paper` ouvre une séance chaque jour ouvré à 13:15 UTC et publie le journal (`docs/reports/orb/live/<run_id>/journal.jsonl`, `state.json`).
4. Arrêt d'urgence : créer le fichier `ops/orb/STOP` (localement ou dans la branche) → plus aucune entrée, position fermée au marché.

Garde-fous : `enabled=false` ou `mode=paper` ⇒ aucun ordre réel ; `oanda_live` n'est jamais sélectionné par le bot ;
taille = capital × 0,5 % / (entrée − stop), bornée à `max_units` ; stop et objectif portés par le serveur OANDA
(une coupure du bot ne laisse pas de position sans protection) ; limite de temps ⇒ fermeture au marché.

**Non testé en conditions réelles** : l'adaptateur OANDA (ordres, clôture partielle, déplacement du stop) est écrit
d'après la documentation v20 mais l'environnement de développement n'a aucun accès réseau vers OANDA. Première séance
obligatoirement en `--broker paper`, puis compte de démonstration, et jamais de compte réel sans décision humaine
explicite et sans un rapport de backtest au verdict favorable.

## 7. Ce que ce système ne promet pas

- Aucun rendement. Un profit factor hors échantillon > 1 sur 2022–2026 n'implique rien sur 2027.
- Le taux de réussite d'une variante RR 1 tourne autour de 50 % par construction ; « 75 % de trades gagnants » ne se produit qu'avec des objectifs plus petits que le risque (et un PF qui n'en est pas meilleur).
- Les coûts réels (spread variable aux annonces, slippage sur gap) peuvent être supérieurs aux hypothèses ; d'où la table de sensibilité.
- La vidéo mélange une stratégie publique et la promotion d'un séminaire : la seule chose qui compte est le rapport.
