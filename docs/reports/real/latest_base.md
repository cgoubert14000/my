# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T23:24:11+00:00 ; durée 39.7 min ; blocs 54937445 → 54949344 (2512 vus)

## Connexion
- Requêtes RPC : 31856 ; erreurs : 193 ; latence p50/p95 : 247.6/968.0 ms
- Rafraîchissements d'état : 2512 ; âge des données au dernier bloc : 6.44 s ; changements de frais LP observés (pools à frais dynamiques) : 2699
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2646 ; cycles déclenchés par événement : 627 ; avance médiane sur le rafraîchissement multicall : 341 ms
- Gaz : base fee 0.005010 gwei ; prix ETH (pool le plus profond) : 2,159.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 466 pools, 272 jetons, 17666 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 289, par paires 0), mesurés 468, sous le plancher de 10000.0 $ : 2 → gardés 466 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2120.787264, 'cbBTC': 74286.143616, 'AERO': 0.573915}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 140,295,511 | 2,159.418321 | 54949363 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,581,179 | 0.028624 | 54949363 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,023,099 | 0.000013 | 54949363 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,919,223 | 0.028649 | 54949363 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,379,383 | 2,159.474516 | 54949363 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,181,832 | 105.630478 | 54949363 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,333,286 | 0.001526 | 54949363 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,999,671 | 0.028625 | 54949363 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,650,410 | 1.712431 | 54949363 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,970,610 | 0.999264 | 54949363 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,961,522 | 2,159.398794 | 54949363 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,202,749 | 42,544.458646 | 54949363 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,074,402 | 2,159.616598 | 54949363 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,404,338 | 0.028641 | 54949363 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,020,196 | 1,158,197.335472 | 54949363 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,721,863 | 0.000013 | 54949363 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,620,902 | 0.000013 | 54949363 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,578,364 | 0.000000 | 54949363 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,573,229 | 0.006411 | 54949363 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,531,885 | 0.015050 | 54949363 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,473,697 | 437.902980 | 54949363 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,117 | 1.431451 | 54949363 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,417,423 | 0.000013 | 54949363 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,344,999 | 3,705.020083 | 54949363 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,302,603 | 2,159.721237 | 54949363 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,247,015 | 15,316.100957 | 54949363 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,231,688 | 2,160.239633 | 54949363 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,122,761 | 77.084041 | 54949363 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,112,214 | 2,160.103832 | 54949363 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,061,774 | 36,877,720.446607 | 54949363 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,020,570 | 106.374529 | 54949363 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 967,406 | 597,288.486572 | 54949363 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 955,887 | 22,792,180.475676 | 54949363 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 951,990 | 21.949273 | 54949363 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 934,303 | 0.000013 | 54949363 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 918,432 | 0.000000 | 54949363 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 917,736 | 2,144.554936 | 54949363 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 909,063 | 75.826312 | 54949363 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 905,965 | 1,061.636167 | 54949363 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 855,293 | 0.824191 | 54949363 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/EDEL | 7000 | 836,668 | 101,556.866822 | 54949363 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 814,829 | 0.048847 | 54949363 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 778,629 | 0.054171 | 54949363 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 760,236 | 3,716.942490 | 54949363 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 748,169 | 22.961115 | 54949363 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 731,821 | 0.801347 | 54949363 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 709,149 | 0.543839 | 54949363 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 657,239 | 5,109,520.913420 | 54949363 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 638,697 | 0.516996 | 54949363 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 633,420 | 0.000008 | 54949363 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 626,759 | 150,139.165389 | 54949363 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 600,689 | 0.000250 | 54949363 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 586,287 | 592,584.158775 | 54949363 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 570,820 | 0.038905 | 54949363 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 535,844 | 2.463661 | 54949363 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 517,627 | 897,857.854590 | 54949363 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 513,434 | 1,061.378607 | 54949363 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 504,052 | 0.074178 | 54949363 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 498,369 | 2,159.505068 | 54949363 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 495,096 | 6,976.383831 | 54949363 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 3138 ; routes examinées : 55435908 ; candidats optimisés : 198005 ; net attendu > 0 : 1822 ; dernier cycle 219.4 ms
- Rejets (moteur) : {'spread_below_threshold': 54370158, 'liquidity_below_min': 863315, 'negative_expected_net': 196183, 'borrow_bound_too_small': 3136, 'cycle_budget_exhausted': 1294}
- Enregistrements de la session : 198005 ; net attendu > 0 : 1822 ; simulés (eth_call de la vraie tx) : 84 (ok 54, échec 30) ; étiquettes ghost N+1 : 31/70 positives
- Décisions : {'REJECTED': 198005} ; motifs de rejet : {'below_safety_margin': 1527, 'negative_expected_net': 196183, 'p_lower_below_threshold': 1653, 'price_impact': 8, 'reliability_not_demonstrated': 169, 'sim_below_estimate': 6, 'simulation_failed': 30, 'stale_data': 49}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 369.838495 USDC | 0.450524 USDC | 0.000000 USDC | 0.007098 USDC | 0.443426 USDC (0.4080 €) | — | 11.99 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54937865 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004758 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4075 €) | — | 12.55 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 328.781193 USDC | 0.334209 USDC | 0.000000 USDC | 0.006775 USDC | 0.327434 USDC (0.3012 €) | — | 9.96 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.004323 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3010 €) | — | 10.20 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 299.072510 USDC | 0.279400 USDC | 0.000000 USDC | 0.006775 USDC | 0.272625 USDC (0.2508 €) | — | 9.12 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003892 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2505 €) | — | 9.43 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 280.437346 USDC | 0.268901 USDC | 0.000000 USDC | 0.006775 USDC | 0.262126 USDC (0.2412 €) | — | 9.35 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003718 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2409 €) | — | 9.49 | 0.031 (n=113) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54937865 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 188.044557 USDC | 0.207211 USDC | 0.000000 USDC | 0.006775 USDC | 0.200436 USDC (0.1844 €) | — | 10.66 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54937865 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002435 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1843 €) | — | 11.09 | 0.129 (n=193) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 54947007 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 891.154081 USDC | 0.165334 USDC | 0.000000 USDC | 0.007804 USDC | 0.157530 USDC (0.1449 €) | — | 1.77 | 0.050 (n=29) | REJECTED | below_safety_margin(157530<178230), reliability_not_demonstrated |
| 54947007 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.429219 WETH | 0.000076 WETH | 0.000000 WETH | 0.000004 WETH | 0.000073 WETH (0.1446 €) | — | 1.70 | 0.050 (n=29) | REJECTED | below_safety_margin(72797280237157<85843751261817), reliability_not_demonstrated |
| 54947007 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011357 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1443 €) | — | 1.83 | 0.050 (n=29) | REJECTED | below_safety_margin(208<227), reliability_not_demonstrated |
| 54938313 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 44.749652 USDC | 0.160879 USDC | 0.000000 USDC | 0.006461 USDC | 0.154418 USDC (0.1421 €) | — | 34.51 | 0.041 (n=20) | REJECTED | reliability_not_demonstrated |
| 54938313 | USDC→[uniswap_v3]→AERO→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 44.481462 USDC | 0.158749 USDC | 0.000000 USDC | 0.006461 USDC | 0.152288 USDC (0.1401 €) | — | 34.24 | 0.041 (n=20) | REJECTED | reliability_not_demonstrated |
| 54938313 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.020985 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1350 €) | — | 32.96 | 0.041 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54938313 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.020985 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1350 €) | 0.000069 WETH | 32.96 | 0.041 (n=20) | REJECTED | reliability_not_demonstrated |
| 54938313 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.020098 WETH | 0.000066 WETH | 0.000000 WETH | 0.000003 WETH | 0.000063 WETH (0.1236 €) | — | 31.52 | 0.041 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54938313 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.020098 WETH | 0.000066 WETH | 0.000000 WETH | 0.000003 WETH | 0.000063 WETH (0.1236 €) | 0.000063 WETH | 31.52 | 0.041 (n=20) | REJECTED | reliability_not_demonstrated |
| 54938313 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.018552 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1205 €) | — | 33.29 | 0.041 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 54938313 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.018552 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1205 €) | 0.000062 WETH | 33.29 | 0.041 (n=20) | REJECTED | reliability_not_demonstrated |
| 54937865 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001977 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1037 €) | — | 7.69 | 0.165 (n=892) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54937865 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.072994 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1036 €) | — | 7.28 | 0.165 (n=892) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 54937865 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.062163 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0834 €) | — | 6.88 | 0.165 (n=892) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 54937865 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001694 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0833 €) | — | 7.20 | 0.165 (n=892) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 6505 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
