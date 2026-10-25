# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T11:04:15+00:00 ; durée 49.17 min ; blocs 53066976 → 53068453 (1475 vus)

## Connexion
- Requêtes RPC : 18479 ; erreurs : 0 ; latence p50/p95 : 187.3/878.0 ms
- Rafraîchissements d'état : 1475 ; âge des données au dernier bloc : 2.44 s ; changements de frais LP observés (pools à frais dynamiques) : 1388
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15362 ; cycles déclenchés par événement : 2221 ; avance médiane sur le rafraîchissement multicall : 290 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,324.96 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 304 jetons, 19588 routes
- Par DEX : uniswap_v3 141, aerodrome 216, aerodrome_slipstream 127, pancakeswap_v3 31, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 191 (rejetés 2) → 596 jetons ; pools candidats 3794 (énumérés 342, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 2 → gardés 530 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2322.777273, 'cbBTC': 80302.249053, 'AERO': 0.673854}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,705,466 | 2,324.958046 | 53068452 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,194,842 | 0.028994 | 53068452 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,174,001 | 0.029036 | 53068452 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,510,643 | 0.000012 | 53068452 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,866,104 | 95.577088 | 53068452 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,390,948 | 2,328.653755 | 53068453 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,557,482 | 1.485526 | 53068452 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,979,808 | 0.001640 | 53068452 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,507,144 | 2,328.334312 | 53068452 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,427,346 | 0.028988 | 53068452 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,407,132 | 2,328.143773 | 53068452 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,219,877 | 0.999704 | 53068452 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,846,873 | 34,587.359822 | 53068452 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,776,960 | 2,325.400685 | 53068452 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,212,075 | 0.029021 | 53068452 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 2,819,591 | 0.000012 | 53068452 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,492,658 | 95.602586 | 53068452 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,196,701 | 413.980560 | 53068452 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,110,429 | 1,230,433.085261 | 53068452 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,898,290 | 0.000012 | 53068452 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,882,892 | 0.000000 | 53068452 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,767,920 | 0.017661 | 53068452 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,726,591 | 0.000012 | 53068452 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 1,715,469 | 0.000012 | 53068452 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,560,705 | 0.000265 | 53068452 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,471,982 | 0.005657 | 53068452 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53068452 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,526 | 0.826205 | 53068452 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,418,818 | 3,456.661811 | 53068452 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,359,592 | 14,274.885539 | 53068452 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,286,115 | 2,328.832768 | 53068452 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,251,295 | 3,445.976476 | 53068452 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,234,462 | 0.000264 | 53068452 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,484 | 65.021354 | 53068452 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,158,583 | 35,412,972.372346 | 53068452 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,152,048 | 0.000000 | 53068452 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,121,585 | 1,127,401.606359 | 53068452 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,111,456 | 495,917.755902 | 53068452 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,069,277 | 54.781992 | 53068452 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,032,785 | 17.311362 | 53068452 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,026,010 | 21,529,738.732403 | 53068452 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,023,142 | 79,132.166610 | 53068452 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 956,091 | 0.041105 | 53068452 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 923,083 | 2,339.197561 | 53068452 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 914,765 | 2.307924 | 53068452 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 909,654 | 17.143691 | 53068452 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/MORPHO | 3000 | 894,766 | 1,119.726632 | 53068452 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 894,008 | 0.000554 | 53068452 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 872,027 | 18.193974 | 53068452 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 862,130 | 95.782023 | 53068452 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 845,612 | 2,324.831624 | 53068452 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 805,946 | 0.000008 | 53068452 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,792 | 0.056181 | 53068452 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 787,196 | 0.803130 | 53068452 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 777,264 | 1.105854 | 53068452 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 738,590 | 0.613210 | 53068452 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 735,708 | 4,713,800.014077 | 53068452 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 732,668 | 0.672300 | 53068452 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 710,513 | 134,736.555188 | 53068452 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 695,392 | 499,895.830413 | 53068452 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 3695 ; routes examinées : 72377660 ; candidats optimisés : 215977 ; net attendu > 0 : 146 ; dernier cycle 103.6 ms
- Rejets (moteur) : {'spread_below_threshold': 70575595, 'liquidity_below_min': 1493656, 'negative_expected_net': 215831, 'unquotable': 88656, 'borrow_bound_too_small': 3694, 'cycle_budget_exhausted': 82}
- Enregistrements de la session : 215977 ; net attendu > 0 : 146 ; simulés (eth_call de la vraie tx) : 8 (ok 2, échec 6) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 215977} ; motifs de rejet : {'below_safety_margin': 88, 'negative_expected_net': 215831, 'p_lower_below_threshold': 130, 'reliability_not_demonstrated': 16, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53068345 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 4,086.699397 USDC | 0.870408 USDC | 0.000000 USDC | 0.007728 USDC | 0.862680 USDC (0.7937 €) | — | 2.11 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.050617 cbBTC | 0.000011 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000011 cbBTC (0.7922 €) | — | 2.12 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 1.780123 WETH | 0.000374 WETH | 0.000000 WETH | 0.000003 WETH | 0.000370 WETH (0.7911 €) | — | 2.08 | 0.137 (n=308) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53068345 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,207.464814 USDC | 0.690821 USDC | 0.000000 USDC | 0.007373 USDC | 0.683448 USDC (0.6288 €) | — | 2.13 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.374882 WETH | 0.000297 WETH | 0.000000 WETH | 0.000003 WETH | 0.000294 WETH (0.6273 €) | — | 2.14 | 0.137 (n=308) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53068345 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.038760 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6271 €) | — | 2.20 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,081.235514 USDC | 0.434208 USDC | 0.000000 USDC | 0.008082 USDC | 0.426126 USDC (0.3920 €) | — | 2.05 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.882847 WETH | 0.000186 WETH | 0.000000 WETH | 0.000003 WETH | 0.000183 WETH (0.3909 €) | — | 2.07 | 0.137 (n=308) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53068345 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.024751 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3906 €) | — | 2.14 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,862.038370 USDC | 0.389992 USDC | 0.000000 USDC | 0.007728 USDC | 0.382264 USDC (0.3517 €) | — | 2.05 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.768199 WETH | 0.000168 WETH | 0.000000 WETH | 0.000003 WETH | 0.000164 WETH (0.3509 €) | — | 2.14 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53068345 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.021649 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3508 €) | — | 2.20 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53068345 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,936.600975 USDC | 0.370529 USDC | 0.000000 USDC | 0.007373 USDC | 0.363156 USDC (0.3341 €) | — | 1.88 | 0.137 (n=308) | REJECTED | below_safety_margin(363156<387320), p_lower_below_threshold(0.14<0.75) |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.854616 WETH | 0.000159 WETH | 0.000000 WETH | 0.000003 WETH | 0.000156 WETH (0.3334 €) | — | 1.83 | 0.137 (n=308) | REJECTED | below_safety_margin(156013860670299<170923123467511), p_lower_below_threshold(0.14<0.75) |
| 53068345 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.024188 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3331 €) | — | 1.87 | 0.137 (n=308) | REJECTED | below_safety_margin(452<483), p_lower_below_threshold(0.14<0.75) |
| 53068345 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,737.153672 USDC | 0.362511 USDC | 0.000000 USDC | 0.007019 USDC | 0.355492 USDC (0.3271 €) | — | 2.05 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.020692 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3265 €) | — | 2.14 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.747032 WETH | 0.000156 WETH | 0.000000 WETH | 0.000003 WETH | 0.000153 WETH (0.3261 €) | — | 2.04 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,613.323622 USDC | 0.332564 USDC | 0.000000 USDC | 0.007019 USDC | 0.325545 USDC (0.2995 €) | — | 2.02 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.018559 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2992 €) | — | 2.19 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.640025 WETH | 0.000143 WETH | 0.000000 WETH | 0.000003 WETH | 0.000140 WETH (0.2986 €) | — | 2.18 | 0.137 (n=308) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53068345 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,748.991719 USDC | 0.329713 USDC | 0.000000 USDC | 0.007019 USDC | 0.322694 USDC (0.2969 €) | — | 1.85 | 0.137 (n=308) | REJECTED | below_safety_margin(322694<349798), p_lower_below_threshold(0.14<0.75) |
| 53068345 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.021065 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2963 €) | — | 1.91 | 0.137 (n=308) | REJECTED | below_safety_margin(402<421), p_lower_below_threshold(0.14<0.75) |
| 53068345 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.750652 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000138 WETH (0.2959 €) | — | 1.84 | 0.137 (n=308) | REJECTED | below_safety_margin(138478322616582<150130386607736), p_lower_below_threshold(0.14<0.75) |
| 53067683 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 47.798421 USDC | 0.188372 USDC | 0.000000 USDC | 0.004895 USDC | 0.183477 USDC (0.1688 €) | — | 38.39 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2421 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
