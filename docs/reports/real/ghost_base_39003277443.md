# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T10:07:03+00:00 ; durée 324.84 min ; blocs 52711390 → 52721131 (9568 vus)

## Connexion
- Requêtes RPC : 130052 ; erreurs : 63 ; latence p50/p95 : 233.9/859.3 ms
- Rafraîchissements d'état : 9568 ; âge des données au dernier bloc : 2.73 s ; changements de frais LP observés (pools à frais dynamiques) : 9876
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 109243 ; cycles déclenchés par événement : 10698 ; avance médiane sur le rafraîchissement multicall : 303 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,430.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 575 pools, 329 jetons, 21010 routes
- Par DEX : uniswap_v3 135, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3922 (énumérés 393, par paires 0), mesurés 577, sous le plancher de 10000.0 $ : 2 → gardés 575 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2421.248535, 'AERO': 0.878353, 'cbBTC': 81453.278136}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,548,879 | 2,430.106568 | 52721132 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 43,233,405 | 1.116680 | 52721132 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,292,205 | 0.029848 | 52721132 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 16,178,581 | 0.029795 | 52721132 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 16,115,593 | 104.471747 | 52721132 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,467,768 | 0.029781 | 52721132 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,757,556 | 0.000012 | 52721132 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 9,131,443 | 2,431.930546 | 52721132 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,918,107 | 0.000012 | 52721132 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 7,842,052 | 0.000012 | 52721132 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,558,850 | 2,432.789522 | 52721132 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,162,439 | 0.001676 | 52721132 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,423,515 | 2,433.762086 | 52721132 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | fBOMB/AERO | 10000 | 5,414,291 | 0.025281 | 52721132 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,352,366 | 0.029849 | 52721132 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,277,148 | 1.000855 | 52721132 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,857,317 | 0.802398 | 52721132 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,701,232 | 0.000276 | 52721132 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,431,651 | 2,432.913330 | 52721132 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,420,946 | 0.998803 | 52721132 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,062,892 | 33,931.544438 | 52721132 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,498,688 | 2,735.997476 | 52721132 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,097,762 | 1.124229 | 52721132 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,928,260 | 1.141834 | 52721132 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,838,019 | 0.000012 | 52721132 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/USDT | 409 | 2,768,492 | 2,435.516751 | 52721132 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,705,716 | 0.000011 | 52721132 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,613,897 | 104.346826 | 52721132 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,389,345 | 402.124474 | 52721132 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,249,193 | 1,185,014.580488 | 52721132 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,279 | 1.123518 | 52721132 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,108,805 | 1.197614 | 52721132 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 2,046,806 | 15.623457 | 52721132 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,000,262 | 1.415889 | 52721132 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 1,883,248 | 1,026.656053 | 52721132 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | fBOMB/USDC | 10000 | 1,831,195 | 0.022355 | 52721132 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,820,663 | 0.000000 | 52721132 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,593 | 0.000012 | 52721132 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,754,728 | 0.018442 | 52721132 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,680,741 | 2.307070 | 52721132 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,655,794 | 13,477.642822 | 52721132 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,557,254 | 2,716.302344 | 52721132 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,553,173 | 0.916550 | 52721132 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | WETH/AERO | 3204 | 1,534,254 | 2,717.391789 | 52721132 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome | weETH_04c0/WETH | 500 | 1,522,318 | 1.105495 | 52721132 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,443 | 0.826463 | 52721132 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,364,691 | 0.000000 | 52721132 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,357,475 | 0.004872 | 52721132 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,095 | 0.435747 | 52721132 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,317,558 | 0.000274 | 52721132 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,248,900 | 62.299956 | 52721132 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,240,919 | 1.131642 | 52721132 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,211,712 | 23.291763 | 52721132 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,207,699 | 0.029776 | 52721132 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| uniswap_v3 | WETH/doginme | 10000 | 1,206,829 | 35,368,823.910888 | 52721132 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,206,525 | 1.105714 | 52721132 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,201,701 | 2,431.960974 | 52721132 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,186,701 | 1,137,165.396017 | 52721132 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,152,403 | 504,562.277444 | 52721132 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,122,345 | 13.997524 | 52721132 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 20265 ; routes examinées : 425767650 ; candidats optimisés : 2185819 ; net attendu > 0 : 379 ; dernier cycle 194.8 ms
- Rejets (moteur) : {'spread_below_threshold': 420253583, 'liquidity_below_min': 3067171, 'negative_expected_net': 2185440, 'unquotable': 229981, 'borrow_bound_too_small': 20254, 'pool_quarantined': 9458, 'cycle_budget_exhausted': 1384}
- Enregistrements de la session : 2185819 ; net attendu > 0 : 379 ; simulés (eth_call de la vraie tx) : 72 (ok 24, échec 48) ; étiquettes ghost N+1 : 0/54 positives
- Décisions : {'REJECTED': 2185819} ; motifs de rejet : {'below_safety_margin': 190, 'negative_expected_net': 2185440, 'p_lower_below_threshold': 249, 'reliability_not_demonstrated': 130, 'simulation_failed': 48, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52720648 | WETH→[aerodrome]→KTA→[aerodrome_slipstream]→WETH | 0.060897 WETH | 0.000180 WETH | 0.000000 WETH | 0.000002 WETH | 0.000178 WETH (0.3967 €) | — | 29.17 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52717343 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 171.681101 USDC | 0.431738 USDC | 0.000000 USDC | 0.005454 USDC | 0.426284 USDC (0.3922 €) | — | 24.83 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52720648 | WETH→[uniswap_v3]→KTA→[aerodrome_slipstream]→WETH | 0.035769 WETH | 0.000152 WETH | 0.000000 WETH | 0.000002 WETH | 0.000150 WETH (0.3342 €) | — | 41.83 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714900 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 159.449852 USDC | 0.353632 USDC | 0.000000 USDC | 0.005449 USDC | 0.348183 USDC (0.3203 €) | — | 21.84 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714406 | WETH→[uniswap_v3]→TEVA→[aerodrome]→WETH | 0.016230 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1209 €) | — | 33.40 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52713483 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 88.741675 USDC | 0.113607 USDC | 0.000000 USDC | 0.005439 USDC | 0.108168 USDC (0.0995 €) | — | 12.19 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036579 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | 0.000043 WETH | 11.74 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | WETH→[aerodrome_slipstream]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036579 WETH | 0.000046 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0957 €) | — | 11.74 | 0.042 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036393 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0947 €) | 0.000043 WETH | 11.68 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | WETH→[uniswap_v3]→wstETH→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.036393 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000043 WETH (0.0947 €) | — | 11.68 | 0.042 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 138.240203 USDC | 0.094365 USDC | 0.000000 USDC | 0.007281 USDC | 0.087084 USDC (0.0801 €) | — | 6.30 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC | 138.240203 USDC | 0.094365 USDC | 0.000000 USDC | 0.007281 USDC | 0.087084 USDC (0.0801 €) | — | 6.30 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001778 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0800 €) | — | 6.02 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | cbBTC→[uniswap_v3]→AERO→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001778 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0800 €) | — | 6.02 | 0.110 (n=69) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52714063 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.033968 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0738 €) | 0.000033 WETH | 9.75 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.033968 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0738 €) | — | 9.75 | 0.042 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 108.176005 USDC | 0.084924 USDC | 0.000000 USDC | 0.006947 USDC | 0.077977 USDC (0.0717 €) | — | 7.21 | 0.013 (n=64) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52714063 | USDC→[aerodrome_slipstream]→USDbC→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 108.176005 USDC | 0.084924 USDC | 0.000000 USDC | 0.006947 USDC | 0.077977 USDC (0.0717 €) | — | 7.21 | 0.013 (n=64) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 52715594 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 76.615035 USDC | 0.082577 USDC | 0.000000 USDC | 0.005445 USDC | 0.077132 USDC (0.0710 €) | — | 10.07 | 0.003 (n=2) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52720214 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 75.645993 USDC | 0.080996 USDC | 0.000000 USDC | 0.005452 USDC | 0.075544 USDC (0.0695 €) | — | 9.99 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 75.153821 USDC | 0.080784 USDC | 0.000000 USDC | 0.006947 USDC | 0.073837 USDC (0.0679 €) | — | 9.82 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→USDC | 75.153821 USDC | 0.080784 USDC | 0.000000 USDC | 0.006947 USDC | 0.073837 USDC (0.0679 €) | — | 9.82 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52716618 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 70.827384 USDC | 0.073103 USDC | 0.000000 USDC | 0.005456 USDC | 0.067647 USDC (0.0622 €) | — | 9.55 | 0.002 (n=3) | REJECTED | stale_data(7796ms>4000.0), simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 67.381396 USDC | 0.071950 USDC | 0.000000 USDC | 0.006947 USDC | 0.065003 USDC (0.0598 €) | — | 9.65 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |
| 52714063 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 67.381396 USDC | 0.071950 USDC | 0.000000 USDC | 0.006947 USDC | 0.065003 USDC (0.0598 €) | — | 9.65 | 0.042 (n=7) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 718 ; taux observé 0.121 ; borne inférieure crédible (0.9) 0.106 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.6% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
