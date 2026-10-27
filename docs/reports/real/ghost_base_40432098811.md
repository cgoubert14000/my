# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T05:23:06+00:00 ; durée 235.33 min ; blocs 53137556 → 53144615 (6955 vus)

## Connexion
- Requêtes RPC : 85509 ; erreurs : 28 ; latence p50/p95 : 254.2/1,334.1 ms
- Rafraîchissements d'état : 6955 ; âge des données au dernier bloc : 3.37 s ; changements de frais LP observés (pools à frais dynamiques) : 9467
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 68883 ; cycles déclenchés par événement : 6858 ; avance médiane sur le rafraîchissement multicall : 660 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,311.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 530 pools, 305 jetons, 19446 routes
- Par DEX : uniswap_v3 143, aerodrome 212, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3790 (énumérés 341, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 3 → gardés 530 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2322.398057, 'cbBTC': 80000.770706, 'AERO': 0.673032}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,905,464 | 2,311.967524 | 53144616 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,079,494 | 0.028993 | 53144616 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,077,541 | 0.028948 | 53144616 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,484,954 | 0.000013 | 53144616 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,588,179 | 93.415771 | 53144616 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,314,688 | 2,310.871574 | 53144616 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 6,996,702 | 1.493389 | 53144616 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,938,676 | 0.001639 | 53144616 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,334,355 | 0.028981 | 53144616 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 639 | 5,226,300 | 2,310.109153 | 53144616 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,456,458 | 2,309.945201 | 53144616 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,200,204 | 0.998750 | 53144616 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,716,840 | 36,216.142158 | 53144616 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,356,388 | 2,309.030560 | 53144616 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,172,591 | 0.028975 | 53144616 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,489,096 | 93.437951 | 53144616 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,438,499 | 0.000013 | 53144616 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,109,704 | 1,217,557.512867 | 53144616 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,832,642 | 0.018728 | 53144616 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,829,078 | 0.000000 | 53144616 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,752,025 | 405.812452 | 53144616 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,687,326 | 0.000013 | 53144616 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,685,149 | 0.000013 | 53144616 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,661,560 | 0.000013 | 53144616 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,498,087 | 0.005842 | 53144616 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,927 | 0.826515 | 53144616 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53144616 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,422,889 | 3,448.157083 | 53144616 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,405,188 | 0.000266 | 53144616 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,363,270 | 13,993.339668 | 53144616 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,245,947 | 2,310.944878 | 53144616 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,231,707 | 0.000265 | 53144616 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53144616 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,200,611 | 3,447.248911 | 53144616 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,139,038 | 0.000000 | 53144616 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,133,769 | 1,091,005.379706 | 53144616 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,132,498 | 37,251,512.319145 | 53144616 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,100,573 | 501,569.878725 | 53144616 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,068,030 | 71,804.892226 | 53144616 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,056,905 | 20,485,563.390844 | 53144616 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,038,596 | 58.033486 | 53144616 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,574 | 17.231952 | 53144616 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,006,329 | 0.040432 | 53144616 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 950,355 | 2,317.651257 | 53144616 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 918,686 | 1,074.410612 | 53144616 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 903,736 | 2.309154 | 53144616 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 891,796 | 0.000558 | 53144616 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 874,736 | 18.117329 | 53144616 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 870,949 | 92.753804 | 53144616 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 845,651 | 17.405958 | 53144616 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 843,413 | 2,314.311825 | 53144616 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 801,604 | 0.057651 | 53144616 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 792,275 | 0.000008 | 53144616 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 782,774 | 0.803179 | 53144616 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,681 | 0.613132 | 53144616 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 737,237 | 4,643,097.200912 | 53144616 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 697,548 | 138,586.395909 | 53144616 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 696,438 | 0.610143 | 53144616 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 687,146 | 502,284.617411 | 53144616 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 670,623 | 0.107918 | 53144616 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 13812 ; routes examinées : 268588152 ; candidats optimisés : 698333 ; net attendu > 0 : 485 ; dernier cycle 510.4 ms
- Rejets (moteur) : {'spread_below_threshold': 264104292, 'liquidity_below_min': 3433681, 'negative_expected_net': 697848, 'unquotable': 296964, 'pool_quarantined': 40112, 'borrow_bound_too_small': 13799, 'cycle_budget_exhausted': 971}
- Enregistrements de la session : 698333 ; net attendu > 0 : 485 ; simulés (eth_call de la vraie tx) : 36 (ok 5, échec 31) ; étiquettes ghost N+1 : 0/33 positives
- Décisions : {'REJECTED': 698333} ; motifs de rejet : {'below_safety_margin': 202, 'negative_expected_net': 697848, 'p_lower_below_threshold': 352, 'price_impact': 3, 'reliability_not_demonstrated': 133, 'simulation_failed': 31, 'stale_data': 12}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53143351 | WETH→[uniswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054583 WETH | 0.000952 WETH | 0.000000 WETH | 0.000003 WETH | 0.000950 WETH (2.0209 €) | — | 173.98 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054910 WETH | 0.000951 WETH | 0.000000 WETH | 0.000003 WETH | 0.000948 WETH (2.0177 €) | — | 172.67 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 125.935794 USDC | 2.196972 USDC | 0.000000 USDC | 0.005914 USDC | 2.191058 USDC (2.0158 €) | — | 173.98 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 126.695173 USDC | 2.193525 USDC | 0.000000 USDC | 0.005914 USDC | 2.187611 USDC (2.0126 €) | — | 172.67 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.054616 WETH | 0.000943 WETH | 0.000000 WETH | 0.000003 WETH | 0.000940 WETH (2.0009 €) | — | 172.16 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 126.003261 USDC | 2.175157 USDC | 0.000000 USDC | 0.005914 USDC | 2.169243 USDC (1.9957 €) | — | 172.16 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.052424 WETH | 0.000919 WETH | 0.000000 WETH | 0.000003 WETH | 0.000916 WETH (1.9497 €) | — | 174.76 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 120.934634 USDC | 2.119371 USDC | 0.000000 USDC | 0.005914 USDC | 2.113457 USDC (1.9444 €) | — | 174.76 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[uniswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.052451 WETH | 0.000916 WETH | 0.000000 WETH | 0.000003 WETH | 0.000913 WETH (1.9428 €) | — | 174.06 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 120.990801 USDC | 2.111837 USDC | 0.000000 USDC | 0.005914 USDC | 2.105923 USDC (1.9374 €) | — | 174.06 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[sushiswap_v3]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.050692 WETH | 0.000890 WETH | 0.000000 WETH | 0.000003 WETH | 0.000888 WETH (1.8887 €) | — | 175.08 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[sushiswap_v3]→USDC | 116.842036 USDC | 2.051957 USDC | 0.000000 USDC | 0.006265 USDC | 2.045692 USDC (1.8820 €) | — | 175.08 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH | 0.051526 WETH | 0.000883 WETH | 0.000000 WETH | 0.000003 WETH | 0.000880 WETH (1.8737 €) | — | 170.88 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143351 | USDC→[aerodrome]→wIRON→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 118.668551 USDC | 2.033663 USDC | 0.000000 USDC | 0.005914 USDC | 2.027749 USDC (1.8655 €) | — | 170.88 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.062844 WETH | 0.000743 WETH | 0.000000 WETH | 0.000003 WETH | 0.000741 WETH (1.5767 €) | — | 117.90 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.062754 WETH | 0.000742 WETH | 0.000000 WETH | 0.000003 WETH | 0.000740 WETH (1.5746 €) | — | 117.91 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.063188 WETH | 0.000742 WETH | 0.000000 WETH | 0.000003 WETH | 0.000740 WETH (1.5741 €) | — | 117.06 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53143242 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 145.055042 USDC | 1.716050 USDC | 0.000000 USDC | 0.005912 USDC | 1.710138 USDC (1.5733 €) | — | 117.90 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[uniswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 144.861660 USDC | 1.713938 USDC | 0.000000 USDC | 0.005912 USDC | 1.708026 USDC (1.5714 €) | — | 117.91 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 145.855037 USDC | 1.713297 USDC | 0.000000 USDC | 0.005912 USDC | 1.707385 USDC (1.5708 €) | — | 117.06 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.060312 WETH | 0.000692 WETH | 0.000000 WETH | 0.000003 WETH | 0.000689 WETH (1.4665 €) | — | 114.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 139.311377 USDC | 1.597670 USDC | 0.000000 USDC | 0.005912 USDC | 1.591758 USDC (1.4644 €) | — | 114.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.058628 WETH | 0.000691 WETH | 0.000000 WETH | 0.000003 WETH | 0.000688 WETH (1.4643 €) | — | 117.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC | 135.528430 USDC | 1.596572 USDC | 0.000000 USDC | 0.005912 USDC | 1.590660 USDC (1.4634 €) | — | 117.37 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53143242 | WETH→[uniswap_v2]→wIRON→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.060344 WETH | 0.000688 WETH | 0.000000 WETH | 0.000003 WETH | 0.000685 WETH (1.4577 €) | — | 113.51 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2808 ; taux observé 0.091 ; borne inférieure crédible (0.9) 0.084 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
