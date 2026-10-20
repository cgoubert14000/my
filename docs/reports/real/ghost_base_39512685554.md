# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-20T23:32:16+00:00 ; durée 21.3 min ; blocs 52874252 → 52874893 (627 vus)

## Connexion
- Requêtes RPC : 8588 ; erreurs : 0 ; latence p50/p95 : 239.8/1,241.8 ms
- Rafraîchissements d'état : 627 ; âge des données au dernier bloc : 3.1 s ; changements de frais LP observés (pools à frais dynamiques) : 1150
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6386 ; cycles déclenchés par événement : 640 ; avance médiane sur le rafraîchissement multicall : 466 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,451.84 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 581 pools, 328 jetons, 22996 routes
- Par DEX : uniswap_v3 137, aerodrome 236, aerodrome_slipstream 158, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 395, par paires 0), mesurés 583, sous le plancher de 10000.0 $ : 2 → gardés 581 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2453.717243, 'AERO': 0.88311, 'cbBTC': 82924.161646}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,615,135 | 2,451.842822 | 52874894 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 40,340,136 | 1.134121 | 52874894 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 17,965,952 | 96.086515 | 52874894 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,488,415 | 0.029520 | 52874894 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,574,381 | 0.029573 | 52874894 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 10,524,029 | 0.029580 | 52874894 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,939,509 | 0.000012 | 52874894 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,617,536 | 2,445.385870 | 52874894 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,390,659 | 2,452.131666 | 52874894 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 8,202,716 | 0.000012 | 52874894 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 8,125,566 | 0.000012 | 52874894 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/USDC | 549 | 7,757,320 | 2,445.710745 | 52874894 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,308,290 | 0.001676 | 52874894 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,449,448 | 0.029517 | 52874894 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,321,651 | 0.024443 | 52874894 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,734,130 | 0.000275 | 52874894 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,726,057 | 0.802394 | 52874894 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,516,690 | 2,445.458000 | 52874894 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,432,239 | 1.130606 | 52874894 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,408,652 | 0.998741 | 52874894 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDT | 400 | 4,069,764 | 2,448.415219 | 52874894 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,054,674 | 34,681.443630 | 52874894 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,421,978 | 2,777.900257 | 52874894 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,877,190 | 0.000012 | 52874894 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,808,757 | 401.733380 | 52874894 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,747,774 | 96.113983 | 52874894 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,539,955 | 1.142084 | 52874894 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,393,845 | 1,018.783775 | 52874894 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,320,576 | 0.000011 | 52874894 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,252,445 | 1,202,829.379446 | 52874894 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,058,907 | 1.238864 | 52874894 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,920 | 1.383226 | 52874894 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,941,401 | 0.000000 | 52874894 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,919,217 | 1.105602 | 52874894 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,874,083 | 15.794996 | 52874894 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,820,790 | 13,592.503880 | 52874894 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | XDP/USDC | 100 | 1,814,290 | 0.019321 | 52874894 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,777,732 | 0.000012 | 52874894 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | fBOMB/USDC | 10000 | 1,707,304 | 0.021274 | 52874894 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | WETH/AERO | 3000 | 1,692,709 | 2,775.236880 | 52874894 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/msETH (stable) | 500 | 1,692,125 | 2.311063 | 52874894 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,572,181 | 0.916062 | 52874894 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,348 | 0.826534 | 52874894 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,390,983 | 1.123061 | 52874894 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,354,039 | 0.004804 | 52874894 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | DRB/WETH | 10000 | 1,349,464 | 0.000000 | 52874894 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,327,358 | 0.000277 | 52874894 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,313,058 | 0.029584 | 52874894 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,271,466 | 2,445.499427 | 52874894 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,235,879 | 63.619562 | 52874894 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,225,026 | 68,676.475238 | 52874894 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,224,853 | 23.060385 | 52874894 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/doginme | 10000 | 1,224,576 | 34,988,111.001513 | 52874894 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,180,993 | 0.436807 | 52874894 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,172,643 | 493,960.319653 | 52874894 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,170,263 | 0.886344 | 52874894 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome | WETH/WELL | 10000 | 1,169,013 | 1,192,702.567237 | 52874894 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 1,158,697 | 46.931590 | 52874894 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,137,721 | 1.106158 | 52874894 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,105,099 | 20,718,712.259716 | 52874894 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 1266 ; routes examinées : 29112936 ; candidats optimisés : 94442 ; net attendu > 0 : 10 ; dernier cycle 588.5 ms
- Rejets (moteur) : {'spread_below_threshold': 28823918, 'liquidity_below_min': 193310, 'negative_expected_net': 94432, 'borrow_bound_too_small': 1266}
- Enregistrements de la session : 94442 ; net attendu > 0 : 10 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 94442} ; motifs de rejet : {'below_safety_margin': 8, 'negative_expected_net': 94432, 'p_lower_below_threshold': 10, 'simulation_failed': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52874740 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 56.113426 USDC | 0.068550 USDC | 0.000000 USDC | 0.005508 USDC | 0.063042 USDC (0.0580 €) | — | 11.23 | 0.000 (n=40) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52874885 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 48.343861 USDC | 0.033265 USDC | 0.000000 USDC | 0.005507 USDC | 0.027758 USDC (0.0255 €) | — | 5.74 | 0.000 (n=95) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52874437 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.262013 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0107 €) | — | 0.18 | 0.014 (n=57) | REJECTED | below_safety_margin(4720184346016<52402566328709), p_lower_below_threshold(0.01<0.75) |
| 52874437 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.262013 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0107 €) | — | 0.18 | 0.014 (n=57) | REJECTED | below_safety_margin(4720184346016<52402566328709), p_lower_below_threshold(0.01<0.75) |
| 52874437 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 636.437210 USDC | 0.017047 USDC | 0.000000 USDC | 0.005514 USDC | 0.011533 USDC (0.0106 €) | — | 0.18 | 0.014 (n=57) | REJECTED | below_safety_margin(11533<127287), p_lower_below_threshold(0.01<0.75) |
| 52874437 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 636.437210 USDC | 0.017047 USDC | 0.000000 USDC | 0.005514 USDC | 0.011533 USDC (0.0106 €) | — | 0.18 | 0.014 (n=57) | REJECTED | below_safety_margin(11533<127287), p_lower_below_threshold(0.01<0.75) |
| 52874437 | WETH→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.025219 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 0.18 | 0.121 (n=191) | REJECTED | below_safety_margin(444549970633<5043881386650), p_lower_below_threshold(0.12<0.75) |
| 52874437 | WETH→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.025219 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0010 €) | — | 0.18 | 0.121 (n=191) | REJECTED | below_safety_margin(444549970633<5043881386650), p_lower_below_threshold(0.12<0.75) |
| 52874437 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→USDC | 61.585579 USDC | 0.008445 USDC | 0.000000 USDC | 0.007380 USDC | 0.001065 USDC (0.0010 €) | — | 0.17 | 0.121 (n=191) | REJECTED | below_safety_margin(1065<12317), p_lower_below_threshold(0.12<0.75) |
| 52874437 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→oUSDT→[aerodrome_slipstream]→USDC | 61.585579 USDC | 0.008445 USDC | 0.000000 USDC | 0.007380 USDC | 0.001065 USDC (0.0010 €) | — | 0.17 | 0.121 (n=191) | REJECTED | below_safety_margin(1065<12317), p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 1569 ; taux observé 0.103 ; borne inférieure crédible (0.9) 0.094 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
