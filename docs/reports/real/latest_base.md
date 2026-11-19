# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-19T05:29:34+00:00 ; durée 307.35 min ; blocs 59286760 → 59378967 (24084 vus)

## Connexion
- Requêtes RPC : 212184 ; erreurs : 0 ; latence p50/p95 : 127.1/1,525.8 ms
- Rafraîchissements d'état : 24084 ; âge des données au dernier bloc : 6.54 s ; changements de frais LP observés (pools à frais dynamiques) : 11668
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 24978 ; cycles déclenchés par événement : 8134 ; avance médiane sur le rafraîchissement multicall : 134 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,799.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 433 pools, 250 jetons, 13330 routes
- Par DEX : uniswap_v3 127, aerodrome 174, aerodrome_slipstream 92, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 265, par paires 0), mesurés 435, sous le plancher de 10000.0 $ : 2 → gardés 433 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1773.13587, 'cbBTC': 62614.282936, 'AERO': 0.431427}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 86,822,085 | 1,799.767095 | 59378966 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 24,847,511 | 1,796.988950 | 59378966 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,888,134 | 0.028347 | 59378966 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,857,246 | 0.028330 | 59378966 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,865,192 | 79.811086 | 59378966 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,055,203 | 0.000016 | 59378966 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,273,003 | 0.028358 | 59378966 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,686,330 | 2.269373 | 59378966 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,369,288 | 1,796.328319 | 59378966 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,338,936 | 1.000000 | 59378966 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,772,642 | 39,432.226123 | 59378966 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 162 | 2,353,826 | 1,796.112006 | 59378966 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,886,651 | 0.000016 | 59378966 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,754,850 | 0.028340 | 59378966 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,693,794 | 1,144,477.909863 | 59378966 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,462,202 | 0.000016 | 59378966 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,717 | 0.843371 | 59378966 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,349,141 | 0.000000 | 59378966 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,326,371 | 0.006652 | 59378966 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,272,747 | 0.000016 | 59378966 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,218,680 | 447.553742 | 59378966 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,127,885 | 13.787612 | 59378966 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,061,339 | 86.264254 | 59378966 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/VVV | 10000 | 1,060,453 | 79.799763 | 59378966 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,037,270 | 15,786.090854 | 59378966 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,034,307 | 1,801.247987 | 59378966 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/AERO | 3000 | 1,033,103 | 4,077.914187 | 59378966 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 998,376 | 1,799.832646 | 59378966 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/doginme | 10000 | 935,720 | 31,519,877.580382 | 59378966 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 926,292 | 0.044389 | 59378966 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 879,087 | 55.363263 | 59378966 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 845,736 | 517,955.142948 | 59378966 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 832,339 | 0.000000 | 59378966 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 810,834 | 22,199,987.083100 | 59378966 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 802,945 | 0.001541 | 59378966 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 770,031 | 1,054.995359 | 59378966 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | XDP/USDC | 100 | 768,251 | 0.016375 | 59378966 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | WETH/USDC | 500 | 733,142 | 1,797.181936 | 59378966 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 728,609 | 0.047192 | 59378966 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/USDC | 10000 | 706,534 | 1,787.047081 | 59378966 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/SAPIEN | 4575 | 683,845 | 26.079960 | 59378966 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 610,891 | 0.798842 | 59378966 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 607,151 | 1,796.434441 | 59378966 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 591,787 | 0.440068 | 59378966 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/AERO | 10000 | 580,701 | 4,061.408622 | 59378966 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 573,615 | 4,680,480.035879 | 59378966 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 527,616 | 523,055.608422 | 59378966 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 522,238 | 1.378082 | 59378966 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 505,092 | 0.032317 | 59378966 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 495,755 | 167,554.146125 | 59378966 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 484,679 | 0.000241 | 59378966 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 461,817 | 0.000007 | 59378966 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/USDT | 8 | 461,701 | 1.001131 | 59378966 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 419,687 | 1,055.016143 | 59378966 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 418,966 | 0.058765 | 59378966 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/UNI | 10000 | 402,265 | 343.709326 | 59378966 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 394,820 | 23.934791 | 59378966 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 390,521 | 845,495.033346 | 59378966 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/VVV | 2718 | 378,861 | 79.825502 | 59378966 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/SPX | 10000 | 375,891 | 5,632.236374 | 59378966 | `0xe96a4E9EA3a2C6Db214174738a19Eb7Dbb8A3069` |

## Recherche d'opportunités
- Cycles : 32217 ; routes examinées : 429452610 ; candidats optimisés : 30943 ; net attendu > 0 : 0 ; dernier cycle 2077.2 ms
- Rejets (moteur) : {'spread_below_threshold': 420483405, 'liquidity_below_min': 6482343, 'borrow_bound_too_small': 32217, 'negative_expected_net': 30943, 'cycle_budget_exhausted': 1462}
- Enregistrements de la session : 56 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 56} ; motifs de rejet : {'negative_expected_net': 56}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 59342270 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.33 |
| 59342270 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.33 |
| 59342270 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.33 |
| 59287994 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.41 |
| 59287994 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.41 |
| 59287994 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.41 |
| 59298995 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.55 |
| 59298995 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.55 |
| 59298995 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.55 |
| 59296383 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0029 | -31.55 |

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
