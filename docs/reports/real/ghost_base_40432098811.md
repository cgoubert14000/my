# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T01:46:08+00:00 ; durée 18.37 min ; blocs 53137556 → 53138107 (538 vus)

## Connexion
- Requêtes RPC : 6816 ; erreurs : 0 ; latence p50/p95 : 381.9/1,515.5 ms
- Rafraîchissements d'état : 538 ; âge des données au dernier bloc : 7.43 s ; changements de frais LP observés (pools à frais dynamiques) : 1049
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7719 ; cycles déclenchés par événement : 478 ; avance médiane sur le rafraîchissement multicall : 852 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,323.63 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,423,894 | 2,323.630467 | 53138107 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,116,538 | 0.029023 | 53138107 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,128,658 | 0.028948 | 53138107 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,461,697 | 0.000012 | 53138107 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,661,899 | 92.761298 | 53138107 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,345,452 | 2,326.470105 | 53138107 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,020,064 | 1.483414 | 53138107 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,972,756 | 0.001642 | 53138107 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,383,563 | 0.029012 | 53138107 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,256,593 | 2,325.733167 | 53138107 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,553,391 | 2,325.871188 | 53138107 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,213,777 | 0.999452 | 53138107 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,779,953 | 35,371.035999 | 53138107 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,364,843 | 2,323.893240 | 53138107 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,190,639 | 0.028965 | 53138107 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,508,356 | 92.743890 | 53138107 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 2,450,145 | 0.000012 | 53138107 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,121,372 | 1,216,380.983500 | 53138107 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,835,817 | 0.000000 | 53138107 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,833,621 | 0.018754 | 53138107 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,763,093 | 404.068812 | 53138107 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,689,114 | 0.000012 | 53138107 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,039 | 0.000012 | 53138107 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,665,084 | 0.000012 | 53138107 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,555,875 | 0.000266 | 53138107 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,923 | 0.005881 | 53138107 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,925 | 0.826518 | 53138107 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53138107 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,991 | 3,442.911596 | 53138107 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,371,531 | 13,942.913046 | 53138107 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,800 | 2,326.467593 | 53138107 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,905 | 0.000266 | 53138107 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53138107 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,207,778 | 3,444.389703 | 53138107 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,148,109 | 0.000000 | 53138107 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,142,098 | 36,863,515.097092 | 53138107 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,139,495 | 1,090,993.540534 | 53138107 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,109,007 | 498,026.006105 | 53138107 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,070,714 | 72,167.979998 | 53138107 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,048,671 | 20,816,565.176003 | 53138107 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,039,242 | 57.961296 | 53138107 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,032,022 | 17.348216 | 53138107 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,002,849 | 0.039821 | 53138107 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 952,473 | 2,317.651270 | 53138107 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,538 | 1,080.856537 | 53138107 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 908,295 | 2.309154 | 53138107 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 896,295 | 0.000558 | 53138107 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 879,695 | 17.950891 | 53138107 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,455 | 92.391232 | 53138107 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 859,977 | 17.193154 | 53138107 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 845,524 | 2,323.754052 | 53138107 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,997 | 0.056954 | 53138107 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 796,588 | 0.000008 | 53138107 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 786,723 | 0.803179 | 53138107 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,533 | 0.618070 | 53138107 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 734,892 | 4,719,909.600110 | 53138107 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,673 | 138,415.538833 | 53138107 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 699,631 | 0.615511 | 53138107 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 693,174 | 502,013.800513 | 53138107 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 674,418 | 0.108921 | 53138107 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 1015 ; routes examinées : 19737690 ; candidats optimisés : 54027 ; net attendu > 0 : 7 ; dernier cycle 418.9 ms
- Rejets (moteur) : {'spread_below_threshold': 19393075, 'liquidity_below_min': 269273, 'negative_expected_net': 54020, 'unquotable': 20300, 'borrow_bound_too_small': 1015}
- Enregistrements de la session : 54027 ; net attendu > 0 : 7 ; simulés (eth_call de la vraie tx) : 1 (ok 0, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 54027} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 54020, 'p_lower_below_threshold': 5, 'reliability_not_demonstrated': 2, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53137626 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 34.617125 USDC | 0.017962 USDC | 0.000000 USDC | 0.005214 USDC | 0.012748 USDC (0.0117 €) | — | 3.68 | 0.002 (n=144) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53137930 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 7.365096 USDC | 0.005432 USDC | 0.000000 USDC | 0.005246 USDC | 0.000186 USDC (0.0002 €) | — | 0.25 | 0.001 (n=13) | REJECTED | below_safety_margin(186<1473), reliability_not_demonstrated |
| 53137930 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 7.365096 USDC | 0.005432 USDC | 0.000000 USDC | 0.005246 USDC | 0.000186 USDC (0.0002 €) | — | 0.25 | 0.001 (n=13) | REJECTED | below_safety_margin(186<1473), reliability_not_demonstrated |
| 53137676 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.131309 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(68032203442<26261817804490), p_lower_below_threshold(0.02<0.75) |
| 53137677 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.131309 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(68032203442<26261817804490), p_lower_below_threshold(0.02<0.75) |
| 53137676 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 302.799137 USDC | 0.005371 USDC | 0.000000 USDC | 0.005214 USDC | 0.000157 USDC (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(157<60559), p_lower_below_threshold(0.02<0.75) |
| 53137677 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 302.799137 USDC | 0.005371 USDC | 0.000000 USDC | 0.005214 USDC | 0.000157 USDC (0.0001 €) | — | 0.01 | 0.021 (n=102) | REJECTED | below_safety_margin(157<60559), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 2776 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
