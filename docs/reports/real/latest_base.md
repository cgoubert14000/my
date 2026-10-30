# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T16:31:37+00:00 ; durée 169.71 min ; blocs 53289181 → 53294270 (5019 vus)

## Connexion
- Requêtes RPC : 60610 ; erreurs : 0 ; latence p50/p95 : 74.7/770.4 ms
- Rafraîchissements d'état : 5020 ; âge des données au dernier bloc : 1.27 s ; changements de frais LP observés (pools à frais dynamiques) : 15264
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 127403 ; cycles déclenchés par événement : 5897 ; avance médiane sur le rafraîchissement multicall : 337 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,230.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,121,329 | 2,230.203477 | 53294270 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,910,955 | 0.028848 | 53294270 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,569,146 | 0.000013 | 53294270 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,026,781 | 0.028776 | 53294270 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,160,798 | 2,234.404651 | 53294270 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,737,316 | 100.551613 | 53294270 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,655,761 | 0.001605 | 53294270 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,088,955 | 1.591994 | 53294270 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,539,252 | 0.028857 | 53294270 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,163,777 | 2,234.936479 | 53294270 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,070,129 | 0.998903 | 53294270 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,041,029 | 2,234.811687 | 53294270 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,542,070 | 37,102.515052 | 53294270 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2520 | 2,740,017 | 0.028797 | 53294270 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,307,524 | 100.602761 | 53294270 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,044,530 | 1,206,344.208581 | 53294270 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,919,038 | 0.000013 | 53294270 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,738,918 | 0.017732 | 53294270 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,713,511 | 0.000000 | 53294270 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,677,230 | 418.152105 | 53294270 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,663,346 | 0.000013 | 53294270 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,547,704 | 0.000013 | 53294270 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,520,073 | 2,231.733171 | 53294270 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,465,855 | 0.000013 | 53294270 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,461,592 | 1.645227 | 53294270 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,551 | 0.825087 | 53294270 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,411,027 | 3,558.516561 | 53294270 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,305,576 | 2,234.404651 | 53294270 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,304,963 | 14,503.707350 | 53294270 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,263,110 | 0.004969 | 53294270 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,053 | 70.018466 | 53294270 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,099,216 | 36,393,028.300731 | 53294270 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,910 | 515,837.237096 | 53294270 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,030,820 | 21,064,637.364881 | 53294270 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,017,543 | 0.000000 | 53294270 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,010,849 | 74,340.733454 | 53294270 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,883 | 2,229.702738 | 53294270 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,241 | 19.321897 | 53294270 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 989,487 | 63.939092 | 53294270 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 962,346 | 100.428309 | 53294270 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 943,188 | 0.045033 | 53294270 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 924,355 | 1,217,084.590838 | 53294270 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 918,780 | 2,235.963227 | 53294270 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 882,931 | 1,076.240322 | 53294270 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 864,377 | 3,545.501696 | 53294270 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 860,311 | 0.000557 | 53294270 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 834,250 | 19.561429 | 53294270 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 815,303 | 0.059726 | 53294270 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 794,423 | 17.729006 | 53294270 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,885 | 0.803616 | 53294270 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 733,419 | 0.000264 | 53294270 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 720,915 | 0.595077 | 53294270 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,344 | 4,565,949.164370 | 53294270 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 692,037 | 0.000008 | 53294270 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,405 | 2.330515 | 53294270 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 655,832 | 145,784.769458 | 53294270 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 652,915 | 517,759.910069 | 53294270 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 637,238 | 0.512952 | 53294270 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,235 | 0.091665 | 53294270 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 599,653 | 0.915115 | 53294270 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 10916 ; routes examinées : 204544008 ; candidats optimisés : 1179466 ; net attendu > 0 : 4963 ; dernier cycle 61.9 ms
- Rejets (moteur) : {'spread_below_threshold': 199758562, 'liquidity_below_min': 3207451, 'negative_expected_net': 1174503, 'pool_quarantined': 338566, 'unquotable': 45663, 'borrow_bound_too_small': 10914, 'cycle_budget_exhausted': 3386}
- Enregistrements de la session : 1179466 ; net attendu > 0 : 4963 ; simulés (eth_call de la vraie tx) : 236 (ok 162, échec 74) ; étiquettes ghost N+1 : 44/145 positives
- Décisions : {'REJECTED': 1179466} ; motifs de rejet : {'below_safety_margin': 4281, 'negative_expected_net': 1174503, 'p_lower_below_threshold': 4545, 'reliability_not_demonstrated': 418, 'sim_below_estimate': 25, 'simulated_net_nonpositive': 6, 'simulation_failed': 74, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.117062 WETH | 0.000177 WETH | 0.000000 WETH | 0.000003 WETH | 0.000174 WETH (0.3554 €) | 0.000174 WETH | 14.86 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.117062 WETH | 0.000177 WETH | 0.000000 WETH | 0.000003 WETH | 0.000174 WETH (0.3554 €) | — | 14.86 | 0.059 (n=87) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 259.464116 USDC | 0.393348 USDC | 0.000000 USDC | 0.007214 USDC | 0.386134 USDC (0.3552 €) | — | 14.88 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 259.464116 USDC | 0.393348 USDC | 0.000000 USDC | 0.007214 USDC | 0.386134 USDC (0.3552 €) | — | 14.88 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.109757 WETH | 0.000172 WETH | 0.000000 WETH | 0.000003 WETH | 0.000169 WETH (0.3456 €) | 0.000169 WETH | 15.41 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.109757 WETH | 0.000172 WETH | 0.000000 WETH | 0.000003 WETH | 0.000169 WETH (0.3456 €) | — | 15.41 | 0.018 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 243.507113 USDC | 0.382725 USDC | 0.000000 USDC | 0.007214 USDC | 0.375511 USDC (0.3455 €) | — | 15.42 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 243.507113 USDC | 0.382725 USDC | 0.000000 USDC | 0.007214 USDC | 0.375511 USDC (0.3455 €) | — | 15.42 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.112422 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3254 €) | 0.000159 WETH | 14.16 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.112422 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3254 €) | — | 14.16 | 0.018 (n=80) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 249.147534 USDC | 0.360718 USDC | 0.000000 USDC | 0.007214 USDC | 0.353504 USDC (0.3252 €) | — | 14.19 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 249.147534 USDC | 0.360718 USDC | 0.000000 USDC | 0.007214 USDC | 0.353504 USDC (0.3252 €) | — | 14.19 | 0.018 (n=80) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.108803 WETH | 0.000155 WETH | 0.000000 WETH | 0.000003 WETH | 0.000152 WETH (0.3103 €) | — | 13.96 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.108803 WETH | 0.000155 WETH | 0.000000 WETH | 0.000003 WETH | 0.000152 WETH (0.3103 €) | — | 13.96 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 241.443620 USDC | 0.344393 USDC | 0.000000 USDC | 0.007214 USDC | 0.337179 USDC (0.3102 €) | — | 13.97 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 241.443620 USDC | 0.344393 USDC | 0.000000 USDC | 0.007214 USDC | 0.337179 USDC (0.3102 €) | — | 13.97 | 0.059 (n=87) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.225957 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2794 €) | — | 6.05 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.225957 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2794 €) | — | 6.05 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 501.049732 USDC | 0.310117 USDC | 0.000000 USDC | 0.006570 USDC | 0.303547 USDC (0.2793 €) | — | 6.06 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53293514 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 501.049732 USDC | 0.310117 USDC | 0.000000 USDC | 0.006570 USDC | 0.303547 USDC (0.2793 €) | — | 6.06 | 0.202 (n=85) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 53289560 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 140.927016 USDC | 0.310023 USDC | 0.000000 USDC | 0.006770 USDC | 0.303253 USDC (0.2790 €) | — | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.063562 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2783 €) | 0.000137 WETH | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 134.625773 USDC | 0.296283 USDC | 0.000000 USDC | 0.007106 USDC | 0.289177 USDC (0.2660 €) | — | 21.48 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.060712 WETH | 0.000134 WETH | 0.000000 WETH | 0.000003 WETH | 0.000130 WETH (0.2653 €) | 0.000130 WETH | 21.48 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53293514 | WETH→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.125735 WETH | 0.000127 WETH | 0.000000 WETH | 0.000002 WETH | 0.000125 WETH (0.2556 €) | — | 9.95 | 0.000 (n=61) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 3795 ; taux observé 0.123 ; borne inférieure crédible (0.9) 0.117 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
