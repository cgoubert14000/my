# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T07:26:12+00:00 ; durée 33.61 min ; blocs 55947872 → 55957923 (1499 vus)

## Connexion
- Requêtes RPC : 20275 ; erreurs : 0 ; latence p50/p95 : 225.3/1,669.2 ms
- Rafraîchissements d'état : 1499 ; âge des données au dernier bloc : 10.52 s ; changements de frais LP observés (pools à frais dynamiques) : 821
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1340 ; cycles déclenchés par événement : 473 ; avance médiane sur le rafraîchissement multicall : 247 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,059.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,209,450 | 2,059.664796 | 55957953 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,416,056 | 0.027932 | 55957953 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,597,542 | 0.027977 | 55957953 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,339,146 | 0.000014 | 55957953 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,081,206 | 2,062.736338 | 55957953 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,757,619 | 108.236718 | 55957953 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,360,760 | 0.027921 | 55957953 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,262,027 | 1.847928 | 55957953 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,088,376 | 2,061.802525 | 55957953 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,874,534 | 1.000003 | 55957953 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,062,109 | 42,341.241935 | 55957953 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 669 | 2,926,936 | 2,062.150070 | 55957953 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,214,747 | 0.027976 | 55957953 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,958,310 | 1,121,311.176185 | 55957953 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,682,596 | 0.000014 | 55957953 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,619,671 | 0.000014 | 55957953 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,608,607 | 0.016184 | 55957953 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,554,505 | 0.000000 | 55957953 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,525,949 | 0.006615 | 55957953 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,745 | 0.824485 | 55957953 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,001 | 1.373191 | 55957953 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,440,707 | 0.000014 | 55957953 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,421,655 | 418.030187 | 55957953 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,527 | 2,059.527477 | 55957953 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,263,185 | 3,812.266755 | 55957953 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,231,561 | 14,959.977045 | 55957953 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,496 | 2,059.921677 | 55957953 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,710 | 85.880156 | 55957953 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,048,665 | 33,199,659.082426 | 55957953 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,015,396 | 2,062.895637 | 55957953 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,425 | 21.359917 | 55957953 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 943,818 | 557,999.178955 | 55957953 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 937,299 | 107.688154 | 55957953 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 912,086 | 0.000014 | 55957953 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 910,918 | 0.001470 | 55957953 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 903,982 | 23,147,877.094335 | 55957953 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 880,429 | 1,026.548782 | 55957953 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 879,442 | 2,050.503253 | 55957953 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 879,253 | 0.000000 | 55957953 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 868,655 | 0.052475 | 55957953 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 767,239 | 79.904459 | 55957953 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 765,891 | 0.052348 | 55957953 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 755,710 | 22.666461 | 55957953 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 746,909 | 115,931.839725 | 55957953 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 707,657 | 3,790.378227 | 55957953 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 697,323 | 0.802938 | 55957953 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 673,287 | 0.529133 | 55957953 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 661,582 | 4,590,230.641335 | 55957953 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 626,906 | 0.494735 | 55957953 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 593,847 | 152,358.306583 | 55957953 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 584,785 | 0.000007 | 55957953 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,496 | 0.000259 | 55957953 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 579,643 | 561,424.165189 | 55957953 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 557,826 | 0.037512 | 55957953 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 492,222 | 1,026.062196 | 55957953 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 461,533 | 0.496647 | 55957953 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 456,792 | 0.065461 | 55957953 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,067 | 1.000989 | 55957953 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | cbBTC/EDGE | 7000 | 448,138 | 870,182.366484 | 55957953 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,643 | 25.056759 | 55957953 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 1971 ; routes examinées : 32698890 ; candidats optimisés : 175413 ; net attendu > 0 : 77 ; dernier cycle 484.8 ms
- Rejets (moteur) : {'spread_below_threshold': 31849554, 'liquidity_below_min': 670214, 'negative_expected_net': 175336, 'borrow_bound_too_small': 3434, 'cycle_budget_exhausted': 275}
- Enregistrements de la session : 175413 ; net attendu > 0 : 77 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 1/2 positives
- Décisions : {'REJECTED': 175413} ; motifs de rejet : {'below_safety_margin': 75, 'negative_expected_net': 175336, 'p_lower_below_threshold': 59, 'reliability_not_demonstrated': 18, 'simulation_failed': 1, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55951267 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 145.747655 USDC | 0.253186 USDC | 0.000000 USDC | 0.004616 USDC | 0.248570 USDC (0.2287 €) | — | 17.05 | 0.007 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55955302 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003160 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0156 €) | — | 0.73 | 0.261 (n=1552) | REJECTED | below_safety_margin(23<63), p_lower_below_threshold(0.26<0.75) |
| 55955303 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003160 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0156 €) | — | 0.73 | 0.261 (n=1552) | REJECTED | below_safety_margin(23<63), p_lower_below_threshold(0.26<0.75) |
| 55955302 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.114190 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0155 €) | — | 0.72 | 0.261 (n=1552) | REJECTED | below_safety_margin(8183111748913<22838005236142), p_lower_below_threshold(0.26<0.75) |
| 55955303 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.114190 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0155 €) | — | 0.72 | 0.261 (n=1552) | REJECTED | below_safety_margin(8183111748913<22838005236142), p_lower_below_threshold(0.26<0.75) |
| 55955302 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 224.865861 USDC | 0.022810 USDC | 0.000000 USDC | 0.006179 USDC | 0.016631 USDC (0.0153 €) | — | 0.74 | 0.261 (n=1552) | REJECTED | below_safety_margin(16631<44973), p_lower_below_threshold(0.26<0.75) |
| 55955303 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 224.865861 USDC | 0.022810 USDC | 0.000000 USDC | 0.006179 USDC | 0.016631 USDC (0.0153 €) | — | 0.74 | 0.261 (n=1552) | REJECTED | below_safety_margin(16631<44973), p_lower_below_threshold(0.26<0.75) |
| 55957325 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 109.728256 USDC | 0.016579 USDC | 0.000000 USDC | 0.004621 USDC | 0.011958 USDC (0.0110 €) | — | 1.09 | 0.055 (n=15) | REJECTED | below_safety_margin(11958<21945), reliability_not_demonstrated |
| 55957325 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 109.728256 USDC | 0.016579 USDC | 0.000000 USDC | 0.004625 USDC | 0.011954 USDC (0.0110 €) | — | 1.09 | 0.055 (n=15) | REJECTED | below_safety_margin(11954<21945), reliability_not_demonstrated |
| 55957326 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 109.728256 USDC | 0.016579 USDC | 0.000000 USDC | 0.004625 USDC | 0.011954 USDC (0.0110 €) | — | 1.09 | 0.055 (n=15) | REJECTED | below_safety_margin(11954<21945), reliability_not_demonstrated |
| 55957325 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001279 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0108 €) | — | 1.25 | 0.055 (n=15) | REJECTED | below_safety_margin(16<25), reliability_not_demonstrated |
| 55957325 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001279 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0108 €) | — | 1.25 | 0.055 (n=15) | REJECTED | below_safety_margin(16<25), reliability_not_demonstrated |
| 55957326 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001279 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0108 €) | — | 1.25 | 0.055 (n=15) | REJECTED | below_safety_margin(16<25), reliability_not_demonstrated |
| 55948986 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002260 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.49 | 0.261 (n=1552) | REJECTED | below_safety_margin(11<45), p_lower_below_threshold(0.26<0.75) |
| 55948986 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002260 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.49 | 0.261 (n=1552) | REJECTED | below_safety_margin(11<45), p_lower_below_threshold(0.26<0.75) |
| 55948986 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 169.132118 USDC | 0.014268 USDC | 0.000000 USDC | 0.006182 USDC | 0.008086 USDC (0.0074 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(8086<33826), p_lower_below_threshold(0.26<0.75) |
| 55948986 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 169.132118 USDC | 0.014268 USDC | 0.000000 USDC | 0.006182 USDC | 0.008086 USDC (0.0074 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(8086<33826), p_lower_below_threshold(0.26<0.75) |
| 55948986 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.077188 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0070 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(3715373181754<15437544997929), p_lower_below_threshold(0.26<0.75) |
| 55948986 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.077188 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0070 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(3715373181754<15437544997929), p_lower_below_threshold(0.26<0.75) |
| 55955302 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 142.763451 USDC | 0.011747 USDC | 0.000000 USDC | 0.004617 USDC | 0.007130 USDC (0.0066 €) | — | 0.50 | 0.081 (n=113) | REJECTED | below_safety_margin(7130<28552), p_lower_below_threshold(0.08<0.75) |
| 55955303 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 142.763451 USDC | 0.011747 USDC | 0.000000 USDC | 0.004617 USDC | 0.007130 USDC (0.0066 €) | — | 0.50 | 0.081 (n=113) | REJECTED | below_safety_margin(7130<28552), p_lower_below_threshold(0.08<0.75) |
| 55955302 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069662 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.50 | 0.081 (n=113) | REJECTED | below_safety_margin(3466188619499<13932461859313), p_lower_below_threshold(0.08<0.75) |
| 55955303 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069662 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.50 | 0.081 (n=113) | REJECTED | below_safety_margin(3466188619499<13932461859313), p_lower_below_threshold(0.08<0.75) |
| 55951147 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→WETH | 0.033715 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0049 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(2583432781203<6743021806988), reliability_not_demonstrated |
| 55951147 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 68.562746 USDC | 0.009266 USDC | 0.000000 USDC | 0.003980 USDC | 0.005286 USDC (0.0049 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(5286<13712), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 7990 ; taux observé 0.211 ; borne inférieure crédible (0.9) 0.205 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
