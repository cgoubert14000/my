# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T08:31:45+00:00 ; durée 39.68 min ; blocs 52630686 → 52631876 (1128 vus)

## Connexion
- Requêtes RPC : 13087 ; erreurs : 115 ; latence p50/p95 : 162.9/1,987.8 ms
- Rafraîchissements d'état : 1128 ; âge des données au dernier bloc : 5.22 s ; changements de frais LP observés (pools à frais dynamiques) : 2859
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,369.99 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 567 pools, 324 jetons, 20918 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 152, pancakeswap_v3 29, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 204 (rejetés 2) → 609 jetons ; pools candidats 3862 (énumérés 388, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 2 → gardés 567 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2370.057693, 'AERO': 0.841029, 'cbBTC': 81234.761422}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,705,006 | 2,369.988595 | 52631876 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,083,472 | 1.183142 | 52631876 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,840,784 | 0.029207 | 52631876 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,620,702 | 105.746520 | 52631876 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,719,914 | 0.029165 | 52631876 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,308,481 | 0.029158 | 52631876 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,619,958 | 0.000012 | 52631876 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,879,986 | 2,372.032280 | 52631876 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,855,796 | 2,370.136852 | 52631876 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 7,940,831 | 0.000012 | 52631876 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,151,628 | 2,371.729504 | 52631876 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,094,290 | 0.001656 | 52631876 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 6,553,910 | 0.000012 | 52631876 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,241,165 | 0.029213 | 52631876 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,170,053 | 0.026626 | 52631876 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,456,768 | 0.802389 | 52631876 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,365,821 | 0.000274 | 52631876 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,231,505 | 2,371.608158 | 52631876 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,163,517 | 1.000078 | 52631876 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,148,714 | 1.180947 | 52631876 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 3,882,905 | 35,334.776321 | 52631876 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,421,122 | 2,802.974601 | 52631876 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,821,864 | 0.000012 | 52631876 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2913 | 2,534,387 | 105.758347 | 52631876 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,475,242 | 1.141644 | 52631876 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,396,870 | 0.000010 | 52631876 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,321,460 | 1,058,026.313216 | 52631876 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,253,119 | 411.763747 | 52631876 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,439 | 1.194817 | 52631876 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 421 | 2,092,097 | 2,377.616850 | 52631876 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,019,562 | 0.000000 | 52631876 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,850,753 | 0.022627 | 52631876 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,837,793 | 1.403288 | 52631876 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,788,390 | 0.916543 | 52631876 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,771,712 | 0.000012 | 52631876 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,304 | 0.018867 | 52631876 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,718,899 | 15.778435 | 52631876 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,674,133 | 2.301503 | 52631876 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,474,962 | 2,806.461212 | 52631876 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,465,344 | 1.105502 | 52631876 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,516 | 0.831299 | 52631876 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,393,554 | 14,108.389173 | 52631876 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,325,718 | 0.000000 | 52631876 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,320,208 | 1.130522 | 52631876 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/AERO | 3020 | 1,311,208 | 2,806.605709 | 52631876 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/MORPHO | 2850 | 1,306,819 | 1,017.918821 | 52631876 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,637 | 0.004795 | 52631876 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,277,974 | 0.000275 | 52631876 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,249,485 | 1.122418 | 52631876 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,246,491 | 62.540973 | 52631876 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,239,258 | 23.180661 | 52631876 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,199,914 | 2,372.105137 | 52631876 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,178,880 | 1.105595 | 52631876 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,173,001 | 35,583,106.426209 | 52631876 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/EDEL | 7000 | 1,144,101 | 74,667.934471 | 52631876 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/cbBTC | 3000 | 1,141,096 | 0.029217 | 52631876 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,132,432 | 1,187,716.036327 | 52631876 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,122,483 | 506,754.020063 | 52631876 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,112,361 | 14.290372 | 52631876 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,105,546 | 51.563107 | 52631876 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 1127 ; routes examinées : 23574586 ; candidats optimisés : 160570 ; net attendu > 0 : 0 ; dernier cycle 567.6 ms
- Rejets (moteur) : {'spread_below_threshold': 23214068, 'liquidity_below_min': 195828, 'negative_expected_net': 160570, 'unquotable': 2993, 'borrow_bound_too_small': 1127}
- Enregistrements de la session : 160570 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 160570} ; motifs de rejet : {'negative_expected_net': 160570}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52630876 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000620 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0007 | -0.16 |
| 52630876 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.027123 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | -0.0008 | -0.13 |
| 52630876 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 76.031352 USDC | 0.006188 USDC | 0.000000 USDC | 0.007132 USDC | -0.0009 | -0.12 |
| 52630828 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 8.891277 USDC | 0.004698 USDC | 0.000000 USDC | 0.006066 USDC | -0.0013 | -1.54 |
| 52630828 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.003751 WETH | 0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0013 | -1.55 |
| 52631044 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 5.205041 USDC | 0.003545 USDC | 0.000000 USDC | 0.005003 USDC | -0.0013 | -2.80 |
| 52631045 | USDC→[uniswap_v3]→WETH→[aerodrome]→USDC | 5.205041 USDC | 0.003545 USDC | 0.000000 USDC | 0.005003 USDC | -0.0013 | -2.80 |
| 52631044 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002232 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0013 | -2.76 |
| 52631045 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.002232 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0013 | -2.76 |
| 52631219 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.025750 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | -0.0015 | -0.27 |

## Fiabilité et décision
- Observations ghost : 258 ; taux observé 0.190 ; borne inférieure crédible (0.9) 0.160 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
