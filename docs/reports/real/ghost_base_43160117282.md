# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T07:21:32+00:00 ; durée 120.23 min ; blocs 56352481 → 56388523 (5540 vus)

## Connexion
- Requêtes RPC : 76305 ; erreurs : 5 ; latence p50/p95 : 415.6/1,442.8 ms
- Rafraîchissements d'état : 5540 ; âge des données au dernier bloc : 8.95 s ; changements de frais LP observés (pools à frais dynamiques) : 2640
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1475 ; cycles déclenchés par événement : 699 ; avance médiane sur le rafraîchissement multicall : 504 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,044.10 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 265 jetons, 15538 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2045.219297, 'cbBTC': 73500.635487, 'AERO': 0.536237}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,838,983 | 2,044.098897 | 56388548 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,395,198 | 0.027854 | 56388548 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,683,524 | 0.027806 | 56388548 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,452,870 | 0.000014 | 56388548 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,077,987 | 2,046.458149 | 56388548 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,834,858 | 104.210656 | 56388548 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,233,919 | 0.027856 | 56388548 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,209,551 | 1.876487 | 56388548 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,180,288 | 2,047.022729 | 56388548 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,866,122 | 0.998657 | 56388548 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,036,601 | 42,407.159947 | 56388548 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 154 | 2,882,263 | 2,047.043021 | 56388548 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,193,155 | 0.027823 | 56388548 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,939,612 | 1,125,823.099915 | 56388548 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,641,557 | 0.000014 | 56388548 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,625,757 | 0.016440 | 56388548 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,588,045 | 0.000014 | 56388548 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,557,909 | 0.000000 | 56388548 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,525,252 | 0.000014 | 56388548 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,498,782 | 0.006525 | 56388548 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,329 | 0.830219 | 56388548 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,447,821 | 1.389936 | 56388548 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,399,168 | 430.597339 | 56388548 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,267,830 | 2,043.845879 | 56388548 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,244,878 | 3,831.105012 | 56388548 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,208,469 | 15,476.560564 | 56388548 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,601 | 2,046.218451 | 56388548 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,117,678 | 2,046.489996 | 56388548 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,555 | 86.229165 | 56388548 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,034,868 | 33,787,417.907718 | 56388548 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,015,004 | 104.123169 | 56388548 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 966,848 | 20.930775 | 56388548 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 933,788 | 563,079.938399 | 56388548 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 908,526 | 0.001476 | 56388548 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 898,262 | 0.000014 | 56388548 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 897,604 | 0.050926 | 56388548 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 893,476 | 23,297,417.836114 | 56388548 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 876,345 | 2,054.853960 | 56388548 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 874,862 | 1,024.265909 | 56388548 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 852,732 | 0.000000 | 56388548 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 779,119 | 77.486209 | 56388548 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 749,184 | 0.050015 | 56388548 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4550 | 747,614 | 23.011933 | 56388548 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 736,602 | 117,404.435098 | 56388548 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 699,041 | 3,803.510040 | 56388548 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,543 | 0.801801 | 56388548 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 663,943 | 0.520802 | 56388548 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 642,611 | 4,797,569.034099 | 56388548 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 615,706 | 0.477157 | 56388548 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 582,236 | 156,246.061486 | 56388548 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 572,979 | 0.000257 | 56388548 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 572,630 | 558,171.048644 | 56388548 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 569,549 | 0.000007 | 56388548 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,967 | 0.037408 | 56388548 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 487,117 | 1,024.529535 | 56388548 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,172 | 0.066819 | 56388548 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,536 | 1.001058 | 56388548 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,358 | 0.501968 | 56388548 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,680 | 24.793780 | 56388548 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 428,420 | 946,097.254733 | 56388548 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 6238 ; routes examinées : 96926044 ; candidats optimisés : 472247 ; net attendu > 0 : 63 ; dernier cycle 447.1 ms
- Rejets (moteur) : {'spread_below_threshold': 95273631, 'liquidity_below_min': 1173615, 'negative_expected_net': 472184, 'borrow_bound_too_small': 6235, 'cycle_budget_exhausted': 316}
- Enregistrements de la session : 472247 ; net attendu > 0 : 63 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 472247} ; motifs de rejet : {'below_safety_margin': 48, 'negative_expected_net': 472184, 'p_lower_below_threshold': 63, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.218273 USDC | 0.032458 USDC | 0.000000 USDC | 0.006143 USDC | 0.026315 USDC (0.0242 €) | — | 7.47 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017342 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0242 €) | 0.000013 WETH | 7.41 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.404259 USDC | 0.032255 USDC | 0.000000 USDC | 0.006143 USDC | 0.026112 USDC (0.0240 €) | — | 7.38 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017304 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0240 €) | 0.000013 WETH | 7.37 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 34.633173 USDC | 0.031152 USDC | 0.000000 USDC | 0.006143 USDC | 0.025009 USDC (0.0230 €) | — | 7.22 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017066 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0230 €) | 0.000012 WETH | 7.16 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.013924 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0160 €) | — | 6.09 | 0.077 (n=120) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 56380462 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004048 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 0.42 | 0.102 (n=366) | REJECTED | below_safety_margin(17<80), p_lower_below_threshold(0.10<0.75) |
| 56380462 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 349.650476 USDC | 0.017156 USDC | 0.000000 USDC | 0.004913 USDC | 0.012243 USDC (0.0113 €) | — | 0.35 | 0.102 (n=366) | REJECTED | below_safety_margin(12243<69930), p_lower_below_threshold(0.10<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 26.577874 USDC | 0.018129 USDC | 0.000000 USDC | 0.006143 USDC | 0.011986 USDC (0.0110 €) | — | 4.51 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.012985 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0110 €) | — | 4.51 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 25.295059 USDC | 0.016679 USDC | 0.000000 USDC | 0.006143 USDC | 0.010536 USDC (0.0097 €) | — | 4.17 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.012479 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0097 €) | — | 4.13 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 18.973789 USDC | 0.012147 USDC | 0.000000 USDC | 0.006143 USDC | 0.006004 USDC (0.0055 €) | — | 3.16 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.009378 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0055 €) | — | 3.13 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56358036 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 127.764441 USDC | 0.010716 USDC | 0.000000 USDC | 0.004903 USDC | 0.005813 USDC (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(5813<25552), p_lower_below_threshold(0.09<0.75) |
| 56358037 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 127.764441 USDC | 0.010716 USDC | 0.000000 USDC | 0.004903 USDC | 0.005813 USDC (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(5813<25552), p_lower_below_threshold(0.09<0.75) |
| 56358036 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.062941 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(2840846607235<12588174234970), p_lower_below_threshold(0.09<0.75) |
| 56358037 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.062941 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(2840846607235<12588174234970), p_lower_below_threshold(0.09<0.75) |
| 56388390 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.005953 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 3.59 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 12.189597 USDC | 0.010513 USDC | 0.000000 USDC | 0.006143 USDC | 0.004370 USDC (0.0040 €) | — | 3.59 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56366735 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.012368 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0024 €) | — | 1.02 | 0.087 (n=116) | REJECTED | below_safety_margin(1265918134090<2473627526013), p_lower_below_threshold(0.09<0.75) |
| 56366735 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.014136 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.53 | 0.087 (n=116) | REJECTED | below_safety_margin(745305964134<2827232825153), p_lower_below_threshold(0.09<0.75) |
| 56379880 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.065202 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0007 €) | — | 0.06 | 0.102 (n=366) | REJECTED | below_safety_margin(364296180358<13040490169434), p_lower_below_threshold(0.10<0.75) |
| 56379880 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 132.216784 USDC | 0.005330 USDC | 0.000000 USDC | 0.004594 USDC | 0.000736 USDC (0.0007 €) | — | 0.06 | 0.102 (n=366) | REJECTED | below_safety_margin(736<26443), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 8243 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
