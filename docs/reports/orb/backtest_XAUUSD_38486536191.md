# Backtest ORB — XAUUSD

Généré le 2026-10-14T00:41:48+00:00 · données : 1231 séances New York du 2022-01-05 au 2026-10-12 (in-sample 738 séances < 2024-11-18 ; out-of-sample 493 séances) · 1080 variantes · coûts : spread 0.3 , slippage 0.05 (unités de prix, par exécution au marché/stop).

> Source : Dukascopy 1 min BID, 2126880 bougies (1477 jours), statut téléchargement {'requested': 1496, 'downloaded': 1477, 'unavailable': 19} (téléchargement du 2026-10-14).

## Verdict : **FIABILITÉ NON DÉMONTRÉE**

- profit factor hors échantillon 0.90 ≤ 1
- borne basse (IC 95 %) du PF hors échantillon 0.71 ≤ 1
- walk-forward : 1033 trades, PF 0.86

> Rappel : avec 1080 variantes testées, la meilleure in-sample paraît toujours excellente même sans aucun avantage réel (biais de sélection). Seules les colonnes **hors échantillon** et le **walk-forward** sont informatives, et elles restent des estimations sur un passé limité — pas une promesse de rendement.

## Variante sélectionnée (meilleur profit factor in-sample)

`R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` — range 5 min, cassure + retest FVG, RR 3, stop = borne opposée, entrées jusqu'à 13:00, filtre EMA200

| période | trades | win rate | profit factor | espérance (R) | max DD (R) | plus longue série perdante |
|---|---|---|---|---|---|---|
| in-sample | 663 | 31.8 % | 1.00 | -0.001 | 56.9 | 16 |
| out-of-sample | 445 | 29.4 % | 0.90 | -0.071 | 45.6 | 13 |
| total | 1108 | 30.9 % | 0.96 | -0.029 | 71.3 | 16 |

IC bootstrap 95 % du PF hors échantillon : [0.71 ; 1.12] ; probabilité (bootstrap) que le PF hors échantillon soit < 1 : 83.5 %.

| année | trades | win rate | PF | total R | max DD R |
|---|---|---|---|---|---|
| 2022 | 232 | 34.9 % | 1.17 | 25.3 | 14.0 |
| 2023 | 226 | 27.9 % | 0.82 | -28.9 | 34.6 |
| 2024 | 233 | 34.3 % | 1.09 | 13.8 | 20.5 |
| 2025 | 233 | 29.6 % | 0.93 | -10.7 | 28.0 |
| 2026 | 184 | 26.6 % | 0.76 | -31.3 | 44.3 |

Sorties (toutes périodes) : {'sl': 720, 'time': 202, 'tp': 186} · longs 557 / shorts 551

## Que valent les 10 meilleures variantes in-sample une fois hors échantillon ?

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 663 / 31.8 % / 1.00 / -0.001 / 56.9 | 445 / 29.4 % / 0.90 / -0.071 / 45.6 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1130` | 647 / 31.8 % / 1.00 / -0.002 / 58.3 | 433 / 29.3 % / 0.89 / -0.072 / 45.5 |
| `R30_fvg_rr2_mid_ma0_p0_n1_cut1300` | 609 / 37.8 % / 0.98 / -0.014 / 49.9 | 409 / 34.5 % / 0.91 / -0.057 / 47.4 |
| `R30_fvg_rr2_mid_ma50_p0_n1_cut1300` | 609 / 37.8 % / 0.98 / -0.014 / 49.9 | 409 / 34.5 % / 0.91 / -0.057 / 47.4 |
| `R30_close_rr2_opposite_ma0_p0_n2_cut1300` | 870 / 43.8 % / 0.97 / -0.014 / 41.1 | 607 / 43.0 % / 1.06 / 0.024 / 17.8 |
| `R30_close_rr2_opposite_ma50_p0_n2_cut1300` | 870 / 43.8 % / 0.97 / -0.014 / 41.1 | 607 / 42.8 % / 1.04 / 0.019 / 17.8 |
| `R30_fvg_rr2_mid_ma200_p0_n1_cut1300` | 612 / 37.9 % / 0.96 / -0.021 / 49.8 | 405 / 35.3 % / 0.92 / -0.047 / 42.9 |
| `R30_fvg_rr1_opposite_ma200_p0_n1_cut1300` | 613 / 49.1 % / 0.96 / -0.014 / 26.6 | 405 / 48.9 % / 0.99 / -0.006 / 18.9 |
| `R30_fvg_rr3_mid_ma0_p0_n1_cut1300` | 609 / 34.8 % / 0.96 / -0.023 / 50.2 | 409 / 29.8 % / 0.87 / -0.087 / 48.5 |
| `R30_fvg_rr3_mid_ma50_p0_n1_cut1300` | 609 / 34.8 % / 0.96 / -0.023 / 50.2 | 409 / 29.8 % / 0.87 / -0.087 / 48.5 |

Sur l'ensemble des variantes avec ≥ 20 trades hors échantillon (1080) : PF médian in-sample 0.78, PF médian hors échantillon 0.87, part des variantes avec PF hors échantillon > 1 : 7.3 %, corrélation de rang IS/OOS : 0.79 (proche de 0 ⇒ le classement in-sample ne prédit pas la suite).

## Walk-forward (sélection automatique année après année)

Chaque année, la variante au meilleur PF sur toutes les années précédentes est appliquée en aveugle à l'année suivante.

| année testée | variante retenue (PF / n en apprentissage) | trades | win rate | PF | total R |
|---|---|---|---|---|---|
| 2023 | `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` (1.17 / 232) | 226 | 27.9 % | 0.82 | -28.9 |
| 2024 | `R30_close_rr3_opposite_ma0_p0_n2_cut1300` (1.08 / 587) | 320 | 40.3 % | 0.74 | -35.8 |
| 2025 | `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` (1.02 / 691) | 233 | 29.6 % | 0.93 | -10.7 |
| 2026 | `R30_close_rr2_opposite_ma0_p0_n2_cut1300` (1.01 / 1223) | 254 | 40.6 % | 0.96 | -4.8 |
| **total** | | 1033 | 35.2 % | 0.86 | -80.1 |

IC bootstrap 95 % du PF walk-forward : [0.73 ; 1.00].

## La variante annoncée dans la vidéo (or, range 30 min, retest FVG, RR 1, « PF ≈ 1,75 »)

`R30_fvg_rr1_structure_ma0_p0_n1_cut1130` — range 30 min, cassure + retest FVG, RR 1, stop = structure (bougie/FVG), entrées jusqu'à 11:30

| période | trades | win rate | profit factor | espérance (R) | max DD (R) |
|---|---|---|---|---|---|
| in-sample | 496 | 28.4 % | 0.37 | -0.487 | 245.1 |
| out-of-sample | 361 | 30.5 % | 0.41 | -0.433 | 156.3 |
| total | 857 | 29.3 % | 0.39 | -0.464 | 397.8 |

IC bootstrap 95 % du PF (toutes périodes) : [0.33 ; 0.45] — probabilité que le vrai PF soit < 1 : 100.0 %.

| année | trades | win rate | PF | total R |
|---|---|---|---|---|
| 2022 | 172 | 27.9 % | 0.36 | -85.7 |
| 2023 | 160 | 28.1 % | 0.36 | -79.6 |
| 2024 | 186 | 30.1 % | 0.40 | -83.3 |
| 2025 | 181 | 29.8 % | 0.40 | -82.6 |
| 2026 | 158 | 30.4 % | 0.42 | -66.6 |

## Meilleures variantes hors échantillon (a posteriori — information, pas sélection)

| variante | in-sample : n / WR / PF / esp. R / DD | out-of-sample : n / WR / PF / esp. R / DD |
|---|---|---|
| `R15_fvg_rr1_mid_ma200_p0_n1_cut1130` | 615 / 43.9 % / 0.76 / -0.137 / 92.9 | 409 / 52.1 % / 1.07 / 0.032 / 13.4 |
| `R15_fvg_rr2_mid_ma200_p1_n1_cut1130` | 615 / 43.9 % / 0.77 / -0.128 / 88.3 | 409 / 52.1 % / 1.06 / 0.030 / 15.0 |
| `R30_close_rr2_opposite_ma200_p0_n1_cut1300` | 700 / 43.0 % / 0.91 / -0.039 / 41.5 | 471 / 42.7 % / 1.06 / 0.026 / 15.4 |
| `R30_close_rr3_opposite_ma200_p0_n1_cut1130` | 660 / 41.8 % / 0.86 / -0.061 / 54.0 | 447 / 42.5 % / 1.06 / 0.025 / 14.8 |
| `R30_close_rr2_opposite_ma200_p0_n1_cut1130` | 660 / 42.3 % / 0.88 / -0.053 / 48.1 | 447 / 42.7 % / 1.06 / 0.025 / 13.6 |

## Sensibilité aux coûts (variante sélectionnée et variante « vidéo »)

| variante | spread | slippage | trades | win rate | PF | espérance (R) |
|---|---|---|---|---|---|---|
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.3 | 0.05 | 1108 | 30.9 % | 0.96 | -0.029 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.45 | 0.075 | 1108 | 29.6 % | 0.88 | -0.084 |
| `R5_fvg_rr3_opposite_ma200_p0_n1_cut1300` | 0.6 | 0.1 | 1108 | 28.7 % | 0.83 | -0.123 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.3 | 0.05 | 857 | 29.3 % | 0.39 | -0.464 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.45 | 0.075 | 857 | 24.9 % | 0.30 | -0.574 |
| `R30_fvg_rr1_structure_ma0_p0_n1_cut1130` | 0.6 | 0.1 | 857 | 20.8 % | 0.23 | -0.683 |

## Méthode

- Bougies 1 minute BID Dukascopy (flux public), séances New York 09:30–16:00 (heure d'été/hiver gérée), journées < 200 bougies ignorées.
- Range = plus haut/plus bas des R premières minutes ; cassure = clôture 1 min au-delà ; entrée au marché à l'ouverture suivante (« close ») ou limite au bord de la première FVG après cassure (« fvg ») ; aucune entrée après l'heure limite ; tout est clôturé à 15:55 NY.
- Coûts : achat à bid + spread, vente à bid ; slippage sur ordres au marché et stops ; stop prioritaire sur l'objectif dans une même bougie ; dans la bougie d'entrée seul le stop est vérifié.
- In-sample = premiers 60 % des séances, out-of-sample = 40 % suivants ; sélection par PF in-sample (≥ 50 trades) ; IC par bootstrap (1 000 rééchantillonnages) ; walk-forward annuel.
- Résultats en R (risque initial par trade) : ils ne dépendent pas de la taille du compte ; aucun rendement en € n'est annoncé.
