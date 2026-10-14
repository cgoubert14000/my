# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T21:59:13+00:00 ; durée 79.86 min ; blocs 52610504 → 52612901 (2340 vus)

## Connexion
- Requêtes RPC : 26670 ; erreurs : 0 ; latence p50/p95 : 77.6/1,858.2 ms
- Rafraîchissements d'état : 2341 ; âge des données au dernier bloc : 1.29 s ; changements de frais LP observés (pools à frais dynamiques) : 4236
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,420.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 327 jetons, 21784 routes
- Par DEX : uniswap_v3 139, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 33, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 394, par paires 0), mesurés 583, sous le plancher de 10000.0 $ : 3 → gardés 580 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2422.373052, 'AERO': 0.888199, 'cbBTC': 81793.071591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,031,663 | 2,420.114522 | 52612901 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,250,575 | 1.117305 | 52612901 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,824,230 | 0.029596 | 52612901 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,171,095 | 0.029578 | 52612901 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,119,379 | 103.646628 | 52612901 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,435,268 | 0.029564 | 52612901 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,220,543 | 0.000012 | 52612901 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,183,501 | 2,418.461124 | 52612901 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,951,623 | 2,420.444392 | 52612901 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 8,156,650 | 0.000012 | 52612901 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,376,628 | 2,418.175974 | 52612901 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,183,443 | 0.001671 | 52612901 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 7,130,494 | 0.000012 | 52612901 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,652,590 | 1.124788 | 52612901 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,398,184 | 0.029603 | 52612901 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,361,626 | 0.026688 | 52612901 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,345,289 | 1.000855 | 52612901 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,605,666 | 0.000279 | 52612901 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,551,636 | 0.802388 | 52612901 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,384,571 | 2,418.009572 | 52612901 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,114,379 | 1.000134 | 52612901 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,993,476 | 34,833.175576 | 52612901 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,642,606 | 2,720.795586 | 52612901 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,841,368 | 0.000012 | 52612901 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,646,400 | 0.000011 | 52612901 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,605,741 | 103.677951 | 52612901 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,576,221 | 1.141643 | 52612901 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,461,401 | 402.954873 | 52612901 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,359,189 | 1,068,249.628419 | 52612901 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 418 | 2,314,385 | 2,422.202825 | 52612901 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 2,146,372 | 1,026.582602 | 52612901 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,113,918 | 1.193280 | 52612901 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,064,398 | 0.000000 | 52612901 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 1,928,141 | 0.023451 | 52612901 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,895,786 | 0.916706 | 52612901 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,872,498 | 15.730712 | 52612901 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,836,402 | 1.402356 | 52612901 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,781,989 | 0.019050 | 52612901 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,778,691 | 0.000012 | 52612901 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,764,824 | 13,616.334103 | 52612901 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,623,807 | 2.304462 | 52612901 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,525,747 | 2,701.030097 | 52612901 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,496,278 | 1.105776 | 52612901 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,472 | 0.835136 | 52612901 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,375,787 | 0.000000 | 52612901 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3064 | 1,364,792 | 2,701.864157 | 52612901 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,360,042 | 0.004877 | 52612901 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,328,337 | 1.115183 | 52612901 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,317,356 | 0.000279 | 52612901 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,291,412 | 1.131111 | 52612901 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,251,873 | 23.266481 | 52612901 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,246,910 | 62.498926 | 52612901 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,244,701 | 2,418.425057 | 52612901 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,224,639 | 33,453,518.990405 | 52612901 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,207,126 | 1.105594 | 52612901 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,179,589 | 72,823.120493 | 52612901 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,162,704 | 487,549.578499 | 52612901 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,155,338 | 1,189,866.155804 | 52612901 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,137,590 | 13.525719 | 52612901 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,133,631 | 49.038126 | 52612901 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 2341 ; routes examinées : 50996344 ; candidats optimisés : 312891 ; net attendu > 0 : 298 ; dernier cycle 591.4 ms
- Rejets (moteur) : {'spread_below_threshold': 50083744, 'liquidity_below_min': 535766, 'negative_expected_net': 312593, 'borrow_bound_too_small': 58525, 'unquotable': 4682, 'cycle_budget_exhausted': 736}
- Enregistrements de la session : 312891 ; net attendu > 0 : 298 ; simulés (eth_call de la vraie tx) : 24 (ok 24, échec 0) ; étiquettes ghost N+1 : 3/21 positives
- Décisions : {'REJECTED': 312891} ; motifs de rejet : {'below_safety_margin': 93, 'negative_expected_net': 312593, 'reliability_not_demonstrated': 298, 'stale_data': 145}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52612307 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 247.423503 USDC | 0.516122 USDC | 0.000000 USDC | 0.007297 USDC | 0.508825 USDC (0.4681 €) | — | 20.56 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.102067 WETH | 0.000213 WETH | 0.000000 WETH | 0.000003 WETH | 0.000210 WETH (0.4674 €) | 0.000210 WETH | 20.57 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.101336 WETH | 0.000209 WETH | 0.000000 WETH | 0.000002 WETH | 0.000207 WETH (0.4606 €) | 0.000207 WETH | 20.41 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 244.664949 USDC | 0.504785 USDC | 0.000000 USDC | 0.007297 USDC | 0.497488 USDC (0.4577 €) | — | 20.33 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.100987 WETH | 0.000208 WETH | 0.000000 WETH | 0.000003 WETH | 0.000205 WETH (0.4569 €) | 0.000205 WETH | 20.32 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 238.348501 USDC | 0.490795 USDC | 0.000000 USDC | 0.007297 USDC | 0.483498 USDC (0.4448 €) | — | 20.29 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 240.688237 USDC | 0.490426 USDC | 0.000000 USDC | 0.007297 USDC | 0.483129 USDC (0.4445 €) | — | 20.07 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.098292 WETH | 0.000203 WETH | 0.000000 WETH | 0.000003 WETH | 0.000199 WETH (0.4442 €) | — | 20.30 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.099311 WETH | 0.000202 WETH | 0.000000 WETH | 0.000003 WETH | 0.000199 WETH (0.4438 €) | — | 20.07 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 238.460396 USDC | 0.483737 USDC | 0.000000 USDC | 0.007297 USDC | 0.476440 USDC (0.4383 €) | — | 19.98 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.098451 WETH | 0.000200 WETH | 0.000000 WETH | 0.000003 WETH | 0.000197 WETH (0.4377 €) | — | 19.97 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 235.142968 USDC | 0.479906 USDC | 0.000000 USDC | 0.007297 USDC | 0.472609 USDC (0.4348 €) | — | 20.10 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.097173 WETH | 0.000198 WETH | 0.000000 WETH | 0.000003 WETH | 0.000195 WETH (0.4342 €) | — | 20.07 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 235.647098 USDC | 0.472833 USDC | 0.000000 USDC | 0.007297 USDC | 0.465536 USDC (0.4283 €) | — | 19.76 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.097288 WETH | 0.000195 WETH | 0.000000 WETH | 0.000003 WETH | 0.000192 WETH (0.4277 €) | — | 19.74 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 231.325423 USDC | 0.466178 USDC | 0.000000 USDC | 0.007297 USDC | 0.458881 USDC (0.4222 €) | — | 19.84 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.095416 WETH | 0.000192 WETH | 0.000000 WETH | 0.000003 WETH | 0.000189 WETH (0.4215 €) | — | 19.84 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 231.655119 USDC | 0.459086 USDC | 0.000000 USDC | 0.007297 USDC | 0.451789 USDC (0.4156 €) | — | 19.50 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.095695 WETH | 0.000189 WETH | 0.000000 WETH | 0.000003 WETH | 0.000186 WETH (0.4150 €) | — | 19.48 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 230.462854 USDC | 0.445992 USDC | 0.000000 USDC | 0.007297 USDC | 0.438695 USDC (0.4036 €) | — | 19.04 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.095115 WETH | 0.000184 WETH | 0.000000 WETH | 0.000003 WETH | 0.000181 WETH (0.4031 €) | — | 19.03 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 227.694736 USDC | 0.435463 USDC | 0.000000 USDC | 0.007297 USDC | 0.428166 USDC (0.3939 €) | — | 18.80 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.094134 WETH | 0.000180 WETH | 0.000000 WETH | 0.000003 WETH | 0.000177 WETH (0.3934 €) | — | 18.77 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52612307 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 223.606122 USDC | 0.422248 USDC | 0.000000 USDC | 0.007297 USDC | 0.414951 USDC (0.3818 €) | — | 18.56 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 52612307 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.092439 WETH | 0.000174 WETH | 0.000000 WETH | 0.000003 WETH | 0.000171 WETH (0.3812 €) | — | 18.52 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 202 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.128 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
