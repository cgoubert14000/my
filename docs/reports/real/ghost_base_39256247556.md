# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-19T17:30:35+00:00 ; durée 267.19 min ; blocs 52812825 → 52820838 (7480 vus)

## Connexion
- Requêtes RPC : 102095 ; erreurs : 211 ; latence p50/p95 : 104.9/661.7 ms
- Rafraîchissements d'état : 7481 ; âge des données au dernier bloc : 1.73 s ; changements de frais LP observés (pools à frais dynamiques) : 22271
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 160284 ; cycles déclenchés par événement : 7109 ; avance médiane sur le rafraîchissement multicall : 533 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,396.43 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 571 pools, 327 jetons, 21004 routes
- Par DEX : uniswap_v3 137, aerodrome 234, aerodrome_slipstream 153, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 390, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 3 → gardés 571 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2419.85313, 'AERO': 0.782295, 'cbBTC': 82567.067054}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,379,530 | 2,396.428554 | 52820838 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 35,186,445 | 1.277117 | 52820838 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,878,690 | 0.029275 | 52820838 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,210,684 | 0.029294 | 52820838 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,212,584 | 100.268205 | 52820838 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,349,103 | 0.029287 | 52820838 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,855,468 | 0.000012 | 52820838 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,354,048 | 2,397.972230 | 52820838 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,300,134 | 2,396.748865 | 52820838 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 7,813,397 | 0.000012 | 52820838 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 7,629,157 | 0.000012 | 52820838 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,157,249 | 0.001657 | 52820838 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 7,003,554 | 2,397.234841 | 52820838 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,333,175 | 0.029283 | 52820838 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,883,272 | 0.025997 | 52820838 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,789,723 | 0.802395 | 52820838 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,750,665 | 1.286154 | 52820838 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,597,950 | 0.000272 | 52820838 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,397,193 | 2,396.823574 | 52820838 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,334,925 | 0.998769 | 52820838 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,012,639 | 33,829.269782 | 52820838 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 433 | 3,690,947 | 2,401.434468 | 52820838 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,219,711 | 3,088.703624 | 52820838 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,849,704 | 0.000012 | 52820838 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,696,381 | 1.142232 | 52820838 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,625,664 | 100.298974 | 52820838 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,355,402 | 404.774170 | 52820838 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,180,326 | 1,226,346.894757 | 52820838 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,126,555 | 0.000010 | 52820838 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,139 | 1.238201 | 52820838 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,743 | 1.372638 | 52820838 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 2,032,788 | 957.651828 | 52820838 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,025,698 | 0.000000 | 52820838 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,844,091 | 16.142459 | 52820838 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,515 | 0.019106 | 52820838 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,776,914 | 0.000012 | 52820838 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,732,297 | 1.105525 | 52820838 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,708,873 | 0.020172 | 52820838 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,658,428 | 2.306958 | 52820838 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,552,189 | 0.916350 | 52820838 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,493,226 | 3,068.261297 | 52820838 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,600 | 0.827499 | 52820838 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,406,427 | 1.121440 | 52820838 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,402,928 | 13,804.918517 | 52820838 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,338,162 | 0.435660 | 52820838 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,312,481 | 0.000000 | 52820838 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,301,580 | 0.004683 | 52820838 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,288,862 | 0.000274 | 52820838 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,278,774 | 0.029283 | 52820838 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,262,866 | 23.118247 | 52820838 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,232,669 | 63.951404 | 52820838 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,218,250 | 2,398.005235 | 52820838 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,196,280 | 1,088,037.367025 | 52820838 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,194,372 | 35,229,025.158531 | 52820838 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,131,372 | 1.131619 | 52820838 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,127,688 | 515,481.870232 | 52820838 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,108,460 | 51.281669 | 52820838 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,084,488 | 0.885473 | 52820838 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,074,654 | 15.614538 | 52820838 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,054,178 | 89,014.343891 | 52820838 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |

## Recherche d'opportunités
- Cycles : 14589 ; routes examinées : 306427356 ; candidats optimisés : 1940374 ; net attendu > 0 : 1049 ; dernier cycle 284.9 ms
- Rejets (moteur) : {'spread_below_threshold': 301198886, 'liquidity_below_min': 2687742, 'negative_expected_net': 1939325, 'borrow_bound_too_small': 314459, 'pool_quarantined': 220376, 'cycle_budget_exhausted': 65519}
- Enregistrements de la session : 1940374 ; net attendu > 0 : 1049 ; simulés (eth_call de la vraie tx) : 97 (ok 37, échec 60) ; étiquettes ghost N+1 : 7/63 positives
- Décisions : {'REJECTED': 1940374} ; motifs de rejet : {'below_safety_margin': 760, 'negative_expected_net': 1939325, 'p_lower_below_threshold': 850, 'price_impact': 30, 'reliability_not_demonstrated': 199, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 3, 'simulation_failed': 60, 'stale_data': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52820655 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 728.408226 USDC | 0.928399 USDC | 0.000000 USDC | 0.007597 USDC | 0.920802 USDC (0.8471 €) | — | 12.64 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 52820655 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.303636 WETH | 0.000387 WETH | 0.000000 WETH | 0.000003 WETH | 0.000384 WETH (0.8459 €) | — | 12.64 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52820655 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 623.045354 USDC | 0.767997 USDC | 0.000000 USDC | 0.008324 USDC | 0.759673 USDC (0.6989 €) | — | 12.19 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 52820655 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.259850 WETH | 0.000320 WETH | 0.000000 WETH | 0.000003 WETH | 0.000316 WETH (0.6976 €) | — | 12.18 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52819356 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.235640 WETH | 0.000256 WETH | 0.000000 WETH | 0.000002 WETH | 0.000254 WETH (0.5590 €) | — | 10.76 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52820655 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 568.320920 USDC | 0.556241 USDC | 0.000000 USDC | 0.007233 USDC | 0.549008 USDC (0.5051 €) | — | 9.66 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 52820655 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.236824 WETH | 0.000232 WETH | 0.000000 WETH | 0.000003 WETH | 0.000229 WETH (0.5041 €) | — | 9.65 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52819356 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.216679 WETH | 0.000204 WETH | 0.000000 WETH | 0.000002 WETH | 0.000202 WETH (0.4445 €) | — | 9.31 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52820655 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 493.877971 USDC | 0.422869 USDC | 0.000000 USDC | 0.007233 USDC | 0.415636 USDC (0.3824 €) | — | 8.42 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 52820655 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.205864 WETH | 0.000176 WETH | 0.000000 WETH | 0.000003 WETH | 0.000173 WETH (0.3815 €) | — | 8.41 | 0.000 (n=19) | REJECTED | reliability_not_demonstrated |
| 52820655 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 472.713969 USDC | 0.400416 USDC | 0.000000 USDC | 0.007233 USDC | 0.393183 USDC (0.3617 €) | — | 8.32 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 52820655 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.196925 WETH | 0.000167 WETH | 0.000000 WETH | 0.000003 WETH | 0.000164 WETH (0.3609 €) | — | 8.31 | 0.000 (n=22) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.194512 WETH | 0.000153 WETH | 0.000000 WETH | 0.000002 WETH | 0.000151 WETH (0.3320 €) | — | 7.74 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52817668 | WETH→[aerodrome]→TEVA→[uniswap_v3]→WETH | 0.024385 WETH | 0.000112 WETH | 0.000000 WETH | 0.000002 WETH | 0.000110 WETH (0.2433 €) | — | 45.10 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52819356 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 231.591617 USDC | 0.188676 USDC | 0.000000 USDC | 0.006480 USDC | 0.182196 USDC (0.1676 €) | — | 7.87 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.096802 WETH | 0.000079 WETH | 0.000000 WETH | 0.000003 WETH | 0.000076 WETH (0.1674 €) | — | 7.85 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52815901 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,462.225373 USDC | 0.173380 USDC | 0.000000 USDC | 0.007902 USDC | 0.165478 USDC (0.1522 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(165478<292445), p_lower_below_threshold(0.12<0.75) |
| 52815901 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.607861 WETH | 0.000072 WETH | 0.000000 WETH | 0.000003 WETH | 0.000069 WETH (0.1518 €) | — | 1.13 | 0.117 (n=152) | REJECTED | below_safety_margin(68791946207429<121572211358974), p_lower_below_threshold(0.12<0.75) |
| 52819356 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 213.125629 USDC | 0.169874 USDC | 0.000000 USDC | 0.006480 USDC | 0.163394 USDC (0.1503 €) | — | 7.67 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52819356 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.089001 WETH | 0.000071 WETH | 0.000000 WETH | 0.000003 WETH | 0.000068 WETH (0.1501 €) | — | 7.65 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52815204 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,735.428521 USDC | 0.154603 USDC | 0.000000 USDC | 0.006144 USDC | 0.148459 USDC (0.1366 €) | — | 0.86 | 0.017 (n=49) | REJECTED | below_safety_margin(148459<347085), p_lower_below_threshold(0.02<0.75) |
| 52815204 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.726513 WETH | 0.000065 WETH | 0.000000 WETH | 0.000003 WETH | 0.000062 WETH (0.1365 €) | — | 0.85 | 0.017 (n=49) | REJECTED | below_safety_margin(61999402150527<145302574799060), p_lower_below_threshold(0.02<0.75) |
| 52820655 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 189.366811 USDC | 0.149721 USDC | 0.000000 USDC | 0.007597 USDC | 0.142124 USDC (0.1308 €) | — | 7.51 | 0.139 (n=67) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52820655 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.078908 WETH | 0.000062 WETH | 0.000000 WETH | 0.000003 WETH | 0.000059 WETH (0.1303 €) | — | 7.49 | 0.139 (n=67) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52819147 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 226.046893 USDC | 0.145848 USDC | 0.000000 USDC | 0.007233 USDC | 0.138615 USDC (0.1275 €) | — | 6.13 | 0.120 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1333 ; taux observé 0.104 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
