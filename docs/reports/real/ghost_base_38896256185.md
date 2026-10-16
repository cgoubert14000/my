# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-16T12:05:27+00:00 ; durée 12.23 min ; blocs 52681120 → 52681489 (367 vus)

## Connexion
- Requêtes RPC : 5006 ; erreurs : 0 ; latence p50/p95 : 86.8/1,011.3 ms
- Rafraîchissements d'état : 367 ; âge des données au dernier bloc : 2.18 s ; changements de frais LP observés (pools à frais dynamiques) : 796
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6698 ; cycles déclenchés par événement : 349 ; avance médiane sur le rafraîchissement multicall : 446 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,475.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 328 jetons, 21482 routes
- Par DEX : uniswap_v3 136, aerodrome 236, aerodrome_slipstream 153, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 209 (rejetés 2) → 614 jetons ; pools candidats 3925 (énumérés 391, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2482.328501, 'AERO': 0.918334, 'cbBTC': 82582.444221}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,150,267 | 2,475.888083 | 52681489 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 47,036,813 | 1.088797 | 52681489 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,710,451 | 0.029983 | 52681489 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,883,357 | 0.030036 | 52681489 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,745,275 | 100.207380 | 52681489 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,622,370 | 0.030047 | 52681489 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,771,300 | 0.000012 | 52681489 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,208,617 | 2,469.683613 | 52681489 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 8,116,088 | 0.000012 | 52681489 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 788 | 7,557,137 | 2,468.723074 | 52681489 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,280,202 | 0.001683 | 52681489 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 6,630,869 | 0.000012 | 52681489 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | fBOMB/AERO | 10000 | 5,504,471 | 0.024796 | 52681489 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | WETH/USDC | 3000 | 5,477,924 | 2,475.894767 | 52681489 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,457,391 | 0.029984 | 52681489 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,290,544 | 1.000855 | 52681489 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,948,796 | 0.802398 | 52681489 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,817,109 | 0.000281 | 52681489 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,601,515 | 1.084051 | 52681489 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,386,457 | 0.998889 | 52681489 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,362,210 | 2,469.179653 | 52681489 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,101,696 | 34,558.788851 | 52681489 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,582,486 | 2,678.451916 | 52681489 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 451 | 3,432,264 | 2,471.951322 | 52681489 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 3,073,490 | 1.141840 | 52681489 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2736 | 3,031,925 | 1,000.594652 | 52681489 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,855,831 | 0.000012 | 52681489 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,705,260 | 400.954841 | 52681489 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2742 | 2,704,912 | 100.222244 | 52681489 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,484,786 | 0.000011 | 52681489 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,323,555 | 1,152,610.812958 | 52681489 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,132,944 | 0.000000 | 52681489 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,736 | 1.195936 | 52681489 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,461 | 1.403757 | 52681489 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,893,654 | 15.125962 | 52681489 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,867,341 | 0.023300 | 52681489 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,824,476 | 13,363.255779 | 52681489 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,784,394 | 0.000012 | 52681489 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,780,855 | 0.018870 | 52681489 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,709,572 | 2.311975 | 52681489 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,587,095 | 2,693.795722 | 52681489 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,538,981 | 0.916551 | 52681489 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | weETH_04c0/WETH | 500 | 1,530,858 | 1.105492 | 52681489 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3016 | 1,504,684 | 2,694.029921 | 52681489 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,120 | 0.825820 | 52681489 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,391,433 | 1.125534 | 52681489 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,389,965 | 0.000000 | 52681489 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,380,429 | 0.004814 | 52681489 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,352,292 | 0.000281 | 52681489 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,309,862 | 0.437020 | 52681489 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,285,169 | 23.275357 | 52681489 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,250,232 | 62.167285 | 52681489 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,228,619 | 1.105591 | 52681489 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,227,406 | 0.030036 | 52681489 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,222,137 | 35,928,486.043046 | 52681489 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,220,797 | 1,115,386.891989 | 52681489 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,220,003 | 2,469.712414 | 52681489 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,212,497 | 0.886584 | 52681489 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,181,768 | 496,085.125904 | 52681489 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,147,056 | 81,119.922572 | 52681489 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 715 ; routes examinées : 15359630 ; candidats optimisés : 82752 ; net attendu > 0 : 122 ; dernier cycle 151.6 ms
- Rejets (moteur) : {'spread_below_threshold': 15082511, 'liquidity_below_min': 177188, 'negative_expected_net': 82630, 'pool_quarantined': 16464, 'borrow_bound_too_small': 715}
- Enregistrements de la session : 82752 ; net attendu > 0 : 122 ; simulés (eth_call de la vraie tx) : 21 (ok 12, échec 9) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 82752} ; motifs de rejet : {'below_safety_margin': 40, 'negative_expected_net': 82630, 'p_lower_below_threshold': 61, 'price_impact': 6, 'reliability_not_demonstrated': 61, 'simulation_failed': 9}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.064584 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1574 €) | 0.000069 WETH | 10.67 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.064584 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1574 €) | 0.000069 WETH | 10.67 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.064584 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1574 €) | — | 10.67 | 0.002 (n=4) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 159.458938 USDC | 0.178085 USDC | 0.000000 USDC | 0.007467 USDC | 0.170618 USDC (0.1570 €) | — | 10.70 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 159.458938 USDC | 0.178085 USDC | 0.000000 USDC | 0.007467 USDC | 0.170618 USDC (0.1570 €) | — | 10.70 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 159.458938 USDC | 0.178085 USDC | 0.000000 USDC | 0.007467 USDC | 0.170618 USDC (0.1570 €) | — | 10.70 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.060495 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1402 €) | 0.000061 WETH | 10.15 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681235 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.060495 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1402 €) | 0.000061 WETH | 10.15 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681236 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.060495 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1402 €) | — | 10.15 | 0.009 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 149.414789 USDC | 0.159068 USDC | 0.000000 USDC | 0.007125 USDC | 0.151943 USDC (0.1398 €) | — | 10.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 149.414789 USDC | 0.159068 USDC | 0.000000 USDC | 0.007125 USDC | 0.151943 USDC (0.1398 €) | — | 10.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 149.414789 USDC | 0.159068 USDC | 0.000000 USDC | 0.007125 USDC | 0.151943 USDC (0.1398 €) | — | 10.17 | 0.009 (n=32) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52681235 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061861 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1393 €) | 0.000061 WETH | 9.86 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061861 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1393 €) | 0.000061 WETH | 9.86 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681236 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061861 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1393 €) | — | 9.86 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 152.667787 USDC | 0.158388 USDC | 0.000000 USDC | 0.007467 USDC | 0.150921 USDC (0.1388 €) | — | 9.89 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 152.667787 USDC | 0.158388 USDC | 0.000000 USDC | 0.007467 USDC | 0.150921 USDC (0.1388 €) | — | 9.89 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 152.667787 USDC | 0.158388 USDC | 0.000000 USDC | 0.007467 USDC | 0.150921 USDC (0.1388 €) | — | 9.89 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061700 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1383 €) | — | 9.81 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061700 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1383 €) | — | 9.81 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061700 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1383 €) | — | 9.81 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 152.479110 USDC | 0.157286 USDC | 0.000000 USDC | 0.007467 USDC | 0.149819 USDC (0.1378 €) | — | 9.83 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 152.479110 USDC | 0.157286 USDC | 0.000000 USDC | 0.007467 USDC | 0.149819 USDC (0.1378 €) | — | 9.83 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681236 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 152.479110 USDC | 0.157286 USDC | 0.000000 USDC | 0.007467 USDC | 0.149819 USDC (0.1378 €) | — | 9.83 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52681235 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.061232 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000060 WETH (0.1362 €) | — | 9.74 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 521 ; taux observé 0.117 ; borne inférieure crédible (0.9) 0.100 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
