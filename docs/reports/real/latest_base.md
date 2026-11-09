# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-09T10:13:51+00:00 ; durée 15.24 min ; blocs 55139673 → 55144238 (552 vus)

## Connexion
- Requêtes RPC : 8465 ; erreurs : 0 ; latence p50/p95 : 461.8/1,621.4 ms
- Rafraîchissements d'état : 552 ; âge des données au dernier bloc : 7.86 s ; changements de frais LP observés (pools à frais dynamiques) : 470
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 847 ; cycles déclenchés par événement : 268 ; avance médiane sur le rafraîchissement multicall : 780 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,103.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 465 pools, 272 jetons, 17388 routes
- Par DEX : uniswap_v3 131, aerodrome_slipstream 99, aerodrome 193, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 167 (rejetés 2) → 572 jetons ; pools candidats 3672 (énumérés 289, par paires 0), mesurés 467, sous le plancher de 10000.0 $ : 2 → gardés 465 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2109.380964, 'cbBTC': 74235.499826, 'AERO': 0.565393}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 137,841,849 | 2,103.780455 | 55144238 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,343,206 | 0.028337 | 55144238 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,245,667 | 0.000013 | 55144238 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,652,516 | 0.028398 | 55144238 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,382,109 | 2,099.932948 | 55144238 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,034,567 | 104.428598 | 55144238 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,220,518 | 0.001520 | 55144238 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,599,174 | 0.028335 | 55144238 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,558,991 | 1.770858 | 55144238 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,930,334 | 2,099.750102 | 55144238 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,910,185 | 0.998733 | 55144238 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,110,724 | 42,804.857885 | 55144238 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,999,695 | 2,099.872719 | 55144238 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2550 | 2,339,754 | 0.028389 | 55144238 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,977,319 | 1,147,475.453732 | 55144238 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,701,540 | 0.000013 | 55144238 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,644,126 | 0.000013 | 55144238 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,613,885 | 0.006923 | 55144238 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,572,832 | 0.015611 | 55144238 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,544,649 | 0.000000 | 55144238 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,476,122 | 1.418208 | 55144238 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,452 | 0.821691 | 55144238 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,444,528 | 429.132947 | 55144238 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,439,573 | 0.000013 | 55144238 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,303,815 | 3,732.675931 | 55144238 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,285,839 | 2,103.923037 | 55144238 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,232,880 | 15,119.273852 | 55144238 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,215,696 | 2,102.989554 | 55144238 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,120,185 | 77.439002 | 55144238 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,091,167 | 2,099.877796 | 55144238 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,035,888 | 36,726,664.920069 | 55144238 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,002,488 | 104.886901 | 55144238 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,190 | 21.443497 | 55144238 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 951,081 | 581,300.568066 | 55144238 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 921,504 | 0.000013 | 55144238 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 913,705 | 23,539,313.749702 | 55144238 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 909,679 | 75.723689 | 55144238 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 907,813 | 2,104.880343 | 55144238 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 897,162 | 1,034.892992 | 55144238 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 895,966 | 0.000000 | 55144238 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 833,930 | 0.049641 | 55144238 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 815,078 | 101,565.213812 | 55144238 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| pancakeswap_v3 | QUID/USDC | 100 | 762,927 | 0.051921 | 55144238 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 762,185 | 22.381645 | 55144238 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 737,129 | 3,721.601102 | 55144238 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 712,112 | 0.803267 | 55144238 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 691,723 | 0.535189 | 55144238 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 645,944 | 5,020,948.896237 | 55144238 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 641,730 | 0.521652 | 55144238 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 616,097 | 0.000008 | 55144238 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 612,535 | 149,222.050958 | 55144238 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 587,060 | 0.000252 | 55144238 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 579,392 | 576,712.111747 | 55144238 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,895 | 0.038578 | 55144238 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 528,231 | 2.378996 | 55144238 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 509,723 | 1,034.701624 | 55144238 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 506,297 | 913,662.011814 | 55144238 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | USDC/USDT | 100 | 497,519 | 1.001238 | 55144238 | `0xD56da2B74bA826f19015E6B7Dd9Dae1903E85DA1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 485,160 | 0.070510 | 55144238 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 477,029 | 7,132.606507 | 55144238 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 819 ; routes examinées : 14240772 ; candidats optimisés : 61594 ; net attendu > 0 : 54 ; dernier cycle 514.6 ms
- Rejets (moteur) : {'spread_below_threshold': 13922894, 'liquidity_below_min': 254579, 'negative_expected_net': 61540, 'borrow_bound_too_small': 1638, 'cycle_budget_exhausted': 67}
- Enregistrements de la session : 61594 ; net attendu > 0 : 54 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 61594} ; motifs de rejet : {'below_safety_margin': 54, 'negative_expected_net': 61540, 'p_lower_below_threshold': 42, 'reliability_not_demonstrated': 12, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55141691 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.100895 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0172 €) | — | 0.88 | 0.059 (n=301) | REJECTED | below_safety_margin(8887739178696<20178939300070), p_lower_below_threshold(0.06<0.75) |
| 55141692 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.100895 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0172 €) | — | 0.88 | 0.059 (n=301) | REJECTED | below_safety_margin(8887739178696<20178939300070), p_lower_below_threshold(0.06<0.75) |
| 55141691 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 210.005583 USDC | 0.023725 USDC | 0.000000 USDC | 0.005060 USDC | 0.018665 USDC (0.0172 €) | — | 0.89 | 0.059 (n=301) | REJECTED | below_safety_margin(18665<42001), p_lower_below_threshold(0.06<0.75) |
| 55141692 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 210.005583 USDC | 0.023725 USDC | 0.000000 USDC | 0.005060 USDC | 0.018665 USDC (0.0172 €) | — | 0.89 | 0.059 (n=301) | REJECTED | below_safety_margin(18665<42001), p_lower_below_threshold(0.06<0.75) |
| 55143237 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.121072 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(7336549129306<24214447333590), p_lower_below_threshold(0.06<0.75) |
| 55143238 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.121072 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(7336549129306<24214447333590), p_lower_below_threshold(0.06<0.75) |
| 55143237 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 252.743506 USDC | 0.020164 USDC | 0.000000 USDC | 0.004739 USDC | 0.015425 USDC (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(15425<50548), p_lower_below_threshold(0.06<0.75) |
| 55143238 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 252.743506 USDC | 0.020164 USDC | 0.000000 USDC | 0.004739 USDC | 0.015425 USDC (0.0142 €) | — | 0.61 | 0.059 (n=301) | REJECTED | below_safety_margin(15425<50548), p_lower_below_threshold(0.06<0.75) |
| 55143643 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025556 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0081 €) | — | 1.64 | 0.203 (n=1237) | REJECTED | below_safety_margin(4185936773466<5111264866502), stale_data(4666ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55143643 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 53.713136 USDC | 0.015201 USDC | 0.000000 USDC | 0.006437 USDC | 0.008764 USDC (0.0081 €) | — | 1.63 | 0.203 (n=1237) | REJECTED | below_safety_margin(8764<10742), stale_data(4672ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55143643 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025002 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0076 €) | — | 1.56 | 0.203 (n=1237) | REJECTED | below_safety_margin(3912701353279<5000492184419), stale_data(4685ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55141691 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.094433 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0075 €) | — | 0.41 | 0.059 (n=301) | REJECTED | below_safety_margin(3891486353181<18886518016087), p_lower_below_threshold(0.06<0.75) |
| 55141692 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.094433 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0075 €) | — | 0.41 | 0.059 (n=301) | REJECTED | below_safety_margin(3891486353181<18886518016087), p_lower_below_threshold(0.06<0.75) |
| 55143643 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 52.371911 USDC | 0.014625 USDC | 0.000000 USDC | 0.006437 USDC | 0.008188 USDC (0.0075 €) | — | 1.56 | 0.203 (n=1237) | REJECTED | below_safety_margin(8188<10474), stale_data(4691ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55141691 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 197.033765 USDC | 0.013224 USDC | 0.000000 USDC | 0.005060 USDC | 0.008164 USDC (0.0075 €) | — | 0.41 | 0.059 (n=301) | REJECTED | below_safety_margin(8164<39406), p_lower_below_threshold(0.06<0.75) |
| 55141692 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 197.033765 USDC | 0.013224 USDC | 0.000000 USDC | 0.005060 USDC | 0.008164 USDC (0.0075 €) | — | 0.41 | 0.059 (n=301) | REJECTED | below_safety_margin(8164<39406), p_lower_below_threshold(0.06<0.75) |
| 55143643 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000534 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0055 €) | — | 1.50 | 0.203 (n=1237) | REJECTED | below_safety_margin(8<10), stale_data(4717ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55143644 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000534 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0055 €) | — | 1.50 | 0.203 (n=1237) | REJECTED | below_safety_margin(8<10), p_lower_below_threshold(0.20<0.75) |
| 55143644 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.023257 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0054 €) | — | 1.21 | 0.203 (n=1237) | REJECTED | below_safety_margin(2802698319313<4651302258843), p_lower_below_threshold(0.20<0.75) |
| 55141426 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.036577 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(2689045639212<7315474365551), reliability_not_demonstrated |
| 55141427 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.036577 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(2689045639212<7315474365551), reliability_not_demonstrated |
| 55141426 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 76.357676 USDC | 0.009732 USDC | 0.000000 USDC | 0.004090 USDC | 0.005642 USDC (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(5642<15271), reliability_not_demonstrated |
| 55141427 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 76.357676 USDC | 0.009732 USDC | 0.000000 USDC | 0.004090 USDC | 0.005642 USDC (0.0052 €) | — | 0.74 | — (n=0) | REJECTED | below_safety_margin(5642<15271), reliability_not_demonstrated |
| 55143643 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.026088 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0050 €) | — | 0.99 | 0.203 (n=1237) | REJECTED | below_safety_margin(2579241528806<5217626127973), stale_data(4710ms>4000.0), p_lower_below_threshold(0.20<0.75) |
| 55144059 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.054590 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0040 €) | — | 0.38 | 0.048 (n=90) | REJECTED | below_safety_margin(2069990320517<10918028184127), stale_data(4908ms>4000.0), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 6740 ; taux observé 0.177 ; borne inférieure crédible (0.9) 0.171 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 17.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
