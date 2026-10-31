# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T00:36:25+00:00 ; durée 316.36 min ; blocs 53299323 → 53308811 (9090 vus)

## Connexion
- Requêtes RPC : 104326 ; erreurs : 150 ; latence p50/p95 : 307.2/1,614.6 ms
- Rafraîchissements d'état : 9090 ; âge des données au dernier bloc : 3.65 s ; changements de frais LP observés (pools à frais dynamiques) : 13286
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 64254 ; cycles déclenchés par événement : 5153 ; avance médiane sur le rafraîchissement multicall : 1,190 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,239.89 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18532 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 112, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3774 (énumérés 315, par paires 0), mesurés 500, sous le plancher de 10000.0 $ : 3 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.87299, 'cbBTC': 76304.747909, 'AERO': 0.609807}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,301,961 | 2,239.891470 | 53308812 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,960,235 | 0.029053 | 53308812 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,237,413 | 0.000013 | 53308812 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,009,855 | 0.029104 | 53308812 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,186,438 | 2,243.248025 | 53308812 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,755,194 | 98.928973 | 53308812 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,684,009 | 0.001627 | 53308812 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,902,182 | 1.598505 | 53308812 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,567,115 | 0.029059 | 53308812 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,139,304 | 2,242.915250 | 53308812 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,054,938 | 1.000000 | 53308812 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,046,496 | 2,242.851978 | 53308812 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,539,713 | 37,475.433377 | 53308812 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,747,944 | 0.029088 | 53308812 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2805 | 2,350,183 | 98.965898 | 53308812 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,053,411 | 1,206,344.208581 | 53308812 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,984,825 | 0.000013 | 53308812 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,764,812 | 0.000000 | 53308812 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,731,895 | 0.017614 | 53308812 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,688,430 | 415.393178 | 53308812 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,613,924 | 0.000013 | 53308812 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,566,329 | 0.000013 | 53308812 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,522,811 | 2,248.024480 | 53308812 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,520,145 | 1.536599 | 53308812 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,512 | 0.825661 | 53308812 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,424,246 | 0.000013 | 53308812 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,418,630 | 3,587.613623 | 53308812 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,312,444 | 2,242.988507 | 53308812 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,308,766 | 14,283.342284 | 53308812 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,302,698 | 0.005104 | 53308812 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53308812 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,110,015 | 35,624,828.121540 | 53308812 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,239 | 513,479.681214 | 53308812 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,630 | 21,020,489.174102 | 53308812 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,021,758 | 73,395.328241 | 53308812 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 1,012,422 | 0.000000 | 53308812 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | WETH/USDC | 3000 | 1,009,100 | 2,240.926202 | 53308812 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,007,577 | 18.546595 | 53308812 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 975,913 | 99.067956 | 53308812 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 967,909 | 66.821739 | 53308812 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 959,214 | 0.044110 | 53308812 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 926,638 | 1,221,638.656269 | 53308812 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,280 | 2,235.963227 | 53308812 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 894,606 | 1,073.060978 | 53308812 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 864,491 | 3,612.674591 | 53308812 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,998 | 0.000557 | 53308812 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | QUID/USDC | 100 | 849,730 | 0.065263 | 53308812 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 846,342 | 19.139431 | 53308812 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 758,205 | 0.803531 | 53308812 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 738,628 | 0.000266 | 53308812 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,876 | 0.596958 | 53308812 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 727,425 | 4,479,436.069394 | 53308812 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 682,107 | 0.000008 | 53308812 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,773 | 2.331396 | 53308812 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 661,108 | 144,754.296800 | 53308812 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2135 | 657,359 | 510,891.121540 | 53308812 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 632,328 | 0.505450 | 53308812 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 622,638 | 0.095474 | 53308812 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 602,390 | 0.914712 | 53308812 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2775 | 541,200 | 1,072.830259 | 53308812 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 14242 ; routes examinées : 263932744 ; candidats optimisés : 1338267 ; net attendu > 0 : 520 ; dernier cycle 599.9 ms
- Rejets (moteur) : {'spread_below_threshold': 258444708, 'liquidity_below_min': 4092049, 'negative_expected_net': 1337747, 'unquotable': 38916, 'borrow_bound_too_small': 14226, 'pool_quarantined': 2340, 'cycle_budget_exhausted': 2238}
- Enregistrements de la session : 1338267 ; net attendu > 0 : 520 ; simulés (eth_call de la vraie tx) : 30 (ok 16, échec 14) ; étiquettes ghost N+1 : 0/26 positives
- Décisions : {'REJECTED': 1338267} ; motifs de rejet : {'below_safety_margin': 354, 'negative_expected_net': 1337747, 'p_lower_below_threshold': 485, 'reliability_not_demonstrated': 35, 'simulation_failed': 14, 'stale_data': 25}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53304483 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 194.189460 USDC | 0.881802 USDC | 0.000000 USDC | 0.005026 USDC | 0.876776 USDC (0.8066 €) | — | 45.15 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 628.636240 USDC | 0.523468 USDC | 0.000000 USDC | 0.006416 USDC | 0.517052 USDC (0.4757 €) | — | 8.22 | 0.096 (n=30) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 628.636240 USDC | 0.523468 USDC | 0.000000 USDC | 0.006416 USDC | 0.517052 USDC (0.4757 €) | — | 8.22 | 0.096 (n=30) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.280829 WETH | 0.000234 WETH | 0.000000 WETH | 0.000003 WETH | 0.000231 WETH (0.4751 €) | — | 8.22 | 0.096 (n=30) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.280829 WETH | 0.000234 WETH | 0.000000 WETH | 0.000003 WETH | 0.000231 WETH (0.4751 €) | 0.000231 WETH | 8.22 | 0.096 (n=30) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 642.908521 USDC | 0.517904 USDC | 0.000000 USDC | 0.006416 USDC | 0.511488 USDC (0.4706 €) | — | 7.96 | 0.254 (n=93) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 642.908521 USDC | 0.517904 USDC | 0.000000 USDC | 0.006416 USDC | 0.511488 USDC (0.4706 €) | — | 7.96 | 0.254 (n=93) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.286774 WETH | 0.000231 WETH | 0.000000 WETH | 0.000003 WETH | 0.000228 WETH (0.4699 €) | — | 7.96 | 0.254 (n=93) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.25<0.75) |
| 53307356 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.286774 WETH | 0.000231 WETH | 0.000000 WETH | 0.000003 WETH | 0.000228 WETH (0.4699 €) | 0.000228 WETH | 7.96 | 0.254 (n=93) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53302962 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.002481 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3587 €) | — | 20.52 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 191.105100 USDC | 0.396516 USDC | 0.000000 USDC | 0.006734 USDC | 0.389782 USDC (0.3586 €) | — | 20.40 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 463.693528 USDC | 0.363565 USDC | 0.000000 USDC | 0.006416 USDC | 0.357149 USDC (0.3286 €) | — | 7.70 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 463.693528 USDC | 0.363565 USDC | 0.000000 USDC | 0.006416 USDC | 0.357149 USDC (0.3286 €) | — | 7.70 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.207042 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3283 €) | — | 7.70 | 0.114 (n=187) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.207042 WETH | 0.000162 WETH | 0.000000 WETH | 0.000003 WETH | 0.000159 WETH (0.3283 €) | 0.000159 WETH | 7.70 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53302962 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[uniswap_v3]→USDC | 172.900069 USDC | 0.342781 USDC | 0.000000 USDC | 0.006734 USDC | 0.336047 USDC (0.3092 €) | — | 19.44 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53302962 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC | 0.002223 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.3086 €) | — | 19.70 | 0.017 (n=82) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 484.598311 USDC | 0.291789 USDC | 0.000000 USDC | 0.006416 USDC | 0.285373 USDC (0.2625 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 484.598311 USDC | 0.291789 USDC | 0.000000 USDC | 0.006416 USDC | 0.285373 USDC (0.2625 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.216284 WETH | 0.000130 WETH | 0.000000 WETH | 0.000003 WETH | 0.000127 WETH (0.2623 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.216284 WETH | 0.000130 WETH | 0.000000 WETH | 0.000003 WETH | 0.000127 WETH (0.2623 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 477.797871 USDC | 0.287690 USDC | 0.000000 USDC | 0.006416 USDC | 0.281274 USDC (0.2588 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 477.797871 USDC | 0.287690 USDC | 0.000000 USDC | 0.006416 USDC | 0.281274 USDC (0.2588 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.213235 WETH | 0.000128 WETH | 0.000000 WETH | 0.000003 WETH | 0.000126 WETH (0.2585 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53307356 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→WETH | 0.213235 WETH | 0.000128 WETH | 0.000000 WETH | 0.000003 WETH | 0.000126 WETH (0.2585 €) | — | 5.89 | 0.114 (n=187) | REJECTED | p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 3898 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
