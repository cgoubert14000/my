# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T22:22:26+00:00 ; durée 130.62 min ; blocs 52782478 → 52786395 (3838 vus)

## Connexion
- Requêtes RPC : 53024 ; erreurs : 3 ; latence p50/p95 : 274.0/949.3 ms
- Rafraîchissements d'état : 3838 ; âge des données au dernier bloc : 3.12 s ; changements de frais LP observés (pools à frais dynamiques) : 10935
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 90929 ; cycles déclenchés par événement : 5210 ; avance médiane sur le rafraîchissement multicall : 642 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,387.69 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232, aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,417,567 | 2,387.687792 | 52786395 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,399,168 | 1.262087 | 52786395 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,048,897 | 0.029300 | 52786395 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,906,100 | 0.029271 | 52786395 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,601,803 | 106.851671 | 52786395 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,306,647 | 0.029263 | 52786395 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,782,890 | 0.000012 | 52786395 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 8,954,840 | 0.000012 | 52786395 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,341,824 | 2,390.646400 | 52786395 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 7,837,296 | 0.000012 | 52786395 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 684 | 7,166,401 | 2,389.943881 | 52786395 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,119,677 | 0.001652 | 52786395 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,449,218 | 2,388.447045 | 52786395 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,229,744 | 0.029297 | 52786395 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,185,033 | 1.000854 | 52786395 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,894,975 | 0.026200 | 52786395 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,772,683 | 0.802398 | 52786395 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,556,589 | 0.000269 | 52786395 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,418,971 | 2,389.690045 | 52786395 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,338,903 | 0.998059 | 52786395 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,037,176 | 33,175.949485 | 52786395 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 439 | 3,654,909 | 2,394.328239 | 52786395 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,250,823 | 3,038.580022 | 52786395 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,877,429 | 1.141829 | 52786395 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,836,805 | 0.000012 | 52786395 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2883 | 2,541,831 | 106.827003 | 52786395 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,528,385 | 1.270413 | 52786395 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,378,126 | 0.000010 | 52786395 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,254,789 | 412.405266 | 52786395 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,186,787 | 1,210,233.823363 | 52786395 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2742 | 2,077,679 | 1,024.608347 | 52786395 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,829 | 1.233121 | 52786395 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52786395 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,964,893 | 0.000000 | 52786395 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,772,709 | 0.020634 | 52786395 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,967 | 0.000012 | 52786395 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,763,353 | 0.018571 | 52786395 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,726,496 | 1.105523 | 52786395 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,675,995 | 15.949732 | 52786395 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,660,933 | 2.305605 | 52786395 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,599,902 | 3,016.814363 | 52786395 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,480,455 | 1.122323 | 52786395 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,411 | 0.827470 | 52786395 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,448,637 | 0.916352 | 52786395 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,387,259 | 14,089.786825 | 52786395 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,318,813 | 0.000000 | 52786395 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,318,033 | 0.435357 | 52786395 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,277,191 | 0.000270 | 52786395 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,260,786 | 0.029261 | 52786395 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,249,802 | 0.004504 | 52786395 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,237,695 | 23.253195 | 52786395 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52786395 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,194,631 | 34,723,672.848865 | 52786395 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,179,750 | 2,390.725691 | 52786395 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,176,706 | 1.131233 | 52786395 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/WELL | 10000 | 1,146,799 | 1,175,319.393100 | 52786395 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,739 | 529,614.722225 | 52786395 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,089,432 | 15.075176 | 52786395 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,088,217 | 53.209022 | 52786395 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,048,017 | 1.105812 | 52786395 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 9047 ; routes examinées : 188213788 ; candidats optimisés : 1163494 ; net attendu > 0 : 1378 ; dernier cycle 138.1 ms
- Rejets (moteur) : {'spread_below_threshold': 184478574, 'liquidity_below_min': 1813996, 'negative_expected_net': 1162116, 'pool_quarantined': 741734, 'borrow_bound_too_small': 9041, 'cycle_budget_exhausted': 4862, 'unquotable': 2087}
- Enregistrements de la session : 1163494 ; net attendu > 0 : 1378 ; simulés (eth_call de la vraie tx) : 121 (ok 24, échec 97) ; étiquettes ghost N+1 : 4/94 positives
- Décisions : {'REJECTED': 1163494} ; motifs de rejet : {'below_safety_margin': 963, 'negative_expected_net': 1162116, 'p_lower_below_threshold': 1045, 'price_impact': 52, 'reliability_not_demonstrated': 333, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 97}

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
- Observations ghost : 1167 ; taux observé 0.107 ; borne inférieure crédible (0.9) 0.096 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
