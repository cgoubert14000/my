# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T03:17:28+00:00 ; durée 259.86 min ; blocs 59693368 → 59771310 (12193 vus)

## Connexion
- Requêtes RPC : 149558 ; erreurs : 0 ; latence p50/p95 : 489.4/1,470.2 ms
- Rafraîchissements d'état : 12193 ; âge des données au dernier bloc : 9.56 s ; changements de frais LP observés (pools à frais dynamiques) : 11827
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 26828 ; cycles déclenchés par événement : 6984 ; avance médiane sur le rafraîchissement multicall : 524 ms
- Gaz : base fee 0.005061 gwei ; prix ETH (pool le plus profond) : 1,738.86 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 425 pools, 247 jetons, 12948 routes
- Par DEX : uniswap_v3 129, aerodrome 171, aerodrome_slipstream 86, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 145 (rejetés 2) → 550 jetons ; pools candidats 3571 (énumérés 255, par paires 0), mesurés 427, sous le plancher de 10000.0 $ : 2 → gardés 425 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1759.475588, 'cbBTC': 62145.383052, 'AERO': 0.418705}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 84,744,223 | 1,738.856711 | 59771309 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,083,764 | 0.028099 | 59771309 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,110,249 | 1,743.305035 | 59771309 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,635,213 | 0.028148 | 59771309 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,481,146 | 83.591153 | 59771309 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,003,567 | 0.000016 | 59771309 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,129,743 | 0.028108 | 59771309 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,559,341 | 2.429641 | 59771309 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,256,899 | 0.999457 | 59771309 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,244,320 | 1,744.133315 | 59771310 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,691,883 | 39,050.016069 | 59771309 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 355 | 2,281,628 | 1,743.284450 | 59771309 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,063,498 | 0.000016 | 59771309 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 1,698,298 | 0.028135 | 59771309 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,634,151 | 1,147,728.379701 | 59771309 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,389 | 0.844466 | 59771309 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,383,223 | 0.000016 | 59771309 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,324,134 | 0.000000 | 59771309 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,241,126 | 0.000016 | 59771309 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,238,385 | 0.006496 | 59771309 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,101,882 | 14.627198 | 59771309 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,060,053 | 86.473728 | 59771309 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,036,355 | 451.249701 | 59771309 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,003,428 | 16,058.708254 | 59771309 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 1,000,448 | 83.164820 | 59771309 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 989,112 | 1,738.672394 | 59771309 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 977,491 | 4,232.258071 | 59771309 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 955,363 | 1,738.816308 | 59771309 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 911,409 | 31,158,362.615146 | 59771309 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 882,589 | 0.047992 | 59771309 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 843,599 | 60.119154 | 59771309 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 813,646 | 523,893.890075 | 59771309 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 789,546 | 0.000000 | 59771309 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 782,886 | 22,232,898.536517 | 59771309 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 781,527 | 0.001536 | 59771309 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 732,389 | 1,074.795325 | 59771309 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | XDP/USDC | 100 | 731,040 | 0.014966 | 59771309 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/SAPIEN | 4765 | 725,249 | 24.154233 | 59771309 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 722,576 | 0.046402 | 59771309 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| pancakeswap_v3 | WETH/USDC | 500 | 720,947 | 1,743.031584 | 59771309 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 10000 | 692,780 | 1,739.551825 | 59771309 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/wstETH | 3000 | 590,217 | 0.798842 | 59771309 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 589,093 | 1,743.775897 | 59771309 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 588,739 | 0.435656 | 59771309 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 551,752 | 4,725,542.329692 | 59771309 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 535,278 | 4,203.495683 | 59771309 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 509,122 | 1.386517 | 59771309 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3724 | 506,894 | 529,319.989358 | 59771309 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 494,155 | 0.031267 | 59771309 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 472,332 | 172,430.940538 | 59771309 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,534 | 1.001462 | 59771309 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 437,384 | 0.000007 | 59771309 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 404,413 | 0.056333 | 59771309 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3037 | 398,868 | 1,074.661277 | 59771309 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/UNI | 10000 | 384,129 | 356.818846 | 59771309 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 382,276 | 23.747263 | 59771309 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 381,739 | 845,002.327871 | 59771309 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 367,344 | 0.056111 | 59771309 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 361,778 | 0.000237 | 59771309 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2760 | 358,389 | 83.542392 | 59771309 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 19176 ; routes examinées : 248290848 ; candidats optimisés : 415668 ; net attendu > 0 : 288 ; dernier cycle 641.0 ms
- Rejets (moteur) : {'spread_below_threshold': 243268831, 'liquidity_below_min': 3033184, 'negative_expected_net': 415380, 'borrow_bound_too_small': 24393, 'cycle_budget_exhausted': 1380}
- Enregistrements de la session : 219817 ; net attendu > 0 : 288 ; simulés (eth_call de la vraie tx) : 8 (ok 8, échec 0) ; étiquettes ghost N+1 : 6/8 positives
- Décisions : {'REJECTED': 219817} ; motifs de rejet : {'below_safety_margin': 248, 'negative_expected_net': 219529, 'p_lower_below_threshold': 288, 'price_impact': 36, 'stale_data': 58}

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
