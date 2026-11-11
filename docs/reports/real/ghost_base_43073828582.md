# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T22:48:06+00:00 ; durée 281.06 min ; blocs 56150210 → 56234438 (13026 vus)

## Connexion
- Requêtes RPC : 170053 ; erreurs : 60 ; latence p50/p95 : 180.1/1,855.3 ms
- Rafraîchissements d'état : 13026 ; âge des données au dernier bloc : 10.0 s ; changements de frais LP observés (pools à frais dynamiques) : 9581
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12231 ; cycles déclenchés par événement : 4565 ; avance médiane sur le rafraîchissement multicall : 760 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,060.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 462 pools, 267 jetons, 16678 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 100, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3639 (énumérés 284, par paires 0), mesurés 464, sous le plancher de 10000.0 $ : 2 → gardés 462 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2091.017157, 'cbBTC': 74374.029387, 'AERO': 0.55788}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,670,950 | 2,060.419765 | 56234465 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,493,693 | 0.027784 | 56234465 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,610,967 | 0.027847 | 56234465 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,547,524 | 0.000014 | 56234465 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,101,264 | 2,057.451147 | 56234465 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,882,536 | 104.419957 | 56234465 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,610,204 | 0.027790 | 56234465 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,252,741 | 1.839476 | 56234465 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,033,223 | 2,058.168512 | 56234465 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,907,526 | 0.998583 | 56234465 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,039,658 | 43,000.439518 | 56234465 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 107 | 2,902,353 | 2,058.308672 | 56234465 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 2,212,703 | 0.027835 | 56234465 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,957,533 | 1,123,024.323907 | 56234465 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,650,822 | 0.000014 | 56234465 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,620,042 | 0.016355 | 56234465 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,613,054 | 0.000014 | 56234465 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,571,729 | 0.000000 | 56234465 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,535,542 | 0.000013 | 56234465 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,510,590 | 0.006489 | 56234465 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,089 | 0.830438 | 56234465 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56234465 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,413,724 | 427.002909 | 56234465 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,845 | 2,060.831561 | 56234465 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,264,284 | 3,784.760219 | 56234465 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,224,361 | 15,323.849394 | 56234465 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,708 | 2,060.852545 | 56234465 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,129,371 | 2,057.311402 | 56234465 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56234465 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,042,216 | 33,772,120.759778 | 56234465 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,021,658 | 103.682399 | 56234465 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,703 | 21.341364 | 56234465 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 941,988 | 561,773.117755 | 56234465 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 919,294 | 0.001480 | 56234465 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 907,043 | 0.000014 | 56234465 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 904,972 | 23,106,451.822214 | 56234465 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 902,628 | 0.050724 | 56234465 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 879,698 | 2,075.094055 | 56234465 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 877,822 | 1,030.272154 | 56234465 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 861,944 | 0.000000 | 56234465 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 777,567 | 77.795971 | 56234465 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 766,081 | 0.052372 | 56234465 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 752,376 | 114,337.239981 | 56234465 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4585 | 748,216 | 22.984948 | 56234465 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 708,851 | 3,758.809430 | 56234465 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 698,073 | 0.801801 | 56234465 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,978 | 0.529916 | 56234465 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 651,604 | 4,740,545.552396 | 56234465 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 620,715 | 0.484711 | 56234465 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 604,701 | 147,123.247345 | 56234465 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 588,834 | 0.000007 | 56234465 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 582,059 | 0.000259 | 56234465 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 577,871 | 566,289.256410 | 56234465 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,114 | 0.037740 | 56234465 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 489,933 | 1,030.557113 | 56234465 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,764 | 0.066985 | 56234465 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,084 | 1.000883 | 56234465 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 453,291 | 0.497365 | 56234465 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 443,389 | 24.658494 | 56234465 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 440,689 | 913,397.669286 | 56234465 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 17590 ; routes examinées : 293366020 ; candidats optimisés : 1454802 ; net attendu > 0 : 1258 ; dernier cycle 394.1 ms
- Rejets (moteur) : {'spread_below_threshold': 286929918, 'liquidity_below_min': 4940597, 'negative_expected_net': 1453544, 'borrow_bound_too_small': 33792, 'cycle_budget_exhausted': 6850, 'unquotable': 61}
- Enregistrements de la session : 1454802 ; net attendu > 0 : 1258 ; simulés (eth_call de la vraie tx) : 50 (ok 35, échec 15) ; étiquettes ghost N+1 : 9/45 positives
- Décisions : {'REJECTED': 1454802} ; motifs de rejet : {'below_safety_margin': 1098, 'negative_expected_net': 1453544, 'p_lower_below_threshold': 1233, 'reliability_not_demonstrated': 25, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 15, 'stale_data': 329}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→WETH | 0.144994 WETH | 0.000244 WETH | 0.000000 WETH | 0.000002 WETH | 0.000241 WETH (0.4571 €) | — | 16.63 | 0.007 (n=114) | REJECTED | stale_data(5203ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.102478 WETH | 0.000199 WETH | 0.000000 WETH | 0.000003 WETH | 0.000196 WETH (0.3710 €) | — | 19.10 | 0.144 (n=237) | REJECTED | stale_data(5094ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 210.605820 USDC | 0.409443 USDC | 0.000000 USDC | 0.006845 USDC | 0.402598 USDC (0.3704 €) | — | 19.12 | 0.144 (n=237) | REJECTED | stale_data(5102ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.098810 WETH | 0.000188 WETH | 0.000000 WETH | 0.000003 WETH | 0.000185 WETH (0.3502 €) | — | 18.70 | 0.144 (n=237) | REJECTED | stale_data(5109ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 203.054716 USDC | 0.386967 USDC | 0.000000 USDC | 0.006845 USDC | 0.380122 USDC (0.3497 €) | — | 18.72 | 0.144 (n=237) | REJECTED | stale_data(5117ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.096276 WETH | 0.000182 WETH | 0.000000 WETH | 0.000003 WETH | 0.000178 WETH (0.3382 €) | — | 18.53 | 0.144 (n=237) | REJECTED | stale_data(5125ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 197.933923 USDC | 0.374016 USDC | 0.000000 USDC | 0.006845 USDC | 0.367171 USDC (0.3378 €) | — | 18.55 | 0.144 (n=237) | REJECTED | stale_data(5132ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.095388 WETH | 0.000174 WETH | 0.000000 WETH | 0.000003 WETH | 0.000171 WETH (0.3237 €) | — | 17.90 | 0.144 (n=237) | REJECTED | stale_data(5157ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 195.999591 USDC | 0.358302 USDC | 0.000000 USDC | 0.006845 USDC | 0.351457 USDC (0.3233 €) | — | 17.93 | 0.144 (n=237) | REJECTED | stale_data(5165ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.088769 WETH | 0.000149 WETH | 0.000000 WETH | 0.000003 WETH | 0.000146 WETH (0.2764 €) | — | 16.43 | 0.144 (n=237) | REJECTED | stale_data(5190ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 182.693531 USDC | 0.306984 USDC | 0.000000 USDC | 0.006845 USDC | 0.300139 USDC (0.2761 €) | — | 16.43 | 0.144 (n=237) | REJECTED | stale_data(5198ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002971 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1669 €) | — | 8.21 | 0.144 (n=236) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56178863 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.106755 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1668 €) | 0.000081 WETH | 8.18 | 0.144 (n=236) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56234265 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 103.752296 USDC | 0.182597 USDC | 0.000000 USDC | 0.006845 USDC | 0.175752 USDC (0.1617 €) | — | 16.94 | 0.144 (n=237) | REJECTED | stale_data(5182ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56234265 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.050415 WETH | 0.000089 WETH | 0.000000 WETH | 0.000003 WETH | 0.000085 WETH (0.1616 €) | — | 16.91 | 0.144 (n=237) | REJECTED | stale_data(5174ms>4000.0), p_lower_below_threshold(0.14<0.75) |
| 56197526 | WETH→[aerodrome]→RISE→[uniswap_v2]→WETH | 0.028799 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1611 €) | — | 29.26 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 56197527 | WETH→[aerodrome]→RISE→[uniswap_v2]→WETH | 0.028799 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1611 €) | — | 29.26 | 0.006 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002669 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1313 €) | — | 7.19 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.092146 WETH | 0.000071 WETH | 0.000000 WETH | 0.000003 WETH | 0.000068 WETH (0.1308 €) | 0.000063 WETH | 7.43 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002515 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1272 €) | — | 7.39 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.092157 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1270 €) | 0.000061 WETH | 7.21 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56234050 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.251484 WETH | 0.000054 WETH | 0.000000 WETH | 0.000002 WETH | 0.000052 WETH (0.0986 €) | — | 2.07 | 0.104 (n=360) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 56234050 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 515.793110 USDC | 0.111924 USDC | 0.000000 USDC | 0.004960 USDC | 0.106964 USDC (0.0984 €) | — | 2.07 | 0.104 (n=360) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 56207836 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008312 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0810 €) | — | 1.42 | 0.265 (n=1579) | REJECTED | below_safety_margin(118<166), p_lower_below_threshold(0.27<0.75) |
| 56207836 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008312 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0810 €) | — | 1.42 | 0.265 (n=1579) | REJECTED | below_safety_margin(118<166), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8209 ; taux observé 0.216 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
