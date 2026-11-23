# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-23T22:09:44+00:00 ; durée 270.61 min ; blocs 61325834 → 61407027 (22387 vus)

## Connexion
- Requêtes RPC : 192967 ; erreurs : 1168 ; latence p50/p95 : 314.9/951.2 ms
- Rafraîchissements d'état : 22387 ; âge des données au dernier bloc : 3.25 s ; changements de frais LP observés (pools à frais dynamiques) : 11195
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 29833 ; cycles déclenchés par événement : 11706 ; avance médiane sur le rafraîchissement multicall : 281 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,717.86 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 424 pools, 251 jetons, 12372 routes
- Par DEX : uniswap_v3 126, aerodrome 171, aerodrome_slipstream 88, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 149 (rejetés 2) → 554 jetons ; pools candidats 3613 (énumérés 257, par paires 0), mesurés 426, sous le plancher de 10000.0 $ : 2 → gardés 424 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1756.440053, 'cbBTC': 61695.292891, 'AERO': 0.426312}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 82,962,031 | 1,717.855097 | 61407027 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 22,289,927 | 0.028098 | 61407027 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 9,897,054 | 1,718.984493 | 61407027 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,658,536 | 0.028121 | 61407027 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,954,883 | 70.581173 | 61407027 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,067,718 | 0.000016 | 61407027 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,009,221 | 0.028090 | 61407027 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,338,967 | 2.407429 | 61407027 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,218,216 | 0.998947 | 61407027 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,070,898 | 1,719.243176 | 61407027 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,639,465 | 39,640.870371 | 61407027 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 154 | 2,226,531 | 1,719.195729 | 61407027 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,908,676 | 0.028108 | 61407027 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,867,483 | 0.000016 | 61407027 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 1,660,058 | 1,085,481.277480 | 61407027 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,701 | 0.843334 | 61407027 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,308,527 | 0.000000 | 61407027 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,277,961 | 0.000016 | 61407027 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,169,051 | 12.652669 | 61407027 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,160,432 | 0.006095 | 61407027 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,136,500 | 0.000016 | 61407027 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/SEND | 3000 | 1,060,664 | 86.374145 | 61407027 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | USDC/VVV | 3000 | 1,022,403 | 0.041028 | 61407027 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 1,020,796 | 70.336659 | 61407027 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,018,461 | 463.467389 | 61407027 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 983,956 | 1,717.661720 | 61407027 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 980,146 | 16,475.455444 | 61407027 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 980,095 | 4,140.042316 | 61407027 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 889,775 | 32,259,842.600716 | 61407027 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 885,659 | 0.000000 | 61407027 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 833,622 | 61.566928 | 61407027 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 795,233 | 539,912.293770 | 61407027 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 789,844 | 21,482,592.617028 | 61407027 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 774,913 | 0.001547 | 61407027 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 727,213 | 0.014786 | 61407027 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 707,883 | 0.044522 | 61407027 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 707,490 | 1,071.223564 | 61407027 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/USDC | 3000 | 702,410 | 1,721.259396 | 61407027 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 701,105 | 25.547564 | 61407027 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | uXRP/WETH | 3000 | 686,004 | 0.000606 | 61407027 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | WETH/USDC | 500 | 617,650 | 1,718.962773 | 61407027 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | ELSA/USDC | 100 | 611,751 | 0.100568 | 61407027 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | TIG/USDC | 10000 | 587,493 | 0.432725 | 61407027 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 583,415 | 0.797948 | 61407027 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 565,950 | 1,719.264489 | 61407027 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 559,347 | 4,500,041.811572 | 61407027 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 532,446 | 4,132.394330 | 61407027 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 499,880 | 0.030488 | 61407027 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 493,838 | 154,703.983987 | 61407027 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 4049 | 493,624 | 541,686.038413 | 61407027 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | WETH/USDC | 10000 | 467,797 | 1,727.996037 | 61407027 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 8 | 459,648 | 1.001395 | 61407027 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 440,842 | 0.000007 | 61407027 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 438,932 | 1.446787 | 61407027 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 3277 | 397,609 | 1,071.035451 | 61407027 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 390,010 | 21.519326 | 61407027 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 381,166 | 354.661835 | 61407027 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 377,339 | 845,900.402322 | 61407027 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/VVV | 2727 | 363,421 | 70.565967 | 61407027 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | WETH/DEGEN | 3000 | 362,868 | 2,384,266.774173 | 61407027 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 34092 ; routes examinées : 421786224 ; candidats optimisés : 52460 ; net attendu > 0 : 0 ; dernier cycle 1439.2 ms
- Rejets (moteur) : {'spread_below_threshold': 414053957, 'liquidity_below_min': 4422948, 'negative_expected_net': 52460, 'borrow_bound_too_small': 38239, 'cycle_budget_exhausted': 321}
- Enregistrements de la session : 20 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 20} ; motifs de rejet : {'negative_expected_net': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 61356438 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -30.83 |
| 61356438 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -30.83 |
| 61356438 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -30.83 |
| 61337106 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.92 |
| 61356438 | cbBTC→[aerodrome]→tBTC→[aerodrome]→WETH→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0085 | -92.48 |
| 61345499 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.011588 USDC | 0.000000 USDC | 0.005542 USDC | -0.0158 | -171.30 |
| 61337106 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.013983 USDC | 0.000000 USDC | 0.005553 USDC | -0.0180 | -195.36 |
| 61337106 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.013983 USDC | 0.000000 USDC | 0.005553 USDC | -0.0180 | -195.36 |
| 61337106 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0181 | -196.92 |
| 61337106 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0181 | -196.92 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
