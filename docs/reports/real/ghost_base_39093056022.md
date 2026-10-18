# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T03:28:24+00:00 ; durée 6.09 min ; blocs 52752192 → 52752377 (183 vus)

## Connexion
- Requêtes RPC : 2347 ; erreurs : 0 ; latence p50/p95 : 267.2/1,366.1 ms
- Rafraîchissements d'état : 183 ; âge des données au dernier bloc : 3.07 s ; changements de frais LP observés (pools à frais dynamiques) : 255
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 603 ; cycles déclenchés par événement : 32 ; avance médiane sur le rafraîchissement multicall : 666 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,415.85 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21108 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2415.845921, 'AERO': 0.842347, 'cbBTC': 81764.569365}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,239,297 | 2,415.845923 | 52752378 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,754,634 | 1.187554 | 52752378 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,207,273 | 0.029569 | 52752378 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,969,105 | 0.029528 | 52752378 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,832,621 | 107.487551 | 52752378 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,463,443 | 0.029512 | 52752378 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,768,960 | 0.000012 | 52752378 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,062,428 | 2,417.277383 | 52752378 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,854,886 | 0.000012 | 52752378 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 7,680,042 | 0.000012 | 52752378 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,514,982 | 2,417.954831 | 52752378 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,147,725 | 0.001658 | 52752378 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,493,161 | 2,416.515491 | 52752378 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,344,258 | 0.029574 | 52752378 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,246,180 | 1.000855 | 52752378 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,152,362 | 0.025619 | 52752378 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/USDT | 409 | 5,100,261 | 2,420.667745 | 52752378 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,828,950 | 0.802399 | 52752378 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,641,495 | 0.000273 | 52752378 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,436,470 | 0.998808 | 52752378 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,414,594 | 2,418.198702 | 52752378 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,109,744 | 32,774.227976 | 52752378 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,978,320 | 1.184583 | 52752378 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,375,547 | 2,850.606683 | 52752378 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,916,191 | 1.141804 | 52752378 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,840,406 | 0.000012 | 52752378 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,805,926 | 0.000010 | 52752378 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,560,284 | 107.522685 | 52752378 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,506,800 | 407.102079 | 52752378 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,242,140 | 1,178,528.054669 | 52752378 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52752378 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,025,824 | 1.385318 | 52752378 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,015,610 | 1.123208 | 52752378 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,914,191 | 1,008.075958 | 52752378 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,885,218 | 15.839935 | 52752378 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,873,592 | 0.000000 | 52752378 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,808,933 | 0.021524 | 52752378 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,598 | 0.000012 | 52752378 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,725,900 | 0.017916 | 52752378 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,673,222 | 2.306764 | 52752378 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,645,062 | 13,771.585693 | 52752378 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,571,384 | 0.916398 | 52752378 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,521,425 | 1.105497 | 52752378 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,519,941 | 2,872.162127 | 52752378 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,463,290 | 2,870.596436 | 52752378 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,614 | 0.825990 | 52752378 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,335,695 | 0.000000 | 52752378 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,714 | 0.435907 | 52752378 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,311,910 | 0.004709 | 52752378 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,866 | 0.000271 | 52752378 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,257,050 | 0.029513 | 52752378 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,249,073 | 62.282694 | 52752378 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,247,118 | 23.317695 | 52752378 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,195,606 | 35,685,659.425166 | 52752378 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,194,294 | 1.105816 | 52752378 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,187,325 | 2,417.251561 | 52752378 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,184,336 | 1.131541 | 52752378 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/WELL | 10000 | 1,167,112 | 1,161,915.898617 | 52752378 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,156,091 | 0.885658 | 52752378 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,141,958 | 514,765.248826 | 52752378 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |

## Recherche d'opportunités
- Cycles : 214 ; routes examinées : 4517112 ; candidats optimisés : 24730 ; net attendu > 0 : 0 ; dernier cycle 443.2 ms
- Rejets (moteur) : {'spread_below_threshold': 4454886, 'liquidity_below_min': 37282, 'negative_expected_net': 24730, 'borrow_bound_too_small': 214}
- Enregistrements de la session : 24730 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 24730} ; motifs de rejet : {'negative_expected_net': 24730}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52752195 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752196 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752197 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752197 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752198 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752198 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752199 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752199 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752200 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |
| 52752200 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 4.027796 USDC | 0.001632 USDC | 0.000000 USDC | 0.005091 USDC | -0.0032 | -8.59 |

## Fiabilité et décision
- Observations ghost : 846 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.116 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
