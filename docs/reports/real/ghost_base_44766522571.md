# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T19:50:05+00:00 ; durée 234.17 min ; blocs 59998862 → 60069095 (10007 vus)

## Connexion
- Requêtes RPC : 119501 ; erreurs : 150 ; latence p50/p95 : 438.7/1,577.6 ms
- Rafraîchissements d'état : 10007 ; âge des données au dernier bloc : 8.31 s ; changements de frais LP observés (pools à frais dynamiques) : 15324
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5819 ; cycles déclenchés par événement : 1196 ; avance médiane sur le rafraîchissement multicall : 440 ms
- Gaz : base fee 0.005063 gwei ; prix ETH (pool le plus profond) : 1,609.60 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 244 jetons, 12400 routes
- Par DEX : uniswap_v3 121, aerodrome_slipstream 85, aerodrome 168, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 144 (rejetés 2) → 549 jetons ; pools candidats 3576 (énumérés 252, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1656.803175, 'cbBTC': 59633.257395, 'AERO': 0.391907}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,480,478 | 1,609.595675 | 60069120 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,742,672 | 0.027479 | 60069120 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,396,595 | 1,608.809452 | 60069120 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,088,706 | 0.027452 | 60069120 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,097,939 | 80.941096 | 60069120 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,429,367 | 0.000017 | 60069120 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,747,028 | 0.027490 | 60069120 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,283,069 | 2.585314 | 60069120 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,084,783 | 0.998706 | 60069120 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,825,379 | 1,608.893220 | 60069120 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,442,129 | 40,653.937824 | 60069120 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 100 | 2,100,573 | 1,608.614466 | 60069120 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,736,621 | 0.000017 | 60069120 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 1,577,348 | 0.027449 | 60069120 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,526,325 | 1,127,289.462865 | 60069120 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,450,951 | 0.844031 | 60069120 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 580 | 1,281,263 | 0.000017 | 60069120 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,227,734 | 0.000000 | 60069120 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,162,024 | 0.006594 | 60069120 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,144,320 | 0.000017 | 60069120 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,070,590 | 15.746693 | 60069120 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,419 | 86.577226 | 60069120 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 959,246 | 451.784316 | 60069120 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 951,808 | 1,609.624840 | 60069120 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 939,797 | 16,432.828620 | 60069120 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 915,815 | 4,158.551625 | 60069120 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 907,154 | 80.696423 | 60069120 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 898,422 | 0.050373 | 60069120 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 860,085 | 1,609.865343 | 60069120 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 849,609 | 30,669,520.144737 | 60069120 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 777,473 | 70.780743 | 60069120 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 756,515 | 517,221.764643 | 60069120 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 737,649 | 0.001528 | 60069120 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 732,810 | 21,908,730.964871 | 60069120 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 730,731 | 23.950769 | 60069120 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | XDP/USDC | 100 | 722,684 | 0.014650 | 60069120 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | DRB/WETH | 10000 | 704,073 | 0.000000 | 60069120 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| pancakeswap_v3 | QUID/USDC | 100 | 700,186 | 0.043576 | 60069120 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 682,909 | 1,062.654813 | 60069120 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 661,821 | 1,598.227500 | 60069120 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 647,305 | 1,608.860817 | 60069120 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 100 | 560,481 | 1,608.754046 | 60069120 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 549,769 | 0.381567 | 60069120 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 546,149 | 0.799406 | 60069120 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 514,316 | 4,661,585.541581 | 60069120 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 499,257 | 4,160.047969 | 60069120 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | ELSA/USDC | 100 | 492,545 | 0.071967 | 60069120 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 478,227 | 0.029779 | 60069120 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 3715 | 472,524 | 518,128.046644 | 60069120 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 471,956 | 1.480049 | 60069120 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 417,039 | 189,731.300173 | 60069120 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 410,888 | 0.000007 | 60069120 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/uSOL | 3000 | 363,763 | 21.825684 | 60069120 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 363,063 | 832,469.090379 | 60069120 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 362,681 | 0.054696 | 60069120 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/DEGEN | 3000 | 346,008 | 2,325,291.162719 | 60069120 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| uniswap_v3 | WETH/UNI | 10000 | 340,951 | 370.063240 | 60069120 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2808 | 335,258 | 80.938847 | 60069120 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 332,576 | 0.000234 | 60069120 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/SPX | 10000 | 318,399 | 6,278.593473 | 60069120 | `0xe96a4E9EA3a2C6Db214174738a19Eb7Dbb8A3069` |

## Recherche d'opportunités
- Cycles : 11202 ; routes examinées : 138904800 ; candidats optimisés : 430578 ; net attendu > 0 : 933 ; dernier cycle 1292.9 ms
- Rejets (moteur) : {'spread_below_threshold': 135025351, 'liquidity_below_min': 2011748, 'negative_expected_net': 429645, 'borrow_bound_too_small': 31874, 'cycle_budget_exhausted': 15728, 'unquotable': 3026}
- Enregistrements de la session : 344146 ; net attendu > 0 : 933 ; simulés (eth_call de la vraie tx) : 49 (ok 41, échec 8) ; étiquettes ghost N+1 : 28/43 positives
- Décisions : {'REJECTED': 344146} ; motifs de rejet : {'below_safety_margin': 638, 'negative_expected_net': 343213, 'p_lower_below_threshold': 915, 'reliability_not_demonstrated': 18, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 4, 'simulation_failed': 8, 'stale_data': 353}

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
| 60059581 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004998 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0931 €) | — | 3.50 | 0.224 (n=1319) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60059581 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 292.227966 USDC | 0.107170 USDC | 0.000000 USDC | 0.006512 USDC | 0.100658 USDC (0.0926 €) | — | 3.44 | 0.224 (n=1319) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60059581 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.174125 WETH | 0.000068 WETH | 0.000000 WETH | 0.000004 WETH | 0.000063 WETH (0.0925 €) | 0.000063 WETH | 3.65 | 0.224 (n=1319) | REJECTED | p_lower_below_threshold(0.22<0.75) |
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
| 60059581 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.134921 WETH | 0.000041 WETH | 0.000000 WETH | 0.000004 WETH | 0.000037 WETH (0.0542 €) | 0.000037 WETH | 2.76 | 0.277 (n=1671) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 60024062 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 106.969606 USDC | 0.063666 USDC | 0.000000 USDC | 0.005122 USDC | 0.058544 USDC (0.0539 €) | — | 5.47 | 0.309 (n=245) | REJECTED | stale_data(4141ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 60059581 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003230 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0537 €) | — | 3.13 | 0.224 (n=1319) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60024062 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.065912 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0537 €) | — | 5.45 | 0.309 (n=245) | REJECTED | stale_data(4136ms>4000.0), p_lower_below_threshold(0.31<0.75) |

## Fiabilité et décision
- Observations ghost : 8755 ; taux observé 0.232 ; borne inférieure crédible (0.9) 0.226 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
