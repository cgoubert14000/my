# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-13T13:50:18+00:00 ; durée 265.05 min ; blocs 56857674 → 56937174 (17443 vus)

## Connexion
- Requêtes RPC : 191018 ; erreurs : 160 ; latence p50/p95 : 530.0/1,599.2 ms
- Rafraîchissements d'état : 17443 ; âge des données au dernier bloc : 8.39 s ; changements de frais LP observés (pools à frais dynamiques) : 8879
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6586 ; cycles déclenchés par événement : 2517 ; avance médiane sur le rafraîchissement multicall : 160 ms
- Gaz : base fee 0.005009 gwei ; prix ETH (pool le plus profond) : 1,977.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 455 pools, 262 jetons, 14628 routes
- Par DEX : uniswap_v3 134 (quarantaine 1), aerodrome_slipstream 96 (quarantaine 1), aerodrome 185, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 155 (rejetés 2) → 560 jetons ; pools candidats 3601 (énumérés 280, par paires 0), mesurés 457, sous le plancher de 10000.0 $ : 2 → gardés 455 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1933.662602, 'cbBTC': 68796.84734, 'AERO': 0.479684}
- Pools en quarantaine : 2 — uniswap_v3:WETH/AIKEK@0x4815C5: liquidity call failed; aerodrome_slipstream:WETH/cbLTC@0x200681: fee call failed

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 127,418,585 | 1,977.085199 | 56937201 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,160,459 | 0.028316 | 56937201 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,385,423 | 0.028284 | 56937201 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 7,032,939 | 0.000014 | 56937201 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,779,480 | 1,972.159076 | 56937201 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,708,235 | 101.172999 | 56937201 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,411,781 | 0.028322 | 56937201 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,103,030 | 1,972.066919 | 56937201 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 3,984,821 | 2.035997 | 56937201 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 3,679,328 | 0.998549 | 56937201 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,936,966 | 42,408.964810 | 56937201 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 247 | 2,687,532 | 1,971.870299 | 56937201 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,109,199 | 0.028298 | 56937201 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,855,647 | 1,150,683.415637 | 56937201 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,674,677 | 0.017227 | 56937201 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,549,644 | 0.000014 | 56937201 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 1,528,554 | 0.000014 | 56937201 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,485,702 | 0.000000 | 56937201 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,257 | 0.833740 | 56937201 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,447,475 | 0.006498 | 56937201 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,359,572 | 423.555131 | 56937201 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,332,175 | 0.000014 | 56937201 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,166,909 | 14,953.336266 | 56937201 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,166,086 | 4,019.523467 | 56937201 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,104,676 | 1,976.497286 | 56937201 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,075,165 | 1,972.252073 | 56937201 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,806 | 86.350896 | 56937201 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | WETH/USDC | 3000 | 1,059,924 | 1,975.884014 | 56937201 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,045,316 | 1.383900 | 56937201 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,007,374 | 33,449,957.209001 | 56937201 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,004,586 | 101.573533 | 56937201 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 985,256 | 19.787497 | 56937201 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 917,150 | 538,684.559840 | 56937201 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 886,023 | 0.051261 | 56937201 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 882,269 | 0.001538 | 56937201 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 875,198 | 22,848,662.254471 | 56937201 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 859,851 | 967.329961 | 56937201 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 800,494 | 0.000000 | 56937201 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 753,983 | 82.738851 | 56937201 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 747,072 | 0.049723 | 56937201 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 746,238 | 23.083451 | 56937201 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 743,225 | 1,967.128377 | 56937201 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/wstETH | 3000 | 670,312 | 0.800670 | 56937201 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 663,144 | 0.527550 | 56937201 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/AERO | 10000 | 651,731 | 4,051.767785 | 56937201 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 628,374 | 4,695,817.200904 | 56937201 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 608,254 | 0.465097 | 56937201 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 606,909 | 134,635.368577 | 56937201 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 566,965 | 535,084.192230 | 56937201 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 564,099 | 0.000266 | 56937201 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,877 | 0.038009 | 56937201 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v3 | WETH/USDC | 100 | 543,206 | 1,972.097160 | 56937201 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 520,286 | 0.000007 | 56937201 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 482,416 | 967.160557 | 56937201 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 473,071 | 0.068420 | 56937201 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 455,757 | 0.492254 | 56937201 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 11 | 449,557 | 1.001010 | 56937201 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 430,964 | 331.967541 | 56937201 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 425,405 | 24.391198 | 56937201 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 419,375 | 887,851.984568 | 56937201 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 19959 ; routes examinées : 291960252 ; candidats optimisés : 26405 ; net attendu > 0 : 44 ; dernier cycle 2504.4 ms
- Rejets (moteur) : {'spread_below_threshold': 285437548, 'liquidity_below_min': 4184486, 'pool_quarantined': 682128, 'negative_expected_net': 26361, 'borrow_bound_too_small': 14874, 'cycle_budget_exhausted': 4596}
- Enregistrements de la session : 176 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 176} ; motifs de rejet : {'negative_expected_net': 176}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 56857997 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.24 |
| 56857997 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.24 |
| 56857997 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.24 |
| 56863207 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 56863207 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 56863207 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 56864089 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 56864151 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 56864151 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |
| 56864151 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -41.35 |

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
