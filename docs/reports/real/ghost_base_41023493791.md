# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T08:18:15+00:00 ; durée 12.15 min ; blocs 53279104 → 53279473 (332 vus)

## Connexion
- Requêtes RPC : 4176 ; erreurs : 5 ; latence p50/p95 : 206.9/1,348.5 ms
- Rafraîchissements d'état : 332 ; âge des données au dernier bloc : 2.45 s ; changements de frais LP observés (pools à frais dynamiques) : 815
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5673 ; cycles déclenchés par événement : 310 ; avance médiane sur le rafraîchissement multicall : 1,050 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.30 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18652 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 114, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 499, sous le plancher de 10000.0 $ : 2 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.189813, 'cbBTC': 78005.931316, 'AERO': 0.620161}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,100,549 | 2,229.300166 | 53279473 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,094,144 | 0.028592 | 53279473 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,512,212 | 0.000013 | 53279473 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,043,648 | 0.028627 | 53279473 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,081,730 | 2,230.672489 | 53279473 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,839,852 | 97.975901 | 53279473 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,761,639 | 0.001628 | 53279473 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,088,839 | 1.600901 | 53279473 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,558,503 | 0.028602 | 53279473 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,138,460 | 2,230.399609 | 53279473 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,103,735 | 0.999256 | 53279473 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 579 | 3,741,749 | 2,230.455466 | 53279473 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,563,626 | 36,625.331128 | 53279473 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,763,873 | 0.028615 | 53279473 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,346,235 | 98.035148 | 53279473 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,032,211 | 1,220,025.263374 | 53279473 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,931,847 | 0.000013 | 53279473 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,791,250 | 0.018675 | 53279473 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,678,501 | 416.667606 | 53279473 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,668,436 | 0.000000 | 53279473 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,668,224 | 0.000013 | 53279473 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,645,617 | 0.000013 | 53279473 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,537,992 | 2,232.419244 | 53279473 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,474,154 | 0.000013 | 53279473 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,202 | 1.642297 | 53279473 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,762 | 0.825557 | 53279473 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,399,573 | 3,571.966172 | 53279473 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,000 | 14,581.862150 | 53279473 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,207 | 0.005125 | 53279473 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,291,423 | 2,230.656647 | 53279473 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,305 | 69.988581 | 53279473 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,079 | 36,634,242.088427 | 53279473 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,133 | 516,029.790227 | 53279473 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,017,031 | 73,387.035573 | 53279473 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,013,083 | 21,697,143.624595 | 53279473 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,608 | 2,230.179331 | 53279473 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 998,846 | 0.000000 | 53279473 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 998,821 | 19.012358 | 53279473 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 970,611 | 97.296347 | 53279473 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 969,629 | 66.584494 | 53279473 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 946,758 | 3,596.785352 | 53279473 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/VVV | 3000 | 939,231 | 0.043990 | 53279473 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 918,158 | 1,232,570.533544 | 53279473 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 913,173 | 2,231.397776 | 53279473 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 876,908 | 1,076.839351 | 53279473 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 859,942 | 0.000557 | 53279473 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 835,218 | 19.521901 | 53279473 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,764 | 0.059643 | 53279473 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 789,130 | 17.868824 | 53279473 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,580 | 0.803616 | 53279473 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,887 | 0.000259 | 53279473 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,033 | 0.580184 | 53279473 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,849 | 4,725,086.898122 | 53279473 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 696,332 | 0.000008 | 53279473 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,415 | 2.329059 | 53279473 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 655,183 | 145,942.233909 | 53279473 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2132 | 652,481 | 514,946.977739 | 53279473 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 646,262 | 0.527193 | 53279473 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 605,542 | 0.091531 | 53279473 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 599,338 | 0.915335 | 53279473 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 641 ; routes examinées : 11955932 ; candidats optimisés : 55841 ; net attendu > 0 : 71 ; dernier cycle 434.5 ms
- Rejets (moteur) : {'spread_below_threshold': 11733812, 'liquidity_below_min': 160455, 'negative_expected_net': 55770, 'unquotable': 5014, 'borrow_bound_too_small': 640, 'cycle_budget_exhausted': 170}
- Enregistrements de la session : 55841 ; net attendu > 0 : 71 ; simulés (eth_call de la vraie tx) : 4 (ok 3, échec 1) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 55841} ; motifs de rejet : {'below_safety_margin': 66, 'negative_expected_net': 55770, 'p_lower_below_threshold': 58, 'reliability_not_demonstrated': 13, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53279324 | WETH→[uniswap_v3]→MEY→[aerodrome]→WETH | 0.030287 WETH | 0.000076 WETH | 0.000000 WETH | 0.000002 WETH | 0.000074 WETH (0.1520 €) | — | 24.48 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53279399 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 475.925085 USDC | 0.034613 USDC | 0.000000 USDC | 0.007063 USDC | 0.027550 USDC (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(27550<95185), reliability_not_demonstrated |
| 53279399 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 475.925085 USDC | 0.034613 USDC | 0.000000 USDC | 0.007063 USDC | 0.027550 USDC (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(27550<95185), reliability_not_demonstrated |
| 53279399 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.212880 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(12328674289373<42575998243671), reliability_not_demonstrated |
| 53279399 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.212880 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(12328674289373<42575998243671), reliability_not_demonstrated |
| 53279399 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006055 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0251 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(35<121), reliability_not_demonstrated |
| 53279399 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006055 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0251 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(35<121), reliability_not_demonstrated |
| 53279220 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.032358 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0156 €) | 0.000008 WETH | 2.35 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279220 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 71.771896 USDC | 0.023660 USDC | 0.000000 USDC | 0.006717 USDC | 0.016943 USDC (0.0156 €) | 0.016943 USDC | 2.36 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279435 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 338.731976 USDC | 0.020201 USDC | 0.000000 USDC | 0.005024 USDC | 0.015177 USDC (0.0140 €) | — | 0.45 | 0.032 (n=134) | REJECTED | below_safety_margin(15177<67746), p_lower_below_threshold(0.03<0.75) |
| 53279436 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 338.731976 USDC | 0.020201 USDC | 0.000000 USDC | 0.005024 USDC | 0.015177 USDC (0.0140 €) | — | 0.45 | 0.032 (n=134) | REJECTED | below_safety_margin(15177<67746), p_lower_below_threshold(0.03<0.75) |
| 53279435 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.152768 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0139 €) | — | 0.44 | 0.032 (n=134) | REJECTED | below_safety_margin(6793744438638<30553618913902), p_lower_below_threshold(0.03<0.75) |
| 53279436 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.152768 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0139 €) | — | 0.44 | 0.032 (n=134) | REJECTED | below_safety_margin(6793744438638<30553618913902), p_lower_below_threshold(0.03<0.75) |
| 53279220 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.030275 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | 0.000006 WETH | 2.09 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279220 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 67.404332 USDC | 0.020827 USDC | 0.000000 USDC | 0.006717 USDC | 0.014110 USDC (0.0130 €) | — | 2.09 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279192 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.022228 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(1923940147941<4445615603556), p_lower_below_threshold(0.13<0.75) |
| 53279193 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.022228 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(1923940147941<4445615603556), p_lower_below_threshold(0.13<0.75) |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 48.923868 USDC | 0.010978 USDC | 0.000000 USDC | 0.006719 USDC | 0.004259 USDC (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(4259<9784), p_lower_below_threshold(0.13<0.75) |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 48.923868 USDC | 0.010978 USDC | 0.000000 USDC | 0.006719 USDC | 0.004259 USDC (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(4259<9784), p_lower_below_threshold(0.13<0.75) |
| 53279192 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.021433 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(1724303343048<4286625972274), p_lower_below_threshold(0.13<0.75) |
| 53279193 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.021433 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(1724303343048<4286625972274), p_lower_below_threshold(0.13<0.75) |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 47.809608 USDC | 0.010535 USDC | 0.000000 USDC | 0.006719 USDC | 0.003816 USDC (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(3816<9561), p_lower_below_threshold(0.13<0.75) |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 47.809608 USDC | 0.010535 USDC | 0.000000 USDC | 0.006719 USDC | 0.003816 USDC (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(3816<9561), p_lower_below_threshold(0.13<0.75) |
| 53279220 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.019975 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0034 €) | — | 0.83 | 0.129 (n=573) | REJECTED | below_safety_margin(1661020909764<3995097575205), p_lower_below_threshold(0.13<0.75) |
| 53279220 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 44.248619 USDC | 0.010408 USDC | 0.000000 USDC | 0.006717 USDC | 0.003691 USDC (0.0034 €) | — | 0.83 | 0.129 (n=573) | REJECTED | below_safety_margin(3691<8849), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 3595 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.105 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
