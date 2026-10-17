# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T04:48:20+00:00 ; durée 6.12 min ; blocs 52711390 → 52711576 (185 vus)

## Connexion
- Requêtes RPC : 2432 ; erreurs : 0 ; latence p50/p95 : 151.7/883.2 ms
- Rafraîchissements d'état : 186 ; âge des données au dernier bloc : 0.92 s ; changements de frais LP observés (pools à frais dynamiques) : 198
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 823 ; cycles déclenchés par événement : 82 ; avance médiane sur le rafraîchissement multicall : 645 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,421.25 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 329 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 393, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2421.248535, 'AERO': 0.878353, 'cbBTC': 81453.278136}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,170,935 | 2,421.247961 | 52711576 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,777,092 | 1.140520 | 52711576 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,240,199 | 0.029774 | 52711576 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,952,325 | 0.029719 | 52711576 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 15,997,652 | 105.169915 | 52711576 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,408,474 | 0.029707 | 52711576 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,754,343 | 0.000012 | 52711576 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,109,591 | 2,424.665156 | 52711576 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 7,839,955 | 0.000012 | 52711576 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,605,656 | 2,423.964107 | 52711576 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,478,980 | 0.000012 | 52711576 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,156,934 | 0.001677 | 52711576 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,587,627 | 1.140417 | 52711576 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/USDC | 3000 | 5,413,753 | 2,426.472088 | 52711576 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,340,357 | 0.025281 | 52711576 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,332,901 | 0.029769 | 52711576 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,257,911 | 1.000855 | 52711576 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,839,610 | 0.802398 | 52711576 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,684,646 | 0.000276 | 52711576 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,419,466 | 2,423.696099 | 52711576 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,317,814 | 0.998900 | 52711576 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,048,909 | 33,917.669178 | 52711576 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 427 | 4,019,356 | 2,426.528580 | 52711576 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,454,491 | 2,759.327696 | 52711576 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,917,566 | 1.141834 | 52711576 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,850,122 | 0.000012 | 52711576 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,776,183 | 399.888507 | 52711576 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,597,150 | 0.000011 | 52711576 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,594,903 | 105.199814 | 52711576 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,276,410 | 1,148,429.551079 | 52711576 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,407 | 1.197840 | 52711576 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,002,143 | 1.413593 | 52711576 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,849,171 | 15.589844 | 52711576 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,824,936 | 0.022214 | 52711576 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,814,062 | 0.000000 | 52711576 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,775,540 | 0.000012 | 52711576 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,771,091 | 0.018693 | 52711576 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,699,450 | 13,437.884738 | 52711576 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,925 | 2.306475 | 52711576 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,638,399 | 1,014.647623 | 52711576 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,634,211 | 1.123835 | 52711576 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,547,510 | 0.916550 | 52711576 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,540,977 | 2,762.769971 | 52711576 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,516,767 | 1.105495 | 52711576 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3040 | 1,515,187 | 2,761.865014 | 52711576 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,637 | 0.826245 | 52711576 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,358,228 | 0.000000 | 52711576 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,325,890 | 0.004757 | 52711576 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,321,935 | 0.435380 | 52711576 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,312,786 | 0.000278 | 52711576 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,256,748 | 23.260018 | 52711576 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52711576 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,239,379 | 1.131518 | 52711576 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,209,304 | 2,424.664589 | 52711576 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,208,995 | 34,801,915.098400 | 52711576 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,204,792 | 0.029700 | 52711576 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,202,810 | 1.105712 | 52711576 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/WELL | 10000 | 1,183,772 | 1,134,483.911280 | 52711576 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,154,176 | 497,468.150224 | 52711576 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,125,747 | 13.885624 | 52711576 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 267 ; routes examinées : 5609670 ; candidats optimisés : 52729 ; net attendu > 0 : 0 ; dernier cycle 351.4 ms
- Rejets (moteur) : {'spread_below_threshold': 5517214, 'negative_expected_net': 52729, 'liquidity_below_min': 39460, 'borrow_bound_too_small': 267}
- Enregistrements de la session : 52729 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 52729} ; motifs de rejet : {'negative_expected_net': 52729}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52711478 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.891997 USDC | 0.001131 USDC | 0.000000 USDC | 0.005440 USDC | -0.0040 | -6.25 |
| 52711392 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711393 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711394 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711394 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711394 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711395 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711395 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711396 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005438 USDC | -0.0042 | -7.52 |
| 52711397 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 6.082938 USDC | 0.000863 USDC | 0.000000 USDC | 0.005439 USDC | -0.0042 | -7.52 |

## Fiabilité et décision
- Observations ghost : 664 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.115 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
