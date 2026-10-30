# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T03:48:40+00:00 ; durée 80.53 min ; blocs 53268968 → 53271382 (2402 vus)

## Connexion
- Requêtes RPC : 29194 ; erreurs : 5 ; latence p50/p95 : 72.5/888.9 ms
- Rafraîchissements d'état : 2402 ; âge des données au dernier bloc : 3.92 s ; changements de frais LP observés (pools à frais dynamiques) : 5815
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 46426 ; cycles déclenchés par événement : 2798 ; avance médiane sur le rafraîchissement multicall : 902 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,225.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 287 jetons, 18448 routes
- Par DEX : uniswap_v3 134, aerodrome 205, aerodrome_slipstream 111, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 314, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 2 → gardés 492 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2206.596047, 'cbBTC': 77084.188033, 'AERO': 0.611873}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,930,498 | 2,225.237032 | 53271382 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,062,436 | 0.028617 | 53271382 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,489,273 | 0.000013 | 53271382 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,034,089 | 0.028642 | 53271382 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,060,303 | 2,230.816768 | 53271382 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,798,227 | 98.663979 | 53271382 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,734,768 | 0.001625 | 53271382 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,063,408 | 1.615235 | 53271382 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,560,399 | 0.028629 | 53271382 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,123,702 | 2,231.515490 | 53271382 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,747,301 | 2,231.596258 | 53271382 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,563,674 | 1.000384 | 53271382 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,473,403 | 38,412.345082 | 53271382 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,758,246 | 0.028628 | 53271382 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,314,429 | 98.623526 | 53271382 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,028,981 | 1,219,455.577691 | 53271382 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,928,286 | 0.000013 | 53271382 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,021 | 0.018328 | 53271382 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,678,693 | 414.206265 | 53271382 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,664,692 | 0.000000 | 53271382 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,643,018 | 0.000013 | 53271382 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,618,559 | 0.000013 | 53271382 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/USDC | 3000 | 1,538,184 | 2,224.991883 | 53271382 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,471,120 | 0.000013 | 53271382 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,839 | 1.641584 | 53271382 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,984 | 0.826796 | 53271382 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,342,746 | 3,603.402941 | 53271382 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,046 | 14,497.526603 | 53271382 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,302,595 | 0.005171 | 53271382 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,297,317 | 2,230.792563 | 53271382 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,295 | 69.989676 | 53271382 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,163,552 | 0.000256 | 53271382 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | WETH/doginme | 10000 | 1,097,211 | 36,519,405.774328 | 53271382 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,045,891 | 519,929.168150 | 53271382 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,011,526 | 73,917.731314 | 53271382 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,006,368 | 18.609016 | 53271382 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,005,672 | 2,225.233420 | 53271382 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,004,151 | 21,930,020.840588 | 53271382 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 992,727 | 0.000000 | 53271382 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/VVV | 10000 | 955,522 | 99.322341 | 53271382 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 942,996 | 3,594.057929 | 53271382 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/NOCK | 3000 | 940,200 | 70.817715 | 53271382 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 932,111 | 0.044237 | 53271382 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 915,890 | 2,209.613470 | 53271382 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 908,141 | 1,255,321.656041 | 53271382 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 861,338 | 1,099.807502 | 53271382 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 855,445 | 0.000553 | 53271382 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 833,383 | 19.585851 | 53271382 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | VIRTUAL/WETH | 10000 | 825,427 | 0.000254 | 53271382 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,540 | 0.059298 | 53271382 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 780,082 | 18.061658 | 53271382 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 753,204 | 0.803616 | 53271382 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 702,051 | 4,745,287.374317 | 53271382 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 699,955 | 0.571148 | 53271382 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 691,594 | 0.000008 | 53271382 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 677,970 | 2.330114 | 53271382 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 648,699 | 518,016.738965 | 53271382 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 643,841 | 0.523473 | 53271382 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 642,366 | 151,233.857442 | 53271382 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,235 | 0.091703 | 53271382 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 5199 ; routes examinées : 95911152 ; candidats optimisés : 596827 ; net attendu > 0 : 760 ; dernier cycle 593.7 ms
- Rejets (moteur) : {'spread_below_threshold': 93737045, 'liquidity_below_min': 1561589, 'negative_expected_net': 596067, 'unquotable': 10396, 'borrow_bound_too_small': 5198, 'cycle_budget_exhausted': 97}
- Enregistrements de la session : 596827 ; net attendu > 0 : 760 ; simulés (eth_call de la vraie tx) : 61 (ok 33, échec 28) ; étiquettes ghost N+1 : 3/37 positives
- Décisions : {'REJECTED': 596827} ; motifs de rejet : {'below_safety_margin': 573, 'negative_expected_net': 596067, 'p_lower_below_threshold': 676, 'reliability_not_demonstrated': 84, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 28}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53269162 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 884.830547 USDC | 0.122047 USDC | 0.000000 USDC | 0.007241 USDC | 0.114806 USDC (0.1056 €) | — | 1.30 | 0.001 (n=14) | REJECTED | below_safety_margin(114806<176966), reliability_not_demonstrated |
| 53269162 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.012045 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1056 €) | — | 1.24 | 0.001 (n=14) | REJECTED | below_safety_margin(149<240), reliability_not_demonstrated |
| 53269162 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.421345 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1055 €) | — | 1.23 | 0.001 (n=14) | REJECTED | below_safety_margin(51939327494826<84268925462009), reliability_not_demonstrated |
| 53271018 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.045191 WETH | 0.000045 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0872 €) | 0.000043 WETH | 9.47 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53271018 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.045191 WETH | 0.000045 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0872 €) | — | 9.47 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
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
| 53271018 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.039509 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0456 €) | — | 5.67 | 0.199 (n=69) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53271018 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.039509 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0456 €) | — | 5.67 | 0.199 (n=69) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001011 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0456 €) | — | 6.33 | 0.199 (n=69) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53271018 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.001011 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0456 €) | — | 6.33 | 0.199 (n=69) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53271018 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 56.608149 USDC | 0.054963 USDC | 0.000000 USDC | 0.006525 USDC | 0.048438 USDC (0.0446 €) | — | 8.56 | 0.086 (n=25) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3513 ; taux observé 0.114 ; borne inférieure crédible (0.9) 0.107 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
