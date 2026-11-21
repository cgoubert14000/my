# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-21T04:33:17+00:00 ; durée 82.15 min ; blocs 60201443 → 60226075 (8188 vus)

## Connexion
- Requêtes RPC : 67373 ; erreurs : 0 ; latence p50/p95 : 142.5/982.0 ms
- Rafraîchissements d'état : 8188 ; âge des données au dernier bloc : 7.36 s ; changements de frais LP observés (pools à frais dynamiques) : 7377
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1142 ; cycles déclenchés par événement : 259 ; avance médiane sur le rafraîchissement multicall : 127 ms
- Gaz : base fee 0.005912 gwei ; prix ETH (pool le plus profond) : 1,550.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 408 pools, 244 jetons, 12106 routes
- Par DEX : uniswap_v3 120, aerodrome 166, aerodrome_slipstream 86, pancakeswap_v3 25, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 410, sous le plancher de 10000.0 $ : 2 → gardés 408 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 1607.555855, 'cbBTC': 58186.714736, 'AERO': 0.387209}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 74,455,026 | 1,550.788190 | 60226087 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,567,631 | 0.027766 | 60226087 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 9,924,809 | 1,554.758946 | 60226087 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 6,777,487 | 0.027760 | 60226087 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 5,969,333 | 78.371631 | 60226087 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,048,796 | 0.000018 | 60226087 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,603,843 | 0.027753 | 60226087 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,216,272 | 2.693559 | 60226087 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 2,929,749 | 1.000008 | 60226087 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,758,766 | 1,555.143222 | 60226087 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,382,844 | 39,635.868864 | 60226087 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 394 | 2,027,997 | 1,554.603410 | 60226087 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,678,154 | 0.000018 | 60226087 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,519,167 | 0.027773 | 60226087 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,482,216 | 1,109,548.128542 | 60226087 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,807 | 0.844768 | 60226087 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,203,235 | 0.000000 | 60226087 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,197,328 | 0.000018 | 60226087 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,109,929 | 0.006481 | 60226087 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,065,523 | 15.957967 | 60226087 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,422 | 86.576680 | 60226087 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,037,193 | 0.000018 | 60226087 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 934,298 | 1,550.503822 | 60226087 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 921,736 | 457.450169 | 60226087 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 905,759 | 77.899814 | 60226087 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 895,325 | 16,478.514139 | 60226087 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | USDC/VVV | 3000 | 882,543 | 0.050606 | 60226087 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/AERO | 3000 | 879,856 | 4,176.879032 | 60226087 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 819,902 | 30,535,087.302828 | 60226087 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 741,959 | 77.718717 | 60226087 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4605 | 737,838 | 23.653050 | 60226087 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/BRETT | 10000 | 730,121 | 514,614.261836 | 60226087 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 713,600 | 21,485,575.843995 | 60226087 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 704,811 | 0.001534 | 60226087 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 698,829 | 0.013741 | 60226087 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | DRB/WETH | 10000 | 688,043 | 0.000000 | 60226087 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| pancakeswap_v3 | QUID/USDC | 100 | 687,079 | 0.042029 | 60226087 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/USDC | 3000 | 675,094 | 1,552.073083 | 60226087 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/MORPHO | 3000 | 659,601 | 1,061.498091 | 60226087 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 622,926 | 0.000625 | 60226087 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | WETH/USDC | 500 | 618,229 | 1,554.435137 | 60226087 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | TIG/USDC | 10000 | 548,937 | 0.380387 | 60226087 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 526,176 | 0.799406 | 60226087 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 514,317 | 1,555.179791 | 60226087 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 507,755 | 4,440,377.262917 | 60226087 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 478,556 | 4,169.204323 | 60226087 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 469,789 | 0.029016 | 60226087 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4040 | 456,519 | 516,059.126548 | 60226087 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 449,767 | 1.459373 | 60226087 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| pancakeswap_v3 | ELSA/USDC | 100 | 441,964 | 0.062592 | 60226087 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 10000 | 433,462 | 1,551.713443 | 60226087 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v2 | WETH/NPC | 3000 | 404,836 | 186,919.971182 | 60226087 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 393,832 | 0.000007 | 60226087 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3172 | 359,272 | 1,061.327178 | 60226087 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | AWE/USDC | 3000 | 354,766 | 0.052335 | 60226087 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/uSOL | 3000 | 353,737 | 21.199732 | 60226087 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 350,157 | 823,078.262975 | 60226087 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/DEGEN | 3000 | 339,307 | 2,351,449.752035 | 60226087 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| uniswap_v3 | WETH/UNI | 10000 | 331,315 | 365.456429 | 60226087 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2727 | 325,139 | 78.406429 | 60226087 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 8446 ; routes examinées : 102247276 ; candidats optimisés : 6357 ; net attendu > 0 : 2 ; dernier cycle 1570.1 ms
- Rejets (moteur) : {'spread_below_threshold': 98914988, 'liquidity_below_min': 1629394, 'borrow_bound_too_small': 8446, 'negative_expected_net': 6355, 'cycle_budget_exhausted': 1870}
- Enregistrements de la session : 14 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 14} ; motifs de rejet : {'negative_expected_net': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 60206159 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -40.79 |
| 60206194 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -40.79 |
| 60202822 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000017 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0038 | -40.84 |
| 60206159 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome]→tBTC→[aerodrome]→WETH | 0.000621 WETH | -0.000001 WETH | 0.000000 WETH | 0.000003 WETH | -0.0057 | -62.31 |
| 60217768 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0062 | -67.23 |
| 60218152 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0072 | -78.21 |
| 60220331 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0103 | -111.86 |
| 60220245 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0103 | -111.92 |
| 60220036 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0108 | -117.45 |
| 60220059 | cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→cbBTC | 0.000018 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0108 | -117.45 |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
