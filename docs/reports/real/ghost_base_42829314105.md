# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T19:25:02+00:00 ; durée 322.31 min ; blocs 55644907 → 55741526 (15606 vus)

## Connexion
- Requêtes RPC : 212642 ; erreurs : 745 ; latence p50/p95 : 244.2/1,295.5 ms
- Rafraîchissements d'état : 15606 ; âge des données au dernier bloc : 9.76 s ; changements de frais LP observés (pools à frais dynamiques) : 17211
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5086 ; cycles déclenchés par événement : 932 ; avance médiane sur le rafraîchissement multicall : 569 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,041.62 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 133,101,625 | 2,041.615035 | 55741555 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,275,793 | 0.027814 | 55741555 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,525,247 | 0.027774 | 55741555 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,290,886 | 0.000014 | 55741555 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,992,483 | 2,039.860876 | 55741555 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,749,377 | 106.834981 | 55741555 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,297,011 | 1.846877 | 55741555 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,296,350 | 0.027819 | 55741555 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,861,265 | 0.999947 | 55741555 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,854,069 | 2,040.448089 | 55741555 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,006,197 | 43,164.614189 | 55741555 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,916,362 | 2,040.437734 | 55741555 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,250,937 | 0.027787 | 55741555 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,941,773 | 1,120,589.867132 | 55741555 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,673,910 | 0.000014 | 55741555 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,617,214 | 0.000014 | 55741555 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,614,263 | 0.016273 | 55741555 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,542,566 | 0.000000 | 55741555 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,524,550 | 0.006679 | 55741555 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,342 | 0.823606 | 55741555 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,434,937 | 1.411479 | 55741555 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,409,313 | 417.701192 | 55741555 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,408,930 | 0.000014 | 55741555 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,266,893 | 2,041.402942 | 55741555 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,258,852 | 3,767.869257 | 55741555 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,223,983 | 15,007.975791 | 55741555 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,154,019 | 2,045.129255 | 55741555 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,064,190 | 85.802599 | 55741555 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,047,998 | 2,039.693477 | 55741555 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,024,202 | 34,812,490.424314 | 55741555 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,532 | 21.769191 | 55741555 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 937,375 | 555,556.133742 | 55741555 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 913,182 | 0.000014 | 55741555 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/VVV | 10000 | 909,778 | 106.527471 | 55741555 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 908,717 | 0.001476 | 55741555 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 904,250 | 22,857,397.181832 | 55741555 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 880,953 | 1,005.051038 | 55741555 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 874,672 | 2,026.985532 | 55741555 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 871,694 | 0.052332 | 55741555 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | DRB/WETH | 10000 | 864,137 | 0.000000 | 55741555 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 774,806 | 78.351377 | 55741555 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 761,696 | 22.416081 | 55741555 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 758,843 | 0.051358 | 55741555 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 746,743 | 113,959.402278 | 55741555 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 710,864 | 3,770.863155 | 55741555 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 691,148 | 0.803085 | 55741555 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 650,431 | 0.526500 | 55741555 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 643,861 | 4,760,416.280389 | 55741555 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 626,797 | 0.494700 | 55741555 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 585,467 | 0.000007 | 55741555 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 576,531 | 0.000259 | 55741555 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2141 | 575,845 | 559,454.462429 | 55741555 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 567,968 | 163,628.125607 | 55741555 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,681 | 0.037402 | 55741555 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 495,557 | 1,004.740176 | 55741555 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 480,442 | 6,622.205229 | 55741555 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 473,955 | 0.068669 | 55741555 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 465,625 | 0.495901 | 55741555 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,012 | 1.001155 | 55741555 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 443,206 | 302.920735 | 55741555 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 16537 ; routes examinées : 270578394 ; candidats optimisés : 1461274 ; net attendu > 0 : 7115 ; dernier cycle 530.4 ms
- Rejets (moteur) : {'spread_below_threshold': 264681994, 'liquidity_below_min': 4351021, 'negative_expected_net': 1454159, 'pool_quarantined': 40664, 'borrow_bound_too_small': 31566, 'cycle_budget_exhausted': 11875}
- Enregistrements de la session : 1461274 ; net attendu > 0 : 7115 ; simulés (eth_call de la vraie tx) : 395 (ok 300, échec 95) ; étiquettes ghost N+1 : 185/348 positives
- Décisions : {'REJECTED': 1461274} ; motifs de rejet : {'below_safety_margin': 5733, 'negative_expected_net': 1454159, 'p_lower_below_threshold': 6900, 'price_impact': 7, 'reliability_not_demonstrated': 215, 'sim_below_estimate': 43, 'simulated_net_nonpositive': 26, 'simulation_failed': 95, 'stale_data': 804}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55689884 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.012577 cbBTC | 0.000013 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000013 cbBTC (0.8596 €) | — | 10.15 | 0.123 (n=62) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55689884 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 948.622129 USDC | 0.939139 USDC | 0.000000 USDC | 0.005944 USDC | 0.933195 USDC (0.8585 €) | 0.933195 USDC | 9.84 | 0.123 (n=62) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 55670011 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066963 WETH | 0.000440 WETH | 0.000000 WETH | 0.000003 WETH | 0.000438 WETH (0.8349 €) | — | 65.34 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 138.463970 USDC | 0.912685 USDC | 0.000000 USDC | 0.006029 USDC | 0.906656 USDC (0.8341 €) | — | 65.48 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066851 WETH | 0.000438 WETH | 0.000000 WETH | 0.000003 WETH | 0.000435 WETH (0.8303 €) | — | 65.10 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 138.459955 USDC | 0.907719 USDC | 0.000000 USDC | 0.006029 USDC | 0.901690 USDC (0.8296 €) | — | 65.12 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.066134 WETH | 0.000434 WETH | 0.000000 WETH | 0.000003 WETH | 0.000432 WETH (0.8233 €) | — | 65.25 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 136.946975 USDC | 0.899995 USDC | 0.000000 USDC | 0.006029 USDC | 0.893966 USDC (0.8224 €) | — | 65.28 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.064805 WETH | 0.000411 WETH | 0.000000 WETH | 0.000003 WETH | 0.000408 WETH (0.7789 €) | — | 62.99 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 134.087851 USDC | 0.851510 USDC | 0.000000 USDC | 0.006029 USDC | 0.845481 USDC (0.7778 €) | — | 63.05 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.064117 WETH | 0.000405 WETH | 0.000000 WETH | 0.000003 WETH | 0.000402 WETH (0.7671 €) | — | 62.71 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 132.821327 USDC | 0.838622 USDC | 0.000000 USDC | 0.006029 USDC | 0.832593 USDC (0.7660 €) | — | 62.69 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→AUKI→[pancakeswap_v3]→WETH | 0.071959 WETH | 0.000375 WETH | 0.000000 WETH | 0.000002 WETH | 0.000373 WETH (0.7119 €) | — | 51.85 | 0.002 (n=4) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[sushiswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.055050 WETH | 0.000345 WETH | 0.000000 WETH | 0.000003 WETH | 0.000342 WETH (0.6532 €) | — | 62.19 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 113.877973 USDC | 0.714076 USDC | 0.000000 USDC | 0.006344 USDC | 0.707732 USDC (0.6511 €) | — | 62.15 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v3]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.056208 WETH | 0.000309 WETH | 0.000000 WETH | 0.000003 WETH | 0.000306 WETH (0.5834 €) | — | 54.40 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 116.152836 USDC | 0.638193 USDC | 0.000000 USDC | 0.006029 USDC | 0.632164 USDC (0.5816 €) | — | 54.43 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[uniswap_v2]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.055179 WETH | 0.000307 WETH | 0.000000 WETH | 0.000003 WETH | 0.000305 WETH (0.5811 €) | — | 55.20 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 114.010951 USDC | 0.634991 USDC | 0.000000 USDC | 0.005385 USDC | 0.629606 USDC (0.5792 €) | — | 55.22 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[aerodrome]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.051894 WETH | 0.000272 WETH | 0.000000 WETH | 0.000003 WETH | 0.000269 WETH (0.5136 €) | — | 51.87 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 107.024642 USDC | 0.561837 USDC | 0.000000 USDC | 0.005743 USDC | 0.556094 USDC (0.5116 €) | — | 51.96 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 55670011 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH | 0.045931 WETH | 0.000268 WETH | 0.000000 WETH | 0.000004 WETH | 0.000264 WETH (0.5046 €) | — | 57.58 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55670011 | USDC→[aerodrome]→AUKI→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 94.751963 USDC | 0.553346 USDC | 0.000000 USDC | 0.007603 USDC | 0.545743 USDC (0.5021 €) | — | 57.60 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 55689884 | cbBTC→[uniswap_v3]→USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC | 0.009507 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4042 €) | — | 6.31 | 0.156 (n=294) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 55689884 | USDC→[aerodrome]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 703.705096 USDC | 0.444803 USDC | 0.000000 USDC | 0.005944 USDC | 0.438859 USDC (0.4038 €) | — | 6.24 | 0.156 (n=294) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 7853 ; taux observé 0.208 ; borne inférieure crédible (0.9) 0.202 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
