# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-14T13:59:58+00:00 ; durée 273.67 min ; blocs 52590312 → 52598518 (8071 vus)

## Connexion
- Requêtes RPC : 108073 ; erreurs : 5 ; latence p50/p95 : 288.2/922.2 ms
- Rafraîchissements d'état : 8071 ; âge des données au dernier bloc : 3.4 s ; changements de frais LP observés (pools à frais dynamiques) : 20616
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 233333 ; cycles déclenchés par événement : 9023 ; avance médiane sur le rafraîchissement multicall : 901 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,460.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 584 pools, 329 jetons, 21950 routes
- Par DEX : uniswap_v3 142, aerodrome 236, aerodrome_slipstream 157, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3924 (énumérés 395, par paires 0), mesurés 586, sous le plancher de 10000.0 $ : 2 → gardés 584 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2506.12853, 'AERO': 0.905993, 'cbBTC': 83225.723803}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,520,995 | 2,460.423945 | 52598519 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 41,130,741 | 1.149063 | 52598519 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,069,074 | 0.029806 | 52598519 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,991,747 | 108.837327 | 52598519 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2545 | 12,103,540 | 0.029866 | 52598519 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,574,760 | 0.029879 | 52598519 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 9,294,524 | 2,454.399844 | 52598519 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,270,105 | 0.000012 | 52598519 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/USDC | 3000 | 9,024,091 | 2,460.373257 | 52598519 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 394 | 8,106,392 | 0.000012 | 52598519 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 1205 | 7,259,065 | 2,454.148993 | 52598519 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,236,058 | 0.001664 | 52598519 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,405,512 | 0.000012 | 52598519 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,480,268 | 0.029795 | 52598519 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,434,291 | 1.000859 | 52598519 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome | fBOMB/AERO | 10000 | 5,255,634 | 0.026542 | 52598519 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,676,195 | 0.000278 | 52598519 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,640,249 | 0.802388 | 52598519 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,444,635 | 2,453.413100 | 52598519 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,381,966 | 0.998943 | 52598519 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,053,470 | 34,944.922767 | 52598519 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,622,004 | 2,804.243574 | 52598519 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,976,897 | 1.141638 | 52598519 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,855,074 | 0.000012 | 52598519 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,603,628 | 0.000011 | 52598519 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,577,351 | 108.877595 | 52598519 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,567,644 | 408.107301 | 52598519 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,477,370 | 1,067.884468 | 52598519 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/FAI | 10000 | 2,407,778 | 1,060,017.930553 | 52598519 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 532 | 2,264,598 | 2,458.754500 | 52598519 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,116,951 | 1.189914 | 52598519 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,107,526 | 0.000000 | 52598519 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDbC | 10000 | 2,018,466 | 0.023569 | 52598519 | `0xC395664B295ed5bf1D249Ae8be9740655AA174ef` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,927,359 | 0.916707 | 52598519 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,866,123 | 15.686941 | 52598519 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,849,637 | 1.385043 | 52598519 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,830,331 | 1.141083 | 52598519 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,496 | 0.018911 | 52598519 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,759,911 | 0.000012 | 52598519 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/msETH (stable) | 500 | 1,649,632 | 2.306277 | 52598519 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,529,150 | 2,823.138762 | 52598519 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,521,200 | 1.105776 | 52598519 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,752 | 0.833455 | 52598519 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,436,184 | 0.000000 | 52598519 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,423,678 | 13,678.534916 | 52598519 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,373,516 | 0.000277 | 52598519 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,363,072 | 0.004827 | 52598519 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,354,553 | 2,823.136767 | 52598519 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | EURC/USDC | 76 | 1,299,917 | 1.112080 | 52598519 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,285,401 | 2,454.395442 | 52598519 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,275,160 | 23.436881 | 52598519 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,251,276 | 33,062,803.516959 | 52598519 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,247,371 | 62.452741 | 52598519 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,218,818 | 1.105594 | 52598519 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,193,688 | 73,289.186429 | 52598519 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,183,600 | 1.131453 | 52598519 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,182,669 | 486,874.868972 | 52598519 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/WELL | 10000 | 1,172,439 | 1,194,203.587382 | 52598519 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,166,033 | 12.765428 | 52598519 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,160,854 | 46.766340 | 52598519 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |

## Recherche d'opportunités
- Cycles : 17093 ; routes examinées : 375191350 ; candidats optimisés : 2095869 ; net attendu > 0 : 3159 ; dernier cycle 357.9 ms
- Rejets (moteur) : {'spread_below_threshold': 369219583, 'liquidity_below_min': 3342303, 'negative_expected_net': 2092710, 'borrow_bound_too_small': 426077, 'cycle_budget_exhausted': 73332, 'unquotable': 34186}
- Enregistrements de la session : 2095869 ; net attendu > 0 : 3159 ; simulés (eth_call de la vraie tx) : 116 (ok 75, échec 41) ; étiquettes ghost N+1 : 18/86 positives
- Décisions : {'REJECTED': 2095869} ; motifs de rejet : {'below_safety_margin': 1210, 'negative_expected_net': 2092710, 'reliability_not_demonstrated': 3159, 'sim_below_estimate': 4, 'simulation_failed': 41}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52591461 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 4.060766 WETH | 0.005574 WETH | 0.000000 WETH | 0.000003 WETH | 0.005572 WETH (12.8002 €) | — | 13.72 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.120287 cbBTC | 0.000167 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000166 cbBTC (12.7602 €) | — | 13.84 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52597125 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 4.003113 WETH | 0.003140 WETH | 0.000000 WETH | 0.000004 WETH | 0.003135 WETH (7.1524 €) | — | 7.83 | 0.106 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52597125 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 9,877.642513 USDC | 7.749996 USDC | 0.000000 USDC | 0.010526 USDC | 7.739470 USDC (7.1203 €) | — | 7.84 | 0.106 (n=14) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 3.396471 WETH | 0.002780 WETH | 0.000000 WETH | 0.000004 WETH | 0.002776 WETH (6.3600 €) | — | 8.17 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.100054 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (6.3572 €) | — | 8.29 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 8,421.081624 USDC | 6.911616 USDC | 0.000000 USDC | 0.010892 USDC | 6.900724 USDC (6.3487 €) | — | 8.19 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 3.359749 WETH | 0.002767 WETH | 0.000000 WETH | 0.000004 WETH | 0.002762 WETH (6.3461 €) | — | 8.22 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.099416 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (6.3272 €) | — | 8.30 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 8,421.081624 USDC | 6.877173 USDC | 0.000000 USDC | 0.010921 USDC | 6.866252 USDC (6.3170 €) | — | 8.15 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.344257 WETH | 0.002578 WETH | 0.000000 WETH | 0.000003 WETH | 0.002575 WETH (5.9158 €) | — | 7.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome_slipstream]→cbBTC | 0.098050 cbBTC | 0.000077 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000077 cbBTC (5.8979 €) | — | 7.85 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52597125 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 3.393251 WETH | 0.002583 WETH | 0.000000 WETH | 0.000004 WETH | 0.002578 WETH (5.8814 €) | — | 7.60 | 0.106 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.790945 WETH | 0.002564 WETH | 0.000000 WETH | 0.000004 WETH | 0.002560 WETH (5.8664 €) | — | 6.75 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.112756 cbBTC | 0.000077 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000077 cbBTC (5.8636 €) | — | 6.79 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,526.367052 USDC | 6.374898 USDC | 0.000000 USDC | 0.010513 USDC | 6.364385 USDC (5.8552 €) | — | 6.68 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52597125 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 8,371.797057 USDC | 6.374308 USDC | 0.000000 USDC | 0.010902 USDC | 6.363406 USDC (5.8543 €) | — | 7.60 | 0.106 (n=14) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 3.798303 WETH | 0.002549 WETH | 0.000000 WETH | 0.000004 WETH | 0.002545 WETH (5.8470 €) | — | 6.70 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.112948 cbBTC | 0.000076 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000076 cbBTC (5.8304 €) | — | 6.73 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 9,459.488712 USDC | 6.336151 USDC | 0.000000 USDC | 0.010542 USDC | 6.325609 USDC (5.8196 €) | — | 6.69 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52591461 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 4.383100 WETH | 0.002288 WETH | 0.000000 WETH | 0.000003 WETH | 0.002285 WETH (5.2487 €) | — | 5.21 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52591461 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10,891.997010 USDC | 5.686515 USDC | 0.000000 USDC | 0.008265 USDC | 5.678250 USDC (5.2240 €) | — | 5.21 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52597125 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 3.326787 WETH | 0.002151 WETH | 0.000000 WETH | 0.000004 WETH | 0.002147 WETH (4.8966 €) | — | 6.45 | 0.106 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52597125 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.099365 cbBTC | 0.000064 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000064 cbBTC (4.8904 €) | — | 6.47 | 0.106 (n=14) | REJECTED | reliability_not_demonstrated |
| 52597125 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 8,255.645959 USDC | 5.308512 USDC | 0.000000 USDC | 0.010526 USDC | 5.297986 USDC (4.8741 €) | — | 6.42 | 0.106 (n=14) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 107 ; taux observé 0.196 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
