# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T10:46:45+00:00 ; durée 204.15 min ; blocs 52975401 → 52981526 (6046 vus)

## Connexion
- Requêtes RPC : 72442 ; erreurs : 140 ; latence p50/p95 : 221.6/657.7 ms
- Rafraîchissements d'état : 6047 ; âge des données au dernier bloc : 1.69 s ; changements de frais LP observés (pools à frais dynamiques) : 7701
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 46493 ; cycles déclenchés par événement : 4302 ; avance médiane sur le rafraîchissement multicall : 424 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,396.31 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19290 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 136, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 199 (rejetés 2) → 604 jetons ; pools candidats 3831 (énumérés 359, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2402.292282, 'AERO': 0.794098, 'cbBTC': 81667.512713}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,613,398 | 2,396.314503 | 52981526 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,462,782 | 0.029379 | 52981526 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,407,724 | 91.327095 | 52981526 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,496,922 | 1.272093 | 52981526 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,317,061 | 0.029405 | 52981526 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,869,167 | 0.000012 | 52981526 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,921,980 | 0.029397 | 52981526 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,681,963 | 2,397.447098 | 52981526 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,155,522 | 0.001666 | 52981526 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 6,349,817 | 0.000012 | 52981526 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 5,608,133 | 2,396.618081 | 52981526 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,438,477 | 0.029368 | 52981526 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 5,253,956 | 0.000012 | 52981526 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,552,145 | 2,396.484707 | 52981526 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,292,566 | 0.999613 | 52981526 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,281,449 | 2,394.905826 | 52981526 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 4,005,739 | 33,908.550399 | 52981526 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,402,267 | 0.000275 | 52981526 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 412 | 2,901,732 | 2,401.420337 | 52981526 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,563,962 | 91.306851 | 52981526 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,311,670 | 390.696965 | 52981526 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,227,949 | 1,172,860.262433 | 52981526 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,139,980 | 3,034.034182 | 52981526 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,989,728 | 0.000000 | 52981526 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,923,375 | 0.000012 | 52981526 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,760,089 | 0.000012 | 52981526 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,518 | 0.017714 | 52981526 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/AERO | 3000 | 1,607,800 | 3,051.293074 | 52981526 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,558,128 | 1.602759 | 52981526 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,343 | 0.823701 | 52981526 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,420,333 | 13,296.556478 | 52981526 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,371,028 | 0.005012 | 52981526 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,297,171 | 2.318292 | 52981526 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,728 | 0.000276 | 52981526 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,291,097 | 2,397.404737 | 52981526 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,256,947 | 0.000000 | 52981526 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,253 | 64.307231 | 52981526 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,180,355 | 36,452,008.841183 | 52981526 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,172,027 | 16.173608 | 52981526 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,163,577 | 1,118,205.958547 | 52981526 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,156,743 | 489,138.644915 | 52981526 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,152,425 | 47.174874 | 52981526 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,092,426 | 0.038056 | 52981526 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,080,600 | 75,757.862592 | 52981526 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,069,863 | 21,090,354.719265 | 52981526 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,053,767 | 16.394797 | 52981526 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,028,207 | 0.000010 | 52981526 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,011,653 | 23.088112 | 52981526 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 963,815 | 1,044.421292 | 52981526 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 948,778 | 2,390.321401 | 52981526 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 916,290 | 0.000548 | 52981526 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4575 | 889,220 | 17.587004 | 52981526 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 865,383 | 2,396.721138 | 52981526 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 858,265 | 1.105789 | 52981526 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 811,785 | 0.803225 | 52981526 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,489 | 0.057061 | 52981526 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 779,298 | 0.662677 | 52981526 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 773,112 | 4,533,095.592994 | 52981526 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | fBOMB/USDC | 10000 | 753,217 | 0.018516 | 52981526 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | TIG/USDC | 10000 | 737,672 | 0.681491 | 52981526 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 10348 ; routes examinées : 199612920 ; candidats optimisés : 854746 ; net attendu > 0 : 324 ; dernier cycle 92.0 ms
- Rejets (moteur) : {'spread_below_threshold': 196692860, 'liquidity_below_min': 2054322, 'negative_expected_net': 854422, 'borrow_bound_too_small': 10348, 'cycle_budget_exhausted': 644}
- Enregistrements de la session : 854746 ; net attendu > 0 : 324 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 854746} ; motifs de rejet : {'below_safety_margin': 305, 'negative_expected_net': 854422, 'p_lower_below_threshold': 287, 'reliability_not_demonstrated': 37}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52975572 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.029140 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0701 €) | 0.000032 WETH | 10.89 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[uniswap_v3]→USDC | 69.929959 USDC | 0.083061 USDC | 0.000000 USDC | 0.006893 USDC | 0.076168 USDC (0.0701 €) | — | 10.89 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.028214 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0640 €) | 0.000029 WETH | 10.27 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 67.426150 USDC | 0.076476 USDC | 0.000000 USDC | 0.006893 USDC | 0.069583 USDC (0.0640 €) | — | 10.32 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52977999 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 518.689610 USDC | 0.076011 USDC | 0.000000 USDC | 0.007227 USDC | 0.068784 USDC (0.0633 €) | — | 1.33 | 0.238 (n=118) | REJECTED | below_safety_margin(68784<103737), p_lower_below_threshold(0.24<0.75) |
| 52977999 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.215596 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0631 €) | — | 1.32 | 0.238 (n=118) | REJECTED | below_safety_margin(28550870976469<43119236587790), p_lower_below_threshold(0.24<0.75) |
| 52975572 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.027874 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0625 €) | 0.000028 WETH | 10.15 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 66.755766 USDC | 0.074809 USDC | 0.000000 USDC | 0.006893 USDC | 0.067916 USDC (0.0625 €) | — | 10.17 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52978388 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 457.454616 USDC | 0.070553 USDC | 0.000000 USDC | 0.005398 USDC | 0.065155 USDC (0.0599 €) | — | 1.42 | 0.021 (n=69) | REJECTED | below_safety_margin(65155<91490), p_lower_below_threshold(0.02<0.75) |
| 52978388 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.190467 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000027 WETH (0.0599 €) | — | 1.42 | 0.021 (n=69) | REJECTED | below_safety_margin(27101274446850<38093415582966), p_lower_below_threshold(0.02<0.75) |
| 52975572 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.022727 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0454 €) | — | 9.04 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[sushiswap_v3]→USDC | 54.395945 USDC | 0.056563 USDC | 0.000000 USDC | 0.007258 USDC | 0.049305 USDC (0.0454 €) | — | 9.06 | 0.021 (n=136) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 52975572 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH | 0.024158 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0453 €) | — | 8.48 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52975572 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 57.724561 USDC | 0.056052 USDC | 0.000000 USDC | 0.006893 USDC | 0.049159 USDC (0.0452 €) | — | 8.52 | 0.043 (n=19) | REJECTED | reliability_not_demonstrated |
| 52977999 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 457.653417 USDC | 0.053432 USDC | 0.000000 USDC | 0.007227 USDC | 0.046205 USDC (0.0425 €) | — | 1.01 | 0.116 (n=238) | REJECTED | below_safety_margin(46205<91530), p_lower_below_threshold(0.12<0.75) |
| 52977999 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 457.653417 USDC | 0.053432 USDC | 0.000000 USDC | 0.007227 USDC | 0.046205 USDC (0.0425 €) | — | 1.01 | 0.116 (n=238) | REJECTED | below_safety_margin(46205<91530), p_lower_below_threshold(0.12<0.75) |
| 52977999 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.182692 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0422 €) | — | 1.04 | 0.116 (n=238) | REJECTED | below_safety_margin(19067851972440<36538414955343), p_lower_below_threshold(0.12<0.75) |
| 52977999 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.182692 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0422 €) | — | 1.04 | 0.116 (n=238) | REJECTED | below_safety_margin(19067851972440<36538414955343), p_lower_below_threshold(0.12<0.75) |
| 52977999 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.006083 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0421 €) | — | 0.92 | 0.116 (n=238) | REJECTED | below_safety_margin(56<121), p_lower_below_threshold(0.12<0.75) |
| 52977999 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.006083 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0421 €) | — | 0.92 | 0.116 (n=238) | REJECTED | below_safety_margin(56<121), p_lower_below_threshold(0.12<0.75) |
| 52977999 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 424.231878 USDC | 0.052294 USDC | 0.000000 USDC | 0.007227 USDC | 0.045067 USDC (0.0415 €) | — | 1.06 | 0.116 (n=238) | REJECTED | below_safety_margin(45067<84846), p_lower_below_threshold(0.12<0.75) |
| 52977999 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 424.231878 USDC | 0.052294 USDC | 0.000000 USDC | 0.007227 USDC | 0.045067 USDC (0.0415 €) | — | 1.06 | 0.116 (n=238) | REJECTED | below_safety_margin(45067<84846), p_lower_below_threshold(0.12<0.75) |
| 52977999 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.182692 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0414 €) | — | 1.03 | 0.116 (n=238) | REJECTED | below_safety_margin(18728315553902<36538414955343), p_lower_below_threshold(0.12<0.75) |
| 52977999 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.182692 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0414 €) | — | 1.03 | 0.116 (n=238) | REJECTED | below_safety_margin(18728315553902<36538414955343), p_lower_below_threshold(0.12<0.75) |
| 52977999 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.006083 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0413 €) | — | 0.90 | 0.116 (n=238) | REJECTED | below_safety_margin(55<121), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1984 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
