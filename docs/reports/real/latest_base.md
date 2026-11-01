# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T22:05:29+00:00 ; durée 15.26 min ; blocs 53390229 → 53390689 (454 vus)

## Connexion
- Requêtes RPC : 5268 ; erreurs : 0 ; latence p50/p95 : 214.2/1,317.7 ms
- Rafraîchissements d'état : 455 ; âge des données au dernier bloc : 2.05 s ; changements de frais LP observés (pools à frais dynamiques) : 433
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3370 ; cycles déclenchés par événement : 675 ; avance médiane sur le rafraîchissement multicall : 423 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,258.83 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 288 jetons, 18180 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 111, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3720 (énumérés 312, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2258.829928, 'cbBTC': 77854.490121, 'AERO': 0.63182}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,398,902 | 2,258.829760 | 53390690 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,133,658 | 0.029065 | 53390690 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,317,665 | 0.000013 | 53390690 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,139,309 | 0.029095 | 53390690 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,889,555 | 2,260.462355 | 53390690 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,816,218 | 98.679419 | 53390690 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,649,849 | 0.001585 | 53390690 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,548,527 | 1.585866 | 53390690 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,150,956 | 0.029057 | 53390690 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,091,961 | 0.998850 | 53390690 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,049,421 | 2,259.870037 | 53390690 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,955,650 | 2,259.869600 | 53390690 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,546,181 | 37,972.776318 | 53390690 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,692,175 | 0.029081 | 53390690 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,378,833 | 98.639071 | 53390690 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,125,213 | 0.000013 | 53390690 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,086,616 | 1,188,094.920793 | 53390690 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,759,760 | 0.018130 | 53390690 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,752,328 | 0.000000 | 53390690 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,658,587 | 0.000013 | 53390690 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,697 | 0.000013 | 53390690 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,549,388 | 427.973521 | 53390690 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,505,219 | 2,262.238170 | 53390690 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53390690 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,721 | 0.825460 | 53390690 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,420,014 | 3,584.300266 | 53390690 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,379,207 | 2,266.511447 | 53390690 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,331,500 | 0.005210 | 53390690 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,321,890 | 2,260.575427 | 53390690 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,768 | 14,715.887783 | 53390690 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,301,273 | 0.000013 | 53390690 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,003 | 71.106813 | 53390690 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,118,651 | 36,002,670.776723 | 53390690 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,063,329 | 519,864.841568 | 53390690 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,048,276 | 0.000000 | 53390690 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,008,388 | 22,413,230.182816 | 53390690 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 993,400 | 98.703056 | 53390690 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,624 | 19.528273 | 53390690 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 974,762 | 81,973.487758 | 53390690 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 950,172 | 1,178,950.343524 | 53390690 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 943,367 | 70.344990 | 53390690 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 928,244 | 1,004.452893 | 53390690 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,286 | 2,252.785626 | 53390690 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 917,688 | 0.043598 | 53390690 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 864,994 | 3,564.630778 | 53390690 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,440 | 0.000549 | 53390690 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 834,214 | 19.577131 | 53390690 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,738 | 0.060591 | 53390690 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,402 | 0.801881 | 53390690 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 726,297 | 0.591644 | 53390690 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,069 | 0.000261 | 53390690 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 715,856 | 4,705,794.573259 | 53390690 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 690,216 | 135,143.812548 | 53390690 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 687,143 | 0.000008 | 53390690 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 673,810 | 0.569790 | 53390690 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 658,533 | 518,786.710004 | 53390690 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 657,964 | 2.340198 | 53390690 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 607,240 | 0.091802 | 53390690 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 606,458 | 0.915597 | 53390690 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,528 | 0.039667 | 53390690 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 1128 ; routes examinées : 20507040 ; candidats optimisés : 51108 ; net attendu > 0 : 20 ; dernier cycle 112.0 ms
- Rejets (moteur) : {'spread_below_threshold': 20143224, 'liquidity_below_min': 309284, 'negative_expected_net': 51088, 'unquotable': 2252, 'borrow_bound_too_small': 1128, 'cycle_budget_exhausted': 36}
- Enregistrements de la session : 51070 ; net attendu > 0 : 20 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 51070} ; motifs de rejet : {'below_safety_margin': 10, 'negative_expected_net': 51050, 'p_lower_below_threshold': 18, 'reliability_not_demonstrated': 2, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53390586 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 92.916822 USDC | 0.060587 USDC | 0.000000 USDC | 0.006788 USDC | 0.053799 USDC (0.0495 €) | — | 5.79 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.041203 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0494 €) | — | 5.77 | 0.117 (n=526) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53390586 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 94.739712 USDC | 0.060419 USDC | 0.000000 USDC | 0.006788 USDC | 0.053631 USDC (0.0493 €) | — | 5.66 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.042056 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0493 €) | — | 5.64 | 0.117 (n=526) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53390586 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 89.897598 USDC | 0.054154 USDC | 0.000000 USDC | 0.006788 USDC | 0.047366 USDC (0.0436 €) | — | 5.27 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.039783 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0435 €) | — | 5.26 | 0.117 (n=526) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53390676 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009470 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0372 €) | — | 0.55 | 0.042 (n=158) | REJECTED | below_safety_margin(52<189), p_lower_below_threshold(0.04<0.75) |
| 53390676 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 790.142481 USDC | 0.045511 USDC | 0.000000 USDC | 0.005414 USDC | 0.040097 USDC (0.0369 €) | — | 0.51 | 0.042 (n=158) | REJECTED | below_safety_margin(40097<158028), p_lower_below_threshold(0.04<0.75) |
| 53390676 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.007485 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0357 €) | — | 0.67 | 0.042 (n=158) | REJECTED | below_safety_margin(50<149), p_lower_below_threshold(0.04<0.75) |
| 53390676 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 667.751897 USDC | 0.044125 USDC | 0.000000 USDC | 0.005414 USDC | 0.038711 USDC (0.0356 €) | — | 0.58 | 0.042 (n=158) | REJECTED | below_safety_margin(38711<133550), p_lower_below_threshold(0.04<0.75) |
| 53390586 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 54.535593 USDC | 0.035863 USDC | 0.000000 USDC | 0.006788 USDC | 0.029075 USDC (0.0267 €) | — | 5.33 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.024288 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0267 €) | — | 5.29 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390586 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 73.620711 USDC | 0.026313 USDC | 0.000000 USDC | 0.006788 USDC | 0.019525 USDC (0.0180 €) | — | 2.65 | 0.136 (n=708) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53390586 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001170 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0179 €) | — | 2.14 | 0.136 (n=708) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53390676 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 114.736675 USDC | 0.014804 USDC | 0.000000 USDC | 0.005071 USDC | 0.009733 USDC (0.0090 €) | — | 0.85 | 0.001 (n=7) | REJECTED | below_safety_margin(9733<22947), reliability_not_demonstrated |
| 53390676 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001847 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0086 €) | — | 0.65 | 0.001 (n=7) | REJECTED | below_safety_margin(12<36), reliability_not_demonstrated |
| 53390586 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 37.553264 USDC | 0.009451 USDC | 0.000000 USDC | 0.006788 USDC | 0.002663 USDC (0.0024 €) | — | 0.71 | 0.136 (n=708) | REJECTED | below_safety_margin(2663<7510), p_lower_below_threshold(0.14<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.016633 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.70 | 0.136 (n=708) | REJECTED | below_safety_margin(1169989615072<3326668881658), p_lower_below_threshold(0.14<0.75) |
| 53390586 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 37.019855 USDC | 0.009334 USDC | 0.000000 USDC | 0.006788 USDC | 0.002546 USDC (0.0023 €) | — | 0.69 | 0.136 (n=708) | REJECTED | below_safety_margin(2546<7403), p_lower_below_threshold(0.14<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.016422 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.68 | 0.136 (n=708) | REJECTED | below_safety_margin(1118356115155<3284458587357), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 4191 ; taux observé 0.126 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
