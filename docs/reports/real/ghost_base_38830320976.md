# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T05:12:19+00:00 ; durée 271.11 min ; blocs 52660958 → 52669084 (6941 vus)

## Connexion
- Requêtes RPC : 81680 ; erreurs : 65 ; latence p50/p95 : 789.1/5,240.4 ms
- Rafraîchissements d'état : 6941 ; âge des données au dernier bloc : 15.42 s ; changements de frais LP observés (pools à frais dynamiques) : 19263
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,448.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21346 routes
- Par DEX : uniswap_v3 134, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 392, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2444.060646, 'AERO': 0.934005, 'cbBTC': 82314.094538}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,886,320 | 2,448.072860 | 52669085 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,448,144 | 1.088734 | 52669085 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,515,627 | 0.029790 | 52669085 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,577,523 | 99.854381 | 52669085 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 16,227,932 | 0.029754 | 52669085 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,595,069 | 0.029739 | 52669085 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,748,349 | 0.000012 | 52669085 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,137,948 | 2,447.755135 | 52669085 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 8,090,673 | 0.000012 | 52669085 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 8,010,830 | 0.000012 | 52669085 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 728 | 7,376,312 | 2,447.289197 | 52669085 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,248,716 | 0.001685 | 52669085 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,558,815 | 1.091478 | 52669085 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,467,972 | 0.024689 | 52669085 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,446,310 | 2,448.423080 | 52669085 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,410,635 | 0.029779 | 52669085 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,231,108 | 1.000855 | 52669085 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,893,338 | 0.802398 | 52669085 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,762,111 | 0.000280 | 52669085 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,408,526 | 2,446.991729 | 52669085 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,363,414 | 0.998880 | 52669085 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,066,854 | 34,368.060625 | 52669085 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,561,487 | 2,649.616928 | 52669085 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,046,848 | 1.141827 | 52669085 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/USDT | 430 | 2,890,081 | 2,451.527198 | 52669085 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,874,525 | 0.000011 | 52669085 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,847,333 | 0.000012 | 52669085 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,707,750 | 401.093912 | 52669085 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,677,317 | 99.875278 | 52669085 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,296,570 | 1,153,495.001439 | 52669085 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2766 | 2,144,639 | 1,007.727583 | 52669085 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52669085 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,106,005 | 0.000000 | 52669085 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52669085 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,958,759 | 15.370518 | 52669085 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,835,518 | 0.023017 | 52669085 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,806,318 | 0.019313 | 52669085 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,127 | 0.000012 | 52669085 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,704,516 | 13,469.548084 | 52669085 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,689,616 | 2.309767 | 52669085 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,574,523 | 2,668.228157 | 52669085 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,521,691 | 0.916551 | 52669085 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,513,659 | 1.105492 | 52669085 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,492,404 | 2,667.897527 | 52669085 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,154 | 0.830051 | 52669085 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,375,170 | 0.000000 | 52669085 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,358,533 | 0.004833 | 52669085 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,334,761 | 0.000282 | 52669085 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,331,326 | 23.218494 | 52669085 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,262,081 | 1.122665 | 52669085 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,987 | 62.291240 | 52669085 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/cbBTC | 3000 | 1,217,539 | 0.029729 | 52669085 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,216,294 | 35,221,664.334566 | 52669085 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,214,341 | 1.105591 | 52669085 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,212,896 | 2,448.116397 | 52669085 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,192,013 | 1,143,765.266237 | 52669085 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,184,216 | 0.886065 | 52669085 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,173,970 | 496,934.809148 | 52669085 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,164,739 | 0.436346 | 52669085 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,138,760 | 13.498315 | 52669085 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 6940 ; routes examinées : 148141240 ; candidats optimisés : 1005119 ; net attendu > 0 : 495 ; dernier cycle 359.0 ms
- Rejets (moteur) : {'spread_below_threshold': 145799943, 'liquidity_below_min': 1277176, 'negative_expected_net': 1004624, 'pool_quarantined': 31860, 'cycle_budget_exhausted': 20170, 'borrow_bound_too_small': 6940, 'unquotable': 32}
- Enregistrements de la session : 1005119 ; net attendu > 0 : 495 ; simulés (eth_call de la vraie tx) : 23 (ok 18, échec 5) ; étiquettes ghost N+1 : 0/23 positives
- Décisions : {'REJECTED': 1005119} ; motifs de rejet : {'below_safety_margin': 428, 'negative_expected_net': 1004624, 'p_lower_below_threshold': 418, 'price_impact': 16, 'reliability_not_demonstrated': 77, 'simulation_failed': 5, 'stale_data': 44}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52665023 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,638.282668 USDC | 0.073302 USDC | 0.000000 USDC | 0.007696 USDC | 0.065606 USDC (0.0604 €) | — | 0.40 | 0.077 (n=47) | REJECTED | below_safety_margin(65606<327656), p_lower_below_threshold(0.08<0.75) |
| 52665023 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.672284 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0603 €) | — | 0.40 | 0.077 (n=47) | REJECTED | below_safety_margin(26903375244089<134456861487392), p_lower_below_threshold(0.08<0.75) |
| 52662051 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010627 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0515 €) | 0.000023 WETH | 21.55 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 25.934333 USDC | 0.063303 USDC | 0.000000 USDC | 0.007345 USDC | 0.055958 USDC (0.0515 €) | — | 21.58 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 25.934333 USDC | 0.059170 USDC | 0.000000 USDC | 0.007345 USDC | 0.051825 USDC (0.0477 €) | — | 19.98 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010624 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0477 €) | 0.000021 WETH | 19.97 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.010605 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0472 €) | 0.000021 WETH | 19.82 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 25.934333 USDC | 0.058702 USDC | 0.000000 USDC | 0.007345 USDC | 0.051357 USDC (0.0472 €) | — | 19.80 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52665023 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 1,532.129430 USDC | 0.053180 USDC | 0.000000 USDC | 0.007326 USDC | 0.045854 USDC (0.0422 €) | — | 0.30 | 0.273 (n=32) | REJECTED | below_safety_margin(45854<306425), p_lower_below_threshold(0.27<0.75) |
| 52665023 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.629326 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0421 €) | — | 0.30 | 0.273 (n=32) | REJECTED | below_safety_margin(18802925772083<125865296993047), p_lower_below_threshold(0.27<0.75) |
| 52662051 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009873 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0398 €) | — | 17.95 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 23.994295 USDC | 0.050627 USDC | 0.000000 USDC | 0.007345 USDC | 0.043282 USDC (0.0398 €) | — | 18.04 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009804 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0392 €) | — | 17.80 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 23.848658 USDC | 0.049957 USDC | 0.000000 USDC | 0.007345 USDC | 0.042612 USDC (0.0392 €) | — | 17.87 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009411 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0357 €) | — | 16.90 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 22.901658 USDC | 0.046164 USDC | 0.000000 USDC | 0.007345 USDC | 0.038819 USDC (0.0357 €) | — | 16.95 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.009123 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0341 €) | — | 16.63 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 22.150661 USDC | 0.044370 USDC | 0.000000 USDC | 0.007345 USDC | 0.037025 USDC (0.0341 €) | — | 16.72 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52666133 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 66.342774 USDC | 0.038393 USDC | 0.000000 USDC | 0.006989 USDC | 0.031404 USDC (0.0289 €) | 0.031404 USDC | 4.73 | 0.007 (n=43) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52665023 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 663.811797 USDC | 0.029543 USDC | 0.000000 USDC | 0.007326 USDC | 0.022217 USDC (0.0204 €) | — | 0.33 | 0.077 (n=47) | REJECTED | below_safety_margin(22217<132762), p_lower_below_threshold(0.08<0.75) |
| 52665023 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.272770 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0204 €) | — | 0.33 | 0.077 (n=47) | REJECTED | below_safety_margin(9108759209522<54554081210366), p_lower_below_threshold(0.08<0.75) |
| 52662051 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.007075 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0184 €) | — | 11.58 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52662051 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 17.138973 USDC | 0.026553 USDC | 0.000000 USDC | 0.006586 USDC | 0.019967 USDC (0.0184 €) | — | 11.65 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52666133 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.000740 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0181 €) | — | 3.24 | 0.126 (n=54) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52666133 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 64.646009 USDC | 0.026793 USDC | 0.000000 USDC | 0.007325 USDC | 0.019468 USDC (0.0179 €) | 0.019468 USDC | 3.01 | 0.126 (n=54) | REJECTED | p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 442 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.112 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
