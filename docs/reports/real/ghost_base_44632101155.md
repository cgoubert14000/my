# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T02:03:44+00:00 ; durée 186.14 min ; blocs 59693368 → 59749205 (9173 vus)

## Connexion
- Requêtes RPC : 110926 ; erreurs : 0 ; latence p50/p95 : 425.1/1,359.1 ms
- Rafraîchissements d'état : 9173 ; âge des données au dernier bloc : 8.45 s ; changements de frais LP observés (pools à frais dynamiques) : 7703
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16978 ; cycles déclenchés par événement : 4954 ; avance médiane sur le rafraîchissement multicall : 424 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,734.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 425 pools, 247 jetons, 12948 routes
- Par DEX : uniswap_v3 129, aerodrome 171, aerodrome_slipstream 86, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 145 (rejetés 2) → 550 jetons ; pools candidats 3571 (énumérés 255, par paires 0), mesurés 427, sous le plancher de 10000.0 $ : 2 → gardés 425 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1759.475588, 'cbBTC': 62145.383052, 'AERO': 0.418705}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 84,609,163 | 1,734.661569 | 59749234 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 25,359,762 | 1,734.928631 | 59749234 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,011,886 | 0.028198 | 59749234 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,608,174 | 0.028191 | 59749234 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,513,344 | 82.367866 | 59749234 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,979,933 | 0.000016 | 59749234 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,115,418 | 0.028208 | 59749234 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,558,232 | 2.431156 | 59749234 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 206 | 3,238,073 | 0.999465 | 59749234 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,235,459 | 1,735.647370 | 59749234 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,697,910 | 38,688.399807 | 59749234 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 162 | 2,276,590 | 1,735.551060 | 59749234 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,051,363 | 0.000016 | 59749234 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,693,157 | 0.028187 | 59749234 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,630,209 | 1,147,728.379701 | 59749234 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,907 | 0.844466 | 59749234 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,376,330 | 0.000016 | 59749234 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,320,017 | 0.000000 | 59749234 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,239,917 | 0.006524 | 59749234 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,235,058 | 0.000016 | 59749234 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,083,468 | 15.272591 | 59749234 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,060,053 | 86.473728 | 59749234 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,033,619 | 451.700338 | 59749234 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 998,703 | 16,026.317033 | 59749234 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 997,785 | 82.379999 | 59749234 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 980,300 | 1,734.905282 | 59749234 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 976,402 | 4,212.066596 | 59749234 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 954,210 | 1,735.516314 | 59749234 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 914,511 | 30,665,215.469460 | 59749234 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 889,978 | 0.047510 | 59749234 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 843,586 | 60.121070 | 59749234 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 811,681 | 523,897.252088 | 59749234 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 789,070 | 0.000000 | 59749234 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 781,710 | 22,197,854.400916 | 59749234 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 776,286 | 0.001533 | 59749234 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 730,692 | 1,074.673719 | 59749234 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | XDP/USDC | 100 | 729,127 | 0.014893 | 59749234 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 720,092 | 24.355253 | 59749234 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 719,623 | 0.046020 | 59749234 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| pancakeswap_v3 | WETH/USDC | 500 | 719,388 | 1,734.801480 | 59749234 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 10000 | 692,034 | 1,739.551825 | 59749234 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | TIG/USDC | 10000 | 589,138 | 0.436229 | 59749234 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 588,793 | 0.798842 | 59749234 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 588,051 | 1,735.528675 | 59749234 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 550,971 | 4,716,098.618114 | 59749234 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 534,464 | 4,203.495683 | 59749234 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 509,122 | 1.386517 | 59749234 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3736 | 505,654 | 526,584.664066 | 59749234 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 494,320 | 0.031284 | 59749234 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 474,665 | 169,848.758815 | 59749234 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 11 | 456,638 | 1.001444 | 59749234 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 436,480 | 0.000007 | 59749234 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 404,125 | 0.056287 | 59749234 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3052 | 397,945 | 1,074.617336 | 59749234 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/UNI | 10000 | 382,175 | 356.110552 | 59749234 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 381,316 | 23.779881 | 59749234 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 379,617 | 845,002.327871 | 59749234 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 366,966 | 0.055996 | 59749234 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 361,677 | 0.000238 | 59749234 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2748 | 359,488 | 82.355356 | 59749234 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 14126 ; routes examinées : 182903448 ; candidats optimisés : 225043 ; net attendu > 0 : 109 ; dernier cycle 350.9 ms
- Rejets (moteur) : {'spread_below_threshold': 179474946, 'liquidity_below_min': 2146387, 'negative_expected_net': 224934, 'borrow_bound_too_small': 17168, 'cycle_budget_exhausted': 836}
- Enregistrements de la session : 62793 ; net attendu > 0 : 109 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 6/6 positives
- Décisions : {'REJECTED': 62793} ; motifs de rejet : {'below_safety_margin': 71, 'negative_expected_net': 62684, 'p_lower_below_threshold': 109, 'price_impact': 36, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59732431 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 69.931296 USDC | 0.030186 USDC | 0.000000 USDC | 0.005521 USDC | 0.024665 USDC (0.0227 €) | — | 3.53 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.039909 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0226 €) | 0.000014 WETH | 3.50 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59732431 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 66.903932 USDC | 0.027131 USDC | 0.000000 USDC | 0.005521 USDC | 0.021610 USDC (0.0199 €) | — | 3.23 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59732431 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.038074 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0198 €) | 0.000011 WETH | 3.21 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59746276 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.055155 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0180 €) | 0.000011 WETH | 2.04 | 0.281 (n=245) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 95.748973 USDC | 0.024811 USDC | 0.000000 USDC | 0.005271 USDC | 0.019540 USDC (0.0180 €) | — | 2.04 | 0.281 (n=245) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59746276 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.083431 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0178 €) | — | 1.33 | 0.281 (n=245) | REJECTED | below_safety_margin(11102813876630<16686108641199), p_lower_below_threshold(0.28<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 144.300977 USDC | 0.024810 USDC | 0.000000 USDC | 0.005550 USDC | 0.019260 USDC (0.0177 €) | — | 1.33 | 0.281 (n=245) | REJECTED | below_safety_margin(19260<28860), p_lower_below_threshold(0.28<0.75) |
| 59732431 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 37.378666 USDC | 0.018956 USDC | 0.000000 USDC | 0.005268 USDC | 0.013688 USDC (0.0126 €) | — | 3.66 | 0.184 (n=331) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.021338 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0125 €) | 0.000008 WETH | 3.63 | 0.184 (n=331) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 59732431 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.829297 USDC | 0.017145 USDC | 0.000000 USDC | 0.005268 USDC | 0.011877 USDC (0.0109 €) | — | 3.31 | 0.305 (n=236) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 59732431 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.020353 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0109 €) | — | 3.30 | 0.305 (n=236) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 59732431 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 25.472668 USDC | 0.015949 USDC | 0.000000 USDC | 0.005521 USDC | 0.010428 USDC (0.0096 €) | — | 4.09 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.014361 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0096 €) | — | 4.11 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59746276 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.024440 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0086 €) | 0.000005 WETH | 2.19 | 0.355 (n=643) | REJECTED | p_lower_below_threshold(0.36<0.75) |
| 59732431 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 24.353050 USDC | 0.014808 USDC | 0.000000 USDC | 0.005521 USDC | 0.009287 USDC (0.0085 €) | — | 3.81 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59746276 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.030615 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0085 €) | — | 1.74 | 0.363 (n=155) | REJECTED | below_safety_margin(5332004153913<6123076512000), p_lower_below_threshold(0.36<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 42.248714 USDC | 0.014796 USDC | 0.000000 USDC | 0.005525 USDC | 0.009271 USDC (0.0085 €) | — | 2.19 | 0.355 (n=643) | REJECTED | p_lower_below_threshold(0.36<0.75) |
| 59732431 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 24.305317 USDC | 0.014772 USDC | 0.000000 USDC | 0.005521 USDC | 0.009251 USDC (0.0085 €) | — | 3.81 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.013785 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0085 €) | — | 3.81 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 52.979752 USDC | 0.014514 USDC | 0.000000 USDC | 0.005271 USDC | 0.009243 USDC (0.0085 €) | — | 1.74 | 0.363 (n=155) | REJECTED | below_safety_margin(9243<10595), p_lower_below_threshold(0.36<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.013823 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0085 €) | — | 3.78 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59732431 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 24.341547 USDC | 0.014675 USDC | 0.000000 USDC | 0.005521 USDC | 0.009154 USDC (0.0084 €) | — | 3.76 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59732431 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.013893 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0084 €) | — | 3.73 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59732431 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 23.445784 USDC | 0.013578 USDC | 0.000000 USDC | 0.005521 USDC | 0.008057 USDC (0.0074 €) | — | 3.44 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |

## Fiabilité et décision
- Observations ghost : 8588 ; taux observé 0.228 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
