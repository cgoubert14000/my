# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T20:41:00+00:00 ; durée 272.92 min ; blocs 52731965 → 52740148 (7713 vus)

## Connexion
- Requêtes RPC : 91868 ; erreurs : 10 ; latence p50/p95 : 128.3/2,027.9 ms
- Rafraîchissements d'état : 7713 ; âge des données au dernier bloc : 5.33 s ; changements de frais LP observés (pools à frais dynamiques) : 9464
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28774 ; cycles déclenchés par événement : 1404 ; avance médiane sur le rafraîchissement multicall : 1,673 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,411.43 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21110 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3916 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2411.894998, 'AERO': 0.849168, 'cbBTC': 81312.167025}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,229,757 | 2,411.432982 | 52740149 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,134,871 | 1.168774 | 52740149 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,959,183 | 0.029621 | 52740149 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,193,331 | 0.029643 | 52740149 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,877,172 | 106.528276 | 52740149 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,429,404 | 0.029634 | 52740149 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,748,673 | 0.000012 | 52740149 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 9,434,317 | 0.000012 | 52740149 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,093,217 | 2,417.151703 | 52740149 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,471,436 | 2,416.534517 | 52740149 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,842,521 | 0.000012 | 52740149 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,135,017 | 0.001666 | 52740149 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,402,627 | 2,415.200236 | 52740149 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,332,961 | 0.029642 | 52740149 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,243,644 | 0.025517 | 52740149 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,236,597 | 1.000855 | 52740149 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,820,020 | 0.802398 | 52740149 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,634,046 | 0.000273 | 52740149 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,495,186 | 1.172912 | 52740149 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,471,160 | 2,416.403189 | 52740149 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,417,343 | 0.998808 | 52740149 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,083,457 | 33,076.377503 | 52740149 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,402,279 | 2,822.131083 | 52740149 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 403 | 3,064,046 | 2,421.415464 | 52740149 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,910,840 | 1.141811 | 52740149 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,832,747 | 0.000012 | 52740149 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,628,650 | 403.458975 | 52740149 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,578,659 | 1,012.330442 | 52740149 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,568,163 | 106.500789 | 52740149 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,509,576 | 0.000011 | 52740149 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,236,390 | 1,180,271.726776 | 52740149 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,132,704 | 1.123257 | 52740149 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,107,543 | 1.199039 | 52740149 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52740149 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,869,677 | 0.000000 | 52740149 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,815,186 | 0.021941 | 52740149 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,666 | 0.018189 | 52740149 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,877 | 0.000012 | 52740149 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,772,847 | 13,622.302890 | 52740149 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,739,027 | 15.842858 | 52740149 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,670,448 | 2.305701 | 52740149 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,541,245 | 0.916547 | 52740149 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,526,374 | 2,824.425906 | 52740149 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,575 | 1.105495 | 52740149 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,479,250 | 2,825.400176 | 52740149 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,301 | 0.826340 | 52740149 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,344,573 | 0.000000 | 52740149 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,316,821 | 0.435668 | 52740149 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,313,434 | 0.004726 | 52740149 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,298,766 | 0.000274 | 52740149 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,249,241 | 62.265951 | 52740149 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,247,170 | 23.341839 | 52740149 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,230,955 | 1.131367 | 52740149 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/cbBTC | 3000 | 1,230,115 | 0.029642 | 52740149 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,216,404 | 1.105716 | 52740149 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,202,447 | 34,964,089.908430 | 52740149 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,195,093 | 2,417.071076 | 52740149 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,170,880 | 1,150,234.390163 | 52740149 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,254 | 511,033.421561 | 52740149 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,121,890 | 14.018134 | 52740149 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 9116 ; routes examinées : 192438760 ; candidats optimisés : 1304679 ; net attendu > 0 : 260 ; dernier cycle 398.5 ms
- Rejets (moteur) : {'spread_below_threshold': 189406579, 'liquidity_below_min': 1447872, 'negative_expected_net': 1304419, 'pool_quarantined': 249022, 'cycle_budget_exhausted': 21498, 'borrow_bound_too_small': 9110}
- Enregistrements de la session : 1304679 ; net attendu > 0 : 260 ; simulés (eth_call de la vraie tx) : 57 (ok 4, échec 53) ; étiquettes ghost N+1 : 0/36 positives
- Décisions : {'REJECTED': 1304679} ; motifs de rejet : {'below_safety_margin': 200, 'negative_expected_net': 1304419, 'p_lower_below_threshold': 181, 'price_impact': 68, 'reliability_not_demonstrated': 79, 'simulation_failed': 53}

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
- Observations ghost : 778 ; taux observé 0.117 ; borne inférieure crédible (0.9) 0.103 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
