# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T07:31:26+00:00 ; durée 314.77 min ; blocs 52620621 → 52630063 (7545 vus)

## Connexion
- Requêtes RPC : 99478 ; erreurs : 88 ; latence p50/p95 : 404.8/1,675.9 ms
- Rafraîchissements d'état : 7546 ; âge des données au dernier bloc : 5.41 s ; changements de frais LP observés (pools à frais dynamiques) : 24126
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,361.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 326 jetons, 21316 routes
- Par DEX : uniswap_v3 139, aerodrome 235, aerodrome_slipstream 153, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3916 (énumérés 390, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2411.100006, 'AERO': 0.880097, 'cbBTC': 81403.044787}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 143,319,638 | 2,361.775379 | 52630063 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,136,348 | 1.180227 | 52630063 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,764,946 | 0.029199 | 52630063 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 15,483,896 | 106.878113 | 52630063 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,418,051 | 0.029165 | 52630063 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,265,838 | 0.029158 | 52630063 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,606,314 | 0.000012 | 52630063 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,853,732 | 2,366.871940 | 52630063 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,840,438 | 2,360.319239 | 52630063 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 7,955,107 | 0.000012 | 52630063 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 7,278,562 | 0.000012 | 52630063 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 579 | 7,098,323 | 2,366.102739 | 52630063 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,051,391 | 0.001646 | 52630063 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,223,514 | 0.029196 | 52630063 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,174,659 | 0.026621 | 52630063 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,614,179 | 1.180947 | 52630063 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,441,322 | 0.802389 | 52630063 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,351,066 | 0.000274 | 52630063 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,220,981 | 2,365.970933 | 52630063 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,151,014 | 1.000077 | 52630063 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,873,382 | 35,263.063088 | 52630063 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,419,314 | 2,773.171681 | 52630063 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,816,310 | 0.000012 | 52630063 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,511,274 | 106.912079 | 52630063 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,500,084 | 412.476913 | 52630063 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,467,540 | 1.141645 | 52630063 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,453,862 | 0.000010 | 52630063 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,313,415 | 1,058,026.313216 | 52630063 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/USDT | 403 | 2,214,291 | 2,372.518553 | 52630063 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,112,439 | 1.194817 | 52630063 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | BNKR/WETH | 10000 | 2,023,120 | 0.000000 | 52630063 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | fBOMB/USDC | 10000 | 1,840,660 | 0.022630 | 52630063 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,837,465 | 1.403316 | 52630063 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,782,192 | 0.916543 | 52630063 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,779,371 | 15.773826 | 52630063 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,768,144 | 0.000012 | 52630063 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,753,211 | 0.018559 | 52630063 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,662,025 | 2.300822 | 52630063 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,637,020 | 14,130.661877 | 52630063 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,472,699 | 2,792.876774 | 52630063 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,460,266 | 1.105502 | 52630063 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,570 | 0.831240 | 52630063 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,320,177 | 0.000000 | 52630063 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,316,519 | 1.130449 | 52630063 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,310,744 | 2,792.715083 | 52630063 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,298,813 | 0.004785 | 52630063 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,273,660 | 0.000274 | 52630063 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,269,912 | 23.184228 | 52630063 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,248,550 | 1.121022 | 52630063 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/SEND | 3000 | 1,246,764 | 62.513593 | 52630063 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,195,798 | 2,366.881741 | 52630063 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,172,506 | 35,260,700.463338 | 52630063 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,172,216 | 1.105595 | 52630063 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/EDEL | 7000 | 1,140,900 | 74,567.932394 | 52630063 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/cbBTC | 3000 | 1,137,300 | 0.029278 | 52630063 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,128,738 | 1,187,230.092635 | 52630063 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,118,593 | 506,754.020063 | 52630063 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,117,024 | 14.141225 | 52630063 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,105,432 | 51.573742 | 52630063 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,094,673 | 0.435020 | 52630063 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 7545 ; routes examinées : 160829220 ; candidats optimisés : 989813 ; net attendu > 0 : 935 ; dernier cycle 412.2 ms
- Rejets (moteur) : {'spread_below_threshold': 158143465, 'liquidity_below_min': 1636436, 'negative_expected_net': 988878, 'cycle_budget_exhausted': 31613, 'unquotable': 17648, 'borrow_bound_too_small': 10245}
- Enregistrements de la session : 989813 ; net attendu > 0 : 935 ; simulés (eth_call de la vraie tx) : 56 (ok 52, échec 4) ; étiquettes ghost N+1 : 16/39 positives
- Décisions : {'REJECTED': 989813} ; motifs de rejet : {'below_safety_margin': 540, 'negative_expected_net': 988878, 'p_lower_below_threshold': 45, 'price_impact': 12, 'reliability_not_demonstrated': 890, 'sim_below_estimate': 1, 'simulation_failed': 4, 'stale_data': 94}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52620798 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.108158 WETH | 0.000076 WETH | 0.000000 WETH | 0.000004 WETH | 0.000073 WETH (0.1606 €) | 0.000073 WETH | 6.74 | 0.204 (n=30) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52620798 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 258.171086 USDC | 0.182629 USDC | 0.000000 USDC | 0.008450 USDC | 0.174179 USDC (0.1602 €) | — | 6.75 | 0.204 (n=30) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52620797 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.122732 WETH | 0.000058 WETH | 0.000000 WETH | 0.000003 WETH | 0.000055 WETH (0.1215 €) | 0.000055 WETH | 4.48 | 0.159 (n=28) | REJECTED | reliability_not_demonstrated |
| 52620797 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→USDC | 293.319331 USDC | 0.139577 USDC | 0.000000 USDC | 0.007914 USDC | 0.131663 USDC (0.1211 €) | — | 4.49 | 0.159 (n=28) | REJECTED | reliability_not_demonstrated |
| 52620798 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.046148 WETH | 0.000054 WETH | 0.000000 WETH | 0.000003 WETH | 0.000051 WETH (0.1120 €) | 0.000051 WETH | 11.02 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52620798 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 110.038974 USDC | 0.129518 USDC | 0.000000 USDC | 0.008081 USDC | 0.121437 USDC (0.1117 €) | — | 11.04 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52620798 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.087952 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1093 €) | 0.000050 WETH | 5.64 | 0.204 (n=30) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52620798 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC | 209.645903 USDC | 0.126635 USDC | 0.000000 USDC | 0.008044 USDC | 0.118591 USDC (0.1091 €) | — | 5.66 | 0.204 (n=30) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 52620798 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.041551 WETH | 0.000044 WETH | 0.000000 WETH | 0.000003 WETH | 0.000041 WETH (0.0909 €) | — | 9.94 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52620798 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 99.161823 USDC | 0.106286 USDC | 0.000000 USDC | 0.007675 USDC | 0.098611 USDC (0.0907 €) | — | 9.94 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 52620798 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.021557 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0837 €) | — | 17.64 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52620798 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 51.359290 USDC | 0.098532 USDC | 0.000000 USDC | 0.007712 USDC | 0.090820 USDC (0.0836 €) | — | 17.68 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52620798 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.035327 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0759 €) | — | 9.76 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52620798 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 84.323615 USDC | 0.090441 USDC | 0.000000 USDC | 0.008081 USDC | 0.082360 USDC (0.0758 €) | — | 9.77 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52620797 | WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.058774 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0749 €) | 0.000034 WETH | 5.78 | 0.159 (n=28) | REJECTED | reliability_not_demonstrated |
| 52621788 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC | 0.006177 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0747 €) | — | 1.62 | 0.033 (n=25) | REJECTED | below_safety_margin(100<123), reliability_not_demonstrated |
| 52620797 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC | 140.364599 USDC | 0.089509 USDC | 0.000000 USDC | 0.008314 USDC | 0.081195 USDC (0.0747 €) | — | 5.78 | 0.159 (n=28) | REJECTED | reliability_not_demonstrated |
| 52620798 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.020286 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0742 €) | — | 16.62 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52621788 | USDC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 502.268184 USDC | 0.087869 USDC | 0.000000 USDC | 0.007240 USDC | 0.080629 USDC (0.0742 €) | — | 1.61 | 0.033 (n=25) | REJECTED | below_safety_margin(80629<100453), reliability_not_demonstrated |
| 52620798 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 48.357956 USDC | 0.087827 USDC | 0.000000 USDC | 0.007306 USDC | 0.080521 USDC (0.0741 €) | — | 16.65 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 52621788 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→tBTC→[uniswap_v3]→cbBTC | 0.005972 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0718 €) | — | 1.61 | 0.033 (n=25) | REJECTED | below_safety_margin(96<119), reliability_not_demonstrated |
| 52621788 | USDC→[aerodrome_slipstream]→tBTC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 446.380873 USDC | 0.084611 USDC | 0.000000 USDC | 0.007240 USDC | 0.077371 USDC (0.0712 €) | — | 1.73 | 0.033 (n=25) | REJECTED | below_safety_margin(77371<89276), reliability_not_demonstrated |
| 52620798 | WETH→[aerodrome]→OVER→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.019304 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0700 €) | — | 16.47 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52620798 | USDC→[sushiswap_v3]→WETH→[aerodrome]→OVER→[aerodrome]→USDC | 46.077765 USDC | 0.083647 USDC | 0.000000 USDC | 0.007712 USDC | 0.075935 USDC (0.0699 €) | — | 16.48 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52620798 | WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.055983 WETH | 0.000034 WETH | 0.000000 WETH | 0.000004 WETH | 0.000030 WETH (0.0666 €) | — | 5.40 | 0.204 (n=30) | REJECTED | p_lower_below_threshold(0.20<0.75) |

## Fiabilité et décision
- Observations ghost : 258 ; taux observé 0.190 ; borne inférieure crédible (0.9) 0.160 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.0% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
