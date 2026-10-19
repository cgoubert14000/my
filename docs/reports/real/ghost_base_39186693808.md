# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T01:55:45+00:00 ; durée 6.08 min ; blocs 52792613 → 52792796 (158 vus)

## Connexion
- Requêtes RPC : 2306 ; erreurs : 0 ; latence p50/p95 : 418.6/1,640.3 ms
- Rafraîchissements d'état : 158 ; âge des données au dernier bloc : 8.44 s ; changements de frais LP observés (pools à frais dynamiques) : 232
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2937 ; cycles déclenchés par événement : 160 ; avance médiane sur le rafraîchissement multicall : 1,409 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,418.69 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 574 pools, 328 jetons, 21112 routes
- Par DEX : uniswap_v3 137, aerodrome 234 (quarantaine 2), aerodrome_slipstream 156, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 576, sous le plancher de 10000.0 $ : 2 → gardés 574 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2418.692382, 'AERO': 0.800914, 'cbBTC': 82392.905144}
- Pools en quarantaine : 2 — aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52793025; aerodrome:fBOMB/USDbC@0xC39566: simulation failed ×5 (model/chain mismatch) — until block 52793025

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,675,120 | 2,418.692397 | 52792796 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,472,235 | 1.248576 | 52792796 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,582,392 | 0.029349 | 52792796 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,276,753 | 0.029399 | 52792796 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,201,185 | 102.136974 | 52792796 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,447,995 | 0.029335 | 52792796 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,819,382 | 0.000012 | 52792796 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,434,486 | 2,423.901559 | 52792796 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,840,800 | 0.000012 | 52792796 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,622,331 | 2,423.083516 | 52792796 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,203,605 | 0.001660 | 52792796 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,769,820 | 0.000012 | 52792796 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,484,364 | 2,419.046087 | 52792796 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,293,088 | 0.029406 | 52792796 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,252,362 | 1.000854 | 52792796 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 4,931,347 | 0.025826 | 52792796 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,834,659 | 0.802398 | 52792796 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,667,007 | 1.256059 | 52792796 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,632,226 | 0.000271 | 52792796 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,439,965 | 2,422.931571 | 52792796 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,382,557 | 0.998060 | 52792796 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,088,499 | 33,193.825249 | 52792796 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 409 | 3,866,133 | 2,427.199824 | 52792796 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,289,491 | 3,024.011342 | 52792796 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,914,756 | 1.141828 | 52792796 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,852,918 | 0.000012 | 52792796 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,760,043 | 409.706542 | 52792796 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,643,944 | 102.118248 | 52792796 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,408,221 | 0.000010 | 52792796 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,218,488 | 1,206,630.652992 | 52792796 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,065,830 | 1.233105 | 52792796 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,703 | 1.372655 | 52792796 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,010,055 | 0.000000 | 52792796 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,942,243 | 15.860538 | 52792796 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,779,859 | 13,957.739500 | 52792796 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,833 | 0.000012 | 52792796 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,769,797 | 0.018685 | 52792796 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | weETH_04c0/WETH | 500 | 1,748,915 | 1.105523 | 52792796 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,736,212 | 0.020718 | 52792796 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,681,028 | 2.308616 | 52792796 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,619,750 | 3,024.509491 | 52792796 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,478,688 | 1.122647 | 52792796 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,467,448 | 0.916352 | 52792796 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,549 | 0.827316 | 52792796 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,338,582 | 0.000000 | 52792796 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,320,191 | 0.436183 | 52792796 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,298,402 | 0.000273 | 52792796 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,291,037 | 0.004582 | 52792796 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,274,995 | 0.029335 | 52792796 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,273,880 | 23.193139 | 52792796 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,233,298 | 63.886174 | 52792796 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,206,037 | 35,030,719.660295 | 52792796 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,200,760 | 2,423.885895 | 52792796 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,175,209 | 0.885945 | 52792796 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 1,173,423 | 1,025.314500 | 52792796 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/WELL | 10000 | 1,163,150 | 1,172,371.683918 | 52792796 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,134,343 | 520,348.319616 | 52792796 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,106,407 | 1.131918 | 52792796 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,090,429 | 15.040999 | 52792796 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,081,112 | 53.910645 | 52792796 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 317 ; routes examinées : 6692504 ; candidats optimisés : 53796 ; net attendu > 0 : 66 ; dernier cycle 797.1 ms
- Rejets (moteur) : {'spread_below_threshold': 6567089, 'liquidity_below_min': 57850, 'negative_expected_net': 53730, 'pool_quarantined': 13452, 'borrow_bound_too_small': 317}
- Enregistrements de la session : 53796 ; net attendu > 0 : 66 ; simulés (eth_call de la vraie tx) : 5 (ok 0, échec 5) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 53796} ; motifs de rejet : {'below_safety_margin': 61, 'negative_expected_net': 53730, 'p_lower_below_threshold': 66, 'price_impact': 62, 'simulation_failed': 5, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52792758 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.845068 USDC | 0.008190 USDC | 0.000000 USDC | 0.007268 USDC | 0.000922 USDC (0.0008 €) | — | 0.26 | 0.100 (n=143) | REJECTED | below_safety_margin(922<7169), p_lower_below_threshold(0.10<0.75) |
| 52792759 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.845068 USDC | 0.008190 USDC | 0.000000 USDC | 0.007268 USDC | 0.000922 USDC (0.0008 €) | — | 0.26 | 0.100 (n=143) | REJECTED | below_safety_margin(922<7169), p_lower_below_threshold(0.10<0.75) |
| 52792758 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.014870 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.25 | 0.100 (n=143) | REJECTED | below_safety_margin(373354487110<2974034541550), p_lower_below_threshold(0.10<0.75) |
| 52792759 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.014870 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.25 | 0.100 (n=143) | REJECTED | below_safety_margin(373354487110<2974034541550), p_lower_below_threshold(0.10<0.75) |
| 52792725 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 3.82 | 0.031 (n=92) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52792723 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 3.82 | 0.031 (n=92) | REJECTED | stale_data(4337ms>4000.0), price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52792726 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 3.82 | 0.031 (n=92) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52792722 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 3.82 | 0.031 (n=91) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52792723 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0004 €) | — | 3.82 | 0.031 (n=91) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.03<0.75) |
| 52792685 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17355440061<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792687 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17355440061<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792687 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17355440061<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792688 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17355440061<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792689 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17355440061<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792690 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17355440061<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792689 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792690 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792690 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792691 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792691 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792692 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792692 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792693 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792695 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17341842638<82689308262), stale_data(4547ms>4000.0), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |
| 52792711 | WETH→[uniswap_v3]→USDbC→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000413 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0000 €) | — | 0.42 | 0.103 (n=58) | REJECTED | below_safety_margin(17323698633<82689307825), price_impact(205bps>150.0), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 1221 ; taux observé 0.105 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
