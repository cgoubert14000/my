# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-27T13:43:43+00:00 ; durée 58.03 min ; blocs 62965805 → 62983222 (5104 vus)

## Connexion
- Requêtes RPC : 42226 ; erreurs : 0 ; latence p50/p95 : 317.6/1,493.4 ms
- Rafraîchissements d'état : 5104 ; âge des données au dernier bloc : 3.75 s ; changements de frais LP observés (pools à frais dynamiques) : 1634
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 701 ; cycles déclenchés par événement : 318 ; avance médiane sur le rafraîchissement multicall : 198 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,719.04 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 431 pools, 252 jetons, 13006 routes
- Par DEX : uniswap_v3 129, aerodrome 171, aerodrome_slipstream 92, pancakeswap_v3 27, uniswap_v2 10, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 148 (rejetés 2) → 553 jetons ; pools candidats 3642 (énumérés 261, par paires 0), mesurés 433, sous le plancher de 10000.0 $ : 2 → gardés 431 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1721.594424, 'cbBTC': 61493.728509, 'AERO': 0.403758}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 96,320,495 | 1,719.039922 | 62983222 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 23,365,895 | 0.028012 | 62983222 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,571,489 | 0.028006 | 62983222 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,349,384 | 63.206693 | 62983222 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,186,022 | 1,719.825045 | 62983222 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,939,821 | 0.000016 | 62983222 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,118,513 | 0.028020 | 62983222 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,252,273 | 2.494198 | 62983222 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,229,702 | 0.999486 | 62983222 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,032,499 | 1,719.884810 | 62983222 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,684,700 | 38,369.182458 | 62983222 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 123 | 2,213,852 | 1,719.711421 | 62983222 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,976,945 | 0.000016 | 62983222 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,880,813 | 0.027994 | 62983222 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,649,991 | 1,100,284.256210 | 62983222 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,301 | 0.834978 | 62983222 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,305,004 | 0.000000 | 62983222 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,283,427 | 0.000016 | 62983222 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,277,698 | 10.318772 | 62983222 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,172,605 | 0.006168 | 62983222 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,137,900 | 0.000016 | 62983222 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/VVV | 3000 | 1,124,264 | 0.036758 | 62983222 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/SEND | 3000 | 1,061,605 | 86.221050 | 62983222 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,026,433 | 450.174350 | 62983222 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 1,021,074 | 63.218391 | 62983222 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 996,392 | 16,094.103948 | 62983222 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 984,859 | 1,718.312099 | 62983222 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 949,943 | 4,282.717672 | 62983222 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 896,623 | 31,581,465.252287 | 62983222 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 856,903 | 0.000000 | 62983222 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 802,164 | 20,930,779.033872 | 62983222 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/BRETT | 10000 | 789,448 | 552,050.174681 | 62983222 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 787,547 | 68.981615 | 62983222 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 782,632 | 0.001566 | 62983222 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 770,766 | 1,037.263203 | 62983222 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 700,049 | 25.639479 | 62983222 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/USDC | 3000 | 695,986 | 1,722.390848 | 62983222 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | uXRP/WETH | 3000 | 692,798 | 0.000624 | 62983222 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | QUID/USDC | 100 | 685,142 | 0.041804 | 62983222 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | XDP/USDC | 100 | 677,080 | 0.013011 | 62983222 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/USDC | 100 | 612,531 | 1,719.884810 | 62983222 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | WETH/USDC | 500 | 596,052 | 1,719.673295 | 62983222 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/wstETH | 3000 | 583,026 | 0.800091 | 62983222 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 561,879 | 4,468,745.084057 | 62983222 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 558,780 | 0.084517 | 62983222 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | TIG/USDC | 10000 | 552,675 | 0.383975 | 62983222 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/AERO | 10000 | 521,930 | 4,252.594256 | 62983222 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 508,400 | 0.030177 | 62983222 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 488,499 | 554,762.394562 | 62983222 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 486,945 | 159,586.139423 | 62983222 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | WETH/USDC | 10000 | 464,942 | 1,731.192378 | 62983222 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 8 | 452,600 | 1.001551 | 62983222 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | USDC/MAI (stable) | 3000 | 443,218 | 1.386525 | 62983222 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 431,721 | 0.000007 | 62983222 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3169 | 404,996 | 1,037.556460 | 62983222 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 388,469 | 21.699620 | 62983222 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 380,190 | 353.669007 | 62983222 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 378,802 | 839,627.964374 | 62983222 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 357,828 | 0.053242 | 62983222 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/DEGEN | 3000 | 348,729 | 2,516,295.138299 | 62983222 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 5421 ; routes examinées : 70505526 ; candidats optimisés : 11509 ; net attendu > 0 : 0 ; dernier cycle 2408.7 ms
- Rejets (moteur) : {'spread_below_threshold': 69577979, 'liquidity_below_min': 562232, 'negative_expected_net': 11509, 'borrow_bound_too_small': 5421, 'cycle_budget_exhausted': 103}
- Enregistrements de la session : 5 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 5} ; motifs de rejet : {'negative_expected_net': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 62977559 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.88 |
| 62977559 | cbBTC→[aerodrome]→tBTC→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.88 |
| 62977559 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.88 |
| 62977375 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0034 | -36.88 |
| 62977559 | cbBTC→[aerodrome]→tBTC→[aerodrome]→WETH→[pancakeswap_v3]→cbBTC | 0.000016 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0079 | -86.05 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
