# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T17:15:42+00:00 ; durée 79.79 min ; blocs 59998862 → 60022791 (3176 vus)

## Connexion
- Requêtes RPC : 39191 ; erreurs : 45 ; latence p50/p95 : 500.2/1,632.5 ms
- Rafraîchissements d'état : 3176 ; âge des données au dernier bloc : 7.98 s ; changements de frais LP observés (pools à frais dynamiques) : 5498
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5819 ; cycles déclenchés par événement : 1196 ; avance médiane sur le rafraîchissement multicall : 440 ms
- Gaz : base fee 0.005438 gwei ; prix ETH (pool le plus profond) : 1,630.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 244 jetons, 12400 routes
- Par DEX : uniswap_v3 121, aerodrome_slipstream 85, aerodrome 168, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 144 (rejetés 2) → 549 jetons ; pools candidats 3576 (énumérés 252, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1656.803175, 'cbBTC': 59633.257395, 'AERO': 0.391907}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 79,393,892 | 1,630.056123 | 60022819 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,898,696 | 0.027492 | 60022819 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,552,443 | 1,628.099240 | 60022819 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,195,413 | 0.027556 | 60022819 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,085,383 | 83.323248 | 60022819 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,630,695 | 0.000017 | 60022819 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,784,522 | 0.027488 | 60022819 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,470,061 | 2.553446 | 60022819 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,122,492 | 0.998713 | 60022819 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,892,186 | 1,627.940928 | 60022819 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,453,624 | 41,304.303734 | 60022819 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 262 | 2,145,866 | 1,628.301210 | 60022819 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,810,230 | 0.000017 | 60022819 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 1,597,162 | 0.027546 | 60022819 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,551,040 | 1,119,579.501926 | 60022819 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,213 | 0.843928 | 60022819 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 1,305,453 | 0.000017 | 60022819 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,236,442 | 0.000000 | 60022819 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,172,925 | 0.000017 | 60022819 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,169,262 | 0.006551 | 60022819 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,059,536 | 86.558041 | 60022819 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,054,591 | 16.398473 | 60022819 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 969,289 | 456.167695 | 60022819 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 957,800 | 1,630.107027 | 60022819 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 947,153 | 16,552.599640 | 60022819 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 926,760 | 4,164.855654 | 60022819 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 910,869 | 82.748080 | 60022819 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 870,930 | 0.051146 | 60022819 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 865,534 | 1,630.685786 | 60022819 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 857,580 | 30,942,562.559710 | 60022819 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 776,663 | 70.928453 | 60022819 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 761,916 | 525,274.982238 | 60022819 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 745,972 | 0.001524 | 60022819 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 735,003 | 22,195,554.911646 | 60022819 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | XDP/USDC | 100 | 729,393 | 0.014911 | 60022819 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | DRB/WETH | 10000 | 726,944 | 0.000000 | 60022819 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| pancakeswap_v3 | QUID/USDC | 100 | 706,548 | 0.044357 | 60022819 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 704,655 | 25.163352 | 60022819 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/MORPHO | 3000 | 678,818 | 1,088.759677 | 60022819 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 671,875 | 1,628.048043 | 60022819 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 10000 | 669,842 | 1,641.151788 | 60022819 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 585,354 | 1,628.305728 | 60022819 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 565,128 | 0.402476 | 60022819 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 553,092 | 0.799406 | 60022819 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 520,103 | 4,674,526.835119 | 60022819 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 60022819 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/AERO | 10000 | 505,549 | 4,191.004814 | 60022819 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 476,724 | 0.029641 | 60022819 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 3718 | 474,657 | 525,777.054078 | 60022819 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| pancakeswap_v3 | ELSA/USDC | 100 | 457,542 | 0.065459 | 60022819 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v2 | WETH/NPC | 3000 | 422,222 | 189,824.384062 | 60022819 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 417,172 | 0.000007 | 60022819 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | cbBTC/EDGE | 7000 | 364,999 | 847,585.698426 | 60022819 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 362,575 | 22.198182 | 60022819 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | AWE/USDC | 3000 | 361,508 | 0.054343 | 60022819 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 346,565 | 368.753488 | 60022819 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/DEGEN | 3000 | 339,802 | 2,461,019.919393 | 60022819 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| aerodrome_slipstream | WETH/VVV | 2709 | 335,504 | 83.301847 | 60022819 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 333,658 | 0.000229 | 60022819 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/SPX | 10000 | 323,807 | 6,225.940648 | 60022819 | `0xe96a4E9EA3a2C6Db214174738a19Eb7Dbb8A3069` |

## Recherche d'opportunités
- Cycles : 4371 ; routes examinées : 54200400 ; candidats optimisés : 165761 ; net attendu > 0 : 213 ; dernier cycle 739.2 ms
- Rejets (moteur) : {'spread_below_threshold': 52405579, 'liquidity_below_min': 930533, 'negative_expected_net': 165548, 'cycle_budget_exhausted': 9430, 'borrow_bound_too_small': 6975, 'unquotable': 2165}
- Enregistrements de la session : 138592 ; net attendu > 0 : 213 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 3/5 positives
- Décisions : {'REJECTED': 138592} ; motifs de rejet : {'below_safety_margin': 163, 'negative_expected_net': 138379, 'p_lower_below_threshold': 205, 'reliability_not_demonstrated': 8, 'stale_data': 106}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60000947 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.063469 WETH | 0.000067 WETH | 0.000000 WETH | 0.000013 WETH | 0.000054 WETH (0.0812 €) | 0.000054 WETH | 8.50 | 0.113 (n=166) | REJECTED | stale_data(5770ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 101.213571 USDC | 0.109088 USDC | 0.000000 USDC | 0.021135 USDC | 0.087953 USDC (0.0809 €) | — | 8.69 | 0.113 (n=166) | REJECTED | stale_data(5765ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 60000947 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.053374 WETH | 0.000051 WETH | 0.000000 WETH | 0.000013 WETH | 0.000038 WETH (0.0569 €) | 0.000038 WETH | 7.09 | 0.334 (n=637) | REJECTED | stale_data(5880ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 87.164835 USDC | 0.082973 USDC | 0.000000 USDC | 0.021135 USDC | 0.061838 USDC (0.0569 €) | — | 7.09 | 0.334 (n=637) | REJECTED | stale_data(5875ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60000947 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.022730 WETH | 0.000046 WETH | 0.000000 WETH | 0.000012 WETH | 0.000033 WETH (0.0503 €) | 0.000033 WETH | 14.71 | 0.122 (n=69) | REJECTED | stale_data(5347ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 36.982921 USDC | 0.074836 USDC | 0.000000 USDC | 0.020305 USDC | 0.054531 USDC (0.0502 €) | — | 14.74 | 0.122 (n=69) | REJECTED | stale_data(5354ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 60000947 | WETH→[aerodrome_slipstream]→LINK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.043576 WETH | 0.000046 WETH | 0.000000 WETH | 0.000013 WETH | 0.000033 WETH (0.0496 €) | — | 7.57 | 0.334 (n=637) | REJECTED | stale_data(5788ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LINK→[uniswap_v3]→USDC | 71.131459 USDC | 0.075871 USDC | 0.000000 USDC | 0.022047 USDC | 0.053824 USDC (0.0495 €) | — | 7.57 | 0.334 (n=637) | REJECTED | stale_data(5793ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60009343 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 256.572512 USDC | 0.061095 USDC | 0.000000 USDC | 0.014999 USDC | 0.046096 USDC (0.0424 €) | — | 1.80 | 0.110 (n=381) | REJECTED | below_safety_margin(46096<51314), p_lower_below_threshold(0.11<0.75) |
| 60009343 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 256.572512 USDC | 0.061095 USDC | 0.000000 USDC | 0.014999 USDC | 0.046096 USDC (0.0424 €) | — | 1.80 | 0.110 (n=381) | REJECTED | below_safety_margin(46096<51314), p_lower_below_threshold(0.11<0.75) |
| 60009343 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.156648 WETH | 0.000037 WETH | 0.000000 WETH | 0.000009 WETH | 0.000028 WETH (0.0423 €) | — | 1.79 | 0.110 (n=381) | REJECTED | below_safety_margin(28068861843051<31329648402441), p_lower_below_threshold(0.11<0.75) |
| 60009343 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.156648 WETH | 0.000037 WETH | 0.000000 WETH | 0.000009 WETH | 0.000028 WETH (0.0423 €) | — | 1.79 | 0.110 (n=381) | REJECTED | below_safety_margin(28068861843051<31329648402441), p_lower_below_threshold(0.11<0.75) |
| 60000947 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.021060 WETH | 0.000039 WETH | 0.000000 WETH | 0.000012 WETH | 0.000027 WETH (0.0406 €) | — | 12.80 | 0.122 (n=69) | REJECTED | stale_data(5390ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 34.375785 USDC | 0.064283 USDC | 0.000000 USDC | 0.020305 USDC | 0.043978 USDC (0.0405 €) | — | 12.79 | 0.122 (n=69) | REJECTED | stale_data(5395ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 60000947 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.041146 WETH | 0.000039 WETH | 0.000000 WETH | 0.000012 WETH | 0.000027 WETH (0.0402 €) | — | 6.49 | 0.185 (n=339) | REJECTED | stale_data(5851ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 66.995257 USDC | 0.063886 USDC | 0.000000 USDC | 0.020305 USDC | 0.043581 USDC (0.0401 €) | — | 6.51 | 0.185 (n=339) | REJECTED | stale_data(5855ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 60000947 | WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.020800 WETH | 0.000038 WETH | 0.000000 WETH | 0.000013 WETH | 0.000025 WETH (0.0383 €) | — | 12.22 | 0.030 (n=48) | REJECTED | stale_data(5400ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 60000947 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AUKI→[aerodrome]→USDC | 33.864057 USDC | 0.062702 USDC | 0.000000 USDC | 0.021218 USDC | 0.041484 USDC (0.0382 €) | — | 12.25 | 0.030 (n=48) | REJECTED | stale_data(5405ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 60010780 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.118384 WETH | 0.000035 WETH | 0.000000 WETH | 0.000010 WETH | 0.000025 WETH (0.0376 €) | 0.000025 WETH | 2.11 | 0.277 (n=1667) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 60010780 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003253 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0376 €) | 0.000001 cbBTC | 2.12 | 0.277 (n=1667) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 60010780 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 204.019356 USDC | 0.057433 USDC | 0.000000 USDC | 0.016700 USDC | 0.040733 USDC (0.0375 €) | — | 2.00 | 0.277 (n=1667) | REJECTED | below_safety_margin(40733<40803), p_lower_below_threshold(0.28<0.75) |
| 60000947 | WETH→[aerodrome_slipstream]→LINK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.038114 WETH | 0.000035 WETH | 0.000000 WETH | 0.000013 WETH | 0.000021 WETH (0.0321 €) | — | 5.60 | 0.334 (n=637) | REJECTED | stale_data(5898ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LINK→[uniswap_v3]→USDC | 62.401420 USDC | 0.056891 USDC | 0.000000 USDC | 0.022047 USDC | 0.034844 USDC (0.0321 €) | — | 5.58 | 0.334 (n=637) | REJECTED | stale_data(5904ms>4000.0), p_lower_below_threshold(0.33<0.75) |
| 60000947 | WETH→[aerodrome]→LCAP→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.025487 WETH | 0.000033 WETH | 0.000000 WETH | 0.000012 WETH | 0.000021 WETH (0.0314 €) | — | 8.19 | 0.072 (n=222) | REJECTED | stale_data(5582ms>4000.0), p_lower_below_threshold(0.07<0.75) |
| 60000947 | USDC→[uniswap_v3]→WETH→[aerodrome]→LCAP→[aerodrome]→USDC | 41.507142 USDC | 0.053503 USDC | 0.000000 USDC | 0.019475 USDC | 0.034028 USDC (0.0313 €) | — | 8.20 | 0.072 (n=222) | REJECTED | stale_data(5585ms>4000.0), p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 8717 ; taux observé 0.230 ; borne inférieure crédible (0.9) 0.225 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
