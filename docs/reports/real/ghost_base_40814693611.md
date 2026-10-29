# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T09:10:39+00:00 ; durée 311.32 min ; blocs 53228503 → 53237841 (9084 vus)

## Connexion
- Requêtes RPC : 109066 ; erreurs : 30 ; latence p50/p95 : 243.0/801.0 ms
- Rafraîchissements d'état : 9084 ; âge des données au dernier bloc : 3.3 s ; changements de frais LP observés (pools à frais dynamiques) : 10052
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 92362 ; cycles déclenchés par événement : 8224 ; avance médiane sur le rafraîchissement multicall : 470 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,316.60 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 512 pools, 294 jetons, 18990 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 116, aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 325, par paires 0), mesurés 514, sous le plancher de 10000.0 $ : 2 → gardés 512 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2304.739386, 'cbBTC': 79763.083067, 'AERO': 0.667567}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,853,301 | 2,316.598947 | 53237842 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,375,112 | 0.028982 | 53237842 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,686,093 | 0.000012 | 53237842 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,367,357 | 0.028932 | 53237842 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,255,903 | 2,322.398670 | 53237842 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,126,286 | 98.490624 | 53237842 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,953,519 | 0.001638 | 53237842 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,579,786 | 1.480559 | 53237842 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,753,021 | 0.028984 | 53237842 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 788 | 4,759,262 | 2,322.779011 | 53237842 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,384,513 | 2,322.301920 | 53237842 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,208,584 | 0.998890 | 53237842 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,624,880 | 38,224.584495 | 53237842 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,905,707 | 0.028948 | 53237842 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2781 | 2,466,366 | 98.516236 | 53237842 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 2,336,268 | 0.000012 | 53237842 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,116,419 | 1,214,695.556270 | 53237842 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,839,073 | 0.019082 | 53237842 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,814,519 | 2,316.727669 | 53237842 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,763,358 | 403.409526 | 53237842 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,753,819 | 0.000000 | 53237842 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,705,743 | 0.000012 | 53237842 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,686,104 | 0.000013 | 53237842 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 1,599,678 | 0.000012 | 53237842 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53237842 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,116 | 0.827421 | 53237842 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,425,257 | 3,438.350908 | 53237842 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,389,996 | 0.005329 | 53237842 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,370,042 | 13,928.857577 | 53237842 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,262,279 | 2,322.626252 | 53237842 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,221,657 | 0.000261 | 53237842 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,189,749 | 68.648579 | 53237842 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,346 | 36,690,876.254683 | 53237842 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,137,050 | 1,087,755.188563 | 53237842 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,129,777 | 0.000263 | 53237842 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,098,379 | 507,461.670803 | 53237842 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,072,718 | 0.000000 | 53237842 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 1,053,987 | 73,753.972579 | 53237842 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,052,742 | 21,637,643.091244 | 53237842 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/AERO | 10000 | 1,045,424 | 3,431.088863 | 53237842 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,041,335 | 16.933174 | 53237842 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,024,919 | 2,316.458056 | 53237842 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,011,482 | 61.187344 | 53237842 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 986,573 | 98.922418 | 53237842 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 982,970 | 0.042410 | 53237842 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 934,969 | 2,314.580420 | 53237842 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 917,308 | 1,058.023908 | 53237842 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 890,421 | 0.000554 | 53237842 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 863,645 | 18.508825 | 53237842 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 863,417 | 0.067631 | 53237842 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/msETH (stable) | 500 | 856,484 | 2.328587 | 53237842 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 826,469 | 17.745123 | 53237842 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 784,033 | 0.803812 | 53237842 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 741,123 | 4,613,488.130711 | 53237842 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 737,693 | 0.000008 | 53237842 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 735,201 | 0.604456 | 53237842 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 693,739 | 140,448.403483 | 53237842 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 683,725 | 510,920.318383 | 53237842 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 648,996 | 0.531887 | 53237842 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 626,775 | 0.096733 | 53237842 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 17307 ; routes examinées : 328659930 ; candidats optimisés : 1215101 ; net attendu > 0 : 359 ; dernier cycle 120.3 ms
- Rejets (moteur) : {'spread_below_threshold': 324152213, 'liquidity_below_min': 3244654, 'negative_expected_net': 1214742, 'unquotable': 28217, 'borrow_bound_too_small': 17306, 'cycle_budget_exhausted': 2439}
- Enregistrements de la session : 1215101 ; net attendu > 0 : 359 ; simulés (eth_call de la vraie tx) : 7 (ok 6, échec 1) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 1215101} ; motifs de rejet : {'below_safety_margin': 349, 'negative_expected_net': 1214742, 'p_lower_below_threshold': 337, 'reliability_not_demonstrated': 22, 'simulation_failed': 1, 'stale_data': 19}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53237585 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 42.829334 USDC | 0.027807 USDC | 0.000000 USDC | 0.005197 USDC | 0.022610 USDC (0.0208 €) | 0.022610 USDC | 5.28 | 0.009 (n=155) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53237585 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 42.829334 USDC | 0.027807 USDC | 0.000000 USDC | 0.005197 USDC | 0.022610 USDC (0.0208 €) | — | 5.28 | 0.009 (n=155) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53231893 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.237019 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(6065471298323<47403803883803), stale_data(4320ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53231894 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.237019 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(6065471298323<47403803883803), stale_data(4461ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53231893 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 545.796287 USDC | 0.019313 USDC | 0.000000 USDC | 0.005222 USDC | 0.014091 USDC (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(14091<109159), stale_data(4323ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53231894 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 545.796287 USDC | 0.019313 USDC | 0.000000 USDC | 0.005222 USDC | 0.014091 USDC (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(14091<109159), stale_data(4465ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53236035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 105.462749 USDC | 0.017972 USDC | 0.000000 USDC | 0.006940 USDC | 0.011032 USDC (0.0101 €) | — | 1.05 | 0.117 (n=430) | REJECTED | below_safety_margin(11032<21092), p_lower_below_threshold(0.12<0.75) |
| 53236035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 105.462749 USDC | 0.017972 USDC | 0.000000 USDC | 0.006940 USDC | 0.011032 USDC (0.0101 €) | — | 1.05 | 0.117 (n=430) | REJECTED | below_safety_margin(11032<21092), p_lower_below_threshold(0.12<0.75) |
| 53236035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.045618 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0101 €) | — | 1.04 | 0.117 (n=430) | REJECTED | below_safety_margin(4758752042127<9123650954363), p_lower_below_threshold(0.12<0.75) |
| 53236035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.045618 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0101 €) | — | 1.04 | 0.117 (n=430) | REJECTED | below_safety_margin(4758752042127<9123650954363), p_lower_below_threshold(0.12<0.75) |
| 53230404 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 87.606018 USDC | 0.015335 USDC | 0.000000 USDC | 0.006960 USDC | 0.008375 USDC (0.0077 €) | — | 0.96 | 0.167 (n=221) | REJECTED | below_safety_margin(8375<17521), p_lower_below_threshold(0.17<0.75) |
| 53230404 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 87.606018 USDC | 0.015335 USDC | 0.000000 USDC | 0.006960 USDC | 0.008375 USDC (0.0077 €) | — | 0.96 | 0.167 (n=221) | REJECTED | below_safety_margin(8375<17521), p_lower_below_threshold(0.17<0.75) |
| 53230404 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.037931 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0077 €) | — | 0.95 | 0.167 (n=221) | REJECTED | below_safety_margin(3597069780249<7586217712760), p_lower_below_threshold(0.17<0.75) |
| 53230404 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.037931 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0077 €) | — | 0.95 | 0.167 (n=221) | REJECTED | below_safety_margin(3597069780249<7586217712760), p_lower_below_threshold(0.17<0.75) |
| 53229792 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 25.572483 USDC | 0.014104 USDC | 0.000000 USDC | 0.006620 USDC | 0.007484 USDC (0.0069 €) | — | 2.93 | 0.206 (n=54) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 53229792 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.011013 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0069 €) | 0.000003 WETH | 2.93 | 0.206 (n=54) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 53229792 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 23.276838 USDC | 0.011656 USDC | 0.000000 USDC | 0.006620 USDC | 0.005036 USDC (0.0046 €) | — | 2.16 | 0.148 (n=121) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53229792 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.010025 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0046 €) | 0.000002 WETH | 2.16 | 0.148 (n=121) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53232797 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.039853 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.51 | 0.167 (n=221) | REJECTED | below_safety_margin(2023608693228<7970683131898), p_lower_below_threshold(0.17<0.75) |
| 53232797 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 91.485124 USDC | 0.011967 USDC | 0.000000 USDC | 0.007314 USDC | 0.004653 USDC (0.0043 €) | — | 0.51 | 0.167 (n=221) | REJECTED | below_safety_margin(4653<18297), p_lower_below_threshold(0.17<0.75) |
| 53229792 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 22.875802 USDC | 0.011618 USDC | 0.000000 USDC | 0.006970 USDC | 0.004648 USDC (0.0043 €) | — | 2.03 | 0.148 (n=121) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53229792 | WETH→[uniswap_v3]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.009960 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | 0.000002 WETH | 2.01 | 0.148 (n=121) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53228815 | WETH→[aerodrome_slipstream]→cbETH→[pancakeswap_v3]→WETH | 0.093614 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.19 | 0.031 (n=113) | REJECTED | below_safety_margin(1820077115526<18722700193347), p_lower_below_threshold(0.03<0.75) |
| 53228815 | WETH→[aerodrome_slipstream]→cbETH→[pancakeswap_v3]→WETH | 0.093614 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0039 €) | — | 0.19 | 0.031 (n=113) | REJECTED | below_safety_margin(1820077115526<18722700193347), p_lower_below_threshold(0.03<0.75) |
| 53235341 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.059900 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0038 €) | — | 0.30 | 0.010 (n=28) | REJECTED | below_safety_margin(1789681698828<11980042637887), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3101 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
