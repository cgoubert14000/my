# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-25T14:47:45+00:00 ; durée 310.38 min ; blocs 62045301 → 62138416 (17068 vus)

## Connexion
- Requêtes RPC : 172050 ; erreurs : 185 ; latence p50/p95 : 405.5/1,333.7 ms
- Rafraîchissements d'état : 17068 ; âge des données au dernier bloc : 7.83 s ; changements de frais LP observés (pools à frais dynamiques) : 12601
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 21205 ; cycles déclenchés par événement : 7502 ; avance médiane sur le rafraîchissement multicall : 402 ms
- Gaz : base fee 0.006623 gwei ; prix ETH (pool le plus profond) : 1,616.94 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 415 pools, 246 jetons, 12424 routes
- Par DEX : uniswap_v3 124, aerodrome 169, aerodrome_slipstream 85, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 145 (rejetés 2) → 550 jetons ; pools candidats 3597 (énumérés 252, par paires 0), mesurés 417, sous le plancher de 10000.0 $ : 2 → gardés 415 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1640.509461, 'cbBTC': 58853.942398, 'AERO': 0.390265}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 91,441,510 | 1,617.868857 | 62138438 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,610,089 | 0.028137 | 62138438 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,080,337 | 0.028068 | 62138438 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 6,859,361 | 1,621.828008 | 62138438 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,801,678 | 65.377983 | 62138438 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,000,735 | 0.000017 | 62138438 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,826,035 | 0.028136 | 62138438 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,178,196 | 2.650514 | 62138438 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,023,882 | 0.999826 | 62138438 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,899,882 | 1,622.308699 | 62138438 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,527,894 | 38,288.865494 | 62138438 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 394 | 2,109,694 | 1,621.774671 | 62138438 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,824,525 | 0.000017 | 62138438 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2540 | 1,784,079 | 0.028079 | 62138438 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,550,799 | 1,101,978.542519 | 62138438 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,303 | 0.834786 | 62138438 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,236,669 | 0.000000 | 62138438 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,189,528 | 0.000017 | 62138438 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,183,524 | 12.290334 | 62138438 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,082,484 | 0.000017 | 62138438 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/VVV | 3000 | 1,065,289 | 0.040302 | 62138438 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,057,669 | 0.005867 | 62138438 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,053,294 | 87.587035 | 62138438 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/VVV | 10000 | 1,012,675 | 65.703962 | 62138438 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 956,654 | 468.033753 | 62138438 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 954,880 | 1,617.440746 | 62138438 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 917,966 | 16,635.474959 | 62138438 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 898,984 | 4,295.758041 | 62138438 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 840,129 | 31,900,542.890669 | 62138438 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 789,129 | 0.000000 | 62138438 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 758,642 | 20,744,385.546157 | 62138438 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 757,757 | 74.511948 | 62138438 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 733,938 | 571,076.081695 | 62138438 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 720,457 | 0.001514 | 62138438 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 706,913 | 1,078.920306 | 62138438 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | XDP/USDC | 100 | 691,173 | 0.013496 | 62138438 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 678,904 | 1,617.082663 | 62138438 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | QUID/USDC | 100 | 675,743 | 0.040748 | 62138438 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4605 | 661,489 | 27.611714 | 62138438 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | uXRP/WETH | 3000 | 646,761 | 0.000609 | 62138438 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | WETH/USDC | 500 | 575,119 | 1,621.595891 | 62138438 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | TIG/USDC | 10000 | 573,326 | 0.412592 | 62138438 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v3 | WETH/USDC | 100 | 571,099 | 1,622.276394 | 62138438 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 549,128 | 0.797990 | 62138438 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | ELSA/USDC | 100 | 532,738 | 0.078952 | 62138438 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 528,248 | 4,471,455.936925 | 62138438 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 492,228 | 4,275.009920 | 62138438 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 471,397 | 0.027039 | 62138438 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,446 | 1.001758 | 62138438 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 451,306 | 570,274.073729 | 62138438 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | WETH/USDC | 10000 | 451,145 | 1,623.154997 | 62138438 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/MAI (stable) | 3000 | 443,185 | 1.386702 | 62138438 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 438,727 | 173,794.643162 | 62138438 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 404,821 | 0.000007 | 62138438 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 374,106 | 1,079.119587 | 62138438 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 366,559 | 21.605498 | 62138438 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 357,784 | 831,513.416145 | 62138438 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 352,133 | 366.168376 | 62138438 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 348,921 | 0.050613 | 62138438 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/DEGEN | 3000 | 330,005 | 2,565,578.611629 | 62138438 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 24569 ; routes examinées : 291094320 ; candidats optimisés : 25709 ; net attendu > 0 : 0 ; dernier cycle 1202.0 ms
- Rejets (moteur) : {'spread_below_threshold': 285059943, 'liquidity_below_min': 3196956, 'negative_expected_net': 25709, 'borrow_bound_too_small': 23430, 'cycle_budget_exhausted': 163}
- Enregistrements de la session : 1 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 1} ; motifs de rejet : {'negative_expected_net': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 62089482 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.000017 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0097 | -105.51 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
