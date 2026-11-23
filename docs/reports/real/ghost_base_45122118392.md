# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-23T09:22:44+00:00 ; durée 183.29 min ; blocs 61121880 → 61176856 (3514 vus)

## Connexion
- Requêtes RPC : 50277 ; erreurs : 0 ; latence p50/p95 : 1,292.6/4,107.3 ms
- Rafraîchissements d'état : 3514 ; âge des données au dernier bloc : 18.75 s ; changements de frais LP observés (pools à frais dynamiques) : 3627
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2743 ; cycles déclenchés par événement : 738 ; avance médiane sur le rafraîchissement multicall : 624 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,727.88 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 249 jetons, 12840 routes
- Par DEX : uniswap_v3 127, aerodrome 171, aerodrome_slipstream 87, pancakeswap_v3 26, uniswap_v2 10, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 148 (rejetés 2) → 553 jetons ; pools candidats 3600 (énumérés 255, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1730.318701, 'cbBTC': 61628.571065, 'AERO': 0.424144}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 82,749,080 | 1,727.884553 | 61176856 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 22,436,434 | 0.028032 | 61176856 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,224,325 | 1,730.484173 | 61176856 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,725,841 | 0.028070 | 61176856 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,198,571 | 66.654865 | 61176856 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,060,704 | 0.000016 | 61176856 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,019,738 | 0.028031 | 61176856 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,380,791 | 2.353868 | 61176856 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,243,499 | 0.999822 | 61176856 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,024,381 | 1,730.320741 | 61176856 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,640,175 | 40,083.527751 | 61176856 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,233,089 | 1,730.387112 | 61176856 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,919,848 | 0.028043 | 61176856 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,853,870 | 0.000016 | 61176856 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 1,671,871 | 1,082,729.557909 | 61176856 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,425 | 0.842389 | 61176856 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,320,230 | 0.000000 | 61176856 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,288,496 | 0.000016 | 61176856 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,187,568 | 0.006152 | 61176856 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,142,205 | 13.382118 | 61176856 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,128,574 | 0.000016 | 61176856 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/SEND | 3000 | 1,061,173 | 86.291215 | 61176856 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | USDC/VVV | 3000 | 1,058,347 | 0.038576 | 61176856 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,022,165 | 467.564920 | 61176856 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 1,006,311 | 66.506874 | 61176856 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/AERO | 3000 | 996,617 | 4,073.967442 | 61176856 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 986,586 | 1,727.487815 | 61176856 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 982,854 | 16,639.436321 | 61176856 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 903,286 | 0.000000 | 61176856 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 902,749 | 31,513,089.255701 | 61176856 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 832,653 | 61.710420 | 61176856 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 798,261 | 551,459.073480 | 61176856 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 788,007 | 21,782,445.112750 | 61176856 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 779,882 | 0.001542 | 61176856 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 714,086 | 0.014280 | 61176856 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 704,620 | 1,728.025947 | 61176856 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | QUID/USDC | 100 | 703,025 | 0.043923 | 61176856 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 697,040 | 1,095.955821 | 61176856 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 691,269 | 0.000610 | 61176856 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 678,192 | 26.634035 | 61176856 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | ELSA/USDC | 100 | 629,498 | 0.106493 | 61176856 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| pancakeswap_v3 | WETH/USDC | 500 | 623,310 | 1,730.493871 | 61176856 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 594,471 | 4,029,231.006200 | 61176856 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/wstETH | 3000 | 585,125 | 0.802580 | 61176856 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 575,080 | 0.415518 | 61176856 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v3 | WETH/USDC | 100 | 564,388 | 1,730.284741 | 61176856 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/AERO | 10000 | 540,041 | 4,066.613772 | 61176856 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 498,412 | 0.030478 | 61176856 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 494,910 | 155,729.909796 | 61176856 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 491,019 | 549,011.146662 | 61176856 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | WETH/USDC | 10000 | 476,692 | 1,730.661994 | 61176856 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 8 | 459,921 | 1.001638 | 61176856 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 448,227 | 0.000007 | 61176856 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 439,393 | 1.444207 | 61176856 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/uSOL | 3000 | 394,324 | 21.185612 | 61176856 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 391,520 | 1,095.799195 | 61176856 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 377,776 | 855,227.078325 | 61176856 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 374,482 | 363.395959 | 61176856 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 357,334 | 0.053095 | 61176856 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/DEGEN | 3000 | 357,082 | 2,489,660.629721 | 61176856 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 4251 ; routes examinées : 54582840 ; candidats optimisés : 2840 ; net attendu > 0 : 0 ; dernier cycle 3480.6 ms
- Rejets (moteur) : {'spread_below_threshold': 53554878, 'liquidity_below_min': 514218, 'borrow_bound_too_small': 4251, 'negative_expected_net': 2840, 'cycle_budget_exhausted': 348}
- Enregistrements de la session : 7 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 7} ; motifs de rejet : {'negative_expected_net': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 61164553 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0028 | -30.67 |
| 61156536 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.83 |
| 61147813 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.92 |
| 61147813 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.92 |
| 61147813 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.92 |
| 61147813 | cbBTC→[aerodrome]→tBTC→[aerodrome]→WETH→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0096 | -104.62 |
| 61147813 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→tBTC→[aerodrome]→WETH | 0.000580 WETH | -0.000004 WETH | 0.000000 WETH | 0.000003 WETH | -0.0103 | -111.94 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
