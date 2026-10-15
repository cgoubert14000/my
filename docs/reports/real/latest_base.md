# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T12:55:43+00:00 ; durée 303.64 min ; blocs 52630686 → 52639792 (8460 vus)

## Connexion
- Requêtes RPC : 97691 ; erreurs : 560 ; latence p50/p95 : 171.3/1,974.7 ms
- Rafraîchissements d'état : 8460 ; âge des données au dernier bloc : 2.3 s ; changements de frais LP observés (pools à frais dynamiques) : 21946
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,355.85 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 567 pools, 324 jetons, 20918 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 152, pancakeswap_v3 29, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 204 (rejetés 2) → 609 jetons ; pools candidats 3862 (énumérés 388, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 2 → gardés 567 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2370.057693, 'AERO': 0.841029, 'cbBTC': 81234.761422}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 142,944,160 | 2,355.850779 | 52639792 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,905,056 | 1.193665 | 52639792 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,680,828 | 0.029148 | 52639792 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,559,802 | 105.226399 | 52639792 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,874,996 | 0.029107 | 52639792 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,299,090 | 0.029106 | 52639792 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,589,220 | 0.000012 | 52639792 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,890,758 | 2,350.098305 | 52639792 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,817,915 | 2,356.143442 | 52639792 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 7,928,542 | 0.000012 | 52639792 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,048,910 | 0.001647 | 52639792 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 773 | 6,984,246 | 2,349.617461 | 52639792 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 6,620,203 | 0.000012 | 52639792 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,203,930 | 0.029142 | 52639792 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,126,837 | 0.026584 | 52639792 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,533,161 | 0.000274 | 52639792 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,430,492 | 0.802389 | 52639792 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,251,831 | 0.999940 | 52639792 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,243,736 | 1.192763 | 52639792 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,239,978 | 2,349.640453 | 52639792 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,874,968 | 35,057.663733 | 52639792 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,395,751 | 2,809.922040 | 52639792 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,814,001 | 0.000012 | 52639792 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,545,121 | 0.000010 | 52639792 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,527,028 | 105.179936 | 52639792 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,461,093 | 1.141650 | 52639792 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,452,298 | 406.953987 | 52639792 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,191,657 | 1,172,943.008374 | 52639792 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,160,991 | 1,030.366767 | 52639792 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/USDT | 442 | 2,126,182 | 2,354.122885 | 52639792 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,476 | 1.194801 | 52639792 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52639792 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,949,528 | 0.000000 | 52639792 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,891,898 | 15.871873 | 52639792 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,872,025 | 0.022346 | 52639792 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,780,620 | 0.916541 | 52639792 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,767,886 | 0.018800 | 52639792 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,756,023 | 0.000012 | 52639792 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,669,690 | 2.301457 | 52639792 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,658,452 | 13,953.023234 | 52639792 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,466,134 | 2,810.726709 | 52639792 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,038 | 0.831422 | 52639792 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | weETH_04c0/WETH | 500 | 1,456,599 | 1.105502 | 52639792 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,350,581 | 1.130488 | 52639792 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | DRB/WETH | 10000 | 1,330,287 | 0.000000 | 52639792 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,311,875 | 2,811.841204 | 52639792 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,278,035 | 0.004707 | 52639792 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,273,948 | 23.198283 | 52639792 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,270,438 | 0.000273 | 52639792 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,246,771 | 1.120623 | 52639792 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,245,648 | 62.625657 | 52639792 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,193,173 | 2,349.954677 | 52639792 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,175,378 | 1.105590 | 52639792 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,165,942 | 35,588,809.396719 | 52639792 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,136,270 | 0.029118 | 52639792 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,129,133 | 1,180,456.347820 | 52639792 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,116,305 | 506,112.041909 | 52639792 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,114,420 | 77,762.612314 | 52639792 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,110,282 | 51.124111 | 52639792 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,110,128 | 0.434918 | 52639792 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 8460 ; routes examinées : 176966280 ; candidats optimisés : 1113838 ; net attendu > 0 : 563 ; dernier cycle 501.2 ms
- Rejets (moteur) : {'spread_below_threshold': 174394283, 'liquidity_below_min': 1430295, 'negative_expected_net': 1113275, 'unquotable': 17829, 'borrow_bound_too_small': 8460, 'cycle_budget_exhausted': 1575}
- Enregistrements de la session : 1113838 ; net attendu > 0 : 563 ; simulés (eth_call de la vraie tx) : 23 (ok 23, échec 0) ; étiquettes ghost N+1 : 3/19 positives
- Décisions : {'REJECTED': 1113838} ; motifs de rejet : {'below_safety_margin': 434, 'negative_expected_net': 1113275, 'p_lower_below_threshold': 216, 'reliability_not_demonstrated': 347, 'stale_data': 36}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52639030 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 2,671.139863 USDC | 0.433758 USDC | 0.000000 USDC | 0.006824 USDC | 0.426934 USDC (0.3928 €) | — | 1.60 | 0.102 (n=3) | REJECTED | below_safety_margin(426934<534227), reliability_not_demonstrated |
| 52639085 | WETH→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.233231 WETH | 0.000082 WETH | 0.000000 WETH | 0.000004 WETH | 0.000078 WETH (0.1685 €) | 0.000078 WETH | 3.34 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639085 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC | 0.006410 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1682 €) | — | 3.53 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639085 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072383 WETH | 0.000046 WETH | 0.000000 WETH | 0.000004 WETH | 0.000042 WETH (0.0910 €) | 0.000042 WETH | 5.82 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639085 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 169.489971 USDC | 0.108070 USDC | 0.000000 USDC | 0.009449 USDC | 0.098621 USDC (0.0907 €) | — | 5.82 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639085 | WETH→[aerodrome_slipstream]→TIBBIR→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.060291 WETH | 0.000044 WETH | 0.000000 WETH | 0.000004 WETH | 0.000040 WETH (0.0863 €) | 0.000040 WETH | 6.62 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639051 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.405203 WETH | 0.000044 WETH | 0.000000 WETH | 0.000004 WETH | 0.000040 WETH (0.0862 €) | — | 0.98 | 0.110 (n=33) | REJECTED | below_safety_margin(39698393228394<81040588723930), p_lower_below_threshold(0.11<0.75) |
| 52639085 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIBBIR→[aerodrome_slipstream]→USDC | 140.757923 USDC | 0.102953 USDC | 0.000000 USDC | 0.009449 USDC | 0.093504 USDC (0.0860 €) | — | 6.64 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639051 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 952.500654 USDC | 0.103090 USDC | 0.000000 USDC | 0.009624 USDC | 0.093466 USDC (0.0860 €) | — | 0.98 | 0.110 (n=33) | REJECTED | below_safety_margin(93466<190500), p_lower_below_threshold(0.11<0.75) |
| 52639085 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.053921 WETH | 0.000040 WETH | 0.000000 WETH | 0.000004 WETH | 0.000036 WETH (0.0778 €) | — | 6.68 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639085 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 125.607602 USDC | 0.093741 USDC | 0.000000 USDC | 0.009449 USDC | 0.084292 USDC (0.0775 €) | — | 6.71 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52639085 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.061901 WETH | 0.000038 WETH | 0.000000 WETH | 0.000004 WETH | 0.000034 WETH (0.0728 €) | — | 5.44 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 145.284601 USDC | 0.088340 USDC | 0.000000 USDC | 0.009449 USDC | 0.078891 USDC (0.0726 €) | — | 5.43 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | WETH→[aerodrome_slipstream]→TIBBIR→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.053370 WETH | 0.000037 WETH | 0.000000 WETH | 0.000004 WETH | 0.000033 WETH (0.0722 €) | — | 6.26 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIBBIR→[aerodrome_slipstream]→USDC | 124.777605 USDC | 0.087733 USDC | 0.000000 USDC | 0.009449 USDC | 0.078284 USDC (0.0720 €) | — | 6.27 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639030 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.061774 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0702 €) | 0.000032 WETH | 5.24 | 0.372 (n=15) | REJECTED | reliability_not_demonstrated |
| 52639030 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 145.354105 USDC | 0.084171 USDC | 0.000000 USDC | 0.007977 USDC | 0.076194 USDC (0.0701 €) | — | 5.24 | 0.372 (n=15) | REJECTED | reliability_not_demonstrated |
| 52639085 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.048140 WETH | 0.000034 WETH | 0.000000 WETH | 0.000004 WETH | 0.000030 WETH (0.0658 €) | — | 6.33 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 112.656508 USDC | 0.080794 USDC | 0.000000 USDC | 0.009449 USDC | 0.071345 USDC (0.0656 €) | — | 6.33 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52635174 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.011261 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0642 €) | 0.000029 WETH | 26.14 | 0.315 (n=3) | REJECTED | reliability_not_demonstrated |
| 52639085 | WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.061220 WETH | 0.000032 WETH | 0.000000 WETH | 0.000004 WETH | 0.000028 WETH (0.0613 €) | — | 4.64 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | WETH→[aerodrome_slipstream]→TIBBIR→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.051969 WETH | 0.000032 WETH | 0.000000 WETH | 0.000004 WETH | 0.000028 WETH (0.0613 €) | — | 5.45 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[uniswap_v3]→USDC | 143.047236 USDC | 0.075918 USDC | 0.000000 USDC | 0.009449 USDC | 0.066469 USDC (0.0612 €) | — | 4.65 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIBBIR→[aerodrome_slipstream]→USDC | 121.437613 USDC | 0.075823 USDC | 0.000000 USDC | 0.009449 USDC | 0.066374 USDC (0.0611 €) | — | 5.47 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52639085 | WETH→[aerodrome_slipstream]→TIBBIR→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.050436 WETH | 0.000031 WETH | 0.000000 WETH | 0.000004 WETH | 0.000027 WETH (0.0592 €) | — | 5.43 | 0.198 (n=35) | REJECTED | p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 277 ; taux observé 0.188 ; borne inférieure crédible (0.9) 0.159 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
