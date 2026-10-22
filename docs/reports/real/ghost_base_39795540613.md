# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T15:11:20+00:00 ; durée 39.66 min ; blocs 52945073 → 52946263 (1156 vus)

## Connexion
- Requêtes RPC : 14355 ; erreurs : 0 ; latence p50/p95 : 285.8/1,289.3 ms
- Rafraîchissements d'état : 1156 ; âge des données au dernier bloc : 5.7 s ; changements de frais LP observés (pools à frais dynamiques) : 3738
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 30206 ; cycles déclenchés par événement : 982 ; avance médiane sur le rafraîchissement multicall : 673 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,402.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 318 jetons, 19398 routes
- Par DEX : uniswap_v3 137, aerodrome 226, aerodrome_slipstream 137, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3827 (énumérés 366, par paires 0), mesurés 549, sous le plancher de 10000.0 $ : 3 → gardés 546 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2404.811718, 'AERO': 0.81356, 'cbBTC': 81633.413427}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,256,837 | 2,402.980451 | 52946263 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 18,369,607 | 1.249713 | 52946263 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,282,213 | 0.029433 | 52946263 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,533,932 | 92.685535 | 52946263 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,276,200 | 0.029434 | 52946263 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,421,895 | 0.000012 | 52946263 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,405,938 | 0.029448 | 52946263 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,731,416 | 2,396.960739 | 52946263 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,172,616 | 0.001671 | 52946263 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 6,812,196 | 0.000012 | 52946263 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,909,673 | 2,396.061250 | 52946263 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 5,511,988 | 0.000012 | 52946263 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,408,649 | 0.029425 | 52946263 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,504,830 | 2,396.369671 | 52946263 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,317,105 | 2,402.387327 | 52946263 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,293,248 | 1.000001 | 52946263 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,981,048 | 34,545.060818 | 52946263 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,486,968 | 0.000275 | 52946263 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 484 | 2,914,710 | 2,400.799133 | 52946263 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2745 | 2,567,694 | 92.707279 | 52946263 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,342,650 | 2,973.782467 | 52946263 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,302,227 | 399.568423 | 52946263 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,217,848 | 0.000012 | 52946263 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,204,013 | 1,205,946.672315 | 52946263 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,055,678 | 0.000012 | 52946263 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,903,610 | 0.000000 | 52946263 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,796,009 | 0.018514 | 52946263 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,661,386 | 1.521320 | 52946263 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,626,797 | 2,995.013719 | 52946263 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,240 | 0.823520 | 52946263 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,410,593 | 13,565.308086 | 52946263 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,363,865 | 0.004962 | 52946263 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,324,190 | 2,396.990252 | 52946263 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/msETH (stable) | 500 | 1,309,307 | 2.370267 | 52946263 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,815 | 0.000274 | 52946263 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,275,642 | 0.000000 | 52946263 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,679 | 64.262670 | 52946263 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,198,218 | 35,205,844.186300 | 52946263 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,188,391 | 16.260104 | 52946263 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,183,367 | 1,095,186.495351 | 52946263 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,150,233 | 499,670.732841 | 52946263 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,149,474 | 47.633472 | 52946263 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,105,606 | 0.000010 | 52946263 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/EDEL | 7000 | 1,105,324 | 74,355.404644 | 52946263 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,097,112 | 1.105751 | 52946263 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,063,811 | 21,408,920.470197 | 52946263 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,977 | 17.109607 | 52946263 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,016,751 | 0.029436 | 52946263 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,012,998 | 23.041127 | 52946263 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 986,067 | 0.038655 | 52946263 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 960,782 | 1,059.633626 | 52946263 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 940,109 | 2,417.796200 | 52946263 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 916,344 | 0.000548 | 52946263 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | EURC/USDC | 79 | 898,617 | 1.120399 | 52946263 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/bsdETH | 100 | 895,079 | 0.916099 | 52946263 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4665 | 886,056 | 17.688548 | 52946263 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 877,213 | 2,402.979861 | 52946263 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 815,885 | 0.803225 | 52946263 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | fBOMB/USDC | 10000 | 809,617 | 0.018711 | 52946263 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 804,002 | 1.106136 | 52946263 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 2137 ; routes examinées : 41453526 ; candidats optimisés : 231377 ; net attendu > 0 : 99 ; dernier cycle 633.7 ms
- Rejets (moteur) : {'spread_below_threshold': 40883410, 'liquidity_below_min': 336085, 'negative_expected_net': 231278, 'borrow_bound_too_small': 2136, 'cycle_budget_exhausted': 243}
- Enregistrements de la session : 231377 ; net attendu > 0 : 99 ; simulés (eth_call de la vraie tx) : 10 (ok 4, échec 6) ; étiquettes ghost N+1 : 3/10 positives
- Décisions : {'REJECTED': 231377} ; motifs de rejet : {'below_safety_margin': 26, 'negative_expected_net': 231278, 'p_lower_below_threshold': 76, 'reliability_not_demonstrated': 23, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52945116 | USDC→[aerodrome]→msUSD→[aerodrome_slipstream]→USDC | 158.467777 USDC | 0.135546 USDC | 0.000000 USDC | 0.005350 USDC | 0.130196 USDC (0.1198 €) | 0.130196 USDC | 8.22 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52945355 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011478 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0864 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(115<229), reliability_not_demonstrated |
| 52945355 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011478 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0864 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(115<229), reliability_not_demonstrated |
| 52945355 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.396421 WETH | 0.000042 WETH | 0.000000 WETH | 0.000004 WETH | 0.000039 WETH (0.0861 €) | — | 0.98 | 0.001 (n=6) | REJECTED | below_safety_margin(38902885680636<79284157046047), reliability_not_demonstrated |
| 52945355 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.396421 WETH | 0.000042 WETH | 0.000000 WETH | 0.000004 WETH | 0.000039 WETH (0.0861 €) | — | 0.98 | 0.001 (n=6) | REJECTED | below_safety_margin(38902885680636<79284157046047), reliability_not_demonstrated |
| 52945355 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 938.256390 USDC | 0.102083 USDC | 0.000000 USDC | 0.008621 USDC | 0.093462 USDC (0.0860 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(93462<187651), reliability_not_demonstrated |
| 52945355 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 938.256390 USDC | 0.102083 USDC | 0.000000 USDC | 0.008621 USDC | 0.093462 USDC (0.0860 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(93462<187651), reliability_not_demonstrated |
| 52945918 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.003258 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0669 €) | — | 2.73 | 0.107 (n=215) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52945918 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 298.996989 USDC | 0.079509 USDC | 0.000000 USDC | 0.007536 USDC | 0.071973 USDC (0.0662 €) | — | 2.41 | 0.107 (n=215) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52945946 | USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→WETH→[uniswap_v3]→USDC | 37.990947 USDC | 0.063097 USDC | 0.000000 USDC | 0.007188 USDC | 0.055909 USDC (0.0514 €) | — | 14.72 | 0.011 (n=130) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52945946 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→WETH | 0.015765 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0513 €) | — | 14.70 | 0.011 (n=130) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52945946 | USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 37.367320 USDC | 0.060723 USDC | 0.000000 USDC | 0.007188 USDC | 0.053535 USDC (0.0493 €) | — | 14.33 | 0.011 (n=130) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52945946 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→WETH | 0.015472 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0492 €) | — | 14.34 | 0.011 (n=130) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52945946 | USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 36.531022 USDC | 0.058158 USDC | 0.000000 USDC | 0.007188 USDC | 0.050970 USDC (0.0469 €) | — | 13.95 | 0.021 (n=14) | REJECTED | reliability_not_demonstrated |
| 52945946 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→WETH | 0.015179 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0468 €) | — | 13.92 | 0.021 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52945918 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002155 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0436 €) | — | 2.69 | 0.107 (n=215) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52945918 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.083102 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0434 €) | — | 2.36 | 0.107 (n=215) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52945918 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 136.012357 USDC | 0.051809 USDC | 0.000000 USDC | 0.007536 USDC | 0.044273 USDC (0.0407 €) | — | 3.26 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52945918 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001566 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0406 €) | — | 3.45 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52945918 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002067 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0338 €) | — | 2.18 | 0.107 (n=215) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52945918 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.067535 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0337 €) | — | 2.25 | 0.107 (n=215) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52945918 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.073205 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0334 €) | — | 2.06 | 0.107 (n=215) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52945918 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002155 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0331 €) | — | 2.04 | 0.107 (n=215) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52945978 | cbBTC→[aerodrome]→FLOCK→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000269 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0316 €) | — | 15.60 | 0.055 (n=15) | REJECTED | reliability_not_demonstrated |
| 52945978 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→FLOCK→[aerodrome_slipstream]→USDC | 21.203284 USDC | 0.040781 USDC | 0.000000 USDC | 0.007192 USDC | 0.033589 USDC (0.0309 €) | 0.033589 USDC | 15.84 | 0.055 (n=15) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1895 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
