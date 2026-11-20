# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T21:57:50+00:00 ; durée 24.4 min ; blocs 60100131 → 60107439 (1707 vus)

## Connexion
- Requêtes RPC : 18112 ; erreurs : 0 ; latence p50/p95 : 264.0/947.7 ms
- Rafraîchissements d'état : 1707 ; âge des données au dernier bloc : 7.43 s ; changements de frais LP observés (pools à frais dynamiques) : 1471
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6505 ; cycles déclenchés par événement : 1242 ; avance médiane sur le rafraîchissement multicall : 263 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,618.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 245 jetons, 12256 routes
- Par DEX : uniswap_v3 122, aerodrome_slipstream 86, aerodrome 166, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1605.51254, 'cbBTC': 58557.611788, 'AERO': 0.386499}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,267,292 | 1,618.823838 | 60107458 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,364,897 | 0.027442 | 60107458 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,374,638 | 1,616.415636 | 60107458 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,099,473 | 0.027458 | 60107458 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,162,420 | 80.137088 | 60107458 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,392,869 | 0.000017 | 60107458 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,769,069 | 0.027436 | 60107458 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,303,569 | 2.553337 | 60107458 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,106,524 | 0.998734 | 60107458 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,914,882 | 1,615.870058 | 60107458 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,463,726 | 40,403.654496 | 60107458 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 138 | 2,112,154 | 1,615.939446 | 60107458 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,774,005 | 0.000017 | 60107458 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,586,696 | 0.027469 | 60107458 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,542,504 | 1,116,458.215704 | 60107458 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,580 | 0.843948 | 60107458 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,283,487 | 0.000017 | 60107458 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,250,136 | 0.000000 | 60107458 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,155,980 | 0.006476 | 60107458 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,152,090 | 0.000017 | 60107458 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,083,571 | 15.275978 | 60107458 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,614 | 86.545397 | 60107458 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 963,973 | 453.404322 | 60107458 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 954,572 | 1,619.001971 | 60107458 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 944,230 | 16,541.213024 | 60107458 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 925,562 | 4,136.507113 | 60107458 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 918,983 | 80.449196 | 60107458 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 908,091 | 0.049624 | 60107458 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 862,547 | 1,619.160778 | 60107458 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 854,246 | 30,694,187.732271 | 60107458 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 760,836 | 517,254.116912 | 60107458 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 760,676 | 73.941302 | 60107458 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 744,260 | 0.001533 | 60107458 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 737,187 | 21,879,794.167717 | 60107458 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 720,116 | 0.000000 | 60107458 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 717,875 | 24.549344 | 60107458 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | XDP/USDC | 100 | 712,944 | 0.014278 | 60107458 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 697,401 | 0.043240 | 60107458 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 681,168 | 1,073.637556 | 60107458 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 662,840 | 1,613.105205 | 60107458 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 648,187 | 1,616.539759 | 60107458 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | uXRP/WETH | 3000 | 647,529 | 0.000607 | 60107458 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/USDC | 100 | 561,708 | 1,615.902799 | 60107458 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 549,280 | 0.799406 | 60107458 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 549,038 | 0.380573 | 60107458 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 522,311 | 4,572,345.683068 | 60107458 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 502,206 | 4,163.697335 | 60107458 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 482,961 | 0.030215 | 60107458 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 475,230 | 514,577.010221 | 60107458 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| pancakeswap_v3 | ELSA/USDC | 100 | 474,972 | 0.068607 | 60107458 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | USDC/MAI (stable) | 3000 | 471,969 | 1.479983 | 60107458 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 418,577 | 190,522.164475 | 60107458 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 415,540 | 0.000007 | 60107458 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 370,252 | 1,073.901778 | 60107458 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 365,235 | 21.871349 | 60107458 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 364,742 | 835,128.924360 | 60107458 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 363,775 | 0.055026 | 60107458 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 345,975 | 365.871981 | 60107458 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2724 | 336,738 | 80.148740 | 60107458 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 334,483 | 0.000234 | 60107458 | `0x21594b992F68495dD28d605834b58889d0a727c7` |

## Recherche d'opportunités
- Cycles : 2948 ; routes examinées : 36130688 ; candidats optimisés : 96514 ; net attendu > 0 : 208 ; dernier cycle 133.2 ms
- Rejets (moteur) : {'spread_below_threshold': 35049032, 'liquidity_below_min': 568267, 'negative_expected_net': 96306, 'borrow_bound_too_small': 11064, 'cycle_budget_exhausted': 1291}
- Enregistrements de la session : 66203 ; net attendu > 0 : 208 ; simulés (eth_call de la vraie tx) : 13 (ok 3, échec 10) ; étiquettes ghost N+1 : 4/11 positives
- Décisions : {'REJECTED': 66203} ; motifs de rejet : {'below_safety_margin': 185, 'negative_expected_net': 65995, 'p_lower_below_threshold': 198, 'price_impact': 3, 'reliability_not_demonstrated': 10, 'sim_below_estimate': 1, 'simulation_failed': 10, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60102844 | USDC→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 104.322676 USDC | 0.024527 USDC | 0.000000 USDC | 0.003227 USDC | 0.021300 USDC (0.0196 €) | — | 2.04 | 0.351 (n=1) | REJECTED | reliability_not_demonstrated |
| 60102844 | WETH→[pancakeswap_v3]→USDC→[uniswap_v2]→WETH | 0.064567 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0195 €) | — | 2.03 | 0.351 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 60102832 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 100.541010 USDC | 0.024709 USDC | 0.000000 USDC | 0.004988 USDC | 0.019721 USDC (0.0181 €) | — | 1.96 | 0.280 (n=1680) | REJECTED | below_safety_margin(19721<20108), p_lower_below_threshold(0.28<0.75) |
| 60102832 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.061972 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0181 €) | — | 1.96 | 0.280 (n=1680) | REJECTED | below_safety_margin(12127415079541<12394357277085), p_lower_below_threshold(0.28<0.75) |
| 60102832 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 94.229329 USDC | 0.022269 USDC | 0.000000 USDC | 0.004988 USDC | 0.017281 USDC (0.0159 €) | — | 1.83 | 0.280 (n=1680) | REJECTED | below_safety_margin(17281<18845), p_lower_below_threshold(0.28<0.75) |
| 60102832 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.058329 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0158 €) | — | 1.82 | 0.280 (n=1680) | REJECTED | below_safety_margin(10625551544050<11665742124250), p_lower_below_threshold(0.28<0.75) |
| 60102844 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 43.921763 USDC | 0.021449 USDC | 0.000000 USDC | 0.004988 USDC | 0.016461 USDC (0.0151 €) | — | 3.75 | 0.225 (n=1322) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 60102844 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.027075 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0151 €) | — | 3.74 | 0.225 (n=1322) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.23<0.75) |
| 60102832 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 123.247161 USDC | 0.019929 USDC | 0.000000 USDC | 0.004763 USDC | 0.015166 USDC (0.0140 €) | — | 1.23 | 0.347 (n=162) | REJECTED | below_safety_margin(15166<24649), p_lower_below_threshold(0.35<0.75) |
| 60102832 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 91.506573 USDC | 0.020095 USDC | 0.000000 USDC | 0.004988 USDC | 0.015107 USDC (0.0139 €) | — | 1.65 | 0.280 (n=1680) | REJECTED | below_safety_margin(15107<18301), p_lower_below_threshold(0.28<0.75) |
| 60102832 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.056175 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0138 €) | — | 1.65 | 0.280 (n=1680) | REJECTED | below_safety_margin(9287975629564<11234947264873), p_lower_below_threshold(0.28<0.75) |
| 60102832 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.001770 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0136 €) | — | 1.41 | 0.347 (n=162) | REJECTED | below_safety_margin(25<35), p_lower_below_threshold(0.35<0.75) |
| 60102844 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 60.497497 USDC | 0.018261 USDC | 0.000000 USDC | 0.004763 USDC | 0.013498 USDC (0.0124 €) | — | 2.23 | 0.219 (n=95) | REJECTED | stale_data(4687ms>4000.0), p_lower_below_threshold(0.22<0.75) |
| 60102844 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.037339 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0124 €) | — | 2.22 | 0.219 (n=95) | REJECTED | stale_data(4685ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 60102850 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 78.273790 USDC | 0.016128 USDC | 0.000000 USDC | 0.003508 USDC | 0.012620 USDC (0.0116 €) | — | 1.61 | 0.264 (n=33) | REJECTED | below_safety_margin(12620<15654), p_lower_below_threshold(0.26<0.75) |
| 60102850 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.048043 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0116 €) | — | 1.61 | 0.264 (n=33) | REJECTED | below_safety_margin(7756381787290<9608686715666), p_lower_below_threshold(0.26<0.75) |
| 60101418 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 81.076662 USDC | 0.017252 USDC | 0.000000 USDC | 0.004918 USDC | 0.012334 USDC (0.0113 €) | — | 1.52 | 0.359 (n=663) | REJECTED | below_safety_margin(12334<16215), p_lower_below_threshold(0.36<0.75) |
| 60101418 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.050096 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0113 €) | — | 1.52 | 0.359 (n=663) | REJECTED | below_safety_margin(7613934097133<10019136977695), p_lower_below_threshold(0.36<0.75) |
| 60102844 | USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 37.840437 USDC | 0.017031 USDC | 0.000000 USDC | 0.004988 USDC | 0.012043 USDC (0.0111 €) | — | 3.18 | 0.225 (n=1322) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 60102844 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.023533 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0110 €) | — | 3.14 | 0.225 (n=1322) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 60102832 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 45.987862 USDC | 0.016472 USDC | 0.000000 USDC | 0.004988 USDC | 0.011484 USDC (0.0106 €) | — | 2.50 | 0.280 (n=1680) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 60102832 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000667 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0103 €) | — | 2.85 | 0.280 (n=1680) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 60101418 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 80.260116 USDC | 0.015997 USDC | 0.000000 USDC | 0.004918 USDC | 0.011079 USDC (0.0102 €) | — | 1.38 | 0.280 (n=1679) | REJECTED | below_safety_margin(11079<16052), p_lower_below_threshold(0.28<0.75) |
| 60101418 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.050091 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0102 €) | — | 1.37 | 0.280 (n=1679) | REJECTED | below_safety_margin(6839069183607<10018148638869), p_lower_below_threshold(0.28<0.75) |
| 60100786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005193 USDC | 0.010080 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10080<36349), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 8777 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
