# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T02:52:14+00:00 ; durée 61.36 min ; blocs 54129350 → 54147740 (3036 vus)

## Connexion
- Requêtes RPC : 39852 ; erreurs : 130 ; latence p50/p95 : 366.9/1,817.6 ms
- Rafraîchissements d'état : 3036 ; âge des données au dernier bloc : 9.87 s ; changements de frais LP observés (pools à frais dynamiques) : 1238
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 165 ; cycles déclenchés par événement : 65 ; avance médiane sur le rafraîchissement multicall : 543 ms
- Gaz : base fee 0.005001 gwei ; prix ETH (pool le plus profond) : 2,241.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 480 pools, 282 jetons, 17844 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 100, aerodrome 199, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 297, par paires 0), mesurés 483, sous le plancher de 10000.0 $ : 3 → gardés 480 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2239.687391, 'cbBTC': 75912.79678, 'AERO': 0.607077}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,932,637 | 2,241.237814 | 54147769 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,780,623 | 0.029553 | 54147769 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,315,273 | 0.000013 | 54147769 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,168,565 | 0.029485 | 54147769 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,019,534 | 2,245.157972 | 54147769 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,420,681 | 106.600105 | 54147769 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,432,184 | 0.001557 | 54147769 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,884,198 | 1.646079 | 54147769 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,763,391 | 0.029556 | 54147769 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,179,168 | 2,244.241367 | 54147769 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,997,132 | 0.998508 | 54147769 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,326,270 | 42,488.942796 | 54147769 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,209 | 2,244.227840 | 54147769 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,561,526 | 0.029498 | 54147769 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,088,980 | 1,166,818.518415 | 54147769 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,741,333 | 0.000013 | 54147769 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,717,039 | 0.006853 | 54147769 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,660,208 | 0.000000 | 54147769 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,631,133 | 0.000013 | 54147769 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,624,605 | 0.016219 | 54147769 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54147769 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,534,105 | 432.885790 | 54147769 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,508,609 | 0.000013 | 54147769 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,379 | 0.819350 | 54147769 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,390,032 | 3,694.212721 | 54147769 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,712 | 2,243.129072 | 54147769 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,324,771 | 2,250.773820 | 54147769 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,276,904 | 14,628.551946 | 54147769 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,175,684 | 2,245.193658 | 54147769 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,722 | 77.089407 | 54147769 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,109,441 | 36,248,304.498282 | 54147769 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,054,720 | 106.733522 | 54147769 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,029,981 | 553,648.485827 | 54147769 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,008,987 | 0.000000 | 54147769 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 999,027 | 22,508,255.999049 | 54147769 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 981,601 | 20.001080 | 54147769 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 941,208 | 1,063.878864 | 54147769 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,465 | 2,228.788739 | 54147769 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 932,452 | 72.067035 | 54147769 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 926,106 | 0.000013 | 54147769 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 893,475 | 95,986.423939 | 54147769 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 814,633 | 0.047515 | 54147769 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 803,172 | 20.780783 | 54147769 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 800,846 | 3,667.284216 | 54147769 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,512 | 0.056669 | 54147769 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,331 | 0.799699 | 54147769 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 720,115 | 0.568284 | 54147769 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 703,676 | 4,800,615.193821 | 54147769 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 687,399 | 0.000255 | 54147769 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 667,751 | 0.559006 | 54147769 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,710 | 145,012.216135 | 54147769 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,340 | 0.000008 | 54147769 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 632,980 | 558,542.624639 | 54147769 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 588,944 | 2.473030 | 54147769 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 586,390 | 0.040730 | 54147769 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 527,071 | 1,064.136415 | 54147769 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 521,464 | 897,343.903978 | 54147769 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 520,812 | 0.077670 | 54147769 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 517,232 | 2,244.295571 | 54147769 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 517,177 | 6,887.064295 | 54147769 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 3100 ; routes examinées : 55316400 ; candidats optimisés : 200958 ; net attendu > 0 : 34 ; dernier cycle 398.2 ms
- Rejets (moteur) : {'spread_below_threshold': 54472343, 'liquidity_below_min': 631013, 'negative_expected_net': 200924, 'pool_quarantined': 8776, 'borrow_bound_too_small': 3098, 'cycle_budget_exhausted': 212}
- Enregistrements de la session : 200958 ; net attendu > 0 : 34 ; simulés (eth_call de la vraie tx) : 17 (ok 5, échec 12) ; étiquettes ghost N+1 : 1/13 positives
- Décisions : {'REJECTED': 200958} ; motifs de rejet : {'below_safety_margin': 16, 'negative_expected_net': 200924, 'p_lower_below_threshold': 30, 'price_impact': 13, 'reliability_not_demonstrated': 4, 'simulation_failed': 12, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54145094 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 34.995920 USDC | 0.046390 USDC | 0.000000 USDC | 0.005032 USDC | 0.041358 USDC (0.0380 €) | 0.041358 USDC | 11.82 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 54133736 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 25.654596 USDC | 0.027046 USDC | 0.000000 USDC | 0.005029 USDC | 0.022017 USDC (0.0203 €) | 0.022017 USDC | 8.58 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 54131500 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 24.545994 USDC | 0.015989 USDC | 0.000000 USDC | 0.005029 USDC | 0.010960 USDC (0.0101 €) | 0.010960 USDC | 4.47 | 0.026 (n=322) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54133628 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 16.785697 USDC | 0.011651 USDC | 0.000000 USDC | 0.005031 USDC | 0.006620 USDC (0.0061 €) | — | 3.94 | 0.065 (n=91) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 54132465 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.625961 USDC | 0.011096 USDC | 0.000000 USDC | 0.005029 USDC | 0.006067 USDC (0.0056 €) | 0.006067 USDC | 2.94 | 0.047 (n=249) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54142205 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0042 €) | — | 45.52 | 0.007 (n=121) | REJECTED | stale_data(4634ms>4000.0), price_impact(209bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 54133929 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 14.185621 USDC | 0.008294 USDC | 0.000000 USDC | 0.005030 USDC | 0.003264 USDC (0.0030 €) | 0.003264 USDC | 2.30 | 0.053 (n=82) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54133049 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.574000 USDC | 0.008255 USDC | 0.000000 USDC | 0.005028 USDC | 0.003227 USDC (0.0030 €) | — | 1.84 | 0.047 (n=250) | REJECTED | below_safety_margin(3227<3514), stale_data(4274ms>4000.0), p_lower_below_threshold(0.05<0.75) |
| 54137594 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.366000 USDC | 0.007954 USDC | 0.000000 USDC | 0.005032 USDC | 0.002922 USDC (0.0027 €) | — | 1.68 | 0.047 (n=250) | REJECTED | below_safety_margin(2922<3473), p_lower_below_threshold(0.05<0.75) |
| 54132664 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 16.491328 USDC | 0.007156 USDC | 0.000000 USDC | 0.005029 USDC | 0.002127 USDC (0.0020 €) | — | 1.29 | 0.047 (n=250) | REJECTED | below_safety_margin(2127<3298), p_lower_below_threshold(0.05<0.75) |
| 54142205 | WETH→[aerodrome]→fBOMB→[aerodrome]→cbBTC→[aerodrome]→WETH | 0.000446 WETH | 0.000001 WETH | 0.000000 WETH | 0.000000 WETH | 0.000001 WETH (0.0011 €) | — | 11.85 | 0.006 (n=1) | REJECTED | stale_data(4642ms>4000.0), price_impact(224bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 54142802 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.140 (n=262) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143470 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | stale_data(4795ms>4000.0), price_impact(210bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143111 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.140 (n=263) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143112 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143113 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54143114 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.139 (n=264) | REJECTED | price_impact(214bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142488 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.141 (n=261) | REJECTED | stale_data(4603ms>4000.0), price_impact(211bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142489 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.140 (n=262) | REJECTED | price_impact(211bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142205 | cbBTC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.141 (n=260) | REJECTED | stale_data(4635ms>4000.0), price_impact(235bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.14<0.75) |
| 54142205 | cbBTC→[aerodrome]→WETH→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 7.59 | 0.002 (n=3) | REJECTED | stale_data(4642ms>4000.0), price_impact(230bps>150.0), reliability_not_demonstrated |
| 54143367 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.719307 USDC | 0.005766 USDC | 0.000000 USDC | 0.005031 USDC | 0.000735 USDC (0.0007 €) | — | 0.50 | 0.047 (n=250) | REJECTED | below_safety_margin(735<2943), p_lower_below_threshold(0.05<0.75) |
| 54147336 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.409645 USDC | 0.005505 USDC | 0.000000 USDC | 0.005031 USDC | 0.000474 USDC (0.0004 €) | — | 0.33 | 0.047 (n=250) | REJECTED | below_safety_margin(474<2881), p_lower_below_threshold(0.05<0.75) |
| 54133184 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.132990 USDC | 0.006845 USDC | 0.000000 USDC | 0.006730 USDC | 0.000115 USDC (0.0001 €) | — | 0.14 | 0.241 (n=407) | REJECTED | below_safety_margin(115<1626), stale_data(4312ms>4000.0), p_lower_below_threshold(0.24<0.75) |
| 54133185 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 8.132990 USDC | 0.006845 USDC | 0.000000 USDC | 0.006730 USDC | 0.000115 USDC (0.0001 €) | — | 0.14 | 0.241 (n=407) | REJECTED | below_safety_margin(115<1626), p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 5936 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
