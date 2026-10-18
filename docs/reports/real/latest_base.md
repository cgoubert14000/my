# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T20:24:03+00:00 ; durée 12.24 min ; blocs 52782478 → 52782847 (367 vus)

## Connexion
- Requêtes RPC : 5276 ; erreurs : 0 ; latence p50/p95 : 221.5/756.4 ms
- Rafraîchissements d'état : 368 ; âge des données au dernier bloc : 1.67 s ; changements de frais LP observés (pools à frais dynamiques) : 1160
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10465 ; cycles déclenchés par événement : 560 ; avance médiane sur le rafraîchissement multicall : 431 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,336.59 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232 (quarantaine 1), aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 1 — aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52783083

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,991,777 | 2,336.592003 | 52782847 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,421,515 | 1.296689 | 52782847 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,683,234 | 0.029013 | 52782847 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,021,840 | 109.869596 | 52782847 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2535 | 12,613,231 | 0.028953 | 52782847 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,116,111 | 0.028937 | 52782847 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,691,656 | 0.000012 | 52782847 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,176,880 | 2,342.478639 | 52782847 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,799,927 | 0.000012 | 52782847 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 7,637,651 | 0.000012 | 52782847 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 669 | 7,006,590 | 2,342.049743 | 52782847 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,987,473 | 0.001630 | 52782847 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,390,597 | 2,337.692279 | 52782847 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,252,605 | 1.288769 | 52782847 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,119,677 | 0.029004 | 52782847 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,074,075 | 1.000854 | 52782847 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,837,211 | 0.026125 | 52782847 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,670,548 | 0.802398 | 52782847 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,460,327 | 0.000269 | 52782847 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,358,572 | 2,341.827938 | 52782847 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,287,702 | 0.998069 | 52782847 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,943,831 | 33,292.985532 | 52782847 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 433 | 3,442,809 | 2,346.989981 | 52782847 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,164,691 | 3,014.284734 | 52782847 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,820,342 | 0.000012 | 52782847 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,815,851 | 1.141832 | 52782847 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,606,050 | 415.693724 | 52782847 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,561,385 | 0.000010 | 52782847 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,429,879 | 109.902392 | 52782847 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,143,318 | 1,206,478.919535 | 52782847 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,785 | 1.233147 | 52782847 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52782847 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,941,815 | 0.000000 | 52782847 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,933,227 | 1,025.872671 | 52782847 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,932,330 | 1.121722 | 52782847 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,901,769 | 15.946124 | 52782847 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,774,682 | 0.020700 | 52782847 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,756,115 | 0.000012 | 52782847 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,725,617 | 0.017893 | 52782847 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,689,610 | 1.105523 | 52782847 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,624,531 | 14,369.981369 | 52782847 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,620,264 | 2.301814 | 52782847 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,562,972 | 3,035.495787 | 52782847 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,768 | 0.826942 | 52782847 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,417,636 | 0.916353 | 52782847 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,780 | 0.434746 | 52782847 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,285,141 | 0.000000 | 52782847 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,250,186 | 0.000267 | 52782847 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,239,885 | 0.028934 | 52782847 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52782847 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,227,798 | 1.130602 | 52782847 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,224,290 | 0.004510 | 52782847 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,203,986 | 23.270764 | 52782847 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,183,465 | 2,342.480171 | 52782847 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,180,185 | 33,768,726.579415 | 52782847 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,122,573 | 1,174,659.991479 | 52782847 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,094,313 | 532,485.414212 | 52782847 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,075,259 | 15.594262 | 52782847 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,069,749 | 55.062036 | 52782847 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,025,560 | 1.105812 | 52782847 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 927 ; routes examinées : 19285308 ; candidats optimisés : 75074 ; net attendu > 0 : 60 ; dernier cycle 154.7 ms
- Rejets (moteur) : {'spread_below_threshold': 19002901, 'liquidity_below_min': 169162, 'negative_expected_net': 75014, 'pool_quarantined': 37244, 'borrow_bound_too_small': 927}
- Enregistrements de la session : 75074 ; net attendu > 0 : 60 ; simulés (eth_call de la vraie tx) : 12 (ok 0, échec 12) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 75074} ; motifs de rejet : {'below_safety_margin': 46, 'negative_expected_net': 75014, 'p_lower_below_threshold': 54, 'price_impact': 11, 'reliability_not_demonstrated': 6, 'simulation_failed': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52782708 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 97.253897 USDC | 0.139738 USDC | 0.000000 USDC | 0.005252 USDC | 0.134486 USDC (0.1237 €) | — | 13.83 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52782715 | USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 201.790613 USDC | 0.061459 USDC | 0.000000 USDC | 0.007028 USDC | 0.054431 USDC (0.0501 €) | — | 2.70 | 0.125 (n=115) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52782715 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH | 0.086322 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0500 €) | — | 2.69 | 0.125 (n=115) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52782715 | USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 119.449451 USDC | 0.027429 USDC | 0.000000 USDC | 0.007383 USDC | 0.020046 USDC (0.0184 €) | — | 1.68 | 0.306 (n=63) | REJECTED | below_safety_margin(20046<23889), p_lower_below_threshold(0.31<0.75) |
| 52782715 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→AERO→[uniswap_v3]→WETH | 0.051106 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0184 €) | — | 1.68 | 0.306 (n=63) | REJECTED | below_safety_margin(8565993817297<10221179323370), p_lower_below_threshold(0.31<0.75) |
| 52782715 | USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 108.767595 USDC | 0.021155 USDC | 0.000000 USDC | 0.007028 USDC | 0.014127 USDC (0.0130 €) | — | 1.30 | 0.125 (n=115) | REJECTED | below_safety_margin(14127<21753), p_lower_below_threshold(0.13<0.75) |
| 52782715 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.046481 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 1.30 | 0.125 (n=115) | REJECTED | below_safety_margin(6033472141725<9296187388066), p_lower_below_threshold(0.13<0.75) |
| 52782727 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 188.934815 USDC | 0.018951 USDC | 0.000000 USDC | 0.005610 USDC | 0.013341 USDC (0.0123 €) | — | 0.71 | 0.019 (n=43) | REJECTED | below_safety_margin(13341<37786), p_lower_below_threshold(0.02<0.75) |
| 52782727 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.081240 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0122 €) | — | 0.70 | 0.019 (n=43) | REJECTED | below_safety_margin(5693164396615<16248095555711), p_lower_below_threshold(0.02<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.972905 USDC | 0.017881 USDC | 0.000000 USDC | 0.007032 USDC | 0.010849 USDC (0.0100 €) | — | 1.05 | 0.125 (n=115) | REJECTED | below_safety_margin(10849<20594), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.972905 USDC | 0.017881 USDC | 0.000000 USDC | 0.007032 USDC | 0.010849 USDC (0.0100 €) | — | 1.05 | 0.125 (n=115) | REJECTED | below_safety_margin(10849<20594), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.794059 USDC | 0.017734 USDC | 0.000000 USDC | 0.007032 USDC | 0.010702 USDC (0.0098 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10702<20558), p_lower_below_threshold(0.13<0.75) |
| 52782618 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 102.794059 USDC | 0.017734 USDC | 0.000000 USDC | 0.007032 USDC | 0.010702 USDC (0.0098 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10702<20558), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 101.747493 USDC | 0.017585 USDC | 0.000000 USDC | 0.007032 USDC | 0.010553 USDC (0.0097 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10553<20349), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 101.747493 USDC | 0.017585 USDC | 0.000000 USDC | 0.007032 USDC | 0.010553 USDC (0.0097 €) | — | 1.04 | 0.125 (n=115) | REJECTED | below_safety_margin(10553<20349), p_lower_below_threshold(0.13<0.75) |
| 52782617 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 102.973047 USDC | 0.017572 USDC | 0.000000 USDC | 0.007032 USDC | 0.010540 USDC (0.0097 €) | — | 1.02 | 0.125 (n=115) | REJECTED | below_safety_margin(10540<20594), p_lower_below_threshold(0.13<0.75) |
| 52782618 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 102.973047 USDC | 0.017572 USDC | 0.000000 USDC | 0.007032 USDC | 0.010540 USDC (0.0097 €) | — | 1.02 | 0.125 (n=115) | REJECTED | below_safety_margin(10540<20594), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001150 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.13 | 0.125 (n=115) | REJECTED | below_safety_margin(13<23), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001228 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.06 | 0.125 (n=115) | REJECTED | below_safety_margin(13<24), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001150 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.13 | 0.125 (n=115) | REJECTED | below_safety_margin(13<23), p_lower_below_threshold(0.13<0.75) |
| 52782616 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001228 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 1.06 | 0.125 (n=115) | REJECTED | below_safety_margin(13<24), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |
| 52782617 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001321 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0097 €) | — | 0.98 | 0.125 (n=115) | REJECTED | below_safety_margin(13<26), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 1080 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.100 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
