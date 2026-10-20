# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T04:13:18+00:00 ; durée 222.64 min ; blocs 52833443 → 52840119 (6509 vus)

## Connexion
- Requêtes RPC : 91408 ; erreurs : 125 ; latence p50/p95 : 187.8/601.7 ms
- Rafraîchissements d'état : 6509 ; âge des données au dernier bloc : 2.47 s ; changements de frais LP observés (pools à frais dynamiques) : 14797
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 128870 ; cycles déclenchés par événement : 7871 ; avance médiane sur le rafraîchissement multicall : 302 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,406.34 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,542,569 | 2,406.344805 | 52840120 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,513,676 | 1.236232 | 52840120 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,505,812 | 0.029339 | 52840120 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,214,604 | 0.029392 | 52840120 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,532,359 | 97.363268 | 52840120 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,388,555 | 0.029323 | 52840120 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,880,150 | 0.000012 | 52840120 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/USDC | 579 | 8,401,352 | 2,409.283322 | 52840120 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | WETH/USDC | 500 | 8,365,592 | 2,409.735975 | 52840120 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,315,637 | 2,406.368848 | 52840120 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 8,290,500 | 0.000012 | 52840120 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,829,463 | 0.000012 | 52840120 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,199,651 | 0.001674 | 52840120 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,356,900 | 0.029381 | 52840120 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,981,956 | 0.025581 | 52840120 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,794,149 | 0.802395 | 52840120 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,636,845 | 0.000274 | 52840120 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 409 | 4,608,219 | 2,412.896285 | 52840120 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,479,445 | 2,409.440438 | 52840120 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,378,288 | 1.238258 | 52840120 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,338,588 | 0.998768 | 52840120 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,033,687 | 33,754.766553 | 52840120 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,261,189 | 2,982.721601 | 52840120 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,876,879 | 0.000012 | 52840120 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,753,139 | 1.142105 | 52840120 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,669,718 | 97.390713 | 52840120 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,368,419 | 399.419668 | 52840120 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,211,918 | 0.000010 | 52840120 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,192,207 | 1,223,150.560610 | 52840120 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/MORPHO | 2739 | 2,083,522 | 962.772304 | 52840120 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,504 | 1.238011 | 52840120 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,017 | 1.373596 | 52840120 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,977,229 | 0.000000 | 52840120 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,950,537 | 15.879301 | 52840120 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,801,003 | 0.019221 | 52840120 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,222 | 0.000012 | 52840120 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,741,067 | 1.105525 | 52840120 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,728,767 | 1.122911 | 52840120 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,710,769 | 13,588.733120 | 52840120 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,677,340 | 0.020323 | 52840120 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,650,419 | 2.307614 | 52840120 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,558,627 | 0.916343 | 52840120 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,513,959 | 2,979.220036 | 52840120 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,488 | 0.826605 | 52840120 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,308,533 | 0.000000 | 52840120 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,348 | 0.004702 | 52840120 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,299,944 | 0.000277 | 52840120 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,285,898 | 0.029321 | 52840120 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,285,070 | 950,763.527233 | 52840120 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,250,369 | 2,409.787537 | 52840120 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,230,445 | 64.182807 | 52840120 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,206,569 | 22.980496 | 52840120 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,198,503 | 35,337,658.925039 | 52840120 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,168,053 | 0.435841 | 52840120 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,143,254 | 511,519.337817 | 52840120 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,131,410 | 0.885676 | 52840120 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,118,158 | 1.131762 | 52840120 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/NOCK | 3000 | 1,101,200 | 51.960084 | 52840120 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,089,440 | 84,168.275882 | 52840120 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,078,406 | 15.488644 | 52840120 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 14379 ; routes examinées : 303080562 ; candidats optimisés : 1857787 ; net attendu > 0 : 518 ; dernier cycle 91.6 ms
- Rejets (moteur) : {'spread_below_threshold': 298294214, 'liquidity_below_min': 2474283, 'negative_expected_net': 1857269, 'borrow_bound_too_small': 359447, 'pool_quarantined': 91780, 'cycle_budget_exhausted': 3051}
- Enregistrements de la session : 1857787 ; net attendu > 0 : 518 ; simulés (eth_call de la vraie tx) : 49 (ok 17, échec 32) ; étiquettes ghost N+1 : 3/34 positives
- Décisions : {'REJECTED': 1857787} ; motifs de rejet : {'below_safety_margin': 301, 'negative_expected_net': 1857269, 'p_lower_below_threshold': 403, 'price_impact': 8, 'reliability_not_demonstrated': 115, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 32}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52837704 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,357.403929 USDC | 1.618250 USDC | 0.000000 USDC | 0.007212 USDC | 1.611038 USDC (1.4822 €) | — | 6.83 | 0.000 (n=88) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.983362 WETH | 0.000675 WETH | 0.000000 WETH | 0.000003 WETH | 0.000672 WETH (1.4812 €) | — | 6.83 | 0.000 (n=88) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52837704 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,960.783478 USDC | 1.243120 USDC | 0.000000 USDC | 0.009035 USDC | 1.234085 USDC (1.1354 €) | — | 6.29 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.826484 WETH | 0.000518 WETH | 0.000000 WETH | 0.000004 WETH | 0.000515 WETH (1.1345 €) | — | 6.23 | 0.115 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52837704 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.023970 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1341 €) | — | 6.30 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 281.209092 USDC | 0.969297 USDC | 0.000000 USDC | 0.009435 USDC | 0.959862 USDC (0.8831 €) | — | 34.13 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.116721 WETH | 0.000402 WETH | 0.000000 WETH | 0.000004 WETH | 0.000398 WETH (0.8810 €) | — | 34.12 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 276.030520 USDC | 0.950791 USDC | 0.000000 USDC | 0.009435 USDC | 0.941356 USDC (0.8660 €) | — | 34.10 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.114583 WETH | 0.000395 WETH | 0.000000 WETH | 0.000004 WETH | 0.000391 WETH (0.8641 €) | — | 34.09 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 266.947343 USDC | 0.870907 USDC | 0.000000 USDC | 0.009435 USDC | 0.861472 USDC (0.7926 €) | — | 32.27 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.110831 WETH | 0.000361 WETH | 0.000000 WETH | 0.000004 WETH | 0.000358 WETH (0.7910 €) | — | 32.26 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52837704 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,805.192585 USDC | 0.866038 USDC | 0.000000 USDC | 0.006484 USDC | 0.859554 USDC (0.7908 €) | — | 4.76 | 0.090 (n=24) | REJECTED | reliability_not_demonstrated |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.753626 WETH | 0.000361 WETH | 0.000000 WETH | 0.000003 WETH | 0.000358 WETH (0.7900 €) | — | 4.75 | 0.090 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 265.497558 USDC | 0.865712 USDC | 0.000000 USDC | 0.009435 USDC | 0.856277 USDC (0.7878 €) | — | 32.25 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.110229 WETH | 0.000359 WETH | 0.000000 WETH | 0.000004 WETH | 0.000355 WETH (0.7862 €) | — | 32.24 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 259.687658 USDC | 0.823189 USDC | 0.000000 USDC | 0.009435 USDC | 0.813754 USDC (0.7487 €) | — | 31.34 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.107888 WETH | 0.000342 WETH | 0.000000 WETH | 0.000004 WETH | 0.000338 WETH (0.7473 €) | — | 31.31 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 220.265262 USDC | 0.707567 USDC | 0.000000 USDC | 0.009435 USDC | 0.698132 USDC (0.6423 €) | — | 31.70 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.091535 WETH | 0.000294 WETH | 0.000000 WETH | 0.000004 WETH | 0.000290 WETH (0.6417 €) | — | 31.69 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52837704 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,463.962719 USDC | 0.563106 USDC | 0.000000 USDC | 0.008307 USDC | 0.554799 USDC (0.5104 €) | — | 3.79 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.611402 WETH | 0.000235 WETH | 0.000000 WETH | 0.000003 WETH | 0.000231 WETH (0.5098 €) | — | 3.78 | 0.145 (n=70) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52836654 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 795.067478 USDC | 0.558489 USDC | 0.000000 USDC | 0.007237 USDC | 0.551252 USDC (0.5072 €) | — | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52836654 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.332070 WETH | 0.000233 WETH | 0.000000 WETH | 0.000003 WETH | 0.000230 WETH (0.5068 €) | 0.000230 WETH | 6.93 | 0.009 (n=33) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52837704 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,331.486427 USDC | 0.526924 USDC | 0.000000 USDC | 0.008307 USDC | 0.518617 USDC (0.4771 €) | — | 3.90 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.554679 WETH | 0.000220 WETH | 0.000000 WETH | 0.000003 WETH | 0.000216 WETH (0.4765 €) | — | 3.90 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1370 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
