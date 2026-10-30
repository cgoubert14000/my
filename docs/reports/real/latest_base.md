# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T15:40:26+00:00 ; durée 118.52 min ; blocs 53289181 → 53292735 (3527 vus)

## Connexion
- Requêtes RPC : 42594 ; erreurs : 0 ; latence p50/p95 : 70.3/501.9 ms
- Rafraîchissements d'état : 3527 ; âge des données au dernier bloc : 2.78 s ; changements de frais LP observés (pools à frais dynamiques) : 11120
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 94519 ; cycles déclenchés par événement : 4129 ; avance médiane sur le rafraîchissement multicall : 876 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,231.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,085,064 | 2,231.573513 | 53292736 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,925,411 | 0.028796 | 53292736 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,587,421 | 0.000013 | 53292736 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,035,629 | 0.028862 | 53292736 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,164,932 | 2,231.513209 | 53292736 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,735,873 | 100.712742 | 53292736 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,652,360 | 0.001595 | 53292736 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,096,589 | 1.591346 | 53292736 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,544,575 | 0.028806 | 53292736 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 743 | 4,166,063 | 2,231.413341 | 53292736 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,076,593 | 0.999937 | 53292736 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,046,201 | 2,231.324313 | 53292736 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,554,685 | 36,884.910243 | 53292736 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 2,756,105 | 0.028850 | 53292736 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2835 | 2,326,059 | 100.736916 | 53292736 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,045,786 | 1,206,344.208581 | 53292736 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,922,100 | 0.000013 | 53292736 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,736,875 | 0.017694 | 53292736 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,713,619 | 0.000000 | 53292736 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,678,449 | 418.067239 | 53292736 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,666,664 | 0.000013 | 53292736 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,563,909 | 0.000013 | 53292736 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,520,539 | 2,232.119975 | 53292736 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 1,468,325 | 0.000013 | 53292736 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,461,592 | 1.645227 | 53292736 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,271 | 0.825377 | 53292736 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,411,605 | 3,553.749015 | 53292736 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,307,439 | 2,231.463307 | 53292736 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,307,309 | 14,501.864188 | 53292736 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,263,864 | 0.004969 | 53292736 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,053 | 70.018466 | 53292736 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,099,888 | 36,393,428.156047 | 53292736 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,052,562 | 515,828.680705 | 53292736 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,030,927 | 21,083,127.034335 | 53292736 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,014,199 | 0.000000 | 53292736 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,010,691 | 74,455.367602 | 53292736 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,007,186 | 2,231.974497 | 53292736 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,798 | 19.234636 | 53292736 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 981,906 | 64.930141 | 53292736 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 961,923 | 100.019942 | 53292736 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 942,403 | 0.045160 | 53292736 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 924,922 | 1,217,084.590838 | 53292736 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 918,651 | 2,235.963227 | 53292736 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 887,019 | 1,068.608182 | 53292736 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 864,819 | 3,545.501696 | 53292736 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 859,936 | 0.000556 | 53292736 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 838,015 | 19.427217 | 53292736 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 808,590 | 0.058684 | 53292736 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 792,854 | 17.778787 | 53292736 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 755,349 | 0.803616 | 53292736 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,129 | 0.000262 | 53292736 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 716,002 | 4,588,674.616720 | 53292736 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 715,416 | 0.587997 | 53292736 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 697,419 | 0.000008 | 53292736 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,493 | 2.332194 | 53292736 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 654,527 | 146,538.522426 | 53292736 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 653,316 | 516,898.568776 | 53292736 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 637,238 | 0.512952 | 53292736 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,347 | 0.091694 | 53292736 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 600,166 | 0.914674 | 53292736 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 7655 ; routes examinées : 143439390 ; candidats optimisés : 866085 ; net attendu > 0 : 4024 ; dernier cycle 74.7 ms
- Rejets (moteur) : {'spread_below_threshold': 139860117, 'liquidity_below_min': 2328021, 'negative_expected_net': 862061, 'pool_quarantined': 338566, 'unquotable': 35611, 'borrow_bound_too_small': 7653, 'cycle_budget_exhausted': 3337}
- Enregistrements de la session : 866085 ; net attendu > 0 : 4024 ; simulés (eth_call de la vraie tx) : 184 (ok 121, échec 63) ; étiquettes ghost N+1 : 35/112 positives
- Décisions : {'REJECTED': 866085} ; motifs de rejet : {'below_safety_margin': 3499, 'negative_expected_net': 862061, 'p_lower_below_threshold': 3661, 'reliability_not_demonstrated': 363, 'sim_below_estimate': 20, 'simulated_net_nonpositive': 3, 'simulation_failed': 63}

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
- Observations ghost : 3762 ; taux observé 0.122 ; borne inférieure crédible (0.9) 0.115 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
