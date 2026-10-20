# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T13:41:21+00:00 ; durée 105.16 min ; blocs 52854009 → 52857163 (3120 vus)

## Connexion
- Requêtes RPC : 41282 ; erreurs : 5 ; latence p50/p95 : 303.7/908.0 ms
- Rafraîchissements d'état : 3120 ; âge des données au dernier bloc : 4.21 s ; changements de frais LP observés (pools à frais dynamiques) : 6639
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 40485 ; cycles déclenchés par événement : 1994 ; avance médiane sur le rafraîchissement multicall : 880 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,392.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21172 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 393, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2381.795213, 'AERO': 0.801082, 'cbBTC': 81409.268719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,345,459 | 2,392.898963 | 52857164 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,404,892 | 1.241375 | 52857164 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,441,369 | 97.334189 | 52857164 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,055,427 | 0.029370 | 52857164 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,855,256 | 0.029340 | 52857164 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,323,124 | 0.029325 | 52857164 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,874,583 | 0.000012 | 52857164 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,317,065 | 2,396.113354 | 52857164 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,289,259 | 2,392.999066 | 52857164 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 8,113,895 | 0.000012 | 52857164 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 7,705,812 | 0.000012 | 52857164 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,155,452 | 0.001670 | 52857164 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 758 | 7,119,080 | 2,395.963119 | 52857164 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,360,877 | 0.029364 | 52857164 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,954,281 | 0.025412 | 52857164 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,615,773 | 0.000275 | 52857164 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,613,595 | 0.802395 | 52857164 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,362,518 | 2,395.663094 | 52857164 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,317,781 | 0.998767 | 52857164 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,982,270 | 34,246.092980 | 52857164 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 448 | 3,501,686 | 2,399.549608 | 52857164 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,230,680 | 2,977.730386 | 52857164 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,871,883 | 0.000012 | 52857164 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 2,845,028 | 983.438386 | 52857164 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,737,748 | 1.142085 | 52857164 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2796 | 2,662,583 | 97.314462 | 52857164 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,655,693 | 402.075259 | 52857164 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,183,487 | 1,219,199.413671 | 52857164 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,107,423 | 0.000010 | 52857164 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,074,982 | 1.250021 | 52857164 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,548 | 1.237984 | 52857164 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,472 | 1.374234 | 52857164 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,934,104 | 0.000000 | 52857164 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,823,895 | 0.019601 | 52857164 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,772,616 | 13,692.495054 | 52857164 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,757,745 | 0.000012 | 52857164 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,731,362 | 1.105512 | 52857164 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,702,127 | 16.017093 | 52857164 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,677,217 | 0.020293 | 52857164 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,652,142 | 2.306429 | 52857164 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,621,366 | 1.123310 | 52857164 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,618,263 | 2,973.939601 | 52857164 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,549,933 | 0.916336 | 52857164 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,713 | 0.826123 | 52857164 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,304,789 | 0.004731 | 52857164 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,300,689 | 0.000000 | 52857164 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,294,150 | 0.000275 | 52857164 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,284,746 | 0.029326 | 52857164 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,236,136 | 63.593116 | 52857164 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,232,442 | 2,396.213561 | 52857164 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,210,686 | 23.007986 | 52857164 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,191,330 | 35,377,099.249005 | 52857164 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,178,385 | 0.435540 | 52857164 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/EDEL | 7000 | 1,150,162 | 74,684.221770 | 52857164 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,149,829 | 1,174,269.494585 | 52857164 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,145,533 | 1.131491 | 52857164 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,115 | 509,984.618203 | 52857164 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,121,990 | 50.052326 | 52857164 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,095,066 | 0.885413 | 52857164 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,072,586 | 1.001448 | 52857164 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 5113 ; routes examinées : 108252436 ; candidats optimisés : 637730 ; net attendu > 0 : 54 ; dernier cycle 274.1 ms
- Rejets (moteur) : {'spread_below_threshold': 106749403, 'liquidity_below_min': 736687, 'negative_expected_net': 637676, 'borrow_bound_too_small': 127675, 'cycle_budget_exhausted': 941}
- Enregistrements de la session : 637730 ; net attendu > 0 : 54 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 637730} ; motifs de rejet : {'below_safety_margin': 54, 'negative_expected_net': 637676, 'p_lower_below_threshold': 47, 'reliability_not_demonstrated': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52855720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 713.236514 USDC | 0.118318 USDC | 0.000000 USDC | 0.005387 USDC | 0.112931 USDC (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(112931<142647), reliability_not_demonstrated |
| 52855720 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.298322 WETH | 0.000049 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(47156112269631<59664491208030), reliability_not_demonstrated |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 538.043039 USDC | 0.088374 USDC | 0.000000 USDC | 0.007208 USDC | 0.081166 USDC (0.0747 €) | — | 1.51 | 0.105 (n=170) | REJECTED | below_safety_margin(81166<107608), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.220537 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0743 €) | — | 1.53 | 0.105 (n=170) | REJECTED | below_safety_margin(33743439129325<44107398343291), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006168 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0742 €) | — | 1.61 | 0.105 (n=170) | REJECTED | below_safety_margin(99<123), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 536.977543 USDC | 0.072310 USDC | 0.000000 USDC | 0.005387 USDC | 0.066923 USDC (0.0616 €) | — | 1.25 | 0.015 (n=55) | REJECTED | below_safety_margin(66923<107395), p_lower_below_threshold(0.01<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.223989 WETH | 0.000030 WETH | 0.000000 WETH | 0.000002 WETH | 0.000028 WETH (0.0615 €) | — | 1.25 | 0.015 (n=55) | REJECTED | below_safety_margin(27946824524775<44797787505007), p_lower_below_threshold(0.01<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004024 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0225 €) | — | 0.75 | 0.105 (n=170) | REJECTED | below_safety_margin(30<80), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.149644 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | — | 0.68 | 0.105 (n=170) | REJECTED | below_safety_margin(10137837285679<29928744395192), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 356.300100 USDC | 0.031278 USDC | 0.000000 USDC | 0.007208 USDC | 0.024070 USDC (0.0221 €) | — | 0.68 | 0.105 (n=170) | REJECTED | below_safety_margin(24070<71260), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002845 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 0.98 | 0.105 (n=170) | REJECTED | below_safety_margin(28<56), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.101917 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0208 €) | — | 0.93 | 0.105 (n=170) | REJECTED | below_safety_margin(9435113610228<20383429878557), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 235.351875 USDC | 0.029739 USDC | 0.000000 USDC | 0.007208 USDC | 0.022531 USDC (0.0207 €) | — | 0.96 | 0.105 (n=170) | REJECTED | below_safety_margin(22531<47070), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.044009 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0110 €) | — | 1.14 | 0.105 (n=170) | REJECTED | below_safety_margin(5008385979697<8801774534475), p_lower_below_threshold(0.10<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 104.563635 USDC | 0.019457 USDC | 0.000000 USDC | 0.007572 USDC | 0.011885 USDC (0.0109 €) | — | 1.14 | 0.105 (n=170) | REJECTED | below_safety_margin(11885<20912), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001405 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | — | 1.00 | 0.105 (n=170) | REJECTED | below_safety_margin(14<28), p_lower_below_threshold(0.10<0.75) |
| 52855680 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 84.613405 USDC | 0.018485 USDC | 0.000000 USDC | 0.007212 USDC | 0.011273 USDC (0.0104 €) | — | 1.33 | 0.105 (n=170) | REJECTED | below_safety_margin(11273<16922), p_lower_below_threshold(0.10<0.75) |
| 52855680 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.035564 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0104 €) | — | 1.32 | 0.105 (n=170) | REJECTED | below_safety_margin(4702508601311<7112792044539), p_lower_below_threshold(0.10<0.75) |
| 52855680 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 87.399957 USDC | 0.018089 USDC | 0.000000 USDC | 0.007212 USDC | 0.010877 USDC (0.0100 €) | — | 1.24 | 0.105 (n=170) | REJECTED | below_safety_margin(10877<17479), p_lower_below_threshold(0.10<0.75) |
| 52855680 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036623 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0100 €) | — | 1.24 | 0.105 (n=170) | REJECTED | below_safety_margin(4536792122586<7324657206735), p_lower_below_threshold(0.10<0.75) |
| 52856880 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.042020 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0052 €) | — | 0.56 | 0.280 (n=78) | REJECTED | below_safety_margin(2345600092714<8403918424527), p_lower_below_threshold(0.28<0.75) |
| 52856880 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 100.936921 USDC | 0.012784 USDC | 0.000000 USDC | 0.007210 USDC | 0.005574 USDC (0.0051 €) | — | 0.55 | 0.280 (n=78) | REJECTED | below_safety_margin(5574<20187), p_lower_below_threshold(0.28<0.75) |
| 52855680 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001150 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.52 | 0.105 (n=170) | REJECTED | below_safety_margin(6<22), p_lower_below_threshold(0.10<0.75) |
| 52855680 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001576 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.38 | 0.002 (n=5) | REJECTED | below_safety_margin(6<31), reliability_not_demonstrated |
| 52855680 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.030290 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.64 | 0.105 (n=170) | REJECTED | below_safety_margin(1935056188454<6058086925961), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1413 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
