# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T12:26:43+00:00 ; durée 180.41 min ; blocs 52590312 → 52595723 (5382 vus)

## Connexion
- Requêtes RPC : 71409 ; erreurs : 0 ; latence p50/p95 : 276.5/810.1 ms
- Rafraîchissements d'état : 5382 ; âge des données au dernier bloc : 3.04 s ; changements de frais LP observés (pools à frais dynamiques) : 9650
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 139816 ; cycles déclenchés par événement : 6024 ; avance médiane sur le rafraîchissement multicall : 689 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,508.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 584 pools, 329 jetons, 21950 routes
- Par DEX : uniswap_v3 142, aerodrome 236, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3924 (énumérés 395, par paires 0), mesurés 586, sous le plancher de 10000.0 $ : 2 → gardés 584 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2506.12853, 'AERO': 0.905993, 'cbBTC': 83225.723803}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,038,027 | 2,508.068668 | 52595724 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,106,141 | 1.095700 | 52595724 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,395,596 | 0.030007 | 52595724 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,369,311 | 107.936378 | 52595724 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,654,977 | 0.029965 | 52595724 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,744,467 | 0.029949 | 52595724 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,415,794 | 2,508.789043 | 52595724 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,305,786 | 0.000012 | 52595724 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,122,968 | 2,508.128461 | 52595724 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 549 | 8,955,049 | 2,508.881103 | 52595724 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,241,774 | 0.000012 | 52595724 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,351,848 | 0.001675 | 52595724 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,882,333 | 0.000012 | 52595724 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,708,277 | 1.097617 | 52595724 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,576,028 | 0.030002 | 52595724 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,539,522 | 1.000859 | 52595724 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,429,668 | 0.026511 | 52595724 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,781,437 | 0.000280 | 52595724 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,730,104 | 0.802388 | 52595724 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,499,653 | 2,509.308608 | 52595724 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,437,057 | 0.998938 | 52595724 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,174,685 | 34,233.373513 | 52595724 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,744,871 | 2,758.593468 | 52595724 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,034,533 | 1.141636 | 52595724 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,870,184 | 0.000012 | 52595724 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,680,528 | 405.763629 | 52595724 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,638,862 | 107.960810 | 52595724 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,572,357 | 0.000011 | 52595724 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,454,404 | 1,060,017.930553 | 52595724 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,395,362 | 2,511.954967 | 52595724 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,136,860 | 0.000000 | 52595724 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,960 | 1.189905 | 52595724 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | fBOMB/USDbC | 10000 | 2,033,410 | 0.023922 | 52595724 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,964,681 | 0.916707 | 52595724 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,892,527 | 15.648351 | 52595724 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 1,882,510 | 1,067.935428 | 52595724 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,859,884 | 1.371858 | 52595724 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,776,828 | 0.019055 | 52595724 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,771,816 | 0.000012 | 52595724 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,241 | 2.308749 | 52595724 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,575,428 | 2,749.329610 | 52595724 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,558,568 | 13,508.112920 | 52595724 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,550,658 | 1.105776 | 52595724 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | DRB/WETH | 10000 | 1,462,542 | 0.000000 | 52595724 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,571 | 0.833169 | 52595724 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,404,398 | 0.000279 | 52595724 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/AERO | 3016 | 1,401,808 | 2,749.918035 | 52595724 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,394,144 | 0.004847 | 52595724 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,309,708 | 1.119473 | 52595724 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,307,382 | 23.431572 | 52595724 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,280,447 | 32,923,552.101271 | 52595724 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,268,430 | 2,508.865188 | 52595724 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,247,381 | 62.451789 | 52595724 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,242,420 | 1.105594 | 52595724 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,219,406 | 72,976.703393 | 52595724 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,208,524 | 483,670.332625 | 52595724 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,195,162 | 1,194,163.262045 | 52595724 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,182,025 | 1.132012 | 52595724 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,150,464 | 47.614784 | 52595724 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,112,140 | 14.306192 | 52595724 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 11405 ; routes examinées : 250339750 ; candidats optimisés : 1294665 ; net attendu > 0 : 912 ; dernier cycle 214.9 ms
- Rejets (moteur) : {'spread_below_threshold': 246582412, 'liquidity_below_min': 2101277, 'negative_expected_net': 1293753, 'borrow_bound_too_small': 285125, 'cycle_budget_exhausted': 53461, 'unquotable': 22810}
- Enregistrements de la session : 1294665 ; net attendu > 0 : 912 ; simulés (eth_call de la vraie tx) : 28 (ok 16, échec 12) ; étiquettes ghost N+1 : 3/18 positives
- Décisions : {'REJECTED': 1294665} ; motifs de rejet : {'below_safety_margin': 245, 'negative_expected_net': 1293753, 'reliability_not_demonstrated': 912, 'simulation_failed': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52591461 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 4.060766 WETH | 0.005574 WETH | 0.000000 WETH | 0.000003 WETH | 0.005572 WETH (12.8002 €) | — | 13.72 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.120287 cbBTC | 0.000167 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000166 cbBTC (12.7602 €) | — | 13.84 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 3.396471 WETH | 0.002780 WETH | 0.000000 WETH | 0.000004 WETH | 0.002776 WETH (6.3600 €) | — | 8.17 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.100054 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (6.3572 €) | — | 8.29 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 8,421.081624 USDC | 6.911616 USDC | 0.000000 USDC | 0.010892 USDC | 6.900724 USDC (6.3487 €) | — | 8.19 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 3.359749 WETH | 0.002767 WETH | 0.000000 WETH | 0.000004 WETH | 0.002762 WETH (6.3461 €) | — | 8.22 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.099416 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (6.3272 €) | — | 8.30 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 8,421.081624 USDC | 6.877173 USDC | 0.000000 USDC | 0.010921 USDC | 6.866252 USDC (6.3170 €) | — | 8.15 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.344257 WETH | 0.002578 WETH | 0.000000 WETH | 0.000003 WETH | 0.002575 WETH (5.9158 €) | — | 7.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.098050 cbBTC | 0.000077 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000077 cbBTC (5.8979 €) | — | 7.85 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.790945 WETH | 0.002564 WETH | 0.000000 WETH | 0.000004 WETH | 0.002560 WETH (5.8664 €) | — | 6.75 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.112756 cbBTC | 0.000077 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000077 cbBTC (5.8636 €) | — | 6.79 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,526.367052 USDC | 6.374898 USDC | 0.000000 USDC | 0.010513 USDC | 6.364385 USDC (5.8552 €) | — | 6.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.798303 WETH | 0.002549 WETH | 0.000000 WETH | 0.000004 WETH | 0.002545 WETH (5.8470 €) | — | 6.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.112948 cbBTC | 0.000076 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000076 cbBTC (5.8304 €) | — | 6.73 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,459.488712 USDC | 6.336151 USDC | 0.000000 USDC | 0.010542 USDC | 6.325609 USDC (5.8196 €) | — | 6.69 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 4.383100 WETH | 0.002288 WETH | 0.000000 WETH | 0.000003 WETH | 0.002285 WETH (5.2487 €) | — | 5.21 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10,891.997010 USDC | 5.686515 USDC | 0.000000 USDC | 0.008265 USDC | 5.678250 USDC (5.2240 €) | — | 5.21 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.460880 WETH | 0.002090 WETH | 0.000000 WETH | 0.000003 WETH | 0.002087 WETH (4.7807 €) | — | 8.48 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 6,115.785412 USDC | 5.195578 USDC | 0.000000 USDC | 0.007864 USDC | 5.187714 USDC (4.7727 €) | — | 8.48 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.454511 WETH | 0.002080 WETH | 0.000000 WETH | 0.000003 WETH | 0.002077 WETH (4.7707 €) | — | 8.46 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 6,101.302985 USDC | 5.170641 USDC | 0.000000 USDC | 0.007886 USDC | 5.162755 USDC (4.7497 €) | — | 8.46 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.678239 WETH | 0.001980 WETH | 0.000000 WETH | 0.000004 WETH | 0.001976 WETH (4.5272 €) | — | 5.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.108217 cbBTC | 0.000059 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000059 cbBTC (4.5248 €) | — | 5.46 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,085.107890 USDC | 4.921764 USDC | 0.000000 USDC | 0.010135 USDC | 4.911629 USDC (4.5187 €) | — | 5.41 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 39 ; taux observé 0.154 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
