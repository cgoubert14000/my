# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T01:35:08+00:00 ; durée 64.47 min ; blocs 52833443 → 52835378 (1849 vus)

## Connexion
- Requêtes RPC : 26252 ; erreurs : 125 ; latence p50/p95 : 203.9/658.1 ms
- Rafraîchissements d'état : 1849 ; âge des données au dernier bloc : 2.44 s ; changements de frais LP observés (pools à frais dynamiques) : 5057
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 43952 ; cycles déclenchés par événement : 1887 ; avance médiane sur le rafraîchissement multicall : 626 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,388.14 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,695,823 | 2,388.137745 | 52835378 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,029,283 | 1.272883 | 52835378 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,132,531 | 0.029355 | 52835378 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,503,774 | 96.214247 | 52835378 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 10,462,343 | 0.029296 | 52835378 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,305,165 | 0.029306 | 52835378 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,854,047 | 0.000012 | 52835378 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,315,719 | 2,394.302280 | 52835378 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,285,744 | 2,388.054232 | 52835378 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 7,807,460 | 0.000012 | 52835378 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,149,071 | 0.001672 | 52835378 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 818 | 7,107,903 | 2,393.738628 | 52835378 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 6,480,755 | 0.000012 | 52835378 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,313,829 | 0.029359 | 52835378 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,896,422 | 0.025627 | 52835378 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,757,875 | 0.802395 | 52835378 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,756,924 | 1.273032 | 52835378 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,601,587 | 0.000274 | 52835378 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,414,215 | 2,393.450354 | 52835378 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,311,261 | 0.998768 | 52835378 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,007,189 | 33,687.044466 | 52835378 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,219,539 | 3,046.013892 | 52835378 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 466 | 3,042,569 | 2,397.202989 | 52835378 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,848,156 | 0.000012 | 52835378 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 3126 | 2,664,051 | 96.240974 | 52835378 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,620,074 | 1.142094 | 52835378 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,594,745 | 400.740703 | 52835378 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,220,105 | 0.000010 | 52835378 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,174,674 | 1,224,214.616513 | 52835378 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,468 | 1.238011 | 52835378 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,304 | 1.373260 | 52835378 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,994,544 | 0.000000 | 52835378 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,811,782 | 0.019512 | 52835378 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,802,675 | 16.094671 | 52835378 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,763,751 | 0.000012 | 52835378 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,727,893 | 1.105525 | 52835378 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,672,859 | 0.020215 | 52835378 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,638,755 | 2.305887 | 52835378 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,546,834 | 0.916343 | 52835378 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,533,342 | 1.121601 | 52835378 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,490,491 | 3,042.689611 | 52835378 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,673 | 0.826781 | 52835378 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,401,720 | 13,659.157428 | 52835378 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,300,695 | 0.000000 | 52835378 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,472 | 0.004702 | 52835378 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,289,986 | 0.000275 | 52835378 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,277,006 | 0.029313 | 52835378 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,230,350 | 64.192636 | 52835378 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,214,348 | 1,048,607.334240 | 52835378 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,206,395 | 23.009285 | 52835378 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,204,879 | 2,394.225098 | 52835378 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,189,267 | 35,351,980.698677 | 52835378 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,130 | 0.435512 | 52835378 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,153,826 | 1.131434 | 52835378 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,126,811 | 511,519.337817 | 52835378 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,095,638 | 52.488909 | 52835378 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,088,215 | 0.885357 | 52835378 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,073,863 | 1.001399 | 52835378 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,073,794 | 15.661029 | 52835378 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,051,776 | 88,942.707477 | 52835378 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 3735 ; routes examinées : 78726330 ; candidats optimisés : 448815 ; net attendu > 0 : 251 ; dernier cycle 128.8 ms
- Rejets (moteur) : {'spread_below_threshold': 77565520, 'liquidity_below_min': 617097, 'negative_expected_net': 448564, 'borrow_bound_too_small': 93371, 'cycle_budget_exhausted': 1527}
- Enregistrements de la session : 448815 ; net attendu > 0 : 251 ; simulés (eth_call de la vraie tx) : 18 (ok 5, échec 13) ; étiquettes ghost N+1 : 3/11 positives
- Décisions : {'REJECTED': 448815} ; motifs de rejet : {'below_safety_margin': 161, 'negative_expected_net': 448564, 'p_lower_below_threshold': 196, 'reliability_not_demonstrated': 55, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 13}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52834629 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.588416 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1500 €) | — | 1.17 | 0.110 (n=162) | REJECTED | below_safety_margin(68558854851700<117683174409720), p_lower_below_threshold(0.11<0.75) |
| 52834629 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,465.213965 USDC | 0.171276 USDC | 0.000000 USDC | 0.008289 USDC | 0.162987 USDC (0.1499 €) | — | 1.11 | 0.110 (n=162) | REJECTED | below_safety_margin(162987<293042), p_lower_below_threshold(0.11<0.75) |
| 52834629 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.016945 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1496 €) | — | 1.18 | 0.110 (n=162) | REJECTED | below_safety_margin(200<338), p_lower_below_threshold(0.11<0.75) |
| 52834629 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.478386 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000048 WETH (0.1045 €) | — | 1.00 | 0.002 (n=5) | REJECTED | below_safety_margin(47774342821363<95677238449549), reliability_not_demonstrated |
| 52834629 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,128.690898 USDC | 0.121836 USDC | 0.000000 USDC | 0.008289 USDC | 0.113547 USDC (0.1045 €) | — | 1.01 | 0.002 (n=5) | REJECTED | below_safety_margin(113547<225738), reliability_not_demonstrated |
| 52834629 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.013417 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1040 €) | — | 1.04 | 0.002 (n=5) | REJECTED | below_safety_margin(139<268), reliability_not_demonstrated |
| 52834629 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.256863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0756 €) | — | 1.34 | 0.002 (n=5) | REJECTED | below_safety_margin(34538246204055<51372517521810), reliability_not_demonstrated |
| 52834629 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007471 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0756 €) | — | 1.35 | 0.002 (n=5) | REJECTED | below_safety_margin(101<149), reliability_not_demonstrated |
| 52834629 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 591.082484 USDC | 0.090237 USDC | 0.000000 USDC | 0.008289 USDC | 0.081948 USDC (0.0754 €) | — | 1.39 | 0.002 (n=5) | REJECTED | below_safety_margin(81948<118216), reliability_not_demonstrated |
| 52834621 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.111020 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0564 €) | — | 2.32 | 0.112 (n=159) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52834622 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.111020 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0564 €) | -0.000002 WETH | 2.32 | 0.110 (n=162) | REJECTED | sim_below_estimate(808119406652<28964997499001), simulated_net_nonpositive, p_lower_below_threshold(0.11<0.75) |
| 52834621 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 262.557115 USDC | 0.068713 USDC | 0.000000 USDC | 0.007630 USDC | 0.061083 USDC (0.0562 €) | — | 2.33 | 0.112 (n=159) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52834622 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 262.557115 USDC | 0.068713 USDC | 0.000000 USDC | 0.007630 USDC | 0.061083 USDC (0.0562 €) | — | 2.33 | 0.110 (n=162) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52834621 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.105930 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0513 €) | — | 2.21 | 0.112 (n=159) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52834622 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.105930 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0513 €) | — | 2.21 | 0.110 (n=162) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52834621 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 251.083332 USDC | 0.063229 USDC | 0.000000 USDC | 0.007630 USDC | 0.055599 USDC (0.0512 €) | — | 2.21 | 0.112 (n=159) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52834622 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 251.083332 USDC | 0.063229 USDC | 0.000000 USDC | 0.007630 USDC | 0.055599 USDC (0.0512 €) | — | 2.21 | 0.110 (n=162) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52834621 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.098408 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0438 €) | — | 2.03 | 0.112 (n=159) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52834622 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.098408 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0438 €) | — | 2.03 | 0.110 (n=162) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52834621 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 232.459386 USDC | 0.055014 USDC | 0.000000 USDC | 0.007630 USDC | 0.047384 USDC (0.0436 €) | — | 2.04 | 0.112 (n=159) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52834622 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 232.459386 USDC | 0.055014 USDC | 0.000000 USDC | 0.007630 USDC | 0.047384 USDC (0.0436 €) | — | 2.04 | 0.110 (n=162) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52834617 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→uSOL→[aerodrome_slipstream]→cbBTC | 0.001473 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0345 €) | — | 3.12 | 0.139 (n=67) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52834617 | WETH→[uniswap_v3]→uSOL→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.055891 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0342 €) | — | 2.79 | 0.280 (n=75) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 52834621 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.065951 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0270 €) | — | 1.87 | 0.112 (n=159) | REJECTED | below_safety_margin(12320314793895<13190171977522), p_lower_below_threshold(0.11<0.75) |
| 52834622 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.065951 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0270 €) | — | 1.87 | 0.110 (n=162) | REJECTED | below_safety_margin(12320314793895<13190171977522), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1347 ; taux observé 0.105 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
