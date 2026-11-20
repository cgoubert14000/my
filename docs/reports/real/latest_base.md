# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T06:46:17+00:00 ; durée 128.42 min ; blocs 59795440 → 59833962 (5170 vus)

## Connexion
- Requêtes RPC : 59450 ; erreurs : 151 ; latence p50/p95 : 394.4/1,703.0 ms
- Rafraîchissements d'état : 5169 ; âge des données au dernier bloc : 8.68 s ; changements de frais LP observés (pools à frais dynamiques) : 4333
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2670 ; cycles déclenchés par événement : 816 ; avance médiane sur le rafraîchissement multicall : 353 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,739.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 424 pools, 248 jetons, 12898 routes
- Par DEX : uniswap_v3 128, aerodrome_slipstream 87, aerodrome 171, pancakeswap_v3 26, uniswap_v2 10, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 256, par paires 0), mesurés 426, sous le plancher de 10000.0 $ : 2 → gardés 424 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 1721.786092, 'cbBTC': 61363.951854, 'AERO': 0.407567}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 84,750,986 | 1,739.199717 | 59834001 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,066,812 | 0.028199 | 59834001 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 11,292,224 | 1,743.066433 | 59834001 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,629,989 | 0.028129 | 59834001 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,463,842 | 84.072460 | 59834001 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,992,151 | 0.000016 | 59834001 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,127,563 | 0.028210 | 59834001 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,561,234 | 2.426708 | 59834001 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,245,789 | 1,743.600444 | 59834001 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,243,788 | 1.000000 | 59834001 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,694,418 | 38,991.970516 | 59834001 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 262 | 2,279,465 | 1,743.344862 | 59834001 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,917,790 | 0.000016 | 59834001 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2535 | 1,697,641 | 0.028143 | 59834001 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,637,151 | 1,143,976.795593 | 59834001 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,718 | 0.844416 | 59834001 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,378,488 | 0.000016 | 59834001 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,325,528 | 0.000000 | 59834001 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,247,054 | 0.006498 | 59834001 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,237,102 | 0.000016 | 59834001 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,103,663 | 14.567979 | 59834001 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,984 | 86.485026 | 59834001 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,036,234 | 451.917815 | 59834001 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,001,020 | 16,056.860577 | 59834001 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 999,743 | 83.700562 | 59834001 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 989,233 | 1,739.199439 | 59834001 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 978,445 | 4,222.868119 | 59834001 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 955,299 | 1,743.458024 | 59834001 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 908,816 | 31,445,796.367457 | 59834001 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 899,744 | 0.048351 | 59834001 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 829,255 | 62.217036 | 59834001 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 813,082 | 525,211.601877 | 59834001 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 783,478 | 0.000000 | 59834001 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 783,040 | 22,232,898.536517 | 59834001 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 779,569 | 0.001539 | 59834001 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 745,330 | 0.015533 | 59834001 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/MORPHO | 3000 | 734,796 | 1,070.856509 | 59834001 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 721,108 | 1,742.950892 | 59834001 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 720,114 | 0.046083 | 59834001 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4645 | 717,333 | 24.530115 | 59834001 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 692,901 | 1,733.858085 | 59834001 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/USDC | 100 | 596,085 | 1,743.544365 | 59834001 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 590,553 | 0.798248 | 59834001 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 584,935 | 0.430231 | 59834001 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 556,710 | 4,643,866.098951 | 59834001 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 535,660 | 4,203.509344 | 59834001 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 508,942 | 1.386517 | 59834001 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3751 | 506,345 | 520,864.539214 | 59834001 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 492,107 | 0.031073 | 59834001 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 470,266 | 173,997.863612 | 59834001 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 8 | 456,691 | 1.001296 | 59834001 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 437,432 | 0.000007 | 59834001 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | ELSA/USDC | 100 | 411,835 | 0.057556 | 59834001 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3052 | 400,268 | 1,070.811052 | 59834001 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 383,085 | 23.661745 | 59834001 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 379,960 | 844,351.785711 | 59834001 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 378,655 | 360.455224 | 59834001 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 367,454 | 0.056145 | 59834001 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome | VIRTUAL/WETH | 10000 | 360,525 | 0.000235 | 59834001 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/DEGEN | 3000 | 358,689 | 2,564,129.261366 | 59834001 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 5982 ; routes examinées : 77155836 ; candidats optimisés : 133214 ; net attendu > 0 : 2 ; dernier cycle 1037.6 ms
- Rejets (moteur) : {'spread_below_threshold': 75402332, 'liquidity_below_min': 966360, 'negative_expected_net': 133212, 'borrow_bound_too_small': 6824, 'cycle_budget_exhausted': 1383}
- Enregistrements de la session : 86034 ; net attendu > 0 : 2 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 86034} ; motifs de rejet : {'below_safety_margin': 2, 'negative_expected_net': 86032, 'p_lower_below_threshold': 2, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59833710 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→WETH→[pancakeswap_v3]→USDC | 13.163118 USDC | 0.005133 USDC | 0.000000 USDC | 0.004999 USDC | 0.000134 USDC (0.0001 €) | — | 0.10 | 0.363 (n=155) | REJECTED | below_safety_margin(134<2632), stale_data(4766ms>4000.0), p_lower_below_threshold(0.36<0.75) |
| 59833710 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→WETH | 0.008856 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0001 €) | — | 0.04 | 0.363 (n=155) | REJECTED | below_safety_margin(39816642291<1771198889100), stale_data(4761ms>4000.0), p_lower_below_threshold(0.36<0.75) |

## Fiabilité et décision
- Observations ghost : 8590 ; taux observé 0.228 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
