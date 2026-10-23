# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-23T16:06:28+00:00 ; durée 187.0 min ; blocs 52985506 → 52991115 (5086 vus)

## Connexion
- Requêtes RPC : 63765 ; erreurs : 218 ; latence p50/p95 : 301.8/1,715.6 ms
- Rafraîchissements d'état : 5087 ; âge des données au dernier bloc : 2.02 s ; changements de frais LP observés (pools à frais dynamiques) : 14266
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 104207 ; cycles déclenchés par événement : 4765 ; avance médiane sur le rafraîchissement multicall : 682 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,402.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 544 pools, 316 jetons, 19376 routes
- Par DEX : uniswap_v3 137, aerodrome 221, aerodrome_slipstream 137, pancakeswap_v3 32, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 200 (rejetés 2) → 605 jetons ; pools candidats 3880 (énumérés 358, par paires 0), mesurés 546, sous le plancher de 10000.0 $ : 2 → gardés 544 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2396.209038, 'AERO': 0.783075, 'cbBTC': 81657.338706}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,103,564 | 2,402.556883 | 52991115 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,555,358 | 0.029479 | 52991115 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 12,858,324 | 92.554807 | 52991115 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 10,548,436 | 1.341123 | 52991115 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,288,496 | 0.029417 | 52991115 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,770,930 | 0.000012 | 52991115 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 8,865,045 | 0.029432 | 52991115 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/USDC | 500 | 8,697,058 | 2,404.733226 | 52991115 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,168,888 | 0.001675 | 52991115 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 6,349,435 | 0.000012 | 52991115 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,532,886 | 2,405.575785 | 52991115 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,449,795 | 0.029470 | 52991115 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 4,932,600 | 0.000012 | 52991115 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,554,826 | 2,405.696668 | 52991115 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,289,286 | 0.999611 | 52991115 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/USDC | 3000 | 4,240,629 | 2,404.446266 | 52991115 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | WETH/KTA | 3000 | 3,995,618 | 34,258.388008 | 52991115 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | VIRTUAL/WETH | 10000 | 3,404,675 | 0.000274 | 52991115 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 406 | 2,804,662 | 2,408.828830 | 52991115 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,558,217 | 92.511213 | 52991115 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,316,196 | 391.636191 | 52991115 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,215,886 | 1,191,849.648555 | 52991115 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/AERO | 10000 | 2,061,281 | 3,249.818038 | 52991115 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,988,810 | 0.000000 | 52991115 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,931,510 | 0.000012 | 52991115 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,542 | 0.017973 | 52991115 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,745,817 | 0.000012 | 52991115 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,556,011 | 1.605522 | 52991115 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,514,457 | 3,226.820570 | 52991115 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,823 | 0.824328 | 52991115 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,419,814 | 13,301.972713 | 52991115 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,393,083 | 0.005092 | 52991115 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | WETH/msETH (stable) | 500 | 1,299,158 | 2.321567 | 52991115 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,297,207 | 0.000276 | 52991115 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,294,825 | 2,404.672154 | 52991115 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,264,600 | 0.000000 | 52991115 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/SEND | 3000 | 1,228,362 | 64.400566 | 52991115 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,181,082 | 36,400,933.786169 | 52991115 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,163,274 | 1,124,543.852204 | 52991115 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,154,688 | 488,458.751080 | 52991115 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,141,937 | 16.331838 | 52991115 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | USDC/NOCK | 3000 | 1,129,586 | 49.101845 | 52991115 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,092,314 | 74,192.309682 | 52991115 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 1,087,375 | 0.038496 | 52991115 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,080,080 | 20,844,355.320413 | 52991115 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,055,254 | 16.333725 | 52991115 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 985,157 | 23.115860 | 52991115 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| uniswap_v3 | WETH/MORPHO | 3000 | 957,634 | 1,057.400000 | 52991115 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 939,976 | 2,390.810405 | 52991115 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 913,803 | 0.000542 | 52991115 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 901,848 | 0.000009 | 52991115 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 891,433 | 17.518047 | 52991115 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 859,655 | 2,405.390508 | 52991115 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | weETH_04c0/WETH | 500 | 833,446 | 1.105789 | 52991115 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 814,081 | 0.803225 | 52991115 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 810,721 | 0.059086 | 52991115 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 778,476 | 4,494,291.644748 | 52991115 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 778,404 | 0.662836 | 52991115 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 730,436 | 0.668963 | 52991115 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 730,181 | 136,143.883877 | 52991115 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |

## Recherche d'opportunités
- Cycles : 9851 ; routes examinées : 190872976 ; candidats optimisés : 1002304 ; net attendu > 0 : 1097 ; dernier cycle 218.1 ms
- Rejets (moteur) : {'spread_below_threshold': 187857677, 'liquidity_below_min': 1965890, 'negative_expected_net': 1001207, 'pool_quarantined': 31014, 'borrow_bound_too_small': 9851, 'cycle_budget_exhausted': 6240}
- Enregistrements de la session : 1002304 ; net attendu > 0 : 1097 ; simulés (eth_call de la vraie tx) : 57 (ok 14, échec 43) ; étiquettes ghost N+1 : 6/51 positives
- Décisions : {'REJECTED': 1002304} ; motifs de rejet : {'below_safety_margin': 819, 'negative_expected_net': 1001207, 'p_lower_below_threshold': 873, 'price_impact': 1, 'reliability_not_demonstrated': 224, 'sim_below_estimate': 8, 'simulated_net_nonpositive': 1, 'simulation_failed': 43, 'stale_data': 134}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52987767 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 4.058687 WETH | 0.016727 WETH | 0.000000 WETH | 0.000003 WETH | 0.016724 WETH (36.9677 €) | — | 41.20 | 0.003 (n=87) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52987767 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 9,741.383658 USDC | 40.147923 USDC | 0.000000 USDC | 0.007556 USDC | 40.140367 USDC (36.9291 €) | — | 41.21 | 0.003 (n=87) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52987767 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 4.060982 WETH | 0.016667 WETH | 0.000000 WETH | 0.000003 WETH | 0.016664 WETH (36.8366 €) | — | 41.04 | 0.003 (n=87) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52987767 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 9,745.667638 USDC | 40.005319 USDC | 0.000000 USDC | 0.007556 USDC | 39.997763 USDC (36.7979 €) | — | 41.04 | 0.003 (n=87) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 52987767 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 3.904517 WETH | 0.016004 WETH | 0.000000 WETH | 0.000004 WETH | 0.016000 WETH (35.3676 €) | — | 40.98 | 0.001 (n=9) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52987767 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[aerodrome]→USDC | 8,125.874120 USDC | 33.416404 USDC | 0.000000 USDC | 0.008354 USDC | 33.408050 USDC (30.7354 €) | — | 41.11 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[uniswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 3.381094 WETH | 0.013904 WETH | 0.000000 WETH | 0.000003 WETH | 0.013901 WETH (30.7274 €) | — | 41.11 | 0.001 (n=9) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.694880 WETH | 0.005092 WETH | 0.000000 WETH | 0.000004 WETH | 0.005088 WETH (11.2472 €) | — | 73.22 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52987767 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 1,667.165057 USDC | 12.218422 USDC | 0.000000 USDC | 0.009951 USDC | 12.208471 USDC (11.2318 €) | — | 73.23 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.693664 WETH | 0.005071 WETH | 0.000000 WETH | 0.000004 WETH | 0.005067 WETH (11.2005 €) | — | 73.05 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52987767 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 1,664.681646 USDC | 12.168115 USDC | 0.000000 USDC | 0.009951 USDC | 12.158164 USDC (11.1855 €) | — | 73.04 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.690803 WETH | 0.005047 WETH | 0.000000 WETH | 0.000004 WETH | 0.005043 WETH (11.1467 €) | — | 73.00 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52987767 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 1,657.559820 USDC | 12.110859 USDC | 0.000000 USDC | 0.010350 USDC | 12.100509 USDC (11.1325 €) | — | 73.00 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.681678 WETH | 0.004988 WETH | 0.000000 WETH | 0.000004 WETH | 0.004984 WETH (11.0165 €) | — | 73.11 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52987767 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 1,635.997254 USDC | 11.971519 USDC | 0.000000 USDC | 0.009951 USDC | 11.961568 USDC (11.0046 €) | — | 73.11 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.654623 WETH | 0.004761 WETH | 0.000000 WETH | 0.000004 WETH | 0.004756 WETH (10.5137 €) | — | 72.66 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52987767 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 1,572.220556 USDC | 11.433044 USDC | 0.000000 USDC | 0.010749 USDC | 11.422295 USDC (10.5085 €) | — | 72.65 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.607597 WETH | 0.004019 WETH | 0.000000 WETH | 0.000004 WETH | 0.004015 WETH (8.8742 €) | — | 66.07 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52987767 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.017786 cbBTC | 0.000118 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000118 cbBTC (8.8734 €) | — | 66.42 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52987767 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.017234 cbBTC | 0.000108 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000108 cbBTC (8.1380 €) | — | 62.87 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.585819 WETH | 0.003684 WETH | 0.000000 WETH | 0.000004 WETH | 0.003680 WETH (8.1339 €) | — | 62.81 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52987767 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.016592 cbBTC | 0.000105 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000105 cbBTC (7.9134 €) | — | 63.49 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.564968 WETH | 0.003581 WETH | 0.000000 WETH | 0.000004 WETH | 0.003576 WETH (7.9058 €) | — | 63.30 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 52987767 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC | 1,110.079396 USDC | 7.999334 USDC | 0.000000 USDC | 0.010749 USDC | 7.988585 USDC (7.3495 €) | — | 71.96 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52987767 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→USDC→[sushiswap_v3]→WETH | 0.460575 WETH | 0.003317 WETH | 0.000000 WETH | 0.000004 WETH | 0.003312 WETH (7.3217 €) | — | 71.92 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2035 ; taux observé 0.097 ; borne inférieure crédible (0.9) 0.089 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
