# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T21:19:04+00:00 ; durée 39.72 min ; blocs 52610504 → 52611697 (1161 vus)

## Connexion
- Requêtes RPC : 13309 ; erreurs : 0 ; latence p50/p95 : 94.2/1,981.7 ms
- Rafraîchissements d'état : 1161 ; âge des données au dernier bloc : 2.31 s ; changements de frais LP observés (pools à frais dynamiques) : 2272
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1 ; cycles déclenchés par événement : 1 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,409.38 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 327 jetons, 21784 routes
- Par DEX : uniswap_v3 139, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 33, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3920 (énumérés 394, par paires 0), mesurés 583, sous le plancher de 10000.0 $ : 3 → gardés 580 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2422.373052, 'AERO': 0.888199, 'cbBTC': 81793.071591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,553,744 | 2,409.384663 | 52611697 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 45,078,435 | 1.125802 | 52611697 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,746,366 | 0.029555 | 52611697 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,060,703 | 103.481272 | 52611697 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,959,555 | 0.029521 | 52611697 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,393,822 | 0.029535 | 52611697 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,203,841 | 0.000012 | 52611697 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,138,058 | 2,415.009357 | 52611697 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,930,147 | 2,409.633397 | 52611697 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 8,151,258 | 0.000012 | 52611697 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 698 | 8,103,986 | 2,415.273398 | 52611697 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,140,123 | 0.001661 | 52611697 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 6,760,011 | 0.000012 | 52611697 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/AERO | 10000 | 5,721,927 | 1.131133 | 52611697 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,400,772 | 0.029566 | 52611697 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,336,487 | 0.026706 | 52611697 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,321,590 | 1.000855 | 52611697 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,585,183 | 0.000279 | 52611697 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,531,456 | 0.802388 | 52611697 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,371,068 | 2,415.696887 | 52611697 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,101,850 | 1.000134 | 52611697 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,975,723 | 34,833.594207 | 52611697 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,621,101 | 2,738.053728 | 52611697 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,836,171 | 0.000012 | 52611697 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,693,034 | 403.976731 | 52611697 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,596,114 | 103.513959 | 52611697 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,564,796 | 1.141642 | 52611697 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,516,281 | 0.000011 | 52611697 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,400,312 | 1,025.794444 | 52611697 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/USDT | 436 | 2,353,330 | 2,418.574767 | 52611697 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/FAI | 10000 | 2,348,729 | 1,068,249.628419 | 52611697 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,113,860 | 1.193312 | 52611697 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,055,073 | 0.000000 | 52611697 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 1,966,009 | 0.023410 | 52611697 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,887,380 | 0.916706 | 52611697 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,842,475 | 15.692738 | 52611697 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,836,402 | 1.402356 | 52611697 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,388 | 0.019122 | 52611697 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,775,536 | 0.000012 | 52611697 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,681,688 | 13,681.713995 | 52611697 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/msETH (stable) | 500 | 1,616,916 | 2.303605 | 52611697 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,518,580 | 2,719.256450 | 52611697 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,489,645 | 1.105776 | 52611697 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,484 | 0.835124 | 52611697 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,370,453 | 0.000000 | 52611697 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,357,023 | 2,719.113949 | 52611697 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,349,572 | 0.004892 | 52611697 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,346,524 | 1.115088 | 52611697 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,311,463 | 0.000280 | 52611697 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,298,827 | 1.131012 | 52611697 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,274,090 | 23.296976 | 52611697 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/SEND | 3000 | 1,246,980 | 62.491890 | 52611697 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,240,606 | 2,415.038708 | 52611697 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,219,506 | 33,453,518.990405 | 52611697 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,201,774 | 1.105594 | 52611697 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,173,168 | 72,971.082894 | 52611697 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,156,533 | 488,691.317475 | 52611697 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,148,230 | 1,193,984.411649 | 52611697 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,136,479 | 13.558224 | 52611697 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,131,656 | 49.210301 | 52611697 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 1161 ; routes examinées : 25291224 ; candidats optimisés : 140697 ; net attendu > 0 : 201 ; dernier cycle 420.4 ms
- Rejets (moteur) : {'spread_below_threshold': 24848778, 'liquidity_below_min': 270061, 'negative_expected_net': 140496, 'borrow_bound_too_small': 29025, 'unquotable': 2322, 'cycle_budget_exhausted': 341}
- Enregistrements de la session : 140697 ; net attendu > 0 : 201 ; simulés (eth_call de la vraie tx) : 15 (ok 15, échec 0) ; étiquettes ghost N+1 : 3/12 positives
- Décisions : {'REJECTED': 140697} ; motifs de rejet : {'below_safety_margin': 68, 'negative_expected_net': 140496, 'reliability_not_demonstrated': 201, 'stale_data': 145}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52610694 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.207976 WETH | 0.000122 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2638 €) | 0.000118 WETH | 5.70 | 0.141 (n=26) | REJECTED | stale_data(4588ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006085 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2638 €) | — | 5.75 | 0.141 (n=26) | REJECTED | stale_data(4604ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 508.108618 USDC | 0.293288 USDC | 0.000000 USDC | 0.007687 USDC | 0.285601 USDC (0.2628 €) | — | 5.62 | 0.141 (n=26) | REJECTED | stale_data(4596ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.184295 WETH | 0.000095 WETH | 0.000000 WETH | 0.000002 WETH | 0.000092 WETH (0.2055 €) | 0.000092 WETH | 5.01 | 0.002 (n=3) | REJECTED | stale_data(4718ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.005276 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2050 €) | — | 5.16 | 0.002 (n=3) | REJECTED | stale_data(4723ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.178692 WETH | 0.000089 WETH | 0.000000 WETH | 0.000003 WETH | 0.000086 WETH (0.1920 €) | 0.000086 WETH | 4.83 | 0.439 (n=13) | REJECTED | stale_data(4730ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 444.021441 USDC | 0.216079 USDC | 0.000000 USDC | 0.007687 USDC | 0.208392 USDC (0.1917 €) | — | 4.69 | 0.439 (n=13) | REJECTED | stale_data(4738ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.005024 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1914 €) | — | 5.06 | 0.439 (n=13) | REJECTED | stale_data(4745ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.172133 WETH | 0.000074 WETH | 0.000000 WETH | 0.000002 WETH | 0.000072 WETH (0.1603 €) | — | 4.18 | 0.264 (n=6) | REJECTED | stale_data(4814ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→cbBTC | 0.004772 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1598 €) | — | 4.44 | 0.264 (n=6) | REJECTED | stale_data(4819ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.128075 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1366 €) | — | 4.79 | 0.439 (n=13) | REJECTED | stale_data(4674ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC | 0.003507 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1364 €) | — | 5.16 | 0.439 (n=13) | REJECTED | stale_data(4681ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→tBTC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.122579 WETH | 0.000064 WETH | 0.000000 WETH | 0.000003 WETH | 0.000061 WETH (0.1360 €) | — | 4.98 | 0.439 (n=13) | REJECTED | stale_data(4688ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→tBTC→[uniswap_v3]→cbBTC | 0.003399 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1357 €) | — | 5.30 | 0.439 (n=13) | REJECTED | stale_data(4695ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC | 0.003491 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1341 €) | — | 5.10 | 0.141 (n=26) | REJECTED | stale_data(4712ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[aerodrome_slipstream]→tBTC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.119080 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000060 WETH (0.1341 €) | — | 5.06 | 0.141 (n=26) | REJECTED | stale_data(4706ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.140146 WETH | 0.000060 WETH | 0.000000 WETH | 0.000003 WETH | 0.000057 WETH (0.1266 €) | — | 4.06 | 0.141 (n=26) | REJECTED | stale_data(4827ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003764 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1266 €) | — | 4.46 | 0.141 (n=26) | REJECTED | stale_data(4842ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 317.781783 USDC | 0.144866 USDC | 0.000000 USDC | 0.007687 USDC | 0.137179 USDC (0.1262 €) | — | 4.32 | 0.141 (n=26) | REJECTED | stale_data(4834ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[aerodrome_slipstream]→ZORA→[uniswap_v3]→USDC | 147.954389 USDC | 0.140518 USDC | 0.000000 USDC | 0.005840 USDC | 0.134678 USDC (0.1239 €) | — | 9.10 | 0.006 (n=1) | REJECTED | stale_data(4433ms>4000.0), reliability_not_demonstrated |
| 52610694 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003408 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0852 €) | — | 3.32 | 0.141 (n=26) | REJECTED | stale_data(5009ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.120186 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0850 €) | — | 3.18 | 0.141 (n=26) | REJECTED | stale_data(4991ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 280.870647 USDC | 0.100121 USDC | 0.000000 USDC | 0.008055 USDC | 0.092066 USDC (0.0847 €) | — | 3.28 | 0.141 (n=26) | REJECTED | stale_data(5000ms>4000.0), reliability_not_demonstrated |
| 52610694 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 261.831522 USDC | 0.095056 USDC | 0.000000 USDC | 0.007687 USDC | 0.087369 USDC (0.0804 €) | — | 3.34 | 0.439 (n=13) | REJECTED | stale_data(4974ms>4000.0), reliability_not_demonstrated |
| 52610694 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.110496 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0803 €) | — | 3.26 | 0.439 (n=13) | REJECTED | stale_data(4967ms>4000.0), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 193 ; taux observé 0.166 ; borne inférieure crédible (0.9) 0.134 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 13.4% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
