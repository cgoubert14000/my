# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-28T00:01:04+00:00 ; durée 296.48 min ; blocs 63079463 → 63168402 (17084 vus)

## Connexion
- Requêtes RPC : 161649 ; erreurs : 150 ; latence p50/p95 : 400.1/1,732.4 ms
- Rafraîchissements d'état : 17084 ; âge des données au dernier bloc : 8.03 s ; changements de frais LP observés (pools à frais dynamiques) : 5218
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 14933 ; cycles déclenchés par événement : 6945 ; avance médiane sur le rafraîchissement multicall : 285 ms
- Gaz : base fee 0.005005 gwei ; prix ETH (pool le plus profond) : 1,658.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 425 pools, 249 jetons, 12996 routes
- Par DEX : uniswap_v3 129, aerodrome 169, aerodrome_slipstream 90, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 145 (rejetés 2) → 550 jetons ; pools candidats 3591 (énumérés 257, par paires 0), mesurés 427, sous le plancher de 10000.0 $ : 2 → gardés 425 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 1667.890547, 'cbBTC': 59929.44067, 'AERO': 0.391629}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 94,806,741 | 1,658.228840 | 63168426 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 28,014,341 | 0.027747 | 63168426 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,310,318 | 0.027792 | 63168426 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,024,432 | 64.381312 | 63168426 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 6,990,728 | 1,662.427277 | 63168426 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,125,607 | 0.000017 | 63168426 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,988,476 | 0.027759 | 63168426 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,162,381 | 2.568151 | 63168426 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,145,900 | 0.999356 | 63168426 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,938,270 | 1,663.175083 | 63168426 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,478,484 | 41,890.802258 | 63168426 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 185 | 2,131,596 | 1,662.964156 | 63168426 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,950,416 | 0.000017 | 63168426 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,818,519 | 0.027779 | 63168426 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,559,719 | 1,145,756.646864 | 63168426 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,891 | 0.835270 | 63168426 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,369,922 | 8.889117 | 63168426 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,267,602 | 0.000000 | 63168426 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,255,636 | 0.000017 | 63168426 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,162,603 | 0.006308 | 63168426 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,111,611 | 0.000017 | 63168426 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/VVV | 3000 | 1,093,796 | 0.038754 | 63168426 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/SEND | 3000 | 1,060,785 | 86.354468 | 63168426 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/VVV | 10000 | 1,017,720 | 64.745495 | 63168426 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 991,628 | 447.167562 | 63168426 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 969,229 | 16,143.432550 | 63168426 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 967,369 | 1,658.425436 | 63168426 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 923,605 | 4,266.443581 | 63168426 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 870,001 | 31,040,782.919024 | 63168426 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 812,909 | 0.000000 | 63168426 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 776,950 | 20,699,274.984516 | 63168426 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 776,180 | 71.016818 | 63168426 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 768,507 | 537,769.550965 | 63168426 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 763,176 | 0.001570 | 63168426 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 750,393 | 1,016.168791 | 63168426 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 707,014 | 25.301589 | 63168426 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 680,644 | 0.041295 | 63168426 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | XDP/USDC | 100 | 678,850 | 0.013072 | 63168426 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | uXRP/WETH | 3000 | 671,865 | 0.000628 | 63168426 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/USDC | 3000 | 654,078 | 1,665.952557 | 63168426 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | ELSA/USDC | 100 | 595,650 | 0.094491 | 63168426 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 588,680 | 1,662.716868 | 63168426 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | WETH/USDC | 500 | 575,883 | 1,662.706901 | 63168426 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/wstETH | 3000 | 563,304 | 0.797531 | 63168426 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 552,211 | 0.383291 | 63168426 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 547,532 | 4,378,605.810532 | 63168426 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 505,177 | 4,252.891866 | 63168426 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 500,613 | 0.029564 | 63168426 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 477,726 | 539,119.414758 | 63168426 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 471,760 | 158,241.568820 | 63168426 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | WETH/USDC | 10000 | 456,706 | 1,668.052516 | 63168426 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 8 | 451,308 | 1.001781 | 63168426 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | USDC/MAI (stable) | 3000 | 444,547 | 1.378013 | 63168426 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 413,633 | 0.000007 | 63168426 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 393,022 | 1,016.381438 | 63168426 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 375,208 | 21.641839 | 63168426 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 372,177 | 829,274.073952 | 63168426 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 371,687 | 346.403887 | 63168426 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 356,653 | 0.052893 | 63168426 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/DEGEN | 3000 | 336,535 | 2,514,227.642932 | 63168426 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 24028 ; routes examinées : 299804724 ; candidats optimisés : 22683 ; net attendu > 0 : 0 ; dernier cycle 1212.0 ms
- Rejets (moteur) : {'spread_below_threshold': 293345102, 'liquidity_below_min': 4299739, 'borrow_bound_too_small': 23069, 'negative_expected_net': 22683, 'cycle_budget_exhausted': 339}
- Enregistrements de la session : 11 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 11} ; motifs de rejet : {'negative_expected_net': 11}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 63143807 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0027 | -29.90 |
| 63143807 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0027 | -29.90 |
| 63147871 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -29.90 |
| 63148302 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -29.90 |
| 63148302 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -29.90 |
| 63148302 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -29.90 |
| 63153175 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -29.90 |
| 63153175 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -29.90 |
| 63153175 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -29.90 |
| 63153175 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.012077 USDC | 0.000000 USDC | 0.004755 USDC | -0.0155 | -168.32 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
