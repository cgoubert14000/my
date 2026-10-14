# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T04:11:30+00:00 ; durée 21.42 min ; blocs 52580225 → 52580869 (640 vus)

## Connexion
- Requêtes RPC : 8448 ; erreurs : 0 ; latence p50/p95 : 365.2/1,299.3 ms
- Rafraîchissements d'état : 640 ; âge des données au dernier bloc : 3.98 s ; changements de frais LP observés (pools à frais dynamiques) : 941
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15018 ; cycles déclenchés par événement : 583 ; avance médiane sur le rafraîchissement multicall : 749 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,513.13 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 582 pools, 328 jetons, 21942 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 156, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 393, par paires 0), mesurés 584, sous le plancher de 10000.0 $ : 2 → gardés 582 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2513.126375, 'AERO': 0.908483, 'cbBTC': 83773.517368}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,613,526 | 2,513.125876 | 52580869 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,099,793 | 1.102210 | 52580869 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,403,174 | 0.030011 | 52580869 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,902,252 | 108.985490 | 52580869 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,459,585 | 0.030071 | 52580869 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,747,721 | 0.030085 | 52580869 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,428,114 | 2,510.382467 | 52580869 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,325,138 | 0.000012 | 52580869 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,129,411 | 2,513.298547 | 52580869 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 8,577,176 | 0.000012 | 52580869 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 639 | 7,704,814 | 2,511.050600 | 52580869 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,376,093 | 0.001680 | 52580869 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 7,046,711 | 0.000012 | 52580869 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 6,402,971 | 1.106283 | 52580869 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,586,605 | 0.030007 | 52580869 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,550,692 | 1.000859 | 52580869 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,460,343 | 0.026732 | 52580869 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,797,613 | 0.000281 | 52580869 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,745,180 | 0.802386 | 52580869 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,523,918 | 2,510.740974 | 52580869 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,432,087 | 0.999384 | 52580869 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,118,844 | 35,309.858765 | 52580869 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,735,240 | 2,769.961728 | 52580869 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,048,785 | 1.141617 | 52580869 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 3,035,429 | 1,054.469552 | 52580869 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,872,673 | 0.000012 | 52580869 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,699,911 | 0.000011 | 52580869 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,671,497 | 401.436622 | 52580869 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,627,921 | 109.025588 | 52580869 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,461,118 | 1,058,498.079298 | 52580869 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 415 | 2,296,385 | 2,513.739207 | 52580869 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,117,208 | 0.000000 | 52580869 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,905 | 1.189936 | 52580869 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | fBOMB/USDbC | 10000 | 2,039,449 | 0.024082 | 52580869 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,944,100 | 15.574547 | 52580869 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,888,161 | 0.916708 | 52580869 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,880,810 | 0.021167 | 52580869 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,841,628 | 1.374454 | 52580869 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,818,448 | 13,351.840525 | 52580869 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,710,100 | 0.000012 | 52580869 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,618,331 | 2.299458 | 52580869 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,574,307 | 2,768.688506 | 52580869 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,553,788 | 1.105774 | 52580869 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | DRB/WETH | 10000 | 1,476,867 | 0.000000 | 52580869 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,372 | 0.832324 | 52580869 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,424,989 | 1.120934 | 52580869 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,409,124 | 0.000282 | 52580869 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,401,369 | 0.004865 | 52580869 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,397,328 | 2,770.777904 | 52580869 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,308,721 | 23.416440 | 52580869 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,280,063 | 2,510.385140 | 52580869 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,261,594 | 34,559,587.229466 | 52580869 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,983 | 62.391461 | 52580869 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,244,925 | 1.105594 | 52580869 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,243,858 | 0.886451 | 52580869 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,217,101 | 73,193.752645 | 52580869 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,211,072 | 483,539.485072 | 52580869 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,205,102 | 1,179,286.020225 | 52580869 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,204,218 | 43.458471 | 52580869 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,394 | 0.436803 | 52580869 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 1221 ; routes examinées : 26791182 ; candidats optimisés : 132855 ; net attendu > 0 : 0 ; dernier cycle 432.1 ms
- Rejets (moteur) : {'spread_below_threshold': 26399203, 'liquidity_below_min': 226157, 'negative_expected_net': 132855, 'borrow_bound_too_small': 30525, 'unquotable': 2442}
- Enregistrements de la session : 132855 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 132855} ; motifs de rejet : {'negative_expected_net': 132855}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52580701 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.013126 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0026 | -0.85 |
| 52580701 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.013126 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0026 | -0.85 |
| 52580852 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |
| 52580852 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |
| 52580853 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |
| 52580854 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |
| 52580854 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |
| 52580855 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |
| 52580857 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |
| 52580857 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 11.032629 USDC | 0.002472 USDC | 0.000000 USDC | 0.005646 USDC | -0.0029 | -2.88 |

## Fiabilité et décision
- Observations ghost : 9 ; taux observé 0.000 ; borne inférieure crédible (0.9) 0.001 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
