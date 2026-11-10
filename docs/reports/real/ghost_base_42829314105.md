# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T14:15:01+00:00 ; durée 12.3 min ; blocs 55644907 → 55648597 (650 vus)

## Connexion
- Requêtes RPC : 9062 ; erreurs : 8 ; latence p50/p95 : 248.7/1,261.4 ms
- Rafraîchissements d'état : 650 ; âge des données au dernier bloc : 8.48 s ; changements de frais LP observés (pools à frais dynamiques) : 484
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 601 ; cycles déclenchés par événement : 154 ; avance médiane sur le rafraîchissement multicall : 576 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,067.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 461 pools, 270 jetons, 16362 routes
- Par DEX : uniswap_v3 132, aerodrome_slipstream 99, aerodrome 190, pancakeswap_v3 26, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 164 (rejetés 2) → 569 jetons ; pools candidats 3648 (énumérés 286, par paires 0), mesurés 463, sous le plancher de 10000.0 $ : 2 → gardés 461 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2067.744894, 'cbBTC': 73787.664735, 'AERO': 0.555242}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 136,960,281 | 2,067.745395 | 55648614 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,206,373 | 0.027986 | 55648614 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,194,788 | 0.000014 | 55648614 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,599,692 | 0.027977 | 55648614 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,319,954 | 2,066.755522 | 55648614 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,923,959 | 104.130709 | 55648614 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,637,820 | 0.027977 | 55648614 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,353,525 | 1.799244 | 55648614 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,928,179 | 2,066.607938 | 55648614 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,882,240 | 1.000003 | 55648614 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,052,310 | 42,948.890050 | 55648614 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,946,884 | 2,066.492509 | 55648614 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,283,427 | 0.027999 | 55648614 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,979,674 | 1,105,866.935214 | 55648614 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,684,335 | 0.000014 | 55648614 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,658,680 | 0.000014 | 55648614 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,617,343 | 0.016327 | 55648614 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,545,206 | 0.006689 | 55648614 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,513,862 | 0.000000 | 55648614 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,492,980 | 0.000014 | 55648614 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,510 | 0.821956 | 55648614 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,433,425 | 415.331643 | 55648614 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55648614 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,274,940 | 2,067.904528 | 55648614 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,263,086 | 3,719.298238 | 55648614 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,238,089 | 14,856.691216 | 55648614 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,203,971 | 2,070.422105 | 55648614 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,632 | 79.347361 | 55648614 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,060,085 | 2,066.977806 | 55648614 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,033,288 | 35,260,186.233240 | 55648614 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 956,079 | 21.660033 | 55648614 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 945,468 | 562,233.189030 | 55648614 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 932,404 | 104.810270 | 55648614 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 919,401 | 0.001491 | 55648614 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 918,333 | 0.000014 | 55648614 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 916,096 | 22,771,584.884619 | 55648614 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 908,655 | 0.050367 | 55648614 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 890,398 | 1,025.061302 | 55648614 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 878,079 | 2,071.230075 | 55648614 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 867,223 | 0.000000 | 55648614 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 788,581 | 75.638044 | 55648614 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 777,473 | 107,836.579144 | 55648614 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 772,514 | 21.973520 | 55648614 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 759,276 | 0.051419 | 55648614 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 724,811 | 3,710.753909 | 55648614 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 701,985 | 0.798536 | 55648614 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 653,951 | 0.536179 | 55648614 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 645,887 | 4,852,179.581510 | 55648614 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 642,813 | 0.519265 | 55648614 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 605,620 | 0.000008 | 55648614 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 587,039 | 157,035.938528 | 55648614 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 582,325 | 0.000257 | 55648614 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 579,557 | 557,751.472043 | 55648614 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 564,476 | 0.038218 | 55648614 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 502,504 | 1,024.799805 | 55648614 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 483,049 | 6,719.679146 | 55648614 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 474,580 | 0.068797 | 55648614 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,503 | 1.001180 | 55648614 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 452,664 | 296.416529 | 55648614 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | WETH/msETH (stable) | 500 | 444,617 | 2.390100 | 55648614 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 803 ; routes examinées : 13138686 ; candidats optimisés : 55114 ; net attendu > 0 : 174 ; dernier cycle 271.7 ms
- Rejets (moteur) : {'spread_below_threshold': 12929120, 'liquidity_below_min': 153270, 'negative_expected_net': 54940, 'borrow_bound_too_small': 1146, 'cycle_budget_exhausted': 36}
- Enregistrements de la session : 55114 ; net attendu > 0 : 174 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 55114} ; motifs de rejet : {'below_safety_margin': 169, 'negative_expected_net': 54940, 'p_lower_below_threshold': 172, 'reliability_not_demonstrated': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.004596 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0468 €) | — | 1.50 | 0.316 (n=517) | REJECTED | below_safety_margin(69<91), p_lower_below_threshold(0.32<0.75) |
| 55647094 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.174281 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0466 €) | — | 1.41 | 0.316 (n=517) | REJECTED | below_safety_margin(24518343617352<34856237954381), p_lower_below_threshold(0.32<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 364.443705 USDC | 0.056893 USDC | 0.000000 USDC | 0.006281 USDC | 0.050612 USDC (0.0466 €) | — | 1.39 | 0.316 (n=517) | REJECTED | below_safety_margin(50612<72888), p_lower_below_threshold(0.32<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003909 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0394 €) | — | 1.48 | 0.227 (n=1406) | REJECTED | below_safety_margin(58<78), p_lower_below_threshold(0.23<0.75) |
| 55647094 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.150305 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0393 €) | — | 1.37 | 0.227 (n=1406) | REJECTED | below_safety_margin(20664748044216<30061088872016), p_lower_below_threshold(0.23<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 297.718576 USDC | 0.048873 USDC | 0.000000 USDC | 0.006281 USDC | 0.042592 USDC (0.0392 €) | — | 1.43 | 0.227 (n=1406) | REJECTED | below_safety_margin(42592<59543), p_lower_below_threshold(0.23<0.75) |
| 55645931 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006254 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0387 €) | — | 0.91 | 0.059 (n=36) | REJECTED | below_safety_margin(57<125), p_lower_below_threshold(0.06<0.75) |
| 55645931 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.223435 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(20184448102296<44686993205901), p_lower_below_threshold(0.06<0.75) |
| 55645931 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 462.507606 USDC | 0.047993 USDC | 0.000000 USDC | 0.006274 USDC | 0.041719 USDC (0.0384 €) | — | 0.90 | 0.059 (n=36) | REJECTED | below_safety_margin(41719<92501), p_lower_below_threshold(0.06<0.75) |
| 55647094 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.099025 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0314 €) | — | 1.67 | 0.227 (n=1406) | REJECTED | below_safety_margin(16512542878146<19804904995583), p_lower_below_threshold(0.23<0.75) |
| 55647094 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 200.308158 USDC | 0.040373 USDC | 0.000000 USDC | 0.006281 USDC | 0.034092 USDC (0.0314 €) | — | 1.70 | 0.227 (n=1406) | REJECTED | below_safety_margin(34092<40061), p_lower_below_threshold(0.23<0.75) |
| 55647094 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002455 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0312 €) | — | 1.87 | 0.227 (n=1406) | REJECTED | below_safety_margin(46<49), p_lower_below_threshold(0.23<0.75) |
| 55645931 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 319.275131 USDC | 0.032633 USDC | 0.000000 USDC | 0.004691 USDC | 0.027942 USDC (0.0257 €) | — | 0.88 | 0.081 (n=338) | REJECTED | below_safety_margin(27942<63855), p_lower_below_threshold(0.08<0.75) |
| 55645931 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.154898 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000013 WETH (0.0257 €) | — | 0.87 | 0.081 (n=338) | REJECTED | below_safety_margin(13496928497097<30979510259946), p_lower_below_threshold(0.08<0.75) |
| 55646688 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 274.848829 USDC | 0.024268 USDC | 0.000000 USDC | 0.004680 USDC | 0.019588 USDC (0.0180 €) | — | 0.71 | 0.081 (n=338) | REJECTED | below_safety_margin(19588<54969), p_lower_below_threshold(0.08<0.75) |
| 55646688 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.133019 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0180 €) | — | 0.71 | 0.081 (n=338) | REJECTED | below_safety_margin(9469341376538<26603798352582), p_lower_below_threshold(0.08<0.75) |
| 55645932 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 86.973484 USDC | 0.023337 USDC | 0.000000 USDC | 0.006277 USDC | 0.017060 USDC (0.0157 €) | — | 1.96 | 0.228 (n=1405) | REJECTED | below_safety_margin(17060<17394), p_lower_below_threshold(0.23<0.75) |
| 55645932 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001167 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0156 €) | — | 1.97 | 0.228 (n=1405) | REJECTED | p_lower_below_threshold(0.23<0.75) |
| 55647292 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.092285 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0152 €) | — | 0.87 | 0.050 (n=102) | REJECTED | below_safety_margin(7989684016711<18456995056030), p_lower_below_threshold(0.05<0.75) |
| 55647292 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 190.367200 USDC | 0.021182 USDC | 0.000000 USDC | 0.004680 USDC | 0.016502 USDC (0.0152 €) | — | 0.87 | 0.050 (n=102) | REJECTED | below_safety_margin(16502<38073), p_lower_below_threshold(0.05<0.75) |
| 55645932 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.054761 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0148 €) | — | 1.42 | 0.228 (n=1405) | REJECTED | below_safety_margin(7790569102684<10952164449274), p_lower_below_threshold(0.23<0.75) |
| 55647747 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.113058 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0148 €) | — | 0.69 | 0.050 (n=102) | REJECTED | below_safety_margin(7760427358988<22611626869902), p_lower_below_threshold(0.05<0.75) |
| 55647748 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.113058 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000008 WETH (0.0148 €) | — | 0.69 | 0.050 (n=102) | REJECTED | below_safety_margin(7760427358988<22611626869902), p_lower_below_threshold(0.05<0.75) |
| 55647747 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 233.297853 USDC | 0.020706 USDC | 0.000000 USDC | 0.004673 USDC | 0.016033 USDC (0.0148 €) | — | 0.69 | 0.050 (n=102) | REJECTED | below_safety_margin(16033<46659), p_lower_below_threshold(0.05<0.75) |
| 55647748 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 233.297853 USDC | 0.020706 USDC | 0.000000 USDC | 0.004673 USDC | 0.016033 USDC (0.0148 €) | — | 0.69 | 0.050 (n=102) | REJECTED | below_safety_margin(16033<46659), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 7508 ; taux observé 0.193 ; borne inférieure crédible (0.9) 0.187 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
