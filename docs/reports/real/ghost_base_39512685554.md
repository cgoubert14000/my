# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T23:56:42+00:00 ; durée 45.73 min ; blocs 52874252 → 52875626 (1356 vus)

## Connexion
- Requêtes RPC : 18678 ; erreurs : 75 ; latence p50/p95 : 246.9/1,030.1 ms
- Rafraîchissements d'état : 1357 ; âge des données au dernier bloc : 1.96 s ; changements de frais LP observés (pools à frais dynamiques) : 2324
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 14807 ; cycles déclenchés par événement : 1488 ; avance médiane sur le rafraîchissement multicall : 462 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,451.14 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 581 pools, 328 jetons, 22996 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 395, par paires 0), mesurés 583, sous le plancher de 10000.0 $ : 2 → gardés 581 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2453.717243, 'AERO': 0.88311, 'cbBTC': 82924.161646}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,632,413 | 2,451.142547 | 52875626 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,354,357 | 1.133344 | 52875626 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,965,030 | 96.041489 | 52875626 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,499,836 | 0.029508 | 52875626 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,573,211 | 0.029573 | 52875626 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 10,560,581 | 0.029567 | 52875626 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,939,956 | 0.000012 | 52875626 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 8,745,359 | 0.000012 | 52875626 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,615,907 | 2,448.263089 | 52875626 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,389,460 | 2,451.507782 | 52875626 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 8,203,075 | 0.000012 | 52875626 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,136,422 | 2,447.566577 | 52875626 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,305,925 | 0.001675 | 52875626 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,448,622 | 0.029496 | 52875626 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,323,581 | 0.024443 | 52875626 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,245,966 | 1.130606 | 52875626 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,732,778 | 0.000275 | 52875626 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,724,708 | 0.802394 | 52875626 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,453,212 | 2,447.250711 | 52875626 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,409,220 | 0.998741 | 52875626 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 406 | 4,204,273 | 2,451.133469 | 52875626 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,052,436 | 34,699.918771 | 52875626 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,422,662 | 2,778.082922 | 52875626 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,877,401 | 0.000012 | 52875626 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,862,150 | 1,018.783965 | 52875626 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,772,111 | 399.904998 | 52875626 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,747,500 | 96.019031 | 52875626 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,539,230 | 1.142084 | 52875626 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,436,478 | 0.000011 | 52875626 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,251,802 | 1,202,829.379446 | 52875626 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,907 | 1.238864 | 52875626 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,920 | 1.383226 | 52875626 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,983,400 | 15.813204 | 52875626 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,943,970 | 0.000000 | 52875626 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,918,669 | 1.105639 | 52875626 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,817,964 | 0.019384 | 52875626 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,803,324 | 13,571.190645 | 52875626 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,121 | 0.000012 | 52875626 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | fBOMB/USDC | 10000 | 1,707,363 | 0.021275 | 52875626 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | WETH/AERO | 3000 | 1,692,724 | 2,774.939830 | 52875626 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,691,694 | 2.310992 | 52875626 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,571,732 | 0.916062 | 52875626 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52875626 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,390,889 | 1.122941 | 52875626 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,353,652 | 0.004804 | 52875626 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,349,079 | 0.000000 | 52875626 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,326,981 | 0.000277 | 52875626 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,312,957 | 0.029584 | 52875626 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,271,223 | 2,448.287222 | 52875626 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,879 | 63.619562 | 52875626 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,224,676 | 68,676.475238 | 52875626 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,224,503 | 23.060385 | 52875626 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,224,226 | 34,988,111.001513 | 52875626 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,057 | 0.436825 | 52875626 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,172,308 | 493,960.319653 | 52875626 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,169,731 | 1,190,557.804945 | 52875626 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,168,797 | 0.886332 | 52875626 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,157,440 | 47.033599 | 52875626 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,155,252 | 1.106158 | 52875626 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,106,668 | 20,658,103.806189 | 52875626 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 2844 ; routes examinées : 65400624 ; candidats optimisés : 213954 ; net attendu > 0 : 145 ; dernier cycle 312.0 ms
- Rejets (moteur) : {'spread_below_threshold': 64775588, 'liquidity_below_min': 408073, 'negative_expected_net': 213809, 'borrow_bound_too_small': 2842, 'cycle_budget_exhausted': 167}
- Enregistrements de la session : 213954 ; net attendu > 0 : 145 ; simulés (eth_call de la vraie tx) : 5 (ok 0, échec 5) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 213954} ; motifs de rejet : {'below_safety_margin': 132, 'negative_expected_net': 213809, 'p_lower_below_threshold': 135, 'reliability_not_demonstrated': 10, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52875037 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.066092 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (1.0071 €) | — | 1.99 | 0.121 (n=191) | REJECTED | below_safety_margin(1318<1321), p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 2.265299 WETH | 0.000450 WETH | 0.000000 WETH | 0.000004 WETH | 0.000446 WETH (1.0070 €) | — | 1.97 | 0.121 (n=191) | REJECTED | below_safety_margin(446424932766654<453059794501778), p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 5,542.392478 USDC | 1.100381 USDC | 0.000000 USDC | 0.008858 USDC | 1.091523 USDC (1.0042 €) | — | 1.97 | 0.121 (n=191) | REJECTED | below_safety_margin(1091523<1108478), p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.856803 WETH | 0.000405 WETH | 0.000000 WETH | 0.000003 WETH | 0.000402 WETH (0.9060 €) | — | 2.16 | 0.121 (n=191) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52875037 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.054128 cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000012 cbBTC (0.9055 €) | — | 2.19 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 4,543.083362 USDC | 0.990633 USDC | 0.000000 USDC | 0.008486 USDC | 0.982147 USDC (0.9036 €) | — | 2.16 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.044885 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7427 €) | — | 2.17 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.508351 WETH | 0.000333 WETH | 0.000000 WETH | 0.000003 WETH | 0.000329 WETH (0.7426 €) | — | 2.18 | 0.121 (n=191) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 3,746.366650 USDC | 0.813956 USDC | 0.000000 USDC | 0.008486 USDC | 0.805470 USDC (0.7410 €) | — | 2.15 | 0.121 (n=191) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.097300 WETH | 0.000264 WETH | 0.000000 WETH | 0.000003 WETH | 0.000261 WETH (0.5886 €) | — | 2.38 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52875037 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.031367 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5884 €) | — | 2.45 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 2,707.137311 USDC | 0.646054 USDC | 0.000000 USDC | 0.008113 USDC | 0.637941 USDC (0.5869 €) | — | 2.36 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52875037 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.670930 WETH | 0.000198 WETH | 0.000000 WETH | 0.000003 WETH | 0.000194 WETH (0.4380 €) | — | 1.16 | 0.121 (n=191) | REJECTED | below_safety_margin(194195621492476<334186067878125), p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 4,079.285042 USDC | 0.482887 USDC | 0.000000 USDC | 0.008113 USDC | 0.474774 USDC (0.4368 €) | — | 1.16 | 0.121 (n=191) | REJECTED | below_safety_margin(474774<815857), p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.444605 WETH | 0.000125 WETH | 0.000000 WETH | 0.000002 WETH | 0.000122 WETH (0.2759 €) | — | 2.75 | 0.014 (n=57) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,085.819408 USDC | 0.304823 USDC | 0.000000 USDC | 0.005878 USDC | 0.298945 USDC (0.2750 €) | — | 2.75 | 0.014 (n=57) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52875037 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.921702 WETH | 0.000092 WETH | 0.000000 WETH | 0.000002 WETH | 0.000089 WETH (0.2012 €) | — | 0.97 | 0.014 (n=57) | REJECTED | below_safety_margin(89187589977729<184340340273100), p_lower_below_threshold(0.01<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,259.304783 USDC | 0.223902 USDC | 0.000000 USDC | 0.005878 USDC | 0.218024 USDC (0.2006 €) | — | 0.97 | 0.014 (n=57) | REJECTED | below_safety_margin(218024<451860), p_lower_below_threshold(0.01<0.75) |
| 52875037 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.636398 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0958 €) | — | 0.67 | 0.121 (n=191) | REJECTED | below_safety_margin(42463054570428<127279622859676), p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 1,555.343181 USDC | 0.111526 USDC | 0.000000 USDC | 0.007741 USDC | 0.103785 USDC (0.0955 €) | — | 0.67 | 0.121 (n=191) | REJECTED | below_safety_margin(103785<311068), p_lower_below_threshold(0.12<0.75) |
| 52875037 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.622705 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0670 €) | — | 0.48 | 0.121 (n=191) | REJECTED | below_safety_margin(29710569958884<124541009898319), p_lower_below_threshold(0.12<0.75) |
| 52875037 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 1,518.669318 USDC | 0.080721 USDC | 0.000000 USDC | 0.008113 USDC | 0.072608 USDC (0.0668 €) | — | 0.48 | 0.121 (n=191) | REJECTED | below_safety_margin(72608<303733), p_lower_below_threshold(0.12<0.75) |
| 52874740 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 56.113426 USDC | 0.068550 USDC | 0.000000 USDC | 0.005508 USDC | 0.063042 USDC (0.0580 €) | — | 11.23 | 0.000 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52875037 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004490 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0573 €) | — | 1.67 | 0.002 (n=5) | REJECTED | below_safety_margin(75<89), reliability_not_demonstrated |
| 52875037 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.163085 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0570 €) | — | 1.55 | 0.002 (n=5) | REJECTED | below_safety_margin(25262949657623<32616986109945), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1572 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
