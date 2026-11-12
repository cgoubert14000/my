# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T06:10:20+00:00 ; durée 49.03 min ; blocs 56352481 → 56367177 (2196 vus)

## Connexion
- Requêtes RPC : 30855 ; erreurs : 5 ; latence p50/p95 : 360.5/1,465.8 ms
- Rafraîchissements d'état : 2196 ; âge des données au dernier bloc : 8.2 s ; changements de frais LP observés (pools à frais dynamiques) : 1064
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1475 ; cycles déclenchés par événement : 699 ; avance médiane sur le rafraîchissement multicall : 504 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,045.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 265 jetons, 15538 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2045.219297, 'cbBTC': 73500.635487, 'AERO': 0.536237}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,876,498 | 2,045.211417 | 56367204 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,404,055 | 0.027832 | 56367204 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,683,686 | 0.027806 | 56367204 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,459,728 | 0.000014 | 56367204 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,089,383 | 2,047.500362 | 56367204 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,843,358 | 104.065544 | 56367204 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,568,216 | 0.027835 | 56367204 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,219,342 | 1.867788 | 56367204 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,181,996 | 2,047.615911 | 56367204 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,871,951 | 0.998581 | 56367204 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,042,906 | 42,277.612977 | 56367204 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 146 | 2,883,636 | 2,047.902201 | 56367204 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,194,582 | 0.027823 | 56367204 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,940,667 | 1,125,823.099915 | 56367204 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,643,153 | 0.000014 | 56367204 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,621,214 | 0.016372 | 56367204 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,587,970 | 0.000014 | 56367204 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,560,018 | 0.000000 | 56367204 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,526,545 | 0.000014 | 56367204 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,499,483 | 0.006524 | 56367204 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,298 | 0.830252 | 56367204 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,447,821 | 1.389936 | 56367204 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,400,775 | 429.704567 | 56367204 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,174 | 2,045.652271 | 56367204 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,248,849 | 3,818.170216 | 56367204 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,210,761 | 15,445.445330 | 56367204 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,915 | 2,049.522546 | 56367204 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,118,121 | 2,047.496464 | 56367204 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,558 | 86.391364 | 56367204 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,035,431 | 33,787,417.907718 | 56367204 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,016,608 | 104.123332 | 56367204 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,619 | 21.211867 | 56367204 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 933,292 | 564,849.379545 | 56367204 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 910,353 | 0.001479 | 56367204 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 899,390 | 0.000014 | 56367204 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 898,975 | 0.050916 | 56367204 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 893,963 | 23,297,417.836114 | 56367204 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,535 | 1,026.008195 | 56367204 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 876,552 | 2,054.853960 | 56367204 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 852,914 | 0.000000 | 56367204 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 779,839 | 77.343223 | 56367204 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 749,766 | 0.050095 | 56367204 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 745,048 | 23.121486 | 56367204 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 737,834 | 117,140.110693 | 56367204 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 700,856 | 3,791.861802 | 56367204 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,920 | 0.801801 | 56367204 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 665,669 | 0.523744 | 56367204 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 643,977 | 4,782,423.994559 | 56367204 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 615,551 | 0.476933 | 56367204 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 583,608 | 155,679.107946 | 56367204 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 573,980 | 0.000258 | 56367204 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 572,000 | 560,364.031602 | 56367204 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 571,628 | 0.000007 | 56367204 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,130 | 0.037323 | 56367204 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 486,913 | 1,025.239043 | 56367204 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 466,211 | 0.067185 | 56367204 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,544 | 1.001028 | 56367204 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 445,985 | 0.501968 | 56367204 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,800 | 24.807640 | 56367204 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 427,515 | 946,097.254733 | 56367204 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 2894 ; routes examinées : 44966972 ; candidats optimisés : 198586 ; net attendu > 0 : 37 ; dernier cycle 332.3 ms
- Rejets (moteur) : {'spread_below_threshold': 44258803, 'liquidity_below_min': 506603, 'negative_expected_net': 198549, 'borrow_bound_too_small': 2893, 'cycle_budget_exhausted': 87}
- Enregistrements de la session : 198586 ; net attendu > 0 : 37 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 198586} ; motifs de rejet : {'below_safety_margin': 37, 'negative_expected_net': 198549, 'p_lower_below_threshold': 37, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56358036 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 127.764441 USDC | 0.010716 USDC | 0.000000 USDC | 0.004903 USDC | 0.005813 USDC (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(5813<25552), p_lower_below_threshold(0.09<0.75) |
| 56358037 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 127.764441 USDC | 0.010716 USDC | 0.000000 USDC | 0.004903 USDC | 0.005813 USDC (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(5813<25552), p_lower_below_threshold(0.09<0.75) |
| 56358036 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.062941 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(2840846607235<12588174234970), p_lower_below_threshold(0.09<0.75) |
| 56358037 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.062941 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(2840846607235<12588174234970), p_lower_below_threshold(0.09<0.75) |
| 56366735 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.012368 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0024 €) | — | 1.02 | 0.087 (n=116) | REJECTED | below_safety_margin(1265918134090<2473627526013), p_lower_below_threshold(0.09<0.75) |
| 56366735 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.014136 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.53 | 0.087 (n=116) | REJECTED | below_safety_margin(745305964134<2827232825153), p_lower_below_threshold(0.09<0.75) |
| 56357692 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.008130 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0007 €) | — | 0.44 | 0.087 (n=116) | REJECTED | below_safety_margin(358260336680<1626018761320), stale_data(4406ms>4000.0), p_lower_below_threshold(0.09<0.75) |
| 56352545 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352546 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352547 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.003784 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 0.54 | 0.344 (n=610) | REJECTED | below_safety_margin(204108972654<756812506909), p_lower_below_threshold(0.34<0.75) |
| 56352545 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352546 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352547 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352548 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352548 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.684145 USDC | 0.006546 USDC | 0.000000 USDC | 0.006146 USDC | 0.000400 USDC (0.0004 €) | — | 0.52 | 0.344 (n=610) | REJECTED | below_safety_margin(400<1536), p_lower_below_threshold(0.34<0.75) |
| 56352545 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352546 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352547 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352548 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003761 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0003 €) | — | 0.36 | 0.267 (n=1585) | REJECTED | below_safety_margin(136978468898<752279609749), p_lower_below_threshold(0.27<0.75) |
| 56352545 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |
| 56352546 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |
| 56352547 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 7.595327 USDC | 0.006409 USDC | 0.000000 USDC | 0.006146 USDC | 0.000263 USDC (0.0002 €) | — | 0.35 | 0.267 (n=1585) | REJECTED | below_safety_margin(263<1519), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8240 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
