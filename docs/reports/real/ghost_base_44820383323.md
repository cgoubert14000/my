# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-21T02:41:25+00:00 ; durée 307.98 min ; blocs 60100131 → 60192510 (22079 vus)

## Connexion
- Requêtes RPC : 228550 ; erreurs : 60 ; latence p50/p95 : 299.7/961.1 ms
- Rafraîchissements d'état : 22079 ; âge des données au dernier bloc : 6.75 s ; changements de frais LP observés (pools à frais dynamiques) : 13058
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 40999 ; cycles déclenchés par événement : 12994 ; avance médiane sur le rafraîchissement multicall : 317 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,620.88 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 245 jetons, 12256 routes
- Par DEX : uniswap_v3 122, aerodrome_slipstream 86, aerodrome 166, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1605.51254, 'cbBTC': 58557.611788, 'AERO': 0.386499}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,396,317 | 1,620.880492 | 60192527 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,505,534 | 0.027587 | 60192527 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,326,806 | 1,616.905307 | 60192527 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,090,847 | 0.027518 | 60192527 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,295,317 | 76.984598 | 60192527 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,432,136 | 0.000017 | 60192527 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,778,178 | 0.027599 | 60192527 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,317,055 | 2.532472 | 60192527 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,089,525 | 1.000001 | 60192527 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,874,436 | 1,617.347549 | 60192527 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,500,914 | 39,310.678058 | 60192527 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 100 | 2,111,147 | 1,617.210846 | 60192527 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,758,327 | 0.000017 | 60192527 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 1,588,552 | 0.027533 | 60192527 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,547,236 | 1,112,461.746607 | 60192527 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,318 | 0.844767 | 60192527 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,254,447 | 0.000000 | 60192527 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,252,451 | 0.000017 | 60192527 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,156,988 | 0.006484 | 60192527 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,089,239 | 0.000017 | 60192527 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,077,832 | 15.492922 | 60192527 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,507 | 86.562874 | 60192527 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 964,817 | 454.412515 | 60192527 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 955,123 | 1,621.095497 | 60192527 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 941,957 | 16,464.008264 | 60192527 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | USDC/VVV | 3000 | 935,296 | 0.047653 | 60192527 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/AERO | 3000 | 930,863 | 4,093.894686 | 60192527 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 925,867 | 76.487976 | 60192527 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/doginme | 10000 | 855,493 | 30,679,878.277765 | 60192527 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 765,541 | 510,266.985985 | 60192527 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 746,791 | 0.000000 | 60192527 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 746,712 | 21,498,650.999868 | 60192527 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 745,729 | 76.934899 | 60192527 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4805 | 741,798 | 23.472566 | 60192527 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 740,647 | 0.001530 | 60192527 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | XDP/USDC | 100 | 704,923 | 0.013976 | 60192527 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 701,730 | 0.043763 | 60192527 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 690,789 | 1,058.272686 | 60192527 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/USDC | 3000 | 690,432 | 1,620.974263 | 60192527 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | uXRP/WETH | 3000 | 649,504 | 0.000610 | 60192527 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | WETH/USDC | 500 | 644,957 | 1,616.937298 | 60192527 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | TIG/USDC | 10000 | 553,497 | 0.386537 | 60192527 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 549,978 | 0.799406 | 60192527 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 531,444 | 1,617.333975 | 60192527 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 523,784 | 4,558,459.012288 | 60192527 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 504,583 | 4,125.723362 | 60192527 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 488,378 | 0.030736 | 60192527 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 479,238 | 507,940.841060 | 60192527 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 474,523 | 1.459373 | 60192527 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| pancakeswap_v3 | ELSA/USDC | 100 | 459,911 | 0.065578 | 60192527 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 10000 | 446,591 | 1,613.105205 | 60192527 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v2 | WETH/NPC | 3000 | 424,672 | 185,576.372282 | 60192527 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 417,472 | 0.000007 | 60192527 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 376,253 | 1,058.723603 | 60192527 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 367,842 | 824,492.317792 | 60192527 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 366,332 | 21.822871 | 60192527 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | AWE/USDC | 3000 | 362,619 | 0.054677 | 60192527 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/DEGEN | 3000 | 350,695 | 2,377,915.129591 | 60192527 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |
| uniswap_v3 | WETH/UNI | 10000 | 347,485 | 364.744931 | 60192527 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2721 | 340,901 | 77.008580 | 60192527 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 35072 ; routes examinées : 429842432 ; candidats optimisés : 593542 ; net attendu > 0 : 442 ; dernier cycle 2481.2 ms
- Rejets (moteur) : {'spread_below_threshold': 420005264, 'liquidity_below_min': 6582467, 'negative_expected_net': 593100, 'borrow_bound_too_small': 68046, 'pool_quarantined': 4224, 'unquotable': 2333, 'cycle_budget_exhausted': 1914, 'no_price_reference': 6}
- Enregistrements de la session : 330489 ; net attendu > 0 : 442 ; simulés (eth_call de la vraie tx) : 28 (ok 5, échec 23) ; étiquettes ghost N+1 : 7/23 positives
- Décisions : {'REJECTED': 330489} ; motifs de rejet : {'below_safety_margin': 365, 'negative_expected_net': 330047, 'p_lower_below_threshold': 430, 'price_impact': 3, 'reliability_not_demonstrated': 12, 'sim_below_estimate': 1, 'simulation_failed': 23, 'stale_data': 50}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60110169 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 441.669958 USDC | 0.179140 USDC | 0.000000 USDC | 0.003671 USDC | 0.175469 USDC (0.1614 €) | — | 3.97 | 0.083 (n=121) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.274289 WETH | 0.000111 WETH | 0.000000 WETH | 0.000002 WETH | 0.000109 WETH (0.1614 €) | — | 3.96 | 0.083 (n=121) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 388.462712 USDC | 0.140972 USDC | 0.000000 USDC | 0.004908 USDC | 0.136064 USDC (0.1252 €) | — | 3.50 | 0.225 (n=1323) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.236296 WETH | 0.000087 WETH | 0.000000 WETH | 0.000003 WETH | 0.000084 WETH (0.1250 €) | — | 3.56 | 0.225 (n=1323) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 60110169 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006181 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1248 €) | — | 3.72 | 0.225 (n=1323) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 431.212801 USDC | 0.138715 USDC | 0.000000 USDC | 0.003916 USDC | 0.134799 USDC (0.1240 €) | — | 3.13 | 0.076 (n=514) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 60110169 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.266734 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000083 WETH (0.1240 €) | — | 3.13 | 0.076 (n=514) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.372077 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0634 €) | — | 1.14 | 0.280 (n=1682) | REJECTED | below_safety_margin(42547535035600<74415482743994), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 588.718473 USDC | 0.074138 USDC | 0.000000 USDC | 0.005394 USDC | 0.068744 USDC (0.0632 €) | — | 1.17 | 0.280 (n=1682) | REJECTED | below_safety_margin(68744<117743), p_lower_below_threshold(0.28<0.75) |
| 60122237 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.009313 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0630 €) | — | 1.25 | 0.280 (n=1682) | REJECTED | below_safety_margin(116<186), p_lower_below_threshold(0.28<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.253918 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0626 €) | — | 1.65 | 0.167 (n=46) | REJECTED | below_safety_margin(42015363744851<50783606376479), p_lower_below_threshold(0.17<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 411.277784 USDC | 0.073158 USDC | 0.000000 USDC | 0.005148 USDC | 0.068010 USDC (0.0626 €) | — | 1.65 | 0.167 (n=46) | REJECTED | below_safety_margin(68010<82255), p_lower_below_threshold(0.17<0.75) |
| 60122237 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006415 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0625 €) | — | 1.79 | 0.167 (n=46) | REJECTED | below_safety_margin(115<128), p_lower_below_threshold(0.17<0.75) |
| 60122237 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004193 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0380 €) | — | 1.67 | 0.280 (n=1682) | REJECTED | below_safety_margin(70<83), p_lower_below_threshold(0.28<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.162854 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0378 €) | — | 1.56 | 0.280 (n=1682) | REJECTED | below_safety_margin(25340036603883<32570824124865), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 266.226905 USDC | 0.046028 USDC | 0.000000 USDC | 0.005148 USDC | 0.040880 USDC (0.0376 €) | — | 1.54 | 0.280 (n=1682) | REJECTED | below_safety_margin(40880<53245), p_lower_below_threshold(0.28<0.75) |
| 60122237 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004256 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0359 €) | — | 1.55 | 0.280 (n=1682) | REJECTED | below_safety_margin(66<85), p_lower_below_threshold(0.28<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.155427 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0357 €) | — | 1.54 | 0.280 (n=1682) | REJECTED | below_safety_margin(23984509100727<31085346828228), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 241.647917 USDC | 0.043637 USDC | 0.000000 USDC | 0.004903 USDC | 0.038734 USDC (0.0356 €) | — | 1.60 | 0.280 (n=1682) | REJECTED | below_safety_margin(38734<48329), p_lower_below_threshold(0.28<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 153.346101 USDC | 0.037729 USDC | 0.000000 USDC | 0.005148 USDC | 0.032581 USDC (0.0300 €) | — | 2.12 | 0.167 (n=46) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 60122237 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002420 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0299 €) | — | 2.27 | 0.167 (n=46) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 60122237 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.097075 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0298 €) | — | 2.06 | 0.167 (n=46) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 60122237 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.135846 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000019 WETH (0.0290 €) | — | 1.43 | 0.110 (n=381) | REJECTED | below_safety_margin(19439958078170<27169166854218), p_lower_below_threshold(0.11<0.75) |
| 60122237 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.646673 USDC | 0.035357 USDC | 0.000000 USDC | 0.003911 USDC | 0.031446 USDC (0.0289 €) | — | 1.44 | 0.110 (n=381) | REJECTED | below_safety_margin(31446<43729), p_lower_below_threshold(0.11<0.75) |
| 60110169 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 171.483819 USDC | 0.031461 USDC | 0.000000 USDC | 0.003671 USDC | 0.027790 USDC (0.0256 €) | — | 1.62 | 0.110 (n=381) | REJECTED | below_safety_margin(27790<34296), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
