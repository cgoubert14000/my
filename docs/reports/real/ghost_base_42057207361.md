# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T19:24:54+00:00 ; durée 219.94 min ; blocs 53552072 → 53581527 (5652 vus)

## Connexion
- Requêtes RPC : 85149 ; erreurs : 60 ; latence p50/p95 : 407.2/1,723.0 ms
- Rafraîchissements d'état : 5652 ; âge des données au dernier bloc : 8.52 s ; changements de frais LP observés (pools à frais dynamiques) : 17460
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 31082 ; cycles déclenchés par événement : 816 ; avance médiane sur le rafraîchissement multicall : 562 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,253.92 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 485 pools, 283 jetons, 19058 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 102, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3708 (énumérés 302, par paires 0), mesurés 488, sous le plancher de 10000.0 $ : 3 → gardés 485 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2284.245505, 'cbBTC': 76255.016176, 'AERO': 0.595113}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,950,243 | 2,253.918690 | 53581555 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,618,601 | 0.029607 | 53581555 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,183,671 | 0.000013 | 53581555 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,098,223 | 0.029636 | 53581555 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,912,445 | 2,248.279253 | 53581555 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,456,455 | 106.842845 | 53581555 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,422,149 | 0.001541 | 53581555 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,138,728 | 1.654710 | 53581555 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,682,554 | 0.029596 | 53581555 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,124,357 | 2,248.339948 | 53581555 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,011,077 | 0.998641 | 53581555 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,372,248 | 41,807.357227 | 53581555 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 922 | 3,253,311 | 2,247.963892 | 53581555 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,579,565 | 0.029622 | 53581555 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,105,765 | 1,161,509.435455 | 53581555 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,880,938 | 0.007611 | 53581555 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,748,227 | 0.000013 | 53581555 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,645,477 | 0.016569 | 53581555 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,642,257 | 0.000000 | 53581555 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,629,229 | 0.000013 | 53581555 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,525,452 | 448.742064 | 53581555 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,525,231 | 1.463979 | 53581555 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,524,188 | 0.000013 | 53581555 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,284 | 0.816558 | 53581555 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,385,622 | 3,727.424082 | 53581555 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,330,617 | 2,251.965023 | 53581555 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,330,307 | 2,253.962557 | 53581555 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,262,433 | 15,183.859492 | 53581555 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,168,961 | 2,248.217896 | 53581555 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,150,791 | 73.374722 | 53581555 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,102,642 | 37,467,805.216865 | 53581555 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,058,888 | 107.584998 | 53581555 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,024,606 | 574,534.007069 | 53581555 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,017,734 | 0.000000 | 53581555 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,000,175 | 22,702,749.945452 | 53581555 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,269 | 21.384041 | 53581555 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 950,329 | 69.428306 | 53581555 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 937,889 | 2,262.763763 | 53581555 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 932,043 | 1,081.061357 | 53581555 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 368 | 926,642 | 0.000013 | 53581555 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 886,526 | 98,602.810017 | 53581555 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 860,519 | 0.000545 | 53581555 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 850,806 | 0.047534 | 53581555 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 801,032 | 3,756.465193 | 53581555 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,720 | 0.056108 | 53581555 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 788,105 | 21.332589 | 53581555 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 764,774 | 0.799698 | 53581555 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 712,103 | 0.567367 | 53581555 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 693,500 | 4,997,701.650854 | 53581555 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 683,985 | 0.000249 | 53581555 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 667,242 | 144,200.361958 | 53581555 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 654,271 | 0.000008 | 53581555 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 648,468 | 0.533313 | 53581555 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2105 | 624,144 | 569,489.717011 | 53581555 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 604,990 | 0.914024 | 53581555 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 600,802 | 2.482559 | 53581555 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,524 | 0.037441 | 53581555 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 546,312 | 0.083722 | 53581555 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 540,575 | 839,695.546249 | 53581555 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 523,944 | 2,248.141723 | 53581555 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 6467 ; routes examinées : 123248086 ; candidats optimisés : 498129 ; net attendu > 0 : 3860 ; dernier cycle 266.9 ms
- Rejets (moteur) : {'spread_below_threshold': 119990646, 'liquidity_below_min': 2449303, 'negative_expected_net': 494269, 'pool_quarantined': 243862, 'unquotable': 45027, 'cycle_budget_exhausted': 18179, 'borrow_bound_too_small': 2940}
- Enregistrements de la session : 498129 ; net attendu > 0 : 3860 ; simulés (eth_call de la vraie tx) : 100 (ok 57, échec 43) ; étiquettes ghost N+1 : 20/92 positives
- Décisions : {'REJECTED': 498129} ; motifs de rejet : {'below_safety_margin': 3316, 'negative_expected_net': 494269, 'p_lower_below_threshold': 3418, 'price_impact': 5, 'reliability_not_demonstrated': 442, 'sim_below_estimate': 6, 'simulated_net_nonpositive': 3, 'simulation_failed': 43, 'stale_data': 412}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53553715 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 144.695729 USDC | 1.993485 USDC | 0.000000 USDC | 0.005193 USDC | 1.988292 USDC (1.8292 €) | — | 137.41 | 0.000 (n=19) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.026532 cbBTC | 0.000008 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000008 cbBTC (0.5547 €) | — | 2.98 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.912068 WETH | 0.000269 WETH | 0.000000 WETH | 0.000004 WETH | 0.000265 WETH (0.5545 €) | — | 2.90 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 2,097.083342 USDC | 0.610892 USDC | 0.000000 USDC | 0.010208 USDC | 0.600684 USDC (0.5526 €) | — | 2.86 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.019735 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3639 €) | — | 2.63 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.659335 WETH | 0.000178 WETH | 0.000000 WETH | 0.000004 WETH | 0.000173 WETH (0.3632 €) | — | 2.63 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,516.653550 USDC | 0.403237 USDC | 0.000000 USDC | 0.009805 USDC | 0.393432 USDC (0.3620 €) | — | 2.59 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.020368 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3604 €) | — | 2.52 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.718376 WETH | 0.000176 WETH | 0.000000 WETH | 0.000004 WETH | 0.000172 WETH (0.3602 €) | — | 2.39 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,601.921125 USDC | 0.400158 USDC | 0.000000 USDC | 0.009805 USDC | 0.390353 USDC (0.3591 €) | — | 2.44 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014238 cbBTC | 0.000004 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2868 €) | — | 2.87 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.484150 WETH | 0.000141 WETH | 0.000000 WETH | 0.000004 WETH | 0.000137 WETH (0.2864 €) | — | 2.82 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,073.308521 USDC | 0.320024 USDC | 0.000000 USDC | 0.009805 USDC | 0.310219 USDC (0.2854 €) | — | 2.89 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.502872 WETH | 0.000116 WETH | 0.000000 WETH | 0.000004 WETH | 0.000112 WETH (0.2355 €) | — | 2.23 | 0.169 (n=990) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.014013 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2347 €) | — | 2.39 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,103.822096 USDC | 0.264249 USDC | 0.000000 USDC | 0.009416 USDC | 0.254833 USDC (0.2344 €) | — | 2.31 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.014087 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2328 €) | — | 2.36 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.490067 WETH | 0.000116 WETH | 0.000000 WETH | 0.000005 WETH | 0.000111 WETH (0.2328 €) | — | 2.27 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,088.666081 USDC | 0.262671 USDC | 0.000000 USDC | 0.010611 USDC | 0.252060 USDC (0.2319 €) | — | 2.32 | 0.169 (n=990) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53552258 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.581731 WETH | 0.000114 WETH | 0.000000 WETH | 0.000004 WETH | 0.000110 WETH (0.2306 €) | — | 1.89 | 0.231 (n=391) | REJECTED | below_safety_margin(110029994644477<116346177193278), p_lower_below_threshold(0.23<0.75) |
| 53552258 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.016774 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2305 €) | — | 1.96 | 0.231 (n=391) | REJECTED | below_safety_margin(329<335), p_lower_below_threshold(0.23<0.75) |
| 53559910 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,260.784372 USDC | 0.257906 USDC | 0.000000 USDC | 0.007598 USDC | 0.250308 USDC (0.2303 €) | — | 1.99 | 0.167 (n=1011) | REJECTED | below_safety_margin(250308<252156), stale_data(5037ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53552258 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 1,318.542935 USDC | 0.259038 USDC | 0.000000 USDC | 0.009012 USDC | 0.250026 USDC (0.2300 €) | — | 1.90 | 0.231 (n=391) | REJECTED | below_safety_margin(250026<263708), p_lower_below_threshold(0.23<0.75) |
| 53559910 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.559951 WETH | 0.000114 WETH | 0.000000 WETH | 0.000003 WETH | 0.000111 WETH (0.2297 €) | — | 1.98 | 0.167 (n=1011) | REJECTED | below_safety_margin(110999596126744<111990164369510), stale_data(5018ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53559910 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.016346 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2295 €) | — | 2.01 | 0.167 (n=1011) | REJECTED | stale_data(5028ms>4000.0), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5767 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
