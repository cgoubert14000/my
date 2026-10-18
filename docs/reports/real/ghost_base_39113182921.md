# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T09:01:15+00:00 ; durée 3.03 min ; blocs 52762270 → 52762363 (91 vus)

## Connexion
- Requêtes RPC : 1335 ; erreurs : 0 ; latence p50/p95 : 292.1/961.7 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 2.08 s ; changements de frais LP observés (pools à frais dynamiques) : 156
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1678 ; cycles déclenchés par événement : 111 ; avance médiane sur le rafraîchissement multicall : 428 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,410.99 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,002,914 | 2,410.986474 | 52762363 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,943,394 | 1.199020 | 52762363 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,198,904 | 0.029518 | 52762363 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,710,734 | 108.631452 | 52762363 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,628,468 | 0.029544 | 52762363 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,397,750 | 0.029525 | 52762363 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,758,135 | 0.000012 | 52762363 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,056,976 | 2,411.606144 | 52762363 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,854,373 | 0.000012 | 52762363 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,130,855 | 0.001651 | 52762363 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 788 | 6,916,931 | 2,412.340871 | 52762363 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 6,554,487 | 0.000012 | 52762363 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,487,490 | 2,412.412553 | 52762363 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,326,319 | 0.029529 | 52762363 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,235,628 | 1.000855 | 52762363 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,130,977 | 0.025622 | 52762363 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,819,252 | 0.802398 | 52762363 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,622,280 | 0.000271 | 52762363 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,445,721 | 2,412.108815 | 52762363 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,435,242 | 0.998809 | 52762363 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,085,409 | 33,032.545440 | 52762363 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,956,399 | 1.190501 | 52762363 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,337,332 | 2,866.464363 | 52762363 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 445 | 3,068,897 | 2,414.741923 | 52762363 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,912,140 | 1.141818 | 52762363 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,994 | 0.000012 | 52762363 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,540,221 | 108.670809 | 52762363 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,516,051 | 0.000010 | 52762363 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,282,009 | 409.810655 | 52762363 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,234,423 | 1,181,913.960766 | 52762363 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52762363 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,374 | 1.374087 | 52762363 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,713 | 1.123477 | 52762363 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,938,469 | 1,008.717005 | 52762363 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,888,683 | 15.851079 | 52762363 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,863,982 | 0.000000 | 52762363 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,809,833 | 0.021550 | 52762363 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,779,083 | 0.000012 | 52762363 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,767,212 | 0.018627 | 52762363 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,670,177 | 2.306444 | 52762363 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | weETH_04c0/WETH | 500 | 1,518,367 | 1.105495 | 52762363 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,512,890 | 2,886.814836 | 52762363 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,465,413 | 0.916373 | 52762363 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,384 | 0.826249 | 52762363 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,451,916 | 2,886.606187 | 52762363 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,397,568 | 13,891.622218 | 52762363 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,326,980 | 0.000000 | 52762363 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,580 | 0.435936 | 52762363 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,493 | 0.000270 | 52762363 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,477 | 0.004649 | 52762363 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,255,616 | 0.029519 | 52762363 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,248,124 | 62.377421 | 52762363 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,218,269 | 23.372954 | 52762363 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,869 | 2,411.492978 | 52762363 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,903 | 35,795,251.835590 | 52762363 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,164,066 | 0.885699 | 52762363 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,162,348 | 1,166,766.396236 | 52762363 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,160,976 | 1.105821 | 52762363 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,157,989 | 516,942.421892 | 52762363 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,153,328 | 1.131512 | 52762363 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |

## Recherche d'opportunités
- Cycles : 202 ; routes examinées : 4359160 ; candidats optimisés : 15840 ; net attendu > 0 : 0 ; dernier cycle 230.2 ms
- Rejets (moteur) : {'spread_below_threshold': 4310648, 'liquidity_below_min': 32470, 'negative_expected_net': 15840, 'borrow_bound_too_small': 202}
- Enregistrements de la session : 15840 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 15840} ; motifs de rejet : {'negative_expected_net': 15840}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52762362 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.634901 USDC | 0.002733 USDC | 0.000000 USDC | 0.005085 USDC | -0.0022 | -5.07 |
| 52762362 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.634901 USDC | 0.002733 USDC | 0.000000 USDC | 0.005085 USDC | -0.0022 | -5.07 |
| 52762363 | USDC→[aerodrome]→WETH→[uniswap_v3]→USDC | 4.634901 USDC | 0.002733 USDC | 0.000000 USDC | 0.005085 USDC | -0.0022 | -5.07 |
| 52762362 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001957 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0022 | -4.99 |
| 52762362 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001957 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0022 | -4.99 |
| 52762363 | WETH→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.001957 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0022 | -4.99 |
| 52762362 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.571361 USDC | 0.002716 USDC | 0.000000 USDC | 0.005085 USDC | -0.0022 | -5.18 |
| 52762362 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.571361 USDC | 0.002716 USDC | 0.000000 USDC | 0.005085 USDC | -0.0022 | -5.18 |
| 52762363 | USDC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 4.571361 USDC | 0.002716 USDC | 0.000000 USDC | 0.005085 USDC | -0.0022 | -5.18 |
| 52762362 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→WETH | 0.001922 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0022 | -5.11 |

## Fiabilité et décision
- Observations ghost : 863 ; taux observé 0.131 ; borne inférieure crédible (0.9) 0.117 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.7% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
