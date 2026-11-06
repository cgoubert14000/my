# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T09:11:58+00:00 ; durée 36.57 min ; blocs 53818717 → 53829678 (1616 vus)

## Connexion
- Requêtes RPC : 26007 ; erreurs : 0 ; latence p50/p95 : 301.8/1,115.5 ms
- Rafraîchissements d'état : 1616 ; âge des données au dernier bloc : 7.05 s ; changements de frais LP observés (pools à frais dynamiques) : 1296
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1138 ; cycles déclenchés par événement : 558 ; avance médiane sur le rafraîchissement multicall : 544 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,232.31 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 281 jetons, 17914 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 103, aerodrome 201, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3751 (énumérés 303, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.035754, 'cbBTC': 75513.528915, 'AERO': 0.590274}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,816,690 | 2,232.311659 | 53829700 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,614,317 | 0.029448 | 53829700 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,244,353 | 0.000013 | 53829700 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,115,526 | 0.029418 | 53829700 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,988,214 | 2,236.987211 | 53829700 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,365,355 | 107.347371 | 53829700 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,415,309 | 0.001550 | 53829700 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,044,737 | 1.684292 | 53829700 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,696,293 | 0.029460 | 53829700 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,115,906 | 2,237.215616 | 53829700 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,995,912 | 0.998447 | 53829700 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,300,284 | 42,817.581001 | 53829700 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,201,318 | 2,237.263374 | 53829700 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,553,756 | 0.029434 | 53829700 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,075,895 | 1,172,181.068675 | 53829700 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,795,056 | 0.007310 | 53829700 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,736,236 | 0.000013 | 53829700 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,651,760 | 0.000013 | 53829700 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,644,377 | 0.016550 | 53829700 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,637,607 | 0.000000 | 53829700 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53829700 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,530,464 | 0.000013 | 53829700 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,521,184 | 439.103374 | 53829700 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,908 | 0.818149 | 53829700 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,366,771 | 3,766.292801 | 53829700 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,985 | 2,232.032637 | 53829700 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,322,501 | 2,232.291523 | 53829700 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,266,324 | 14,906.219887 | 53829700 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,170,442 | 2,236.870248 | 53829700 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,888 | 76.929483 | 53829700 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,092,638 | 37,371,614.316905 | 53829700 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,042,641 | 107.774218 | 53829700 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,019,791 | 563,513.421758 | 53829700 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,006,859 | 0.000000 | 53829700 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 999,021 | 22,582,648.446445 | 53829700 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 983,201 | 19.904823 | 53829700 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 934,985 | 2,225.328831 | 53829700 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,198 | 1,069.107214 | 53829700 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 926,318 | 73.074456 | 53829700 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 924,212 | 0.000013 | 53829700 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 865,147 | 101,560.960753 | 53829700 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 839,762 | 0.000531 | 53829700 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 811,315 | 20.471678 | 53829700 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 807,825 | 0.047994 | 53829700 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 790,151 | 3,786.756709 | 53829700 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,250 | 0.055146 | 53829700 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 757,303 | 0.799699 | 53829700 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 719,252 | 0.572136 | 53829700 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 691,657 | 4,928,923.110440 | 53829700 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 684,664 | 0.000255 | 53829700 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 658,702 | 145,173.180619 | 53829700 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 655,245 | 0.539393 | 53829700 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 647,024 | 0.000008 | 53829700 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 624,601 | 561,143.505411 | 53829700 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 598,448 | 0.914286 | 53829700 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 598,368 | 2.462288 | 53829700 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,598 | 0.038059 | 53829700 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 530,316 | 0.079858 | 53829700 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 525,676 | 879,922.476135 | 53829700 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 525,079 | 2,237.130584 | 53829700 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 2173 ; routes examinées : 38927122 ; candidats optimisés : 111074 ; net attendu > 0 : 8 ; dernier cycle 85.9 ms
- Rejets (moteur) : {'spread_below_threshold': 38347026, 'liquidity_below_min': 466849, 'negative_expected_net': 111066, 'borrow_bound_too_small': 2173}
- Enregistrements de la session : 111074 ; net attendu > 0 : 8 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 111074} ; motifs de rejet : {'below_safety_margin': 6, 'negative_expected_net': 111066, 'p_lower_below_threshold': 8, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53823058 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.007869 USDC | 0.030104 USDC | 0.000000 USDC | 0.005012 USDC | 0.025092 USDC (0.0231 €) | 0.025092 USDC | 5.12 | 0.028 (n=300) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53823641 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 47.715028 USDC | 0.028656 USDC | 0.000000 USDC | 0.005013 USDC | 0.023643 USDC (0.0218 €) | — | 4.96 | 0.028 (n=301) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53822585 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.473769 USDC | 0.009535 USDC | 0.000000 USDC | 0.005012 USDC | 0.004523 USDC (0.0042 €) | — | 1.65 | 0.046 (n=234) | REJECTED | below_safety_margin(4523<5494), p_lower_below_threshold(0.05<0.75) |
| 53822586 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.473769 USDC | 0.009535 USDC | 0.000000 USDC | 0.005012 USDC | 0.004523 USDC (0.0042 €) | — | 1.65 | 0.046 (n=234) | REJECTED | below_safety_margin(4523<5494), p_lower_below_threshold(0.05<0.75) |
| 53828342 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 209.478301 USDC | 0.009147 USDC | 0.000000 USDC | 0.005030 USDC | 0.004117 USDC (0.0038 €) | — | 0.20 | 0.046 (n=234) | REJECTED | below_safety_margin(4117<41895), p_lower_below_threshold(0.05<0.75) |
| 53828342 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.094008 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0038 €) | — | 0.20 | 0.046 (n=234) | REJECTED | below_safety_margin(1835791606212<18801667074057), p_lower_below_threshold(0.05<0.75) |
| 53828894 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 30.937696 USDC | 0.005573 USDC | 0.000000 USDC | 0.005026 USDC | 0.000547 USDC (0.0005 €) | — | 0.18 | 0.054 (n=80) | REJECTED | below_safety_margin(547<6187), p_lower_below_threshold(0.05<0.75) |
| 53828894 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.013950 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0005 €) | — | 0.17 | 0.054 (n=80) | REJECTED | below_safety_margin(239182194707<2790097583785), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5803 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
