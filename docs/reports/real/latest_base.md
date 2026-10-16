# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T08:11:17+00:00 ; durée 113.88 min ; blocs 52671044 → 52674463 (3050 vus)

## Connexion
- Requêtes RPC : 36954 ; erreurs : 270 ; latence p50/p95 : 348.4/1,851.0 ms
- Rafraîchissements d'état : 3050 ; âge des données au dernier bloc : 2.91 s ; changements de frais LP observés (pools à frais dynamiques) : 7884
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4182 ; cycles déclenchés par événement : 246 ; avance médiane sur le rafraîchissement multicall : 1,333 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,450.52 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 327 jetons, 21788 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 392, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 3 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2445.329592, 'AERO': 0.931569, 'cbBTC': 81962.021553}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,240,970 | 2,450.516709 | 52674462 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 48,050,015 | 1.043967 | 52674462 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,522,721 | 0.029856 | 52674462 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,545,992 | 100.438365 | 52674462 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,543,368 | 0.029813 | 52674462 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,605,088 | 0.029799 | 52674462 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,740,126 | 0.000012 | 52674462 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,142,905 | 2,454.873933 | 52674462 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 8,125,062 | 0.000012 | 52674462 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,940,148 | 2,455.434373 | 52674462 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,534,094 | 0.000012 | 52674462 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,245,965 | 0.001688 | 52674462 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,044,391 | 1.040294 | 52674462 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,636,147 | 0.024549 | 52674462 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,449,726 | 2,450.685460 | 52674462 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,417,021 | 0.029862 | 52674462 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,236,330 | 1.000855 | 52674462 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,898,083 | 0.802398 | 52674462 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,771,271 | 0.000281 | 52674462 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,368,911 | 2,455.198854 | 52674462 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,358,156 | 0.998881 | 52674462 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,070,321 | 34,378.063505 | 52674462 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 403 | 3,772,848 | 2,458.560415 | 52674462 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,639,591 | 2,549.081348 | 52674462 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,048,055 | 1.141826 | 52674462 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,862,832 | 400.915705 | 52674462 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,845,934 | 0.000012 | 52674462 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,673,434 | 100.426560 | 52674462 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,489,614 | 0.000012 | 52674462 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 2,458,879 | 992.606378 | 52674462 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,301,193 | 1,151,160.279250 | 52674462 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52674462 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,107,964 | 0.000000 | 52674462 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,016,109 | 15.263441 | 52674462 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52674462 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,872,015 | 0.023425 | 52674462 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,324 | 0.019000 | 52674463 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,330 | 0.000012 | 52674463 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,708,054 | 13,443.945453 | 52674462 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,691,117 | 2.310270 | 52674462 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,595,391 | 2,563.071040 | 52674463 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,523,210 | 0.916551 | 52674462 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,515,171 | 1.105492 | 52674462 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3128 | 1,506,088 | 2,562.008829 | 52674462 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,179 | 0.829157 | 52674462 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,373,637 | 0.000000 | 52674462 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,370,987 | 0.004828 | 52674462 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,356,136 | 23.199960 | 52674462 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,338,340 | 0.000282 | 52674462 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,301,614 | 0.436479 | 52674462 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,270,484 | 1.123953 | 52674462 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,250,965 | 62.094409 | 52674462 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,226,011 | 34,505,057.205265 | 52674462 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,217,425 | 0.029794 | 52674462 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,216,029 | 1.105591 | 52674462 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,204,822 | 2,454.829919 | 52674462 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,193,886 | 0.886142 | 52674462 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,193,367 | 1,143,450.992518 | 52674462 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,175,974 | 496,085.125904 | 52674462 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,141,174 | 13.428430 | 52674462 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 3295 ; routes examinées : 71791460 ; candidats optimisés : 362397 ; net attendu > 0 : 73 ; dernier cycle 261.6 ms
- Rejets (moteur) : {'spread_below_threshold': 70851192, 'liquidity_below_min': 566172, 'negative_expected_net': 362324, 'pool_quarantined': 7588, 'borrow_bound_too_small': 3295, 'cycle_budget_exhausted': 816}
- Enregistrements de la session : 362397 ; net attendu > 0 : 73 ; simulés (eth_call de la vraie tx) : 15 (ok 9, échec 6) ; étiquettes ghost N+1 : 0/11 positives
- Décisions : {'REJECTED': 362397} ; motifs de rejet : {'below_safety_margin': 54, 'negative_expected_net': 362324, 'p_lower_below_threshold': 30, 'price_impact': 6, 'reliability_not_demonstrated': 43, 'simulation_failed': 6, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.028664 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1011 €) | — | 0.47 | 0.001 (n=10) | REJECTED | below_safety_margin(134<573), reliability_not_demonstrated |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.051068 WETH | 0.000047 WETH | 0.000000 WETH | 0.000002 WETH | 0.000045 WETH (0.1011 €) | — | 0.43 | 0.001 (n=10) | REJECTED | below_safety_margin(44910967314113<210213569031069), reliability_not_demonstrated |
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007406 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0264 €) | — | 0.47 | 0.072 (n=50) | REJECTED | below_safety_margin(35<148), p_lower_below_threshold(0.07<0.75) |
| 52671989 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 665.496868 USDC | 0.036012 USDC | 0.000000 USDC | 0.007407 USDC | 0.028605 USDC (0.0263 €) | — | 0.43 | 0.072 (n=50) | REJECTED | below_safety_margin(28605<133099), p_lower_below_threshold(0.07<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.232200 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0262 €) | — | 0.50 | 0.072 (n=50) | REJECTED | below_safety_margin(11661461449146<46439988969480), p_lower_below_threshold(0.07<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.093167 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0245 €) | — | 1.17 | 0.072 (n=50) | REJECTED | below_safety_margin(10874860639808<18633447966148), p_lower_below_threshold(0.07<0.75) |
| 52671989 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002696 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0241 €) | — | 1.19 | 0.072 (n=50) | REJECTED | below_safety_margin(32<53), p_lower_below_threshold(0.07<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH | 0.103348 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0229 €) | — | 0.98 | 0.072 (n=50) | REJECTED | below_safety_margin(10167054477022<20669634333982), p_lower_below_threshold(0.07<0.75) |
| 52671989 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003031 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0226 €) | — | 0.99 | 0.072 (n=50) | REJECTED | below_safety_margin(30<60), p_lower_below_threshold(0.07<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.093742 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0225 €) | — | 1.06 | 0.072 (n=50) | REJECTED | below_safety_margin(9978043670532<18748316762697), p_lower_below_threshold(0.07<0.75) |
| 52671989 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002537 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0219 €) | — | 1.14 | 0.072 (n=50) | REJECTED | below_safety_margin(29<50), p_lower_below_threshold(0.07<0.75) |
| 52672454 | WETH→[pancakeswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.033454 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0172 €) | 0.000008 WETH | 2.29 | 0.001 (n=11) | REJECTED | stale_data(5594ms>4000.0), reliability_not_demonstrated |
| 52671989 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001773 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0136 €) | — | 1.02 | — (n=0) | REJECTED | below_safety_margin(18<35), reliability_not_demonstrated |
| 52671989 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 143.624751 USDC | 0.022115 USDC | 0.000000 USDC | 0.007407 USDC | 0.014708 USDC (0.0135 €) | — | 1.02 | 0.003 (n=2) | REJECTED | below_safety_margin(14708<28724), reliability_not_demonstrated |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.054541 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0133 €) | — | 1.09 | — (n=0) | REJECTED | below_safety_margin(5928356130639<10908167036115), reliability_not_demonstrated |
| 52671989 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.066985 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 0.88 | 0.003 (n=2) | REJECTED | below_safety_margin(5881536736545<13396950184326), reliability_not_demonstrated |
| 52671989 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001565 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0128 €) | — | 1.09 | 0.003 (n=2) | REJECTED | below_safety_margin(17<31), reliability_not_demonstrated |
| 52671987 | USDC→[uniswap_v3]→MORPHO→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 19.574661 USDC | 0.019767 USDC | 0.000000 USDC | 0.007020 USDC | 0.012747 USDC (0.0117 €) | — | 6.51 | 0.007 (n=44) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52671987 | USDC→[aerodrome]→AUKI→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 12.040832 USDC | 0.016946 USDC | 0.000000 USDC | 0.006682 USDC | 0.010264 USDC (0.0094 €) | — | 8.52 | 0.013 (n=23) | REJECTED | reliability_not_demonstrated |
| 52671328 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.099397 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0090 €) | — | 0.40 | 0.001 (n=10) | REJECTED | below_safety_margin(4017279468264<19879480264111), reliability_not_demonstrated |
| 52671328 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 240.463093 USDC | 0.015303 USDC | 0.000000 USDC | 0.005495 USDC | 0.009808 USDC (0.0090 €) | — | 0.41 | 0.001 (n=10) | REJECTED | below_safety_margin(9808<48092), reliability_not_demonstrated |
| 52671987 | USDC→[uniswap_v3]→MORPHO→[aerodrome]→AERO→[uniswap_v3]→USDC | 17.970499 USDC | 0.016793 USDC | 0.000000 USDC | 0.007020 USDC | 0.009773 USDC (0.0090 €) | — | 5.44 | 0.007 (n=44) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52671987 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.013193 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0080 €) | 0.000004 WETH | 2.69 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |
| 52671987 | USDC→[aerodrome]→AUKI→[aerodrome]→AERO→[uniswap_v3]→USDC | 11.426641 USDC | 0.015180 USDC | 0.000000 USDC | 0.006682 USDC | 0.008498 USDC (0.0078 €) | — | 7.44 | 0.007 (n=44) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52671987 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.012992 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0076 €) | 0.000003 WETH | 2.58 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 454 ; taux observé 0.128 ; borne inférieure crédible (0.9) 0.109 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
