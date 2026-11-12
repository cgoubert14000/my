# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T23:04:19+00:00 ; durée 52.27 min ; blocs 56655713 → 56671378 (3343 vus)

## Connexion
- Requêtes RPC : 42368 ; erreurs : 0 ; latence p50/p95 : 182.7/984.1 ms
- Rafraîchissements d'état : 3343 ; âge des données au dernier bloc : 6.51 s ; changements de frais LP observés (pools à frais dynamiques) : 1191
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3743 ; cycles déclenchés par événement : 1537 ; avance médiane sur le rafraîchissement multicall : 370 ms
- Gaz : base fee 0.005006 gwei ; prix ETH (pool le plus profond) : 2,013.08 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 266 jetons, 14822 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3621 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2015.232847, 'cbBTC': 71439.030081, 'AERO': 0.524681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,567,032 | 2,013.076000 | 56671398 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,335,661 | 0.028227 | 56671398 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,520,423 | 0.028170 | 56671398 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,135,303 | 0.000014 | 56671398 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,857,723 | 2,014.670273 | 56671398 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,663,955 | 106.322585 | 56671398 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,201,276 | 0.028228 | 56671398 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,140,198 | 1.910419 | 56671398 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,108,352 | 2,015.246731 | 56671398 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,756,351 | 0.998724 | 56671398 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,987,105 | 42,503.412415 | 56671398 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 169 | 2,796,993 | 2,015.082199 | 56671398 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,152,434 | 0.028182 | 56671398 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,879,393 | 1,163,003.281972 | 56671398 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,643,891 | 0.016726 | 56671398 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,598,245 | 0.000014 | 56671398 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,565,819 | 0.000014 | 56671398 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,503,115 | 0.000000 | 56671398 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,487,662 | 0.006571 | 56671398 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,469,135 | 0.000014 | 56671398 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,710 | 0.831859 | 56671398 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,383,589 | 424.273558 | 56671398 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,258,240 | 2,014.834690 | 56671398 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,225,396 | 3,840.713492 | 56671398 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,189,174 | 15,052.991792 | 56671398 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,143,504 | 2,013.421399 | 56671398 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,098,983 | 2,014.690661 | 56671398 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,912 | 86.333633 | 56671398 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,037,340 | 1.402298 | 56671398 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,003,992 | 35,458,223.889743 | 56671398 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 983,907 | 106.184688 | 56671398 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,319 | 20.081868 | 56671398 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 921,868 | 559,043.576846 | 56671398 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 888,374 | 0.001495 | 56671398 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 882,413 | 23,226,178.240886 | 56671398 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 871,967 | 0.052788 | 56671398 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 871,704 | 1,000.366142 | 56671398 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 869,220 | 2,005.198605 | 56671398 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 865,733 | 0.000014 | 56671398 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 806,623 | 0.000000 | 56671398 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 779,763 | 77.358327 | 56671398 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 747,981 | 0.049849 | 56671398 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 746,461 | 23.067643 | 56671398 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 687,081 | 3,863.880959 | 56671398 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 682,032 | 0.801801 | 56671398 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 662,895 | 0.525869 | 56671398 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 623,763 | 4,939,300.387967 | 56671398 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 603,176 | 0.458194 | 56671398 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 582,751 | 151,294.920400 | 56671398 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 567,028 | 0.000260 | 56671398 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 566,159 | 554,895.046951 | 56671398 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,655 | 0.037895 | 56671398 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 556,343 | 0.000007 | 56671398 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 485,720 | 1,000.314131 | 56671398 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 458,713 | 0.065810 | 56671398 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 449,547 | 1.000979 | 56671398 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 449,513 | 0.499782 | 56671398 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 435,191 | 333.133817 | 56671398 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 429,304 | 24.862308 | 56671398 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 423,639 | 914,999.414728 | 56671398 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 4879 ; routes examinées : 72316538 ; candidats optimisés : 321170 ; net attendu > 0 : 311 ; dernier cycle 73.4 ms
- Rejets (moteur) : {'spread_below_threshold': 70787057, 'liquidity_below_min': 1206019, 'negative_expected_net': 320859, 'borrow_bound_too_small': 1975, 'unquotable': 242, 'cycle_budget_exhausted': 75}
- Enregistrements de la session : 321170 ; net attendu > 0 : 311 ; simulés (eth_call de la vraie tx) : 24 (ok 19, échec 5) ; étiquettes ghost N+1 : 16/17 positives
- Décisions : {'REJECTED': 321170} ; motifs de rejet : {'below_safety_margin': 261, 'negative_expected_net': 320859, 'p_lower_below_threshold': 303, 'reliability_not_demonstrated': 8, 'sim_below_estimate': 17, 'simulated_net_nonpositive': 10, 'simulation_failed': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56660485 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 26.746133 USDC | 0.021836 USDC | 0.000000 USDC | 0.004527 USDC | 0.017309 USDC (0.0159 €) | — | 6.47 | 0.076 (n=503) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 56660486 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 19.597201 USDC | 0.011690 USDC | 0.000000 USDC | 0.004527 USDC | 0.007163 USDC (0.0066 €) | — | 3.66 | 0.076 (n=503) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 56661371 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.005092 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0052 €) | 0.000000 WETH | 5.51 | 0.211 (n=1280) | REJECTED | sim_below_estimate(3486903282408<5815101595038), p_lower_below_threshold(0.21<0.75) |
| 56661371 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 10.166637 USDC | 0.011701 USDC | 0.000000 USDC | 0.006059 USDC | 0.005642 USDC (0.0052 €) | — | 5.55 | 0.211 (n=1280) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 56656791 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 185.539711 USDC | 0.011603 USDC | 0.000000 USDC | 0.006085 USDC | 0.005518 USDC (0.0051 €) | — | 0.30 | 0.270 (n=1622) | REJECTED | below_safety_margin(5518<37107), p_lower_below_threshold(0.27<0.75) |
| 56656795 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 185.539711 USDC | 0.011603 USDC | 0.000000 USDC | 0.006085 USDC | 0.005518 USDC (0.0051 €) | — | 0.30 | 0.270 (n=1622) | REJECTED | below_safety_margin(5518<37107), p_lower_below_threshold(0.27<0.75) |
| 56656791 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.073455 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | — | 0.36 | 0.270 (n=1622) | REJECTED | below_safety_margin(2652904339512<14691081269871), p_lower_below_threshold(0.27<0.75) |
| 56656795 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.073455 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | — | 0.36 | 0.270 (n=1622) | REJECTED | below_safety_margin(2652904339512<14691081269871), p_lower_below_threshold(0.27<0.75) |
| 56661371 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.005054 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | 0.000000 WETH | 5.25 | 0.326 (n=604) | REJECTED | sim_below_estimate(3351052862314<5661548829623), p_lower_below_threshold(0.33<0.75) |
| 56661371 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 10.094298 USDC | 0.011393 USDC | 0.000000 USDC | 0.006059 USDC | 0.005334 USDC (0.0049 €) | — | 5.28 | 0.326 (n=604) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 56656791 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002789 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0046 €) | — | 0.25 | 0.270 (n=1622) | REJECTED | below_safety_margin(7<55), p_lower_below_threshold(0.27<0.75) |
| 56656795 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002789 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0046 €) | — | 0.25 | 0.270 (n=1622) | REJECTED | below_safety_margin(7<55), p_lower_below_threshold(0.27<0.75) |
| 56661371 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004931 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0045 €) | 0.000000 WETH | 4.95 | 0.326 (n=604) | REJECTED | sim_below_estimate(3193846283988<5448071900117), p_lower_below_threshold(0.33<0.75) |
| 56661371 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 9.847331 USDC | 0.010962 USDC | 0.000000 USDC | 0.006059 USDC | 0.004903 USDC (0.0045 €) | — | 4.98 | 0.326 (n=604) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 56656790 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.114811 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(2197903303363<22962287772088), reliability_not_demonstrated |
| 56656793 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.114811 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(2197903303363<22962287772088), reliability_not_demonstrated |
| 56656790 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 227.968388 USDC | 0.008955 USDC | 0.000000 USDC | 0.004547 USDC | 0.004408 USDC (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(4408<45593), reliability_not_demonstrated |
| 56656793 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 227.968388 USDC | 0.008955 USDC | 0.000000 USDC | 0.004547 USDC | 0.004408 USDC (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(4408<45593), reliability_not_demonstrated |
| 56661371 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004017 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0038 €) | — | 5.05 | 0.326 (n=604) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 56661371 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 7.999996 USDC | 0.010126 USDC | 0.000000 USDC | 0.006059 USDC | 0.004067 USDC (0.0037 €) | — | 5.08 | 0.326 (n=604) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 56661187 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.004725 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0037 €) | 0.000000 WETH | 4.17 | 0.210 (n=1278) | REJECTED | sim_below_estimate(3022261654781<4979512263742), p_lower_below_threshold(0.21<0.75) |
| 56661187 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 9.413961 USDC | 0.010022 USDC | 0.000000 USDC | 0.006058 USDC | 0.003964 USDC (0.0036 €) | — | 4.21 | 0.210 (n=1278) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 56661322 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.004541 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0030 €) | 0.000001 WETH | 3.61 | 0.325 (n=603) | REJECTED | sim_below_estimate(4150780651186<4648464866956), p_lower_below_threshold(0.33<0.75) |
| 56661322 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 9.116613 USDC | 0.009354 USDC | 0.000000 USDC | 0.006059 USDC | 0.003295 USDC (0.0030 €) | — | 3.61 | 0.325 (n=603) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 56661008 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.004530 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0029 €) | 0.000000 WETH | 3.48 | 0.323 (n=601) | REJECTED | sim_below_estimate(3155800376288<4585638879644), p_lower_below_threshold(0.32<0.75) |

## Fiabilité et décision
- Observations ghost : 8485 ; taux observé 0.224 ; borne inférieure crédible (0.9) 0.219 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.9% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
