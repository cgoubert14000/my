# Backtest ORB — EURUSD

Généré le 2026-10-14T02:11:05+00:00 · données : 1247 séances New York du 2022-01-03 au 2026-10-13 (in-sample 748 séances < 2024-11-14 ; out-of-sample 499 séances) · 1080 variantes · coûts : spread 0.0001 , slippage 2e-05 (unités de prix, par exécution au marché/stop).

> Source : Dukascopy 1 min BID, 2155680 bougies (1497 jours), statut téléchargement {'requested': 1497, 'cached': 1494, 'downloaded': 3} (téléchargement du 2026-10-14).

## Verdict : **FIABILITÉ NON DÉMONTRÉE**

- profit factor hors échantillon 0.80 ≤ 1
- borne basse (IC 95 %) du PF hors échantillon 0.65 ≤ 1
- walk-forward : 969 trades, PF 0.77

> Rappel : avec 1080 variantes testées, la meilleure in-sample paraît toujours excellente même sans aucun avantage réel (biais de sélection). Seules les colonnes **hors échantillon** et le **walk-forward** sont informatives, et elles restent des estimations sur un passé limité — pas une promesse de rendement.

## Variante sélectionnée (meilleur profit factor in-sample)

`R30_close_rr2_opposite_ma0_p1_n1_cut1300` — range 30 min, clôture hors range, RR 2, stop = borne opposée, entrées jusqu'à 13:00, TP partiel 1R + break-even

| période | trades | win rate | profit factor | espérance (R) | max DD (R) | plus longue série perdante |
|---|---|---|---|---|---|---|
| in-sample | 734 | 48.9 % | 1.00 | 0.000 | 52.3 | 8 |
| out-of-sample | 492 | 46.1 % | 0.80 | -0.096 | 49.5 | 13 |
| total | 1226 | 47.8 % | 0.91 | -0.039 | 95.8 | 13 |

IC bootstrap 95 % du PF hors échantillon : [0.65 ; 0.97] ; probabilité (bootstrap) que le PF hors échantillon soit < 1 : 98.9 %.

| année | trades | win rate | PF | total R | max DD R |
|---|---|---|---|---|---|
| 2022 | 257 | 57.2 % | 1.47 | 42.5 | 8.3 |
| 2023 | 255 | 43.9 % | 0.81 | -21.5 | 24.4 |
| 2024 | 255 | 43.9 % | 0.75 | -32.3 | 34.8 |
| 2025 | 258 | 49.2 % | 0.93 | -7.9 | 18.1 |
| 2026 | 201 | 43.8 % | 0.72 | -28.2 | 34.3 |

Sorties (toutes périodes) : {'be': 143, 'sl': 491, 'time': 444, 'tp2': 148} · longs 606 / shorts 620

## Que valent les 10 meilleures variantes in-sample une fois hors échantillon ?

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 734 / 48.9 % / 1.00 / 0.000 / 52.3 | 492 / 46.1 % / 0.80 / -0.096 / 49.5 |
| `R30_close_rr2_opposite_ma50_p1_n1_cut1300` | 734 / 48.9 % / 1.00 / 0.000 / 52.3 | 492 / 46.1 % / 0.80 / -0.096 / 49.5 |
| `R15_close_rr3_opposite_ma200_p1_n1_cut1130` | 736 / 49.3 % / 1.00 / 0.000 / 54.5 | 493 / 43.6 % / 0.69 / -0.167 / 84.5 |
| `R15_close_rr3_opposite_ma200_p1_n1_cut1300` | 743 / 49.4 % / 1.00 / -0.000 / 54.3 | 495 / 43.6 % / 0.69 / -0.166 / 84.2 |
| `R30_close_rr2_opposite_ma200_p1_n1_cut1300` | 734 / 49.0 % / 1.00 / -0.001 / 51.4 | 491 / 47.7 % / 0.85 / -0.068 / 39.6 |
| `R30_close_rr3_opposite_ma200_p1_n1_cut1300` | 734 / 49.0 % / 1.00 / -0.001 / 50.8 | 491 / 47.7 % / 0.85 / -0.070 / 41.8 |
| `R30_close_rr3_opposite_ma0_p1_n1_cut1300` | 734 / 48.9 % / 0.99 / -0.002 / 50.5 | 492 / 46.1 % / 0.78 / -0.104 / 52.6 |
| `R30_close_rr3_opposite_ma50_p1_n1_cut1300` | 734 / 48.9 % / 0.99 / -0.002 / 50.5 | 492 / 46.1 % / 0.78 / -0.104 / 52.6 |
| `R30_close_rr2_opposite_ma200_p1_n1_cut1130` | 712 / 48.9 % / 0.99 / -0.003 / 51.0 | 477 / 47.8 % / 0.86 / -0.064 / 38.5 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1130` | 721 / 48.7 % / 0.99 / -0.004 / 53.2 | 480 / 46.2 % / 0.80 / -0.095 / 47.6 |

Sur l'ensemble des variantes avec ≥ 20 trades hors échantillon (1080) : PF médian in-sample 0.68, PF médian hors échantillon 0.62, part des variantes avec PF hors échantillon > 1 : 0.0 %, corrélation de rang IS/OOS : 0.95 (proche de 0 ⇒ le classement in-sample ne prédit pas la suite).

## Walk-forward (sélection automatique année après année)

Chaque année, la variante au meilleur PF sur toutes les années précédentes est appliquée en aveugle à l'année suivante.

| année testée | variante retenue (PF / n en apprentissage) | trades | win rate | PF | total R |
|---|---|---|---|---|---|
| 2023 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (1.49 / 257) | 255 | 43.9 % | 0.83 | -19.0 |
| 2024 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (1.12 / 512) | 255 | 43.9 % | 0.70 | -38.5 |
| 2025 | `R15_close_rr3_opposite_ma200_p1_n1_cut1130` (0.98 / 769) | 258 | 47.7 % | 0.79 | -27.3 |
| 2026 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (0.98 / 1024) | 201 | 44.8 % | 0.76 | -23.8 |
| **total** | | 969 | 45.1 % | 0.77 | -108.6 |

IC bootstrap 95 % du PF walk-forward : [0.67 ; 0.88].

## La variante annoncée dans la vidéo (or, range 30 min, retest FVG, RR 1, « PF ≈ 1,75 »)

`R30_fvg_rr1_structure_ma0_p0_n1_cut1130` — range 30 min, cassure + retest FVG, RR 1, stop = structure (bougie/FVG), entrées jusqu'à 11:30

| période | trades | win rate | profit factor | espérance (R) | max DD (R) |
|---|---|---|---|---|---|
| in-sample | 533 | 27.0 % | 0.34 | -0.532 | 284.7 |
| out-of-sample | 362 | 19.3 % | 0.22 | -0.701 | 253.7 |
| total | 895 | 23.9 % | 0.28 | -0.600 | 537.4 |

IC bootstrap 95 % du PF (toutes périodes) : [0.25 ; 0.33] — probabilité que le vrai PF soit < 1 : 100.0 %.

| année | trades | win rate | PF | total R |
|---|---|---|---|---|
| 2022 | 187 | 27.8 % | 0.35 | -96.2 |
| 2023 | 192 | 28.1 % | 0.36 | -96.8 |
| 2024 | 176 | 23.9 % | 0.28 | -106.5 |
| 2025 | 194 | 21.6 % | 0.25 | -125.9 |
| 2026 | 146 | 16.4 % | 0.18 | -112.1 |

## Meilleures variantes hors échantillon (a posteriori — information, pas sélection)

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R30_fvg_rr2_opposite_ma0_p0_n2_cut1130` | 718 / 40.8 % / 0.93 / -0.037 / 49.7 | 500 / 41.0 % / 0.95 / -0.028 / 35.3 |
| `R30_fvg_rr2_opposite_ma50_p0_n2_cut1130` | 718 / 40.8 % / 0.93 / -0.037 / 49.7 | 500 / 41.0 % / 0.95 / -0.028 / 35.3 |
| `R30_fvg_rr3_opposite_ma200_p0_n2_cut1130` | 703 / 39.8 % / 0.91 / -0.048 / 52.5 | 481 / 40.1 % / 0.94 / -0.031 / 34.0 |
| `R30_fvg_rr3_opposite_ma200_p0_n1_cut1130` | 593 / 40.6 % / 0.93 / -0.035 / 43.5 | 400 / 38.2 % / 0.94 / -0.033 / 29.6 |
| `R30_fvg_rr2_opposite_ma200_p0_n2_cut1130` | 703 / 41.1 % / 0.92 / -0.043 / 52.7 | 481 / 41.6 % / 0.94 / -0.033 / 34.5 |

## Sensibilité aux coûts et au stop minimal (variante sélectionnée et variante « vidéo »)

Ligne « spread 0 » = aucun coût : c'est l'avantage brut de la règle ; « stop min. » = distance entrée-stop minimale acceptée (les trades au stop plus serré sont ignorés).

| variante | spread | slippage | stop min. | trades | win rate | PF | espérance (R) | max DD (R) |
|---|---|---|---|---|---|---|---|---|
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0 | 0.0 | 0.0001 | 1226 | 51.7 % | 1.12 | 0.048 | 22.1 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0001 | 2e-05 | 0.0001 | 1226 | 47.8 % | 0.91 | -0.039 | 95.8 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.00015 | 3e-05 | 0.0001 | 1226 | 45.3 % | 0.82 | -0.082 | 140.2 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0002 | 4e-05 | 0.0001 | 1226 | 43.4 % | 0.74 | -0.126 | 184.9 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0001 | 2e-05 | 0.0005 | 1226 | 47.8 % | 0.91 | -0.039 | 95.8 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0001 | 2e-05 | 0.001 | 1126 | 48.2 % | 0.94 | -0.028 | 80.5 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0 | 0.0 | 0.0001 | 747 | 44.6 % | 0.81 | -0.107 | 83.2 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0001 | 2e-05 | 0.0001 | 895 | 23.9 % | 0.28 | -0.600 | 537.4 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.00015 | 3e-05 | 0.0001 | 895 | 18.4 % | 0.20 | -0.744 | 666.1 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0002 | 4e-05 | 0.0001 | 895 | 14.6 % | 0.14 | -0.863 | 772.3 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0001 | 2e-05 | 0.0005 | 139 | 49.6 % | 0.96 | -0.021 | 10.6 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0001 | 2e-05 | 0.001 | 37 | 45.9 % | 0.83 | -0.090 | 4.2 |

## Méthode

- Bougies 1 minute BID Dukascopy (flux public), séances New York 09:30–16:00 (heure d'été/hiver gérée), journées < 200 bougies ignorées.
- Range = plus haut/plus bas des R premières minutes ; cassure = clôture 1 min au-delà ; entrée au marché à l'ouverture suivante (« close ») ou limite au bord de la première FVG après cassure (« fvg ») ; aucune entrée après l'heure limite ; tout est clôturé à 15:55 NY.
- Coûts : achat à bid + spread, vente à bid ; slippage sur ordres au marché et stops ; stop prioritaire sur l'objectif dans une même bougie ; dans la bougie d'entrée seul le stop est vérifié.
- In-sample = premiers 60 % des séances, out-of-sample = 40 % suivants ; sélection par PF in-sample (≥ 50 trades) ; IC par bootstrap (1 000 rééchantillonnages) ; walk-forward annuel.
- Résultats en R (risque initial par trade) : ils ne dépendent pas de la taille du compte ; aucun rendement en € n'est annoncé.
