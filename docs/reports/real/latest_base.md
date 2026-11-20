# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T19:09:54+00:00 ; durée 194.0 min ; blocs 59998862 → 60057039 (8118 vus)

## Connexion
- Requêtes RPC : 97641 ; erreurs : 150 ; latence p50/p95 : 417.2/1,567.8 ms
- Rafraîchissements d'état : 8118 ; âge des données au dernier bloc : 9.31 s ; changements de frais LP observés (pools à frais dynamiques) : 12227
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5819 ; cycles déclenchés par événement : 1196 ; avance médiane sur le rafraîchissement multicall : 440 ms
- Gaz : base fee 0.005339 gwei ; prix ETH (pool le plus profond) : 1,607.85 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 244 jetons, 12400 routes
- Par DEX : uniswap_v3 121, aerodrome_slipstream 85, aerodrome 168, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 144 (rejetés 2) → 549 jetons ; pools candidats 3576 (énumérés 252, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1656.803175, 'cbBTC': 59633.257395, 'AERO': 0.391907}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,355,572 | 1,607.218611 | 60057067 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,703,612 | 0.027588 | 60057067 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,384,059 | 1,603.309881 | 60057067 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,079,162 | 0.027642 | 60057067 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,009,697 | 83.122962 | 60057067 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,494,892 | 0.000017 | 60057067 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,740,851 | 0.027584 | 60057067 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,284,679 | 2.583172 | 60057067 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,069,272 | 0.998485 | 60057067 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,839,844 | 1,603.542034 | 60057067 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,432,176 | 40,898.320321 | 60057067 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 386 | 2,098,578 | 1,603.580324 | 60057067 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,758,870 | 0.000017 | 60057067 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2535 | 1,574,800 | 0.027624 | 60057067 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,543,208 | 1,100,363.616604 | 60057067 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,973 | 0.844047 | 60057067 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 1,275,811 | 0.000017 | 60057067 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,224,237 | 0.000000 | 60057067 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,163,195 | 0.006594 | 60057067 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,139,255 | 0.000017 | 60057067 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,153 | 15.558205 | 60057067 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,451 | 86.571976 | 60057067 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 958,045 | 452.092708 | 60057067 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 951,260 | 1,607.491692 | 60057067 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 936,455 | 16,382.232324 | 60057067 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 916,109 | 4,164.162536 | 60057067 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 901,298 | 82.813206 | 60057067 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 879,203 | 0.051641 | 60057067 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 859,618 | 1,606.426235 | 60057067 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 852,216 | 30,321,776.575042 | 60057067 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 785,777 | 69.292497 | 60057067 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 755,694 | 517,221.947891 | 60057067 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 737,989 | 0.001545 | 60057067 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 728,343 | 22,021,332.043979 | 60057067 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 720,043 | 24.436752 | 60057067 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | XDP/USDC | 100 | 718,350 | 0.014485 | 60057067 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | DRB/WETH | 10000 | 708,738 | 0.000000 | 60057067 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| pancakeswap_v3 | QUID/USDC | 100 | 702,044 | 0.043802 | 60057067 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 676,959 | 1,073.820262 | 60057067 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 661,193 | 1,618.767093 | 60057067 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 633,542 | 1,602.934765 | 60057067 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 100 | 569,634 | 1,603.650921 | 60057067 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 559,997 | 0.395454 | 60057067 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 545,556 | 0.799406 | 60057067 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 513,155 | 4,672,436.536385 | 60057067 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | USDC/MAI (stable) | 3000 | 505,680 | 1.393621 | 60057067 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/AERO | 10000 | 499,237 | 4,191.004814 | 60057067 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | ELSA/USDC | 100 | 487,148 | 0.070856 | 60057067 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 479,121 | 0.029860 | 60057067 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 3778 | 472,004 | 514,000.144660 | 60057067 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 416,995 | 189,356.060075 | 60057067 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 410,634 | 0.000007 | 60057067 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | AWE/USDC | 3000 | 363,135 | 0.054833 | 60057067 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/uSOL | 3000 | 362,149 | 22.078622 | 60057067 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 361,454 | 837,323.072290 | 60057067 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 341,899 | 368.173535 | 60057067 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/DEGEN | 3000 | 339,401 | 2,399,067.021261 | 60057067 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| aerodrome | VIRTUAL/WETH | 10000 | 332,215 | 0.000234 | 60057067 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2703 | 331,514 | 83.104827 | 60057067 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/SPX | 10000 | 317,790 | 6,288.997243 | 60057067 | `0xe96a4E9EA3a2C6Db214174738a19Eb7Dbb8A3069` |

## Recherche d'opportunités
- Cycles : 9313 ; routes examinées : 115481200 ; candidats optimisés : 366848 ; net attendu > 0 : 591 ; dernier cycle 814.6 ms
- Rejets (moteur) : {'spread_below_threshold': 112246655, 'liquidity_below_min': 1671590, 'negative_expected_net': 366257, 'borrow_bound_too_small': 24561, 'cycle_budget_exhausted': 12193, 'unquotable': 2186}
- Enregistrements de la session : 301907 ; net attendu > 0 : 591 ; simulés (eth_call de la vraie tx) : 22 (ok 16, échec 6) ; étiquettes ghost N+1 : 8/18 positives
- Décisions : {'REJECTED': 301907} ; motifs de rejet : {'below_safety_margin': 422, 'negative_expected_net': 301316, 'p_lower_below_threshold': 583, 'reliability_not_demonstrated': 8, 'simulation_failed': 6, 'stale_data': 287}

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
