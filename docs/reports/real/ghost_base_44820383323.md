# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-20T21:36:29+00:00 ; durée 3.04 min ; blocs 60100131 → 60101046 (160 vus)

## Connexion
- Requêtes RPC : 1978 ; erreurs : 0 ; latence p50/p95 : 323.3/967.0 ms
- Rafraîchissements d'état : 160 ; âge des données au dernier bloc : 5.13 s ; changements de frais LP observés (pools à frais dynamiques) : 196
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 723 ; cycles déclenchés par événement : 129 ; avance médiane sur le rafraîchissement multicall : 392 ms
- Gaz : base fee 0.005001 gwei ; prix ETH (pool le plus profond) : 1,612.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 411 pools, 245 jetons, 12256 routes
- Par DEX : uniswap_v3 122, aerodrome_slipstream 86, aerodrome 166, pancakeswap_v3 26, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 143 (rejetés 2) → 548 jetons ; pools candidats 3595 (énumérés 251, par paires 0), mesurés 413, sous le plancher de 10000.0 $ : 2 → gardés 411 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1605.51254, 'cbBTC': 58557.611788, 'AERO': 0.386499}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 77,053,784 | 1,612.969533 | 60101045 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 19,816,641 | 0.027501 | 60101045 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 10,330,996 | 1,615.009959 | 60101045 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,077,828 | 0.027433 | 60101045 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,139,050 | 80.165389 | 60101045 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,426,064 | 0.000017 | 60101045 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,754,363 | 0.027504 | 60101045 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,289,982 | 2.574470 | 60101045 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,088,683 | 0.998739 | 60101045 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,916,910 | 1,614.399298 | 60101045 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,454,035 | 40,429.373014 | 60101045 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 363 | 2,105,219 | 1,614.878853 | 60101045 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,763,785 | 0.000017 | 60101045 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,580,603 | 0.027445 | 60101045 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,534,861 | 1,119,463.985823 | 60101045 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,580 | 0.843948 | 60101045 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,276,989 | 0.000017 | 60101045 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,245,633 | 0.000000 | 60101045 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,145,793 | 0.000017 | 60101045 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,139,151 | 0.006433 | 60101045 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,075,616 | 15.567737 | 60101046 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,614 | 86.545397 | 60101045 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 959,275 | 456.030425 | 60101045 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 952,837 | 1,612.534240 | 60101045 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 937,275 | 16,599.075326 | 60101045 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 919,225 | 4,157.977370 | 60101045 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 918,553 | 80.592350 | 60101045 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 905,524 | 0.049654 | 60101045 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/USDC | 3000 | 860,986 | 1,612.877529 | 60101045 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/doginme | 10000 | 850,423 | 30,766,629.741603 | 60101045 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 758,082 | 517,258.086387 | 60101045 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 756,457 | 74.768282 | 60101045 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 736,662 | 0.001519 | 60101045 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 734,524 | 21,879,764.326289 | 60101045 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 716,841 | 24.597703 | 60101045 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | DRB/WETH | 10000 | 713,780 | 0.000000 | 60101045 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | XDP/USDC | 100 | 712,238 | 0.014250 | 60101045 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 697,318 | 0.043230 | 60101045 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | WETH/MORPHO | 3000 | 677,925 | 1,076.055692 | 60101045 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 661,348 | 1,601.585682 | 60101045 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 646,819 | 1,615.108596 | 60101045 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | uXRP/WETH | 3000 | 645,188 | 0.000607 | 60101045 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/USDC | 100 | 560,289 | 1,614.434041 | 60101045 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 548,412 | 0.379740 | 60101045 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/wstETH | 3000 | 547,294 | 0.799406 | 60101045 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 513,250 | 4,700,703.485893 | 60101045 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 499,236 | 4,187.895804 | 60101045 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | ELSA/USDC | 100 | 482,363 | 0.069982 | 60101045 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | FLOCK/USDC | 3000 | 478,950 | 0.029845 | 60101045 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4055 | 473,503 | 516,596.972708 | 60101045 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 471,969 | 1.479983 | 60101045 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 415,501 | 191,955.650539 | 60101045 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 412,383 | 0.000007 | 60101045 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 368,252 | 1,075.921401 | 60101045 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 363,898 | 21.874197 | 60101045 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 363,115 | 833,522.709084 | 60101045 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 362,220 | 0.054557 | 60101045 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 342,389 | 369.094078 | 60101045 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2838 | 335,478 | 80.217913 | 60101045 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | VIRTUAL/WETH | 10000 | 333,273 | 0.000234 | 60101045 | `0x21594b992F68495dD28d605834b58889d0a727c7` |

## Recherche d'opportunités
- Cycles : 288 ; routes examinées : 3529728 ; candidats optimisés : 26485 ; net attendu > 0 : 24 ; dernier cycle 415.7 ms
- Rejets (moteur) : {'spread_below_threshold': 3413469, 'liquidity_below_min': 46948, 'negative_expected_net': 26461, 'borrow_bound_too_small': 2755, 'cycle_budget_exhausted': 469}
- Enregistrements de la session : 24455 ; net attendu > 0 : 24 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 24455} ; motifs de rejet : {'below_safety_margin': 24, 'negative_expected_net': 24431, 'p_lower_below_threshold': 24}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 60100786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005193 USDC | 0.010080 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10080<36349), p_lower_below_threshold(0.17<0.75) |
| 60100786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005193 USDC | 0.010080 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10080<36349), p_lower_below_threshold(0.17<0.75) |
| 60100785 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005197 USDC | 0.010076 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10076<36349), p_lower_below_threshold(0.17<0.75) |
| 60100786 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 181.748793 USDC | 0.015273 USDC | 0.000000 USDC | 0.005197 USDC | 0.010076 USDC (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(10076<36349), p_lower_below_threshold(0.17<0.75) |
| 60100786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6239758834343<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60100786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0093 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6239758834343<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60100785 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0092 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6237127405493<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60100786 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.112620 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0092 €) | — | 0.55 | 0.167 (n=46) | REJECTED | below_safety_margin(6237127405493<22524079666277), p_lower_below_threshold(0.17<0.75) |
| 60100785 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60100786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60100786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60100786 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0092 €) | — | 0.60 | 0.167 (n=46) | REJECTED | below_safety_margin(17<56), p_lower_below_threshold(0.17<0.75) |
| 60100578 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 55.916076 USDC | 0.008171 USDC | 0.000000 USDC | 0.004910 USDC | 0.003261 USDC (0.0030 €) | — | 0.58 | 0.359 (n=663) | REJECTED | below_safety_margin(3261<11183), p_lower_below_threshold(0.36<0.75) |
| 60100579 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 55.916076 USDC | 0.008171 USDC | 0.000000 USDC | 0.004910 USDC | 0.003261 USDC (0.0030 €) | — | 0.58 | 0.359 (n=663) | REJECTED | below_safety_margin(3261<11183), p_lower_below_threshold(0.36<0.75) |
| 60100578 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.034657 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0030 €) | — | 0.58 | 0.359 (n=663) | REJECTED | below_safety_margin(2013879441074<6931386492547), p_lower_below_threshold(0.36<0.75) |
| 60100579 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.034657 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0030 €) | — | 0.58 | 0.359 (n=663) | REJECTED | below_safety_margin(2013879441074<6931386492547), p_lower_below_threshold(0.36<0.75) |
| 60100578 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 51.386349 USDC | 0.007111 USDC | 0.000000 USDC | 0.004910 USDC | 0.002201 USDC (0.0020 €) | — | 0.43 | 0.280 (n=1679) | REJECTED | below_safety_margin(2201<10277), p_lower_below_threshold(0.28<0.75) |
| 60100579 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 51.386349 USDC | 0.007111 USDC | 0.000000 USDC | 0.004910 USDC | 0.002201 USDC (0.0020 €) | — | 0.43 | 0.280 (n=1679) | REJECTED | below_safety_margin(2201<10277), p_lower_below_threshold(0.28<0.75) |
| 60100578 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.032147 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0020 €) | — | 0.42 | 0.280 (n=1679) | REJECTED | below_safety_margin(1355925823200<6429425744715), p_lower_below_threshold(0.28<0.75) |
| 60100579 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.032147 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0020 €) | — | 0.42 | 0.280 (n=1679) | REJECTED | below_safety_margin(1355925823200<6429425744715), p_lower_below_threshold(0.28<0.75) |
| 60100578 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 47.738461 USDC | 0.005978 USDC | 0.000000 USDC | 0.004910 USDC | 0.001068 USDC (0.0010 €) | — | 0.22 | 0.359 (n=663) | REJECTED | below_safety_margin(1068<9547), p_lower_below_threshold(0.36<0.75) |
| 60100579 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 47.738461 USDC | 0.005978 USDC | 0.000000 USDC | 0.004910 USDC | 0.001068 USDC (0.0010 €) | — | 0.22 | 0.359 (n=663) | REJECTED | below_safety_margin(1068<9547), p_lower_below_threshold(0.36<0.75) |
| 60100578 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.029698 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0010 €) | — | 0.22 | 0.359 (n=663) | REJECTED | below_safety_margin(653302580725<5939620184701), p_lower_below_threshold(0.36<0.75) |
| 60100579 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.029698 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0010 €) | — | 0.22 | 0.359 (n=663) | REJECTED | below_safety_margin(653302580725<5939620184701), p_lower_below_threshold(0.36<0.75) |

## Fiabilité et décision
- Observations ghost : 8766 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
