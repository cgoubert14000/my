# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T11:46:07+00:00 ; durée 91.17 min ; blocs 59896587 → 59923927 (8992 vus)

## Connexion
- Requêtes RPC : 82579 ; erreurs : 0 ; latence p50/p95 : 80.3/852.3 ms
- Rafraîchissements d'état : 8992 ; âge des données au dernier bloc : 5.03 s ; changements de frais LP observés (pools à frais dynamiques) : 3956
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8064 ; cycles déclenchés par événement : 1983 ; avance médiane sur le rafraîchissement multicall : 138 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,750.44 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 248 jetons, 12740 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 86, aerodrome 171, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1747.036684, 'cbBTC': 61757.075443, 'AERO': 0.420112}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 85,310,430 | 1,750.442873 | 59923934 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,172,488 | 0.028314 | 59923934 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,218,992 | 1,748.652630 | 59923934 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,661,780 | 0.028298 | 59923934 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,441,313 | 85.759766 | 59923934 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,011,301 | 0.000016 | 59923934 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,153,270 | 0.028307 | 59923934 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,593,070 | 2.383700 | 59923934 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,391,419 | 1,749.163964 | 59923934 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,255,796 | 0.998714 | 59923934 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,700,116 | 39,331.202161 | 59923934 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 115 | 2,292,161 | 1,749.014835 | 59923934 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,913,128 | 0.000016 | 59923934 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,707,354 | 0.028311 | 59923934 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,647,287 | 1,144,598.292141 | 59923934 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,461 | 0.844852 | 59923934 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,381,269 | 0.000016 | 59923934 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,324,819 | 0.000000 | 59923934 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,253,330 | 0.006488 | 59923934 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,239,182 | 0.000016 | 59923934 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,119,675 | 14.050207 | 59923934 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,937 | 86.492551 | 59923934 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,039,514 | 458.636669 | 59923934 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 999,082 | 85.738965 | 59923934 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 998,564 | 16,154.408345 | 59923934 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 993,085 | 4,185.065678 | 59923934 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 992,394 | 1,750.458525 | 59923934 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/doginme | 10000 | 906,961 | 32,215,148.144233 | 59923934 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/USDC | 3000 | 897,118 | 1,750.548871 | 59923934 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | USDC/VVV | 3000 | 891,871 | 0.049008 | 59923934 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/BRETT | 10000 | 818,503 | 524,916.856160 | 59923934 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 803,259 | 66.309297 | 59923934 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | DRB/WETH | 10000 | 788,908 | 0.000000 | 59923934 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 784,867 | 22,390,562.345203 | 59923934 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 778,306 | 0.001527 | 59923934 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 746,592 | 0.015582 | 59923934 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/MORPHO | 3000 | 726,227 | 1,094.704613 | 59923934 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 724,747 | 1,748.654193 | 59923934 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 721,826 | 0.046305 | 59923934 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 706,758 | 25.044582 | 59923934 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 695,017 | 1,744.307706 | 59923934 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 619,044 | 1,749.029945 | 59923934 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 594,460 | 0.798008 | 59923934 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 583,938 | 0.428810 | 59923934 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 557,497 | 4,691,015.913984 | 59923934 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 542,215 | 4,190.092648 | 59923934 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 509,794 | 530,208.866880 | 59923934 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,939 | 1.386531 | 59923934 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 496,669 | 0.031501 | 59923934 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 462,915 | 181,940.568698 | 59923934 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,605 | 1.001554 | 59923934 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 443,456 | 0.000007 | 59923934 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 419,658 | 0.058854 | 59923934 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3055 | 393,902 | 1,094.685459 | 59923934 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 384,717 | 23.772755 | 59923934 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 379,984 | 361.906950 | 59923934 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 379,925 | 851,906.574132 | 59923934 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 367,604 | 0.056191 | 59923934 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 360,485 | 0.000232 | 59923934 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/DEGEN | 3000 | 359,529 | 2,534,378.950723 | 59923934 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 10968 ; routes examinées : 139732320 ; candidats optimisés : 97517 ; net attendu > 0 : 3 ; dernier cycle 1247.5 ms
- Rejets (moteur) : {'spread_below_threshold': 137057477, 'liquidity_below_min': 1369736, 'negative_expected_net': 97514, 'cycle_budget_exhausted': 21427, 'borrow_bound_too_small': 11185}
- Enregistrements de la session : 26128 ; net attendu > 0 : 3 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 1/1 positives
- Décisions : {'REJECTED': 26128} ; motifs de rejet : {'below_safety_margin': 2, 'negative_expected_net': 26125, 'p_lower_below_threshold': 3, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59913838 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 12.932215 USDC | 0.009418 USDC | 0.000000 USDC | 0.003954 USDC | 0.005464 USDC (0.0050 €) | — | 4.23 | 0.077 (n=120) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 59913836 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 8.813621 USDC | 0.004349 USDC | 0.000000 USDC | 0.003954 USDC | 0.000395 USDC (0.0004 €) | — | 0.45 | 0.098 (n=128) | REJECTED | below_safety_margin(395<1762), p_lower_below_threshold(0.10<0.75) |
| 59913836 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 8.813621 USDC | 0.004349 USDC | 0.000000 USDC | 0.003954 USDC | 0.000395 USDC (0.0004 €) | — | 0.45 | 0.098 (n=128) | REJECTED | below_safety_margin(395<1762), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 8591 ; taux observé 0.228 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
