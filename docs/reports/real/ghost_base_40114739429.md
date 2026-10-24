# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T19:30:05+00:00 ; durée 136.18 min ; blocs 53036340 → 53040427 (4040 vus)

## Connexion
- Requêtes RPC : 50129 ; erreurs : 5 ; latence p50/p95 : 228.3/725.2 ms
- Rafraîchissements d'état : 4040 ; âge des données au dernier bloc : 2.3 s ; changements de frais LP observés (pools à frais dynamiques) : 5369
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 51839 ; cycles déclenchés par événement : 5378 ; avance médiane sur le rafraîchissement multicall : 412 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,332.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 306 jetons, 19348 routes
- Par DEX : uniswap_v3 139, aerodrome 216, aerodrome_slipstream 130, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3808 (énumérés 345, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 2 → gardés 530 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2311.365621, 'cbBTC': 80049.166907, 'AERO': 0.688082}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,923,656 | 2,332.777111 | 53040426 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,221,739 | 0.029054 | 53040426 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,094,231 | 96.641161 | 53040426 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,150,021 | 0.028983 | 53040426 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,558,055 | 0.000012 | 53040426 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,739,260 | 1.434425 | 53040426 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,434,555 | 2,337.799617 | 53040427 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 7,645,766 | 0.028996 | 53040426 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,990,255 | 0.001641 | 53040426 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 6,290,917 | 0.000012 | 53040426 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,651,586 | 2,337.920420 | 53040426 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,364,996 | 0.029061 | 53040426 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 4,491,247 | 0.000012 | 53040426 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,445,740 | 2,337.669714 | 53040426 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,224,786 | 0.999829 | 53040426 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,845,124 | 34,852.921657 | 53040426 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,793,559 | 2,334.056704 | 53040426 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,756,188 | 2,346.330412 | 53040426 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,487,454 | 96.676014 | 53040426 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,215,288 | 408.380245 | 53040426 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,106,740 | 1,243,064.919347 | 53040426 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,899,449 | 0.000012 | 53040426 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,895,661 | 0.000000 | 53040426 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,788,739 | 0.018023 | 53040426 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,729,158 | 0.000012 | 53040426 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,570,024 | 0.000264 | 53040426 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,469,617 | 1.675565 | 53040426 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53040426 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,449,451 | 3,345.279739 | 53040426 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,370,017 | 14,071.233594 | 53040426 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,367,095 | 0.005182 | 53040426 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/AERO | 10000 | 1,282,663 | 3,341.127574 | 53040426 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,238,242 | 2,337.749163 | 53040426 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,961 | 0.000266 | 53040426 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,778 | 65.096518 | 53040426 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,199,135 | 0.000000 | 53040426 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,162,006 | 35,455,458.932345 | 53040426 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,128,480 | 1,122,243.809861 | 53040426 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,123,821 | 49.593182 | 53040426 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,111,299 | 500,570.621406 | 53040426 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,039,150 | 77,250.084504 | 53040426 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,025,283 | 17.659720 | 53040426 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,021,330 | 21,823,007.922020 | 53040426 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 950,439 | 0.041363 | 53040426 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 949,536 | 17.087566 | 53040426 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 948,492 | 23.207081 | 53040426 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 926,612 | 1,092.665038 | 53040426 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 924,111 | 2,316.453656 | 53040426 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 919,795 | 2.306651 | 53040426 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 891,855 | 0.000548 | 53040426 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,153 | 17.917068 | 53040426 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 866,830 | 96.914814 | 53040426 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 846,984 | 2,331.573930 | 53040426 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 823,600 | 0.000009 | 53040426 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,859 | 0.059398 | 53040426 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 796,671 | 1.105883 | 53040426 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 789,844 | 0.803130 | 53040426 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,346 | 0.622473 | 53040426 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 737,812 | 4,718,121.203218 | 53040426 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 735,595 | 0.677428 | 53040426 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 9417 ; routes examinées : 182200116 ; candidats optimisés : 768123 ; net attendu > 0 : 986 ; dernier cycle 95.8 ms
- Rejets (moteur) : {'spread_below_threshold': 178073379, 'liquidity_below_min': 2255106, 'pool_quarantined': 1080678, 'negative_expected_net': 767137, 'unquotable': 12035, 'borrow_bound_too_small': 9406, 'cycle_budget_exhausted': 1389}
- Enregistrements de la session : 768123 ; net attendu > 0 : 986 ; simulés (eth_call de la vraie tx) : 88 (ok 3, échec 85) ; étiquettes ghost N+1 : 0/56 positives
- Décisions : {'REJECTED': 768123} ; motifs de rejet : {'below_safety_margin': 627, 'negative_expected_net': 767137, 'p_lower_below_threshold': 849, 'price_impact': 252, 'reliability_not_demonstrated': 137, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 85, 'stale_data': 18}

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
- Observations ghost : 2311 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
