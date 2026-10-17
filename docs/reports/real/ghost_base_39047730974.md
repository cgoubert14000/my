# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T21:23:22+00:00 ; durée 315.28 min ; blocs 52731965 → 52741420 (8820 vus)

## Connexion
- Requêtes RPC : 104983 ; erreurs : 10 ; latence p50/p95 : 142.3/1,978.2 ms
- Rafraîchissements d'état : 8821 ; âge des données au dernier bloc : 1.85 s ; changements de frais LP observés (pools à frais dynamiques) : 10617
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28774 ; cycles déclenchés par événement : 1404 ; avance médiane sur le rafraîchissement multicall : 1,673 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,415.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21110 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3916 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2411.894998, 'AERO': 0.849168, 'cbBTC': 81312.167025}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,370,892 | 2,415.058233 | 52741420 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,107,529 | 1.170201 | 52741420 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,217,880 | 0.029658 | 52741420 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,903,746 | 106.513500 | 52741420 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,438,717 | 0.029621 | 52741420 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,442,972 | 0.029634 | 52741420 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,751,391 | 0.000012 | 52741420 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,102,961 | 2,416.684822 | 52741420 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,845,615 | 0.000012 | 52741420 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 773 | 7,645,691 | 2,415.453862 | 52741420 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,132,876 | 0.001661 | 52741420 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 6,553,396 | 0.000012 | 52741420 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,406,685 | 2,416.371996 | 52741420 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,340,831 | 0.029646 | 52741420 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,244,469 | 1.000855 | 52741420 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,240,481 | 0.025517 | 52741420 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,827,266 | 0.802398 | 52741420 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,641,078 | 0.000273 | 52741420 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,488,470 | 1.172914 | 52741420 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,424,276 | 2,415.719705 | 52741420 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,421,842 | 0.998808 | 52741420 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,112,122 | 32,714.986530 | 52741420 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,402,758 | 2,822.441216 | 52741420 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 439 | 3,069,040 | 2,420.837363 | 52741420 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,915,216 | 1.141811 | 52741420 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,834,654 | 0.000012 | 52741420 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,810,573 | 0.000010 | 52741420 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,593,295 | 404.820591 | 52741420 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,572,143 | 106.504694 | 52741420 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,239,752 | 1,180,271.726776 | 52741420 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,132,701 | 1.123256 | 52741420 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,582 | 1.200159 | 52741420 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,540 | 1.418010 | 52741420 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,915,305 | 15.841437 | 52741420 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,873,020 | 0.000000 | 52741420 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,815,261 | 0.021941 | 52741420 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,774,932 | 0.000012 | 52741420 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,740,323 | 0.018158 | 52741420 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,672,819 | 2.305988 | 52741420 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,611,464 | 1,010.329790 | 52741420 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,543,562 | 0.916547 | 52741420 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,529,419 | 13,645.632109 | 52741420 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,527,249 | 2,826.917497 | 52741420 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,520,858 | 1.105495 | 52741420 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3008 | 1,478,786 | 2,826.050173 | 52741420 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,401 | 0.826229 | 52741420 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,336,117 | 0.000000 | 52741420 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,051 | 0.435782 | 52741420 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,315,406 | 0.004726 | 52741420 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,731 | 0.000273 | 52741420 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,249,241 | 62.265951 | 52741420 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,249,045 | 23.341836 | 52741420 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,231,667 | 0.029640 | 52741420 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,218,233 | 1.105716 | 52741420 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,197,134 | 1.131439 | 52741420 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,196,107 | 2,416.685586 | 52741420 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,194,580 | 35,814,934.488960 | 52741420 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,172,641 | 1,150,234.390163 | 52741420 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,139,965 | 511,033.421561 | 52741420 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,123,379 | 13.965762 | 52741420 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 10224 ; routes examinées : 215828640 ; candidats optimisés : 1464305 ; net attendu > 0 : 263 ; dernier cycle 290.1 ms
- Rejets (moteur) : {'spread_below_threshold': 212456983, 'liquidity_below_min': 1626614, 'negative_expected_net': 1464042, 'pool_quarantined': 249022, 'cycle_budget_exhausted': 21498, 'borrow_bound_too_small': 10218}
- Enregistrements de la session : 1464305 ; net attendu > 0 : 263 ; simulés (eth_call de la vraie tx) : 59 (ok 6, échec 53) ; étiquettes ghost N+1 : 0/38 positives
- Décisions : {'REJECTED': 1464305} ; motifs de rejet : {'below_safety_margin': 201, 'negative_expected_net': 1464042, 'p_lower_below_threshold': 181, 'price_impact': 68, 'reliability_not_demonstrated': 82, 'simulation_failed': 53}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52732232 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 264.379140 USDC | 0.953137 USDC | 0.000000 USDC | 0.005417 USDC | 0.947720 USDC (0.8719 €) | — | 35.85 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52739066 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 5,817.804447 USDC | 0.920842 USDC | 0.000000 USDC | 0.005416 USDC | 0.915426 USDC (0.8422 €) | — | 1.57 | 0.060 (n=5) | REJECTED | below_safety_margin(915426<1163560), reliability_not_demonstrated |
| 52739066 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.071462 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.8413 €) | — | 1.57 | 0.060 (n=5) | REJECTED | below_safety_margin(1124<1429), reliability_not_demonstrated |
| 52739066 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.056698 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3234 €) | — | 0.76 | 0.060 (n=5) | REJECTED | below_safety_margin(432<1133), reliability_not_demonstrated |
| 52739066 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 4,835.644447 USDC | 0.356364 USDC | 0.000000 USDC | 0.005416 USDC | 0.350948 USDC (0.3229 €) | — | 0.73 | 0.060 (n=5) | REJECTED | below_safety_margin(350948<967128), reliability_not_demonstrated |
| 52732691 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 82.007926 USDC | 0.093812 USDC | 0.000000 USDC | 0.005413 USDC | 0.088399 USDC (0.0813 €) | — | 10.78 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52739066 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,433.670995 USDC | 0.089233 USDC | 0.000000 USDC | 0.007614 USDC | 0.081619 USDC (0.0751 €) | — | 0.57 | 0.112 (n=83) | REJECTED | below_safety_margin(81619<286734), p_lower_below_threshold(0.11<0.75) |
| 52739066 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.599916 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0750 €) | — | 0.56 | 0.112 (n=83) | REJECTED | below_safety_margin(33796008972771<119983109842836), p_lower_below_threshold(0.11<0.75) |
| 52739066 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.017725 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0749 €) | — | 0.56 | 0.112 (n=83) | REJECTED | below_safety_margin(100<354), p_lower_below_threshold(0.11<0.75) |
| 52739066 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,261.524411 USDC | 0.077333 USDC | 0.000000 USDC | 0.005416 USDC | 0.071917 USDC (0.0662 €) | — | 0.57 | 0.037 (n=22) | REJECTED | below_safety_margin(71917<252304), reliability_not_demonstrated |
| 52739066 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.015466 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0659 €) | — | 0.57 | 0.037 (n=22) | REJECTED | below_safety_margin(88<309), reliability_not_demonstrated |
| 52733290 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 73.561974 USDC | 0.076184 USDC | 0.000000 USDC | 0.005410 USDC | 0.070774 USDC (0.0651 €) | — | 9.62 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52733325 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.429660 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0639 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(28823934244612<85931943319960), p_lower_below_threshold(0.11<0.75) |
| 52733326 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.429660 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0639 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(28823934244612<85931943319960), p_lower_below_threshold(0.11<0.75) |
| 52733325 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,030.836384 USDC | 0.076442 USDC | 0.000000 USDC | 0.007239 USDC | 0.069203 USDC (0.0637 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(69203<206167), p_lower_below_threshold(0.11<0.75) |
| 52733326 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,030.836384 USDC | 0.076442 USDC | 0.000000 USDC | 0.007239 USDC | 0.069203 USDC (0.0637 €) | — | 0.67 | 0.114 (n=81) | REJECTED | below_safety_margin(69203<206167), p_lower_below_threshold(0.11<0.75) |
| 52732602 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 71.137118 USDC | 0.070045 USDC | 0.000000 USDC | 0.005414 USDC | 0.064631 USDC (0.0595 €) | — | 9.09 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52739066 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 452.617647 USDC | 0.065925 USDC | 0.000000 USDC | 0.007614 USDC | 0.058311 USDC (0.0536 €) | — | 1.29 | 0.112 (n=83) | REJECTED | below_safety_margin(58311<90523), p_lower_below_threshold(0.11<0.75) |
| 52739066 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.192202 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0532 €) | — | 1.25 | 0.112 (n=83) | REJECTED | below_safety_margin(23997530628883<38440344199474), p_lower_below_threshold(0.11<0.75) |
| 52739066 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004567 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0531 €) | — | 1.55 | 0.112 (n=83) | REJECTED | below_safety_margin(71<91), p_lower_below_threshold(0.11<0.75) |
| 52732142 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 66.177836 USDC | 0.061275 USDC | 0.000000 USDC | 0.005418 USDC | 0.055857 USDC (0.0514 €) | — | 8.44 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52733101 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003508 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0501 €) | — | 1.91 | 0.114 (n=81) | REJECTED | below_safety_margin(67<70), p_lower_below_threshold(0.11<0.75) |
| 52733100 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003508 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0501 €) | — | 1.91 | 0.114 (n=81) | REJECTED | below_safety_margin(67<70), p_lower_below_threshold(0.11<0.75) |
| 52733101 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.129765 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0495 €) | — | 1.72 | 0.114 (n=81) | REJECTED | below_safety_margin(22316890957272<25953007010325), p_lower_below_threshold(0.11<0.75) |
| 52733100 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.129765 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0495 €) | — | 1.72 | 0.114 (n=81) | REJECTED | below_safety_margin(22316890957272<25953007010325), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 780 ; taux observé 0.117 ; borne inférieure crédible (0.9) 0.103 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
