# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T01:04:17+00:00 ; durée 33.62 min ; blocs 52833443 → 52834452 (984 vus)

## Connexion
- Requêtes RPC : 13825 ; erreurs : 78 ; latence p50/p95 : 396.3/1,931.5 ms
- Rafraîchissements d'état : 984 ; âge des données au dernier bloc : 5.48 s ; changements de frais LP observés (pools à frais dynamiques) : 1893
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17672 ; cycles déclenchés par événement : 997 ; avance médiane sur le rafraîchissement multicall : 513 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,396.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,070,654 | 2,396.885821 | 52834453 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,174,445 | 1.262380 | 52834453 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,445,167 | 0.029333 | 52834453 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,191,785 | 0.029377 | 52834453 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,245,686 | 99.843033 | 52834453 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,340,509 | 0.029315 | 52834453 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,868,148 | 0.000012 | 52834453 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,339,372 | 2,394.099057 | 52834453 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,300,905 | 2,397.466529 | 52834453 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 7,816,522 | 0.000012 | 52834453 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 773 | 7,405,827 | 2,393.493582 | 52834453 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 7,366,090 | 0.000012 | 52834453 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,172,839 | 0.001673 | 52834453 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,332,171 | 0.029366 | 52834453 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,916,698 | 0.025626 | 52834453 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,775,303 | 0.802395 | 52834453 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,708,674 | 1.269249 | 52834453 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,618,443 | 0.000274 | 52834453 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,412,709 | 2,393.147658 | 52834453 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,323,816 | 0.998768 | 52834453 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,021,087 | 33,700.123444 | 52834453 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 436 | 3,989,371 | 2,397.585132 | 52834453 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,238,837 | 3,045.949625 | 52834453 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,853,049 | 0.000012 | 52834453 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,633,666 | 99.858069 | 52834453 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,629,691 | 1.142112 | 52834453 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,628,915 | 400.874399 | 52834453 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,247,102 | 0.000010 | 52834453 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,180,742 | 1,226,346.894757 | 52834453 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,129,156 | 970.935697 | 52834453 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,184 | 1.238174 | 52834453 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,084 | 1.373409 | 52834453 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,001,946 | 0.000000 | 52834453 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,809,443 | 0.019437 | 52834453 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,243 | 0.000012 | 52834453 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,734,223 | 1.105525 | 52834453 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,733,218 | 16.080303 | 52834453 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,715,934 | 13,662.465353 | 52834453 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,672,752 | 0.020215 | 52834453 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,644,067 | 2.307332 | 52834453 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,552,500 | 0.916343 | 52834453 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,533,295 | 1.121555 | 52834453 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,498,541 | 3,028.020357 | 52834453 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,673 | 0.826781 | 52834453 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,304,792 | 0.000000 | 52834453 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,300,664 | 0.004704 | 52834453 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,294,711 | 0.000275 | 52834453 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,281,205 | 0.029313 | 52834453 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,230,346 | 64.193056 | 52834453 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,219,048 | 1,048,175.782724 | 52834453 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,218,025 | 2,394.104592 | 52834453 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,211,733 | 23.009247 | 52834453 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,193,626 | 35,351,980.698677 | 52834453 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,401 | 0.435758 | 52834453 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,132,028 | 510,323.224563 | 52834453 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,129,909 | 1.131630 | 52834453 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,114,135 | 50.760540 | 52834453 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,113,820 | 0.885551 | 52834453 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,076,584 | 1.001376 | 52834453 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,073,587 | 15.676269 | 52834453 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 1980 ; routes examinées : 41734440 ; candidats optimisés : 173286 ; net attendu > 0 : 0 ; dernier cycle 162.0 ms
- Rejets (moteur) : {'spread_below_threshold': 41203952, 'liquidity_below_min': 307511, 'negative_expected_net': 173286, 'borrow_bound_too_small': 49498, 'cycle_budget_exhausted': 193}
- Enregistrements de la session : 173286 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 173286} ; motifs de rejet : {'negative_expected_net': 173286}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52834383 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002172 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0014 | -3.00 |
| 52834384 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.002172 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0014 | -3.00 |
| 52834383 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 5.246616 USDC | 0.003501 USDC | 0.000000 USDC | 0.005065 USDC | -0.0014 | -2.98 |
| 52834384 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 5.246616 USDC | 0.003501 USDC | 0.000000 USDC | 0.005065 USDC | -0.0014 | -2.98 |
| 52834385 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002168 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0015 | -3.12 |
| 52834385 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002168 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0015 | -3.12 |
| 52834385 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 5.196697 USDC | 0.003444 USDC | 0.000000 USDC | 0.005065 USDC | -0.0015 | -3.12 |
| 52834385 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 5.196697 USDC | 0.003444 USDC | 0.000000 USDC | 0.005065 USDC | -0.0015 | -3.12 |
| 52834384 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002168 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0015 | -3.12 |
| 52834384 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002168 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0015 | -3.12 |

## Fiabilité et décision
- Observations ghost : 1336 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
