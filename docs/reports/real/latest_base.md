# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T23:05:19+00:00 ; durée 268.87 min ; blocs 52995614 → 53003679 (7518 vus)

## Connexion
- Requêtes RPC : 91427 ; erreurs : 118 ; latence p50/p95 : 310.2/1,970.4 ms
- Rafraîchissements d'état : 7518 ; âge des données au dernier bloc : 6.34 s ; changements de frais LP observés (pools à frais dynamiques) : 13289
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55309 ; cycles déclenchés par événement : 3954 ; avance médiane sur le rafraîchissement multicall : 897 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,363.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 317 jetons, 19488 routes
- Par DEX : uniswap_v3 138, aerodrome 222, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 359, par paires 0), mesurés 548, sous le plancher de 10000.0 $ : 2 → gardés 546 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2404.297357, 'AERO': 0.765849, 'cbBTC': 81434.30056}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,813,185 | 2,363.729936 | 53003680 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,340,384 | 0.029305 | 53003680 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,369,280 | 95.958783 | 53003680 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,140,385 | 0.029279 | 53003680 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | USDC/AERO | 3000 | 9,969,468 | 1.369998 | 53003680 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,719,944 | 0.000012 | 53003680 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,720,622 | 0.029272 | 53003680 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,617,996 | 2,369.652030 | 53003680 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,049,570 | 0.001654 | 53003680 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 6,307,204 | 0.000012 | 53003680 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 833 | 5,492,896 | 2,369.689508 | 53003680 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,404,895 | 0.029309 | 53003680 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 4,871,714 | 0.000012 | 53003680 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,494,209 | 2,369.483076 | 53003680 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,245,378 | 0.999388 | 53003680 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,193,047 | 2,363.455503 | 53003680 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,931,981 | 34,238.157285 | 53003680 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,327,674 | 0.000271 | 53003680 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 463 | 2,778,419 | 2,373.606681 | 53003680 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,485,136 | 95.952032 | 53003680 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,253,038 | 404.896493 | 53003680 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,150,989 | 1,224,301.247088 | 53003680 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,003,732 | 3,221.839496 | 53003680 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,922,776 | 0.000000 | 53003680 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,920,204 | 0.000012 | 53003680 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,735,208 | 0.000012 | 53003680 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,727,421 | 0.017284 | 53003680 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,300 | 1.607287 | 53003680 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,488,834 | 3,244.791300 | 53003680 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,261 | 0.824379 | 53003680 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,385,194 | 13,822.640431 | 53003680 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,361,109 | 0.005019 | 53003680 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,277,930 | 2,369.590031 | 53003680 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,270,406 | 0.000269 | 53003680 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,244,241 | 0.000000 | 53003680 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/msETH (stable) | 500 | 1,238,246 | 2.306692 | 53003680 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,227,434 | 64.498001 | 53003680 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,175,544 | 35,616,621.346345 | 53003680 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,152,466 | 1,108,230.900997 | 53003680 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,132,868 | 48.817794 | 53003680 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,130,127 | 495,610.449757 | 53003680 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,117,890 | 16.465317 | 53003680 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,070,760 | 74,718.382498 | 53003680 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,054,579 | 0.040599 | 53003680 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,038,104 | 21,704,064.273104 | 53003680 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,368 | 17.102209 | 53003680 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 969,543 | 23.151343 | 53003680 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 939,760 | 1,062.251387 | 53003680 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 900,731 | 0.000544 | 53003680 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 877,308 | 17.994529 | 53003680 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 872,380 | 0.000009 | 53003680 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 856,197 | 0.066354 | 53003680 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/USDC | 3000 | 852,718 | 2,363.609015 | 53003680 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 817,249 | 1.105909 | 53003680 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 800,277 | 0.803225 | 53003680 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 789,537 | 2,373.724925 | 53003680 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 780,087 | 95.404362 | 53003680 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 764,439 | 0.636332 | 53003680 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 758,396 | 4,583,768.469135 | 53003680 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 735,734 | 0.678119 | 53003680 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 11471 ; routes examinées : 223546848 ; candidats optimisés : 968645 ; net attendu > 0 : 538 ; dernier cycle 309.0 ms
- Rejets (moteur) : {'spread_below_threshold': 219187304, 'liquidity_below_min': 3376288, 'negative_expected_net': 968107, 'borrow_bound_too_small': 11470, 'cycle_budget_exhausted': 2961, 'unquotable': 180}
- Enregistrements de la session : 968645 ; net attendu > 0 : 538 ; simulés (eth_call de la vraie tx) : 30 (ok 24, échec 6) ; étiquettes ghost N+1 : 8/27 positives
- Décisions : {'REJECTED': 968645} ; motifs de rejet : {'below_safety_margin': 369, 'negative_expected_net': 968107, 'p_lower_below_threshold': 481, 'reliability_not_demonstrated': 57, 'simulation_failed': 6, 'stale_data': 68}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.013052 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1048 €) | — | 1.07 | 0.001 (n=7) | REJECTED | below_safety_margin(140<261), reliability_not_demonstrated |
| 52997859 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.013052 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1048 €) | — | 1.07 | 0.001 (n=7) | REJECTED | below_safety_margin(140<261), reliability_not_demonstrated |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.469736 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1044 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(47310295624478<93947291756440), reliability_not_demonstrated |
| 52997859 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.469736 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1044 €) | — | 1.01 | 0.001 (n=7) | REJECTED | below_safety_margin(47310295624478<93947291756440), reliability_not_demonstrated |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,085.695509 USDC | 0.121282 USDC | 0.000000 USDC | 0.007951 USDC | 0.113331 USDC (0.1043 €) | — | 1.04 | 0.001 (n=7) | REJECTED | below_safety_margin(113331<217139), reliability_not_demonstrated |
| 52997859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,085.695509 USDC | 0.121282 USDC | 0.000000 USDC | 0.007951 USDC | 0.113331 USDC (0.1043 €) | — | 1.04 | 0.001 (n=7) | REJECTED | below_safety_margin(113331<217139), reliability_not_demonstrated |
| 52997059 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 67.235756 USDC | 0.069204 USDC | 0.000000 USDC | 0.005568 USDC | 0.063636 USDC (0.0585 €) | — | 9.46 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53003254 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.095406 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0573 €) | 0.000026 WETH | 2.75 | 0.241 (n=120) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 53003254 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 224.689943 USDC | 0.069242 USDC | 0.000000 USDC | 0.007140 USDC | 0.062102 USDC (0.0571 €) | — | 2.76 | 0.241 (n=120) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 53003254 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.092290 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0537 €) | 0.000025 WETH | 2.67 | 0.241 (n=120) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 53003254 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 218.375881 USDC | 0.065348 USDC | 0.000000 USDC | 0.007140 USDC | 0.058208 USDC (0.0536 €) | — | 2.67 | 0.241 (n=120) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 52997045 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[aerodrome_slipstream]→WETH | 0.011664 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0519 €) | 0.000024 WETH | 20.17 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53003161 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.078367 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0509 €) | 0.000023 WETH | 2.96 | 0.020 (n=72) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53003161 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002264 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0508 €) | — | 3.00 | 0.003 (n=109) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53003254 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.087078 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0476 €) | 0.000022 WETH | 2.50 | 0.127 (n=246) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53003254 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 206.267305 USDC | 0.059030 USDC | 0.000000 USDC | 0.007500 USDC | 0.051530 USDC (0.0474 €) | — | 2.50 | 0.127 (n=246) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53003254 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.073583 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0467 €) | — | 2.91 | 0.241 (n=120) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 53003254 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 173.433731 USDC | 0.057765 USDC | 0.000000 USDC | 0.007140 USDC | 0.050625 USDC (0.0466 €) | — | 2.92 | 0.241 (n=120) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 53003254 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.093477 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0391 €) | — | 1.92 | 0.127 (n=246) | REJECTED | below_safety_margin(17931723791041<18695388703592), p_lower_below_threshold(0.13<0.75) |
| 53003254 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 221.057250 USDC | 0.049513 USDC | 0.000000 USDC | 0.007140 USDC | 0.042373 USDC (0.0390 €) | — | 1.92 | 0.127 (n=246) | REJECTED | below_safety_margin(42373<44211), p_lower_below_threshold(0.13<0.75) |
| 53003254 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.089382 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0356 €) | — | 1.83 | 0.127 (n=246) | REJECTED | below_safety_margin(16329187217836<17876401577257), p_lower_below_threshold(0.13<0.75) |
| 53003254 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 211.189029 USDC | 0.045726 USDC | 0.000000 USDC | 0.007140 USDC | 0.038586 USDC (0.0355 €) | — | 1.83 | 0.127 (n=246) | REJECTED | below_safety_margin(38586<42237), p_lower_below_threshold(0.13<0.75) |
| 53003254 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.067657 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0301 €) | — | 2.04 | 0.127 (n=246) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53003254 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 159.678104 USDC | 0.039736 USDC | 0.000000 USDC | 0.007140 USDC | 0.032596 USDC (0.0300 €) | — | 2.04 | 0.127 (n=246) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53003341 | WETH→[aerodrome_slipstream]→uSOL→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.050606 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0298 €) | — | 2.72 | 0.235 (n=123) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 2076 ; taux observé 0.099 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
