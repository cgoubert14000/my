# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T20:08:52+00:00 ; durée 154.92 min ; blocs 52864139 → 52868781 (4264 vus)

## Connexion
- Requêtes RPC : 58873 ; erreurs : 180 ; latence p50/p95 : 435.4/1,416.7 ms
- Rafraîchissements d'état : 4264 ; âge des données au dernier bloc : 16.86 s ; changements de frais LP observés (pools à frais dynamiques) : 9621
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 75645 ; cycles déclenchés par événement : 3513 ; avance médiane sur le rafraîchissement multicall : 732 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,432.06 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 577 pools, 327 jetons, 22534 routes
- Par DEX : uniswap_v3 136, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 395, par paires 0), mesurés 579, sous le plancher de 10000.0 $ : 2 → gardés 577 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2447.454075, 'AERO': 0.860145, 'cbBTC': 82683.957961}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,980,992 | 2,432.061687 | 52868787 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,176,400 | 1.164920 | 52868787 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,712,256 | 97.270675 | 52868787 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,305,425 | 0.029524 | 52868787 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,933,485 | 0.029513 | 52868787 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,489,196 | 0.029526 | 52868787 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,914,102 | 0.000012 | 52868787 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,559,466 | 2,437.906189 | 52868787 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,356,739 | 2,432.132452 | 52868787 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 8,152,154 | 0.000012 | 52868787 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,252,628 | 0.001678 | 52868787 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 758 | 7,175,743 | 2,438.698782 | 52868787 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 6,522,148 | 0.000012 | 52868787 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,408,609 | 0.029536 | 52868787 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,229,279 | 0.024538 | 52868787 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,695,822 | 0.000275 | 52868787 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,689,110 | 0.802394 | 52868787 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,582,635 | 1.168083 | 52868787 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,410,960 | 2,438.892225 | 52868787 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,370,651 | 0.998747 | 52868787 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,017,772 | 34,753.797524 | 52868787 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,362,794 | 2,841.307773 | 52868787 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 439 | 3,075,943 | 2,441.171113 | 52868787 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,864,043 | 0.000012 | 52868787 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,826,207 | 1,032.567074 | 52868787 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,711,165 | 97.297704 | 52868787 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,519,336 | 1.142086 | 52868787 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,376,487 | 403.011256 | 52868787 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,342,585 | 0.000010 | 52868787 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,219,461 | 1,218,937.898289 | 52868787 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,857 | 1.238895 | 52868787 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,920 | 1.383226 | 52868787 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,932,607 | 0.000000 | 52868787 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,903,762 | 1.105600 | 52868787 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,844,007 | 16.087197 | 52868787 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,816,776 | 0.019380 | 52868787 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,771,777 | 0.000012 | 52868787 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | fBOMB/USDC | 10000 | 1,703,929 | 0.021101 | 52868787 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,678,665 | 2.310418 | 52868787 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,669,121 | 2,834.714561 | 52868787 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,559,497 | 0.916062 | 52868787 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,827 | 0.825996 | 52868787 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,445,898 | 1.123801 | 52868787 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,419,650 | 13,653.892136 | 52868787 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,343,116 | 0.004804 | 52868787 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,337,970 | 0.000000 | 52868787 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,316,608 | 0.000276 | 52868787 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,302,474 | 0.029529 | 52868787 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,283,684 | 23.100650 | 52868787 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,254,291 | 2,437.911185 | 52868787 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,052 | 63.601712 | 52868787 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,211,983 | 35,279,712.983508 | 52868787 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/EDEL | 7000 | 1,211,734 | 69,062.488129 | 52868787 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,097 | 0.436382 | 52868787 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,162,932 | 494,160.495614 | 52868787 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,154,341 | 1,203,555.921362 | 52868787 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,135,750 | 1.106158 | 52868787 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | USDC/NOCK | 3000 | 1,128,962 | 49.420620 | 52868787 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,091,109 | 0.886057 | 52868787 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,084,670 | 21,094,738.474963 | 52868787 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 7776 ; routes examinées : 175224384 ; candidats optimisés : 764583 ; net attendu > 0 : 82 ; dernier cycle 576.5 ms
- Rejets (moteur) : {'spread_below_threshold': 173165887, 'liquidity_below_min': 1177031, 'negative_expected_net': 764501, 'pool_quarantined': 106232, 'borrow_bound_too_small': 7756, 'cycle_budget_exhausted': 2895}
- Enregistrements de la session : 764583 ; net attendu > 0 : 82 ; simulés (eth_call de la vraie tx) : 13 (ok 4, échec 9) ; étiquettes ghost N+1 : 4/7 positives
- Décisions : {'REJECTED': 764583} ; motifs de rejet : {'below_safety_margin': 47, 'negative_expected_net': 764501, 'p_lower_below_threshold': 61, 'reliability_not_demonstrated': 21, 'sim_below_estimate': 1, 'simulation_failed': 9}

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
| 52868406 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,156.579353 USDC | 0.062489 USDC | 0.000000 USDC | 0.005476 USDC | 0.057013 USDC (0.0525 €) | — | 0.49 | 0.014 (n=56) | REJECTED | below_safety_margin(57013<231315), p_lower_below_threshold(0.01<0.75) |
| 52868407 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,156.579353 USDC | 0.062489 USDC | 0.000000 USDC | 0.005476 USDC | 0.057013 USDC (0.0525 €) | — | 0.49 | 0.014 (n=56) | REJECTED | below_safety_margin(57013<231315), p_lower_below_threshold(0.01<0.75) |
| 52868406 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.475691 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0524 €) | — | 0.49 | 0.014 (n=56) | REJECTED | below_safety_margin(23413190135071<95138231129005), p_lower_below_threshold(0.01<0.75) |
| 52868407 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.475691 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0524 €) | — | 0.49 | 0.014 (n=56) | REJECTED | below_safety_margin(23413190135071<95138231129005), p_lower_below_threshold(0.01<0.75) |
| 52864215 | WETH→[uniswap_v2]→USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH | 0.031723 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0339 €) | — | 4.74 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52864215 | USDC→[uniswap_v3]→ZORA→[aerodrome_slipstream]→WETH→[uniswap_v2]→USDC | 77.032104 USDC | 0.043354 USDC | 0.000000 USDC | 0.006687 USDC | 0.036667 USDC (0.0337 €) | — | 4.76 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1552 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.095 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.5% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
