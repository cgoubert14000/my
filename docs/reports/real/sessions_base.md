# Sessions de marché réel — base (généré 2026-10-13T22:52:43Z)

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
| [38475616089](https://github.com/cgoubert14000/my/actions/runs/38475616089) | 2026-10-13T22:52:43+00:00 | 40 | 1165 | 579 / 328 / 21606 | 419 | 344805 | 4 | 1 / 1 | 0 / 1 | 1 / 0.6 % | APPRENTISSAGE |

**Totaux** : 311 min, 5456 blocs, 471570 candidats, 69 à net attendu > 0, 1 simulations réussies / 18 échouées, 0/16 étiquettes N+1 positives.

Décision de maturité : elle n'est jamais prise sur cette table mais par le moteur (≥ 30 observations par segment, borne inférieure ≥ 75 %) ; tant que le statut est APPRENTISSAGE / FIABILITÉ INSUFFISANTE, aucun passage en réel n'est proposé.
