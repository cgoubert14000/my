# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T22:06:12+00:00 ; durée 297.92 min ; blocs 54836572 → 54925882 (12250 vus)

## Connexion
- Requêtes RPC : 168115 ; erreurs : 15 ; latence p50/p95 : 544.9/1,845.3 ms
- Rafraîchissements d'état : 12250 ; âge des données au dernier bloc : 14.31 s ; changements de frais LP observés (pools à frais dynamiques) : 5635
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3502 ; cycles déclenchés par événement : 1686 ; avance médiane sur le rafraîchissement multicall : 480 ms
- Gaz : base fee 0.029196 gwei ; prix ETH (pool le plus profond) : 2,161.88 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 276 jetons, 17556 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 196, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3671 (énumérés 291, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.430141, 'cbBTC': 75744.13603, 'AERO': 0.592088}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,806,762 | 2,161.785355 | 54925927 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,408,020 | 0.029174 | 54925927 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,885,725 | 0.029248 | 54925927 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,772,022 | 0.000014 | 54925927 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,303,484 | 2,156.095854 | 54925927 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,120,380 | 107.707537 | 54925927 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,231,913 | 0.001530 | 54925927 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,986,938 | 0.029163 | 54925927 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,595,840 | 1.752900 | 54925927 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,048,203 | 2,155.729152 | 54925927 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 3,901,067 | 0.998887 | 54925927 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,205,088 | 42,579.426993 | 54925927 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 1071 | 3,086,451 | 2,155.391797 | 54925927 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2620 | 2,395,990 | 0.029236 | 54925927 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,022,502 | 1,158,197.335472 | 54925927 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,699,240 | 0.000014 | 54925927 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,600,254 | 0.000014 | 54925927 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,579,255 | 0.000000 | 54925927 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,554,102 | 0.006310 | 54925927 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,525,666 | 0.014967 | 54925927 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,470,607 | 442.515332 | 54925927 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,117 | 1.431451 | 54925927 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,014 | 0.823568 | 54925927 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,450,389 | 0.000014 | 54925927 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,326,068 | 3,780.156999 | 54925927 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,303,355 | 2,150.350599 | 54925927 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,234,908 | 2,161.097415 | 54925927 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,229,505 | 15,234.339863 | 54925927 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,141,452 | 2,155.633912 | 54925927 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,761 | 77.084041 | 54925927 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,063,879 | 36,781,065.796708 | 54925927 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,007,985 | 108.072270 | 54925927 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 962,336 | 608,968.272255 | 54925927 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 953,438 | 22,934,430.965975 | 54925927 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 946,793 | 22.328972 | 54925927 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 932,880 | 0.000000 | 54925927 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 921,872 | 2,176.177307 | 54925927 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 910,932 | 75.515442 | 54925927 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 908,088 | 0.000014 | 54925927 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 901,759 | 1,069.875543 | 54925927 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 834,739 | 102,259.810442 | 54925927 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 802,686 | 0.049909 | 54925927 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 778,881 | 0.054208 | 54925927 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 751,743 | 3,805.850785 | 54925927 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4710 | 743,042 | 23.179901 | 54925927 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 732,656 | 0.801347 | 54925927 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 684,931 | 0.538773 | 54925927 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 665,535 | 0.559644 | 54925927 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 655,332 | 5,150,893.331815 | 54925927 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 629,138 | 149,341.512555 | 54925927 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 628,092 | 0.000008 | 54925927 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 598,082 | 0.000248 | 54925927 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2309 | 581,019 | 603,837.231209 | 54925927 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,553 | 0.038535 | 54925927 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 536,471 | 2.463619 | 54925927 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 514,130 | 881,412.899473 | 54925927 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2748 | 510,576 | 1,069.844745 | 54925927 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 505,018 | 0.074346 | 54925927 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 501,618 | 2,155.861640 | 54925927 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 496,440 | 6,954.521650 | 54925927 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 13935 ; routes examinées : 244642860 ; candidats optimisés : 741573 ; net attendu > 0 : 3272 ; dernier cycle 1200.1 ms
- Rejets (moteur) : {'spread_below_threshold': 240109554, 'liquidity_below_min': 3728593, 'negative_expected_net': 738301, 'borrow_bound_too_small': 31215, 'cycle_budget_exhausted': 27973, 'pool_quarantined': 3952}
- Enregistrements de la session : 741573 ; net attendu > 0 : 3272 ; simulés (eth_call de la vraie tx) : 158 (ok 87, échec 71) ; étiquettes ghost N+1 : 42/138 positives
- Décisions : {'REJECTED': 741573} ; motifs de rejet : {'below_safety_margin': 1025, 'negative_expected_net': 738301, 'p_lower_below_threshold': 3101, 'price_impact': 16, 'reliability_not_demonstrated': 171, 'sim_below_estimate': 13, 'simulated_net_nonpositive': 4, 'simulation_failed': 71, 'stale_data': 1300}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54921444 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.167170 WETH | 0.000280 WETH | 0.000000 WETH | 0.000003 WETH | 0.000277 WETH (0.5623 €) | 0.000078 WETH | 16.56 | 0.077 (n=164) | REJECTED | sim_below_estimate(80808336744466<279894877184788), p_lower_below_threshold(0.08<0.75) |
| 54921444 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 367.671012 USDC | 0.616284 USDC | 0.000000 USDC | 0.006719 USDC | 0.609565 USDC (0.5608 €) | — | 16.58 | 0.077 (n=164) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54921444 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.158046 WETH | 0.000264 WETH | 0.000000 WETH | 0.000003 WETH | 0.000261 WETH (0.5303 €) | 0.000073 WETH | 16.52 | 0.077 (n=164) | REJECTED | sim_below_estimate(75906267212778<264131406002443), p_lower_below_threshold(0.08<0.75) |
| 54921444 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 348.145611 USDC | 0.581574 USDC | 0.000000 USDC | 0.006719 USDC | 0.574855 USDC (0.5289 €) | — | 16.51 | 0.077 (n=164) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54922779 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.127818 WETH | 0.000267 WETH | 0.000000 WETH | 0.000006 WETH | 0.000261 WETH (0.5225 €) | — | 20.41 | 0.016 (n=52) | REJECTED | stale_data(5836ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 54922779 | USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 277.401956 USDC | 0.580027 USDC | 0.000000 USDC | 0.013171 USDC | 0.566856 USDC (0.5215 €) | — | 20.43 | 0.016 (n=52) | REJECTED | stale_data(5843ms>4000.0), p_lower_below_threshold(0.02<0.75) |
| 54921444 | WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.157289 WETH | 0.000254 WETH | 0.000000 WETH | 0.000003 WETH | 0.000251 WETH (0.5098 €) | 0.000064 WETH | 15.96 | 0.077 (n=164) | REJECTED | sim_below_estimate(66734972486626<254048783930936), p_lower_below_threshold(0.08<0.75) |
| 54921444 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC | 346.383794 USDC | 0.559374 USDC | 0.000000 USDC | 0.006719 USDC | 0.552655 USDC (0.5084 €) | — | 15.95 | 0.077 (n=164) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54922779 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.117067 WETH | 0.000246 WETH | 0.000000 WETH | 0.000006 WETH | 0.000240 WETH (0.4808 €) | — | 20.51 | 0.000 (n=61) | REJECTED | stale_data(5823ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54922779 | USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 254.082880 USDC | 0.534639 USDC | 0.000000 USDC | 0.013171 USDC | 0.521468 USDC (0.4798 €) | — | 20.52 | 0.000 (n=61) | REJECTED | stale_data(5829ms>4000.0), p_lower_below_threshold(0.00<0.75) |
| 54922779 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH | 0.122425 WETH | 0.000243 WETH | 0.000000 WETH | 0.000006 WETH | 0.000237 WETH (0.4740 €) | — | 19.33 | 0.027 (n=104) | REJECTED | stale_data(5878ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54922779 | USDC→[uniswap_v3]→AAVE→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 265.653270 USDC | 0.527282 USDC | 0.000000 USDC | 0.013171 USDC | 0.514111 USDC (0.4730 €) | — | 19.35 | 0.027 (n=104) | REJECTED | stale_data(5885ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 54922848 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.136164 WETH | 0.000218 WETH | 0.000000 WETH | 0.000001 WETH | 0.000218 WETH (0.4356 €) | — | 15.98 | 0.127 (n=176) | REJECTED | stale_data(4736ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 54922848 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 295.558123 USDC | 0.473365 USDC | 0.000000 USDC | 0.001102 USDC | 0.472263 USDC (0.4345 €) | — | 15.98 | 0.127 (n=176) | REJECTED | stale_data(4743ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.020353 WETH | 0.000213 WETH | 0.000000 WETH | 0.000003 WETH | 0.000210 WETH (0.4303 €) | — | 103.09 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54846483 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 45.336647 USDC | 0.473745 USDC | 0.000000 USDC | 0.006396 USDC | 0.467349 USDC (0.4300 €) | — | 103.08 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.020201 WETH | 0.000212 WETH | 0.000000 WETH | 0.000003 WETH | 0.000210 WETH (0.4299 €) | — | 103.77 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54846483 | USDC→[uniswap_v3]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 44.998596 USDC | 0.473353 USDC | 0.000000 USDC | 0.006396 USDC | 0.466957 USDC (0.4296 €) | — | 103.77 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54846483 | WETH→[aerodrome]→SLC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.019755 WETH | 0.000209 WETH | 0.000000 WETH | 0.000003 WETH | 0.000206 WETH (0.4222 €) | — | 104.20 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54846483 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→SLC→[uniswap_v3]→USDC | 44.004281 USDC | 0.464900 USDC | 0.000000 USDC | 0.006396 USDC | 0.458504 USDC (0.4218 €) | — | 104.20 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 54922848 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.124362 WETH | 0.000207 WETH | 0.000000 WETH | 0.000001 WETH | 0.000206 WETH (0.4124 €) | — | 16.56 | 0.027 (n=106) | REJECTED | stale_data(4722ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54922848 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 269.973645 USDC | 0.448341 USDC | 0.000000 USDC | 0.001102 USDC | 0.447239 USDC (0.4115 €) | — | 16.57 | 0.027 (n=106) | REJECTED | stale_data(4729ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 54922722 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002844 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4068 €) | — | 20.81 | 0.016 (n=52) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54922722 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 212.077660 USDC | 0.452636 USDC | 0.000000 USDC | 0.011975 USDC | 0.440661 USDC (0.4054 €) | — | 20.78 | 0.016 (n=52) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 54922722 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002854 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4033 €) | — | 20.57 | 0.016 (n=52) | REJECTED | p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 6374 ; taux observé 0.164 ; borne inférieure crédible (0.9) 0.158 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
