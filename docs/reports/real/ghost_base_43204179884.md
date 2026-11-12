# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T13:08:37+00:00 ; durée 129.91 min ; blocs 56453704 → 56492635 (5876 vus)

## Connexion
- Requêtes RPC : 83257 ; erreurs : 3 ; latence p50/p95 : 535.1/1,554.5 ms
- Rafraîchissements d'état : 5876 ; âge des données au dernier bloc : 11.0 s ; changements de frais LP observés (pools à frais dynamiques) : 4668
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5771 ; cycles déclenchés par événement : 1741 ; avance médiane sur le rafraîchissement multicall : 537 ms
- Gaz : base fee 0.005431 gwei ; prix ETH (pool le plus profond) : 2,019.76 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 456 pools, 265 jetons, 15214 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 25, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 282, par paires 0), mesurés 458, sous le plancher de 10000.0 $ : 2 → gardés 456 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2045.271447, 'cbBTC': 73394.102525, 'AERO': 0.529681}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 132,478,101 | 2,019.764286 | 56492635 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,213,072 | 0.027709 | 56492635 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,589,071 | 0.027741 | 56492635 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,394,343 | 0.000014 | 56492635 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 6,996,659 | 2,015.442739 | 56492635 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,685,611 | 106.337966 | 56492635 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,176,754 | 0.027705 | 56492635 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,152,616 | 1.919234 | 56492635 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,143,373 | 2,015.402368 | 56492635 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,841,231 | 0.998530 | 56492635 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,006,520 | 42,236.130181 | 56492635 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 185 | 2,820,161 | 2,014.849879 | 56492635 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,168,495 | 0.027732 | 56492635 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,914,834 | 1,127,807.662643 | 56492635 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,642,079 | 0.016703 | 56492635 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,633,417 | 0.000014 | 56492635 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,584,122 | 0.000014 | 56492635 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,537,281 | 0.000000 | 56492635 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,501,948 | 0.000014 | 56492635 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,497,125 | 0.006611 | 56492635 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,729 | 0.829949 | 56492635 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,380,074 | 432.774363 | 56492635 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,260,279 | 2,019.664352 | 56492635 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,221,899 | 3,870.767022 | 56492635 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,194,899 | 15,601.228104 | 56492635 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,146,428 | 2,019.881494 | 56492635 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,114,549 | 2,015.024734 | 56492635 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,061,623 | 86.218152 | 56492635 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,046,779 | 1.389936 | 56492635 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/doginme | 10000 | 1,022,076 | 33,833,259.428073 | 56492635 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 989,962 | 105.721510 | 56492635 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 954,603 | 21.765110 | 56492635 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 922,730 | 562,924.402076 | 56492635 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 902,144 | 0.001476 | 56492635 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 889,744 | 0.000014 | 56492635 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 884,289 | 23,232,283.954573 | 56492635 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 874,066 | 0.052644 | 56492635 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 872,073 | 2,032.174616 | 56492635 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 866,283 | 1,020.278806 | 56492635 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 848,950 | 0.000000 | 56492635 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 772,545 | 78.810634 | 56492635 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 744,844 | 0.049422 | 56492635 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 738,869 | 23.390305 | 56492635 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 730,742 | 116,459.766860 | 56492635 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 687,083 | 3,843.739114 | 56492635 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 684,298 | 0.801801 | 56492635 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 655,940 | 0.513792 | 56492635 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 635,888 | 4,783,780.781250 | 56492635 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 610,972 | 0.470038 | 56492635 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 577,349 | 155,151.788185 | 56492635 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2102 | 565,910 | 565,562.681195 | 56492635 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | VIRTUAL/WETH | 10000 | 565,868 | 0.000257 | 56492635 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 559,460 | 0.000007 | 56492635 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | FLOCK/USDC | 3000 | 549,834 | 0.036700 | 56492635 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 482,861 | 1,020.187274 | 56492635 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 462,438 | 0.066498 | 56492635 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 11 | 450,222 | 1.001102 | 56492635 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 443,759 | 0.502453 | 56492635 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 433,688 | 24.756286 | 56492635 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 428,350 | 930,299.766615 | 56492635 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 7616 ; routes examinées : 115869824 ; candidats optimisés : 593161 ; net attendu > 0 : 939 ; dernier cycle 166.4 ms
- Rejets (moteur) : {'spread_below_threshold': 113330300, 'liquidity_below_min': 1929810, 'negative_expected_net': 592222, 'borrow_bound_too_small': 7611, 'pool_quarantined': 6370, 'cycle_budget_exhausted': 2481}
- Enregistrements de la session : 593160 ; net attendu > 0 : 939 ; simulés (eth_call de la vraie tx) : 62 (ok 40, échec 22) ; étiquettes ghost N+1 : 33/48 positives
- Décisions : {'REJECTED': 593160} ; motifs de rejet : {'below_safety_margin': 650, 'negative_expected_net': 592221, 'p_lower_below_threshold': 897, 'reliability_not_demonstrated': 42, 'sim_below_estimate': 16, 'simulated_net_nonpositive': 15, 'simulation_failed': 22, 'stale_data': 347}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56486832 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 77.387925 USDC | 0.517155 USDC | 0.000000 USDC | 0.004270 USDC | 0.512885 USDC (0.4719 €) | — | 66.27 | 0.000 (n=22) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.050848 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0486 €) | — | 5.09 | 0.203 (n=1243) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 103.311208 USDC | 0.058790 USDC | 0.000000 USDC | 0.006190 USDC | 0.052600 USDC (0.0484 €) | — | 5.09 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56466300 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.006809 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0450 €) | — | 0.98 | 0.105 (n=367) | REJECTED | below_safety_margin(67<136), p_lower_below_threshold(0.10<0.75) |
| 56466300 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 497.012432 USDC | 0.053683 USDC | 0.000000 USDC | 0.004880 USDC | 0.048803 USDC (0.0449 €) | — | 0.98 | 0.105 (n=367) | REJECTED | below_safety_margin(48803<99402), p_lower_below_threshold(0.10<0.75) |
| 56463349 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.043081 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0402 €) | — | 4.97 | 0.203 (n=1243) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 87.411861 USDC | 0.049699 USDC | 0.000000 USDC | 0.006190 USDC | 0.043509 USDC (0.0400 €) | — | 4.98 | 0.203 (n=1243) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56469841 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.043702 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0340 €) | — | 4.17 | 0.205 (n=1245) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56469841 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 88.114661 USDC | 0.042829 USDC | 0.000000 USDC | 0.006101 USDC | 0.036728 USDC (0.0338 €) | — | 4.17 | 0.205 (n=1245) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56484922 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003749 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0329 €) | — | 1.31 | 0.269 (n=1594) | REJECTED | below_safety_margin(49<74), p_lower_below_threshold(0.27<0.75) |
| 56484922 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003749 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0329 €) | — | 1.31 | 0.269 (n=1594) | REJECTED | below_safety_margin(49<74), p_lower_below_threshold(0.27<0.75) |
| 56484922 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.129619 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0327 €) | — | 1.36 | 0.269 (n=1594) | REJECTED | below_safety_margin(17579017177507<25923814688836), p_lower_below_threshold(0.27<0.75) |
| 56484922 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.129619 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0327 €) | — | 1.36 | 0.269 (n=1594) | REJECTED | below_safety_margin(17579017177507<25923814688836), p_lower_below_threshold(0.27<0.75) |
| 56484922 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 261.793303 USDC | 0.041600 USDC | 0.000000 USDC | 0.006094 USDC | 0.035506 USDC (0.0327 €) | — | 1.36 | 0.269 (n=1594) | REJECTED | below_safety_margin(35506<52358), p_lower_below_threshold(0.27<0.75) |
| 56484922 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 261.793303 USDC | 0.041600 USDC | 0.000000 USDC | 0.006094 USDC | 0.035506 USDC (0.0327 €) | — | 1.36 | 0.269 (n=1594) | REJECTED | below_safety_margin(35506<52358), p_lower_below_threshold(0.27<0.75) |
| 56469842 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[pancakeswap_v3]→WETH | 0.027956 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0310 €) | — | 5.96 | 0.301 (n=223) | REJECTED | stale_data(4761ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.30<0.75) |
| 56469842 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC | 56.332138 USDC | 0.039489 USDC | 0.000000 USDC | 0.005908 USDC | 0.033581 USDC (0.0309 €) | — | 5.96 | 0.301 (n=223) | REJECTED | stale_data(4764ms>4000.0), p_lower_below_threshold(0.30<0.75) |
| 56463349 | WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.028294 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0304 €) | — | 5.73 | 0.311 (n=577) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 56463349 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AAVE→[uniswap_v3]→USDC | 57.177531 USDC | 0.039098 USDC | 0.000000 USDC | 0.006190 USDC | 0.032908 USDC (0.0303 €) | — | 5.76 | 0.311 (n=577) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56460049 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 503.872102 USDC | 0.036307 USDC | 0.000000 USDC | 0.006149 USDC | 0.030158 USDC (0.0277 €) | — | 0.60 | 0.160 (n=43) | REJECTED | below_safety_margin(30158<100774), p_lower_below_threshold(0.16<0.75) |
| 56460049 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005935 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0277 €) | — | 0.69 | 0.160 (n=43) | REJECTED | below_safety_margin(41<118), p_lower_below_threshold(0.16<0.75) |
| 56460049 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.245576 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0275 €) | — | 0.60 | 0.160 (n=43) | REJECTED | below_safety_margin(14617304400314<49115134048151), p_lower_below_threshold(0.16<0.75) |
| 56492421 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.139438 WETH | 0.000017 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0273 €) | — | 1.05 | 0.104 (n=368) | REJECTED | below_safety_margin(14667942796626<27887651619711), stale_data(4248ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56492421 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 279.529058 USDC | 0.034386 USDC | 0.000000 USDC | 0.004769 USDC | 0.029617 USDC (0.0272 €) | — | 1.06 | 0.104 (n=368) | REJECTED | below_safety_margin(29617<55905), stale_data(4251ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56469842 | WETH→[aerodrome_slipstream]→LCAP→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.025659 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0267 €) | — | 5.59 | 0.187 (n=320) | REJECTED | stale_data(4779ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 8315 ; taux observé 0.220 ; borne inférieure crédible (0.9) 0.215 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
