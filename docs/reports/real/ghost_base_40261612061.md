# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T03:04:24+00:00 ; durée 3.06 min ; blocs 53097164 → 53097258 (91 vus)

## Connexion
- Requêtes RPC : 1174 ; erreurs : 0 ; latence p50/p95 : 77.9/1,456.8 ms
- Rafraîchissements d'état : 92 ; âge des données au dernier bloc : 1.64 s ; changements de frais LP observés (pools à frais dynamiques) : 247
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2339 ; cycles déclenchés par événement : 107 ; avance médiane sur le rafraîchissement multicall : 743 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,303.87 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 302 jetons, 19436 routes
- Par DEX : uniswap_v3 140, aerodrome 213, aerodrome_slipstream 125, pancakeswap_v3 31, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 337, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2299.668664, 'cbBTC': 79491.484, 'AERO': 0.669155}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,575,767 | 2,303.869526 | 53097258 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,241,030 | 0.029000 | 53097258 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,088,452 | 0.028978 | 53097258 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,430,111 | 0.000013 | 53097258 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,744,330 | 94.064425 | 53097258 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,286,188 | 2,309.275405 | 53097258 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,207,309 | 1.490666 | 53097258 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,944,404 | 0.001654 | 53097258 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 877 | 5,413,402 | 2,309.275843 | 53097258 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,277,679 | 0.029007 | 53097258 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,440,536 | 2,309.723138 | 53097258 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,172,093 | 1.000005 | 53097258 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,769,711 | 34,961.183713 | 53097258 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,748,954 | 2,303.904574 | 53097258 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,169,150 | 0.028961 | 53097258 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 2,521,444 | 0.000013 | 53097258 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2808 | 2,466,240 | 94.312966 | 53097258 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,180,695 | 410.588315 | 53097258 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,108,601 | 1,210,308.594714 | 53097258 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,884,241 | 0.000013 | 53097258 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,875,576 | 0.000000 | 53097258 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,780,806 | 0.017795 | 53097258 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 1,706,662 | 0.000013 | 53097258 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,704,473 | 0.000013 | 53097258 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,546,200 | 0.000265 | 53097258 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,242 | 0.826241 | 53097258 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53097258 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,413,375 | 0.005476 | 53097258 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,412,169 | 3,443.370423 | 53097258 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,351,757 | 14,180.431058 | 53097258 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,237,743 | 2,309.608177 | 53097258 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,234,496 | 3,445.900743 | 53097258 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,224,055 | 0.000267 | 53097258 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,221,037 | 65.175518 | 53097258 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,152,649 | 34,998,102.063033 | 53097258 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,147,430 | 0.000000 | 53097258 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,121,435 | 1,107,338.641946 | 53097258 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,106,023 | 496,118.627836 | 53097258 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,083,629 | 53.340587 | 53097258 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,059,102 | 72,514.571542 | 53097258 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,875 | 17.217252 | 53097258 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,005,742 | 21,983,711.415667 | 53097258 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 957,381 | 0.040822 | 53097258 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 919,378 | 2,317.752371 | 53097258 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 903,230 | 2.308285 | 53097258 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 889,494 | 1,141.001527 | 53097258 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 887,313 | 0.000556 | 53097258 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 872,568 | 17.133555 | 53097258 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 868,471 | 18.319507 | 53097258 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 861,670 | 93.418683 | 53097258 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 841,839 | 2,304.961384 | 53097258 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 791,235 | 0.000008 | 53097258 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,035 | 0.055916 | 53097258 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 780,056 | 0.803130 | 53097258 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 770,247 | 1.105951 | 53097258 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 738,001 | 0.613997 | 53097258 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,615 | 4,771,874.064065 | 53097258 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 707,451 | 0.629137 | 53097258 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 704,011 | 134,783.222420 | 53097258 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 688,945 | 497,024.677826 | 53097258 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 198 ; routes examinées : 3848328 ; candidats optimisés : 14959 ; net attendu > 0 : 14 ; dernier cycle 285.6 ms
- Rejets (moteur) : {'spread_below_threshold': 3776450, 'liquidity_below_min': 51969, 'negative_expected_net': 14945, 'unquotable': 4752, 'borrow_bound_too_small': 198}
- Enregistrements de la session : 14959 ; net attendu > 0 : 14 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 14959} ; motifs de rejet : {'below_safety_margin': 14, 'negative_expected_net': 14945, 'p_lower_below_threshold': 10, 'reliability_not_demonstrated': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53097171 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 112.631959 USDC | 0.007066 USDC | 0.000000 USDC | 0.005519 USDC | 0.001547 USDC (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(1547<22526), reliability_not_demonstrated |
| 53097171 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 112.631959 USDC | 0.007066 USDC | 0.000000 USDC | 0.005519 USDC | 0.001547 USDC (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(1547<22526), reliability_not_demonstrated |
| 53097171 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.049240 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(665141777599<9847954143486), reliability_not_demonstrated |
| 53097171 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.049240 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0014 €) | — | 0.14 | 0.018 (n=16) | REJECTED | below_safety_margin(665141777599<9847954143486), reliability_not_demonstrated |
| 53097171 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 101.201862 USDC | 0.005884 USDC | 0.000000 USDC | 0.005519 USDC | 0.000365 USDC (0.0003 €) | — | 0.04 | 0.022 (n=94) | REJECTED | below_safety_margin(365<20240), p_lower_below_threshold(0.02<0.75) |
| 53097171 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.044555 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.03 | 0.022 (n=94) | REJECTED | below_safety_margin(152235090017<8910902764057), p_lower_below_threshold(0.02<0.75) |
| 53097173 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.503979 USDC | 0.007228 USDC | 0.000000 USDC | 0.006955 USDC | 0.000273 USDC (0.0003 €) | — | 0.29 | 0.124 (n=340) | REJECTED | below_safety_margin(273<1900), p_lower_below_threshold(0.12<0.75) |
| 53097174 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 9.503979 USDC | 0.007228 USDC | 0.000000 USDC | 0.006955 USDC | 0.000273 USDC (0.0003 €) | — | 0.29 | 0.124 (n=340) | REJECTED | below_safety_margin(273<1900), p_lower_below_threshold(0.12<0.75) |
| 53097173 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004156 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.26 | 0.124 (n=340) | REJECTED | below_safety_margin(109733476668<831208414576), p_lower_below_threshold(0.12<0.75) |
| 53097174 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004156 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.26 | 0.124 (n=340) | REJECTED | below_safety_margin(109733476668<831208414576), p_lower_below_threshold(0.12<0.75) |
| 53097173 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.454353 USDC | 0.007113 USDC | 0.000000 USDC | 0.006955 USDC | 0.000158 USDC (0.0001 €) | — | 0.17 | 0.180 (n=175) | REJECTED | below_safety_margin(158<1890), p_lower_below_threshold(0.18<0.75) |
| 53097174 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.454353 USDC | 0.007113 USDC | 0.000000 USDC | 0.006955 USDC | 0.000158 USDC (0.0001 €) | — | 0.17 | 0.180 (n=175) | REJECTED | below_safety_margin(158<1890), p_lower_below_threshold(0.18<0.75) |
| 53097173 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004084 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.15 | 0.180 (n=175) | REJECTED | below_safety_margin(60260813131<816886174227), p_lower_below_threshold(0.18<0.75) |
| 53097174 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004084 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.15 | 0.180 (n=175) | REJECTED | below_safety_margin(60260813131<816886174227), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 2588 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
