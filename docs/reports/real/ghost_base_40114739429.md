# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T18:49:32+00:00 ; durée 95.63 min ; blocs 53036340 → 53039209 (2830 vus)

## Connexion
- Requêtes RPC : 35097 ; erreurs : 5 ; latence p50/p95 : 244.1/1,069.4 ms
- Rafraîchissements d'état : 2830 ; âge des données au dernier bloc : 4.56 s ; changements de frais LP observés (pools à frais dynamiques) : 3765
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 36481 ; cycles déclenchés par événement : 4199 ; avance médiane sur le rafraîchissement multicall : 428 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,327.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 306 jetons, 19348 routes
- Par DEX : uniswap_v3 139, aerodrome 216 (quarantaine 2), aerodrome_slipstream 130, pancakeswap_v3 30, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3808 (énumérés 345, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 2 → gardés 530 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2311.365621, 'cbBTC': 80049.166907, 'AERO': 0.688082}
- Pools en quarantaine : 2 — aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 53039497; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 53039497

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,646,524 | 2,327.890895 | 53039210 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,174,041 | 0.029036 | 53039210 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,056,754 | 96.835952 | 53039210 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,130,599 | 0.028983 | 53039210 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,553,365 | 0.000012 | 53039210 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,758,859 | 1.429629 | 53039210 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/USDC | 500 | 8,407,049 | 2,331.908151 | 53039210 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 7,631,606 | 0.028995 | 53039210 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,982,812 | 0.001642 | 53039210 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 6,287,261 | 0.000012 | 53039210 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,641,728 | 2,331.851273 | 53039210 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,373,430 | 0.029038 | 53039210 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 4,502,622 | 0.000012 | 53039210 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,437,732 | 2,331.758076 | 53039210 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,218,540 | 0.999830 | 53039210 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,838,448 | 34,827.897394 | 53039210 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,789,583 | 2,328.740446 | 53039210 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,752,724 | 2,341.273437 | 53039210 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,479,683 | 96.812006 | 53039210 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,209,379 | 409.011003 | 53039210 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,102,327 | 1,243,064.919347 | 53039210 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,897,974 | 0.000012 | 53039210 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,891,700 | 0.000000 | 53039210 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,788,831 | 0.018026 | 53039210 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,732,762 | 0.000012 | 53039210 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,566,735 | 0.000264 | 53039210 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,489,581 | 1.675565 | 53039210 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,852 | 0.826899 | 53039210 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,450,515 | 3,329.987368 | 53039210 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,366,826 | 14,091.338912 | 53039210 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,364,232 | 0.005182 | 53039210 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/AERO | 10000 | 1,283,479 | 3,341.127574 | 53039210 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,748 | 2,332.149742 | 53039210 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,235,363 | 0.000266 | 53039210 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,224,787 | 64.777090 | 53039210 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,172,404 | 0.000000 | 53039210 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,159,601 | 35,452,918.487825 | 53039210 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,126,135 | 1,122,207.256227 | 53039210 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,121,889 | 49.764171 | 53039210 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,108,942 | 500,570.621406 | 53039210 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,037,084 | 77,220.359643 | 53039210 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,023,214 | 17.758185 | 53039210 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,019,110 | 21,823,007.922020 | 53039210 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 947,259 | 17.093443 | 53039210 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | USDC/VVV | 3000 | 947,256 | 0.041559 | 53039210 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 946,999 | 23.207061 | 53039210 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 926,259 | 1,091.100791 | 53039210 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 918,006 | 2.306135 | 53039210 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 889,987 | 0.000548 | 53039210 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 879,754 | 17.930201 | 53039210 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 864,158 | 97.275922 | 53039210 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 846,094 | 2,327.746879 | 53039210 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 824,408 | 0.000009 | 53039210 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,212 | 0.059610 | 53039210 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 796,050 | 1.105883 | 53039210 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 788,205 | 0.803098 | 53039210 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 781,803 | 2,311.545045 | 53039210 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,655 | 0.619399 | 53039210 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 740,885 | 4,659,381.096911 | 53039210 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 735,594 | 0.677428 | 53039210 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 7028 ; routes examinées : 135977744 ; candidats optimisés : 591238 ; net attendu > 0 : 800 ; dernier cycle 87.6 ms
- Rejets (moteur) : {'spread_below_threshold': 132885670, 'liquidity_below_min': 1627057, 'pool_quarantined': 856926, 'negative_expected_net': 590438, 'unquotable': 8595, 'borrow_bound_too_small': 7019, 'cycle_budget_exhausted': 1239}
- Enregistrements de la session : 591238 ; net attendu > 0 : 800 ; simulés (eth_call de la vraie tx) : 75 (ok 3, échec 72) ; étiquettes ghost N+1 : 0/51 positives
- Décisions : {'REJECTED': 591238} ; motifs de rejet : {'below_safety_margin': 473, 'negative_expected_net': 590438, 'p_lower_below_threshold': 693, 'price_impact': 240, 'reliability_not_demonstrated': 107, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 72, 'stale_data': 10}

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
| 53036954 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 805.153556 USDC | 0.349917 USDC | 0.000000 USDC | 0.007657 USDC | 0.342260 USDC (0.3149 €) | — | 4.25 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.348043 WETH | 0.000151 WETH | 0.000000 WETH | 0.000003 WETH | 0.000148 WETH (0.3146 €) | — | 4.25 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 668.059828 USDC | 0.306813 USDC | 0.000000 USDC | 0.007657 USDC | 0.299156 USDC (0.2752 €) | — | 4.48 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.288447 WETH | 0.000133 WETH | 0.000000 WETH | 0.000003 WETH | 0.000129 WETH (0.2749 €) | — | 4.48 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 716.976085 USDC | 0.278834 USDC | 0.000000 USDC | 0.007657 USDC | 0.271177 USDC (0.2495 €) | — | 3.78 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53036954 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.309745 WETH | 0.000120 WETH | 0.000000 WETH | 0.000003 WETH | 0.000117 WETH (0.2492 €) | — | 3.78 | 0.091 (n=243) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53037034 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 91.645027 USDC | 0.196533 USDC | 0.000000 USDC | 0.005197 USDC | 0.191336 USDC (0.1760 €) | — | 20.88 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2306 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
