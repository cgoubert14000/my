# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T21:48:05+00:00 ; durée 9.17 min ; blocs 52914691 → 52914968 (273 vus)

## Connexion
- Requêtes RPC : 3773 ; erreurs : 0 ; latence p50/p95 : 103.3/1,481.2 ms
- Rafraîchissements d'état : 274 ; âge des données au dernier bloc : 1.65 s ; changements de frais LP observés (pools à frais dynamiques) : 271
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3256 ; cycles déclenchés par événement : 265 ; avance médiane sur le rafraîchissement multicall : 1,021 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,492.49 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 326 jetons, 22742 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 158, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 2 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2492.485305, 'AERO': 0.830593, 'cbBTC': 84747.685068}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,074,809 | 2,492.485299 | 52914968 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,516,598 | 1.202581 | 52914968 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,198,931 | 90.551186 | 52914968 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,738,709 | 0.029471 | 52914968 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,129,994 | 0.029486 | 52914968 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,625,916 | 0.029499 | 52914968 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,919,431 | 0.000012 | 52914968 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,873,279 | 2,498.003760 | 52914968 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,430,357 | 2,492.718856 | 52914968 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 7,942,443 | 0.000012 | 52914968 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,872,848 | 2,497.562014 | 52914968 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,460,780 | 0.000012 | 52914968 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,420,717 | 0.001667 | 52914968 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,686,359 | 0.029465 | 52914968 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,894,873 | 0.023185 | 52914968 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,602,449 | 2,497.712309 | 52914968 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,452,656 | 0.999948 | 52914968 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,409,894 | 2,500.593259 | 52914968 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,246,512 | 0.000278 | 52914968 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,124,277 | 34,639.984518 | 52914968 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,879,502 | 1.195212 | 52914968 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,347,093 | 2,985.686175 | 52914968 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/wstETH | 90 | 3,192,650 | 0.802246 | 52914968 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,874,723 | 90.516983 | 52914968 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,701,786 | 390.977348 | 52914968 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,325,103 | 0.000010 | 52914968 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,298,097 | 1,193,481.314505 | 52914968 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,283,876 | 0.915907 | 52914968 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,280,050 | 0.000012 | 52914968 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,114,905 | 1,045.052232 | 52914968 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,111,871 | 0.000012 | 52914968 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,030,750 | 1.383527 | 52914968 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,965,832 | 0.000000 | 52914968 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,940,630 | 1.105712 | 52914968 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,833,105 | 13,270.023680 | 52914968 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,824,967 | 0.019044 | 52914968 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,759,297 | 15.890244 | 52914968 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,718,002 | 2.310661 | 52914968 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,708,898 | 1.490996 | 52914968 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,687,068 | 3,003.349180 | 52914968 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,572,484 | 1.142104 | 52914968 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,542 | 0.826835 | 52914968 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,428,464 | 1.123405 | 52914968 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | fBOMB/USDC | 10000 | 1,407,156 | 0.019789 | 52914968 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,405,984 | 0.004892 | 52914968 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,387,984 | 0.000000 | 52914968 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,356,602 | 0.000280 | 52914968 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,324,771 | 0.029502 | 52914968 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,304,355 | 2,497.992985 | 52914968 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/NOCK | 3000 | 1,267,499 | 39.220465 | 52914968 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 1,255,260 | 1,068,938.943313 | 52914968 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,242,176 | 35,184,363.349647 | 52914968 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,232,698 | 63.948314 | 52914968 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,215,421 | 71,993.977150 | 52914968 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,214,482 | 23.099980 | 52914968 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,207,963 | 485,402.667813 | 52914968 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,175,696 | 0.436598 | 52914968 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,149,576 | 0.886164 | 52914968 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,143,258 | 1.106154 | 52914968 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,118,190 | 20,907,427.211674 | 52914968 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 538 ; routes examinées : 12235196 ; candidats optimisés : 91387 ; net attendu > 0 : 0 ; dernier cycle 400.8 ms
- Rejets (moteur) : {'spread_below_threshold': 12041277, 'liquidity_below_min': 101994, 'negative_expected_net': 91387, 'borrow_bound_too_small': 538}
- Enregistrements de la session : 91387 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 91387} ; motifs de rejet : {'negative_expected_net': 91387}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52914791 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914792 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914792 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914774 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914774 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914775 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914775 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914776 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914776 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |
| 52914777 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000401 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0005 | -5.40 |

## Fiabilité et décision
- Observations ghost : 1750 ; taux observé 0.099 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
