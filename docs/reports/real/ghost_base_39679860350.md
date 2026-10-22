# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-22T03:07:13+00:00 ; durée 328.31 min ; blocs 52914691 → 52924536 (9184 vus)

## Connexion
- Requêtes RPC : 112439 ; erreurs : 35 ; latence p50/p95 : 98.1/1,953.4 ms
- Rafraîchissements d'état : 9185 ; âge des données au dernier bloc : 0.63 s ; changements de frais LP observés (pools à frais dynamiques) : 19609
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 20975 ; cycles déclenchés par événement : 1412 ; avance médiane sur le rafraîchissement multicall : 780 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,442.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 326 jetons, 22742 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 158, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 2 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2492.485305, 'AERO': 0.830593, 'cbBTC': 84747.685068}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,657,638 | 2,442.747336 | 52924536 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 25,930,185 | 1.214616 | 52924536 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 16,712,276 | 89.134655 | 52924536 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,405,479 | 0.029452 | 52924536 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,423,653 | 0.029404 | 52924536 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 9,803,780 | 0.029394 | 52924536 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,477,199 | 0.000012 | 52924536 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,753,791 | 2,441.119511 | 52924536 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 7,399,216 | 2,442.934569 | 52924536 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,270,254 | 0.001664 | 52924536 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,138,708 | 0.000012 | 52924536 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 6,627,045 | 2,441.473045 | 52924536 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 5,997,483 | 0.000012 | 52924536 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,541,800 | 0.029459 | 52924536 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,605,116 | 2,441.434504 | 52924536 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,364,417 | 0.999956 | 52924536 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,085,874 | 0.000278 | 52924536 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,038,185 | 34,705.053705 | 52924536 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 400 | 2,919,131 | 2,444.436364 | 52924536 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,826,853 | 89.117698 | 52924536 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/AERO | 10000 | 2,515,328 | 2,976.871737 | 52924536 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,423,243 | 393.401047 | 52924536 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,260,939 | 0.000012 | 52924536 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,250,174 | 1,195,585.171955 | 52924536 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,092,885 | 0.000012 | 52924536 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,937,040 | 0.000000 | 52924536 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,798,099 | 0.018567 | 52924536 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,765,550 | 1.105712 | 52924536 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,703,434 | 1.495412 | 52924536 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | fBOMB/AERO | 10000 | 1,683,067 | 0.023325 | 52924536 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| uniswap_v3 | WETH/AERO | 3000 | 1,659,505 | 2,963.383283 | 52924536 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,626,524 | 2.331563 | 52924536 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/USDC | 3000 | 1,545,293 | 2,443.090655 | 52924536 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,500,104 | 1.407572 | 52924536 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,766 | 0.826427 | 52924536 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,441,399 | 13,373.864560 | 52924536 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,382,073 | 0.000000 | 52924536 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/wstETH | 90 | 1,381,392 | 0.802236 | 52924536 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,372,378 | 0.004868 | 52924536 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,362,999 | 16.156297 | 52924536 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,329,393 | 0.000277 | 52924536 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,292,573 | 2,441.081496 | 52924536 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,288,906 | 0.000010 | 52924536 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/SEND | 3000 | 1,231,877 | 64.033499 | 52924536 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,218,334 | 1,083,379.230217 | 52924536 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,214,648 | 35,458,267.717002 | 52924536 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,191,243 | 44.402553 | 52924536 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,178,459 | 492,403.031955 | 52924536 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,174,639 | 23.134704 | 52924536 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | fBOMB/USDC | 10000 | 1,153,955 | 0.019354 | 52924536 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/EDEL | 7000 | 1,153,250 | 71,962.441998 | 52924536 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,088,136 | 21,166,261.097057 | 52924536 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/cbBTC | 3000 | 1,075,161 | 0.029409 | 52924536 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | EURC/USDC | 82 | 1,074,291 | 1.125181 | 52924536 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,070,080 | 0.915940 | 52924536 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,054,467 | 16.411788 | 52924536 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,029,707 | 1.208446 | 52924536 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/VVV | 3000 | 1,001,163 | 0.036488 | 52924536 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 973,269 | 1,058.025275 | 52924536 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/USDT | 8 | 951,478 | 1.001347 | 52924536 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 10596 ; routes examinées : 240974232 ; candidats optimisés : 1534984 ; net attendu > 0 : 321 ; dernier cycle 218.0 ms
- Rejets (moteur) : {'spread_below_threshold': 236491637, 'liquidity_below_min': 2424159, 'negative_expected_net': 1534663, 'pool_quarantined': 506172, 'borrow_bound_too_small': 10591, 'cycle_budget_exhausted': 6689}
- Enregistrements de la session : 1534984 ; net attendu > 0 : 321 ; simulés (eth_call de la vraie tx) : 87 (ok 11, échec 76) ; étiquettes ghost N+1 : 0/48 positives
- Décisions : {'REJECTED': 1534984} ; motifs de rejet : {'below_safety_margin': 197, 'negative_expected_net': 1534663, 'p_lower_below_threshold': 271, 'price_impact': 102, 'reliability_not_demonstrated': 50, 'simulation_failed': 76, 'stale_data': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52915931 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 159.556387 USDC | 4.823624 USDC | 0.000000 USDC | 0.005306 USDC | 4.818318 USDC (4.4329 €) | — | 301.98 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52921034 | WETH→[aerodrome_slipstream]→VVV→[aerodrome]→WETH | 0.528123 WETH | 0.000571 WETH | 0.000000 WETH | 0.000002 WETH | 0.000569 WETH (1.2944 €) | 0.000569 WETH | 10.78 | 0.001 (n=11) | REJECTED | reliability_not_demonstrated |
| 52915935 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 98.761994 USDC | 0.721808 USDC | 0.000000 USDC | 0.005311 USDC | 0.716497 USDC (0.6592 €) | — | 72.55 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.113620 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1682 €) | 0.000074 WETH | 6.51 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 280.778322 USDC | 0.190310 USDC | 0.000000 USDC | 0.007512 USDC | 0.182798 USDC (0.1682 €) | — | 6.51 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 247.609122 USDC | 0.150127 USDC | 0.000000 USDC | 0.007512 USDC | 0.142615 USDC (0.1312 €) | — | 5.76 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.100298 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1312 €) | 0.000058 WETH | 5.75 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 232.816856 USDC | 0.139821 USDC | 0.000000 USDC | 0.007512 USDC | 0.132309 USDC (0.1217 €) | — | 5.68 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.094320 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1217 €) | — | 5.67 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915567 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 31.983662 USDC | 0.077174 USDC | 0.000000 USDC | 0.005263 USDC | 0.071911 USDC (0.0662 €) | — | 22.48 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52915729 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 31.332892 USDC | 0.075372 USDC | 0.000000 USDC | 0.005264 USDC | 0.070108 USDC (0.0645 €) | — | 22.38 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52915437 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040504 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0581 €) | — | 6.25 | 0.109 (n=163) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 100.466132 USDC | 0.070583 USDC | 0.000000 USDC | 0.007495 USDC | 0.063088 USDC (0.0580 €) | — | 6.28 | 0.109 (n=163) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 121.326469 USDC | 0.070977 USDC | 0.000000 USDC | 0.007891 USDC | 0.063086 USDC (0.0580 €) | — | 5.20 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.049227 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0580 €) | — | 5.18 | 0.108 (n=165) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915437 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040412 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0577 €) | — | 6.23 | 0.133 (n=89) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 100.336417 USDC | 0.070164 USDC | 0.000000 USDC | 0.007495 USDC | 0.062669 USDC (0.0577 €) | — | 6.25 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040023 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0571 €) | — | 6.23 | 0.109 (n=163) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 99.595363 USDC | 0.069558 USDC | 0.000000 USDC | 0.007495 USDC | 0.062063 USDC (0.0571 €) | — | 6.23 | 0.109 (n=163) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915437 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.039020 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0547 €) | — | 6.11 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 96.885708 USDC | 0.066862 USDC | 0.000000 USDC | 0.007495 USDC | 0.059367 USDC (0.0546 €) | — | 6.13 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.033505 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0526 €) | — | 6.85 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 83.007657 USDC | 0.064632 USDC | 0.000000 USDC | 0.007495 USDC | 0.057137 USDC (0.0526 €) | — | 6.88 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52921034 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 135.379872 USDC | 0.043973 USDC | 0.000000 USDC | 0.007512 USDC | 0.036461 USDC (0.0335 €) | — | 2.69 | 0.114 (n=203) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52921034 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.054676 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0335 €) | — | 2.70 | 0.114 (n=203) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1798 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
