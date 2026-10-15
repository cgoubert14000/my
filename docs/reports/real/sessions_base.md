# Sessions de marché réel — base (généré 2026-10-15T00:04:06Z)

Chaque ligne vient du rapport final de la session (`ghost_<chain>_<run>.json`) ; la session en cours vient de `latest_<chain>.json`.
Aucune transaction n'a été signée : « simulées » = eth_call du contrat sur l'état réel ; « ghost N+1 » = re-simulation au bloc suivant.

| Run | Fin | Durée (min) | Blocs | Pools / jetons / routes | Cycle (ms) | Candidats | Net attendu > 0 | Simulées ok / échec | Ghost N+1 + / n | Fiabilité n / borne inf. | Statut |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| [38419015127](https://github.com/cgoubert14000/my/actions/runs/38419015127) | 2026-10-13T15:32:55+00:00 | 25 | 82 | 251 / — / 192222 | 16056 | 20000 | 0 | 0 / 0 | 0 / 0 | 0 / — | APPRENTISSAGE |
| [38425105547](https://github.com/cgoubert14000/my/actions/runs/38425105547) | 2026-10-13T16:50:17+00:00 | 60 | 418 | 251 / — / 192222 | 7084 | 0 | 0 | 0 / 0 | 0 / 0 | 0 / — | APPRENTISSAGE |
| [38429265408](https://github.com/cgoubert14000/my/actions/runs/38429265408) | 2026-10-13T17:53:29+00:00 | 60 | 324 | 251 / — / 192222 | 8740 | 0 | 0 | 0 / 0 | 0 / 0 | 0 / — | APPRENTISSAGE |
| [38445117116](https://github.com/cgoubert14000/my/actions/runs/38445117116) | 2026-10-13T20:00:30+00:00 | 60 | 1779 | 251 / — / 192222 | 840 | 43218 | 65 | 0 / 17 | 0 / 15 | 15 / 0.1 % | APPRENTISSAGE |
| [38452875318](https://github.com/cgoubert14000/my/actions/runs/38452875318) | 2026-10-13T21:06:26+00:00 | 60 | 1519 | 251 / — / 192222 | 266 | 47798 | 0 | 0 / 0 | 0 / 0 | 0 / — | APPRENTISSAGE |
| [38473562031](https://github.com/cgoubert14000/my/actions/runs/38473562031) | 2026-10-13T22:07:31+00:00 | 6 | 169 | 579 / 328 / 21722 | 480 | 15749 | 0 | 0 / 0 | 0 / 0 | 0 / — | APPRENTISSAGE |
| [38475616089](https://github.com/cgoubert14000/my/actions/runs/38475616089) | 2026-10-14T03:43:15+00:00 | 330 | 8902 | 579 / 328 / 21606 | 130 | 2146414 | 357 | 9 / 10 | 0 / 9 | 9 / 0.1 % | APPRENTISSAGE |
| [38507809632](https://github.com/cgoubert14000/my/actions/runs/38507809632) | 2026-10-14T09:20:18+00:00 | 330 | 9662 | 582 / 328 / 21942 | 150 | 1259229 | 141 | 7 / 14 | 3 / 12 | 21 / 6.9 % | APPRENTISSAGE |
| [38541720121](https://github.com/cgoubert14000/my/actions/runs/38541720121) | 2026-10-14T14:56:36+00:00 | 330 | 9654 | 584 / 329 / 21950 | 523 | 2671125 | 3992 | 93 / 77 | 26 / 116 | 137 / 17.0 % | FIABILITÉ INSUFFISANTE |
| [38585200409](https://github.com/cgoubert14000/my/actions/runs/38585200409) | 2026-10-14T20:34:13+00:00 | 330 | 8337 | 575 / 327 / 21004 | 250 | 1548738 | 1137 | 15 / 73 | 0 / 44 | 181 / 12.8 % | FIABILITÉ INSUFFISANTE |
| [38633303619](https://github.com/cgoubert14000/my/actions/runs/38633303619) | 2026-10-15T00:04:06+00:00 | 205 | 6015 | 580 / 327 / 21784 | 800 | 785592 | 361 | 27 / 12 | 3 / 29 | 210 / 12.3 % | FIABILITÉ INSUFFISANTE |

**Totaux** : 1797 min, 46861 blocs, 8537863 candidats, 6053 à net attendu > 0, 151 simulations réussies / 203 échouées, 32/225 étiquettes N+1 positives.

Décision de maturité : elle n'est jamais prise sur cette table mais par le moteur (≥ 30 observations par segment, borne inférieure ≥ 75 %) ; tant que le statut est APPRENTISSAGE / FIABILITÉ INSUFFISANTE, aucun passage en réel n'est proposé.
