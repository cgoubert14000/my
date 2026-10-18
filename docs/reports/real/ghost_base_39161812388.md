# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T23:04:02+00:00 ; durée 172.23 min ; blocs 52782478 → 52787642 (5037 vus)

## Connexion
- Requêtes RPC : 69648 ; erreurs : 5 ; latence p50/p95 : 225.5/852.9 ms
- Rafraîchissements d'état : 5038 ; âge des données au dernier bloc : 2.03 s ; changements de frais LP observés (pools à frais dynamiques) : 13794
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 116220 ; cycles déclenchés par événement : 6805 ; avance médiane sur le rafraîchissement multicall : 402 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,389.19 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232, aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,504,812 | 2,389.185036 | 52787642 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,430,709 | 1.259952 | 52787642 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,078,458 | 0.029281 | 52787642 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,672,933 | 106.074830 | 52787642 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,939,660 | 0.029271 | 52787642 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,328,415 | 0.029263 | 52787642 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,786,698 | 0.000012 | 52787642 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,365,782 | 2,393.165362 | 52787642 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,842,909 | 0.000012 | 52787642 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 609 | 7,205,407 | 2,393.780135 | 52787642 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,142,921 | 0.001659 | 52787642 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 6,617,843 | 0.000012 | 52787642 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,450,926 | 2,389.814299 | 52787642 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,233,305 | 0.029292 | 52787642 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,188,285 | 1.000854 | 52787642 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,899,178 | 0.025959 | 52787642 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,817,134 | 1.265170 | 52787642 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,775,677 | 0.802398 | 52787642 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,567,776 | 0.000270 | 52787642 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,428,602 | 2,393.931991 | 52787642 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,344,471 | 0.998059 | 52787642 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 403 | 4,202,854 | 2,396.561754 | 52787642 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,040,048 | 33,170.368103 | 52787642 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,254,583 | 3,028.386306 | 52787642 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,879,234 | 1.141829 | 52787642 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,839,032 | 0.000012 | 52787642 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,771,525 | 409.209828 | 52787642 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,553,997 | 106.046884 | 52787642 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,474,440 | 0.000010 | 52787642 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,187,352 | 1,211,125.950841 | 52787642 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 2,098,938 | 1,023.458532 | 52787642 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,829 | 1.233121 | 52787642 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52787642 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,966,120 | 0.000000 | 52787642 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,807,730 | 15.871320 | 52787642 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,360 | 0.018699 | 52787642 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,314 | 0.000012 | 52787642 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | fBOMB/USDC | 10000 | 1,749,370 | 0.020635 | 52787642 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,735,079 | 13,980.215427 | 52787642 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,727,579 | 1.105523 | 52787642 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,661,979 | 2.305596 | 52787642 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,601,595 | 3,015.436892 | 52787642 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,479,322 | 1.121065 | 52787642 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,427 | 0.827453 | 52787642 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,449,545 | 0.916352 | 52787642 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,515 | 0.435377 | 52787642 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,316,689 | 0.000000 | 52787642 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,280,340 | 0.000272 | 52787642 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,261,989 | 0.029261 | 52787642 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,260,386 | 0.004546 | 52787642 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52787642 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,191,211 | 23.150571 | 52787642 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,190,561 | 34,984,808.159432 | 52787642 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,189,414 | 2,392.978978 | 52787642 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,172,810 | 1.131271 | 52787642 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/WELL | 10000 | 1,147,518 | 1,175,319.806971 | 52787642 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,114,503 | 528,194.777482 | 52787642 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,090,839 | 52.953503 | 52787642 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,087,593 | 15.141856 | 52787642 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,048,674 | 1.105812 | 52787642 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 11842 ; routes examinées : 246360968 ; candidats optimisés : 1441532 ; net attendu > 0 : 1550 ; dernier cycle 210.9 ms
- Rejets (moteur) : {'spread_below_threshold': 241693218, 'liquidity_below_min': 2465580, 'negative_expected_net': 1439982, 'pool_quarantined': 741734, 'borrow_bound_too_small': 11835, 'cycle_budget_exhausted': 4982, 'unquotable': 2087}
- Enregistrements de la session : 1441532 ; net attendu > 0 : 1550 ; simulés (eth_call de la vraie tx) : 128 (ok 24, échec 104) ; étiquettes ghost N+1 : 4/101 positives
- Décisions : {'REJECTED': 1441532} ; motifs de rejet : {'below_safety_margin': 1127, 'negative_expected_net': 1439982, 'p_lower_below_threshold': 1195, 'price_impact': 52, 'reliability_not_demonstrated': 355, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 104}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52784851 | WETH→[aerodrome]→MEY→[uniswap_v3]→WETH | 0.120024 WETH | 0.007760 WETH | 0.000000 WETH | 0.000002 WETH | 0.007758 WETH (16.7917 €) | — | 646.36 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52785954 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.735064 WETH | 0.000503 WETH | 0.000000 WETH | 0.000003 WETH | 0.000500 WETH (1.0975 €) | — | 2.88 | 0.112 (n=128) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52785954 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 4,197.876405 USDC | 1.200081 USDC | 0.000000 USDC | 0.008278 USDC | 1.191803 USDC (1.0965 €) | — | 2.84 | 0.112 (n=128) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52785954 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.050951 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.0963 €) | — | 2.87 | 0.112 (n=128) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52785724 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 4,552.177263 USDC | 1.124744 USDC | 0.000000 USDC | 0.008535 USDC | 1.116209 USDC (1.0269 €) | — | 2.45 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.055050 cbBTC | 0.000014 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000014 cbBTC (1.0242 €) | — | 2.50 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.900097 WETH | 0.000475 WETH | 0.000000 WETH | 0.000004 WETH | 0.000471 WETH (1.0238 €) | — | 2.48 | 0.116 (n=124) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52785954 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.795843 WETH | 0.000450 WETH | 0.000000 WETH | 0.000003 WETH | 0.000447 WETH (0.9812 €) | — | 2.49 | 0.112 (n=128) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52785954 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 4,197.402189 USDC | 1.074155 USDC | 0.000000 USDC | 0.008278 USDC | 1.065877 USDC (0.9806 €) | — | 2.54 | 0.112 (n=128) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52785954 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.051068 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.9800 €) | — | 2.56 | 0.112 (n=128) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52785724 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,172.069766 USDC | 1.012969 USDC | 0.000000 USDC | 0.008535 USDC | 1.004434 USDC (0.9241 €) | — | 3.17 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.038827 cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000012 cbBTC (0.9215 €) | — | 3.19 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.350669 WETH | 0.000427 WETH | 0.000000 WETH | 0.000004 WETH | 0.000424 WETH (0.9211 €) | — | 3.14 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52785724 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,844.265288 USDC | 0.985803 USDC | 0.000000 USDC | 0.008894 USDC | 0.976909 USDC (0.8988 €) | — | 2.54 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.047602 cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000012 cbBTC (0.8969 €) | — | 2.53 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.622718 WETH | 0.000416 WETH | 0.000000 WETH | 0.000004 WETH | 0.000412 WETH (0.8962 €) | — | 2.54 | 0.116 (n=124) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52785724 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,375.880815 USDC | 0.846803 USDC | 0.000000 USDC | 0.008176 USDC | 0.838627 USDC (0.7715 €) | — | 2.48 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.041160 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7695 €) | — | 2.51 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785724 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.394504 WETH | 0.000357 WETH | 0.000000 WETH | 0.000003 WETH | 0.000354 WETH (0.7686 €) | — | 2.54 | 0.116 (n=124) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52785954 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.232621 WETH | 0.000353 WETH | 0.000000 WETH | 0.000003 WETH | 0.000349 WETH (0.7671 €) | — | 2.83 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52785954 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,963.624234 USDC | 0.841445 USDC | 0.000000 USDC | 0.008278 USDC | 0.833167 USDC (0.7665 €) | — | 2.81 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52785954 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.035527 cbBTC | 0.000010 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000010 cbBTC (0.7656 €) | — | 2.87 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52785954 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.529771 WETH | 0.000320 WETH | 0.000000 WETH | 0.000003 WETH | 0.000316 WETH (0.6952 €) | — | 2.07 | 0.112 (n=128) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52785954 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.045087 cbBTC | 0.000009 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000009 cbBTC (0.6951 €) | — | 2.06 | 0.112 (n=128) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52785954 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,677.134319 USDC | 0.763237 USDC | 0.000000 USDC | 0.007915 USDC | 0.755322 USDC (0.6949 €) | — | 2.05 | 0.112 (n=128) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1174 ; taux observé 0.106 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
