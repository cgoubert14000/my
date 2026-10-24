# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T22:33:51+00:00 ; durée 319.94 min ; blocs 53036340 → 53045937 (9434 vus)

## Connexion
- Requêtes RPC : 116417 ; erreurs : 35 ; latence p50/p95 : 238.1/873.5 ms
- Rafraîchissements d'état : 9435 ; âge des données au dernier bloc : 1.06 s ; changements de frais LP observés (pools à frais dynamiques) : 10500
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 104366 ; cycles déclenchés par événement : 10641 ; avance médiane sur le rafraîchissement multicall : 407 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,338.58 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 306 jetons, 19348 routes
- Par DEX : uniswap_v3 139, aerodrome 216, aerodrome_slipstream 130, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3808 (énumérés 345, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 2 → gardés 530 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2311.365621, 'cbBTC': 80049.166907, 'AERO': 0.688082}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,306,259 | 2,338.582299 | 53045937 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,265,744 | 0.029100 | 53045937 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 10,596,663 | 97.029602 | 53045937 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,170,557 | 0.029071 | 53045937 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,514,198 | 0.000012 | 53045937 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,454,570 | 2,340.266095 | 53045937 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 8,023,009 | 1.442933 | 53045937 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,009,288 | 0.001647 | 53045937 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,667,985 | 2,340.689672 | 53045937 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,409,846 | 0.029102 | 53045937 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,457,209 | 2,340.546670 | 53045937 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,228,693 | 0.999829 | 53045937 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,863,807 | 34,688.685504 | 53045937 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,798,143 | 2,342.717959 | 53045937 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,258,610 | 0.029085 | 53045937 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,557,681 | 0.000012 | 53045937 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,488,997 | 97.061299 | 53045937 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,217,668 | 409.962919 | 53045937 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,111,982 | 1,243,064.919347 | 53045937 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,901,365 | 0.000000 | 53045937 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,901,289 | 0.000012 | 53045937 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,796,739 | 0.018158 | 53045937 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,728,869 | 0.000012 | 53045937 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,719,648 | 0.000012 | 53045937 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,573,392 | 0.000265 | 53045937 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,617 | 1.675565 | 53045937 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53045937 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,446,615 | 3,372.704730 | 53045937 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,414,917 | 0.005384 | 53045937 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,370,066 | 14,082.170084 | 53045937 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/AERO | 10000 | 1,277,708 | 3,348.684155 | 53045937 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,241,497 | 0.000266 | 53045937 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,237,813 | 2,340.170648 | 53045937 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,221,567 | 65.118992 | 53045937 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,198,892 | 0.000000 | 53045937 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,164,471 | 35,494,240.689132 | 53045937 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,130,450 | 1,122,839.144480 | 53045937 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,123,879 | 49.588129 | 53045937 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,116,426 | 497,654.493802 | 53045937 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,037,307 | 77,911.196975 | 53045937 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,028,575 | 17.505029 | 53045937 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,868 | 21,823,007.922020 | 53045937 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 950,910 | 17.097857 | 53045937 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | USDC/VVV | 3000 | 948,719 | 0.041507 | 53045937 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 925,765 | 2,323.794498 | 53045937 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 923,558 | 1,101.179718 | 53045937 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 921,976 | 2.307052 | 53045937 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 896,516 | 0.000551 | 53045937 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 882,905 | 17.826396 | 53045937 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 861,469 | 96.914711 | 53045937 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 848,066 | 2,335.828097 | 53045937 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 821,191 | 0.000009 | 53045937 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 818,950 | 0.060352 | 53045937 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 798,652 | 1.105879 | 53045937 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 791,809 | 0.803130 | 53045937 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,585 | 0.622757 | 53045937 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 739,233 | 4,723,422.155055 | 53045937 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 736,844 | 0.679611 | 53045937 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 710,603 | 136,276.894279 | 53045937 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 698,081 | 494,518.402332 | 53045937 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 20075 ; routes examinées : 388411100 ; candidats optimisés : 1558312 ; net attendu > 0 : 1357 ; dernier cycle 53.2 ms
- Rejets (moteur) : {'spread_below_threshold': 380106357, 'liquidity_below_min': 5598591, 'negative_expected_net': 1556955, 'pool_quarantined': 1080678, 'unquotable': 44675, 'borrow_bound_too_small': 20050, 'cycle_budget_exhausted': 2396}
- Enregistrements de la session : 1558309 ; net attendu > 0 : 1357 ; simulés (eth_call de la vraie tx) : 109 (ok 14, échec 95) ; étiquettes ghost N+1 : 1/73 positives
- Décisions : {'REJECTED': 1558309} ; motifs de rejet : {'below_safety_margin': 934, 'negative_expected_net': 1556952, 'p_lower_below_threshold': 1152, 'price_impact': 252, 'reliability_not_demonstrated': 205, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 95, 'stale_data': 18}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53036954 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 3,546.739603 USDC | 1.811470 USDC | 0.000000 USDC | 0.009061 USDC | 1.802409 USDC (1.6582 €) | — | 5.08 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.532620 WETH | 0.000782 WETH | 0.000000 WETH | 0.000004 WETH | 0.000778 WETH (1.6564 €) | — | 5.08 | 0.091 (n=243) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53036954 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 3,826.357676 USDC | 1.720634 USDC | 0.000000 USDC | 0.008008 USDC | 1.712626 USDC (1.5756 €) | — | 4.48 | 0.141 (n=127) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 1.652467 WETH | 0.000743 WETH | 0.000000 WETH | 0.000003 WETH | 0.000740 WETH (1.5739 €) | — | 4.48 | 0.141 (n=127) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53036954 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 3,323.053185 USDC | 1.344194 USDC | 0.000000 USDC | 0.008008 USDC | 1.336186 USDC (1.2293 €) | — | 4.02 | 0.141 (n=127) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.435795 WETH | 0.000581 WETH | 0.000000 WETH | 0.000003 WETH | 0.000577 WETH (1.2279 €) | — | 4.02 | 0.141 (n=127) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53036954 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 1,421.266103 USDC | 1.216057 USDC | 0.000000 USDC | 0.008710 USDC | 1.207347 USDC (1.1108 €) | — | 8.49 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.614260 WETH | 0.000525 WETH | 0.000000 WETH | 0.000004 WETH | 0.000521 WETH (1.1091 €) | — | 8.49 | 0.000 (n=37) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53036954 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 1,785.329026 USDC | 0.836589 USDC | 0.000000 USDC | 0.007657 USDC | 0.828932 USDC (0.7626 €) | — | 4.64 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.770840 WETH | 0.000361 WETH | 0.000000 WETH | 0.000003 WETH | 0.000358 WETH (0.7615 €) | — | 4.64 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 823.242012 USDC | 0.699259 USDC | 0.000000 USDC | 0.008008 USDC | 0.691251 USDC (0.6360 €) | — | 8.40 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.356252 WETH | 0.000302 WETH | 0.000000 WETH | 0.000003 WETH | 0.000299 WETH (0.6354 €) | — | 8.38 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53036954 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 875.588674 USDC | 0.434471 USDC | 0.000000 USDC | 0.008008 USDC | 0.426463 USDC (0.3923 €) | — | 4.87 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.378382 WETH | 0.000188 WETH | 0.000000 WETH | 0.000003 WETH | 0.000184 WETH (0.3920 €) | — | 4.87 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53037399 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,260.057391 USDC | 0.424675 USDC | 0.000000 USDC | 0.006292 USDC | 0.418383 USDC (0.3849 €) | — | 3.32 | 0.063 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.733205 WETH | 0.000159 WETH | 0.000000 WETH | 0.000003 WETH | 0.000156 WETH (0.3315 €) | — | 2.12 | 0.140 (n=289) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036954 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,702.398638 USDC | 0.367591 USDC | 0.000000 USDC | 0.007306 USDC | 0.360285 USDC (0.3315 €) | — | 2.12 | 0.140 (n=289) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53036954 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.020531 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3314 €) | — | 2.19 | 0.140 (n=289) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53039638 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 66.248154 USDC | 0.357873 USDC | 0.000000 USDC | 0.007022 USDC | 0.350851 USDC (0.3228 €) | — | 52.96 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 53039638 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.028393 WETH | 0.000153 WETH | 0.000000 WETH | 0.000003 WETH | 0.000150 WETH (0.3225 €) | — | 52.92 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53039638 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 65.697539 USDC | 0.354533 USDC | 0.000000 USDC | 0.007022 USDC | 0.347511 USDC (0.3197 €) | — | 52.90 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53039638 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.028162 WETH | 0.000152 WETH | 0.000000 WETH | 0.000003 WETH | 0.000149 WETH (0.3194 €) | — | 52.84 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53036954 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 805.153556 USDC | 0.349917 USDC | 0.000000 USDC | 0.007657 USDC | 0.342260 USDC (0.3149 €) | — | 4.25 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.348043 WETH | 0.000151 WETH | 0.000000 WETH | 0.000003 WETH | 0.000148 WETH (0.3146 €) | — | 4.25 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53039638 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 63.293188 USDC | 0.326580 USDC | 0.000000 USDC | 0.007022 USDC | 0.319558 USDC (0.2940 €) | — | 50.49 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2328 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
