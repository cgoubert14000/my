# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T23:53:19+00:00 ; durée 9.12 min ; blocs 56251356 → 56254071 (533 vus)

## Connexion
- Requêtes RPC : 6646 ; erreurs : 0 ; latence p50/p95 : 186.8/1,312.6 ms
- Rafraîchissements d'état : 533 ; âge des données au dernier bloc : 9.98 s ; changements de frais LP observés (pools à frais dynamiques) : 329
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 612 ; cycles déclenchés par événement : 236 ; avance médiane sur le rafraîchissement multicall : 466 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,050.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 458 pools, 265 jetons, 15592 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 281, par paires 0), mesurés 460, sous le plancher de 10000.0 $ : 2 → gardés 458 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2049.11291, 'cbBTC': 73781.879924, 'AERO': 0.537258}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,271,397 | 2,050.458533 | 56254097 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,420,263 | 0.027790 | 56254097 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,611,373 | 0.027789 | 56254097 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,521,249 | 0.000014 | 56254097 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,086,557 | 2,055.383488 | 56254097 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,842,558 | 104.624666 | 56254097 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,581,018 | 0.027790 | 56254097 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,232,800 | 1.856849 | 56254097 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,013,924 | 2,055.531639 | 56254097 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,887,800 | 0.998581 | 56254097 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,028,288 | 42,906.046872 | 56254097 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 224 | 2,890,226 | 2,055.398145 | 56254097 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,201,958 | 0.027775 | 56254097 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,948,069 | 1,123,024.323907 | 56254097 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 1,648,347 | 0.000014 | 56254097 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,618,148 | 0.016327 | 56254097 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,607,059 | 0.000014 | 56254097 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,568,641 | 0.000000 | 56254097 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,539,102 | 0.006693 | 56254097 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,530,893 | 0.000014 | 56254097 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,473 | 0.830438 | 56254097 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56254097 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,405,045 | 428.956244 | 56254097 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,269,779 | 2,049.949323 | 56254097 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,254,592 | 3,814.230317 | 56254097 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,215,834 | 15,417.060243 | 56254097 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,155,904 | 2,050.834243 | 56254097 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,125,632 | 2,055.427985 | 56254097 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56254097 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,040,425 | 33,565,775.327902 | 56254097 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,015,743 | 104.619525 | 56254097 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,433 | 21.359816 | 56254097 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 934,352 | 567,212.196347 | 56254097 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 912,154 | 0.001472 | 56254097 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 902,821 | 0.000014 | 56254097 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 895,995 | 0.050982 | 56254097 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 892,969 | 23,441,832.010363 | 56254097 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 877,971 | 2,054.856011 | 56254097 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 872,793 | 1,032.124716 | 56254097 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 857,235 | 0.000000 | 56254097 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 781,010 | 77.111415 | 56254097 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 763,641 | 0.052077 | 56254097 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4575 | 746,657 | 23.052273 | 56254097 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 745,200 | 115,425.871186 | 56254097 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 703,816 | 3,786.866427 | 56254097 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 694,698 | 0.801801 | 56254097 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 666,105 | 0.526504 | 56254097 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 648,178 | 4,744,656.615251 | 56254097 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 618,918 | 0.482007 | 56254097 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 598,610 | 148,687.990375 | 56254097 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 584,164 | 0.000007 | 56254097 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 574,929 | 0.000257 | 56254097 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 572,194 | 567,670.004864 | 56254097 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,427 | 0.037357 | 56254097 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 487,079 | 1,032.323882 | 56254097 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 465,890 | 0.067145 | 56254097 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,830 | 1.000920 | 56254097 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 451,172 | 0.502364 | 56254097 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 440,238 | 901,092.523948 | 56254097 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,953 | 24.796078 | 56254097 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 768 ; routes examinées : 11974656 ; candidats optimisés : 56202 ; net attendu > 0 : 14 ; dernier cycle 246.9 ms
- Rejets (moteur) : {'spread_below_threshold': 11724123, 'liquidity_below_min': 193305, 'negative_expected_net': 56188, 'borrow_bound_too_small': 758, 'cycle_budget_exhausted': 268}
- Enregistrements de la session : 56202 ; net attendu > 0 : 14 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 56202} ; motifs de rejet : {'below_safety_margin': 14, 'negative_expected_net': 56188, 'p_lower_below_threshold': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56252219 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252220 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56252219 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252220 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56251546 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 138.957744 USDC | 0.004948 USDC | 0.000000 USDC | 0.004615 USDC | 0.000333 USDC (0.0003 €) | — | 0.02 | 0.103 (n=364) | REJECTED | below_safety_margin(333<27791), p_lower_below_threshold(0.10<0.75) |
| 56251546 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.068503 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.02 | 0.103 (n=364) | REJECTED | below_safety_margin(160772408236<13700566209003), p_lower_below_threshold(0.10<0.75) |
| 56252054 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.052724 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.03 | 0.103 (n=364) | REJECTED | below_safety_margin(139256400774<10544753384408), p_lower_below_threshold(0.10<0.75) |
| 56252055 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.052724 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0003 €) | — | 0.03 | 0.103 (n=364) | REJECTED | below_safety_margin(139256400774<10544753384408), p_lower_below_threshold(0.10<0.75) |
| 56252054 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 106.027968 USDC | 0.004891 USDC | 0.000000 USDC | 0.004606 USDC | 0.000285 USDC (0.0003 €) | — | 0.03 | 0.103 (n=364) | REJECTED | below_safety_margin(285<21205), p_lower_below_threshold(0.10<0.75) |
| 56252055 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 106.027968 USDC | 0.004891 USDC | 0.000000 USDC | 0.004606 USDC | 0.000285 USDC (0.0003 €) | — | 0.03 | 0.103 (n=364) | REJECTED | below_safety_margin(285<21205), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 8234 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
