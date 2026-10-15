# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T21:35:17+00:00 ; durée 151.1 min ; blocs 52650847 → 52655380 (3929 vus)

## Connexion
- Requêtes RPC : 47226 ; erreurs : 1060 ; latence p50/p95 : 120.0/1,981.6 ms
- Rafraîchissements d'état : 3929 ; âge des données au dernier bloc : 6.13 s ; changements de frais LP observés (pools à frais dynamiques) : 8006
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5 ; cycles déclenchés par événement : 4 ; avance médiane sur le rafraîchissement multicall : 25,539 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,453.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21444 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3921 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 3 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2444.445842, 'AERO': 0.898266, 'cbBTC': 82361.329534}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,925,382 | 2,453.249821 | 52655381 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,646,133 | 1.102164 | 52655381 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,481,052 | 0.029888 | 52655381 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,787,667 | 98.035324 | 52655381 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,807,207 | 0.029833 | 52655381 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,593,297 | 0.029819 | 52655381 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,746,964 | 0.000012 | 52655381 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,156,013 | 2,457.863223 | 52655381 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,570,633 | 0.000012 | 52655381 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 535 | 8,422,460 | 2,457.084691 | 52655381 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,988,594 | 0.000012 | 52655381 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,234,668 | 0.001682 | 52655381 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,094,237 | 1.106340 | 52655381 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,452,072 | 2,454.790595 | 52655381 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,370,883 | 0.029900 | 52655381 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,365,936 | 0.024884 | 52655381 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,806,883 | 0.802398 | 52655381 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,758,392 | 0.000278 | 52655381 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,369,007 | 2,456.932540 | 52655381 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,330,634 | 0.997998 | 52655381 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,984,815 | 35,949.321691 | 52655381 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,543,343 | 2,717.540075 | 52655381 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,038,860 | 2,461.190653 | 52655381 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,845,199 | 0.000012 | 52655381 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,687,002 | 98.064377 | 52655381 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,624,247 | 404.249519 | 52655381 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,571,375 | 0.000011 | 52655381 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,555,503 | 1.141761 | 52655381 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,372,282 | 1,005.762764 | 52655381 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,279,038 | 1,176,270.195541 | 52655381 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52655381 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,081,810 | 0.000000 | 52655381 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52655381 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,892,177 | 15.607849 | 52655381 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,817,571 | 0.022581 | 52655381 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,794,363 | 0.019096 | 52655381 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,497 | 0.000012 | 52655381 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,750,423 | 13,539.785341 | 52655381 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,692,438 | 2.310794 | 52655381 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,570,088 | 2,708.918139 | 52655381 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,516,822 | 1.105497 | 52655381 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,495,919 | 0.916551 | 52655381 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,445 | 0.830186 | 52655381 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3016 | 1,452,399 | 2,709.150167 | 52655381 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,392,560 | 0.000000 | 52655381 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,373,243 | 0.004830 | 52655381 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,342,858 | 23.254102 | 52655381 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,333,659 | 0.000278 | 52655381 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,326,912 | 1.121780 | 52655381 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,937 | 62.296194 | 52655381 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,232,492 | 2,457.832347 | 52655381 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/cbBTC | 3000 | 1,218,129 | 0.029822 | 52655381 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,217,444 | 35,328,805.562558 | 52655381 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,216,908 | 1.105591 | 52655381 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,194,777 | 1,143,300.017384 | 52655381 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,168,991 | 498,440.584433 | 52655381 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,164,748 | 0.436451 | 52655381 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,161,208 | 0.885929 | 52655381 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,132,580 | 13.679008 | 52655381 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,117,447 | 1.132188 | 52655381 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 3932 ; routes examinées : 84317808 ; candidats optimisés : 507548 ; net attendu > 0 : 116 ; dernier cycle 572.5 ms
- Rejets (moteur) : {'spread_below_threshold': 82939941, 'liquidity_below_min': 860317, 'negative_expected_net': 507432, 'cycle_budget_exhausted': 6070, 'borrow_bound_too_small': 3932}
- Enregistrements de la session : 507548 ; net attendu > 0 : 116 ; simulés (eth_call de la vraie tx) : 7 (ok 7, échec 0) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 507548} ; motifs de rejet : {'below_safety_margin': 83, 'negative_expected_net': 507432, 'p_lower_below_threshold': 51, 'reliability_not_demonstrated': 65, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52651372 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 199.591538 USDC | 0.055396 USDC | 0.000000 USDC | 0.007374 USDC | 0.048022 USDC (0.0442 €) | — | 2.41 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.081382 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0440 €) | 0.000020 WETH | 2.40 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001652 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0288 €) | — | 2.30 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 143.482480 USDC | 0.038444 USDC | 0.000000 USDC | 0.007374 USDC | 0.031070 USDC (0.0286 €) | — | 2.17 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.058126 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0280 €) | 0.000012 WETH | 2.14 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 45.757782 USDC | 0.022825 USDC | 0.000000 USDC | 0.007036 USDC | 0.015789 USDC (0.0145 €) | — | 3.45 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.018813 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0145 €) | 0.000006 WETH | 3.41 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651372 | USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 40.516789 USDC | 0.021229 USDC | 0.000000 USDC | 0.007374 USDC | 0.013855 USDC (0.0127 €) | — | 3.42 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH | 0.016648 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0127 €) | — | 3.38 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 32.066029 USDC | 0.017671 USDC | 0.000000 USDC | 0.007036 USDC | 0.010635 USDC (0.0098 €) | — | 3.32 | 0.008 (n=38) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52651372 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.013070 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0097 €) | — | 3.31 | 0.008 (n=38) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 30.055472 USDC | 0.017279 USDC | 0.000000 USDC | 0.007374 USDC | 0.009905 USDC (0.0091 €) | — | 3.30 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52651372 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH | 0.012291 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | — | 3.27 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52651372 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 37.938496 USDC | 0.015405 USDC | 0.000000 USDC | 0.007036 USDC | 0.008369 USDC (0.0077 €) | — | 2.21 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.015548 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0077 €) | — | 2.18 | 0.151 (n=10) | REJECTED | reliability_not_demonstrated |
| 52651372 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 49.975566 USDC | 0.015592 USDC | 0.000000 USDC | 0.007374 USDC | 0.008218 USDC (0.0076 €) | — | 1.64 | 0.080 (n=45) | REJECTED | below_safety_margin(8218<9995), p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.020337 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0075 €) | — | 1.64 | 0.080 (n=45) | REJECTED | below_safety_margin(3333735924263<4067342478717), p_lower_below_threshold(0.08<0.75) |
| 52651373 | USDC→[aerodrome]→OVER→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 19.664202 USDC | 0.014349 USDC | 0.000000 USDC | 0.006723 USDC | 0.007626 USDC (0.0070 €) | — | 3.88 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651373 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→OVER→[aerodrome]→WETH | 0.008074 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0070 €) | 0.000003 WETH | 3.83 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52651372 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000522 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 1.72 | 0.080 (n=45) | REJECTED | below_safety_margin(9<10), p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 33.993600 USDC | 0.014616 USDC | 0.000000 USDC | 0.007374 USDC | 0.007242 USDC (0.0067 €) | — | 2.13 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USD→[aerodrome_slipstream]→WETH | 0.013880 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0066 €) | — | 2.12 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 43.445532 USDC | 0.014290 USDC | 0.000000 USDC | 0.007374 USDC | 0.006916 USDC (0.0064 €) | — | 1.59 | 0.282 (n=31) | REJECTED | below_safety_margin(6916<8689), p_lower_below_threshold(0.28<0.75) |
| 52651372 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.017763 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0063 €) | — | 1.58 | 0.282 (n=31) | REJECTED | below_safety_margin(2806582179664<3552507083952), p_lower_below_threshold(0.28<0.75) |
| 52651373 | USDC→[aerodrome]→OVER→[aerodrome]→WETH→[uniswap_v3]→USDC | 18.715192 USDC | 0.013098 USDC | 0.000000 USDC | 0.006723 USDC | 0.006375 USDC (0.0059 €) | — | 3.41 | 0.008 (n=38) | REJECTED | p_lower_below_threshold(0.01<0.75) |

## Fiabilité et décision
- Observations ghost : 391 ; taux observé 0.148 ; borne inférieure crédible (0.9) 0.127 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
