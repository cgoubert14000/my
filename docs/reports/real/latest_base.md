# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T00:06:35+00:00 ; durée 70.41 min ; blocs 53521807 → 53523923 (2102 vus)

## Connexion
- Requêtes RPC : 22911 ; erreurs : 0 ; latence p50/p95 : 324.0/1,481.2 ms
- Rafraîchissements d'état : 2103 ; âge des données au dernier bloc : 2.08 s ; changements de frais LP observés (pools à frais dynamiques) : 2777
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 481 ; cycles déclenchés par événement : 54 ; avance médiane sur le rafraîchissement multicall : 480 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,427.01 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 289 jetons, 19656 routes
- Par DEX : uniswap_v3 145, aerodrome_slipstream 108, aerodrome 206, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3710 (énumérés 312, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2435.517454, 'cbBTC': 80725.683876, 'AERO': 0.642935}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,766,571 | 2,427.014277 | 53523923 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,365,729 | 0.030075 | 53523923 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,691,543 | 0.030150 | 53523923 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,453,506 | 0.000012 | 53523923 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,382,988 | 2,420.987905 | 53523923 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,816,633 | 112.732005 | 53523923 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,830,040 | 0.001551 | 53523923 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,306,117 | 1.574089 | 53523923 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,027,514 | 0.030063 | 53523923 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,335,841 | 2,420.329098 | 53523923 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,247,705 | 0.999050 | 53523923 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,712,693 | 39,992.792252 | 53523923 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 639 | 3,484,099 | 2,420.148525 | 53523923 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2535 | 2,758,323 | 0.030135 | 53523923 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,267,339 | 1,161,662.081839 | 53523923 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,973,579 | 0.007501 | 53523923 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,828,609 | 0.000012 | 53523923 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,780,306 | 0.000000 | 53523923 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,185 | 0.017963 | 53523923 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,690,659 | 0.000012 | 53523923 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,644,891 | 446.319033 | 53523923 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,555,771 | 0.000012 | 53523923 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,440 | 1.472010 | 53523923 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,466,917 | 3,810.912568 | 53523923 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,448 | 0.816604 | 53523923 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,413,668 | 2,420.975251 | 53523923 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,380,901 | 2,427.416099 | 53523923 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,380,242 | 2,427.038905 | 53523923 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,350,196 | 14,807.871116 | 53523923 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,189,000 | 37,351,625.033570 | 53523923 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,296 | 73.310294 | 53523923 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,142,143 | 0.000000 | 53523923 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,110,869 | 560,350.683457 | 53523923 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,071,987 | 111.932255 | 53523923 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,068,725 | 23,018,393.135731 | 53523923 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 996,409 | 1,076.997952 | 53523923 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 992,260 | 19.380634 | 53523923 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 982,305 | 64.900043 | 53523923 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 966,534 | 0.000012 | 53523923 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 966,414 | 96,207.782241 | 53523923 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 958,061 | 2,419.823218 | 53523923 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 917,161 | 0.000536 | 53523923 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 868,359 | 0.046588 | 53523923 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 852,267 | 3,790.454216 | 53523923 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 831,341 | 19.716433 | 53523923 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 823,791 | 0.799146 | 53523923 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 802,741 | 0.057785 | 53523923 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 751,200 | 4,937,807.130895 | 53523923 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 749,031 | 0.598144 | 53523923 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 741,767 | 135,242.048689 | 53523923 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 732,739 | 0.000246 | 53523923 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 688,720 | 0.000008 | 53523923 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 680,634 | 559,099.812907 | 53523923 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 675,159 | 0.576246 | 53523923 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 651,428 | 0.914089 | 53523923 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 640,926 | 2.516852 | 53523923 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 622,314 | 0.106855 | 53523923 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 608,512 | 0.091919 | 53523923 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/DRV | 3000 | 578,771 | 6,448.681490 | 53523923 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| uniswap_v3 | FLOCK/USDC | 3000 | 572,299 | 0.039324 | 53523923 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 2156 ; routes examinées : 42378336 ; candidats optimisés : 111009 ; net attendu > 0 : 46 ; dernier cycle 358.6 ms
- Rejets (moteur) : {'spread_below_threshold': 41851993, 'liquidity_below_min': 415152, 'negative_expected_net': 110963, 'cycle_budget_exhausted': 182}
- Enregistrements de la session : 111009 ; net attendu > 0 : 46 ; simulés (eth_call de la vraie tx) : 13 (ok 12, échec 1) ; étiquettes ghost N+1 : 0/13 positives
- Décisions : {'REJECTED': 111009} ; motifs de rejet : {'below_safety_margin': 19, 'negative_expected_net': 110963, 'p_lower_below_threshold': 43, 'reliability_not_demonstrated': 3, 'simulation_failed': 1, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53521849 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.093750 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2310 €) | 0.000103 WETH | 11.00 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 228.057798 USDC | 0.258391 USDC | 0.000000 USDC | 0.007320 USDC | 0.251071 USDC (0.2310 €) | — | 11.01 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.095513 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2303 €) | 0.000103 WETH | 10.76 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 232.330795 USDC | 0.257687 USDC | 0.000000 USDC | 0.007320 USDC | 0.250367 USDC (0.2303 €) | — | 10.78 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.095575 WETH | 0.000105 WETH | 0.000000 WETH | 0.000003 WETH | 0.000102 WETH (0.2292 €) | 0.000102 WETH | 10.70 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 232.397471 USDC | 0.256437 USDC | 0.000000 USDC | 0.007320 USDC | 0.249117 USDC (0.2292 €) | — | 10.72 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.095305 WETH | 0.000105 WETH | 0.000000 WETH | 0.000003 WETH | 0.000102 WETH (0.2275 €) | — | 10.66 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 232.330795 USDC | 0.254631 USDC | 0.000000 USDC | 0.007320 USDC | 0.247311 USDC (0.2275 €) | — | 10.64 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.091928 WETH | 0.000098 WETH | 0.000000 WETH | 0.000003 WETH | 0.000095 WETH (0.2135 €) | — | 10.37 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 224.164697 USDC | 0.239385 USDC | 0.000000 USDC | 0.007320 USDC | 0.232065 USDC (0.2135 €) | — | 10.35 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.069904 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1736 €) | — | 11.09 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 170.112430 USDC | 0.196308 USDC | 0.000000 USDC | 0.007689 USDC | 0.188619 USDC (0.1735 €) | — | 11.09 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH | 0.021917 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0598 €) | — | 12.17 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521849 | USDC→[uniswap_v3]→cbXRP→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 52.842361 USDC | 0.072162 USDC | 0.000000 USDC | 0.007320 USDC | 0.064842 USDC (0.0597 €) | — | 12.27 | 0.090 (n=131) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53521837 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 28.710657 USDC | 0.020882 USDC | 0.000000 USDC | 0.005469 USDC | 0.015413 USDC (0.0142 €) | — | 5.37 | 0.032 (n=263) | REJECTED | stale_data(4495ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53523789 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 27.107666 USDC | 0.018391 USDC | 0.000000 USDC | 0.005499 USDC | 0.012892 USDC (0.0119 €) | 0.012892 USDC | 4.76 | 0.031 (n=264) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53523793 | WETH→[aerodrome_slipstream]→DRV→[uniswap_v3]→WETH | 0.003263 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0076 €) | 0.000003 WETH | 10.42 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53522534 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.007723 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0074 €) | 0.000003 WETH | 4.28 | 0.292 (n=150) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53522534 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 18.726666 USDC | 0.014963 USDC | 0.000000 USDC | 0.006965 USDC | 0.007998 USDC (0.0074 €) | — | 4.27 | 0.292 (n=150) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53522534 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.007648 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0070 €) | 0.000003 WETH | 4.07 | 0.292 (n=150) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53522534 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 18.438964 USDC | 0.014496 USDC | 0.000000 USDC | 0.006965 USDC | 0.007531 USDC (0.0069 €) | — | 4.08 | 0.292 (n=150) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53523793 | WETH→[aerodrome_slipstream]→DRV→[aerodrome]→WETH | 0.003057 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0064 €) | 0.000003 WETH | 9.44 | 0.009 (n=31) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53522534 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.007439 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0063 €) | 0.000003 WETH | 3.80 | 0.153 (n=106) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53522534 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 17.946321 USDC | 0.013796 USDC | 0.000000 USDC | 0.006965 USDC | 0.006831 USDC (0.0063 €) | — | 3.81 | 0.153 (n=106) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53522841 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.950989 USDC | 0.010036 USDC | 0.000000 USDC | 0.005455 USDC | 0.004581 USDC (0.0042 €) | 0.004581 USDC | 2.30 | 0.043 (n=213) | REJECTED | p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 5281 ; taux observé 0.162 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
