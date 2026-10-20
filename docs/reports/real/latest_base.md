# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T03:09:07+00:00 ; durée 158.45 min ; blocs 52833443 → 52838196 (4645 vus)

## Connexion
- Requêtes RPC : 65244 ; erreurs : 125 ; latence p50/p95 : 216.8/625.6 ms
- Rafraîchissements d'état : 4645 ; âge des données au dernier bloc : 3.12 s ; changements de frais LP observés (pools à frais dynamiques) : 11401
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 98824 ; cycles déclenchés par événement : 5311 ; avance médiane sur le rafraîchissement multicall : 332 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,399.28 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,200,444 | 2,399.554459 | 52838196 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,498,623 | 1.238399 | 52838196 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,162,012 | 0.029377 | 52838196 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,576,244 | 96.309336 | 52838196 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,350,371 | 0.029306 | 52838196 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2525 | 9,965,129 | 0.029317 | 52838196 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,870,208 | 0.000012 | 52838196 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,344,546 | 2,405.790785 | 52838196 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,305,026 | 2,399.481790 | 52838196 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 7,822,079 | 0.000012 | 52838196 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 877 | 7,367,756 | 2,406.152616 | 52838196 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,189,872 | 0.001678 | 52838196 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 6,535,989 | 0.000012 | 52838196 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,341,085 | 0.029389 | 52838196 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,963,759 | 0.025584 | 52838196 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,780,072 | 0.802395 | 52838196 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,622,720 | 0.000274 | 52838196 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,459,088 | 2,406.289580 | 52838196 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,328,308 | 0.998768 | 52838196 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,026,234 | 33,681.176337 | 52838196 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,253,544 | 2,992.587358 | 52838196 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 463 | 3,050,450 | 2,408.786553 | 52838196 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,980,265 | 1.246697 | 52838196 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,855,086 | 0.000012 | 52838196 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,745,053 | 1.142106 | 52838196 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2757 | 2,673,242 | 96.328552 | 52838196 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,579,321 | 400.071559 | 52838196 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,238,060 | 970.167561 | 52838196 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,185,770 | 1,223,150.560610 | 52838196 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,142,630 | 0.000010 | 52838196 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,468 | 1.238011 | 52838196 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,304 | 1.373260 | 52838196 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,001,170 | 0.000000 | 52838196 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,900,951 | 15.902208 | 52838196 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,795,174 | 0.019167 | 52838196 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,793,708 | 13,636.837087 | 52838196 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,767,846 | 0.000012 | 52838196 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,735,955 | 1.105525 | 52838196 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,672,783 | 0.020210 | 52838196 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,646,082 | 2.307177 | 52838196 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,554,051 | 0.916343 | 52838196 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,510,113 | 2,970.934478 | 52838196 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,476,831 | 1.122870 | 52838196 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,403 | 0.826700 | 52838196 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,301,504 | 0.004702 | 52838196 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,299,851 | 0.000000 | 52838196 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,295,923 | 0.000276 | 52838196 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,282,487 | 0.029313 | 52838196 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,254,371 | 991,950.838217 | 52838196 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,239,629 | 2,405.789094 | 52838196 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,230,445 | 64.182807 | 52838196 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,203,990 | 22.952196 | 52838196 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,194,984 | 35,337,658.925039 | 52838196 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,450 | 0.435690 | 52838196 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,139,897 | 511,519.337817 | 52838196 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,136,980 | 1.131597 | 52838196 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,110,389 | 0.885516 | 52838196 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,099,197 | 52.149558 | 52838196 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,080,689 | 15.402831 | 52838196 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,079,280 | 85,257.473023 | 52838196 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 9955 ; routes examinées : 209831490 ; candidats optimisés : 1157930 ; net attendu > 0 : 457 ; dernier cycle 399.6 ms
- Rejets (moteur) : {'spread_below_threshold': 206734633, 'liquidity_below_min': 1687867, 'negative_expected_net': 1157473, 'borrow_bound_too_small': 248853, 'cycle_budget_exhausted': 2207}
- Enregistrements de la session : 1157930 ; net attendu > 0 : 457 ; simulés (eth_call de la vraie tx) : 36 (ok 13, échec 23) ; étiquettes ghost N+1 : 3/27 positives
- Décisions : {'REJECTED': 1157930} ; motifs de rejet : {'below_safety_margin': 273, 'negative_expected_net': 1157473, 'p_lower_below_threshold': 365, 'reliability_not_demonstrated': 92, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 23}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52837704 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,357.403929 USDC | 1.618250 USDC | 0.000000 USDC | 0.007212 USDC | 1.611038 USDC (1.4822 €) | — | 6.83 | 0.000 (n=88) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.983362 WETH | 0.000675 WETH | 0.000000 WETH | 0.000003 WETH | 0.000672 WETH (1.4812 €) | — | 6.83 | 0.000 (n=88) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52837704 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,960.783478 USDC | 1.243120 USDC | 0.000000 USDC | 0.009035 USDC | 1.234085 USDC (1.1354 €) | — | 6.29 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.826484 WETH | 0.000518 WETH | 0.000000 WETH | 0.000004 WETH | 0.000515 WETH (1.1345 €) | — | 6.23 | 0.115 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52837704 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.023970 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1341 €) | — | 6.30 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,805.192585 USDC | 0.866038 USDC | 0.000000 USDC | 0.006484 USDC | 0.859554 USDC (0.7908 €) | — | 4.76 | 0.090 (n=24) | REJECTED | reliability_not_demonstrated |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.753626 WETH | 0.000361 WETH | 0.000000 WETH | 0.000003 WETH | 0.000358 WETH (0.7900 €) | — | 4.75 | 0.090 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52837704 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,463.962719 USDC | 0.563106 USDC | 0.000000 USDC | 0.008307 USDC | 0.554799 USDC (0.5104 €) | — | 3.79 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.611402 WETH | 0.000235 WETH | 0.000000 WETH | 0.000003 WETH | 0.000231 WETH (0.5098 €) | — | 3.78 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 795.067478 USDC | 0.558489 USDC | 0.000000 USDC | 0.007237 USDC | 0.551252 USDC (0.5072 €) | — | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52836654 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.332070 WETH | 0.000233 WETH | 0.000000 WETH | 0.000003 WETH | 0.000230 WETH (0.5068 €) | 0.000230 WETH | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52837704 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,331.486427 USDC | 0.526924 USDC | 0.000000 USDC | 0.008307 USDC | 0.518617 USDC (0.4771 €) | — | 3.90 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.554679 WETH | 0.000220 WETH | 0.000000 WETH | 0.000003 WETH | 0.000216 WETH (0.4765 €) | — | 3.90 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.016238 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4762 €) | — | 3.90 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,313.107794 USDC | 0.476580 USDC | 0.000000 USDC | 0.006484 USDC | 0.470096 USDC (0.4325 €) | — | 3.58 | 0.090 (n=24) | REJECTED | reliability_not_demonstrated |
| 52837704 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.547953 WETH | 0.000199 WETH | 0.000000 WETH | 0.000003 WETH | 0.000196 WETH (0.4320 €) | — | 3.58 | 0.090 (n=24) | REJECTED | reliability_not_demonstrated |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 651.132267 USDC | 0.472163 USDC | 0.000000 USDC | 0.006874 USDC | 0.465289 USDC (0.4281 €) | — | 7.15 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52836654 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.271806 WETH | 0.000197 WETH | 0.000000 WETH | 0.000003 WETH | 0.000194 WETH (0.4279 €) | 0.000194 WETH | 7.15 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52837704 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,062.827893 USDC | 0.421848 USDC | 0.000000 USDC | 0.006484 USDC | 0.415364 USDC (0.3821 €) | — | 3.91 | 0.000 (n=88) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.443108 WETH | 0.000176 WETH | 0.000000 WETH | 0.000003 WETH | 0.000173 WETH (0.3816 €) | — | 3.91 | 0.000 (n=88) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52837704 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,136.896811 USDC | 0.362322 USDC | 0.000000 USDC | 0.008307 USDC | 0.354015 USDC (0.3257 €) | — | 3.11 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.474471 WETH | 0.000151 WETH | 0.000000 WETH | 0.000003 WETH | 0.000148 WETH (0.3253 €) | — | 3.11 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,146.943753 USDC | 0.353352 USDC | 0.000000 USDC | 0.008307 USDC | 0.345045 USDC (0.3174 €) | — | 3.01 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.478621 WETH | 0.000147 WETH | 0.000000 WETH | 0.000003 WETH | 0.000144 WETH (0.3170 €) | — | 3.00 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52837704 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 471.181429 USDC | 0.292558 USDC | 0.000000 USDC | 0.008307 USDC | 0.284251 USDC (0.2615 €) | — | 6.03 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1363 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
