# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T22:56:04+00:00 ; durée 124.47 min ; blocs 53258868 → 53262604 (3454 vus)

## Connexion
- Requêtes RPC : 41695 ; erreurs : 15 ; latence p50/p95 : 229.3/1,056.9 ms
- Rafraîchissements d'état : 3454 ; âge des données au dernier bloc : 4.2 s ; changements de frais LP observés (pools à frais dynamiques) : 12461
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 126548 ; cycles déclenchés par événement : 3536 ; avance médiane sur le rafraîchissement multicall : 698 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,275.16 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 499 pools, 290 jetons, 18414 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 319, par paires 0), mesurés 502, sous le plancher de 10000.0 $ : 3 → gardés 499 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2268.963647, 'cbBTC': 79202.631326, 'AERO': 0.656707}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,790,931 | 2,275.164955 | 53262604 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,281,492 | 0.028812 | 53262604 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,597,274 | 0.000013 | 53262604 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,220,442 | 0.028764 | 53262604 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,161,718 | 2,272.346181 | 53262604 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,929,551 | 99.753106 | 53262604 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,799,220 | 0.001605 | 53262604 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,158,778 | 1.569535 | 53262604 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,671,196 | 0.028803 | 53262604 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,351,682 | 2,272.906750 | 53262604 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,339,035 | 2,273.257651 | 53262604 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,159,647 | 0.998727 | 53262604 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,589,014 | 37,610.072714 | 53262604 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,829,204 | 0.028777 | 53262604 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2745 | 2,350,483 | 99.770079 | 53262604 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,085,285 | 1,206,880.704280 | 53262604 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,056,720 | 0.000013 | 53262604 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,797,378 | 0.018771 | 53262604 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,712,116 | 2,276.905678 | 53262604 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,712,006 | 417.131664 | 53262604 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,711,812 | 0.000000 | 53262604 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,693,327 | 0.000013 | 53262604 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,686,718 | 0.000013 | 53262604 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,587,161 | 0.000013 | 53262604 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,118 | 1.588216 | 53262604 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,578 | 0.827498 | 53262604 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,368,613 | 3,564.360056 | 53262604 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,365,946 | 0.005331 | 53262604 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,333,055 | 14,456.065595 | 53262604 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,232,385 | 2,272.294438 | 53262604 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,180,350 | 0.000252 | 53262604 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,179,805 | 69.810635 | 53262604 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,115,134 | 37,311,434.019650 | 53262604 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,069,950 | 519,097.942451 | 53262604 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,047,506 | 72,054.695055 | 53262604 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 1,034,641 | 0.000000 | 53262604 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,257 | 21,691,507.139382 | 53262604 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,020,649 | 17.880140 | 53262604 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,015,861 | 2,274.388050 | 53262604 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | VIRTUAL/WETH | 10000 | 991,017 | 0.000254 | 53262604 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 988,800 | 1,106,924.670165 | 53262604 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 981,147 | 0.043928 | 53262604 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 970,566 | 99.055324 | 53262604 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 967,308 | 3,539.295283 | 53262604 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/NOCK | 3000 | 958,767 | 68.101328 | 53262604 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 925,437 | 2,271.410543 | 53262604 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 903,194 | 1,054.257899 | 53262604 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 868,501 | 0.000546 | 53262604 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 848,590 | 19.044720 | 53262604 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 818,736 | 0.060270 | 53262604 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 770,104 | 0.803616 | 53262604 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 766,532 | 18.835936 | 53262604 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 726,753 | 4,628,502.084730 | 53262604 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 708,893 | 0.000008 | 53262604 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 703,567 | 0.573566 | 53262604 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 693,642 | 2.327816 | 53262604 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 664,105 | 147,866.836721 | 53262604 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 663,746 | 521,943.989781 | 53262604 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 642,370 | 0.521315 | 53262604 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 617,826 | 0.094455 | 53262604 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 6989 ; routes examinées : 128695446 ; candidats optimisés : 743209 ; net attendu > 0 : 1412 ; dernier cycle 266.9 ms
- Rejets (moteur) : {'spread_below_threshold': 125908189, 'liquidity_below_min': 2025846, 'negative_expected_net': 741797, 'cycle_budget_exhausted': 11219, 'borrow_bound_too_small': 6983}
- Enregistrements de la session : 743209 ; net attendu > 0 : 1412 ; simulés (eth_call de la vraie tx) : 39 (ok 10, échec 29) ; étiquettes ghost N+1 : 4/38 positives
- Décisions : {'REJECTED': 743209} ; motifs de rejet : {'below_safety_margin': 1156, 'negative_expected_net': 741797, 'p_lower_below_threshold': 1175, 'price_impact': 10, 'reliability_not_demonstrated': 237, 'simulation_failed': 29, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.087669 WETH | 0.007300 WETH | 0.000000 WETH | 0.000018 WETH | 0.007282 WETH (15.2342 €) | — | 830.57 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.083895 WETH | 0.006985 WETH | 0.000000 WETH | 0.000018 WETH | 0.006967 WETH (14.5760 €) | — | 830.43 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 194.516486 USDC | 15.588983 USDC | 0.000000 USDC | 0.042064 USDC | 15.546919 USDC (14.3032 €) | — | 799.26 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.074170 WETH | 0.006048 WETH | 0.000000 WETH | 0.000018 WETH | 0.006030 WETH (12.6155 €) | — | 812.97 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.073121 WETH | 0.005996 WETH | 0.000000 WETH | 0.000018 WETH | 0.005978 WETH (12.5070 €) | — | 817.55 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.071054 WETH | 0.005909 WETH | 0.000000 WETH | 0.000018 WETH | 0.005891 WETH (12.3250 €) | — | 829.09 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.070554 WETH | 0.005753 WETH | 0.000000 WETH | 0.000018 WETH | 0.005735 WETH (11.9978 €) | — | 812.79 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.069593 WETH | 0.005707 WETH | 0.000000 WETH | 0.000018 WETH | 0.005688 WETH (11.9009 €) | — | 817.36 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 158.488819 USDC | 12.466653 USDC | 0.000000 USDC | 0.041719 USDC | 12.424934 USDC (11.4309 €) | — | 783.96 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v2]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.066843 WETH | 0.005450 WETH | 0.000000 WETH | 0.000018 WETH | 0.005432 WETH (11.3656 €) | — | 812.72 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome]→USDC | 160.275220 USDC | 12.199157 USDC | 0.000000 USDC | 0.041750 USDC | 12.157407 USDC (11.1848 €) | — | 758.53 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53259987 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.001836 cbBTC | 0.000141 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC | 0.000141 cbBTC (10.2641 €) | — | 767.17 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.059219 WETH | 0.004823 WETH | 0.000000 WETH | 0.000018 WETH | 0.004804 WETH (10.0519 €) | — | 811.30 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.058561 WETH | 0.004796 WETH | 0.000000 WETH | 0.000018 WETH | 0.004778 WETH (9.9962 €) | — | 815.87 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.057714 WETH | 0.004686 WETH | 0.000000 WETH | 0.000018 WETH | 0.004667 WETH (9.7649 €) | — | 808.70 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 122.415685 USDC | 9.647129 USDC | 0.000000 USDC | 0.041405 USDC | 9.605724 USDC (8.8373 €) | — | 784.68 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53260683 | USDC→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 1,195.188380 USDC | 9.477670 USDC | 0.000000 USDC | 0.020085 USDC | 9.457585 USDC (8.7010 €) | — | 79.13 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v2]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.051575 WETH | 0.004117 WETH | 0.000000 WETH | 0.000018 WETH | 0.004099 WETH (8.5752 €) | — | 794.71 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v2]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.050859 WETH | 0.004083 WETH | 0.000000 WETH | 0.000018 WETH | 0.004065 WETH (8.5045 €) | — | 799.25 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome]→USDC | 119.707043 USDC | 8.934374 USDC | 0.000000 USDC | 0.041405 USDC | 8.892969 USDC (8.1815 €) | — | 742.89 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.043965 WETH | 0.003494 WETH | 0.000000 WETH | 0.000018 WETH | 0.003475 WETH (7.2710 €) | — | 790.48 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.043444 WETH | 0.003472 WETH | 0.000000 WETH | 0.000018 WETH | 0.003454 WETH (7.2261 €) | — | 795.02 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53260683 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 739.515088 USDC | 7.619124 USDC | 0.000000 USDC | 0.019190 USDC | 7.599934 USDC (6.9919 €) | — | 102.77 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53260683 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.324836 WETH | 0.003347 WETH | 0.000000 WETH | 0.000008 WETH | 0.003338 WETH (6.9771 €) | — | 102.77 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.001157 cbBTC | 0.000095 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC | 0.000095 cbBTC (6.9110 €) | — | 819.89 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3290 ; taux observé 0.107 ; borne inférieure crédible (0.9) 0.100 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
