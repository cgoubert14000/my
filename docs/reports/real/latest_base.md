# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T23:54:38+00:00 ; durée 290.46 min ; blocs 52650847 → 52659560 (7740 vus)

## Connexion
- Requêtes RPC : 91609 ; erreurs : 1090 ; latence p50/p95 : 111.1/2,059.7 ms
- Rafraîchissements d'état : 7741 ; âge des données au dernier bloc : 1.9 s ; changements de frais LP observés (pools à frais dynamiques) : 15187
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5 ; cycles déclenchés par événement : 4 ; avance médiane sur le rafraîchissement multicall : 25,539 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,444.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21444 routes
- Par DEX : uniswap_v3 135, aerodrome 235 (quarantaine 1), aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3921 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 3 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2444.445842, 'AERO': 0.898266, 'cbBTC': 82361.329534}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52659649

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,546,314 | 2,444.063100 | 52659560 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 46,350,682 | 1.068956 | 52659560 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,475,076 | 0.029756 | 52659560 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,503,341 | 0.029706 | 52659560 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,670,049 | 98.680440 | 52659560 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,569,687 | 0.029771 | 52659560 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,749,311 | 0.000012 | 52659560 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,135,867 | 2,440.693776 | 52659560 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 594 | 8,865,281 | 2,441.064202 | 52659560 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,018,774 | 0.000012 | 52659560 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,844,879 | 0.000012 | 52659560 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,233,745 | 0.001674 | 52659560 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,665,184 | 1.074383 | 52659560 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,462,977 | 0.024854 | 52659560 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,441,848 | 2,444.773786 | 52659560 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,347,923 | 0.029714 | 52659560 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,788,883 | 0.802398 | 52659560 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,739,513 | 0.000278 | 52659560 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,383,704 | 2,440.909288 | 52659560 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,332,755 | 0.998704 | 52659560 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,032,647 | 34,839.184807 | 52659560 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,591,265 | 2,628.320824 | 52659560 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 412 | 3,265,803 | 2,444.089400 | 52659560 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,849,350 | 0.000012 | 52659560 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,670,284 | 98.701113 | 52659560 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,599,129 | 0.000011 | 52659560 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,594,815 | 1.141777 | 52659560 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,396,589 | 403.304961 | 52659560 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,380,616 | 1,006.630687 | 52659560 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,272,254 | 1,174,457.834162 | 52659560 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52659560 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,102,420 | 0.000000 | 52659560 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,007,548 | 1.404816 | 52659560 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,932,870 | 15.556505 | 52659560 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,822,279 | 0.022696 | 52659560 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,801,081 | 0.019237 | 52659560 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,780,179 | 0.000012 | 52659560 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,686,742 | 2.309483 | 52659560 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,676,388 | 13,581.740393 | 52659560 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,580,610 | 2,609.721023 | 52659560 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,511,243 | 1.105497 | 52659560 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,490,317 | 0.916551 | 52659560 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AERO | 3040 | 1,477,169 | 2,609.969328 | 52659560 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,097 | 0.830051 | 52659560 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,368,236 | 1.121341 | 52659560 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,362,715 | 0.004861 | 52659560 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,353,044 | 0.000000 | 52659560 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,342,367 | 23.257488 | 52659560 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,328,382 | 0.000279 | 52659560 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,947 | 62.295199 | 52659560 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,217,654 | 2,440.380575 | 52659560 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/cbBTC | 3000 | 1,217,281 | 0.029772 | 52659560 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,212,351 | 1.105591 | 52659560 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,209,091 | 35,654,685.234520 | 52659560 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,190,464 | 1,142,990.554894 | 52659560 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,166,029 | 496,809.210529 | 52659560 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,164,307 | 0.436159 | 52659560 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,150,091 | 0.885843 | 52659560 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,134,269 | 13.630076 | 52659560 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,118,254 | 83,161.764950 | 52659560 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 7744 ; routes examinées : 166062336 ; candidats optimisés : 1091170 ; net attendu > 0 : 229 ; dernier cycle 616.6 ms
- Rejets (moteur) : {'spread_below_threshold': 163257792, 'liquidity_below_min': 1565050, 'negative_expected_net': 1090941, 'pool_quarantined': 133318, 'borrow_bound_too_small': 7744, 'cycle_budget_exhausted': 7262}
- Enregistrements de la session : 1091170 ; net attendu > 0 : 229 ; simulés (eth_call de la vraie tx) : 40 (ok 13, échec 27) ; étiquettes ghost N+1 : 0/29 positives
- Décisions : {'REJECTED': 1091170} ; motifs de rejet : {'below_safety_margin': 139, 'negative_expected_net': 1090941, 'p_lower_below_threshold': 103, 'price_impact': 33, 'reliability_not_demonstrated': 126, 'simulation_failed': 27, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52656437 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 588.796609 USDC | 0.240700 USDC | 0.000000 USDC | 0.005181 USDC | 0.235519 USDC (0.2167 €) | — | 4.00 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 52656437 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 177.804685 USDC | 0.226124 USDC | 0.000000 USDC | 0.007049 USDC | 0.219075 USDC (0.2015 €) | — | 12.32 | 0.023 (n=13) | REJECTED | reliability_not_demonstrated |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002169 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1424 €) | — | 8.67 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52656437 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 175.837187 USDC | 0.161358 USDC | 0.000000 USDC | 0.007388 USDC | 0.153970 USDC (0.1417 €) | — | 8.76 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52656437 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[uniswap_v3]→USDC | 107.299341 USDC | 0.096530 USDC | 0.000000 USDC | 0.007049 USDC | 0.089481 USDC (0.0823 €) | — | 8.34 | 0.023 (n=13) | REJECTED | reliability_not_demonstrated |
| 52656437 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 131.953672 USDC | 0.084198 USDC | 0.000000 USDC | 0.007388 USDC | 0.076810 USDC (0.0707 €) | — | 5.82 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001396 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0705 €) | — | 6.66 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001496 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0614 €) | — | 5.41 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52656437 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 123.509899 USDC | 0.073255 USDC | 0.000000 USDC | 0.007388 USDC | 0.065867 USDC (0.0606 €) | — | 5.33 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52656992 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 151.465687 USDC | 0.063874 USDC | 0.000000 USDC | 0.007388 USDC | 0.056486 USDC (0.0520 €) | 0.056486 USDC | 3.73 | 0.139 (n=49) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52656992 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.061861 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0520 €) | 0.000023 WETH | 3.71 | 0.139 (n=49) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52656992 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 155.299910 USDC | 0.062519 USDC | 0.000000 USDC | 0.007388 USDC | 0.055131 USDC (0.0507 €) | — | 3.55 | 0.139 (n=49) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52656992 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.063262 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0507 €) | 0.000022 WETH | 3.55 | 0.139 (n=49) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52656437 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 109.794167 USDC | 0.059507 USDC | 0.000000 USDC | 0.007388 USDC | 0.052119 USDC (0.0479 €) | — | 4.75 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.001180 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0477 €) | — | 5.34 | 0.244 (n=22) | REJECTED | reliability_not_demonstrated |
| 52651372 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 199.591538 USDC | 0.055396 USDC | 0.000000 USDC | 0.007374 USDC | 0.048022 USDC (0.0442 €) | — | 2.41 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52651372 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.081382 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0440 €) | 0.000020 WETH | 2.40 | 0.080 (n=45) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001180 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0424 €) | — | 4.75 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52656437 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.040597 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0421 €) | 0.000019 WETH | 4.59 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001180 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0371 €) | — | 4.15 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52656437 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 96.366688 USDC | 0.047351 USDC | 0.000000 USDC | 0.007388 USDC | 0.039963 USDC (0.0368 €) | — | 4.15 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52656437 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 79.280872 USDC | 0.044708 USDC | 0.000000 USDC | 0.007388 USDC | 0.037320 USDC (0.0343 €) | — | 4.71 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001180 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0341 €) | — | 3.81 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52656437 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.035809 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0336 €) | 0.000015 WETH | 4.15 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52656437 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001180 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0333 €) | — | 3.73 | 0.146 (n=47) | REJECTED | p_lower_below_threshold(0.15<0.75) |

## Fiabilité et décision
- Observations ghost : 413 ; taux observé 0.140 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
