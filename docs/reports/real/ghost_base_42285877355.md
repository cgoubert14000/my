# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T01:10:13+00:00 ; durée 295.97 min ; blocs 54028370 → 54117095 (17790 vus)

## Connexion
- Requêtes RPC : 215234 ; erreurs : 20 ; latence p50/p95 : 195.7/1,541.0 ms
- Rafraîchissements d'état : 17790 ; âge des données au dernier bloc : 8.66 s ; changements de frais LP observés (pools à frais dynamiques) : 5324
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11172 ; cycles déclenchés par événement : 4626 ; avance médiane sur le rafraîchissement multicall : 305 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,239.69 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 282 jetons, 17936 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3742 (énumérés 299, par paires 0), mesurés 485, sous le plancher de 10000.0 $ : 3 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2228.731074, 'cbBTC': 75812.648558, 'AERO': 0.606832}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,916,093 | 2,239.687008 | 54117119 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,777,119 | 0.029523 | 54117119 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,311,971 | 0.000013 | 54117119 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,165,892 | 0.029484 | 54117119 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,015,280 | 2,239.965991 | 54117119 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,398,426 | 107.094029 | 54117119 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,434,857 | 0.001558 | 54117119 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,886,753 | 1.645397 | 54117119 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,761,999 | 0.029531 | 54117119 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,179,223 | 2,240.243411 | 54117119 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,998,338 | 0.998508 | 54117119 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,315,191 | 42,714.246168 | 54117119 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,203,671 | 2,240.268793 | 54117119 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,560,807 | 0.029497 | 54117119 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,087,535 | 1,166,818.518415 | 54117119 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,737,837 | 0.006946 | 54117119 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,736,699 | 0.000013 | 54117119 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,661,642 | 0.000000 | 54117119 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,632,319 | 0.000013 | 54117119 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,622,604 | 0.016226 | 54117119 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54117119 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,538,860 | 0.000013 | 54117119 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,534,970 | 431.037101 | 54117119 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,379 | 0.819350 | 54117119 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,390,098 | 3,685.810250 | 54117119 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,252 | 2,241.401119 | 54117119 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,324,349 | 2,245.352183 | 54117119 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,279,040 | 14,611.189861 | 54117119 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,173,457 | 2,239.989085 | 54117119 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,722 | 77.089421 | 54117119 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,103,450 | 36,621,353.349668 | 54117119 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,050,822 | 106.771369 | 54117119 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,031,202 | 553,642.029370 | 54117119 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,019,037 | 0.000000 | 54117119 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,336 | 22,508,235.864785 | 54117119 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 978,507 | 20.188793 | 54117119 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 943,121 | 1,059.806427 | 54117119 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,194 | 2,228.788696 | 54117119 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 926,334 | 0.000013 | 54117119 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 923,515 | 73.471634 | 54117119 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 893,165 | 95,920.007066 | 54117119 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 838,314 | 0.000526 | 54117119 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 811,436 | 0.047815 | 54117119 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 803,431 | 20.771044 | 54117119 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 800,737 | 3,657.335167 | 54117119 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,528 | 0.056973 | 54117119 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 759,805 | 0.799699 | 54117119 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,802 | 0.568445 | 54117119 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 701,421 | 4,824,808.833856 | 54117119 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 688,125 | 0.000256 | 54117119 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 667,756 | 0.559006 | 54117119 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,960 | 144,700.680243 | 54117119 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,558 | 0.000008 | 54117119 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 632,538 | 555,820.545471 | 54117119 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 592,491 | 0.041380 | 54117119 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 588,692 | 2.472072 | 54117119 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 529,552 | 0.079524 | 54117119 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 528,223 | 1,059.538149 | 54117119 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 521,136 | 896,324.680068 | 54117119 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 519,316 | 2,240.295529 | 54117119 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 22415 ; routes examinées : 402035440 ; candidats optimisés : 1118093 ; net attendu > 0 : 341 ; dernier cycle 279.5 ms
- Rejets (moteur) : {'spread_below_threshold': 395904875, 'liquidity_below_min': 4969762, 'negative_expected_net': 1117752, 'borrow_bound_too_small': 22407, 'pool_quarantined': 19012, 'cycle_budget_exhausted': 1291}
- Enregistrements de la session : 1118093 ; net attendu > 0 : 341 ; simulés (eth_call de la vraie tx) : 41 (ok 15, échec 26) ; étiquettes ghost N+1 : 8/25 positives
- Décisions : {'REJECTED': 1118093} ; motifs de rejet : {'below_safety_margin': 214, 'negative_expected_net': 1117752, 'p_lower_below_threshold': 311, 'price_impact': 15, 'reliability_not_demonstrated': 30, 'simulation_failed': 26, 'stale_data': 27}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54112438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003057 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2345 €) | — | 10.99 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 241.527918 USDC | 0.261430 USDC | 0.000000 USDC | 0.006731 USDC | 0.254699 USDC (0.2343 €) | — | 10.55 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003061 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2338 €) | — | 10.95 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54112438 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 230.657232 USDC | 0.260268 USDC | 0.000000 USDC | 0.006731 USDC | 0.253537 USDC (0.2333 €) | — | 10.99 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54112438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002737 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2080 €) | — | 10.89 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 207.330696 USDC | 0.231952 USDC | 0.000000 USDC | 0.006731 USDC | 0.225221 USDC (0.2072 €) | — | 10.86 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002784 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2031 €) | — | 10.45 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.093357 WETH | 0.000102 WETH | 0.000000 WETH | 0.000003 WETH | 0.000098 WETH (0.2027 €) | — | 10.54 | 0.080 (n=147) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 54112438 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003057 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2003 €) | — | 9.39 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54112438 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 221.971934 USDC | 0.223994 USDC | 0.000000 USDC | 0.006731 USDC | 0.217263 USDC (0.1999 €) | — | 9.79 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54112438 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002314 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1849 €) | — | 11.45 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.078373 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1844 €) | — | 11.42 | 0.080 (n=147) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 54112438 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002239 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1354 €) | — | 8.66 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54112438 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 176.391939 USDC | 0.153520 USDC | 0.000000 USDC | 0.006731 USDC | 0.146789 USDC (0.1350 €) | — | 8.32 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54112438 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002057 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1235 €) | — | 8.60 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.073728 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000060 WETH (0.1234 €) | — | 8.12 | 0.080 (n=147) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 54112438 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002059 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1207 €) | — | 8.40 | 0.080 (n=147) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54112438 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.076356 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1204 €) | — | 7.65 | 0.155 (n=797) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 54060684 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 837.885496 USDC | 0.111051 USDC | 0.000000 USDC | 0.005054 USDC | 0.105997 USDC (0.0975 €) | — | 1.27 | 0.047 (n=247) | REJECTED | below_safety_margin(105997<167577), p_lower_below_threshold(0.05<0.75) |
| 54060684 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.374447 WETH | 0.000050 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.0972 €) | — | 1.26 | 0.047 (n=247) | REJECTED | below_safety_margin(47277268623202<74889389706557), p_lower_below_threshold(0.05<0.75) |
| 54060684 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 757.927748 USDC | 0.070574 USDC | 0.000000 USDC | 0.006764 USDC | 0.063810 USDC (0.0587 €) | — | 0.84 | 0.029 (n=28) | REJECTED | below_safety_margin(63810<151585), reliability_not_demonstrated |
| 54060684 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008755 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0585 €) | — | 0.96 | 0.029 (n=28) | REJECTED | below_safety_margin(84<175), reliability_not_demonstrated |
| 54060684 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.329385 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0581 €) | — | 0.86 | 0.029 (n=28) | REJECTED | below_safety_margin(28267304274076<65877091333329), reliability_not_demonstrated |
| 54057958 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 68.807723 USDC | 0.056511 USDC | 0.000000 USDC | 0.005004 USDC | 0.051507 USDC (0.0474 €) | — | 7.49 | 0.026 (n=319) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54102295 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 119.155898 USDC | 0.054005 USDC | 0.000000 USDC | 0.006730 USDC | 0.047275 USDC (0.0435 €) | — | 3.97 | 0.156 (n=794) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 5922 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
