# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T14:16:08+00:00 ; durée 64.51 min ; blocs 53461072 → 53463009 (1922 vus)

## Connexion
- Requêtes RPC : 21969 ; erreurs : 38 ; latence p50/p95 : 131.5/998.9 ms
- Rafraîchissements d'état : 1923 ; âge des données au dernier bloc : 1.53 s ; changements de frais LP observés (pools à frais dynamiques) : 3976
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15884 ; cycles déclenchés par événement : 988 ; avance médiane sur le rafraîchissement multicall : 449 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,280.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 286 jetons, 19214 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 495, sous le plancher de 10000.0 $ : 3 → gardés 492 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2276.593928, 'cbBTC': 77247.513172, 'AERO': 0.617437}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,166,384 | 2,280.980037 | 53463009 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,435,246 | 0.029542 | 53463009 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,156,619 | 0.029576 | 53463009 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,995,146 | 0.000013 | 53463009 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,916,642 | 2,278.157316 | 53463009 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,713,381 | 103.167987 | 53463009 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,592,257 | 0.001578 | 53463009 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,443,382 | 1.572416 | 53463009 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,806,237 | 0.029553 | 53463009 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,167,809 | 2,277.219842 | 53463009 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,062,865 | 0.999818 | 53463009 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,906,184 | 2,277.337156 | 53463009 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,490,472 | 39,965.973929 | 53463009 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,700,474 | 0.029581 | 53463009 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,162,996 | 1,127,458.546379 | 53463009 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,099,059 | 103.185682 | 53463009 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,808,803 | 0.000013 | 53463009 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,738,261 | 0.017806 | 53463009 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,671,074 | 0.000000 | 53463009 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,635,092 | 0.000013 | 53463009 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,549,933 | 442.001267 | 53463009 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,549,431 | 0.000013 | 53463009 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,556 | 1.442896 | 53463009 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,506,164 | 2,279.491611 | 53463009 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,645 | 0.821370 | 53463009 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,458 | 3,596.255966 | 53463009 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,341,882 | 2,277.750422 | 53463009 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,322,565 | 0.005069 | 53463009 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,319,547 | 2,278.160534 | 53463009 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,286,648 | 14,947.995861 | 53463009 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,233,588 | 0.000013 | 53463009 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,706 | 72.375843 | 53463009 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,120,983 | 36,971,749.322472 | 53463009 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,057,652 | 542,613.463249 | 53463009 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,741 | 21,938,543.803452 | 53463009 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,016,340 | 0.000000 | 53463009 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,003,480 | 18.763391 | 53463009 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 958,124 | 86,460.706547 | 53463009 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 939,403 | 103.747822 | 53463009 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/WELL | 10000 | 931,160 | 1,251,776.267170 | 53463009 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 928,426 | 2,282.122456 | 53463009 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 918,943 | 1,089.256424 | 53463009 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 910,465 | 75.521658 | 53463009 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 886,388 | 0.045296 | 53463009 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 880,735 | 0.000558 | 53463009 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 851,887 | 3,621.623438 | 53463009 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 823,368 | 19.979438 | 53463009 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,508 | 0.056545 | 53463009 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 774,233 | 0.799125 | 53463009 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 728,087 | 0.589198 | 53463009 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 724,149 | 0.000257 | 53463009 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 716,572 | 4,791,523.598101 | 53463009 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 674,927 | 0.000008 | 53463009 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 666,513 | 147,856.833054 | 53463009 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 660,147 | 2.343097 | 53463009 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 657,629 | 0.543960 | 53463009 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 650,323 | 541,194.288279 | 53463009 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 612,733 | 0.914615 | 53463009 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 592,029 | 0.088252 | 53463009 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 565,579 | 0.038671 | 53463009 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 2910 ; routes examinées : 55912740 ; candidats optimisés : 191424 ; net attendu > 0 : 397 ; dernier cycle 268.5 ms
- Rejets (moteur) : {'spread_below_threshold': 54659538, 'liquidity_below_min': 998945, 'negative_expected_net': 191027, 'pool_quarantined': 43706, 'unquotable': 12092, 'cycle_budget_exhausted': 4039, 'borrow_bound_too_small': 2907}
- Enregistrements de la session : 191424 ; net attendu > 0 : 397 ; simulés (eth_call de la vraie tx) : 32 (ok 9, échec 23) ; étiquettes ghost N+1 : 6/28 positives
- Décisions : {'REJECTED': 191424} ; motifs de rejet : {'below_safety_margin': 260, 'negative_expected_net': 191027, 'p_lower_below_threshold': 384, 'price_impact': 8, 'reliability_not_demonstrated': 13, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 23}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,437.832122 USDC | 0.380030 USDC | 0.000000 USDC | 0.005524 USDC | 0.374506 USDC (0.3445 €) | — | 1.54 | 0.035 (n=191) | REJECTED | below_safety_margin(374506<487566), p_lower_below_threshold(0.03<0.75) |
| 53462613 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017895 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2361 €) | — | 1.86 | 0.035 (n=191) | REJECTED | below_safety_margin(332<357), p_lower_below_threshold(0.03<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,456.013948 USDC | 0.261195 USDC | 0.000000 USDC | 0.005177 USDC | 0.256018 USDC (0.2355 €) | — | 1.76 | 0.035 (n=191) | REJECTED | below_safety_margin(256018<291202), p_lower_below_threshold(0.03<0.75) |
| 53462613 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014168 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1693 €) | — | 1.68 | 0.035 (n=191) | REJECTED | below_safety_margin(238<283), p_lower_below_threshold(0.03<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,040.360009 USDC | 0.188515 USDC | 0.000000 USDC | 0.005177 USDC | 0.183338 USDC (0.1687 €) | — | 1.76 | 0.035 (n=191) | REJECTED | below_safety_margin(183338<208072), p_lower_below_threshold(0.03<0.75) |
| 53462614 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.231063 WETH | 0.000080 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1613 €) | — | 3.32 | 0.311 (n=141) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 53462614 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 524.697751 USDC | 0.181245 USDC | 0.000000 USDC | 0.006600 USDC | 0.174645 USDC (0.1607 €) | — | 3.33 | 0.311 (n=141) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 53462792 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 112.493699 USDC | 0.169547 USDC | 0.000000 USDC | 0.005195 USDC | 0.164352 USDC (0.1512 €) | — | 14.61 | 0.000 (n=76) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53462613 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.012254 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1444 €) | — | 1.66 | 0.035 (n=191) | REJECTED | below_safety_margin(203<245), p_lower_below_threshold(0.03<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,008.494084 USDC | 0.161904 USDC | 0.000000 USDC | 0.005177 USDC | 0.156727 USDC (0.1442 €) | — | 1.55 | 0.035 (n=191) | REJECTED | below_safety_margin(156727<201698), p_lower_below_threshold(0.03<0.75) |
| 53462614 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.130254 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000041 WETH (0.0854 €) | — | 3.12 | 0.311 (n=141) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 53462614 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 296.629497 USDC | 0.099020 USDC | 0.000000 USDC | 0.006600 USDC | 0.092420 USDC (0.0850 €) | — | 3.12 | 0.311 (n=141) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 53462614 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.124941 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0704 €) | — | 2.68 | 0.187 (n=842) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53462614 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 285.095701 USDC | 0.083172 USDC | 0.000000 USDC | 0.006915 USDC | 0.076257 USDC (0.0702 €) | — | 2.67 | 0.187 (n=842) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53462614 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.123721 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0680 €) | — | 2.61 | 0.187 (n=842) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53462614 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 281.188127 USDC | 0.080546 USDC | 0.000000 USDC | 0.006915 USDC | 0.073631 USDC (0.0677 €) | — | 2.62 | 0.187 (n=842) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53462614 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.118477 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0655 €) | — | 2.63 | 0.187 (n=842) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53462614 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 268.958104 USDC | 0.077800 USDC | 0.000000 USDC | 0.006915 USDC | 0.070885 USDC (0.0652 €) | — | 2.64 | 0.187 (n=842) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53461592 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 863.053285 USDC | 0.058737 USDC | 0.000000 USDC | 0.005490 USDC | 0.053247 USDC (0.0490 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(53247<172610), p_lower_below_threshold(0.03<0.75) |
| 53461593 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 863.053285 USDC | 0.058737 USDC | 0.000000 USDC | 0.005490 USDC | 0.053247 USDC (0.0490 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(53247<172610), p_lower_below_threshold(0.03<0.75) |
| 53461592 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.378818 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0488 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(23308414488570<75763685316246), p_lower_below_threshold(0.03<0.75) |
| 53461593 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.378818 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0488 €) | — | 0.62 | 0.035 (n=191) | REJECTED | below_safety_margin(23308414488570<75763685316246), p_lower_below_threshold(0.03<0.75) |
| 53462613 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.083039 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0474 €) | — | 2.72 | 0.187 (n=842) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 188.984643 USDC | 0.058279 USDC | 0.000000 USDC | 0.006924 USDC | 0.051355 USDC (0.0472 €) | — | 2.72 | 0.187 (n=842) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53462614 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008180 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0449 €) | — | 0.77 | 0.187 (n=842) | REJECTED | below_safety_margin(63<163), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4863 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
