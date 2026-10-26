# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T01:52:21+00:00 ; durée 266.25 min ; blocs 53087107 → 53095094 (7966 vus)

## Connexion
- Requêtes RPC : 95734 ; erreurs : 5 ; latence p50/p95 : 79.8/1,081.6 ms
- Rafraîchissements d'état : 7967 ; âge des données au dernier bloc : 1.88 s ; changements de frais LP observés (pools à frais dynamiques) : 15647
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12740 ; cycles déclenchés par événement : 1579 ; avance médiane sur le rafraîchissement multicall : 461 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,304.47 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 533 pools, 308 jetons, 19442 routes
- Par DEX : uniswap_v3 143, aerodrome 214, aerodrome_slipstream 129, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 192 (rejetés 2) → 597 jetons ; pools candidats 3802 (énumérés 342, par paires 0), mesurés 535, sous le plancher de 10000.0 $ : 2 → gardés 533 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2341.931042, 'cbBTC': 80341.676682, 'AERO': 0.683871}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,609,609 | 2,304.474081 | 53095094 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,245,550 | 0.028993 | 53095094 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,091,743 | 0.029036 | 53095094 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,425,372 | 0.000013 | 53095094 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,830,934 | 92.276913 | 53095094 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,371,203 | 2,305.382299 | 53095094 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,369,745 | 1.499964 | 53095094 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,945,710 | 0.001653 | 53095094 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,423,808 | 2,306.021726 | 53095094 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,280,806 | 0.029002 | 53095094 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,440,688 | 2,306.183713 | 53095094 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,178,172 | 1.000002 | 53095094 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,780,360 | 34,782.732643 | 53095094 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,754,548 | 2,304.525144 | 53095094 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,169,232 | 0.029045 | 53095094 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,504,670 | 0.000013 | 53095094 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,487,519 | 92.255342 | 53095094 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,180,023 | 411.207529 | 53095094 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,102,638 | 1,217,822.198824 | 53095094 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,886,585 | 0.000013 | 53095094 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,875,814 | 0.000000 | 53095094 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,783,890 | 0.017847 | 53095094 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,707,098 | 0.000013 | 53095094 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,705,446 | 0.000013 | 53095094 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,546,604 | 0.000265 | 53095094 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,692 | 0.826241 | 53095094 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53095094 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,407,404 | 3,455.852963 | 53095094 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,392,434 | 0.005436 | 53095094 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,351,487 | 14,169.539516 | 53095094 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,232,655 | 2,305.383788 | 53095094 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,231,636 | 3,445.900743 | 53095094 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,224,375 | 0.000267 | 53095094 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,037 | 65.175518 | 53095094 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,152,501 | 35,037,854.119773 | 53095094 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,144,463 | 0.000000 | 53095094 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,121,777 | 1,107,243.650383 | 53095094 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,106,163 | 495,900.701362 | 53095094 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,087,971 | 52.915719 | 53095094 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,055,180 | 73,093.050248 | 53095094 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,620 | 17.093723 | 53095094 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,006,373 | 21,969,859.621726 | 53095094 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 969,393 | 0.040010 | 53095094 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 919,573 | 2,320.640490 | 53095094 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 903,318 | 2.308855 | 53095094 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 892,250 | 1,136.362602 | 53095094 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 885,718 | 0.000554 | 53095094 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 871,101 | 17.169920 | 53095094 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 867,731 | 92.426665 | 53095094 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 866,676 | 18.379838 | 53095094 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 841,944 | 2,305.218308 | 53095094 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,482 | 0.057183 | 53095094 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 790,929 | 0.000008 | 53095094 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 780,261 | 0.803130 | 53095094 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 770,449 | 1.105951 | 53095094 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 738,102 | 0.613830 | 53095094 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,387 | 4,777,365.381657 | 53095094 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 706,617 | 133,857.434074 | 53095094 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 703,408 | 0.622381 | 53095094 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 689,276 | 495,417.986720 | 53095094 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 9545 ; routes examinées : 185573890 ; candidats optimisés : 561010 ; net attendu > 0 : 629 ; dernier cycle 219.7 ms
- Rejets (moteur) : {'spread_below_threshold': 181940073, 'liquidity_below_min': 2853364, 'negative_expected_net': 560381, 'unquotable': 209327, 'borrow_bound_too_small': 9545, 'cycle_budget_exhausted': 571}
- Enregistrements de la session : 561010 ; net attendu > 0 : 629 ; simulés (eth_call de la vraie tx) : 56 (ok 46, échec 10) ; étiquettes ghost N+1 : 8/47 positives
- Décisions : {'REJECTED': 561010} ; motifs de rejet : {'below_safety_margin': 424, 'negative_expected_net': 560381, 'p_lower_below_threshold': 563, 'reliability_not_demonstrated': 66, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 4, 'simulation_failed': 10}

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
- Observations ghost : 2585 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
