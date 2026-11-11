# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T01:28:17+00:00 ; durée 12.22 min ; blocs 55846916 → 55850570 (835 vus)

## Connexion
- Requêtes RPC : 9800 ; erreurs : 0 ; latence p50/p95 : 147.7/1,133.6 ms
- Rafraîchissements d'état : 835 ; âge des données au dernier bloc : 7.43 s ; changements de frais LP observés (pools à frais dynamiques) : 246
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 510 ; cycles déclenchés par événement : 224 ; avance médiane sur le rafraîchissement multicall : 444 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,047.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 459 pools, 268 jetons, 15492 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 189, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 162 (rejetés 2) → 567 jetons ; pools candidats 3634 (énumérés 283, par paires 0), mesurés 461, sous le plancher de 10000.0 $ : 2 → gardés 459 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2047.571772, 'cbBTC': 73300.62757, 'AERO': 0.541198}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,503,320 | 2,047.571767 | 55850592 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,317,248 | 0.027862 | 55850592 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,529,830 | 0.027851 | 55850592 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,317,786 | 0.000014 | 55850592 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,048,117 | 2,047.017662 | 55850592 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,795,868 | 105.775238 | 55850592 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,322,499 | 0.027871 | 55850592 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,261,960 | 1.848788 | 55850592 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,184,160 | 2,047.800860 | 55850592 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,868,328 | 0.998998 | 55850592 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,050,208 | 42,172.685722 | 55850592 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,917,183 | 2,047.727244 | 55850592 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,272,579 | 0.027839 | 55850592 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,946,293 | 1,121,909.747723 | 55850592 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,678,181 | 0.000014 | 55850592 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,623,007 | 0.016405 | 55850592 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,615,555 | 0.000014 | 55850592 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,556,212 | 0.000000 | 55850592 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,522,206 | 0.006643 | 55850592 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,952 | 0.824067 | 55850592 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,454,876 | 1.378306 | 55850592 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,422,634 | 0.000014 | 55850592 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,416,641 | 414.381444 | 55850592 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,756 | 2,047.459560 | 55850592 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,259,460 | 3,783.644550 | 55850592 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,230,651 | 14,863.966801 | 55850592 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,155,312 | 2,048.554834 | 55850592 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,864 | 85.855202 | 55850592 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,051,205 | 2,047.019384 | 55850592 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,040,721 | 33,463,519.137143 | 55850592 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 957,573 | 21.556166 | 55850592 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 941,353 | 106.226713 | 55850592 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 939,270 | 556,999.600230 | 55850592 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 911,106 | 0.001481 | 55850592 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 909,166 | 0.000014 | 55850592 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 905,604 | 22,848,882.859993 | 55850592 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 880,878 | 0.051695 | 55850592 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 880,205 | 1,015.232609 | 55850592 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 877,239 | 2,042.470303 | 55850592 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 867,726 | 0.000000 | 55850592 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 766,411 | 80.077248 | 55850592 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 764,585 | 22.298778 | 55850592 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,974 | 0.051656 | 55850592 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 748,133 | 114,199.781138 | 55850592 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 705,412 | 3,770.863155 | 55850592 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 693,228 | 0.802938 | 55850592 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 654,040 | 0.531598 | 55850592 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 646,280 | 4,753,267.123086 | 55850592 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,669 | 0.495924 | 55850592 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 593,282 | 150,879.610518 | 55850592 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 584,910 | 0.000007 | 55850592 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 578,082 | 0.000259 | 55850592 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 576,759 | 554,536.328043 | 55850592 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,655 | 0.037397 | 55850592 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 492,667 | 1,015.909356 | 55850592 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 463,236 | 0.495049 | 55850592 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 460,755 | 0.066225 | 55850592 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,066 | 1.001050 | 55850592 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 440,543 | 306.226790 | 55850592 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 439,457 | 24.791464 | 55850592 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 1058 ; routes examinées : 16390536 ; candidats optimisés : 77576 ; net attendu > 0 : 32 ; dernier cycle 380.1 ms
- Rejets (moteur) : {'spread_below_threshold': 16096861, 'liquidity_below_min': 213296, 'negative_expected_net': 77544, 'borrow_bound_too_small': 1631, 'cycle_budget_exhausted': 1172}
- Enregistrements de la session : 77576 ; net attendu > 0 : 32 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 77576} ; motifs de rejet : {'below_safety_margin': 32, 'negative_expected_net': 77544, 'p_lower_below_threshold': 32}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55849115 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.084633 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0100 €) | — | 0.62 | 0.098 (n=356) | REJECTED | below_safety_margin(5283971602795<16926646224768), p_lower_below_threshold(0.10<0.75) |
| 55849116 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.084633 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0100 €) | — | 0.62 | 0.098 (n=356) | REJECTED | below_safety_margin(5283971602795<16926646224768), p_lower_below_threshold(0.10<0.75) |
| 55849115 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 171.925948 USDC | 0.015402 USDC | 0.000000 USDC | 0.004598 USDC | 0.010804 USDC (0.0099 €) | — | 0.63 | 0.098 (n=356) | REJECTED | below_safety_margin(10804<34385), p_lower_below_threshold(0.10<0.75) |
| 55849116 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 171.925948 USDC | 0.015402 USDC | 0.000000 USDC | 0.004598 USDC | 0.010804 USDC (0.0099 €) | — | 0.63 | 0.098 (n=356) | REJECTED | below_safety_margin(10804<34385), p_lower_below_threshold(0.10<0.75) |
| 55850267 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.057102 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0030 €) | — | 0.28 | 0.098 (n=356) | REJECTED | below_safety_margin(1605942880214<11420449190096), p_lower_below_threshold(0.10<0.75) |
| 55850268 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.057102 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0030 €) | — | 0.28 | 0.098 (n=356) | REJECTED | below_safety_margin(1604548792714<11420449190096), p_lower_below_threshold(0.10<0.75) |
| 55850267 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 116.179716 USDC | 0.007882 USDC | 0.000000 USDC | 0.004597 USDC | 0.003285 USDC (0.0030 €) | — | 0.28 | 0.098 (n=356) | REJECTED | below_safety_margin(3285<23235), p_lower_below_threshold(0.10<0.75) |
| 55850268 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 116.179716 USDC | 0.007882 USDC | 0.000000 USDC | 0.004600 USDC | 0.003282 USDC (0.0030 €) | — | 0.28 | 0.098 (n=356) | REJECTED | below_safety_margin(3282<23235), p_lower_below_threshold(0.10<0.75) |
| 55850267 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 152.539590 USDC | 0.009273 USDC | 0.000000 USDC | 0.006153 USDC | 0.003120 USDC (0.0029 €) | — | 0.20 | 0.256 (n=1534) | REJECTED | below_safety_margin(3120<30507), p_lower_below_threshold(0.26<0.75) |
| 55850268 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 152.539590 USDC | 0.009273 USDC | 0.000000 USDC | 0.006157 USDC | 0.003116 USDC (0.0029 €) | — | 0.20 | 0.256 (n=1534) | REJECTED | below_safety_margin(3116<30507), p_lower_below_threshold(0.26<0.75) |
| 55850267 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.070287 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 0.21 | 0.256 (n=1534) | REJECTED | below_safety_margin(1494332406204<14057382433504), p_lower_below_threshold(0.26<0.75) |
| 55850268 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.070287 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0028 €) | — | 0.21 | 0.256 (n=1534) | REJECTED | below_safety_margin(1492466477434<14057382433504), p_lower_below_threshold(0.26<0.75) |
| 55850267 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001548 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0027 €) | — | 0.26 | 0.256 (n=1534) | REJECTED | below_safety_margin(4<30), p_lower_below_threshold(0.26<0.75) |
| 55850268 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001548 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0027 €) | — | 0.26 | 0.256 (n=1534) | REJECTED | below_safety_margin(4<30), p_lower_below_threshold(0.26<0.75) |
| 55846943 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 35.867483 USDC | 0.006034 USDC | 0.000000 USDC | 0.004597 USDC | 0.001437 USDC (0.0013 €) | — | 0.40 | 0.098 (n=356) | REJECTED | below_safety_margin(1437<7173), p_lower_below_threshold(0.10<0.75) |
| 55846945 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 35.867483 USDC | 0.006034 USDC | 0.000000 USDC | 0.004597 USDC | 0.001437 USDC (0.0013 €) | — | 0.40 | 0.098 (n=356) | REJECTED | below_safety_margin(1437<7173), p_lower_below_threshold(0.10<0.75) |
| 55846944 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 35.867483 USDC | 0.006034 USDC | 0.000000 USDC | 0.004597 USDC | 0.001437 USDC (0.0013 €) | — | 0.40 | 0.098 (n=356) | REJECTED | below_safety_margin(1437<7173), p_lower_below_threshold(0.10<0.75) |
| 55846945 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 35.867483 USDC | 0.006034 USDC | 0.000000 USDC | 0.004597 USDC | 0.001437 USDC (0.0013 €) | — | 0.40 | 0.098 (n=356) | REJECTED | below_safety_margin(1437<7173), p_lower_below_threshold(0.10<0.75) |
| 55846946 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 35.867483 USDC | 0.006034 USDC | 0.000000 USDC | 0.004598 USDC | 0.001436 USDC (0.0013 €) | — | 0.40 | 0.098 (n=356) | REJECTED | below_safety_margin(1436<7173), p_lower_below_threshold(0.10<0.75) |
| 55849683 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 20.334032 USDC | 0.007040 USDC | 0.000000 USDC | 0.006153 USDC | 0.000887 USDC (0.0008 €) | — | 0.44 | 0.256 (n=1534) | REJECTED | below_safety_margin(887<4066), p_lower_below_threshold(0.26<0.75) |
| 55849684 | USDC→[uniswap_v3]→AERO→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 20.334032 USDC | 0.007040 USDC | 0.000000 USDC | 0.006153 USDC | 0.000887 USDC (0.0008 €) | — | 0.44 | 0.256 (n=1534) | REJECTED | below_safety_margin(887<4066), p_lower_below_threshold(0.26<0.75) |
| 55846943 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000505 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.20 | 0.098 (n=356) | REJECTED | below_safety_margin(1<10), p_lower_below_threshold(0.10<0.75) |
| 55846945 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000505 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.20 | 0.098 (n=356) | REJECTED | below_safety_margin(1<10), p_lower_below_threshold(0.10<0.75) |
| 55846944 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000505 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.20 | 0.098 (n=356) | REJECTED | below_safety_margin(1<10), p_lower_below_threshold(0.10<0.75) |
| 55846945 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000505 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.20 | 0.098 (n=356) | REJECTED | below_safety_margin(1<10), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 7932 ; taux observé 0.209 ; borne inférieure crédible (0.9) 0.203 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
