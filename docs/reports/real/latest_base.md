# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T23:55:49+00:00 ; durée 49.23 min ; blocs 52701320 → 52702799 (1472 vus)

## Connexion
- Requêtes RPC : 18670 ; erreurs : 0 ; latence p50/p95 : 195.7/1,363.8 ms
- Rafraîchissements d'état : 1472 ; âge des données au dernier bloc : 2.34 s ; changements de frais LP observés (pools à frais dynamiques) : 1419
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2483 ; cycles déclenchés par événement : 238 ; avance médiane sur le rafraîchissement multicall : 558 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,418.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2418.060843, 'AERO': 0.878781, 'cbBTC': 81702.724694}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,394,320 | 2,418.061146 | 52702799 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,848,007 | 1.138012 | 52702799 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,259,726 | 0.029690 | 52702799 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,921,125 | 105.902616 | 52702799 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,459,354 | 0.029630 | 52702799 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,417,239 | 0.029623 | 52702799 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,784,453 | 0.000012 | 52702799 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,083,780 | 2,420.298969 | 52702799 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 9,036,069 | 0.000012 | 52702799 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,226,595 | 2,419.931597 | 52702799 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,864,007 | 0.000012 | 52702799 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,153,260 | 0.001670 | 52702799 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,410,109 | 2,419.540443 | 52702799 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,345,468 | 0.025295 | 52702799 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,334,181 | 0.029688 | 52702799 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,166,978 | 1.000855 | 52702799 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,851,880 | 1.137994 | 52702799 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,833,240 | 0.802398 | 52702799 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,678,683 | 0.000276 | 52702799 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,440,871 | 2,419.955386 | 52702799 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,324,248 | 0.998900 | 52702799 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 400 | 4,064,129 | 2,424.012442 | 52702799 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,033,423 | 34,088.702710 | 52702799 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,458,355 | 2,755.775778 | 52702799 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,997,323 | 1.141834 | 52702799 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,852,794 | 0.000012 | 52702799 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,580,947 | 105.878522 | 52702799 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,525,909 | 0.000011 | 52702799 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,361,550 | 399.189670 | 52702799 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,273,413 | 1,148,429.551079 | 52702799 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,207,724 | 1,019.358990 | 52702799 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,352 | 1.197871 | 52702799 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,887 | 1.405725 | 52702799 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,912,823 | 15.650807 | 52702799 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,824,230 | 0.022208 | 52702799 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,813,601 | 0.000000 | 52702799 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,776,416 | 0.018794 | 52702799 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,775,684 | 0.000012 | 52702799 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,672,619 | 2.306400 | 52702799 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,555,775 | 1.123642 | 52702799 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,540,606 | 2,755.607813 | 52702799 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,515,093 | 2,754.300608 | 52702799 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,514,682 | 1.105494 | 52702799 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,503,036 | 0.916551 | 52702799 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,459,486 | 13,450.112667 | 52702799 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52702799 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,353,458 | 0.000000 | 52702799 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,512 | 0.435241 | 52702799 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,321,199 | 0.004744 | 52702799 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,311,092 | 0.000277 | 52702799 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,380 | 62.351801 | 52702799 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,244,145 | 1.131470 | 52702799 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,243,740 | 23.316681 | 52702799 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,243,739 | 2,420.514042 | 52702799 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,209,769 | 34,629,639.829662 | 52702799 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,204,895 | 0.029619 | 52702799 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,199,938 | 1.105606 | 52702799 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,185,310 | 1,128,565.088412 | 52702799 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,145,893 | 505,504.940816 | 52702799 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,127,610 | 13.828587 | 52702799 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 1709 ; routes examinées : 35906090 ; candidats optimisés : 189775 ; net attendu > 0 : 0 ; dernier cycle 416.1 ms
- Rejets (moteur) : {'spread_below_threshold': 35447203, 'liquidity_below_min': 265313, 'negative_expected_net': 189775, 'unquotable': 2090, 'borrow_bound_too_small': 1709}
- Enregistrements de la session : 189775 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 189775} ; motifs de rejet : {'negative_expected_net': 189775}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52701339 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 25.399139 USDC | 0.004335 USDC | 0.000000 USDC | 0.005801 USDC | -0.0013 | -0.58 |
| 52701339 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.010701 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0014 | -0.57 |
| 52701339 | USDC→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 38.432434 USDC | 0.003180 USDC | 0.000000 USDC | 0.005434 USDC | -0.0021 | -0.59 |
| 52701339 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.015899 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0021 | -0.59 |
| 52701935 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 5.645253 USDC | 0.002754 USDC | 0.000000 USDC | 0.005098 USDC | -0.0022 | -4.15 |
| 52701936 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 5.645253 USDC | 0.002754 USDC | 0.000000 USDC | 0.005098 USDC | -0.0022 | -4.15 |
| 52701937 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 5.645253 USDC | 0.002754 USDC | 0.000000 USDC | 0.005098 USDC | -0.0022 | -4.15 |
| 52701938 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 5.645253 USDC | 0.002754 USDC | 0.000000 USDC | 0.005098 USDC | -0.0022 | -4.15 |
| 52701939 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 5.645253 USDC | 0.002754 USDC | 0.000000 USDC | 0.005098 USDC | -0.0022 | -4.15 |
| 52701940 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 5.645253 USDC | 0.002754 USDC | 0.000000 USDC | 0.005098 USDC | -0.0022 | -4.15 |

## Fiabilité et décision
- Observations ghost : 658 ; taux observé 0.132 ; borne inférieure crédible (0.9) 0.116 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
