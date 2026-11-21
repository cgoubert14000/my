# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-21T04:36:20+00:00 ; durée 85.2 min ; blocs 60201443 → 60226998 (8505 vus)

## Connexion
- Requêtes RPC : 69942 ; erreurs : 0 ; latence p50/p95 : 164.3/1,015.5 ms
- Rafraîchissements d'état : 8505 ; âge des données au dernier bloc : 5.84 s ; changements de frais LP observés (pools à frais dynamiques) : 7612
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1142 ; cycles déclenchés par événement : 259 ; avance médiane sur le rafraîchissement multicall : 127 ms
- Gaz : base fee 0.005376 gwei ; prix ETH (pool le plus profond) : 1,549.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 408 pools, 244 jetons, 12106 routes
- Par DEX : uniswap_v3 120, aerodrome 166, aerodrome_slipstream 86, pancakeswap_v3 25, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 410, sous le plancher de 10000.0 $ : 2 → gardés 408 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 1607.555855, 'cbBTC': 58186.714736, 'AERO': 0.387209}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 74,419,320 | 1,549.971450 | 60226998 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,566,215 | 0.027692 | 60226998 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 9,920,033 | 1,552.807608 | 60226998 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 6,779,730 | 0.027748 | 60226998 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 5,971,147 | 78.247242 | 60226998 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,061,396 | 0.000018 | 60226998 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,603,754 | 0.027691 | 60226998 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,218,101 | 2.690500 | 60226998 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 2,936,356 | 1.000008 | 60226998 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,757,473 | 1,553.395210 | 60226998 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,381,733 | 39,633.949348 | 60226998 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 247 | 2,027,067 | 1,553.139331 | 60226998 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,681,528 | 0.000018 | 60226998 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2550 | 1,519,007 | 0.027741 | 60226998 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,481,490 | 1,109,548.128542 | 60226998 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,807 | 0.844768 | 60226998 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,202,645 | 0.000000 | 60226998 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,199,762 | 0.000018 | 60226998 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,101,920 | 0.006481 | 60226998 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,068,626 | 15.836413 | 60226998 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,422 | 86.576680 | 60226998 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,039,460 | 0.000018 | 60226998 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 934,071 | 1,549.656297 | 60226998 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 921,704 | 456.537280 | 60226998 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 905,533 | 77.899696 | 60226998 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 897,031 | 16,482.003974 | 60226998 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | USDC/VVV | 3000 | 883,280 | 0.050376 | 60226998 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/AERO | 3000 | 880,443 | 4,176.879032 | 60226998 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 819,500 | 30,535,087.302828 | 60226998 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 741,959 | 77.718717 | 60226998 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4610 | 738,651 | 23.617177 | 60226998 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/BRETT | 10000 | 729,763 | 514,614.261836 | 60226998 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 713,251 | 21,485,575.843995 | 60226998 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 705,798 | 0.001532 | 60226998 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 698,050 | 0.013712 | 60226998 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 688,204 | 0.042158 | 60226998 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | DRB/WETH | 10000 | 687,706 | 0.000000 | 60226998 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/USDC | 3000 | 674,929 | 1,549.564985 | 60226998 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/MORPHO | 3000 | 659,278 | 1,061.498091 | 60226998 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 622,549 | 0.000625 | 60226998 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | WETH/USDC | 500 | 617,951 | 1,552.783771 | 60226998 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | TIG/USDC | 10000 | 548,937 | 0.380387 | 60226998 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 525,918 | 0.799406 | 60226998 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 514,120 | 1,553.121502 | 60226998 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 506,811 | 4,452,583.684796 | 60226998 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 478,711 | 4,169.204323 | 60226998 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 470,787 | 0.029106 | 60226998 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4229 | 456,300 | 512,379.285522 | 60226998 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 449,767 | 1.459373 | 60226998 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| pancakeswap_v3 | ELSA/USDC | 100 | 443,080 | 0.062788 | 60226998 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 10000 | 433,307 | 1,551.435661 | 60226998 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v2 | WETH/NPC | 3000 | 404,864 | 186,711.837971 | 60226998 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 394,397 | 0.000007 | 60226998 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3169 | 359,095 | 1,061.327178 | 60226998 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | AWE/USDC | 3000 | 355,022 | 0.052410 | 60226998 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/uSOL | 3000 | 353,564 | 21.199732 | 60226998 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 350,804 | 812,078.109402 | 60226998 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/DEGEN | 3000 | 339,140 | 2,351,449.752035 | 60226998 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| uniswap_v3 | WETH/UNI | 10000 | 331,153 | 365.456429 | 60226998 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2763 | 325,079 | 78.187582 | 60226998 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 8763 ; routes examinées : 106084878 ; candidats optimisés : 6617 ; net attendu > 0 : 2 ; dernier cycle 1343.5 ms
- Rejets (moteur) : {'spread_below_threshold': 102622573, 'liquidity_below_min': 1705028, 'borrow_bound_too_small': 8763, 'negative_expected_net': 6615, 'cycle_budget_exhausted': 2290}
- Enregistrements de la session : 16 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 16} ; motifs de rejet : {'negative_expected_net': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 60226215 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -39.17 |
| 60226668 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -39.17 |
| 60206159 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -40.79 |
| 60206194 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -40.79 |
| 60202822 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -40.84 |
| 60206159 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome]→tBTC→[aerodrome]→WETH | 0.000621 WETH | -0.000001 WETH | 0.000000 WETH | 0.000003 WETH | -0.0057 | -62.31 |
| 60217768 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0062 | -67.23 |
| 60218152 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0072 | -78.21 |
| 60220331 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0103 | -111.86 |
| 60220245 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0103 | -111.92 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
