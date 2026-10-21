# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T19:06:17+00:00 ; durée 182.93 min ; blocs 52904622 → 52910111 (5373 vus)

## Connexion
- Requêtes RPC : 69358 ; erreurs : 8 ; latence p50/p95 : 375.9/1,083.4 ms
- Rafraîchissements d'état : 5373 ; âge des données au dernier bloc : 3.08 s ; changements de frais LP observés (pools à frais dynamiques) : 11323
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44757 ; cycles déclenchés par événement : 2376 ; avance médiane sur le rafraîchissement multicall : 510 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,491.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 327 jetons, 21568 routes
- Par DEX : uniswap_v3 138, aerodrome 236, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3876 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2506.228815, 'AERO': 0.862155, 'cbBTC': 84485.636227}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,383,422 | 2,491.733593 | 52910112 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 37,802,540 | 1.169741 | 52910112 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,986,510 | 92.634322 | 52910112 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,716,677 | 0.029542 | 52910112 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 12,575,562 | 0.029587 | 52910112 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,611,777 | 0.029599 | 52910112 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,910,303 | 0.000012 | 52910112 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,873,773 | 2,488.592456 | 52910112 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,429,086 | 2,491.625613 | 52910112 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,435,455 | 0.000012 | 52910112 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,407,219 | 0.001670 | 52910112 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 743 | 7,053,098 | 2,487.958444 | 52910112 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 6,580,068 | 0.000012 | 52910112 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,679,691 | 0.029542 | 52910112 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,982,942 | 0.022982 | 52910112 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,579,589 | 2,488.314098 | 52910112 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,440,573 | 0.999950 | 52910112 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,252,089 | 0.000278 | 52910112 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,104,120 | 34,959.981472 | 52910112 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/wstETH | 90 | 3,832,128 | 0.802296 | 52910112 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | WETH/USDT | 436 | 3,668,004 | 2,491.203888 | 52910112 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,395,114 | 2,901.456953 | 52910112 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,278,304 | 1.162945 | 52910112 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,831,787 | 92.626339 | 52910112 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,767,464 | 389.157400 | 52910112 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,303,448 | 0.000010 | 52910112 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,294,514 | 1,196,489.382095 | 52910112 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,284,675 | 0.915907 | 52910112 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,277,736 | 0.000012 | 52910112 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,091,690 | 0.000012 | 52910112 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,030,750 | 1.383527 | 52910112 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,964,121 | 0.000000 | 52910112 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,941,211 | 1.105712 | 52910112 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,899,178 | 15.813013 | 52910112 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,844,860 | 1.142103 | 52910112 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | XDP/USDC | 100 | 1,820,840 | 0.018968 | 52910112 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,752,802 | 13,161.092287 | 52910112 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,717,397 | 2.310834 | 52910112 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,708,545 | 1.493581 | 52910112 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,702,513 | 2,913.866274 | 52910112 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,697 | 0.826661 | 52910112 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 1,432,502 | 1,048.890117 | 52910112 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,427,373 | 1.122252 | 52910112 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | fBOMB/USDC | 10000 | 1,422,259 | 0.019950 | 52910112 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,402,467 | 0.004847 | 52910112 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,377,004 | 0.000000 | 52910112 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,356,325 | 0.000280 | 52910112 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,333,924 | 0.029607 | 52910112 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,295,737 | 2,488.838460 | 52910112 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,279,146 | 23.133103 | 52910112 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,272,930 | 1,038,860.938767 | 52910112 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,245,583 | 40.612716 | 52910112 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/doginme | 10000 | 1,239,248 | 35,399,426.800340 | 52910112 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,233,076 | 63.909097 | 52910112 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,216,514 | 71,805.520529 | 52910112 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,199,913 | 485,112.673500 | 52910112 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,179,237 | 1.106158 | 52910112 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,175,325 | 0.436479 | 52910112 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,151,778 | 0.886185 | 52910112 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,117,416 | 20,921,606.432470 | 52910112 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 7748 ; routes examinées : 167108864 ; candidats optimisés : 873232 ; net attendu > 0 : 207 ; dernier cycle 352.0 ms
- Rejets (moteur) : {'spread_below_threshold': 164787458, 'liquidity_below_min': 1437454, 'negative_expected_net': 873025, 'borrow_bound_too_small': 7736, 'cycle_budget_exhausted': 2984}
- Enregistrements de la session : 873232 ; net attendu > 0 : 207 ; simulés (eth_call de la vraie tx) : 15 (ok 8, échec 7) ; étiquettes ghost N+1 : 0/15 positives
- Décisions : {'REJECTED': 873232} ; motifs de rejet : {'below_safety_margin': 145, 'negative_expected_net': 873025, 'p_lower_below_threshold': 144, 'reliability_not_demonstrated': 63, 'simulation_failed': 7, 'stale_data': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52904867 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 5.290395 WETH | 0.004687 WETH | 0.000000 WETH | 0.000003 WETH | 0.004684 WETH (10.8029 €) | — | 8.85 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 13,257.243552 USDC | 11.747487 USDC | 0.000000 USDC | 0.007596 USDC | 11.739891 USDC (10.8007 €) | — | 8.86 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 4.690550 WETH | 0.004357 WETH | 0.000000 WETH | 0.000004 WETH | 0.004353 WETH (10.0396 €) | — | 9.28 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 11,757.060894 USDC | 10.919145 USDC | 0.000000 USDC | 0.010260 USDC | 10.908885 USDC (10.0362 €) | — | 9.28 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.523217 WETH | 0.003930 WETH | 0.000000 WETH | 0.000003 WETH | 0.003927 WETH (9.0578 €) | — | 8.68 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 11,336.129402 USDC | 9.852500 USDC | 0.000000 USDC | 0.008357 USDC | 9.844143 USDC (9.0566 €) | — | 8.68 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.094311 WETH | 0.003734 WETH | 0.000000 WETH | 0.000004 WETH | 0.003730 WETH (8.6031 €) | — | 9.11 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 10,260.868308 USDC | 9.359500 USDC | 0.000000 USDC | 0.010640 USDC | 9.348860 USDC (8.6010 €) | — | 9.11 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 4.773284 WETH | 0.003527 WETH | 0.000000 WETH | 0.000003 WETH | 0.003524 WETH (8.1278 €) | — | 7.38 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 11,963.205563 USDC | 8.839237 USDC | 0.000000 USDC | 0.007596 USDC | 8.831641 USDC (8.1251 €) | — | 7.38 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.026460 WETH | 0.002904 WETH | 0.000000 WETH | 0.000003 WETH | 0.002900 WETH (6.6900 €) | — | 7.20 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 10,092.039463 USDC | 7.278144 USDC | 0.000000 USDC | 0.008357 USDC | 7.269787 USDC (6.6882 €) | — | 7.20 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 2.498645 WETH | 0.002198 WETH | 0.000000 WETH | 0.000003 WETH | 0.002195 WETH (5.0618 €) | — | 8.78 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 6,257.474670 USDC | 5.505138 USDC | 0.000000 USDC | 0.007976 USDC | 5.497162 USDC (5.0574 €) | — | 8.78 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 2.295257 WETH | 0.001970 WETH | 0.000000 WETH | 0.000003 WETH | 0.001967 WETH (4.5360 €) | — | 8.57 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 5,748.469875 USDC | 4.935009 USDC | 0.000000 USDC | 0.008357 USDC | 4.926652 USDC (4.5325 €) | — | 8.57 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 3,663.050751 USDC | 4.493251 USDC | 0.000000 USDC | 0.010640 USDC | 4.482611 USDC (4.1240 €) | — | 12.24 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.460331 WETH | 0.001792 WETH | 0.000000 WETH | 0.000004 WETH | 0.001787 WETH (4.1229 €) | — | 12.24 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 3,663.050751 USDC | 4.329451 USDC | 0.000000 USDC | 0.009879 USDC | 4.319572 USDC (3.9740 €) | — | 11.79 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.459881 WETH | 0.001726 WETH | 0.000000 WETH | 0.000004 WETH | 0.001722 WETH (3.9721 €) | — | 11.80 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 3,663.050751 USDC | 3.318625 USDC | 0.000000 USDC | 0.009879 USDC | 3.308746 USDC (3.0440 €) | — | 9.03 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.460239 WETH | 0.001323 WETH | 0.000000 WETH | 0.000004 WETH | 0.001320 WETH (3.0435 €) | — | 9.04 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.459884 WETH | 0.001316 WETH | 0.000000 WETH | 0.000004 WETH | 0.001312 WETH (3.0265 €) | — | 8.99 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 3,663.050751 USDC | 3.298919 USDC | 0.000000 USDC | 0.010260 USDC | 3.288659 USDC (3.0256 €) | — | 8.98 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 1.246273 WETH | 0.001113 WETH | 0.000000 WETH | 0.000004 WETH | 0.001109 WETH (2.5578 €) | — | 8.90 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1724 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
