# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T03:51:58+00:00 ; durée 155.91 min ; blocs 55846916 → 55893642 (11449 vus)

## Connexion
- Requêtes RPC : 125051 ; erreurs : 40 ; latence p50/p95 : 123.4/1,113.4 ms
- Rafraîchissements d'état : 11449 ; âge des données au dernier bloc : 5.92 s ; changements de frais LP observés (pools à frais dynamiques) : 5263
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
| uniswap_v3 | WETH/USDC | 3000 | 134,269,419 | 2,060.705503 | 55893664 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,396,691 | 0.027973 | 55893664 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,580,151 | 0.027925 | 55893664 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,337,014 | 0.000014 | 55893664 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,082,891 | 2,060.582023 | 55893664 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,823,368 | 106.274693 | 55893664 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,350,829 | 0.027968 | 55893664 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,273,518 | 1.838801 | 55893664 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,205,296 | 2,061.370415 | 55893664 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,877,716 | 0.998998 | 55893664 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,070,874 | 42,142.453314 | 55893664 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,933,603 | 2,061.244723 | 55893664 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,216,001 | 0.027938 | 55893664 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,959,300 | 1,121,311.176185 | 55893664 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,681,439 | 0.000014 | 55893664 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,618,488 | 0.000014 | 55893664 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,611,981 | 0.016239 | 55893664 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,560,789 | 0.000000 | 55893664 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,530,131 | 0.006622 | 55893664 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,354 | 0.824067 | 55893664 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,020 | 1.373161 | 55893664 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,428,035 | 411.981689 | 55893664 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,424,984 | 0.000014 | 55893664 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,272,834 | 2,060.503753 | 55893664 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,266,811 | 3,792.061347 | 55893664 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,238,834 | 14,746.206323 | 55893664 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,158,789 | 2,065.841870 | 55893664 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,702 | 85.881444 | 55893664 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,054,355 | 2,060.471250 | 55893664 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,052,351 | 32,972,486.590054 | 55893664 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,874 | 21.397524 | 55893664 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 949,421 | 106.914260 | 55893664 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 946,453 | 555,029.280829 | 55893664 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 913,412 | 0.001481 | 55893664 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 912,370 | 22,806,816.387051 | 55893664 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 911,219 | 0.000014 | 55893664 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 882,364 | 0.051584 | 55893664 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 881,058 | 1,026.328218 | 55893664 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 879,544 | 2,046.596008 | 55893664 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 872,405 | 0.000000 | 55893664 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 769,009 | 79.537121 | 55893664 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 764,993 | 0.052222 | 55893664 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 762,938 | 22.367067 | 55893664 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 751,469 | 114,644.804522 | 55893664 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 709,591 | 3,772.891608 | 55893664 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 697,675 | 0.802938 | 55893664 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 662,625 | 0.535281 | 55893664 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 656,169 | 4,670,715.248134 | 55893664 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,064 | 0.495004 | 55893664 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 591,806 | 153,557.814059 | 55893664 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 587,550 | 0.000007 | 55893664 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 581,790 | 0.000259 | 55893664 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 581,578 | 554,621.197363 | 55893664 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 561,245 | 0.037869 | 55893664 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 493,017 | 1,026.658762 | 55893664 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 467,264 | 0.067416 | 55893664 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 461,769 | 0.496352 | 55893664 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,048 | 1.000998 | 55893664 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | cbBTC/EDGE | 7000 | 444,229 | 880,272.840590 | 55893664 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 443,638 | 305.890640 | 55893664 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 11667 ; routes examinées : 180745164 ; candidats optimisés : 882612 ; net attendu > 0 : 1848 ; dernier cycle 192.7 ms
- Rejets (moteur) : {'spread_below_threshold': 176768246, 'liquidity_below_min': 3059196, 'negative_expected_net': 880764, 'borrow_bound_too_small': 20315, 'cycle_budget_exhausted': 14795}
- Enregistrements de la session : 882612 ; net attendu > 0 : 1848 ; simulés (eth_call de la vraie tx) : 54 (ok 48, échec 6) ; étiquettes ghost N+1 : 22/46 positives
- Décisions : {'REJECTED': 882612} ; motifs de rejet : {'below_safety_margin': 1681, 'negative_expected_net': 880764, 'p_lower_below_threshold': 1811, 'reliability_not_demonstrated': 37, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 6, 'stale_data': 22}

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
