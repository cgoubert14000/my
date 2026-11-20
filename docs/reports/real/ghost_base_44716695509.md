# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T12:31:53+00:00 ; durée 136.94 min ; blocs 59896587 → 59937659 (13293 vus)

## Connexion
- Requêtes RPC : 122680 ; erreurs : 0 ; latence p50/p95 : 79.3/826.8 ms
- Rafraîchissements d'état : 13293 ; âge des données au dernier bloc : 4.59 s ; changements de frais LP observés (pools à frais dynamiques) : 6489
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16431 ; cycles déclenchés par événement : 3401 ; avance médiane sur le rafraîchissement multicall : 154 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,738.60 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 84,824,662 | 1,738.598203 | 59937667 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,043,845 | 0.028265 | 59937667 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,186,382 | 1,737.240781 | 59937667 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,614,676 | 0.028289 | 59937667 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,410,262 | 85.424706 | 59937667 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,990,065 | 0.000016 | 59937667 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,128,129 | 0.028257 | 59937667 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,574,464 | 2.408579 | 59937667 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,370,351 | 1,737.017996 | 59937667 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,239,330 | 0.998714 | 59937667 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,681,035 | 39,354.970785 | 59937667 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 224 | 2,277,943 | 1,736.855514 | 59937667 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,905,869 | 0.000016 | 59937667 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,696,378 | 0.028276 | 59937667 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,637,351 | 1,142,907.098486 | 59937667 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,492 | 0.844819 | 59937667 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,375,314 | 0.000016 | 59937667 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,315,899 | 0.000000 | 59937667 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,239,035 | 0.006454 | 59937667 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,233,401 | 0.000016 | 59937667 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,101,902 | 14.628329 | 59937667 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,917 | 86.495839 | 59937667 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,031,989 | 459.603466 | 59937667 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 991,775 | 16,228.142957 | 59937667 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 991,639 | 85.794022 | 59937667 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 989,041 | 1,738.318652 | 59937667 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 983,867 | 4,192.582386 | 59937667 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 905,990 | 31,704,188.062133 | 59937667 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/USDC | 3000 | 893,973 | 1,738.849574 | 59937667 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | USDC/VVV | 3000 | 892,724 | 0.049175 | 59937667 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/BRETT | 10000 | 811,434 | 527,713.721501 | 59937667 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 807,909 | 65.548118 | 59937667 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 783,574 | 0.000000 | 59937667 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 778,438 | 22,446,056.229025 | 59937667 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 771,612 | 0.001516 | 59937667 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 746,451 | 0.015579 | 59937667 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 722,293 | 0.046365 | 59937667 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| pancakeswap_v3 | WETH/USDC | 500 | 720,957 | 1,737.234638 | 59937667 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/MORPHO | 3000 | 719,970 | 1,096.633773 | 59937667 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 709,830 | 24.897622 | 59937667 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 692,884 | 1,743.566465 | 59937667 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 616,455 | 1,736.959740 | 59937667 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 590,403 | 0.798100 | 59937667 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 583,940 | 0.428812 | 59937667 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 551,259 | 4,733,295.521158 | 59937667 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 537,578 | 4,190.092648 | 59937667 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59937667 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 504,949 | 530,618.109539 | 59937667 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 492,319 | 0.031090 | 59937667 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 458,823 | 182,704.893376 | 59937667 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 11 | 456,580 | 1.001632 | 59937667 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 439,600 | 0.000007 | 59937667 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 431,886 | 0.060935 | 59937667 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3043 | 390,397 | 1,096.654840 | 59937667 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 382,000 | 23.790496 | 59937667 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 376,602 | 862,782.565960 | 59937667 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 376,599 | 362.539056 | 59937667 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 366,467 | 0.055844 | 59937667 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 357,458 | 0.000231 | 59937667 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/VVV | 2715 | 356,114 | 85.460359 | 59937667 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 16685 ; routes examinées : 212566900 ; candidats optimisés : 184620 ; net attendu > 0 : 152 ; dernier cycle 1350.7 ms
- Rejets (moteur) : {'spread_below_threshold': 208541232, 'liquidity_below_min': 2202274, 'negative_expected_net': 184468, 'cycle_budget_exhausted': 30862, 'borrow_bound_too_small': 29156}
- Enregistrements de la session : 72002 ; net attendu > 0 : 152 ; simulés (eth_call de la vraie tx) : 8 (ok 6, échec 2) ; étiquettes ghost N+1 : 7/8 positives
- Décisions : {'REJECTED': 72002} ; motifs de rejet : {'below_safety_margin': 142, 'negative_expected_net': 71850, 'p_lower_below_threshold': 152, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59931575 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931589 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.457140 USDC | 0.119872 USDC | 0.000000 USDC | 0.004198 USDC | 0.115674 USDC (0.1064 €) | — | 1.69 | 0.111 (n=380) | REJECTED | below_safety_margin(115674<137291), p_lower_below_threshold(0.11<0.75) |
| 59931575 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59931589 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.397053 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000067 WETH (0.1063 €) | — | 1.68 | 0.111 (n=380) | REJECTED | below_safety_margin(66717612332529<79410520469949), p_lower_below_threshold(0.11<0.75) |
| 59931575 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 283.558757 USDC | 0.042818 USDC | 0.000000 USDC | 0.003935 USDC | 0.038883 USDC (0.0358 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(38883<56711), p_lower_below_threshold(0.10<0.75) |
| 59931589 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 283.558757 USDC | 0.042818 USDC | 0.000000 USDC | 0.003935 USDC | 0.038883 USDC (0.0358 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(38883<56711), p_lower_below_threshold(0.10<0.75) |
| 59931575 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.163619 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0357 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(22426759358077<32723734311580), p_lower_below_threshold(0.10<0.75) |
| 59931589 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.163619 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0357 €) | — | 1.37 | 0.098 (n=128) | REJECTED | below_safety_margin(22426759358077<32723734311580), p_lower_below_threshold(0.10<0.75) |
| 59931546 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 316.509578 USDC | 0.026700 USDC | 0.000000 USDC | 0.004195 USDC | 0.022505 USDC (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(22505<63301), p_lower_below_threshold(0.11<0.75) |
| 59931553 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 316.509578 USDC | 0.026700 USDC | 0.000000 USDC | 0.004195 USDC | 0.022505 USDC (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(22505<63301), p_lower_below_threshold(0.11<0.75) |
| 59931546 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.183276 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(12977313126533<36655103564637), p_lower_below_threshold(0.11<0.75) |
| 59931553 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.183276 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0207 €) | — | 0.71 | 0.111 (n=380) | REJECTED | below_safety_margin(12977313126533<36655103564637), p_lower_below_threshold(0.11<0.75) |
| 59930972 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002191 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 0.55 | 0.273 (n=1642) | REJECTED | below_safety_margin(12<43), p_lower_below_threshold(0.27<0.75) |
| 59930976 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002191 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0068 €) | — | 0.55 | 0.273 (n=1642) | REJECTED | below_safety_margin(12<43), p_lower_below_threshold(0.27<0.75) |
| 59930972 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 141.251327 USDC | 0.012521 USDC | 0.000000 USDC | 0.005329 USDC | 0.007192 USDC (0.0066 €) | — | 0.51 | 0.273 (n=1642) | REJECTED | below_safety_margin(7192<28250), p_lower_below_threshold(0.27<0.75) |
| 59930976 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 141.251327 USDC | 0.012521 USDC | 0.000000 USDC | 0.005329 USDC | 0.007192 USDC (0.0066 €) | — | 0.51 | 0.273 (n=1642) | REJECTED | below_safety_margin(7192<28250), p_lower_below_threshold(0.27<0.75) |
| 59930972 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.081307 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0066 €) | — | 0.51 | 0.273 (n=1642) | REJECTED | below_safety_margin(4114685510798<16261403177937), p_lower_below_threshold(0.27<0.75) |
| 59930976 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.081307 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0066 €) | — | 0.51 | 0.273 (n=1642) | REJECTED | below_safety_margin(4114685510798<16261403177937), p_lower_below_threshold(0.27<0.75) |
| 59935635 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 32.839741 USDC | 0.010772 USDC | 0.000000 USDC | 0.003953 USDC | 0.006819 USDC (0.0063 €) | — | 2.08 | 0.111 (n=380) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 59930972 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.004274 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0051 €) | — | 0.21 | 0.273 (n=1642) | REJECTED | below_safety_margin(9<85), p_lower_below_threshold(0.27<0.75) |
| 59930976 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.004274 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0051 €) | — | 0.21 | 0.273 (n=1642) | REJECTED | below_safety_margin(9<85), p_lower_below_threshold(0.27<0.75) |
| 59913838 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 12.932215 USDC | 0.009418 USDC | 0.000000 USDC | 0.003954 USDC | 0.005464 USDC (0.0050 €) | — | 4.23 | 0.077 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 59930390 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.014918 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | 0.000005 WETH | 2.06 | 0.272 (n=1640) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59930390 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 25.549414 USDC | 0.010634 USDC | 0.000000 USDC | 0.005344 USDC | 0.005290 USDC (0.0049 €) | 0.007877 USDC | 2.07 | 0.272 (n=1640) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 59930972 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.157220 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0048 €) | — | 0.19 | 0.273 (n=1642) | REJECTED | below_safety_margin(3019027987537<31443911899138), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8598 ; taux observé 0.229 ; borne inférieure crédible (0.9) 0.223 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
