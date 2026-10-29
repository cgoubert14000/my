# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T01:52:43+00:00 ; durée 209.82 min ; blocs 53218407 → 53224705 (6235 vus)

## Connexion
- Requêtes RPC : 71591 ; erreurs : 83 ; latence p50/p95 : 157.3/1,791.5 ms
- Rafraîchissements d'état : 6235 ; âge des données au dernier bloc : 2.76 s ; changements de frais LP observés (pools à frais dynamiques) : 7989
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 751 ; cycles déclenchés par événement : 79 ; avance médiane sur le rafraîchissement multicall : 796 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,316.93 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 522 pools, 300 jetons, 19152 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 122, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 331, par paires 0), mesurés 524, sous le plancher de 10000.0 $ : 2 → gardés 522 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2360.669373, 'cbBTC': 81164.401586, 'AERO': 0.699093}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,934,894 | 2,316.928285 | 53224706 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,367,045 | 0.028932 | 53224706 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,849,230 | 0.000012 | 53224706 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,357,467 | 0.028969 | 53224706 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,286,893 | 2,318.035390 | 53224706 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,128,342 | 98.468847 | 53224706 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,955,387 | 0.001632 | 53224706 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,583,893 | 1.484411 | 53224706 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,715,222 | 0.028934 | 53224706 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 833 | 4,763,555 | 2,317.225178 | 53224706 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,427,279 | 2,317.273250 | 53224706 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,215,893 | 0.998959 | 53224706 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,600,094 | 38,763.782676 | 53224706 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2540 | 2,907,697 | 0.028961 | 53224706 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,472,228 | 98.500939 | 53224706 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 2,338,929 | 0.000012 | 53224706 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,116,727 | 1,214,687.424040 | 53224706 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,306 | 0.018556 | 53224706 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,814,906 | 2,317.373343 | 53224706 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,764,974 | 402.181637 | 53224706 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,751,188 | 0.000000 | 53224706 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,708,297 | 0.000012 | 53224706 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,687,309 | 0.000012 | 53224706 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 1,601,281 | 0.000012 | 53224706 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,128 | 1.588199 | 53224706 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,999 | 0.826762 | 53224706 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,423,166 | 3,436.329976 | 53224706 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,397,748 | 0.005358 | 53224706 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,373,172 | 13,894.488043 | 53224706 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,247,919 | 2,318.018948 | 53224706 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,229,133 | 0.000264 | 53224706 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,192,113 | 68.376561 | 53224706 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,423 | 36,699,159.479503 | 53224706 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,138,623 | 1,085,075.208111 | 53224706 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,136,976 | 0.000266 | 53224706 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,115,324 | 487,020.084505 | 53224706 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,096,344 | 0.000000 | 53224706 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,063,644 | 21,260,405.893380 | 53224706 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,053,979 | 73,826.476040 | 53224706 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,049,306 | 16.593928 | 53224706 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/AERO | 10000 | 1,045,968 | 3,412.081029 | 53224706 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/USDC | 3000 | 1,024,968 | 2,317.240931 | 53224706 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,010,527 | 61.303091 | 53224706 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 984,360 | 0.042474 | 53224706 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 983,817 | 98.206122 | 53224706 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 935,198 | 2,333.390147 | 53224706 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 917,159 | 1,056.731453 | 53224706 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 894,168 | 0.000558 | 53224706 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4665 | 874,309 | 18.145861 | 53224706 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 864,590 | 2.329401 | 53224706 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | QUID/USDC | 100 | 837,232 | 0.063257 | 53224706 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 832,058 | 17.618210 | 53224706 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 784,554 | 0.802973 | 53224706 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,809 | 0.610445 | 53224706 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 738,963 | 4,641,418.424165 | 53224706 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 737,130 | 0.000008 | 53224706 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 703,020 | 136,792.585180 | 53224706 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2165 | 698,686 | 490,499.993399 | 53224706 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 654,286 | 0.103570 | 53224706 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 650,363 | 0.534013 | 53224706 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 6313 ; routes examinées : 120906576 ; candidats optimisés : 434304 ; net attendu > 0 : 468 ; dernier cycle 416.9 ms
- Rejets (moteur) : {'spread_below_threshold': 118954748, 'liquidity_below_min': 1507635, 'negative_expected_net': 433836, 'borrow_bound_too_small': 6308, 'cycle_budget_exhausted': 3581}
- Enregistrements de la session : 434304 ; net attendu > 0 : 468 ; simulés (eth_call de la vraie tx) : 36 (ok 34, échec 2) ; étiquettes ghost N+1 : 5/34 positives
- Décisions : {'REJECTED': 434304} ; motifs de rejet : {'below_safety_margin': 267, 'negative_expected_net': 433836, 'p_lower_below_threshold': 440, 'reliability_not_demonstrated': 28, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 2, 'stale_data': 35}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53220050 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,720.189536 USDC | 0.194471 USDC | 0.000000 USDC | 0.006015 USDC | 0.188456 USDC (0.1734 €) | — | 1.10 | 0.032 (n=111) | REJECTED | below_safety_margin(188456<344037), p_lower_below_threshold(0.03<0.75) |
| 53224574 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.124981 WETH | 0.000058 WETH | 0.000000 WETH | 0.000003 WETH | 0.000055 WETH (0.1173 €) | 0.000055 WETH | 4.38 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 288.859449 USDC | 0.134223 USDC | 0.000000 USDC | 0.007153 USDC | 0.127070 USDC (0.1169 €) | — | 4.40 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.154905 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1158 €) | 0.000054 WETH | 3.49 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 358.547290 USDC | 0.132641 USDC | 0.000000 USDC | 0.007153 USDC | 0.125488 USDC (0.1154 €) | — | 3.50 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.152020 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1127 €) | 0.000053 WETH | 3.46 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 352.977780 USDC | 0.129196 USDC | 0.000000 USDC | 0.007153 USDC | 0.122043 USDC (0.1123 €) | — | 3.46 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.152185 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1115 €) | — | 3.42 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 353.226538 USDC | 0.127946 USDC | 0.000000 USDC | 0.007153 USDC | 0.120793 USDC (0.1111 €) | — | 3.42 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53220050 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→USDC | 1,313.415456 USDC | 0.106189 USDC | 0.000000 USDC | 0.005657 USDC | 0.100532 USDC (0.0925 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(100532<262683), p_lower_below_threshold(0.03<0.75) |
| 53224574 | WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.050396 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0478 €) | — | 4.43 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC | 116.402747 USDC | 0.058968 USDC | 0.000000 USDC | 0.007153 USDC | 0.051815 USDC (0.0477 €) | — | 4.45 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000955 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0355 €) | — | 5.03 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 85.281842 USDC | 0.046012 USDC | 0.000000 USDC | 0.007514 USDC | 0.038498 USDC (0.0354 €) | — | 4.51 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 54.484703 USDC | 0.042520 USDC | 0.000000 USDC | 0.007153 USDC | 0.035367 USDC (0.0325 €) | — | 6.49 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.024629 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0325 €) | — | 6.16 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224599 | WETH→[uniswap_v3]→NOCK→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.016139 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0294 €) | 0.000014 WETH | 8.53 | 0.024 (n=150) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53224599 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→NOCK→[aerodrome]→USDC | 37.266632 USDC | 0.039202 USDC | 0.000000 USDC | 0.007375 USDC | 0.031827 USDC (0.0293 €) | — | 8.54 | 0.024 (n=150) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53224575 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000853 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0259 €) | — | 4.10 | 0.099 (n=333) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224575 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 76.762214 USDC | 0.034838 USDC | 0.000000 USDC | 0.007222 USDC | 0.027616 USDC (0.0254 €) | — | 3.60 | 0.099 (n=333) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224599 | WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.026187 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0239 €) | 0.000011 WETH | 4.28 | 0.099 (n=333) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224599 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC | 60.533798 USDC | 0.033632 USDC | 0.000000 USDC | 0.007730 USDC | 0.025902 USDC (0.0238 €) | — | 4.28 | 0.099 (n=333) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53220644 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.008013 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0219 €) | 0.000010 WETH | 12.57 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 18.909534 USDC | 0.030843 USDC | 0.000000 USDC | 0.007091 USDC | 0.023752 USDC (0.0219 €) | — | 12.56 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53220644 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.007967 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0214 €) | 0.000010 WETH | 12.35 | 0.004 (n=71) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 3075 ; taux observé 0.098 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
