# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-17T16:14:08+00:00 ; durée 6.05 min ; blocs 52731965 → 52732150 (180 vus)

## Connexion
- Requêtes RPC : 2500 ; erreurs : 0 ; latence p50/p95 : 222.7/1,499.9 ms
- Rafraîchissements d'état : 180 ; âge des données au dernier bloc : 2.79 s ; changements de frais LP observés (pools à frais dynamiques) : 169
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2778 ; cycles déclenchés par événement : 239 ; avance médiane sur le rafraîchissement multicall : 354 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,411.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 576 pools, 328 jetons, 21110 routes
- Par DEX : uniswap_v3 136, aerodrome 235, aerodrome_slipstream 156, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 207 (rejetés 2) → 612 jetons ; pools candidats 3916 (énumérés 393, par paires 0), mesurés 578, sous le plancher de 10000.0 $ : 2 → gardés 576 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2411.894998, 'AERO': 0.849168, 'cbBTC': 81312.167025}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,230,517 | 2,411.894999 | 52732150 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 42,100,662 | 1.177623 | 52732150 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,199,021 | 0.029637 | 52732150 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 18,120,620 | 0.029677 | 52732150 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/VVV | 3000 | 15,791,175 | 107.291033 | 52732150 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,431,356 | 0.029691 | 52732150 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,753,671 | 0.000012 | 52732150 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 9,305,600 | 0.000012 | 52732150 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 9,090,666 | 2,409.642030 | 52732150 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | WETH/USDC | 594 | 7,906,782 | 2,410.480330 | 52732150 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,840,789 | 0.000012 | 52732150 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,135,975 | 0.001665 | 52732150 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | WETH/USDC | 3000 | 5,403,142 | 2,412.354576 | 52732150 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,323,773 | 0.029646 | 52732150 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,242,830 | 0.025339 | 52732150 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/superOETHb | 400 | 5,237,600 | 1.000855 | 52732150 | `0x6446021F4E396dA3df4235C62537431372195D38` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,821,022 | 0.802398 | 52732150 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,639,408 | 0.000273 | 52732150 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,501,654 | 1.171051 | 52732150 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,419,355 | 0.998801 | 52732150 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,389,530 | 2,410.601763 | 52732150 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 4,027,264 | 34,018.883140 | 52732150 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,391,162 | 2,820.054675 | 52732150 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/USDT | 406 | 3,068,904 | 2,413.772020 | 52732150 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,911,356 | 1.141792 | 52732150 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,837,058 | 0.000012 | 52732150 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,678,909 | 0.000010 | 52732150 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,608,345 | 407.158984 | 52732150 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,557,950 | 107.291363 | 52732150 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,234,908 | 1,182,290.188062 | 52732150 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | EURC/USDC | 70 | 2,126,019 | 1.123561 | 52732150 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,107,462 | 1.199039 | 52732150 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 1,998,480 | 1.418053 | 52732150 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,896,181 | 15.777593 | 52732150 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | fBOMB/USDC | 10000 | 1,821,232 | 0.022096 | 52732150 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,806,082 | 0.000000 | 52732150 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,404 | 0.000012 | 52732150 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,737,830 | 0.018109 | 52732150 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/msETH (stable) | 500 | 1,670,109 | 2.306138 | 52732150 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,658,235 | 13,732.710662 | 52732150 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,541,540 | 0.916547 | 52732150 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | WETH/AERO | 3000 | 1,522,779 | 2,838.465841 | 52732150 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,510,911 | 1.105495 | 52732150 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,475,507 | 2,839.620112 | 52732150 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,780 | 0.825404 | 52732150 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | DRB/WETH | 10000 | 1,358,784 | 0.000000 | 52732150 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,326,864 | 0.435603 | 52732150 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | WETH/MORPHO | 2748 | 1,325,495 | 1,027.604222 | 52732150 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,306,989 | 0.004696 | 52732150 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,300,252 | 0.000272 | 52732150 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,260,918 | 1.131432 | 52732150 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| aerodrome | USDC/SEND | 3000 | 1,248,708 | 62.319117 | 52732150 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,247,376 | 23.342754 | 52732150 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/cbBTC | 3000 | 1,230,487 | 0.029692 | 52732150 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,216,637 | 1.105716 | 52732150 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/doginme | 10000 | 1,195,196 | 35,598,184.590662 | 52732150 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,181,855 | 2,409.647599 | 52732150 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/WELL | 10000 | 1,171,058 | 1,150,326.144335 | 52732150 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,138,969 | 510,422.916985 | 52732150 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,119,176 | 14.101459 | 52732150 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |

## Recherche d'opportunités
- Cycles : 418 ; routes examinées : 8823980 ; candidats optimisés : 38055 ; net attendu > 0 : 7 ; dernier cycle 263.4 ms
- Rejets (moteur) : {'spread_below_threshold': 8739876, 'liquidity_below_min': 45631, 'negative_expected_net': 38048, 'borrow_bound_too_small': 418}
- Enregistrements de la session : 38055 ; net attendu > 0 : 7 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 38055} ; motifs de rejet : {'below_safety_margin': 4, 'negative_expected_net': 38048, 'p_lower_below_threshold': 2, 'reliability_not_demonstrated': 5, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52732142 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 66.177836 USDC | 0.061275 USDC | 0.000000 USDC | 0.005418 USDC | 0.055857 USDC (0.0514 €) | — | 8.44 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52732133 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 63.237107 USDC | 0.055672 USDC | 0.000000 USDC | 0.005417 USDC | 0.050255 USDC (0.0462 €) | — | 7.95 | 0.000 (n=39) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52731994 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.123984 USDC | 0.035056 USDC | 0.000000 USDC | 0.005418 USDC | 0.029638 USDC (0.0273 €) | — | 6.03 | 0.000 (n=38) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52732109 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 25.543389 USDC | 0.009270 USDC | 0.000000 USDC | 0.005418 USDC | 0.003852 USDC (0.0035 €) | — | 1.51 | 0.039 (n=21) | REJECTED | below_safety_margin(3852<5108), reliability_not_demonstrated |
| 52732048 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 22.379814 USDC | 0.007324 USDC | 0.000000 USDC | 0.005419 USDC | 0.001905 USDC (0.0018 €) | — | 0.85 | 0.039 (n=21) | REJECTED | below_safety_margin(1905<4475), reliability_not_demonstrated |
| 52732053 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 22.177216 USDC | 0.007079 USDC | 0.000000 USDC | 0.005419 USDC | 0.001660 USDC (0.0015 €) | — | 0.75 | 0.039 (n=21) | REJECTED | below_safety_margin(1660<4435), reliability_not_demonstrated |
| 52732123 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 20.453823 USDC | 0.005927 USDC | 0.000000 USDC | 0.005417 USDC | 0.000510 USDC (0.0005 €) | — | 0.25 | 0.039 (n=21) | REJECTED | below_safety_margin(510<4090), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 744 ; taux observé 0.122 ; borne inférieure crédible (0.9) 0.108 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.8% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
