# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T14:50:00+00:00 ; durée 18.33 min ; blocs 52945073 → 52945624 (522 vus)

## Connexion
- Requêtes RPC : 6529 ; erreurs : 0 ; latence p50/p95 : 306.7/1,554.9 ms
- Rafraîchissements d'état : 522 ; âge des données au dernier bloc : 4.8 s ; changements de frais LP observés (pools à frais dynamiques) : 1828
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15269 ; cycles déclenchés par événement : 445 ; avance médiane sur le rafraîchissement multicall : 1,070 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,408.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 546 pools, 318 jetons, 19398 routes
- Par DEX : uniswap_v3 137, aerodrome 226, aerodrome_slipstream 137, pancakeswap_v3 30, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 198 (rejetés 2) → 603 jetons ; pools candidats 3827 (énumérés 366, par paires 0), mesurés 549, sous le plancher de 10000.0 $ : 3 → gardés 546 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2404.811718, 'AERO': 0.81356, 'cbBTC': 81633.413427}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,504,592 | 2,408.203195 | 52945625 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 18,537,248 | 1.229043 | 52945625 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,318,032 | 0.029455 | 52945625 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,560,095 | 92.794495 | 52945625 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,297,256 | 0.029434 | 52945625 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,427,811 | 0.000012 | 52945625 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,425,246 | 0.029448 | 52945625 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,745,541 | 2,408.486273 | 52945625 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,176,623 | 0.001669 | 52945625 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 6,815,865 | 0.000012 | 52945625 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 579 | 5,922,883 | 2,409.307777 | 52945625 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 5,516,431 | 0.000012 | 52945625 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,419,132 | 0.029464 | 52945625 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,511,917 | 2,409.396748 | 52945625 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/USDC | 3000 | 4,321,824 | 2,407.995821 | 52945625 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,299,276 | 1.000001 | 52945625 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,992,770 | 34,491.982027 | 52945625 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,766,117 | 0.000275 | 52945625 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,914,569 | 2,412.255231 | 52945625 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 3024 | 2,572,140 | 92.792084 | 52945625 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,370,070 | 2,960.672151 | 52945625 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,309,506 | 398.363485 | 52945625 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,219,442 | 0.000012 | 52945625 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,208,803 | 1,205,946.672315 | 52945625 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,062,383 | 0.000012 | 52945625 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,907,748 | 0.000000 | 52945625 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,797,036 | 0.018533 | 52945625 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,661,386 | 1.521320 | 52945625 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,639,152 | 2,960.688638 | 52945625 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,240 | 0.823520 | 52945625 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,414,529 | 13,511.648442 | 52945625 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,370,788 | 0.004940 | 52945625 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,326,163 | 2,408.518328 | 52945625 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/msETH (stable) | 500 | 1,311,664 | 2.371578 | 52945625 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,303,638 | 0.000274 | 52945625 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,281,102 | 0.000000 | 52945625 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,679 | 64.262670 | 52945625 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,201,115 | 35,180,238.587614 | 52945625 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,190,634 | 16.266116 | 52945625 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,186,447 | 1,094,249.323909 | 52945625 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,152,648 | 499,670.732841 | 52945625 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,146,560 | 47.875902 | 52945625 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,113,785 | 0.000010 | 52945625 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/EDEL | 7000 | 1,108,229 | 74,288.013839 | 52945625 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,099,496 | 1.105751 | 52945625 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,066,124 | 21,408,920.470197 | 52945625 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,035,898 | 17.213058 | 52945625 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/cbBTC | 3000 | 1,018,856 | 0.029436 | 52945625 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,015,200 | 23.041130 | 52945625 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | USDC/VVV | 3000 | 974,930 | 0.038528 | 52945625 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 963,442 | 1,058.672506 | 52945625 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 940,897 | 2,417.796200 | 52945625 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,424 | 0.000548 | 52945625 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | EURC/USDC | 70 | 901,523 | 1.119544 | 52945625 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/bsdETH | 100 | 897,025 | 0.916099 | 52945625 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4595 | 889,416 | 17.577605 | 52945625 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 878,165 | 2,407.969617 | 52945625 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 817,659 | 0.803225 | 52945625 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | fBOMB/USDC | 10000 | 809,094 | 0.018687 | 52945625 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 805,748 | 1.106135 | 52945625 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 966 ; routes examinées : 18738468 ; candidats optimisés : 119958 ; net attendu > 0 : 25 ; dernier cycle 730.5 ms
- Rejets (moteur) : {'spread_below_threshold': 18466635, 'liquidity_below_min': 150666, 'negative_expected_net': 119933, 'borrow_bound_too_small': 966, 'cycle_budget_exhausted': 243}
- Enregistrements de la session : 119958 ; net attendu > 0 : 25 ; simulés (eth_call de la vraie tx) : 1 (ok 1, échec 0) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 119958} ; motifs de rejet : {'below_safety_margin': 24, 'negative_expected_net': 119933, 'p_lower_below_threshold': 16, 'reliability_not_demonstrated': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52945116 | USDC→[aerodrome]→msUSD→[aerodrome_slipstream]→USDC | 158.467777 USDC | 0.135546 USDC | 0.000000 USDC | 0.005350 USDC | 0.130196 USDC (0.1198 €) | 0.130196 USDC | 8.22 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 52945355 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011478 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0864 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(115<229), reliability_not_demonstrated |
| 52945355 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.011478 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0864 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(115<229), reliability_not_demonstrated |
| 52945355 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.396421 WETH | 0.000042 WETH | 0.000000 WETH | 0.000004 WETH | 0.000039 WETH (0.0861 €) | — | 0.98 | 0.001 (n=6) | REJECTED | below_safety_margin(38902885680636<79284157046047), reliability_not_demonstrated |
| 52945355 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.396421 WETH | 0.000042 WETH | 0.000000 WETH | 0.000004 WETH | 0.000039 WETH (0.0861 €) | — | 0.98 | 0.001 (n=6) | REJECTED | below_safety_margin(38902885680636<79284157046047), reliability_not_demonstrated |
| 52945355 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 938.256390 USDC | 0.102083 USDC | 0.000000 USDC | 0.008621 USDC | 0.093462 USDC (0.0860 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(93462<187651), reliability_not_demonstrated |
| 52945355 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 938.256390 USDC | 0.102083 USDC | 0.000000 USDC | 0.008621 USDC | 0.093462 USDC (0.0860 €) | — | 1.00 | 0.001 (n=6) | REJECTED | below_safety_margin(93462<187651), reliability_not_demonstrated |
| 52945270 | WETH→[aerodrome]→msETH→[aerodrome_slipstream]→WETH | 0.076415 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0200 €) | — | 1.18 | 0.151 (n=10) | REJECTED | below_safety_margin(9018915115216<15283026652965), reliability_not_demonstrated |
| 52945270 | WETH→[aerodrome]→msETH→[aerodrome_slipstream]→WETH | 0.076415 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0200 €) | — | 1.18 | 0.151 (n=10) | REJECTED | below_safety_margin(9018915115216<15283026652965), reliability_not_demonstrated |
| 52945355 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 235.258076 USDC | 0.017125 USDC | 0.000000 USDC | 0.005645 USDC | 0.011480 USDC (0.0106 €) | — | 0.49 | 0.022 (n=64) | REJECTED | below_safety_margin(11480<47051), p_lower_below_threshold(0.02<0.75) |
| 52945355 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 235.258076 USDC | 0.017125 USDC | 0.000000 USDC | 0.005645 USDC | 0.011480 USDC (0.0106 €) | — | 0.49 | 0.022 (n=64) | REJECTED | below_safety_margin(11480<47051), p_lower_below_threshold(0.02<0.75) |
| 52945355 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.098584 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0106 €) | — | 0.48 | 0.022 (n=64) | REJECTED | below_safety_margin(4771919026802<19716745043261), p_lower_below_threshold(0.02<0.75) |
| 52945355 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.098584 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0106 €) | — | 0.48 | 0.022 (n=64) | REJECTED | below_safety_margin(4771919026802<19716745043261), p_lower_below_threshold(0.02<0.75) |
| 52945119 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 481.343784 USDC | 0.012505 USDC | 0.000000 USDC | 0.006062 USDC | 0.006443 USDC (0.0059 €) | — | 0.13 | 0.022 (n=64) | REJECTED | below_safety_margin(6443<96268), p_lower_below_threshold(0.02<0.75) |
| 52945120 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 481.343784 USDC | 0.012505 USDC | 0.000000 USDC | 0.006062 USDC | 0.006443 USDC (0.0059 €) | — | 0.13 | 0.022 (n=64) | REJECTED | below_safety_margin(6443<96268), p_lower_below_threshold(0.02<0.75) |
| 52945119 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.201090 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0059 €) | — | 0.13 | 0.022 (n=64) | REJECTED | below_safety_margin(2677123097415<40218005266263), p_lower_below_threshold(0.02<0.75) |
| 52945120 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.201090 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0059 €) | — | 0.13 | 0.022 (n=64) | REJECTED | below_safety_margin(2677123097415<40218005266263), p_lower_below_threshold(0.02<0.75) |
| 52945355 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 429.249190 USDC | 0.012261 USDC | 0.000000 USDC | 0.006010 USDC | 0.006251 USDC (0.0058 €) | — | 0.15 | 0.022 (n=64) | REJECTED | below_safety_margin(6251<85849), p_lower_below_threshold(0.02<0.75) |
| 52945355 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 429.249190 USDC | 0.012261 USDC | 0.000000 USDC | 0.006010 USDC | 0.006251 USDC (0.0058 €) | — | 0.15 | 0.022 (n=64) | REJECTED | below_safety_margin(6251<85849), p_lower_below_threshold(0.02<0.75) |
| 52945355 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004837 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0053 €) | — | 0.14 | 0.022 (n=64) | REJECTED | below_safety_margin(7<96), p_lower_below_threshold(0.02<0.75) |
| 52945355 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.004837 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0053 €) | — | 0.14 | 0.022 (n=64) | REJECTED | below_safety_margin(7<96), p_lower_below_threshold(0.02<0.75) |
| 52945355 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 70.954962 USDC | 0.009104 USDC | 0.000000 USDC | 0.007527 USDC | 0.001577 USDC (0.0015 €) | — | 0.22 | 0.243 (n=108) | REJECTED | below_safety_margin(1577<14190), p_lower_below_threshold(0.24<0.75) |
| 52945355 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 70.954962 USDC | 0.009104 USDC | 0.000000 USDC | 0.007527 USDC | 0.001577 USDC (0.0015 €) | — | 0.22 | 0.243 (n=108) | REJECTED | below_safety_margin(1577<14190), p_lower_below_threshold(0.24<0.75) |
| 52945355 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.029873 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.22 | 0.243 (n=108) | REJECTED | below_safety_margin(654827961206<5974652921261), p_lower_below_threshold(0.24<0.75) |
| 52945355 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.029873 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0014 €) | — | 0.22 | 0.243 (n=108) | REJECTED | below_safety_margin(654827961206<5974652921261), p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 1886 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
