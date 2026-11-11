# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T23:47:12+00:00 ; durée 3.01 min ; blocs 56251356 → 56252250 (192 vus)

## Connexion
- Requêtes RPC : 2368 ; erreurs : 0 ; latence p50/p95 : 153.1/1,286.1 ms
- Rafraîchissements d'état : 192 ; âge des données au dernier bloc : 7.78 s ; changements de frais LP observés (pools à frais dynamiques) : 114
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 254 ; cycles déclenchés par événement : 88 ; avance médiane sur le rafraîchissement multicall : 449 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,049.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 458 pools, 265 jetons, 15592 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 281, par paires 0), mesurés 460, sous le plancher de 10000.0 $ : 2 → gardés 458 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2049.11291, 'cbBTC': 73781.879924, 'AERO': 0.537258}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,209,233 | 2,049.112910 | 56252272 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,411,205 | 0.027771 | 56252272 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,606,961 | 0.027789 | 56252272 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,521,238 | 0.000014 | 56252272 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,082,664 | 2,049.906747 | 56252272 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,837,931 | 104.628851 | 56252272 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,578,421 | 0.027768 | 56252272 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,229,376 | 1.859857 | 56252272 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,011,814 | 2,049.685179 | 56252272 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,887,859 | 0.998581 | 56252272 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,026,301 | 42,906.046872 | 56252272 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,888,565 | 2,049.657324 | 56252272 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,200,710 | 0.027775 | 56252272 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,946,791 | 1,123,024.323907 | 56252272 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,648,357 | 0.000014 | 56252272 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,616,666 | 0.016305 | 56252272 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,607,053 | 0.000014 | 56252272 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,568,457 | 0.000000 | 56252272 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,533,964 | 0.006692 | 56252272 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,530,889 | 0.000014 | 56252272 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,473 | 0.830438 | 56252272 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56252272 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,404,123 | 428.956244 | 56252272 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,269,362 | 2,048.612979 | 56252272 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,252,999 | 3,814.230317 | 56252272 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,215,491 | 15,417.060243 | 56252272 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,155,524 | 2,050.241156 | 56252272 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,125,086 | 2,049.739543 | 56252272 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56252272 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,039,836 | 33,556,884.209672 | 56252272 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,015,052 | 104.619523 | 56252272 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,323 | 21.367349 | 56252272 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 933,739 | 567,211.113272 | 56252272 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 911,893 | 0.001471 | 56252272 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 902,824 | 0.000014 | 56252272 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 895,477 | 0.051068 | 56252272 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 891,759 | 23,469,322.299545 | 56252272 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 877,721 | 2,054.856011 | 56252272 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 872,220 | 1,032.124716 | 56252272 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 860,472 | 0.000000 | 56252272 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 780,780 | 77.157019 | 56252272 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 763,445 | 0.052000 | 56252272 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 745,574 | 23.098556 | 56252272 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 745,384 | 115,217.236770 | 56252272 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 703,017 | 3,786.866427 | 56252272 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 694,242 | 0.801801 | 56252272 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 665,728 | 0.526036 | 56252272 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 647,753 | 4,744,656.615251 | 56252272 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 619,477 | 0.482845 | 56252272 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 598,217 | 148,687.990375 | 56252272 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 583,516 | 0.000007 | 56252272 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 574,551 | 0.000257 | 56252272 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 571,819 | 567,350.432190 | 56252272 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,306 | 0.037344 | 56252272 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 486,759 | 1,032.323882 | 56252272 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,696 | 0.066926 | 56252272 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,822 | 1.000954 | 56252272 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 450,956 | 0.502364 | 56252272 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 440,207 | 901,092.523948 | 56252272 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,716 | 24.790032 | 56252272 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 279 ; routes examinées : 4350168 ; candidats optimisés : 17641 ; net attendu > 0 : 14 ; dernier cycle 124.5 ms
- Rejets (moteur) : {'spread_below_threshold': 4263559, 'liquidity_below_min': 68598, 'negative_expected_net': 17627, 'borrow_bound_too_small': 276, 'cycle_budget_exhausted': 94}
- Enregistrements de la session : 17641 ; net attendu > 0 : 14 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 17641} ; motifs de rejet : {'below_safety_margin': 14, 'negative_expected_net': 17627, 'p_lower_below_threshold': 14}

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
