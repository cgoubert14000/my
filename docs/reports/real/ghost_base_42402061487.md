# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T19:23:01+00:00 ; durée 42.74 min ; blocs 54432179 → 54444994 (3585 vus)

## Connexion
- Requêtes RPC : 35493 ; erreurs : 0 ; latence p50/p95 : 90.5/1,552.2 ms
- Rafraîchissements d'état : 3585 ; âge des données au dernier bloc : 7.02 s ; changements de frais LP observés (pools à frais dynamiques) : 870
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2880 ; cycles déclenchés par événement : 828 ; avance médiane sur le rafraîchissement multicall : 205 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,234.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 473 pools, 277 jetons, 17824 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 96, aerodrome 198, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 169 (rejetés 2) → 574 jetons ; pools candidats 3672 (énumérés 292, par paires 0), mesurés 476, sous le plancher de 10000.0 $ : 3 → gardés 473 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.638115, 'cbBTC': 75748.316454, 'AERO': 0.612979}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,736,363 | 2,234.628809 | 54445013 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,809,208 | 0.029487 | 54445013 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,340,950 | 0.000013 | 54445013 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,161,057 | 0.029513 | 54445013 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,057,828 | 2,232.166061 | 54445013 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,329,918 | 108.592603 | 54445013 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,410,898 | 0.001549 | 54445013 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,165,337 | 0.029478 | 54445013 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,899,394 | 1.632407 | 54445013 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,219,707 | 2,231.730508 | 54445013 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,989,017 | 0.998992 | 54445013 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,327,481 | 42,207.990901 | 54445013 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,186,344 | 2,231.609497 | 54445013 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,546,817 | 0.029525 | 54445013 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,100,349 | 1,147,424.274597 | 54445013 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,737,031 | 0.000013 | 54445013 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,695,892 | 0.006747 | 54445013 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,645,229 | 0.000013 | 54445013 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,631,032 | 0.000000 | 54445013 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,599,215 | 0.015978 | 54445013 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,524,824 | 437.527452 | 54445013 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,504,508 | 0.000013 | 54445013 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,494,357 | 1.466903 | 54445013 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54445013 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,396,307 | 3,643.607954 | 54445013 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,324,789 | 2,234.919022 | 54445013 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,643 | 2,238.133456 | 54445013 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,269,128 | 14,848.856752 | 54445013 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,308 | 2,232.230363 | 54445013 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,471 | 76.986684 | 54445013 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,106,166 | 36,110,001.238542 | 54445013 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,043,761 | 109.234854 | 54445013 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,016,445 | 570,246.531723 | 54445013 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,400 | 22,537,303.536336 | 54445013 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 982,695 | 19.936075 | 54445013 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 976,954 | 0.000000 | 54445013 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/MORPHO | 3000 | 941,499 | 1,055.364412 | 54445013 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,368 | 2,228.787514 | 54445013 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 925,645 | 0.000013 | 54445013 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 918,707 | 74.242786 | 54445013 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 875,059 | 99,479.785313 | 54445013 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 817,506 | 0.048659 | 54445013 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 793,352 | 3,663.435290 | 54445013 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 791,950 | 21.197687 | 54445013 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,215 | 0.055284 | 54445013 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,089 | 0.799699 | 54445013 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 718,350 | 0.565149 | 54445013 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,846 | 4,894,894.675211 | 54445013 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 683,149 | 0.000253 | 54445013 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 674,688 | 0.574487 | 54445013 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 660,625 | 0.000008 | 54445013 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 647,772 | 150,467.698182 | 54445013 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 621,539 | 570,301.571421 | 54445013 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 589,116 | 0.041007 | 54445013 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 587,319 | 2.472336 | 54445013 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 527,568 | 1,055.063272 | 54445013 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 519,007 | 899,970.460963 | 54445013 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 515,845 | 2,231.764126 | 54445013 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 513,856 | 0.076220 | 54445013 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 504,433 | 7,196.809503 | 54445013 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 4412 ; routes examinées : 78639488 ; candidats optimisés : 40127 ; net attendu > 0 : 171 ; dernier cycle 28.0 ms
- Rejets (moteur) : {'spread_below_threshold': 77499723, 'liquidity_below_min': 1094286, 'negative_expected_net': 39956, 'borrow_bound_too_small': 4412, 'cycle_budget_exhausted': 724, 'pool_quarantined': 216}
- Enregistrements de la session : 40127 ; net attendu > 0 : 171 ; simulés (eth_call de la vraie tx) : 21 (ok 3, échec 18) ; étiquettes ghost N+1 : 3/17 positives
- Décisions : {'REJECTED': 40127} ; motifs de rejet : {'below_safety_margin': 63, 'negative_expected_net': 39956, 'p_lower_below_threshold': 171, 'simulation_failed': 18, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54441177 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.912476 WETH | 0.000347 WETH | 0.000000 WETH | 0.000002 WETH | 0.000345 WETH (0.7087 €) | — | 3.78 | 0.079 (n=96) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 2,035.652673 USDC | 0.774170 USDC | 0.000000 USDC | 0.005018 USDC | 0.769152 USDC (0.7076 €) | — | 3.78 | 0.079 (n=96) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.900158 WETH | 0.000342 WETH | 0.000000 WETH | 0.000003 WETH | 0.000340 WETH (0.6982 €) | — | 3.77 | 0.026 (n=348) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,007.352772 USDC | 0.763436 USDC | 0.000000 USDC | 0.005696 USDC | 0.757740 USDC (0.6971 €) | — | 3.77 | 0.026 (n=348) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54441177 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.022473 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.5041 €) | — | 3.22 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.771353 WETH | 0.000248 WETH | 0.000000 WETH | 0.000003 WETH | 0.000245 WETH (0.5040 €) | — | 3.18 | 0.154 (n=828) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,770.502825 USDC | 0.553561 USDC | 0.000000 USDC | 0.006716 USDC | 0.546845 USDC (0.5031 €) | — | 3.09 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.022769 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4880 €) | — | 3.07 | 0.277 (n=382) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54441177 | WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.789801 WETH | 0.000240 WETH | 0.000000 WETH | 0.000003 WETH | 0.000237 WETH (0.4878 €) | — | 3.00 | 0.277 (n=382) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,770.767158 USDC | 0.536128 USDC | 0.000000 USDC | 0.006716 USDC | 0.529412 USDC (0.4871 €) | — | 2.99 | 0.240 (n=408) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.606885 WETH | 0.000191 WETH | 0.000000 WETH | 0.000003 WETH | 0.000187 WETH (0.3854 €) | — | 3.09 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.017548 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3849 €) | — | 3.15 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,360.687868 USDC | 0.425206 USDC | 0.000000 USDC | 0.007055 USDC | 0.418151 USDC (0.3847 €) | — | 3.07 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.607163 WETH | 0.000183 WETH | 0.000000 WETH | 0.000003 WETH | 0.000180 WETH (0.3707 €) | — | 2.97 | 0.182 (n=1058) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54441177 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.017275 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3702 €) | — | 3.07 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,358.336950 USDC | 0.409090 USDC | 0.000000 USDC | 0.007055 USDC | 0.402035 USDC (0.3699 €) | — | 2.96 | 0.182 (n=1058) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.549665 WETH | 0.000180 WETH | 0.000000 WETH | 0.000002 WETH | 0.000178 WETH (0.3651 €) | — | 3.23 | 0.026 (n=348) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,225.808314 USDC | 0.401126 USDC | 0.000000 USDC | 0.005018 USDC | 0.396108 USDC (0.3644 €) | — | 3.23 | 0.026 (n=348) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54441177 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.358952 WETH | 0.000147 WETH | 0.000000 WETH | 0.000003 WETH | 0.000145 WETH (0.2974 €) | — | 4.03 | 0.079 (n=96) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 799.471843 USDC | 0.328288 USDC | 0.000000 USDC | 0.005696 USDC | 0.322592 USDC (0.2968 €) | — | 4.04 | 0.079 (n=96) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 54441177 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.012502 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2775 €) | — | 3.18 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.439939 WETH | 0.000138 WETH | 0.000000 WETH | 0.000003 WETH | 0.000135 WETH (0.2774 €) | — | 3.07 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 983.462996 USDC | 0.307673 USDC | 0.000000 USDC | 0.006716 USDC | 0.300957 USDC (0.2769 €) | — | 3.06 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.011149 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2705 €) | — | 3.48 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54441177 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.367728 WETH | 0.000134 WETH | 0.000000 WETH | 0.000003 WETH | 0.000131 WETH (0.2699 €) | — | 3.57 | 0.154 (n=828) | REJECTED | p_lower_below_threshold(0.15<0.75) |

## Fiabilité et décision
- Observations ghost : 6088 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
