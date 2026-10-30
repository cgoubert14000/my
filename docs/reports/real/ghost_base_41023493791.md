# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T10:36:58+00:00 ; durée 150.85 min ; blocs 53279104 → 53283633 (4452 vus)

## Connexion
- Requêtes RPC : 50325 ; erreurs : 23 ; latence p50/p95 : 146.3/1,451.6 ms
- Rafraîchissements d'état : 4453 ; âge des données au dernier bloc : 1.61 s ; changements de frais LP observés (pools à frais dynamiques) : 7435
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 14487 ; cycles déclenchés par événement : 832 ; avance médiane sur le rafraîchissement multicall : 565 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,235.01 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18652 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 114, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 499, sous le plancher de 10000.0 $ : 2 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.189813, 'cbBTC': 78005.931316, 'AERO': 0.620161}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,076,267 | 2,235.007255 | 53283633 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,118,306 | 0.028866 | 53283633 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,494,306 | 0.000013 | 53283633 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,039,000 | 0.028816 | 53283633 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,119,689 | 2,237.276718 | 53283633 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,827,658 | 98.785244 | 53283633 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,725,406 | 0.001633 | 53283633 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,091,028 | 1.599200 | 53283633 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,544,107 | 0.028857 | 53283633 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,072,643 | 0.999983 | 53283633 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,050,500 | 2,237.875139 | 53283633 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,730,403 | 2,237.813777 | 53283633 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,568,244 | 36,717.861860 | 53283633 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2560 | 2,764,452 | 0.028829 | 53283633 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,338,835 | 98.804834 | 53283633 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,037,413 | 1,220,025.263374 | 53283633 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,921,857 | 0.000013 | 53283633 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,803,023 | 0.018889 | 53283633 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,683,597 | 416.100943 | 53283633 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,672,708 | 0.000000 | 53283633 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,660,165 | 0.000013 | 53283633 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,637,830 | 0.000013 | 53283633 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,539,876 | 2,235.273943 | 53283633 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 1,466,934 | 0.000013 | 53283633 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,463,654 | 1.642991 | 53283633 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,759 | 0.824777 | 53283633 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,400,960 | 3,572.478590 | 53283633 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,333,981 | 2,237.254694 | 53283633 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,309,794 | 14,425.969502 | 53283633 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,281,268 | 0.005042 | 53283633 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,305 | 69.988581 | 53283633 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,101,122 | 36,625,893.300953 | 53283633 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,054,013 | 516,049.872959 | 53283633 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,020,533 | 73,257.863634 | 53283633 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,019,498 | 21,546,653.225655 | 53283633 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v2 | WETH/USDC | 3000 | 1,007,901 | 2,234.568909 | 53283633 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,000,503 | 18.921181 | 53283633 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 994,347 | 0.000000 | 53283633 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 976,550 | 65.644413 | 53283633 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 969,130 | 98.385118 | 53283633 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 968,101 | 0.044180 | 53283633 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 922,565 | 1,227,080.046277 | 53283633 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 919,160 | 2,231.397776 | 53283633 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 876,128 | 1,084.878580 | 53283633 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 867,534 | 3,570.651573 | 53283633 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,019 | 0.000558 | 53283633 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4535 | 838,816 | 19.395225 | 53283633 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 814,423 | 0.059590 | 53283633 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 788,974 | 17.922231 | 53283633 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 756,511 | 0.803616 | 53283633 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,755 | 0.000259 | 53283633 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 710,251 | 0.583830 | 53283633 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 709,483 | 4,687,559.425961 | 53283633 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 694,917 | 0.000008 | 53283633 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 680,683 | 2.331455 | 53283633 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 654,149 | 512,523.864836 | 53283633 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 653,804 | 147,324.821992 | 53283633 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 649,774 | 0.532633 | 53283633 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 608,788 | 0.092275 | 53283633 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 600,855 | 0.915386 | 53283633 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 5284 ; routes examinées : 98557168 ; candidats optimisés : 453033 ; net attendu > 0 : 769 ; dernier cycle 102.5 ms
- Rejets (moteur) : {'spread_below_threshold': 96814997, 'liquidity_below_min': 1248453, 'negative_expected_net': 452264, 'unquotable': 34330, 'borrow_bound_too_small': 5276, 'cycle_budget_exhausted': 1079}
- Enregistrements de la session : 453033 ; net attendu > 0 : 769 ; simulés (eth_call de la vraie tx) : 42 (ok 29, échec 13) ; étiquettes ghost N+1 : 12/34 positives
- Décisions : {'REJECTED': 453033} ; motifs de rejet : {'below_safety_margin': 613, 'negative_expected_net': 452264, 'p_lower_below_threshold': 698, 'reliability_not_demonstrated': 71, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 13, 'stale_data': 150}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53280155 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.549303 WETH | 0.000095 WETH | 0.000000 WETH | 0.000003 WETH | 0.000092 WETH (0.1889 €) | — | 1.68 | 0.001 (n=14) | REJECTED | below_safety_margin(92121724782817<109860500413333), stale_data(4442ms>4000.0), reliability_not_demonstrated |
| 53280155 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.015378 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1889 €) | — | 1.71 | 0.001 (n=14) | REJECTED | below_safety_margin(263<307), stale_data(4464ms>4000.0), reliability_not_demonstrated |
| 53280155 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,174.612570 USDC | 0.211665 USDC | 0.000000 USDC | 0.007052 USDC | 0.204613 USDC (0.1882 €) | — | 1.74 | 0.001 (n=14) | REJECTED | below_safety_margin(204613<234922), stale_data(4453ms>4000.0), reliability_not_demonstrated |
| 53279324 | WETH→[uniswap_v3]→MEY→[aerodrome]→WETH | 0.030287 WETH | 0.000076 WETH | 0.000000 WETH | 0.000002 WETH | 0.000074 WETH (0.1520 €) | — | 24.48 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53280155 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003628 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1192 €) | — | 4.58 | 0.103 (n=426) | REJECTED | stale_data(4272ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 53280155 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.135302 WETH | 0.000061 WETH | 0.000000 WETH | 0.000003 WETH | 0.000058 WETH (0.1190 €) | 0.000058 WETH | 4.29 | 0.103 (n=426) | REJECTED | stale_data(4266ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 53280155 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 292.935131 USDC | 0.135881 USDC | 0.000000 USDC | 0.006714 USDC | 0.129167 USDC (0.1188 €) | 0.129167 USDC | 4.41 | 0.103 (n=426) | REJECTED | stale_data(4278ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 53280155 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.379278 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0857 €) | — | 1.10 | 0.128 (n=576) | REJECTED | below_safety_margin(41785014404391<75855535063457), stale_data(4622ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 839.665456 USDC | 0.100130 USDC | 0.000000 USDC | 0.007052 USDC | 0.093078 USDC (0.0856 €) | — | 1.11 | 0.128 (n=576) | REJECTED | below_safety_margin(93078<167933), stale_data(4643ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010669 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0855 €) | — | 1.12 | 0.128 (n=576) | REJECTED | below_safety_margin(119<213), stale_data(4633ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH | 0.114341 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0819 €) | 0.000040 WETH | 3.49 | 0.103 (n=426) | REJECTED | stale_data(4285ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 53280155 | cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003001 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0819 €) | — | 3.80 | 0.103 (n=426) | REJECTED | stale_data(4291ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 53280155 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 265.728114 USDC | 0.095429 USDC | 0.000000 USDC | 0.006714 USDC | 0.088715 USDC (0.0816 €) | — | 3.34 | 0.103 (n=426) | REJECTED | stale_data(4297ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 53283516 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 231.919188 USDC | 0.089269 USDC | 0.000000 USDC | 0.007066 USDC | 0.082203 USDC (0.0756 €) | — | 3.54 | 0.106 (n=439) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53283516 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 231.919188 USDC | 0.089269 USDC | 0.000000 USDC | 0.007072 USDC | 0.082197 USDC (0.0756 €) | — | 3.54 | 0.106 (n=439) | REJECTED | stale_data(5632ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 53283516 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.103806 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0754 €) | 0.000037 WETH | 3.54 | 0.106 (n=439) | REJECTED | stale_data(5625ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 53283516 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.103941 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0753 €) | — | 3.53 | 0.106 (n=439) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 53280155 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.352892 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0655 €) | — | 0.91 | 0.128 (n=576) | REJECTED | below_safety_margin(31940656864819<70578429915919), stale_data(4677ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 785.910636 USDC | 0.077788 USDC | 0.000000 USDC | 0.006714 USDC | 0.071074 USDC (0.0654 €) | — | 0.90 | 0.128 (n=576) | REJECTED | below_safety_margin(71074<157182), stale_data(4686ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010024 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0654 €) | — | 0.91 | 0.128 (n=576) | REJECTED | below_safety_margin(91<200), stale_data(4696ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53281344 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.057789 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0542 €) | 0.000026 WETH | 4.58 | 0.102 (n=429) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53281344 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 128.245678 USDC | 0.065525 USDC | 0.000000 USDC | 0.006709 USDC | 0.058816 USDC (0.0541 €) | — | 4.59 | 0.102 (n=429) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53281344 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.051008 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0411 €) | 0.000020 WETH | 3.93 | 0.102 (n=429) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53281344 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.047521 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0411 €) | 0.000020 WETH | 4.22 | 0.102 (n=429) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53281344 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 112.967210 USDC | 0.051319 USDC | 0.000000 USDC | 0.006709 USDC | 0.044610 USDC (0.0410 €) | — | 3.95 | 0.102 (n=429) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 3625 ; taux observé 0.114 ; borne inférieure crédible (0.9) 0.108 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
