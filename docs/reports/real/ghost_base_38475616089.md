# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-13T23:05:05+00:00 ; durée 52.19 min ; blocs 52570110 → 52571676 (1529 vus)

## Connexion
- Requêtes RPC : 19722 ; erreurs : 70 ; latence p50/p95 : 249.9/1,228.6 ms
- Rafraîchissements d'état : 1529 ; âge des données au dernier bloc : 2.18 s ; changements de frais LP observés (pools à frais dynamiques) : 1642
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22772 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : 618 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,505.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 328 jetons, 21606 routes
- Par DEX : uniswap_v3 141, aerodrome 236, aerodrome_slipstream 154, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3923 (énumérés 392, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 2 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2504.448027, 'AERO': 0.900554, 'cbBTC': 83392.589857}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,433,107 | 2,505.564063 | 52571676 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,898,121 | 1.109941 | 52571676 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,266,999 | 0.030041 | 52571676 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,716,650 | 110.810823 | 52571676 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 14,405,737 | 0.030102 | 52571676 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,713,866 | 0.030112 | 52571676 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,407,376 | 2,502.300556 | 52571676 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,374,169 | 0.000012 | 52571676 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,115,666 | 2,508.352303 | 52571676 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 833 | 9,082,404 | 2,501.640674 | 52571676 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 362 | 8,484,019 | 0.000012 | 52571676 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,325,293 | 0.001670 | 52571676 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 580 | 6,988,363 | 0.000012 | 52571676 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,568,500 | 0.030029 | 52571676 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,564,166 | 1.104830 | 52571676 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,533,990 | 1.000859 | 52571676 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,425,000 | 0.026858 | 52571676 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,775,014 | 0.000280 | 52571676 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,730,901 | 0.802386 | 52571676 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,469,615 | 2,501.402149 | 52571676 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,415,802 | 0.999277 | 52571676 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,089,662 | 35,600.356925 | 52571676 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,724,523 | 2,771.980379 | 52571676 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,039,608 | 1.141617 | 52571676 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,866,246 | 0.000012 | 52571676 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,660,850 | 0.000011 | 52571676 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,596,574 | 403.236768 | 52571676 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 2,585,237 | 1,059.108598 | 52571676 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,576,276 | 110.837589 | 52571676 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,453,712 | 1,058,498.264142 | 52571676 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 460 | 2,452,232 | 2,505.656079 | 52571676 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,464 | 1.190192 | 52571676 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,101,719 | 0.000000 | 52571676 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,033,001 | 0.023939 | 52571676 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,909,046 | 15.648147 | 52571676 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,904,902 | 0.021440 | 52571676 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,882,479 | 0.916708 | 52571676 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,800,190 | 1.429328 | 52571676 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,741,227 | 13,410.178722 | 52571676 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,707,266 | 0.000012 | 52571676 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,614,833 | 2.296211 | 52571676 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,577,766 | 2,782.238420 | 52571676 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,549,113 | 1.105798 | 52571676 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | DRB/WETH | 10000 | 1,494,238 | 0.000000 | 52571676 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,372 | 0.832324 | 52571676 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,424,112 | 1.119806 | 52571676 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,402,947 | 0.004865 | 52571676 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,402,468 | 0.000281 | 52571676 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/AERO | 3012 | 1,390,876 | 2,782.960861 | 52571676 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,316,345 | 1.105595 | 52571676 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,292,520 | 23.476426 | 52571676 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,277,561 | 2,502.302090 | 52571676 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,261,371 | 34,338,298.620289 | 52571676 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,882 | 62.401582 | 52571676 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,225,382 | 0.886355 | 52571676 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/EDEL | 7000 | 1,212,884 | 73,236.618943 | 52571676 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,207,117 | 483,941.217980 | 52571676 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,201,937 | 1,178,381.926299 | 52571676 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,200,223 | 43.748217 | 52571676 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,200,113 | 0.436949 | 52571676 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 2818 ; routes examinées : 60885708 ; candidats optimisés : 440006 ; net attendu > 0 : 5 ; dernier cycle 174.3 ms
- Rejets (moteur) : {'spread_below_threshold': 59905302, 'liquidity_below_min': 531258, 'negative_expected_net': 440001, 'unquotable': 5628, 'borrow_bound_too_small': 2814, 'cycle_budget_exhausted': 700}
- Enregistrements de la session : 440006 ; net attendu > 0 : 5 ; simulés (eth_call de la vraie tx) : 3 (ok 2, échec 1) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 440006} ; motifs de rejet : {'below_safety_margin': 2, 'negative_expected_net': 440001, 'reliability_not_demonstrated': 5, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52570167 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 160.347048 USDC | 0.162817 USDC | 0.000000 USDC | 0.005640 USDC | 0.157177 USDC (0.1446 €) | 0.157177 USDC | 9.80 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52570167 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 160.347048 USDC | 0.162817 USDC | 0.000000 USDC | 0.005640 USDC | 0.157177 USDC (0.1446 €) | — | 9.80 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52571476 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 32.734204 USDC | 0.021201 USDC | 0.000000 USDC | 0.005629 USDC | 0.015572 USDC (0.0143 €) | 0.015572 USDC | 4.76 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52570227 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.895664 USDC | 0.006425 USDC | 0.000000 USDC | 0.005641 USDC | 0.000784 USDC (0.0007 €) | — | 0.44 | — (n=0) | REJECTED | below_safety_margin(784<3579), reliability_not_demonstrated |
| 52570227 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 17.895664 USDC | 0.006425 USDC | 0.000000 USDC | 0.005641 USDC | 0.000784 USDC (0.0007 €) | — | 0.44 | — (n=0) | REJECTED | below_safety_margin(784<3579), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2 ; taux observé 0.000 ; borne inférieure crédible (0.9) 0.003 ; seuil 0.75 → **FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES**
- Statut de maturité : **APPRENTISSAGE** — FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ❌ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
