# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-15T16:34:21+00:00 ; durée 282.72 min ; blocs 57765594 → 57850373 (25443 vus)

## Connexion
- Requêtes RPC : 240291 ; erreurs : 15 ; latence p50/p95 : 96.6/1,361.2 ms
- Rafraîchissements d'état : 25443 ; âge des données au dernier bloc : 11.48 s ; changements de frais LP observés (pools à frais dynamiques) : 10798
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22082 ; cycles déclenchés par événement : 6179 ; avance médiane sur le rafraîchissement multicall : 120 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,816.81 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 436 pools, 253 jetons, 13300 routes
- Par DEX : uniswap_v3 130, aerodrome_slipstream 88, aerodrome 177, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 149 (rejetés 2) → 554 jetons ; pools candidats 3593 (énumérés 264, par paires 0), mesurés 438, sous le plancher de 10000.0 $ : 2 → gardés 436 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1831.864662, 'cbBTC': 65446.070264, 'AERO': 0.441982}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 86,707,985 | 1,816.811100 | 57850408 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,965,098 | 0.028087 | 57850408 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,718,757 | 0.028062 | 57850408 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,512,728 | 90.637142 | 57850408 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,340,956 | 0.000015 | 57850408 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 5,864,760 | 1,812.255625 | 57850408 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,173,241 | 0.028084 | 57850408 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,735,125 | 1,812.888112 | 57850408 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 3,715,439 | 2.307084 | 57850408 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,403,647 | 0.999829 | 57850408 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,744,218 | 41,019.183316 | 57850408 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 138 | 2,459,546 | 1,812.524926 | 57850408 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2565 | 1,832,830 | 0.028070 | 57850408 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,702,163 | 1,153,941.910013 | 57850408 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,683,231 | 0.017364 | 57850408 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,501,726 | 0.000015 | 57850408 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,268 | 0.842686 | 57850408 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,398,934 | 0.000000 | 57850408 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,316,127 | 0.006531 | 57850408 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,285,321 | 0.000015 | 57850408 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,235,582 | 440.462833 | 57850408 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,201,078 | 0.000015 | 57850408 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/SEND | 3000 | 1,061,409 | 86.252803 | 57850408 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,059,428 | 15,677.155883 | 57850408 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,046,871 | 4,184.222657 | 57850408 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,040,787 | 1,817.218807 | 57850408 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,002,579 | 1,817.108377 | 57850408 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/VVV | 10000 | 985,439 | 90.802958 | 57850408 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 970,098 | 20.724907 | 57850408 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| pancakeswap_v3 | WETH/USDC | 500 | 968,045 | 1,812.334348 | 57850408 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 941,544 | 31,957,074.125919 | 57850408 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 834,833 | 552,840.749882 | 57850408 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | USDC/VVV | 3000 | 831,720 | 0.050027 | 57850408 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 817,271 | 1,042.595877 | 57850408 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/TOSHI | 10000 | 793,358 | 23,398,522.762968 | 57850408 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 793,328 | 0.001449 | 57850408 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | DRB/WETH | 10000 | 791,286 | 0.000000 | 57850408 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 731,038 | 88.013660 | 57850408 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 714,969 | 1,812.371966 | 57850408 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | QUID/USDC | 100 | 687,570 | 0.042129 | 57850408 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4575 | 674,093 | 26.541148 | 57850408 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 100 | 620,546 | 1,812.823358 | 57850408 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 616,842 | 0.798414 | 57850408 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 608,290 | 0.464431 | 57850408 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/AERO | 10000 | 578,657 | 4,162.576168 | 57850408 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 573,121 | 4,773,119.410023 | 57850408 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 534,050 | 146,939.086194 | 57850408 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | USDC/MAI (stable) | 3000 | 521,922 | 1.385672 | 57850408 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3703 | 514,400 | 553,748.814951 | 57850408 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 501,503 | 0.446673 | 57850408 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 495,897 | 0.000245 | 57850408 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | FLOCK/USDC | 3000 | 489,139 | 0.030859 | 57850408 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 464,859 | 0.000007 | 57850408 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/USDT | 8 | 452,141 | 1.000527 | 57850408 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | WETH/MORPHO | 3130 | 427,331 | 1,042.582763 | 57850408 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 422,753 | 0.059451 | 57850408 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 397,774 | 0.572573 | 57850408 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 392,894 | 878,068.074104 | 57850408 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 387,707 | 25.036464 | 57850408 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | WETH/msETH (stable) | 500 | 379,371 | 2.326203 | 57850408 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 31621 ; routes examinées : 420466200 ; candidats optimisés : 23481 ; net attendu > 0 : 28 ; dernier cycle 1372.9 ms
- Rejets (moteur) : {'spread_below_threshold': 412062647, 'liquidity_below_min': 6090155, 'borrow_bound_too_small': 31614, 'negative_expected_net': 23453, 'cycle_budget_exhausted': 4053}
- Enregistrements de la session : 104 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 104} ; motifs de rejet : {'negative_expected_net': 104}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 57825016 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.81 |
| 57842586 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57844452 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57828610 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57828610 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57828610 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57828653 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57828653 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57828653 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |
| 57827909 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -38.83 |

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
