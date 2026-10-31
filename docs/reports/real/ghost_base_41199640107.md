# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T16:56:00+00:00 ; durée 283.17 min ; blocs 53329707 → 53338201 (8249 vus)

## Connexion
- Requêtes RPC : 97115 ; erreurs : 30 ; latence p50/p95 : 296.7/1,058.1 ms
- Rafraîchissements d'état : 8249 ; âge des données au dernier bloc : 4.79 s ; changements de frais LP observés (pools à frais dynamiques) : 8557
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 71052 ; cycles déclenchés par événement : 8445 ; avance médiane sur le rafraîchissement multicall : 542 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,246.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 290 jetons, 18658 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 318, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2242.796031, 'cbBTC': 77486.299825, 'AERO': 0.625959}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,102,713 | 2,246.025557 | 53338202 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,034,333 | 0.029027 | 53338202 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,279,714 | 0.000013 | 53338202 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,036,998 | 0.029054 | 53338202 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,867,532 | 96.575061 | 53338202 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,848,913 | 2,249.751520 | 53338202 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,685,651 | 0.001616 | 53338202 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,742,252 | 1.567945 | 53338202 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,300,061 | 0.029029 | 53338202 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,099,421 | 2,249.734132 | 53338202 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,078,595 | 2,249.901027 | 53338202 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,074,389 | 0.998824 | 53338202 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,538,625 | 37,704.002566 | 53338202 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,683,353 | 0.029042 | 53338202 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,405,953 | 96.532396 | 53338202 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,064,362 | 1,200,126.211824 | 53338202 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,968,112 | 0.000013 | 53338202 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,754,439 | 0.000000 | 53338202 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,730,418 | 0.017615 | 53338202 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,639,486 | 0.000013 | 53338202 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,592,798 | 2,248.767228 | 53338202 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,583,241 | 1.434908 | 53338202 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,572 | 0.000013 | 53338202 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,549,245 | 419.524834 | 53338202 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,343 | 0.825841 | 53338202 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,424,165 | 3,526.901839 | 53338202 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,410,163 | 2,256.158605 | 53338202 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,356,933 | 2,249.667220 | 53338202 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,340,101 | 0.005286 | 53338202 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,307,948 | 14,467.225133 | 53338202 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,305,613 | 0.000013 | 53338202 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,174,369 | 70.458427 | 53338202 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,120,470 | 35,240,976.602131 | 53338202 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,059,927 | 515,109.940220 | 53338202 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,034,108 | 0.000000 | 53338202 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,024,036 | 21,577,072.539196 | 53338202 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,012,876 | 75,061.126843 | 53338202 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 998,142 | 19.050066 | 53338202 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 995,042 | 96.789223 | 53338202 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 961,284 | 67.746565 | 53338202 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 939,805 | 943.029571 | 53338202 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/WELL | 10000 | 935,639 | 1,204,816.407411 | 53338202 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 922,381 | 2,236.005346 | 53338202 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 913,939 | 0.042916 | 53338202 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 873,018 | 3,535.754982 | 53338202 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,265 | 0.000554 | 53338202 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 846,887 | 19.125201 | 53338202 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 829,164 | 0.061937 | 53338202 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,607 | 0.802843 | 53338202 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,853 | 0.000262 | 53338202 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 727,236 | 4,506,662.470950 | 53338202 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,318 | 0.592802 | 53338202 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 690,980 | 0.000008 | 53338202 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 670,613 | 141,465.488936 | 53338202 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 660,991 | 2.335058 | 53338202 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 657,799 | 511,270.548179 | 53338202 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 631,471 | 0.504029 | 53338202 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 626,980 | 0.096480 | 53338202 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,618 | 0.916818 | 53338202 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 562,710 | 943.293527 | 53338202 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 16693 ; routes examinées : 311457994 ; candidats optimisés : 868267 ; net attendu > 0 : 372 ; dernier cycle 273.5 ms
- Rejets (moteur) : {'spread_below_threshold': 307770837, 'liquidity_below_min': 2765227, 'negative_expected_net': 867895, 'unquotable': 33240, 'borrow_bound_too_small': 16658, 'cycle_budget_exhausted': 3765}
- Enregistrements de la session : 868267 ; net attendu > 0 : 372 ; simulés (eth_call de la vraie tx) : 25 (ok 5, échec 20) ; étiquettes ghost N+1 : 1/19 positives
- Décisions : {'REJECTED': 868267} ; motifs de rejet : {'below_safety_margin': 285, 'negative_expected_net': 867895, 'p_lower_below_threshold': 352, 'reliability_not_demonstrated': 20, 'simulation_failed': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 1,169.382766 USDC | 3.349481 USDC | 0.000000 USDC | 0.006775 USDC | 3.342706 USDC (3.0753 €) | — | 28.59 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.520561 WETH | 0.001491 WETH | 0.000000 WETH | 0.000003 WETH | 0.001488 WETH (3.0748 €) | — | 28.59 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.536835 WETH | 0.001165 WETH | 0.000000 WETH | 0.000003 WETH | 0.001162 WETH (2.4012 €) | — | 21.65 | 0.000 (n=28) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,204.187156 USDC | 2.616046 USDC | 0.000000 USDC | 0.007116 USDC | 2.608930 USDC (2.4002 €) | — | 21.67 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53335509 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.440282 WETH | 0.000976 WETH | 0.000000 WETH | 0.000003 WETH | 0.000973 WETH (2.0109 €) | — | 22.10 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 988.126456 USDC | 2.190896 USDC | 0.000000 USDC | 0.006775 USDC | 2.184121 USDC (2.0094 €) | — | 22.10 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.422302 WETH | 0.000945 WETH | 0.000000 WETH | 0.000003 WETH | 0.000942 WETH (1.9460 €) | — | 22.30 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 947.639796 USDC | 2.120061 USDC | 0.000000 USDC | 0.006775 USDC | 2.113286 USDC (1.9442 €) | — | 22.30 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53335509 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.411280 WETH | 0.000883 WETH | 0.000000 WETH | 0.000003 WETH | 0.000879 WETH (1.8168 €) | — | 21.38 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 922.614280 USDC | 1.979736 USDC | 0.000000 USDC | 0.007798 USDC | 1.971938 USDC (1.8142 €) | — | 21.37 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.614710 WETH | 0.000372 WETH | 0.000000 WETH | 0.000002 WETH | 0.000369 WETH (0.7630 €) | — | 2.29 | 0.039 (n=152) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53335509 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 3,625.255582 USDC | 0.834698 USDC | 0.000000 USDC | 0.005405 USDC | 0.829293 USDC (0.7629 €) | — | 2.29 | 0.039 (n=152) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53335509 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.143528 WETH | 0.000321 WETH | 0.000000 WETH | 0.000003 WETH | 0.000318 WETH (0.6569 €) | — | 22.15 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 321.267429 USDC | 0.718649 USDC | 0.000000 USDC | 0.007116 USDC | 0.711533 USDC (0.6546 €) | — | 22.15 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.133456 WETH | 0.000285 WETH | 0.000000 WETH | 0.000003 WETH | 0.000282 WETH (0.5826 €) | — | 21.13 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 298.477340 USDC | 0.637680 USDC | 0.000000 USDC | 0.006775 USDC | 0.630905 USDC (0.5804 €) | — | 21.14 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.289510 WETH | 0.000274 WETH | 0.000000 WETH | 0.000002 WETH | 0.000272 WETH (0.5622 €) | — | 9.40 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53335509 | WETH→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.087497 WETH | 0.000222 WETH | 0.000000 WETH | 0.000002 WETH | 0.000220 WETH (0.4541 €) | — | 25.11 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53336277 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 227.045518 USDC | 0.415783 USDC | 0.000000 USDC | 0.008473 USDC | 0.407310 USDC (0.3747 €) | — | 17.94 | 0.017 (n=83) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53336277 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.101120 WETH | 0.000185 WETH | 0.000000 WETH | 0.000004 WETH | 0.000181 WETH (0.3744 €) | — | 17.92 | 0.017 (n=83) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53336277 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 225.447587 USDC | 0.408839 USDC | 0.000000 USDC | 0.008473 USDC | 0.400366 USDC (0.3683 €) | — | 17.76 | 0.072 (n=93) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53336277 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.100513 WETH | 0.000182 WETH | 0.000000 WETH | 0.000004 WETH | 0.000178 WETH (0.3680 €) | — | 17.72 | 0.072 (n=93) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53336277 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 212.027435 USDC | 0.383988 USDC | 0.000000 USDC | 0.008814 USDC | 0.375174 USDC (0.3452 €) | — | 17.69 | 0.017 (n=83) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53336277 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.094243 WETH | 0.000171 WETH | 0.000000 WETH | 0.000004 WETH | 0.000167 WETH (0.3448 €) | — | 17.70 | 0.017 (n=83) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53336277 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 190.873791 USDC | 0.294025 USDC | 0.000000 USDC | 0.008132 USDC | 0.285893 USDC (0.2630 €) | — | 14.98 | 0.017 (n=83) | REJECTED | p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 3964 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
