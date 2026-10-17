# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T23:39:24+00:00 ; durée 114.43 min ; blocs 52742072 → 52745504 (3179 vus)

## Connexion
- Requêtes RPC : 42484 ; erreurs : 0 ; latence p50/p95 : 367.1/1,331.9 ms
- Rafraîchissements d'état : 3179 ; âge des données au dernier bloc : 3.14 s ; changements de frais LP observés (pools à frais dynamiques) : 6571
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 60347 ; cycles déclenchés par événement : 3227 ; avance médiane sur le rafraîchissement multicall : 775 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,389.04 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21034 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3915 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2370.395845, 'AERO': 0.840439, 'cbBTC': 80973.333664}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,367,466 | 2,389.039531 | 52745505 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,770,679 | 1.188275 | 52745505 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,021,192 | 0.029461 | 52745505 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,661,993 | 107.277440 | 52745505 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 11,814,310 | 0.029403 | 52745505 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,363,878 | 0.029389 | 52745505 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,734,702 | 0.000012 | 52745505 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 9,305,584 | 0.000012 | 52745505 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,017,501 | 2,393.390418 | 52745505 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,829,288 | 0.000012 | 52745505 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,090,437 | 0.001655 | 52745505 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 654 | 6,991,884 | 2,393.749834 | 52745505 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,462,848 | 2,389.700855 | 52745505 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,290,519 | 0.029469 | 52745505 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,187,968 | 1.000855 | 52745505 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,149,114 | 0.025517 | 52745505 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,775,365 | 0.802399 | 52745505 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,589,914 | 0.000273 | 52745505 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,403,444 | 0.998808 | 52745505 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,372,181 | 2,393.937241 | 52745505 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDT | 421 | 4,053,393 | 2,397.511023 | 52745505 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,042,123 | 33,132.271471 | 52745505 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,000,057 | 1.184582 | 52745505 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,355,744 | 2,822.949925 | 52745505 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,928,565 | 0.000010 | 52745505 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,884,819 | 1.141815 | 52745505 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,827,638 | 0.000012 | 52745505 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,775,608 | 405.555272 | 52745505 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,534,492 | 107.306637 | 52745505 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,222,275 | 1,173,215.805170 | 52745505 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,128,792 | 1.123129 | 52745505 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52745505 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,540 | 1.418010 | 52745505 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,909,027 | 15.803407 | 52745505 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,876,483 | 0.000000 | 52745505 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,797,439 | 0.021510 | 52745505 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,770,670 | 0.000012 | 52745505 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,715,561 | 0.017735 | 52745505 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 1,715,469 | 1,011.770232 | 52745505 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/msETH (stable) | 500 | 1,655,812 | 2.304324 | 52745505 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,619,787 | 13,774.463004 | 52745505 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,526,942 | 0.916543 | 52745505 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,508,573 | 2,838.568689 | 52745505 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,504,475 | 1.105497 | 52745505 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3004 | 1,458,410 | 2,838.510308 | 52745505 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,614 | 0.825990 | 52745505 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,572 | 0.435397 | 52745505 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,322,237 | 0.000000 | 52745505 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,815 | 0.004702 | 52745505 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,286,409 | 0.000272 | 52745505 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,249,143 | 62.275669 | 52745505 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,234,073 | 1.131049 | 52745505 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,231,748 | 23.327051 | 52745505 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,222,708 | 0.029388 | 52745505 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,205,108 | 1.105716 | 52745505 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,196,279 | 34,538,835.727227 | 52745505 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,179,359 | 2,393.321920 | 52745505 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,159,072 | 1,152,092.793349 | 52745505 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,129,534 | 508,805.536462 | 52745505 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,113,660 | 14.276301 | 52745505 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 6405 ; routes examinées : 134722770 ; candidats optimisés : 717132 ; net attendu > 0 : 396 ; dernier cycle 292.5 ms
- Rejets (moteur) : {'spread_below_threshold': 132924987, 'liquidity_below_min': 1070517, 'negative_expected_net': 716736, 'borrow_bound_too_small': 6402, 'cycle_budget_exhausted': 2520, 'pool_quarantined': 1212}
- Enregistrements de la session : 717132 ; net attendu > 0 : 396 ; simulés (eth_call de la vraie tx) : 14 (ok 0, échec 14) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 717132} ; motifs de rejet : {'below_safety_margin': 350, 'negative_expected_net': 716736, 'p_lower_below_threshold': 268, 'reliability_not_demonstrated': 128, 'simulation_failed': 14, 'stale_data': 52}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,927.577789 USDC | 21.654326 USDC | 0.000000 USDC | 0.008630 USDC | 21.645696 USDC (19.9140 €) | — | 112.29 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.806783 WETH | 0.009063 WETH | 0.000000 WETH | 0.000004 WETH | 0.009060 WETH (19.9097 €) | — | 112.29 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,848.244551 USDC | 21.382642 USDC | 0.000000 USDC | 0.008268 USDC | 21.374374 USDC (19.6644 €) | — | 115.65 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.773564 WETH | 0.008949 WETH | 0.000000 WETH | 0.000003 WETH | 0.008946 WETH (19.6597 €) | — | 115.65 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52744597 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.763494 WETH | 0.008710 WETH | 0.000000 WETH | 0.000004 WETH | 0.008707 WETH (19.1339 €) | — | 114.04 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,823.421253 USDC | 20.802603 USDC | 0.000000 USDC | 0.008630 USDC | 20.793973 USDC (19.1305 €) | — | 114.04 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.766810 WETH | 0.008607 WETH | 0.000000 WETH | 0.000003 WETH | 0.008603 WETH (18.9061 €) | — | 112.19 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 1,831.431265 USDC | 20.555575 USDC | 0.000000 USDC | 0.008268 USDC | 20.547307 USDC (18.9035 €) | — | 112.19 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.749373 WETH | 0.008448 WETH | 0.000000 WETH | 0.000004 WETH | 0.008444 WETH (18.5557 €) | — | 112.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,787.915432 USDC | 20.154925 USDC | 0.000000 USDC | 0.009355 USDC | 20.145570 USDC (18.5339 €) | — | 112.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→USDC | 1,340.686726 USDC | 17.751180 USDC | 0.000000 USDC | 0.006090 USDC | 17.745090 USDC (16.3255 €) | — | 132.36 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.516148 WETH | 0.005948 WETH | 0.000000 WETH | 0.000004 WETH | 0.005944 WETH (13.0625 €) | — | 115.16 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.553256 WETH | 0.005947 WETH | 0.000000 WETH | 0.000003 WETH | 0.005943 WETH (13.0614 €) | — | 107.43 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 1,317.592977 USDC | 14.162060 USDC | 0.000000 USDC | 0.007542 USDC | 14.154518 USDC (13.0222 €) | — | 107.43 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 1,225.139036 USDC | 14.118515 USDC | 0.000000 USDC | 0.009718 USDC | 14.108797 USDC (12.9801 €) | — | 115.16 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[aerodrome]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.514318 WETH | 0.005614 WETH | 0.000000 WETH | 0.000003 WETH | 0.005611 WETH (12.3314 €) | — | 109.10 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 1,223.572246 USDC | 13.356571 USDC | 0.000000 USDC | 0.007213 USDC | 13.349358 USDC (12.2814 €) | — | 109.10 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.374517 WETH | 0.004882 WETH | 0.000000 WETH | 0.000003 WETH | 0.004879 WETH (10.7217 €) | — | 130.27 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 888.379692 USDC | 11.579701 USDC | 0.000000 USDC | 0.006801 USDC | 11.572900 USDC (10.6471 €) | — | 130.27 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.327880 WETH | 0.003652 WETH | 0.000000 WETH | 0.000004 WETH | 0.003648 WETH (8.0169 €) | — | 111.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 774.007474 USDC | 8.620255 USDC | 0.000000 USDC | 0.008630 USDC | 8.611625 USDC (7.9227 €) | — | 111.26 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52744597 | WETH→[aerodrome]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.030006 WETH | 0.000364 WETH | 0.000000 WETH | 0.000003 WETH | 0.000361 WETH (0.7937 €) | — | 120.36 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 70.297514 USDC | 0.852826 USDC | 0.000000 USDC | 0.006850 USDC | 0.845976 USDC (0.7783 €) | — | 120.34 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52742532 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,627.590133 USDC | 0.324655 USDC | 0.000000 USDC | 0.007868 USDC | 0.316787 USDC (0.2914 €) | — | 1.21 | 0.123 (n=89) | REJECTED | below_safety_margin(316787<525518), p_lower_below_threshold(0.12<0.75) |
| 52742534 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,627.590133 USDC | 0.324655 USDC | 0.000000 USDC | 0.007868 USDC | 0.316787 USDC (0.2914 €) | — | 1.21 | 0.123 (n=89) | REJECTED | below_safety_margin(316787<525518), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 825 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.115 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
