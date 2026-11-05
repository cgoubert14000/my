# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T15:17:23+00:00 ; durée 308.9 min ; blocs 53541978 → 53551243 (9186 vus)

## Connexion
- Requêtes RPC : 107972 ; erreurs : 13 ; latence p50/p95 : 115.3/864.1 ms
- Rafraîchissements d'état : 9186 ; âge des données au dernier bloc : 4.57 s ; changements de frais LP observés (pools à frais dynamiques) : 16421
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 81199 ; cycles déclenchés par événement : 7997 ; avance médiane sur le rafraîchissement multicall : 515 ms
- Gaz : base fee 0.015309 gwei ; prix ETH (pool le plus profond) : 2,313.77 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 288 jetons, 19416 routes
- Par DEX : uniswap_v3 142, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 310, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2417.172064, 'cbBTC': 80337.642272, 'AERO': 0.664358}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,518,135 | 2,313.774541 | 53551242 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,811,568 | 0.029918 | 53551243 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,291,958 | 0.029949 | 53551242 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,055,398 | 0.000013 | 53551243 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,072,121 | 2,315.741641 | 53551243 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,512,989 | 110.904994 | 53551242 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,532,426 | 0.001547 | 53551242 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,191,590 | 1.637807 | 53551242 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,142,795 | 0.029906 | 53551243 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,173,198 | 2,316.798828 | 53551243 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,072,828 | 0.998760 | 53551242 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,443,175 | 42,260.933363 | 53551242 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 788 | 3,352,176 | 2,316.394585 | 53551243 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2605 | 2,634,288 | 0.029876 | 53551242 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,162,626 | 1,160,500.715180 | 53551242 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,815,999 | 0.007059 | 53551242 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,787,734 | 0.000013 | 53551243 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,689,281 | 0.000000 | 53551242 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,666,064 | 0.016779 | 53551243 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,647,116 | 0.000013 | 53551243 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,563,942 | 450.360515 | 53551243 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,549,151 | 1.432376 | 53551242 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,530,875 | 0.000013 | 53551243 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,076 | 0.817054 | 53551242 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,406,569 | 3,787.366994 | 53551242 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,348,170 | 2,310.309814 | 53551242 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,347,752 | 2,310.841559 | 53551242 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,286,143 | 15,087.844775 | 53551242 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,220,608 | 2,315.647052 | 53551243 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,151,099 | 73.335477 | 53551242 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,129,586 | 37,667,688.172912 | 53551242 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,059,093 | 0.000000 | 53551242 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/VVV | 10000 | 1,050,632 | 110.474030 | 53551242 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,047,724 | 578,268.634530 | 53551242 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,018,719 | 23,003,409.905224 | 53551242 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 986,134 | 64.477869 | 53551242 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 974,747 | 20.423469 | 53551242 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 947,888 | 1,082.419474 | 53551242 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 947,213 | 2,330.326029 | 53551242 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 937,848 | 0.000013 | 53551243 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 907,164 | 99,235.318393 | 53551242 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 881,134 | 0.000544 | 53551242 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 859,086 | 0.047797 | 53551242 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 815,771 | 3,778.476022 | 53551242 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 800,185 | 0.057382 | 53551242 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4825 | 797,510 | 20.968963 | 53551242 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 785,470 | 0.798912 | 53551242 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 716,420 | 0.566217 | 53551242 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 707,938 | 5,053,867.691143 | 53551242 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 696,854 | 0.000246 | 53551242 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 693,635 | 140,598.891959 | 53551242 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 661,675 | 0.000008 | 53551243 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 656,493 | 0.546090 | 53551242 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2168 | 638,362 | 579,569.396191 | 53551242 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 621,002 | 0.914182 | 53551242 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 617,539 | 2.478123 | 53551242 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 583,359 | 0.086202 | 53551242 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | cbBTC/EDGE | 7000 | 555,423 | 819,165.401801 | 53551242 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,350 | 0.037433 | 53551242 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 542,730 | 6,665.160704 | 53551242 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 17182 ; routes examinées : 333605712 ; candidats optimisés : 1009869 ; net attendu > 0 : 2302 ; dernier cycle 616.3 ms
- Rejets (moteur) : {'spread_below_threshold': 327845340, 'liquidity_below_min': 4717914, 'negative_expected_net': 1007567, 'borrow_bound_too_small': 17159, 'cycle_budget_exhausted': 10162, 'pool_quarantined': 5268}
- Enregistrements de la session : 1009869 ; net attendu > 0 : 2302 ; simulés (eth_call de la vraie tx) : 147 (ok 103, échec 44) ; étiquettes ghost N+1 : 25/130 positives
- Décisions : {'REJECTED': 1009869} ; motifs de rejet : {'below_safety_margin': 1498, 'negative_expected_net': 1007567, 'p_lower_below_threshold': 2069, 'price_impact': 2, 'reliability_not_demonstrated': 233, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 44, 'stale_data': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53545322 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 275.403994 USDC | 1.039397 USDC | 0.000000 USDC | 0.005442 USDC | 1.033955 USDC (0.9512 €) | — | 37.54 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53546498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.562613 WETH | 0.000210 WETH | 0.000000 WETH | 0.000003 WETH | 0.000207 WETH (0.4585 €) | — | 3.68 | 0.029 (n=289) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53546498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,348.351386 USDC | 0.502972 USDC | 0.000000 USDC | 0.006547 USDC | 0.496425 USDC (0.4567 €) | — | 3.68 | 0.029 (n=289) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53550662 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.053100 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4182 €) | — | 1.09 | 0.176 (n=947) | REJECTED | below_safety_margin(580<1061), p_lower_below_threshold(0.18<0.75) |
| 53550662 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 1.811073 WETH | 0.000197 WETH | 0.000000 WETH | 0.000004 WETH | 0.000193 WETH (0.4175 €) | — | 1.07 | 0.176 (n=947) | REJECTED | below_safety_margin(193493367157033<362214623988788), p_lower_below_threshold(0.18<0.75) |
| 53550662 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 4,161.444678 USDC | 0.461401 USDC | 0.000000 USDC | 0.008525 USDC | 0.452876 USDC (0.4166 €) | — | 1.09 | 0.176 (n=947) | REJECTED | below_safety_margin(452876<832288), p_lower_below_threshold(0.18<0.75) |
| 53551210 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.840294 WETH | 0.000196 WETH | 0.000000 WETH | 0.000009 WETH | 0.000188 WETH (0.3992 €) | — | 2.23 | 0.034 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53551210 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,951.554074 USDC | 0.454194 USDC | 0.000000 USDC | 0.020433 USDC | 0.433761 USDC (0.3991 €) | — | 2.22 | 0.034 (n=24) | REJECTED | reliability_not_demonstrated |
| 53551210 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,354.875003 USDC | 0.453107 USDC | 0.000000 USDC | 0.019560 USDC | 0.433547 USDC (0.3989 €) | — | 3.20 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53551210 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.025124 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3988 €) | — | 2.24 | 0.034 (n=24) | REJECTED | reliability_not_demonstrated |
| 53551210 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.568824 WETH | 0.000196 WETH | 0.000000 WETH | 0.000008 WETH | 0.000187 WETH (0.3985 €) | — | 3.29 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53551210 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.016912 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3981 €) | — | 3.32 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53551210 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.576480 WETH | 0.000185 WETH | 0.000000 WETH | 0.000008 WETH | 0.000177 WETH (0.3761 €) | — | 3.07 | 0.152 (n=721) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53551210 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,357.178026 USDC | 0.428231 USDC | 0.000000 USDC | 0.019560 USDC | 0.408671 USDC (0.3760 €) | — | 3.01 | 0.152 (n=721) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551210 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.016538 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3754 €) | — | 3.20 | 0.152 (n=721) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53551210 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,903.436419 USDC | 0.423327 USDC | 0.000000 USDC | 0.020433 USDC | 0.402894 USDC (0.3707 €) | — | 2.12 | 0.173 (n=963) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53551210 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.840087 WETH | 0.000183 WETH | 0.000000 WETH | 0.000009 WETH | 0.000174 WETH (0.3706 €) | — | 2.07 | 0.173 (n=963) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53551210 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.023948 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3705 €) | — | 2.18 | 0.173 (n=963) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53546498 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.973775 WETH | 0.000165 WETH | 0.000000 WETH | 0.000003 WETH | 0.000162 WETH (0.3595 €) | — | 1.67 | 0.040 (n=230) | REJECTED | below_safety_margin(162364200074970<194755001232002), p_lower_below_threshold(0.04<0.75) |
| 53546498 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,330.456691 USDC | 0.395369 USDC | 0.000000 USDC | 0.006182 USDC | 0.389187 USDC (0.3581 €) | — | 1.67 | 0.040 (n=230) | REJECTED | below_safety_margin(389187<466091), p_lower_below_threshold(0.04<0.75) |
| 53544070 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 5,239.460210 USDC | 0.370578 USDC | 0.000000 USDC | 0.006166 USDC | 0.364412 USDC (0.3353 €) | — | 0.70 | 0.033 (n=63) | REJECTED | below_safety_margin(364412<1047892), p_lower_below_threshold(0.03<0.75) |
| 53550913 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.024134 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2489 €) | — | 1.44 | 0.176 (n=949) | REJECTED | below_safety_margin(348<482), p_lower_below_threshold(0.18<0.75) |
| 53550913 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.817065 WETH | 0.000120 WETH | 0.000000 WETH | 0.000004 WETH | 0.000116 WETH (0.2486 €) | — | 1.42 | 0.176 (n=949) | REJECTED | below_safety_margin(116065972363841<163413025652921), p_lower_below_threshold(0.18<0.75) |
| 53550913 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,928.914252 USDC | 0.279493 USDC | 0.000000 USDC | 0.010008 USDC | 0.269485 USDC (0.2479 €) | — | 1.40 | 0.176 (n=949) | REJECTED | below_safety_margin(269485<385782), p_lower_below_threshold(0.18<0.75) |
| 53550616 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.712508 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000098 WETH (0.2114 €) | — | 1.37 | 0.176 (n=947) | REJECTED | below_safety_margin(97832523416394<142501557658349), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 5597 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
