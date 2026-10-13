# 09 — MEV, concurrence et qualité d'exécution

## Ce qui change sur un L2 par rapport à Ethereum

* **Pas de mempool publique** : sur Base et Arbitrum, les transactions vont directement au séquenceur. Le
  front-running classique (voir une tx en attente et passer devant) n'existe pas ; un relais privé type Flashbots
  Protect n'apporte rien ici.
* **Le jeu est le backrunning** : qui, après un gros swap qui déséquilibre un pool, remet le prix en place le premier.
  Sur Base, les **Flashblocks** (sous-blocs de 200 ms depuis juillet 2025) ordonnent par priority fee à l'intérieur de
  chaque sous-bloc : la compétition est une enchère de frais à très haute fréquence, et des analyses 2025–2026
  attribuent ≈ 80 % de la MEV capturée à deux entités. Sur Arbitrum, **Timeboost** (avril 2025) vend une voie express
  (≈ 200 ms d'avance) aux enchères ; le priority fee n'a pas d'effet d'ordonnancement hors voie express.
* Conséquence pour ce bot : l'opportunité détectée au bloc N peut avoir disparu avant l'inclusion ; la transaction
  revert alors proprement (`InsufficientProfit`) et coûte le gaz. **La probabilité de succès que mesure le mode ghost
  (re-simulation au bloc N+1) est précisément la part des écarts qui survivent à cette concurrence.**

## Ce que le bot fait

| Mesure | Mécanisme |
|---|---|
| Protection on-chain | `minProfit` ≥ gaz + marge ; `minAmountOut` par saut = quote × (1 − slippage) ; `deadline` courte ; revert = seule perte possible = gaz |
| Latence | lecture multicall par bloc (p50 ≈ 3 ms sur devnet, à mesurer sur votre RPC : `verify-chain` affiche p50/max), quote locale exacte, cycle complet ≈ 300–450 ms pour 700 routes ; `grid_points` ajusté automatiquement si le cycle dépasse la moitié du temps de bloc |
| Prix du gaz | base fee du bloc + priority fee ≥ plancher configurable, plafonné par la politique ; pas d'enchère agressive automatique (une guerre d'enchères sur Flashblocks consomme le budget sans garantie) |
| Mesure de la concurrence | taux ghost par segment ; écart simulation N vs N+1 ; part des reverts `InsufficientProfit` dans les exécutions réelles |
| Soumission | RPC du séquenceur (`submission: public_rpc`) ; un envoi via WS ou un RPC géographiquement proche réduit la latence de quelques dizaines de ms |

## Ce que le bot ne fait pas (et pourquoi)

* Pas d'achat de voie express Timeboost ni d'enchère de priority fee dynamique : coût non borné, incompatible avec un
  budget de 10–20 €.
* Pas de bundles ni de relais privés : inexistants ou inutiles sur ces réseaux.
* Pas de « sandwich » ni de stratégie nuisible aux autres utilisateurs : hors périmètre et contraire à l'objectif.

## Lecture honnête

Sur des marchés aussi disputés, un bot domestique avec un RPC public arrive structurellement après les acteurs
colocalisés. Le système ne cache pas cela : il **mesure** le taux de survie des écarts, refuse d'exécuter si la borne
inférieure est sous 75 %, et borne la perte au gaz plafonné. Les segments où un petit acteur garde une chance sont
généralement les routes à 3 sauts mêlant courbes différentes (V2/V3/Solidly) avec des marges plus larges — ce que le
laboratoire fait ressortir dans ses tableaux par segment.
