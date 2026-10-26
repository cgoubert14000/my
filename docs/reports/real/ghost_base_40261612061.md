# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T05:10:35+00:00 ; durée 129.24 min ; blocs 53097164 → 53101042 (3873 vus)

## Connexion
- Requêtes RPC : 47256 ; erreurs : 10 ; latence p50/p95 : 69.6/890.0 ms
- Rafraîchissements d'état : 3874 ; âge des données au dernier bloc : 1.78 s ; changements de frais LP observés (pools à frais dynamiques) : 6458
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16418 ; cycles déclenchés par événement : 1008 ; avance médiane sur le rafraîchissement multicall : 349 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,317.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 524 pools, 302 jetons, 19436 routes
- Par DEX : uniswap_v3 140, aerodrome 213, aerodrome_slipstream 125, pancakeswap_v3 31, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 337, par paires 0), mesurés 526, sous le plancher de 10000.0 $ : 2 → gardés 524 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2299.668664, 'cbBTC': 79491.484, 'AERO': 0.669155}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,268,431 | 2,317.759698 | 53101042 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,402,356 | 0.029003 | 53101042 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,156,760 | 0.028978 | 53101042 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,455,472 | 0.000013 | 53101042 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,807,243 | 93.846824 | 53101042 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,303,854 | 2,319.763196 | 53101042 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,161,287 | 1.497028 | 53101042 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,983,735 | 0.001653 | 53101042 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,437,076 | 2,319.661330 | 53101042 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,347,777 | 0.029003 | 53101042 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,461,194 | 2,319.732104 | 53101042 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,206,937 | 0.998974 | 53101042 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,803,451 | 34,759.031354 | 53101042 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,758,287 | 2,318.055135 | 53101042 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,188,213 | 0.028967 | 53101042 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,529,472 | 0.000013 | 53101042 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,483,515 | 93.804892 | 53101042 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,192,339 | 411.347653 | 53101042 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,121,314 | 1,210,308.594714 | 53101042 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,890,192 | 0.000013 | 53101042 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,886,895 | 0.000000 | 53101042 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,787,150 | 0.017911 | 53101042 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,712,813 | 0.000013 | 53101042 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,711,268 | 0.000013 | 53101042 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,554,981 | 0.000265 | 53101042 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,242 | 0.826241 | 53101042 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,220 | 1.698035 | 53101042 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,436,219 | 0.005538 | 53101042 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,412,576 | 3,470.901710 | 53101042 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,358,842 | 14,190.235347 | 53101042 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/AERO | 10000 | 1,234,867 | 3,447.475820 | 53101042 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,231,452 | 0.000267 | 53101042 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,221,896 | 2,319.570743 | 53101042 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,220,854 | 65.195116 | 53101042 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,157,599 | 35,178,934.907761 | 53101042 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,156,093 | 0.000000 | 53101042 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,128,144 | 1,107,441.603620 | 53101042 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,112,576 | 496,251.821126 | 53101042 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,083,122 | 53.390629 | 53101042 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,063,647 | 72,765.765495 | 53101042 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,031,073 | 17.391158 | 53101042 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,014,345 | 21,889,661.602154 | 53101042 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 962,338 | 0.040427 | 53101042 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 921,808 | 2,314.067320 | 53101042 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 908,854 | 2.307612 | 53101042 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 890,430 | 0.000553 | 53101042 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 883,248 | 1,142.220719 | 53101042 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 877,008 | 17.151122 | 53101042 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 873,286 | 18.158318 | 53101042 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 867,791 | 94.004703 | 53101042 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 844,383 | 2,317.979190 | 53101042 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 790,711 | 0.000008 | 53101042 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,341 | 0.055961 | 53101042 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 784,759 | 0.803130 | 53101042 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | weETH_04c0/WETH | 500 | 774,891 | 1.105951 | 53101042 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 741,438 | 0.618080 | 53101042 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 730,377 | 4,753,781.258004 | 53101042 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 708,110 | 0.630239 | 53101042 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 707,588 | 135,038.225895 | 53101042 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2129 | 693,012 | 496,100.948259 | 53101042 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 4881 ; routes examinées : 94867116 ; candidats optimisés : 313675 ; net attendu > 0 : 169 ; dernier cycle 208.7 ms
- Rejets (moteur) : {'spread_below_threshold': 93004310, 'liquidity_below_min': 1431920, 'negative_expected_net': 313506, 'unquotable': 112180, 'borrow_bound_too_small': 4881, 'cycle_budget_exhausted': 150}
- Enregistrements de la session : 313675 ; net attendu > 0 : 169 ; simulés (eth_call de la vraie tx) : 5 (ok 3, échec 2) ; étiquettes ghost N+1 : 2/3 positives
- Décisions : {'REJECTED': 313675} ; motifs de rejet : {'below_safety_margin': 164, 'negative_expected_net': 313506, 'p_lower_below_threshold': 147, 'reliability_not_demonstrated': 22, 'sim_below_estimate': 2, 'simulation_failed': 2, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53098029 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.142261 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000024 WETH (0.0501 €) | — | 1.66 | 0.022 (n=94) | REJECTED | below_safety_margin(23566127176808<28452265992404), p_lower_below_threshold(0.02<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 327.219771 USDC | 0.059835 USDC | 0.000000 USDC | 0.005543 USDC | 0.054292 USDC (0.0499 €) | — | 1.66 | 0.022 (n=94) | REJECTED | below_safety_margin(54292<65443), p_lower_below_threshold(0.02<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.098833 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0198 €) | — | 0.94 | 0.129 (n=342) | REJECTED | below_safety_margin(9338811363951<19766565681607), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002899 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0198 €) | — | 0.93 | 0.129 (n=342) | REJECTED | below_safety_margin(27<57), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 192.423773 USDC | 0.028144 USDC | 0.000000 USDC | 0.006948 USDC | 0.021196 USDC (0.0195 €) | — | 1.10 | 0.129 (n=342) | REJECTED | below_safety_margin(21196<38484), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002446 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0191 €) | — | 1.06 | 0.129 (n=342) | REJECTED | below_safety_margin(26<48), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.093531 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0189 €) | — | 0.95 | 0.129 (n=342) | REJECTED | below_safety_margin(8880679294217<18706197028796), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 208.572973 USDC | 0.027344 USDC | 0.000000 USDC | 0.006948 USDC | 0.020396 USDC (0.0188 €) | — | 0.98 | 0.129 (n=342) | REJECTED | below_safety_margin(20396<41714), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002900 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0183 €) | — | 0.86 | 0.129 (n=342) | REJECTED | below_safety_margin(25<57), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.098785 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0182 €) | — | 0.87 | 0.129 (n=342) | REJECTED | below_safety_margin(8567298155534<19757042730904), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 195.851277 USDC | 0.026645 USDC | 0.000000 USDC | 0.006948 USDC | 0.019697 USDC (0.0181 €) | — | 1.01 | 0.129 (n=342) | REJECTED | below_safety_margin(19697<39170), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.055574 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0162 €) | — | 1.37 | 0.129 (n=342) | REJECTED | below_safety_margin(7610299035162<11114801967723), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 128.153521 USDC | 0.024481 USDC | 0.000000 USDC | 0.006948 USDC | 0.017533 USDC (0.0161 €) | — | 1.37 | 0.129 (n=342) | REJECTED | below_safety_margin(17533<25630), p_lower_below_threshold(0.13<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001395 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0147 €) | — | 1.43 | 0.180 (n=175) | REJECTED | below_safety_margin(20<27), p_lower_below_threshold(0.18<0.75) |
| 53098029 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001492 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0147 €) | — | 1.34 | 0.180 (n=175) | REJECTED | below_safety_margin(20<29), p_lower_below_threshold(0.18<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 138.355232 USDC | 0.022683 USDC | 0.000000 USDC | 0.006948 USDC | 0.015735 USDC (0.0145 €) | — | 1.14 | 0.180 (n=175) | REJECTED | below_safety_margin(15735<27671), p_lower_below_threshold(0.18<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.066994 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0142 €) | — | 1.00 | 0.180 (n=175) | REJECTED | below_safety_margin(6686863175120<13398720985300), p_lower_below_threshold(0.18<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 118.828226 USDC | 0.022342 USDC | 0.000000 USDC | 0.006948 USDC | 0.015394 USDC (0.0142 €) | — | 1.30 | 0.180 (n=175) | REJECTED | below_safety_margin(15394<23765), p_lower_below_threshold(0.18<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.050495 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0140 €) | — | 1.31 | 0.180 (n=175) | REJECTED | below_safety_margin(6603141486837<10099080547927), p_lower_below_threshold(0.18<0.75) |
| 53098029 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001438 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0139 €) | — | 1.32 | 0.129 (n=342) | REJECTED | below_safety_margin(19<28), p_lower_below_threshold(0.13<0.75) |
| 53098029 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 118.828226 USDC | 0.022043 USDC | 0.000000 USDC | 0.006948 USDC | 0.015095 USDC (0.0139 €) | — | 1.27 | 0.129 (n=342) | REJECTED | below_safety_margin(15095<23765), p_lower_below_threshold(0.13<0.75) |
| 53098029 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.051267 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0138 €) | — | 1.27 | 0.129 (n=342) | REJECTED | below_safety_margin(6509871033140<10253483185164), p_lower_below_threshold(0.13<0.75) |
| 53099408 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001734 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0132 €) | — | 1.04 | 0.129 (n=342) | REJECTED | below_safety_margin(18<34), p_lower_below_threshold(0.13<0.75) |
| 53099408 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 142.144379 USDC | 0.021683 USDC | 0.000000 USDC | 0.007394 USDC | 0.014289 USDC (0.0131 €) | — | 1.01 | 0.129 (n=342) | REJECTED | below_safety_margin(14289<28428), p_lower_below_threshold(0.13<0.75) |
| 53099408 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.066210 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.93 | 0.129 (n=342) | REJECTED | below_safety_margin(6133012101569<13241987517452), p_lower_below_threshold(0.13<0.75) |

## Fiabilité et décision
- Observations ghost : 2591 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.086 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
