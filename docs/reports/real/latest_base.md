# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T21:39:34+00:00 ; durée 6.12 min ; blocs 60100131 → 60101958 (335 vus)

## Connexion
- Requêtes RPC : 4025 ; erreurs : 0 ; latence p50/p95 : 293.1/958.5 ms
- Rafraîchissements d'état : 335 ; âge des données au dernier bloc : 7.08 s ; changements de frais LP observés (pools à frais dynamiques) : 375
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1173 ; cycles déclenchés par événement : 260 ; avance médiane sur le rafraîchissement multicall : 487 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,614.87 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 245 jetons, 12256 routes
- Par DEX : uniswap_v3 122, aerodrome_slipstream 86, aerodrome 166, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1605.51254, 'cbBTC': 58557.611788, 'AERO': 0.386499}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,102,760 | 1,614.865163 | 60101980 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,838,274 | 0.027522 | 60101980 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,341,491 | 1,617.138900 | 60101980 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,078,364 | 0.027458 | 60101980 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,146,366 | 80.161972 | 60101980 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,423,863 | 0.000017 | 60101980 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,758,390 | 0.027515 | 60101980 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,294,506 | 2.567405 | 60101980 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,089,888 | 0.998739 | 60101980 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,920,105 | 1,617.314113 | 60101980 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,456,919 | 40,429.373014 | 60101980 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 293 | 2,107,472 | 1,617.017605 | 60101980 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,764,298 | 0.000017 | 60101980 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 1,582,314 | 0.027469 | 60101980 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,536,665 | 1,119,463.985823 | 60101980 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,580 | 0.843948 | 60101980 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,277,429 | 0.000017 | 60101980 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,247,079 | 0.000000 | 60101980 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,146,223 | 0.000017 | 60101980 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,140,363 | 0.006433 | 60101980 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,079,373 | 15.409818 | 60101980 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,614 | 86.545397 | 60101980 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 960,816 | 455.164575 | 60101980 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 953,398 | 1,614.298406 | 60101980 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 938,834 | 16,549.850252 | 60101980 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 921,318 | 4,152.061547 | 60101980 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 919,528 | 80.592350 | 60101980 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 906,186 | 0.049589 | 60101980 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 861,492 | 1,614.442699 | 60101980 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 851,723 | 30,737,078.911590 | 60101980 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 758,977 | 517,250.959523 | 60101980 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 758,956 | 74.276816 | 60101980 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 737,944 | 0.001524 | 60101980 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 735,386 | 21,879,764.326289 | 60101980 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 716,725 | 24.603167 | 60101980 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | DRB/WETH | 10000 | 715,127 | 0.000000 | 60101980 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | XDP/USDC | 100 | 714,079 | 0.014320 | 60101980 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 697,368 | 0.043236 | 60101980 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 678,670 | 1,076.070249 | 60101980 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 661,817 | 1,603.269352 | 60101980 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 646,781 | 1,617.298713 | 60101980 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | uXRP/WETH | 3000 | 645,946 | 0.000607 | 60101980 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/USDC | 100 | 560,679 | 1,617.362252 | 60101980 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 548,412 | 0.379740 | 60101980 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 547,937 | 0.799406 | 60101980 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 514,467 | 4,689,495.089175 | 60101980 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 500,218 | 4,185.295625 | 60101980 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | ELSA/USDC | 100 | 484,399 | 0.070324 | 60101980 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 480,283 | 0.029978 | 60101980 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4061 | 474,064 | 515,881.668556 | 60101980 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 471,969 | 1.479983 | 60101980 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 416,179 | 191,780.719400 | 60101980 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 413,269 | 0.000007 | 60101980 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 368,681 | 1,075.921401 | 60101980 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 364,325 | 21.874197 | 60101980 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 363,187 | 833,522.709084 | 60101980 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 362,684 | 0.054697 | 60101980 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 342,760 | 369.094078 | 60101980 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2775 | 335,876 | 80.166794 | 60101980 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 333,665 | 0.000234 | 60101980 | `0x21594b992F68495dD28d605834b58889d0a727c7` |

## Recherche d'opportunités
- Cycles : 594 ; routes examinées : 7280064 ; candidats optimisés : 51845 ; net attendu > 0 : 63 ; dernier cycle 178.6 ms
- Rejets (moteur) : {'spread_below_threshold': 7031057, 'liquidity_below_min': 111843, 'negative_expected_net': 51782, 'borrow_bound_too_small': 6232, 'cycle_budget_exhausted': 1174}
- Enregistrements de la session : 48854 ; net attendu > 0 : 63 ; simulés (eth_call de la vraie tx) : 1 (ok 1, échec 0) ; étiquettes ghost N+1 : 1/1 positives
- Décisions : {'REJECTED': 48854} ; motifs de rejet : {'below_safety_margin': 62, 'negative_expected_net': 48791, 'p_lower_below_threshold': 63}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60101418 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 81.076662 USDC | 0.017252 USDC | 0.000000 USDC | 0.004918 USDC | 0.012334 USDC (0.0113 €) | — | 1.52 | 0.359 (n=663) | REJECTED | below_safety_margin(12334<16215), p_lower_below_threshold(0.36<0.75) |
| 60101418 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.050096 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0113 €) | — | 1.52 | 0.359 (n=663) | REJECTED | below_safety_margin(7613934097133<10019136977695), p_lower_below_threshold(0.36<0.75) |
| 60101418 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 80.260116 USDC | 0.015997 USDC | 0.000000 USDC | 0.004918 USDC | 0.011079 USDC (0.0102 €) | — | 1.38 | 0.280 (n=1679) | REJECTED | below_safety_margin(11079<16052), p_lower_below_threshold(0.28<0.75) |
| 60101418 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.050091 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0102 €) | — | 1.37 | 0.280 (n=1679) | REJECTED | below_safety_margin(6839069183607<10018148638869), p_lower_below_threshold(0.28<0.75) |
| 60100786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005193 USDC | 0.010080 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10080<36349), p_lower_below_threshold(0.17<0.75) |
| 60100786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005193 USDC | 0.010080 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10080<36349), p_lower_below_threshold(0.17<0.75) |
| 60100785 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005197 USDC | 0.010076 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10076<36349), p_lower_below_threshold(0.17<0.75) |
| 60100786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005197 USDC | 0.010076 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10076<36349), p_lower_below_threshold(0.17<0.75) |
| 60100786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6239758834343<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60100786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6239758834343<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60100785 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0092 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6237127405493<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60100786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0092 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6237127405493<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60101418 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001377 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 1.23 | 0.280 (n=1679) | REJECTED | below_safety_margin(17<27), p_lower_below_threshold(0.28<0.75) |
| 60100785 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60100786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60100786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60100786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60101418 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 85.674002 USDC | 0.014813 USDC | 0.000000 USDC | 0.004918 USDC | 0.009895 USDC (0.0091 €) | — | 1.15 | 0.280 (n=1679) | REJECTED | below_safety_margin(9895<17134), p_lower_below_threshold(0.28<0.75) |
| 60101418 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.052214 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0090 €) | — | 1.16 | 0.280 (n=1679) | REJECTED | below_safety_margin(6055416258292<10442866324375), p_lower_below_threshold(0.28<0.75) |
| 60101418 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.036927 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0066 €) | — | 1.20 | 0.280 (n=1679) | REJECTED | below_safety_margin(4447129726124<7385355360943), p_lower_below_threshold(0.28<0.75) |
| 60101418 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 59.629937 USDC | 0.012067 USDC | 0.000000 USDC | 0.004918 USDC | 0.007149 USDC (0.0066 €) | — | 1.20 | 0.280 (n=1679) | REJECTED | below_safety_margin(7149<11925), p_lower_below_threshold(0.28<0.75) |
| 60101418 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000985 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0065 €) | — | 1.22 | 0.280 (n=1679) | REJECTED | below_safety_margin(12<19), p_lower_below_threshold(0.28<0.75) |
| 60101418 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 41.161326 USDC | 0.011632 USDC | 0.000000 USDC | 0.004918 USDC | 0.006714 USDC (0.0062 €) | — | 1.63 | 0.359 (n=663) | REJECTED | below_safety_margin(6714<8232), p_lower_below_threshold(0.36<0.75) |
| 60101418 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 65.598538 USDC | 0.011620 USDC | 0.000000 USDC | 0.004918 USDC | 0.006702 USDC (0.0062 €) | — | 1.02 | 0.280 (n=1679) | REJECTED | below_safety_margin(6702<13119), p_lower_below_threshold(0.28<0.75) |
| 60101418 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.025661 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0062 €) | — | 1.61 | 0.359 (n=663) | REJECTED | below_safety_margin(4141260952128<5132161893313), p_lower_below_threshold(0.36<0.75) |

## Fiabilité et décision
- Observations ghost : 8767 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
