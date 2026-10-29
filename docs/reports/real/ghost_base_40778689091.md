# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T03:13:47+00:00 ; durée 290.88 min ; blocs 53218407 → 53227136 (8612 vus)

## Connexion
- Requêtes RPC : 98032 ; erreurs : 83 ; latence p50/p95 : 227.1/1,896.7 ms
- Rafraîchissements d'état : 8613 ; âge des données au dernier bloc : 1.98 s ; changements de frais LP observés (pools à frais dynamiques) : 13628
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 751 ; cycles déclenchés par événement : 79 ; avance médiane sur le rafraîchissement multicall : 796 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,304.74 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 522 pools, 300 jetons, 19152 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 122, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 183 (rejetés 2) → 588 jetons ; pools candidats 3758 (énumérés 331, par paires 0), mesurés 524, sous le plancher de 10000.0 $ : 2 → gardés 522 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2360.669373, 'cbBTC': 81164.401586, 'AERO': 0.699093}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,440,645 | 2,304.742820 | 53227136 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,286,034 | 0.028897 | 53227136 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,676,966 | 0.000013 | 53227136 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,311,859 | 0.028839 | 53227136 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,203,825 | 2,306.418506 | 53227136 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,010,906 | 100.313491 | 53227136 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,929,226 | 0.001634 | 53227136 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,552,426 | 1.497110 | 53227136 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,686,815 | 0.028891 | 53227136 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 669 | 4,742,078 | 2,305.441006 | 53227136 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,386,458 | 2,305.537954 | 53227136 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,198,725 | 0.998958 | 53227136 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,580,731 | 38,773.075393 | 53227136 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,893,230 | 0.028851 | 53227136 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,417,006 | 100.298337 | 53227136 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,332,737 | 0.000013 | 53227136 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,105,588 | 1,214,695.545645 | 53227136 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,809,928 | 2,305.414083 | 53227136 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,809,711 | 0.018530 | 53227136 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,753,886 | 403.651202 | 53227136 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,742,736 | 0.000000 | 53227136 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,703,498 | 0.000013 | 53227136 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,683,651 | 0.000013 | 53227136 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,597,435 | 0.000013 | 53227136 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,128 | 1.588199 | 53227136 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,067 | 0.826762 | 53227136 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,413,158 | 3,452.784015 | 53227136 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,383,393 | 0.005287 | 53227136 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,365,082 | 13,971.143534 | 53227136 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,279,597 | 2,306.466453 | 53227136 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,217,881 | 0.000262 | 53227136 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,190,323 | 68.582376 | 53227136 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,135,420 | 36,699,159.479503 | 53227136 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,131,967 | 1,086,355.429247 | 53227136 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,126,554 | 0.000263 | 53227136 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,102,991 | 494,725.552371 | 53227136 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,082,841 | 0.000000 | 53227136 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,054,637 | 21,379,851.748997 | 53227136 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,066 | 16.472978 | 53227136 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,050,957 | 73,472.621456 | 53227136 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 1,037,019 | 3,428.407229 | 53227136 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/USDC | 3000 | 1,022,278 | 2,304.366952 | 53227136 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,013,613 | 60.930390 | 53227136 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 968,627 | 100.647392 | 53227136 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 965,416 | 0.043484 | 53227136 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 933,079 | 2,314.580420 | 53227136 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,504 | 1,057.693993 | 53227136 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 889,527 | 0.000558 | 53227136 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 867,723 | 18.368775 | 53227136 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 860,692 | 2.326790 | 53227136 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | QUID/USDC | 100 | 839,036 | 0.063551 | 53227136 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 821,172 | 17.769765 | 53227136 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 780,428 | 0.802973 | 53227136 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,853 | 4,520,587.388099 | 53227136 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 732,476 | 0.605531 | 53227136 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 732,352 | 0.000008 | 53227136 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 697,242 | 137,612.966563 | 53227136 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2165 | 689,328 | 499,049.432099 | 53227136 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 650,546 | 0.534361 | 53227136 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 636,505 | 0.099116 | 53227136 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 8691 ; routes examinées : 166450032 ; candidats optimisés : 685480 ; net attendu > 0 : 903 ; dernier cycle 354.9 ms
- Rejets (moteur) : {'spread_below_threshold': 163563538, 'liquidity_below_min': 2185694, 'negative_expected_net': 684577, 'borrow_bound_too_small': 8679, 'cycle_budget_exhausted': 6641}
- Enregistrements de la session : 685480 ; net attendu > 0 : 903 ; simulés (eth_call de la vraie tx) : 56 (ok 54, échec 2) ; étiquettes ghost N+1 : 13/51 positives
- Décisions : {'REJECTED': 685480} ; motifs de rejet : {'below_safety_margin': 589, 'negative_expected_net': 684577, 'p_lower_below_threshold': 835, 'reliability_not_demonstrated': 68, 'sim_below_estimate': 4, 'simulated_net_nonpositive': 3, 'simulation_failed': 2, 'stale_data': 88}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53220050 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 1,720.189536 USDC | 0.194471 USDC | 0.000000 USDC | 0.006015 USDC | 0.188456 USDC (0.1734 €) | — | 1.10 | 0.032 (n=111) | REJECTED | below_safety_margin(188456<344037), p_lower_below_threshold(0.03<0.75) |
| 53224574 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.124981 WETH | 0.000058 WETH | 0.000000 WETH | 0.000003 WETH | 0.000055 WETH (0.1173 €) | 0.000055 WETH | 4.38 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 288.859449 USDC | 0.134223 USDC | 0.000000 USDC | 0.007153 USDC | 0.127070 USDC (0.1169 €) | — | 4.40 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.154905 WETH | 0.000057 WETH | 0.000000 WETH | 0.000003 WETH | 0.000054 WETH (0.1158 €) | 0.000054 WETH | 3.49 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 358.547290 USDC | 0.132641 USDC | 0.000000 USDC | 0.007153 USDC | 0.125488 USDC (0.1154 €) | — | 3.50 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.152020 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1127 €) | 0.000053 WETH | 3.46 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 352.977780 USDC | 0.129196 USDC | 0.000000 USDC | 0.007153 USDC | 0.122043 USDC (0.1123 €) | — | 3.46 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.152185 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1115 €) | — | 3.42 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 353.226538 USDC | 0.127946 USDC | 0.000000 USDC | 0.007153 USDC | 0.120793 USDC (0.1111 €) | — | 3.42 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53220050 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→USDC | 1,313.415456 USDC | 0.106189 USDC | 0.000000 USDC | 0.005657 USDC | 0.100532 USDC (0.0925 €) | — | 0.77 | 0.032 (n=111) | REJECTED | below_safety_margin(100532<262683), p_lower_below_threshold(0.03<0.75) |
| 53224574 | WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.050396 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0478 €) | — | 4.43 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbXRP→[uniswap_v3]→USDC | 116.402747 USDC | 0.058968 USDC | 0.000000 USDC | 0.007153 USDC | 0.051815 USDC (0.0477 €) | — | 4.45 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53225124 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.362853 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0424 €) | — | 0.55 | 0.032 (n=112) | REJECTED | below_safety_margin(19943323892094<72570549919866), p_lower_below_threshold(0.03<0.75) |
| 53225124 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 833.028156 USDC | 0.051816 USDC | 0.000000 USDC | 0.005847 USDC | 0.045969 USDC (0.0423 €) | — | 0.55 | 0.032 (n=112) | REJECTED | below_safety_margin(45969<166605), p_lower_below_threshold(0.03<0.75) |
| 53224574 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000955 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0355 €) | — | 5.03 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 85.281842 USDC | 0.046012 USDC | 0.000000 USDC | 0.007514 USDC | 0.038498 USDC (0.0354 €) | — | 4.51 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53225100 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.071145 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0334 €) | 0.000016 WETH | 2.21 | 0.117 (n=429) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53225100 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 163.728602 USDC | 0.043325 USDC | 0.000000 USDC | 0.007140 USDC | 0.036185 USDC (0.0333 €) | — | 2.21 | 0.117 (n=429) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53224574 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 54.484703 USDC | 0.042520 USDC | 0.000000 USDC | 0.007153 USDC | 0.035367 USDC (0.0325 €) | — | 6.49 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224574 | WETH→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.024629 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0325 €) | — | 6.16 | 0.100 (n=330) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224933 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.125895 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0324 €) | — | 1.21 | 0.032 (n=112) | REJECTED | below_safety_margin(15248956732434<25179098502382), p_lower_below_threshold(0.03<0.75) |
| 53224933 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 289.296759 USDC | 0.041003 USDC | 0.000000 USDC | 0.005840 USDC | 0.035163 USDC (0.0323 €) | — | 1.22 | 0.032 (n=112) | REJECTED | below_safety_margin(35163<57859), p_lower_below_threshold(0.03<0.75) |
| 53224929 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000860 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0302 €) | — | 4.77 | 0.098 (n=335) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224929 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 75.956155 USDC | 0.039595 USDC | 0.000000 USDC | 0.007069 USDC | 0.032526 USDC (0.0299 €) | — | 4.28 | 0.098 (n=335) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53224929 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.025777 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0298 €) | 0.000014 WETH | 5.44 | 0.098 (n=335) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 3092 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
