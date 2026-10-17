# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T16:35:40+00:00 ; durée 27.59 min ; blocs 52731965 → 52732793 (783 vus)

## Connexion
- Requêtes RPC : 10546 ; erreurs : 0 ; latence p50/p95 : 270.1/1,611.1 ms
- Rafraîchissements d'état : 783 ; âge des données au dernier bloc : 4.83 s ; changements de frais LP observés (pools à frais dynamiques) : 1153
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16507 ; cycles déclenchés par événement : 885 ; avance médiane sur le rafraîchissement multicall : 1,704 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,409.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21110 routes
- Par DEX : uniswap_v3 136 (quarantaine 1), aerodrome 235 (quarantaine 1), aerodrome_slipstream 156, pancakeswap_v3 31 (quarantaine 1), uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3916 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2411.894998, 'AERO': 0.849168, 'cbBTC': 81312.167025}
- Pools en quarantaine : 3 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52732875; uniswap_v3:USDC/ICNT@0x9331F5: simulation failed ×5 (model/chain mismatch) — until block 52733024; pancakeswap_v3:USDC/ICNT@0x175Aa9: simulation failed ×5 (model/chain mismatch) — until block 52733024

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,154,966 | 2,409.751489 | 52732793 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,046,902 | 1.180644 | 52732793 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 19,201,949 | 0.029663 | 52732793 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,177,989 | 0.029620 | 52732793 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,781,885 | 107.226541 | 52732793 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,424,619 | 0.029687 | 52732793 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,753,232 | 0.000012 | 52732793 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,087,450 | 2,404.650984 | 52732793 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,839,826 | 0.000012 | 52732793 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 7,658,436 | 0.000012 | 52732793 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,233,850 | 2,404.129009 | 52732795 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,124,684 | 0.001661 | 52732793 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,400,741 | 2,409.823421 | 52732793 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,319,962 | 0.029619 | 52732795 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,233,484 | 0.025348 | 52732793 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,232,945 | 1.000855 | 52732793 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,816,737 | 0.802398 | 52732793 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,635,285 | 0.000273 | 52732793 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,417,976 | 0.998801 | 52732793 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,405,086 | 2,404.393644 | 52732795 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDT | 409 | 4,174,902 | 2,408.205229 | 52732793 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,023,990 | 34,013.734427 | 52732793 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,555,610 | 1.172258 | 52732793 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,385,328 | 2,820.082885 | 52732793 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,910,473 | 1.141801 | 52732793 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,836,523 | 0.000012 | 52732793 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,556,581 | 107.265796 | 52732793 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,491,148 | 407.531174 | 52732793 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,396,934 | 0.000010 | 52732793 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,232,922 | 1,182,290.188062 | 52732793 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,125,971 | 1.123521 | 52732793 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,107,462 | 1.199039 | 52732793 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 2,080,177 | 1,025.258776 | 52732795 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52732793 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,866,341 | 15.788277 | 52732793 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,820,322 | 0.022074 | 52732793 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,804,477 | 0.000000 | 52732793 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,075 | 0.000012 | 52732793 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,736,890 | 0.018092 | 52732794 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,668,625 | 2.306138 | 52732793 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,638,768 | 13,760.526679 | 52732793 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,540,170 | 0.916547 | 52732793 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,520,538 | 2,838.484362 | 52732793 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,517,516 | 1.105495 | 52732793 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,472,476 | 2,839.620112 | 52732793 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,780 | 0.825404 | 52732793 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,357,592 | 0.000000 | 52732793 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,327,029 | 0.435657 | 52732793 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,305,827 | 0.004696 | 52732793 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,299,098 | 0.000272 | 52732793 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,708 | 62.319117 | 52732793 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,246,267 | 23.342752 | 52732793 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,229,745 | 0.029692 | 52732793 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,226,085 | 1.131401 | 52732793 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,215,556 | 1.105716 | 52732793 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,194,134 | 35,598,184.590662 | 52732793 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,189,520 | 2,404.667768 | 52732793 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,169,615 | 1,151,117.734969 | 52732793 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,137,735 | 510,695.154033 | 52732793 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,116,314 | 14.187172 | 52732793 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 1667 ; routes examinées : 35190370 ; candidats optimisés : 278103 ; net attendu > 0 : 59 ; dernier cycle 824.5 ms
- Rejets (moteur) : {'spread_below_threshold': 34544847, 'negative_expected_net': 278044, 'liquidity_below_min': 272681, 'pool_quarantined': 84432, 'cycle_budget_exhausted': 8296, 'borrow_bound_too_small': 1665}
- Enregistrements de la session : 278103 ; net attendu > 0 : 59 ; simulés (eth_call de la vraie tx) : 22 (ok 1, échec 21) ; étiquettes ghost N+1 : 0/12 positives
- Décisions : {'REJECTED': 278103} ; motifs de rejet : {'below_safety_margin': 36, 'negative_expected_net': 278044, 'p_lower_below_threshold': 36, 'price_impact': 32, 'reliability_not_demonstrated': 23, 'simulation_failed': 21}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52732232 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 264.379140 USDC | 0.953137 USDC | 0.000000 USDC | 0.005417 USDC | 0.947720 USDC (0.8719 €) | — | 35.85 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732691 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 82.007926 USDC | 0.093812 USDC | 0.000000 USDC | 0.005413 USDC | 0.088399 USDC (0.0813 €) | — | 10.78 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732602 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 71.137118 USDC | 0.070045 USDC | 0.000000 USDC | 0.005414 USDC | 0.064631 USDC (0.0595 €) | — | 9.09 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732142 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 66.177836 USDC | 0.061275 USDC | 0.000000 USDC | 0.005418 USDC | 0.055857 USDC (0.0514 €) | — | 8.44 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732133 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 63.237107 USDC | 0.055672 USDC | 0.000000 USDC | 0.005417 USDC | 0.050255 USDC (0.0462 €) | — | 7.95 | 0.000 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732724 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 57.353428 USDC | 0.045997 USDC | 0.000000 USDC | 0.005413 USDC | 0.040584 USDC (0.0373 €) | — | 7.08 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732707 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 56.643370 USDC | 0.045074 USDC | 0.000000 USDC | 0.005413 USDC | 0.039661 USDC (0.0365 €) | — | 7.00 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52731994 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.123984 USDC | 0.035056 USDC | 0.000000 USDC | 0.005418 USDC | 0.029638 USDC (0.0273 €) | — | 6.03 | 0.000 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732179 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 47.491583 USDC | 0.031398 USDC | 0.000000 USDC | 0.005418 USDC | 0.025980 USDC (0.0239 €) | — | 5.47 | 0.000 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732563 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 43.225845 USDC | 0.026339 USDC | 0.000000 USDC | 0.005413 USDC | 0.020926 USDC (0.0193 €) | 0.020926 USDC | 4.84 | 0.000 (n=41) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52732460 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.019406 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0065 €) | — | 1.52 | 0.290 (n=51) | REJECTED | below_safety_margin(2943520689558<3881143784511), p_lower_below_threshold(0.29<0.75) |
| 52732460 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 46.869297 USDC | 0.015056 USDC | 0.000000 USDC | 0.007979 USDC | 0.007077 USDC (0.0065 €) | — | 1.51 | 0.290 (n=51) | REJECTED | below_safety_margin(7077<9373), p_lower_below_threshold(0.29<0.75) |
| 52732460 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.019718 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0064 €) | — | 1.46 | 0.114 (n=81) | REJECTED | below_safety_margin(2887808715383<3943537922103), p_lower_below_threshold(0.11<0.75) |
| 52732460 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 47.437273 USDC | 0.014921 USDC | 0.000000 USDC | 0.007979 USDC | 0.006942 USDC (0.0064 €) | — | 1.46 | 0.114 (n=81) | REJECTED | below_safety_margin(6942<9487), p_lower_below_threshold(0.11<0.75) |
| 52732225 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.052177 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0063 €) | — | 0.55 | 0.060 (n=5) | REJECTED | below_safety_margin(2848717723533<10435382408403), reliability_not_demonstrated |
| 52732225 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.044966 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0062 €) | — | 0.63 | 0.060 (n=5) | REJECTED | below_safety_margin(2811407128763<8993117040184), reliability_not_demonstrated |
| 52732703 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 28.271366 USDC | 0.011093 USDC | 0.000000 USDC | 0.005413 USDC | 0.005680 USDC (0.0052 €) | — | 2.01 | 0.039 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732228 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.072788 USDC | 0.010116 USDC | 0.000000 USDC | 0.005417 USDC | 0.004699 USDC (0.0043 €) | — | 1.74 | 0.039 (n=21) | REJECTED | below_safety_margin(4699<5414), reliability_not_demonstrated |
| 52732228 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.072788 USDC | 0.010116 USDC | 0.000000 USDC | 0.005417 USDC | 0.004699 USDC (0.0043 €) | — | 1.74 | 0.039 (n=21) | REJECTED | below_safety_margin(4699<5414), reliability_not_demonstrated |
| 52732109 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 25.543389 USDC | 0.009270 USDC | 0.000000 USDC | 0.005418 USDC | 0.003852 USDC (0.0035 €) | — | 1.51 | 0.039 (n=21) | REJECTED | below_safety_margin(3852<5108), reliability_not_demonstrated |
| 52732652 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 24.755464 USDC | 0.008691 USDC | 0.000000 USDC | 0.005413 USDC | 0.003278 USDC (0.0030 €) | — | 1.32 | 0.039 (n=21) | REJECTED | below_safety_margin(3278<4951), reliability_not_demonstrated |
| 52732653 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 24.755464 USDC | 0.008691 USDC | 0.000000 USDC | 0.005413 USDC | 0.003278 USDC (0.0030 €) | — | 1.32 | 0.039 (n=21) | REJECTED | below_safety_margin(3278<4951), reliability_not_demonstrated |
| 52732575 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.008779 USDC | 0.000000 USDC | 0.006579 USDC | 0.002200 USDC (0.0020 €) | — | 22.00 | 0.011 (n=26) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 52732574 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.008762 USDC | 0.000000 USDC | 0.006580 USDC | 0.002182 USDC (0.0020 €) | — | 21.82 | 0.012 (n=24) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 52732575 | USDC→[uniswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.008680 USDC | 0.000000 USDC | 0.006579 USDC | 0.002101 USDC (0.0019 €) | — | 21.01 | 0.011 (n=26) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 754 ; taux observé 0.121 ; borne inférieure crédible (0.9) 0.106 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
