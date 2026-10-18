# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T13:45:22+00:00 ; durée 287.16 min ; blocs 52762270 → 52770881 (8442 vus)

## Connexion
- Requêtes RPC : 115952 ; erreurs : 0 ; latence p50/p95 : 317.0/1,069.8 ms
- Rafraîchissements d'état : 8442 ; âge des données au dernier bloc : 3.68 s ; changements de frais LP observés (pools à frais dynamiques) : 15393
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 133012 ; cycles déclenchés par événement : 11687 ; avance médiane sur le rafraîchissement multicall : 410 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,387.65 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,452,736 | 2,387.645798 | 52770880 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,492,758 | 1.232779 | 52770880 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,047,945 | 0.029393 | 52770880 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,667,945 | 0.029387 | 52770880 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,526,940 | 108.084211 | 52770880 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,319,730 | 0.029399 | 52770880 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,745,445 | 0.000012 | 52770880 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,985,114 | 2,390.983603 | 52770880 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,536,216 | 0.000012 | 52770880 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,844,572 | 0.000012 | 52770880 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,087,187 | 0.001648 | 52770880 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 639 | 6,867,090 | 2,390.232138 | 52770880 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,460,708 | 2,387.731639 | 52770880 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,270,292 | 0.029381 | 52770880 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,184,942 | 1.000855 | 52770880 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,042,870 | 0.025720 | 52770880 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,772,598 | 0.802398 | 52770880 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,584,710 | 0.000272 | 52770880 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,410,945 | 0.998809 | 52770880 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,375,910 | 2,390.046127 | 52770880 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,308,064 | 1.227494 | 52770880 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,020,031 | 33,458.346263 | 52770880 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 409 | 3,695,364 | 2,394.746213 | 52770880 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,285,096 | 2,937.827667 | 52770880 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,877,333 | 1.141820 | 52770880 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,830,770 | 0.000012 | 52770880 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,667,406 | 409.470540 | 52770880 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,523,560 | 108.112644 | 52770880 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,492,516 | 0.000010 | 52770880 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,229,286 | 1,164,488.939756 | 52770880 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,106,813 | 1.199655 | 52770880 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,564 | 1.373959 | 52770880 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,959,572 | 1.123334 | 52770880 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,844,820 | 0.000000 | 52770880 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,841,030 | 15.765635 | 52770880 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,803,852 | 0.021398 | 52770880 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,771,020 | 0.018728 | 52770880 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,763,509 | 0.000012 | 52770880 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,726,489 | 1.105521 | 52770880 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,719,521 | 13,931.893815 | 52770880 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,654,631 | 2.304383 | 52770880 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,642,468 | 1,015.871183 | 52770880 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/AERO | 3000 | 1,488,760 | 2,951.173781 | 52770880 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,394 | 0.826238 | 52770880 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,448,611 | 0.916353 | 52770880 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,449 | 0.435380 | 52770880 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,310,262 | 0.000000 | 52770880 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,285,025 | 0.000270 | 52770880 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,270,473 | 0.004595 | 52770880 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,246,100 | 0.029402 | 52770880 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,250 | 63.891160 | 52770880 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,225,835 | 23.333401 | 52770880 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,200,615 | 1.131038 | 52770880 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,197,412 | 2,391.047939 | 52770880 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,186,991 | 35,292,776.914954 | 52770880 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,151,391 | 1,165,957.462515 | 52770880 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,119,821 | 520,265.007663 | 52770880 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,105,453 | 0.885258 | 52770880 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,093,577 | 14.943357 | 52770880 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,070,661 | 54.967930 | 52770880 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 20128 ; routes examinées : 434362240 ; candidats optimisés : 2223551 ; net attendu > 0 : 1220 ; dernier cycle 267.1 ms
- Rejets (moteur) : {'spread_below_threshold': 428647667, 'liquidity_below_min': 3237640, 'negative_expected_net': 2222331, 'pool_quarantined': 219014, 'borrow_bound_too_small': 20121, 'cycle_budget_exhausted': 14247}
- Enregistrements de la session : 2223551 ; net attendu > 0 : 1220 ; simulés (eth_call de la vraie tx) : 112 (ok 31, échec 81) ; étiquettes ghost N+1 : 0/83 positives
- Décisions : {'REJECTED': 2223551} ; motifs de rejet : {'below_safety_margin': 873, 'negative_expected_net': 2222331, 'p_lower_below_threshold': 863, 'price_impact': 10, 'reliability_not_demonstrated': 357, 'simulation_failed': 81, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,417.325434 USDC | 59.066396 USDC | 0.000000 USDC | 0.008276 USDC | 59.058120 USDC (54.3335 €) | — | 244.31 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 1.011007 WETH | 0.024704 WETH | 0.000000 WETH | 0.000003 WETH | 0.024700 WETH (54.2571 €) | — | 244.31 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,312.634946 USDC | 56.708251 USDC | 0.000000 USDC | 0.007913 USDC | 56.700338 USDC (52.1643 €) | — | 245.18 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.967329 WETH | 0.023720 WETH | 0.000000 WETH | 0.000003 WETH | 0.023717 WETH (52.0967 €) | — | 245.18 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 2,274.640161 USDC | 55.554743 USDC | 0.000000 USDC | 0.007551 USDC | 55.547192 USDC (51.1034 €) | — | 244.20 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.951562 WETH | 0.023241 WETH | 0.000000 WETH | 0.000003 WETH | 0.023237 WETH (51.0440 €) | — | 244.20 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,243.288344 USDC | 55.084663 USDC | 0.000000 USDC | 0.007913 USDC | 55.076750 USDC (50.6706 €) | — | 245.52 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.939175 WETH | 0.023062 WETH | 0.000000 WETH | 0.000003 WETH | 0.023058 WETH (50.6508 €) | — | 245.52 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.914135 WETH | 0.022310 WETH | 0.000000 WETH | 0.000004 WETH | 0.022307 WETH (48.9994 €) | — | 244.02 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,178.809292 USDC | 53.176189 USDC | 0.000000 USDC | 0.009001 USDC | 53.167188 USDC (48.9138 €) | — | 244.02 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.666406 WETH | 0.014989 WETH | 0.000000 WETH | 0.000003 WETH | 0.014985 WETH (32.9176 €) | — | 224.87 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,586.359759 USDC | 35.680055 USDC | 0.000000 USDC | 0.007551 USDC | 35.672504 USDC (32.8187 €) | — | 224.87 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.573961 WETH | 0.014054 WETH | 0.000000 WETH | 0.000004 WETH | 0.014050 WETH (30.8629 €) | — | 244.79 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 1,355.113824 USDC | 33.181754 USDC | 0.000000 USDC | 0.009725 USDC | 33.172029 USDC (30.5183 €) | — | 244.79 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.604121 WETH | 0.013597 WETH | 0.000000 WETH | 0.000003 WETH | 0.013594 WETH (29.8603 €) | — | 225.02 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 1,434.352755 USDC | 32.282352 USDC | 0.000000 USDC | 0.007221 USDC | 32.275131 USDC (29.6931 €) | — | 225.02 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v2]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.410707 WETH | 0.009351 WETH | 0.000000 WETH | 0.000003 WETH | 0.009348 WETH (20.5339 €) | — | 227.61 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 967.499101 USDC | 22.027141 USDC | 0.000000 USDC | 0.006447 USDC | 22.020694 USDC (20.2590 €) | — | 227.60 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 766.381127 USDC | 18.425084 USDC | 0.000000 USDC | 0.007221 USDC | 18.417863 USDC (16.9444 €) | — | 240.32 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.320435 WETH | 0.007704 WETH | 0.000000 WETH | 0.000003 WETH | 0.007701 WETH (16.9157 €) | — | 240.32 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 742.964236 USDC | 17.838472 USDC | 0.000000 USDC | 0.007221 USDC | 17.831251 USDC (16.4048 €) | — | 240.00 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.310957 WETH | 0.007466 WETH | 0.000000 WETH | 0.000003 WETH | 0.007463 WETH (16.3935 €) | — | 240.00 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 733.066834 USDC | 17.688253 USDC | 0.000000 USDC | 0.006859 USDC | 17.681394 USDC (16.2669 €) | — | 241.20 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52770826 | WETH→[uniswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.306584 WETH | 0.007398 WETH | 0.000000 WETH | 0.000003 WETH | 0.007395 WETH (16.2435 €) | — | 241.20 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52770826 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 726.602549 USDC | 17.556407 USDC | 0.000000 USDC | 0.007221 USDC | 17.549186 USDC (16.1453 €) | — | 241.52 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 946 ; taux observé 0.119 ; borne inférieure crédible (0.9) 0.107 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
