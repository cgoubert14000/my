# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T20:02:49+00:00 ; durée 12.13 min ; blocs 53127443 → 53127810 (358 vus)

## Connexion
- Requêtes RPC : 4485 ; erreurs : 0 ; latence p50/p95 : 256.2/1,435.1 ms
- Rafraîchissements d'état : 359 ; âge des données au dernier bloc : 2.0 s ; changements de frais LP observés (pools à frais dynamiques) : 566
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4432 ; cycles déclenchés par événement : 530 ; avance médiane sur le rafraîchissement multicall : 567 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,315.80 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19514 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 190 (rejetés 2) → 595 jetons ; pools candidats 3792 (énumérés 342, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2315.799118, 'cbBTC': 79865.457277, 'AERO': 0.681738}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 127,777,399 | 2,315.797730 | 53127810 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,674,647 | 0.028980 | 53127810 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,144,779 | 0.028964 | 53127810 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,468,346 | 0.000013 | 53127810 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,878,691 | 92.044175 | 53127810 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,317,944 | 2,313.438636 | 53127810 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,049,968 | 1.473534 | 53127810 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,958,787 | 0.001642 | 53127810 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,358,247 | 0.028983 | 53127810 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 624 | 5,263,532 | 2,313.929617 | 53127810 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,507,185 | 2,314.043507 | 53127810 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,205,521 | 0.999561 | 53127810 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,778,688 | 35,156.502803 | 53127810 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,361,458 | 2,316.328905 | 53127810 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,184,383 | 0.028951 | 53127810 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,506,923 | 92.075859 | 53127810 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 2,448,941 | 0.000013 | 53127810 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,121,954 | 1,207,531.602222 | 53127810 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,901,446 | 0.000012 | 53127810 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,833,639 | 0.000000 | 53127810 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,820,271 | 0.018331 | 53127810 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,751,502 | 408.257453 | 53127810 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,696 | 0.000013 | 53127810 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 1,696,045 | 0.000013 | 53127810 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,550,618 | 0.000266 | 53127810 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,482,183 | 0.005756 | 53127810 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,036 | 0.825844 | 53127810 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53127810 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,432,983 | 3,409.186289 | 53127810 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,362,572 | 14,075.079579 | 53127810 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,233,642 | 0.000266 | 53127810 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,650 | 65.538581 | 53127810 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,210,522 | 3,388.322097 | 53127810 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,182,942 | 2,313.672192 | 53127810 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,146,167 | 0.000000 | 53127810 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,137,001 | 1,088,409.510469 | 53127810 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,134,851 | 37,123,987.616527 | 53127810 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,104,765 | 498,636.060676 | 53127810 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,068,802 | 71,938.876024 | 53127810 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,058,615 | 20,350,659.119575 | 53127810 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,053,078 | 56.448271 | 53127810 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,027,815 | 17.542908 | 53127810 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,005,166 | 0.039784 | 53127810 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 951,339 | 2,317.651191 | 53127810 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,924 | 1,095.152360 | 53127810 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 905,233 | 2.309155 | 53127810 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,312 | 0.000557 | 53127810 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 878,135 | 18.001612 | 53127810 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 875,463 | 17.127755 | 53127810 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/VVV | 10000 | 869,768 | 91.816323 | 53127810 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,079 | 2,317.064250 | 53127810 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 800,190 | 0.000008 | 53127810 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,539 | 0.056735 | 53127810 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 784,087 | 0.803146 | 53127810 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 735,868 | 0.614689 | 53127810 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 733,177 | 4,709,914.438854 | 53127810 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 698,961 | 0.614411 | 53127810 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 698,783 | 138,225.760033 | 53127810 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 690,453 | 502,390.640971 | 53127810 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 677,099 | 0.109638 | 53127810 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 888 ; routes examinées : 17328432 ; candidats optimisés : 42668 ; net attendu > 0 : 76 ; dernier cycle 190.2 ms
- Rejets (moteur) : {'spread_below_threshold': 17055165, 'liquidity_below_min': 211587, 'negative_expected_net': 42592, 'unquotable': 18010, 'borrow_bound_too_small': 887, 'cycle_budget_exhausted': 115}
- Enregistrements de la session : 42668 ; net attendu > 0 : 76 ; simulés (eth_call de la vraie tx) : 6 (ok 0, échec 6) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 42668} ; motifs de rejet : {'below_safety_margin': 55, 'negative_expected_net': 42592, 'p_lower_below_threshold': 64, 'reliability_not_demonstrated': 12, 'simulation_failed': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53127765 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.512672 WETH | 0.000064 WETH | 0.000000 WETH | 0.000002 WETH | 0.000062 WETH (0.1324 €) | — | 1.21 | 0.021 (n=101) | REJECTED | below_safety_margin(62127277652393<102534382357389), p_lower_below_threshold(0.02<0.75) |
| 53127765 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,182.521916 USDC | 0.148852 USDC | 0.000000 USDC | 0.005202 USDC | 0.143650 USDC (0.1322 €) | — | 1.21 | 0.021 (n=101) | REJECTED | below_safety_margin(143650<236504), p_lower_below_threshold(0.02<0.75) |
| 53127765 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.235656 WETH | 0.000061 WETH | 0.000000 WETH | 0.000002 WETH | 0.000059 WETH (0.1258 €) | — | 2.51 | 0.015 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53127765 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 543.411552 USDC | 0.141726 USDC | 0.000000 USDC | 0.005202 USDC | 0.136524 USDC (0.1256 €) | — | 2.51 | 0.015 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53127765 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.206610 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0926 €) | — | 2.10 | 0.132 (n=374) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 53127765 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.005724 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0926 €) | — | 2.20 | 0.132 (n=374) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53127765 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 477.937119 USDC | 0.107545 USDC | 0.000000 USDC | 0.006962 USDC | 0.100583 USDC (0.0925 €) | — | 2.10 | 0.132 (n=374) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53127765 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010946 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0662 €) | — | 0.82 | 0.132 (n=374) | REJECTED | below_safety_margin(90<218), p_lower_below_threshold(0.13<0.75) |
| 53127765 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.378823 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0659 €) | — | 0.82 | 0.132 (n=374) | REJECTED | below_safety_margin(30918114616149<75764552473040), p_lower_below_threshold(0.13<0.75) |
| 53127765 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 876.133698 USDC | 0.078429 USDC | 0.000000 USDC | 0.006962 USDC | 0.071467 USDC (0.0657 €) | — | 0.82 | 0.132 (n=374) | REJECTED | below_safety_margin(71467<175226), p_lower_below_threshold(0.13<0.75) |
| 53127765 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.164476 WETH | 0.000031 WETH | 0.000000 WETH | 0.000002 WETH | 0.000029 WETH (0.0612 €) | — | 1.75 | 0.021 (n=101) | REJECTED | below_safety_margin(28745832692693<32895226608554), p_lower_below_threshold(0.02<0.75) |
| 53127765 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 379.423827 USDC | 0.072023 USDC | 0.000000 USDC | 0.005553 USDC | 0.066470 USDC (0.0612 €) | — | 1.75 | 0.021 (n=101) | REJECTED | below_safety_margin(66470<75884), p_lower_below_threshold(0.02<0.75) |
| 53127765 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.159018 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0553 €) | — | 1.63 | 0.015 (n=19) | REJECTED | below_safety_margin(25956625965183<31803644805828), reliability_not_demonstrated |
| 53127765 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 367.525008 USDC | 0.065223 USDC | 0.000000 USDC | 0.005202 USDC | 0.060021 USDC (0.0552 €) | — | 1.63 | 0.015 (n=19) | REJECTED | below_safety_margin(60021<73505), reliability_not_demonstrated |
| 53127753 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.007974 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0201 €) | — | 11.85 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53127753 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 18.423323 USDC | 0.028819 USDC | 0.000000 USDC | 0.006962 USDC | 0.021857 USDC (0.0201 €) | — | 11.86 | 0.000 (n=52) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127753 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.007744 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0194 €) | — | 11.76 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53127753 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 17.961260 USDC | 0.028028 USDC | 0.000000 USDC | 0.006962 USDC | 0.021066 USDC (0.0194 €) | — | 11.73 | 0.000 (n=52) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127765 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 230.583788 USDC | 0.027835 USDC | 0.000000 USDC | 0.006962 USDC | 0.020873 USDC (0.0192 €) | — | 0.91 | 0.132 (n=374) | REJECTED | below_safety_margin(20873<46116), p_lower_below_threshold(0.13<0.75) |
| 53127765 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.092799 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0192 €) | — | 0.97 | 0.132 (n=374) | REJECTED | below_safety_margin(8994223551074<18559878110373), p_lower_below_threshold(0.13<0.75) |
| 53127765 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002788 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0191 €) | — | 0.93 | 0.132 (n=374) | REJECTED | below_safety_margin(26<55), p_lower_below_threshold(0.13<0.75) |
| 53127753 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.007884 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0189 €) | — | 11.22 | 0.000 (n=51) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53127753 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 18.203490 USDC | 0.027430 USDC | 0.000000 USDC | 0.006962 USDC | 0.020468 USDC (0.0188 €) | — | 11.24 | 0.000 (n=51) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127753 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.007780 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0181 €) | — | 10.92 | 0.000 (n=52) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53127753 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 17.952581 USDC | 0.026617 USDC | 0.000000 USDC | 0.006962 USDC | 0.019655 USDC (0.0181 €) | — | 10.95 | 0.000 (n=52) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2734 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
