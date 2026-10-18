# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T04:17:32+00:00 ; durée 55.22 min ; blocs 52752192 → 52753851 (1650 vus)

## Connexion
- Requêtes RPC : 20250 ; erreurs : 5 ; latence p50/p95 : 291.0/1,401.0 ms
- Rafraîchissements d'état : 1651 ; âge des données au dernier bloc : 1.04 s ; changements de frais LP observés (pools à frais dynamiques) : 2373
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 603 ; cycles déclenchés par événement : 32 ; avance médiane sur le rafraîchissement multicall : 666 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,420.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21108 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2415.845921, 'AERO': 0.842347, 'cbBTC': 81764.569365}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,402,379 | 2,420.093724 | 52753851 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,795,329 | 1.185306 | 52753851 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,771,282 | 0.029544 | 52753851 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,243,260 | 0.029589 | 52753851 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,925,422 | 106.686328 | 52753851 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,485,101 | 0.029525 | 52753851 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,779,691 | 0.000012 | 52753851 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,073,643 | 2,420.498066 | 52753851 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 8,587,944 | 0.000012 | 52753851 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,863,024 | 0.000012 | 52753851 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,290,173 | 2,419.719450 | 52753851 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,176,576 | 0.001662 | 52753851 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,497,988 | 2,420.727889 | 52753851 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,354,961 | 0.029578 | 52753851 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,255,405 | 1.000855 | 52753851 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,165,863 | 0.025619 | 52753851 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 400 | 5,071,953 | 2,423.661155 | 52753851 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,837,440 | 0.802399 | 52753851 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,649,656 | 0.000273 | 52753851 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,448,055 | 0.998808 | 52753851 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,430,653 | 2,419.599938 | 52753851 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,138,863 | 32,428.411014 | 52753851 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,980,268 | 1.184583 | 52753851 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,362,852 | 2,850.930627 | 52753851 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,921,321 | 1.141804 | 52753851 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,844,869 | 0.000012 | 52753851 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,705,951 | 0.000010 | 52753851 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,575,778 | 106.716738 | 52753851 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,295,920 | 407.220325 | 52753851 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,239,522 | 1,185,443.228187 | 52753851 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52753851 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,032,576 | 1.377366 | 52753851 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,022,014 | 1,004.744142 | 52753851 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,797 | 1.123381 | 52753851 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,907,906 | 15.807009 | 52753851 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,876,130 | 0.000000 | 52753851 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,812,532 | 0.021595 | 52753851 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,781,214 | 0.000012 | 52753851 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,725,814 | 0.017913 | 52753851 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,676,128 | 2.307142 | 52753851 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,608,389 | 13,761.355320 | 52753851 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,574,147 | 0.916398 | 52753851 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,524,100 | 1.105497 | 52753851 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,522,689 | 2,872.052118 | 52753851 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,465,925 | 2,870.600588 | 52753851 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,614 | 0.825990 | 52753851 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,337,108 | 0.000000 | 52753851 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,890 | 0.435965 | 52753851 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,313,909 | 0.004708 | 52753851 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,303,153 | 0.000271 | 52753851 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,259,795 | 0.029519 | 52753851 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,505 | 62.339340 | 52753851 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,248,320 | 23.290285 | 52753851 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,199,021 | 35,680,417.296081 | 52753851 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,196,394 | 1.105816 | 52753851 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,190,966 | 2,420.477611 | 52753851 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,172,866 | 1.131646 | 52753851 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,169,613 | 0.885761 | 52753851 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,167,144 | 1,165,942.906985 | 52753851 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,143,966 | 514,765.248826 | 52753851 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |

## Recherche d'opportunités
- Cycles : 1682 ; routes examinées : 35503656 ; candidats optimisés : 276788 ; net attendu > 0 : 54 ; dernier cycle 361.9 ms
- Rejets (moteur) : {'spread_below_threshold': 34888038, 'liquidity_below_min': 335908, 'negative_expected_net': 276734, 'borrow_bound_too_small': 1678, 'cycle_budget_exhausted': 1106}
- Enregistrements de la session : 276788 ; net attendu > 0 : 54 ; simulés (eth_call de la vraie tx) : 8 (ok 8, échec 0) ; étiquettes ghost N+1 : 3/7 positives
- Décisions : {'REJECTED': 276788} ; motifs de rejet : {'below_safety_margin': 44, 'negative_expected_net': 276734, 'p_lower_below_threshold': 48, 'reliability_not_demonstrated': 6, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52752740 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 52.254860 USDC | 0.018706 USDC | 0.000000 USDC | 0.005424 USDC | 0.013282 USDC (0.0122 €) | 0.013282 USDC | 2.54 | 0.033 (n=25) | REJECTED | reliability_not_demonstrated |
| 52752740 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.021792 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0122 €) | 0.000005 WETH | 2.52 | 0.033 (n=25) | REJECTED | reliability_not_demonstrated |
| 52752740 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 46.729221 USDC | 0.015632 USDC | 0.000000 USDC | 0.005424 USDC | 0.010208 USDC (0.0094 €) | — | 2.18 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 52752740 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.019495 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0094 €) | 0.000004 WETH | 2.16 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 52752740 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000468 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.85 | 0.132 (n=96) | REJECTED | below_safety_margin(4<9), p_lower_below_threshold(0.13<0.75) |
| 52752740 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000393 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 1.02 | 0.132 (n=96) | REJECTED | below_safety_margin(4<7), p_lower_below_threshold(0.13<0.75) |
| 52752740 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 38.734659 USDC | 0.010182 USDC | 0.000000 USDC | 0.007259 USDC | 0.002923 USDC (0.0027 €) | — | 0.75 | 0.132 (n=96) | REJECTED | below_safety_margin(2923<7746), p_lower_below_threshold(0.13<0.75) |
| 52752740 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.013481 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0027 €) | — | 0.89 | 0.132 (n=96) | REJECTED | below_safety_margin(1200238950774<2696295221375), p_lower_below_threshold(0.13<0.75) |
| 52752740 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.015972 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0027 €) | — | 0.75 | 0.132 (n=96) | REJECTED | below_safety_margin(1197881282799<3194487296294), p_lower_below_threshold(0.13<0.75) |
| 52752740 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 32.252295 USDC | 0.010129 USDC | 0.000000 USDC | 0.007259 USDC | 0.002870 USDC (0.0026 €) | — | 0.89 | 0.132 (n=96) | REJECTED | below_safety_margin(2870<6450), p_lower_below_threshold(0.13<0.75) |
| 52752888 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.550990 USDC | 0.009828 USDC | 0.000000 USDC | 0.007260 USDC | 0.002568 USDC (0.0024 €) | 0.002568 USDC | 2.43 | 0.319 (n=55) | REJECTED | p_lower_below_threshold(0.32<0.75) |
| 52752888 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004365 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | 0.000001 WETH | 2.41 | 0.319 (n=55) | REJECTED | p_lower_below_threshold(0.32<0.75) |
| 52752892 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.458829 USDC | 0.009620 USDC | 0.000000 USDC | 0.007260 USDC | 0.002360 USDC (0.0022 €) | 0.002360 USDC | 2.26 | 0.140 (n=97) | REJECTED | stale_data(4144ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 52752892 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004311 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | 0.000001 WETH | 2.24 | 0.140 (n=97) | REJECTED | stale_data(4141ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 52752888 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.417544 USDC | 0.009494 USDC | 0.000000 USDC | 0.007260 USDC | 0.002234 USDC (0.0021 €) | — | 2.14 | 0.132 (n=96) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52752888 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004330 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0020 €) | 0.000001 WETH | 2.11 | 0.132 (n=96) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52752889 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.123175 USDC | 0.009114 USDC | 0.000000 USDC | 0.007260 USDC | 0.001854 USDC (0.0017 €) | — | 1.83 | 0.340 (n=57) | REJECTED | below_safety_margin(1854<2024), p_lower_below_threshold(0.34<0.75) |
| 52752889 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004238 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 1.79 | 0.340 (n=57) | REJECTED | below_safety_margin(757234989642<847557973311), p_lower_below_threshold(0.34<0.75) |
| 52752890 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.127534 USDC | 0.009062 USDC | 0.000000 USDC | 0.007260 USDC | 0.001802 USDC (0.0017 €) | — | 1.78 | 0.140 (n=97) | REJECTED | below_safety_margin(1802<2025), p_lower_below_threshold(0.14<0.75) |
| 52752891 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.127534 USDC | 0.009062 USDC | 0.000000 USDC | 0.007260 USDC | 0.001802 USDC (0.0017 €) | — | 1.78 | 0.140 (n=97) | REJECTED | below_safety_margin(1802<2025), p_lower_below_threshold(0.14<0.75) |
| 52752890 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.130226 USDC | 0.009054 USDC | 0.000000 USDC | 0.007260 USDC | 0.001794 USDC (0.0017 €) | — | 1.77 | 0.340 (n=57) | REJECTED | below_safety_margin(1794<2026), p_lower_below_threshold(0.34<0.75) |
| 52752890 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004205 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.75 | 0.140 (n=97) | REJECTED | below_safety_margin(735737789849<841093496380), p_lower_below_threshold(0.14<0.75) |
| 52752891 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004205 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.75 | 0.140 (n=97) | REJECTED | below_safety_margin(735737789849<841093496380), p_lower_below_threshold(0.14<0.75) |
| 52752890 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004195 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 1.75 | 0.340 (n=57) | REJECTED | below_safety_margin(732322798642<838971023634), p_lower_below_threshold(0.34<0.75) |
| 52752891 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.134585 USDC | 0.009026 USDC | 0.000000 USDC | 0.007260 USDC | 0.001766 USDC (0.0016 €) | — | 1.74 | 0.340 (n=57) | REJECTED | below_safety_margin(1766<2026), p_lower_below_threshold(0.34<0.75) |

## Fiabilité et décision
- Observations ghost : 853 ; taux observé 0.132 ; borne inférieure crédible (0.9) 0.118 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
