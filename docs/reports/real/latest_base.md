# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T17:32:36+00:00 ; durée 3.04 min ; blocs 52691210 → 52691304 (92 vus)

## Connexion
- Requêtes RPC : 1325 ; erreurs : 0 ; latence p50/p95 : 108.0/1,369.2 ms
- Rafraîchissements d'état : 93 ; âge des données au dernier bloc : 1.56 s ; changements de frais LP observés (pools à frais dynamiques) : 282
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2959 ; cycles déclenchés par événement : 90 ; avance médiane sur le rafraîchissement multicall : 911 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,398.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21274 routes
- Par DEX : uniswap_v3 134, aerodrome 235 (quarantaine 1), aerodrome_slipstream 152, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3918 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2397.934409, 'AERO': 0.857255, 'cbBTC': 80846.375646}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52691514

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,572,002 | 2,398.822422 | 52691304 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,520,415 | 1.162726 | 52691304 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,182,032 | 0.029712 | 52691304 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,829,459 | 105.300472 | 52691304 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,855,592 | 0.029691 | 52691304 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,330,726 | 0.029702 | 52691304 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,712,351 | 0.000012 | 52691304 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,023,827 | 2,404.166689 | 52691304 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 7,804,339 | 0.000012 | 52691304 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 7,545,809 | 0.000012 | 52691304 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 967 | 7,242,083 | 2,404.902561 | 52691304 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,081,677 | 0.001666 | 52691304 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,388,517 | 2,399.274306 | 52691304 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,296,349 | 0.029714 | 52691304 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,293,157 | 0.025264 | 52691304 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,125,868 | 1.000855 | 52691304 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,914,418 | 1.158261 | 52691304 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,794,782 | 0.802398 | 52691304 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,641,942 | 0.000277 | 52691304 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,352,117 | 2,404.850683 | 52691304 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,288,838 | 0.998889 | 52691304 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,963,294 | 34,746.183658 | 52691304 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,414,138 | 2,784.081118 | 52691304 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,973,456 | 1.141827 | 52691304 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,832,746 | 0.000012 | 52691304 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/USDT | 475 | 2,740,639 | 2,407.584846 | 52691304 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,567,033 | 105.321439 | 52691304 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,565,561 | 402.444722 | 52691304 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,474,849 | 0.000011 | 52691304 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 2,465,637 | 1,026.088881 | 52691304 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,257,783 | 1,145,930.704504 | 52691304 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,133 | 1.195719 | 52691304 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,059,822 | 0.000000 | 52691304 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,009,165 | 1.405359 | 52691304 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,956,220 | 15.576724 | 52691304 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,825,866 | 0.022263 | 52691304 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,779,502 | 0.018861 | 52691304 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,761,075 | 0.000012 | 52691304 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,754,917 | 13,549.906602 | 52691304 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,660,242 | 2.304247 | 52691304 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,522,635 | 2,792.824704 | 52691304 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,502,629 | 1.105492 | 52691304 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,491,126 | 2,793.914120 | 52691304 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,491,078 | 0.916551 | 52691304 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,735 | 0.825924 | 52691304 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,420,931 | 1.122473 | 52691304 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,338,772 | 0.000000 | 52691304 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,320,265 | 0.434652 | 52691304 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,309,756 | 0.004705 | 52691304 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,847 | 0.000275 | 52691304 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299949 | 52691304 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,230,360 | 23.390384 | 52691304 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,219,216 | 1.131095 | 52691304 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,196,436 | 2,404.099877 | 52691304 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/cbBTC | 3000 | 1,194,876 | 0.029705 | 52691304 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,191,435 | 35,380,958.737576 | 52691304 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,190,390 | 1.105606 | 52691304 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,179,886 | 1,120,912.565446 | 52691304 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,079 | 508,813.636861 | 52691304 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,131,567 | 13.711904 | 52691304 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 182 ; routes examinées : 3871868 ; candidats optimisés : 21171 ; net attendu > 0 : 28 ; dernier cycle 242.7 ms
- Rejets (moteur) : {'spread_below_threshold': 3792295, 'liquidity_below_min': 49870, 'negative_expected_net': 21143, 'pool_quarantined': 5012, 'unquotable': 3338, 'borrow_bound_too_small': 182}
- Enregistrements de la session : 21171 ; net attendu > 0 : 28 ; simulés (eth_call de la vraie tx) : 8 (ok 0, échec 8) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 21171} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 21143, 'p_lower_below_threshold': 22, 'price_impact': 9, 'reliability_not_demonstrated': 6, 'simulation_failed': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52691265 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 279.120581 USDC | 0.058097 USDC | 0.000000 USDC | 0.007286 USDC | 0.050811 USDC (0.0467 €) | — | 1.82 | 0.128 (n=66) | REJECTED | below_safety_margin(50811<55824), p_lower_below_threshold(0.13<0.75) |
| 52691265 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003163 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0461 €) | — | 1.96 | 0.128 (n=66) | REJECTED | below_safety_margin(62<63), p_lower_below_threshold(0.13<0.75) |
| 52691265 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.099999 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0331 €) | — | 1.50 | 0.128 (n=66) | REJECTED | below_safety_margin(15010432427715<19999775649055), p_lower_below_threshold(0.13<0.75) |
| 52691265 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002858 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0327 €) | — | 1.54 | 0.128 (n=66) | REJECTED | below_safety_margin(44<57), p_lower_below_threshold(0.13<0.75) |
| 52691265 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.061912 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0307 €) | — | 2.25 | 0.128 (n=66) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52691265 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001594 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0297 €) | — | 2.51 | 0.128 (n=66) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52691265 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 169.131768 USDC | 0.021058 USDC | 0.000000 USDC | 0.005115 USDC | 0.015943 USDC (0.0147 €) | — | 0.94 | 0.143 (n=6) | REJECTED | below_safety_margin(15943<33826), reliability_not_demonstrated |
| 52691265 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 139.464320 USDC | 0.015094 USDC | 0.000000 USDC | 0.006954 USDC | 0.008140 USDC (0.0075 €) | — | 0.58 | 0.037 (n=22) | REJECTED | below_safety_margin(8140<27892), reliability_not_demonstrated |
| 52691265 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.058701 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0075 €) | — | 0.58 | 0.037 (n=22) | REJECTED | below_safety_margin(3379634134451<11740246448763), reliability_not_demonstrated |
| 52691265 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 147.855145 USDC | 0.014889 USDC | 0.000000 USDC | 0.007286 USDC | 0.007603 USDC (0.0070 €) | — | 0.51 | 0.303 (n=49) | REJECTED | below_safety_margin(7603<29571), p_lower_below_threshold(0.30<0.75) |
| 52691265 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 139.067668 USDC | 0.014795 USDC | 0.000000 USDC | 0.007286 USDC | 0.007509 USDC (0.0069 €) | — | 0.54 | 0.303 (n=49) | REJECTED | below_safety_margin(7509<27813), p_lower_below_threshold(0.30<0.75) |
| 52691265 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.001622 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0067 €) | — | 0.55 | 0.303 (n=49) | REJECTED | below_safety_margin(9<32), p_lower_below_threshold(0.30<0.75) |
| 52691265 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001380 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0059 €) | — | 0.58 | 0.303 (n=49) | REJECTED | below_safety_margin(8<27), p_lower_below_threshold(0.30<0.75) |
| 52691265 | USDC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 85.325649 USDC | 0.010684 USDC | 0.000000 USDC | 0.005448 USDC | 0.005236 USDC (0.0048 €) | — | 0.61 | 0.075 (n=4) | REJECTED | below_safety_margin(5236<17065), reliability_not_demonstrated |
| 52691256 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000816 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0037 €) | — | 0.61 | 0.075 (n=4) | REJECTED | below_safety_margin(5<16), reliability_not_demonstrated |
| 52691256 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.046378 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0035 €) | — | 0.35 | 0.075 (n=4) | REJECTED | below_safety_margin(1602294727272<9275590893933), reliability_not_demonstrated |
| 52691213 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 8.09 | 0.027 (n=53) | REJECTED | price_impact(216bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52691214 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 8.09 | 0.027 (n=54) | REJECTED | price_impact(216bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52691214 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 8.09 | 0.027 (n=54) | REJECTED | price_impact(216bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52691265 | USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 72.277504 USDC | 0.007816 USDC | 0.000000 USDC | 0.007286 USDC | 0.000530 USDC (0.0005 €) | — | 0.07 | 0.128 (n=66) | REJECTED | below_safety_margin(530<14455), p_lower_below_threshold(0.13<0.75) |
| 52691265 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.030440 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.07 | 0.128 (n=66) | REJECTED | below_safety_margin(213845911632<6088007122341), p_lower_below_threshold(0.13<0.75) |
| 52691265 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.041717 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.05 | 0.128 (n=66) | REJECTED | below_safety_margin(210106513792<8343309796520), p_lower_below_threshold(0.13<0.75) |
| 52691213 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006805 USDC | 0.000000 USDC | 0.006593 USDC | 0.000212 USDC (0.0002 €) | — | 2.12 | 0.113 (n=39) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.11<0.75) |
| 52691214 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006805 USDC | 0.000000 USDC | 0.006593 USDC | 0.000212 USDC (0.0002 €) | — | 2.12 | 0.110 (n=40) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.11<0.75) |
| 52691214 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.006805 USDC | 0.000000 USDC | 0.006593 USDC | 0.000212 USDC (0.0002 €) | — | 2.12 | 0.110 (n=40) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 635 ; taux observé 0.135 ; borne inférieure crédible (0.9) 0.119 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.9% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
