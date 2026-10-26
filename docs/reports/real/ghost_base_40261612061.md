# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T03:22:39+00:00 ; durée 21.31 min ; blocs 53097164 → 53097805 (639 vus)

## Connexion
- Requêtes RPC : 8113 ; erreurs : 0 ; latence p50/p95 : 76.9/985.1 ms
- Rafraîchissements d'état : 639 ; âge des données au dernier bloc : 2.2 s ; changements de frais LP observés (pools à frais dynamiques) : 1367
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12367 ; cycles déclenchés par événement : 687 ; avance médiane sur le rafraîchissement multicall : 452 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,308.92 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 302 jetons, 19436 routes
- Par DEX : uniswap_v3 140, aerodrome 213, aerodrome_slipstream 125, pancakeswap_v3 31, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 337, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2299.668664, 'cbBTC': 79491.484, 'AERO': 0.669155}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,841,466 | 2,308.922857 | 53097805 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,282,089 | 0.028971 | 53097805 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,113,409 | 0.028978 | 53097805 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,442,414 | 0.000013 | 53097805 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,746,940 | 94.421153 | 53097805 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,298,939 | 2,308.359170 | 53097805 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,193,103 | 1.496560 | 53097805 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,962,326 | 0.001653 | 53097805 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 713 | 5,419,149 | 2,309.053493 | 53097805 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,290,385 | 0.028981 | 53097805 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,447,878 | 2,309.276024 | 53097805 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,185,337 | 1.000005 | 53097805 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,784,281 | 34,844.843952 | 53097805 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,753,064 | 2,308.728176 | 53097805 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,176,848 | 0.028982 | 53097805 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 2,526,680 | 0.000013 | 53097805 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,467,732 | 94.430986 | 53097805 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,184,993 | 410.832982 | 53097805 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,113,226 | 1,210,308.594714 | 53097805 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,887,393 | 0.000013 | 53097805 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,879,690 | 0.000000 | 53097805 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,781,836 | 0.017812 | 53097805 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,709,953 | 0.000013 | 53097805 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,708,105 | 0.000013 | 53097805 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,549,589 | 0.000265 | 53097805 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,242 | 0.826241 | 53097805 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53097805 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,420,591 | 0.005496 | 53097805 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,410,393 | 3,451.388836 | 53097805 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,355,208 | 14,168.161818 | 53097805 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,240,225 | 2,308.366765 | 53097805 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,233,412 | 3,445.900743 | 53097805 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,226,737 | 0.000266 | 53097805 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,037 | 65.175518 | 53097805 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,155,178 | 34,998,102.063033 | 53097805 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,151,961 | 0.000000 | 53097805 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,123,890 | 1,107,347.413734 | 53097805 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,108,496 | 496,061.225832 | 53097805 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,083,764 | 53.327361 | 53097805 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,061,425 | 72,514.571543 | 53097805 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,030,935 | 17.397359 | 53097805 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,007,948 | 21,983,711.415667 | 53097805 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 956,403 | 0.040957 | 53097805 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 920,253 | 2,317.752371 | 53097805 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 905,211 | 2.308285 | 53097805 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 894,173 | 1,144.611115 | 53097805 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 886,069 | 0.000552 | 53097805 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 874,928 | 17.124033 | 53097805 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 868,468 | 18.319507 | 53097805 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 862,366 | 93.747486 | 53097805 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 842,763 | 2,309.076377 | 53097805 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,297 | 0.056104 | 53097805 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 790,662 | 0.000008 | 53097805 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 781,767 | 0.803130 | 53097805 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 771,937 | 1.105951 | 53097805 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,231 | 0.613879 | 53097805 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,738 | 4,791,223.694285 | 53097805 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 707,451 | 0.629137 | 53097805 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 705,392 | 134,845.880496 | 53097805 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 690,499 | 496,948.893422 | 53097805 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 1325 ; routes examinées : 25752700 ; candidats optimisés : 77956 ; net attendu > 0 : 49 ; dernier cycle 182.4 ms
- Rejets (moteur) : {'spread_below_threshold': 25307003, 'liquidity_below_min': 335675, 'negative_expected_net': 77907, 'unquotable': 30660, 'borrow_bound_too_small': 1325, 'cycle_budget_exhausted': 81}
- Enregistrements de la session : 77956 ; net attendu > 0 : 49 ; simulés (eth_call de la vraie tx) : 4 (ok 2, échec 2) ; étiquettes ghost N+1 : 2/2 positives
- Décisions : {'REJECTED': 77956} ; motifs de rejet : {'below_safety_margin': 45, 'negative_expected_net': 77907, 'p_lower_below_threshold': 45, 'reliability_not_demonstrated': 4, 'sim_below_estimate': 2, 'simulation_failed': 2, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53097384 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 68.777003 USDC | 0.009306 USDC | 0.000000 USDC | 0.006954 USDC | 0.002352 USDC (0.0022 €) | — | 0.34 | 0.180 (n=175) | REJECTED | below_safety_margin(2352<13755), p_lower_below_threshold(0.18<0.75) |
| 53097385 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 68.777003 USDC | 0.009306 USDC | 0.000000 USDC | 0.006954 USDC | 0.002352 USDC (0.0022 €) | — | 0.34 | 0.180 (n=175) | REJECTED | below_safety_margin(2352<13755), p_lower_below_threshold(0.18<0.75) |
| 53097385 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 68.617109 USDC | 0.009306 USDC | 0.000000 USDC | 0.006954 USDC | 0.002352 USDC (0.0022 €) | — | 0.34 | 0.180 (n=175) | REJECTED | below_safety_margin(2352<13723), p_lower_below_threshold(0.18<0.75) |
| 53097264 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.809626 USDC | 0.009287 USDC | 0.000000 USDC | 0.006937 USDC | 0.002350 USDC (0.0022 €) | 0.000731 USDC | 2.17 | 0.124 (n=340) | REJECTED | sim_below_estimate(7668<9287), p_lower_below_threshold(0.12<0.75) |
| 53097265 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.809626 USDC | 0.009287 USDC | 0.000000 USDC | 0.006937 USDC | 0.002350 USDC (0.0022 €) | — | 2.17 | 0.124 (n=340) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53097384 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.029956 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | — | 0.34 | 0.180 (n=175) | REJECTED | below_safety_margin(1015649011794<5991215601366), p_lower_below_threshold(0.18<0.75) |
| 53097385 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.029956 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | — | 0.34 | 0.180 (n=175) | REJECTED | below_safety_margin(1015649011794<5991215601366), p_lower_below_threshold(0.18<0.75) |
| 53097385 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.030226 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0022 €) | — | 0.34 | 0.180 (n=175) | REJECTED | below_safety_margin(1015135920280<6045265594306), p_lower_below_threshold(0.18<0.75) |
| 53097264 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004639 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | 0.000000 WETH | 2.17 | 0.124 (n=340) | REJECTED | sim_below_estimate(3323061924971<4017824617411), p_lower_below_threshold(0.12<0.75) |
| 53097265 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004639 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 2.17 | 0.124 (n=340) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53097171 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 112.631959 USDC | 0.007066 USDC | 0.000000 USDC | 0.005519 USDC | 0.001547 USDC (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(1547<22526), reliability_not_demonstrated |
| 53097171 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 112.631959 USDC | 0.007066 USDC | 0.000000 USDC | 0.005519 USDC | 0.001547 USDC (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(1547<22526), reliability_not_demonstrated |
| 53097171 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.049240 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(665141777599<9847954143486), reliability_not_demonstrated |
| 53097171 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.049240 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(665141777599<9847954143486), reliability_not_demonstrated |
| 53097384 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 33.514465 USDC | 0.008000 USDC | 0.000000 USDC | 0.006954 USDC | 0.001046 USDC (0.0010 €) | — | 0.31 | 0.180 (n=175) | REJECTED | below_safety_margin(1046<6702), p_lower_below_threshold(0.18<0.75) |
| 53097385 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 33.514465 USDC | 0.008000 USDC | 0.000000 USDC | 0.006954 USDC | 0.001046 USDC (0.0010 €) | — | 0.31 | 0.180 (n=175) | REJECTED | below_safety_margin(1046<6702), p_lower_below_threshold(0.18<0.75) |
| 53097384 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.014560 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 0.31 | 0.180 (n=175) | REJECTED | below_safety_margin(450691947201<2911906157496), p_lower_below_threshold(0.18<0.75) |
| 53097385 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.014560 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 0.31 | 0.180 (n=175) | REJECTED | below_safety_margin(450691947201<2911906157496), p_lower_below_threshold(0.18<0.75) |
| 53097385 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 33.396619 USDC | 0.007899 USDC | 0.000000 USDC | 0.006954 USDC | 0.000945 USDC (0.0009 €) | — | 0.28 | 0.180 (n=175) | REJECTED | below_safety_margin(945<6679), p_lower_below_threshold(0.18<0.75) |
| 53097385 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.014561 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0009 €) | — | 0.28 | 0.180 (n=175) | REJECTED | below_safety_margin(406900114376<2912286016579), p_lower_below_threshold(0.18<0.75) |
| 53097384 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000775 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.13 | 0.180 (n=175) | REJECTED | below_safety_margin(1<15), p_lower_below_threshold(0.18<0.75) |
| 53097385 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000775 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.13 | 0.180 (n=175) | REJECTED | below_safety_margin(1<15), stale_data(4576ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53097385 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000775 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.13 | 0.180 (n=175) | REJECTED | below_safety_margin(1<15), p_lower_below_threshold(0.18<0.75) |
| 53097384 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.026705 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.12 | 0.180 (n=175) | REJECTED | below_safety_margin(332382761937<5340963607936), p_lower_below_threshold(0.18<0.75) |
| 53097385 | WETH→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.026705 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0007 €) | — | 0.12 | 0.180 (n=175) | REJECTED | below_safety_margin(332382761937<5340963607936), stale_data(4570ms>4000.0), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 2590 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
