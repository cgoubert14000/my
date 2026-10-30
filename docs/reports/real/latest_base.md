# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T00:19:33+00:00 ; durée 207.95 min ; blocs 53258868 → 53265101 (5780 vus)

## Connexion
- Requêtes RPC : 68576 ; erreurs : 15 ; latence p50/p95 : 258.2/2,568.1 ms
- Rafraîchissements d'état : 5780 ; âge des données au dernier bloc : 4.1 s ; changements de frais LP observés (pools à frais dynamiques) : 19348
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 178681 ; cycles déclenchés par événement : 5324 ; avance médiane sur le rafraîchissement multicall : 1,184 ms
- Gaz : base fee 0.011928 gwei ; prix ETH (pool le plus profond) : 2,234.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 499 pools, 290 jetons, 18414 routes
- Par DEX : uniswap_v3 138 (quarantaine 1), aerodrome_slipstream 113 (quarantaine 2), aerodrome 207, pancakeswap_v3 27 (quarantaine 2), uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 319, par paires 0), mesurés 502, sous le plancher de 10000.0 $ : 3 → gardés 499 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2268.963647, 'cbBTC': 79202.631326, 'AERO': 0.656707}
- Pools en quarantaine : 5 — aerodrome_slipstream:WETH/USDT@0x9785eF: simulation failed ×5 (model/chain mismatch) — until block 53265396; uniswap_v3:WETH/USDT@0xd92E07: simulation failed ×5 (model/chain mismatch) — until block 53265397; pancakeswap_v3:VIRTUAL/USDC@0x7CB770: simulation failed ×5 (model/chain mismatch) — until block 53265388; aerodrome_slipstream:VIRTUAL/WETH@0xC200F2: simulation failed ×5 (model/chain mismatch) — until block 53265388; pancakeswap_v3:USDC/USDT@0x5f07bb: simulation failed ×5 (model/chain mismatch) — until block 53265397

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,698,974 | 2,234.017481 | 53265105 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,978,294 | 0.028867 | 53265105 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,538,096 | 0.000013 | 53265105 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,047,692 | 0.028854 | 53265105 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,055,582 | 2,231.250631 | 53265105 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,765,600 | 100.281530 | 53265105 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,634,512 | 0.001588 | 53265105 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,052,562 | 1.625011 | 53265105 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,587,834 | 0.028856 | 53265105 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,264,819 | 2,230.490679 | 53265105 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,245,480 | 2,231.104811 | 53265105 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,526,647 | 37,555.945226 | 53265105 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 3,304,422 | 1.000563 | 53265105 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/cbBTC | 2545 | 2,775,227 | 0.028840 | 53265105 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2820 | 2,301,909 | 100.297304 | 53265105 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,043,830 | 1,211,303.220815 | 53265105 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 2,029,213 | 0.000013 | 53265105 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,764,657 | 0.018172 | 53265105 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,695,243 | 2,225.254756 | 53265105 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,681,484 | 0.000000 | 53265105 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,671,149 | 424.420037 | 53265105 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,664,485 | 0.000013 | 53265105 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,659,266 | 0.000013 | 53265105 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 404 | 1,566,117 | 0.000013 | 53265105 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,118 | 1.588216 | 53265105 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,578 | 0.827498 | 53265105 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,339,311 | 3,619.528582 | 53265105 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,309,956 | 0.005181 | 53265105 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,298,150 | 14,678.064742 | 53265105 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,214,872 | 2,231.261188 | 53265105 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,179,787 | 69.812777 | 53265105 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,149,642 | 0.000248 | 53265105 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | WETH/doginme | 10000 | 1,094,174 | 37,268,590.268244 | 53265105 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,044,694 | 527,322.846605 | 53265105 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,026,642 | 72,324.661456 | 53265105 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,651 | 2,230.208752 | 53265105 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,005,468 | 22,021,438.837002 | 53265105 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,001,183 | 18.884210 | 53265105 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 971,900 | 1,104,685.602236 | 53265105 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 965,232 | 0.000249 | 53265105 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | DRB/WETH | 10000 | 965,046 | 0.000000 | 53265105 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 963,334 | 0.045185 | 53265105 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 949,480 | 100.608452 | 53265105 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 943,021 | 70.394583 | 53265105 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 942,015 | 3,603.586478 | 53265105 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/USDC | 10000 | 918,156 | 2,247.123561 | 53265105 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 884,851 | 1,057.829578 | 53265105 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 853,064 | 0.000546 | 53265105 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4790 | 840,364 | 19.333962 | 53265105 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 839,166 | 0.063550 | 53265105 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 756,176 | 0.803616 | 53265105 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 746,177 | 19.024892 | 53265105 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 709,526 | 4,682,065.375897 | 53265105 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 687,961 | 0.000008 | 53265105 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 683,322 | 0.553334 | 53265105 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | WETH/msETH (stable) | 500 | 680,197 | 2.332398 | 53265105 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 651,797 | 148,008.125551 | 53265105 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2426 | 646,401 | 531,735.954360 | 53265105 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 637,511 | 0.513797 | 53265105 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 605,091 | 0.091475 | 53265105 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 11101 ; routes examinées : 204413814 ; candidats optimisés : 1267904 ; net attendu > 0 : 3087 ; dernier cycle 897.1 ms
- Rejets (moteur) : {'spread_below_threshold': 199734696, 'liquidity_below_min': 3357547, 'negative_expected_net': 1264817, 'cycle_budget_exhausted': 17569, 'unquotable': 17310, 'borrow_bound_too_small': 11088, 'pool_quarantined': 7700}
- Enregistrements de la session : 1267904 ; net attendu > 0 : 3087 ; simulés (eth_call de la vraie tx) : 131 (ok 52, échec 79) ; étiquettes ghost N+1 : 34/119 positives
- Décisions : {'REJECTED': 1267904} ; motifs de rejet : {'below_safety_margin': 2383, 'negative_expected_net': 1264817, 'p_lower_below_threshold': 2666, 'price_impact': 10, 'reliability_not_demonstrated': 421, 'sim_below_estimate': 8, 'simulated_net_nonpositive': 6, 'simulation_failed': 79, 'stale_data': 114}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.087669 WETH | 0.007300 WETH | 0.000000 WETH | 0.000018 WETH | 0.007282 WETH (15.2342 €) | — | 830.57 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.083895 WETH | 0.006985 WETH | 0.000000 WETH | 0.000018 WETH | 0.006967 WETH (14.5760 €) | — | 830.43 | 0.002 (n=3) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 194.516486 USDC | 15.588983 USDC | 0.000000 USDC | 0.042064 USDC | 15.546919 USDC (14.3032 €) | — | 799.26 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.074170 WETH | 0.006048 WETH | 0.000000 WETH | 0.000018 WETH | 0.006030 WETH (12.6155 €) | — | 812.97 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.073121 WETH | 0.005996 WETH | 0.000000 WETH | 0.000018 WETH | 0.005978 WETH (12.5070 €) | — | 817.55 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.071054 WETH | 0.005909 WETH | 0.000000 WETH | 0.000018 WETH | 0.005891 WETH (12.3250 €) | — | 829.09 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.070554 WETH | 0.005753 WETH | 0.000000 WETH | 0.000018 WETH | 0.005735 WETH (11.9978 €) | — | 812.79 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.069593 WETH | 0.005707 WETH | 0.000000 WETH | 0.000018 WETH | 0.005688 WETH (11.9009 €) | — | 817.36 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 158.488819 USDC | 12.466653 USDC | 0.000000 USDC | 0.041719 USDC | 12.424934 USDC (11.4309 €) | — | 783.96 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v2]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.066843 WETH | 0.005450 WETH | 0.000000 WETH | 0.000018 WETH | 0.005432 WETH (11.3656 €) | — | 812.72 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome]→USDC | 160.275220 USDC | 12.199157 USDC | 0.000000 USDC | 0.041750 USDC | 12.157407 USDC (11.1848 €) | — | 758.53 | 0.002 (n=5) | REJECTED | reliability_not_demonstrated |
| 53259987 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.001836 cbBTC | 0.000141 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC | 0.000141 cbBTC (10.2641 €) | — | 767.17 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.059219 WETH | 0.004823 WETH | 0.000000 WETH | 0.000018 WETH | 0.004804 WETH (10.0519 €) | — | 811.30 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.058561 WETH | 0.004796 WETH | 0.000000 WETH | 0.000018 WETH | 0.004778 WETH (9.9962 €) | — | 815.87 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.057714 WETH | 0.004686 WETH | 0.000000 WETH | 0.000018 WETH | 0.004667 WETH (9.7649 €) | — | 808.70 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→USDC | 122.415685 USDC | 9.647129 USDC | 0.000000 USDC | 0.041405 USDC | 9.605724 USDC (8.8373 €) | — | 784.68 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53260683 | USDC→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 1,195.188380 USDC | 9.477670 USDC | 0.000000 USDC | 0.020085 USDC | 9.457585 USDC (8.7010 €) | — | 79.13 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v2]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.051575 WETH | 0.004117 WETH | 0.000000 WETH | 0.000018 WETH | 0.004099 WETH (8.5752 €) | — | 794.71 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v2]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.050859 WETH | 0.004083 WETH | 0.000000 WETH | 0.000018 WETH | 0.004065 WETH (8.5045 €) | — | 799.25 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53259987 | USDC→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome]→USDC | 119.707043 USDC | 8.934374 USDC | 0.000000 USDC | 0.041405 USDC | 8.892969 USDC (8.1815 €) | — | 742.89 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→WETH | 0.043965 WETH | 0.003494 WETH | 0.000000 WETH | 0.000018 WETH | 0.003475 WETH (7.2710 €) | — | 790.48 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53259987 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.043444 WETH | 0.003472 WETH | 0.000000 WETH | 0.000018 WETH | 0.003454 WETH (7.2261 €) | — | 795.02 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53260683 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 739.515088 USDC | 7.619124 USDC | 0.000000 USDC | 0.019190 USDC | 7.599934 USDC (6.9919 €) | — | 102.77 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53260683 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH | 0.324836 WETH | 0.003347 WETH | 0.000000 WETH | 0.000008 WETH | 0.003338 WETH (6.9771 €) | — | 102.77 | 0.000 (n=26) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53259987 | cbBTC→[aerodrome]→VIRTUAL→[aerodrome]→AERO→[uniswap_v3]→cbBTC | 0.001157 cbBTC | 0.000095 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC | 0.000095 cbBTC (6.9110 €) | — | 819.89 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3371 ; taux observé 0.113 ; borne inférieure crédible (0.9) 0.106 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
