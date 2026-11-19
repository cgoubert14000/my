# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-19T21:01:40+00:00 ; durée 223.52 min ; blocs 59591500 → 59658576 (10544 vus)

## Connexion
- Requêtes RPC : 117820 ; erreurs : 385 ; latence p50/p95 : 342.4/1,695.7 ms
- Rafraîchissements d'état : 10544 ; âge des données au dernier bloc : 9.21 s ; changements de frais LP observés (pools à frais dynamiques) : 9908
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 12317 ; cycles déclenchés par événement : 3595 ; avance médiane sur le rafraîchissement multicall : 262 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,760.39 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 428 pools, 248 jetons, 13064 routes
- Par DEX : uniswap_v3 129, aerodrome 172, aerodrome_slipstream 87, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3579 (énumérés 257, par paires 0), mesurés 430, sous le plancher de 10000.0 $ : 2 → gardés 428 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 1755.680432, 'cbBTC': 62293.409251, 'AERO': 0.417081}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 85,774,169 | 1,760.389370 | 59658601 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 25,640,725 | 1,756.672861 | 59658601 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 21,184,949 | 0.028346 | 59658601 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,705,326 | 0.028335 | 59658601 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,747,394 | 79.046314 | 59658601 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,137,067 | 0.000016 | 59658601 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,166,873 | 0.028353 | 59658601 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,584,026 | 2.396697 | 59658601 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,267,974 | 1,757.312537 | 59658601 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,266,263 | 1.000000 | 59658601 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,742,596 | 38,556.698327 | 59658601 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 262 | 2,308,035 | 1,756.749736 | 59658601 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,070,409 | 0.000016 | 59658601 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,716,756 | 0.028335 | 59658601 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,654,387 | 1,147,728.379701 | 59658601 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,093 | 0.844466 | 59658601 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,435,706 | 0.000016 | 59658601 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,323,733 | 0.000000 | 59658601 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,266,763 | 0.006522 | 59658601 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,246,915 | 0.000016 | 59658601 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,113,260 | 14.252206 | 59658601 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,060,084 | 86.468548 | 59658601 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,050,609 | 448.290892 | 59658601 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 1,022,747 | 78.590582 | 59658601 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/USDC | 3000 | 1,022,257 | 1,760.628554 | 59658601 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,013,949 | 15,805.474421 | 59658601 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 990,500 | 4,208.639940 | 59658601 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 987,487 | 1,760.417642 | 59658601 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/doginme | 10000 | 944,451 | 29,211,254.596354 | 59658601 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 923,601 | 0.045037 | 59658601 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 855,204 | 58.498715 | 59658601 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 823,734 | 523,871.575253 | 59658601 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 810,181 | 0.000000 | 59658601 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 794,470 | 22,197,849.965724 | 59658601 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 785,320 | 0.001540 | 59658601 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 739,157 | 1,079.369862 | 59658601 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | WETH/USDC | 500 | 729,380 | 1,756.663017 | 59658601 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | XDP/USDC | 100 | 724,699 | 0.014637 | 59658601 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | QUID/USDC | 100 | 723,465 | 0.046519 | 59658601 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4595 | 702,444 | 25.183375 | 59658601 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 10000 | 696,530 | 1,767.869224 | 59658601 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/wstETH | 3000 | 597,525 | 0.798842 | 59658601 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | WETH/USDC | 100 | 593,468 | 1,757.370648 | 59658601 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v3 | TIG/USDC | 10000 | 591,645 | 0.439834 | 59658601 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 557,067 | 4,750,984.587509 | 59658601 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 542,272 | 4,190.759325 | 59658601 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 3724 | 513,120 | 525,154.985536 | 59658601 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 509,175 | 1.386543 | 59658601 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | FLOCK/USDC | 3000 | 499,205 | 0.031751 | 59658601 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 484,565 | 167,823.490085 | 59658601 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | USDC/USDT | 14 | 460,039 | 1.001708 | 59658601 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 442,082 | 0.000007 | 59658601 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 428,490 | 0.000239 | 59658601 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| pancakeswap_v3 | ELSA/USDC | 100 | 403,464 | 0.056182 | 59658601 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3043 | 402,282 | 1,079.440208 | 59658601 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/UNI | 10000 | 387,233 | 354.882199 | 59658601 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 384,956 | 24.104714 | 59658601 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 384,027 | 839,040.957247 | 59658601 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 371,757 | 0.057468 | 59658601 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| aerodrome_slipstream | WETH/VVV | 2700 | 370,600 | 79.095661 | 59658601 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |

## Recherche d'opportunités
- Cycles : 14138 ; routes examinées : 184698832 ; candidats optimisés : 274782 ; net attendu > 0 : 138 ; dernier cycle 2759.2 ms
- Rejets (moteur) : {'spread_below_threshold': 181046129, 'liquidity_below_min': 2360646, 'negative_expected_net': 274644, 'borrow_bound_too_small': 18278, 'cycle_budget_exhausted': 5260}
- Enregistrements de la session : 151392 ; net attendu > 0 : 138 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 6/6 positives
- Décisions : {'REJECTED': 151392} ; motifs de rejet : {'below_safety_margin': 130, 'negative_expected_net': 151254, 'p_lower_below_threshold': 136, 'reliability_not_demonstrated': 2, 'stale_data': 29}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 59649109 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC→[uniswap_v3]→cbBTC | 0.003597 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0474 €) | 0.000001 cbBTC | 2.31 | 0.276 (n=243) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59649109 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→USDC | 252.867906 USDC | 0.056122 USDC | 0.000000 USDC | 0.005209 USDC | 0.050913 USDC (0.0468 €) | 0.050913 USDC | 2.01 | 0.276 (n=243) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 59649109 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.001060 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0268 €) | — | 4.44 | 0.333 (n=622) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59649109 | USDC→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 76.631505 USDC | 0.034430 USDC | 0.000000 USDC | 0.005457 USDC | 0.028973 USDC (0.0267 €) | 0.028973 USDC | 3.78 | 0.333 (n=622) | REJECTED | p_lower_below_threshold(0.33<0.75) |
| 59591958 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.126331 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0177 €) | — | 0.87 | 0.109 (n=377) | REJECTED | below_safety_margin(10948928198956<25266204118772), p_lower_below_threshold(0.11<0.75) |
| 59591958 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.126331 WETH | 0.000013 WETH | 0.000000 WETH | 0.000002 WETH | 0.000011 WETH (0.0177 €) | — | 0.87 | 0.109 (n=377) | REJECTED | below_safety_margin(10948928198956<25266204118772), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.769810 USDC | 0.023215 USDC | 0.000000 USDC | 0.004050 USDC | 0.019165 USDC (0.0176 €) | — | 0.88 | 0.109 (n=377) | REJECTED | below_safety_margin(19165<43753), p_lower_below_threshold(0.11<0.75) |
| 59591958 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 218.769810 USDC | 0.023215 USDC | 0.000000 USDC | 0.004050 USDC | 0.019165 USDC (0.0176 €) | — | 0.88 | 0.109 (n=377) | REJECTED | below_safety_margin(19165<43753), p_lower_below_threshold(0.11<0.75) |
| 59649109 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.003350 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0148 €) | — | 0.78 | 0.109 (n=377) | REJECTED | below_safety_margin(26<66), p_lower_below_threshold(0.11<0.75) |
| 59649109 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 185.216132 USDC | 0.020171 USDC | 0.000000 USDC | 0.004081 USDC | 0.016090 USDC (0.0148 €) | — | 0.87 | 0.109 (n=377) | REJECTED | below_safety_margin(16090<37043), p_lower_below_threshold(0.11<0.75) |
| 59655128 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001040 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0120 €) | 0.000000 cbBTC | 2.02 | 0.109 (n=377) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 59655128 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 65.018184 USDC | 0.016963 USDC | 0.000000 USDC | 0.004027 USDC | 0.012936 USDC (0.0119 €) | — | 1.99 | 0.109 (n=377) | REJECTED | below_safety_margin(12936<13003), p_lower_below_threshold(0.11<0.75) |
| 59649106 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.053090 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0105 €) | — | 1.22 | 0.272 (n=1639) | REJECTED | below_safety_margin(6473544586717<10617958064661), p_lower_below_threshold(0.27<0.75) |
| 59649107 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.053090 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0105 €) | — | 1.22 | 0.272 (n=1639) | REJECTED | below_safety_margin(6465638151272<10617958064661), p_lower_below_threshold(0.27<0.75) |
| 59649106 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 93.105842 USDC | 0.016779 USDC | 0.000000 USDC | 0.005440 USDC | 0.011339 USDC (0.0104 €) | — | 1.22 | 0.272 (n=1639) | REJECTED | below_safety_margin(11339<18621), p_lower_below_threshold(0.27<0.75) |
| 59649107 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 93.105842 USDC | 0.016779 USDC | 0.000000 USDC | 0.005453 USDC | 0.011326 USDC (0.0104 €) | — | 1.22 | 0.272 (n=1639) | REJECTED | below_safety_margin(11326<18621), p_lower_below_threshold(0.27<0.75) |
| 59649106 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.050599 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0089 €) | — | 1.09 | 0.272 (n=1639) | REJECTED | below_safety_margin(5525297203062<10119844597094), p_lower_below_threshold(0.27<0.75) |
| 59649107 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.050599 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0089 €) | — | 1.09 | 0.272 (n=1639) | REJECTED | below_safety_margin(5517390767617<10119844597094), p_lower_below_threshold(0.27<0.75) |
| 59649106 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 88.347406 USDC | 0.015116 USDC | 0.000000 USDC | 0.005440 USDC | 0.009676 USDC (0.0089 €) | — | 1.10 | 0.272 (n=1639) | REJECTED | below_safety_margin(9676<17669), p_lower_below_threshold(0.27<0.75) |
| 59649107 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 88.347406 USDC | 0.015116 USDC | 0.000000 USDC | 0.005453 USDC | 0.009663 USDC (0.0089 €) | — | 1.09 | 0.272 (n=1639) | REJECTED | below_safety_margin(9663<17669), p_lower_below_threshold(0.27<0.75) |
| 59649108 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.043167 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0074 €) | — | 1.06 | 0.114 (n=32) | REJECTED | below_safety_margin(4594064751386<8633400891748), p_lower_below_threshold(0.11<0.75) |
| 59649109 | WETH→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.043167 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0074 €) | — | 1.06 | 0.114 (n=32) | REJECTED | below_safety_margin(4593258377136<8633400891748), p_lower_below_threshold(0.11<0.75) |
| 59649108 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 74.735321 USDC | 0.011877 USDC | 0.000000 USDC | 0.003831 USDC | 0.008046 USDC (0.0074 €) | — | 1.08 | 0.114 (n=32) | REJECTED | below_safety_margin(8046<14947), p_lower_below_threshold(0.11<0.75) |
| 59649109 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 74.735321 USDC | 0.011877 USDC | 0.000000 USDC | 0.003833 USDC | 0.008044 USDC (0.0074 €) | — | 1.08 | 0.114 (n=32) | REJECTED | below_safety_margin(8044<14947), p_lower_below_threshold(0.11<0.75) |
| 59649108 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000584 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0051 €) | — | 1.54 | 0.272 (n=1639) | REJECTED | below_safety_margin(9<11), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8582 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.222 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
