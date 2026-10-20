# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T10:34:06+00:00 ; durée 267.62 min ; blocs 52843518 → 52851542 (7471 vus)

## Connexion
- Requêtes RPC : 101051 ; erreurs : 65 ; latence p50/p95 : 93.4/1,679.6 ms
- Rafraîchissements d'état : 7472 ; âge des données au dernier bloc : 3.56 s ; changements de frais LP observés (pools à frais dynamiques) : 14558
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 83664 ; cycles déclenchés par événement : 5733 ; avance médiane sur le rafraîchissement multicall : 885 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,381.79 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21244 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 2 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.704066, 'AERO': 0.805188, 'cbBTC': 81576.404653}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,681,241 | 2,381.794367 | 52851541 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,345,357 | 1.247211 | 52851541 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,255,310 | 0.029296 | 52851541 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,234,156 | 98.717402 | 52851541 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,971,507 | 0.029259 | 52851541 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,294,635 | 0.029310 | 52851541 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,867,619 | 0.000012 | 52851541 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,289,442 | 2,382.157003 | 52851541 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,270,004 | 2,382.917669 | 52851541 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,803,087 | 0.000012 | 52851541 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,127,481 | 0.001664 | 52851541 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 698 | 7,091,496 | 2,381.553780 | 52851541 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 6,788,208 | 0.000012 | 52851541 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,339,082 | 0.029247 | 52851542 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,961,377 | 0.025548 | 52851541 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,745,238 | 0.802395 | 52851541 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,594,314 | 0.000275 | 52851541 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,341,883 | 2,381.361177 | 52851541 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDT | 427 | 4,321,935 | 2,385.154867 | 52851541 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,308,690 | 0.998767 | 52851541 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,961,725 | 34,281.796935 | 52851541 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,253,782 | 1.239528 | 52851541 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,230,204 | 2,963.260958 | 52851541 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,864,995 | 0.000012 | 52851541 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,725,059 | 1.142107 | 52851541 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,674,526 | 400.977996 | 52851541 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,634,100 | 98.810068 | 52851541 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,576,908 | 984.618818 | 52851541 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,172,978 | 1,219,622.054171 | 52851541 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,153,798 | 0.000010 | 52851541 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,548 | 1.237984 | 52851541 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52851541 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,924,582 | 0.000000 | 52851541 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,797,905 | 0.019049 | 52851541 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,763,357 | 0.000012 | 52851541 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,761,824 | 16.064564 | 52851541 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,723,327 | 1.105526 | 52851541 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,746 | 0.020336 | 52851541 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,664,318 | 13,691.291675 | 52851541 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,641,854 | 2.305920 | 52851541 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,610,662 | 2,972.096255 | 52851541 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,542,728 | 0.916342 | 52851541 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,804 | 0.826479 | 52851541 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,406,568 | 1.121294 | 52851541 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,298,426 | 0.000000 | 52851541 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,296,343 | 0.004721 | 52851541 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,288,099 | 0.000275 | 52851541 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,280,413 | 0.029315 | 52851541 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,245,081 | 2,382.156968 | 52851541 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,674 | 63.537857 | 52851541 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,205,798 | 23.000790 | 52851541 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,184,071 | 35,528,848.342447 | 52851541 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,178,292 | 0.435505 | 52851541 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/WELL | 10000 | 1,173,608 | 1,116,729.721199 | 52851541 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,153,474 | 1.131383 | 52851541 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,140,989 | 75,187.237399 | 52851541 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,125,530 | 509,894.264808 | 52851541 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,115,303 | 50.654342 | 52851541 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,082,461 | 0.885313 | 52851541 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,073,670 | 1.001447 | 52851541 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 13204 ; routes examinées : 280505776 ; candidats optimisés : 1597264 ; net attendu > 0 : 292 ; dernier cycle 319.9 ms
- Rejets (moteur) : {'spread_below_threshold': 276309797, 'liquidity_below_min': 2209177, 'negative_expected_net': 1596972, 'borrow_bound_too_small': 330075, 'pool_quarantined': 58800, 'cycle_budget_exhausted': 663}
- Enregistrements de la session : 1597264 ; net attendu > 0 : 292 ; simulés (eth_call de la vraie tx) : 34 (ok 9, échec 25) ; étiquettes ghost N+1 : 0/23 positives
- Décisions : {'REJECTED': 1597264} ; motifs de rejet : {'below_safety_margin': 133, 'negative_expected_net': 1596972, 'p_lower_below_threshold': 238, 'price_impact': 10, 'reliability_not_demonstrated': 54, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 25, 'stale_data': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52850453 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.003076 WETH | 0.000750 WETH | 0.000000 WETH | 0.000003 WETH | 0.000747 WETH (1.6364 €) | — | 7.45 | 0.000 (n=89) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52850453 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,387.441838 USDC | 1.784172 USDC | 0.000000 USDC | 0.006432 USDC | 1.777740 USDC (1.6355 €) | — | 7.45 | 0.000 (n=89) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52850453 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.892076 WETH | 0.000595 WETH | 0.000000 WETH | 0.000003 WETH | 0.000591 WETH (1.2961 €) | — | 6.63 | 0.112 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52850453 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.025632 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.2960 €) | — | 6.75 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,139.069615 USDC | 1.415763 USDC | 0.000000 USDC | 0.007880 USDC | 1.407883 USDC (1.2953 €) | — | 6.58 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.026262 cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000017 cbBTC (1.2736 €) | — | 6.47 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.908796 WETH | 0.000584 WETH | 0.000000 WETH | 0.000003 WETH | 0.000581 WETH (1.2733 €) | — | 6.39 | 0.112 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52850453 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,140.496701 USDC | 1.391103 USDC | 0.000000 USDC | 0.007880 USDC | 1.383223 USDC (1.2726 €) | — | 6.46 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.874416 WETH | 0.000553 WETH | 0.000000 WETH | 0.000003 WETH | 0.000549 WETH (1.2034 €) | — | 6.28 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.024861 cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000016 cbBTC (1.2031 €) | — | 6.46 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,057.695597 USDC | 1.315252 USDC | 0.000000 USDC | 0.007880 USDC | 1.307372 USDC (1.2028 €) | — | 6.35 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.881504 WETH | 0.000527 WETH | 0.000000 WETH | 0.000003 WETH | 0.000524 WETH (1.1481 €) | — | 5.94 | 0.143 (n=71) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52850453 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,096.602573 USDC | 1.254991 USDC | 0.000000 USDC | 0.007518 USDC | 1.247473 USDC (1.1477 €) | — | 5.95 | 0.143 (n=71) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52850453 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.779012 WETH | 0.000498 WETH | 0.000000 WETH | 0.000003 WETH | 0.000495 WETH (1.0841 €) | — | 6.35 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.022541 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0840 €) | — | 6.42 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,864.884360 USDC | 1.186067 USDC | 0.000000 USDC | 0.007880 USDC | 1.178187 USDC (1.0839 €) | — | 6.32 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.041999 WETH | 0.000452 WETH | 0.000000 WETH | 0.000003 WETH | 0.000449 WETH (0.9838 €) | — | 106.83 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52849710 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 100.003701 USDC | 1.075489 USDC | 0.000000 USDC | 0.007161 USDC | 1.068328 USDC (0.9829 €) | — | 106.83 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52850453 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.791585 WETH | 0.000448 WETH | 0.000000 WETH | 0.000002 WETH | 0.000445 WETH (0.9754 €) | — | 5.62 | 0.086 (n=25) | REJECTED | reliability_not_demonstrated |
| 52850453 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,882.801775 USDC | 1.065623 USDC | 0.000000 USDC | 0.005709 USDC | 1.059914 USDC (0.9751 €) | — | 5.63 | 0.086 (n=25) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.041877 WETH | 0.000448 WETH | 0.000000 WETH | 0.000003 WETH | 0.000445 WETH (0.9749 €) | — | 106.17 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52849710 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 99.727098 USDC | 1.065960 USDC | 0.000000 USDC | 0.007161 USDC | 1.058799 USDC (0.9741 €) | — | 106.17 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52850453 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.728998 WETH | 0.000425 WETH | 0.000000 WETH | 0.000003 WETH | 0.000422 WETH (0.9251 €) | — | 5.79 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52850453 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,734.970970 USDC | 1.013192 USDC | 0.000000 USDC | 0.007880 USDC | 1.005312 USDC (0.9249 €) | — | 5.79 | 0.112 (n=120) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.039592 WETH | 0.000422 WETH | 0.000000 WETH | 0.000003 WETH | 0.000419 WETH (0.9198 €) | — | 105.95 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1411 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
