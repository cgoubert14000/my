# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T15:23:27+00:00 ; durée 308.51 min ; blocs 59896587 → 59989146 (28975 vus)

## Connexion
- Requêtes RPC : 269759 ; erreurs : 95 ; latence p50/p95 : 175.8/925.8 ms
- Rafraîchissements d'état : 28976 ; âge des données au dernier bloc : 3.9 s ; changements de frais LP observés (pools à frais dynamiques) : 18126
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 64027 ; cycles déclenchés par événement : 11426 ; avance médiane sur le rafraîchissement multicall : 161 ms
- Gaz : base fee 0.020220 gwei ; prix ETH (pool le plus profond) : 1,679.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 82,674,017 | 1,679.108746 | 59989129 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,427,491 | 0.027882 | 59989129 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,978,508 | 1,675.780957 | 59989137 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,387,482 | 0.027899 | 59989129 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,269,149 | 83.305890 | 59989142 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,850,378 | 0.000017 | 59989129 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,002,226 | 0.027881 | 59989137 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,486,117 | 2.532205 | 59989129 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 3,171,669 | 0.998617 | 59989129 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,017,309 | 1,675.521203 | 59989146 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,573,716 | 39,832.948884 | 59989129 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 735 | 2,207,398 | 1,675.138635 | 59989129 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,873,415 | 0.000017 | 59989129 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2710 | 1,642,017 | 0.027889 | 59989129 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,590,533 | 1,129,713.019288 | 59989129 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,477 | 0.843780 | 59989129 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,350,449 | 0.000017 | 59989129 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,271,879 | 0.000000 | 59989129 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,210,668 | 0.000017 | 59989137 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,169,650 | 0.006326 | 59989129 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,067,037 | 15.896502 | 59989133 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,621 | 86.544226 | 59989129 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 995,499 | 461.997156 | 59989129 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 972,035 | 1,679.143469 | 59989129 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 962,577 | 16,545.715471 | 59989129 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 939,974 | 4,250.569857 | 59989129 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 937,596 | 83.924543 | 59989129 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 889,810 | 0.049637 | 59989129 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 878,461 | 1,680.087340 | 59989142 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 873,376 | 31,870,617.535109 | 59989129 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 788,170 | 68.872399 | 59989129 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 780,660 | 533,478.758276 | 59989129 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 757,502 | 22,176,696.239115 | 59989129 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 751,390 | 0.001499 | 59989129 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | DRB/WETH | 10000 | 742,200 | 0.000000 | 59989129 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | XDP/USDC | 100 | 737,324 | 0.015219 | 59989129 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 719,763 | 0.046037 | 59989129 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| pancakeswap_v3 | WETH/USDC | 500 | 699,321 | 1,675.590492 | 59989129 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/SAPIEN | 4880 | 694,198 | 25.672927 | 59989129 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/MORPHO | 3000 | 687,602 | 1,110.049789 | 59989129 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 681,298 | 1,689.627578 | 59989129 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | TIG/USDC | 10000 | 575,386 | 0.416743 | 59989129 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v3 | WETH/USDC | 100 | 574,988 | 1,675.477044 | 59989142 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 569,736 | 0.799406 | 59989129 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 537,175 | 4,649,662.738399 | 59989129 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 515,244 | 4,262.693180 | 59989129 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59989129 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3748 | 484,972 | 536,662.006029 | 59989129 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 480,785 | 0.030022 | 59989129 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 458,998 | 0.065724 | 59989146 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 17 | 455,910 | 1.002434 | 59989139 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v2 | WETH/NPC | 3000 | 431,811 | 192,502.581870 | 59989129 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 421,483 | 0.000007 | 59989129 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | WETH/uSOL | 3000 | 373,062 | 23.119690 | 59989129 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome_slipstream | WETH/MORPHO | 3055 | 372,751 | 1,110.420806 | 59989129 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 369,100 | 857,809.770631 | 59989129 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 363,094 | 0.054821 | 59989129 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 357,062 | 369.617279 | 59989129 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2820 | 345,226 | 83.335970 | 59989129 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | WETH/DEGEN | 3000 | 343,840 | 2,549,735.976357 | 59989129 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 40401 ; routes examinées : 514708740 ; candidats optimisés : 694648 ; net attendu > 0 : 1478 ; dernier cycle 685.3 ms
- Rejets (moteur) : {'spread_below_threshold': 503813100, 'liquidity_below_min': 6053807, 'negative_expected_net': 693170, 'cycle_budget_exhausted': 76685, 'pool_quarantined': 72560, 'borrow_bound_too_small': 57434, 'no_price_reference': 279}
- Enregistrements de la session : 409304 ; net attendu > 0 : 1478 ; simulés (eth_call de la vraie tx) : 133 (ok 41, échec 92) ; étiquettes ghost N+1 : 42/104 positives
- Décisions : {'REJECTED': 409304} ; motifs de rejet : {'below_safety_margin': 954, 'negative_expected_net': 407826, 'p_lower_below_threshold': 1441, 'price_impact': 145, 'reliability_not_demonstrated': 37, 'sim_below_estimate': 15, 'simulated_net_nonpositive': 10, 'simulation_failed': 92, 'stale_data': 126}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59986570 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.542832 WETH | 0.000110 WETH | 0.000000 WETH | 0.000005 WETH | 0.000105 WETH (0.1664 €) | — | 1.94 | 0.276 (n=1653) | REJECTED | below_safety_margin(105453345218430<108566410041576), p_lower_below_threshold(0.28<0.75) |
| 59986570 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 929.597658 USDC | 0.188458 USDC | 0.000000 USDC | 0.007950 USDC | 0.180508 USDC (0.1661 €) | — | 1.94 | 0.276 (n=1653) | REJECTED | below_safety_margin(180508<185919), p_lower_below_threshold(0.28<0.75) |
| 59986570 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.014710 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1658 €) | — | 2.01 | 0.276 (n=1653) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59986570 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.009526 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1636 €) | — | 3.07 | 0.076 (n=513) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 59986570 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 581.678195 USDC | 0.183827 USDC | 0.000000 USDC | 0.006347 USDC | 0.177480 USDC (0.1633 €) | — | 3.05 | 0.076 (n=513) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 59986570 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.365073 WETH | 0.000081 WETH | 0.000000 WETH | 0.000005 WETH | 0.000076 WETH (0.1207 €) | — | 2.10 | 0.276 (n=1653) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 59986570 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 625.326847 USDC | 0.138939 USDC | 0.000000 USDC | 0.007950 USDC | 0.130989 USDC (0.1205 €) | — | 2.09 | 0.276 (n=1653) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59986570 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010072 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1204 €) | — | 2.13 | 0.276 (n=1653) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59931575 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931589 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931575 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59931589 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59986570 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.006554 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0941 €) | — | 2.56 | 0.276 (n=1653) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59986570 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.230430 WETH | 0.000064 WETH | 0.000000 WETH | 0.000005 WETH | 0.000059 WETH (0.0935 €) | — | 2.57 | 0.276 (n=1653) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |
| 59986570 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 427.458780 USDC | 0.109848 USDC | 0.000000 USDC | 0.008338 USDC | 0.101510 USDC (0.0934 €) | — | 2.37 | 0.276 (n=1653) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59975591 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 363.997118 USDC | 0.107146 USDC | 0.000000 USDC | 0.008095 USDC | 0.099051 USDC (0.0911 €) | — | 2.72 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005606 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0910 €) | — | 2.85 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.216239 WETH | 0.000061 WETH | 0.000000 WETH | 0.000005 WETH | 0.000057 WETH (0.0909 €) | -0.000001 WETH | 2.61 | 0.273 (n=1646) | REJECTED | sim_below_estimate(3842308596892<61157677787177), simulated_net_nonpositive, p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.269412 WETH | 0.000060 WETH | 0.000000 WETH | 0.000005 WETH | 0.000056 WETH (0.0894 €) | — | 2.06 | 0.273 (n=1646) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 59975591 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.007429 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0893 €) | — | 2.11 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 497.623320 USDC | 0.105172 USDC | 0.000000 USDC | 0.008095 USDC | 0.097077 USDC (0.0893 €) | — | 1.95 | 0.273 (n=1646) | REJECTED | below_safety_margin(97077<99524), p_lower_below_threshold(0.27<0.75) |
| 59975591 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.268883 WETH | 0.000060 WETH | 0.000000 WETH | 0.000005 WETH | 0.000055 WETH (0.0886 €) | — | 2.05 | 0.273 (n=1646) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.27<0.75) |
| 59975591 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.007423 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.0882 €) | — | 2.09 | 0.273 (n=1646) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59975591 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 480.766129 USDC | 0.103900 USDC | 0.000000 USDC | 0.008095 USDC | 0.095805 USDC (0.0881 €) | — | 1.99 | 0.273 (n=1646) | REJECTED | below_safety_margin(95805<96153), p_lower_below_threshold(0.27<0.75) |
| 59986570 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.215686 WETH | 0.000059 WETH | 0.000000 WETH | 0.000005 WETH | 0.000055 WETH (0.0862 €) | — | 2.53 | 0.276 (n=1653) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.28<0.75) |

## Fiabilité et décision
- Observations ghost : 8694 ; taux observé 0.230 ; borne inférieure crédible (0.9) 0.224 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
