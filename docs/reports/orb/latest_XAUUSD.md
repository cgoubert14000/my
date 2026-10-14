# Backtest ORB — XAUUSD

Généré le 2026-10-14T02:06:35+00:00 · données : 1247 séances New York du 2022-01-03 au 2026-10-13 (in-sample 748 séances < 2024-11-14 ; out-of-sample 499 séances) · 1080 variantes · coûts : spread 0.3 , slippage 0.05 (unités de prix, par exécution au marché/stop).

> Source : Dukascopy 1 min BID, 2155680 bougies (1497 jours), statut téléchargement {'requested': 1497, 'cached': 1497} (téléchargement du 2026-10-14).

## Verdict : **FIABILITÉ NON DÉMONTRÉE**

- profit factor hors échantillon 0.89 ≤ 1
- borne basse (IC 95 %) du PF hors échantillon 0.70 ≤ 1
- walk-forward : 963 trades, PF 0.85

> Rappel : avec 1080 variantes testées, la meilleure in-sample paraît toujours excellente même sans aucun avantage réel (biais de sélection). Seules les colonnes **hors échantillon** et le **walk-forward** sont informatives, et elles restent des estimations sur un passé limité — pas une promesse de rendement.

## Variante sélectionnée (meilleur profit factor in-sample)

`R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` — range 5 min, cassure + retest FVG, RR 3, stop = borne opposée, entrées jusqu'à 13:00, filtre EMA200

| période | trades | win rate | profit factor | espérance (R) | max DD (R) | plus longue série perdante |
|---|---|---|---|---|---|---|
| in-sample | 673 | 32.4 % | 1.03 | 0.020 | 44.9 | 16 |
| out-of-sample | 450 | 29.3 % | 0.89 | -0.072 | 44.7 | 13 |
| total | 1123 | 31.2 % | 0.97 | -0.017 | 58.4 | 16 |

IC bootstrap 95 % du PF hors échantillon : [0.70 ; 1.11] ; probabilité (bootstrap) que le PF hors échantillon soit < 1 : 85.0 %.

| année | trades | win rate | PF | total R | max DD R |
|---|---|---|---|---|---|
| 2022 | 236 | 35.2 % | 1.17 | 24.9 | 14.0 |
| 2023 | 229 | 28.4 % | 0.85 | -23.9 | 34.6 |
| 2024 | 238 | 34.9 % | 1.14 | 20.7 | 20.5 |
| 2025 | 236 | 29.7 % | 0.94 | -9.7 | 28.0 |
| 2026 | 184 | 26.6 % | 0.76 | -31.3 | 44.3 |

Sorties (toutes périodes) : {'sl': 727, 'time': 204, 'tp': 192} · longs 565 / shorts 558

## Que valent les 10 meilleures variantes in-sample une fois hors échantillon ?

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 673 / 32.4 % / 1.03 / 0.020 / 44.9 | 450 / 29.3 % / 0.89 / -0.072 / 44.7 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1130` | 657 / 32.4 % / 1.03 / 0.018 / 46.4 | 438 / 29.2 % / 0.89 / -0.074 / 44.5 |
| `R30_fvg_rr1_opposite_ma200_p0_n1_cut1300` | 623 / 49.4 % / 0.98 / -0.008 / 23.2 | 411 / 49.4 % / 1.00 / 0.001 / 18.9 |
| `R15_fvg_rr3_opposite_ma50_p0_n2_cut1300` | 917 / 38.3 % / 0.98 / -0.012 / 60.1 | 610 / 38.5 % / 0.96 / -0.023 / 38.1 |
| `R15_fvg_rr3_opposite_ma0_p0_n2_cut1300` | 918 / 38.2 % / 0.98 / -0.013 / 60.1 | 609 / 38.6 % / 0.97 / -0.018 / 38.1 |
| `R15_fvg_rr3_opposite_ma200_p0_n2_cut1300` | 898 / 38.9 % / 0.97 / -0.016 / 48.7 | 595 / 39.7 % / 0.95 / -0.027 / 40.4 |
| `R30_close_rr2_opposite_ma0_p0_n2_cut1300` | 883 / 43.8 % / 0.97 / -0.013 / 36.9 | 614 / 43.3 % / 1.07 / 0.029 / 17.8 |
| `R30_close_rr2_opposite_ma50_p0_n2_cut1300` | 883 / 43.8 % / 0.97 / -0.013 / 36.9 | 614 / 43.2 % / 1.06 / 0.024 / 17.8 |
| `R5_fvg_rr3_opposite_ma50_p0_n1_cut1300` | 666 / 29.4 % / 0.97 / -0.024 / 75.2 | 448 / 27.0 % / 0.88 / -0.085 / 55.8 |
| `R30_fvg_rr2_opposite_ma200_p0_n1_cut1300` | 623 / 45.3 % / 0.96 / -0.014 / 29.8 | 411 / 45.0 % / 1.00 / 0.001 / 14.3 |

Sur l'ensemble des variantes avec ≥ 20 trades hors échantillon (1080) : PF médian in-sample 0.78, PF médian hors échantillon 0.88, part des variantes avec PF hors échantillon > 1 : 8.6 %, corrélation de rang IS/OOS : 0.82 (proche de 0 ⇒ le classement in-sample ne prédit pas la suite).

## Walk-forward (sélection automatique année après année)

Chaque année, la variante au meilleur PF sur toutes les années précédentes est appliquée en aveugle à l'année suivante.

| année testée | variante retenue (PF / n en apprentissage) | trades | win rate | PF | total R |
|---|---|---|---|---|---|
| 2023 | `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` (1.17 / 236) | 229 | 28.4 % | 0.85 | -23.9 |
| 2024 | `R30_close_rr3_opposite_ma0_p0_n2_cut1300` (1.07 / 596) | 326 | 40.8 % | 0.77 | -32.6 |
| 2025 | `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` (1.05 / 703) | 236 | 29.7 % | 0.94 | -9.7 |
| 2026 | `R30_fvg_rr1_opposite_ma200_p0_n1_cut1300` (1.02 / 862) | 172 | 45.3 % | 0.83 | -12.0 |
| **total** | | 963 | 35.9 % | 0.85 | -78.2 |

IC bootstrap 95 % du PF walk-forward : [0.72 ; 0.99].

## La variante annoncée dans la vidéo (or, range 30 min, retest FVG, RR 1, « PF ≈ 1,75 »)

`R30_fvg_rr1_structure_ma0_p0_n1_cut1130` — range 30 min, cassure + retest FVG, RR 1, stop = structure (bougie/FVG), entrées jusqu'à 11:30

| période | trades | win rate | profit factor | espérance (R) | max DD (R) |
|---|---|---|---|---|---|
| in-sample | 504 | 27.8 % | 0.36 | -0.500 | 254.6 |
| out-of-sample | 367 | 30.8 % | 0.42 | -0.426 | 158.4 |
| total | 871 | 29.0 % | 0.38 | -0.469 | 409.4 |

IC bootstrap 95 % du PF (toutes périodes) : [0.33 ; 0.45] — probabilité que le vrai PF soit < 1 : 100.0 %.

| année | trades | win rate | PF | total R |
|---|---|---|---|---|
| 2022 | 175 | 28.0 % | 0.36 | -86.9 |
| 2023 | 162 | 27.8 % | 0.36 | -81.6 |
| 2024 | 191 | 29.3 % | 0.39 | -88.6 |
| 2025 | 184 | 29.9 % | 0.40 | -83.7 |
| 2026 | 159 | 30.2 % | 0.42 | -67.6 |

## Meilleures variantes hors échantillon (a posteriori — information, pas sélection)

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R15_fvg_rr2_mid_ma200_p1_n1_cut1130` | 625 / 43.8 % / 0.77 / -0.131 / 92.1 | 415 / 52.3 % / 1.08 / 0.037 / 15.0 |
| `R15_fvg_rr1_mid_ma200_p0_n1_cut1130` | 625 / 43.8 % / 0.76 / -0.138 / 97.1 | 415 / 52.3 % / 1.08 / 0.037 / 13.4 |
| `R30_close_rr2_opposite_ma200_p0_n1_cut1300` | 710 / 43.2 % / 0.92 / -0.033 / 37.2 | 477 / 43.0 % / 1.08 / 0.031 / 15.4 |
| `R30_close_rr2_opposite_ma200_p0_n1_cut1130` | 670 / 42.5 % / 0.89 / -0.045 / 43.8 | 453 / 43.0 % / 1.07 / 0.031 / 13.6 |
| `R30_close_rr2_opposite_ma0_p0_n2_cut1300` | 883 / 43.8 % / 0.97 / -0.013 / 36.9 | 614 / 43.3 % / 1.07 / 0.029 / 17.8 |

## Sensibilité aux coûts et au stop minimal (variante sélectionnée et variante « vidéo »)

Ligne « spread 0 » = aucun coût : c'est l'avantage brut de la règle ; « stop min. » = distance entrée-stop minimale acceptée (les trades au stop plus serré sont ignorés).

| variante | spread | slippage | stop min. | trades | win rate | PF | espérance (R) | max DD (R) |
|---|---|---|---|---|---|---|---|---|
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.0 | 0.0 | 0.3 | 1123 | 33.1 % | 1.14 | 0.088 | 38.9 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.3 | 0.05 | 0.3 | 1123 | 31.2 % | 0.97 | -0.017 | 58.4 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.45 | 0.075 | 0.3 | 1123 | 29.9 % | 0.90 | -0.072 | 98.3 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.6 | 0.1 | 0.3 | 1123 | 28.9 % | 0.84 | -0.114 | 142.1 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.3 | 0.05 | 1.5 | 1105 | 31.1 % | 0.97 | -0.022 | 64.5 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.3 | 0.05 | 3.0 | 946 | 33.2 % | 0.98 | -0.014 | 52.9 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.0 | 0.0 | 0.3 | 792 | 42.6 % | 0.74 | -0.149 | 120.0 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.3 | 0.05 | 0.3 | 871 | 29.0 % | 0.38 | -0.469 | 409.4 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.45 | 0.075 | 0.3 | 871 | 24.5 % | 0.30 | -0.582 | 507.0 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.6 | 0.1 | 0.3 | 871 | 20.4 % | 0.23 | -0.689 | 600.2 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.3 | 0.05 | 1.5 | 301 | 43.9 % | 0.77 | -0.134 | 41.2 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.3 | 0.05 | 3.0 | 120 | 42.5 % | 0.73 | -0.156 | 20.7 |

## Méthode

- Bougies 1 minute BID Dukascopy (flux public), séances New York 09:30–16:00 (heure d'été/hiver gérée), journées < 200 bougies ignorées.
- Range = plus haut/plus bas des R premières minutes ; cassure = clôture 1 min au-delà ; entrée au marché à l'ouverture suivante (« close ») ou limite au bord de la première FVG après cassure (« fvg ») ; aucune entrée après l'heure limite ; tout est clôturé à 15:55 NY.
- Coûts : achat à bid + spread, vente à bid ; slippage sur ordres au marché et stops ; stop prioritaire sur l'objectif dans une même bougie ; dans la bougie d'entrée seul le stop est vérifié.
- In-sample = premiers 60 % des séances, out-of-sample = 40 % suivants ; sélection par PF in-sample (≥ 50 trades) ; IC par bootstrap (1 000 rééchantillonnages) ; walk-forward annuel.
- Résultats en R (risque initial par trade) : ils ne dépendent pas de la taille du compte ; aucun rendement en € n'est annoncé.
