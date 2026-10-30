# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T08:52:03+00:00 ; durée 45.94 min ; blocs 53279104 → 53280484 (1325 vus)

## Connexion
- Requêtes RPC : 15450 ; erreurs : 5 ; latence p50/p95 : 337.4/2,182.7 ms
- Rafraîchissements d'état : 1325 ; âge des données au dernier bloc : 7.3 s ; changements de frais LP observés (pools à frais dynamiques) : 2423
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5673 ; cycles déclenchés par événement : 310 ; avance médiane sur le rafraîchissement multicall : 1,050 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,228.53 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18652 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 114, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 499, sous le plancher de 10000.0 $ : 2 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.189813, 'cbBTC': 78005.931316, 'AERO': 0.620161}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,523,299 | 2,228.527771 | 53280485 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,091,780 | 0.028558 | 53280485 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,521,216 | 0.000013 | 53280485 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,043,593 | 0.028620 | 53280485 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,116,921 | 2,223.593607 | 53280485 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,826,233 | 98.249078 | 53280485 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,769,183 | 0.001629 | 53280485 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,072,587 | 1.609447 | 53280485 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,201,331 | 0.028557 | 53280485 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,138,522 | 2,224.469763 | 53280485 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,107,246 | 0.999256 | 53280485 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 594 | 3,737,180 | 2,223.947874 | 53280485 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,560,480 | 36,664.667228 | 53280485 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,762,395 | 0.028607 | 53280485 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,342,109 | 98.268046 | 53280485 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,031,507 | 1,220,025.263374 | 53280485 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,932,020 | 0.000013 | 53280485 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,783,905 | 0.018553 | 53280485 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,677,564 | 416.929724 | 53280485 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,669,257 | 0.000013 | 53280485 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,667,858 | 0.000000 | 53280485 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,646,475 | 0.000013 | 53280485 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,537,725 | 2,229.287137 | 53280485 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,475,075 | 0.000013 | 53280485 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,202 | 1.642297 | 53280485 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,516 | 0.825813 | 53280485 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,395,150 | 3,578.956406 | 53280485 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,129 | 14,586.357450 | 53280485 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,236 | 0.005127 | 53280485 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,291,435 | 2,223.514181 | 53280485 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,305 | 69.988581 | 53280485 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,097,697 | 36,634,242.088427 | 53280485 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,050,765 | 516,035.399709 | 53280485 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,017,759 | 73,231.319964 | 53280485 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,015,078 | 21,611,916.410003 | 53280485 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,435 | 2,228.534040 | 53280485 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 998,567 | 0.000000 | 53280485 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 997,007 | 19.100629 | 53280485 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 981,760 | 64.985762 | 53280485 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 968,874 | 97.562460 | 53280485 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 944,071 | 3,596.785352 | 53280485 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/VVV | 3000 | 937,006 | 0.044204 | 53280485 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 916,973 | 1,234,900.484428 | 53280485 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 913,007 | 2,231.397776 | 53280485 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 875,836 | 1,080.278303 | 53280485 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,414 | 0.000560 | 53280485 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 835,858 | 19.499319 | 53280485 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 815,956 | 0.059829 | 53280485 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 789,801 | 17.845730 | 53280485 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,318 | 0.803616 | 53280485 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,710 | 0.000259 | 53280485 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 706,960 | 0.579769 | 53280485 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 705,528 | 4,712,746.752110 | 53280485 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 694,378 | 0.000008 | 53280485 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,179 | 2.329059 | 53280485 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 655,636 | 145,640.646489 | 53280485 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 652,253 | 514,528.396235 | 53280485 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 648,899 | 0.531275 | 53280485 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 603,716 | 0.091109 | 53280485 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 599,165 | 0.915228 | 53280485 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 1634 ; routes examinées : 30477368 ; candidats optimisés : 149180 ; net attendu > 0 : 150 ; dernier cycle 573.4 ms
- Rejets (moteur) : {'spread_below_threshold': 29953300, 'liquidity_below_min': 359349, 'negative_expected_net': 149030, 'unquotable': 13549, 'borrow_bound_too_small': 1631, 'cycle_budget_exhausted': 359}
- Enregistrements de la session : 149180 ; net attendu > 0 : 150 ; simulés (eth_call de la vraie tx) : 7 (ok 6, échec 1) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 149180} ; motifs de rejet : {'below_safety_margin': 139, 'negative_expected_net': 149030, 'p_lower_below_threshold': 126, 'reliability_not_demonstrated': 24, 'simulation_failed': 1, 'stale_data': 54}

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
| 53280155 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.352892 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0655 €) | — | 0.91 | 0.128 (n=576) | REJECTED | below_safety_margin(31940656864819<70578429915919), stale_data(4677ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 785.910636 USDC | 0.077788 USDC | 0.000000 USDC | 0.006714 USDC | 0.071074 USDC (0.0654 €) | — | 0.90 | 0.128 (n=576) | REJECTED | below_safety_margin(71074<157182), stale_data(4686ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010024 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0654 €) | — | 0.91 | 0.128 (n=576) | REJECTED | below_safety_margin(91<200), stale_data(4696ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 53280155 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.110748 WETH | 0.000020 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0361 €) | — | 1.59 | 0.032 (n=134) | REJECTED | below_safety_margin(17624942129350<22149670633147), stale_data(4397ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53280155 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 245.113876 USDC | 0.044577 USDC | 0.000000 USDC | 0.005356 USDC | 0.039221 USDC (0.0361 €) | — | 1.60 | 0.032 (n=134) | REJECTED | below_safety_margin(39221<49022), stale_data(4406ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53280155 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.200935 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0268 €) | — | 0.65 | 0.002 (n=5) | REJECTED | below_safety_margin(13045414509068<40187011549876), stale_data(4775ms>4000.0), reliability_not_demonstrated |
| 53280155 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 447.538708 USDC | 0.034046 USDC | 0.000000 USDC | 0.005018 USDC | 0.029028 USDC (0.0267 €) | — | 0.65 | 0.002 (n=5) | REJECTED | below_safety_margin(29028<89507), stale_data(4783ms>4000.0), reliability_not_demonstrated |
| 53279399 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 475.925085 USDC | 0.034613 USDC | 0.000000 USDC | 0.007063 USDC | 0.027550 USDC (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(27550<95185), reliability_not_demonstrated |
| 53279399 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 475.925085 USDC | 0.034613 USDC | 0.000000 USDC | 0.007063 USDC | 0.027550 USDC (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(27550<95185), reliability_not_demonstrated |
| 53279399 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.212880 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(12328674289373<42575998243671), reliability_not_demonstrated |
| 53279399 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.212880 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0253 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(12328674289373<42575998243671), reliability_not_demonstrated |
| 53279399 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006055 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0251 €) | — | 0.58 | 0.001 (n=14) | REJECTED | below_safety_margin(35<121), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3598 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.105 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
