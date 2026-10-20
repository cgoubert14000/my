# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T16:50:48+00:00 ; durée 294.62 min ; blocs 52854009 → 52862845 (8461 vus)

## Connexion
- Requêtes RPC : 107655 ; erreurs : 45 ; latence p50/p95 : 376.3/948.0 ms
- Rafraîchissements d'état : 8461 ; âge des données au dernier bloc : 4.22 s ; changements de frais LP observés (pools à frais dynamiques) : 30067
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 88510 ; cycles déclenchés par événement : 3888 ; avance médiane sur le rafraîchissement multicall : 672 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,447.13 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 573 pools, 327 jetons, 21172 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156 (quarantaine 2), pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3877 (énumérés 393, par paires 0), mesurés 575, sous le plancher de 10000.0 $ : 2 → gardés 573 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2381.795213, 'AERO': 0.801082, 'cbBTC': 81409.268719}
- Pools en quarantaine : 2 — aerodrome_slipstream:USDC/VELVET@0x6b0F53: simulation failed ×5 (model/chain mismatch) — until block 52862910; aerodrome_slipstream:WETH/VELVET@0xF579B1: simulation failed ×5 (model/chain mismatch) — until block 52862910

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 147,786,812 | 2,447.126727 | 52862845 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,017,813 | 1.164712 | 52862845 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,955,294 | 95.823489 | 52862845 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,358,970 | 0.029641 | 52862845 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2540 | 10,930,627 | 0.029580 | 52862845 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,536,251 | 0.029567 | 52862845 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,925,246 | 0.000012 | 52862845 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,582,950 | 2,451.751742 | 52862845 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,382,682 | 2,447.275290 | 52862845 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 366 | 8,158,562 | 0.000012 | 52862845 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 8,013,606 | 0.000012 | 52862845 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 952 | 7,359,807 | 2,452.424757 | 52862845 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,276,657 | 0.001682 | 52862845 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,435,545 | 0.029645 | 52862845 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,236,305 | 0.024700 | 52862845 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,725,723 | 0.000275 | 52862845 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,718,153 | 0.802394 | 52862845 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,426,401 | 2,452.569583 | 52862845 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,375,667 | 0.998767 | 52862845 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,059,481 | 34,466.372469 | 52862845 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 475 | 3,384,695 | 2,455.029480 | 52862845 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,372,837 | 2,851.715582 | 52862845 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 3,064,458 | 1,022.322163 | 52862845 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,980,782 | 1.142083 | 52862845 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,885,205 | 0.000012 | 52862845 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,835,117 | 403.785507 | 52862845 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2835 | 2,743,347 | 95.811826 | 52862845 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,232,906 | 1,219,268.722629 | 52862845 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,230,701 | 0.000010 | 52862845 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,857 | 1.238895 | 52862845 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,028,987 | 1.381848 | 52862845 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,977,195 | 0.000000 | 52862845 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,876,698 | 16.049080 | 52862845 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,841,502 | 1.173105 | 52862845 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| uniswap_v3 | XDP/USDC | 100 | 1,814,741 | 0.019414 | 52862845 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,773,791 | 0.000012 | 52862845 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | weETH_04c0/WETH | 500 | 1,770,864 | 1.105512 | 52862845 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,716,952 | 13,639.212455 | 52862845 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | fBOMB/USDC | 10000 | 1,705,708 | 0.021154 | 52862845 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | WETH/msETH (stable) | 500 | 1,688,154 | 2.312225 | 52862845 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,676,721 | 2,855.949914 | 52862845 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,572,193 | 0.916062 | 52862845 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,783 | 0.826046 | 52862845 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,416,474 | 1.123468 | 52862845 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,360,239 | 0.004842 | 52862845 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,344,493 | 0.000000 | 52862845 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,324,966 | 0.000276 | 52862845 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,307,852 | 0.029568 | 52862845 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,300,488 | 23.114716 | 52862845 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,258,838 | 2,451.768233 | 52862845 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,236,075 | 63.599454 | 52862845 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,230,660 | 67,580.613531 | 52862845 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/doginme | 10000 | 1,215,124 | 35,656,571.832345 | 52862845 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,879 | 0.436867 | 52862845 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,170,200 | 494,160.495614 | 52862845 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 503 | 1,168,552 | 0.886509 | 52862845 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,161,329 | 1,203,893.085639 | 52862845 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,141,376 | 48.366766 | 52862845 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,086,356 | 21,261,604.476198 | 52862845 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/USDT | 8 | 1,071,990 | 1.001295 | 52862845 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 12348 ; routes examinées : 261431856 ; candidats optimisés : 1542438 ; net attendu > 0 : 1639 ; dernier cycle 431.6 ms
- Rejets (moteur) : {'spread_below_threshold': 257359851, 'liquidity_below_min': 2132154, 'negative_expected_net': 1540799, 'pool_quarantined': 242276, 'borrow_bound_too_small': 139011, 'cycle_budget_exhausted': 16126}
- Enregistrements de la session : 1542438 ; net attendu > 0 : 1639 ; simulés (eth_call de la vraie tx) : 166 (ok 104, échec 62) ; étiquettes ghost N+1 : 17/125 positives
- Décisions : {'REJECTED': 1542438} ; motifs de rejet : {'below_safety_margin': 989, 'negative_expected_net': 1540799, 'p_lower_below_threshold': 1355, 'price_impact': 45, 'reliability_not_demonstrated': 284, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 2, 'simulation_failed': 62, 'stale_data': 91}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52862756 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 3,649.245624 USDC | 1.813612 USDC | 0.000000 USDC | 0.007784 USDC | 1.805828 USDC (1.6614 €) | — | 4.95 | 0.106 (n=135) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52862756 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 1.474351 WETH | 0.000741 WETH | 0.000000 WETH | 0.000003 WETH | 0.000738 WETH (1.6565 €) | — | 5.01 | 0.106 (n=135) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52862756 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.043422 cbBTC | 0.000022 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000022 cbBTC (1.6561 €) | — | 5.03 | 0.106 (n=135) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52862756 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 543.665623 USDC | 0.420830 USDC | 0.000000 USDC | 0.007784 USDC | 0.413046 USDC (0.3800 €) | — | 7.60 | 0.106 (n=135) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52862756 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.222549 WETH | 0.000172 WETH | 0.000000 WETH | 0.000003 WETH | 0.000169 WETH (0.3785 €) | — | 7.58 | 0.106 (n=135) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52862756 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 507.959795 USDC | 0.406470 USDC | 0.000000 USDC | 0.007784 USDC | 0.398686 USDC (0.3668 €) | — | 7.85 | 0.106 (n=135) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52862756 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.207576 WETH | 0.000166 WETH | 0.000000 WETH | 0.000003 WETH | 0.000163 WETH (0.3654 €) | — | 7.84 | 0.106 (n=135) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52862756 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→USDC | 377.723248 USDC | 0.362910 USDC | 0.000000 USDC | 0.006286 USDC | 0.356624 USDC (0.3281 €) | — | 9.44 | 0.000 (n=39) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52862756 | WETH→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.154678 WETH | 0.000148 WETH | 0.000000 WETH | 0.000003 WETH | 0.000146 WETH (0.3268 €) | — | 9.41 | 0.000 (n=39) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52860553 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.269723 WETH | 0.000149 WETH | 0.000000 WETH | 0.000003 WETH | 0.000146 WETH (0.3266 €) | — | 5.41 | 0.109 (n=132) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52860553 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.007574 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3264 €) | — | 5.68 | 0.109 (n=132) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52862756 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 360.963401 USDC | 0.322665 USDC | 0.000000 USDC | 0.007784 USDC | 0.314881 USDC (0.2897 €) | — | 8.72 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52862756 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.147495 WETH | 0.000132 WETH | 0.000000 WETH | 0.000003 WETH | 0.000129 WETH (0.2886 €) | — | 8.72 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52860377 | WETH→[aerodrome_slipstream]→BRETT→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.028655 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000123 WETH (0.2754 €) | 0.000123 WETH | 42.94 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 52862756 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 332.487817 USDC | 0.274393 USDC | 0.000000 USDC | 0.007784 USDC | 0.266609 USDC (0.2453 €) | — | 8.02 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52862756 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.135977 WETH | 0.000112 WETH | 0.000000 WETH | 0.000003 WETH | 0.000109 WETH (0.2444 €) | — | 8.01 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 52862756 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 320.613748 USDC | 0.259158 USDC | 0.000000 USDC | 0.008154 USDC | 0.251004 USDC (0.2309 €) | — | 7.83 | 0.106 (n=135) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52862756 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[sushiswap_v3]→WETH | 0.130989 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2301 €) | — | 7.83 | 0.106 (n=135) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52861527 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,289.600704 USDC | 0.246212 USDC | 0.000000 USDC | 0.005934 USDC | 0.240278 USDC (0.2211 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(240278<457920), p_lower_below_threshold(0.01<0.75) |
| 52861528 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 2,289.600704 USDC | 0.246212 USDC | 0.000000 USDC | 0.005934 USDC | 0.240278 USDC (0.2211 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(240278<457920), p_lower_below_threshold(0.01<0.75) |
| 52861527 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.939641 WETH | 0.000101 WETH | 0.000000 WETH | 0.000002 WETH | 0.000098 WETH (0.2205 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(98465456722515<187928164483069), p_lower_below_threshold(0.01<0.75) |
| 52861528 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.939641 WETH | 0.000101 WETH | 0.000000 WETH | 0.000002 WETH | 0.000098 WETH (0.2205 €) | — | 1.05 | 0.015 (n=55) | REJECTED | below_safety_margin(98465456722515<187928164483069), p_lower_below_threshold(0.01<0.75) |
| 52862756 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 416.086859 USDC | 0.229991 USDC | 0.000000 USDC | 0.007413 USDC | 0.222578 USDC (0.2048 €) | — | 5.35 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52862756 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.170020 WETH | 0.000094 WETH | 0.000000 WETH | 0.000003 WETH | 0.000091 WETH (0.2040 €) | — | 5.35 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 52862756 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 390.873220 USDC | 0.226551 USDC | 0.000000 USDC | 0.007413 USDC | 0.219138 USDC (0.2016 €) | — | 5.61 | 0.146 (n=81) | REJECTED | p_lower_below_threshold(0.15<0.75) |

## Fiabilité et décision
- Observations ghost : 1538 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
