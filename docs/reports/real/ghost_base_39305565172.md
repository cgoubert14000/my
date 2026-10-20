# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T00:09:48+00:00 ; durée 316.1 min ; blocs 52823333 → 52832812 (9087 vus)

## Connexion
- Requêtes RPC : 123857 ; erreurs : 180 ; latence p50/p95 : 329.6/1,253.5 ms
- Rafraîchissements d'état : 9087 ; âge des données au dernier bloc : 4.27 s ; changements de frais LP observés (pools à frais dynamiques) : 13319
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 131183 ; cycles déclenchés par événement : 8199 ; avance médiane sur le rafraîchissement multicall : 1,190 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,405.84 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21062 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3873 (énumérés 387, par paires 0), mesurés 573, sous le plancher de 10000.0 $ : 2 → gardés 571 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2395.019975, 'AERO': 0.776373, 'cbBTC': 81898.158416}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,400,739 | 2,405.841469 | 52832812 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,216,025 | 1.259663 | 52832812 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,930,274 | 0.029321 | 52832812 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,246,481 | 0.029376 | 52832812 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,370,964 | 99.143980 | 52832812 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,379,153 | 0.029306 | 52832812 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,885,996 | 0.000012 | 52832812 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 9,671,836 | 0.000012 | 52832812 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,360,873 | 2,400.476456 | 52832812 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,316,417 | 2,405.731369 | 52832812 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 7,828,075 | 0.000012 | 52832812 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,267,338 | 2,401.302648 | 52832812 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,197,610 | 0.001672 | 52832812 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,353,889 | 0.029376 | 52832812 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,922,002 | 0.025626 | 52832812 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 433 | 4,881,964 | 2,403.722098 | 52832812 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,793,146 | 0.802395 | 52832812 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,635,677 | 0.000274 | 52832812 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,581,709 | 1.263518 | 52832812 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,428,411 | 2,401.455840 | 52832812 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,340,030 | 0.998768 | 52832812 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,034,907 | 33,720.235230 | 52832812 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,248,372 | 3,045.567430 | 52832812 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,859,348 | 0.000012 | 52832812 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,722,677 | 1.142200 | 52832812 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,651,395 | 99.128252 | 52832812 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,437,964 | 402.457972 | 52832812 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 2,312,704 | 965.481333 | 52832812 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,188,890 | 1,226,346.894757 | 52832812 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,096,924 | 0.000010 | 52832812 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,184 | 1.238174 | 52832812 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,084 | 1.373409 | 52832812 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,018,538 | 0.000000 | 52832812 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,862,483 | 16.130514 | 52832812 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,802,247 | 0.019298 | 52832812 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,559 | 0.000012 | 52832812 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,740,866 | 13,710.657401 | 52832812 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,740,459 | 1.105525 | 52832812 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,672,712 | 0.020215 | 52832812 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,649,917 | 2.307943 | 52832812 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,558,301 | 0.916343 | 52832812 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,533,440 | 1.121735 | 52832812 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,503,206 | 3,023.441180 | 52832812 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,172 | 0.826863 | 52832812 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,308,386 | 0.000000 | 52832812 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,306,596 | 0.004709 | 52832812 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,299,544 | 0.000276 | 52832812 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,286,004 | 0.029299 | 52832812 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,230,534 | 64.173528 | 52832812 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,223,601 | 1,048,177.283063 | 52832812 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,222,295 | 2,400.472869 | 52832812 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,216,255 | 23.009238 | 52832812 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,197,803 | 35,376,680.519362 | 52832812 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,723 | 0.435937 | 52832812 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,156,498 | 0.885725 | 52832812 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,137,601 | 508,665.214646 | 52832812 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,113,693 | 50.800855 | 52832812 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,111,384 | 1.131814 | 52832812 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,077,707 | 1.001386 | 52832812 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,760 | 15.549842 | 52832812 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 17285 ; routes examinées : 364056670 ; candidats optimisés : 2048225 ; net attendu > 0 : 37 ; dernier cycle 163.2 ms
- Rejets (moteur) : {'spread_below_threshold': 358660683, 'liquidity_below_min': 2913742, 'negative_expected_net': 2048188, 'borrow_bound_too_small': 432059, 'cycle_budget_exhausted': 1961}
- Enregistrements de la session : 2048225 ; net attendu > 0 : 37 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 2048225} ; motifs de rejet : {'below_safety_margin': 36, 'negative_expected_net': 2048188, 'p_lower_below_threshold': 32, 'reliability_not_demonstrated': 5, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52829937 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 71.479846 USDC | 0.079497 USDC | 0.000000 USDC | 0.005776 USDC | 0.073721 USDC (0.0678 €) | — | 10.31 | 0.000 (n=35) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002113 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0166 €) | — | 1.04 | 0.113 (n=158) | REJECTED | below_safety_margin(22<42), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002113 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0166 €) | — | 1.04 | 0.113 (n=158) | REJECTED | below_safety_margin(22<42), p_lower_below_threshold(0.11<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 178.132705 USDC | 0.024804 USDC | 0.000000 USDC | 0.007210 USDC | 0.017594 USDC (0.0162 €) | — | 0.99 | 0.113 (n=158) | REJECTED | below_safety_margin(17594<35626), p_lower_below_threshold(0.11<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 178.132705 USDC | 0.024804 USDC | 0.000000 USDC | 0.007210 USDC | 0.017594 USDC (0.0162 €) | — | 0.99 | 0.113 (n=158) | REJECTED | below_safety_margin(17594<35626), p_lower_below_threshold(0.11<0.75) |
| 52830940 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 83.817978 USDC | 0.022036 USDC | 0.000000 USDC | 0.005410 USDC | 0.016626 USDC (0.0153 €) | — | 1.98 | 0.042 (n=7) | REJECTED | below_safety_margin(16626<16763), reliability_not_demonstrated |
| 52830941 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 83.817978 USDC | 0.022036 USDC | 0.000000 USDC | 0.005410 USDC | 0.016626 USDC (0.0153 €) | — | 1.98 | 0.042 (n=7) | REJECTED | below_safety_margin(16626<16763), reliability_not_demonstrated |
| 52830941 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 83.817978 USDC | 0.022036 USDC | 0.000000 USDC | 0.005410 USDC | 0.016626 USDC (0.0153 €) | — | 1.98 | 0.042 (n=7) | REJECTED | below_safety_margin(16626<16763), reliability_not_demonstrated |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 230.403378 USDC | 0.015615 USDC | 0.000000 USDC | 0.007210 USDC | 0.008405 USDC (0.0077 €) | — | 0.36 | 0.280 (n=75) | REJECTED | below_safety_margin(8405<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 230.403378 USDC | 0.015615 USDC | 0.000000 USDC | 0.007210 USDC | 0.008405 USDC (0.0077 €) | — | 0.36 | 0.280 (n=75) | REJECTED | below_safety_margin(8405<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.39 | 0.280 (n=75) | REJECTED | below_safety_margin(10<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.39 | 0.280 (n=75) | REJECTED | below_safety_margin(10<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002436 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 0.37 | 0.280 (n=75) | REJECTED | below_safety_margin(9<48), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002436 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 0.37 | 0.280 (n=75) | REJECTED | below_safety_margin(9<48), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 230.403378 USDC | 0.013944 USDC | 0.000000 USDC | 0.007210 USDC | 0.006734 USDC (0.0062 €) | — | 0.29 | 0.280 (n=75) | REJECTED | below_safety_margin(6734<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 230.403378 USDC | 0.013944 USDC | 0.000000 USDC | 0.007210 USDC | 0.006734 USDC (0.0062 €) | — | 0.29 | 0.280 (n=75) | REJECTED | below_safety_margin(6734<46080), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.24 | 0.280 (n=75) | REJECTED | below_safety_margin(6<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002551 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0045 €) | — | 0.24 | 0.280 (n=75) | REJECTED | below_safety_margin(6<51), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 192.067166 USDC | 0.012104 USDC | 0.000000 USDC | 0.007210 USDC | 0.004894 USDC (0.0045 €) | — | 0.25 | 0.280 (n=75) | REJECTED | below_safety_margin(4894<38413), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 192.067166 USDC | 0.012104 USDC | 0.000000 USDC | 0.007210 USDC | 0.004894 USDC (0.0045 €) | — | 0.25 | 0.280 (n=75) | REJECTED | below_safety_margin(4894<38413), p_lower_below_threshold(0.28<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 179.501113 USDC | 0.010639 USDC | 0.000000 USDC | 0.007210 USDC | 0.003429 USDC (0.0032 €) | — | 0.19 | 0.113 (n=158) | REJECTED | below_safety_margin(3429<35900), p_lower_below_threshold(0.11<0.75) |
| 52825003 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 179.501113 USDC | 0.010639 USDC | 0.000000 USDC | 0.007210 USDC | 0.003429 USDC (0.0032 €) | — | 0.19 | 0.113 (n=158) | REJECTED | below_safety_margin(3429<35900), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002552 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.16 | 0.113 (n=158) | REJECTED | below_safety_margin(4<51), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002552 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.16 | 0.113 (n=158) | REJECTED | below_safety_margin(4<51), p_lower_below_threshold(0.11<0.75) |
| 52825003 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001291 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0023 €) | — | 0.23 | 0.113 (n=158) | REJECTED | below_safety_margin(3<25), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1336 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
