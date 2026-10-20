# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T05:24:44+00:00 ; durée 294.07 min ; blocs 52833443 → 52842261 (8558 vus)

## Connexion
- Requêtes RPC : 120216 ; erreurs : 125 ; latence p50/p95 : 197.9/688.9 ms
- Rafraîchissements d'état : 8559 ; âge des données au dernier bloc : 1.87 s ; changements de frais LP observés (pools à frais dynamiques) : 17677
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 158745 ; cycles déclenchés par événement : 10358 ; avance médiane sur le rafraîchissement multicall : 338 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,407.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21078 routes
- Par DEX : uniswap_v3 136, aerodrome 234, aerodrome_slipstream 155, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 391, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 3 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.875305, 'AERO': 0.785623, 'cbBTC': 81488.469771}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,607,638 | 2,407.762722 | 52842261 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,487,112 | 1.237147 | 52842261 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,229,760 | 0.029377 | 52842261 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 17,506,967 | 97.761011 | 52842261 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,428,831 | 0.029339 | 52842261 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,396,312 | 0.029323 | 52842261 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,884,731 | 0.000012 | 52842261 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,369,250 | 2,406.335246 | 52842261 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,318,086 | 2,408.852862 | 52842261 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,832,892 | 0.000012 | 52842261 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 579 | 7,828,628 | 2,406.543525 | 52842261 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,203,310 | 0.001672 | 52842261 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 6,672,415 | 0.000012 | 52842261 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,359,835 | 0.029372 | 52842261 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,981,099 | 0.025575 | 52842261 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,796,974 | 0.802395 | 52842261 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,644,297 | 0.000275 | 52842261 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,482,160 | 2,406.358669 | 52842261 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDT | 409 | 4,440,498 | 2,409.876096 | 52842261 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,343,383 | 0.998768 | 52842261 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,336,805 | 1.238258 | 52842261 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/KTA | 3000 | 4,030,201 | 33,853.039059 | 52842261 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,260,924 | 2,982.765937 | 52842261 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,878,796 | 0.000012 | 52842261 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,754,763 | 1.142104 | 52842261 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,666,844 | 97.786731 | 52842261 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,548,790 | 399.936911 | 52842261 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,354,448 | 0.000010 | 52842261 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,193,499 | 1,223,150.560610 | 52842261 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,504 | 1.238011 | 52842261 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52842261 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,977,362 | 0.000000 | 52842261 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,975,847 | 15.940294 | 52842261 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 1,828,423 | 976.844120 | 52842261 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | XDP/USDC | 100 | 1,801,241 | 0.019222 | 52842261 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,771,329 | 0.000012 | 52842261 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,755,175 | 13,604.929473 | 52842261 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | weETH_04c0/WETH | 500 | 1,742,093 | 1.105525 | 52842261 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,088 | 0.020332 | 52842261 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,673,689 | 1.123374 | 52842261 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/msETH (stable) | 500 | 1,658,774 | 2.307691 | 52842261 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,559,546 | 0.916343 | 52842261 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,514,155 | 2,973.863704 | 52842261 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,795 | 0.826442 | 52842261 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,309,289 | 0.000000 | 52842261 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,306,117 | 0.004702 | 52842261 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,302,090 | 0.000276 | 52842261 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,286,989 | 0.029321 | 52842261 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,250,912 | 2,406.385783 | 52842261 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,230,445 | 64.182807 | 52842261 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/WELL | 10000 | 1,221,716 | 1,053,105.100363 | 52842261 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,207,206 | 22.983009 | 52842261 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,198,205 | 35,425,939.067534 | 52842261 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,168,390 | 0.436011 | 52842261 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,142,553 | 517,350.485364 | 52842261 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,136,012 | 0.885710 | 52842261 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,120,802 | 50.158464 | 52842261 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,115,113 | 1.131792 | 52842261 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,090,570 | 84,092.880788 | 52842261 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,076,145 | 15.571240 | 52842261 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 18916 ; routes examinées : 398711448 ; candidats optimisés : 2289988 ; net attendu > 0 : 707 ; dernier cycle 215.4 ms
- Rejets (moteur) : {'spread_below_threshold': 392701766, 'liquidity_below_min': 3151839, 'negative_expected_net': 2289281, 'borrow_bound_too_small': 472866, 'pool_quarantined': 91780, 'cycle_budget_exhausted': 3209}
- Enregistrements de la session : 2289988 ; net attendu > 0 : 707 ; simulés (eth_call de la vraie tx) : 59 (ok 17, échec 42) ; étiquettes ghost N+1 : 3/44 positives
- Décisions : {'REJECTED': 2289988} ; motifs de rejet : {'below_safety_margin': 426, 'negative_expected_net': 2289281, 'p_lower_below_threshold': 498, 'price_impact': 16, 'reliability_not_demonstrated': 209, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 42, 'stale_data': 25}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52841421 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 89.889229 USDC | 4.512221 USDC | 0.000000 USDC | 0.006913 USDC | 4.505308 USDC (4.1449 €) | — | 501.21 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52841421 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.037284 WETH | 0.001872 WETH | 0.000000 WETH | 0.000003 WETH | 0.001869 WETH (4.1395 €) | — | 501.21 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52841421 | WETH→[uniswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.036920 WETH | 0.001815 WETH | 0.000000 WETH | 0.000003 WETH | 0.001812 WETH (4.0137 €) | — | 490.77 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52841421 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 88.874307 USDC | 4.368596 USDC | 0.000000 USDC | 0.006913 USDC | 4.361683 USDC (4.0127 €) | — | 490.77 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52841421 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 70.961389 USDC | 3.526978 USDC | 0.000000 USDC | 0.006913 USDC | 3.520065 USDC (3.2385 €) | — | 496.05 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52841421 | WETH→[uniswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.029459 WETH | 0.001464 WETH | 0.000000 WETH | 0.000003 WETH | 0.001461 WETH (3.2370 €) | — | 496.05 | 0.002 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52841421 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 70.759201 USDC | 3.521423 USDC | 0.000000 USDC | 0.006913 USDC | 3.514510 USDC (3.2333 €) | — | 496.69 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52841421 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.029377 WETH | 0.001462 WETH | 0.000000 WETH | 0.000003 WETH | 0.001459 WETH (3.2321 €) | — | 496.69 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52841421 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 64.393481 USDC | 3.227357 USDC | 0.000000 USDC | 0.006913 USDC | 3.220444 USDC (2.9628 €) | — | 500.12 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52841421 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.026725 WETH | 0.001339 WETH | 0.000000 WETH | 0.000003 WETH | 0.001337 WETH (2.9607 €) | — | 500.12 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52841421 | WETH→[sushiswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.026454 WETH | 0.001312 WETH | 0.000000 WETH | 0.000003 WETH | 0.001309 WETH (2.8998 €) | — | 494.86 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52841421 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 63.385082 USDC | 3.143567 USDC | 0.000000 USDC | 0.006913 USDC | 3.136654 USDC (2.8857 €) | — | 494.86 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52841421 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.016641 WETH | 0.000833 WETH | 0.000000 WETH | 0.000003 WETH | 0.000831 WETH (1.8398 €) | — | 499.10 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52841421 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 38.985290 USDC | 1.952500 USDC | 0.000000 USDC | 0.006913 USDC | 1.945587 USDC (1.7899 €) | — | 499.06 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 52837704 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,357.403929 USDC | 1.618250 USDC | 0.000000 USDC | 0.007212 USDC | 1.611038 USDC (1.4822 €) | — | 6.83 | 0.000 (n=88) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.983362 WETH | 0.000675 WETH | 0.000000 WETH | 0.000003 WETH | 0.000672 WETH (1.4812 €) | — | 6.83 | 0.000 (n=88) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52842165 | WETH→[aerodrome_slipstream]→VIRTUAL→[uniswap_v2]→WETH | 0.370633 WETH | 0.000632 WETH | 0.000000 WETH | 0.000002 WETH | 0.000630 WETH (1.3952 €) | — | 16.99 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52842165 | WETH→[uniswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.347585 WETH | 0.000523 WETH | 0.000000 WETH | 0.000002 WETH | 0.000521 WETH (1.1543 €) | — | 14.99 | 0.002 (n=3) | REJECTED | stale_data(13687ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52837704 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,960.783478 USDC | 1.243120 USDC | 0.000000 USDC | 0.009035 USDC | 1.234085 USDC (1.1354 €) | — | 6.29 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52837704 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.826484 WETH | 0.000518 WETH | 0.000000 WETH | 0.000004 WETH | 0.000515 WETH (1.1345 €) | — | 6.23 | 0.115 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 52837704 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.023970 cbBTC | 0.000015 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000015 cbBTC (1.1341 €) | — | 6.30 | 0.115 (n=117) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 281.209092 USDC | 0.969297 USDC | 0.000000 USDC | 0.009435 USDC | 0.959862 USDC (0.8831 €) | — | 34.13 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.116721 WETH | 0.000402 WETH | 0.000000 WETH | 0.000004 WETH | 0.000398 WETH (0.8810 €) | — | 34.12 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52839614 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 276.030520 USDC | 0.950791 USDC | 0.000000 USDC | 0.009435 USDC | 0.941356 USDC (0.8660 €) | — | 34.10 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52839614 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.114583 WETH | 0.000395 WETH | 0.000000 WETH | 0.000004 WETH | 0.000391 WETH (0.8641 €) | — | 34.09 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1380 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.092 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.2% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
