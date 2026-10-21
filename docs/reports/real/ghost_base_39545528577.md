# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T07:42:40+00:00 ; durée 173.82 min ; blocs 52884388 → 52889601 (4748 vus)

## Connexion
- Requêtes RPC : 61085 ; erreurs : 200 ; latence p50/p95 : 332.6/1,552.7 ms
- Rafraîchissements d'état : 4748 ; âge des données au dernier bloc : 4.04 s ; changements de frais LP observés (pools à frais dynamiques) : 9226
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28417 ; cycles déclenchés par événement : 1508 ; avance médiane sur le rafraîchissement multicall : 659 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,446.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236 (quarantaine 2), aerodrome_slipstream 158, pancakeswap_v3 31 (quarantaine 1), uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 3 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52889796; aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52889796; pancakeswap_v3:USDC/PLAY@0xf1CaCd: simulation failed ×5 (model/chain mismatch) — until block 52889736

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,469,117 | 2,446.763718 | 52889602 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,447,929 | 1.182138 | 52889602 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,439,411 | 0.029539 | 52889602 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 18,064,038 | 94.378385 | 52889602 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,494,125 | 0.029507 | 52889602 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,356,691 | 0.029551 | 52889602 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,954,695 | 0.000012 | 52889602 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,609,758 | 2,448.533884 | 52889602 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 8,537,344 | 0.000012 | 52889602 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 8,413,872 | 2,447.019078 | 52889602 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 8,194,687 | 0.000012 | 52889602 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 624 | 7,615,472 | 2,448.196673 | 52889602 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,287,783 | 0.001676 | 52889602 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,600,311 | 0.029516 | 52889602 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,233,282 | 0.024771 | 52889602 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,716,245 | 0.802393 | 52889602 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,714,160 | 0.000278 | 52889602 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,444,734 | 2,448.382442 | 52889602 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,396,692 | 0.998741 | 52889602 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,038,055 | 34,823.175288 | 52889602 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 418 | 3,385,088 | 2,451.149995 | 52889602 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,346,695 | 2,872.570569 | 52889602 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,218,635 | 1.174892 | 52889602 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,829,965 | 396.669685 | 52889602 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2739 | 2,762,718 | 94.407396 | 52889602 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,534,710 | 1.142086 | 52889602 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,268,880 | 0.000012 | 52889602 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,261,527 | 0.000010 | 52889602 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,241,583 | 1,209,488.803510 | 52889602 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,074,808 | 0.000012 | 52889602 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,316 | 1.383640 | 52889602 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 2,009,603 | 1,050.709590 | 52889602 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,947,778 | 0.000000 | 52889602 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,906,164 | 1.105697 | 52889602 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,811,758 | 0.019268 | 52889602 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,794,689 | 15.750886 | 52889602 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,721,554 | 13,455.284678 | 52889602 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,717,061 | 0.916061 | 52889602 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | fBOMB/USDC | 10000 | 1,715,862 | 0.021475 | 52889602 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,815 | 1.490058 | 52889602 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,688,981 | 2.310610 | 52889602 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,675,722 | 2,893.129100 | 52889602 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,162 | 0.826535 | 52889602 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,423,341 | 1.122532 | 52889602 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,348,698 | 0.004793 | 52889602 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,332,218 | 0.000280 | 52889602 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,322,206 | 0.000000 | 52889602 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,309,919 | 0.029555 | 52889602 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,277,414 | 2,448.315129 | 52889602 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,876 | 63.619861 | 52889602 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,224,676 | 34,771,915.296574 | 52889602 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,215,035 | 23.077228 | 52889602 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,196,676 | 71,268.749987 | 52889602 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,196,084 | 1,134,549.966586 | 52889602 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,212 | 0.436545 | 52889602 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,179,196 | 484,015.695185 | 52889602 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,157,955 | 1.106158 | 52889602 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,151,978 | 0.886186 | 52889602 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | USDC/NOCK | 3000 | 1,147,534 | 47.849052 | 52889602 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,111,809 | 20,441,193.204374 | 52889602 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 6255 ; routes examinées : 134257320 ; candidats optimisés : 806251 ; net attendu > 0 : 174 ; dernier cycle 132.2 ms
- Rejets (moteur) : {'spread_below_threshold': 132309373, 'liquidity_below_min': 881362, 'negative_expected_net': 806077, 'pool_quarantined': 250192, 'borrow_bound_too_small': 6244, 'cycle_budget_exhausted': 3898}
- Enregistrements de la session : 806251 ; net attendu > 0 : 174 ; simulés (eth_call de la vraie tx) : 30 (ok 0, échec 30) ; étiquettes ghost N+1 : 1/9 positives
- Décisions : {'REJECTED': 806251} ; motifs de rejet : {'below_safety_margin': 144, 'negative_expected_net': 806077, 'p_lower_below_threshold': 164, 'price_impact': 122, 'reliability_not_demonstrated': 10, 'simulation_failed': 30, 'stale_data': 16}

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
| 52889496 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000409 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0020 €) | — | 21.64 | 0.020 (n=40) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889192 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.021 (n=39) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889192 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.021 (n=39) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889193 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.020 (n=40) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889193 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.020 (n=40) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889192 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000410 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 20.95 | 0.021 (n=39) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.02<0.75) |
| 52889495 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→fBOMB→[aerodrome]→WETH | 0.000409 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 19.65 | 0.000 (n=23) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, reliability_not_demonstrated |
| 52885990 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004233 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0018 €) | — | 1.87 | 0.286 (n=89) | REJECTED | below_safety_margin(791748084320<846554872539), p_lower_below_threshold(0.29<0.75) |

## Fiabilité et décision
- Observations ghost : 1602 ; taux observé 0.102 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
