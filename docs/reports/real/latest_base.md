# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T17:38:43+00:00 ; durée 30.44 min ; blocs 54836572 → 54845701 (1277 vus)

## Connexion
- Requêtes RPC : 17858 ; erreurs : 0 ; latence p50/p95 : 409.4/1,826.6 ms
- Rafraîchissements d'état : 1277 ; âge des données au dernier bloc : 7.97 s ; changements de frais LP observés (pools à frais dynamiques) : 637
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1045 ; cycles déclenchés par événement : 477 ; avance médiane sur le rafraîchissement multicall : 526 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 276 jetons, 17556 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 196, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3671 (énumérés 291, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.430141, 'cbBTC': 75744.13603, 'AERO': 0.592088}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,155,411 | 2,229.177701 | 54845702 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,843,993 | 0.029416 | 54845702 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,319,725 | 0.000013 | 54845702 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,143,195 | 0.029477 | 54845702 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,513,047 | 2,224.510083 | 54845702 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,302,279 | 108.883046 | 54845702 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,392,838 | 0.001541 | 54845702 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,141,478 | 0.029418 | 54845702 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,751,067 | 1.703752 | 54845702 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,174,565 | 2,224.513823 | 54845702 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,988,684 | 0.999112 | 54845702 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,272,370 | 43,428.991079 | 54845702 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,166,464 | 2,224.541059 | 54845702 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,461,649 | 0.029461 | 54845702 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,082,444 | 1,161,552.106913 | 54845702 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,737,419 | 0.000013 | 54845702 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,629,530 | 0.006441 | 54845702 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,626,806 | 0.000013 | 54845702 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,616,842 | 0.000000 | 54845702 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,551,885 | 0.015278 | 54845702 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,511,364 | 446.955838 | 54845702 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,044 | 0.000013 | 54845702 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,118 | 1.431449 | 54845702 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,404 | 0.824203 | 54845702 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,365,033 | 3,791.218240 | 54845702 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,243 | 2,229.322122 | 54845702 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,256,239 | 15,171.169242 | 54845702 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,253,980 | 2,230.045267 | 54845702 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,169,680 | 2,224.442971 | 54845702 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54845702 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,091,998 | 37,301,150.846749 | 54845702 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,029,684 | 108.120009 | 54845702 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 994,306 | 605,218.020553 | 54845702 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 978,701 | 23,100,700.027305 | 54845702 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,242 | 21.370973 | 54845702 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 957,761 | 0.000000 | 54845702 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,141 | 2,228.787393 | 54845702 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 925,610 | 0.000013 | 54845702 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 922,153 | 1,080.949567 | 54845702 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 919,092 | 74.180524 | 54845702 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 861,635 | 102,043.282152 | 54845702 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 819,389 | 0.048959 | 54845702 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,045 | 0.055109 | 54845702 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 774,291 | 3,764.163022 | 54845702 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 764,034 | 22.296771 | 54845702 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 756,190 | 0.799805 | 54845702 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,350 | 0.554992 | 54845702 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 677,159 | 5,129,742.979269 | 54845702 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 669,894 | 0.566696 | 54845702 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 646,135 | 150,517.884548 | 54845702 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 644,694 | 0.000008 | 54845702 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 619,986 | 0.000250 | 54845702 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2174 | 600,997 | 609,388.121194 | 54845702 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 573,534 | 0.039201 | 54845702 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 553,160 | 2.471747 | 54845702 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 523,248 | 891,542.099279 | 54845702 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2745 | 521,555 | 1,081.085621 | 54845702 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 514,465 | 2,224.460342 | 54845702 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 511,603 | 6,962.408836 | 54845702 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 508,308 | 0.075030 | 54845702 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 1753 ; routes examinées : 30775668 ; candidats optimisés : 86408 ; net attendu > 0 : 77 ; dernier cycle 267.8 ms
- Rejets (moteur) : {'spread_below_threshold': 30251748, 'liquidity_below_min': 435964, 'negative_expected_net': 86331, 'borrow_bound_too_small': 1340, 'cycle_budget_exhausted': 208}
- Enregistrements de la session : 86408 ; net attendu > 0 : 77 ; simulés (eth_call de la vraie tx) : 9 (ok 6, échec 3) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 86408} ; motifs de rejet : {'below_safety_margin': 67, 'negative_expected_net': 86331, 'p_lower_below_threshold': 71, 'reliability_not_demonstrated': 6, 'simulation_failed': 3, 'stale_data': 13}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54842272 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001153 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0258 €) | 0.000000 cbBTC | 3.21 | 0.153 (n=850) | REJECTED | stale_data(4330ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 54842272 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.043415 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | 0.000012 WETH | 2.86 | 0.181 (n=1080) | REJECTED | stale_data(4322ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54837017 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000872 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0174 €) | 0.000000 cbBTC | 2.87 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54837017 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.030050 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | 0.000008 WETH | 2.76 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54837017 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000804 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0167 €) | — | 2.98 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54837017 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.030714 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0163 €) | 0.000008 WETH | 2.58 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54842272 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.026501 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0106 €) | — | 1.94 | 0.181 (n=1080) | REJECTED | below_safety_margin(5144842696324<5300101825992), stale_data(4337ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54842272 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000634 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | 0.000000 cbBTC | 2.36 | 0.181 (n=1080) | REJECTED | stale_data(4345ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54842272 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001289 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0105 €) | — | 1.16 | 0.242 (n=420) | REJECTED | below_safety_margin(15<25), stale_data(4352ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 54842272 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 107.915524 USDC | 0.017850 USDC | 0.000000 USDC | 0.006704 USDC | 0.011146 USDC (0.0103 €) | — | 1.03 | 0.242 (n=420) | REJECTED | below_safety_margin(11146<21583), stale_data(4360ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 54842272 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001158 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0098 €) | — | 1.21 | 0.181 (n=1080) | REJECTED | below_safety_margin(14<23), stale_data(4367ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54842272 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 104.517103 USDC | 0.016988 USDC | 0.000000 USDC | 0.006704 USDC | 0.010284 USDC (0.0095 €) | — | 0.98 | 0.181 (n=1080) | REJECTED | below_safety_margin(10284<20903), stale_data(4376ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54842272 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001232 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0091 €) | — | 1.06 | 0.242 (n=420) | REJECTED | below_safety_margin(13<24), stale_data(4390ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 54842272 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 88.724376 USDC | 0.015861 USDC | 0.000000 USDC | 0.006704 USDC | 0.009157 USDC (0.0084 €) | — | 1.03 | 0.242 (n=420) | REJECTED | below_safety_margin(9157<17744), stale_data(4383ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 54838078 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.857327 USDC | 0.011384 USDC | 0.000000 USDC | 0.005012 USDC | 0.006372 USDC (0.0059 €) | — | 3.21 | 0.036 (n=389) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 54838079 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.857327 USDC | 0.011384 USDC | 0.000000 USDC | 0.005012 USDC | 0.006372 USDC (0.0059 €) | — | 3.21 | 0.036 (n=389) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 54840170 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 18.242781 USDC | 0.009783 USDC | 0.000000 USDC | 0.005011 USDC | 0.004772 USDC (0.0044 €) | — | 2.62 | 0.051 (n=280) | REJECTED | stale_data(4646ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54845668 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.021001 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0031 €) | — | 0.71 | 0.181 (n=1082) | REJECTED | below_safety_margin(1487872746619<4200285533306), p_lower_below_threshold(0.18<0.75) |
| 54845669 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.021001 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0031 €) | — | 0.71 | 0.181 (n=1082) | REJECTED | below_safety_margin(1487872746619<4200285533306), p_lower_below_threshold(0.18<0.75) |
| 54845669 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.021001 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0031 €) | — | 0.71 | 0.181 (n=1082) | REJECTED | below_safety_margin(1487872746619<4200285533306), p_lower_below_threshold(0.18<0.75) |
| 54845669 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.021001 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0031 €) | — | 0.71 | 0.181 (n=1082) | REJECTED | below_safety_margin(1487872746619<4200285533306), p_lower_below_threshold(0.18<0.75) |
| 54845668 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 46.796614 USDC | 0.009998 USDC | 0.000000 USDC | 0.006702 USDC | 0.003296 USDC (0.0030 €) | — | 0.70 | 0.181 (n=1082) | REJECTED | below_safety_margin(3296<9359), p_lower_below_threshold(0.18<0.75) |
| 54845669 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 46.796614 USDC | 0.009998 USDC | 0.000000 USDC | 0.006702 USDC | 0.003296 USDC (0.0030 €) | — | 0.70 | 0.181 (n=1082) | REJECTED | below_safety_margin(3296<9359), p_lower_below_threshold(0.18<0.75) |
| 54845669 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 46.796614 USDC | 0.009998 USDC | 0.000000 USDC | 0.006702 USDC | 0.003296 USDC (0.0030 €) | — | 0.70 | 0.181 (n=1082) | REJECTED | below_safety_margin(3296<9359), p_lower_below_threshold(0.18<0.75) |
| 54845669 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 46.796614 USDC | 0.009998 USDC | 0.000000 USDC | 0.006702 USDC | 0.003296 USDC (0.0030 €) | — | 0.70 | 0.181 (n=1082) | REJECTED | below_safety_margin(3296<9359), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 6244 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
