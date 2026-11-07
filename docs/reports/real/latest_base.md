# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T08:11:19+00:00 ; durée 42.79 min ; blocs 54230643 → 54243465 (1999 vus)

## Connexion
- Requêtes RPC : 26666 ; erreurs : 88 ; latence p50/p95 : 576.0/1,952.2 ms
- Rafraîchissements d'état : 1999 ; âge des données au dernier bloc : 10.52 s ; changements de frais LP observés (pools à frais dynamiques) : 574
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1436 ; cycles déclenchés par événement : 660 ; avance médiane sur le rafraîchissement multicall : 471 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,241.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 476 pools, 279 jetons, 17784 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 99, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 295, par paires 0), mesurés 479, sous le plancher de 10000.0 $ : 3 → gardés 476 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2241.234025, 'cbBTC': 75952.6335, 'AERO': 0.608777}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,985,454 | 2,241.234355 | 54243495 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,804,766 | 0.029518 | 54243495 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,329,097 | 0.000013 | 54243495 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,174,394 | 0.029513 | 54243495 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,021,658 | 2,244.945340 | 54243495 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,418,861 | 106.652068 | 54243495 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,429,229 | 0.001552 | 54243495 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,886,436 | 1.643907 | 54243495 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,769,521 | 0.029525 | 54243495 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,228,160 | 2,244.851162 | 54243495 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,001,822 | 0.998507 | 54243495 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,316,066 | 42,750.713390 | 54243495 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,121 | 2,244.903100 | 54243495 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,562,430 | 0.029528 | 54243495 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,098,061 | 1,156,736.421986 | 54243495 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,742,800 | 0.000013 | 54243495 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,705,735 | 0.006780 | 54243495 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,660,210 | 0.000000 | 54243495 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,634,993 | 0.000013 | 54243495 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,616,971 | 0.016135 | 54243495 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54243495 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,532,116 | 434.932980 | 54243495 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,477 | 0.000013 | 54243495 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,378 | 0.819350 | 54243495 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,391,382 | 3,686.083921 | 54243495 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,727 | 2,245.848726 | 54243495 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,171 | 2,238.185861 | 54243495 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,275,417 | 14,712.204869 | 54243495 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,192,701 | 2,244.659529 | 54243495 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54243495 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,750 | 35,925,909.624487 | 54243495 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,054,423 | 107.127653 | 54243495 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,027,483 | 557,553.955869 | 54243495 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,001,355 | 0.000000 | 54243495 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,655 | 22,522,526.287595 | 54243495 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 985,805 | 19.765844 | 54243495 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 942,028 | 1,058.499964 | 54243495 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 937,846 | 2,228.788739 | 54243495 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 927,037 | 0.000013 | 54243495 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 915,707 | 74.730041 | 54243495 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 881,680 | 98,571.507697 | 54243495 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 815,488 | 0.047517 | 54243495 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 801,371 | 3,680.501020 | 54243495 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 799,816 | 20.898177 | 54243495 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,860 | 0.056122 | 54243495 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,330 | 0.799699 | 54243495 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 720,866 | 0.570068 | 54243495 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 697,515 | 4,885,967.803220 | 54243495 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,335 | 0.000253 | 54243495 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 671,668 | 0.565228 | 54243495 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 660,661 | 145,479.938352 | 54243495 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 657,342 | 0.000008 | 54243495 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 630,657 | 559,413.389566 | 54243495 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 588,883 | 2.473403 | 54243495 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 580,186 | 0.040061 | 54243495 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 529,249 | 1,058.134776 | 54243495 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 526,107 | 0.078883 | 54243495 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 523,812 | 895,564.580693 | 54243495 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 515,817 | 2,244.836810 | 54243495 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 514,479 | 6,959.444540 | 54243495 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 2658 ; routes examinées : 47269872 ; candidats optimisés : 100205 ; net attendu > 0 : 3 ; dernier cycle 81.5 ms
- Rejets (moteur) : {'spread_below_threshold': 46747380, 'liquidity_below_min': 419558, 'negative_expected_net': 100202, 'borrow_bound_too_small': 2656, 'cycle_budget_exhausted': 73}
- Enregistrements de la session : 100205 ; net attendu > 0 : 3 ; simulés (eth_call de la vraie tx) : 3 (ok 2, échec 1) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 100205} ; motifs de rejet : {'negative_expected_net': 100202, 'p_lower_below_threshold': 3, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | 0.009649 USDC | 4.10 | 0.025 (n=328) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | — | 4.10 | 0.025 (n=328) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54238043 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 18.092171 USDC | 0.008744 USDC | 0.000000 USDC | 0.005033 USDC | 0.003711 USDC (0.0034 €) | 0.003711 USDC | 2.05 | 0.046 (n=254) | REJECTED | p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5957 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
