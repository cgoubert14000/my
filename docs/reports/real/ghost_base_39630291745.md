# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T19:53:31+00:00 ; durée 230.17 min ; blocs 52904622 → 52911528 (6771 vus)

## Connexion
- Requêtes RPC : 85927 ; erreurs : 8 ; latence p50/p95 : 323.0/1,110.1 ms
- Rafraîchissements d'état : 6771 ; âge des données au dernier bloc : 2.5 s ; changements de frais LP observés (pools à frais dynamiques) : 14470
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44757 ; cycles déclenchés par événement : 2376 ; avance médiane sur le rafraîchissement multicall : 510 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,491.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 327 jetons, 21568 routes
- Par DEX : uniswap_v3 138, aerodrome 236, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3876 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2506.228815, 'AERO': 0.862155, 'cbBTC': 84485.636227}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,094,772 | 2,491.074497 | 52911528 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 37,569,455 | 1.184322 | 52911528 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,066,025 | 91.772119 | 52911528 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,718,025 | 0.029513 | 52911528 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,079,825 | 0.029570 | 52911528 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,613,394 | 0.029586 | 52911528 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,913,361 | 0.000012 | 52911528 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,872,537 | 2,493.733579 | 52911528 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,427,971 | 2,491.383247 | 52911528 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,424,330 | 0.000012 | 52911528 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,417,254 | 0.001672 | 52911528 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,064,622 | 2,493.434430 | 52911528 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 6,578,198 | 0.000012 | 52911528 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,680,483 | 0.029511 | 52911528 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,952,549 | 0.023048 | 52911528 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,579,956 | 2,493.568880 | 52911528 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,443,764 | 0.999950 | 52911528 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,250,989 | 0.000278 | 52911528 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,120,537 | 34,663.614326 | 52911528 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,492,922 | 1.179039 | 52911528 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,373,680 | 2,940.920157 | 52911528 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 400 | 3,159,192 | 2,496.299483 | 52911528 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/wstETH | 90 | 3,012,124 | 0.802297 | 52911528 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | WETH/VVV | 2724 | 2,865,872 | 91.797881 | 52911528 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,712,527 | 389.055671 | 52911528 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,293,907 | 1,196,489.382095 | 52911528 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,284,071 | 0.915907 | 52911528 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,278,366 | 0.000012 | 52911528 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,236,409 | 0.000010 | 52911528 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,093,309 | 0.000012 | 52911528 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,030,750 | 1.383527 | 52911528 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,963,601 | 0.000000 | 52911528 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,940,698 | 1.105712 | 52911528 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,818,802 | 0.018925 | 52911528 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,735,091 | 13,167.058056 | 52911528 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,721,775 | 15.815795 | 52911528 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,716,946 | 2.310827 | 52911528 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,708,545 | 1.493581 | 52911528 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,695,221 | 2,955.258029 | 52911528 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,571,589 | 1.142105 | 52911528 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,817 | 0.826528 | 52911528 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,437,962 | 1,045.691093 | 52911528 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,428,589 | 1.123587 | 52911528 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | fBOMB/USDC | 10000 | 1,412,814 | 0.019951 | 52911528 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,402,759 | 0.004850 | 52911528 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,380,200 | 0.000000 | 52911528 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,355,970 | 0.000280 | 52911528 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,334,227 | 0.029590 | 52911528 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,295,597 | 2,493.656786 | 52911528 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,270,451 | 1,042,367.967433 | 52911528 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,268,474 | 23.113475 | 52911528 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,242,702 | 35,080,447.920107 | 52911528 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,232,878 | 63.929620 | 52911528 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/NOCK | 3000 | 1,232,235 | 41.497337 | 52911528 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,214,131 | 72,065.278855 | 52911528 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,207,280 | 485,402.667813 | 52911528 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,178,926 | 1.106158 | 52911528 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,175,297 | 0.436479 | 52911528 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,140,249 | 0.886087 | 52911528 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,117,343 | 20,914,444.961615 | 52911528 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 9146 ; routes examinées : 197260928 ; candidats optimisés : 1071615 ; net attendu > 0 : 256 ; dernier cycle 298.1 ms
- Rejets (moteur) : {'spread_below_threshold': 194464970, 'liquidity_below_min': 1673421, 'negative_expected_net': 1071359, 'pool_quarantined': 38480, 'borrow_bound_too_small': 9132, 'cycle_budget_exhausted': 3310}
- Enregistrements de la session : 1071615 ; net attendu > 0 : 256 ; simulés (eth_call de la vraie tx) : 27 (ok 14, échec 13) ; étiquettes ghost N+1 : 0/23 positives
- Décisions : {'REJECTED': 1071615} ; motifs de rejet : {'below_safety_margin': 163, 'negative_expected_net': 1071359, 'p_lower_below_threshold': 186, 'price_impact': 7, 'reliability_not_demonstrated': 70, 'simulation_failed': 13, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52904867 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 5.290395 WETH | 0.004687 WETH | 0.000000 WETH | 0.000003 WETH | 0.004684 WETH (10.8029 €) | — | 8.85 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 13,257.243552 USDC | 11.747487 USDC | 0.000000 USDC | 0.007596 USDC | 11.739891 USDC (10.8007 €) | — | 8.86 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 4.690550 WETH | 0.004357 WETH | 0.000000 WETH | 0.000004 WETH | 0.004353 WETH (10.0396 €) | — | 9.28 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 11,757.060894 USDC | 10.919145 USDC | 0.000000 USDC | 0.010260 USDC | 10.908885 USDC (10.0362 €) | — | 9.28 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.523217 WETH | 0.003930 WETH | 0.000000 WETH | 0.000003 WETH | 0.003927 WETH (9.0578 €) | — | 8.68 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 11,336.129402 USDC | 9.852500 USDC | 0.000000 USDC | 0.008357 USDC | 9.844143 USDC (9.0566 €) | — | 8.68 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.094311 WETH | 0.003734 WETH | 0.000000 WETH | 0.000004 WETH | 0.003730 WETH (8.6031 €) | — | 9.11 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 10,260.868308 USDC | 9.359500 USDC | 0.000000 USDC | 0.010640 USDC | 9.348860 USDC (8.6010 €) | — | 9.11 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 4.773284 WETH | 0.003527 WETH | 0.000000 WETH | 0.000003 WETH | 0.003524 WETH (8.1278 €) | — | 7.38 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 11,963.205563 USDC | 8.839237 USDC | 0.000000 USDC | 0.007596 USDC | 8.831641 USDC (8.1251 €) | — | 7.38 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 4.026460 WETH | 0.002904 WETH | 0.000000 WETH | 0.000003 WETH | 0.002900 WETH (6.6900 €) | — | 7.20 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 10,092.039463 USDC | 7.278144 USDC | 0.000000 USDC | 0.008357 USDC | 7.269787 USDC (6.6882 €) | — | 7.20 | 0.138 (n=86) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 2.498645 WETH | 0.002198 WETH | 0.000000 WETH | 0.000003 WETH | 0.002195 WETH (5.0618 €) | — | 8.78 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 6,257.474670 USDC | 5.505138 USDC | 0.000000 USDC | 0.007976 USDC | 5.497162 USDC (5.0574 €) | — | 8.78 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 2.295257 WETH | 0.001970 WETH | 0.000000 WETH | 0.000003 WETH | 0.001967 WETH (4.5360 €) | — | 8.57 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 5,748.469875 USDC | 4.935009 USDC | 0.000000 USDC | 0.008357 USDC | 4.926652 USDC (4.5325 €) | — | 8.57 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 3,663.050751 USDC | 4.493251 USDC | 0.000000 USDC | 0.010640 USDC | 4.482611 USDC (4.1240 €) | — | 12.24 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.460331 WETH | 0.001792 WETH | 0.000000 WETH | 0.000004 WETH | 0.001787 WETH (4.1229 €) | — | 12.24 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 3,663.050751 USDC | 4.329451 USDC | 0.000000 USDC | 0.009879 USDC | 4.319572 USDC (3.9740 €) | — | 11.79 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.459881 WETH | 0.001726 WETH | 0.000000 WETH | 0.000004 WETH | 0.001722 WETH (3.9721 €) | — | 11.80 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 3,663.050751 USDC | 3.318625 USDC | 0.000000 USDC | 0.009879 USDC | 3.308746 USDC (3.0440 €) | — | 9.03 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.460239 WETH | 0.001323 WETH | 0.000000 WETH | 0.000004 WETH | 0.001320 WETH (3.0435 €) | — | 9.04 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH | 1.459884 WETH | 0.001316 WETH | 0.000000 WETH | 0.000004 WETH | 0.001312 WETH (3.0265 €) | — | 8.99 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 3,663.050751 USDC | 3.298919 USDC | 0.000000 USDC | 0.010260 USDC | 3.288659 USDC (3.0256 €) | — | 8.98 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 52904867 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 1.246273 WETH | 0.001113 WETH | 0.000000 WETH | 0.000004 WETH | 0.001109 WETH (2.5578 €) | — | 8.90 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1732 ; taux observé 0.099 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
