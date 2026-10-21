# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T08:17:35+00:00 ; durée 208.74 min ; blocs 52884388 → 52890649 (5690 vus)

## Connexion
- Requêtes RPC : 74222 ; erreurs : 248 ; latence p50/p95 : 454.8/1,443.8 ms
- Rafraîchissements d'état : 5691 ; âge des données au dernier bloc : 1.82 s ; changements de frais LP observés (pools à frais dynamiques) : 11228
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 44096 ; cycles déclenchés par événement : 2287 ; avance médiane sur le rafraîchissement multicall : 633 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,449.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236 (quarantaine 2), aerodrome_slipstream 158, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 2 — aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52890705; aerodrome:fBOMB/cbBTC@0x3d36Cf: simulation failed ×5 (model/chain mismatch) — until block 52890705

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,562,852 | 2,449.615971 | 52890649 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,439,667 | 1.181937 | 52890649 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,505,269 | 0.029539 | 52890649 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 17,968,500 | 95.607189 | 52890649 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,513,544 | 0.029520 | 52890649 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,368,322 | 0.029551 | 52890649 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,959,071 | 0.000012 | 52890649 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,616,014 | 2,451.198767 | 52890649 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,423,723 | 2,449.941266 | 52890649 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 8,173,418 | 0.000012 | 52890649 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 7,971,313 | 0.000012 | 52890649 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,877,407 | 2,450.680915 | 52890649 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,291,525 | 0.001674 | 52890649 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,606,425 | 0.029518 | 52890649 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,233,760 | 0.024779 | 52890649 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,721,743 | 0.802393 | 52890649 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,720,616 | 0.000279 | 52890649 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,458,285 | 2,450.969408 | 52890649 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDT | 418 | 4,446,096 | 2,453.579393 | 52890649 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,401,818 | 0.998741 | 52890649 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,043,832 | 34,804.754250 | 52890649 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,349,070 | 2,880.425201 | 52890649 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,219,145 | 1.174892 | 52890649 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,752,226 | 95.631924 | 52890649 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,690,317 | 397.091300 | 52890649 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,565,692 | 0.000010 | 52890649 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,538,977 | 1.142085 | 52890649 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,270,072 | 0.000012 | 52890649 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,244,196 | 1,209,488.803510 | 52890649 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,076,539 | 0.000012 | 52890649 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52890649 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,952,946 | 0.000000 | 52890649 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,914,186 | 15.710334 | 52890649 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,908,386 | 1.105697 | 52890649 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,810,542 | 0.019242 | 52890649 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,726,057 | 13,459.417512 | 52890649 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,719,062 | 0.916061 | 52890649 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,877 | 0.021475 | 52890649 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,828 | 1.490038 | 52890649 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,690,950 | 2.310610 | 52890649 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,677,141 | 2,900.871389 | 52890649 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 1,528,313 | 1,052.754498 | 52890649 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,162 | 0.826535 | 52890649 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,422,728 | 1.122099 | 52890649 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,350,270 | 0.004793 | 52890649 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,334,042 | 0.000280 | 52890649 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,323,048 | 0.000000 | 52890649 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,311,446 | 0.029555 | 52890649 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,278,372 | 2,451.297974 | 52890649 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,876 | 63.619861 | 52890649 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,226,104 | 34,771,915.296574 | 52890649 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,216,452 | 23.077223 | 52890649 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,198,071 | 71,268.745124 | 52890649 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,197,478 | 1,134,549.966586 | 52890649 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,212 | 0.436545 | 52890649 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,180,961 | 483,588.380365 | 52890649 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,159,305 | 1.106158 | 52890649 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,156,643 | 0.886230 | 52890649 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,148,807 | 47.743103 | 52890649 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,108,574 | 20,586,460.917356 | 52890649 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 7977 ; routes examinées : 171218328 ; candidats optimisés : 951803 ; net attendu > 0 : 197 ; dernier cycle 147.0 ms
- Rejets (moteur) : {'spread_below_threshold': 168711951, 'liquidity_below_min': 1111313, 'negative_expected_net': 951606, 'pool_quarantined': 430808, 'borrow_bound_too_small': 7958, 'cycle_budget_exhausted': 4431}
- Enregistrements de la session : 951803 ; net attendu > 0 : 197 ; simulés (eth_call de la vraie tx) : 45 (ok 0, échec 45) ; étiquettes ghost N+1 : 1/15 positives
- Décisions : {'REJECTED': 951803} ; motifs de rejet : {'below_safety_margin': 152, 'negative_expected_net': 951606, 'p_lower_below_threshold': 187, 'price_impact': 137, 'reliability_not_demonstrated': 10, 'simulation_failed': 45, 'stale_data': 25}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52887788 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 76.776773 USDC | 0.127547 USDC | 0.000000 USDC | 0.005482 USDC | 0.122065 USDC (0.1123 €) | — | 15.90 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52887787 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 53.684559 USDC | 0.062580 USDC | 0.000000 USDC | 0.005482 USDC | 0.057098 USDC (0.0525 €) | — | 10.64 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52888691 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 45.892851 USDC | 0.045720 USDC | 0.000000 USDC | 0.005481 USDC | 0.040239 USDC (0.0370 €) | — | 8.77 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52888691 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 14.917647 USDC | 0.021142 USDC | 0.000000 USDC | 0.005144 USDC | 0.015998 USDC (0.0147 €) | — | 10.72 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52889396 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 81.977931 USDC | 0.014628 USDC | 0.000000 USDC | 0.007394 USDC | 0.007234 USDC (0.0067 €) | — | 0.88 | 0.119 (n=194) | REJECTED | below_safety_margin(7234<16395), p_lower_below_threshold(0.12<0.75) |
| 52889397 | USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 81.977931 USDC | 0.014628 USDC | 0.000000 USDC | 0.007394 USDC | 0.007234 USDC (0.0067 €) | — | 0.88 | 0.119 (n=194) | REJECTED | below_safety_margin(7234<16395), p_lower_below_threshold(0.12<0.75) |
| 52889396 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH | 0.033296 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0066 €) | — | 0.88 | 0.119 (n=194) | REJECTED | below_safety_margin(2939099648995<6659111179248), p_lower_below_threshold(0.12<0.75) |
| 52889397 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→WETH | 0.033296 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0066 €) | — | 0.88 | 0.119 (n=194) | REJECTED | below_safety_margin(2939099648995<6659111179248), p_lower_below_threshold(0.12<0.75) |
| 52889396 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 60.317375 USDC | 0.013585 USDC | 0.000000 USDC | 0.007394 USDC | 0.006191 USDC (0.0057 €) | — | 1.03 | 0.119 (n=194) | REJECTED | below_safety_margin(6191<12063), p_lower_below_threshold(0.12<0.75) |
| 52889397 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 60.317375 USDC | 0.013585 USDC | 0.000000 USDC | 0.007394 USDC | 0.006191 USDC (0.0057 €) | — | 1.03 | 0.119 (n=194) | REJECTED | below_safety_margin(6191<12063), p_lower_below_threshold(0.12<0.75) |
| 52889396 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.024735 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 1.02 | 0.119 (n=194) | REJECTED | below_safety_margin(2514195905560<4947004580954), p_lower_below_threshold(0.12<0.75) |
| 52889397 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.024735 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 1.02 | 0.119 (n=194) | REJECTED | below_safety_margin(2514195905560<4947004580954), p_lower_below_threshold(0.12<0.75) |
| 52889396 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 58.522026 USDC | 0.012928 USDC | 0.000000 USDC | 0.007394 USDC | 0.005534 USDC (0.0051 €) | — | 0.95 | 0.119 (n=194) | REJECTED | below_safety_margin(5534<11704), p_lower_below_threshold(0.12<0.75) |
| 52889397 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 58.522026 USDC | 0.012928 USDC | 0.000000 USDC | 0.007394 USDC | 0.005534 USDC (0.0051 €) | — | 0.95 | 0.119 (n=194) | REJECTED | below_safety_margin(5534<11704), p_lower_below_threshold(0.12<0.75) |
| 52889396 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.024046 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0051 €) | — | 0.93 | 0.119 (n=194) | REJECTED | below_safety_margin(2246251010528<4809253884718), p_lower_below_threshold(0.12<0.75) |
| 52889397 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.024046 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0051 €) | — | 0.93 | 0.119 (n=194) | REJECTED | below_safety_margin(2246251010528<4809253884718), p_lower_below_threshold(0.12<0.75) |
| 52889436 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 21.937954 USDC | 0.010548 USDC | 0.000000 USDC | 0.005523 USDC | 0.005025 USDC (0.0046 €) | — | 2.29 | 0.014 (n=59) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 52890163 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 32.497887 USDC | 0.012298 USDC | 0.000000 USDC | 0.007362 USDC | 0.004936 USDC (0.0045 €) | — | 1.52 | 0.286 (n=89) | REJECTED | below_safety_margin(4936<6499), p_lower_below_threshold(0.29<0.75) |
| 52890162 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 32.497887 USDC | 0.012298 USDC | 0.000000 USDC | 0.007362 USDC | 0.004936 USDC (0.0045 €) | — | 1.52 | 0.286 (n=89) | REJECTED | below_safety_margin(4936<6499), stale_data(4972ms>4000.0), p_lower_below_threshold(0.29<0.75) |
| 52890163 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.013189 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0045 €) | — | 1.52 | 0.286 (n=89) | REJECTED | below_safety_margin(2001977998726<2637754166529), p_lower_below_threshold(0.29<0.75) |
| 52890162 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.013220 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0045 €) | — | 1.51 | 0.286 (n=89) | REJECTED | below_safety_margin(2001891732976<2644084579309), stale_data(4978ms>4000.0), p_lower_below_threshold(0.29<0.75) |
| 52890163 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 31.607950 USDC | 0.011711 USDC | 0.000000 USDC | 0.007362 USDC | 0.004349 USDC (0.0040 €) | — | 1.38 | 0.119 (n=194) | REJECTED | below_safety_margin(4349<6321), p_lower_below_threshold(0.12<0.75) |
| 52890162 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 31.607950 USDC | 0.011711 USDC | 0.000000 USDC | 0.007362 USDC | 0.004349 USDC (0.0040 €) | — | 1.38 | 0.119 (n=194) | REJECTED | below_safety_margin(4349<6321), stale_data(5002ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52890162 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.012952 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 1.36 | 0.119 (n=194) | REJECTED | below_safety_margin(1763348042984<2590481537469), stale_data(5009ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 52890163 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.013001 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0040 €) | — | 1.36 | 0.119 (n=194) | REJECTED | below_safety_margin(1763304044582<2600154454327), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1608 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
