# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T17:22:09+00:00 ; durée 36.58 min ; blocs 53208289 → 53209389 (1057 vus)

## Connexion
- Requêtes RPC : 12027 ; erreurs : 30 ; latence p50/p95 : 261.3/1,558.2 ms
- Rafraîchissements d'état : 1057 ; âge des données au dernier bloc : 3.35 s ; changements de frais LP observés (pools à frais dynamiques) : 1735
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5351 ; cycles déclenchés par événement : 442 ; avance médiane sur le rafraîchissement multicall : 674 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,331.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 517 pools, 298 jetons, 19028 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 330, par paires 0), mesurés 519, sous le plancher de 10000.0 $ : 2 → gardés 517 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2331.23448, 'cbBTC': 80382.611332, 'AERO': 0.701638}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,268,762 | 2,331.949214 | 53209390 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,445,851 | 0.028975 | 53209390 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,856,325 | 0.000012 | 53209390 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,414,802 | 0.028977 | 53209390 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,479,156 | 2,332.108280 | 53209390 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,205,998 | 97.966937 | 53209390 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,005,036 | 0.001640 | 53209390 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,759,412 | 1.438695 | 53209390 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,784,563 | 0.028969 | 53209390 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,927,845 | 2,332.764072 | 53209390 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,418,316 | 2,332.557544 | 53209390 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,238,248 | 0.998804 | 53209390 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,681,237 | 37,560.982527 | 53209390 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,925,672 | 0.028964 | 53209390 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,504,151 | 97.979716 | 53209390 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 2,382,793 | 0.000012 | 53209390 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,130,920 | 1,214,151.729099 | 53209390 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,854,235 | 2,329.533358 | 53209390 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,823,350 | 0.018688 | 53209390 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,774,275 | 401.249466 | 53209390 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,773,893 | 0.000000 | 53209390 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,716,482 | 0.000012 | 53209390 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,691,351 | 0.000012 | 53209390 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 1,663,472 | 0.000012 | 53209390 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,132 | 1.588195 | 53209390 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,484,730 | 0.005718 | 53209390 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,758 | 0.826986 | 53209390 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,451,725 | 3,351.623135 | 53209390 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,381,854 | 13,829.413654 | 53209390 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,245,166 | 2,332.103549 | 53209390 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,239,542 | 0.000265 | 53209390 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,193,805 | 68.182945 | 53209390 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,154,472 | 0.000266 | 53209390 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,151,327 | 36,458,114.983492 | 53209390 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,149,009 | 1,080,081.000904 | 53209390 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,120,088 | 504,300.459577 | 53209390 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,113,534 | 0.000000 | 53209390 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,074,389 | 21,111,176.745031 | 53209390 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,073,721 | 72,061.977045 | 53209390 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,071,227 | 3,328.444397 | 53209390 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,051,950 | 16.453883 | 53209390 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 1,007,230 | 61.704828 | 53209390 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 990,703 | 0.042020 | 53209390 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 989,212 | 97.421878 | 53209390 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 937,508 | 2,344.326232 | 53209390 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 924,115 | 1,061.469131 | 53209390 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 901,361 | 0.000560 | 53209390 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 876,598 | 2.328767 | 53209390 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 871,928 | 18.220831 | 53209390 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 846,519 | 2,331.659603 | 53209390 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 835,617 | 17.644014 | 53209390 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| pancakeswap_v3 | QUID/USDC | 100 | 805,535 | 0.058246 | 53209390 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 789,640 | 0.802973 | 53209390 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 753,863 | 0.000009 | 53209390 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,615 | 4,630,573.297358 | 53209390 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,434 | 0.617795 | 53209390 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 705,960 | 137,412.850934 | 53209390 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2123 | 690,406 | 502,532.398241 | 53209390 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 666,760 | 0.106812 | 53209390 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | TIG/USDC | 10000 | 657,510 | 0.545603 | 53209390 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |

## Recherche d'opportunités
- Cycles : 1498 ; routes examinées : 28503944 ; candidats optimisés : 105265 ; net attendu > 0 : 247 ; dernier cycle 315.0 ms
- Rejets (moteur) : {'spread_below_threshold': 28076321, 'liquidity_below_min': 320551, 'negative_expected_net': 105018, 'borrow_bound_too_small': 1495, 'cycle_budget_exhausted': 312}
- Enregistrements de la session : 105265 ; net attendu > 0 : 247 ; simulés (eth_call de la vraie tx) : 8 (ok 2, échec 6) ; étiquettes ghost N+1 : 0/8 positives
- Décisions : {'REJECTED': 105265} ; motifs de rejet : {'below_safety_margin': 234, 'negative_expected_net': 105018, 'p_lower_below_threshold': 219, 'reliability_not_demonstrated': 28, 'simulation_failed': 6, 'stale_data': 70}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53208319 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.122130 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | — | 0.85 | 0.122 (n=412) | REJECTED | below_safety_margin(10414748764798<24426083849228), stale_data(5490ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.122130 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0223 €) | — | 0.85 | 0.122 (n=412) | REJECTED | below_safety_margin(10414748764798<24426083849228), stale_data(6530ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 301.138389 USDC | 0.031316 USDC | 0.000000 USDC | 0.007037 USDC | 0.024279 USDC (0.0223 €) | — | 0.81 | 0.122 (n=412) | REJECTED | below_safety_margin(24279<60227), stale_data(5497ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 301.138389 USDC | 0.031316 USDC | 0.000000 USDC | 0.007037 USDC | 0.024279 USDC (0.0223 €) | — | 0.81 | 0.122 (n=412) | REJECTED | below_safety_margin(24279<60227), stale_data(6537ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0222 €) | — | 0.82 | 0.122 (n=412) | REJECTED | below_safety_margin(30<72), stale_data(5504ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0222 €) | — | 0.82 | 0.122 (n=412) | REJECTED | below_safety_margin(30<72), stale_data(6544ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 288.371092 USDC | 0.027508 USDC | 0.000000 USDC | 0.007037 USDC | 0.020471 USDC (0.0188 €) | — | 0.71 | 0.001 (n=7) | REJECTED | below_safety_margin(20471<57674), stale_data(5537ms>4000.0), reliability_not_demonstrated |
| 53208322 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 288.371092 USDC | 0.027508 USDC | 0.000000 USDC | 0.007037 USDC | 0.020471 USDC (0.0188 €) | — | 0.71 | 0.001 (n=7) | REJECTED | below_safety_margin(20471<57674), stale_data(6576ms>4000.0), reliability_not_demonstrated |
| 53208319 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110251 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0187 €) | — | 0.79 | 0.001 (n=7) | REJECTED | below_safety_margin(8741214283322<22050149691238), stale_data(5545ms>4000.0), reliability_not_demonstrated |
| 53208322 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.110251 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0187 €) | — | 0.79 | 0.001 (n=7) | REJECTED | below_safety_margin(8741214283322<22050149691238), stale_data(6583ms>4000.0), reliability_not_demonstrated |
| 53208319 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0185 €) | — | 0.69 | 0.001 (n=7) | REJECTED | below_safety_margin(25<72), stale_data(5530ms>4000.0), reliability_not_demonstrated |
| 53208322 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0185 €) | — | 0.69 | 0.001 (n=7) | REJECTED | below_safety_margin(25<72), stale_data(6569ms>4000.0), reliability_not_demonstrated |
| 53208319 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 268.781622 USDC | 0.024180 USDC | 0.000000 USDC | 0.007037 USDC | 0.017143 USDC (0.0158 €) | — | 0.64 | 0.122 (n=412) | REJECTED | below_safety_margin(17143<53756), stale_data(5564ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 268.781622 USDC | 0.024180 USDC | 0.000000 USDC | 0.007037 USDC | 0.017143 USDC (0.0158 €) | — | 0.64 | 0.122 (n=412) | REJECTED | below_safety_margin(17143<53756), stale_data(6602ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.111410 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0157 €) | — | 0.66 | 0.122 (n=412) | REJECTED | below_safety_margin(7313454472818<22281999774565), stale_data(5571ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.111410 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0157 €) | — | 0.66 | 0.122 (n=412) | REJECTED | below_safety_margin(7313454472818<22281999774565), stale_data(6609ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208319 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0156 €) | — | 0.58 | 0.122 (n=412) | REJECTED | below_safety_margin(21<72), stale_data(5579ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003647 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0156 €) | — | 0.58 | 0.122 (n=412) | REJECTED | below_safety_margin(21<72), stale_data(6616ms>4000.0), p_lower_below_threshold(0.12<0.75) |
| 53208322 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002550 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0126 €) | — | 0.67 | 0.122 (n=412) | REJECTED | below_safety_margin(17<50), p_lower_below_threshold(0.12<0.75) |
| 53208323 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002550 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0126 €) | — | 0.67 | 0.122 (n=412) | REJECTED | below_safety_margin(17<50), p_lower_below_threshold(0.12<0.75) |
| 53208322 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.098641 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0126 €) | — | 0.59 | 0.122 (n=412) | REJECTED | below_safety_margin(5860358347425<19728132612879), p_lower_below_threshold(0.12<0.75) |
| 53208323 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.098641 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0126 €) | — | 0.59 | 0.122 (n=412) | REJECTED | below_safety_margin(5860358347425<19728132612879), p_lower_below_threshold(0.12<0.75) |
| 53208322 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 222.003652 USDC | 0.020484 USDC | 0.000000 USDC | 0.007039 USDC | 0.013445 USDC (0.0124 €) | — | 0.61 | 0.122 (n=412) | REJECTED | below_safety_margin(13445<44400), p_lower_below_threshold(0.12<0.75) |
| 53208323 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 222.003652 USDC | 0.020484 USDC | 0.000000 USDC | 0.007039 USDC | 0.013445 USDC (0.0124 €) | — | 0.61 | 0.122 (n=412) | REJECTED | below_safety_margin(13445<44400), p_lower_below_threshold(0.12<0.75) |
| 53208563 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 53.801650 USDC | 0.020174 USDC | 0.000000 USDC | 0.007675 USDC | 0.012499 USDC (0.0115 €) | — | 2.32 | 0.167 (n=204) | REJECTED | p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 2973 ; taux observé 0.093 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
