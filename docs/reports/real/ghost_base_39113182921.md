# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T13:32:23+00:00 ; durée 274.17 min ; blocs 52762270 → 52770491 (8078 vus)

## Connexion
- Requêtes RPC : 110874 ; erreurs : 0 ; latence p50/p95 : 259.7/776.1 ms
- Rafraîchissements d'état : 8078 ; âge des données au dernier bloc : 3.06 s ; changements de frais LP observés (pools à frais dynamiques) : 13841
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 119731 ; cycles déclenchés par événement : 11201 ; avance médiane sur le rafraîchissement multicall : 412 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,395.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 328 jetons, 21580 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 157 (quarantaine 2), pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3915 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2410.986474, 'AERO': 0.834015, 'cbBTC': 81629.281689}
- Pools en quarantaine : 2 — aerodrome_slipstream:TIG/WETH@0xb4cfcD: simulation failed ×5 (model/chain mismatch) — until block 52770692; aerodrome_slipstream:TIG/USDC@0x3F5E98: simulation failed ×5 (model/chain mismatch) — until block 52770692

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,797,132 | 2,395.890641 | 52770492 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,803,705 | 1.214495 | 52770492 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,110,664 | 0.029391 | 52770492 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,630,948 | 107.474975 | 52770492 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 12,435,034 | 0.029450 | 52770492 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,354,873 | 0.029465 | 52770492 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,760,507 | 0.000012 | 52770492 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,008,217 | 2,391.517941 | 52770492 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 362 | 7,855,758 | 0.000012 | 52770492 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,109,540 | 0.001647 | 52770492 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 952 | 6,884,206 | 2,391.913228 | 52770492 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,662,413 | 0.000012 | 52770492 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 5,470,128 | 2,395.669984 | 52770492 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,290,883 | 0.029393 | 52770492 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,202,846 | 1.000855 | 52770492 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,099,067 | 0.025640 | 52770492 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,789,078 | 0.802398 | 52770492 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,600,542 | 0.000272 | 52770492 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,426,438 | 0.998809 | 52770492 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,407,230 | 2,392.125385 | 52770492 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,032,661 | 33,479.121721 | 52770492 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 490 | 3,342,954 | 2,395.169971 | 52770492 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,315,443 | 2,901.114018 | 52770492 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,949,451 | 1.205953 | 52770492 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,887,267 | 1.141820 | 52770492 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,836,826 | 0.000012 | 52770492 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,655,298 | 408.720479 | 52770492 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,540,488 | 107.444235 | 52770492 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,453,212 | 0.000010 | 52770492 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 2,405,777 | 1,015.298990 | 52770492 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,230,202 | 1,171,582.091169 | 52770492 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,106,813 | 1.199655 | 52770492 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,035,564 | 1.373959 | 52770492 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,959,529 | 1.123297 | 52770492 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,852,564 | 15.742474 | 52770492 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,851,439 | 0.000000 | 52770492 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,810,402 | 0.021555 | 52770492 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | XDP/USDC | 100 | 1,775,354 | 0.018798 | 52770492 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,767,161 | 0.000012 | 52770492 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,732,451 | 1.105521 | 52770492 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/msETH (stable) | 500 | 1,660,060 | 2.304972 | 52770492 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,651,591 | 13,890.418938 | 52770492 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,500,137 | 2,906.225288 | 52770492 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,457,164 | 0.916369 | 52770492 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,394 | 0.826238 | 52770492 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3040 | 1,436,791 | 2,905.651003 | 52770492 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,320,168 | 0.000000 | 52770492 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,319,038 | 0.435670 | 52770492 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,289,451 | 0.000271 | 52770492 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,274,865 | 0.004595 | 52770492 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/cbBTC | 3000 | 1,250,441 | 0.029467 | 52770492 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,233,250 | 63.891160 | 52770492 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,197,950 | 2,391.483317 | 52770492 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,192,248 | 1.131139 | 52770492 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/doginme | 10000 | 1,191,208 | 35,282,739.038168 | 52770492 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,177,090 | 23.332474 | 52770492 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,155,366 | 1,165,957.462515 | 52770492 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,125,212 | 518,621.626839 | 52770492 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 506 | 1,118,240 | 0.885351 | 52770492 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,095,099 | 14.890327 | 52770492 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 19278 ; routes examinées : 416019240 ; candidats optimisés : 2124336 ; net attendu > 0 : 951 ; dernier cycle 138.9 ms
- Rejets (moteur) : {'spread_below_threshold': 410705571, 'liquidity_below_min': 3107551, 'negative_expected_net': 2123385, 'pool_quarantined': 52506, 'borrow_bound_too_small': 19271, 'cycle_budget_exhausted': 10005}
- Enregistrements de la session : 2124336 ; net attendu > 0 : 951 ; simulés (eth_call de la vraie tx) : 94 (ok 25, échec 69) ; étiquettes ghost N+1 : 0/72 positives
- Décisions : {'REJECTED': 2124336} ; motifs de rejet : {'below_safety_margin': 733, 'negative_expected_net': 2123385, 'p_lower_below_threshold': 721, 'reliability_not_demonstrated': 230, 'simulation_failed': 69, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52763312 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.045860 WETH | 0.000451 WETH | 0.000000 WETH | 0.000002 WETH | 0.000449 WETH (0.9969 €) | — | 97.84 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52763336 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.044695 WETH | 0.000379 WETH | 0.000000 WETH | 0.000002 WETH | 0.000377 WETH (0.8390 €) | — | 84.36 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 331.897771 USDC | 0.790288 USDC | 0.000000 USDC | 0.007637 USDC | 0.782651 USDC (0.7200 €) | — | 23.58 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.137210 WETH | 0.000326 WETH | 0.000000 WETH | 0.000003 WETH | 0.000323 WETH (0.7192 €) | — | 23.55 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 334.557229 USDC | 0.776637 USDC | 0.000000 USDC | 0.007637 USDC | 0.769000 USDC (0.7075 €) | — | 22.99 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.138268 WETH | 0.000321 WETH | 0.000000 WETH | 0.000003 WETH | 0.000317 WETH (0.7067 €) | — | 22.96 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52770431 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.536170 WETH | 0.000301 WETH | 0.000000 WETH | 0.000003 WETH | 0.000297 WETH (0.6567 €) | — | 1.94 | 0.131 (n=103) | REJECTED | below_safety_margin(297431252520989<307233958732228), p_lower_below_threshold(0.13<0.75) |
| 52770431 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 3,679.785940 USDC | 0.720256 USDC | 0.000000 USDC | 0.008309 USDC | 0.711947 USDC (0.6550 €) | — | 1.93 | 0.131 (n=103) | REJECTED | below_safety_margin(711947<735957), p_lower_below_threshold(0.13<0.75) |
| 52769416 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.560034 WETH | 0.000286 WETH | 0.000000 WETH | 0.000002 WETH | 0.000284 WETH (0.6307 €) | — | 5.06 | 0.000 (n=67) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52769416 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,349.869585 USDC | 0.690241 USDC | 0.000000 USDC | 0.005796 USDC | 0.684445 USDC (0.6297 €) | — | 5.07 | 0.000 (n=67) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52762636 | WETH→[aerodrome_slipstream]→KTA→[aerodrome]→WETH | 0.107115 WETH | 0.000278 WETH | 0.000000 WETH | 0.000002 WETH | 0.000276 WETH (0.6125 €) | — | 25.74 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52769416 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.015054 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.6051 €) | — | 5.33 | 0.136 (n=81) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52769416 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.528671 WETH | 0.000275 WETH | 0.000000 WETH | 0.000003 WETH | 0.000272 WETH (0.6048 €) | — | 5.14 | 0.136 (n=81) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 52769416 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,272.043171 USDC | 0.663285 USDC | 0.000000 USDC | 0.007266 USDC | 0.656019 USDC (0.6035 €) | — | 5.16 | 0.136 (n=81) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52770431 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.411056 WETH | 0.000275 WETH | 0.000000 WETH | 0.000003 WETH | 0.000272 WETH (0.6003 €) | — | 1.93 | 0.131 (n=103) | REJECTED | below_safety_margin(271850490476985<282211220469743), p_lower_below_threshold(0.13<0.75) |
| 52770431 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 3,371.626297 USDC | 0.659006 USDC | 0.000000 USDC | 0.008309 USDC | 0.650697 USDC (0.5986 €) | — | 1.93 | 0.131 (n=103) | REJECTED | below_safety_margin(650697<674325), p_lower_below_threshold(0.13<0.75) |
| 52765230 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 294.578188 USDC | 0.599486 USDC | 0.000000 USDC | 0.007637 USDC | 0.591849 USDC (0.5445 €) | — | 20.09 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.121496 WETH | 0.000247 WETH | 0.000000 WETH | 0.000003 WETH | 0.000244 WETH (0.5436 €) | — | 20.10 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52765230 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 287.191677 USDC | 0.570485 USDC | 0.000000 USDC | 0.007637 USDC | 0.562848 USDC (0.5178 €) | — | 19.60 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.118596 WETH | 0.000235 WETH | 0.000000 WETH | 0.000003 WETH | 0.000232 WETH (0.5169 €) | — | 19.58 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 279.567138 USDC | 0.544737 USDC | 0.000000 USDC | 0.007637 USDC | 0.537100 USDC (0.4941 €) | — | 19.21 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52765230 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.115494 WETH | 0.000225 WETH | 0.000000 WETH | 0.000003 WETH | 0.000222 WETH (0.4932 €) | — | 19.19 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 52770431 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 1.012027 WETH | 0.000202 WETH | 0.000000 WETH | 0.000003 WETH | 0.000198 WETH (0.4383 €) | — | 1.96 | 0.131 (n=103) | REJECTED | below_safety_margin(198490182309506<202405437407813), p_lower_below_threshold(0.13<0.75) |
| 52770431 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 2,420.659123 USDC | 0.483370 USDC | 0.000000 USDC | 0.008309 USDC | 0.475061 USDC (0.4371 €) | — | 1.96 | 0.131 (n=103) | REJECTED | below_safety_margin(475061<484131), p_lower_below_threshold(0.13<0.75) |
| 52765230 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 211.066296 USDC | 0.415657 USDC | 0.000000 USDC | 0.008004 USDC | 0.407653 USDC (0.3750 €) | — | 19.31 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 935 ; taux observé 0.121 ; borne inférieure crédible (0.9) 0.108 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
