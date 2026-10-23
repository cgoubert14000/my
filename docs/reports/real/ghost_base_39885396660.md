# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T02:13:51+00:00 ; durée 27.55 min ; blocs 52965306 → 52966141 (827 vus)

## Connexion
- Requêtes RPC : 10554 ; erreurs : 3 ; latence p50/p95 : 191.7/861.0 ms
- Rafraîchissements d'état : 828 ; âge des données au dernier bloc : 1.88 s ; changements de frais LP observés (pools à frais dynamiques) : 2100
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16765 ; cycles déclenchés par événement : 785 ; avance médiane sur le rafraîchissement multicall : 377 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,393.35 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19290 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 136, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 199 (rejetés 2) → 604 jetons ; pools candidats 3831 (énumérés 358, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2390.436843, 'AERO': 0.786132, 'cbBTC': 81441.109035}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,784,937 | 2,393.352559 | 52966141 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,260,116 | 0.029423 | 52966141 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,447,103 | 92.027837 | 52966141 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,925,465 | 1.267537 | 52966141 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,262,350 | 0.029380 | 52966141 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,847,867 | 0.000012 | 52966141 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,923,074 | 0.029396 | 52966141 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,669,721 | 2,393.174214 | 52966141 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,145,994 | 0.001671 | 52966141 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 6,777,498 | 0.000012 | 52966141 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 5,664,960 | 2,392.649719 | 52966141 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,400,965 | 0.029418 | 52966141 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 5,257,196 | 0.000012 | 52966141 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,590,700 | 2,392.454021 | 52966141 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,284,193 | 0.998772 | 52966141 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,282,585 | 2,393.592939 | 52966141 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,980,448 | 34,262.867766 | 52966141 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,409,410 | 0.000274 | 52966141 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 433 | 2,905,548 | 2,397.120624 | 52966141 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,552,424 | 92.067674 | 52966141 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,310,815 | 389.402068 | 52966141 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,264,311 | 3,025.076784 | 52966141 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,218,302 | 1,180,895.734555 | 52966141 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,003,689 | 0.000000 | 52966141 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,920,930 | 0.000012 | 52966141 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,777,430 | 0.018120 | 52966141 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,748,191 | 0.000012 | 52966141 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,025 | 1.525684 | 52966141 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,615,822 | 3,033.797944 | 52966141 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,771 | 0.823199 | 52966141 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,418,750 | 13,232.939327 | 52966141 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,369,715 | 0.004989 | 52966141 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,293,414 | 0.000274 | 52966141 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,281,766 | 2.362221 | 52966141 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,279,210 | 2,393.213709 | 52966141 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,269,261 | 0.000000 | 52966141 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,423 | 64.289389 | 52966141 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,187,021 | 35,771,448.901355 | 52966141 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,181,025 | 16.208310 | 52966141 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,074 | 1,105,075.590022 | 52966141 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,158,633 | 46.748377 | 52966141 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,146,521 | 498,148.209539 | 52966141 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | weETH_04c0/WETH | 500 | 1,090,048 | 1.105790 | 52966141 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/EDEL | 7000 | 1,087,263 | 74,647.214712 | 52966141 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,086,612 | 0.038529 | 52966141 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,062,006 | 21,313,449.073659 | 52966141 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,537 | 17.228474 | 52966141 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,028,220 | 0.000010 | 52966141 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/cbBTC | 3000 | 1,010,842 | 0.029376 | 52966141 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,005,242 | 23.057654 | 52966141 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 961,716 | 1,055.903634 | 52966141 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 938,596 | 2,381.973285 | 52966141 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 913,455 | 0.000546 | 52966141 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 889,793 | 0.917079 | 52966141 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 884,314 | 17.747930 | 52966141 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 874,586 | 2,392.542555 | 52966141 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 810,796 | 0.803225 | 52966141 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 788,866 | 0.654832 | 52966141 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,305 | 0.055391 | 52966141 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | fBOMB/USDC | 10000 | 770,158 | 0.018347 | 52966141 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |

## Recherche d'opportunités
- Cycles : 1612 ; routes examinées : 31095480 ; candidats optimisés : 120618 ; net attendu > 0 : 172 ; dernier cycle 88.7 ms
- Rejets (moteur) : {'spread_below_threshold': 30631846, 'liquidity_below_min': 341281, 'negative_expected_net': 120446, 'borrow_bound_too_small': 1612, 'cycle_budget_exhausted': 123}
- Enregistrements de la session : 120618 ; net attendu > 0 : 172 ; simulés (eth_call de la vraie tx) : 21 (ok 21, échec 0) ; étiquettes ghost N+1 : 5/5 positives
- Décisions : {'REJECTED': 120618} ; motifs de rejet : {'below_safety_margin': 146, 'negative_expected_net': 120446, 'p_lower_below_threshold': 156, 'reliability_not_demonstrated': 16, 'sim_below_estimate': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52965328 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 733.579452 USDC | 0.044077 USDC | 0.000000 USDC | 0.005375 USDC | 0.038702 USDC (0.0356 €) | — | 0.53 | 0.021 (n=69) | REJECTED | below_safety_margin(38702<146715), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 733.579452 USDC | 0.044077 USDC | 0.000000 USDC | 0.005375 USDC | 0.038702 USDC (0.0356 €) | — | 0.53 | 0.021 (n=69) | REJECTED | below_safety_margin(38702<146715), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.008336 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0352 €) | — | 0.56 | 0.021 (n=69) | REJECTED | below_safety_margin(47<166), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.008336 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0352 €) | — | 0.56 | 0.021 (n=69) | REJECTED | below_safety_margin(47<166), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 749.403957 USDC | 0.040099 USDC | 0.000000 USDC | 0.005375 USDC | 0.034724 USDC (0.0319 €) | — | 0.46 | 0.021 (n=69) | REJECTED | below_safety_margin(34724<149880), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 749.403957 USDC | 0.040099 USDC | 0.000000 USDC | 0.005375 USDC | 0.034724 USDC (0.0319 €) | — | 0.46 | 0.021 (n=69) | REJECTED | below_safety_margin(34724<149880), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.007880 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0314 €) | — | 0.53 | 0.021 (n=69) | REJECTED | below_safety_margin(42<157), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.007880 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0314 €) | — | 0.53 | 0.021 (n=69) | REJECTED | below_safety_margin(42<157), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.007382 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0239 €) | — | 0.43 | 0.021 (n=69) | REJECTED | below_safety_margin(32<147), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.007382 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0239 €) | — | 0.43 | 0.021 (n=69) | REJECTED | below_safety_margin(32<147), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 575.531692 USDC | 0.030935 USDC | 0.000000 USDC | 0.005375 USDC | 0.025560 USDC (0.0235 €) | — | 0.44 | 0.021 (n=69) | REJECTED | below_safety_margin(25560<115106), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 575.531692 USDC | 0.030935 USDC | 0.000000 USDC | 0.005375 USDC | 0.025560 USDC (0.0235 €) | — | 0.44 | 0.021 (n=69) | REJECTED | below_safety_margin(25560<115106), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 101.518755 USDC | 0.018529 USDC | 0.000000 USDC | 0.007194 USDC | 0.011335 USDC (0.0104 €) | — | 1.12 | 0.232 (n=113) | REJECTED | below_safety_margin(11335<20303), p_lower_below_threshold(0.23<0.75) |
| 52965328 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.042618 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0104 €) | — | 1.11 | 0.232 (n=113) | REJECTED | below_safety_margin(4714029629147<8523610461762), p_lower_below_threshold(0.23<0.75) |
| 52965328 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 292.367391 USDC | 0.012159 USDC | 0.000000 USDC | 0.005375 USDC | 0.006784 USDC (0.0062 €) | — | 0.23 | 0.021 (n=69) | REJECTED | below_safety_margin(6784<58473), p_lower_below_threshold(0.02<0.75) |
| 52965328 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 292.367391 USDC | 0.012159 USDC | 0.000000 USDC | 0.005375 USDC | 0.006784 USDC (0.0062 €) | — | 0.23 | 0.021 (n=69) | REJECTED | below_safety_margin(6784<58473), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.003626 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0060 €) | — | 0.22 | 0.021 (n=69) | REJECTED | below_safety_margin(8<72), p_lower_below_threshold(0.02<0.75) |
| 52965328 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.003626 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0060 €) | — | 0.22 | 0.021 (n=69) | REJECTED | below_safety_margin(8<72), p_lower_below_threshold(0.02<0.75) |
| 52965339 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 103.233654 USDC | 0.013334 USDC | 0.000000 USDC | 0.007229 USDC | 0.006105 USDC (0.0056 €) | — | 0.59 | 0.232 (n=113) | REJECTED | below_safety_margin(6105<20646), p_lower_below_threshold(0.23<0.75) |
| 52965339 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.043188 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | — | 0.59 | 0.232 (n=113) | REJECTED | below_safety_margin(2531033013349<8637604777244), p_lower_below_threshold(0.23<0.75) |
| 52965339 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001044 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0052 €) | — | 0.67 | 0.115 (n=232) | REJECTED | below_safety_margin(7<20), p_lower_below_threshold(0.12<0.75) |
| 52965339 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.031877 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0048 €) | — | 0.68 | 0.115 (n=232) | REJECTED | below_safety_margin(2173862273808<6375494347368), p_lower_below_threshold(0.12<0.75) |
| 52965339 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 72.245664 USDC | 0.011966 USDC | 0.000000 USDC | 0.007229 USDC | 0.004737 USDC (0.0044 €) | — | 0.66 | 0.115 (n=232) | REJECTED | below_safety_margin(4737<14449), p_lower_below_threshold(0.12<0.75) |
| 52965328 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 54.253264 USDC | 0.011820 USDC | 0.000000 USDC | 0.007194 USDC | 0.004626 USDC (0.0043 €) | — | 0.85 | 0.115 (n=232) | REJECTED | below_safety_margin(4626<10850), p_lower_below_threshold(0.12<0.75) |
| 52965328 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.022744 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0042 €) | — | 0.84 | 0.115 (n=232) | REJECTED | below_safety_margin(1918750762848<4548789371257), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1967 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.089 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
