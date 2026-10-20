# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T02:47:03+00:00 ; durée 136.4 min ; blocs 52833443 → 52837535 (3994 vus)

## Connexion
- Requêtes RPC : 56228 ; erreurs : 125 ; latence p50/p95 : 218.3/597.1 ms
- Rafraîchissements d'état : 3995 ; âge des données au dernier bloc : 1.13 s ; changements de frais LP observés (pools à frais dynamiques) : 9972
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 85830 ; cycles déclenchés par événement : 4404 ; avance médiane sur le rafraîchissement multicall : 355 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,392.17 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,909,413 | 2,392.169585 | 52837535 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,443,122 | 1.242387 | 52837535 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,113,280 | 0.029336 | 52837535 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,565,079 | 0.029296 | 52837535 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,451,396 | 97.119813 | 52837535 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,324,628 | 0.029306 | 52837535 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,863,702 | 0.000012 | 52837535 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,326,775 | 2,395.668456 | 52837535 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,292,712 | 2,393.079240 | 52837535 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 7,816,906 | 0.000012 | 52837535 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,177,791 | 0.001678 | 52837535 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 773 | 7,170,515 | 2,396.483376 | 52837535 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 6,674,597 | 0.000012 | 52837535 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,327,220 | 0.029348 | 52837535 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,955,697 | 0.025593 | 52837535 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,765,908 | 0.802395 | 52837535 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,609,021 | 0.000274 | 52837535 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,418,984 | 2,396.600653 | 52837535 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,365,788 | 1.251385 | 52837535 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,321,283 | 0.998768 | 52837535 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,014,666 | 33,675.087713 | 52837535 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,243,510 | 2,997.662417 | 52837535 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 442 | 3,046,834 | 2,399.032410 | 52837535 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,852,245 | 0.000012 | 52837535 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,736,917 | 1.142106 | 52837535 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,710,357 | 400.279208 | 52837535 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,656,249 | 97.092207 | 52837535 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,496,004 | 972.770210 | 52837535 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,179,293 | 1,223,150.560610 | 52837535 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,111,921 | 0.000010 | 52837535 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,468 | 1.238011 | 52837535 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,304 | 1.373260 | 52837535 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,996,205 | 0.000000 | 52837535 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,839,046 | 13,651.838572 | 52837535 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,806,235 | 0.019393 | 52837535 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,766,155 | 0.000012 | 52837535 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,730,810 | 1.105525 | 52837535 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,672,690 | 0.020210 | 52837535 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,665,442 | 15.957416 | 52837535 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,641,205 | 2.306551 | 52837535 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,549,446 | 0.916343 | 52837535 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,534,035 | 1.122415 | 52837535 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | WETH/AERO | 3000 | 1,505,498 | 2,975.622959 | 52837535 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,673 | 0.826781 | 52837535 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,297,648 | 0.004702 | 52837535 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,296,185 | 0.000000 | 52837535 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,292,083 | 0.000277 | 52837535 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,279,544 | 0.029313 | 52837535 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,247,180 | 997,485.133365 | 52837535 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,244,869 | 2,395.637359 | 52837535 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,230,445 | 64.182807 | 52837535 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,192,078 | 35,281,573.925432 | 52837535 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,189,019 | 22.968163 | 52837535 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,167,130 | 0.435512 | 52837535 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,145,646 | 1.131486 | 52837535 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,136,519 | 511,519.337817 | 52837535 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,098,913 | 52.176527 | 52837535 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,098,053 | 0.885407 | 52837535 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,078,734 | 15.475543 | 52837535 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,074,592 | 1.001422 | 52837535 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 8398 ; routes examinées : 177013044 ; candidats optimisés : 956970 ; net attendu > 0 : 322 ; dernier cycle 335.5 ms
- Rejets (moteur) : {'spread_below_threshold': 174426698, 'liquidity_below_min': 1417345, 'negative_expected_net': 956648, 'borrow_bound_too_small': 209928, 'cycle_budget_exhausted': 1921}
- Enregistrements de la session : 956967 ; net attendu > 0 : 322 ; simulés (eth_call de la vraie tx) : 29 (ok 10, échec 19) ; étiquettes ghost N+1 : 3/20 positives
- Décisions : {'REJECTED': 956967} ; motifs de rejet : {'below_safety_margin': 189, 'negative_expected_net': 956645, 'p_lower_below_threshold': 245, 'reliability_not_demonstrated': 77, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 19}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 795.067478 USDC | 0.558489 USDC | 0.000000 USDC | 0.007237 USDC | 0.551252 USDC (0.5072 €) | — | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52836654 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.332070 WETH | 0.000233 WETH | 0.000000 WETH | 0.000003 WETH | 0.000230 WETH (0.5068 €) | 0.000230 WETH | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 651.132267 USDC | 0.472163 USDC | 0.000000 USDC | 0.006874 USDC | 0.465289 USDC (0.4281 €) | — | 7.15 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52836654 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.271806 WETH | 0.000197 WETH | 0.000000 WETH | 0.000003 WETH | 0.000194 WETH (0.4279 €) | 0.000194 WETH | 7.15 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 516.931248 USDC | 0.232691 USDC | 0.000000 USDC | 0.006874 USDC | 0.225817 USDC (0.2078 €) | — | 4.37 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52836654 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.216075 WETH | 0.000097 WETH | 0.000000 WETH | 0.000003 WETH | 0.000094 WETH (0.2077 €) | 0.000094 WETH | 4.37 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52836654 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 527.675926 USDC | 0.213250 USDC | 0.000000 USDC | 0.005054 USDC | 0.208196 USDC (0.1915 €) | — | 3.95 | 0.051 (n=16) | REJECTED | reliability_not_demonstrated |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 469.184211 USDC | 0.188638 USDC | 0.000000 USDC | 0.006874 USDC | 0.181764 USDC (0.1672 €) | — | 3.87 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52836654 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.196108 WETH | 0.000079 WETH | 0.000000 WETH | 0.000003 WETH | 0.000076 WETH (0.1672 €) | — | 3.87 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 52836705 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 105.097958 USDC | 0.170214 USDC | 0.000000 USDC | 0.005383 USDC | 0.164831 USDC (0.1516 €) | — | 15.68 | 0.000 (n=36) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 417.217201 USDC | 0.170069 USDC | 0.000000 USDC | 0.006874 USDC | 0.163195 USDC (0.1501 €) | — | 3.91 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52836654 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.174938 WETH | 0.000071 WETH | 0.000000 WETH | 0.000003 WETH | 0.000068 WETH (0.1501 €) | — | 3.90 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52834629 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.588416 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1500 €) | — | 1.17 | 0.110 (n=162) | REJECTED | below_safety_margin(68558854851700<117683174409720), p_lower_below_threshold(0.11<0.75) |
| 52834629 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,465.213965 USDC | 0.171276 USDC | 0.000000 USDC | 0.008289 USDC | 0.162987 USDC (0.1499 €) | — | 1.11 | 0.110 (n=162) | REJECTED | below_safety_margin(162987<293042), p_lower_below_threshold(0.11<0.75) |
| 52834629 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.016945 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1496 €) | — | 1.18 | 0.110 (n=162) | REJECTED | below_safety_margin(200<338), p_lower_below_threshold(0.11<0.75) |
| 52834629 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.478386 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000048 WETH (0.1045 €) | — | 1.00 | 0.002 (n=5) | REJECTED | below_safety_margin(47774342821363<95677238449549), reliability_not_demonstrated |
| 52834629 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,128.690898 USDC | 0.121836 USDC | 0.000000 USDC | 0.008289 USDC | 0.113547 USDC (0.1045 €) | — | 1.01 | 0.002 (n=5) | REJECTED | below_safety_margin(113547<225738), reliability_not_demonstrated |
| 52834629 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.013417 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1040 €) | — | 1.04 | 0.002 (n=5) | REJECTED | below_safety_margin(139<268), reliability_not_demonstrated |
| 52836654 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001766 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0818 €) | — | 6.17 | 0.117 (n=115) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52836654 | cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001766 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0818 €) | — | 6.17 | 0.117 (n=115) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52836654 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.061359 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0813 €) | — | 6.02 | 0.117 (n=115) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52836654 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.061359 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0813 €) | — | 6.02 | 0.117 (n=115) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52834629 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.256863 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0756 €) | — | 1.34 | 0.002 (n=5) | REJECTED | below_safety_margin(34538246204055<51372517521810), reliability_not_demonstrated |
| 52834629 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.007471 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0756 €) | — | 1.35 | 0.002 (n=5) | REJECTED | below_safety_margin(101<149), reliability_not_demonstrated |
| 52834629 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 591.082484 USDC | 0.090237 USDC | 0.000000 USDC | 0.008289 USDC | 0.081948 USDC (0.0754 €) | — | 1.39 | 0.002 (n=5) | REJECTED | below_safety_margin(81948<118216), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1356 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
