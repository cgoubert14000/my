# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T15:17:27+00:00 ; durée 45.78 min ; blocs 52945073 → 52946446 (1318 vus)

## Connexion
- Requêtes RPC : 16377 ; erreurs : 0 ; latence p50/p95 : 398.0/1,337.5 ms
- Rafraîchissements d'état : 1318 ; âge des données au dernier bloc : 6.38 s ; changements de frais LP observés (pools à frais dynamiques) : 4495
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 37215 ; cycles déclenchés par événement : 1113 ; avance médiane sur le rafraîchissement multicall : 918 ms
- Gaz : base fee 0.005025 gwei ; prix ETH (pool le plus profond) : 2,393.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 318 jetons, 19398 routes
- Par DEX : uniswap_v3 137, aerodrome 226, aerodrome_slipstream 137, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3827 (énumérés 366, par paires 0), mesurés 549, sous le plancher de 10000.0 $ : 3 → gardés 546 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2404.811718, 'AERO': 0.81356, 'cbBTC': 81633.413427}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,861,094 | 2,393.628843 | 52946447 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 18,350,721 | 1.252287 | 52946447 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,229,476 | 0.029368 | 52946447 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,464,511 | 92.793079 | 52946447 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,245,056 | 0.029426 | 52946447 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,414,657 | 0.000012 | 52946447 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 9,376,593 | 0.029425 | 52946447 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,706,893 | 2,392.804515 | 52946447 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,159,237 | 0.001670 | 52946447 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 6,807,609 | 0.000012 | 52946447 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 564 | 5,874,188 | 2,393.364984 | 52946447 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 5,505,697 | 0.000012 | 52946447 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,390,934 | 0.029369 | 52946447 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,491,574 | 2,393.614096 | 52946447 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,308,696 | 2,392.661548 | 52946447 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,285,886 | 1.000001 | 52946447 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,965,371 | 34,548.267859 | 52946447 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,473,398 | 0.000275 | 52946447 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 421 | 2,905,724 | 2,396.615095 | 52946447 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,556,538 | 92.814222 | 52946447 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,335,659 | 2,982.432706 | 52946447 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,292,743 | 399.845552 | 52946447 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,215,928 | 0.000012 | 52946447 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,195,435 | 1,205,946.672315 | 52946447 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,053,674 | 0.000012 | 52946447 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,896,201 | 0.000000 | 52946447 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,795,995 | 0.018515 | 52946447 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,661,386 | 1.521320 | 52946447 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,621,613 | 2,998.041773 | 52946447 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,240 | 0.823520 | 52946447 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,406,685 | 13,605.766016 | 52946447 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,371,405 | 0.005018 | 52946447 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,320,527 | 2,392.711787 | 52946447 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/msETH (stable) | 500 | 1,297,888 | 2.368210 | 52946447 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,757 | 0.000273 | 52946447 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,265,393 | 0.000000 | 52946447 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,679 | 64.262670 | 52946447 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,555 | 35,205,844.186300 | 52946447 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,179,356 | 1,094,082.944795 | 52946447 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,179,125 | 16.343249 | 52946447 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/NOCK | 3000 | 1,151,149 | 47.491694 | 52946447 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,145,750 | 500,017.713432 | 52946447 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,103,555 | 0.000010 | 52946447 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/EDEL | 7000 | 1,101,245 | 74,325.330550 | 52946447 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,092,843 | 1.105751 | 52946447 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,059,671 | 21,408,920.470197 | 52946447 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,945 | 17.111077 | 52946447 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,013,900 | 0.029406 | 52946447 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,008,719 | 23.031212 | 52946447 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 983,164 | 0.038816 | 52946447 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 953,530 | 1,065.428812 | 52946447 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,875 | 2,409.501940 | 52946447 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 912,778 | 0.000548 | 52946447 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | EURC/USDC | 70 | 898,545 | 1.120282 | 52946447 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/bsdETH | 100 | 891,596 | 0.916099 | 52946447 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 885,719 | 17.699723 | 52946447 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 875,508 | 2,392.811179 | 52946447 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 812,710 | 0.803225 | 52946447 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | fBOMB/USDC | 10000 | 809,617 | 0.018711 | 52946447 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 800,873 | 1.106136 | 52946447 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 2430 ; routes examinées : 47137140 ; candidats optimisés : 279694 ; net attendu > 0 : 164 ; dernier cycle 684.8 ms
- Rejets (moteur) : {'spread_below_threshold': 46470839, 'liquidity_below_min': 383366, 'negative_expected_net': 279530, 'borrow_bound_too_small': 2429, 'cycle_budget_exhausted': 812}
- Enregistrements de la session : 279694 ; net attendu > 0 : 164 ; simulés (eth_call de la vraie tx) : 13 (ok 4, échec 9) ; étiquettes ghost N+1 : 3/13 positives
- Décisions : {'REJECTED': 279694} ; motifs de rejet : {'below_safety_margin': 76, 'negative_expected_net': 279530, 'p_lower_below_threshold': 136, 'reliability_not_demonstrated': 28, 'simulation_failed': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52946299 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017489 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2258 €) | — | 1.72 | 0.001 (n=6) | REJECTED | below_safety_margin(301<349), reliability_not_demonstrated |
| 52946299 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.595274 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000102 WETH (0.2257 €) | — | 1.72 | 0.001 (n=6) | REJECTED | below_safety_margin(102399355594060<119054820899875), reliability_not_demonstrated |
| 52946299 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,478.363420 USDC | 0.252661 USDC | 0.000000 USDC | 0.008652 USDC | 0.244009 USDC (0.2245 €) | — | 1.65 | 0.001 (n=6) | REJECTED | below_safety_margin(244009<295672), reliability_not_demonstrated |
| 52946299 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.316550 WETH | 0.000099 WETH | 0.000000 WETH | 0.000003 WETH | 0.000096 WETH (0.2116 €) | — | 3.03 | 0.094 (n=190) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 52946299 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009285 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2116 €) | — | 3.04 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52946299 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 764.368596 USDC | 0.237843 USDC | 0.000000 USDC | 0.008282 USDC | 0.229561 USDC (0.2112 €) | — | 3.00 | 0.094 (n=190) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 52946299 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.269461 WETH | 0.000074 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1573 €) | — | 2.65 | 0.022 (n=64) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52946299 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 644.411865 USDC | 0.176635 USDC | 0.000000 USDC | 0.006021 USDC | 0.170614 USDC (0.1570 €) | — | 2.65 | 0.022 (n=64) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52945116 | USDC→[aerodrome]→msUSD→[aerodrome_slipstream]→USDC | 158.467777 USDC | 0.135546 USDC | 0.000000 USDC | 0.005350 USDC | 0.130196 USDC (0.1198 €) | 0.130196 USDC | 8.22 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52946299 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.390994 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1189 €) | — | 1.38 | 0.003 (n=2) | REJECTED | below_safety_margin(53933268041385<78198898589374), reliability_not_demonstrated |
| 52946299 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 936.046966 USDC | 0.134941 USDC | 0.000000 USDC | 0.006021 USDC | 0.128920 USDC (0.1186 €) | — | 1.38 | 0.003 (n=2) | REJECTED | below_safety_margin(128920<187209), reliability_not_demonstrated |
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

## Fiabilité et décision
- Observations ghost : 1898 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
