# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T12:07:26+00:00 ; durée 112.49 min ; blocs 59896587 → 59930336 (11001 vus)

## Connexion
- Requêtes RPC : 101839 ; erreurs : 0 ; latence p50/p95 : 95.6/871.1 ms
- Rafraîchissements d'état : 11001 ; âge des données au dernier bloc : 9.05 s ; changements de frais LP observés (pools à frais dynamiques) : 4803
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9278 ; cycles déclenchés par événement : 2070 ; avance médiane sur le rafraîchissement multicall : 155 ms
- Gaz : base fee 0.005159 gwei ; prix ETH (pool le plus profond) : 1,734.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 84,684,413 | 1,734.105954 | 59930339 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,997,609 | 0.028231 | 59930339 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,138,401 | 1,730.947783 | 59930339 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,598,357 | 0.028298 | 59930339 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,352,546 | 86.534782 | 59930339 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,983,575 | 0.000016 | 59930339 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,118,916 | 0.028238 | 59930339 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,561,790 | 2.425755 | 59930339 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,362,681 | 1,731.178665 | 59930339 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,234,904 | 0.998714 | 59930339 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,673,805 | 39,363.890695 | 59930339 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 634 | 2,272,643 | 1,730.584155 | 59930339 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,903,793 | 0.000016 | 59930339 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2550 | 1,692,393 | 0.028285 | 59930339 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,633,120 | 1,142,907.098486 | 59930339 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,461 | 0.844852 | 59930339 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,373,692 | 0.000016 | 59930339 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,312,453 | 0.000000 | 59930339 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,231,843 | 0.006466 | 59930339 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,231,831 | 0.000016 | 59930339 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,115,480 | 14.196532 | 59930339 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,937 | 86.492551 | 59930339 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,029,183 | 459.868428 | 59930339 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 989,594 | 16,228.253919 | 59930339 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 987,758 | 1,734.394960 | 59930339 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/VVV | 10000 | 983,916 | 85.926055 | 59930339 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/AERO | 3000 | 978,132 | 4,197.192779 | 59930339 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 903,785 | 31,690,919.865906 | 59930339 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/USDC | 3000 | 892,921 | 1,734.603637 | 59930339 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | USDC/VVV | 3000 | 882,778 | 0.049871 | 59930339 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 809,442 | 65.300061 | 59930339 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 809,337 | 527,712.911218 | 59930339 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 781,548 | 0.000000 | 59930339 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 776,426 | 22,446,056.229025 | 59930339 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 771,721 | 0.001519 | 59930339 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 746,838 | 0.015591 | 59930339 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 721,562 | 0.046270 | 59930339 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| pancakeswap_v3 | WETH/USDC | 500 | 719,030 | 1,730.837214 | 59930339 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/MORPHO | 3000 | 718,829 | 1,095.797543 | 59930339 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 706,611 | 25.051674 | 59930339 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 692,066 | 1,744.307706 | 59930339 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 594,468 | 1,731.152616 | 59930339 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 588,911 | 0.798009 | 59930339 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 584,006 | 0.428905 | 59930339 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 552,471 | 4,688,012.155081 | 59930339 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 534,980 | 4,190.092648 | 59930339 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59930339 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3718 | 503,637 | 531,089.306623 | 59930339 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 493,762 | 0.031214 | 59930339 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 459,078 | 181,558.010892 | 59930339 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 14 | 456,337 | 1.001737 | 59930339 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 437,200 | 0.000007 | 59930339 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 423,292 | 0.059668 | 59930339 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 389,880 | 1,095.579281 | 59930339 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 381,013 | 23.790509 | 59930339 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 378,463 | 851,906.574132 | 59930339 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 376,438 | 361.906950 | 59930339 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 366,876 | 0.055968 | 59930339 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 356,738 | 0.000231 | 59930339 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/DEGEN | 3000 | 354,125 | 2,563,875.514117 | 59930339 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 13070 ; routes examinées : 166511800 ; candidats optimisés : 128990 ; net attendu > 0 : 65 ; dernier cycle 1631.7 ms
- Rejets (moteur) : {'spread_below_threshold': 163264393, 'liquidity_below_min': 1742497, 'negative_expected_net': 128925, 'cycle_budget_exhausted': 27487, 'borrow_bound_too_small': 14862}
- Enregistrements de la session : 38388 ; net attendu > 0 : 65 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 1/1 positives
- Décisions : {'REJECTED': 38388} ; motifs de rejet : {'below_safety_margin': 64, 'negative_expected_net': 38323, 'p_lower_below_threshold': 65, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59913838 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 12.932215 USDC | 0.009418 USDC | 0.000000 USDC | 0.003954 USDC | 0.005464 USDC (0.0050 €) | — | 4.23 | 0.077 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 59929973 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.036126 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0020 €) | — | 0.34 | 0.272 (n=1640) | REJECTED | below_safety_margin(1238952709459<7225240482219), p_lower_below_threshold(0.27<0.75) |
| 59929973 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.036126 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0020 €) | — | 0.34 | 0.272 (n=1640) | REJECTED | below_safety_margin(1238952709459<7225240482219), p_lower_below_threshold(0.27<0.75) |
| 59929973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 61.575826 USDC | 0.007473 USDC | 0.000000 USDC | 0.005339 USDC | 0.002134 USDC (0.0020 €) | — | 0.35 | 0.272 (n=1640) | REJECTED | below_safety_margin(2134<12315), p_lower_below_threshold(0.27<0.75) |
| 59929973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 61.575826 USDC | 0.007473 USDC | 0.000000 USDC | 0.005339 USDC | 0.002134 USDC (0.0020 €) | — | 0.35 | 0.272 (n=1640) | REJECTED | below_safety_margin(2134<12315), p_lower_below_threshold(0.27<0.75) |
| 59929431 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.027457 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0019 €) | — | 0.42 | 0.253 (n=31) | REJECTED | below_safety_margin(1162513404157<5491445151273), p_lower_below_threshold(0.25<0.75) |
| 59929431 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 47.666953 USDC | 0.005718 USDC | 0.000000 USDC | 0.003703 USDC | 0.002015 USDC (0.0019 €) | — | 0.42 | 0.253 (n=31) | REJECTED | below_safety_margin(2015<9533), p_lower_below_threshold(0.25<0.75) |
| 59929973 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.034538 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.31 | 0.272 (n=1640) | REJECTED | below_safety_margin(1084023188695<6907503286436), p_lower_below_threshold(0.27<0.75) |
| 59929973 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.034538 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.31 | 0.272 (n=1640) | REJECTED | below_safety_margin(1084023188695<6907503286436), p_lower_below_threshold(0.27<0.75) |
| 59929973 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.035097 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.31 | 0.272 (n=1640) | REJECTED | below_safety_margin(1076116133718<7019399357372), p_lower_below_threshold(0.27<0.75) |
| 59929973 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.035097 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.31 | 0.272 (n=1640) | REJECTED | below_safety_margin(1076116133718<7019399357372), p_lower_below_threshold(0.27<0.75) |
| 59929973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 59.619416 USDC | 0.007205 USDC | 0.000000 USDC | 0.005339 USDC | 0.001866 USDC (0.0017 €) | — | 0.31 | 0.272 (n=1640) | REJECTED | below_safety_margin(1866<11923), p_lower_below_threshold(0.27<0.75) |
| 59929973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 59.619416 USDC | 0.007205 USDC | 0.000000 USDC | 0.005339 USDC | 0.001866 USDC (0.0017 €) | — | 0.31 | 0.272 (n=1640) | REJECTED | below_safety_margin(1866<11923), p_lower_below_threshold(0.27<0.75) |
| 59929973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 61.225253 USDC | 0.007192 USDC | 0.000000 USDC | 0.005339 USDC | 0.001853 USDC (0.0017 €) | — | 0.30 | 0.272 (n=1640) | REJECTED | below_safety_margin(1853<12245), p_lower_below_threshold(0.27<0.75) |
| 59929973 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 61.225253 USDC | 0.007192 USDC | 0.000000 USDC | 0.005339 USDC | 0.001853 USDC (0.0017 €) | — | 0.30 | 0.272 (n=1640) | REJECTED | below_safety_margin(1853<12245), p_lower_below_threshold(0.27<0.75) |
| 59929974 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.034547 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.26 | 0.272 (n=1640) | REJECTED | below_safety_margin(897429294794<6909307717639), p_lower_below_threshold(0.27<0.75) |
| 59929974 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.034547 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.26 | 0.272 (n=1640) | REJECTED | below_safety_margin(897429294794<6909307717639), p_lower_below_threshold(0.27<0.75) |
| 59929974 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 59.954516 USDC | 0.006890 USDC | 0.000000 USDC | 0.005347 USDC | 0.001543 USDC (0.0014 €) | — | 0.26 | 0.272 (n=1640) | REJECTED | below_safety_margin(1543<11990), p_lower_below_threshold(0.27<0.75) |
| 59929974 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 59.954516 USDC | 0.006890 USDC | 0.000000 USDC | 0.005347 USDC | 0.001543 USDC (0.0014 €) | — | 0.26 | 0.272 (n=1640) | REJECTED | below_safety_margin(1543<11990), p_lower_below_threshold(0.27<0.75) |
| 59929974 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.033151 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.23 | 0.272 (n=1640) | REJECTED | below_safety_margin(755010998489<6630196061010), p_lower_below_threshold(0.27<0.75) |
| 59929974 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.033151 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0012 €) | — | 0.23 | 0.272 (n=1640) | REJECTED | below_safety_margin(755010998489<6630196061010), p_lower_below_threshold(0.27<0.75) |
| 59929974 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 57.352599 USDC | 0.006642 USDC | 0.000000 USDC | 0.005347 USDC | 0.001295 USDC (0.0012 €) | — | 0.23 | 0.272 (n=1640) | REJECTED | below_safety_margin(1295<11470), p_lower_below_threshold(0.27<0.75) |
| 59929974 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 57.352599 USDC | 0.006642 USDC | 0.000000 USDC | 0.005347 USDC | 0.001295 USDC (0.0012 €) | — | 0.23 | 0.272 (n=1640) | REJECTED | below_safety_margin(1295<11470), p_lower_below_threshold(0.27<0.75) |
| 59929973 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.012321 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 0.58 | 0.272 (n=1640) | REJECTED | below_safety_margin(713841419333<2464202969598), p_lower_below_threshold(0.27<0.75) |
| 59929973 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.012321 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 0.58 | 0.272 (n=1640) | REJECTED | below_safety_margin(713841419333<2464202969598), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8591 ; taux observé 0.228 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
