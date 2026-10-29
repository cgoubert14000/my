# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T01:43:24+00:00 ; durée 200.5 min ; blocs 53218407 → 53224426 (5959 vus)

## Connexion
- Requêtes RPC : 68454 ; erreurs : 83 ; latence p50/p95 : 189.0/1,755.8 ms
- Rafraîchissements d'état : 5960 ; âge des données au dernier bloc : 1.84 s ; changements de frais LP observés (pools à frais dynamiques) : 7037
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 751 ; cycles déclenchés par événement : 79 ; avance médiane sur le rafraîchissement multicall : 796 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,334.14 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 522 pools, 300 jetons, 19152 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 122, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 331, par paires 0), mesurés 524, sous le plancher de 10000.0 $ : 2 → gardés 522 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2360.669373, 'cbBTC': 81164.401586, 'AERO': 0.699093}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,677,839 | 2,334.142490 | 53224426 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,486,602 | 0.028951 | 53224426 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,881,307 | 0.000012 | 53224426 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,425,153 | 0.029024 | 53224426 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,332,646 | 2,328.473505 | 53224426 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,188,417 | 98.476473 | 53224426 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,008,059 | 0.001636 | 53224426 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,614,299 | 1.470794 | 53224426 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,756,825 | 0.028945 | 53224426 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 803 | 4,792,107 | 2,328.326937 | 53224426 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,453,574 | 2,327.996866 | 53224426 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,244,405 | 0.998959 | 53224426 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,624,508 | 38,813.716799 | 53224426 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 2,928,837 | 0.029010 | 53224426 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,490,496 | 98.500939 | 53224426 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 2,349,105 | 0.000012 | 53224426 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,130,182 | 1,217,279.567811 | 53224426 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,821,636 | 2,334.348683 | 53224426 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,820,117 | 0.018626 | 53224426 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,780,092 | 400.580203 | 53224426 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,764,285 | 0.000000 | 53224426 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,715,539 | 0.000012 | 53224426 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,692,985 | 0.000012 | 53224426 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 1,607,551 | 0.000012 | 53224426 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,128 | 1.588199 | 53224426 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,999 | 0.826762 | 53224426 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,170 | 3,423.989525 | 53224426 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,429,830 | 0.005393 | 53224426 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,384,912 | 13,819.947052 | 53224426 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,254,836 | 2,328.557269 | 53224426 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,240,092 | 0.000265 | 53224426 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,192,122 | 68.375509 | 53224426 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,150,068 | 36,683,292.056054 | 53224426 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,147,113 | 0.000266 | 53224426 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,147,083 | 1,085,075.208111 | 53224426 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,871 | 485,543.711898 | 53224426 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,105,594 | 0.000000 | 53224426 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,072,699 | 21,220,744.729631 | 53224426 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,059,483 | 74,151.081327 | 53224426 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,054,696 | 3,403.955264 | 53224426 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,053,111 | 16.429240 | 53224426 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,028,763 | 2,334.457082 | 53224426 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,013,515 | 60.942105 | 53224426 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 991,038 | 98.206122 | 53224426 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 989,523 | 0.042237 | 53224426 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 937,928 | 2,350.543271 | 53224426 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 923,986 | 1,056.731335 | 53224426 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 900,812 | 0.000558 | 53224426 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4595 | 878,009 | 18.021347 | 53224426 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 870,650 | 2.330852 | 53224426 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 839,386 | 17.592104 | 53224426 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 834,190 | 0.062762 | 53224426 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 790,383 | 0.802973 | 53224426 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 745,536 | 0.616469 | 53224426 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,026 | 4,646,737.595509 | 53224426 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 743,126 | 0.000008 | 53224426 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 708,605 | 136,652.936604 | 53224426 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2204 | 704,989 | 487,453.157925 | 53224426 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 651,168 | 0.102790 | 53224426 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 650,363 | 0.534013 | 53224426 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 6038 ; routes examinées : 115639776 ; candidats optimisés : 405936 ; net attendu > 0 : 148 ; dernier cycle 482.5 ms
- Rejets (moteur) : {'spread_below_threshold': 113789652, 'liquidity_below_min': 1436361, 'negative_expected_net': 405788, 'borrow_bound_too_small': 6033, 'cycle_budget_exhausted': 1794}
- Enregistrements de la session : 405936 ; net attendu > 0 : 148 ; simulés (eth_call de la vraie tx) : 16 (ok 16, échec 0) ; étiquettes ghost N+1 : 0/16 positives
- Décisions : {'REJECTED': 405936} ; motifs de rejet : {'below_safety_margin': 110, 'negative_expected_net': 405788, 'p_lower_below_threshold': 138, 'reliability_not_demonstrated': 10, 'stale_data': 32}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53220050 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,720.189536 USDC | 0.194471 USDC | 0.000000 USDC | 0.006015 USDC | 0.188456 USDC (0.1734 €) | — | 1.10 | 0.032 (n=111) | REJECTED | below_safety_margin(188456<344037), p_lower_below_threshold(0.03<0.75) |
| 53220050 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→USDC | 1,313.415456 USDC | 0.106189 USDC | 0.000000 USDC | 0.005657 USDC | 0.100532 USDC (0.0925 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(100532<262683), p_lower_below_threshold(0.03<0.75) |
| 53220644 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.008013 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0219 €) | 0.000010 WETH | 12.57 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 18.909534 USDC | 0.030843 USDC | 0.000000 USDC | 0.007091 USDC | 0.023752 USDC (0.0219 €) | — | 12.56 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007967 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0214 €) | 0.000010 WETH | 12.35 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 18.755953 USDC | 0.030303 USDC | 0.000000 USDC | 0.007091 USDC | 0.023212 USDC (0.0214 €) | — | 12.38 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007165 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0191 €) | 0.000009 WETH | 12.31 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 16.951352 USDC | 0.028238 USDC | 0.000000 USDC | 0.007450 USDC | 0.020788 USDC (0.0191 €) | — | 12.26 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007215 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0164 €) | — | 10.44 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 16.961312 USDC | 0.024850 USDC | 0.000000 USDC | 0.007091 USDC | 0.017759 USDC (0.0163 €) | — | 10.47 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007138 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0157 €) | — | 10.14 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 16.768812 USDC | 0.024161 USDC | 0.000000 USDC | 0.007091 USDC | 0.017070 USDC (0.0157 €) | — | 10.18 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007014 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0149 €) | — | 9.78 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 16.426008 USDC | 0.023261 USDC | 0.000000 USDC | 0.007091 USDC | 0.016170 USDC (0.0149 €) | — | 9.84 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 17.735437 USDC | 0.023238 USDC | 0.000000 USDC | 0.007098 USDC | 0.016140 USDC (0.0148 €) | — | 9.10 | 0.004 (n=70) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.007509 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0148 €) | 0.000007 WETH | 9.08 | 0.004 (n=70) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 17.595281 USDC | 0.022963 USDC | 0.000000 USDC | 0.007098 USDC | 0.015865 USDC (0.0146 €) | — | 9.02 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.007471 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0146 €) | 0.000007 WETH | 8.97 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.006845 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0142 €) | — | 9.57 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 16.078501 USDC | 0.022892 USDC | 0.000000 USDC | 0.007450 USDC | 0.015442 USDC (0.0142 €) | — | 9.60 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53222585 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 382.997752 USDC | 0.019625 USDC | 0.000000 USDC | 0.005299 USDC | 0.014326 USDC (0.0132 €) | — | 0.37 | 0.010 (n=28) | REJECTED | below_safety_margin(14326<76599), reliability_not_demonstrated |
| 53220948 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC | 0.000448 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0112 €) | 0.000000 cbBTC | 3.35 | 0.066 (n=164) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53220948 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→cbBTC→[aerodrome_slipstream]→WETH | 0.016113 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0112 €) | 0.000005 WETH | 3.20 | 0.066 (n=164) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53218704 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 14.056658 USDC | 0.017001 USDC | 0.000000 USDC | 0.007098 USDC | 0.009903 USDC (0.0091 €) | — | 7.05 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53218704 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.005930 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0091 €) | 0.000004 WETH | 7.05 | 0.139 (n=186) | REJECTED | p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3057 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
