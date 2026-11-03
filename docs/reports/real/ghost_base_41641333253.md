# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T15:45:44+00:00 ; durée 154.11 min ; blocs 53461072 → 53465695 (4603 vus)

## Connexion
- Requêtes RPC : 53960 ; erreurs : 45 ; latence p50/p95 : 198.0/789.4 ms
- Rafraîchissements d'état : 4603 ; âge des données au dernier bloc : 3.32 s ; changements de frais LP observés (pools à frais dynamiques) : 9074
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55812 ; cycles déclenchés par événement : 3584 ; avance médiane sur le rafraîchissement multicall : 446 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,289.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 286 jetons, 19214 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 495, sous le plancher de 10000.0 $ : 3 → gardés 492 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2276.593928, 'cbBTC': 77247.513172, 'AERO': 0.617437}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,457,573 | 2,289.034584 | 53465696 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,363,698 | 0.029586 | 53465696 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,184,633 | 0.029576 | 53465696 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,992,285 | 0.000013 | 53465696 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,000,480 | 2,291.878506 | 53465696 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,745,135 | 102.990097 | 53465696 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,606,451 | 0.001578 | 53465696 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,439,604 | 1.574506 | 53465696 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,876,044 | 0.029579 | 53465696 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,159,749 | 2,292.250597 | 53465696 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,071,407 | 0.999763 | 53465696 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,915,475 | 2,292.077941 | 53465696 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,447,708 | 41,253.390408 | 53465696 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,708,637 | 0.029581 | 53465696 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,167,726 | 1,130,485.614086 | 53465696 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,108,557 | 102.977455 | 53465696 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,810,307 | 0.000013 | 53465696 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,738,469 | 0.017790 | 53465696 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,680,480 | 0.000000 | 53465696 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,637,511 | 0.000013 | 53465696 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53465696 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,554,721 | 442.662136 | 53465696 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,550,991 | 0.000013 | 53465696 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,825 | 2,288.668704 | 53465696 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,645 | 0.821370 | 53465696 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,437,531 | 3,598.064074 | 53465696 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,344,249 | 2,291.282518 | 53465696 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,342,302 | 2,291.914386 | 53465696 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,585 | 0.005095 | 53465696 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,289,289 | 14,966.261764 | 53465696 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 1,235,616 | 0.000013 | 53465696 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,709 | 72.375481 | 53465696 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,125,595 | 36,906,653.599702 | 53465696 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,061,383 | 542,619.378379 | 53465696 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,975 | 21,938,543.803452 | 53465696 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,019,915 | 0.000000 | 53465696 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,808 | 19.180445 | 53465696 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 959,720 | 86,783.079694 | 53465696 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 945,720 | 102.504595 | 53465696 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/WELL | 10000 | 934,660 | 1,251,209.027974 | 53465696 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 930,680 | 72.276563 | 53465696 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 929,545 | 2,282.122456 | 53465696 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 928,283 | 1,075.222881 | 53465696 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 890,086 | 0.044881 | 53465696 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 877,475 | 0.000553 | 53465696 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 852,568 | 3,621.623438 | 53465696 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 822,953 | 19.994753 | 53465696 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,833 | 0.056744 | 53465696 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 776,960 | 0.799140 | 53465696 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 730,546 | 0.591122 | 53465696 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,929 | 0.000257 | 53465696 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 716,765 | 4,822,908.631512 | 53465696 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 675,141 | 0.000008 | 53465696 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 668,453 | 148,041.110614 | 53465696 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 662,478 | 2.343097 | 53465696 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 658,035 | 0.544597 | 53465696 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 652,618 | 542,610.452133 | 53465696 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,897 | 0.914615 | 53465696 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 587,801 | 0.087303 | 53465696 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 568,323 | 0.038958 | 53465696 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 8186 ; routes examinées : 157285804 ; candidats optimisés : 448994 ; net attendu > 0 : 825 ; dernier cycle 93.1 ms
- Rejets (moteur) : {'spread_below_threshold': 154142510, 'liquidity_below_min': 2608271, 'negative_expected_net': 448169, 'pool_quarantined': 44948, 'unquotable': 28688, 'borrow_bound_too_small': 8181, 'cycle_budget_exhausted': 4212}
- Enregistrements de la session : 448994 ; net attendu > 0 : 825 ; simulés (eth_call de la vraie tx) : 54 (ok 9, échec 45) ; étiquettes ghost N+1 : 6/47 positives
- Décisions : {'REJECTED': 448994} ; motifs de rejet : {'below_safety_margin': 629, 'negative_expected_net': 448169, 'p_lower_below_threshold': 777, 'price_impact': 8, 'reliability_not_demonstrated': 48, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 45}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53463332 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,541.897939 USDC | 0.510453 USDC | 0.000000 USDC | 0.005620 USDC | 0.504833 USDC (0.4644 €) | — | 1.99 | 0.034 (n=196) | REJECTED | below_safety_margin(504833<508379), p_lower_below_threshold(0.03<0.75) |
| 53463333 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 2,541.897939 USDC | 0.510453 USDC | 0.000000 USDC | 0.005620 USDC | 0.504833 USDC (0.4644 €) | — | 1.99 | 0.034 (n=196) | REJECTED | below_safety_margin(504833<508379), p_lower_below_threshold(0.03<0.75) |
| 53463332 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.112655 WETH | 0.000223 WETH | 0.000000 WETH | 0.000002 WETH | 0.000221 WETH (0.4634 €) | — | 1.98 | 0.034 (n=196) | REJECTED | below_safety_margin(220793398221565<222530927350268), p_lower_below_threshold(0.03<0.75) |
| 53463333 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 1.112655 WETH | 0.000223 WETH | 0.000000 WETH | 0.000002 WETH | 0.000221 WETH (0.4634 €) | — | 1.98 | 0.034 (n=196) | REJECTED | below_safety_margin(220793398221565<222530927350268), p_lower_below_threshold(0.03<0.75) |
| 53463325 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 2,161.011839 USDC | 0.458620 USDC | 0.000000 USDC | 0.007599 USDC | 0.451021 USDC (0.4149 €) | — | 2.09 | 0.039 (n=21) | REJECTED | reliability_not_demonstrated |
| 53463325 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.939134 WETH | 0.000201 WETH | 0.000000 WETH | 0.000003 WETH | 0.000197 WETH (0.4144 €) | — | 2.10 | 0.039 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53463325 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.026928 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4142 €) | — | 2.17 | 0.039 (n=21) | REJECTED | reliability_not_demonstrated |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 2,437.832122 USDC | 0.380030 USDC | 0.000000 USDC | 0.005524 USDC | 0.374506 USDC (0.3445 €) | — | 1.54 | 0.035 (n=191) | REJECTED | below_safety_margin(374506<487566), p_lower_below_threshold(0.03<0.75) |
| 53462613 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017895 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2361 €) | — | 1.86 | 0.035 (n=191) | REJECTED | below_safety_margin(332<357), p_lower_below_threshold(0.03<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,456.013948 USDC | 0.261195 USDC | 0.000000 USDC | 0.005177 USDC | 0.256018 USDC (0.2355 €) | — | 1.76 | 0.035 (n=191) | REJECTED | below_safety_margin(256018<291202), p_lower_below_threshold(0.03<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.080292 WETH | 0.000096 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.1953 €) | — | 11.59 | 0.104 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 183.058743 USDC | 0.219783 USDC | 0.000000 USDC | 0.007608 USDC | 0.212175 USDC (0.1952 €) | — | 11.59 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53464609 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.018425 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1948 €) | — | 1.49 | 0.037 (n=22) | REJECTED | below_safety_margin(274<368), reliability_not_demonstrated |
| 53464609 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,469.043519 USDC | 0.219155 USDC | 0.000000 USDC | 0.007595 USDC | 0.211560 USDC (0.1946 €) | — | 1.44 | 0.037 (n=22) | REJECTED | below_safety_margin(211560<293808), reliability_not_demonstrated |
| 53464609 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.631609 WETH | 0.000096 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.1944 €) | — | 1.46 | 0.037 (n=22) | REJECTED | below_safety_margin(92530146250747<126321894567622), reliability_not_demonstrated |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.077981 WETH | 0.000095 WETH | 0.000000 WETH | 0.000003 WETH | 0.000091 WETH (0.1911 €) | — | 11.68 | 0.104 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 177.444601 USDC | 0.215528 USDC | 0.000000 USDC | 0.007954 USDC | 0.207574 USDC (0.1910 €) | — | 11.70 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.078998 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000090 WETH (0.1879 €) | — | 11.33 | 0.104 (n=113) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 179.899012 USDC | 0.211745 USDC | 0.000000 USDC | 0.007608 USDC | 0.204137 USDC (0.1878 €) | — | 11.35 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.078379 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1875 €) | — | 11.40 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 178.637756 USDC | 0.211322 USDC | 0.000000 USDC | 0.007608 USDC | 0.203714 USDC (0.1874 €) | — | 11.40 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.078819 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1867 €) | — | 11.29 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53463086 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 179.287953 USDC | 0.210412 USDC | 0.000000 USDC | 0.007608 USDC | 0.202804 USDC (0.1866 €) | — | 11.31 | 0.104 (n=113) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53462613 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014168 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1693 €) | — | 1.68 | 0.035 (n=191) | REJECTED | below_safety_margin(238<283), p_lower_below_threshold(0.03<0.75) |
| 53462613 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,040.360009 USDC | 0.188515 USDC | 0.000000 USDC | 0.005177 USDC | 0.183338 USDC (0.1687 €) | — | 1.76 | 0.035 (n=191) | REJECTED | below_safety_margin(183338<208072), p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 4882 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
