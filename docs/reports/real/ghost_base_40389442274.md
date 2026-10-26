# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T21:03:51+00:00 ; durée 73.17 min ; blocs 53127443 → 53129640 (2146 vus)

## Connexion
- Requêtes RPC : 26178 ; erreurs : 0 ; latence p50/p95 : 235.2/1,684.2 ms
- Rafraîchissements d'état : 2146 ; âge des données au dernier bloc : 2.54 s ; changements de frais LP observés (pools à frais dynamiques) : 2829
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17282 ; cycles déclenchés par événement : 2029 ; avance médiane sur le rafraîchissement multicall : 674 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,309.05 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19514 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 190 (rejetés 2) → 595 jetons ; pools candidats 3792 (énumérés 342, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2315.799118, 'cbBTC': 79865.457277, 'AERO': 0.681738}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,434,136 | 2,309.052788 | 53129640 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,637,430 | 0.028891 | 53129640 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,123,460 | 0.028956 | 53129640 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,465,451 | 0.000013 | 53129640 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,857,533 | 91.946478 | 53129640 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,299,708 | 2,306.866937 | 53129640 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,023,970 | 1.484147 | 53129640 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,959,571 | 0.001642 | 53129640 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,346,133 | 0.028886 | 53129640 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,225,689 | 2,307.372466 | 53129640 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,495,729 | 2,307.255598 | 53129640 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,206,466 | 0.999474 | 53129640 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,768,789 | 35,135.847332 | 53129640 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,354,272 | 2,305.828546 | 53129640 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 3,175,971 | 0.028941 | 53129640 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,500,696 | 91.948403 | 53129640 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 2,449,254 | 0.000013 | 53129640 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,117,499 | 1,205,564.015608 | 53129640 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,901,801 | 0.000013 | 53129640 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,826,031 | 0.000000 | 53129640 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,305 | 0.018435 | 53129640 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,746,738 | 408.008844 | 53129640 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,864 | 0.000013 | 53129640 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 1,688,251 | 0.000013 | 53129640 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,546,102 | 0.000266 | 53129640 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,480,834 | 0.005770 | 53129640 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,916 | 0.826527 | 53129640 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53129640 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,425,484 | 3,427.330591 | 53129640 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,361,494 | 14,094.533247 | 53129640 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,230,050 | 0.000266 | 53129640 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,650 | 65.538581 | 53129640 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,204,426 | 3,405.064240 | 53129640 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,180,580 | 2,306.865276 | 53129640 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,141,608 | 0.000000 | 53129640 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,133,615 | 1,088,552.703489 | 53129640 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,131,558 | 37,122,688.831356 | 53129640 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,101,584 | 498,590.256602 | 53129640 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,064,823 | 72,055.946109 | 53129640 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,018 | 20,170,039.012473 | 53129640 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,046,743 | 57.133574 | 53129640 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,026,899 | 17.585922 | 53129640 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,004,035 | 0.039905 | 53129640 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 950,121 | 2,317.651230 | 53129640 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 911,236 | 1,090.406317 | 53129640 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 902,597 | 2.309155 | 53129640 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 889,713 | 0.000557 | 53129640 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 878,135 | 18.001612 | 53129640 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 867,987 | 91.815708 | 53129640 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 856,129 | 17.127755 | 53129640 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 842,852 | 2,309.053584 | 53129640 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 797,274 | 0.000008 | 53129640 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 793,457 | 0.056423 | 53129640 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 781,803 | 0.803146 | 53129640 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 734,151 | 0.611245 | 53129640 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 729,998 | 4,723,420.760049 | 53129640 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 697,266 | 0.611582 | 53129640 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 695,289 | 138,807.148747 | 53129640 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 688,473 | 499,987.478320 | 53129640 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 677,332 | 0.109699 | 53129640 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 4174 ; routes examinées : 81451436 ; candidats optimisés : 264871 ; net attendu > 0 : 216 ; dernier cycle 422.4 ms
- Rejets (moteur) : {'spread_below_threshold': 79983013, 'liquidity_below_min': 1017917, 'negative_expected_net': 264655, 'pool_quarantined': 90664, 'unquotable': 90214, 'borrow_bound_too_small': 4170, 'cycle_budget_exhausted': 587}
- Enregistrements de la session : 264871 ; net attendu > 0 : 216 ; simulés (eth_call de la vraie tx) : 31 (ok 3, échec 28) ; étiquettes ghost N+1 : 3/29 positives
- Décisions : {'REJECTED': 264871} ; motifs de rejet : {'below_safety_margin': 95, 'negative_expected_net': 264655, 'p_lower_below_threshold': 166, 'price_impact': 8, 'reliability_not_demonstrated': 50, 'simulation_failed': 28}

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
