# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T07:10:50+00:00 ; durée 18.24 min ; blocs 55947872 → 55953321 (819 vus)

## Connexion
- Requêtes RPC : 11020 ; erreurs : 0 ; latence p50/p95 : 205.6/1,591.7 ms
- Rafraîchissements d'état : 819 ; âge des données au dernier bloc : 10.18 s ; changements de frais LP observés (pools à frais dynamiques) : 432
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 856 ; cycles déclenchés par événement : 296 ; avance médiane sur le rafraîchissement multicall : 247 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,056.17 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,112,663 | 2,056.167763 | 55953350 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,390,828 | 0.027921 | 55953350 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,582,360 | 0.027977 | 55953350 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,332,044 | 0.000014 | 55953350 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,071,296 | 2,054.381209 | 55953350 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,739,328 | 108.455828 | 55953350 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,353,722 | 0.027935 | 55953350 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,245,316 | 1.862516 | 55953350 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,083,038 | 2,054.814282 | 55953350 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,869,510 | 1.000003 | 55953350 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,057,193 | 42,333.398004 | 55953350 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,922,614 | 2,054.888083 | 55953350 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,211,119 | 0.027976 | 55953350 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,954,985 | 1,121,311.176185 | 55953350 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,681,127 | 0.000014 | 55953350 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,618,106 | 0.000014 | 55953350 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,603,992 | 0.016119 | 55953350 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,552,174 | 0.000000 | 55953350 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,529,664 | 0.006622 | 55953350 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,280 | 0.824485 | 55953350 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,001 | 1.373191 | 55953350 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,439,508 | 0.000014 | 55953350 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,418,869 | 418.417500 | 55953350 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,271,444 | 2,055.607494 | 55953350 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,255,898 | 3,818.508368 | 55953350 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,229,258 | 14,959.311866 | 55953350 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,157,512 | 2,056.642810 | 55953350 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,702 | 85.881444 | 55953350 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,047,579 | 33,135,723.536569 | 55953350 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,014,044 | 2,054.387148 | 55953350 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,076 | 21.452330 | 55953350 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 942,219 | 557,994.244774 | 55953350 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 934,366 | 107.688191 | 55953350 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 910,967 | 0.000014 | 55953350 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 909,250 | 0.001469 | 55953350 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 902,447 | 23,147,877.094335 | 55953350 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 878,788 | 2,050.503253 | 55953350 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 878,469 | 1,027.526551 | 55953350 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 876,472 | 0.000000 | 55953350 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 865,853 | 0.052872 | 55953350 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 767,239 | 79.904459 | 55953350 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 766,809 | 0.052478 | 55953350 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 754,893 | 22.700496 | 55953350 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 746,659 | 115,615.997892 | 55953350 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 704,290 | 3,790.378227 | 55953350 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 696,139 | 0.802938 | 55953350 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,318 | 0.527251 | 55953350 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 658,159 | 4,622,220.931414 | 55953350 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 626,006 | 0.493384 | 55953350 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 593,592 | 151,971.406662 | 55953350 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 581,391 | 0.000007 | 55953350 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 580,509 | 0.000259 | 55953350 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 578,663 | 562,434.396870 | 55953350 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,506 | 0.037377 | 55953350 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 491,107 | 1,027.076180 | 55953350 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 460,658 | 0.496647 | 55953350 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 456,023 | 0.065359 | 55953350 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,063 | 1.001024 | 55953350 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | cbBTC/EDGE | 7000 | 448,078 | 870,182.366484 | 55953350 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,897 | 25.056759 | 55953350 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 1114 ; routes examinées : 18481260 ; candidats optimisés : 100190 ; net attendu > 0 : 43 ; dernier cycle 550.5 ms
- Rejets (moteur) : {'spread_below_threshold': 17998169, 'liquidity_below_min': 380537, 'negative_expected_net': 100147, 'borrow_bound_too_small': 2226, 'cycle_budget_exhausted': 138}
- Enregistrements de la session : 100190 ; net attendu > 0 : 43 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 1/2 positives
- Décisions : {'REJECTED': 100190} ; motifs de rejet : {'below_safety_margin': 41, 'negative_expected_net': 100147, 'p_lower_below_threshold': 31, 'reliability_not_demonstrated': 12, 'simulation_failed': 1, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55951267 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 145.747655 USDC | 0.253186 USDC | 0.000000 USDC | 0.004616 USDC | 0.248570 USDC (0.2287 €) | — | 17.05 | 0.007 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 55948986 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002260 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.49 | 0.261 (n=1552) | REJECTED | below_safety_margin(11<45), p_lower_below_threshold(0.26<0.75) |
| 55948986 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002260 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0075 €) | — | 0.49 | 0.261 (n=1552) | REJECTED | below_safety_margin(11<45), p_lower_below_threshold(0.26<0.75) |
| 55948986 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 169.132118 USDC | 0.014268 USDC | 0.000000 USDC | 0.006182 USDC | 0.008086 USDC (0.0074 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(8086<33826), p_lower_below_threshold(0.26<0.75) |
| 55948986 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 169.132118 USDC | 0.014268 USDC | 0.000000 USDC | 0.006182 USDC | 0.008086 USDC (0.0074 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(8086<33826), p_lower_below_threshold(0.26<0.75) |
| 55948986 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.077188 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0070 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(3715373181754<15437544997929), p_lower_below_threshold(0.26<0.75) |
| 55948986 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.077188 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0070 €) | — | 0.48 | 0.261 (n=1552) | REJECTED | below_safety_margin(3715373181754<15437544997929), p_lower_below_threshold(0.26<0.75) |
| 55951147 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→WETH | 0.033715 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0049 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(2583432781203<6743021806988), reliability_not_demonstrated |
| 55951147 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 68.562746 USDC | 0.009266 USDC | 0.000000 USDC | 0.003980 USDC | 0.005286 USDC (0.0049 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(5286<13712), reliability_not_demonstrated |
| 55951180 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→WETH | 0.033462 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0049 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(2564984443879<6692383355538), stale_data(6369ms>4000.0), reliability_not_demonstrated |
| 55951180 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→WETH | 0.033462 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0049 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(2564984443879<6692383355538), stale_data(7648ms>4000.0), reliability_not_demonstrated |
| 55951180 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 68.474153 USDC | 0.009266 USDC | 0.000000 USDC | 0.004016 USDC | 0.005250 USDC (0.0048 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(5250<13694), stale_data(6373ms>4000.0), reliability_not_demonstrated |
| 55951180 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→USDC | 68.474153 USDC | 0.009266 USDC | 0.000000 USDC | 0.004016 USDC | 0.005250 USDC (0.0048 €) | — | 0.77 | 0.001 (n=8) | REJECTED | below_safety_margin(5250<13694), stale_data(7653ms>4000.0), reliability_not_demonstrated |
| 55951181 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[uniswap_v3]→WETH | 0.008090 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0033 €) | 0.000002 WETH | 2.13 | 0.360 (n=146) | REJECTED | p_lower_below_threshold(0.36<0.75) |
| 55951181 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→wstETH→[aerodrome_slipstream]→WETH | 0.007522 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 1.69 | 0.360 (n=146) | REJECTED | below_safety_margin(1268087289674<1504439045749), p_lower_below_threshold(0.36<0.75) |
| 55951147 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.029718 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0018 €) | — | 0.33 | — (n=0) | REJECTED | below_safety_margin(973893954224<5943562133174), reliability_not_demonstrated |
| 55951147 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 60.715028 USDC | 0.005965 USDC | 0.000000 USDC | 0.003980 USDC | 0.001985 USDC (0.0018 €) | — | 0.33 | — (n=0) | REJECTED | below_safety_margin(1985<12143), reliability_not_demonstrated |
| 55951180 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.029785 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0018 €) | — | 0.32 | — (n=0) | REJECTED | below_safety_margin(955166756393<5957086565808), stale_data(6570ms>4000.0), reliability_not_demonstrated |
| 55951180 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.029785 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0018 €) | — | 0.32 | — (n=0) | REJECTED | below_safety_margin(955166756393<5957086565808), stale_data(7849ms>4000.0), reliability_not_demonstrated |
| 55951180 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 60.715028 USDC | 0.005965 USDC | 0.000000 USDC | 0.004016 USDC | 0.001949 USDC (0.0018 €) | — | 0.32 | — (n=0) | REJECTED | below_safety_margin(1949<12143), stale_data(6575ms>4000.0), reliability_not_demonstrated |
| 55951180 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 60.715028 USDC | 0.005965 USDC | 0.000000 USDC | 0.004016 USDC | 0.001949 USDC (0.0018 €) | — | 0.32 | — (n=0) | REJECTED | below_safety_margin(1949<12143), stale_data(7854ms>4000.0), reliability_not_demonstrated |
| 55948986 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002987 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.03 | 0.147 (n=41) | REJECTED | below_safety_margin(1<59), p_lower_below_threshold(0.15<0.75) |
| 55948986 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002987 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.03 | 0.147 (n=41) | REJECTED | below_safety_margin(1<59), p_lower_below_threshold(0.15<0.75) |
| 55951181 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[uniswap_v3]→WETH | 0.004302 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.72 | 0.261 (n=1552) | REJECTED | below_safety_margin(308857794216<860492866242), p_lower_below_threshold(0.26<0.75) |
| 55951147 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.011366 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0005 €) | — | 0.23 | 0.328 (n=569) | REJECTED | below_safety_margin(266512476685<2273118126969), p_lower_below_threshold(0.33<0.75) |

## Fiabilité et décision
- Observations ghost : 7990 ; taux observé 0.211 ; borne inférieure crédible (0.9) 0.205 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
