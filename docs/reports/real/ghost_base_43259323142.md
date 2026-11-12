# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T16:44:15+00:00 ; durée 9.11 min ; blocs 56554640 → 56557365 (441 vus)

## Connexion
- Requêtes RPC : 5781 ; erreurs : 0 ; latence p50/p95 : 273.8/1,486.1 ms
- Rafraîchissements d'état : 441 ; âge des données au dernier bloc : 7.22 s ; changements de frais LP observés (pools à frais dynamiques) : 378
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 852 ; cycles déclenchés par événement : 246 ; avance médiane sur le rafraîchissement multicall : 460 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,004.68 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 454 pools, 266 jetons, 14202 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 96, aerodrome 187, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 160 (rejetés 2) → 565 jetons ; pools candidats 3627 (énumérés 281, par paires 0), mesurés 456, sous le plancher de 10000.0 $ : 2 → gardés 454 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2012.424484, 'cbBTC': 71768.389273, 'AERO': 0.523178}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,415,074 | 2,004.678278 | 56557364 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,260,553 | 0.027971 | 56557364 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,634,872 | 0.000014 | 56557364 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,503,010 | 0.028017 | 56557364 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 6,957,226 | 1,999.583647 | 56557364 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,670,608 | 105.227129 | 56557364 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,183,946 | 0.027970 | 56557364 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,150,131 | 1.920268 | 56557364 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,059,869 | 1,999.496816 | 56557365 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,776,224 | 0.998590 | 56557364 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,973,790 | 42,528.478465 | 56557364 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 247 | 2,801,180 | 1,999.281511 | 56557364 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 2,147,901 | 0.028010 | 56557364 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,873,222 | 1,160,931.772445 | 56557364 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,649,532 | 0.016818 | 56557365 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,605,990 | 0.000014 | 56557364 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,572,902 | 0.000014 | 56557364 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,525,098 | 0.000000 | 56557364 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,494,603 | 0.006656 | 56557364 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,472,648 | 0.000014 | 56557364 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,486 | 0.831291 | 56557364 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,373,542 | 428.790929 | 56557364 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,255,600 | 2,004.972592 | 56557364 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,219,458 | 3,843.833263 | 56557364 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,184,639 | 15,299.364682 | 56557364 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,141,259 | 2,004.893961 | 56557364 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,087,654 | 1,999.780212 | 56557364 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,177 | 86.290648 | 56557364 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,047,058 | 1.389298 | 56557364 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,011,248 | 34,297,458.139575 | 56557364 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 977,157 | 105.928309 | 56557364 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 969,093 | 20.784831 | 56557364 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 913,765 | 566,668.742386 | 56557364 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 890,211 | 0.001486 | 56557364 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 877,851 | 23,229,511.263151 | 56557364 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 876,598 | 0.052513 | 56557364 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 370 | 869,678 | 0.000014 | 56557364 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 867,678 | 2,005.358242 | 56557364 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 865,364 | 1,006.401204 | 56557364 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 829,998 | 0.000000 | 56557364 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 768,542 | 79.633851 | 56557364 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 743,500 | 0.049239 | 56557364 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 738,229 | 23.422694 | 56557364 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 684,047 | 3,870.915778 | 56557364 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 679,187 | 0.801801 | 56557364 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 649,301 | 0.513893 | 56557364 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 628,976 | 4,816,909.901838 | 56557364 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/EDEL | 7000 | 601,891 | 169,107.657008 | 56557364 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | TIG/USDC | 10000 | 592,554 | 0.442934 | 56557364 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 575,946 | 153,577.891344 | 56557364 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 560,142 | 0.000255 | 56557364 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 559,798 | 564,499.437238 | 56557364 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 556,505 | 0.000007 | 56557364 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,465 | 0.037361 | 56557364 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 482,803 | 1,006.601982 | 56557364 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 456,568 | 0.065425 | 56557364 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 450,227 | 1.001070 | 56557364 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 446,179 | 0.502823 | 56557364 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 427,932 | 24.789313 | 56557364 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 422,594 | 333.493261 | 56557364 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 686 ; routes examinées : 9742572 ; candidats optimisés : 46682 ; net attendu > 0 : 49 ; dernier cycle 221.1 ms
- Rejets (moteur) : {'spread_below_threshold': 9541002, 'liquidity_below_min': 154774, 'negative_expected_net': 46633, 'cycle_budget_exhausted': 114}
- Enregistrements de la session : 46682 ; net attendu > 0 : 49 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 46682} ; motifs de rejet : {'below_safety_margin': 49, 'negative_expected_net': 46633, 'p_lower_below_threshold': 33, 'reliability_not_demonstrated': 16, 'stale_data': 13}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56556875 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.055027 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(4989908289805<11005499079417), p_lower_below_threshold(0.27<0.75) |
| 56556875 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.055027 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(4989908289805<11005499079417), stale_data(4616ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56556875 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 109.404960 USDC | 0.016420 USDC | 0.000000 USDC | 0.006455 USDC | 0.009965 USDC (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(9965<21880), p_lower_below_threshold(0.27<0.75) |
| 56556875 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 109.404960 USDC | 0.016420 USDC | 0.000000 USDC | 0.006455 USDC | 0.009965 USDC (0.0092 €) | — | 0.91 | 0.268 (n=1617) | REJECTED | below_safety_margin(9965<21880), stale_data(4623ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56556908 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.077170 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0065 €) | — | 0.45 | 0.097 (n=121) | REJECTED | below_safety_margin(3507660798968<15434025788782), p_lower_below_threshold(0.10<0.75) |
| 56556909 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.077170 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0065 €) | — | 0.45 | 0.097 (n=121) | REJECTED | below_safety_margin(3507660798968<15434025788782), p_lower_below_threshold(0.10<0.75) |
| 56556908 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 153.147022 USDC | 0.011601 USDC | 0.000000 USDC | 0.004598 USDC | 0.007003 USDC (0.0064 €) | — | 0.46 | 0.097 (n=121) | REJECTED | below_safety_margin(7003<30629), p_lower_below_threshold(0.10<0.75) |
| 56556909 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 153.147022 USDC | 0.011601 USDC | 0.000000 USDC | 0.004598 USDC | 0.007003 USDC (0.0064 €) | — | 0.46 | 0.097 (n=121) | REJECTED | below_safety_margin(7003<30629), p_lower_below_threshold(0.10<0.75) |
| 56556669 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.103533 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0047 €) | — | 0.25 | 0.104 (n=370) | REJECTED | below_safety_margin(2570115362304<20706505795890), p_lower_below_threshold(0.10<0.75) |
| 56556670 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.103533 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0047 €) | — | 0.25 | 0.104 (n=370) | REJECTED | below_safety_margin(2570115362304<20706505795890), p_lower_below_threshold(0.10<0.75) |
| 56556669 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 207.398405 USDC | 0.009742 USDC | 0.000000 USDC | 0.004609 USDC | 0.005133 USDC (0.0047 €) | — | 0.25 | 0.104 (n=370) | REJECTED | below_safety_margin(5133<41479), p_lower_below_threshold(0.10<0.75) |
| 56556670 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 207.398405 USDC | 0.009742 USDC | 0.000000 USDC | 0.004609 USDC | 0.005133 USDC (0.0047 €) | — | 0.25 | 0.104 (n=370) | REJECTED | below_safety_margin(5133<41479), p_lower_below_threshold(0.10<0.75) |
| 56556908 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.042666 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.54 | 0.349 (n=627) | REJECTED | below_safety_margin(2310781975939<8533250863495), p_lower_below_threshold(0.35<0.75) |
| 56556909 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.042666 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0043 €) | — | 0.54 | 0.349 (n=627) | REJECTED | below_safety_margin(2310781975939<8533250863495), p_lower_below_threshold(0.35<0.75) |
| 56556908 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 84.176265 USDC | 0.010747 USDC | 0.000000 USDC | 0.006143 USDC | 0.004604 USDC (0.0042 €) | — | 0.55 | 0.349 (n=627) | REJECTED | below_safety_margin(4604<16835), p_lower_below_threshold(0.35<0.75) |
| 56556909 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 84.176265 USDC | 0.010747 USDC | 0.000000 USDC | 0.006143 USDC | 0.004604 USDC (0.0042 €) | — | 0.55 | 0.349 (n=627) | REJECTED | below_safety_margin(4604<16835), p_lower_below_threshold(0.35<0.75) |
| 56555438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001695 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0033 €) | — | 0.29 | 0.268 (n=1617) | REJECTED | below_safety_margin(5<33), p_lower_below_threshold(0.27<0.75) |
| 56555438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001695 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0033 €) | — | 0.29 | 0.268 (n=1617) | REJECTED | below_safety_margin(5<33), p_lower_below_threshold(0.27<0.75) |
| 56555438 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.052888 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0029 €) | — | 0.30 | 0.268 (n=1617) | REJECTED | below_safety_margin(1573120128124<10577649162355), p_lower_below_threshold(0.27<0.75) |
| 56555438 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.052888 WETH | 0.000005 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0029 €) | — | 0.30 | 0.268 (n=1617) | REJECTED | below_safety_margin(1573120128124<10577649162355), p_lower_below_threshold(0.27<0.75) |
| 56555438 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 121.694191 USDC | 0.009251 USDC | 0.000000 USDC | 0.006165 USDC | 0.003086 USDC (0.0028 €) | — | 0.25 | 0.268 (n=1617) | REJECTED | below_safety_margin(3086<24338), p_lower_below_threshold(0.27<0.75) |
| 56555438 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 121.694191 USDC | 0.009251 USDC | 0.000000 USDC | 0.006165 USDC | 0.003086 USDC (0.0028 €) | — | 0.25 | 0.268 (n=1617) | REJECTED | below_safety_margin(3086<24338), p_lower_below_threshold(0.27<0.75) |
| 56555351 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.029980 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0019 €) | — | 0.34 | — (n=0) | REJECTED | below_safety_margin(1009039948270<5995965538256), stale_data(4350ms>4000.0), reliability_not_demonstrated |
| 56555352 | WETH→[uniswap_v2]→USDC→[pancakeswap_v3]→WETH | 0.029980 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0019 €) | — | 0.34 | — (n=0) | REJECTED | below_safety_margin(1009039948270<5995965538256), stale_data(5564ms>4000.0), reliability_not_demonstrated |
| 56555351 | USDC→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 60.497904 USDC | 0.006006 USDC | 0.000000 USDC | 0.003993 USDC | 0.002013 USDC (0.0019 €) | — | 0.33 | — (n=0) | REJECTED | below_safety_margin(2013<12099), stale_data(4355ms>4000.0), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 8415 ; taux observé 0.222 ; borne inférieure crédible (0.9) 0.216 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
