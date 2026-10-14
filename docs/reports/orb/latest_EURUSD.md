# Backtest ORB — EURUSD

Généré le 2026-10-14T01:44:27+00:00 · données : 1238 séances New York du 2022-01-03 au 2026-10-13 (in-sample 742 séances < 2024-11-14 ; out-of-sample 496 séances) · 1080 variantes · coûts : spread 0.0001 , slippage 2e-05 (unités de prix, par exécution au marché/stop).

> Source : Dukascopy 1 min BID, 2139840 bougies (1486 jours), statut téléchargement {'requested': 1497, 'downloaded': 1486, 'unavailable': 11} (téléchargement du 2026-10-14).

## Verdict : **FIABILITÉ NON DÉMONTRÉE**

- profit factor hors échantillon 0.80 ≤ 1
- borne basse (IC 95 %) du PF hors échantillon 0.65 ≤ 1
- walk-forward : 962 trades, PF 0.76

> Rappel : avec 1080 variantes testées, la meilleure in-sample paraît toujours excellente même sans aucun avantage réel (biais de sélection). Seules les colonnes **hors échantillon** et le **walk-forward** sont informatives, et elles restent des estimations sur un passé limité — pas une promesse de rendement.

## Variante sélectionnée (meilleur profit factor in-sample)

`R30_close_rr2_opposite_ma0_p1_n1_cut1300` — range 30 min, clôture hors range, RR 2, stop = borne opposée, entrées jusqu'à 13:00, TP partiel 1R + break-even

| période | trades | win rate | profit factor | espérance (R) | max DD (R) | plus longue série perdante |
|---|---|---|---|---|---|---|
| in-sample | 728 | 48.9 % | 1.00 | 0.001 | 51.5 | 8 |
| out-of-sample | 489 | 46.2 % | 0.80 | -0.096 | 49.0 | 13 |
| total | 1217 | 47.8 % | 0.92 | -0.038 | 94.6 | 13 |

IC bootstrap 95 % du PF hors échantillon : [0.65 ; 0.96] ; probabilité (bootstrap) que le PF hors échantillon soit < 1 : 98.9 %.

| année | trades | win rate | PF | total R | max DD R |
|---|---|---|---|---|---|
| 2022 | 256 | 57.4 % | 1.49 | 43.5 | 8.3 |
| 2023 | 251 | 43.8 % | 0.81 | -21.3 | 24.2 |
| 2024 | 254 | 43.7 % | 0.74 | -32.7 | 35.3 |
| 2025 | 257 | 49.4 % | 0.94 | -6.9 | 18.1 |
| 2026 | 199 | 43.7 % | 0.72 | -28.7 | 34.8 |

Sorties (toutes périodes) : {'be': 141, 'sl': 487, 'time': 442, 'tp2': 147} · longs 604 / shorts 613

## Que valent les 10 meilleures variantes in-sample une fois hors échantillon ?

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 728 / 48.9 % / 1.00 / 0.001 / 51.5 | 489 / 46.2 % / 0.80 / -0.096 / 49.0 |
| `R30_close_rr2_opposite_ma50_p1_n1_cut1300` | 728 / 48.9 % / 1.00 / 0.001 / 51.5 | 489 / 46.2 % / 0.80 / -0.096 / 49.0 |
| `R15_close_rr3_opposite_ma200_p1_n1_cut1300` | 737 / 49.4 % / 1.00 / 0.001 / 54.4 | 492 / 43.9 % / 0.70 / -0.160 / 81.2 |
| `R15_close_rr3_opposite_ma200_p1_n1_cut1130` | 731 / 49.2 % / 1.00 / -0.000 / 54.6 | 490 / 43.9 % / 0.70 / -0.162 / 81.4 |
| `R30_close_rr2_opposite_ma200_p1_n1_cut1300` | 728 / 49.0 % / 1.00 / -0.000 / 51.0 | 488 / 47.7 % / 0.85 / -0.067 / 40.1 |
| `R30_close_rr3_opposite_ma200_p1_n1_cut1300` | 728 / 49.0 % / 1.00 / -0.001 / 50.4 | 488 / 47.7 % / 0.85 / -0.070 / 42.4 |
| `R30_close_rr3_opposite_ma0_p1_n1_cut1300` | 728 / 48.9 % / 1.00 / -0.001 / 49.8 | 489 / 46.2 % / 0.78 / -0.104 / 52.6 |
| `R30_close_rr3_opposite_ma50_p1_n1_cut1300` | 728 / 48.9 % / 1.00 / -0.001 / 49.8 | 489 / 46.2 % / 0.78 / -0.104 / 52.6 |
| `R30_close_rr2_opposite_ma0_p0_n1_cut1300` | 728 / 42.9 % / 1.00 / -0.002 / 48.8 | 489 / 38.4 % / 0.79 / -0.114 / 59.4 |
| `R30_close_rr2_opposite_ma50_p0_n1_cut1300` | 728 / 42.9 % / 1.00 / -0.002 / 48.8 | 489 / 38.4 % / 0.79 / -0.114 / 59.4 |

Sur l'ensemble des variantes avec ≥ 20 trades hors échantillon (1080) : PF médian in-sample 0.68, PF médian hors échantillon 0.61, part des variantes avec PF hors échantillon > 1 : 0.0 %, corrélation de rang IS/OOS : 0.95 (proche de 0 ⇒ le classement in-sample ne prédit pas la suite).

## Walk-forward (sélection automatique année après année)

Chaque année, la variante au meilleur PF sur toutes les années précédentes est appliquée en aveugle à l'année suivante.

| année testée | variante retenue (PF / n en apprentissage) | trades | win rate | PF | total R |
|---|---|---|---|---|---|
| 2023 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (1.50 / 256) | 251 | 43.8 % | 0.83 | -19.3 |
| 2024 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (1.12 / 507) | 254 | 43.7 % | 0.69 | -39.5 |
| 2025 | `R15_close_rr3_opposite_ma200_p1_n1_cut1300` (0.98 / 770) | 258 | 47.7 % | 0.79 | -27.3 |
| 2026 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (0.99 / 1017) | 199 | 44.7 % | 0.76 | -23.8 |
| **total** | | 962 | 45.0 % | 0.76 | -109.8 |

IC bootstrap 95 % du PF walk-forward : [0.66 ; 0.87].

## La variante annoncée dans la vidéo (or, range 30 min, retest FVG, RR 1, « PF ≈ 1,75 »)

`R30_fvg_rr1_structure_ma0_p0_n1_cut1130` — range 30 min, cassure + retest FVG, RR 1, stop = structure (bougie/FVG), entrées jusqu'à 11:30

| période | trades | win rate | profit factor | espérance (R) | max DD (R) |
|---|---|---|---|---|---|
| in-sample | 530 | 27.0 % | 0.33 | -0.533 | 283.5 |
| out-of-sample | 360 | 19.2 % | 0.21 | -0.704 | 253.6 |
| total | 890 | 23.8 % | 0.28 | -0.602 | 536.1 |

IC bootstrap 95 % du PF (toutes périodes) : [0.24 ; 0.33] — probabilité que le vrai PF soit < 1 : 100.0 %.

| année | trades | win rate | PF | total R |
|---|---|---|---|---|
| 2022 | 187 | 27.8 % | 0.35 | -96.2 |
| 2023 | 190 | 27.9 % | 0.35 | -96.7 |
| 2024 | 175 | 24.0 % | 0.28 | -105.4 |
| 2025 | 193 | 21.8 % | 0.25 | -124.8 |
| 2026 | 145 | 15.9 % | 0.17 | -113.1 |

## Meilleures variantes hors échantillon (a posteriori — information, pas sélection)

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R30_fvg_rr2_opposite_ma0_p0_n2_cut1130` | 713 / 40.8 % / 0.93 / -0.037 / 49.3 | 496 / 41.1 % / 0.95 / -0.027 / 36.3 |
| `R30_fvg_rr2_opposite_ma50_p0_n2_cut1130` | 713 / 40.8 % / 0.93 / -0.037 / 49.3 | 496 / 41.1 % / 0.95 / -0.027 / 36.3 |
| `R30_fvg_rr3_opposite_ma200_p0_n2_cut1130` | 698 / 39.8 % / 0.91 / -0.048 / 52.0 | 477 / 40.3 % / 0.94 / -0.031 / 34.0 |
| `R30_fvg_rr2_opposite_ma200_p0_n2_cut1130` | 698 / 41.1 % / 0.92 / -0.042 / 52.3 | 477 / 41.7 % / 0.94 / -0.031 / 35.5 |
| `R30_fvg_rr3_opposite_ma200_p0_n1_cut1130` | 588 / 40.6 % / 0.93 / -0.035 / 43.1 | 397 / 38.3 % / 0.93 / -0.036 / 29.6 |

## Sensibilité aux coûts (variante sélectionnée et variante « vidéo »)

| variante | spread | slippage | trades | win rate | PF | espérance (R) |
|---|---|---|---|---|---|---|
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0001 | 2e-05 | 1217 | 47.8 % | 0.92 | -0.038 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.00015 | 3e-05 | 1217 | 45.3 % | 0.83 | -0.082 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0002 | 4e-05 | 1217 | 43.4 % | 0.74 | -0.126 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0001 | 2e-05 | 890 | 23.8 % | 0.28 | -0.602 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.00015 | 3e-05 | 890 | 18.3 % | 0.20 | -0.747 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0002 | 4e-05 | 890 | 14.5 % | 0.14 | -0.866 |

## Méthode

- Bougies 1 minute BID Dukascopy (flux public), séances New York 09:30–16:00 (heure d'été/hiver gérée), journées < 200 bougies ignorées.
- Range = plus haut/plus bas des R premières minutes ; cassure = clôture 1 min au-delà ; entrée au marché à l'ouverture suivante (« close ») ou limite au bord de la première FVG après cassure (« fvg ») ; aucune entrée après l'heure limite ; tout est clôturé à 15:55 NY.
- Coûts : achat à bid + spread, vente à bid ; slippage sur ordres au marché et stops ; stop prioritaire sur l'objectif dans une même bougie ; dans la bougie d'entrée seul le stop est vérifié.
- In-sample = premiers 60 % des séances, out-of-sample = 40 % suivants ; sélection par PF in-sample (≥ 50 trades) ; IC par bootstrap (1 000 rééchantillonnages) ; walk-forward annuel.
- Résultats en R (risque initial par trade) : ils ne dépendent pas de la taille du compte ; aucun rendement en € n'est annoncé.
