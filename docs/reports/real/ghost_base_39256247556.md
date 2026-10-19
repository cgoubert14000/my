# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T13:49:20+00:00 ; durée 45.94 min ; blocs 52812825 → 52814204 (1378 vus)

## Connexion
- Requêtes RPC : 16817 ; erreurs : 0 ; latence p50/p95 : 174.4/849.9 ms
- Rafraîchissements d'état : 1378 ; âge des données au dernier bloc : 4.06 s ; changements de frais LP observés (pools à frais dynamiques) : 3751
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2148 ; cycles déclenchés par événement : 109 ; avance médiane sur le rafraîchissement multicall : 1,027 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,410.81 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,812,524 | 2,410.808937 | 52814205 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,022,724 | 1.280571 | 52814205 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,336,850 | 0.029304 | 52814205 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,181,297 | 101.850560 | 52814205 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,094,663 | 0.029347 | 52814205 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,381,035 | 0.029362 | 52814205 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,857,811 | 0.000012 | 52814205 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,354,884 | 2,410.928877 | 52814205 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,326,248 | 2,410.687054 | 52814205 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 7,832,824 | 0.000012 | 52814205 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,249,455 | 2,410.990163 | 52814205 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,207,803 | 0.001662 | 52814205 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 6,631,303 | 0.000012 | 52814205 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,368,123 | 0.029292 | 52814205 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,940,664 | 0.025987 | 52814205 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,818,463 | 0.802395 | 52814205 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,741,975 | 1.281750 | 52814205 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/USDT | 409 | 4,635,950 | 2,414.107354 | 52814205 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,634,090 | 0.000273 | 52814205 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,431,749 | 2,409.974261 | 52814205 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,359,339 | 0.998770 | 52814205 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,030,431 | 33,934.882010 | 52814205 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,242,888 | 3,085.308719 | 52814205 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,857,818 | 0.000012 | 52814205 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,727,213 | 1.142006 | 52814205 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,667,350 | 405.819584 | 52814205 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,638,587 | 101.812403 | 52814205 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,622,658 | 0.000009 | 52814205 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2736 | 2,529,529 | 992.289475 | 52814205 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,185,659 | 1,235,059.554017 | 52814205 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,062,172 | 1.234881 | 52814205 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,054,805 | 0.000000 | 52814205 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52814205 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,796,052 | 16.021945 | 52814205 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,774,122 | 0.000012 | 52814205 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,772,018 | 13,840.094665 | 52814205 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,758,550 | 0.018477 | 52814205 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,743,213 | 1.105523 | 52814205 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,726,266 | 0.020593 | 52814205 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,667,723 | 2.308304 | 52814205 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,612,094 | 1.122131 | 52814205 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,600,846 | 3,084.568621 | 52814205 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,561,503 | 0.916350 | 52814205 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,163 | 0.827402 | 52814205 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,339,143 | 0.436137 | 52814205 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,320,081 | 0.000000 | 52814205 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,298,953 | 0.000274 | 52814205 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,286,227 | 0.029362 | 52814205 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,279,810 | 0.004581 | 52814205 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,277,867 | 23.129471 | 52814205 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,868 | 63.930699 | 52814205 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,208,066 | 1,079,754.573121 | 52814205 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,202,409 | 35,153,103.776698 | 52814205 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,197,304 | 2,410.939928 | 52814205 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,165,853 | 0.885881 | 52814205 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,486 | 515,481.870232 | 52814205 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,106,708 | 1.131870 | 52814205 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,103,501 | 51.743549 | 52814205 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,080,548 | 15.393974 | 52814205 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,055,086 | 89,930.736201 | 52814205 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 1486 ; routes examinées : 31211944 ; candidats optimisés : 225087 ; net attendu > 0 : 32 ; dernier cycle 293.8 ms
- Rejets (moteur) : {'spread_below_threshold': 30674020, 'liquidity_below_min': 271006, 'negative_expected_net': 225055, 'borrow_bound_too_small': 34226, 'cycle_budget_exhausted': 7605}
- Enregistrements de la session : 225087 ; net attendu > 0 : 32 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 225087} ; motifs de rejet : {'below_safety_margin': 26, 'negative_expected_net': 225055, 'p_lower_below_threshold': 32}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52813880 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.051297 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0187 €) | — | 1.64 | 0.282 (n=68) | REJECTED | below_safety_margin(8432011708986<10259353737266), p_lower_below_threshold(0.28<0.75) |
| 52813880 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 122.747609 USDC | 0.027572 USDC | 0.000000 USDC | 0.007287 USDC | 0.020285 USDC (0.0187 €) | — | 1.65 | 0.282 (n=68) | REJECTED | below_safety_margin(20285<24549), p_lower_below_threshold(0.28<0.75) |
| 52813880 | WETH→[aerodrome]→MET→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.012282 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0058 €) | 0.000003 WETH | 2.14 | 0.127 (n=60) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52813880 | USDC→[uniswap_v3]→WETH→[aerodrome]→MET→[aerodrome]→USDC | 29.673821 USDC | 0.012939 USDC | 0.000000 USDC | 0.006620 USDC | 0.006319 USDC (0.0058 €) | 0.006319 USDC | 2.13 | 0.127 (n=60) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52813898 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004736 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0038 €) | 0.000002 WETH | 3.58 | 0.125 (n=108) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52813898 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.347311 USDC | 0.011351 USDC | 0.000000 USDC | 0.007290 USDC | 0.004061 USDC (0.0037 €) | 0.004061 USDC | 3.58 | 0.125 (n=108) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52813898 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004540 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | 0.000001 WETH | 2.84 | 0.282 (n=68) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 52813898 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.921530 USDC | 0.010374 USDC | 0.000000 USDC | 0.007290 USDC | 0.003084 USDC (0.0028 €) | — | 2.82 | 0.282 (n=68) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 52813804 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004144 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.43 | 0.098 (n=146) | REJECTED | below_safety_margin(593942958774<828825150175), p_lower_below_threshold(0.10<0.75) |
| 52813805 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004152 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.41 | 0.098 (n=146) | REJECTED | below_safety_margin(584409191829<830362453590), p_lower_below_threshold(0.10<0.75) |
| 52813804 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.949683 USDC | 0.008698 USDC | 0.000000 USDC | 0.007286 USDC | 0.001412 USDC (0.0013 €) | — | 1.42 | 0.098 (n=146) | REJECTED | below_safety_margin(1412<1989), p_lower_below_threshold(0.10<0.75) |
| 52813805 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.947531 USDC | 0.008686 USDC | 0.000000 USDC | 0.007297 USDC | 0.001389 USDC (0.0013 €) | — | 1.40 | 0.098 (n=146) | REJECTED | below_safety_margin(1389<1989), p_lower_below_threshold(0.10<0.75) |
| 52813831 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003994 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.92 | 0.098 (n=146) | REJECTED | below_safety_margin(368875072634<798842227760), p_lower_below_threshold(0.10<0.75) |
| 52813831 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.628025 USDC | 0.008157 USDC | 0.000000 USDC | 0.007287 USDC | 0.000870 USDC (0.0008 €) | — | 0.90 | 0.098 (n=146) | REJECTED | below_safety_margin(870<1925), p_lower_below_threshold(0.10<0.75) |
| 52813831 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003974 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.80 | 0.282 (n=68) | REJECTED | below_safety_margin(318936575720<794817108183), p_lower_below_threshold(0.28<0.75) |
| 52813831 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.536565 USDC | 0.008036 USDC | 0.000000 USDC | 0.007287 USDC | 0.000749 USDC (0.0007 €) | — | 0.79 | 0.282 (n=68) | REJECTED | below_safety_margin(749<1907), p_lower_below_threshold(0.28<0.75) |
| 52813831 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.003464 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.82 | 0.282 (n=68) | REJECTED | below_safety_margin(285583276218<692862386630), p_lower_below_threshold(0.28<0.75) |
| 52813798 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003957 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.70 | 0.282 (n=68) | REJECTED | below_safety_margin(278376931757<791377318253), p_lower_below_threshold(0.28<0.75) |
| 52813831 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.304169 USDC | 0.007957 USDC | 0.000000 USDC | 0.007287 USDC | 0.000670 USDC (0.0006 €) | — | 0.81 | 0.282 (n=68) | REJECTED | below_safety_margin(670<1660), p_lower_below_threshold(0.28<0.75) |
| 52813798 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.536940 USDC | 0.007936 USDC | 0.000000 USDC | 0.007285 USDC | 0.000651 USDC (0.0006 €) | — | 0.68 | 0.282 (n=68) | REJECTED | below_safety_margin(651<1907), p_lower_below_threshold(0.28<0.75) |
| 52813806 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.62 | 0.282 (n=68) | REJECTED | below_safety_margin(244560031629<789881455488), p_lower_below_threshold(0.28<0.75) |
| 52813805 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.61 | 0.282 (n=68) | REJECTED | below_safety_margin(239976250042<789881455488), p_lower_below_threshold(0.28<0.75) |
| 52813806 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.535538 USDC | 0.007856 USDC | 0.000000 USDC | 0.007286 USDC | 0.000570 USDC (0.0005 €) | — | 0.60 | 0.282 (n=68) | REJECTED | below_safety_margin(570<1907), p_lower_below_threshold(0.28<0.75) |
| 52813805 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.535538 USDC | 0.007856 USDC | 0.000000 USDC | 0.007297 USDC | 0.000559 USDC (0.0005 €) | — | 0.59 | 0.282 (n=68) | REJECTED | below_safety_margin(559<1907), p_lower_below_threshold(0.28<0.75) |
| 52813806 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003898 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.40 | 0.098 (n=146) | REJECTED | below_safety_margin(157735730047<779506605458), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1275 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
