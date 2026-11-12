# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T21:43:58+00:00 ; durée 308.82 min ; blocs 56554640 → 56647207 (15686 vus)

## Connexion
- Requêtes RPC : 194442 ; erreurs : 420 ; latence p50/p95 : 157.9/1,450.6 ms
- Rafraîchissements d'état : 15686 ; âge des données au dernier bloc : 8.98 s ; changements de frais LP observés (pools à frais dynamiques) : 9175
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 13290 ; cycles déclenchés par événement : 4276 ; avance médiane sur le rafraîchissement multicall : 490 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,015.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 454 pools, 266 jetons, 14202 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 96, aerodrome 187, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 160 (rejetés 2) → 565 jetons ; pools candidats 3627 (énumérés 281, par paires 0), mesurés 456, sous le plancher de 10000.0 $ : 2 → gardés 454 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2012.424484, 'cbBTC': 71768.389273, 'AERO': 0.523178}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,727,024 | 2,015.232601 | 56647234 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,350,086 | 0.028233 | 56647234 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,528,501 | 0.028170 | 56647234 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,137,024 | 0.000014 | 56647234 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,864,343 | 2,019.356168 | 56647234 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,693,070 | 105.625516 | 56647234 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,212,184 | 0.028227 | 56647234 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,154,753 | 1.899538 | 56647234 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,087,449 | 2,018.669563 | 56647234 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,759,485 | 0.998727 | 56647234 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,984,499 | 42,668.962438 | 56647234 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 100 | 2,805,782 | 2,018.813354 | 56647234 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,155,218 | 0.028182 | 56647234 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,881,407 | 1,163,003.281972 | 56647234 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,646,032 | 0.016760 | 56647234 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,599,267 | 0.000014 | 56647234 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,566,935 | 0.000014 | 56647234 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,506,225 | 0.000000 | 56647234 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,481,692 | 0.006532 | 56647234 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,468,270 | 0.000014 | 56647234 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,149 | 0.831283 | 56647234 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,383,696 | 425.727860 | 56647234 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,258,912 | 2,016.076723 | 56647234 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,230,360 | 3,834.997301 | 56647234 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,188,499 | 15,099.286330 | 56647234 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,144,120 | 2,022.388082 | 56647234 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,099,826 | 2,019.360192 | 56647234 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,906 | 86.334668 | 56647234 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,047,056 | 1.389303 | 56647234 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,005,655 | 35,384,516.220924 | 56647234 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 989,225 | 106.184703 | 56647234 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 980,736 | 20.056598 | 56647234 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 922,258 | 560,097.000938 | 56647234 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 888,474 | 0.001493 | 56647234 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 883,359 | 23,226,178.240886 | 56647234 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 877,644 | 0.052294 | 56647234 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 872,019 | 1,001.866652 | 56647234 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 869,595 | 2,005.198605 | 56647234 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 866,429 | 0.000014 | 56647234 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | DRB/WETH | 10000 | 815,103 | 0.000000 | 56647234 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 771,243 | 79.076963 | 56647234 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 746,468 | 23.067316 | 56647234 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 746,190 | 0.049604 | 56647234 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 689,420 | 3,863.882062 | 56647234 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 682,763 | 0.801801 | 56647234 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | WETH/EDEL | 7000 | 672,156 | 137,015.192258 | 56647234 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 663,482 | 0.526341 | 56647234 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 625,470 | 4,922,842.725891 | 56647234 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 602,896 | 0.457818 | 56647234 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 582,250 | 151,879.341559 | 56647234 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 567,636 | 0.000260 | 56647234 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2105 | 566,208 | 555,931.364858 | 56647234 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,175 | 0.037949 | 56647234 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 558,593 | 0.000007 | 56647234 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 485,883 | 1,001.506243 | 56647234 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 461,446 | 0.066308 | 56647234 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 449,565 | 1.000953 | 56647234 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 449,375 | 0.499790 | 56647234 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/UNI | 10000 | 435,657 | 333.133889 | 56647234 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| uniswap_v3 | WETH/uSOL | 3000 | 429,764 | 24.862308 | 56647234 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |

## Recherche d'opportunités
- Cycles : 19961 ; routes examinées : 283486122 ; candidats optimisés : 1387182 ; net attendu > 0 : 1182 ; dernier cycle 467.3 ms
- Rejets (moteur) : {'spread_below_threshold': 277409040, 'liquidity_below_min': 4680948, 'negative_expected_net': 1386000, 'cycle_budget_exhausted': 5296, 'borrow_bound_too_small': 2697, 'unquotable': 959}
- Enregistrements de la session : 1387182 ; net attendu > 0 : 1182 ; simulés (eth_call de la vraie tx) : 63 (ok 46, échec 17) ; étiquettes ghost N+1 : 19/51 positives
- Décisions : {'REJECTED': 1387182} ; motifs de rejet : {'below_safety_margin': 998, 'negative_expected_net': 1386000, 'p_lower_below_threshold': 1135, 'reliability_not_demonstrated': 47, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 17, 'stale_data': 215}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56641724 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 167.397696 USDC | 0.339931 USDC | 0.000000 USDC | 0.004529 USDC | 0.335402 USDC (0.3086 €) | — | 20.04 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 56564036 | WETH→[aerodrome]→NPC→[uniswap_v2]→WETH | 0.011966 WETH | 0.000080 WETH | 0.000000 WETH | 0.000002 WETH | 0.000079 WETH (0.1449 €) | 0.000079 WETH | 65.72 | 0.006 (n=1) | REJECTED | reliability_not_demonstrated |
| 56641725 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 89.595783 USDC | 0.097086 USDC | 0.000000 USDC | 0.004529 USDC | 0.092557 USDC (0.0852 €) | — | 10.33 | 0.007 (n=117) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 56598010 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.934169 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0475 €) | — | 0.27 | 0.104 (n=371) | REJECTED | below_safety_margin(25652669957624<186833754396777), p_lower_below_threshold(0.10<0.75) |
| 56598011 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.934169 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0475 €) | — | 0.27 | 0.104 (n=371) | REJECTED | below_safety_margin(25652669957624<186833754396777), stale_data(4336ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56598010 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.023133 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0475 €) | — | 0.31 | 0.104 (n=371) | REJECTED | below_safety_margin(72<462), p_lower_below_threshold(0.10<0.75) |
| 56598011 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.023133 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0475 €) | — | 0.31 | 0.104 (n=371) | REJECTED | below_safety_margin(72<462), stale_data(4342ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56628325 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 447.549612 USDC | 0.055992 USDC | 0.000000 USDC | 0.004527 USDC | 0.051465 USDC (0.0473 €) | — | 1.15 | 0.106 (n=372) | REJECTED | below_safety_margin(51465<89509), p_lower_below_threshold(0.11<0.75) |
| 56628326 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 447.549612 USDC | 0.055992 USDC | 0.000000 USDC | 0.004527 USDC | 0.051465 USDC (0.0473 €) | — | 1.15 | 0.106 (n=372) | REJECTED | below_safety_margin(51465<89509), p_lower_below_threshold(0.11<0.75) |
| 56628325 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.222346 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0473 €) | — | 1.15 | 0.106 (n=372) | REJECTED | below_safety_margin(25533400638721<44469187302115), p_lower_below_threshold(0.11<0.75) |
| 56628326 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.222346 WETH | 0.000028 WETH | 0.000000 WETH | 0.000002 WETH | 0.000026 WETH (0.0473 €) | — | 1.15 | 0.106 (n=372) | REJECTED | below_safety_margin(25533400638721<44469187302115), p_lower_below_threshold(0.11<0.75) |
| 56598985 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC | 307.406334 USDC | 0.056015 USDC | 0.000000 USDC | 0.006064 USDC | 0.049951 USDC (0.0460 €) | — | 1.62 | 0.269 (n=1619) | REJECTED | below_safety_margin(49951<61481), stale_data(4133ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56625071 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008176 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0459 €) | — | 0.86 | 0.270 (n=1622) | REJECTED | below_safety_margin(70<163), p_lower_below_threshold(0.27<0.75) |
| 56625072 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008176 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0459 €) | — | 0.86 | 0.270 (n=1622) | REJECTED | below_safety_margin(70<163), p_lower_below_threshold(0.27<0.75) |
| 56625071 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 602.340280 USDC | 0.055849 USDC | 0.000000 USDC | 0.006059 USDC | 0.049790 USDC (0.0458 €) | — | 0.83 | 0.270 (n=1622) | REJECTED | below_safety_margin(49790<120468), p_lower_below_threshold(0.27<0.75) |
| 56625072 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 602.340280 USDC | 0.055849 USDC | 0.000000 USDC | 0.006059 USDC | 0.049790 USDC (0.0458 €) | — | 0.83 | 0.270 (n=1622) | REJECTED | below_safety_margin(49790<120468), p_lower_below_threshold(0.27<0.75) |
| 56625071 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.308386 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0455 €) | — | 0.80 | 0.270 (n=1622) | REJECTED | below_safety_margin(24575434488948<61677135214282), p_lower_below_threshold(0.27<0.75) |
| 56625072 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.308386 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0455 €) | — | 0.80 | 0.270 (n=1622) | REJECTED | below_safety_margin(24575434488948<61677135214282), p_lower_below_threshold(0.27<0.75) |
| 56598985 | cbBTC→[uniswap_v3]→WBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003777 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0455 €) | — | 1.83 | 0.269 (n=1619) | REJECTED | below_safety_margin(69<75), stale_data(4139ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56598986 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006612 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0369 €) | — | 0.85 | 0.104 (n=371) | REJECTED | below_safety_margin(56<132), p_lower_below_threshold(0.10<0.75) |
| 56620659 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.022714 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0368 €) | — | 0.25 | 0.106 (n=372) | REJECTED | below_safety_margin(56<454), p_lower_below_threshold(0.11<0.75) |
| 56620659 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.781863 WETH | 0.000022 WETH | 0.000000 WETH | 0.000002 WETH | 0.000020 WETH (0.0368 €) | — | 0.25 | 0.106 (n=372) | REJECTED | below_safety_margin(19854008577885<156372517458642), p_lower_below_threshold(0.11<0.75) |
| 56598986 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 464.648392 USDC | 0.044332 USDC | 0.000000 USDC | 0.004531 USDC | 0.039801 USDC (0.0366 €) | — | 0.86 | 0.104 (n=371) | REJECTED | below_safety_margin(39801<92929), p_lower_below_threshold(0.10<0.75) |
| 56625071 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006903 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0354 €) | — | 0.78 | 0.270 (n=1622) | REJECTED | below_safety_margin(54<138), p_lower_below_threshold(0.27<0.75) |
| 56625072 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006903 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0354 €) | — | 0.78 | 0.270 (n=1622) | REJECTED | below_safety_margin(54<138), p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 8466 ; taux observé 0.223 ; borne inférieure crédible (0.9) 0.217 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
