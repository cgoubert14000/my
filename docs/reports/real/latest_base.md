# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T10:22:02+00:00 ; durée 3.03 min ; blocs 52721493 → 52721586 (87 vus)

## Connexion
- Requêtes RPC : 1238 ; erreurs : 0 ; latence p50/p95 : 427.5/1,667.6 ms
- Rafraîchissements d'état : 87 ; âge des données au dernier bloc : 3.83 s ; changements de frais LP observés (pools à frais dynamiques) : 115
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1207 ; cycles déclenchés par événement : 73 ; avance médiane sur le rafraîchissement multicall : 721 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,430.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 329 jetons, 21508 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3914 (énumérés 394, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2430.106481, 'AERO': 0.895375, 'cbBTC': 81495.8779}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,549,234 | 2,430.105098 | 52721586 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,250,018 | 1.115866 | 52721586 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,292,944 | 0.029842 | 52721586 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,068,879 | 0.029795 | 52721586 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,114,005 | 104.492217 | 52721586 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,469,385 | 0.029781 | 52721586 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,758,371 | 0.000012 | 52721586 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,131,471 | 2,433.182505 | 52721586 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 8,469,057 | 0.000012 | 52721586 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,842,671 | 0.000012 | 52721586 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 7,267,391 | 2,433.762022 | 52721586 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,163,019 | 0.001675 | 52721586 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,423,537 | 2,433.969114 | 52721586 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,416,289 | 0.025281 | 52721586 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,352,651 | 0.029852 | 52721586 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,277,145 | 1.000855 | 52721586 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,175,924 | 1.122170 | 52721586 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,857,314 | 0.802398 | 52721586 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,698,441 | 0.000276 | 52721586 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,484,259 | 2,433.593493 | 52721586 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,421,798 | 0.998803 | 52721586 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,062,889 | 33,931.544714 | 52721586 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,499,954 | 2,729.988110 | 52721586 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 421 | 3,244,330 | 2,436.762639 | 52721586 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,928,258 | 1.141834 | 52721586 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,838,351 | 0.000012 | 52721586 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,702,566 | 0.000011 | 52721586 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,613,648 | 104.513981 | 52721586 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,577,840 | 402.344946 | 52721586 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,249,192 | 1,185,014.580488 | 52721586 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,278 | 1.123518 | 52721586 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,805 | 1.197614 | 52721586 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52721586 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,876,131 | 15.624220 | 52721586 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,831,202 | 0.022355 | 52721586 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,819,679 | 0.000000 | 52721586 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,806,832 | 1,024.980462 | 52721586 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,800 | 0.000012 | 52721586 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,752,730 | 0.018404 | 52721586 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,740 | 2.307070 | 52721586 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,668,110 | 13,477.642822 | 52721586 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,557,621 | 2,713.256593 | 52721586 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,553,172 | 0.916550 | 52721586 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,534,799 | 2,712.701995 | 52721586 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,522,317 | 1.105495 | 52721586 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,550 | 0.826343 | 52721586 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,367,896 | 0.004872 | 52721586 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,364,690 | 0.000000 | 52721586 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,095 | 0.435747 | 52721586 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,316,774 | 0.000274 | 52721586 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,254,685 | 23.293965 | 52721586 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52721586 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,240,918 | 1.131642 | 52721586 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,230,811 | 1.105714 | 52721586 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,230,714 | 0.029776 | 52721586 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,205,675 | 35,368,823.910888 | 52721586 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,201,712 | 2,433.177758 | 52721586 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,186,700 | 1,137,165.472697 | 52721586 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,152,400 | 504,564.039742 | 52721586 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,122,909 | 13.980057 | 52721586 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 159 ; routes examinées : 3419772 ; candidats optimisés : 15625 ; net attendu > 0 : 0 ; dernier cycle 415.1 ms
- Rejets (moteur) : {'spread_below_threshold': 3369438, 'liquidity_below_min': 31211, 'negative_expected_net': 15625, 'unquotable': 3339, 'borrow_bound_too_small': 159}
- Enregistrements de la session : 15625 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 15625} ; motifs de rejet : {'negative_expected_net': 15625}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52721507 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721507 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721508 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721508 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721509 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721509 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721510 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721510 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721511 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |
| 52721511 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 4.913172 USDC | 0.002121 USDC | 0.000000 USDC | 0.005122 USDC | -0.0028 | -6.11 |

## Fiabilité et décision
- Observations ghost : 721 ; taux observé 0.121 ; borne inférieure crédible (0.9) 0.106 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
