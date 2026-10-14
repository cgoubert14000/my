# Backtest ORB — EURUSD

Généré le 2026-10-14T02:01:54+00:00 · données : 1244 séances New York du 2022-01-03 au 2026-10-13 (in-sample 746 séances < 2024-11-13 ; out-of-sample 498 séances) · 1080 variantes · coûts : spread 0.0001 , slippage 2e-05 (unités de prix, par exécution au marché/stop).

> Source : Dukascopy 1 min BID, 2151360 bougies (1494 jours), statut téléchargement {'requested': 1497, 'cached': 1486, 'unavailable': 3, 'downloaded': 8} (téléchargement du 2026-10-14).

## Verdict : **FIABILITÉ NON DÉMONTRÉE**

- profit factor hors échantillon 0.81 ≤ 1
- borne basse (IC 95 %) du PF hors échantillon 0.66 ≤ 1
- walk-forward : 966 trades, PF 0.77

> Rappel : avec 1080 variantes testées, la meilleure in-sample paraît toujours excellente même sans aucun avantage réel (biais de sélection). Seules les colonnes **hors échantillon** et le **walk-forward** sont informatives, et elles restent des estimations sur un passé limité — pas une promesse de rendement.

## Variante sélectionnée (meilleur profit factor in-sample)

`R30_close_rr2_opposite_ma0_p1_n1_cut1300` — range 30 min, clôture hors range, RR 2, stop = borne opposée, entrées jusqu'à 13:00, TP partiel 1R + break-even

| période | trades | win rate | profit factor | espérance (R) | max DD (R) | plus longue série perdante |
|---|---|---|---|---|---|---|
| in-sample | 732 | 48.8 % | 1.00 | -0.001 | 52.8 | 8 |
| out-of-sample | 491 | 46.4 % | 0.81 | -0.092 | 47.5 | 13 |
| total | 1223 | 47.8 % | 0.92 | -0.037 | 94.3 | 13 |

IC bootstrap 95 % du PF hors échantillon : [0.66 ; 0.98] ; probabilité (bootstrap) que le PF hors échantillon soit < 1 : 99.0 %.

| année | trades | win rate | PF | total R | max DD R |
|---|---|---|---|---|---|
| 2022 | 257 | 57.2 % | 1.47 | 42.5 | 8.3 |
| 2023 | 254 | 43.7 % | 0.81 | -22.0 | 24.9 |
| 2024 | 255 | 43.9 % | 0.75 | -32.3 | 34.8 |
| 2025 | 257 | 49.4 % | 0.94 | -6.9 | 18.1 |
| 2026 | 200 | 44.0 % | 0.73 | -27.2 | 33.3 |

Sorties (toutes périodes) : {'be': 142, 'sl': 489, 'time': 444, 'tp2': 148} · longs 605 / shorts 618

## Que valent les 10 meilleures variantes in-sample une fois hors échantillon ?

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 732 / 48.8 % / 1.00 / -0.001 / 52.8 | 491 / 46.4 % / 0.81 / -0.092 / 47.5 |
| `R30_close_rr2_opposite_ma50_p1_n1_cut1300` | 732 / 48.8 % / 1.00 / -0.001 / 52.8 | 491 / 46.4 % / 0.81 / -0.092 / 47.5 |
| `R30_close_rr2_opposite_ma200_p1_n1_cut1300` | 732 / 48.9 % / 1.00 / -0.002 / 51.8 | 490 / 48.0 % / 0.86 / -0.064 / 38.6 |
| `R30_close_rr3_opposite_ma200_p1_n1_cut1300` | 732 / 48.9 % / 0.99 / -0.002 / 51.3 | 490 / 48.0 % / 0.86 / -0.066 / 40.7 |
| `R15_close_rr3_opposite_ma200_p1_n1_cut1130` | 734 / 49.2 % / 0.99 / -0.003 / 55.0 | 492 / 43.9 % / 0.70 / -0.160 / 82.5 |
| `R15_close_rr3_opposite_ma200_p1_n1_cut1300` | 741 / 49.3 % / 0.99 / -0.003 / 54.8 | 494 / 43.9 % / 0.71 / -0.159 / 82.2 |
| `R30_close_rr3_opposite_ma0_p1_n1_cut1300` | 732 / 48.8 % / 0.99 / -0.003 / 51.0 | 491 / 46.4 % / 0.79 / -0.099 / 50.6 |
| `R30_close_rr3_opposite_ma50_p1_n1_cut1300` | 732 / 48.8 % / 0.99 / -0.003 / 51.0 | 491 / 46.4 % / 0.79 / -0.099 / 50.6 |
| `R30_close_rr2_opposite_ma200_p1_n1_cut1130` | 710 / 48.7 % / 0.99 / -0.004 / 51.5 | 476 / 48.1 % / 0.87 / -0.060 / 37.5 |
| `R30_close_rr2_opposite_ma0_p0_n1_cut1300` | 732 / 42.8 % / 0.99 / -0.005 / 50.4 | 491 / 38.7 % / 0.80 / -0.109 / 57.4 |

Sur l'ensemble des variantes avec ≥ 20 trades hors échantillon (1080) : PF médian in-sample 0.68, PF médian hors échantillon 0.62, part des variantes avec PF hors échantillon > 1 : 0.0 %, corrélation de rang IS/OOS : 0.96 (proche de 0 ⇒ le classement in-sample ne prédit pas la suite).

## Walk-forward (sélection automatique année après année)

Chaque année, la variante au meilleur PF sur toutes les années précédentes est appliquée en aveugle à l'année suivante.

| année testée | variante retenue (PF / n en apprentissage) | trades | win rate | PF | total R |
|---|---|---|---|---|---|
| 2023 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (1.49 / 257) | 254 | 43.7 % | 0.82 | -20.0 |
| 2024 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (1.12 / 511) | 255 | 43.9 % | 0.70 | -38.5 |
| 2025 | `R15_close_rr3_opposite_ma200_p1_n1_cut1130` (0.97 / 768) | 257 | 47.9 % | 0.79 | -26.3 |
| 2026 | `R30_close_rr1_opposite_ma200_p0_n1_cut1300` (0.98 / 1022) | 200 | 45.0 % | 0.77 | -22.8 |
| **total** | | 966 | 45.1 % | 0.77 | -107.6 |

IC bootstrap 95 % du PF walk-forward : [0.67 ; 0.87].

## La variante annoncée dans la vidéo (or, range 30 min, retest FVG, RR 1, « PF ≈ 1,75 »)

`R30_fvg_rr1_structure_ma0_p0_n1_cut1130` — range 30 min, cassure + retest FVG, RR 1, stop = structure (bougie/FVG), entrées jusqu'à 11:30

| période | trades | win rate | profit factor | espérance (R) | max DD (R) |
|---|---|---|---|---|---|
| in-sample | 531 | 26.7 % | 0.33 | -0.538 | 285.7 |
| out-of-sample | 361 | 19.4 % | 0.22 | -0.700 | 253.6 |
| total | 892 | 23.8 % | 0.28 | -0.603 | 538.3 |

IC bootstrap 95 % du PF (toutes périodes) : [0.24 ; 0.33] — probabilité que le vrai PF soit < 1 : 100.0 %.

| année | trades | win rate | PF | total R |
|---|---|---|---|---|
| 2022 | 187 | 27.8 % | 0.35 | -96.2 |
| 2023 | 191 | 27.7 % | 0.35 | -97.8 |
| 2024 | 176 | 23.9 % | 0.28 | -106.5 |
| 2025 | 193 | 21.8 % | 0.25 | -124.8 |
| 2026 | 145 | 15.9 % | 0.17 | -113.1 |

## Meilleures variantes hors échantillon (a posteriori — information, pas sélection)

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R30_fvg_rr2_opposite_ma0_p0_n2_cut1130` | 716 / 40.8 % / 0.93 / -0.038 / 49.4 | 498 / 41.4 % / 0.96 / -0.022 / 34.3 |
| `R30_fvg_rr2_opposite_ma50_p0_n2_cut1130` | 716 / 40.8 % / 0.93 / -0.038 / 49.4 | 498 / 41.4 % / 0.96 / -0.022 / 34.3 |
| `R30_fvg_rr3_opposite_ma200_p0_n2_cut1130` | 701 / 39.8 % / 0.91 / -0.048 / 52.1 | 479 / 40.5 % / 0.96 / -0.024 / 34.0 |
| `R30_fvg_rr2_opposite_ma200_p0_n2_cut1130` | 701 / 41.1 % / 0.92 / -0.043 / 52.4 | 479 / 42.0 % / 0.95 / -0.025 / 33.5 |
| `R30_fvg_rr3_opposite_ma200_p0_n1_cut1130` | 591 / 40.6 % / 0.93 / -0.036 / 43.2 | 399 / 38.6 % / 0.95 / -0.027 / 29.6 |

## Sensibilité aux coûts (variante sélectionnée et variante « vidéo »)

| variante | spread | slippage | trades | win rate | PF | espérance (R) |
|---|---|---|---|---|---|---|
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0001 | 2e-05 | 1223 | 47.8 % | 0.92 | -0.037 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.00015 | 3e-05 | 1223 | 45.3 % | 0.83 | -0.081 |
| `R30_close_rr2_opposite_ma0_p1_n1_cut1300` | 0.0002 | 4e-05 | 1223 | 43.4 % | 0.74 | -0.125 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0001 | 2e-05 | 892 | 23.8 % | 0.28 | -0.603 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.00015 | 3e-05 | 892 | 18.3 % | 0.20 | -0.748 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0002 | 4e-05 | 892 | 14.5 % | 0.14 | -0.867 |

## Méthode

- Bougies 1 minute BID Dukascopy (flux public), séances New York 09:30–16:00 (heure d'été/hiver gérée), journées < 200 bougies ignorées.
- Range = plus haut/plus bas des R premières minutes ; cassure = clôture 1 min au-delà ; entrée au marché à l'ouverture suivante (« close ») ou limite au bord de la première FVG après cassure (« fvg ») ; aucune entrée après l'heure limite ; tout est clôturé à 15:55 NY.
- Coûts : achat à bid + spread, vente à bid ; slippage sur ordres au marché et stops ; stop prioritaire sur l'objectif dans une même bougie ; dans la bougie d'entrée seul le stop est vérifié.
- In-sample = premiers 60 % des séances, out-of-sample = 40 % suivants ; sélection par PF in-sample (≥ 50 trades) ; IC par bootstrap (1 000 rééchantillonnages) ; walk-forward annuel.
- Résultats en R (risque initial par trade) : ils ne dépendent pas de la taille du compte ; aucun rendement en € n'est annoncé.
