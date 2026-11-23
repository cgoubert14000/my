# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-23T16:29:34+00:00 ; durée 268.5 min ; blocs 61224414 → 61304972 (15185 vus)

## Connexion
- Requêtes RPC : 150750 ; erreurs : 165 ; latence p50/p95 : 516.3/1,712.6 ms
- Rafraîchissements d'état : 15185 ; âge des données au dernier bloc : 4.87 s ; changements de frais LP observés (pools à frais dynamiques) : 16403
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 36348 ; cycles déclenchés par événement : 9386 ; avance médiane sur le rafraîchissement multicall : 286 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,768.86 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 423 pools, 250 jetons, 12764 routes
- Par DEX : uniswap_v3 126, aerodrome 171, aerodrome_slipstream 88, pancakeswap_v3 26, uniswap_v2 10, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 148 (rejetés 2) → 553 jetons ; pools candidats 3600 (énumérés 256, par paires 0), mesurés 425, sous le plancher de 10000.0 $ : 2 → gardés 423 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1722.853517, 'cbBTC': 61334.05263, 'AERO': 0.41994}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 84,136,557 | 1,768.861518 | 61304972 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 22,743,072 | 0.028284 | 61304972 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,150,183 | 1,772.216061 | 61304972 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,867,437 | 0.028255 | 61304972 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,181,421 | 70.187902 | 61304972 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,481,916 | 0.000016 | 61304972 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,112,282 | 0.028296 | 61304972 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,404,978 | 2.315051 | 61304972 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,291,302 | 0.999602 | 61304972 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,146,526 | 1,772.349480 | 61304972 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,707,202 | 39,952.893296 | 61304972 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 115 | 2,284,301 | 1,772.101269 | 61304972 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,957,792 | 0.028241 | 61304972 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,897,951 | 0.000016 | 61304972 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 1,702,606 | 1,094,096.302924 | 61304972 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,971 | 0.843272 | 61304972 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,339,182 | 0.000000 | 61304972 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,302,285 | 0.000016 | 61304972 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,199,615 | 0.006130 | 61304972 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,193,821 | 12.038303 | 61304972 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,142,201 | 0.000016 | 61304972 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/SEND | 3000 | 1,060,869 | 86.340761 | 61304972 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,050,230 | 460.505899 | 61304972 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/VVV | 3000 | 1,040,669 | 0.039638 | 61304972 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/AERO | 3000 | 1,016,009 | 4,102.657632 | 61304972 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,008,660 | 16,298.174042 | 61304972 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 1,004,084 | 69.698557 | 61304972 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 998,356 | 1,768.835817 | 61304972 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 930,060 | 0.000000 | 61304972 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 920,169 | 31,846,653.701654 | 61304972 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 850,303 | 59.175120 | 61304972 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 814,465 | 548,275.347626 | 61304972 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 806,774 | 21,786,479.492092 | 61304972 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 799,606 | 0.001574 | 61304972 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 738,957 | 0.015247 | 61304972 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 738,304 | 23.795844 | 61304972 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/MORPHO | 3000 | 724,182 | 1,075.053959 | 61304972 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | QUID/USDC | 100 | 718,680 | 0.045897 | 61304972 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | uXRP/WETH | 3000 | 713,104 | 0.000619 | 61304972 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/USDC | 3000 | 712,832 | 1,771.355336 | 61304972 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | ELSA/USDC | 100 | 642,204 | 0.110560 | 61304972 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| pancakeswap_v3 | WETH/USDC | 500 | 634,318 | 1,772.263492 | 61304972 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/wstETH | 3000 | 600,770 | 0.797862 | 61304972 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 592,800 | 4,247,118.667656 | 61304972 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 591,380 | 0.438265 | 61304972 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v3 | WETH/USDC | 100 | 579,693 | 1,772.364700 | 61304972 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/AERO | 10000 | 550,969 | 4,071.497111 | 61304972 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 530,634 | 0.033388 | 61304972 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 516,908 | 149,665.351769 | 61304972 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 4040 | 504,206 | 544,488.381185 | 61304972 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | WETH/USDC | 10000 | 481,771 | 1,777.941202 | 61304972 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 8 | 459,588 | 1.001534 | 61304972 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 455,691 | 0.000007 | 61304972 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 438,932 | 1.446787 | 61304972 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 3286 | 408,009 | 1,074.796332 | 61304972 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 402,231 | 21.387358 | 61304972 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 397,802 | 348.615278 | 61304972 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 382,983 | 862,344.212908 | 61304972 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/VVV | 2724 | 372,830 | 70.206455 | 61304972 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | WETH/DEGEN | 3000 | 367,985 | 2,458,043.404940 | 61304972 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 24570 ; routes examinées : 313611480 ; candidats optimisés : 26667 ; net attendu > 0 : 2 ; dernier cycle 2492.1 ms
- Rejets (moteur) : {'spread_below_threshold': 306522961, 'liquidity_below_min': 3897176, 'negative_expected_net': 26665, 'borrow_bound_too_small': 24572, 'cycle_budget_exhausted': 512}
- Enregistrements de la session : 7 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 7} ; motifs de rejet : {'negative_expected_net': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
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
