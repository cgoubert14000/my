# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T22:21:13+00:00 ; durée 9.16 min ; blocs 56655713 → 56658453 (586 vus)

## Connexion
- Requêtes RPC : 7476 ; erreurs : 0 ; latence p50/p95 : 180.7/910.4 ms
- Rafraîchissements d'état : 586 ; âge des données au dernier bloc : 6.74 s ; changements de frais LP observés (pools à frais dynamiques) : 246
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 822 ; cycles déclenchés par événement : 297 ; avance médiane sur le rafraîchissement multicall : 393 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,014.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 266 jetons, 14822 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3621 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2015.232847, 'cbBTC': 71439.030081, 'AERO': 0.524681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,622,434 | 2,014.535955 | 56658474 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,355,881 | 0.028170 | 56658474 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,531,866 | 0.028170 | 56658474 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,151,460 | 0.000014 | 56658474 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,860,232 | 2,009.582461 | 56658474 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,667,127 | 106.375542 | 56658474 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,211,296 | 0.028159 | 56658474 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,143,050 | 1.909173 | 56658474 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,103,101 | 2,010.380985 | 56658474 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,766,606 | 0.998724 | 56658474 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,964,327 | 43,221.760244 | 56658474 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 115 | 2,804,967 | 2,010.336980 | 56658474 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,155,317 | 0.028182 | 56658474 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,880,756 | 1,163,003.281972 | 56658474 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,640,178 | 0.016668 | 56658474 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,601,635 | 0.000014 | 56658474 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,569,350 | 0.000014 | 56658474 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,504,211 | 0.000000 | 56658474 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,482,797 | 0.006541 | 56658474 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,471,967 | 0.000014 | 56658474 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,867 | 0.831699 | 56658474 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,382,790 | 426.189011 | 56658474 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,258,696 | 2,014.576696 | 56658474 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,226,210 | 3,837.712617 | 56658474 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,189,013 | 15,134.189129 | 56658474 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,143,920 | 2,014.943214 | 56658474 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,099,585 | 2,009.578272 | 56658474 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,906 | 86.334668 | 56658474 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,037,340 | 1.402298 | 56658474 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,005,423 | 35,384,516.220924 | 56658474 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 984,299 | 106.184689 | 56658474 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,118 | 20.094044 | 56658474 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 922,014 | 559,964.211944 | 56658474 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 889,978 | 0.001492 | 56658474 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 883,053 | 23,226,178.240886 | 56658474 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 872,126 | 0.052875 | 56658474 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 871,742 | 1,002.023251 | 56658474 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 869,486 | 2,005.198605 | 56658474 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 867,981 | 0.000014 | 56658474 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 813,501 | 0.000000 | 56658474 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 783,888 | 76.546366 | 56658474 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 747,636 | 0.049802 | 56658474 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 746,462 | 23.067562 | 56658474 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 687,554 | 3,863.880959 | 56658474 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 682,527 | 0.801801 | 56658474 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | WETH/EDEL | 7000 | 671,688 | 137,111.225885 | 56658474 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 663,284 | 0.523679 | 56658474 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 623,783 | 4,946,140.933560 | 56658474 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 603,649 | 0.458886 | 56658474 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 582,912 | 151,430.597931 | 56658474 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 567,440 | 0.000260 | 56658474 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 566,082 | 556,107.219215 | 56658474 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 559,976 | 0.037928 | 56658474 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 557,083 | 0.000007 | 56658474 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2730 | 485,725 | 1,002.277615 | 56658474 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 460,386 | 0.066114 | 56658474 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 449,548 | 1.000977 | 56658474 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 449,267 | 0.499782 | 56658474 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 435,506 | 333.133889 | 56658474 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 429,615 | 24.862308 | 56658474 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 882 ; routes examinées : 13073004 ; candidats optimisés : 61558 ; net attendu > 0 : 150 ; dernier cycle 44.3 ms
- Rejets (moteur) : {'spread_below_threshold': 12835168, 'liquidity_below_min': 176222, 'negative_expected_net': 61408, 'cycle_budget_exhausted': 56}
- Enregistrements de la session : 61558 ; net attendu > 0 : 150 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 61558} ; motifs de rejet : {'below_safety_margin': 150, 'negative_expected_net': 61408, 'p_lower_below_threshold': 142, 'reliability_not_demonstrated': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56656791 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 185.539711 USDC | 0.011603 USDC | 0.000000 USDC | 0.006085 USDC | 0.005518 USDC (0.0051 €) | — | 0.30 | 0.270 (n=1622) | REJECTED | below_safety_margin(5518<37107), p_lower_below_threshold(0.27<0.75) |
| 56656795 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 185.539711 USDC | 0.011603 USDC | 0.000000 USDC | 0.006085 USDC | 0.005518 USDC (0.0051 €) | — | 0.30 | 0.270 (n=1622) | REJECTED | below_safety_margin(5518<37107), p_lower_below_threshold(0.27<0.75) |
| 56656791 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.073455 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | — | 0.36 | 0.270 (n=1622) | REJECTED | below_safety_margin(2652904339512<14691081269871), p_lower_below_threshold(0.27<0.75) |
| 56656795 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.073455 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0049 €) | — | 0.36 | 0.270 (n=1622) | REJECTED | below_safety_margin(2652904339512<14691081269871), p_lower_below_threshold(0.27<0.75) |
| 56656791 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002789 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0046 €) | — | 0.25 | 0.270 (n=1622) | REJECTED | below_safety_margin(7<55), p_lower_below_threshold(0.27<0.75) |
| 56656795 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002789 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0046 €) | — | 0.25 | 0.270 (n=1622) | REJECTED | below_safety_margin(7<55), p_lower_below_threshold(0.27<0.75) |
| 56656790 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.114811 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(2197903303363<22962287772088), reliability_not_demonstrated |
| 56656793 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.114811 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(2197903303363<22962287772088), reliability_not_demonstrated |
| 56656790 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 227.968388 USDC | 0.008955 USDC | 0.000000 USDC | 0.004547 USDC | 0.004408 USDC (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(4408<45593), reliability_not_demonstrated |
| 56656793 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 227.968388 USDC | 0.008955 USDC | 0.000000 USDC | 0.004547 USDC | 0.004408 USDC (0.0041 €) | — | 0.19 | 0.055 (n=15) | REJECTED | below_safety_margin(4408<45593), reliability_not_demonstrated |
| 56656791 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000636 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0026 €) | — | 0.63 | 0.270 (n=1622) | REJECTED | below_safety_margin(4<12), p_lower_below_threshold(0.27<0.75) |
| 56656795 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000636 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0026 €) | — | 0.63 | 0.270 (n=1622) | REJECTED | below_safety_margin(4<12), p_lower_below_threshold(0.27<0.75) |
| 56656791 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 45.637786 USDC | 0.008615 USDC | 0.000000 USDC | 0.006085 USDC | 0.002530 USDC (0.0023 €) | — | 0.55 | 0.270 (n=1622) | REJECTED | below_safety_margin(2530<9127), p_lower_below_threshold(0.27<0.75) |
| 56656795 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 45.637786 USDC | 0.008615 USDC | 0.000000 USDC | 0.006085 USDC | 0.002530 USDC (0.0023 €) | — | 0.55 | 0.270 (n=1622) | REJECTED | below_safety_margin(2530<9127), p_lower_below_threshold(0.27<0.75) |
| 56656791 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025189 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.50 | 0.270 (n=1622) | REJECTED | below_safety_margin(1250770259656<5037766025930), p_lower_below_threshold(0.27<0.75) |
| 56656795 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025189 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0023 €) | — | 0.50 | 0.270 (n=1622) | REJECTED | below_safety_margin(1250770259656<5037766025930), p_lower_below_threshold(0.27<0.75) |
| 56656789 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.028884 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.31 | 0.114 (n=32) | REJECTED | below_safety_margin(885024049728<5776864792472), p_lower_below_threshold(0.11<0.75) |
| 56656793 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.028884 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.31 | 0.114 (n=32) | REJECTED | below_safety_margin(885024049728<5776864792472), p_lower_below_threshold(0.11<0.75) |
| 56656789 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 57.314891 USDC | 0.006035 USDC | 0.000000 USDC | 0.004266 USDC | 0.001769 USDC (0.0016 €) | — | 0.31 | 0.114 (n=32) | REJECTED | below_safety_margin(1769<11462), p_lower_below_threshold(0.11<0.75) |
| 56656793 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 57.314891 USDC | 0.006035 USDC | 0.000000 USDC | 0.004266 USDC | 0.001769 USDC (0.0016 €) | — | 0.31 | 0.114 (n=32) | REJECTED | below_safety_margin(1769<11462), p_lower_below_threshold(0.11<0.75) |
| 56656790 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.028637 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.30 | 0.114 (n=32) | REJECTED | below_safety_margin(853758186821<5727330037156), p_lower_below_threshold(0.11<0.75) |
| 56656793 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.028637 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.30 | 0.114 (n=32) | REJECTED | below_safety_margin(853758186821<5727330037156), p_lower_below_threshold(0.11<0.75) |
| 56656789 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.028409 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.30 | 0.253 (n=31) | REJECTED | below_safety_margin(850045041135<5681819141776), p_lower_below_threshold(0.25<0.75) |
| 56656793 | WETH→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.028409 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.30 | 0.253 (n=31) | REJECTED | below_safety_margin(850045041135<5681819141776), p_lower_below_threshold(0.25<0.75) |
| 56656790 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 57.007378 USDC | 0.005974 USDC | 0.000000 USDC | 0.004268 USDC | 0.001706 USDC (0.0016 €) | — | 0.30 | 0.114 (n=32) | REJECTED | below_safety_margin(1706<11401), p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 8468 ; taux observé 0.223 ; borne inférieure crédible (0.9) 0.217 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
