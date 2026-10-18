# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T21:50:49+00:00 ; durée 99.01 min ; blocs 52782478 → 52785448 (2940 vus)

## Connexion
- Requêtes RPC : 40741 ; erreurs : 0 ; latence p50/p95 : 278.1/687.7 ms
- Rafraîchissements d'état : 2940 ; âge des données au dernier bloc : 2.69 s ; changements de frais LP observés (pools à frais dynamiques) : 7283
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 64114 ; cycles déclenchés par événement : 4114 ; avance médiane sur le rafraîchissement multicall : 830 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,356.49 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 569 pools, 326 jetons, 20804 routes
- Par DEX : uniswap_v3 135, aerodrome 232 (quarantaine 3), aerodrome_slipstream 153 (quarantaine 3), pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3913 (énumérés 387, par paires 0), mesurés 571, sous le plancher de 10000.0 $ : 2 → gardés 569 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2337.16445, 'AERO': 0.771529, 'cbBTC': 80785.7814}
- Pools en quarantaine : 6 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52785606; aerodrome_slipstream:MAMO/cbBTC@0xE2B3aA: simulation failed ×5 (model/chain mismatch) — until block 52785706; aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52785592; aerodrome:fBOMB/cbBTC@0x3d36Cf: simulation failed ×5 (model/chain mismatch) — until block 52785606; aerodrome_slipstream:MAMO/USDC@0x678F43: simulation failed ×5 (model/chain mismatch) — until block 52785636; aerodrome_slipstream:WETH/MAMO@0xAa067F: simulation failed ×5 (model/chain mismatch) — until block 52785706

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,016,768 | 2,356.491118 | 52785447 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,849,746 | 1.302182 | 52785447 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,827,008 | 0.029144 | 52785447 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,323,497 | 0.029088 | 52785447 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,175,348 | 109.638068 | 52785447 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,189,228 | 0.029073 | 52785447 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,738,187 | 0.000012 | 52785447 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 9,077,463 | 0.000012 | 52785447 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,262,392 | 2,361.710144 | 52785447 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,811,913 | 0.000012 | 52785447 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,662,947 | 2,362.215617 | 52785447 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,032,725 | 0.001638 | 52785447 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,413,502 | 2,356.415559 | 52785447 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,406,496 | 1.295932 | 52785447 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,167,018 | 0.029147 | 52785447 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,117,287 | 1.000854 | 52785447 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,819,373 | 0.026198 | 52785447 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,710,325 | 0.802398 | 52785447 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,497,054 | 0.000269 | 52785447 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,374,209 | 2,362.391632 | 52785447 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,305,017 | 0.998062 | 52785447 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,979,997 | 33,249.857497 | 52785447 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,973,979 | 2,365.877283 | 52785447 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,179,390 | 3,053.370789 | 52785447 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,839,832 | 1.141832 | 52785447 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,823,033 | 0.000012 | 52785447 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,539,073 | 414.918108 | 52785447 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2931 | 2,454,246 | 109.636018 | 52785447 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,249,764 | 0.000009 | 52785447 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,215,142 | 1,029.532325 | 52785447 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,162,020 | 1,205,977.942461 | 52785447 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,829 | 1.233121 | 52785447 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52785447 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,954,857 | 0.000000 | 52785447 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,903,023 | 15.991826 | 52785447 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,772,697 | 0.020634 | 52785447 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,760,572 | 0.000012 | 52785447 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,755,509 | 0.018415 | 52785447 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,703,999 | 1.105523 | 52785447 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,633,524 | 2.303038 | 52785447 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,620,349 | 14,254.000188 | 52785447 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,569,081 | 3,073.684834 | 52785447 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,477,653 | 1.119403 | 52785448 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,297 | 0.827470 | 52785447 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,429,709 | 0.916353 | 52785447 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,142 | 0.434918 | 52785447 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,301,546 | 0.000000 | 52785447 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,260,473 | 0.000269 | 52785447 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,247,633 | 0.029069 | 52785447 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,238,685 | 0.004503 | 52785447 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,233,273 | 63.888794 | 52785447 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,216,871 | 23.291377 | 52785447 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,213,818 | 1.130802 | 52785447 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,189,667 | 33,818,948.200743 | 52785447 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,171,219 | 2,361.674469 | 52785447 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,131,826 | 1,175,298.236206 | 52785447 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,102,487 | 534,059.559101 | 52785447 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,088,042 | 53.226146 | 52785447 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,080,486 | 15.399157 | 52785447 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,034,294 | 1.105812 | 52785447 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |

## Recherche d'opportunités
- Cycles : 7053 ; routes examinées : 146730612 ; candidats optimisés : 846581 ; net attendu > 0 : 554 ; dernier cycle 344.8 ms
- Rejets (moteur) : {'spread_below_threshold': 143920780, 'liquidity_below_min': 1320753, 'negative_expected_net': 846027, 'pool_quarantined': 632290, 'borrow_bound_too_small': 7048, 'unquotable': 2087, 'cycle_budget_exhausted': 1073}
- Enregistrements de la session : 846581 ; net attendu > 0 : 554 ; simulés (eth_call de la vraie tx) : 87 (ok 3, échec 84) ; étiquettes ghost N+1 : 0/65 positives
- Décisions : {'REJECTED': 846581} ; motifs de rejet : {'below_safety_margin': 294, 'negative_expected_net': 846027, 'p_lower_below_threshold': 401, 'price_impact': 52, 'reliability_not_demonstrated': 153, 'simulation_failed': 84}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52784851 | WETH→[aerodrome]→MEY→[uniswap_v3]→WETH | 0.120024 WETH | 0.007760 WETH | 0.000000 WETH | 0.000002 WETH | 0.007758 WETH (16.7917 €) | — | 646.36 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52783726 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.034582 WETH | 0.000210 WETH | 0.000000 WETH | 0.000002 WETH | 0.000208 WETH (0.4484 €) | — | 60.13 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52784612 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 686.250964 USDC | 0.220769 USDC | 0.000000 USDC | 0.005996 USDC | 0.214773 USDC (0.1976 €) | — | 3.13 | 0.000 (n=70) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52784612 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.291665 WETH | 0.000094 WETH | 0.000000 WETH | 0.000003 WETH | 0.000091 WETH (0.1971 €) | — | 3.12 | 0.000 (n=70) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52782961 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 516.106625 USDC | 0.154973 USDC | 0.000000 USDC | 0.007399 USDC | 0.147574 USDC (0.1358 €) | — | 2.86 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52782961 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006038 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1351 €) | — | 3.01 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.216555 WETH | 0.000066 WETH | 0.000000 WETH | 0.000003 WETH | 0.000063 WETH (0.1350 €) | — | 2.89 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52782961 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 530.350793 USDC | 0.145165 USDC | 0.000000 USDC | 0.007043 USDC | 0.138122 USDC (0.1271 €) | — | 2.60 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.006195 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1269 €) | — | 2.76 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.232551 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1265 €) | — | 2.52 | 0.123 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52782708 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 97.253897 USDC | 0.139738 USDC | 0.000000 USDC | 0.005252 USDC | 0.134486 USDC (0.1237 €) | — | 13.83 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52783765 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 96.463943 USDC | 0.137998 USDC | 0.000000 USDC | 0.005262 USDC | 0.132736 USDC (0.1221 €) | — | 13.76 | 0.000 (n=25) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52782961 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.006037 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1150 €) | — | 2.57 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 499.915405 USDC | 0.131749 USDC | 0.000000 USDC | 0.007043 USDC | 0.124706 USDC (0.1147 €) | — | 2.49 | 0.123 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.213187 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1142 €) | — | 2.49 | 0.123 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52784385 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000693 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1018 €) | — | 19.78 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 52784385 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.023711 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1016 €) | — | 19.82 | 0.001 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52784385 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.024604 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.1011 €) | — | 19.00 | 0.001 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52784385 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000686 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1010 €) | — | 19.84 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |
| 52784385 | cbBTC→[aerodrome]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000659 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1003 €) | — | 20.47 | 0.005 (n=55) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52784385 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome]→WETH | 0.022850 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.1000 €) | — | 20.25 | 0.005 (n=55) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52782961 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 335.455591 USDC | 0.115142 USDC | 0.000000 USDC | 0.007043 USDC | 0.108099 USDC (0.0995 €) | — | 3.22 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52782961 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.142816 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.0991 €) | — | 3.22 | 0.138 (n=98) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52784385 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000664 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0988 €) | — | 20.03 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52784385 | WETH→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.022833 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0982 €) | — | 19.90 | 0.001 (n=15) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1138 ; taux observé 0.106 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
