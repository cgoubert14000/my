# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-24T11:36:29+00:00 ; durée 12.21 min ; blocs 53025852 → 53026220 (367 vus)

## Connexion
- Requêtes RPC : 4440 ; erreurs : 0 ; latence p50/p95 : 146.1/866.7 ms
- Rafraîchissements d'état : 368 ; âge des données au dernier bloc : 2.01 s ; changements de frais LP observés (pools à frais dynamiques) : 316
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5319 ; cycles déclenchés par événement : 439 ; avance médiane sur le rafraîchissement multicall : 305 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,363.67 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 536 pools, 308 jetons, 19360 routes
- Par DEX : uniswap_v3 143, aerodrome 216, aerodrome_slipstream 133, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 348, par paires 0), mesurés 538, sous le plancher de 10000.0 $ : 2 → gardés 536 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2363.674955, 'cbBTC': 80533.217668, 'AERO': 0.705694}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,342,942 | 2,363.674982 | 53026220 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,984,494 | 0.029364 | 53026220 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,232,281 | 97.959003 | 53026220 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,142,014 | 0.029383 | 53026220 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,563,110 | 0.000012 | 53026220 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | USDC/AERO | 3000 | 8,926,991 | 1.421701 | 53026220 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,498,781 | 0.029369 | 53026220 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,199,637 | 2,363.581195 | 53026220 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,013,834 | 0.001644 | 53026220 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 6,302,093 | 0.000012 | 53026220 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,503,378 | 2,364.234295 | 53026220 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,458,256 | 0.029360 | 53026220 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 4,862,202 | 0.000012 | 53026220 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,554,882 | 2,364.196177 | 53026220 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,237,561 | 0.998962 | 53026220 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,923,284 | 34,372.485869 | 53026220 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,828,817 | 2,364.692574 | 53026220 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDT | 409 | 2,779,469 | 2,372.637842 | 53026220 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,502,156 | 97.991875 | 53026220 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,245,280 | 408.900563 | 53026220 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,118,648 | 1,261,906.512700 | 53026220 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 1,922,052 | 3,326.455783 | 53026220 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,920,076 | 0.000000 | 53026220 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,913,853 | 0.000012 | 53026220 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,797,225 | 0.018184 | 53026220 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,736,635 | 0.000012 | 53026220 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,604,120 | 0.000267 | 53026220 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,717 | 1.610679 | 53026220 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,463,555 | 3,349.792042 | 53026220 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,069 | 0.825630 | 53026220 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,393,903 | 0.005222 | 53026220 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,378,338 | 13,932.105970 | 53026220 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,175 | 2,363.327335 | 53026220 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,260,520 | 0.000265 | 53026220 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/msETH (stable) | 500 | 1,231,077 | 2.308317 | 53026220 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/SEND | 3000 | 1,225,112 | 64.742662 | 53026220 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,196,736 | 0.000000 | 53026220 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,178,574 | 35,296,733.949307 | 53026220 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,146,341 | 1,120,054.486088 | 53026220 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,134,729 | 48.644349 | 53026220 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,131,850 | 493,533.548554 | 53026220 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,095,815 | 16.864081 | 53026220 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/EDEL | 7000 | 1,077,154 | 73,812.125995 | 53026220 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,039,428 | 21,654,616.189288 | 53026220 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,039,056 | 17.027483 | 53026220 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,033,183 | 0.041471 | 53026220 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 955,258 | 23.314033 | 53026220 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 926,485 | 1,091.602128 | 53026220 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 895,888 | 0.000539 | 53026220 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 888,914 | 17.620139 | 53026220 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 852,589 | 2,363.482788 | 53026220 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 845,046 | 0.000009 | 53026220 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 820,424 | 0.060575 | 53026220 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | weETH_04c0/WETH | 500 | 813,505 | 1.105904 | 53026220 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 800,365 | 0.803010 | 53026220 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 10000 | 788,086 | 2,373.719186 | 53026220 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/VVV | 10000 | 773,063 | 97.276347 | 53026220 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 755,849 | 0.628566 | 53026220 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 749,090 | 4,698,503.819310 | 53026220 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 728,390 | 0.665325 | 53026220 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 806 ; routes examinées : 15604160 ; candidats optimisés : 64038 ; net attendu > 0 : 44 ; dernier cycle 108.9 ms
- Rejets (moteur) : {'spread_below_threshold': 15402706, 'liquidity_below_min': 136610, 'negative_expected_net': 63994, 'borrow_bound_too_small': 806}
- Enregistrements de la session : 64038 ; net attendu > 0 : 44 ; simulés (eth_call de la vraie tx) : 4 (ok 0, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 64038} ; motifs de rejet : {'below_safety_margin': 29, 'negative_expected_net': 63994, 'p_lower_below_threshold': 42, 'reliability_not_demonstrated': 2, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53025864 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 53.071423 USDC | 0.064455 USDC | 0.000000 USDC | 0.005307 USDC | 0.059148 USDC (0.0544 €) | — | 11.14 | 0.000 (n=50) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.009236 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0277 €) | — | 13.78 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 21.754914 USDC | 0.037187 USDC | 0.000000 USDC | 0.007103 USDC | 0.030084 USDC (0.0277 €) | — | 13.83 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 21.714709 USDC | 0.036699 USDC | 0.000000 USDC | 0.007103 USDC | 0.029596 USDC (0.0272 €) | — | 13.63 | 0.000 (n=39) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.009202 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0272 €) | — | 13.61 | 0.000 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 21.310484 USDC | 0.035421 USDC | 0.000000 USDC | 0.007103 USDC | 0.028318 USDC (0.0261 €) | — | 13.29 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.009032 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0260 €) | — | 13.26 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 17.154680 USDC | 0.026932 USDC | 0.000000 USDC | 0.007103 USDC | 0.019829 USDC (0.0182 €) | — | 11.56 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.007328 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0182 €) | — | 11.44 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 18.223051 USDC | 0.025935 USDC | 0.000000 USDC | 0.007103 USDC | 0.018832 USDC (0.0173 €) | — | 10.33 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.007729 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0173 €) | — | 10.30 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 18.153389 USDC | 0.025806 USDC | 0.000000 USDC | 0.007103 USDC | 0.018703 USDC (0.0172 €) | — | 10.30 | 0.000 (n=39) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.007729 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0172 €) | — | 10.23 | 0.000 (n=39) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 17.179750 USDC | 0.023691 USDC | 0.000000 USDC | 0.007103 USDC | 0.016588 USDC (0.0153 €) | — | 9.66 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53026140 | WETH→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.007279 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0152 €) | — | 9.63 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53025981 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.947240 USDC | 0.009156 USDC | 0.000000 USDC | 0.005306 USDC | 0.003850 USDC (0.0035 €) | — | 1.93 | 0.018 (n=79) | REJECTED | below_safety_margin(3850<3989), p_lower_below_threshold(0.02<0.75) |
| 53025981 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.947240 USDC | 0.009156 USDC | 0.000000 USDC | 0.005306 USDC | 0.003850 USDC (0.0035 €) | — | 1.93 | 0.018 (n=79) | REJECTED | below_safety_margin(3850<3989), p_lower_below_threshold(0.02<0.75) |
| 53025982 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.947240 USDC | 0.009156 USDC | 0.000000 USDC | 0.005306 USDC | 0.003850 USDC (0.0035 €) | — | 1.93 | 0.018 (n=79) | REJECTED | below_safety_margin(3850<3989), p_lower_below_threshold(0.02<0.75) |
| 53026018 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.012810 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0033 €) | — | 1.20 | 0.133 (n=263) | REJECTED | below_safety_margin(1532239492659<2561973448100), p_lower_below_threshold(0.13<0.75) |
| 53026018 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.012810 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0033 €) | — | 1.20 | 0.133 (n=263) | REJECTED | below_safety_margin(1532239492659<2561973448100), p_lower_below_threshold(0.13<0.75) |
| 53026018 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 29.919213 USDC | 0.011080 USDC | 0.000000 USDC | 0.007461 USDC | 0.003619 USDC (0.0033 €) | — | 1.21 | 0.133 (n=263) | REJECTED | below_safety_margin(3619<5983), p_lower_below_threshold(0.13<0.75) |
| 53026018 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 29.919213 USDC | 0.011080 USDC | 0.000000 USDC | 0.007461 USDC | 0.003619 USDC (0.0033 €) | — | 1.21 | 0.133 (n=263) | REJECTED | below_safety_margin(3619<5983), p_lower_below_threshold(0.13<0.75) |
| 53026018 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.012225 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 1.07 | 0.231 (n=129) | REJECTED | below_safety_margin(1308262029928<2445070654487), p_lower_below_threshold(0.23<0.75) |
| 53026018 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.012225 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 1.07 | 0.231 (n=129) | REJECTED | below_safety_margin(1308262029928<2445070654487), p_lower_below_threshold(0.23<0.75) |
| 53026018 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 29.024953 USDC | 0.010550 USDC | 0.000000 USDC | 0.007461 USDC | 0.003089 USDC (0.0028 €) | — | 1.06 | 0.231 (n=129) | REJECTED | below_safety_margin(3089<5804), p_lower_below_threshold(0.23<0.75) |

## Fiabilité et décision
- Observations ghost : 2135 ; taux observé 0.096 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
