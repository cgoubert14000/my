# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T00:30:05+00:00 ; durée 137.2 min ; blocs 52570110 → 52574221 (4003 vus)

## Connexion
- Requêtes RPC : 52238 ; erreurs : 245 ; latence p50/p95 : 385.6/1,456.3 ms
- Rafraîchissements d'état : 4003 ; âge des données au dernier bloc : 9.02 s ; changements de frais LP observés (pools à frais dynamiques) : 4803
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 67115 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : 1,404 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,502.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 328 jetons, 21606 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 392, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 2 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2504.448027, 'AERO': 0.900554, 'cbBTC': 83392.589857}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,305,980 | 2,502.744034 | 52574222 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,016,423 | 1.106491 | 52574222 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,237,500 | 0.030070 | 52574222 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,786,947 | 109.579093 | 52574222 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 15,528,541 | 0.030077 | 52574222 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,696,852 | 0.030093 | 52574222 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,401,933 | 2,508.182860 | 52574222 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,366,922 | 0.000012 | 52574222 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,110,534 | 2,503.302282 | 52574222 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,656,938 | 0.000012 | 52574222 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,785,379 | 0.000012 | 52574222 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 639 | 7,655,816 | 2,508.734405 | 52574222 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,331,643 | 0.001681 | 52574222 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,560,340 | 0.030082 | 52574222 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,527,762 | 1.000859 | 52574222 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,437,795 | 0.026858 | 52574222 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,414,777 | 1.104830 | 52574222 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,776,723 | 0.000280 | 52574222 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,725,577 | 0.802386 | 52574222 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,527,802 | 2,508.931267 | 52574222 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,405,322 | 0.999370 | 52574222 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,086,494 | 35,575.360423 | 52574222 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,720,258 | 2,772.245130 | 52574222 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 3,308,311 | 1,057.880302 | 52574222 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,036,187 | 1.141617 | 52574222 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,862,878 | 0.000012 | 52574222 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,798,817 | 401.090032 | 52574222 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,657,775 | 0.000011 | 52574222 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,590,584 | 109.556083 | 52574222 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,450,951 | 1,058,498.079298 | 52574222 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 415 | 2,287,746 | 2,511.363264 | 52574222 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,464 | 1.190192 | 52574222 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,099,772 | 0.000000 | 52574222 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,034,728 | 0.023976 | 52574222 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,913,450 | 15.600109 | 52574222 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,909,411 | 0.021522 | 52574222 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,880,361 | 0.916708 | 52574222 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,800,190 | 1.429328 | 52574222 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,705,690 | 0.000012 | 52574222 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,683,844 | 13,363.220967 | 52574222 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,613,448 | 2.295584 | 52574222 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,577,884 | 2,769.116969 | 52574222 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,547,370 | 1.105774 | 52574222 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | DRB/WETH | 10000 | 1,465,202 | 0.000000 | 52574222 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,372 | 0.832324 | 52574222 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,424,346 | 1.120095 | 52574222 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,402,977 | 0.000282 | 52574222 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,401,368 | 0.004865 | 52574222 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,392,687 | 2,768.136613 | 52574222 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,314,863 | 1.105595 | 52574222 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,281,910 | 23.438158 | 52574222 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,274,743 | 2,508.037726 | 52574222 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,257,783 | 34,477,549.028073 | 52574222 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,882 | 62.401582 | 52574222 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,235,327 | 0.886380 | 52574222 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,211,519 | 73,236.618943 | 52574222 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,206,339 | 43.305745 | 52574222 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,205,758 | 483,941.217980 | 52574222 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,200,113 | 0.436949 | 52574222 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/WELL | 10000 | 1,197,818 | 1,183,829.574507 | 52574222 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |

## Recherche d'opportunités
- Cycles : 7535 ; routes examinées : 162801210 ; candidats optimisés : 897547 ; net attendu > 0 : 15 ; dernier cycle 600.3 ms
- Rejets (moteur) : {'spread_below_threshold': 160521795, 'liquidity_below_min': 1358386, 'negative_expected_net': 897532, 'unquotable': 15058, 'borrow_bound_too_small': 7529, 'cycle_budget_exhausted': 895}
- Enregistrements de la session : 897547 ; net attendu > 0 : 15 ; simulés (eth_call de la vraie tx) : 7 (ok 5, échec 2) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 897547} ; motifs de rejet : {'below_safety_margin': 8, 'negative_expected_net': 897532, 'reliability_not_demonstrated': 15, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52570167 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 160.347048 USDC | 0.162817 USDC | 0.000000 USDC | 0.005640 USDC | 0.157177 USDC (0.1446 €) | 0.157177 USDC | 9.80 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52570167 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 160.347048 USDC | 0.162817 USDC | 0.000000 USDC | 0.005640 USDC | 0.157177 USDC (0.1446 €) | — | 9.80 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52574058 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 227.858475 USDC | 0.037864 USDC | 0.000000 USDC | 0.007525 USDC | 0.030339 USDC (0.0279 €) | — | 1.33 | — (n=0) | REJECTED | below_safety_margin(30339<45571), reliability_not_demonstrated |
| 52574060 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 227.858475 USDC | 0.037864 USDC | 0.000000 USDC | 0.007525 USDC | 0.030339 USDC (0.0279 €) | — | 1.33 | — (n=0) | REJECTED | below_safety_margin(30339<45571), reliability_not_demonstrated |
| 52574058 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002900 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0276 €) | — | 1.24 | — (n=0) | REJECTED | below_safety_margin(36<58), reliability_not_demonstrated |
| 52574060 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002900 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0276 €) | — | 1.24 | — (n=0) | REJECTED | below_safety_margin(36<58), reliability_not_demonstrated |
| 52571476 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 32.734204 USDC | 0.021201 USDC | 0.000000 USDC | 0.005629 USDC | 0.015572 USDC (0.0143 €) | 0.015572 USDC | 4.76 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52572009 | USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 16.547401 USDC | 0.011563 USDC | 0.000000 USDC | 0.007185 USDC | 0.004378 USDC (0.0040 €) | 0.004378 USDC | 2.65 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52572009 | USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 16.547401 USDC | 0.011563 USDC | 0.000000 USDC | 0.007185 USDC | 0.004378 USDC (0.0040 €) | 0.004378 USDC | 2.65 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52572009 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→cbBTC | 0.000152 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0038 €) | 0.000000 cbBTC | 3.28 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52572009 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→FLOCK→[aerodrome]→cbBTC | 0.000152 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0038 €) | — | 3.28 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52571756 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.146681 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0017 €) | — | 0.05 | — (n=0) | REJECTED | below_safety_margin(723976840044<29336115387580), reliability_not_demonstrated |
| 52571756 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 365.127271 USDC | 0.009322 USDC | 0.000000 USDC | 0.007534 USDC | 0.001788 USDC (0.0016 €) | — | 0.05 | — (n=0) | REJECTED | below_safety_margin(1788<73025), reliability_not_demonstrated |
| 52570227 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.895664 USDC | 0.006425 USDC | 0.000000 USDC | 0.005641 USDC | 0.000784 USDC (0.0007 €) | — | 0.44 | — (n=0) | REJECTED | below_safety_margin(784<3579), reliability_not_demonstrated |
| 52570227 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.895664 USDC | 0.006425 USDC | 0.000000 USDC | 0.005641 USDC | 0.000784 USDC (0.0007 €) | — | 0.44 | — (n=0) | REJECTED | below_safety_margin(784<3579), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4 ; taux observé 0.000 ; borne inférieure crédible (0.9) 0.002 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
