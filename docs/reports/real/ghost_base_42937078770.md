# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T01:34:22+00:00 ; durée 18.32 min ; blocs 55846916 → 55852397 (1264 vus)

## Connexion
- Requêtes RPC : 14674 ; erreurs : 30 ; latence p50/p95 : 121.1/1,162.8 ms
- Rafraîchissements d'état : 1264 ; âge des données au dernier bloc : 6.82 s ; changements de frais LP observés (pools à frais dynamiques) : 569
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 510 ; cycles déclenchés par événement : 224 ; avance médiane sur le rafraîchissement multicall : 444 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,051.52 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 459 pools, 268 jetons, 15492 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 189, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 162 (rejetés 2) → 567 jetons ; pools candidats 3634 (énumérés 283, par paires 0), mesurés 461, sous le plancher de 10000.0 $ : 2 → gardés 459 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2047.571772, 'cbBTC': 73300.62757, 'AERO': 0.541198}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,680,154 | 2,051.516336 | 55852419 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,346,202 | 0.027874 | 55852419 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,545,440 | 0.027851 | 55852419 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,328,327 | 0.000014 | 55852419 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,059,518 | 2,054.001907 | 55852419 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,822,088 | 105.368522 | 55852419 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,330,510 | 0.027877 | 55852419 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,261,960 | 1.848788 | 55852419 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,190,475 | 2,053.180224 | 55852419 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,874,128 | 0.998998 | 55852419 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,056,084 | 42,172.685722 | 55852419 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,922,082 | 2,053.422774 | 55852419 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,276,819 | 0.027839 | 55852419 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,950,042 | 1,121,909.747723 | 55852419 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,680,147 | 0.000014 | 55852419 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,620,724 | 0.016370 | 55852419 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,617,365 | 0.000014 | 55852419 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,560,755 | 0.000000 | 55852419 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,525,138 | 0.006643 | 55852419 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,952 | 0.824067 | 55852419 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,454,876 | 1.378306 | 55852419 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,424,045 | 0.000014 | 55852419 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,419,691 | 414.042271 | 55852419 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,269,979 | 2,051.013875 | 55852419 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,260,361 | 3,789.305264 | 55852419 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,233,154 | 14,863.966801 | 55852419 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,424 | 2,051.508017 | 55852419 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,864 | 85.855202 | 55852419 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,052,824 | 2,054.077325 | 55852419 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,042,726 | 33,463,519.137143 | 55852419 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 958,173 | 21.514594 | 55852419 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 945,611 | 106.103524 | 55852419 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 941,083 | 556,993.316528 | 55852419 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 913,045 | 0.001483 | 55852419 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 910,462 | 0.000014 | 55852419 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 908,657 | 22,793,699.651296 | 55852419 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 885,162 | 0.051228 | 55852419 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 881,662 | 1,015.829071 | 55852419 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 878,016 | 2,042.470303 | 55852419 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 869,374 | 0.000000 | 55852419 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 766,967 | 79.961100 | 55852419 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4565 | 766,536 | 22.219766 | 55852419 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,337 | 0.051566 | 55852419 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 749,442 | 114,239.922698 | 55852419 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 706,093 | 3,770.863155 | 55852419 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 694,564 | 0.802938 | 55852419 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 655,120 | 0.533081 | 55852419 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 649,718 | 4,721,359.397724 | 55852419 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,466 | 0.495615 | 55852419 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 594,287 | 150,949.513751 | 55852419 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 585,188 | 0.000007 | 55852419 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 579,196 | 0.000259 | 55852419 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 577,873 | 554,570.865593 | 55852419 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 557,059 | 0.037439 | 55852419 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 493,474 | 1,016.444199 | 55852419 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 463,678 | 0.495049 | 55852419 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 459,319 | 0.065918 | 55852419 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 455,066 | 1.001002 | 55852419 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 441,392 | 306.226790 | 55852419 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 440,303 | 24.791464 | 55852419 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 1487 ; routes examinées : 23036604 ; candidats optimisés : 116378 ; net attendu > 0 : 158 ; dernier cycle 368.8 ms
- Rejets (moteur) : {'spread_below_threshold': 22570588, 'liquidity_below_min': 345234, 'negative_expected_net': 116220, 'cycle_budget_exhausted': 2327, 'borrow_bound_too_small': 2077}
- Enregistrements de la session : 116378 ; net attendu > 0 : 158 ; simulés (eth_call de la vraie tx) : 8 (ok 5, échec 3) ; étiquettes ghost N+1 : 2/5 positives
- Décisions : {'REJECTED': 116378} ; motifs de rejet : {'below_safety_margin': 150, 'negative_expected_net': 116220, 'p_lower_below_threshold': 144, 'reliability_not_demonstrated': 14, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55850988 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 41.765208 USDC | 0.020370 USDC | 0.000000 USDC | 0.004638 USDC | 0.015732 USDC (0.0145 €) | 0.015732 USDC | 3.77 | 0.073 (n=489) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 55849115 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.084633 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0100 €) | — | 0.62 | 0.098 (n=356) | REJECTED | below_safety_margin(5283971602795<16926646224768), p_lower_below_threshold(0.10<0.75) |
| 55849116 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.084633 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0100 €) | — | 0.62 | 0.098 (n=356) | REJECTED | below_safety_margin(5283971602795<16926646224768), p_lower_below_threshold(0.10<0.75) |
| 55849115 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 171.925948 USDC | 0.015402 USDC | 0.000000 USDC | 0.004598 USDC | 0.010804 USDC (0.0099 €) | — | 0.63 | 0.098 (n=356) | REJECTED | below_safety_margin(10804<34385), p_lower_below_threshold(0.10<0.75) |
| 55849116 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 171.925948 USDC | 0.015402 USDC | 0.000000 USDC | 0.004598 USDC | 0.010804 USDC (0.0099 €) | — | 0.63 | 0.098 (n=356) | REJECTED | below_safety_margin(10804<34385), p_lower_below_threshold(0.10<0.75) |
| 55850769 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 48.613350 USDC | 0.016211 USDC | 0.000000 USDC | 0.006160 USDC | 0.010051 USDC (0.0092 €) | 0.010051 USDC | 2.07 | 0.257 (n=1536) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55850768 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 48.613350 USDC | 0.016211 USDC | 0.000000 USDC | 0.006162 USDC | 0.010049 USDC (0.0092 €) | 0.010049 USDC | 2.07 | 0.256 (n=1534) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55850769 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.023729 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0092 €) | 0.000005 WETH | 2.06 | 0.257 (n=1536) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55850768 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.023729 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0092 €) | 0.000005 WETH | 2.06 | 0.256 (n=1534) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55850769 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 94.690239 USDC | 0.015969 USDC | 0.000000 USDC | 0.006160 USDC | 0.009809 USDC (0.0090 €) | — | 1.04 | 0.113 (n=39) | REJECTED | below_safety_margin(9809<18938), p_lower_below_threshold(0.11<0.75) |
| 55850768 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 94.690239 USDC | 0.015969 USDC | 0.000000 USDC | 0.006162 USDC | 0.009807 USDC (0.0090 €) | — | 1.04 | 0.113 (n=39) | REJECTED | below_safety_margin(9807<18938), p_lower_below_threshold(0.11<0.75) |
| 55850769 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.042542 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0089 €) | — | 1.11 | 0.113 (n=39) | REJECTED | below_safety_margin(4716602033152<8508325434437), p_lower_below_threshold(0.11<0.75) |
| 55850768 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.042542 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0089 €) | — | 1.11 | 0.113 (n=39) | REJECTED | below_safety_margin(4715798633258<8508325434437), p_lower_below_threshold(0.11<0.75) |
| 55850768 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001147 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0088 €) | — | 1.13 | 0.113 (n=39) | REJECTED | below_safety_margin(13<22), p_lower_below_threshold(0.11<0.75) |
| 55850769 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001147 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0088 €) | — | 1.13 | 0.113 (n=39) | REJECTED | below_safety_margin(13<22), p_lower_below_threshold(0.11<0.75) |
| 55850958 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 62.231924 USDC | 0.015615 USDC | 0.000000 USDC | 0.006207 USDC | 0.009408 USDC (0.0087 €) | — | 1.51 | 0.257 (n=1536) | REJECTED | below_safety_margin(9408<12446), p_lower_below_threshold(0.26<0.75) |
| 55850958 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.030407 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0086 €) | — | 1.50 | 0.257 (n=1536) | REJECTED | below_safety_margin(4573525299713<6081481583809), p_lower_below_threshold(0.26<0.75) |
| 55852034 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 56.075798 USDC | 0.015489 USDC | 0.000000 USDC | 0.006166 USDC | 0.009323 USDC (0.0086 €) | — | 1.66 | 0.256 (n=1537) | REJECTED | below_safety_margin(9323<11215), p_lower_below_threshold(0.26<0.75) |
| 55850959 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 62.187057 USDC | 0.015395 USDC | 0.000000 USDC | 0.006204 USDC | 0.009191 USDC (0.0085 €) | — | 1.48 | 0.257 (n=1536) | REJECTED | below_safety_margin(9191<12437), p_lower_below_threshold(0.26<0.75) |
| 55850959 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.030180 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0084 €) | — | 1.48 | 0.257 (n=1536) | REJECTED | below_safety_margin(4466751770712<6036043063028), p_lower_below_threshold(0.26<0.75) |
| 55852034 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000614 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0081 €) | — | 1.96 | 0.256 (n=1537) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.26<0.75) |
| 55850959 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 54.061306 USDC | 0.012766 USDC | 0.000000 USDC | 0.006518 USDC | 0.006248 USDC (0.0057 €) | — | 1.16 | 0.257 (n=1536) | REJECTED | below_safety_margin(6248<10812), p_lower_below_threshold(0.26<0.75) |
| 55850958 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 54.061306 USDC | 0.012766 USDC | 0.000000 USDC | 0.006520 USDC | 0.006246 USDC (0.0057 €) | — | 1.16 | 0.257 (n=1536) | REJECTED | below_safety_margin(6246<10812), p_lower_below_threshold(0.26<0.75) |
| 55850959 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.026265 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 1.16 | 0.257 (n=1536) | REJECTED | below_safety_margin(3033861119949<5253086678637), p_lower_below_threshold(0.26<0.75) |
| 55850958 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.026265 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 1.15 | 0.257 (n=1536) | REJECTED | below_safety_margin(3032676004699<5253086678637), p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 7937 ; taux observé 0.209 ; borne inférieure crédible (0.9) 0.203 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
