# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T12:31:07+00:00 ; durée 92.41 min ; blocs 56453704 → 56481401 (4406 vus)

## Connexion
- Requêtes RPC : 61488 ; erreurs : 0 ; latence p50/p95 : 279.5/1,335.2 ms
- Rafraîchissements d'état : 4406 ; âge des données au dernier bloc : 9.13 s ; changements de frais LP observés (pools à frais dynamiques) : 3529
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3437 ; cycles déclenchés par événement : 948 ; avance médiane sur le rafraîchissement multicall : 467 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,022.50 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 456 pools, 265 jetons, 15214 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 458, sous le plancher de 10000.0 $ : 2 → gardés 456 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2045.271447, 'cbBTC': 73394.102525, 'AERO': 0.529681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,533,385 | 2,022.502929 | 56481425 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,119,046 | 0.027742 | 56481425 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,598,931 | 0.027741 | 56481425 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,397,638 | 0.000014 | 56481425 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,003,949 | 2,019.562275 | 56481425 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,690,752 | 106.462737 | 56481425 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,181,683 | 0.027750 | 56481425 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,178,501 | 1.895530 | 56481425 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,143,802 | 2,019.981182 | 56481425 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,841,884 | 0.998532 | 56481425 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,008,713 | 42,289.023907 | 56481425 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 100 | 2,825,352 | 2,019.986707 | 56481425 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,171,102 | 0.027732 | 56481425 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,917,431 | 1,127,807.662643 | 56481425 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,655,977 | 0.016960 | 56481425 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,633,620 | 0.000014 | 56481425 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,584,324 | 0.000014 | 56481425 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,539,377 | 0.000000 | 56481425 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,502,041 | 0.000014 | 56481425 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,501,807 | 0.006625 | 56481425 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,729 | 0.829949 | 56481425 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,381,524 | 433.219162 | 56481425 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,261,132 | 2,022.256515 | 56481425 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,232,347 | 3,825.983506 | 56481425 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,195,187 | 15,599.201250 | 56481425 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,147,205 | 2,023.786522 | 56481425 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,115,848 | 2,019.486214 | 56481425 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,623 | 86.218152 | 56481425 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,046,779 | 1.389936 | 56481425 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,023,510 | 33,828,527.879027 | 56481425 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 990,524 | 105.711504 | 56481425 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,253 | 21.789905 | 56481425 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 923,982 | 562,921.790255 | 56481425 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 903,173 | 0.001479 | 56481425 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 889,905 | 0.000014 | 56481425 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 885,488 | 23,232,283.954573 | 56481425 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 874,202 | 0.052702 | 56481425 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 872,595 | 2,032.174616 | 56481425 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 867,450 | 1,020.294892 | 56481425 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 850,163 | 0.000000 | 56481425 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 772,150 | 78.891372 | 56481425 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 745,301 | 0.049484 | 56481425 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4600 | 739,470 | 23.364026 | 56481425 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 730,168 | 116,959.300380 | 56481425 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 691,829 | 3,843.739114 | 56481425 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 685,226 | 0.801801 | 56481425 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 657,287 | 0.515143 | 56481425 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 636,899 | 4,781,540.106604 | 56481425 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 612,652 | 0.472568 | 56481425 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 578,740 | 154,825.114907 | 56481425 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 566,921 | 0.000257 | 56481425 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 566,677 | 565,262.106440 | 56481425 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 564,421 | 0.000007 | 56481425 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 549,484 | 0.036665 | 56481425 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 483,095 | 1,020.115305 | 56481425 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 461,117 | 0.066257 | 56481425 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 450,246 | 1.001097 | 56481425 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 444,186 | 0.501968 | 56481425 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 434,538 | 24.725850 | 56481425 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 427,810 | 332.178420 | 56481425 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 5353 ; routes examinées : 81440542 ; candidats optimisés : 427175 ; net attendu > 0 : 524 ; dernier cycle 90.2 ms
- Rejets (moteur) : {'spread_below_threshold': 79763930, 'liquidity_below_min': 1235245, 'negative_expected_net': 426651, 'pool_quarantined': 6370, 'borrow_bound_too_small': 5349, 'cycle_budget_exhausted': 2473}
- Enregistrements de la session : 427175 ; net attendu > 0 : 524 ; simulés (eth_call de la vraie tx) : 34 (ok 20, échec 14) ; étiquettes ghost N+1 : 19/29 positives
- Décisions : {'REJECTED': 427175} ; motifs de rejet : {'below_safety_margin': 293, 'negative_expected_net': 426651, 'p_lower_below_threshold': 491, 'reliability_not_demonstrated': 33, 'sim_below_estimate': 9, 'simulated_net_nonpositive': 8, 'simulation_failed': 14, 'stale_data': 201}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.050848 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0486 €) | — | 5.09 | 0.203 (n=1243) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 103.311208 USDC | 0.058790 USDC | 0.000000 USDC | 0.006190 USDC | 0.052600 USDC (0.0484 €) | — | 5.09 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56466300 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006809 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0450 €) | — | 0.98 | 0.105 (n=367) | REJECTED | below_safety_margin(67<136), p_lower_below_threshold(0.10<0.75) |
| 56466300 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 497.012432 USDC | 0.053683 USDC | 0.000000 USDC | 0.004880 USDC | 0.048803 USDC (0.0449 €) | — | 0.98 | 0.105 (n=367) | REJECTED | below_safety_margin(48803<99402), p_lower_below_threshold(0.10<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.043081 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0402 €) | — | 4.97 | 0.203 (n=1243) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 87.411861 USDC | 0.049699 USDC | 0.000000 USDC | 0.006190 USDC | 0.043509 USDC (0.0400 €) | — | 4.98 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56469841 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.043702 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0340 €) | — | 4.17 | 0.205 (n=1245) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56469841 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 88.114661 USDC | 0.042829 USDC | 0.000000 USDC | 0.006101 USDC | 0.036728 USDC (0.0338 €) | — | 4.17 | 0.205 (n=1245) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56469842 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.027956 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0310 €) | — | 5.96 | 0.301 (n=223) | REJECTED | stale_data(4761ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.30<0.75) |
| 56469842 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 56.332138 USDC | 0.039489 USDC | 0.000000 USDC | 0.005908 USDC | 0.033581 USDC (0.0309 €) | — | 5.96 | 0.301 (n=223) | REJECTED | stale_data(4764ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 56463349 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.028294 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0304 €) | — | 5.73 | 0.311 (n=577) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 57.177531 USDC | 0.039098 USDC | 0.000000 USDC | 0.006190 USDC | 0.032908 USDC (0.0303 €) | — | 5.76 | 0.311 (n=577) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56460049 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 503.872102 USDC | 0.036307 USDC | 0.000000 USDC | 0.006149 USDC | 0.030158 USDC (0.0277 €) | — | 0.60 | 0.160 (n=43) | REJECTED | below_safety_margin(30158<100774), p_lower_below_threshold(0.16<0.75) |
| 56460049 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005935 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0277 €) | — | 0.69 | 0.160 (n=43) | REJECTED | below_safety_margin(41<118), p_lower_below_threshold(0.16<0.75) |
| 56460049 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.245576 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0275 €) | — | 0.60 | 0.160 (n=43) | REJECTED | below_safety_margin(14617304400314<49115134048151), p_lower_below_threshold(0.16<0.75) |
| 56469842 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.025659 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0267 €) | — | 5.59 | 0.187 (n=320) | REJECTED | stale_data(4779ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 56469842 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 51.416121 USDC | 0.034797 USDC | 0.000000 USDC | 0.005908 USDC | 0.028889 USDC (0.0266 €) | — | 5.62 | 0.187 (n=320) | REJECTED | stale_data(4783ms>4000.0), p_lower_below_threshold(0.19<0.75) |
| 56469841 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.037072 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0262 €) | — | 3.79 | 0.205 (n=1245) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56469841 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 74.708663 USDC | 0.034405 USDC | 0.000000 USDC | 0.006101 USDC | 0.028304 USDC (0.0260 €) | — | 3.79 | 0.205 (n=1245) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.038174 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0254 €) | — | 3.55 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 77.549336 USDC | 0.033710 USDC | 0.000000 USDC | 0.006190 USDC | 0.027520 USDC (0.0253 €) | — | 3.55 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.032432 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0207 €) | — | 3.40 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 65.695777 USDC | 0.028612 USDC | 0.000000 USDC | 0.006190 USDC | 0.022422 USDC (0.0206 €) | — | 3.41 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56469842 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[aerodrome_slipstream]→WETH | 0.023181 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0199 €) | — | 4.63 | 0.187 (n=320) | REJECTED | stale_data(4861ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |
| 56469842 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 46.388267 USDC | 0.027516 USDC | 0.000000 USDC | 0.005908 USDC | 0.021608 USDC (0.0199 €) | — | 4.66 | 0.187 (n=320) | REJECTED | stale_data(4864ms>4000.0), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 8296 ; taux observé 0.219 ; borne inférieure crédible (0.9) 0.213 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
