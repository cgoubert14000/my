# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T09:18:05+00:00 ; durée 86.01 min ; blocs 52630686 → 52633265 (2436 vus)

## Connexion
- Requêtes RPC : 28064 ; erreurs : 140 ; latence p50/p95 : 129.6/1,943.3 ms
- Rafraîchissements d'état : 2436 ; âge des données au dernier bloc : 5.29 s ; changements de frais LP observés (pools à frais dynamiques) : 5787
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,370.55 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 567 pools, 324 jetons, 20918 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 152, pancakeswap_v3 29, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 204 (rejetés 2) → 609 jetons ; pools candidats 3862 (énumérés 388, par paires 0), mesurés 569, sous le plancher de 10000.0 $ : 2 → gardés 567 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2370.057693, 'AERO': 0.841029, 'cbBTC': 81234.761422}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,698,046 | 2,370.554690 | 52633266 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,040,723 | 1.185440 | 52633266 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,845,407 | 0.029198 | 52633266 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,624,464 | 105.746074 | 52633266 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,808,597 | 0.029166 | 52633266 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,329,306 | 0.029158 | 52633266 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,627,910 | 0.000012 | 52633266 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,952,983 | 2,370.676678 | 52633266 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,856,853 | 2,370.794694 | 52633266 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,967,770 | 0.000012 | 52633266 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,099,473 | 0.001654 | 52633266 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 743 | 6,944,287 | 2,370.783217 | 52633266 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 6,745,376 | 0.000012 | 52633266 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,244,068 | 0.029195 | 52633266 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,165,491 | 0.026641 | 52633266 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,784,353 | 1.180947 | 52633266 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,458,142 | 0.802389 | 52633266 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,366,864 | 0.000274 | 52633266 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,236,396 | 2,370.740224 | 52633266 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,165,912 | 1.000078 | 52633266 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,881,752 | 35,372.676515 | 52633266 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,418,198 | 2,803.256784 | 52633266 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,822,865 | 0.000012 | 52633266 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2847 | 2,535,547 | 105.755140 | 52633266 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,475,911 | 1.141650 | 52633266 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,363,633 | 0.000010 | 52633266 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,331,459 | 1,049,472.215109 | 52633266 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,253,146 | 407.402399 | 52633266 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/USDT | 445 | 2,218,818 | 2,375.519210 | 52633266 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,439 | 1.194817 | 52633266 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,020,372 | 0.000000 | 52633266 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,862,347 | 0.022629 | 52633266 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,837,793 | 1.403288 | 52633266 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,800,392 | 15.769936 | 52633266 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,787,458 | 0.916541 | 52633266 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,303 | 0.000012 | 52633266 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,324 | 0.018864 | 52633266 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,089 | 2.301503 | 52633266 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2721 | 1,587,754 | 1,019.599002 | 52633266 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/AERO | 3000 | 1,474,250 | 2,812.126172 | 52633266 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,465,694 | 1.105502 | 52633266 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,410 | 0.831299 | 52633266 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,383,686 | 13,940.145675 | 52633266 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,328,654 | 0.000000 | 52633266 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,323,014 | 1.130500 | 52633266 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/AERO | 3060 | 1,309,861 | 2,810.201170 | 52633266 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,949 | 0.004795 | 52633266 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,298,127 | 23.171446 | 52633266 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,278,283 | 0.000275 | 52633266 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,249,012 | 1.121548 | 52633266 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,246,459 | 62.544172 | 52633266 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,208,500 | 2,370.719813 | 52633266 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,179,162 | 1.105595 | 52633266 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,174,110 | 35,586,327.025337 | 52633266 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/cbBTC | 3000 | 1,142,395 | 0.029217 | 52633266 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,132,702 | 1,187,716.036327 | 52633266 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,124,056 | 505,145.788086 | 52633266 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,123,992 | 77,400.701065 | 52633266 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,118,336 | 50.390449 | 52633266 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,112,479 | 14.286604 | 52633266 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 2436 ; routes examinées : 50956248 ; candidats optimisés : 365755 ; net attendu > 0 : 4 ; dernier cycle 627.7 ms
- Rejets (moteur) : {'spread_below_threshold': 50156999, 'liquidity_below_min': 425048, 'negative_expected_net': 365751, 'unquotable': 5611, 'borrow_bound_too_small': 2436, 'cycle_budget_exhausted': 399}
- Enregistrements de la session : 365755 ; net attendu > 0 : 4 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 365755} ; motifs de rejet : {'below_safety_margin': 4, 'negative_expected_net': 365751, 'p_lower_below_threshold': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52633002 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001862 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0030 €) | — | 0.21 | 0.071 (n=30) | REJECTED | below_safety_margin(4<37), p_lower_below_threshold(0.07<0.75) |
| 52633002 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 194.176044 USDC | 0.010260 USDC | 0.000000 USDC | 0.007128 USDC | 0.003132 USDC (0.0029 €) | — | 0.16 | 0.071 (n=30) | REJECTED | below_safety_margin(3132<38835), p_lower_below_threshold(0.07<0.75) |
| 52633002 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 161.706871 USDC | 0.008627 USDC | 0.000000 USDC | 0.007128 USDC | 0.001499 USDC (0.0014 €) | — | 0.09 | 0.071 (n=30) | REJECTED | below_safety_margin(1499<32341), p_lower_below_threshold(0.07<0.75) |
| 52633002 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.002004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.05 | 0.071 (n=30) | REJECTED | below_safety_margin(1<40), p_lower_below_threshold(0.07<0.75) |

## Fiabilité et décision
- Observations ghost : 258 ; taux observé 0.190 ; borne inférieure crédible (0.9) 0.160 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
