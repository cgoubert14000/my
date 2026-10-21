# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T07:33:09+00:00 ; durée 164.32 min ; blocs 52884388 → 52889317 (4484 vus)

## Connexion
- Requêtes RPC : 57450 ; erreurs : 200 ; latence p50/p95 : 428.9/1,258.3 ms
- Rafraîchissements d'état : 4484 ; âge des données au dernier bloc : 4.12 s ; changements de frais LP observés (pools à frais dynamiques) : 8618
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 23673 ; cycles déclenchés par événement : 1271 ; avance médiane sur le rafraîchissement multicall : 608 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,444.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236 (quarantaine 2), aerodrome_slipstream 158, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52889493; aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52889493

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,384,352 | 2,444.444055 | 52889317 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,452,185 | 1.182131 | 52889316 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,034,068 | 94.496328 | 52889316 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,482,533 | 0.029507 | 52889316 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 14,051,645 | 0.029539 | 52889316 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,350,728 | 0.029551 | 52889316 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,954,942 | 0.000012 | 52889317 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,603,584 | 2,450.599410 | 52889317 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,409,538 | 2,444.502976 | 52889316 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 378 | 8,169,911 | 0.000012 | 52889317 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 818 | 7,360,562 | 2,451.199373 | 52889316 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,288,272 | 0.001676 | 52889316 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 6,672,338 | 0.000012 | 52889317 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,596,433 | 0.029499 | 52889316 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,233,221 | 0.024769 | 52889316 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,711,388 | 0.802393 | 52889316 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,705,868 | 0.000278 | 52889316 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,441,241 | 2,451.582130 | 52889317 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,396,930 | 0.998741 | 52889316 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,033,896 | 34,823.175288 | 52889316 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,562,212 | 1.174892 | 52889316 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/AERO | 10000 | 3,344,979 | 2,869.050427 | 52889316 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 451 | 3,083,907 | 2,453.498225 | 52889317 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,763,897 | 396.669685 | 52889316 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2799 | 2,758,494 | 94.328128 | 52889316 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,532,099 | 1.142086 | 52889316 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,269,058 | 0.000012 | 52889317 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,239,274 | 1,209,488.803510 | 52889316 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,149,815 | 0.000010 | 52889316 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,767 | 0.000012 | 52889317 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,316 | 1.383640 | 52889316 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,945,772 | 0.000000 | 52889316 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,904,201 | 1.105697 | 52889316 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,811,356 | 0.019260 | 52889316 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/MORPHO | 2745 | 1,724,157 | 1,050.089157 | 52889316 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,811 | 0.021474 | 52889316 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,715,292 | 0.916061 | 52889316 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,715,004 | 15.754264 | 52889316 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,801 | 1.490078 | 52889316 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,687,241 | 2.310610 | 52889316 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,674,558 | 2,889.464235 | 52889316 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,671,108 | 13,455.284678 | 52889316 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,162 | 0.826535 | 52889316 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 73 | 1,423,379 | 1.122577 | 52889316 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,347,309 | 0.004793 | 52889316 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,329,873 | 0.000280 | 52889316 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,326,025 | 0.000000 | 52889316 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,309,280 | 0.029555 | 52889316 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,276,570 | 2,450.600490 | 52889317 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,876 | 63.619861 | 52889316 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,223,415 | 34,771,915.296574 | 52889316 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,213,784 | 23.077228 | 52889316 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,195,442 | 71,268.898148 | 52889316 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,194,852 | 1,134,549.966586 | 52889316 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,212 | 0.436545 | 52889316 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,177,982 | 484,015.695185 | 52889316 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,156,762 | 1.106158 | 52889316 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,148,257 | 0.886155 | 52889316 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,147,494 | 47.852398 | 52889316 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,110,664 | 20,441,193.204374 | 52889316 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 5754 ; routes examinées : 123503856 ; candidats optimisés : 767911 ; net attendu > 0 : 154 ; dernier cycle 260.3 ms
- Rejets (moteur) : {'spread_below_threshold': 121715299, 'liquidity_below_min': 824651, 'negative_expected_net': 767757, 'pool_quarantined': 186496, 'borrow_bound_too_small': 5744, 'cycle_budget_exhausted': 3755}
- Enregistrements de la session : 767911 ; net attendu > 0 : 154 ; simulés (eth_call de la vraie tx) : 24 (ok 0, échec 24) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 767911} ; motifs de rejet : {'below_safety_margin': 130, 'negative_expected_net': 767757, 'p_lower_below_threshold': 148, 'price_impact': 117, 'reliability_not_demonstrated': 6, 'simulation_failed': 24, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52887788 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 76.776773 USDC | 0.127547 USDC | 0.000000 USDC | 0.005482 USDC | 0.122065 USDC (0.1123 €) | — | 15.90 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52887787 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 53.684559 USDC | 0.062580 USDC | 0.000000 USDC | 0.005482 USDC | 0.057098 USDC (0.0525 €) | — | 10.64 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52888691 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 45.892851 USDC | 0.045720 USDC | 0.000000 USDC | 0.005481 USDC | 0.040239 USDC (0.0370 €) | — | 8.77 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52888691 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 14.917647 USDC | 0.021142 USDC | 0.000000 USDC | 0.005144 USDC | 0.015998 USDC (0.0147 €) | — | 10.72 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52889192 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.021 (n=39) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889192 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.021 (n=39) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889193 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.020 (n=40) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889193 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.020 (n=40) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889192 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.021 (n=39) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52885990 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004233 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.87 | 0.286 (n=89) | REJECTED | below_safety_margin(791748084320<846554872539), p_lower_below_threshold(0.29<0.75) |
| 52885990 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.339254 USDC | 0.009289 USDC | 0.000000 USDC | 0.007378 USDC | 0.001911 USDC (0.0018 €) | — | 1.85 | 0.286 (n=89) | REJECTED | below_safety_margin(1911<2067), p_lower_below_threshold(0.29<0.75) |
| 52885990 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004162 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0015 €) | — | 1.62 | 0.119 (n=194) | REJECTED | below_safety_margin(675391846905<832447526675), p_lower_below_threshold(0.12<0.75) |
| 52885990 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.047831 USDC | 0.009005 USDC | 0.000000 USDC | 0.007378 USDC | 0.001627 USDC (0.0015 €) | — | 1.62 | 0.119 (n=194) | REJECTED | below_safety_margin(1627<2009), p_lower_below_threshold(0.12<0.75) |
| 52887839 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 8.378860 USDC | 0.006715 USDC | 0.000000 USDC | 0.005146 USDC | 0.001569 USDC (0.0014 €) | — | 1.87 | 0.001 (n=7) | REJECTED | below_safety_margin(1569<1675), reliability_not_demonstrated |
| 52887839 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 8.378860 USDC | 0.006715 USDC | 0.000000 USDC | 0.005146 USDC | 0.001569 USDC (0.0014 €) | — | 1.87 | 0.001 (n=7) | REJECTED | below_safety_margin(1569<1675), reliability_not_demonstrated |
| 52886001 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004097 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0013 €) | — | 1.45 | 0.286 (n=89) | REJECTED | below_safety_margin(592488913815<819454971974), p_lower_below_threshold(0.29<0.75) |
| 52886001 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.053350 USDC | 0.008770 USDC | 0.000000 USDC | 0.007345 USDC | 0.001425 USDC (0.0013 €) | — | 1.42 | 0.286 (n=89) | REJECTED | below_safety_margin(1425<2010), p_lower_below_threshold(0.29<0.75) |
| 52886001 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004048 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0011 €) | — | 1.18 | 0.119 (n=194) | REJECTED | below_safety_margin(477669725534<809537137834), p_lower_below_threshold(0.12<0.75) |
| 52886001 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.754404 USDC | 0.008490 USDC | 0.000000 USDC | 0.007345 USDC | 0.001145 USDC (0.0011 €) | — | 1.17 | 0.119 (n=194) | REJECTED | below_safety_margin(1145<1950), p_lower_below_threshold(0.12<0.75) |
| 52885988 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.84 | 0.119 (n=194) | REJECTED | below_safety_margin(333503695751<789830782116), stale_data(4609ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52885988 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.583833 USDC | 0.008139 USDC | 0.000000 USDC | 0.007346 USDC | 0.000793 USDC (0.0007 €) | — | 0.83 | 0.119 (n=194) | REJECTED | below_safety_margin(793<1916), stale_data(4615ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52885992 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 19.726878 USDC | 0.006191 USDC | 0.000000 USDC | 0.005488 USDC | 0.000703 USDC (0.0006 €) | — | 0.36 | 0.027 (n=11) | REJECTED | below_safety_margin(703<3945), reliability_not_demonstrated |
| 52885999 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.70 | 0.119 (n=194) | REJECTED | below_safety_margin(277719272866<789753522689), p_lower_below_threshold(0.12<0.75) |
| 52886000 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.003949 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.70 | 0.119 (n=194) | REJECTED | below_safety_margin(277719272866<789753522689), p_lower_below_threshold(0.12<0.75) |
| 52885999 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.453670 USDC | 0.008003 USDC | 0.000000 USDC | 0.007345 USDC | 0.000658 USDC (0.0006 €) | — | 0.70 | 0.119 (n=194) | REJECTED | below_safety_margin(658<1890), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1600 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
