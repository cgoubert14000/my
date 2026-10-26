# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T21:10:04+00:00 ; durée 79.38 min ; blocs 53127443 → 53129825 (2330 vus)

## Connexion
- Requêtes RPC : 28283 ; erreurs : 0 ; latence p50/p95 : 220.0/1,641.4 ms
- Rafraîchissements d'état : 2330 ; âge des données au dernier bloc : 5.08 s ; changements de frais LP observés (pools à frais dynamiques) : 3170
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17282 ; cycles déclenchés par événement : 2029 ; avance médiane sur le rafraîchissement multicall : 674 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,308.27 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19514 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 190 (rejetés 2) → 595 jetons ; pools candidats 3792 (énumérés 342, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2315.799118, 'cbBTC': 79865.457277, 'AERO': 0.681738}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,395,034 | 2,308.266653 | 53129826 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,634,037 | 0.028860 | 53129826 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,123,072 | 0.028931 | 53129826 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,468,918 | 0.000013 | 53129826 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,831,506 | 92.426267 | 53129826 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,297,600 | 2,304.499192 | 53129826 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,022,729 | 1.484671 | 53129826 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,961,238 | 0.001640 | 53129826 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,345,405 | 0.028861 | 53129826 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,224,238 | 2,304.440319 | 53129826 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,494,738 | 2,304.135853 | 53129826 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,209,438 | 0.999474 | 53129826 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,767,479 | 35,136.363259 | 53129826 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,353,700 | 2,306.008096 | 53129826 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 3,175,659 | 0.028915 | 53129826 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2784 | 2,494,910 | 92.442101 | 53129826 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,450,375 | 0.000013 | 53129826 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,116,778 | 1,205,564.015608 | 53129826 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,902,309 | 0.000013 | 53129826 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,825,401 | 0.000000 | 53129826 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,111 | 0.018431 | 53129826 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,746,035 | 408.090240 | 53129826 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,712,665 | 0.000013 | 53129826 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,688,972 | 0.000013 | 53129826 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,545,576 | 0.000266 | 53129826 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,480,330 | 0.005770 | 53129826 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,916 | 0.826527 | 53129826 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53129826 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,424,989 | 3,427.330591 | 53129826 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,361,789 | 14,125.565943 | 53129826 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,229,633 | 0.000265 | 53129826 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,650 | 65.538581 | 53129826 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,204,009 | 3,405.064240 | 53129826 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,171,815 | 2,304.300875 | 53129826 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,141,225 | 0.000000 | 53129826 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,133,229 | 1,088,552.703489 | 53129826 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,130,759 | 37,164,407.347049 | 53129826 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,224 | 498,571.955099 | 53129826 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,064,273 | 72,081.390994 | 53129826 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,060,657 | 20,170,039.012473 | 53129826 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,044,225 | 57.409402 | 53129826 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,026,423 | 17.608348 | 53129826 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,000,607 | 0.040149 | 53129826 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 949,979 | 2,317.651230 | 53129826 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,926 | 1,090.406315 | 53129826 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 902,289 | 2.309155 | 53129826 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 889,410 | 0.000557 | 53129826 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,135 | 18.001612 | 53129826 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 866,194 | 91.815782 | 53129826 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 855,837 | 17.127755 | 53129826 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 842,708 | 2,308.577020 | 53129826 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 797,387 | 0.000008 | 53129826 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 793,443 | 0.056421 | 53129826 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 781,537 | 0.803146 | 53129826 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 733,963 | 0.611105 | 53129826 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 729,805 | 4,722,712.436021 | 53129826 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 695,052 | 138,807.148747 | 53129826 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 694,594 | 0.607132 | 53129826 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 688,252 | 499,987.478320 | 53129826 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 676,698 | 0.109531 | 53129826 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 4358 ; routes examinées : 85042012 ; candidats optimisés : 285040 ; net attendu > 0 : 216 ; dernier cycle 408.7 ms
- Rejets (moteur) : {'spread_below_threshold': 83499657, 'liquidity_below_min': 1067124, 'negative_expected_net': 284824, 'unquotable': 94240, 'pool_quarantined': 90664, 'borrow_bound_too_small': 4353, 'cycle_budget_exhausted': 934}
- Enregistrements de la session : 285040 ; net attendu > 0 : 216 ; simulés (eth_call de la vraie tx) : 31 (ok 3, échec 28) ; étiquettes ghost N+1 : 3/29 positives
- Décisions : {'REJECTED': 285040} ; motifs de rejet : {'below_safety_margin': 95, 'negative_expected_net': 284824, 'p_lower_below_threshold': 166, 'price_impact': 8, 'reliability_not_demonstrated': 50, 'simulation_failed': 28}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.023209 WETH | 0.000907 WETH | 0.000000 WETH | 0.000003 WETH | 0.000904 WETH (1.9240 €) | — | 389.33 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53128709 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 53.644555 USDC | 2.095475 USDC | 0.000000 USDC | 0.006955 USDC | 2.088520 USDC (1.9214 €) | — | 389.33 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.022925 WETH | 0.000895 WETH | 0.000000 WETH | 0.000003 WETH | 0.000892 WETH (1.8994 €) | — | 389.10 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53128709 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 53.015983 USDC | 2.070165 USDC | 0.000000 USDC | 0.007307 USDC | 2.062858 USDC (1.8978 €) | — | 389.10 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.022608 WETH | 0.000882 WETH | 0.000000 WETH | 0.000003 WETH | 0.000879 WETH (1.8717 €) | — | 388.80 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53128709 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 52.260446 USDC | 2.038830 USDC | 0.000000 USDC | 0.006955 USDC | 2.031875 USDC (1.8693 €) | — | 388.80 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 47.739345 USDC | 1.869729 USDC | 0.000000 USDC | 0.006955 USDC | 1.862774 USDC (1.7138 €) | — | 390.20 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.020555 WETH | 0.000805 WETH | 0.000000 WETH | 0.000003 WETH | 0.000802 WETH (1.7078 €) | — | 390.19 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.018327 WETH | 0.000721 WETH | 0.000000 WETH | 0.000003 WETH | 0.000718 WETH (1.5298 €) | — | 392.01 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 42.364576 USDC | 1.667668 USDC | 0.000000 USDC | 0.006955 USDC | 1.660713 USDC (1.5279 €) | — | 392.01 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.018262 WETH | 0.000719 WETH | 0.000000 WETH | 0.000003 WETH | 0.000716 WETH (1.5243 €) | — | 392.01 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 42.219910 USDC | 1.662016 USDC | 0.000000 USDC | 0.006955 USDC | 1.655061 USDC (1.5227 €) | — | 392.01 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 39.634488 USDC | 1.562977 USDC | 0.000000 USDC | 0.006955 USDC | 1.556022 USDC (1.4315 €) | — | 392.59 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.017102 WETH | 0.000674 WETH | 0.000000 WETH | 0.000003 WETH | 0.000671 WETH (1.4296 €) | — | 392.59 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128573 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 46.939311 USDC | 0.192827 USDC | 0.000000 USDC | 0.004880 USDC | 0.187947 USDC (0.1729 €) | — | 40.04 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
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

## Fiabilité et décision
- Observations ghost : 2757 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
