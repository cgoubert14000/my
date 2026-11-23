# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-23T16:50:52+00:00 ; durée 289.8 min ; blocs 61224414 → 61311323 (16284 vus)

## Connexion
- Requêtes RPC : 161649 ; erreurs : 165 ; latence p50/p95 : 429.9/1,761.8 ms
- Rafraîchissements d'état : 16284 ; âge des données au dernier bloc : 12.96 s ; changements de frais LP observés (pools à frais dynamiques) : 17786
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 38869 ; cycles déclenchés par événement : 10103 ; avance médiane sur le rafraîchissement multicall : 328 ms
- Gaz : base fee 0.005004 gwei ; prix ETH (pool le plus profond) : 1,758.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 250 jetons, 12764 routes
- Par DEX : uniswap_v3 126, aerodrome 171, aerodrome_slipstream 88, pancakeswap_v3 26, uniswap_v2 10, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 148 (rejetés 2) → 553 jetons ; pools candidats 3600 (énumérés 256, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1722.853517, 'cbBTC': 61334.05263, 'AERO': 0.41994}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 83,846,584 | 1,758.742822 | 61311359 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 22,778,468 | 0.028390 | 61311359 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,107,426 | 1,761.768158 | 61311359 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,809,997 | 0.028319 | 61311359 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,125,137 | 70.487712 | 61311359 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,447,567 | 0.000016 | 61311359 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,100,109 | 0.028386 | 61311359 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,389,013 | 2.336914 | 61311359 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,261,167 | 0.998675 | 61311359 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,137,173 | 1,762.511079 | 61311359 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,691,560 | 39,957.518964 | 61311359 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 216 | 2,272,905 | 1,762.327397 | 61311359 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2555 | 1,944,431 | 0.028332 | 61311359 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,885,995 | 0.000016 | 61311359 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 1,692,866 | 1,094,096.302924 | 61311359 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,756 | 0.843272 | 61311359 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,325,286 | 0.000000 | 61311359 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,292,207 | 0.000016 | 61311359 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,213,424 | 0.006196 | 61311359 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,185,899 | 12.228660 | 61311359 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,132,624 | 0.000016 | 61311359 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/SEND | 3000 | 1,060,862 | 86.341829 | 61311359 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,043,101 | 462.654712 | 61311359 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/VVV | 3000 | 1,035,253 | 0.040048 | 61311359 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/AERO | 3000 | 1,007,651 | 4,106.734639 | 61311359 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 998,721 | 16,288.268940 | 61311359 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 997,433 | 70.957741 | 61311359 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 995,506 | 1,758.731594 | 61311359 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 925,267 | 0.000000 | 61311359 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 915,720 | 31,767,531.265653 | 61311359 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 850,149 | 59.196541 | 61311359 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 809,811 | 548,263.886712 | 61311359 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 802,671 | 21,762,625.097002 | 61311359 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 790,346 | 0.001568 | 61311359 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 736,810 | 0.015162 | 61311359 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/SAPIEN | 4590 | 732,336 | 24.064578 | 61311359 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/MORPHO | 3000 | 719,054 | 1,077.336952 | 61311359 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | QUID/USDC | 100 | 715,102 | 0.045438 | 61311359 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/USDC | 3000 | 710,720 | 1,758.604245 | 61311359 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | uXRP/WETH | 3000 | 708,908 | 0.000618 | 61311359 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | ELSA/USDC | 100 | 635,009 | 0.108112 | 61311359 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| pancakeswap_v3 | WETH/USDC | 500 | 631,467 | 1,761.823798 | 61311359 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/wstETH | 3000 | 597,327 | 0.797878 | 61311359 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 591,627 | 0.438614 | 61311359 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 589,359 | 4,247,836.398259 | 61311359 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | WETH/USDC | 100 | 577,874 | 1,762.482025 | 61311359 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/AERO | 10000 | 546,817 | 4,076.758181 | 61311359 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 537,063 | 0.033996 | 61311359 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 514,660 | 149,269.125406 | 61311359 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 4058 | 501,327 | 545,243.482897 | 61311359 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | WETH/USDC | 10000 | 480,563 | 1,768.900377 | 61311359 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 8 | 459,564 | 1.001609 | 61311359 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 451,414 | 0.000007 | 61311359 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 438,932 | 1.446787 | 61311359 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 405,017 | 1,077.199980 | 61311359 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 399,930 | 21.387358 | 61311359 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 393,133 | 349.708229 | 61311359 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 380,536 | 856,801.082204 | 61311359 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/VVV | 2730 | 370,249 | 70.507496 | 61311359 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | WETH/DEGEN | 3000 | 365,992 | 2,456,527.390176 | 61311359 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 26386 ; routes examinées : 336790904 ; candidats optimisés : 27220 ; net attendu > 0 : 2 ; dernier cycle 2497.7 ms
- Rejets (moteur) : {'spread_below_threshold': 329217037, 'liquidity_below_min': 4145998, 'negative_expected_net': 27218, 'borrow_bound_too_small': 26388, 'cycle_budget_exhausted': 633}
- Enregistrements de la session : 8 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 8} ; motifs de rejet : {'negative_expected_net': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 61308262 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0023 | -24.30 |
| 61249979 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.70 |
| 61249171 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.70 |
| 61243640 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.70 |
| 61243640 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.70 |
| 61243640 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.70 |
| 61291795 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | 0.000567 USDC | 0.000000 USDC | 0.005589 USDC | -0.0046 | -50.22 |
| 61243640 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome]→tBTC→[aerodrome]→WETH | 0.000582 WETH | -0.000002 WETH | 0.000000 WETH | 0.000003 WETH | -0.0070 | -75.88 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
