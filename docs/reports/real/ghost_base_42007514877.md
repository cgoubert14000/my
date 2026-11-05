# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T14:20:12+00:00 ; durée 251.73 min ; blocs 53541978 → 53549529 (7507 vus)

## Connexion
- Requêtes RPC : 89574 ; erreurs : 5 ; latence p50/p95 : 110.1/980.7 ms
- Rafraîchissements d'état : 7508 ; âge des données au dernier bloc : 1.52 s ; changements de frais LP observés (pools à frais dynamiques) : 9551
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 80554 ; cycles déclenchés par événement : 7984 ; avance médiane sur le rafraîchissement multicall : 515 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,383.90 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 288 jetons, 19416 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 310, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2417.172064, 'cbBTC': 80337.642272, 'AERO': 0.664358}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,407,856 | 2,383.896806 | 53549529 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,257,127 | 0.029989 | 53549529 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,551,030 | 0.030035 | 53549529 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,258,252 | 0.000013 | 53549529 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,224,755 | 2,379.179906 | 53549529 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,771,552 | 110.025433 | 53549529 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,770,683 | 0.001570 | 53549529 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,307,118 | 1.567278 | 53549529 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,305,546 | 0.029976 | 53549529 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,358,428 | 2,378.205147 | 53549529 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,183,831 | 0.999331 | 53549529 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,586,784 | 41,340.866979 | 53549529 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,427,904 | 2,378.406273 | 53549529 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,711,199 | 0.030020 | 53549529 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,222,478 | 1,166,450.380608 | 53549529 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,862,540 | 0.007025 | 53549529 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,819,594 | 0.000013 | 53549529 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,735,001 | 0.000000 | 53549529 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,717,614 | 0.017392 | 53549529 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,679,914 | 0.000013 | 53549529 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,614,043 | 447.925151 | 53549529 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,556,824 | 0.000013 | 53549529 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,309 | 1.424267 | 53549529 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,462,012 | 3,728.273911 | 53549529 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,999 | 0.817136 | 53549529 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | WETH/USDC | 3000 | 1,368,446 | 2,385.006639 | 53549529 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,367,964 | 2,384.185737 | 53549529 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,326,543 | 14,937.428322 | 53549529 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,248,089 | 2,379.069026 | 53549529 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,163,279 | 37,718,938.893924 | 53549529 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,272 | 73.313327 | 53549529 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,104,444 | 0.000000 | 53549529 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,087,616 | 565,634.502664 | 53549529 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,085,284 | 110.097723 | 53549529 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,048,620 | 23,039,107.409351 | 53549529 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 994,882 | 63.348757 | 53549529 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,404 | 19.260324 | 53549529 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 983,407 | 1,072.507532 | 53549529 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 956,976 | 0.000013 | 53549529 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 954,477 | 2,400.788204 | 53549529 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/EDEL | 7000 | 945,952 | 96,878.902712 | 53549529 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 907,014 | 0.000545 | 53549529 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 885,000 | 0.046220 | 53549529 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 846,476 | 3,700.823303 | 53549529 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 823,508 | 20.003451 | 53549529 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,812 | 0.059321 | 53549529 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 809,274 | 0.798912 | 53549529 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,464 | 0.589942 | 53549529 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 728,314 | 5,068,722.852529 | 53549529 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 720,168 | 0.000247 | 53549529 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 719,449 | 138,727.794996 | 53549529 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 687,203 | 0.000008 | 53549529 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 670,466 | 0.568594 | 53549529 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 665,348 | 567,360.399527 | 53549529 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 639,797 | 0.914257 | 53549529 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 635,154 | 2.484251 | 53549529 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 596,607 | 0.089170 | 53549529 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | cbBTC/EDGE | 7000 | 588,643 | 774,644.303862 | 53549529 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,170 | 0.038878 | 53549529 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 563,356 | 6,566.680257 | 53549529 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 15491 ; routes examinées : 300773256 ; candidats optimisés : 838406 ; net attendu > 0 : 639 ; dernier cycle 375.4 ms
- Rejets (moteur) : {'spread_below_threshold': 295676700, 'liquidity_below_min': 4236885, 'negative_expected_net': 837767, 'borrow_bound_too_small': 15486, 'pool_quarantined': 5268, 'cycle_budget_exhausted': 511}
- Enregistrements de la session : 838406 ; net attendu > 0 : 639 ; simulés (eth_call de la vraie tx) : 44 (ok 17, échec 27) ; étiquettes ghost N+1 : 5/39 positives
- Décisions : {'REJECTED': 838406} ; motifs de rejet : {'below_safety_margin': 539, 'negative_expected_net': 837767, 'p_lower_below_threshold': 568, 'reliability_not_demonstrated': 71, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 27, 'stale_data': 22}

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
| 53546947 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.014183 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000075 WETH (0.1641 €) | — | 52.55 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53546947 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 33.810639 USDC | 0.184547 USDC | 0.000000 USDC | 0.006606 USDC | 0.177941 USDC (0.1637 €) | — | 52.63 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53546947 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.014137 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1633 €) | — | 52.47 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53546947 | USDC→[uniswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 33.714190 USDC | 0.183714 USDC | 0.000000 USDC | 0.006606 USDC | 0.177108 USDC (0.1629 €) | — | 52.53 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53546947 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.014137 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1627 €) | — | 52.29 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53546947 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.014119 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1624 €) | — | 52.26 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53546947 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 33.657798 USDC | 0.183084 USDC | 0.000000 USDC | 0.006606 USDC | 0.176478 USDC (0.1624 €) | — | 52.43 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53546947 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 33.615634 USDC | 0.182778 USDC | 0.000000 USDC | 0.006606 USDC | 0.176172 USDC (0.1621 €) | — | 52.41 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53546947 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.014087 WETH | 0.000076 WETH | 0.000000 WETH | 0.000003 WETH | 0.000073 WETH (0.1615 €) | — | 52.09 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53546947 | USDC→[uniswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 33.575442 USDC | 0.181809 USDC | 0.000000 USDC | 0.006606 USDC | 0.175203 USDC (0.1612 €) | — | 52.18 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53546947 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.013727 WETH | 0.000073 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1554 €) | — | 51.42 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53546947 | USDC→[sushiswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 32.685572 USDC | 0.175191 USDC | 0.000000 USDC | 0.006606 USDC | 0.168585 USDC (0.1551 €) | — | 51.58 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53546947 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.012721 WETH | 0.000067 WETH | 0.000000 WETH | 0.000003 WETH | 0.000064 WETH (0.1419 €) | — | 50.67 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53546947 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 30.363713 USDC | 0.161019 USDC | 0.000000 USDC | 0.006969 USDC | 0.154050 USDC (0.1417 €) | — | 50.73 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53544070 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,487.252720 USDC | 0.159582 USDC | 0.000000 USDC | 0.006166 USDC | 0.153416 USDC (0.1411 €) | — | 1.03 | 0.040 (n=228) | REJECTED | below_safety_margin(153416<297450), p_lower_below_threshold(0.04<0.75) |
| 53546498 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006666 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0957 €) | — | 1.95 | 0.176 (n=942) | REJECTED | below_safety_margin(130<133), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5506 ; taux observé 0.157 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
