# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T15:18:42+00:00 ; durée 202.52 min ; blocs 52854009 → 52860082 (5856 vus)

## Connexion
- Requêtes RPC : 72926 ; erreurs : 43 ; latence p50/p95 : 424.0/1,496.3 ms
- Rafraîchissements d'état : 5856 ; âge des données au dernier bloc : 5.72 s ; changements de frais LP observés (pools à frais dynamiques) : 20421
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 40485 ; cycles déclenchés par événement : 1994 ; avance médiane sur le rafraîchissement multicall : 880 ms
- Gaz : base fee 0.006778 gwei ; prix ETH (pool le plus profond) : 2,435.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21172 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 393, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2381.795213, 'AERO': 0.801082, 'cbBTC': 81409.268719}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,333,777 | 2,435.815602 | 52860083 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 39,377,340 | 1.176916 | 52860083 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,001,868 | 94.582023 | 52860083 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,295,642 | 0.029573 | 52860083 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2545 | 13,305,241 | 0.029607 | 52860083 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,494,107 | 0.029619 | 52860083 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,921,035 | 0.000012 | 52860083 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,492,368 | 2,440.241457 | 52860083 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,363,303 | 2,435.851553 | 52860083 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,150,713 | 0.000012 | 52860083 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 7,360,005 | 2,440.553024 | 52860083 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,241,766 | 0.001671 | 52860083 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 6,527,298 | 0.000012 | 52860083 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,413,674 | 0.029566 | 52860083 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,222,489 | 0.024873 | 52860083 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,704,620 | 0.000275 | 52860083 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,696,345 | 0.802394 | 52860083 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,408,233 | 2,441.029165 | 52860083 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,365,450 | 0.998767 | 52860083 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,038,015 | 34,512.519939 | 52860083 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 430 | 3,449,193 | 2,443.386322 | 52860083 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,347,580 | 2,868.171674 | 52860083 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,968,738 | 1.142081 | 52860083 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,891,144 | 0.000012 | 52860083 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2766 | 2,730,777 | 94.605945 | 52860083 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,520,950 | 403.242000 | 52860083 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,228,534 | 1,212,767.760885 | 52860083 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,218,795 | 1.180895 | 52860083 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,162,543 | 0.000010 | 52860083 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,548 | 1.237984 | 52860083 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,472 | 1.374234 | 52860083 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,966,942 | 0.000000 | 52860083 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,560 | 0.019513 | 52860083 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,771,226 | 13,631.856779 | 52860083 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,592 | 0.000012 | 52860083 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,762,414 | 1.105512 | 52860083 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,712,403 | 0.021152 | 52860083 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,708,986 | 15.885474 | 52860083 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,681,016 | 2.312536 | 52860083 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,667,157 | 2,870.102569 | 52860083 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,564,926 | 0.916062 | 52860083 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,716 | 0.826121 | 52860083 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,416,921 | 1.124105 | 52860083 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,346,903 | 0.004811 | 52860083 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,342,264 | 0.000000 | 52860083 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,319,033 | 0.000275 | 52860083 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,303,299 | 0.029619 | 52860083 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,256,626 | 2,440.170906 | 52860083 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,078 | 63.599131 | 52860083 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,216,115 | 23.117674 | 52860083 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,214,404 | 69,416.381736 | 52860083 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/doginme | 10000 | 1,211,251 | 35,503,621.931895 | 52860083 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 509 | 1,182,518 | 0.886358 | 52860083 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,029 | 0.436967 | 52860083 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,164,702 | 494,262.857494 | 52860083 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,159,413 | 1,196,734.371957 | 52860083 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,151,492 | 47.520732 | 52860083 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,072,060 | 1.001371 | 52860083 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,067,763 | 15.892004 | 52860083 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,052,839 | 22,252,559.523601 | 52860083 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 7849 ; routes examinées : 166179028 ; candidats optimisés : 1010067 ; net attendu > 0 : 1104 ; dernier cycle 283.1 ms
- Rejets (moteur) : {'spread_below_threshold': 163526508, 'liquidity_below_min': 1328815, 'negative_expected_net': 1008963, 'pool_quarantined': 167416, 'borrow_bound_too_small': 134545, 'cycle_budget_exhausted': 11677}
- Enregistrements de la session : 1010067 ; net attendu > 0 : 1104 ; simulés (eth_call de la vraie tx) : 133 (ok 95, échec 38) ; étiquettes ghost N+1 : 17/94 positives
- Décisions : {'REJECTED': 1010067} ; motifs de rejet : {'below_safety_margin': 773, 'negative_expected_net': 1008963, 'p_lower_below_threshold': 910, 'price_impact': 42, 'reliability_not_demonstrated': 194, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 2, 'simulation_failed': 38, 'stale_data': 91}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52855720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 713.236514 USDC | 0.118318 USDC | 0.000000 USDC | 0.005387 USDC | 0.112931 USDC (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(112931<142647), reliability_not_demonstrated |
| 52855720 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.298322 WETH | 0.000049 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.1039 €) | — | 1.58 | 0.037 (n=8) | REJECTED | below_safety_margin(47156112269631<59664491208030), reliability_not_demonstrated |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 538.043039 USDC | 0.088374 USDC | 0.000000 USDC | 0.007208 USDC | 0.081166 USDC (0.0747 €) | — | 1.51 | 0.105 (n=170) | REJECTED | below_safety_margin(81166<107608), p_lower_below_threshold(0.10<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.220537 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0743 €) | — | 1.53 | 0.105 (n=170) | REJECTED | below_safety_margin(33743439129325<44107398343291), p_lower_below_threshold(0.10<0.75) |
| 52855720 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006168 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0742 €) | — | 1.61 | 0.105 (n=170) | REJECTED | below_safety_margin(99<123), p_lower_below_threshold(0.10<0.75) |
| 52858173 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 233.952408 USDC | 0.082506 USDC | 0.000000 USDC | 0.008077 USDC | 0.074429 USDC (0.0685 €) | — | 3.18 | 0.111 (n=129) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52858173 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.095097 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0683 €) | 0.000030 WETH | 3.18 | 0.111 (n=129) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52859942 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 278.999675 USDC | 0.080290 USDC | 0.000000 USDC | 0.009981 USDC | 0.070309 USDC (0.0647 €) | — | 2.52 | 0.118 (n=181) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52859942 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003341 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0645 €) | — | 2.54 | 0.118 (n=181) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52859942 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 278.875418 USDC | 0.078346 USDC | 0.000000 USDC | 0.009981 USDC | 0.068365 USDC (0.0629 €) | — | 2.45 | 0.118 (n=181) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52859942 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003145 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0622 €) | — | 2.61 | 0.118 (n=181) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52855720 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 536.977543 USDC | 0.072310 USDC | 0.000000 USDC | 0.005387 USDC | 0.066923 USDC (0.0616 €) | — | 1.25 | 0.015 (n=55) | REJECTED | below_safety_margin(66923<107395), p_lower_below_threshold(0.01<0.75) |
| 52855720 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.223989 WETH | 0.000030 WETH | 0.000000 WETH | 0.000002 WETH | 0.000028 WETH (0.0615 €) | — | 1.25 | 0.015 (n=55) | REJECTED | below_safety_margin(27946824524775<44797787505007), p_lower_below_threshold(0.01<0.75) |
| 52859942 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.003277 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0607 €) | — | 2.44 | 0.118 (n=181) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52859942 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 279.265483 USDC | 0.075835 USDC | 0.000000 USDC | 0.009981 USDC | 0.065854 USDC (0.0606 €) | — | 2.36 | 0.118 (n=181) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52858173 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 197.809913 USDC | 0.068017 USDC | 0.000000 USDC | 0.008077 USDC | 0.059940 USDC (0.0551 €) | — | 3.03 | 0.156 (n=76) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52858173 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.080556 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0550 €) | 0.000024 WETH | 3.02 | 0.156 (n=76) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52858043 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 129.489718 USDC | 0.066709 USDC | 0.000000 USDC | 0.008153 USDC | 0.058556 USDC (0.0539 €) | — | 4.52 | 0.115 (n=125) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52858043 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.052847 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0537 €) | 0.000024 WETH | 4.52 | 0.115 (n=125) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52858043 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 124.096602 USDC | 0.061595 USDC | 0.000000 USDC | 0.008153 USDC | 0.053442 USDC (0.0492 €) | — | 4.31 | 0.115 (n=125) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52858043 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.050692 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0490 €) | 0.000022 WETH | 4.30 | 0.115 (n=125) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52858043 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 113.256018 USDC | 0.047890 USDC | 0.000000 USDC | 0.008153 USDC | 0.039737 USDC (0.0366 €) | — | 3.51 | 0.115 (n=125) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52858043 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.046241 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0364 €) | 0.000016 WETH | 3.51 | 0.115 (n=125) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52858043 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[uniswap_v3]→USDC | 66.869385 USDC | 0.045146 USDC | 0.000000 USDC | 0.007785 USDC | 0.037361 USDC (0.0344 €) | — | 5.59 | 0.040 (n=109) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 52858043 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.027306 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0343 €) | — | 5.58 | 0.040 (n=109) | REJECTED | p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 1507 ; taux observé 0.105 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
