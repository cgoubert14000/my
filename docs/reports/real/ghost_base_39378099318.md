# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T09:51:36+00:00 ; durée 225.11 min ; blocs 52843518 → 52850268 (6597 vus)

## Connexion
- Requêtes RPC : 87151 ; erreurs : 40 ; latence p50/p95 : 182.7/1,892.7 ms
- Rafraîchissements d'état : 6598 ; âge des données au dernier bloc : 2.15 s ; changements de frais LP observés (pools à frais dynamiques) : 12346
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 63738 ; cycles déclenchés par événement : 4104 ; avance médiane sur le rafraîchissement multicall : 1,004 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,381.79 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 572 pools, 327 jetons, 21244 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 154, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 392, par paires 0), mesurés 574, sous le plancher de 10000.0 $ : 2 → gardés 572 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.704066, 'AERO': 0.805188, 'cbBTC': 81576.404653}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,634,146 | 2,381.791372 | 52850268 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 34,424,038 | 1.241752 | 52850268 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,253,287 | 98.498262 | 52850269 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,976,443 | 0.029249 | 52850268 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,202,325 | 0.029296 | 52850268 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,297,416 | 0.029310 | 52850268 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,874,286 | 0.000012 | 52850268 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,296,305 | 2,377.412166 | 52850268 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,273,136 | 2,381.947492 | 52850269 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 7,909,436 | 0.000012 | 52850268 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,808,058 | 0.000012 | 52850268 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,143,799 | 0.001666 | 52850268 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 564 | 7,092,149 | 2,377.613656 | 52850268 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,341,003 | 0.029242 | 52850268 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,972,293 | 0.025548 | 52850268 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,745,232 | 0.802395 | 52850268 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,594,308 | 0.000275 | 52850268 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,351,557 | 2,377.411892 | 52850268 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,315,453 | 0.998767 | 52850268 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,955,620 | 34,387.614289 | 52850268 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 412 | 3,835,372 | 2,380.894320 | 52850268 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,353,678 | 1.236545 | 52850268 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,237,293 | 2,963.221612 | 52850268 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,867,741 | 0.000012 | 52850268 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,725,055 | 1.142107 | 52850268 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,636,382 | 98.491907 | 52850268 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,614,001 | 400.846411 | 52850268 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,576,774 | 984.622909 | 52850268 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,172,975 | 1,219,622.054171 | 52850268 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,133,429 | 0.000010 | 52850268 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,059,548 | 1.237984 | 52850268 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,036,015 | 1.373598 | 52850268 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,924,585 | 0.000000 | 52850268 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,802,589 | 0.019145 | 52850268 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,764,998 | 0.000012 | 52850268 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,751,593 | 16.064564 | 52850268 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,723,325 | 1.105526 | 52850268 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | fBOMB/USDC | 10000 | 1,678,656 | 0.020336 | 52850268 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,654,199 | 13,691.291675 | 52850268 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,651,438 | 1.121805 | 52850268 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | WETH/msETH (stable) | 500 | 1,641,852 | 2.305920 | 52850268 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,613,030 | 2,950.937750 | 52850268 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,542,726 | 0.916342 | 52850268 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,802 | 0.826481 | 52850268 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,298,424 | 0.000000 | 52850268 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,296,367 | 0.004721 | 52850268 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,288,095 | 0.000276 | 52850268 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,281,422 | 0.029315 | 52850268 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,246,664 | 2,377.371154 | 52850268 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,674 | 63.537857 | 52850268 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/VVV | 8000 | 1,207,745 | 98.000729 | 52850268 | `0x46D398A5b33709877f50c8918A7eE96F1Be1d7dd` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,205,814 | 23.000192 | 52850268 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,184,467 | 35,493,293.966546 | 52850268 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,178,288 | 0.435505 | 52850268 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome | WETH/WELL | 10000 | 1,177,708 | 1,108,964.464311 | 52850268 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,153,473 | 1.131383 | 52850268 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | WETH/EDEL | 7000 | 1,143,976 | 74,794.895348 | 52850268 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,133,909 | 509,894.264808 | 52850268 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,116,204 | 50.572529 | 52850268 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,082,461 | 0.885313 | 52850268 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |

## Recherche d'opportunités
- Cycles : 10701 ; routes examinées : 227332044 ; candidats optimisés : 1274651 ; net attendu > 0 : 138 ; dernier cycle 260.3 ms
- Rejets (moteur) : {'spread_below_threshold': 223969373, 'liquidity_below_min': 1761071, 'negative_expected_net': 1274513, 'borrow_bound_too_small': 267500, 'pool_quarantined': 58800, 'cycle_budget_exhausted': 649}
- Enregistrements de la session : 1274651 ; net attendu > 0 : 138 ; simulés (eth_call de la vraie tx) : 23 (ok 6, échec 17) ; étiquettes ghost N+1 : 0/15 positives
- Décisions : {'REJECTED': 1274651} ; motifs de rejet : {'below_safety_margin': 95, 'negative_expected_net': 1274513, 'p_lower_below_threshold': 97, 'price_impact': 10, 'reliability_not_demonstrated': 41, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 17, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.041999 WETH | 0.000452 WETH | 0.000000 WETH | 0.000003 WETH | 0.000449 WETH (0.9838 €) | — | 106.83 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52849710 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 100.003701 USDC | 1.075489 USDC | 0.000000 USDC | 0.007161 USDC | 1.068328 USDC (0.9829 €) | — | 106.83 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.041877 WETH | 0.000448 WETH | 0.000000 WETH | 0.000003 WETH | 0.000445 WETH (0.9749 €) | — | 106.17 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52849710 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 99.727098 USDC | 1.065960 USDC | 0.000000 USDC | 0.007161 USDC | 1.058799 USDC (0.9741 €) | — | 106.17 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.039592 WETH | 0.000422 WETH | 0.000000 WETH | 0.000003 WETH | 0.000419 WETH (0.9198 €) | — | 105.95 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52849710 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 94.329563 USDC | 1.006579 USDC | 0.000000 USDC | 0.007161 USDC | 0.999418 USDC (0.9195 €) | — | 105.95 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.040103 WETH | 0.000417 WETH | 0.000000 WETH | 0.000003 WETH | 0.000414 WETH (0.9075 €) | — | 103.21 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 95.561051 USDC | 0.993439 USDC | 0.000000 USDC | 0.007161 USDC | 0.986278 USDC (0.9074 €) | — | 103.21 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.040077 WETH | 0.000415 WETH | 0.000000 WETH | 0.000003 WETH | 0.000412 WETH (0.9036 €) | — | 102.83 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 95.504048 USDC | 0.989201 USDC | 0.000000 USDC | 0.007161 USDC | 0.982040 USDC (0.9035 €) | — | 102.83 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 93.356130 USDC | 0.952799 USDC | 0.000000 USDC | 0.007523 USDC | 0.945276 USDC (0.8697 €) | — | 101.25 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.039152 WETH | 0.000400 WETH | 0.000000 WETH | 0.000003 WETH | 0.000396 WETH (0.8692 €) | — | 101.25 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 78.951845 USDC | 0.832385 USDC | 0.000000 USDC | 0.007884 USDC | 0.824501 USDC (0.7585 €) | — | 104.43 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.033013 WETH | 0.000348 WETH | 0.000000 WETH | 0.000003 WETH | 0.000345 WETH (0.7559 €) | — | 104.43 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 67.554460 USDC | 0.658530 USDC | 0.000000 USDC | 0.007161 USDC | 0.651369 USDC (0.5993 €) | — | 96.42 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.028260 WETH | 0.000275 WETH | 0.000000 WETH | 0.000003 WETH | 0.000272 WETH (0.5974 €) | — | 96.42 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[aerodrome]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 67.375470 USDC | 0.654108 USDC | 0.000000 USDC | 0.006832 USDC | 0.647276 USDC (0.5955 €) | — | 96.07 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.028183 WETH | 0.000274 WETH | 0.000000 WETH | 0.000003 WETH | 0.000271 WETH (0.5936 €) | — | 96.07 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[uniswap_v2]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 65.867126 USDC | 0.632158 USDC | 0.000000 USDC | 0.006421 USDC | 0.625737 USDC (0.5757 €) | — | 95.00 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v2]→WETH | 0.027539 WETH | 0.000264 WETH | 0.000000 WETH | 0.000003 WETH | 0.000262 WETH (0.5736 €) | — | 95.00 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52849710 | USDC→[aerodrome]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 39.673622 USDC | 0.395150 USDC | 0.000000 USDC | 0.006832 USDC | 0.388318 USDC (0.3573 €) | — | 97.88 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52849710 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome]→WETH | 0.016463 WETH | 0.000164 WETH | 0.000000 WETH | 0.000003 WETH | 0.000161 WETH (0.3532 €) | — | 97.86 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52849790 | WETH→[aerodrome_slipstream]→BRETT→[uniswap_v3]→WETH | 0.027808 WETH | 0.000034 WETH | 0.000000 WETH | 0.000002 WETH | 0.000031 WETH (0.0688 €) | — | 11.29 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52848456 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.590707 WETH | 0.000027 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0537 €) | — | 0.41 | 0.016 (n=52) | REJECTED | below_safety_margin(24476682940086<118141400154432), p_lower_below_threshold(0.02<0.75) |
| 52848456 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,404.469589 USDC | 0.063558 USDC | 0.000000 USDC | 0.005356 USDC | 0.058202 USDC (0.0535 €) | — | 0.41 | 0.016 (n=52) | REJECTED | below_safety_margin(58202<280893), p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 1403 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
