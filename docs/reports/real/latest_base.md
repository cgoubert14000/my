# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T07:55:08+00:00 ; durée 3.06 min ; blocs 52630686 → 52630780 (91 vus)

## Connexion
- Requêtes RPC : 1083 ; erreurs : 0 ; latence p50/p95 : 124.4/1,981.0 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 1.72 s ; changements de frais LP observés (pools à frais dynamiques) : 253
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,370.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 567 pools, 324 jetons, 20918 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 152, pancakeswap_v3 29, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 204 (rejetés 2) → 609 jetons ; pools candidats 3862 (énumérés 388, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 2 → gardés 567 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2370.057693, 'AERO': 0.841029, 'cbBTC': 81234.761422}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,701,472 | 2,370.057091 | 52630780 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,972,951 | 1.189020 | 52630780 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,830,777 | 0.029185 | 52630780 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,515,561 | 107.190134 | 52630780 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,726,288 | 0.029165 | 52630780 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,305,114 | 0.029158 | 52630780 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,623,885 | 0.000012 | 52630780 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,881,028 | 2,375.239020 | 52630780 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,855,923 | 2,370.134684 | 52630780 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 362 | 7,943,452 | 0.000012 | 52630780 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,091,639 | 0.001651 | 52630780 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 818 | 6,923,823 | 2,375.880431 | 52630780 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 6,309,407 | 0.000012 | 52630780 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,242,082 | 0.029190 | 52630780 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,157,524 | 0.026621 | 52630780 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,456,896 | 0.802389 | 52630780 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,365,886 | 0.000274 | 52630780 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,232,186 | 2,376.150171 | 52630780 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,167,685 | 1.000077 | 52630780 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,884,681 | 35,304.527233 | 52630780 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,412,622 | 2,799.659587 | 52630780 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,231,379 | 1.180947 | 52630780 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,823,255 | 0.000012 | 52630780 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2799 | 2,516,286 | 107.154095 | 52630780 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,504,709 | 412.564580 | 52630780 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,475,381 | 1.141645 | 52630780 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,364,884 | 0.000010 | 52630780 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,321,527 | 1,058,026.313216 | 52630780 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,439 | 1.194817 | 52630780 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 451 | 2,063,292 | 2,381.127064 | 52630780 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,052,226 | 1,028.404981 | 52630780 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,030,214 | 0.000000 | 52630780 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,840,610 | 0.022629 | 52630780 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,837,793 | 1.403288 | 52630780 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,788,442 | 0.916543 | 52630780 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,772,582 | 0.000012 | 52630780 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,768,135 | 15.778591 | 52630780 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,750,698 | 0.018511 | 52630780 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,116 | 2.301592 | 52630780 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,513,172 | 14,135.443433 | 52630780 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,472,528 | 2,819.352292 | 52630780 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,465,386 | 1.105502 | 52630780 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,570 | 0.831240 | 52630780 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,122 | 0.000000 | 52630780 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,322,966 | 1.130500 | 52630780 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/AERO | 3036 | 1,307,182 | 2,819.257670 | 52630780 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,676 | 0.004795 | 52630780 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,277,999 | 0.000274 | 52630780 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,248,468 | 1.120891 | 52630780 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,246,491 | 62.540973 | 52630780 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,234,588 | 23.208491 | 52630780 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,198,932 | 2,375.197883 | 52630780 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,178,914 | 1.105595 | 52630780 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,174,954 | 35,409,724.513881 | 52630780 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/EDEL | 7000 | 1,144,139 | 74,667.350288 | 52630780 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/cbBTC | 3000 | 1,141,577 | 0.029264 | 52630780 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,132,477 | 1,187,690.005083 | 52630780 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,122,516 | 506,754.020063 | 52630780 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,114,827 | 14.211134 | 52630780 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,105,291 | 51.586943 | 52630780 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 91 ; routes examinées : 1903538 ; candidats optimisés : 16661 ; net attendu > 0 : 0 ; dernier cycle 411.6 ms
- Rejets (moteur) : {'spread_below_threshold': 1870884, 'negative_expected_net': 16661, 'liquidity_below_min': 15720, 'unquotable': 182, 'borrow_bound_too_small': 91}
- Enregistrements de la session : 16661 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 16661} ; motifs de rejet : {'negative_expected_net': 16661}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52630763 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.887831 USDC | 0.003067 USDC | 0.000000 USDC | 0.004999 USDC | -0.0018 | -3.95 |
| 52630763 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.002058 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0018 | -3.97 |
| 52630763 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.695560 USDC | 0.002852 USDC | 0.000000 USDC | 0.004999 USDC | -0.0020 | -4.57 |
| 52630763 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.002009 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0020 | -4.52 |
| 52630762 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.503912 USDC | 0.002550 USDC | 0.000000 USDC | 0.004999 USDC | -0.0023 | -5.44 |
| 52630762 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.001907 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0023 | -5.43 |
| 52630761 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.363740 USDC | 0.002507 USDC | 0.000000 USDC | 0.004999 USDC | -0.0023 | -5.71 |
| 52630761 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001907 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0023 | -5.52 |
| 52630761 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.397436 USDC | 0.002461 USDC | 0.000000 USDC | 0.004999 USDC | -0.0023 | -5.77 |
| 52630761 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.001876 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0023 | -5.72 |

## Fiabilité et décision
- Observations ghost : 258 ; taux observé 0.190 ; borne inférieure crédible (0.9) 0.160 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
