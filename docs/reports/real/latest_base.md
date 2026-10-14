# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T03:53:06+00:00 ; durée 3.02 min ; blocs 52580225 → 52580319 (90 vus)

## Connexion
- Requêtes RPC : 1245 ; erreurs : 0 ; latence p50/p95 : 278.0/1,650.2 ms
- Rafraîchissements d'état : 91 ; âge des données au dernier bloc : 1.36 s ; changements de frais LP observés (pools à frais dynamiques) : 146
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1930 ; cycles déclenchés par événement : 81 ; avance médiane sur le rafraîchissement multicall : 449 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,513.13 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 582 pools, 328 jetons, 21942 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 393, par paires 0), mesurés 584, sous le plancher de 10000.0 $ : 2 → gardés 582 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2513.126375, 'AERO': 0.908483, 'cbBTC': 83773.517368}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,615,526 | 2,513.125835 | 52580319 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,128,239 | 1.100736 | 52580319 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,399,659 | 0.030038 | 52580319 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,897,598 | 108.957840 | 52580319 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,140,771 | 0.030073 | 52580319 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,743,632 | 0.030085 | 52580319 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,428,059 | 2,515.653551 | 52580319 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,322,197 | 0.000012 | 52580319 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,129,411 | 2,513.113549 | 52580319 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,674,517 | 0.000012 | 52580319 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 609 | 8,236,155 | 2,514.955115 | 52580319 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,377,078 | 0.001684 | 52580319 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 7,369,624 | 0.000012 | 52580319 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,172,898 | 1.106283 | 52580319 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,585,142 | 0.030034 | 52580319 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,550,692 | 1.000859 | 52580319 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,464,017 | 0.026741 | 52580319 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,797,613 | 0.000281 | 52580319 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,745,179 | 0.802386 | 52580319 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,523,760 | 2,514.841341 | 52580319 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,428,118 | 0.999384 | 52580319 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,120,875 | 35,275.057604 | 52580319 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,737,742 | 2,769.955422 | 52580319 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,048,785 | 1.141617 | 52580319 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,871,298 | 0.000012 | 52580319 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,695,013 | 1,054.469552 | 52580319 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,669,596 | 0.000011 | 52580319 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,628,300 | 108.992467 | 52580319 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,461,118 | 1,058,498.079298 | 52580319 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,417,743 | 400.543536 | 52580319 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 412 | 2,394,151 | 2,518.563827 | 52580319 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,117,207 | 0.000000 | 52580319 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,905 | 1.189936 | 52580319 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | fBOMB/USDbC | 10000 | 2,039,449 | 0.024082 | 52580319 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,920,797 | 15.574547 | 52580319 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,888,161 | 0.916708 | 52580319 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,881,447 | 0.021197 | 52580319 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,841,628 | 1.374454 | 52580319 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,709,305 | 0.000012 | 52580319 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,618,331 | 2.299458 | 52580319 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,574,994 | 2,768.704723 | 52580319 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,553,788 | 1.105774 | 52580319 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | DRB/WETH | 10000 | 1,476,064 | 0.000000 | 52580319 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,372 | 0.832324 | 52580319 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,456,696 | 13,320.767633 | 52580319 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,424,748 | 1.120601 | 52580319 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,409,125 | 0.000282 | 52580319 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,401,369 | 0.004865 | 52580319 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3016 | 1,398,296 | 2,770.778055 | 52580319 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,308,721 | 23.416440 | 52580319 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,289,127 | 2,515.649263 | 52580319 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,261,596 | 34,559,417.593909 | 52580319 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,983 | 62.391461 | 52580319 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,244,925 | 1.105594 | 52580319 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,243,826 | 0.886451 | 52580319 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,217,097 | 73,194.260179 | 52580319 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,211,072 | 483,539.485072 | 52580319 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,205,102 | 1,179,286.020225 | 52580319 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,202,941 | 43.550751 | 52580319 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,361 | 0.436784 | 52580319 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 171 ; routes examinées : 3752082 ; candidats optimisés : 9928 ; net attendu > 0 : 0 ; dernier cycle 103.3 ms
- Rejets (moteur) : {'spread_below_threshold': 3711869, 'liquidity_below_min': 25668, 'negative_expected_net': 9928, 'borrow_bound_too_small': 4275, 'unquotable': 342}
- Enregistrements de la session : 9928 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 9928} ; motifs de rejet : {'negative_expected_net': 9928}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52580229 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.000178 USDC | 0.000000 USDC | 0.005299 USDC | -0.0050 | -54.77 |
| 52580230 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.000178 USDC | 0.000000 USDC | 0.005299 USDC | -0.0050 | -54.77 |
| 52580230 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.000178 USDC | 0.000000 USDC | 0.005299 USDC | -0.0050 | -54.77 |
| 52580229 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.000398 WETH | -0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0050 | -54.78 |
| 52580230 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.000398 WETH | -0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0050 | -54.78 |
| 52580230 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.000398 WETH | -0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0050 | -54.78 |
| 52580235 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 4.306256 USDC | 0.000116 USDC | 0.000000 USDC | 0.005645 USDC | -0.0051 | -12.84 |
| 52580237 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 4.306256 USDC | 0.000116 USDC | 0.000000 USDC | 0.005645 USDC | -0.0051 | -12.84 |
| 52580237 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 4.306256 USDC | 0.000116 USDC | 0.000000 USDC | 0.005645 USDC | -0.0051 | -12.84 |
| 52580238 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 4.306256 USDC | 0.000116 USDC | 0.000000 USDC | 0.005645 USDC | -0.0051 | -12.84 |

## Fiabilité et décision
- Observations ghost : 9 ; taux observé 0.000 ; borne inférieure crédible (0.9) 0.001 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
