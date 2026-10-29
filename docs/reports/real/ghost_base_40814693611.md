# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T07:39:17+00:00 ; durée 219.95 min ; blocs 53228503 → 53235101 (6384 vus)

## Connexion
- Requêtes RPC : 76484 ; erreurs : 0 ; latence p50/p95 : 240.4/810.9 ms
- Rafraîchissements d'état : 6384 ; âge des données au dernier bloc : 3.17 s ; changements de frais LP observés (pools à frais dynamiques) : 6990
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 63193 ; cycles déclenchés par événement : 5549 ; avance médiane sur le rafraîchissement multicall : 478 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,310.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 512 pools, 294 jetons, 18990 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 116, aerodrome 210, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 182 (rejetés 2) → 587 jetons ; pools candidats 3756 (énumérés 325, par paires 0), mesurés 514, sous le plancher de 10000.0 $ : 2 → gardés 512 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2304.739386, 'cbBTC': 79763.083067, 'AERO': 0.667567}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,658,288 | 2,310.619367 | 53235101 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,336,159 | 0.028889 | 53235101 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,689,348 | 0.000013 | 53235101 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,340,149 | 0.028932 | 53235101 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,239,193 | 2,306.072322 | 53235101 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,105,208 | 98.493170 | 53235101 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,947,142 | 0.001633 | 53235101 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,561,056 | 1.489076 | 53235101 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,741,643 | 0.028894 | 53235101 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,751,254 | 2,306.627950 | 53235101 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,390,802 | 2,306.471344 | 53235101 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,210,652 | 0.998956 | 53235101 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,609,180 | 38,359.102628 | 53235101 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,900,307 | 0.028945 | 53235101 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,459,800 | 98.460561 | 53235101 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,337,289 | 0.000013 | 53235101 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,110,957 | 1,214,695.545645 | 53235101 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,847,045 | 0.019242 | 53235101 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | WETH/USDC | 3000 | 1,812,234 | 2,311.360148 | 53235101 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,757,654 | 404.278080 | 53235101 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,747,537 | 0.000000 | 53235101 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,707,079 | 0.000013 | 53235101 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,686,668 | 0.000012 | 53235101 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 1,600,239 | 0.000013 | 53235101 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53235101 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,116 | 0.827421 | 53235101 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,419,067 | 3,432.121065 | 53235101 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,372,774 | 0.005260 | 53235101 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,368,045 | 13,983.409671 | 53235101 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,263,290 | 2,306.058934 | 53235101 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,218,820 | 0.000261 | 53235101 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,190,327 | 68.581891 | 53235101 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,138,400 | 36,690,876.254683 | 53235101 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,134,976 | 1,086,105.361534 | 53235101 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,127,155 | 0.000263 | 53235101 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,099,113 | 502,961.769662 | 53235101 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,089,254 | 0.000000 | 53235101 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,051,577 | 21,582,524.904682 | 53235101 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,051,131 | 73,773.024012 | 53235101 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,041,242 | 16.937186 | 53235101 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/AERO | 10000 | 1,041,122 | 3,431.088863 | 53235101 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/USDC | 3000 | 1,023,593 | 2,310.710052 | 53235101 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/NOCK | 3000 | 1,019,295 | 60.252922 | 53235101 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 981,619 | 99.001743 | 53235101 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 981,049 | 0.042690 | 53235101 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 933,909 | 2,314.580420 | 53235101 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 913,474 | 1,062.282854 | 53235101 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 890,985 | 0.000557 | 53235101 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | QUID/USDC | 100 | 864,774 | 0.067867 | 53235101 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 863,543 | 18.512286 | 53235101 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/msETH (stable) | 500 | 862,439 | 2.328586 | 53235101 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 823,915 | 17.754917 | 53235101 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 782,009 | 0.803812 | 53235101 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 741,454 | 4,585,567.667335 | 53235101 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 735,561 | 0.000008 | 53235101 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 732,026 | 0.601728 | 53235101 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 693,508 | 139,814.178396 | 53235101 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 685,150 | 506,958.858899 | 53235101 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 653,867 | 0.539542 | 53235101 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 629,847 | 0.097477 | 53235101 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 11932 ; routes examinées : 226588680 ; candidats optimisés : 895096 ; net attendu > 0 : 313 ; dernier cycle 80.3 ms
- Rejets (moteur) : {'spread_below_threshold': 223436262, 'liquidity_below_min': 2227593, 'negative_expected_net': 894783, 'unquotable': 15643, 'borrow_bound_too_small': 11931, 'cycle_budget_exhausted': 2155}
- Enregistrements de la session : 895096 ; net attendu > 0 : 313 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 895096} ; motifs de rejet : {'below_safety_margin': 305, 'negative_expected_net': 894783, 'p_lower_below_threshold': 295, 'reliability_not_demonstrated': 18, 'stale_data': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53231893 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.237019 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(6065471298323<47403803883803), stale_data(4320ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53231894 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.237019 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(6065471298323<47403803883803), stale_data(4461ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53231893 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 545.796287 USDC | 0.019313 USDC | 0.000000 USDC | 0.005222 USDC | 0.014091 USDC (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(14091<109159), stale_data(4323ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53231894 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 545.796287 USDC | 0.019313 USDC | 0.000000 USDC | 0.005222 USDC | 0.014091 USDC (0.0130 €) | — | 0.26 | 0.031 (n=113) | REJECTED | below_safety_margin(14091<109159), stale_data(4465ms>4000.0), p_lower_below_threshold(0.03<0.75) |
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
| 53232489 | WETH→[uniswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.029572 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0036 €) | — | 0.58 | 0.010 (n=28) | REJECTED | below_safety_margin(1700432660305<5914385718807), reliability_not_demonstrated |
| 53232489 | WETH→[uniswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.029572 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0036 €) | — | 0.58 | 0.010 (n=28) | REJECTED | below_safety_margin(1700432660305<5914385718807), reliability_not_demonstrated |
| 53232489 | WETH→[pancakeswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.027846 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0028 €) | — | 0.47 | 0.031 (n=113) | REJECTED | below_safety_margin(1302313181647<5569188595031), p_lower_below_threshold(0.03<0.75) |
| 53232489 | WETH→[pancakeswap_v3]→cbETH→[aerodrome_slipstream]→WETH | 0.027846 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0028 €) | — | 0.47 | 0.031 (n=113) | REJECTED | below_safety_margin(1302313181647<5569188595031), p_lower_below_threshold(0.03<0.75) |
| 53229792 | USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 18.949496 USDC | 0.009492 USDC | 0.000000 USDC | 0.006620 USDC | 0.002872 USDC (0.0026 €) | — | 1.52 | 0.148 (n=121) | REJECTED | below_safety_margin(2872<3789), p_lower_below_threshold(0.15<0.75) |
| 53232797 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004740 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | 0.000001 WETH | 2.60 | 0.167 (n=221) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53229792 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.008235 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0026 €) | — | 1.50 | 0.148 (n=121) | REJECTED | below_safety_margin(1234292194565<1646975313604), p_lower_below_threshold(0.15<0.75) |

## Fiabilité et décision
- Observations ghost : 3100 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
