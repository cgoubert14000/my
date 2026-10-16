# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T01:08:39+00:00 ; durée 27.45 min ; blocs 52660958 → 52661785 (745 vus)

## Connexion
- Requêtes RPC : 8651 ; erreurs : 0 ; latence p50/p95 : 444.8/2,423.4 ms
- Rafraîchissements d'état : 746 ; âge des données au dernier bloc : 1.59 s ; changements de frais LP observés (pools à frais dynamiques) : 1645
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,442.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21346 routes
- Par DEX : uniswap_v3 134, aerodrome 235, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 392, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2444.060646, 'AERO': 0.934005, 'cbBTC': 82314.094538}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,517,966 | 2,442.886829 | 52661785 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,076,366 | 1.074076 | 52661785 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,498,029 | 0.029660 | 52661785 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,650,917 | 98.586979 | 52661785 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,036,469 | 0.029711 | 52661785 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,570,543 | 0.029725 | 52661785 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,755,513 | 0.000012 | 52661785 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 9,164,173 | 0.000012 | 52661785 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,132,621 | 2,439.173676 | 52661785 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 535 | 8,230,206 | 2,439.430432 | 52661785 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,076,990 | 0.000012 | 52661785 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,241,952 | 0.001674 | 52661785 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,781,097 | 1.073512 | 52661785 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | fBOMB/AERO | 10000 | 5,449,910 | 0.024845 | 52661785 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,440,538 | 2,443.013629 | 52661785 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,392,651 | 0.029672 | 52661785 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,220,026 | 1.000855 | 52661785 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,883,097 | 0.802398 | 52661785 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,737,310 | 0.000278 | 52661785 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,443,005 | 2,439.290868 | 52661785 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,373,251 | 0.998878 | 52661785 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,032,123 | 34,814.692941 | 52661785 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,581,872 | 2,623.106246 | 52661785 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 409 | 3,364,242 | 2,442.540700 | 52661785 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,850,887 | 0.000012 | 52661785 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,670,125 | 98.563623 | 52661785 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,624,105 | 1,005.057850 | 52661785 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,574,168 | 401.359013 | 52661785 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,505,595 | 0.000011 | 52661785 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,344,753 | 1.141780 | 52661785 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome | WETH/FAI | 10000 | 2,278,172 | 1,167,239.860854 | 52661785 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,440 | 1.196097 | 52661785 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,101,539 | 0.000000 | 52661785 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,385 | 1.403810 | 52661785 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,834,828 | 15.521993 | 52661785 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,822,672 | 0.022698 | 52661785 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,805,847 | 0.019327 | 52661785 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,781,213 | 0.000012 | 52661785 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,686,333 | 2.309115 | 52661785 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,578,064 | 2,621.465017 | 52661785 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,518,467 | 0.916551 | 52661785 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,510,453 | 1.105497 | 52661785 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3060 | 1,477,612 | 2,619.882118 | 52661785 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,377 | 0.830051 | 52661785 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,420,459 | 13,540.733494 | 52661785 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,365,952 | 0.004827 | 52661785 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,353,828 | 0.000000 | 52661785 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,349,938 | 23.252745 | 52661785 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,327,761 | 0.000280 | 52661785 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,326,543 | 1.121123 | 52661785 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,248,881 | 62.301783 | 52661785 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/cbBTC | 3000 | 1,217,621 | 0.029733 | 52661785 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,211,978 | 35,374,630.668579 | 52661785 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,211,768 | 1.105591 | 52661785 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,202,046 | 2,439.173644 | 52661785 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,189,540 | 1,143,664.079159 | 52661785 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,183,568 | 0.886060 | 52661785 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,171,802 | 496,809.210529 | 52661785 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,164,837 | 0.436393 | 52661785 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,129,818 | 13.765763 | 52661785 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 745 ; routes examinées : 15902770 ; candidats optimisés : 128421 ; net attendu > 0 : 0 ; dernier cycle 644.4 ms
- Rejets (moteur) : {'spread_below_threshold': 15616545, 'liquidity_below_min': 155207, 'negative_expected_net': 128421, 'cycle_budget_exhausted': 1852, 'borrow_bound_too_small': 745}
- Enregistrements de la session : 128421 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 128421} ; motifs de rejet : {'negative_expected_net': 128421}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52661112 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661108 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661110 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661111 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002031 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0019 | -4.22 |
| 52661108 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661110 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661111 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661112 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 4.873874 USDC | 0.003053 USDC | 0.000000 USDC | 0.005153 USDC | -0.0019 | -4.31 |
| 52661105 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001985 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -4.55 |
| 52661106 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.001985 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -4.55 |

## Fiabilité et décision
- Observations ghost : 419 ; taux observé 0.138 ; borne inférieure crédible (0.9) 0.118 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
