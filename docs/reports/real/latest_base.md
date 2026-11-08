# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T17:32:38+00:00 ; durée 24.34 min ; blocs 54836572 → 54843861 (1009 vus)

## Connexion
- Requêtes RPC : 14185 ; erreurs : 0 ; latence p50/p95 : 442.2/1,862.0 ms
- Rafraîchissements d'état : 1009 ; âge des données au dernier bloc : 10.38 s ; changements de frais LP observés (pools à frais dynamiques) : 524
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 859 ; cycles déclenchés par événement : 377 ; avance médiane sur le rafraîchissement multicall : 538 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 276 jetons, 17556 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 196, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3671 (énumérés 291, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.430141, 'cbBTC': 75744.13603, 'AERO': 0.592088}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,153,240 | 2,229.178616 | 54843890 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,843,996 | 0.029416 | 54843890 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,319,727 | 0.000013 | 54843890 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,143,199 | 0.029477 | 54843890 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,513,064 | 2,223.635077 | 54843890 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,303,888 | 108.835157 | 54843890 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,392,895 | 0.001541 | 54843890 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,141,476 | 0.029407 | 54843890 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,751,067 | 1.703752 | 54843890 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,174,584 | 2,222.996216 | 54843890 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,988,703 | 0.999097 | 54843890 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,271,377 | 43,455.390224 | 54843890 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,166,468 | 2,223.020366 | 54843890 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,461,650 | 0.029461 | 54843890 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,082,445 | 1,161,552.106913 | 54843890 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,737,419 | 0.000013 | 54843890 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,628,172 | 0.006434 | 54843890 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,626,809 | 0.000013 | 54843890 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,616,714 | 0.000000 | 54843890 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,549,453 | 0.015284 | 54843890 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,511,364 | 446.955804 | 54843890 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,045 | 0.000013 | 54843890 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,118 | 1.431449 | 54843890 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,404 | 0.824203 | 54843890 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,365,033 | 3,791.218240 | 54843890 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,244 | 2,229.322029 | 54843890 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,256,239 | 15,167.372303 | 54843890 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,253,981 | 2,229.338629 | 54843890 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,169,683 | 2,223.696600 | 54843890 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54843890 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,091,998 | 37,301,150.846749 | 54843890 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,029,998 | 108.093320 | 54843890 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 994,307 | 605,216.735223 | 54843890 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 978,702 | 23,100,700.027305 | 54843890 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,350 | 21.295527 | 54843890 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 957,760 | 0.000000 | 54843890 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,142 | 2,228.787393 | 54843890 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 925,610 | 0.000013 | 54843890 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 924,222 | 1,077.816992 | 54843890 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 919,092 | 74.180524 | 54843890 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 861,635 | 102,043.282152 | 54843890 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 819,680 | 0.048937 | 54843890 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,045 | 0.055109 | 54843890 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 774,291 | 3,764.163022 | 54843890 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 764,367 | 22.283161 | 54843890 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 756,190 | 0.799805 | 54843890 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,350 | 0.554992 | 54843890 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 678,786 | 5,105,094.757201 | 54843890 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 669,894 | 0.566696 | 54843890 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 646,133 | 150,501.562552 | 54843890 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 644,683 | 0.000008 | 54843890 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 619,986 | 0.000250 | 54843890 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 600,993 | 605,836.719917 | 54843890 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 572,787 | 0.039122 | 54843890 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 553,160 | 2.471747 | 54843890 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 523,014 | 891,911.172531 | 54843890 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 522,866 | 1,078.083265 | 54843890 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 514,466 | 2,222.973553 | 54843890 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 510,232 | 6,999.869975 | 54843890 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 509,153 | 0.075194 | 54843890 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 1385 ; routes examinées : 24315060 ; candidats optimisés : 70997 ; net attendu > 0 : 29 ; dernier cycle 307.6 ms
- Rejets (moteur) : {'spread_below_threshold': 23891092, 'liquidity_below_min': 352768, 'negative_expected_net': 70968, 'cycle_budget_exhausted': 203}
- Enregistrements de la session : 70997 ; net attendu > 0 : 29 ; simulés (eth_call de la vraie tx) : 9 (ok 6, échec 3) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 70997} ; motifs de rejet : {'below_safety_margin': 19, 'negative_expected_net': 70968, 'p_lower_below_threshold': 23, 'reliability_not_demonstrated': 6, 'simulation_failed': 3, 'stale_data': 13}

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
| 54837867 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003064 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.13 | 0.029 (n=28) | REJECTED | below_safety_margin(4<61), reliability_not_demonstrated |
| 54837867 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003064 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.13 | 0.029 (n=28) | REJECTED | below_safety_margin(4<61), reliability_not_demonstrated |
| 54842272 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000849 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.47 | 0.242 (n=420) | REJECTED | below_safety_margin(4<16), stale_data(4405ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 54842272 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 69.191952 USDC | 0.009419 USDC | 0.000000 USDC | 0.006704 USDC | 0.002715 USDC (0.0025 €) | — | 0.39 | 0.242 (n=420) | REJECTED | below_safety_margin(2715<13838), stale_data(4398ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 54837867 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 332.539448 USDC | 0.009375 USDC | 0.000000 USDC | 0.006706 USDC | 0.002669 USDC (0.0025 €) | — | 0.08 | 0.029 (n=28) | REJECTED | below_safety_margin(2669<66507), reliability_not_demonstrated |
| 54837867 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 332.539448 USDC | 0.009375 USDC | 0.000000 USDC | 0.006706 USDC | 0.002669 USDC (0.0025 €) | — | 0.08 | 0.029 (n=28) | REJECTED | below_safety_margin(2669<66507), reliability_not_demonstrated |
| 54837867 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.134440 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.09 | 0.029 (n=28) | REJECTED | below_safety_margin(1154281752379<26888078288877), reliability_not_demonstrated |
| 54837867 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.134440 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.09 | 0.029 (n=28) | REJECTED | below_safety_margin(1154281752379<26888078288877), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 6244 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
