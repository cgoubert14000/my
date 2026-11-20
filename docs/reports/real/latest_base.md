# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T18:48:11+00:00 ; durée 172.28 min ; blocs 59998862 → 60050529 (7152 vus)

## Connexion
- Requêtes RPC : 86509 ; erreurs : 150 ; latence p50/p95 : 498.1/1,560.5 ms
- Rafraîchissements d'état : 7152 ; âge des données au dernier bloc : 8.19 s ; changements de frais LP observés (pools à frais dynamiques) : 10498
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5819 ; cycles déclenchés par événement : 1196 ; avance médiane sur le rafraîchissement multicall : 440 ms
- Gaz : base fee 0.006900 gwei ; prix ETH (pool le plus profond) : 1,608.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 244 jetons, 12400 routes
- Par DEX : uniswap_v3 121, aerodrome_slipstream 85, aerodrome 168, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 144 (rejetés 2) → 549 jetons ; pools candidats 3576 (énumérés 252, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1656.803175, 'cbBTC': 59633.257395, 'AERO': 0.391907}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,651,999 | 1,608.424478 | 60050529 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,653,739 | 0.027733 | 60050529 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,383,854 | 1,611.085206 | 60050529 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,078,679 | 0.027719 | 60050529 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,001,637 | 83.406289 | 60050529 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,496,653 | 0.000017 | 60050529 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,742,848 | 0.027740 | 60050529 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,283,849 | 2.584074 | 60050529 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 3,053,877 | 0.998798 | 60050529 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,840,774 | 1,610.869221 | 60050529 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,428,676 | 41,045.747523 | 60050529 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 758 | 2,104,026 | 1,611.800643 | 60050529 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,755,084 | 0.000017 | 60050529 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2580 | 1,574,265 | 0.027734 | 60050529 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,543,763 | 1,100,363.616604 | 60050529 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,411 | 0.844096 | 60050529 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,272,396 | 0.000017 | 60050529 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,224,685 | 0.000000 | 60050529 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,157,626 | 0.006578 | 60050529 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,134,000 | 0.000017 | 60050529 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,080,098 | 15.399963 | 60050529 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,458 | 86.570826 | 60050529 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 957,169 | 454.656324 | 60050529 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 951,448 | 1,613.613672 | 60050529 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 931,749 | 16,418.726114 | 60050529 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 915,900 | 4,173.337835 | 60050529 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 900,963 | 82.813146 | 60050529 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 877,223 | 0.051704 | 60050529 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 859,773 | 1,613.368937 | 60050529 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 845,184 | 31,046,927.103409 | 60050529 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 790,964 | 68.386759 | 60050529 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 752,463 | 523,985.066776 | 60050529 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 734,469 | 0.001545 | 60050529 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 726,353 | 22,138,096.310060 | 60050529 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/SAPIEN | 4990 | 719,734 | 24.450660 | 60050529 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | DRB/WETH | 10000 | 718,432 | 0.000000 | 60050529 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | XDP/USDC | 100 | 715,320 | 0.014369 | 60050529 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 703,971 | 0.044038 | 60050529 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 670,617 | 1,087.209495 | 60050529 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 661,351 | 1,624.776596 | 60050529 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 633,916 | 1,610.959847 | 60050529 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 100 | 570,541 | 1,611.176575 | 60050529 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 561,453 | 0.397419 | 60050529 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 545,752 | 0.799406 | 60050529 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 511,008 | 4,714,884.095916 | 60050529 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,931 | 1.386569 | 60050529 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/AERO | 10000 | 499,200 | 4,191.004814 | 60050529 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | ELSA/USDC | 100 | 481,038 | 0.069757 | 60050529 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 476,857 | 0.029653 | 60050529 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 468,977 | 521,758.303473 | 60050529 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 417,065 | 189,427.850315 | 60050529 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 409,957 | 0.000007 | 60050529 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | AWE/USDC | 3000 | 362,395 | 0.054610 | 60050529 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | cbBTC/EDGE | 7000 | 360,165 | 840,745.522441 | 60050529 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 359,883 | 22.082944 | 60050529 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 341,413 | 369.002171 | 60050529 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/DEGEN | 3000 | 339,181 | 2,404,072.804636 | 60050529 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| aerodrome | VIRTUAL/WETH | 10000 | 331,653 | 0.000233 | 60050529 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2730 | 331,180 | 83.381954 | 60050529 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/SPX | 10000 | 317,904 | 6,288.997243 | 60050529 | `0xe96a4E9EA3a2C6Db214174738a19Eb7Dbb8A3069` |

## Recherche d'opportunités
- Cycles : 8347 ; routes examinées : 103502800 ; candidats optimisés : 340235 ; net attendu > 0 : 492 ; dernier cycle 1205.3 ms
- Rejets (moteur) : {'spread_below_threshold': 100590841, 'liquidity_below_min': 1504363, 'negative_expected_net': 339743, 'borrow_bound_too_small': 20295, 'cycle_budget_exhausted': 11760, 'unquotable': 2174}
- Enregistrements de la session : 283928 ; net attendu > 0 : 492 ; simulés (eth_call de la vraie tx) : 22 (ok 16, échec 6) ; étiquettes ghost N+1 : 8/18 positives
- Décisions : {'REJECTED': 283928} ; motifs de rejet : {'below_safety_margin': 323, 'negative_expected_net': 283436, 'p_lower_below_threshold': 484, 'reliability_not_demonstrated': 8, 'simulation_failed': 6, 'stale_data': 286}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60024062 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 345.648439 USDC | 0.151255 USDC | 0.000000 USDC | 0.005122 USDC | 0.146133 USDC (0.1344 €) | — | 4.23 | 0.185 (n=339) | REJECTED | stale_data(4266ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60024062 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.005793 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1344 €) | — | 4.26 | 0.185 (n=339) | REJECTED | stale_data(4271ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 282.858034 USDC | 0.147980 USDC | 0.000000 USDC | 0.005122 USDC | 0.142858 USDC (0.1314 €) | — | 5.05 | 0.309 (n=245) | REJECTED | stale_data(4204ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60024062 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.004695 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1311 €) | — | 5.13 | 0.309 (n=245) | REJECTED | stale_data(4199ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 233.265543 USDC | 0.129247 USDC | 0.000000 USDC | 0.005122 USDC | 0.124125 USDC (0.1142 €) | — | 5.32 | 0.185 (n=339) | REJECTED | stale_data(4158ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60024062 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.142794 WETH | 0.000079 WETH | 0.000000 WETH | 0.000003 WETH | 0.000076 WETH (0.1140 €) | 0.000076 WETH | 5.33 | 0.185 (n=339) | REJECTED | stale_data(4153ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 214.501580 USDC | 0.127967 USDC | 0.000000 USDC | 0.005122 USDC | 0.122845 USDC (0.1130 €) | — | 5.73 | 0.185 (n=339) | REJECTED | stale_data(4132ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60024062 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.131915 WETH | 0.000078 WETH | 0.000000 WETH | 0.000003 WETH | 0.000075 WETH (0.1128 €) | 0.000075 WETH | 5.71 | 0.185 (n=339) | REJECTED | stale_data(4127ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 176.565932 USDC | 0.094340 USDC | 0.000000 USDC | 0.005122 USDC | 0.089218 USDC (0.0821 €) | — | 5.05 | 0.309 (n=245) | REJECTED | stale_data(4184ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60024062 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.108438 WETH | 0.000058 WETH | 0.000000 WETH | 0.000003 WETH | 0.000055 WETH (0.0819 €) | 0.000055 WETH | 5.05 | 0.309 (n=245) | REJECTED | stale_data(4179ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60000947 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.063469 WETH | 0.000067 WETH | 0.000000 WETH | 0.000013 WETH | 0.000054 WETH (0.0812 €) | 0.000054 WETH | 8.50 | 0.113 (n=166) | REJECTED | stale_data(5770ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 101.213571 USDC | 0.109088 USDC | 0.000000 USDC | 0.021135 USDC | 0.087953 USDC (0.0809 €) | — | 8.69 | 0.113 (n=166) | REJECTED | stale_data(5765ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 200.627158 USDC | 0.091366 USDC | 0.000000 USDC | 0.005369 USDC | 0.085997 USDC (0.0791 €) | — | 4.29 | 0.309 (n=245) | REJECTED | stale_data(4226ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60024062 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.123485 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.0790 €) | — | 4.27 | 0.309 (n=245) | REJECTED | stale_data(4220ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 213.578470 USDC | 0.083982 USDC | 0.000000 USDC | 0.005122 USDC | 0.078860 USDC (0.0726 €) | — | 3.69 | 0.185 (n=339) | REJECTED | stale_data(4276ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60024062 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.003641 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0724 €) | — | 3.65 | 0.185 (n=339) | REJECTED | stale_data(4280ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60000947 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.053374 WETH | 0.000051 WETH | 0.000000 WETH | 0.000013 WETH | 0.000038 WETH (0.0569 €) | 0.000038 WETH | 7.09 | 0.334 (n=637) | REJECTED | stale_data(5880ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 87.164835 USDC | 0.082973 USDC | 0.000000 USDC | 0.021135 USDC | 0.061838 USDC (0.0569 €) | — | 7.09 | 0.334 (n=637) | REJECTED | stale_data(5875ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 106.969606 USDC | 0.063666 USDC | 0.000000 USDC | 0.005122 USDC | 0.058544 USDC (0.0539 €) | — | 5.47 | 0.309 (n=245) | REJECTED | stale_data(4141ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60024062 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.065912 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0537 €) | — | 5.45 | 0.309 (n=245) | REJECTED | stale_data(4136ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60000947 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.022730 WETH | 0.000046 WETH | 0.000000 WETH | 0.000012 WETH | 0.000033 WETH (0.0503 €) | 0.000033 WETH | 14.71 | 0.122 (n=69) | REJECTED | stale_data(5347ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 36.982921 USDC | 0.074836 USDC | 0.000000 USDC | 0.020305 USDC | 0.054531 USDC (0.0502 €) | — | 14.74 | 0.122 (n=69) | REJECTED | stale_data(5354ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 107.327196 USDC | 0.059435 USDC | 0.000000 USDC | 0.005122 USDC | 0.054313 USDC (0.0500 €) | — | 5.06 | 0.309 (n=245) | REJECTED | stale_data(4174ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60024062 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.066055 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0499 €) | — | 5.04 | 0.309 (n=245) | REJECTED | stale_data(4169ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60000947 | WETH→[aerodrome_slipstream]→LINK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.043576 WETH | 0.000046 WETH | 0.000000 WETH | 0.000013 WETH | 0.000033 WETH (0.0496 €) | — | 7.57 | 0.334 (n=637) | REJECTED | stale_data(5788ms>4000.0), p_lower_below_threshold(0.33<0.75) |

## Fiabilité et décision
- Observations ghost : 8730 ; taux observé 0.231 ; borne inférieure crédible (0.9) 0.225 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
