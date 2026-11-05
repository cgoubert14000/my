# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T12:51:48+00:00 ; durée 163.31 min ; blocs 53541978 → 53546878 (4891 vus)

## Connexion
- Requêtes RPC : 59095 ; erreurs : 5 ; latence p50/p95 : 178.4/982.8 ms
- Rafraîchissements d'état : 4891 ; âge des données au dernier bloc : 2.83 s ; changements de frais LP observés (pools à frais dynamiques) : 5525
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 59473 ; cycles déclenchés par événement : 5691 ; avance médiane sur le rafraîchissement multicall : 1,135 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,392.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 288 jetons, 19416 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 310, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2417.172064, 'cbBTC': 80337.642272, 'AERO': 0.664358}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,675,800 | 2,392.756779 | 53546878 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,291,003 | 0.030036 | 53546878 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,581,832 | 0.030071 | 53546878 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,231,896 | 0.000013 | 53546878 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,244,895 | 2,387.847803 | 53546878 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,712,022 | 112.562644 | 53546878 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,774,154 | 0.001565 | 53546878 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,350,751 | 0.030036 | 53546878 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 5,337,185 | 1.550062 | 53546878 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,370,806 | 2,388.862536 | 53546878 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 204 | 4,192,729 | 0.999331 | 53546878 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,614,213 | 41,018.962922 | 53546878 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 773 | 3,435,015 | 2,388.045078 | 53546878 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,716,181 | 0.030058 | 53546878 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,232,788 | 1,164,309.449368 | 53546878 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,845,280 | 0.006914 | 53546878 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,819,700 | 0.000013 | 53546878 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,740,569 | 0.000000 | 53546878 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,724,078 | 0.017488 | 53546878 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,967 | 0.000013 | 53546878 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,615,038 | 452.366766 | 53546878 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,311 | 1.424265 | 53546878 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,548,928 | 0.000013 | 53546878 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,474,180 | 3,711.893858 | 53546878 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,014 | 0.817120 | 53546878 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/USDC | 3000 | 1,370,987 | 2,393.952420 | 53546878 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,370,500 | 2,393.008532 | 53546878 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,324,570 | 15,043.988277 | 53546878 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,254,544 | 2,387.900445 | 53546878 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,167,608 | 37,718,300.660506 | 53546878 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,292 | 73.310807 | 53546878 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,110,022 | 0.000000 | 53546878 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,091,655 | 565,639.590300 | 53546878 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,066,600 | 112.393148 | 53546878 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,052,518 | 23,039,107.409351 | 53546878 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,004,996 | 62.080068 | 53546878 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,780 | 19.509030 | 53546878 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 989,563 | 1,076.893850 | 53546878 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 958,357 | 0.000013 | 53546878 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 954,598 | 2,409.906906 | 53546878 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 948,799 | 97,015.547663 | 53546878 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 907,469 | 0.000541 | 53546878 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 866,322 | 0.047082 | 53546878 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 852,739 | 3,683.763346 | 53546878 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 824,022 | 19.984731 | 53546878 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 812,282 | 0.798912 | 53546878 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 811,112 | 0.059058 | 53546878 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 739,940 | 0.592175 | 53546878 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 731,665 | 5,059,791.249062 | 53546878 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 723,758 | 138,098.691403 | 53546878 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 723,111 | 0.000247 | 53546878 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 692,103 | 0.000008 | 53546878 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 670,466 | 0.568594 | 53546878 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 667,813 | 568,878.789942 | 53546878 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 642,174 | 0.914257 | 53546878 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 637,950 | 2.481761 | 53546878 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 598,887 | 746,901.317527 | 53546878 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 595,978 | 0.089029 | 53546878 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 570,230 | 0.039095 | 53546878 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 564,562 | 6,587.329689 | 53546878 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 10581 ; routes examinées : 205440696 ; candidats optimisés : 575420 ; net attendu > 0 : 435 ; dernier cycle 173.0 ms
- Rejets (moteur) : {'spread_below_threshold': 202016480, 'liquidity_below_min': 2837804, 'negative_expected_net': 574985, 'borrow_bound_too_small': 10577, 'cycle_budget_exhausted': 415}
- Enregistrements de la session : 575420 ; net attendu > 0 : 435 ; simulés (eth_call de la vraie tx) : 24 (ok 7, échec 17) ; étiquettes ghost N+1 : 4/22 positives
- Décisions : {'REJECTED': 575420} ; motifs de rejet : {'below_safety_margin': 405, 'negative_expected_net': 574985, 'p_lower_below_threshold': 395, 'reliability_not_demonstrated': 40, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 17, 'stale_data': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53545322 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 275.403994 USDC | 1.039397 USDC | 0.000000 USDC | 0.005442 USDC | 1.033955 USDC (0.9512 €) | — | 37.54 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53546498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.562613 WETH | 0.000210 WETH | 0.000000 WETH | 0.000003 WETH | 0.000207 WETH (0.4585 €) | — | 3.68 | 0.029 (n=289) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53546498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,348.351386 USDC | 0.502972 USDC | 0.000000 USDC | 0.006547 USDC | 0.496425 USDC (0.4567 €) | — | 3.68 | 0.029 (n=289) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53546498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.973775 WETH | 0.000165 WETH | 0.000000 WETH | 0.000003 WETH | 0.000162 WETH (0.3595 €) | — | 1.67 | 0.040 (n=230) | REJECTED | below_safety_margin(162364200074970<194755001232002), p_lower_below_threshold(0.04<0.75) |
| 53546498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,330.456691 USDC | 0.395369 USDC | 0.000000 USDC | 0.006182 USDC | 0.389187 USDC (0.3581 €) | — | 1.67 | 0.040 (n=230) | REJECTED | below_safety_margin(389187<466091), p_lower_below_threshold(0.04<0.75) |
| 53544070 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 5,239.460210 USDC | 0.370578 USDC | 0.000000 USDC | 0.006166 USDC | 0.364412 USDC (0.3353 €) | — | 0.70 | 0.033 (n=63) | REJECTED | below_safety_margin(364412<1047892), p_lower_below_threshold(0.03<0.75) |
| 53546498 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.503570 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000083 WETH (0.1845 €) | — | 1.65 | 0.001 (n=10) | REJECTED | below_safety_margin(83339351958796<100714020510957), reliability_not_demonstrated |
| 53545204 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 122.539819 USDC | 0.205768 USDC | 0.000000 USDC | 0.005435 USDC | 0.200333 USDC (0.1843 €) | — | 16.35 | 0.000 (n=96) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53546498 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,205.015413 USDC | 0.205592 USDC | 0.000000 USDC | 0.005816 USDC | 0.199776 USDC (0.1838 €) | — | 1.66 | 0.001 (n=10) | REJECTED | below_safety_margin(199776<241003), reliability_not_demonstrated |
| 53544070 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,487.252720 USDC | 0.159582 USDC | 0.000000 USDC | 0.006166 USDC | 0.153416 USDC (0.1411 €) | — | 1.03 | 0.040 (n=228) | REJECTED | below_safety_margin(153416<297450), p_lower_below_threshold(0.04<0.75) |
| 53546498 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006666 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0957 €) | — | 1.95 | 0.176 (n=942) | REJECTED | below_safety_margin(130<133), p_lower_below_threshold(0.18<0.75) |
| 53546498 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.258941 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | — | 1.67 | 0.176 (n=942) | REJECTED | below_safety_margin(43225482427872<51788100084523), p_lower_below_threshold(0.18<0.75) |
| 53543753 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.291862 WETH | 0.000045 WETH | 0.000000 WETH | 0.000002 WETH | 0.000043 WETH (0.0956 €) | — | 1.47 | 0.040 (n=228) | REJECTED | below_safety_margin(43000827415442<58372477421099), p_lower_below_threshold(0.04<0.75) |
| 53546498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 603.853057 USDC | 0.111223 USDC | 0.000000 USDC | 0.007290 USDC | 0.103933 USDC (0.0956 €) | — | 1.72 | 0.176 (n=942) | REJECTED | below_safety_margin(103933<120770), p_lower_below_threshold(0.18<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 702.965505 USDC | 0.109668 USDC | 0.000000 USDC | 0.005799 USDC | 0.103869 USDC (0.0956 €) | — | 1.48 | 0.040 (n=228) | REJECTED | below_safety_margin(103869<140593), p_lower_below_threshold(0.04<0.75) |
| 53546771 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.389406 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0936 €) | — | 1.09 | 0.176 (n=947) | REJECTED | below_safety_margin(42516602392955<77881246321050), p_lower_below_threshold(0.18<0.75) |
| 53546771 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.011112 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0931 €) | — | 1.14 | 0.176 (n=947) | REJECTED | below_safety_margin(127<222), p_lower_below_threshold(0.18<0.75) |
| 53546771 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 968.025034 USDC | 0.108334 USDC | 0.000000 USDC | 0.007307 USDC | 0.101027 USDC (0.0929 €) | — | 1.04 | 0.176 (n=947) | REJECTED | below_safety_margin(101027<193605), p_lower_below_threshold(0.18<0.75) |
| 53546498 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.008750 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0869 €) | — | 1.35 | 0.176 (n=942) | REJECTED | below_safety_margin(118<174), p_lower_below_threshold(0.18<0.75) |
| 53546498 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.295311 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0867 €) | — | 1.33 | 0.176 (n=942) | REJECTED | below_safety_margin(39154805172933<59062161974816), p_lower_below_threshold(0.18<0.75) |
| 53546498 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 654.128245 USDC | 0.101400 USDC | 0.000000 USDC | 0.007655 USDC | 0.093745 USDC (0.0862 €) | — | 1.43 | 0.176 (n=942) | REJECTED | below_safety_margin(93745<130825), p_lower_below_threshold(0.18<0.75) |
| 53546061 | WETH→[uniswap_v3]→CLANKER→[aerodrome_slipstream]→WETH | 0.014588 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0660 €) | — | 20.37 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53543753 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.234841 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0581 €) | — | 1.11 | 0.033 (n=63) | REJECTED | below_safety_margin(26147944501251<46968210313569), p_lower_below_threshold(0.03<0.75) |
| 53543753 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 566.507608 USDC | 0.068588 USDC | 0.000000 USDC | 0.005432 USDC | 0.063156 USDC (0.0581 €) | — | 1.11 | 0.033 (n=63) | REJECTED | below_safety_margin(63156<113301), p_lower_below_threshold(0.03<0.75) |
| 53543753 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.193982 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0516 €) | — | 1.20 | 0.040 (n=228) | REJECTED | below_safety_margin(23193184659714<38796370936021), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 5489 ; taux observé 0.157 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
