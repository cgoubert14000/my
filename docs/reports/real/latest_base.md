# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T12:08:28+00:00 ; durée 119.98 min ; blocs 53541978 → 53545579 (3599 vus)

## Connexion
- Requêtes RPC : 43524 ; erreurs : 5 ; latence p50/p95 : 131.7/733.0 ms
- Rafraîchissements d'état : 3599 ; âge des données au dernier bloc : 2.84 s ; changements de frais LP observés (pools à frais dynamiques) : 3315
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 32191 ; cycles déclenchés par événement : 3148 ; avance médiane sur le rafraîchissement multicall : 292 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,417.17 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 288 jetons, 19416 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 310, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2417.172064, 'cbBTC': 80337.642272, 'AERO': 0.664358}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,252,401 | 2,417.168640 | 53545578 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,444,972 | 0.030130 | 53545578 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,663,388 | 0.030091 | 53545578 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,264,467 | 0.000012 | 53545578 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,298,184 | 2,414.051376 | 53545578 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,777,886 | 112.933923 | 53545578 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,835,676 | 0.001572 | 53545578 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,396,546 | 0.030136 | 53545578 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 5,364,324 | 1.534418 | 53545578 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,419,644 | 2,413.521278 | 53545578 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,223,381 | 0.998936 | 53545578 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,649,570 | 41,053.077869 | 53545578 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,460,050 | 2,413.591532 | 53545578 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,740,319 | 0.030090 | 53545578 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,255,568 | 1,164,309.449368 | 53545578 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,835,255 | 0.006830 | 53545578 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,827,426 | 0.000012 | 53545578 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,757,804 | 0.000000 | 53545578 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,732,073 | 0.017621 | 53545578 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,685,104 | 0.000012 | 53545578 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,635,529 | 448.804595 | 53545578 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,317 | 1.424256 | 53545578 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,484 | 0.000012 | 53545578 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,489,201 | 3,703.070831 | 53545578 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,937 | 0.817202 | 53545578 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/USDC | 3000 | 1,377,963 | 2,420.761375 | 53545578 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,377,462 | 2,417.781772 | 53545578 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,340,290 | 14,867.170552 | 53545578 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,262,286 | 2,414.053312 | 53545578 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,179,521 | 37,718,300.660506 | 53545578 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,295 | 73.310460 | 53545578 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,141,506 | 0.000000 | 53545578 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,102,789 | 565,644.884299 | 53545578 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,076,935 | 112.141007 | 53545578 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,063,256 | 23,039,107.409351 | 53545578 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,003,850 | 62.221731 | 53545578 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 999,560 | 1,075.058612 | 53545578 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,703 | 19.412498 | 53545579 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 962,954 | 0.000012 | 53545578 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 958,244 | 97,063.141781 | 53545578 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 956,477 | 2,419.823218 | 53545578 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 920,120 | 0.000543 | 53545578 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 870,796 | 0.046795 | 53545578 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 861,439 | 3,677.577192 | 53545578 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 827,737 | 19.849974 | 53545578 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 820,569 | 0.798912 | 53545578 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 811,701 | 0.059150 | 53545578 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,221 | 0.599283 | 53545578 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 738,967 | 5,062,010.598066 | 53545578 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 734,404 | 136,872.892758 | 53545578 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,656 | 0.000247 | 53545578 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 698,173 | 0.000008 | 53545578 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 674,617 | 569,706.966218 | 53545578 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 670,466 | 0.568594 | 53545578 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 648,726 | 0.914257 | 53545578 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 644,009 | 2.484309 | 53545578 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 602,090 | 753,497.749855 | 53545578 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 597,360 | 0.089344 | 53545578 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 570,431 | 0.039117 | 53545578 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 569,805 | 6,599.283775 | 53545578 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 6746 ; routes examinées : 130980336 ; candidats optimisés : 325769 ; net attendu > 0 : 50 ; dernier cycle 107.6 ms
- Rejets (moteur) : {'spread_below_threshold': 128735265, 'liquidity_below_min': 1912422, 'negative_expected_net': 325719, 'borrow_bound_too_small': 6743, 'cycle_budget_exhausted': 137}
- Enregistrements de la session : 325769 ; net attendu > 0 : 50 ; simulés (eth_call de la vraie tx) : 6 (ok 4, échec 2) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 325769} ; motifs de rejet : {'below_safety_margin': 44, 'negative_expected_net': 325719, 'p_lower_below_threshold': 43, 'reliability_not_demonstrated': 7, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53545322 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 275.403994 USDC | 1.039397 USDC | 0.000000 USDC | 0.005442 USDC | 1.033955 USDC (0.9512 €) | — | 37.54 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53544070 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 5,239.460210 USDC | 0.370578 USDC | 0.000000 USDC | 0.006166 USDC | 0.364412 USDC (0.3353 €) | — | 0.70 | 0.033 (n=63) | REJECTED | below_safety_margin(364412<1047892), p_lower_below_threshold(0.03<0.75) |
| 53545204 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 122.539819 USDC | 0.205768 USDC | 0.000000 USDC | 0.005435 USDC | 0.200333 USDC (0.1843 €) | — | 16.35 | 0.000 (n=96) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53544070 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,487.252720 USDC | 0.159582 USDC | 0.000000 USDC | 0.006166 USDC | 0.153416 USDC (0.1411 €) | — | 1.03 | 0.040 (n=228) | REJECTED | below_safety_margin(153416<297450), p_lower_below_threshold(0.04<0.75) |
| 53543753 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.291862 WETH | 0.000045 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0956 €) | — | 1.47 | 0.040 (n=228) | REJECTED | below_safety_margin(43000827415442<58372477421099), p_lower_below_threshold(0.04<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 702.965505 USDC | 0.109668 USDC | 0.000000 USDC | 0.005799 USDC | 0.103869 USDC (0.0956 €) | — | 1.48 | 0.040 (n=228) | REJECTED | below_safety_margin(103869<140593), p_lower_below_threshold(0.04<0.75) |
| 53543753 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.234841 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0581 €) | — | 1.11 | 0.033 (n=63) | REJECTED | below_safety_margin(26147944501251<46968210313569), p_lower_below_threshold(0.03<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 566.507608 USDC | 0.068588 USDC | 0.000000 USDC | 0.005432 USDC | 0.063156 USDC (0.0581 €) | — | 1.11 | 0.033 (n=63) | REJECTED | below_safety_margin(63156<113301), p_lower_below_threshold(0.03<0.75) |
| 53543753 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.193982 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0516 €) | — | 1.20 | 0.040 (n=228) | REJECTED | below_safety_margin(23193184659714<38796370936021), p_lower_below_threshold(0.04<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 470.408050 USDC | 0.061449 USDC | 0.000000 USDC | 0.005432 USDC | 0.056017 USDC (0.0515 €) | — | 1.19 | 0.040 (n=228) | REJECTED | below_safety_margin(56017<94081), p_lower_below_threshold(0.04<0.75) |
| 53543753 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.198777 WETH | 0.000023 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0472 €) | — | 1.07 | 0.033 (n=63) | REJECTED | below_safety_margin(21217844609161<39755482760830), p_lower_below_threshold(0.03<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 478.647661 USDC | 0.056677 USDC | 0.000000 USDC | 0.005432 USDC | 0.051245 USDC (0.0471 €) | — | 1.07 | 0.033 (n=63) | REJECTED | below_safety_margin(51245<95729), p_lower_below_threshold(0.03<0.75) |
| 53542841 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 36.877139 USDC | 0.018745 USDC | 0.000000 USDC | 0.005433 USDC | 0.013312 USDC (0.0122 €) | 0.013312 USDC | 3.61 | 0.029 (n=285) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 256.143612 USDC | 0.019157 USDC | 0.000000 USDC | 0.007636 USDC | 0.011521 USDC (0.0106 €) | — | 0.45 | 0.176 (n=942) | REJECTED | below_safety_margin(11521<51228), p_lower_below_threshold(0.18<0.75) |
| 53543753 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.125717 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0105 €) | — | 0.37 | 0.176 (n=942) | REJECTED | below_safety_margin(4700728297632<25143316825794), p_lower_below_threshold(0.18<0.75) |
| 53543753 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002581 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0103 €) | — | 0.54 | 0.176 (n=942) | REJECTED | below_safety_margin(14<51), p_lower_below_threshold(0.18<0.75) |
| 53543753 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.027586 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0073 €) | — | 1.20 | 0.232 (n=385) | REJECTED | below_safety_margin(3301500843465<5517206624924), p_lower_below_threshold(0.23<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 66.336830 USDC | 0.015236 USDC | 0.000000 USDC | 0.007269 USDC | 0.007967 USDC (0.0073 €) | — | 1.20 | 0.232 (n=385) | REJECTED | below_safety_margin(7967<13267), p_lower_below_threshold(0.23<0.75) |
| 53544141 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.029837 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0072 €) | — | 1.09 | 0.176 (n=942) | REJECTED | below_safety_margin(3243506185752<5967339524183), p_lower_below_threshold(0.18<0.75) |
| 53544141 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.029837 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0072 €) | — | 1.09 | 0.176 (n=942) | REJECTED | below_safety_margin(3243506185752<5967339524183), p_lower_below_threshold(0.18<0.75) |
| 53543490 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 253.216668 USDC | 0.013211 USDC | 0.000000 USDC | 0.005435 USDC | 0.007776 USDC (0.0072 €) | — | 0.31 | 0.040 (n=228) | REJECTED | below_safety_margin(7776<50643), p_lower_below_threshold(0.04<0.75) |
| 53544141 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 77.329655 USDC | 0.014936 USDC | 0.000000 USDC | 0.007272 USDC | 0.007664 USDC (0.0071 €) | — | 0.99 | 0.176 (n=942) | REJECTED | below_safety_margin(7664<15465), p_lower_below_threshold(0.18<0.75) |
| 53544141 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 77.329655 USDC | 0.014936 USDC | 0.000000 USDC | 0.007272 USDC | 0.007664 USDC (0.0071 €) | — | 0.99 | 0.176 (n=942) | REJECTED | below_safety_margin(7664<15465), p_lower_below_threshold(0.18<0.75) |
| 53543490 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.002512 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0066 €) | — | 0.36 | 0.040 (n=228) | REJECTED | below_safety_margin(9<50), p_lower_below_threshold(0.04<0.75) |
| 53544141 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000875 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0066 €) | — | 1.03 | 0.176 (n=942) | REJECTED | below_safety_margin(9<17), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5472 ; taux observé 0.157 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
