# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T17:20:27+00:00 ; durée 12.16 min ; blocs 54836572 → 54840207 (483 vus)

## Connexion
- Requêtes RPC : 6951 ; erreurs : 0 ; latence p50/p95 : 474.7/1,868.4 ms
- Rafraîchissements d'état : 483 ; âge des données au dernier bloc : 9.83 s ; changements de frais LP observés (pools à frais dynamiques) : 338
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 484 ; cycles déclenchés par événement : 188 ; avance médiane sur le rafraîchissement multicall : 580 ms
- Gaz : base fee 0.005002 gwei ; prix ETH (pool le plus profond) : 2,229.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 276 jetons, 17556 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 97, aerodrome 196, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3671 (énumérés 291, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.430141, 'cbBTC': 75744.13603, 'AERO': 0.592088}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,153,054 | 2,229.177825 | 54840237 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,843,781 | 0.029417 | 54840237 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,320,301 | 0.000013 | 54840237 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,143,117 | 0.029477 | 54840237 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,512,983 | 2,226.371119 | 54840237 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,304,380 | 108.820289 | 54840237 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,396,249 | 0.001542 | 54840237 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,153,968 | 0.029423 | 54840237 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,754,437 | 1.701337 | 54840237 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,174,536 | 2,225.959789 | 54840237 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,988,634 | 0.999079 | 54840237 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,269,584 | 43,503.050574 | 54840237 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,166,456 | 2,226.069362 | 54840237 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,461,632 | 0.029461 | 54840237 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,082,444 | 1,161,552.106913 | 54840237 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,737,388 | 0.000013 | 54840237 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,629,490 | 0.000013 | 54840237 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,616,713 | 0.000000 | 54840237 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,605,861 | 0.006328 | 54840237 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,549,992 | 0.015288 | 54840237 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,511,364 | 446.955805 | 54840237 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,020 | 0.000013 | 54840237 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,118 | 1.431449 | 54840237 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,404 | 0.824203 | 54840237 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,366,258 | 3,786.206378 | 54840237 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,243 | 2,229.319703 | 54840237 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,256,223 | 15,166.126678 | 54840237 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,253,980 | 2,230.011536 | 54840237 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,169,673 | 2,226.178605 | 54840237 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54840237 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,087,785 | 37,301,150.846749 | 54840237 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,030,739 | 108.088738 | 54840237 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 994,303 | 605,222.878064 | 54840237 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 978,701 | 23,100,700.027305 | 54840237 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,351 | 21.227814 | 54840237 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 957,762 | 0.000000 | 54840237 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,141 | 2,228.787393 | 54840237 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 925,587 | 0.000013 | 54840237 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 924,349 | 1,077.621449 | 54840237 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 919,092 | 74.180524 | 54840237 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 861,635 | 102,043.282152 | 54840237 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 819,769 | 0.048927 | 54840237 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,176 | 0.055128 | 54840237 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 774,840 | 3,758.428167 | 54840237 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 764,531 | 22.276515 | 54840237 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 756,190 | 0.799805 | 54840237 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,349 | 0.555188 | 54840237 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 678,785 | 5,105,094.757201 | 54840237 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 669,894 | 0.566696 | 54840237 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 646,129 | 150,519.710150 | 54840237 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 645,242 | 0.000008 | 54840237 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 619,986 | 0.000250 | 54840237 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 600,989 | 605,442.619073 | 54840237 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 572,797 | 0.039123 | 54840237 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 553,160 | 2.471747 | 54840237 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 522,969 | 1,077.927478 | 54840237 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 522,375 | 893,993.745056 | 54840237 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 514,460 | 2,226.064842 | 54840237 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | ELSA/USDC | 100 | 510,301 | 0.075427 | 54840237 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 510,179 | 7,001.328459 | 54840237 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 670 ; routes examinées : 11762520 ; candidats optimisés : 39119 ; net attendu > 0 : 17 ; dernier cycle 149.6 ms
- Rejets (moteur) : {'spread_below_threshold': 11540055, 'liquidity_below_min': 183194, 'negative_expected_net': 39102, 'cycle_budget_exhausted': 152}
- Enregistrements de la session : 39119 ; net attendu > 0 : 17 ; simulés (eth_call de la vraie tx) : 6 (ok 3, échec 3) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 39119} ; motifs de rejet : {'below_safety_margin': 10, 'negative_expected_net': 39102, 'p_lower_below_threshold': 11, 'reliability_not_demonstrated': 6, 'simulation_failed': 3, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54837017 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000872 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0174 €) | 0.000000 cbBTC | 2.87 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54837017 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.030050 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | 0.000008 WETH | 2.76 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54837017 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000804 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0167 €) | — | 2.98 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54837017 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.030714 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0163 €) | 0.000008 WETH | 2.58 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54838078 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.857327 USDC | 0.011384 USDC | 0.000000 USDC | 0.005012 USDC | 0.006372 USDC (0.0059 €) | — | 3.21 | 0.036 (n=389) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 54838079 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.857327 USDC | 0.011384 USDC | 0.000000 USDC | 0.005012 USDC | 0.006372 USDC (0.0059 €) | — | 3.21 | 0.036 (n=389) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 54840170 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 18.242781 USDC | 0.009783 USDC | 0.000000 USDC | 0.005011 USDC | 0.004772 USDC (0.0044 €) | — | 2.62 | 0.051 (n=280) | REJECTED | stale_data(4646ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 54837867 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003064 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.13 | 0.029 (n=28) | REJECTED | below_safety_margin(4<61), reliability_not_demonstrated |
| 54837867 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003064 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0028 €) | — | 0.13 | 0.029 (n=28) | REJECTED | below_safety_margin(4<61), reliability_not_demonstrated |
| 54837867 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 332.539448 USDC | 0.009375 USDC | 0.000000 USDC | 0.006706 USDC | 0.002669 USDC (0.0025 €) | — | 0.08 | 0.029 (n=28) | REJECTED | below_safety_margin(2669<66507), reliability_not_demonstrated |
| 54837867 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 332.539448 USDC | 0.009375 USDC | 0.000000 USDC | 0.006706 USDC | 0.002669 USDC (0.0025 €) | — | 0.08 | 0.029 (n=28) | REJECTED | below_safety_margin(2669<66507), reliability_not_demonstrated |
| 54837867 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.134440 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.09 | 0.029 (n=28) | REJECTED | below_safety_margin(1154281752379<26888078288877), reliability_not_demonstrated |
| 54837867 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.134440 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0024 €) | — | 0.09 | 0.029 (n=28) | REJECTED | below_safety_margin(1154281752379<26888078288877), reliability_not_demonstrated |
| 54837867 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.060950 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.16 | 0.051 (n=280) | REJECTED | below_safety_margin(999342499579<12190017818965), p_lower_below_threshold(0.05<0.75) |
| 54837867 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.060950 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0021 €) | — | 0.16 | 0.051 (n=280) | REJECTED | below_safety_margin(999342499579<12190017818965), p_lower_below_threshold(0.05<0.75) |
| 54837867 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 134.207743 USDC | 0.007559 USDC | 0.000000 USDC | 0.005350 USDC | 0.002209 USDC (0.0020 €) | — | 0.16 | 0.051 (n=280) | REJECTED | below_safety_margin(2209<26841), p_lower_below_threshold(0.05<0.75) |
| 54837867 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 134.207743 USDC | 0.007559 USDC | 0.000000 USDC | 0.005350 USDC | 0.002209 USDC (0.0020 €) | — | 0.16 | 0.051 (n=280) | REJECTED | below_safety_margin(2209<26841), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 6241 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
