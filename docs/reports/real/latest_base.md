# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T00:06:25+00:00 ; durée 160.3 min ; blocs 53087107 → 53091917 (4799 vus)

## Connexion
- Requêtes RPC : 58498 ; erreurs : 5 ; latence p50/p95 : 81.7/1,134.4 ms
- Rafraîchissements d'état : 4800 ; âge des données au dernier bloc : 0.91 s ; changements de frais LP observés (pools à frais dynamiques) : 8509
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12740 ; cycles déclenchés par événement : 1579 ; avance médiane sur le rafraîchissement multicall : 461 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,322.92 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 533 pools, 308 jetons, 19442 routes
- Par DEX : uniswap_v3 143, aerodrome 214, aerodrome_slipstream 129, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 192 (rejetés 2) → 597 jetons ; pools candidats 3802 (énumérés 342, par paires 0), mesurés 535, sous le plancher de 10000.0 $ : 2 → gardés 533 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2341.931042, 'cbBTC': 80341.676682, 'AERO': 0.683871}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,589,568 | 2,322.919222 | 53091917 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,373,284 | 0.029056 | 53091917 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,163,660 | 0.029036 | 53091917 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,455,545 | 0.000013 | 53091917 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,865,910 | 93.021698 | 53091917 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,405,928 | 2,323.706650 | 53091917 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,442,452 | 1.477529 | 53091917 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,985,296 | 0.001653 | 53091917 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,459,992 | 2,324.115476 | 53091917 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,322,339 | 0.029057 | 53091917 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,429,682 | 2,324.039356 | 53091917 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,202,829 | 1.000002 | 53091917 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,805,103 | 34,883.645069 | 53091917 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,769,915 | 2,323.349354 | 53091917 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,204,925 | 0.029044 | 53091917 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 2,513,736 | 0.000013 | 53091917 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2763 | 2,499,198 | 93.057915 | 53091917 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,200,318 | 409.773332 | 53091917 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,119,266 | 1,218,053.752992 | 53091917 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,892,167 | 0.000013 | 53091917 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,890,832 | 0.000000 | 53091917 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,792,491 | 0.017993 | 53091917 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,712,933 | 0.000013 | 53091917 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,712,477 | 0.000013 | 53091917 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,559,262 | 0.000265 | 53091917 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,681 | 0.826253 | 53091917 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53091917 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,425,919 | 0.005540 | 53091917 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,424,230 | 3,438.537094 | 53091917 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,362,378 | 14,102.281926 | 53091917 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,283,996 | 2,323.834631 | 53091917 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,246,109 | 3,445.890916 | 53091917 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,234,276 | 0.000267 | 53091917 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,037 | 65.175518 | 53091917 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,159,727 | 35,217,689.646465 | 53091917 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,158,952 | 0.000000 | 53091917 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,130,756 | 1,107,243.455942 | 53091917 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,114,944 | 495,987.941841 | 53091917 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,087,564 | 52.955277 | 53091917 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,064,069 | 73,032.094060 | 53091917 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,669 | 16.958279 | 53091917 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,014,428 | 21,969,859.621726 | 53091917 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 969,263 | 0.040041 | 53091917 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 922,741 | 2,331.998463 | 53091917 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 910,215 | 2.310113 | 53091917 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 903,324 | 1,129.117728 | 53091917 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,809 | 0.000554 | 53091917 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 880,711 | 17.113708 | 53091917 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 872,883 | 18.168994 | 53091917 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 871,895 | 92.387503 | 53091917 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 845,278 | 2,322.927000 | 53091917 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 799,546 | 0.000008 | 53091917 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,445 | 0.055829 | 53091917 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 786,506 | 0.803130 | 53091917 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 776,582 | 1.105854 | 53091917 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,673 | 0.620287 | 53091917 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 729,135 | 4,791,111.590343 | 53091917 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 719,937 | 0.650490 | 53091917 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 712,668 | 133,708.434918 | 53091917 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2108 | 694,724 | 495,626.599135 | 53091917 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 6378 ; routes examinées : 124001076 ; candidats optimisés : 377142 ; net attendu > 0 : 464 ; dernier cycle 225.6 ms
- Rejets (moteur) : {'spread_below_threshold': 121542695, 'liquidity_below_min': 1933144, 'negative_expected_net': 376678, 'unquotable': 141146, 'borrow_bound_too_small': 6378, 'cycle_budget_exhausted': 571}
- Enregistrements de la session : 377142 ; net attendu > 0 : 464 ; simulés (eth_call de la vraie tx) : 33 (ok 23, échec 10) ; étiquettes ghost N+1 : 6/29 positives
- Décisions : {'REJECTED': 377142} ; motifs de rejet : {'below_safety_margin': 302, 'negative_expected_net': 376678, 'p_lower_below_threshold': 409, 'reliability_not_demonstrated': 55, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 4, 'simulation_failed': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53087522 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.016486 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1666 €) | — | 1.36 | 0.129 (n=327) | REJECTED | below_safety_margin(225<329), p_lower_below_threshold(0.13<0.75) |
| 53087522 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.577121 WETH | 0.000080 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1663 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(77178992824150<115424216900843), p_lower_below_threshold(0.13<0.75) |
| 53087522 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,348.818293 USDC | 0.188160 USDC | 0.000000 USDC | 0.007747 USDC | 0.180413 USDC (0.1660 €) | — | 1.34 | 0.129 (n=327) | REJECTED | below_safety_margin(180413<269763), p_lower_below_threshold(0.13<0.75) |
| 53090757 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.128362 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1233 €) | 0.000058 WETH | 4.48 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53090757 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 297.259241 USDC | 0.141012 USDC | 0.000000 USDC | 0.007454 USDC | 0.133558 USDC (0.1229 €) | — | 4.49 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53090757 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.147291 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1039 €) | 0.000049 WETH | 3.29 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53090757 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 341.588750 USDC | 0.119682 USDC | 0.000000 USDC | 0.007095 USDC | 0.112587 USDC (0.1036 €) | — | 3.30 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53090757 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.141067 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0962 €) | 0.000045 WETH | 3.18 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53090757 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 326.547534 USDC | 0.111295 USDC | 0.000000 USDC | 0.007095 USDC | 0.104200 USDC (0.0959 €) | — | 3.19 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53090757 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.097279 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0911 €) | — | 4.37 | 0.118 (n=151) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53090757 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 226.570308 USDC | 0.105763 USDC | 0.000000 USDC | 0.007095 USDC | 0.098668 USDC (0.0908 €) | — | 4.35 | 0.118 (n=151) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53090757 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.131988 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0824 €) | — | 2.91 | 0.129 (n=328) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53090757 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 305.669366 USDC | 0.096370 USDC | 0.000000 USDC | 0.007095 USDC | 0.089275 USDC (0.0821 €) | — | 2.92 | 0.129 (n=328) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53090757 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.098982 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0662 €) | — | 3.12 | 0.118 (n=151) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53090757 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 229.678788 USDC | 0.078856 USDC | 0.000000 USDC | 0.007095 USDC | 0.071761 USDC (0.0660 €) | — | 3.12 | 0.118 (n=151) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53090757 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.095191 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0614 €) | — | 3.01 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53090757 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 220.805599 USDC | 0.073625 USDC | 0.000000 USDC | 0.007095 USDC | 0.066530 USDC (0.0612 €) | — | 3.01 | 0.080 (n=277) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.079575 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0528 €) | — | 3.09 | 0.119 (n=150) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 184.808006 USDC | 0.064257 USDC | 0.000000 USDC | 0.007020 USDC | 0.057237 USDC (0.0527 €) | — | 3.10 | 0.119 (n=150) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53090757 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.088662 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0519 €) | — | 2.73 | 0.190 (n=166) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53090757 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 205.258197 USDC | 0.063292 USDC | 0.000000 USDC | 0.007095 USDC | 0.056197 USDC (0.0517 €) | — | 2.74 | 0.190 (n=166) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.076234 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0480 €) | — | 2.93 | 0.191 (n=165) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53088047 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.075973 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0479 €) | — | 2.93 | 0.129 (n=327) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 176.937266 USDC | 0.059079 USDC | 0.000000 USDC | 0.007020 USDC | 0.052059 USDC (0.0479 €) | — | 2.94 | 0.191 (n=165) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53088047 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 175.993196 USDC | 0.058953 USDC | 0.000000 USDC | 0.007020 USDC | 0.051933 USDC (0.0478 €) | — | 2.95 | 0.129 (n=327) | REJECTED | p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2567 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
