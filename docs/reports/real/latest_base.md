# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T22:34:23+00:00 ; durée 60.94 min ; blocs 60100131 → 60118418 (4213 vus)

## Connexion
- Requêtes RPC : 44836 ; erreurs : 38 ; latence p50/p95 : 279.6/920.6 ms
- Rafraîchissements d'état : 4213 ; âge des données au dernier bloc : 3.95 s ; changements de frais LP observés (pools à frais dynamiques) : 3345
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12427 ; cycles déclenchés par événement : 2933 ; avance médiane sur le rafraîchissement multicall : 307 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,620.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 245 jetons, 12256 routes
- Par DEX : uniswap_v3 122, aerodrome_slipstream 86, aerodrome 166, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1605.51254, 'cbBTC': 58557.611788, 'AERO': 0.386499}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,242,183 | 1,620.415293 | 60118418 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,379,689 | 0.027450 | 60118418 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,422,114 | 1,619.130295 | 60118418 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,105,972 | 0.027458 | 60118418 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,222,186 | 78.759628 | 60118418 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,444,348 | 0.000017 | 60118418 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,779,828 | 0.027460 | 60118418 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,312,188 | 2.540065 | 60118418 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,105,915 | 0.999868 | 60118418 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,917,408 | 1,618.906013 | 60118418 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,474,065 | 40,145.487541 | 60118418 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 123 | 2,114,220 | 1,618.877663 | 60118418 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,779,839 | 0.000017 | 60118418 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,588,204 | 0.027466 | 60118418 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,548,160 | 1,110,496.380176 | 60118418 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,736 | 0.844843 | 60118418 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,284,306 | 0.000017 | 60118418 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,251,981 | 0.000000 | 60118418 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,159,641 | 0.006488 | 60118418 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,152,980 | 0.000017 | 60118418 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,080,450 | 15.387390 | 60118418 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,499 | 86.564217 | 60118418 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 965,161 | 453.003346 | 60118418 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 955,044 | 1,620.209438 | 60118418 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 945,507 | 16,508.392660 | 60118418 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 929,217 | 4,116.045753 | 60118418 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 923,826 | 79.315430 | 60118418 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 919,945 | 0.048648 | 60118418 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 862,971 | 1,621.209928 | 60118418 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 854,246 | 30,777,510.541246 | 60118418 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 763,163 | 514,280.347855 | 60118418 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 751,237 | 75.810879 | 60118418 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 744,512 | 0.001532 | 60118418 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 736,944 | 21,872,554.174726 | 60118418 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 722,754 | 0.000000 | 60118418 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/SAPIEN | 4605 | 722,024 | 24.357147 | 60118418 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | XDP/USDC | 100 | 712,764 | 0.014269 | 60118418 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 699,715 | 0.043519 | 60118418 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 685,316 | 1,066.195631 | 60118418 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 663,229 | 1,613.105205 | 60118418 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 648,763 | 1,619.017702 | 60118418 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | uXRP/WETH | 3000 | 643,960 | 0.000611 | 60118418 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/USDC | 100 | 562,445 | 1,618.868348 | 60118418 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 549,820 | 0.799406 | 60118418 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 549,739 | 0.381509 | 60118418 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 523,762 | 4,556,088.515536 | 60118418 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 503,764 | 4,147.646343 | 60118418 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 485,043 | 0.030408 | 60118418 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4049 | 477,132 | 512,004.306633 | 60118418 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| pancakeswap_v3 | ELSA/USDC | 100 | 475,412 | 0.068673 | 60118418 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | USDC/MAI (stable) | 3000 | 470,602 | 1.479983 | 60118418 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 420,909 | 188,794.586246 | 60118418 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 417,116 | 0.000007 | 60118418 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3196 | 372,473 | 1,066.375765 | 60118418 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 366,727 | 832,629.971823 | 60118418 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 365,830 | 21.777827 | 60118418 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | AWE/USDC | 3000 | 364,413 | 0.055220 | 60118418 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 346,549 | 365.871981 | 60118418 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2730 | 338,970 | 78.731283 | 60118418 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 334,812 | 0.000234 | 60118418 | `0x21594b992F68495dD28d605834b58889d0a727c7` |

## Recherche d'opportunités
- Cycles : 7145 ; routes examinées : 87569120 ; candidats optimisés : 170568 ; net attendu > 0 : 239 ; dernier cycle 564.7 ms
- Rejets (moteur) : {'spread_below_threshold': 85221998, 'liquidity_below_min': 1381461, 'negative_expected_net': 170329, 'borrow_bound_too_small': 15877, 'unquotable': 1984, 'cycle_budget_exhausted': 1291}
- Enregistrements de la session : 100426 ; net attendu > 0 : 239 ; simulés (eth_call de la vraie tx) : 19 (ok 5, échec 14) ; étiquettes ghost N+1 : 7/17 positives
- Décisions : {'REJECTED': 100426} ; motifs de rejet : {'below_safety_margin': 203, 'negative_expected_net': 100187, 'p_lower_below_threshold': 229, 'price_impact': 3, 'reliability_not_demonstrated': 10, 'sim_below_estimate': 1, 'simulation_failed': 14, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60110169 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 441.669958 USDC | 0.179140 USDC | 0.000000 USDC | 0.003671 USDC | 0.175469 USDC (0.1614 €) | — | 3.97 | 0.083 (n=121) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.274289 WETH | 0.000111 WETH | 0.000000 WETH | 0.000002 WETH | 0.000109 WETH (0.1614 €) | — | 3.96 | 0.083 (n=121) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 388.462712 USDC | 0.140972 USDC | 0.000000 USDC | 0.004908 USDC | 0.136064 USDC (0.1252 €) | — | 3.50 | 0.225 (n=1323) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.236296 WETH | 0.000087 WETH | 0.000000 WETH | 0.000003 WETH | 0.000084 WETH (0.1250 €) | — | 3.56 | 0.225 (n=1323) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 60110169 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006181 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1248 €) | — | 3.72 | 0.225 (n=1323) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 431.212801 USDC | 0.138715 USDC | 0.000000 USDC | 0.003916 USDC | 0.134799 USDC (0.1240 €) | — | 3.13 | 0.076 (n=514) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.266734 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000083 WETH (0.1240 €) | — | 3.13 | 0.076 (n=514) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 171.483819 USDC | 0.031461 USDC | 0.000000 USDC | 0.003671 USDC | 0.027790 USDC (0.0256 €) | — | 1.62 | 0.110 (n=381) | REJECTED | below_safety_margin(27790<34296), p_lower_below_threshold(0.11<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.106668 WETH | 0.000019 WETH | 0.000000 WETH | 0.000002 WETH | 0.000017 WETH (0.0255 €) | — | 1.61 | 0.110 (n=381) | REJECTED | below_safety_margin(17183294073573<21333506539644), p_lower_below_threshold(0.11<0.75) |
| 60102844 | USDC→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 104.322676 USDC | 0.024527 USDC | 0.000000 USDC | 0.003227 USDC | 0.021300 USDC (0.0196 €) | — | 2.04 | 0.351 (n=1) | REJECTED | reliability_not_demonstrated |
| 60102844 | WETH→[pancakeswap_v3]→USDC→[uniswap_v2]→WETH | 0.064567 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0195 €) | — | 2.03 | 0.351 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 60102832 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 100.541010 USDC | 0.024709 USDC | 0.000000 USDC | 0.004988 USDC | 0.019721 USDC (0.0181 €) | — | 1.96 | 0.280 (n=1680) | REJECTED | below_safety_margin(19721<20108), p_lower_below_threshold(0.28<0.75) |
| 60102832 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.061972 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0181 €) | — | 1.96 | 0.280 (n=1680) | REJECTED | below_safety_margin(12127415079541<12394357277085), p_lower_below_threshold(0.28<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 148.513526 USDC | 0.023240 USDC | 0.000000 USDC | 0.004908 USDC | 0.018332 USDC (0.0169 €) | — | 1.23 | 0.280 (n=1682) | REJECTED | below_safety_margin(18332<29702), p_lower_below_threshold(0.28<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.099616 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0168 €) | — | 1.14 | 0.280 (n=1682) | REJECTED | below_safety_margin(11325644791986<19923125519076), p_lower_below_threshold(0.28<0.75) |
| 60110169 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002698 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0168 €) | — | 1.15 | 0.280 (n=1682) | REJECTED | below_safety_margin(31<53), p_lower_below_threshold(0.28<0.75) |
| 60102832 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 94.229329 USDC | 0.022269 USDC | 0.000000 USDC | 0.004988 USDC | 0.017281 USDC (0.0159 €) | — | 1.83 | 0.280 (n=1680) | REJECTED | below_safety_margin(17281<18845), p_lower_below_threshold(0.28<0.75) |
| 60102832 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.058329 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0158 €) | — | 1.82 | 0.280 (n=1680) | REJECTED | below_safety_margin(10625551544050<11665742124250), p_lower_below_threshold(0.28<0.75) |
| 60102844 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 43.921763 USDC | 0.021449 USDC | 0.000000 USDC | 0.004988 USDC | 0.016461 USDC (0.0151 €) | — | 3.75 | 0.225 (n=1322) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 60102844 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.027075 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0151 €) | — | 3.74 | 0.225 (n=1322) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.23<0.75) |
| 60102832 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 123.247161 USDC | 0.019929 USDC | 0.000000 USDC | 0.004763 USDC | 0.015166 USDC (0.0140 €) | — | 1.23 | 0.347 (n=162) | REJECTED | below_safety_margin(15166<24649), p_lower_below_threshold(0.35<0.75) |
| 60102832 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 91.506573 USDC | 0.020095 USDC | 0.000000 USDC | 0.004988 USDC | 0.015107 USDC (0.0139 €) | — | 1.65 | 0.280 (n=1680) | REJECTED | below_safety_margin(15107<18301), p_lower_below_threshold(0.28<0.75) |
| 60102832 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.056175 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0138 €) | — | 1.65 | 0.280 (n=1680) | REJECTED | below_safety_margin(9287975629564<11234947264873), p_lower_below_threshold(0.28<0.75) |
| 60102832 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.001770 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0136 €) | — | 1.41 | 0.347 (n=162) | REJECTED | below_safety_margin(25<35), p_lower_below_threshold(0.35<0.75) |
| 60102844 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 60.497497 USDC | 0.018261 USDC | 0.000000 USDC | 0.004763 USDC | 0.013498 USDC (0.0124 €) | — | 2.23 | 0.219 (n=95) | REJECTED | stale_data(4687ms>4000.0), p_lower_below_threshold(0.22<0.75) |

## Fiabilité et décision
- Observations ghost : 8783 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
