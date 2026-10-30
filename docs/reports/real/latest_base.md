# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T08:27:27+00:00 ; durée 21.33 min ; blocs 53279104 → 53279749 (604 vus)

## Connexion
- Requêtes RPC : 7351 ; erreurs : 5 ; latence p50/p95 : 207.7/1,370.2 ms
- Rafraîchissements d'état : 605 ; âge des données au dernier bloc : 1.42 s ; changements de frais LP observés (pools à frais dynamiques) : 1207
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5673 ; cycles déclenchés par événement : 310 ; avance médiane sur le rafraîchissement multicall : 1,050 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.29 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18652 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 114, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 499, sous le plancher de 10000.0 $ : 2 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.189813, 'cbBTC': 78005.931316, 'AERO': 0.620161}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,104,629 | 2,229.286475 | 53279749 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,095,303 | 0.028571 | 53279749 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,516,152 | 0.000013 | 53279749 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,045,447 | 0.028627 | 53279749 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,081,753 | 2,226.127058 | 53279749 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,839,509 | 97.983259 | 53279749 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,771,146 | 0.001630 | 53279749 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,084,104 | 1.603394 | 53279749 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,505,183 | 0.028573 | 53279749 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,138,478 | 2,226.352151 | 53279749 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,106,691 | 0.999256 | 53279749 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 803 | 3,741,738 | 2,226.478940 | 53279749 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,563,624 | 36,624.920742 | 53279749 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,764,246 | 0.028615 | 53279749 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,346,130 | 98.038145 | 53279749 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,032,198 | 1,220,025.263374 | 53279749 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 1,932,785 | 0.000013 | 53279749 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,793,503 | 0.018717 | 53279749 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,678,918 | 416.356072 | 53279749 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,669,071 | 0.000013 | 53279749 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,668,426 | 0.000000 | 53279749 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,646,330 | 0.000013 | 53279749 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,537,987 | 2,232.161919 | 53279749 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,474,908 | 0.000013 | 53279749 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,202 | 1.642297 | 53279749 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,516 | 0.825813 | 53279749 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,398,325 | 3,577.107322 | 53279749 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,961 | 14,566.082943 | 53279749 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,199 | 0.005125 | 53279749 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,290,517 | 2,226.139142 | 53279749 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,305 | 69.988581 | 53279749 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,072 | 36,634,242.088427 | 53279749 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,127 | 516,029.790227 | 53279749 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,017,025 | 73,387.035573 | 53279749 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,014,717 | 21,637,514.256039 | 53279749 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,605 | 2,230.180854 | 53279749 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 998,840 | 0.000000 | 53279749 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 998,204 | 19.046056 | 53279749 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 970,567 | 97.296352 | 53279749 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 969,085 | 66.659379 | 53279749 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 946,016 | 3,596.785352 | 53279749 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/VVV | 3000 | 939,173 | 0.043990 | 53279749 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 917,526 | 1,234,253.296737 | 53279749 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 913,170 | 2,231.397776 | 53279749 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 877,516 | 1,076.984884 | 53279749 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,653 | 0.000559 | 53279749 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 835,402 | 19.515425 | 53279749 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,786 | 0.059646 | 53279749 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 789,318 | 17.864105 | 53279749 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,575 | 0.803616 | 53279749 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,882 | 0.000259 | 53279749 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,042 | 0.580976 | 53279749 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,844 | 4,725,086.898122 | 53279749 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 695,884 | 0.000008 | 53279749 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,411 | 2.329059 | 53279749 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 656,729 | 145,254.866782 | 53279749 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2111 | 652,478 | 514,298.039264 | 53279749 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 648,933 | 0.531326 | 53279749 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,010 | 0.091638 | 53279749 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 599,334 | 0.915335 | 53279749 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 914 ; routes examinées : 17047928 ; candidats optimisés : 75529 ; net attendu > 0 : 96 ; dernier cycle 424.0 ms
- Rejets (moteur) : {'spread_below_threshold': 16745853, 'liquidity_below_min': 218913, 'negative_expected_net': 75433, 'unquotable': 6550, 'borrow_bound_too_small': 913, 'cycle_budget_exhausted': 170}
- Enregistrements de la session : 75529 ; net attendu > 0 : 96 ; simulés (eth_call de la vraie tx) : 4 (ok 3, échec 1) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 75529} ; motifs de rejet : {'below_safety_margin': 91, 'negative_expected_net': 75433, 'p_lower_below_threshold': 80, 'reliability_not_demonstrated': 16, 'simulation_failed': 1}

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
| 53279712 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 497.548831 USDC | 0.033829 USDC | 0.000000 USDC | 0.007055 USDC | 0.026774 USDC (0.0246 €) | — | 0.54 | 0.128 (n=576) | REJECTED | below_safety_margin(26774<99509), p_lower_below_threshold(0.13<0.75) |
| 53279712 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.230226 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0246 €) | — | 0.52 | 0.128 (n=576) | REJECTED | below_safety_margin(11975755707719<46045120205816), p_lower_below_threshold(0.13<0.75) |
| 53279712 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.006448 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0244 €) | — | 0.53 | 0.128 (n=576) | REJECTED | below_safety_margin(34<128), p_lower_below_threshold(0.13<0.75) |
| 53279712 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 452.134183 USDC | 0.031755 USDC | 0.000000 USDC | 0.007055 USDC | 0.024700 USDC (0.0227 €) | — | 0.55 | 0.001 (n=14) | REJECTED | below_safety_margin(24700<90426), reliability_not_demonstrated |
| 53279712 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.223095 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0223 €) | — | 0.49 | 0.001 (n=14) | REJECTED | below_safety_margin(10889214559778<44619042643038), reliability_not_demonstrated |
| 53279712 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.005724 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0222 €) | — | 0.54 | 0.001 (n=14) | REJECTED | below_safety_margin(31<114), reliability_not_demonstrated |
| 53279220 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.032358 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0156 €) | 0.000008 WETH | 2.35 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279220 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 71.771896 USDC | 0.023660 USDC | 0.000000 USDC | 0.006717 USDC | 0.016943 USDC (0.0156 €) | 0.016943 USDC | 2.36 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279435 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 338.731976 USDC | 0.020201 USDC | 0.000000 USDC | 0.005024 USDC | 0.015177 USDC (0.0140 €) | — | 0.45 | 0.032 (n=134) | REJECTED | below_safety_margin(15177<67746), p_lower_below_threshold(0.03<0.75) |
| 53279436 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 338.731976 USDC | 0.020201 USDC | 0.000000 USDC | 0.005024 USDC | 0.015177 USDC (0.0140 €) | — | 0.45 | 0.032 (n=134) | REJECTED | below_safety_margin(15177<67746), p_lower_below_threshold(0.03<0.75) |
| 53279435 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.152768 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0139 €) | — | 0.44 | 0.032 (n=134) | REJECTED | below_safety_margin(6793744438638<30553618913902), p_lower_below_threshold(0.03<0.75) |
| 53279436 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.152768 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0139 €) | — | 0.44 | 0.032 (n=134) | REJECTED | below_safety_margin(6793744438638<30553618913902), p_lower_below_threshold(0.03<0.75) |
| 53279220 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.030275 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | 0.000006 WETH | 2.09 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279220 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 67.404332 USDC | 0.020827 USDC | 0.000000 USDC | 0.006717 USDC | 0.014110 USDC (0.0130 €) | — | 2.09 | 0.129 (n=573) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 53279712 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001349 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 1.19 | 0.128 (n=576) | REJECTED | below_safety_margin(16<26), p_lower_below_threshold(0.13<0.75) |
| 53279712 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 109.096695 USDC | 0.019071 USDC | 0.000000 USDC | 0.007055 USDC | 0.012016 USDC (0.0111 €) | — | 1.10 | 0.128 (n=576) | REJECTED | below_safety_margin(12016<21819), p_lower_below_threshold(0.13<0.75) |
| 53279712 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.048643 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0110 €) | — | 1.10 | 0.128 (n=576) | REJECTED | below_safety_margin(5357540402500<9728541622655), p_lower_below_threshold(0.13<0.75) |
| 53279712 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000794 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 0.88 | 0.128 (n=576) | REJECTED | below_safety_margin(7<15), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 3595 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.105 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
