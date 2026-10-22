# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T13:23:14+00:00 ; durée 269.29 min ; blocs 52934940 → 52943017 (7357 vus)

## Connexion
- Requêtes RPC : 91804 ; erreurs : 120 ; latence p50/p95 : 276.9/1,707.2 ms
- Rafraîchissements d'état : 7358 ; âge des données au dernier bloc : 1.96 s ; changements de frais LP observés (pools à frais dynamiques) : 12168
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 68216 ; cycles déclenchés par événement : 5326 ; avance médiane sur le rafraîchissement multicall : 563 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,400.86 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 552 pools, 321 jetons, 20574 routes
- Par DEX : uniswap_v3 136, aerodrome 228, aerodrome_slipstream 141 (quarantaine 2), pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 201 (rejetés 2) → 606 jetons ; pools candidats 3839 (énumérés 370, par paires 0), mesurés 554, sous le plancher de 10000.0 $ : 2 → gardés 552 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2409.153844, 'AERO': 0.798022, 'cbBTC': 81873.188532}
- Pools en quarantaine : 2 — aerodrome_slipstream:MAMO/cbBTC@0xE2B3aA: simulation failed ×5 (model/chain mismatch) — until block 52943259; aerodrome_slipstream:WETH/MAMO@0xAa067F: simulation failed ×5 (model/chain mismatch) — until block 52943259

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,776,776 | 2,400.859063 | 52943017 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 20,533,255 | 1.245366 | 52943017 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,273,800 | 0.029358 | 52943017 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,881,647 | 88.543031 | 52943017 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,255,850 | 0.029399 | 52943017 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,427,728 | 0.000012 | 52943017 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,422,124 | 0.029384 | 52943017 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,621,474 | 2,398.090220 | 52943017 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,177,917 | 0.001668 | 52943017 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,023,167 | 0.000012 | 52943017 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,941,998 | 2,398.568836 | 52943017 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 5,621,567 | 0.000012 | 52943017 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,397,953 | 0.029360 | 52943017 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,493,767 | 2,398.751827 | 52943017 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,315,821 | 2,398.276885 | 52943017 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,300,292 | 1.000001 | 52943017 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,984,354 | 34,426.893018 | 52943017 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,762,087 | 0.000275 | 52943017 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,911,150 | 2,402.042183 | 52943017 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,601,038 | 88.587849 | 52943017 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,353,568 | 2,970.236535 | 52943017 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,303,833 | 397.612260 | 52943017 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,219,628 | 0.000012 | 52943017 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,200,999 | 1,207,117.448597 | 52943017 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,062,386 | 0.000012 | 52943017 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,901,912 | 0.000000 | 52943017 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,799,977 | 0.018590 | 52943017 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,661,419 | 1.521320 | 52943017 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,742 | 0.822994 | 52943017 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,414,273 | 13,540.720819 | 52943017 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,384,944 | 2,986.020990 | 52943017 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,363,872 | 2,397.850809 | 52943017 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,359,340 | 0.004919 | 52943017 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,314,803 | 2.361494 | 52943017 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,299,312 | 0.000275 | 52943017 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,289,910 | 0.000000 | 52943017 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,679 | 64.262670 | 52943017 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,196,140 | 35,295,161.583947 | 52943017 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,184,514 | 1,091,136.905662 | 52943017 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,184,078 | 16.315917 | 52943017 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/NOCK | 3000 | 1,153,888 | 47.269709 | 52943017 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,149,096 | 500,799.079441 | 52943017 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,112,737 | 73,551.650097 | 52943017 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,109,371 | 0.000010 | 52943017 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 1,096,149 | 1.105751 | 52943017 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,060,261 | 21,485,745.113481 | 52943017 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,757 | 17.209114 | 52943017 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,019,050 | 0.029398 | 52943017 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,012,120 | 23.032718 | 52943017 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 997,879 | 0.036935 | 52943017 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 960,060 | 1,061.338908 | 52943017 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 933,173 | 2,417.791097 | 52943017 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 915,691 | 0.000548 | 52943017 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | EURC/USDC | 73 | 902,067 | 1.120425 | 52943017 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/bsdETH | 100 | 894,289 | 0.916099 | 52943017 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 892,020 | 17.491209 | 52943017 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 875,826 | 2,400.868753 | 52943017 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 815,196 | 0.803225 | 52943017 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | fBOMB/USDC | 10000 | 811,836 | 0.018812 | 52943017 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 803,286 | 1.106146 | 52943017 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 12683 ; routes examinées : 260940042 ; candidats optimisés : 1229861 ; net attendu > 0 : 296 ; dernier cycle 173.9 ms
- Rejets (moteur) : {'spread_below_threshold': 257296527, 'liquidity_below_min': 2379910, 'negative_expected_net': 1229565, 'pool_quarantined': 15048, 'borrow_bound_too_small': 12665, 'cycle_budget_exhausted': 6031}
- Enregistrements de la session : 1229861 ; net attendu > 0 : 296 ; simulés (eth_call de la vraie tx) : 33 (ok 10, échec 23) ; étiquettes ghost N+1 : 0/33 positives
- Décisions : {'REJECTED': 1229861} ; motifs de rejet : {'below_safety_margin': 101, 'negative_expected_net': 1229565, 'p_lower_below_threshold': 225, 'reliability_not_demonstrated': 71, 'simulation_failed': 23, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52940243 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→cbBTC | 0.013410 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2916 €) | — | 2.89 | 0.182 (n=29) | REJECTED | stale_data(11071ms>4000.0), reliability_not_demonstrated |
| 52940243 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 1,119.170950 USDC | 0.323051 USDC | 0.000000 USDC | 0.006907 USDC | 0.316144 USDC (0.2909 €) | — | 2.82 | 0.182 (n=29) | REJECTED | stale_data(11065ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005862 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2338 €) | — | 5.29 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52935498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.359582 WETH | 0.000108 WETH | 0.000000 WETH | 0.000002 WETH | 0.000106 WETH (0.2336 €) | 0.000106 WETH | 2.94 | 0.023 (n=63) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52938641 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 483.768011 USDC | 0.260782 USDC | 0.000000 USDC | 0.007249 USDC | 0.253533 USDC (0.2333 €) | — | 5.24 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 860.319661 USDC | 0.259021 USDC | 0.000000 USDC | 0.005776 USDC | 0.253245 USDC (0.2330 €) | — | 2.94 | 0.023 (n=63) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52941399 | WETH→[aerodrome]→msETH→[aerodrome_slipstream]→WETH | 0.222882 WETH | 0.000083 WETH | 0.000000 WETH | 0.000002 WETH | 0.000081 WETH (0.1796 €) | 0.000081 WETH | 3.64 | 0.066 (n=22) | REJECTED | reliability_not_demonstrated |
| 52940243 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005230 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1771 €) | — | 4.49 | 0.097 (n=183) | REJECTED | stale_data(11020ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52940243 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 426.532059 USDC | 0.198713 USDC | 0.000000 USDC | 0.007239 USDC | 0.191474 USDC (0.1762 €) | — | 4.49 | 0.097 (n=183) | REJECTED | stale_data(11006ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52938641 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 431.669333 USDC | 0.191189 USDC | 0.000000 USDC | 0.007249 USDC | 0.183940 USDC (0.1692 €) | — | 4.26 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.004955 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1689 €) | — | 4.52 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.065171 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.1017 €) | — | 7.06 | 0.099 (n=180) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52938641 | WETH→[uniswap_v3]→wstETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.064612 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0999 €) | — | 6.99 | 0.099 (n=180) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52935498 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.103454 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0950 €) | 0.000043 WETH | 4.15 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52935498 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 247.137886 USDC | 0.110224 USDC | 0.000000 USDC | 0.007240 USDC | 0.102984 USDC (0.0947 €) | — | 4.17 | 0.130 (n=91) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.003730 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0875 €) | — | 3.11 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 307.015328 USDC | 0.101744 USDC | 0.000000 USDC | 0.007249 USDC | 0.094495 USDC (0.0869 €) | — | 3.08 | 0.124 (n=95) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002499 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0867 €) | — | 4.60 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52938641 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 191.834564 USDC | 0.101363 USDC | 0.000000 USDC | 0.007249 USDC | 0.094114 USDC (0.0866 €) | — | 4.91 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002752 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0860 €) | — | 4.14 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52938641 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.095400 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0858 €) | — | 4.07 | 0.099 (n=180) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52940243 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002769 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0814 €) | — | 3.90 | 0.097 (n=183) | REJECTED | stale_data(11059ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 52938641 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002758 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0807 €) | — | 3.88 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52940243 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.109760 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0807 €) | — | 3.32 | 0.097 (n=183) | REJECTED | stale_data(11052ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52938641 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.103642 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0807 €) | — | 3.52 | 0.099 (n=180) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1877 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
