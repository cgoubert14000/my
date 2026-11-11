# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T04:01:25+00:00 ; durée 165.36 min ; blocs 55846916 → 55896442 (12125 vus)

## Connexion
- Requêtes RPC : 132406 ; erreurs : 40 ; latence p50/p95 : 144.8/1,123.7 ms
- Rafraîchissements d'état : 12125 ; âge des données au dernier bloc : 13.87 s ; changements de frais LP observés (pools à frais dynamiques) : 5369
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 510 ; cycles déclenchés par événement : 224 ; avance médiane sur le rafraîchissement multicall : 444 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,060.71 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 459 pools, 268 jetons, 15492 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 189, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 162 (rejetés 2) → 567 jetons ; pools candidats 3634 (énumérés 283, par paires 0), mesurés 461, sous le plancher de 10000.0 $ : 2 → gardés 459 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2047.571772, 'cbBTC': 73300.62757, 'AERO': 0.541198}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,276,355 | 2,060.705465 | 55896497 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,397,682 | 0.027969 | 55896497 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,580,395 | 0.027925 | 55896497 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,337,658 | 0.000014 | 55896497 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,082,914 | 2,060.584240 | 55896497 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,810,454 | 106.678117 | 55896497 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,350,935 | 0.027964 | 55896497 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,273,518 | 1.838801 | 55896497 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,205,355 | 2,061.158100 | 55896497 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,878,173 | 0.998998 | 55896497 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,070,874 | 42,142.453314 | 55896497 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,933,605 | 2,060.920490 | 55896497 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,216,039 | 0.027938 | 55896497 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,959,300 | 1,121,311.176185 | 55896497 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,681,593 | 0.000014 | 55896497 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,618,630 | 0.000014 | 55896497 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,612,528 | 0.016249 | 55896497 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,560,789 | 0.000000 | 55896497 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,530,864 | 0.006626 | 55896497 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,354 | 0.824067 | 55896497 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,020 | 1.373161 | 55896497 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,428,035 | 411.981689 | 55896497 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,425,093 | 0.000014 | 55896497 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,834 | 2,060.503748 | 55896497 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,267,127 | 3,791.482508 | 55896497 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,238,918 | 14,746.206323 | 55896497 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,789 | 2,066.321650 | 55896497 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,702 | 85.881444 | 55896497 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,054,356 | 2,060.718880 | 55896497 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,049,420 | 32,972,486.590054 | 55896497 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,832 | 21.400410 | 55896497 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 946,948 | 106.914266 | 55896497 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 946,036 | 555,024.015990 | 55896497 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 913,130 | 0.001480 | 55896497 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 912,370 | 22,806,816.387051 | 55896497 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 911,322 | 0.000014 | 55896497 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 881,023 | 1,026.407506 | 55896497 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | USDC/VVV | 3000 | 879,590 | 0.051793 | 55896497 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 879,543 | 2,046.596008 | 55896497 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 872,405 | 0.000000 | 55896497 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 769,009 | 79.537121 | 55896497 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 764,685 | 0.052178 | 55896497 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 762,938 | 22.367067 | 55896497 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 751,263 | 114,707.624046 | 55896497 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 709,591 | 3,772.891608 | 55896497 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 697,675 | 0.802938 | 55896497 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 662,625 | 0.535281 | 55896497 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 656,568 | 4,665,036.456026 | 55896497 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,066 | 0.495005 | 55896497 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 591,753 | 153,585.689225 | 55896497 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,915 | 0.000007 | 55896497 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,790 | 0.000259 | 55896497 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 581,582 | 554,706.289350 | 55896497 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 561,245 | 0.037869 | 55896497 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 492,446 | 1,026.714415 | 55896497 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 467,181 | 0.067400 | 55896497 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 461,743 | 0.496352 | 55896497 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,048 | 1.000955 | 55896497 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | cbBTC/EDGE | 7000 | 448,885 | 869,950.479549 | 55896497 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 442,700 | 305.890640 | 55896497 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 12348 ; routes examinées : 191295216 ; candidats optimisés : 918462 ; net attendu > 0 : 1848 ; dernier cycle 242.6 ms
- Rejets (moteur) : {'spread_below_threshold': 187110028, 'liquidity_below_min': 3229915, 'negative_expected_net': 916614, 'borrow_bound_too_small': 21671, 'cycle_budget_exhausted': 15140}
- Enregistrements de la session : 918462 ; net attendu > 0 : 1848 ; simulés (eth_call de la vraie tx) : 54 (ok 48, échec 6) ; étiquettes ghost N+1 : 22/46 positives
- Décisions : {'REJECTED': 918462} ; motifs de rejet : {'below_safety_margin': 1681, 'negative_expected_net': 916614, 'p_lower_below_threshold': 1811, 'reliability_not_demonstrated': 37, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 6, 'stale_data': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55884922 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,111.905987 USDC | 0.349839 USDC | 0.000000 USDC | 0.006505 USDC | 0.343334 USDC (0.3159 €) | — | 3.09 | 0.200 (n=1176) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55884922 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→cbBTC | 0.015037 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3156 €) | — | 3.10 | 0.200 (n=1176) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55884922 | WETH→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.536019 WETH | 0.000170 WETH | 0.000000 WETH | 0.000003 WETH | 0.000166 WETH (0.3156 €) | 0.000166 WETH | 3.11 | 0.200 (n=1176) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55884922 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,105.270988 USDC | 0.331899 USDC | 0.000000 USDC | 0.006505 USDC | 0.325394 USDC (0.2994 €) | — | 2.94 | 0.257 (n=1541) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55884922 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.014051 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000004 cbBTC (0.2993 €) | — | 3.15 | 0.200 (n=1176) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55884922 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.506414 WETH | 0.000161 WETH | 0.000000 WETH | 0.000003 WETH | 0.000158 WETH (0.2992 €) | 0.000158 WETH | 3.12 | 0.200 (n=1176) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55884922 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 985.698549 USDC | 0.232023 USDC | 0.000000 USDC | 0.004627 USDC | 0.227396 USDC (0.2092 €) | — | 2.31 | 0.082 (n=112) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55884922 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.478323 WETH | 0.000112 WETH | 0.000000 WETH | 0.000002 WETH | 0.000110 WETH (0.2090 €) | 0.000110 WETH | 2.30 | 0.082 (n=112) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55884922 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 809.852488 USDC | 0.171678 USDC | 0.000000 USDC | 0.004940 USDC | 0.166738 USDC (0.1534 €) | — | 2.06 | 0.098 (n=356) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55884922 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.392662 WETH | 0.000083 WETH | 0.000000 WETH | 0.000002 WETH | 0.000081 WETH (0.1533 €) | — | 2.06 | 0.098 (n=356) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55884922 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 480.499297 USDC | 0.130855 USDC | 0.000000 USDC | 0.004627 USDC | 0.126228 USDC (0.1161 €) | — | 2.63 | 0.082 (n=112) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55884922 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.232954 WETH | 0.000063 WETH | 0.000000 WETH | 0.000002 WETH | 0.000061 WETH (0.1160 €) | — | 2.63 | 0.082 (n=112) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55884922 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.005473 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1145 €) | — | 3.09 | 0.200 (n=1176) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55884922 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 576.036365 USDC | 0.129017 USDC | 0.000000 USDC | 0.004627 USDC | 0.124390 USDC (0.1144 €) | — | 2.16 | 0.098 (n=356) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55884922 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 418.188923 USDC | 0.130894 USDC | 0.000000 USDC | 0.006505 USDC | 0.124389 USDC (0.1144 €) | — | 2.97 | 0.257 (n=1541) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55884922 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.279789 WETH | 0.000063 WETH | 0.000000 WETH | 0.000002 WETH | 0.000060 WETH (0.1143 €) | — | 2.16 | 0.098 (n=356) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 55884922 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.192764 WETH | 0.000063 WETH | 0.000000 WETH | 0.000003 WETH | 0.000060 WETH (0.1139 €) | — | 3.12 | 0.200 (n=1176) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55854227 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 412.007847 USDC | 0.098781 USDC | 0.000000 USDC | 0.006174 USDC | 0.092607 USDC (0.0852 €) | — | 2.25 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.198394 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0848 €) | 0.000045 WETH | 2.26 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005463 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0847 €) | — | 2.29 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004451 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0664 €) | — | 2.20 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.161267 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0663 €) | 0.000035 WETH | 2.18 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 328.352486 USDC | 0.078084 USDC | 0.000000 USDC | 0.006174 USDC | 0.071910 USDC (0.0662 €) | — | 2.19 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 330.106605 USDC | 0.067840 USDC | 0.000000 USDC | 0.006174 USDC | 0.061666 USDC (0.0567 €) | — | 1.87 | 0.256 (n=1538) | REJECTED | below_safety_margin(61666<66021), p_lower_below_threshold(0.26<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.151824 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0567 €) | — | 1.98 | 0.256 (n=1538) | REJECTED | below_safety_margin(29997961983564<30364700178971), p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 7978 ; taux observé 0.210 ; borne inférieure crédible (0.9) 0.205 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
