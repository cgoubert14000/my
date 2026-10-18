# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-18T03:07:21+00:00 ; durée 322.39 min ; blocs 52742072 → 52751738 (8498 vus)

## Connexion
- Requêtes RPC : 116975 ; erreurs : 230 ; latence p50/p95 : 348.8/1,554.8 ms
- Rafraîchissements d'état : 8498 ; âge des données au dernier bloc : 3.07 s ; changements de frais LP observés (pools à frais dynamiques) : 15995
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 152264 ; cycles déclenchés par événement : 8293 ; avance médiane sur le rafraîchissement multicall : 665 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,410.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21034 routes
- Par DEX : uniswap_v3 135, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3915 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2370.395845, 'AERO': 0.840439, 'cbBTC': 80973.333664}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,137,618 | 2,410.069913 | 52751737 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,717,925 | 1.189761 | 52751737 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,167,230 | 0.029544 | 52751737 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,771,795 | 107.751571 | 52751737 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,197,467 | 0.029492 | 52751737 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,441,915 | 0.029478 | 52751737 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,759,925 | 0.000012 | 52751737 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,046,520 | 2,416.190322 | 52751737 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 7,850,094 | 0.000012 | 52751737 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 7,589,847 | 0.000012 | 52751737 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,141,067 | 0.001659 | 52751737 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 669 | 7,050,013 | 2,417.028172 | 52751737 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/USDC | 3000 | 5,486,590 | 2,411.136008 | 52751737 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,333,292 | 0.029554 | 52751737 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,233,637 | 1.000855 | 52751737 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,147,566 | 0.025619 | 52751737 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,817,404 | 0.802399 | 52751737 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,630,398 | 0.000273 | 52751737 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 424 | 4,518,395 | 2,419.807359 | 52751737 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,429,677 | 0.998808 | 52751737 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,407,755 | 2,416.641135 | 52751738 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,102,427 | 32,734.152492 | 52751737 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,806,694 | 1.184583 | 52751737 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,368,378 | 2,850.603965 | 52751737 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,909,210 | 1.141805 | 52751737 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,837,770 | 0.000012 | 52751737 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,585,179 | 407.031705 | 52751737 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,550,502 | 107.723381 | 52751737 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,482,157 | 0.000010 | 52751737 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,236,780 | 1,178,528.054669 | 52751737 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,105,878 | 1.199991 | 52751737 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,025,824 | 1.385318 | 52751737 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,015,587 | 1.123188 | 52751737 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,871,428 | 0.000000 | 52751737 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,808,924 | 0.021524 | 52751737 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,055 | 0.000012 | 52751737 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,727,611 | 0.017950 | 52751737 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,692,958 | 15.851932 | 52751737 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,669,625 | 2.305932 | 52751737 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,567,629 | 0.916398 | 52751737 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,517,787 | 1.105497 | 52751737 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | WETH/AERO | 3000 | 1,516,609 | 2,870.652508 | 52751737 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,460,384 | 2,870.610476 | 52751737 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,614 | 0.825990 | 52751737 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,399,520 | 13,792.169175 | 52751737 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | DRB/WETH | 10000 | 1,332,501 | 0.000000 | 52751737 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,317,254 | 0.435707 | 52751737 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,309,869 | 0.004714 | 52751737 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,297,756 | 0.000271 | 52751737 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,254,585 | 0.029474 | 52751737 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | USDC/SEND | 3000 | 1,249,073 | 62.282694 | 52751737 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,244,442 | 23.308722 | 52751737 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,197,780 | 35,330,684.463418 | 52751737 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,195,400 | 1.131434 | 52751737 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,191,439 | 1.105817 | 52751737 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,176,017 | 2,416.150678 | 52751737 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,164,322 | 1,161,915.898617 | 52751737 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,141,984 | 0.885553 | 52751737 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,139,228 | 514,765.248826 | 52751737 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,105,671 | 14.537634 | 52751737 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 16790 ; routes examinées : 353160860 ; candidats optimisés : 2009443 ; net attendu > 0 : 706 ; dernier cycle 275.6 ms
- Rejets (moteur) : {'spread_below_threshold': 348097906, 'liquidity_below_min': 3026713, 'negative_expected_net': 2008737, 'borrow_bound_too_small': 16780, 'cycle_budget_exhausted': 7826, 'pool_quarantined': 2192}
- Enregistrements de la session : 2009443 ; net attendu > 0 : 706 ; simulés (eth_call de la vraie tx) : 35 (ok 2, échec 33) ; étiquettes ghost N+1 : 0/32 positives
- Décisions : {'REJECTED': 2009443} ; motifs de rejet : {'below_safety_margin': 619, 'negative_expected_net': 2008737, 'p_lower_below_threshold': 548, 'reliability_not_demonstrated': 158, 'simulation_failed': 33, 'stale_data': 76}

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
| 52749533 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 467.075315 USDC | 3.613777 USDC | 0.000000 USDC | 0.005410 USDC | 3.608367 USDC (3.3197 €) | — | 77.25 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52744597 | WETH→[aerodrome]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.030006 WETH | 0.000364 WETH | 0.000000 WETH | 0.000003 WETH | 0.000361 WETH (0.7937 €) | — | 120.36 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52744597 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 70.297514 USDC | 0.852826 USDC | 0.000000 USDC | 0.006850 USDC | 0.845976 USDC (0.7783 €) | — | 120.34 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52747442 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→USDC | 792.015544 USDC | 0.564790 USDC | 0.000000 USDC | 0.007560 USDC | 0.557230 USDC (0.5127 €) | — | 7.04 | 0.141 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 843 ; taux observé 0.127 ; borne inférieure crédible (0.9) 0.113 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
