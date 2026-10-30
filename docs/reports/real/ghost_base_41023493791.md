# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T08:09:10+00:00 ; durée 3.06 min ; blocs 53279104 → 53279197 (68 vus)

## Connexion
- Requêtes RPC : 937 ; erreurs : 0 ; latence p50/p95 : 507.2/2,594.6 ms
- Rafraîchissements d'état : 68 ; âge des données au dernier bloc : 11.76 s ; changements de frais LP observés (pools à frais dynamiques) : 169
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1602 ; cycles déclenchés par événement : 55 ; avance médiane sur le rafraîchissement multicall : 1,309 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.31 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 497 pools, 288 jetons, 18652 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 114, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 499, sous le plancher de 10000.0 $ : 2 → gardés 497 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2234.189813, 'cbBTC': 78005.931316, 'AERO': 0.620161}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,083,336 | 2,229.305524 | 53279196 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,096,121 | 0.028558 | 53279196 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,518,574 | 0.000013 | 53279196 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,046,670 | 0.028627 | 53279196 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,081,763 | 2,223.848835 | 53279196 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,840,330 | 97.964417 | 53279196 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,764,044 | 0.001625 | 53279196 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,066,927 | 1.612486 | 53279196 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,570,332 | 0.028550 | 53279197 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,138,284 | 2,223.246557 | 53279196 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,108,568 | 0.999256 | 53279196 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 952 | 3,741,769 | 2,223.014571 | 53279196 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,563,671 | 36,624.582699 | 53279196 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 2,764,517 | 0.028615 | 53279196 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2898 | 2,346,355 | 97.964551 | 53279196 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,032,216 | 1,220,025.263374 | 53279196 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,933,368 | 0.000013 | 53279196 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,793,922 | 0.018726 | 53279196 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,677,972 | 417.052616 | 53279196 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,669,600 | 0.000013 | 53279196 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,668,441 | 0.000000 | 53279196 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,646,782 | 0.000013 | 53279196 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,537,994 | 2,230.145337 | 53279196 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 1,475,373 | 0.000013 | 53279196 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,202 | 1.642297 | 53279196 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,762 | 0.825557 | 53279196 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,393,711 | 3,593.768494 | 53279196 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,313,396 | 14,592.392235 | 53279196 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,295,211 | 0.005125 | 53279196 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,290,925 | 2,223.918728 | 53279196 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,305 | 69.988581 | 53279196 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,082 | 36,634,242.088427 | 53279196 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,132 | 516,035.322484 | 53279196 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,017,033 | 73,387.035573 | 53279196 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,011,492 | 21,755,255.508864 | 53279196 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,609 | 2,229.778976 | 53279196 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | DRB/WETH | 10000 | 998,849 | 0.000000 | 53279196 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 996,783 | 19.124179 | 53279196 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 970,673 | 97.285291 | 53279196 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 954,720 | 68.680308 | 53279196 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/AERO | 10000 | 943,345 | 3,600.937902 | 53279196 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/VVV | 3000 | 939,314 | 0.043960 | 53279196 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 918,160 | 1,232,570.533544 | 53279196 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 913,174 | 2,231.397776 | 53279196 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 876,411 | 1,077.808508 | 53279196 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 859,737 | 0.000557 | 53279196 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4510 | 834,952 | 19.531309 | 53279196 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 818,795 | 0.060275 | 53279196 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 789,132 | 17.868824 | 53279196 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,582 | 0.803616 | 53279196 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,889 | 0.000259 | 53279196 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,326 | 0.578406 | 53279196 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,544 | 4,729,181.635584 | 53279196 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 693,611 | 0.000008 | 53279196 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,416 | 2.329059 | 53279196 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 652,753 | 147,029.877076 | 53279196 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2120 | 652,477 | 517,462.942478 | 53279196 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 646,262 | 0.527193 | 53279196 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 603,314 | 0.091019 | 53279196 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 599,339 | 0.915335 | 53279196 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 122 ; routes examinées : 2275544 ; candidats optimisés : 13005 ; net attendu > 0 : 30 ; dernier cycle 588.5 ms
- Rejets (moteur) : {'spread_below_threshold': 2235241, 'liquidity_below_min': 25797, 'negative_expected_net': 12975, 'unquotable': 1210, 'cycle_budget_exhausted': 170, 'borrow_bound_too_small': 121}
- Enregistrements de la session : 13005 ; net attendu > 0 : 30 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 13005} ; motifs de rejet : {'below_safety_margin': 30, 'negative_expected_net': 12975, 'p_lower_below_threshold': 26, 'reliability_not_demonstrated': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53279192 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.022228 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(1923940147941<4445615603556), p_lower_below_threshold(0.13<0.75) |
| 53279193 | WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.022228 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(1923940147941<4445615603556), p_lower_below_threshold(0.13<0.75) |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 48.923868 USDC | 0.010978 USDC | 0.000000 USDC | 0.006719 USDC | 0.004259 USDC (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(4259<9784), p_lower_below_threshold(0.13<0.75) |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[uniswap_v3]→USDC | 48.923868 USDC | 0.010978 USDC | 0.000000 USDC | 0.006719 USDC | 0.004259 USDC (0.0039 €) | — | 0.87 | 0.129 (n=573) | REJECTED | below_safety_margin(4259<9784), p_lower_below_threshold(0.13<0.75) |
| 53279192 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.021433 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(1724303343048<4286625972274), p_lower_below_threshold(0.13<0.75) |
| 53279193 | WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.021433 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(1724303343048<4286625972274), p_lower_below_threshold(0.13<0.75) |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 47.809608 USDC | 0.010535 USDC | 0.000000 USDC | 0.006719 USDC | 0.003816 USDC (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(3816<9561), p_lower_below_threshold(0.13<0.75) |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[pancakeswap_v3]→USDC | 47.809608 USDC | 0.010535 USDC | 0.000000 USDC | 0.006719 USDC | 0.003816 USDC (0.0035 €) | — | 0.80 | 0.129 (n=573) | REJECTED | below_safety_margin(3816<9561), p_lower_below_threshold(0.13<0.75) |
| 53279192 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.020924 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | — | 0.66 | 0.129 (n=573) | REJECTED | below_safety_margin(1391333212918<4184772507618), p_lower_below_threshold(0.13<0.75) |
| 53279193 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.020924 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0029 €) | — | 0.66 | 0.129 (n=573) | REJECTED | below_safety_margin(1391333212918<4184772507618), p_lower_below_threshold(0.13<0.75) |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 46.188726 USDC | 0.009794 USDC | 0.000000 USDC | 0.006719 USDC | 0.003075 USDC (0.0028 €) | — | 0.67 | 0.129 (n=573) | REJECTED | below_safety_margin(3075<9237), p_lower_below_threshold(0.13<0.75) |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 46.188726 USDC | 0.009794 USDC | 0.000000 USDC | 0.006719 USDC | 0.003075 USDC (0.0028 €) | — | 0.67 | 0.129 (n=573) | REJECTED | below_safety_margin(3075<9237), p_lower_below_threshold(0.13<0.75) |
| 53279192 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.020341 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0026 €) | — | 0.62 | 0.032 (n=134) | REJECTED | below_safety_margin(1252864302594<4068178139672), p_lower_below_threshold(0.03<0.75) |
| 53279193 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.020341 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0026 €) | — | 0.62 | 0.032 (n=134) | REJECTED | below_safety_margin(1252864302594<4068178139672), p_lower_below_threshold(0.03<0.75) |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 44.919694 USDC | 0.007794 USDC | 0.000000 USDC | 0.005022 USDC | 0.002772 USDC (0.0026 €) | — | 0.62 | 0.032 (n=134) | REJECTED | below_safety_margin(2772<8983), p_lower_below_threshold(0.03<0.75) |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 44.919694 USDC | 0.007794 USDC | 0.000000 USDC | 0.005022 USDC | 0.002772 USDC (0.0026 €) | — | 0.62 | 0.032 (n=134) | REJECTED | below_safety_margin(2772<8983), p_lower_below_threshold(0.03<0.75) |
| 53279192 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.025392 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0020 €) | — | 0.37 | — (n=0) | REJECTED | below_safety_margin(951257105637<5078488264647), reliability_not_demonstrated |
| 53279193 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.025392 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0020 €) | — | 0.37 | — (n=0) | REJECTED | below_safety_margin(951257105637<5078488264647), reliability_not_demonstrated |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 55.336291 USDC | 0.006432 USDC | 0.000000 USDC | 0.004330 USDC | 0.002102 USDC (0.0019 €) | — | 0.38 | — (n=0) | REJECTED | below_safety_margin(2102<11067), reliability_not_demonstrated |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 55.336291 USDC | 0.006432 USDC | 0.000000 USDC | 0.004330 USDC | 0.002102 USDC (0.0019 €) | — | 0.38 | — (n=0) | REJECTED | below_safety_margin(2102<11067), reliability_not_demonstrated |
| 53279192 | WETH→[aerodrome]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.010270 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 0.89 | 0.179 (n=62) | REJECTED | below_safety_margin(914965786694<2053903992407), p_lower_below_threshold(0.18<0.75) |
| 53279193 | WETH→[aerodrome]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.010270 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0019 €) | — | 0.89 | 0.179 (n=62) | REJECTED | below_safety_margin(914965786694<2053903992407), p_lower_below_threshold(0.18<0.75) |
| 53279192 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→LCAP→[aerodrome_slipstream]→USDC | 22.444062 USDC | 0.008428 USDC | 0.000000 USDC | 0.006412 USDC | 0.002016 USDC (0.0019 €) | — | 0.90 | 0.179 (n=62) | REJECTED | below_safety_margin(2016<4488), p_lower_below_threshold(0.18<0.75) |
| 53279193 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→LCAP→[aerodrome_slipstream]→USDC | 22.444062 USDC | 0.008428 USDC | 0.000000 USDC | 0.006412 USDC | 0.002016 USDC (0.0019 €) | — | 0.90 | 0.179 (n=62) | REJECTED | below_safety_margin(2016<4488), p_lower_below_threshold(0.18<0.75) |
| 53279192 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.019625 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0011 €) | — | 0.28 | 0.129 (n=573) | REJECTED | below_safety_margin(554314118771<3925071206638), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 3591 ; taux observé 0.112 ; borne inférieure crédible (0.9) 0.105 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
