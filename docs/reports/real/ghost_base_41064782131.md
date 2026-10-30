# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T15:46:44+00:00 ; durée 124.81 min ; blocs 53289181 → 53292923 (3712 vus)

## Connexion
- Requêtes RPC : 44807 ; erreurs : 0 ; latence p50/p95 : 61.3/553.2 ms
- Rafraîchissements d'état : 3712 ; âge des données au dernier bloc : 3.15 s ; changements de frais LP observés (pools à frais dynamiques) : 11746
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 99598 ; cycles déclenchés par événement : 4342 ; avance médiane sur le rafraîchissement multicall : 835 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,960,418 | 2,229.059574 | 53292924 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,911,516 | 0.028761 | 53292924 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,593,235 | 0.000013 | 53292924 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,029,259 | 0.028833 | 53292924 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,157,018 | 2,223.626934 | 53292924 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,722,661 | 100.830079 | 53292924 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,647,604 | 0.001593 | 53292924 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,081,730 | 1.599131 | 53292924 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,540,017 | 0.028771 | 53292924 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 713 | 4,162,272 | 2,224.953242 | 53292924 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,077,179 | 0.999926 | 53292924 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,042,557 | 2,224.255201 | 53292924 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,550,681 | 36,884.910243 | 53292924 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2545 | 2,753,757 | 0.028819 | 53292924 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,321,942 | 100.865978 | 53292924 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,043,481 | 1,206,344.208581 | 53292924 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 1,922,277 | 0.000013 | 53292924 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,732,007 | 0.017617 | 53292924 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,711,721 | 0.000000 | 53292924 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,675,928 | 418.472212 | 53292924 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,666,848 | 0.000013 | 53292924 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,564,029 | 0.000013 | 53292924 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,519,682 | 2,228.942817 | 53292924 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,468,476 | 0.000013 | 53292924 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,461,592 | 1.645227 | 53292924 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,271 | 0.825377 | 53292924 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,407,005 | 3,557.745026 | 53292924 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,306,471 | 2,223.529686 | 53292924 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,306,197 | 14,506.207757 | 53292924 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,262,440 | 0.004969 | 53292924 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,053 | 70.018466 | 53292924 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,649 | 36,393,428.156047 | 53292924 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,380 | 515,823.603752 | 53292924 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,029,765 | 21,083,127.034335 | 53292924 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,013,944 | 0.000000 | 53292924 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,009,683 | 74,436.147958 | 53292924 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,619 | 2,229.588727 | 53292924 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 992,793 | 19.347105 | 53292924 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 982,066 | 64.909062 | 53292924 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 960,170 | 100.122700 | 53292924 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 940,785 | 0.045359 | 53292924 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 923,881 | 1,217,084.590838 | 53292924 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 918,586 | 2,235.963227 | 53292924 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 884,252 | 1,072.307550 | 53292924 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 862,228 | 3,545.501696 | 53292924 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 858,967 | 0.000556 | 53292924 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4615 | 836,199 | 19.491790 | 53292924 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 808,605 | 0.058687 | 53292924 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 791,128 | 17.799104 | 53292924 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,498 | 0.803616 | 53292924 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 729,306 | 0.000262 | 53292924 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 715,390 | 4,586,179.137619 | 53292924 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 714,776 | 0.587835 | 53292924 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 695,495 | 0.000008 | 53292924 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 678,900 | 2.331312 | 53292924 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 653,889 | 146,494.227034 | 53292924 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 652,585 | 517,479.684604 | 53292924 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 637,238 | 0.512952 | 53292924 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 604,371 | 0.091238 | 53292924 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 599,490 | 0.914674 | 53292924 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 8053 ; routes examinées : 150897114 ; candidats optimisés : 917931 ; net attendu > 0 : 4202 ; dernier cycle 579.6 ms
- Rejets (moteur) : {'spread_below_threshold': 147167162, 'liquidity_below_min': 2423205, 'negative_expected_net': 913729, 'pool_quarantined': 338566, 'unquotable': 38813, 'borrow_bound_too_small': 8051, 'cycle_budget_exhausted': 3386}
- Enregistrements de la session : 917931 ; net attendu > 0 : 4202 ; simulés (eth_call de la vraie tx) : 197 (ok 131, échec 66) ; étiquettes ghost N+1 : 38/121 positives
- Décisions : {'REJECTED': 917931} ; motifs de rejet : {'below_safety_margin': 3655, 'negative_expected_net': 913729, 'p_lower_below_threshold': 3809, 'reliability_not_demonstrated': 393, 'sim_below_estimate': 22, 'simulated_net_nonpositive': 3, 'simulation_failed': 66}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53289560 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 140.927016 USDC | 0.310023 USDC | 0.000000 USDC | 0.006770 USDC | 0.303253 USDC (0.2790 €) | — | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.063562 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2783 €) | 0.000137 WETH | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 134.625773 USDC | 0.296283 USDC | 0.000000 USDC | 0.007106 USDC | 0.289177 USDC (0.2660 €) | — | 21.48 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.060712 WETH | 0.000134 WETH | 0.000000 WETH | 0.000003 WETH | 0.000130 WETH (0.2653 €) | 0.000130 WETH | 21.48 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 111.503746 USDC | 0.272062 USDC | 0.000000 USDC | 0.006770 USDC | 0.265292 USDC (0.2441 €) | — | 23.79 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.050283 WETH | 0.000123 WETH | 0.000000 WETH | 0.000003 WETH | 0.000120 WETH (0.2434 €) | 0.000120 WETH | 23.79 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 110.539928 USDC | 0.269722 USDC | 0.000000 USDC | 0.006770 USDC | 0.262952 USDC (0.2419 €) | — | 23.79 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.049846 WETH | 0.000122 WETH | 0.000000 WETH | 0.000003 WETH | 0.000119 WETH (0.2413 €) | — | 23.79 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289898 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 1,075.433514 USDC | 0.229695 USDC | 0.000000 USDC | 0.005769 USDC | 0.223926 USDC (0.2060 €) | — | 2.08 | 0.008 (n=36) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53289560 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 94.442109 USDC | 0.227270 USDC | 0.000000 USDC | 0.006770 USDC | 0.220500 USDC (0.2029 €) | — | 23.35 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.042577 WETH | 0.000102 WETH | 0.000000 WETH | 0.000003 WETH | 0.000099 WETH (0.2023 €) | — | 23.35 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 87.250859 USDC | 0.224754 USDC | 0.000000 USDC | 0.007106 USDC | 0.217648 USDC (0.2002 €) | — | 24.95 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.039317 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000098 WETH (0.1996 €) | — | 24.94 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289479 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.135000 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1819 €) | — | 6.62 | 0.161 (n=223) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 297.734168 USDC | 0.204126 USDC | 0.000000 USDC | 0.006774 USDC | 0.197352 USDC (0.1816 €) | — | 6.63 | 0.161 (n=223) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53292110 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.473223 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1121 €) | — | 1.14 | 0.139 (n=610) | REJECTED | below_safety_margin(54050712639533<94644534387919), p_lower_below_threshold(0.14<0.75) |
| 53292110 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,065.815648 USDC | 0.128728 USDC | 0.000000 USDC | 0.006964 USDC | 0.121764 USDC (0.1120 €) | — | 1.14 | 0.139 (n=610) | REJECTED | below_safety_margin(121764<213163), p_lower_below_threshold(0.14<0.75) |
| 53292110 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.011580 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1118 €) | — | 1.35 | 0.139 (n=610) | REJECTED | below_safety_margin(156<231), p_lower_below_threshold(0.14<0.75) |
| 53290065 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,007.174039 USDC | 0.113535 USDC | 0.000000 USDC | 0.005397 USDC | 0.108138 USDC (0.0995 €) | — | 1.07 | 0.042 (n=141) | REJECTED | below_safety_margin(108138<201434), p_lower_below_threshold(0.04<0.75) |
| 53290065 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.012476 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0990 €) | — | 1.12 | 0.042 (n=141) | REJECTED | below_safety_margin(140<249), p_lower_below_threshold(0.04<0.75) |
| 53292110 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 903.653380 USDC | 0.103372 USDC | 0.000000 USDC | 0.007306 USDC | 0.096066 USDC (0.0884 €) | — | 1.06 | 0.139 (n=610) | REJECTED | below_safety_margin(96066<180730), p_lower_below_threshold(0.14<0.75) |
| 53292110 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 903.653380 USDC | 0.103372 USDC | 0.000000 USDC | 0.007306 USDC | 0.096066 USDC (0.0884 €) | — | 1.06 | 0.139 (n=610) | REJECTED | below_safety_margin(96066<180730), p_lower_below_threshold(0.14<0.75) |
| 53292110 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.407330 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0882 €) | — | 1.04 | 0.139 (n=610) | REJECTED | below_safety_margin(42560017048124<81465946809010), p_lower_below_threshold(0.14<0.75) |
| 53292110 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.407330 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0882 €) | — | 1.04 | 0.139 (n=610) | REJECTED | below_safety_margin(42560017048124<81465946809010), p_lower_below_threshold(0.14<0.75) |
| 53292110 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.011241 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0881 €) | — | 1.09 | 0.139 (n=610) | REJECTED | below_safety_margin(123<224), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3771 ; taux observé 0.123 ; borne inférieure crédible (0.9) 0.116 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
