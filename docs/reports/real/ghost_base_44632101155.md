# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T02:37:31+00:00 ; durée 219.91 min ; blocs 59693368 → 59759333 (10594 vus)

## Connexion
- Requêtes RPC : 128728 ; erreurs : 0 ; latence p50/p95 : 478.3/1,494.5 ms
- Rafraîchissements d'état : 10594 ; âge des données au dernier bloc : 8.46 s ; changements de frais LP observés (pools à frais dynamiques) : 9563
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22457 ; cycles déclenchés par événement : 5974 ; avance médiane sur le rafraîchissement multicall : 404 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,730.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 425 pools, 247 jetons, 12948 routes
- Par DEX : uniswap_v3 129, aerodrome 171, aerodrome_slipstream 86, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 145 (rejetés 2) → 550 jetons ; pools candidats 3571 (énumérés 255, par paires 0), mesurés 427, sous le plancher de 10000.0 $ : 2 → gardés 425 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1759.475588, 'cbBTC': 62145.383052, 'AERO': 0.418705}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 84,414,509 | 1,730.207923 | 59759361 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,971,371 | 0.028146 | 59759361 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,058,970 | 1,731.509172 | 59759361 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,593,057 | 0.028191 | 59759361 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,464,446 | 83.189723 | 59759361 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,970,710 | 0.000016 | 59759361 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,107,077 | 0.028150 | 59759361 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,550,630 | 2.441579 | 59759361 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,235,327 | 0.999456 | 59759361 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,229,954 | 1,730.926949 | 59759361 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,686,505 | 38,817.493621 | 59759361 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 208 | 2,271,335 | 1,731.099150 | 59759361 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,052,397 | 0.000016 | 59759361 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,689,338 | 0.028187 | 59759361 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,626,023 | 1,147,728.379701 | 59759361 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,389 | 0.844466 | 59759361 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,375,357 | 0.000016 | 59759361 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,316,610 | 0.000000 | 59759361 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,234,098 | 0.000016 | 59759361 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,233,902 | 0.006506 | 59759361 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,083,391 | 15.275512 | 59759361 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,060,053 | 86.473728 | 59759361 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,030,716 | 452.154449 | 59759361 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 996,579 | 16,044.186002 | 59759361 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 995,855 | 82.605482 | 59759361 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 979,046 | 1,730.527574 | 59759361 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 972,697 | 4,218.645921 | 59759361 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 952,984 | 1,730.810364 | 59759361 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 907,363 | 31,122,873.728043 | 59759361 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 882,408 | 0.048151 | 59759361 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 842,165 | 60.324070 | 59759361 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 809,597 | 523,898.145691 | 59759361 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 785,623 | 0.000000 | 59759361 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 779,703 | 22,197,854.400916 | 59759361 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 775,372 | 0.001532 | 59759361 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 728,823 | 1,074.661594 | 59759361 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | XDP/USDC | 100 | 728,117 | 0.014853 | 59759361 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/SAPIEN | 5005 | 724,793 | 24.142928 | 59759361 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 718,498 | 0.045875 | 59759361 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| pancakeswap_v3 | WETH/USDC | 500 | 717,823 | 1,731.598992 | 59759361 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 10000 | 691,205 | 1,739.551825 | 59759361 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | TIG/USDC | 10000 | 589,088 | 0.436156 | 59759361 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 587,281 | 0.798842 | 59759361 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 587,133 | 1,730.934644 | 59759361 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 549,111 | 4,723,759.644300 | 59759361 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 532,638 | 4,203.495683 | 59759361 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 509,122 | 1.386517 | 59759361 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 504,362 | 527,639.647320 | 59759361 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 493,338 | 0.031191 | 59759361 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 471,037 | 171,657.792315 | 59759361 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,610 | 1.001527 | 59759361 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 435,031 | 0.000007 | 59759361 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 402,883 | 0.056066 | 59759361 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 396,927 | 1,074.617337 | 59759361 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/UNI | 10000 | 382,611 | 356.312784 | 59759361 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 380,337 | 23.779881 | 59759361 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 379,445 | 845,002.327871 | 59759361 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 367,077 | 0.056030 | 59759361 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 360,092 | 0.000237 | 59759361 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2718 | 357,241 | 83.219857 | 59759361 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 16567 ; routes examinées : 214509516 ; candidats optimisés : 271890 ; net attendu > 0 : 168 ; dernier cycle 480.2 ms
- Rejets (moteur) : {'spread_below_threshold': 210308929, 'liquidity_below_min': 2537698, 'negative_expected_net': 271722, 'borrow_bound_too_small': 20670, 'cycle_budget_exhausted': 935}
- Enregistrements de la session : 92796 ; net attendu > 0 : 168 ; simulés (eth_call de la vraie tx) : 8 (ok 8, échec 0) ; étiquettes ghost N+1 : 6/8 positives
- Décisions : {'REJECTED': 92796} ; motifs de rejet : {'below_safety_margin': 128, 'negative_expected_net': 92628, 'p_lower_below_threshold': 168, 'price_impact': 36, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59732431 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 69.931296 USDC | 0.030186 USDC | 0.000000 USDC | 0.005521 USDC | 0.024665 USDC (0.0227 €) | — | 3.53 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.039909 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0226 €) | 0.000014 WETH | 3.50 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59732431 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 66.903932 USDC | 0.027131 USDC | 0.000000 USDC | 0.005521 USDC | 0.021610 USDC (0.0199 €) | — | 3.23 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59732431 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.038074 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0198 €) | 0.000011 WETH | 3.21 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59746276 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.055155 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0180 €) | 0.000011 WETH | 2.04 | 0.281 (n=245) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 95.748973 USDC | 0.024811 USDC | 0.000000 USDC | 0.005271 USDC | 0.019540 USDC (0.0180 €) | — | 2.04 | 0.281 (n=245) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59746276 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.083431 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0178 €) | — | 1.33 | 0.281 (n=245) | REJECTED | below_safety_margin(11102813876630<16686108641199), p_lower_below_threshold(0.28<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 144.300977 USDC | 0.024810 USDC | 0.000000 USDC | 0.005550 USDC | 0.019260 USDC (0.0177 €) | — | 1.33 | 0.281 (n=245) | REJECTED | below_safety_margin(19260<28860), p_lower_below_threshold(0.28<0.75) |
| 59752040 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000992 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0130 €) | 0.000000 cbBTC | 2.32 | 0.111 (n=378) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59752040 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 61.320491 USDC | 0.018020 USDC | 0.000000 USDC | 0.003937 USDC | 0.014083 USDC (0.0130 €) | 0.014083 USDC | 2.30 | 0.111 (n=378) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59732431 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 37.378666 USDC | 0.018956 USDC | 0.000000 USDC | 0.005268 USDC | 0.013688 USDC (0.0126 €) | — | 3.66 | 0.184 (n=331) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.021338 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0125 €) | 0.000008 WETH | 3.63 | 0.184 (n=331) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 59732431 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.829297 USDC | 0.017145 USDC | 0.000000 USDC | 0.005268 USDC | 0.011877 USDC (0.0109 €) | — | 3.31 | 0.305 (n=236) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 59732431 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.020353 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0109 €) | — | 3.30 | 0.305 (n=236) | REJECTED | p_lower_below_threshold(0.30<0.75) |
| 59752040 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 140.581022 USDC | 0.015129 USDC | 0.000000 USDC | 0.003937 USDC | 0.011192 USDC (0.0103 €) | — | 0.80 | 0.111 (n=378) | REJECTED | below_safety_margin(11192<28116), p_lower_below_threshold(0.11<0.75) |
| 59752040 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001935 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0102 €) | — | 0.93 | 0.111 (n=378) | REJECTED | below_safety_margin(18<38), p_lower_below_threshold(0.11<0.75) |
| 59732431 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 25.472668 USDC | 0.015949 USDC | 0.000000 USDC | 0.005521 USDC | 0.010428 USDC (0.0096 €) | — | 4.09 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.014361 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0096 €) | — | 4.11 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59746276 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.024440 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0086 €) | 0.000005 WETH | 2.19 | 0.355 (n=643) | REJECTED | p_lower_below_threshold(0.36<0.75) |
| 59732431 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 24.353050 USDC | 0.014808 USDC | 0.000000 USDC | 0.005521 USDC | 0.009287 USDC (0.0085 €) | — | 3.81 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59746276 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.030615 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0085 €) | — | 1.74 | 0.363 (n=155) | REJECTED | below_safety_margin(5332004153913<6123076512000), p_lower_below_threshold(0.36<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 42.248714 USDC | 0.014796 USDC | 0.000000 USDC | 0.005525 USDC | 0.009271 USDC (0.0085 €) | — | 2.19 | 0.355 (n=643) | REJECTED | p_lower_below_threshold(0.36<0.75) |
| 59732431 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 24.305317 USDC | 0.014772 USDC | 0.000000 USDC | 0.005521 USDC | 0.009251 USDC (0.0085 €) | — | 3.81 | 0.216 (n=1294) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 59732431 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.013785 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0085 €) | — | 3.81 | 0.334 (n=623) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59746276 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 52.979752 USDC | 0.014514 USDC | 0.000000 USDC | 0.005271 USDC | 0.009243 USDC (0.0085 €) | — | 1.74 | 0.363 (n=155) | REJECTED | below_safety_margin(9243<10595), p_lower_below_threshold(0.36<0.75) |

## Fiabilité et décision
- Observations ghost : 8590 ; taux observé 0.228 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
