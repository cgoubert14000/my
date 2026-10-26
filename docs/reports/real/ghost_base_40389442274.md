# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T20:21:01+00:00 ; durée 30.32 min ; blocs 53127443 → 53128355 (900 vus)

## Connexion
- Requêtes RPC : 11211 ; erreurs : 0 ; latence p50/p95 : 278.6/1,318.1 ms
- Rafraîchissements d'état : 900 ; âge des données au dernier bloc : 5.09 s ; changements de frais LP observés (pools à frais dynamiques) : 1319
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10284 ; cycles déclenchés par événement : 1287 ; avance médiane sur le rafraîchissement multicall : 909 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,315.80 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19514 routes
- Par DEX : uniswap_v3 143 (quarantaine 2), aerodrome 213, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 190 (rejetés 2) → 595 jetons ; pools candidats 3792 (énumérés 342, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2315.799118, 'cbBTC': 79865.457277, 'AERO': 0.681738}
- Pools en quarantaine : 2 — uniswap_v3:USDC/BASECAT@0x229065: simulation failed ×5 (model/chain mismatch) — until block 53128377; uniswap_v3:WETH/BASECAT@0xf79478: simulation failed ×5 (model/chain mismatch) — until block 53128377

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,835,198 | 2,315.798811 | 53128354 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,676,486 | 0.028978 | 53128354 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,145,019 | 0.028964 | 53128354 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,468,714 | 0.000013 | 53128354 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,874,690 | 92.127265 | 53128354 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,318,001 | 2,311.602798 | 53128354 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,027,999 | 1.482783 | 53128354 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,958,732 | 0.001641 | 53128354 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,358,364 | 0.028966 | 53128354 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,261,578 | 2,311.001184 | 53128354 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,507,054 | 2,310.783720 | 53128354 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,205,859 | 0.999561 | 53128354 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,778,679 | 35,156.703861 | 53128354 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,361,459 | 2,316.808988 | 53128354 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,190,594 | 0.028951 | 53128354 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,506,066 | 92.158606 | 53128354 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,448,671 | 0.000013 | 53128354 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,121,955 | 1,207,531.602222 | 53128354 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,901,526 | 0.000012 | 53128354 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,833,330 | 0.000000 | 53128354 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,814,632 | 0.018356 | 53128354 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,751,503 | 408.257346 | 53128354 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,679 | 0.000013 | 53128354 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,688,137 | 0.000013 | 53128354 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,550,619 | 0.000266 | 53128354 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,482,662 | 0.005758 | 53128354 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,036 | 0.825844 | 53128354 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53128354 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,428,057 | 3,429.545583 | 53128354 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,362,640 | 14,079.867347 | 53128354 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,233,643 | 0.000266 | 53128354 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,650 | 65.538581 | 53128354 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,206,745 | 3,405.064240 | 53128354 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,182,945 | 2,311.710252 | 53128354 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,146,173 | 0.000000 | 53128354 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,137,002 | 1,088,409.510469 | 53128354 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,134,851 | 37,123,987.616527 | 53128354 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,104,796 | 498,598.939159 | 53128354 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,068,803 | 71,938.876024 | 53128354 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,060,860 | 20,276,651.098435 | 53128354 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,051,021 | 56.669412 | 53128354 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,026,464 | 17.606372 | 53128354 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,004,610 | 0.039853 | 53128354 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 951,339 | 2,317.651230 | 53128354 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,570 | 1,094.365559 | 53128354 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 905,234 | 2.309155 | 53128354 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,312 | 0.000557 | 53128354 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,135 | 18.001612 | 53128354 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 875,463 | 17.127755 | 53128354 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 869,508 | 91.816271 | 53128354 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,080 | 2,317.655226 | 53128354 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 797,610 | 0.000008 | 53128354 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,098 | 0.056820 | 53128354 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 784,087 | 0.803146 | 53128354 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 735,872 | 0.614354 | 53128354 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 732,606 | 4,717,274.286968 | 53128354 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 698,961 | 0.614411 | 53128354 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 698,783 | 138,225.760033 | 53128354 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 690,478 | 501,012.974791 | 53128354 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 677,274 | 0.109684 | 53128354 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 2186 ; routes examinées : 42657604 ; candidats optimisés : 111618 ; net attendu > 0 : 127 ; dernier cycle 533.2 ms
- Rejets (moteur) : {'spread_below_threshold': 41930838, 'liquidity_below_min': 529864, 'negative_expected_net': 111491, 'unquotable': 46544, 'pool_quarantined': 36400, 'borrow_bound_too_small': 2185, 'cycle_budget_exhausted': 155}
- Enregistrements de la session : 111618 ; net attendu > 0 : 127 ; simulés (eth_call de la vraie tx) : 15 (ok 0, échec 15) ; étiquettes ghost N+1 : 0/15 positives
- Décisions : {'REJECTED': 111618} ; motifs de rejet : {'below_safety_margin': 73, 'negative_expected_net': 111491, 'p_lower_below_threshold': 106, 'reliability_not_demonstrated': 21, 'simulation_failed': 15}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53127765 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.512672 WETH | 0.000064 WETH | 0.000000 WETH | 0.000002 WETH | 0.000062 WETH (0.1324 €) | — | 1.21 | 0.021 (n=101) | REJECTED | below_safety_margin(62127277652393<102534382357389), p_lower_below_threshold(0.02<0.75) |
| 53127765 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,182.521916 USDC | 0.148852 USDC | 0.000000 USDC | 0.005202 USDC | 0.143650 USDC (0.1322 €) | — | 1.21 | 0.021 (n=101) | REJECTED | below_safety_margin(143650<236504), p_lower_below_threshold(0.02<0.75) |
| 53127765 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.235656 WETH | 0.000061 WETH | 0.000000 WETH | 0.000002 WETH | 0.000059 WETH (0.1258 €) | — | 2.51 | 0.015 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53127765 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 543.411552 USDC | 0.141726 USDC | 0.000000 USDC | 0.005202 USDC | 0.136524 USDC (0.1256 €) | — | 2.51 | 0.015 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53127902 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.021799 WETH | 0.000052 WETH | 0.000000 WETH | 0.000003 WETH | 0.000049 WETH (0.1036 €) | — | 22.31 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53127902 | USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 50.409900 USDC | 0.119432 USDC | 0.000000 USDC | 0.006962 USDC | 0.112470 USDC (0.1035 €) | — | 22.31 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127902 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.021471 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1009 €) | — | 22.06 | 0.000 (n=33) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53127902 | USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 49.653387 USDC | 0.116513 USDC | 0.000000 USDC | 0.006962 USDC | 0.109551 USDC (0.1008 €) | — | 22.06 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127867 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[uniswap_v3]→WETH | 0.053391 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.0998 €) | — | 8.77 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53127902 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.022044 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.0996 €) | — | 21.22 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53127902 | USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 50.978307 USDC | 0.115108 USDC | 0.000000 USDC | 0.006962 USDC | 0.108146 USDC (0.0995 €) | — | 21.21 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53127902 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.019731 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.0986 €) | — | 23.45 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127902 | USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 45.615958 USDC | 0.113927 USDC | 0.000000 USDC | 0.006962 USDC | 0.106965 USDC (0.0984 €) | — | 23.45 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127867 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→wstETH→[aerodrome_slipstream]→WETH | 0.051674 WETH | 0.000047 WETH | 0.000000 WETH | 0.000003 WETH | 0.000044 WETH (0.0941 €) | — | 8.55 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53127765 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.206610 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0926 €) | — | 2.10 | 0.132 (n=374) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53127765 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.005724 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0926 €) | — | 2.20 | 0.132 (n=374) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53127765 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 477.937119 USDC | 0.107545 USDC | 0.000000 USDC | 0.006962 USDC | 0.100583 USDC (0.0925 €) | — | 2.10 | 0.132 (n=374) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53127902 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.017412 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0787 €) | — | 21.22 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127902 | USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 40.251536 USDC | 0.092363 USDC | 0.000000 USDC | 0.006962 USDC | 0.085401 USDC (0.0786 €) | — | 21.22 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127902 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.016341 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0783 €) | — | 22.50 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127902 | USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 37.772453 USDC | 0.091925 USDC | 0.000000 USDC | 0.006962 USDC | 0.084963 USDC (0.0782 €) | — | 22.49 | 0.000 (n=33) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127902 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH | 0.017386 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0755 €) | — | 20.39 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53127902 | USDC→[uniswap_v3]→BASECAT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 40.187867 USDC | 0.088909 USDC | 0.000000 USDC | 0.006962 USDC | 0.081947 USDC (0.0754 €) | — | 20.39 | 0.000 (n=25) | REJECTED | reliability_not_demonstrated |
| 53127867 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDbC→[aerodrome_slipstream]→USDC | 80.993638 USDC | 0.082281 USDC | 0.000000 USDC | 0.006643 USDC | 0.075638 USDC (0.0696 €) | — | 9.34 | 0.024 (n=149) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53127765 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010946 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0662 €) | — | 0.82 | 0.132 (n=374) | REJECTED | below_safety_margin(90<218), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2743 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
