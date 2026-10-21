# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T21:00:11+00:00 ; durée 296.83 min ; blocs 52904622 → 52913527 (8734 vus)

## Connexion
- Requêtes RPC : 108828 ; erreurs : 35 ; latence p50/p95 : 306.3/1,076.7 ms
- Rafraîchissements d'état : 8734 ; âge des données au dernier bloc : 2.17 s ; changements de frais LP observés (pools à frais dynamiques) : 17851
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44757 ; cycles déclenchés par événement : 2376 ; avance médiane sur le rafraîchissement multicall : 510 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,491.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 578 pools, 327 jetons, 21568 routes
- Par DEX : uniswap_v3 138, aerodrome 236 (quarantaine 1), aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3876 (énumérés 394, par paires 0), mesurés 580, sous le plancher de 10000.0 $ : 2 → gardés 578 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2506.228815, 'AERO': 0.862155, 'cbBTC': 84485.636227}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52913618

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,035,407 | 2,491.079425 | 52913527 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,657,827 | 1.203598 | 52913527 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,023,244 | 92.220751 | 52913527 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,713,037 | 0.029433 | 52913527 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 14,238,598 | 0.029493 | 52913527 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,625,586 | 0.029507 | 52913527 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,922,640 | 0.000012 | 52913527 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,871,504 | 2,490.977255 | 52913527 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,427,979 | 2,491.478021 | 52913527 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/USDC | 594 | 8,209,419 | 2,490.594016 | 52913527 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,430,756 | 0.000012 | 52913527 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,426,312 | 0.001667 | 52913527 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 7,288,694 | 0.000012 | 52913527 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,685,208 | 0.029431 | 52913527 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDT | 409 | 5,161,958 | 2,493.446943 | 52913527 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | fBOMB/AERO | 10000 | 4,893,696 | 0.023182 | 52913527 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,595,844 | 2,490.801868 | 52913527 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,455,857 | 0.999949 | 52913527 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,250,430 | 0.000278 | 52913527 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/KTA | 3000 | 4,132,040 | 34,471.026627 | 52913527 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,722,224 | 1.195196 | 52913527 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,346,465 | 2,977.954242 | 52913527 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/wstETH | 90 | 3,015,114 | 0.802245 | 52913527 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,860,957 | 92.195827 | 52913527 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,670,802 | 390.656668 | 52913527 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,306,047 | 1,041.270829 | 52913527 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,293,911 | 1,196,489.382095 | 52913527 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,282,588 | 0.915907 | 52913527 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,280,761 | 0.000012 | 52913527 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,114,793 | 0.000010 | 52913527 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,112,628 | 0.000012 | 52913527 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,030,750 | 1.383527 | 52913527 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,963,690 | 0.000000 | 52913527 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,940,698 | 1.105712 | 52913527 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,834,156 | 15.830132 | 52913527 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,827,759 | 0.019094 | 52913527 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,717,032 | 2.310661 | 52913527 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,709,116 | 1.492742 | 52913527 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,685,978 | 2,999.099717 | 52913527 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,650,324 | 13,259.896611 | 52913527 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,571,597 | 1.142105 | 52913527 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,821 | 0.826523 | 52913527 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,428,537 | 1.123501 | 52913527 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | fBOMB/USDC | 10000 | 1,407,352 | 0.019796 | 52913527 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,397,002 | 0.004892 | 52913527 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,384,819 | 0.000000 | 52913527 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,355,837 | 0.000280 | 52913527 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,336,040 | 0.029508 | 52913527 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,304,761 | 2,491.016206 | 52913527 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,277,494 | 23.100308 | 52913527 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/WELL | 10000 | 1,255,221 | 1,067,799.760765 | 52913527 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,242,821 | 35,070,849.039555 | 52913527 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/NOCK | 3000 | 1,233,577 | 41.407074 | 52913527 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | USDC/SEND | 3000 | 1,232,678 | 63.950408 | 52913527 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,215,197 | 71,939.261062 | 52913527 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,207,282 | 485,402.667813 | 52913527 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,175,617 | 0.436598 | 52913527 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,149,378 | 0.886163 | 52913527 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,142,613 | 1.106154 | 52913527 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,117,560 | 20,907,427.211674 | 52913527 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 11109 ; routes examinées : 239598912 ; candidats optimisés : 1370101 ; net attendu > 0 : 299 ; dernier cycle 298.6 ms
- Rejets (moteur) : {'spread_below_threshold': 236054137, 'liquidity_below_min': 2025894, 'negative_expected_net': 1369802, 'pool_quarantined': 133762, 'borrow_bound_too_small': 11093, 'cycle_budget_exhausted': 3906, 'unquotable': 19}
- Enregistrements de la session : 1370101 ; net attendu > 0 : 299 ; simulés (eth_call de la vraie tx) : 47 (ok 18, échec 29) ; étiquettes ghost N+1 : 2/34 positives
- Décisions : {'REJECTED': 1370101} ; motifs de rejet : {'below_safety_margin': 186, 'negative_expected_net': 1369802, 'p_lower_below_threshold': 225, 'price_impact': 30, 'reliability_not_demonstrated': 74, 'simulation_failed': 29, 'stale_data': 10}

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
- Observations ghost : 1743 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
