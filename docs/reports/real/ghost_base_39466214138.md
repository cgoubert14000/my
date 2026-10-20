# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T19:24:51+00:00 ; durée 110.9 min ; blocs 52864139 → 52867467 (3039 vus)

## Connexion
- Requêtes RPC : 42319 ; erreurs : 180 ; latence p50/p95 : 524.3/1,654.8 ms
- Rafraîchissements d'état : 3039 ; âge des données au dernier bloc : 5.72 s ; changements de frais LP observés (pools à frais dynamiques) : 6592
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 53978 ; cycles déclenchés par événement : 2518 ; avance médiane sur le rafraîchissement multicall : 1,188 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,430.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 327 jetons, 22534 routes
- Par DEX : uniswap_v3 136, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 395, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2447.454075, 'AERO': 0.860145, 'cbBTC': 82683.957961}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,919,995 | 2,430.569910 | 52867467 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 39,921,571 | 1.172481 | 52867467 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,719,542 | 97.072456 | 52867467 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,304,979 | 0.029455 | 52867469 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2570 | 10,700,763 | 0.029514 | 52867467 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,492,191 | 0.029527 | 52867467 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,922,125 | 0.000012 | 52867467 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,556,448 | 2,424.344174 | 52867467 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,354,176 | 2,430.625253 | 52867467 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 8,182,226 | 0.000012 | 52867467 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 907 | 7,713,438 | 2,423.614298 | 52867468 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,249,916 | 0.001670 | 52867467 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 6,536,620 | 0.000012 | 52867468 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,408,781 | 0.029441 | 52867468 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,212,437 | 0.024538 | 52867467 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,693,010 | 0.000275 | 52867467 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,686,232 | 0.802394 | 52867467 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,408,079 | 2,423.538904 | 52867469 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,377,579 | 0.998747 | 52867467 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,013,770 | 34,780.440254 | 52867467 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 469 | 3,651,559 | 2,427.867699 | 52867468 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,351,235 | 2,841.070781 | 52867467 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,960,622 | 1.142085 | 52867468 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,884,388 | 0.000012 | 52867467 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,774,693 | 404.141962 | 52867467 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2904 | 2,711,538 | 97.053507 | 52867468 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,310,223 | 0.000010 | 52867467 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,218,099 | 1,218,937.898289 | 52867467 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/AERO | 10000 | 2,119,972 | 1.163788 | 52867467 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,857 | 1.238895 | 52867467 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,920 | 1.383226 | 52867467 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,931,096 | 0.000000 | 52867467 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,902,114 | 1.105600 | 52867467 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 1,833,004 | 1,028.088149 | 52867467 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | XDP/USDC | 100 | 1,812,536 | 0.019306 | 52867467 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,250 | 0.000012 | 52867467 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,773,062 | 16.078035 | 52867467 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,722,928 | 13,706.135010 | 52867467 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,703,574 | 0.021101 | 52867467 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,677,581 | 2.310418 | 52867467 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,664,975 | 2,842.240529 | 52867467 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,561,557 | 0.916062 | 52867467 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,827 | 0.825996 | 52867467 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,411,603 | 1.123609 | 52867467 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,342,292 | 0.004804 | 52867467 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,336,879 | 0.000000 | 52867467 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,315,799 | 0.000276 | 52867467 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,303,108 | 0.029529 | 52867467 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,253,755 | 2,424.363037 | 52867467 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,052 | 63.601712 | 52867467 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,212,352 | 23.091499 | 52867467 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,211,922 | 68,956.367313 | 52867467 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/doginme | 10000 | 1,206,862 | 35,660,200.259008 | 52867467 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,104 | 0.436382 | 52867467 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,162,218 | 494,160.495614 | 52867467 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,156,294 | 1,198,023.429938 | 52867467 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,134,225 | 48.978563 | 52867467 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 506 | 1,091,741 | 0.886066 | 52867468 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,083,044 | 21,126,867.748703 | 52867467 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,077,132 | 15.535849 | 52867468 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 5556 ; routes examinées : 125198904 ; candidats optimisés : 527279 ; net attendu > 0 : 68 ; dernier cycle 818.7 ms
- Rejets (moteur) : {'spread_below_threshold': 123722156, 'liquidity_below_min': 835019, 'negative_expected_net': 527211, 'pool_quarantined': 106232, 'borrow_bound_too_small': 5537, 'cycle_budget_exhausted': 2470}
- Enregistrements de la session : 527277 ; net attendu > 0 : 68 ; simulés (eth_call de la vraie tx) : 13 (ok 4, échec 9) ; étiquettes ghost N+1 : 4/7 positives
- Décisions : {'REJECTED': 527277} ; motifs de rejet : {'below_safety_margin': 33, 'negative_expected_net': 527209, 'p_lower_below_threshold': 47, 'reliability_not_demonstrated': 21, 'sim_below_estimate': 1, 'simulation_failed': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.107790 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3137 €) | — | 12.93 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.107651 WETH | 0.000142 WETH | 0.000000 WETH | 0.000003 WETH | 0.000139 WETH (0.3131 €) | — | 12.92 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 263.009308 USDC | 0.347768 USDC | 0.000000 USDC | 0.007447 USDC | 0.340321 USDC (0.3131 €) | — | 12.94 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 262.890606 USDC | 0.347145 USDC | 0.000000 USDC | 0.007447 USDC | 0.339698 USDC (0.3125 €) | — | 12.92 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.104793 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.3090 €) | — | 13.10 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 255.494914 USDC | 0.342672 USDC | 0.000000 USDC | 0.007447 USDC | 0.335225 USDC (0.3084 €) | — | 13.12 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.105902 WETH | 0.000139 WETH | 0.000000 WETH | 0.000003 WETH | 0.000136 WETH (0.3058 €) | — | 12.82 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 258.491603 USDC | 0.339173 USDC | 0.000000 USDC | 0.007447 USDC | 0.331726 USDC (0.3052 €) | — | 12.83 | 0.000 (n=24) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 223.523660 USDC | 0.301346 USDC | 0.000000 USDC | 0.005571 USDC | 0.295775 USDC (0.2721 €) | — | 13.23 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.075471 WETH | 0.000103 WETH | 0.000000 WETH | 0.000003 WETH | 0.000100 WETH (0.2250 €) | — | 13.24 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 183.847545 USDC | 0.251751 USDC | 0.000000 USDC | 0.007818 USDC | 0.243933 USDC (0.2244 €) | — | 13.27 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.085936 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1959 €) | — | 10.12 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 209.235903 USDC | 0.219816 USDC | 0.000000 USDC | 0.007447 USDC | 0.212369 USDC (0.1954 €) | — | 10.15 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.063447 WETH | 0.000049 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.1038 €) | — | 7.26 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 154.894625 USDC | 0.119867 USDC | 0.000000 USDC | 0.007447 USDC | 0.112420 USDC (0.1034 €) | — | 7.26 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52864215 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.021357 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0595 €) | — | 12.37 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 51.983831 USDC | 0.071826 USDC | 0.000000 USDC | 0.007447 USDC | 0.064379 USDC (0.0592 €) | — | 12.38 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52864215 | WETH→[aerodrome]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.046829 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0565 €) | — | 5.36 | 0.038 (n=114) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 113.842964 USDC | 0.068253 USDC | 0.000000 USDC | 0.007109 USDC | 0.061144 USDC (0.0563 €) | — | 5.37 | 0.038 (n=114) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 52864215 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.031723 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0339 €) | — | 4.74 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 77.032104 USDC | 0.043354 USDC | 0.000000 USDC | 0.006687 USDC | 0.036667 USDC (0.0337 €) | — | 4.76 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52864934 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 44.658147 USDC | 0.019481 USDC | 0.000000 USDC | 0.007414 USDC | 0.012067 USDC (0.0111 €) | — | 2.70 | 0.113 (n=189) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52864935 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 44.658147 USDC | 0.019481 USDC | 0.000000 USDC | 0.007414 USDC | 0.012067 USDC (0.0111 €) | — | 2.70 | 0.113 (n=189) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52864934 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.018455 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0111 €) | — | 2.67 | 0.113 (n=189) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52864935 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.018455 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0111 €) | — | 2.67 | 0.113 (n=189) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 1552 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
