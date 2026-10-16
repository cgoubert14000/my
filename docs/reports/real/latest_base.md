# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T10:30:07+00:00 ; durée 252.72 min ; blocs 52671044 → 52678624 (7057 vus)

## Connexion
- Requêtes RPC : 91635 ; erreurs : 353 ; latence p50/p95 : 171.2/1,204.2 ms
- Rafraîchissements d'état : 7057 ; âge des données au dernier bloc : 2.67 s ; changements de frais LP observés (pools à frais dynamiques) : 16571
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 71100 ; cycles déclenchés par événement : 3857 ; avance médiane sur le rafraîchissement multicall : 573 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,449.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 327 jetons, 21788 routes
- Par DEX : uniswap_v3 137, aerodrome 236 (quarantaine 2), aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 392, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 3 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2445.329592, 'AERO': 0.931569, 'cbBTC': 81962.021553}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52678642; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52678641

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,329,923 | 2,449.539110 | 52678625 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,037,450 | 1.088728 | 52678625 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,508,836 | 0.029893 | 52678625 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,528,783 | 100.567397 | 52678625 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,578,725 | 0.029834 | 52678625 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,589,238 | 0.029819 | 52678625 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,743,997 | 0.000012 | 52678625 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,142,349 | 2,449.980607 | 52678625 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,530,949 | 2,449.576748 | 52678625 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,091,852 | 0.000012 | 52678625 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 7,341,386 | 0.000012 | 52678625 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,233,180 | 0.001687 | 52678625 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,800,498 | 1.081700 | 52678625 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,506,105 | 0.024684 | 52678625 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,448,633 | 2,449.838965 | 52678625 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,413,053 | 0.029897 | 52678625 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,234,241 | 1.000855 | 52678625 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,896,129 | 0.802398 | 52678625 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,766,315 | 0.000281 | 52678625 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,353,121 | 0.998888 | 52678625 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,331,889 | 2,449.447538 | 52678625 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,066,001 | 34,423.680305 | 52678625 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 412 | 3,802,994 | 2,452.556302 | 52678625 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,563,488 | 2,648.496269 | 52678625 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,046,792 | 1.141824 | 52678625 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,843,179 | 0.000012 | 52678625 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,716,919 | 400.553381 | 52678625 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,684,471 | 0.000011 | 52678625 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,671,146 | 100.616496 | 52678625 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,356,700 | 992.203822 | 52678625 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,297,348 | 1,154,095.794367 | 52678625 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52678625 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,110,002 | 0.000000 | 52678625 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52678625 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,964,649 | 15.259642 | 52678625 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,867,630 | 0.023309 | 52678625 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,830,825 | 13,406.016008 | 52678625 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,780,445 | 0.018879 | 52678625 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,714 | 0.000012 | 52678625 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,691,310 | 2.308808 | 52678625 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,575,416 | 2,667.246022 | 52678625 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,522,602 | 0.916551 | 52678625 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,514,566 | 1.105492 | 52678625 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3048 | 1,494,025 | 2,666.968435 | 52678625 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,894 | 0.827237 | 52678625 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,373,109 | 0.000000 | 52678625 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,370,444 | 0.004828 | 52678625 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,354,610 | 23.206532 | 52678625 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,337,894 | 0.000282 | 52678625 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,316,178 | 1.126418 | 52678625 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,308,199 | 0.436294 | 52678625 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/SEND | 3000 | 1,250,965 | 62.094409 | 52678625 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,221,841 | 2,450.030993 | 52678625 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/cbBTC | 3000 | 1,216,168 | 0.029819 | 52678625 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,216,072 | 35,298,636.837928 | 52678625 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,215,544 | 1.105591 | 52678625 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,209,175 | 1,112,859.941136 | 52678625 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,174,415 | 496,085.125904 | 52678625 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,147,517 | 13.246747 | 52678625 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,142,905 | 0.885951 | 52678625 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |

## Recherche d'opportunités
- Cycles : 10913 ; routes examinées : 237772444 ; candidats optimisés : 1130742 ; net attendu > 0 : 296 ; dernier cycle 184.2 ms
- Rejets (moteur) : {'spread_below_threshold': 234314778, 'liquidity_below_min': 1797637, 'negative_expected_net': 1130446, 'pool_quarantined': 517054, 'borrow_bound_too_small': 10909, 'cycle_budget_exhausted': 1324}
- Enregistrements de la session : 1130742 ; net attendu > 0 : 296 ; simulés (eth_call de la vraie tx) : 63 (ok 14, échec 49) ; étiquettes ghost N+1 : 3/36 positives
- Décisions : {'REJECTED': 1130742} ; motifs de rejet : {'below_safety_margin': 179, 'negative_expected_net': 1130446, 'p_lower_below_threshold': 147, 'price_impact': 89, 'reliability_not_demonstrated': 149, 'simulation_failed': 49, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.028664 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1011 €) | — | 0.47 | 0.001 (n=10) | REJECTED | below_safety_margin(134<573), reliability_not_demonstrated |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.051068 WETH | 0.000047 WETH | 0.000000 WETH | 0.000002 WETH | 0.000045 WETH (0.1011 €) | — | 0.43 | 0.001 (n=10) | REJECTED | below_safety_margin(44910967314113<210213569031069), reliability_not_demonstrated |
| 52677220 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002693 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0854 €) | — | 4.20 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 221.202314 USDC | 0.099215 USDC | 0.000000 USDC | 0.007377 USDC | 0.091838 USDC (0.0845 €) | — | 4.15 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002694 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0839 €) | — | 4.12 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 219.481750 USDC | 0.098552 USDC | 0.000000 USDC | 0.007377 USDC | 0.091175 USDC (0.0839 €) | — | 4.15 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002694 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0832 €) | — | 4.08 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 222.439475 USDC | 0.097929 USDC | 0.000000 USDC | 0.007749 USDC | 0.090180 USDC (0.0830 €) | — | 4.05 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002359 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0748 €) | — | 4.20 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 187.810486 USDC | 0.087479 USDC | 0.000000 USDC | 0.007377 USDC | 0.080102 USDC (0.0737 €) | — | 4.27 | 0.233 (n=23) | REJECTED | reliability_not_demonstrated |
| 52677220 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002015 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0643 €) | — | 4.22 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 174.775027 USDC | 0.076985 USDC | 0.000000 USDC | 0.007749 USDC | 0.069236 USDC (0.0637 €) | — | 3.96 | 0.119 (n=57) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 146.123767 USDC | 0.045955 USDC | 0.000000 USDC | 0.005174 USDC | 0.040781 USDC (0.0375 €) | — | 2.79 | 0.143 (n=6) | REJECTED | reliability_not_demonstrated |
| 52677221 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 146.123767 USDC | 0.045955 USDC | 0.000000 USDC | 0.005174 USDC | 0.040781 USDC (0.0375 €) | — | 2.79 | 0.143 (n=6) | REJECTED | reliability_not_demonstrated |
| 52671989 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007406 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0264 €) | — | 0.47 | 0.072 (n=50) | REJECTED | below_safety_margin(35<148), p_lower_below_threshold(0.07<0.75) |
| 52671989 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 665.496868 USDC | 0.036012 USDC | 0.000000 USDC | 0.007407 USDC | 0.028605 USDC (0.0263 €) | — | 0.43 | 0.072 (n=50) | REJECTED | below_safety_margin(28605<133099), p_lower_below_threshold(0.07<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.232200 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0262 €) | — | 0.50 | 0.072 (n=50) | REJECTED | below_safety_margin(11661461449146<46439988969480), p_lower_below_threshold(0.07<0.75) |
| 52677220 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.052428 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0261 €) | — | 2.21 | 0.248 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.25<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 127.229995 USDC | 0.035656 USDC | 0.000000 USDC | 0.007377 USDC | 0.028279 USDC (0.0260 €) | — | 2.22 | 0.248 (n=35) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 52677220 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.051409 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0252 €) | — | 2.17 | 0.072 (n=50) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 52677220 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 125.273527 USDC | 0.034630 USDC | 0.000000 USDC | 0.007377 USDC | 0.027253 USDC (0.0251 €) | — | 2.18 | 0.072 (n=50) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 52677221 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.051086 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0247 €) | — | 2.14 | 0.248 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.25<0.75) |
| 52677221 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 124.819694 USDC | 0.034132 USDC | 0.000000 USDC | 0.007377 USDC | 0.026755 USDC (0.0246 €) | — | 2.14 | 0.248 (n=35) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 52671989 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH | 0.093167 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0245 €) | — | 1.17 | 0.072 (n=50) | REJECTED | below_safety_margin(10874860639808<18633447966148), p_lower_below_threshold(0.07<0.75) |
| 52671989 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.002696 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0241 €) | — | 1.19 | 0.072 (n=50) | REJECTED | below_safety_margin(32<53), p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 479 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.109 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
