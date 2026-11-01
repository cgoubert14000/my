# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T22:11:35+00:00 ; durée 21.36 min ; blocs 53390229 → 53390873 (636 vus)

## Connexion
- Requêtes RPC : 7374 ; erreurs : 0 ; latence p50/p95 : 238.3/1,307.1 ms
- Rafraîchissements d'état : 637 ; âge des données au dernier bloc : 1.87 s ; changements de frais LP observés (pools à frais dynamiques) : 706
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5404 ; cycles déclenchés par événement : 952 ; avance médiane sur le rafraîchissement multicall : 496 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,258.83 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 495 pools, 288 jetons, 18180 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 111, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3720 (énumérés 312, par paires 0), mesurés 498, sous le plancher de 10000.0 $ : 3 → gardés 495 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2258.829928, 'cbBTC': 77854.490121, 'AERO': 0.63182}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,398,904 | 2,258.829774 | 53390873 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,133,658 | 0.029065 | 53390873 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,317,665 | 0.000013 | 53390873 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,139,309 | 0.029095 | 53390873 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,889,485 | 2,260.182190 | 53390873 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,816,455 | 98.673428 | 53390873 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,643,601 | 0.001582 | 53390873 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,543,819 | 1.588561 | 53390873 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,150,960 | 0.029065 | 53390873 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,091,961 | 0.998850 | 53390873 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,049,431 | 2,260.161539 | 53390873 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,955,663 | 2,260.000118 | 53390873 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,543,611 | 38,027.886043 | 53390873 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,692,175 | 0.029081 | 53390873 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,378,907 | 98.639071 | 53390873 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,125,213 | 0.000013 | 53390873 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,086,616 | 1,188,094.920793 | 53390873 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,758,889 | 0.018115 | 53390873 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,752,327 | 0.000000 | 53390873 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,658,617 | 0.000013 | 53390873 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,697 | 0.000013 | 53390873 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,548,911 | 428.427128 | 53390873 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,505,219 | 2,262.238457 | 53390873 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53390873 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,642 | 0.825542 | 53390873 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,418,629 | 3,588.203917 | 53390873 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,379,207 | 2,265.561258 | 53390873 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,331,500 | 0.005210 | 53390873 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,321,893 | 2,260.221161 | 53390873 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,186 | 14,724.645075 | 53390873 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,301,276 | 0.000013 | 53390873 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,003 | 71.106813 | 53390873 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,115,866 | 36,002,670.776723 | 53390873 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,063,331 | 519,862.177513 | 53390873 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,048,277 | 0.000000 | 53390873 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,008,388 | 22,413,230.182816 | 53390873 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 993,434 | 98.703042 | 53390873 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 990,058 | 19.503395 | 53390873 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 974,762 | 81,973.487758 | 53390873 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 950,172 | 1,178,950.343524 | 53390873 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 943,367 | 70.344990 | 53390873 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 928,118 | 1,004.452893 | 53390873 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,286 | 2,252.785626 | 53390873 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 917,731 | 0.043652 | 53390873 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 864,308 | 0.000549 | 53390873 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 864,099 | 3,564.630778 | 53390873 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 834,055 | 19.582839 | 53390873 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,615 | 0.060572 | 53390873 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 765,402 | 0.801881 | 53390873 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 726,297 | 0.591644 | 53390873 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,069 | 0.000261 | 53390873 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 715,856 | 4,705,794.573259 | 53390873 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 690,217 | 135,143.653674 | 53390873 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 686,477 | 0.000008 | 53390873 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 673,810 | 0.569790 | 53390873 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 658,535 | 520,135.837380 | 53390873 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 657,964 | 2.340198 | 53390873 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 607,565 | 0.091877 | 53390873 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 606,458 | 0.915597 | 53390873 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,529 | 0.039667 | 53390873 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 1588 ; routes examinées : 28869840 ; candidats optimisés : 77240 ; net attendu > 0 : 40 ; dernier cycle 137.1 ms
- Rejets (moteur) : {'spread_below_threshold': 28373169, 'liquidity_below_min': 414621, 'negative_expected_net': 77200, 'unquotable': 3174, 'borrow_bound_too_small': 1588, 'cycle_budget_exhausted': 48}
- Enregistrements de la session : 77240 ; net attendu > 0 : 40 ; simulés (eth_call de la vraie tx) : 5 (ok 1, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 77240} ; motifs de rejet : {'below_safety_margin': 28, 'negative_expected_net': 77200, 'p_lower_below_threshold': 35, 'reliability_not_demonstrated': 5, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53390786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.013685 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0937 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(131<273), reliability_not_demonstrated |
| 53390786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,064.663235 USDC | 0.108835 USDC | 0.000000 USDC | 0.007130 USDC | 0.101705 USDC (0.0936 €) | — | 0.96 | 0.000 (n=18) | REJECTED | below_safety_margin(101705<212932), reliability_not_demonstrated |
| 53390786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.480798 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0934 €) | — | 0.94 | 0.000 (n=18) | REJECTED | below_safety_margin(44960344685998<96159606306820), reliability_not_demonstrated |
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
| 53390786 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006077 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0272 €) | — | 0.63 | 0.136 (n=709) | REJECTED | below_safety_margin(38<121), p_lower_below_threshold(0.14<0.75) |
| 53390786 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.216239 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0270 €) | — | 0.60 | 0.136 (n=709) | REJECTED | below_safety_margin(13016508408293<43247781501173), p_lower_below_threshold(0.14<0.75) |
| 53390586 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 54.535593 USDC | 0.035863 USDC | 0.000000 USDC | 0.006788 USDC | 0.029075 USDC (0.0267 €) | — | 5.33 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 485.606064 USDC | 0.035823 USDC | 0.000000 USDC | 0.006787 USDC | 0.029036 USDC (0.0267 €) | — | 0.60 | 0.136 (n=709) | REJECTED | below_safety_margin(29036<97121), p_lower_below_threshold(0.14<0.75) |
| 53390586 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.024288 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0267 €) | — | 5.29 | 0.117 (n=526) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53390586 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 73.620711 USDC | 0.026313 USDC | 0.000000 USDC | 0.006788 USDC | 0.019525 USDC (0.0180 €) | — | 2.65 | 0.136 (n=708) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53390586 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001170 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0179 €) | — | 2.14 | 0.136 (n=708) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53390676 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 114.736675 USDC | 0.014804 USDC | 0.000000 USDC | 0.005071 USDC | 0.009733 USDC (0.0090 €) | — | 0.85 | 0.001 (n=7) | REJECTED | below_safety_margin(9733<22947), reliability_not_demonstrated |
| 53390676 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001847 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0086 €) | — | 0.65 | 0.001 (n=7) | REJECTED | below_safety_margin(12<36), reliability_not_demonstrated |
| 53390786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 175.909981 USDC | 0.014275 USDC | 0.000000 USDC | 0.007130 USDC | 0.007145 USDC (0.0066 €) | — | 0.41 | 0.136 (n=709) | REJECTED | below_safety_margin(7145<35181), p_lower_below_threshold(0.14<0.75) |
| 53390786 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002224 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0064 €) | — | 0.40 | 0.136 (n=709) | REJECTED | below_safety_margin(9<44), p_lower_below_threshold(0.14<0.75) |
| 53390786 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.094389 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0063 €) | — | 0.32 | 0.136 (n=709) | REJECTED | below_safety_margin(3024088916225<18877761463930), p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 4192 ; taux observé 0.126 ; borne inférieure crédible (0.9) 0.120 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
