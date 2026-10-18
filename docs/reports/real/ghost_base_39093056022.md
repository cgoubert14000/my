# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T08:45:14+00:00 ; durée 322.93 min ; blocs 52752192 → 52761878 (9507 vus)

## Connexion
- Requêtes RPC : 110654 ; erreurs : 13 ; latence p50/p95 : 313.9/1,639.7 ms
- Rafraîchissements d'état : 9508 ; âge des données au dernier bloc : 1.14 s ; changements de frais LP observés (pools à frais dynamiques) : 13947
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 603 ; cycles déclenchés par événement : 32 ; avance médiane sur le rafraîchissement multicall : 666 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,410.99 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21108 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2415.845921, 'AERO': 0.842347, 'cbBTC': 81764.569365}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,220,021 | 2,410.986474 | 52761878 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,959,826 | 1.198079 | 52761878 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,201,230 | 0.029506 | 52761878 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,715,740 | 108.566401 | 52761878 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,074,184 | 0.029544 | 52761878 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,402,133 | 0.029525 | 52761878 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,758,763 | 0.000012 | 52761878 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 9,506,563 | 0.000012 | 52761878 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,056,936 | 2,409.315280 | 52761878 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,855,604 | 0.000012 | 52761878 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,316,054 | 2,408.496690 | 52761878 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,128,330 | 0.001648 | 52761878 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,487,490 | 2,412.109408 | 52761878 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,326,848 | 0.029505 | 52761878 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,235,628 | 1.000855 | 52761878 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,132,964 | 0.025622 | 52761878 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,819,250 | 0.802398 | 52761878 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,622,280 | 0.000271 | 52761878 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,445,708 | 2,408.351924 | 52761878 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,436,993 | 0.998809 | 52761878 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,091,943 | 32,927.129286 | 52761878 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,338,637 | 2,866.457212 | 52761878 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,070,080 | 2,412.702657 | 52761878 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,910,437 | 1.141818 | 52761878 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,840,663 | 0.000012 | 52761878 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,740,721 | 0.000010 | 52761878 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,577,637 | 1.189684 | 52761878 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,541,112 | 108.598680 | 52761878 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,281,032 | 410.272630 | 52761878 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,234,423 | 1,181,913.960766 | 52761878 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52761878 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,374 | 1.374087 | 52761878 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,731 | 1.123493 | 52761878 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,957,322 | 15.851079 | 52761878 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,863,982 | 0.000000 | 52761878 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,809,826 | 0.021550 | 52761878 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,483 | 0.000012 | 52761878 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,766,510 | 0.018616 | 52761878 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,670,177 | 2.306444 | 52761878 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,367 | 1.105495 | 52761878 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,513,310 | 2,886.814836 | 52761878 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,384 | 0.826249 | 52761878 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3008 | 1,452,746 | 2,886.606187 | 52761878 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,397,293 | 13,890.940340 | 52761878 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,348,018 | 0.916373 | 52761878 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | DRB/WETH | 10000 | 1,326,980 | 0.000000 | 52761878 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,350 | 0.435823 | 52761878 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,302,550 | 0.004680 | 52761878 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,488 | 0.000270 | 52761878 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,255,863 | 0.029519 | 52761878 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,124 | 62.377421 | 52761878 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,239,314 | 23.372954 | 52761878 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,858 | 2,409.274890 | 52761878 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,903 | 35,795,251.835590 | 52761878 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,162,852 | 0.885696 | 52761878 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,162,348 | 1,166,766.396236 | 52761878 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,160,976 | 1.105821 | 52761878 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,153,328 | 1.131512 | 52761878 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,133,509 | 516,776.619631 | 52761878 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,098,591 | 14.769754 | 52761878 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 9539 ; routes examinées : 201349212 ; candidats optimisés : 1342533 ; net attendu > 0 : 117 ; dernier cycle 291.2 ms
- Rejets (moteur) : {'spread_below_threshold': 198273516, 'liquidity_below_min': 1719332, 'negative_expected_net': 1342416, 'borrow_bound_too_small': 9520, 'cycle_budget_exhausted': 4311}
- Enregistrements de la session : 1342533 ; net attendu > 0 : 117 ; simulés (eth_call de la vraie tx) : 18 (ok 18, échec 0) ; étiquettes ghost N+1 : 3/17 positives
- Décisions : {'REJECTED': 1342533} ; motifs de rejet : {'below_safety_margin': 72, 'negative_expected_net': 1342416, 'p_lower_below_threshold': 71, 'reliability_not_demonstrated': 46, 'stale_data': 20}

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
| 52760581 | WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.026854 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0503 €) | 0.000023 WETH | 8.44 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |
| 52760581 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC | 64.355026 USDC | 0.061774 USDC | 0.000000 USDC | 0.007244 USDC | 0.054530 USDC (0.0502 €) | — | 8.47 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |
| 52760581 | WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025665 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0459 €) | 0.000021 WETH | 8.07 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |
| 52760581 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC | 61.369012 USDC | 0.057434 USDC | 0.000000 USDC | 0.007610 USDC | 0.049824 USDC (0.0458 €) | — | 8.12 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |
| 52760581 | WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.022798 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0347 €) | 0.000016 WETH | 6.86 | 0.171 (n=45) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 52760581 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC | 54.941299 USDC | 0.044870 USDC | 0.000000 USDC | 0.007244 USDC | 0.037626 USDC (0.0346 €) | — | 6.85 | 0.171 (n=45) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 52760581 | WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.021543 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0300 €) | — | 6.28 | 0.171 (n=45) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 52760581 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC | 51.695970 USDC | 0.039798 USDC | 0.000000 USDC | 0.007244 USDC | 0.032554 USDC (0.0299 €) | — | 6.30 | 0.171 (n=45) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 52760581 | WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.021468 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0298 €) | — | 6.26 | 0.139 (n=79) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52760581 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC | 51.487020 USDC | 0.039576 USDC | 0.000000 USDC | 0.007244 USDC | 0.032332 USDC (0.0297 €) | — | 6.28 | 0.139 (n=79) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52760581 | WETH→[aerodrome_slipstream]→BIO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.011822 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0246 €) | — | 9.37 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 863 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.117 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
