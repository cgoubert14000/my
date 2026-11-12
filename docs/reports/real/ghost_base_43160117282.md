# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T09:20:45+00:00 ; durée 239.44 min ; blocs 56352481 → 56424277 (10606 vus)

## Connexion
- Requêtes RPC : 145350 ; erreurs : 40 ; latence p50/p95 : 424.7/1,560.6 ms
- Rafraîchissements d'état : 10606 ; âge des données au dernier bloc : 7.23 s ; changements de frais LP observés (pools à frais dynamiques) : 5013
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1475 ; cycles déclenchés par événement : 699 ; avance médiane sur le rafraîchissement multicall : 504 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,044.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 457 pools, 265 jetons, 15538 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 459, sous le plancher de 10000.0 $ : 2 → gardés 457 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2045.219297, 'cbBTC': 73500.635487, 'AERO': 0.536237}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,561,158 | 2,044.776462 | 56424304 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,380,256 | 0.027852 | 56424304 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,674,609 | 0.027806 | 56424304 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,455,865 | 0.000014 | 56424304 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,068,378 | 2,040.569327 | 56424304 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,832,989 | 104.336817 | 56424304 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,249,755 | 0.027856 | 56424304 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,185,616 | 2,039.772680 | 56424304 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 4,183,013 | 1.900372 | 56424304 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,867,645 | 0.998656 | 56424304 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,035,364 | 42,469.894307 | 56424304 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 169 | 2,861,774 | 2,039.509636 | 56424304 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,193,828 | 0.027823 | 56424304 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,938,765 | 1,127,553.662132 | 56424304 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,645,795 | 0.016750 | 56424304 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,641,979 | 0.000014 | 56424304 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,587,449 | 0.000014 | 56424304 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,558,580 | 0.000000 | 56424304 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,525,627 | 0.000014 | 56424304 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,504,938 | 0.006554 | 56424304 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,872 | 0.830193 | 56424304 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,399,344 | 430.901800 | 56424304 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,268,041 | 2,044.941756 | 56424304 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,234,816 | 3,880.085733 | 56424304 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,208,532 | 15,467.147541 | 56424304 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,153,504 | 2,045.926419 | 56424304 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,127,343 | 2,040.451891 | 56424304 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,555 | 86.229165 | 56424304 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,046,779 | 1.389936 | 56424304 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,035,049 | 33,802,831.521373 | 56424304 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,014,668 | 104.382781 | 56424304 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 961,805 | 21.266871 | 56424304 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 934,096 | 563,082.873336 | 56424304 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 909,294 | 0.001478 | 56424304 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 898,605 | 0.000014 | 56424304 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 897,196 | 0.051102 | 56424304 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 893,773 | 23,297,416.943306 | 56424304 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 876,393 | 2,054.853960 | 56424304 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 873,798 | 1,027.293193 | 56424304 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 850,749 | 0.000000 | 56424304 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 778,882 | 77.533375 | 56424304 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 745,671 | 23.095214 | 56424304 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 743,915 | 0.049296 | 56424304 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 739,072 | 116,698.172294 | 56424304 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 694,751 | 3,849.659936 | 56424304 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 692,773 | 0.801801 | 56424304 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 664,119 | 0.521796 | 56424304 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 641,429 | 4,818,518.009561 | 56424304 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 615,845 | 0.477345 | 56424304 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 582,465 | 156,231.903212 | 56424304 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 573,169 | 0.000257 | 56424304 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 572,820 | 561,533.966215 | 56424304 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 564,631 | 0.000007 | 56424304 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 558,517 | 0.037567 | 56424304 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 486,486 | 1,027.423003 | 56424304 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 461,398 | 0.066310 | 56424304 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 453,542 | 1.001038 | 56424304 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 445,512 | 0.501968 | 56424304 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 438,521 | 24.820221 | 56424304 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 432,584 | 332.166763 | 56424304 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 11304 ; routes examinées : 175641552 ; candidats optimisés : 843351 ; net attendu > 0 : 100 ; dernier cycle 535.1 ms
- Rejets (moteur) : {'spread_below_threshold': 172629663, 'liquidity_below_min': 2156246, 'negative_expected_net': 843251, 'borrow_bound_too_small': 11292, 'cycle_budget_exhausted': 1000}
- Enregistrements de la session : 843351 ; net attendu > 0 : 100 ; simulés (eth_call de la vraie tx) : 8 (ok 8, échec 0) ; étiquettes ghost N+1 : 4/7 positives
- Décisions : {'REJECTED': 843351} ; motifs de rejet : {'below_safety_margin': 75, 'negative_expected_net': 843251, 'p_lower_below_threshold': 100, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 3, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 35.218273 USDC | 0.032458 USDC | 0.000000 USDC | 0.006143 USDC | 0.026315 USDC (0.0242 €) | — | 7.47 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017342 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0242 €) | 0.000013 WETH | 7.41 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 35.404259 USDC | 0.032255 USDC | 0.000000 USDC | 0.006143 USDC | 0.026112 USDC (0.0240 €) | — | 7.38 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017304 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0240 €) | 0.000013 WETH | 7.37 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 34.633173 USDC | 0.031152 USDC | 0.000000 USDC | 0.006143 USDC | 0.025009 USDC (0.0230 €) | — | 7.22 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.017066 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0230 €) | 0.000012 WETH | 7.16 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56423611 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 284.828522 USDC | 0.026950 USDC | 0.000000 USDC | 0.006147 USDC | 0.020803 USDC (0.0191 €) | — | 0.73 | 0.268 (n=1587) | REJECTED | below_safety_margin(20803<56965), p_lower_below_threshold(0.27<0.75) |
| 56423611 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.143286 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0191 €) | — | 0.71 | 0.268 (n=1587) | REJECTED | below_safety_margin(10147226635661<28657215835462), p_lower_below_threshold(0.27<0.75) |
| 56423611 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.003089 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0189 €) | — | 0.91 | 0.268 (n=1587) | REJECTED | below_safety_margin(28<61), p_lower_below_threshold(0.27<0.75) |
| 56388390 | WETH→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.013924 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0160 €) | — | 6.09 | 0.077 (n=120) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 56380462 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004048 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 0.42 | 0.102 (n=366) | REJECTED | below_safety_margin(17<80), p_lower_below_threshold(0.10<0.75) |
| 56380462 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 349.650476 USDC | 0.017156 USDC | 0.000000 USDC | 0.004913 USDC | 0.012243 USDC (0.0113 €) | — | 0.35 | 0.102 (n=366) | REJECTED | below_safety_margin(12243<69930), p_lower_below_threshold(0.10<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 26.577874 USDC | 0.018129 USDC | 0.000000 USDC | 0.006143 USDC | 0.011986 USDC (0.0110 €) | — | 4.51 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.012985 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0110 €) | — | 4.51 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 25.295059 USDC | 0.016679 USDC | 0.000000 USDC | 0.006143 USDC | 0.010536 USDC (0.0097 €) | — | 4.17 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56388390 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.012479 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0097 €) | — | 4.13 | 0.203 (n=1238) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56421406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.005566 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0073 €) | 0.000001 WETH | 7.01 | 0.203 (n=1239) | REJECTED | sim_below_estimate(3767706711565<6905694966251), p_lower_below_threshold(0.20<0.75) |
| 56421406 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 11.275295 USDC | 0.014100 USDC | 0.000000 USDC | 0.006147 USDC | 0.007953 USDC (0.0073 €) | — | 7.05 | 0.203 (n=1239) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56421406 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.005306 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0063 €) | 0.000000 WETH | 6.29 | 0.307 (n=569) | REJECTED | sim_below_estimate(3354715840022<6346431563904), p_lower_below_threshold(0.31<0.75) |
| 56421406 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 10.825725 USDC | 0.012960 USDC | 0.000000 USDC | 0.006147 USDC | 0.006813 USDC (0.0063 €) | — | 6.29 | 0.307 (n=569) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56423611 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.060799 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0056 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(2951889622845<12159726330500), p_lower_below_threshold(0.09<0.75) |
| 56423611 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 123.342356 USDC | 0.010926 USDC | 0.000000 USDC | 0.004903 USDC | 0.006023 USDC (0.0055 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(6023<24668), p_lower_below_threshold(0.09<0.75) |
| 56388390 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 18.973789 USDC | 0.012147 USDC | 0.000000 USDC | 0.006143 USDC | 0.006004 USDC (0.0055 €) | — | 3.16 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56388390 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→WETH | 0.009378 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0055 €) | — | 3.13 | 0.308 (n=567) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56358036 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 127.764441 USDC | 0.010716 USDC | 0.000000 USDC | 0.004903 USDC | 0.005813 USDC (0.0053 €) | — | 0.45 | 0.087 (n=116) | REJECTED | below_safety_margin(5813<25552), p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 8247 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.212 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
