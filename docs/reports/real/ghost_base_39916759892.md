# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T07:25:37+00:00 ; durée 3.01 min ; blocs 52975401 → 52975494 (91 vus)

## Connexion
- Requêtes RPC : 1089 ; erreurs : 0 ; latence p50/p95 : 191.5/1,159.0 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 2.05 s ; changements de frais LP observés (pools à frais dynamiques) : 91
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 66 ; cycles déclenchés par événement : 17 ; avance médiane sur le rafraîchissement multicall : 442 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,402.29 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 316 jetons, 19290 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 136, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 199 (rejetés 2) → 604 jetons ; pools candidats 3831 (énumérés 359, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2402.292282, 'AERO': 0.794098, 'cbBTC': 81667.512713}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,700,062 | 2,402.291810 | 52975494 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,435,502 | 0.029421 | 52975494 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 13,451,282 | 91.458999 | 52975494 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 11,627,282 | 1.259291 | 52975494 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,301,539 | 0.029405 | 52975494 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,863,281 | 0.000012 | 52975494 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,953,513 | 0.029402 | 52975494 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,691,998 | 2,401.640899 | 52975494 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,171,214 | 0.001670 | 52975494 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,354,570 | 0.000012 | 52975494 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,636,931 | 2,401.964438 | 52975494 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,444,978 | 0.029414 | 52975494 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 5,261,466 | 0.000012 | 52975494 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,573,293 | 2,401.860394 | 52975494 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,297,196 | 0.999617 | 52975494 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,290,047 | 2,403.644235 | 52975494 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 4,002,065 | 34,147.377976 | 52975494 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,408,317 | 0.000274 | 52975494 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 400 | 2,907,051 | 2,405.831558 | 52975494 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,568,661 | 91.433313 | 52975494 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,316,556 | 391.152998 | 52975494 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/AERO | 10000 | 2,251,387 | 3,025.077109 | 52975494 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/FAI | 10000 | 2,236,597 | 1,169,621.444452 | 52975494 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,007,619 | 0.000000 | 52975494 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,924,286 | 0.000012 | 52975494 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,781,908 | 0.018189 | 52975494 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,760,918 | 0.000012 | 52975494 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,641,025 | 1.525684 | 52975494 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,615,844 | 3,028.748341 | 52975494 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,772 | 0.823512 | 52975494 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,421,961 | 13,284.861746 | 52975494 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,356,546 | 0.004930 | 52975494 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,300,658 | 2.317665 | 52975494 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,297,823 | 0.000276 | 52975494 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,287,192 | 2,401.629187 | 52975494 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,268,975 | 0.000000 | 52975494 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,229,408 | 64.291011 | 52975494 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,188,982 | 36,009,984.560886 | 52975494 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,179,019 | 16.097978 | 52975494 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/WELL | 10000 | 1,169,907 | 1,111,759.578421 | 52975494 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,168,040 | 45.998434 | 52975494 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,151,045 | 497,888.024170 | 52975494 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 1,092,014 | 0.038038 | 52975494 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 1,087,716 | 75,143.296246 | 52975494 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | weETH_04c0/WETH | 500 | 1,074,678 | 1.105789 | 52975494 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,065,972 | 21,313,449.073659 | 52975494 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,046,676 | 16.693291 | 52975494 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 1,033,489 | 0.000010 | 52975494 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,005,593 | 23.092166 | 52975494 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 967,096 | 1,051.349228 | 52975494 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 949,271 | 2,390.321401 | 52975494 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 919,888 | 0.000550 | 52975494 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/bsdETH | 100 | 893,074 | 0.917166 | 52975494 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 885,665 | 17.703601 | 52975494 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 866,459 | 2,402.691380 | 52975494 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/wstETH | 3000 | 813,825 | 0.803225 | 52975494 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 789,730 | 0.055898 | 52975494 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 789,317 | 0.664050 | 52975494 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | fBOMB/USDC | 10000 | 773,700 | 0.018516 | 52975494 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 772,714 | 4,560,326.587097 | 52975494 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |

## Recherche d'opportunités
- Cycles : 108 ; routes examinées : 2083320 ; candidats optimisés : 6397 ; net attendu > 0 : 0 ; dernier cycle 256.1 ms
- Rejets (moteur) : {'spread_below_threshold': 2066413, 'liquidity_below_min': 10402, 'negative_expected_net': 6397, 'borrow_bound_too_small': 108}
- Enregistrements de la session : 6397 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 6397} ; motifs de rejet : {'negative_expected_net': 6397}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52975456 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975457 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975458 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975459 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975460 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975461 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975462 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975463 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975464 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |
| 52975465 | USDC→[aerodrome]→PLAY→[pancakeswap_v3]→USDC | 5.697840 USDC | 0.003164 USDC | 0.000000 USDC | 0.005066 USDC | -0.0017 | -3.34 |

## Fiabilité et décision
- Observations ghost : 1980 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
