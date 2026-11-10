# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T19:52:27+00:00 ; durée 12.16 min ; blocs 55746173 → 55749847 (257 vus)

## Connexion
- Requêtes RPC : 5978 ; erreurs : 0 ; latence p50/p95 : 595.0/1,531.8 ms
- Rafraîchissements d'état : 257 ; âge des données au dernier bloc : 10.08 s ; changements de frais LP observés (pools à frais dynamiques) : 299
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2476 ; cycles déclenchés par événement : 722 ; avance médiane sur le rafraîchissement multicall : 648 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,041.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 269 jetons, 15520 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 98, aerodrome 190, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 163 (rejetés 2) → 568 jetons ; pools candidats 3640 (énumérés 285, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2041.615001, 'cbBTC': 73281.760168, 'AERO': 0.54062}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,125,367 | 2,041.615001 | 55749842 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,266,948 | 0.027824 | 55749842 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,523,580 | 0.027774 | 55749842 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,290,742 | 0.000014 | 55749842 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,075,036 | 2,044.536046 | 55749842 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,750,418 | 106.801911 | 55749842 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,302,578 | 1.842095 | 55749842 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,295,020 | 0.027829 | 55749855 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,859,880 | 0.999947 | 55749842 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,854,133 | 2,045.254014 | 55749856 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,000,502 | 43,328.623020 | 55749842 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,914,454 | 2,044.905389 | 55749842 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,250,826 | 0.027787 | 55749842 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,940,733 | 1,121,791.087457 | 55749842 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,673,611 | 0.000014 | 55749842 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 1,617,603 | 0.000014 | 55749842 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,609,861 | 0.016208 | 55749842 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,542,604 | 0.000000 | 55749842 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,524,209 | 0.006677 | 55749842 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,342 | 0.823606 | 55749842 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,434,937 | 1.411479 | 55749842 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,408,665 | 418.389903 | 55749842 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,408,582 | 0.000014 | 55749842 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,266,896 | 2,042.852520 | 55749842 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,260,912 | 3,767.604181 | 55749842 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,222,862 | 15,034.481941 | 55749842 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,154,019 | 2,044.590538 | 55749842 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,064,190 | 85.802599 | 55749842 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,048,734 | 2,044.545324 | 55749842 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,024,202 | 34,812,490.424314 | 55749842 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,585 | 21.765431 | 55749842 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 937,375 | 555,555.439774 | 55749847 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 912,873 | 0.000014 | 55749842 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/VVV | 10000 | 909,965 | 106.527490 | 55749842 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 908,728 | 0.001478 | 55749842 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 904,250 | 22,857,397.181832 | 55749842 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 881,268 | 1,004.230901 | 55749842 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 876,712 | 2,026.985532 | 55749842 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 871,584 | 0.052273 | 55749842 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | DRB/WETH | 10000 | 863,595 | 0.000000 | 55749842 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 771,430 | 79.038569 | 55749842 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 761,241 | 22.434834 | 55749842 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 759,149 | 0.051401 | 55749842 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 746,964 | 113,891.804651 | 55749842 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 711,787 | 3,770.863155 | 55749842 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 691,148 | 0.803085 | 55749842 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 645,366 | 0.525728 | 55749842 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 643,129 | 4,771,277.171488 | 55749842 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,137 | 0.495205 | 55749842 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 586,439 | 0.000007 | 55749842 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 576,531 | 0.000259 | 55749842 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2150 | 575,845 | 557,801.515479 | 55749842 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 569,486 | 162,758.481862 | 55749842 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,157 | 0.037143 | 55749842 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 495,747 | 1,004.514167 | 55749842 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 479,943 | 6,635.980210 | 55749842 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 474,168 | 0.068708 | 55749842 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 465,899 | 0.495575 | 55749842 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,022 | 1.001119 | 55749842 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 442,585 | 303.301208 | 55749842 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 978 ; routes examinées : 15178560 ; candidats optimisés : 98420 ; net attendu > 0 : 265 ; dernier cycle 107.5 ms
- Rejets (moteur) : {'spread_below_threshold': 14825957, 'liquidity_below_min': 252174, 'negative_expected_net': 98155, 'borrow_bound_too_small': 1956, 'cycle_budget_exhausted': 53}
- Enregistrements de la session : 98420 ; net attendu > 0 : 265 ; simulés (eth_call de la vraie tx) : 2 (ok 0, échec 2) ; étiquettes ghost N+1 : 2/2 positives
- Décisions : {'REJECTED': 98420} ; motifs de rejet : {'below_safety_margin': 263, 'negative_expected_net': 98155, 'p_lower_below_threshold': 261, 'reliability_not_demonstrated': 4, 'simulation_failed': 2, 'stale_data': 214}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55749600 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 245.095506 USDC | 0.031340 USDC | 0.000000 USDC | 0.004597 USDC | 0.026743 USDC (0.0246 €) | — | 1.09 | 0.097 (n=348) | REJECTED | below_safety_margin(26743<49019), p_lower_below_threshold(0.10<0.75) |
| 55749600 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.120591 WETH | 0.000015 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0246 €) | — | 1.08 | 0.097 (n=348) | REJECTED | below_safety_margin(13083696454985<24118199747370), p_lower_below_threshold(0.10<0.75) |
| 55749600 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 380.540893 USDC | 0.030412 USDC | 0.000000 USDC | 0.006151 USDC | 0.024261 USDC (0.0223 €) | — | 0.64 | 0.113 (n=39) | REJECTED | below_safety_margin(24261<76108), p_lower_below_threshold(0.11<0.75) |
| 55749600 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.186519 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0223 €) | — | 0.64 | 0.113 (n=39) | REJECTED | below_safety_margin(11879522297834<37303812909711), p_lower_below_threshold(0.11<0.75) |
| 55749600 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004466 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0223 €) | — | 0.74 | 0.113 (n=39) | REJECTED | below_safety_margin(33<89), p_lower_below_threshold(0.11<0.75) |
| 55748150 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.034449 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0121 €) | — | 1.87 | 0.113 (n=39) | REJECTED | below_safety_margin(6425030108626<6889877337089), stale_data(6291ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 55748150 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 93.890557 USDC | 0.019247 USDC | 0.000000 USDC | 0.006458 USDC | 0.012789 USDC (0.0118 €) | — | 1.36 | 0.113 (n=39) | REJECTED | below_safety_margin(12789<18778), stale_data(6301ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 55749084 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.043019 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0115 €) | — | 1.43 | 0.253 (n=1516) | REJECTED | below_safety_margin(6147318696569<8603707908227), stale_data(4849ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55748150 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000964 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 1.76 | 0.113 (n=39) | REJECTED | below_safety_margin(17<19), stale_data(6296ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 55749084 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001068 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 1.59 | 0.253 (n=1516) | REJECTED | below_safety_margin(17<21), stale_data(4844ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55748150 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.030777 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0114 €) | — | 1.97 | 0.252 (n=1514) | REJECTED | below_safety_margin(6054528582385<6155480630018), stale_data(6157ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55749084 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 92.287361 USDC | 0.018818 USDC | 0.000000 USDC | 0.006459 USDC | 0.012359 USDC (0.0114 €) | — | 1.34 | 0.253 (n=1516) | REJECTED | below_safety_margin(12359<18457), stale_data(4840ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55748150 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 70.414833 USDC | 0.018220 USDC | 0.000000 USDC | 0.006148 USDC | 0.012072 USDC (0.0111 €) | — | 1.71 | 0.252 (n=1514) | REJECTED | below_safety_margin(12072<14082), stale_data(6162ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55748150 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000923 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0108 €) | — | 1.73 | 0.252 (n=1514) | REJECTED | below_safety_margin(16<18), stale_data(6166ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55748163 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 175.284434 USDC | 0.016109 USDC | 0.000000 USDC | 0.004904 USDC | 0.011205 USDC (0.0103 €) | — | 0.64 | 0.097 (n=348) | REJECTED | below_safety_margin(11205<35056), p_lower_below_threshold(0.10<0.75) |
| 55748163 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.086059 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0103 €) | — | 0.64 | 0.097 (n=348) | REJECTED | below_safety_margin(5486552462375<17211809654264), p_lower_below_threshold(0.10<0.75) |
| 55749084 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000974 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0101 €) | — | 1.54 | 0.253 (n=1516) | REJECTED | below_safety_margin(15<19), stale_data(4815ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55749084 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.039487 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0100 €) | — | 1.34 | 0.253 (n=1516) | REJECTED | below_safety_margin(5301005832124<7897479841578), stale_data(4819ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55749600 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.111045 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0099 €) | — | 0.48 | 0.253 (n=1516) | REJECTED | below_safety_margin(5283025606884<22209034669331), p_lower_below_threshold(0.25<0.75) |
| 55749084 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 76.081755 USDC | 0.017096 USDC | 0.000000 USDC | 0.006459 USDC | 0.010637 USDC (0.0098 €) | — | 1.40 | 0.253 (n=1516) | REJECTED | below_safety_margin(10637<15216), stale_data(4810ms>4000.0), p_lower_below_threshold(0.25<0.75) |
| 55748150 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 88.026116 USDC | 0.016770 USDC | 0.000000 USDC | 0.006458 USDC | 0.010312 USDC (0.0095 €) | — | 1.17 | 0.113 (n=39) | REJECTED | below_safety_margin(10312<17605), stale_data(6450ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 55748150 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000964 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0095 €) | — | 1.45 | 0.113 (n=39) | REJECTED | below_safety_margin(14<19), stale_data(6455ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 55749600 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002800 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0095 €) | — | 0.50 | 0.253 (n=1516) | REJECTED | below_safety_margin(14<55), p_lower_below_threshold(0.25<0.75) |
| 55748150 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.042523 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0094 €) | — | 1.17 | 0.113 (n=39) | REJECTED | below_safety_margin(4990355003942<8504554256258), stale_data(6445ms>4000.0), p_lower_below_threshold(0.11<0.75) |
| 55749600 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 200.108086 USDC | 0.016192 USDC | 0.000000 USDC | 0.006151 USDC | 0.010041 USDC (0.0092 €) | — | 0.50 | 0.253 (n=1516) | REJECTED | below_safety_margin(10041<40021), p_lower_below_threshold(0.25<0.75) |

## Fiabilité et décision
- Observations ghost : 7858 ; taux observé 0.208 ; borne inférieure crédible (0.9) 0.202 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
