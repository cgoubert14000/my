# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T14:30:17+00:00 ; durée 27.57 min ; blocs 55644907 → 55653170 (1307 vus)

## Connexion
- Requêtes RPC : 19377 ; erreurs : 10 ; latence p50/p95 : 243.1/1,220.5 ms
- Rafraîchissements d'état : 1307 ; âge des données au dernier bloc : 7.6 s ; changements de frais LP observés (pools à frais dynamiques) : 979
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2340 ; cycles déclenchés par événement : 505 ; avance médiane sur le rafraîchissement multicall : 535 ms
- Gaz : base fee 0.005235 gwei ; prix ETH (pool le plus profond) : 2,065.88 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 136,769,675 | 2,065.881941 | 55653192 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,190,026 | 0.027993 | 55653192 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,356,745 | 0.000014 | 55653192 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,587,472 | 0.027977 | 55653192 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,318,588 | 2,063.113374 | 55653192 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,941,471 | 103.419301 | 55653192 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,642,491 | 0.028001 | 55653192 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,341,371 | 1.809332 | 55653192 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,925,222 | 2,063.543913 | 55653192 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,878,266 | 1.000003 | 55653192 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,049,436 | 42,952.367153 | 55653192 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 609 | 2,944,492 | 2,063.475561 | 55653192 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,281,338 | 0.027999 | 55653192 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,976,023 | 1,107,956.754543 | 55653192 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,682,996 | 0.000014 | 55653192 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,657,431 | 0.000014 | 55653192 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,611,919 | 0.016254 | 55653192 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,543,814 | 0.006689 | 55653192 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,512,490 | 0.000000 | 55653192 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,491,954 | 0.000014 | 55653192 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,510 | 0.821956 | 55653192 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,432,228 | 415.236586 | 55653192 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55653192 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,274,367 | 2,066.250788 | 55653192 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,258,370 | 3,723.594082 | 55653192 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,237,008 | 14,852.270746 | 55653192 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,203,428 | 2,066.835348 | 55653192 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,632 | 79.347361 | 55653192 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,053,676 | 2,063.422045 | 55653192 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,032,321 | 35,263,884.321102 | 55653192 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 956,252 | 21.647954 | 55653192 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 944,616 | 562,233.189030 | 55653192 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 935,529 | 104.150548 | 55653192 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 917,471 | 0.000014 | 55653192 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 916,762 | 0.001487 | 55653192 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 915,298 | 22,771,584.884619 | 55653192 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 913,096 | 0.050119 | 55653192 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 889,804 | 1,024.608261 | 55653192 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 877,726 | 2,071.230075 | 55653192 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 866,345 | 0.000000 | 55653192 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 788,721 | 75.611167 | 55653192 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 774,764 | 108,396.584159 | 55653192 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 772,514 | 21.973520 | 55653192 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 759,276 | 0.051419 | 55653192 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 722,466 | 3,710.753909 | 55653192 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 699,262 | 0.803317 | 55653192 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 653,447 | 0.535014 | 55653192 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 645,306 | 4,852,158.261623 | 55653192 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 642,488 | 0.518762 | 55653192 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 603,201 | 0.000008 | 55653192 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 585,779 | 157,428.600493 | 55653192 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,658 | 0.000257 | 55653192 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 579,035 | 557,761.814344 | 55653192 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 562,674 | 0.038031 | 55653192 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 502,178 | 1,024.594194 | 55653192 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 482,689 | 6,717.560483 | 55653192 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 478,318 | 0.069508 | 55653192 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,523 | 1.001169 | 55653192 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 452,256 | 296.416529 | 55653192 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | WETH/msETH (stable) | 500 | 444,217 | 2.390100 | 55653192 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 1811 ; routes examinées : 29631582 ; candidats optimisés : 126749 ; net attendu > 0 : 391 ; dernier cycle 237.0 ms
- Rejets (moteur) : {'spread_below_threshold': 29085874, 'liquidity_below_min': 403907, 'negative_expected_net': 126358, 'pool_quarantined': 11826, 'borrow_bound_too_small': 3161, 'cycle_budget_exhausted': 65}
- Enregistrements de la session : 126749 ; net attendu > 0 : 391 ; simulés (eth_call de la vraie tx) : 22 (ok 6, échec 16) ; étiquettes ghost N+1 : 2/13 positives
- Décisions : {'REJECTED': 126749} ; motifs de rejet : {'below_safety_margin': 355, 'negative_expected_net': 126358, 'p_lower_below_threshold': 385, 'reliability_not_demonstrated': 6, 'simulation_failed': 16, 'stale_data': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004596 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0468 €) | — | 1.50 | 0.316 (n=517) | REJECTED | below_safety_margin(69<91), p_lower_below_threshold(0.32<0.75) |
| 55647094 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.174281 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0466 €) | — | 1.41 | 0.316 (n=517) | REJECTED | below_safety_margin(24518343617352<34856237954381), p_lower_below_threshold(0.32<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 364.443705 USDC | 0.056893 USDC | 0.000000 USDC | 0.006281 USDC | 0.050612 USDC (0.0466 €) | — | 1.39 | 0.316 (n=517) | REJECTED | below_safety_margin(50612<72888), p_lower_below_threshold(0.32<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003909 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0394 €) | — | 1.48 | 0.227 (n=1406) | REJECTED | below_safety_margin(58<78), p_lower_below_threshold(0.23<0.75) |
| 55647094 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.150305 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0393 €) | — | 1.37 | 0.227 (n=1406) | REJECTED | below_safety_margin(20664748044216<30061088872016), p_lower_below_threshold(0.23<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 297.718576 USDC | 0.048873 USDC | 0.000000 USDC | 0.006281 USDC | 0.042592 USDC (0.0392 €) | — | 1.43 | 0.227 (n=1406) | REJECTED | below_safety_margin(42592<59543), p_lower_below_threshold(0.23<0.75) |
| 55645931 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006254 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0387 €) | — | 0.91 | 0.059 (n=36) | REJECTED | below_safety_margin(57<125), p_lower_below_threshold(0.06<0.75) |
| 55645931 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.223435 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(20184448102296<44686993205901), p_lower_below_threshold(0.06<0.75) |
| 55645931 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 462.507606 USDC | 0.047993 USDC | 0.000000 USDC | 0.006274 USDC | 0.041719 USDC (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(41719<92501), p_lower_below_threshold(0.06<0.75) |
| 55647094 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.099025 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0314 €) | — | 1.67 | 0.227 (n=1406) | REJECTED | below_safety_margin(16512542878146<19804904995583), p_lower_below_threshold(0.23<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 200.308158 USDC | 0.040373 USDC | 0.000000 USDC | 0.006281 USDC | 0.034092 USDC (0.0314 €) | — | 1.70 | 0.227 (n=1406) | REJECTED | below_safety_margin(34092<40061), p_lower_below_threshold(0.23<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002455 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0312 €) | — | 1.87 | 0.227 (n=1406) | REJECTED | below_safety_margin(46<49), p_lower_below_threshold(0.23<0.75) |
| 55645931 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 319.275131 USDC | 0.032633 USDC | 0.000000 USDC | 0.004691 USDC | 0.027942 USDC (0.0257 €) | — | 0.88 | 0.081 (n=338) | REJECTED | below_safety_margin(27942<63855), p_lower_below_threshold(0.08<0.75) |
| 55645931 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.154898 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0257 €) | — | 0.87 | 0.081 (n=338) | REJECTED | below_safety_margin(13496928497097<30979510259946), p_lower_below_threshold(0.08<0.75) |
| 55652356 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000887 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 3.49 | 0.183 (n=1104) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 55652357 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000887 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0210 €) | — | 3.49 | 0.183 (n=1104) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 55652356 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.038461 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0210 €) | — | 2.88 | 0.228 (n=1411) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.23<0.75) |
| 55652357 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.038461 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0210 €) | — | 2.88 | 0.228 (n=1411) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.23<0.75) |
| 55649310 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.058433 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0191 €) | — | 1.72 | 0.071 (n=30) | REJECTED | below_safety_margin(10029285594149<11686564214872), stale_data(5769ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55649310 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 119.674274 USDC | 0.025066 USDC | 0.000000 USDC | 0.004384 USDC | 0.020682 USDC (0.0190 €) | — | 1.73 | 0.071 (n=30) | REJECTED | below_safety_margin(20682<23934), stale_data(5772ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 55649290 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.134850 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0186 €) | — | 0.72 | 0.081 (n=338) | REJECTED | below_safety_margin(9762602554739<26970083020775), p_lower_below_threshold(0.08<0.75) |
| 55649290 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 278.333345 USDC | 0.024815 USDC | 0.000000 USDC | 0.004669 USDC | 0.020146 USDC (0.0185 €) | — | 0.72 | 0.081 (n=338) | REJECTED | below_safety_margin(20146<55666), p_lower_below_threshold(0.08<0.75) |
| 55646688 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 274.848829 USDC | 0.024268 USDC | 0.000000 USDC | 0.004680 USDC | 0.019588 USDC (0.0180 €) | — | 0.71 | 0.081 (n=338) | REJECTED | below_safety_margin(19588<54969), p_lower_below_threshold(0.08<0.75) |
| 55646688 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.133019 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0180 €) | — | 0.71 | 0.081 (n=338) | REJECTED | below_safety_margin(9469341376538<26603798352582), p_lower_below_threshold(0.08<0.75) |
| 55652381 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000845 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0177 €) | 0.000000 cbBTC | 3.08 | 0.183 (n=1105) | REJECTED | p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 7518 ; taux observé 0.193 ; borne inférieure crédible (0.9) 0.187 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
