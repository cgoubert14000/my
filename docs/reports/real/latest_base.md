# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T06:08:21+00:00 ; durée 86.14 min ; blocs 52711390 → 52713974 (2582 vus)

## Connexion
- Requêtes RPC : 33625 ; erreurs : 50 ; latence p50/p95 : 183.5/708.1 ms
- Rafraîchissements d'état : 2583 ; âge des données au dernier bloc : 2.07 s ; changements de frais LP observés (pools à frais dynamiques) : 2571
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16338 ; cycles déclenchés par événement : 1552 ; avance médiane sur le rafraîchissement multicall : 381 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,421.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 329 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 393, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2421.248535, 'AERO': 0.878353, 'cbBTC': 81453.278136}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,170,606 | 2,421.247451 | 52713974 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,955,830 | 1.131246 | 52713974 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,239,340 | 0.029778 | 52713974 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,982,859 | 105.364723 | 52713974 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,727,380 | 0.029719 | 52713974 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,413,972 | 0.029707 | 52713974 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,752,184 | 0.000012 | 52713974 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 9,327,855 | 0.000012 | 52713974 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,109,654 | 2,426.917083 | 52713974 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,983,046 | 2,425.731424 | 52713974 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,840,065 | 0.000012 | 52713974 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,157,042 | 0.001678 | 52713974 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,468,628 | 1.138430 | 52713974 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,413,648 | 2,428.529178 | 52713974 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,362,803 | 0.025281 | 52713974 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,337,346 | 0.029781 | 52713974 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,257,910 | 1.000855 | 52713974 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,839,609 | 0.802398 | 52713974 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,684,269 | 0.000276 | 52713974 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,503,597 | 2,425.793003 | 52713974 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,415,228 | 0.998803 | 52713974 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,045,261 | 33,978.858169 | 52713974 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,694,052 | 2,429.228228 | 52713974 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,468,649 | 2,759.708535 | 52713974 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,917,579 | 1.141834 | 52713974 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,849,873 | 0.000012 | 52713974 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,640,839 | 1,015.791077 | 52713974 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,592,370 | 105.398857 | 52713974 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,526,656 | 0.000011 | 52713974 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,394,881 | 399.356075 | 52713974 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,266,257 | 1,158,742.078326 | 52713974 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,152,266 | 1.123823 | 52713974 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,407 | 1.197840 | 52713974 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,023,074 | 15.589863 | 52713974 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,001,549 | 1.414312 | 52713974 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome | fBOMB/USDC | 10000 | 1,825,234 | 0.022219 | 52713974 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,814,063 | 0.000000 | 52713974 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,775,434 | 0.000012 | 52713974 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,762,823 | 0.018540 | 52713974 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,738,681 | 13,425.083381 | 52713974 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,924 | 2.306475 | 52713974 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,547,510 | 0.916550 | 52713974 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,545,107 | 2,738.421043 | 52713974 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,521,850 | 2,742.762347 | 52713974 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,516,767 | 1.105495 | 52713974 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52713974 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,358,868 | 0.000000 | 52713974 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,325,877 | 0.004756 | 52713974 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,933 | 0.435379 | 52713974 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,312,800 | 0.000278 | 52713974 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,256,730 | 23.260550 | 52713974 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52713974 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,239,395 | 1.131518 | 52713974 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,994 | 34,801,915.098400 | 52713974 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,204,704 | 0.029700 | 52713974 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,202,810 | 1.105712 | 52713974 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,189,846 | 2,425.711708 | 52713974 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,182,654 | 1,136,628.171484 | 52713974 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,154,176 | 497,468.150224 | 52713974 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,126,873 | 13.851974 | 52713974 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 4134 ; routes examinées : 86855340 ; candidats optimisés : 713931 ; net attendu > 0 : 14 ; dernier cycle 245.4 ms
- Rejets (moteur) : {'spread_below_threshold': 85524152, 'negative_expected_net': 713917, 'liquidity_below_min': 611410, 'borrow_bound_too_small': 4132, 'pool_quarantined': 1366, 'cycle_budget_exhausted': 349}
- Enregistrements de la session : 713931 ; net attendu > 0 : 14 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 713931} ; motifs de rejet : {'below_safety_margin': 8, 'negative_expected_net': 713917, 'p_lower_below_threshold': 2, 'reliability_not_demonstrated': 12, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52713483 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 88.741675 USDC | 0.113607 USDC | 0.000000 USDC | 0.005439 USDC | 0.108168 USDC (0.0995 €) | — | 12.19 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52713372 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 53.655747 USDC | 0.041553 USDC | 0.000000 USDC | 0.005439 USDC | 0.036114 USDC (0.0332 €) | — | 6.73 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52713109 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 41.715991 USDC | 0.024780 USDC | 0.000000 USDC | 0.005439 USDC | 0.019341 USDC (0.0178 €) | — | 4.64 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52713608 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 37.839923 USDC | 0.021019 USDC | 0.000000 USDC | 0.005438 USDC | 0.015581 USDC (0.0143 €) | — | 4.12 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52712850 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001091 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0127 €) | — | 1.56 | 0.114 (n=74) | REJECTED | below_safety_margin(17<21), p_lower_below_threshold(0.11<0.75) |
| 52712850 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 91.213868 USDC | 0.020481 USDC | 0.000000 USDC | 0.007279 USDC | 0.013202 USDC (0.0121 €) | — | 1.45 | 0.114 (n=74) | REJECTED | below_safety_margin(13202<18242), p_lower_below_threshold(0.11<0.75) |
| 52712846 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 22.549920 USDC | 0.011502 USDC | 0.000000 USDC | 0.005440 USDC | 0.006062 USDC (0.0056 €) | — | 2.69 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52713484 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.481705 USDC | 0.011052 USDC | 0.000000 USDC | 0.005439 USDC | 0.005613 USDC (0.0052 €) | — | 2.04 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52713544 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 25.865181 USDC | 0.009832 USDC | 0.000000 USDC | 0.005438 USDC | 0.004394 USDC (0.0040 €) | — | 1.70 | 0.001 (n=14) | REJECTED | below_safety_margin(4394<5173), reliability_not_demonstrated |
| 52713544 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 25.865181 USDC | 0.009832 USDC | 0.000000 USDC | 0.005438 USDC | 0.004394 USDC (0.0040 €) | — | 1.70 | 0.001 (n=14) | REJECTED | below_safety_margin(4394<5173), reliability_not_demonstrated |
| 52712820 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.605241 USDC | 0.005500 USDC | 0.000000 USDC | 0.005440 USDC | 0.000060 USDC (0.0001 €) | — | 0.04 | 0.001 (n=12) | REJECTED | below_safety_margin(60<3121), reliability_not_demonstrated |
| 52712821 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.605241 USDC | 0.005500 USDC | 0.000000 USDC | 0.005440 USDC | 0.000060 USDC (0.0001 €) | — | 0.04 | 0.001 (n=12) | REJECTED | below_safety_margin(60<3121), reliability_not_demonstrated |
| 52712821 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.605241 USDC | 0.005500 USDC | 0.000000 USDC | 0.005449 USDC | 0.000051 USDC (0.0000 €) | — | 0.03 | 0.001 (n=12) | REJECTED | below_safety_margin(51<3121), reliability_not_demonstrated |
| 52712822 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.605241 USDC | 0.005500 USDC | 0.000000 USDC | 0.005449 USDC | 0.000051 USDC (0.0000 €) | — | 0.03 | 0.001 (n=12) | REJECTED | below_safety_margin(51<3121), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 670 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.114 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
