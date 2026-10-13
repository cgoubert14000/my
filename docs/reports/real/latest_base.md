# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-13T22:04:16+00:00 ; durée 3.02 min ; blocs 52569760 → 52569854 (82 vus)

## Connexion
- Requêtes RPC : 1025 ; erreurs : 0 ; latence p50/p95 : 278.6/2,214.1 ms
- Rafraîchissements d'état : 83 ; âge des données au dernier bloc : 1.79 s ; changements de frais LP observés (pools à frais dynamiques) : 284
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,504.44 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 328 jetons, 21722 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 393, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 3 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2504.443148, 'AERO': 0.902089, 'cbBTC': 83415.257366}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,003,897 | 2,504.443150 | 52569854 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,921,034 | 1.108645 | 52569854 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,255,092 | 0.030073 | 52569854 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,742,011 | 0.030129 | 52569854 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 15,624,574 | 112.019890 | 52569854 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,704,288 | 0.030112 | 52569854 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,550,812 | 2,508.606080 | 52569854 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,361,569 | 0.000012 | 52569854 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,113,627 | 2,507.404145 | 52569854 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 594 | 8,666,026 | 2,507.927315 | 52569854 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,479,448 | 0.000012 | 52569854 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 7,674,766 | 0.000012 | 52569854 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,319,715 | 0.001673 | 52569854 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,597,844 | 1.104830 | 52569854 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,564,184 | 0.030067 | 52569854 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,531,514 | 1.000859 | 52569854 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,428,116 | 0.026858 | 52569854 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,770,173 | 0.000279 | 52569854 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,728,785 | 0.802386 | 52569854 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,476,445 | 2,507.854949 | 52569854 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,409,103 | 0.999278 | 52569854 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,120,914 | 35,031.067944 | 52569854 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,725,862 | 2,771.546269 | 52569854 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,038,229 | 1.141617 | 52569854 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,863,900 | 0.000012 | 52569854 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,718,132 | 403.500997 | 52569854 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,580,518 | 0.000011 | 52569854 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2946 | 2,557,917 | 112.017285 | 52569854 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,452,614 | 1,058,498.264142 | 52569854 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 409 | 2,408,863 | 2,511.742660 | 52569854 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,464 | 1.190192 | 52569854 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,101,710 | 0.000000 | 52569854 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,032,947 | 0.023938 | 52569854 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,949,302 | 15.649372 | 52569854 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,903,672 | 0.021477 | 52569854 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,881,637 | 0.916708 | 52569854 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,800,190 | 1.429328 | 52569854 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,705,856 | 0.000012 | 52569854 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,678,633 | 13,401.012358 | 52569854 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,614,111 | 2.296211 | 52569854 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,577,454 | 2,780.873716 | 52569854 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,548,420 | 1.105798 | 52569854 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 1,533,832 | 1,054.842529 | 52569854 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | DRB/WETH | 10000 | 1,494,890 | 0.000000 | 52569854 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,374 | 0.832322 | 52569854 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,424,149 | 1.119854 | 52569854 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,402,321 | 0.004865 | 52569854 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,401,140 | 0.000281 | 52569854 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/AERO | 3004 | 1,391,467 | 2,780.639007 | 52569854 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,315,756 | 1.105595 | 52569854 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,298,929 | 23.454623 | 52569854 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,277,155 | 2,508.626505 | 52569854 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,262,011 | 34,147,217.178257 | 52569854 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,882 | 62.401582 | 52569854 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,221,532 | 0.886325 | 52569854 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,212,342 | 73,236.598723 | 52569854 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,206,578 | 483,941.217980 | 52569854 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,200,130 | 1,180,874.593192 | 52569854 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,199,796 | 0.436908 | 52569854 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | USDC/NOCK | 3000 | 1,197,471 | 43.949510 | 52569854 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 82 ; routes examinées : 1781204 ; candidats optimisés : 9336 ; net attendu > 0 : 0 ; dernier cycle 384.0 ms
- Rejets (moteur) : {'spread_below_threshold': 1757905, 'liquidity_below_min': 13717, 'negative_expected_net': 9336, 'unquotable': 164, 'borrow_bound_too_small': 82}
- Enregistrements de la session : 9336 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 9336} ; motifs de rejet : {'negative_expected_net': 9336}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 52569770 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000341 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -1.47 |
| 52569770 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.014578 WETH | 0.000001 WETH | 0.000000 WETH | 0.000002 WETH | -0.0040 | -1.18 |
| 52569823 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 12.377548 USDC | 0.000960 USDC | 0.000000 USDC | 0.005638 USDC | -0.0043 | -3.78 |
| 52569823 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.004948 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH | -0.0043 | -3.78 |
| 52569808 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000112 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0046 | -5.38 |
| 52569809 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000112 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0046 | -5.38 |
| 52569810 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000112 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0046 | -5.38 |
| 52569772 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000112 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0046 | -5.37 |
| 52569773 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000112 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0046 | -5.37 |
| 52569774 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.000112 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0046 | -5.37 |

## Fiabilité et décision
- Observations ghost : 0 ; taux observé — ; borne inférieure crédible (0.9) — ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
