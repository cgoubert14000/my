# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T06:41:11+00:00 ; durée 198.88 min ; blocs 52752192 → 52758158 (5903 vus)

## Connexion
- Requêtes RPC : 70527 ; erreurs : 5 ; latence p50/p95 : 314.8/1,705.4 ms
- Rafraîchissements d'état : 5903 ; âge des données au dernier bloc : 2.42 s ; changements de frais LP observés (pools à frais dynamiques) : 7427
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 603 ; cycles déclenchés par événement : 32 ; avance médiane sur le rafraîchissement multicall : 666 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,411.67 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21108 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2415.845921, 'AERO': 0.842347, 'cbBTC': 81764.569365}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,125,106 | 2,411.670960 | 52758158 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,437,313 | 1.194853 | 52758158 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,182,587 | 0.029527 | 52758158 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,750,392 | 108.178692 | 52758158 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,307,742 | 0.029544 | 52758158 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,457,119 | 0.029525 | 52758158 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 9,845,051 | 0.000012 | 52758158 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,764,965 | 0.000012 | 52758158 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,058,228 | 2,412.120534 | 52758158 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 564 | 8,248,506 | 2,411.325689 | 52758158 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,879,085 | 0.000012 | 52758158 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,144,088 | 0.001656 | 52758158 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,488,412 | 2,413.121439 | 52758158 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,336,932 | 0.029525 | 52758158 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,237,114 | 1.000855 | 52758158 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,143,089 | 0.025620 | 52758158 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,820,617 | 0.802398 | 52758158 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | WETH/USDT | 400 | 4,808,090 | 2,415.371153 | 52758158 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,623,593 | 0.000271 | 52758158 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,435,197 | 0.998809 | 52758158 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,410,287 | 2,411.321452 | 52758158 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,116,614 | 32,552.121977 | 52758158 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,343,574 | 2,856.652507 | 52758158 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,939,055 | 1.186496 | 52758158 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,912,902 | 1.141808 | 52758158 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,989 | 0.000012 | 52758158 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,760,948 | 409.072732 | 52758158 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,547,256 | 108.144380 | 52758158 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,483,517 | 0.000010 | 52758158 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,232,207 | 1,184,933.816615 | 52758158 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52758158 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,034,422 | 1.375202 | 52758158 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,815 | 1.123396 | 52758158 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,864,589 | 0.000000 | 52758158 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,811,990 | 0.021577 | 52758158 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,787,289 | 15.863904 | 52758158 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,343 | 0.000012 | 52758158 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,751,852 | 0.018354 | 52758158 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,745,118 | 13,863.486284 | 52758158 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,670,615 | 2.306483 | 52758158 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,796 | 1.105497 | 52758158 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,515,007 | 2,874.645659 | 52758158 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,466,963 | 0.916373 | 52758158 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,614 | 0.825990 | 52758158 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,455,843 | 2,876.710556 | 52758158 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,327,357 | 0.000000 | 52758158 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,120 | 0.435965 | 52758158 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,306,236 | 0.004694 | 52758158 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,852 | 0.000270 | 52758158 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,255,787 | 0.029519 | 52758158 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,124 | 62.377421 | 52758158 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,244,144 | 23.342283 | 52758158 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,202,502 | 1.105817 | 52758158 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,194,880 | 35,677,639.570842 | 52758158 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,187,201 | 2,412.112924 | 52758158 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,183,947 | 1.131529 | 52758158 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/WELL | 10000 | 1,163,036 | 1,166,033.609627 | 52758158 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,155,044 | 0.885649 | 52758158 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,139,259 | 516,776.619631 | 52758158 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,098,673 | 14.773713 | 52758158 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 5934 ; routes examinées : 125254872 ; candidats optimisés : 790959 ; net attendu > 0 : 75 ; dernier cycle 479.2 ms
- Rejets (moteur) : {'spread_below_threshold': 123378361, 'liquidity_below_min': 1076833, 'negative_expected_net': 790884, 'borrow_bound_too_small': 5921, 'cycle_budget_exhausted': 2798}
- Enregistrements de la session : 790959 ; net attendu > 0 : 75 ; simulés (eth_call de la vraie tx) : 13 (ok 13, échec 0) ; étiquettes ghost N+1 : 3/12 positives
- Décisions : {'REJECTED': 790959} ; motifs de rejet : {'below_safety_margin': 47, 'negative_expected_net': 790884, 'p_lower_below_threshold': 52, 'reliability_not_demonstrated': 23, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.062487 WETH | 0.000116 WETH | 0.000000 WETH | 0.000003 WETH | 0.000113 WETH (0.2504 €) | 0.000113 WETH | 18.06 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 150.166554 USDC | 0.279716 USDC | 0.000000 USDC | 0.007978 USDC | 0.271738 USDC (0.2500 €) | — | 18.10 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.059921 WETH | 0.000109 WETH | 0.000000 WETH | 0.000003 WETH | 0.000106 WETH (0.2356 €) | 0.000106 WETH | 17.72 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 143.885710 USDC | 0.263712 USDC | 0.000000 USDC | 0.007978 USDC | 0.255734 USDC (0.2353 €) | — | 17.77 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.056007 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.2000 €) | 0.000090 WETH | 16.09 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 134.827113 USDC | 0.225120 USDC | 0.000000 USDC | 0.007978 USDC | 0.217142 USDC (0.1998 €) | — | 16.11 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.054422 WETH | 0.000088 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1890 €) | — | 15.65 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 130.831975 USDC | 0.213155 USDC | 0.000000 USDC | 0.007978 USDC | 0.205177 USDC (0.1888 €) | — | 15.68 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.053204 WETH | 0.000084 WETH | 0.000000 WETH | 0.000003 WETH | 0.000081 WETH (0.1796 €) | — | 15.21 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 128.209747 USDC | 0.202962 USDC | 0.000000 USDC | 0.007978 USDC | 0.194984 USDC (0.1794 €) | — | 15.21 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.043868 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000065 WETH (0.1450 €) | — | 14.90 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 105.778714 USDC | 0.165882 USDC | 0.000000 USDC | 0.008344 USDC | 0.157538 USDC (0.1449 €) | — | 14.89 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 45.973554 USDC | 0.083693 USDC | 0.000000 USDC | 0.007978 USDC | 0.075715 USDC (0.0697 €) | — | 16.47 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.019103 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0696 €) | — | 16.41 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52752740 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 52.254860 USDC | 0.018706 USDC | 0.000000 USDC | 0.005424 USDC | 0.013282 USDC (0.0122 €) | 0.013282 USDC | 2.54 | 0.033 (n=25) | REJECTED | reliability_not_demonstrated |
| 52752740 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.021792 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0122 €) | 0.000005 WETH | 2.52 | 0.033 (n=25) | REJECTED | reliability_not_demonstrated |
| 52756570 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 26.978619 USDC | 0.017132 USDC | 0.000000 USDC | 0.005415 USDC | 0.011717 USDC (0.0108 €) | 0.011717 USDC | 4.34 | 0.000 (n=54) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52755499 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 32.693727 USDC | 0.015793 USDC | 0.000000 USDC | 0.005430 USDC | 0.010363 USDC (0.0095 €) | 0.010363 USDC | 3.17 | 0.000 (n=53) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52752740 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 46.729221 USDC | 0.015632 USDC | 0.000000 USDC | 0.005424 USDC | 0.010208 USDC (0.0094 €) | — | 2.18 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 52752740 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.019495 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0094 €) | 0.000004 WETH | 2.16 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 52757582 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 10.217936 USDC | 0.014573 USDC | 0.000000 USDC | 0.007279 USDC | 0.007294 USDC (0.0067 €) | — | 7.14 | 0.030 (n=71) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52757582 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.004269 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0067 €) | — | 7.06 | 0.030 (n=71) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52755043 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 26.425697 USDC | 0.010580 USDC | 0.000000 USDC | 0.005432 USDC | 0.005148 USDC (0.0047 €) | — | 1.95 | 0.030 (n=27) | REJECTED | below_safety_margin(5148<5285), reliability_not_demonstrated |
| 52752740 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.000468 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.85 | 0.132 (n=96) | REJECTED | below_safety_margin(4<9), p_lower_below_threshold(0.13<0.75) |
| 52752740 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000393 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 1.02 | 0.132 (n=96) | REJECTED | below_safety_margin(4<7), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 858 ; taux observé 0.132 ; borne inférieure crédible (0.9) 0.118 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
