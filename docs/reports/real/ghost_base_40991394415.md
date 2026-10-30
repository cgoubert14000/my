# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T04:45:42+00:00 ; durée 137.57 min ; blocs 53268968 → 53273093 (4069 vus)

## Connexion
- Requêtes RPC : 49273 ; erreurs : 10 ; latence p50/p95 : 72.7/728.7 ms
- Rafraîchissements d'état : 4069 ; âge des données au dernier bloc : 2.91 s ; changements de frais LP observés (pools à frais dynamiques) : 9480
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 74349 ; cycles déclenchés par événement : 4780 ; avance médiane sur le rafraîchissement multicall : 333 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,236.28 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 287 jetons, 18448 routes
- Par DEX : uniswap_v3 134, aerodrome 205, aerodrome_slipstream 111, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 314, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 2 → gardés 492 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2206.596047, 'cbBTC': 77084.188033, 'AERO': 0.611873}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,487,901 | 2,236.283198 | 53273093 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,132,166 | 0.028682 | 53273093 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,499,944 | 0.000013 | 53273093 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,065,296 | 0.028642 | 53273093 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,096,289 | 2,241.550958 | 53273093 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,832,710 | 98.770531 | 53273093 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,753,049 | 0.001624 | 53273093 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,007,704 | 1.645239 | 53273093 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,585,207 | 0.028678 | 53273093 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,129,867 | 2,242.427672 | 53273093 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,763,293 | 2,242.252933 | 53273093 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,651,259 | 1.000327 | 53273093 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,496,142 | 38,291.661811 | 53273093 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,770,704 | 0.028628 | 53273093 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,341,194 | 98.749057 | 53273093 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,039,053 | 1,219,455.565885 | 53273093 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,932,332 | 0.000013 | 53273093 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,772,892 | 0.018380 | 53273093 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,683,582 | 416.739082 | 53273093 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,672,879 | 0.000000 | 53273093 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,644,736 | 0.000013 | 53273093 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,622,442 | 0.000013 | 53273093 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/USDC | 3000 | 1,540,590 | 2,236.607287 | 53273093 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,474,018 | 0.000013 | 53273093 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,839 | 1.641584 | 53273093 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,017 | 0.825881 | 53273093 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,378,715 | 3,687.538276 | 53273093 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,314,516 | 14,530.507644 | 53273093 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,278 | 0.005153 | 53273093 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,294,320 | 2,241.840610 | 53273093 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,295 | 69.989676 | 53273093 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,102,603 | 36,524,857.692141 | 53273093 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,792 | 518,958.482200 | 53273093 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,014,473 | 74,220.380188 | 53273093 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,011,964 | 21,854,128.078081 | 53273093 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v2 | WETH/USDC | 3000 | 1,008,169 | 2,236.536938 | 53273093 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,003,147 | 18.779086 | 53273093 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 997,881 | 0.000000 | 53273093 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/VVV | 10000 | 959,752 | 98.857988 | 53273093 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 944,913 | 70.113124 | 53273093 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 936,677 | 3,660.029181 | 53273093 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/VVV | 3000 | 935,509 | 0.044051 | 53273093 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 917,916 | 2,220.594991 | 53273093 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 916,325 | 1,245,271.117674 | 53273093 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,782 | 0.000556 | 53273093 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 858,286 | 1,113.402635 | 53273093 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 835,756 | 19.502001 | 53273093 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 818,440 | 0.060219 | 53273093 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 783,365 | 18.076621 | 53273093 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 756,943 | 0.803616 | 53273093 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 724,990 | 0.000254 | 53273093 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 705,524 | 4,745,507.649224 | 53273093 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 698,085 | 0.572332 | 53273093 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 684,364 | 0.000008 | 53273093 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 681,106 | 2.331282 | 53273093 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 652,565 | 519,375.691686 | 53273093 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 648,712 | 149,776.626242 | 53273093 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 644,004 | 0.523725 | 53273093 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,204 | 0.091693 | 53273093 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 601,580 | 0.914226 | 53273093 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 8848 ; routes examinées : 163227904 ; candidats optimisés : 953274 ; net attendu > 0 : 1020 ; dernier cycle 269.5 ms
- Rejets (moteur) : {'spread_below_threshold': 159501160, 'liquidity_below_min': 2584095, 'negative_expected_net': 952254, 'pool_quarantined': 165584, 'unquotable': 14629, 'borrow_bound_too_small': 8845, 'cycle_budget_exhausted': 317}
- Enregistrements de la session : 953274 ; net attendu > 0 : 1020 ; simulés (eth_call de la vraie tx) : 88 (ok 44, échec 44) ; étiquettes ghost N+1 : 3/55 positives
- Décisions : {'REJECTED': 953274} ; motifs de rejet : {'below_safety_margin': 719, 'negative_expected_net': 952254, 'p_lower_below_threshold': 904, 'reliability_not_demonstrated': 116, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 44}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53269162 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 884.830547 USDC | 0.122047 USDC | 0.000000 USDC | 0.007241 USDC | 0.114806 USDC (0.1056 €) | — | 1.30 | 0.001 (n=14) | REJECTED | below_safety_margin(114806<176966), reliability_not_demonstrated |
| 53269162 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.012045 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1056 €) | — | 1.24 | 0.001 (n=14) | REJECTED | below_safety_margin(149<240), reliability_not_demonstrated |
| 53269162 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.421345 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1055 €) | — | 1.23 | 0.001 (n=14) | REJECTED | below_safety_margin(51939327494826<84268925462009), reliability_not_demonstrated |
| 53271018 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.045191 WETH | 0.000045 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0872 €) | 0.000043 WETH | 9.47 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53271018 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.045191 WETH | 0.000045 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0872 €) | — | 9.47 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53272621 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 792.336287 USDC | 0.093450 USDC | 0.000000 USDC | 0.005424 USDC | 0.088026 USDC (0.0810 €) | — | 1.11 | 0.032 (n=133) | REJECTED | below_safety_margin(88026<158467), p_lower_below_threshold(0.03<0.75) |
| 53272622 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 792.336287 USDC | 0.093450 USDC | 0.000000 USDC | 0.005424 USDC | 0.088026 USDC (0.0810 €) | — | 1.11 | 0.032 (n=133) | REJECTED | below_safety_margin(88026<158467), p_lower_below_threshold(0.03<0.75) |
| 53272621 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.355379 WETH | 0.000042 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0808 €) | — | 1.11 | 0.032 (n=133) | REJECTED | below_safety_margin(39300506553016<71075766436879), p_lower_below_threshold(0.03<0.75) |
| 53272622 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.355379 WETH | 0.000042 WETH | 0.000000 WETH | 0.000002 WETH | 0.000039 WETH (0.0808 €) | — | 1.11 | 0.032 (n=133) | REJECTED | below_safety_margin(39300506553016<71075766436879), p_lower_below_threshold(0.03<0.75) |
| 53271018 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.043099 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0623 €) | 0.000031 WETH | 7.09 | 0.199 (n=69) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53271018 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.043099 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0623 €) | — | 7.09 | 0.199 (n=69) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001161 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0620 €) | — | 7.49 | 0.199 (n=69) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001161 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0620 €) | — | 7.49 | 0.199 (n=69) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53271018 | WETH→[uniswap_v3]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.039508 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0533 €) | 0.000026 WETH | 6.62 | 0.092 (n=175) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53271018 | WETH→[uniswap_v3]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.039508 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0533 €) | — | 6.62 | 0.092 (n=175) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.001036 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0527 €) | — | 7.15 | 0.092 (n=175) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.001036 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0527 €) | — | 7.15 | 0.092 (n=175) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53269162 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.367867 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0524 €) | — | 0.70 | 0.135 (n=540) | REJECTED | below_safety_margin(25826590791060<73573344629983), p_lower_below_threshold(0.13<0.75) |
| 53269162 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.010214 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0524 €) | — | 0.72 | 0.135 (n=540) | REJECTED | below_safety_margin(74<204), p_lower_below_threshold(0.13<0.75) |
| 53269162 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 830.311808 USDC | 0.064150 USDC | 0.000000 USDC | 0.007241 USDC | 0.056909 USDC (0.0524 €) | — | 0.69 | 0.135 (n=540) | REJECTED | below_safety_margin(56909<166062), p_lower_below_threshold(0.13<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.001056 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0506 €) | — | 6.72 | 0.092 (n=175) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.001056 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0506 €) | — | 6.72 | 0.092 (n=175) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53271018 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.034494 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0505 €) | — | 7.18 | 0.092 (n=175) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53271018 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.034494 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0505 €) | — | 7.18 | 0.092 (n=175) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53272343 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 101.331638 USDC | 0.059842 USDC | 0.000000 USDC | 0.006871 USDC | 0.052971 USDC (0.0487 €) | — | 5.23 | 0.196 (n=70) | REJECTED | p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 3531 ; taux observé 0.113 ; borne inférieure crédible (0.9) 0.106 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
