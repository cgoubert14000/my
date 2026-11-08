# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T23:42:36+00:00 ; durée 58.12 min ; blocs 54937445 → 54954863 (3693 vus)

## Connexion
- Requêtes RPC : 46493 ; erreurs : 240 ; latence p50/p95 : 283.8/1,058.8 ms
- Rafraîchissements d'état : 3693 ; âge des données au dernier bloc : 7.11 s ; changements de frais LP observés (pools à frais dynamiques) : 3627
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2674 ; cycles déclenchés par événement : 636 ; avance médiane sur le rafraîchissement multicall : 351 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,142.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 466 pools, 272 jetons, 17666 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 194, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3664 (énumérés 289, par paires 0), mesurés 468, sous le plancher de 10000.0 $ : 2 → gardés 466 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2120.787264, 'cbBTC': 74286.143616, 'AERO': 0.573915}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 139,319,718 | 2,142.026997 | 54954863 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,463,275 | 0.028492 | 54954863 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,998,528 | 0.000013 | 54954863 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,838,834 | 0.028564 | 54954863 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,323,119 | 2,137.216157 | 54954863 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,114,561 | 105.910698 | 54954863 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,294,978 | 0.001518 | 54954863 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,934,479 | 0.028496 | 54954863 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,624,903 | 1.730939 | 54954863 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,956,994 | 0.999264 | 54954863 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,934,564 | 2,138.092732 | 54954863 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,178,938 | 42,491.379359 | 54954863 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,053,170 | 2,137.938629 | 54954863 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 2,387,162 | 0.028552 | 54954863 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,003,926 | 1,158,197.335472 | 54954863 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 1,717,635 | 0.000013 | 54954863 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,617,671 | 0.000013 | 54954863 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,565,653 | 0.000000 | 54954863 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,560,559 | 0.006411 | 54954863 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,527,954 | 0.014998 | 54954863 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,117 | 1.431451 | 54954863 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,462,317 | 437.418230 | 54954863 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,414,395 | 0.000013 | 54954863 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,331,816 | 3,702.389089 | 54954863 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,297,355 | 2,142.482711 | 54954863 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,240,785 | 15,305.364999 | 54954863 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,226,719 | 2,142.547413 | 54954863 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,122,761 | 77.084041 | 54954863 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,104,965 | 2,137.256421 | 54954863 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,053,223 | 36,877,720.446607 | 54954863 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,056 | 106.374520 | 54954863 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 959,813 | 596,917.820337 | 54954863 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 949,402 | 22.136846 | 54954863 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 948,189 | 22,792,180.475676 | 54954863 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 931,536 | 0.000013 | 54954863 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 914,220 | 2,144.554936 | 54954863 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 911,049 | 0.000000 | 54954863 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 909,063 | 75.826312 | 54954863 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 900,274 | 1,058.982634 | 54954863 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 855,293 | 0.824191 | 54954863 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/EDEL | 7000 | 831,359 | 101,208.003691 | 54954863 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 807,747 | 0.049568 | 54954863 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 778,266 | 0.054118 | 54954863 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 753,013 | 3,716.942490 | 54954863 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 748,050 | 22.966172 | 54954863 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 725,927 | 0.801347 | 54954863 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 704,435 | 0.541575 | 54954863 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 651,946 | 5,109,520.913420 | 54954863 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 638,697 | 0.516996 | 54954863 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 628,200 | 0.000008 | 54954863 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 622,865 | 149,583.995762 | 54954863 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 595,851 | 0.000250 | 54954863 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 581,755 | 592,015.317546 | 54954863 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,696 | 0.038682 | 54954863 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 531,729 | 2.462292 | 54954863 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 517,878 | 896,552.676296 | 54954863 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2727 | 510,313 | 1,058.681774 | 54954863 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 502,816 | 0.073935 | 54954863 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 494,939 | 2,137.915728 | 54954863 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | USDC/USDT | 100 | 494,795 | 1.001486 | 54954863 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |

## Recherche d'opportunités
- Cycles : 4328 ; routes examinées : 76458448 ; candidats optimisés : 286321 ; net attendu > 0 : 2496 ; dernier cycle 187.5 ms
- Rejets (moteur) : {'spread_below_threshold': 74999472, 'liquidity_below_min': 1165297, 'negative_expected_net': 283825, 'borrow_bound_too_small': 4326, 'cycle_budget_exhausted': 3032}
- Enregistrements de la session : 286321 ; net attendu > 0 : 2496 ; simulés (eth_call de la vraie tx) : 111 (ok 81, échec 30) ; étiquettes ghost N+1 : 39/88 positives
- Décisions : {'REJECTED': 286321} ; motifs de rejet : {'below_safety_margin': 2158, 'negative_expected_net': 283825, 'p_lower_below_threshold': 2292, 'price_impact': 8, 'reliability_not_demonstrated': 204, 'sim_below_estimate': 7, 'simulated_net_nonpositive': 1, 'simulation_failed': 30, 'stale_data': 49}

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
- Observations ghost : 6523 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
