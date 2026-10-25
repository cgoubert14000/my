# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T12:46:35+00:00 ; durée 151.51 min ; blocs 53066976 → 53071521 (4544 vus)

## Connexion
- Requêtes RPC : 56158 ; erreurs : 0 ; latence p50/p95 : 152.7/780.4 ms
- Rafraîchissements d'état : 4544 ; âge des données au dernier bloc : 2.48 s ; changements de frais LP observés (pools à frais dynamiques) : 5988
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 29398 ; cycles déclenchés par événement : 4165 ; avance médiane sur le rafraîchissement multicall : 317 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,332.22 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 304 jetons, 19588 routes
- Par DEX : uniswap_v3 141, aerodrome 216, aerodrome_slipstream 127, pancakeswap_v3 31, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 191 (rejetés 2) → 596 jetons ; pools candidats 3794 (énumérés 342, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 2 → gardés 530 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2322.777273, 'cbBTC': 80302.249053, 'AERO': 0.673854}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,067,942 | 2,332.215422 | 53071522 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,415,041 | 0.028999 | 53071522 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,198,928 | 0.029036 | 53071522 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,523,020 | 0.000012 | 53071522 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,939,831 | 94.594737 | 53071522 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,412,897 | 2,329.651976 | 53071522 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,605,250 | 1.456542 | 53071522 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,997,258 | 0.001639 | 53071522 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,516,829 | 2,330.499746 | 53071522 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,332,302 | 0.029010 | 53071522 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,418,962 | 2,330.566317 | 53071522 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,228,160 | 1.000001 | 53071522 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,851,175 | 34,725.908283 | 53071522 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,782,289 | 2,332.252890 | 53071522 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,219,455 | 0.029021 | 53071522 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,815,881 | 0.000012 | 53071522 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,499,614 | 94.521214 | 53071522 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,206,938 | 412.349546 | 53071522 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,115,460 | 1,232,243.786789 | 53071522 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,901,167 | 0.000012 | 53071522 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,888,781 | 0.000000 | 53071522 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,508 | 0.017688 | 53071522 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,729,876 | 0.000012 | 53071522 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,718,519 | 0.000012 | 53071522 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,564,044 | 0.000264 | 53071522 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53071522 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,208 | 0.826535 | 53071522 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,437,033 | 0.005565 | 53071522 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,968 | 3,393.238915 | 53071522 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,365,899 | 14,224.400450 | 53071522 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,902 | 2,329.680581 | 53071522 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,264,136 | 3,399.802637 | 53071522 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,978 | 0.000264 | 53071522 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,238 | 65.047554 | 53071522 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,162,199 | 35,412,972.372346 | 53071522 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,152,289 | 0.000000 | 53071522 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,124,039 | 1,129,503.568538 | 53071522 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,120,612 | 496,353.419182 | 53071522 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,073,706 | 54.330973 | 53071522 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,039,257 | 17.019979 | 53071522 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,028,988 | 21,537,463.803818 | 53071522 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,025,647 | 79,238.567972 | 53071522 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 964,693 | 0.040618 | 53071522 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 924,280 | 2,339.197561 | 53071522 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 917,600 | 2.308002 | 53071522 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 897,135 | 1,118.701327 | 53071522 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 896,529 | 0.000554 | 53071522 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 896,454 | 17.147926 | 53071522 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 872,140 | 18.190181 | 53071522 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 868,860 | 95.196920 | 53071522 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 846,936 | 2,332.253785 | 53071522 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 807,263 | 0.000009 | 53071522 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 789,654 | 0.803130 | 53071522 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,663 | 0.055714 | 53071522 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 779,690 | 1.105854 | 53071522 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,626 | 0.616007 | 53071522 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 739,886 | 4,689,943.862983 | 53071522 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 732,544 | 0.672084 | 53071522 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 711,160 | 135,334.022024 | 53071522 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 697,189 | 498,544.071195 | 53071522 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 8708 ; routes examinées : 170572304 ; candidats optimisés : 511272 ; net attendu > 0 : 364 ; dernier cycle 252.7 ms
- Rejets (moteur) : {'spread_below_threshold': 166966602, 'liquidity_below_min': 2876598, 'negative_expected_net': 510908, 'unquotable': 208944, 'borrow_bound_too_small': 8707, 'cycle_budget_exhausted': 181}
- Enregistrements de la session : 511272 ; net attendu > 0 : 364 ; simulés (eth_call de la vraie tx) : 35 (ok 17, échec 18) ; étiquettes ghost N+1 : 0/29 positives
- Décisions : {'REJECTED': 511272} ; motifs de rejet : {'below_safety_margin': 230, 'negative_expected_net': 510908, 'p_lower_below_threshold': 333, 'reliability_not_demonstrated': 31, 'simulation_failed': 18}

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
- Observations ghost : 2443 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
