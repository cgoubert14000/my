# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-19T17:06:29+00:00 ; durée 328.78 min ; blocs 59489413 → 59587993 (27513 vus)

## Connexion
- Requêtes RPC : 250177 ; erreurs : 790 ; latence p50/p95 : 321.9/2,220.6 ms
- Rafraîchissements d'état : 27513 ; âge des données au dernier bloc : 14.82 s ; changements de frais LP observés (pools à frais dynamiques) : 15395
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 42196 ; cycles déclenchés par événement : 12724 ; avance médiane sur le rafraîchissement multicall : 239 ms
- Gaz : base fee 0.005574 gwei ; prix ETH (pool le plus profond) : 1,756.86 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 434 pools, 251 jetons, 13296 routes
- Par DEX : uniswap_v3 128, aerodrome 174, aerodrome_slipstream 92, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 148 (rejetés 2) → 553 jetons ; pools candidats 3584 (énumérés 265, par paires 0), mesurés 436, sous le plancher de 10000.0 $ : 2 → gardés 434 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1806.52516, 'cbBTC': 63966.353313, 'AERO': 0.433079}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 85,625,972 | 1,756.864602 | 59588004 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 25,402,650 | 1,752.497182 | 59588004 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,606,449 | 0.028135 | 59588004 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,709,423 | 0.028203 | 59588004 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,734,933 | 79.021670 | 59588004 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,922,561 | 0.000016 | 59588004 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,157,280 | 0.028130 | 59588004 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,589,357 | 2.390568 | 59588004 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,284,112 | 1.000000 | 59588004 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,259,372 | 1,752.453300 | 59588004 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,741,538 | 38,432.090669 | 59588004 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 549 | 2,303,906 | 1,752.373947 | 59588004 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,061,597 | 0.000016 | 59588004 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,715,624 | 0.028192 | 59588004 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,660,022 | 1,135,390.211883 | 59588004 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,388 | 0.844383 | 59588004 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,442,411 | 0.000016 | 59588004 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,312,242 | 0.000000 | 59588004 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,270,795 | 0.006529 | 59588004 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,253,197 | 0.000016 | 59588004 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,117,862 | 14.104186 | 59588004 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,060,530 | 86.395886 | 59588004 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,048,100 | 449.032438 | 59588004 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 1,029,695 | 78.923163 | 59588004 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/USDC | 3000 | 1,021,233 | 1,756.957985 | 59588004 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,015,288 | 15,949.912974 | 59588004 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 991,720 | 4,207.615641 | 59588004 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 986,458 | 1,757.473078 | 59588004 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/doginme | 10000 | 952,074 | 28,115,424.911663 | 59588004 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 922,298 | 0.045025 | 59588004 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 867,262 | 56.883291 | 59588004 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 822,065 | 523,906.357619 | 59588004 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 812,459 | 0.000000 | 59588004 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 791,929 | 22,182,820.497108 | 59588004 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 786,693 | 0.001529 | 59588004 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 735,902 | 0.015060 | 59588004 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/MORPHO | 3000 | 732,746 | 1,087.838432 | 59588004 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 729,090 | 1,752.586489 | 59588004 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 717,514 | 0.045749 | 59588004 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/USDC | 10000 | 694,876 | 1,769.645921 | 59588004 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/SAPIEN | 4890 | 686,478 | 25.959017 | 59588004 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 100 | 599,276 | 1,752.420139 | 59588004 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 596,329 | 0.798842 | 59588004 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 593,436 | 0.442409 | 59588004 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 553,165 | 4,798,755.580716 | 59588004 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 542,420 | 4,190.759325 | 59588004 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 512,057 | 525,287.382020 | 59588004 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 499,332 | 0.031763 | 59588004 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | USDC/MAI (stable) | 3000 | 499,205 | 1.434405 | 59588004 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 483,247 | 168,059.275422 | 59588004 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 14 | 461,661 | 1.001603 | 59588004 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 443,523 | 0.000007 | 59588004 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 428,439 | 0.000240 | 59588004 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | ELSA/USDC | 100 | 411,272 | 0.057495 | 59588004 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3064 | 398,956 | 1,087.720883 | 59588004 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 386,821 | 843,213.644958 | 59588004 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 384,167 | 357.843371 | 59588004 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 383,645 | 24.177256 | 59588004 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | AWE/USDC | 3000 | 372,196 | 0.057603 | 59588004 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome_slipstream | WETH/VVV | 2733 | 369,758 | 79.039280 | 59588004 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 40236 ; routes examinées : 534977856 ; candidats optimisés : 124148 ; net attendu > 0 : 68 ; dernier cycle 592.2 ms
- Rejets (moteur) : {'spread_below_threshold': 523391374, 'liquidity_below_min': 8178524, 'negative_expected_net': 124080, 'borrow_bound_too_small': 78768, 'cycle_budget_exhausted': 1747}
- Enregistrements de la session : 62687 ; net attendu > 0 : 68 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 62687} ; motifs de rejet : {'below_safety_margin': 56, 'negative_expected_net': 62619, 'p_lower_below_threshold': 68}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59583707 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002328 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0151 €) | — | 1.12 | 0.272 (n=1637) | REJECTED | below_safety_margin(26<46), p_lower_below_threshold(0.27<0.75) |
| 59583707 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 158.199943 USDC | 0.021742 USDC | 0.000000 USDC | 0.005536 USDC | 0.016206 USDC (0.0149 €) | — | 1.02 | 0.272 (n=1637) | REJECTED | below_safety_margin(16206<31639), p_lower_below_threshold(0.27<0.75) |
| 59583707 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.084574 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0148 €) | — | 1.07 | 0.272 (n=1637) | REJECTED | below_safety_margin(9082981029962<16914730948532), p_lower_below_threshold(0.27<0.75) |
| 59583707 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.022393 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0104 €) | 0.000006 WETH | 2.83 | 0.272 (n=1637) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59583707 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 39.496931 USDC | 0.016741 USDC | 0.000000 USDC | 0.005536 USDC | 0.011205 USDC (0.0103 €) | — | 2.84 | 0.272 (n=1637) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59583707 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000905 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0081 €) | — | 1.55 | 0.272 (n=1637) | REJECTED | below_safety_margin(14<18), p_lower_below_threshold(0.27<0.75) |
| 59583707 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 54.242652 USDC | 0.014070 USDC | 0.000000 USDC | 0.005536 USDC | 0.008534 USDC (0.0079 €) | — | 1.57 | 0.272 (n=1637) | REJECTED | below_safety_margin(8534<10848), p_lower_below_threshold(0.27<0.75) |
| 59583707 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.033016 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0076 €) | — | 1.41 | 0.272 (n=1637) | REJECTED | below_safety_margin(4653717812440<6603237890689), p_lower_below_threshold(0.27<0.75) |
| 59583707 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.020372 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0075 €) | 0.000005 WETH | 2.25 | 0.272 (n=1637) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59583707 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 35.917034 USDC | 0.013626 USDC | 0.000000 USDC | 0.005536 USDC | 0.008090 USDC (0.0074 €) | — | 2.25 | 0.272 (n=1637) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59583707 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000664 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0041 €) | — | 1.05 | 0.272 (n=1637) | REJECTED | below_safety_margin(7<13), p_lower_below_threshold(0.27<0.75) |
| 59583707 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.039433 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 0.63 | 0.354 (n=640) | REJECTED | below_safety_margin(2469545845949<7886597452150), p_lower_below_threshold(0.35<0.75) |
| 59583707 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 69.866897 USDC | 0.009894 USDC | 0.000000 USDC | 0.005536 USDC | 0.004358 USDC (0.0040 €) | — | 0.62 | 0.354 (n=640) | REJECTED | below_safety_margin(4358<13973), p_lower_below_threshold(0.35<0.75) |
| 59583707 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.024135 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 1.01 | 0.272 (n=1637) | REJECTED | below_safety_margin(2442724779914<4827071514546), p_lower_below_threshold(0.27<0.75) |
| 59583707 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 44.436288 USDC | 0.009865 USDC | 0.000000 USDC | 0.005536 USDC | 0.004329 USDC (0.0040 €) | — | 0.97 | 0.272 (n=1637) | REJECTED | below_safety_margin(4329<8887), p_lower_below_threshold(0.27<0.75) |
| 59583707 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.011271 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0038 €) | 0.000002 WETH | 2.09 | 0.354 (n=640) | REJECTED | p_lower_below_threshold(0.35<0.75) |
| 59583707 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 19.765286 USDC | 0.009682 USDC | 0.000000 USDC | 0.005536 USDC | 0.004146 USDC (0.0038 €) | — | 2.10 | 0.354 (n=640) | REJECTED | p_lower_below_threshold(0.35<0.75) |
| 59583707 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.022344 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.66 | 0.363 (n=155) | REJECTED | below_safety_margin(1478311962867<4468727088872), p_lower_below_threshold(0.36<0.75) |
| 59583707 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 39.074675 USDC | 0.007888 USDC | 0.000000 USDC | 0.005285 USDC | 0.002603 USDC (0.0024 €) | — | 0.67 | 0.363 (n=155) | REJECTED | below_safety_margin(2603<7814), p_lower_below_threshold(0.36<0.75) |
| 59583707 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.010260 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 1.40 | 0.272 (n=1637) | REJECTED | below_safety_margin(1435356519310<2051951881886), p_lower_below_threshold(0.27<0.75) |
| 59583707 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 18.207570 USDC | 0.008064 USDC | 0.000000 USDC | 0.005536 USDC | 0.002528 USDC (0.0023 €) | — | 1.39 | 0.272 (n=1637) | REJECTED | below_safety_margin(2528<3641), p_lower_below_threshold(0.27<0.75) |
| 59583707 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000295 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0023 €) | — | 1.36 | 0.272 (n=1637) | REJECTED | below_safety_margin(4<5), p_lower_below_threshold(0.27<0.75) |
| 59583707 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000295 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0023 €) | — | 1.36 | 0.272 (n=1637) | REJECTED | below_safety_margin(4<5), p_lower_below_threshold(0.27<0.75) |
| 59583707 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000402 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0023 €) | — | 0.99 | 0.354 (n=640) | REJECTED | below_safety_margin(4<8), p_lower_below_threshold(0.35<0.75) |
| 59583707 | WETH→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.005070 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 2.78 | 0.276 (n=243) | REJECTED | p_lower_below_threshold(0.28<0.75) |

## Fiabilité et décision
- Observations ghost : 8576 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
