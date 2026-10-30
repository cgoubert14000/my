# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T13:51:02+00:00 ; durée 9.11 min ; blocs 53289181 → 53289457 (274 vus)

## Connexion
- Requêtes RPC : 3296 ; erreurs : 0 ; latence p50/p95 : 74.4/776.4 ms
- Rafraîchissements d'état : 275 ; âge des données au dernier bloc : 0.62 s ; changements de frais LP observés (pools à frais dynamiques) : 819
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7618 ; cycles déclenchés par événement : 345 ; avance médiane sur le rafraîchissement multicall : 474 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,216.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,220,243 | 2,216.395940 | 53289457 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,007,090 | 0.028867 | 53289457 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,543,576 | 0.000013 | 53289457 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,965,390 | 0.028860 | 53289457 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,069,602 | 2,213.628200 | 53289457 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,704,874 | 100.148459 | 53289457 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,631,894 | 0.001615 | 53289457 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,035,393 | 1.624413 | 53289457 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,504,227 | 0.028873 | 53289457 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 728 | 4,172,036 | 2,214.186473 | 53289457 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,038,976 | 0.999939 | 53289457 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,018,716 | 2,214.344211 | 53289457 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,531,489 | 36,864.448851 | 53289457 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,740,781 | 0.028852 | 53289457 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,316,618 | 100.181127 | 53289457 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,030,754 | 1,207,672.376600 | 53289457 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,910,582 | 0.000013 | 53289457 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,767,540 | 0.018232 | 53289457 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,692,290 | 0.000000 | 53289457 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,667,513 | 417.627109 | 53289457 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,655,653 | 0.000013 | 53289457 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,558,542 | 0.000013 | 53289457 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,528,584 | 2,217.385547 | 53289457 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,463,389 | 1.643209 | 53289457 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 1,458,031 | 0.000013 | 53289457 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,887 | 0.824971 | 53289457 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,390,706 | 3,594.744225 | 53289457 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,306,501 | 2,213.378989 | 53289457 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,296,982 | 14,486.288531 | 53289457 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,267,545 | 0.005028 | 53289457 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,067 | 70.016773 | 53289457 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,093,720 | 36,265,727.250085 | 53289457 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,045,404 | 515,828.434616 | 53289457 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,023,918 | 21,083,127.034335 | 53289457 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,004,018 | 74,432.473106 | 53289457 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,003,719 | 2,216.932526 | 53289457 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 995,319 | 0.000000 | 53289457 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,328 | 19.260784 | 53289457 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 968,598 | 66.726688 | 53289457 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 954,305 | 99.903240 | 53289457 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 951,726 | 0.045241 | 53289457 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 921,594 | 1,209,274.366068 | 53289457 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 915,979 | 2,231.397776 | 53289457 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 871,873 | 1,083.811894 | 53289457 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 856,270 | 3,587.716388 | 53289457 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 853,918 | 0.000556 | 53289457 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 831,646 | 19.651882 | 53289457 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 811,344 | 0.059110 | 53289457 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 781,558 | 17.950100 | 53289457 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 750,212 | 0.803616 | 53289457 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 723,418 | 0.000260 | 53289457 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 708,392 | 0.577559 | 53289457 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 705,676 | 4,659,770.357888 | 53289457 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 686,299 | 0.000008 | 53289457 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 675,581 | 2.328550 | 53289457 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 648,865 | 516,023.333139 | 53289457 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 648,843 | 147,091.457185 | 53289457 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 640,152 | 0.517611 | 53289457 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 603,933 | 0.091146 | 53289457 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 596,052 | 0.914771 | 53289457 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 619 ; routes examinées : 11598822 ; candidats optimisés : 70090 ; net attendu > 0 : 493 ; dernier cycle 199.2 ms
- Rejets (moteur) : {'spread_below_threshold': 11299790, 'liquidity_below_min': 221208, 'negative_expected_net': 69597, 'unquotable': 6871, 'borrow_bound_too_small': 618, 'cycle_budget_exhausted': 152}
- Enregistrements de la session : 70080 ; net attendu > 0 : 493 ; simulés (eth_call de la vraie tx) : 19 (ok 17, échec 2) ; étiquettes ghost N+1 : 4/11 positives
- Décisions : {'REJECTED': 70080} ; motifs de rejet : {'below_safety_margin': 430, 'negative_expected_net': 69587, 'p_lower_below_threshold': 440, 'reliability_not_demonstrated': 53, 'sim_below_estimate': 3, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53289450 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.270767 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0376 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(18423171082899<54153435228351), p_lower_below_threshold(0.04<0.75) |
| 53289450 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.270767 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0376 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(18423171082899<54153435228351), p_lower_below_threshold(0.04<0.75) |
| 53289450 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 597.627664 USDC | 0.046181 USDC | 0.000000 USDC | 0.005422 USDC | 0.040759 USDC (0.0375 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(40759<119525), p_lower_below_threshold(0.04<0.75) |
| 53289450 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 597.627664 USDC | 0.046181 USDC | 0.000000 USDC | 0.005422 USDC | 0.040759 USDC (0.0375 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(40759<119525), p_lower_below_threshold(0.04<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069651 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | — | 1.78 | 0.163 (n=260) | REJECTED | below_safety_margin(12418220348479<13930177782132), p_lower_below_threshold(0.16<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069651 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | — | 1.78 | 0.163 (n=260) | REJECTED | below_safety_margin(12418220348479<13930177782132), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 153.449517 USDC | 0.034317 USDC | 0.000000 USDC | 0.006814 USDC | 0.027503 USDC (0.0253 €) | — | 1.79 | 0.163 (n=260) | REJECTED | below_safety_margin(27503<30689), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 153.449517 USDC | 0.034317 USDC | 0.000000 USDC | 0.006814 USDC | 0.027503 USDC (0.0253 €) | — | 1.79 | 0.163 (n=260) | REJECTED | below_safety_margin(27503<30689), p_lower_below_threshold(0.16<0.75) |
| 53289409 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005817 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0247 €) | — | 0.60 | 0.001 (n=14) | REJECTED | below_safety_margin(35<116), reliability_not_demonstrated |
| 53289409 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.206185 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0246 €) | — | 0.59 | 0.001 (n=14) | REJECTED | below_safety_margin(12076796169334<41236949996657), reliability_not_demonstrated |
| 53289409 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 489.139675 USDC | 0.033850 USDC | 0.000000 USDC | 0.007131 USDC | 0.026719 USDC (0.0246 €) | — | 0.55 | 0.001 (n=14) | REJECTED | below_safety_margin(26719<97827), reliability_not_demonstrated |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.087989 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0226 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(11054198859110<17597794778243), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.087989 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0226 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(11054198859110<17597794778243), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 194.969906 USDC | 0.031292 USDC | 0.000000 USDC | 0.006814 USDC | 0.024478 USDC (0.0225 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(24478<38993), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 194.969906 USDC | 0.031292 USDC | 0.000000 USDC | 0.006814 USDC | 0.024478 USDC (0.0225 €) | — | 1.26 | 0.137 (n=587) | REJECTED | below_safety_margin(24478<38993), p_lower_below_threshold(0.14<0.75) |
| 53289409 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005393 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0219 €) | — | 0.57 | 0.137 (n=587) | REJECTED | below_safety_margin(31<107), p_lower_below_threshold(0.14<0.75) |
| 53289409 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.179956 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0216 €) | — | 0.59 | 0.137 (n=587) | REJECTED | below_safety_margin(10586526255970<35991218764174), p_lower_below_threshold(0.14<0.75) |
| 53289409 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 451.796142 USDC | 0.030046 USDC | 0.000000 USDC | 0.007131 USDC | 0.022915 USDC (0.0211 €) | — | 0.51 | 0.137 (n=587) | REJECTED | below_safety_margin(22915<90359), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.061192 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0193 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(9420108116413<12238423936110), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.061192 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0193 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(9420108116413<12238423936110), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 135.598893 USDC | 0.027673 USDC | 0.000000 USDC | 0.006814 USDC | 0.020859 USDC (0.0192 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(20859<27119), p_lower_below_threshold(0.14<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 135.598893 USDC | 0.027673 USDC | 0.000000 USDC | 0.006814 USDC | 0.020859 USDC (0.0192 €) | — | 1.54 | 0.137 (n=587) | REJECTED | below_safety_margin(20859<27119), p_lower_below_threshold(0.14<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.059869 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | — | 1.39 | 0.163 (n=260) | REJECTED | below_safety_margin(8336129713696<11973719896332), p_lower_below_threshold(0.16<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.059869 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | — | 1.39 | 0.163 (n=260) | REJECTED | below_safety_margin(8336129713696<11973719896332), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 132.023925 USDC | 0.025269 USDC | 0.000000 USDC | 0.006814 USDC | 0.018455 USDC (0.0170 €) | — | 1.40 | 0.163 (n=260) | REJECTED | below_safety_margin(18455<26404), p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 3661 ; taux observé 0.117 ; borne inférieure crédible (0.9) 0.110 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
