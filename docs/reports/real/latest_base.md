# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T12:13:49+00:00 ; durée 321.23 min ; blocs 55947872 → 56044155 (16082 vus)

## Connexion
- Requêtes RPC : 201715 ; erreurs : 430 ; latence p50/p95 : 110.5/1,727.1 ms
- Rafraîchissements d'état : 16082 ; âge des données au dernier bloc : 9.0 s ; changements de frais LP observés (pools à frais dynamiques) : 7817
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 9477 ; cycles déclenchés par événement : 3914 ; avance médiane sur le rafraîchissement multicall : 578 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,056.67 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 16590 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 282, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2057.512263, 'cbBTC': 73519.133148, 'AERO': 0.539928}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,067,376 | 2,056.666125 | 56044181 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,424,498 | 0.027800 | 56044181 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,583,966 | 0.027860 | 56044181 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,431,462 | 0.000014 | 56044181 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,084,313 | 2,053.877764 | 56044181 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,794,789 | 106.744273 | 56044181 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,318,119 | 0.027793 | 56044181 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,240,658 | 1.866589 | 56044181 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,047,943 | 2,053.021663 | 56044181 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,887,372 | 1.000003 | 56044181 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,052,981 | 42,470.831991 | 56044181 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,933,159 | 2,052.871972 | 56044181 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,213,058 | 0.027847 | 56044181 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,954,456 | 1,122,462.090019 | 56044181 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,654,258 | 0.000014 | 56044181 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,616,019 | 0.016306 | 56044181 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,590,455 | 0.000014 | 56044181 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,552,503 | 0.000000 | 56044181 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,507,061 | 0.006494 | 56044181 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,463,882 | 0.825575 | 56044181 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,000 | 1.373193 | 56044181 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,442,634 | 0.000014 | 56044181 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,420,381 | 417.244340 | 56044181 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,271,611 | 2,056.632627 | 56044181 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,254,687 | 3,833.640089 | 56044181 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,234,145 | 15,023.655045 | 56044181 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,157,652 | 2,057.739373 | 56044181 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,108,802 | 2,053.819081 | 56044181 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,872 | 86.340286 | 56044181 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,047,128 | 33,250,347.878996 | 56044181 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 963,327 | 21.163784 | 56044181 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 952,696 | 107.495889 | 56044181 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 942,432 | 558,021.159866 | 56044181 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 918,388 | 0.001485 | 56044181 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 914,989 | 0.000014 | 56044181 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 904,164 | 23,083,911.649235 | 56044181 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 890,418 | 0.051942 | 56044181 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 888,403 | 1,007.655258 | 56044181 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 878,799 | 2,050.503253 | 56044181 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 878,239 | 0.000000 | 56044181 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 765,367 | 80.295826 | 56044181 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 760,135 | 0.051535 | 56044181 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 758,434 | 22.553647 | 56044181 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 756,816 | 112,587.969888 | 56044181 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 703,135 | 3,815.056844 | 56044181 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 696,307 | 0.802938 | 56044181 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 672,115 | 0.534246 | 56044181 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 666,601 | 4,510,269.054394 | 56044181 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 623,585 | 0.489683 | 56044181 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 598,946 | 149,353.129876 | 56044181 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 581,321 | 0.000007 | 56044181 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 580,484 | 0.000259 | 56044181 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 578,798 | 554,451.415111 | 56044181 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 563,103 | 0.038052 | 56044181 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 496,460 | 1,007.223145 | 56044181 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 459,753 | 0.493874 | 56044181 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 459,634 | 0.066010 | 56044181 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,334 | 1.000915 | 56044181 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 442,319 | 24.671975 | 56044181 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 438,506 | 912,884.763550 | 56044181 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 19995 ; routes examinées : 331717050 ; candidats optimisés : 1496377 ; net attendu > 0 : 1367 ; dernier cycle 314.0 ms
- Rejets (moteur) : {'spread_below_threshold': 323831999, 'liquidity_below_min': 6343265, 'negative_expected_net': 1495010, 'borrow_bound_too_small': 39385, 'cycle_budget_exhausted': 6024}
- Enregistrements de la session : 1496377 ; net attendu > 0 : 1367 ; simulés (eth_call de la vraie tx) : 57 (ok 39, échec 18) ; étiquettes ghost N+1 : 19/51 positives
- Décisions : {'REJECTED': 1496377} ; motifs de rejet : {'below_safety_margin': 1167, 'negative_expected_net': 1495010, 'p_lower_below_threshold': 1332, 'reliability_not_demonstrated': 35, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 18, 'stale_data': 167}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56001114 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 137.998270 USDC | 4.819843 USDC | 0.000000 USDC | 0.004326 USDC | 4.815517 USDC (4.4303 €) | — | 348.95 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55983017 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.020036 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4822 €) | — | 3.54 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.719100 WETH | 0.000257 WETH | 0.000000 WETH | 0.000003 WETH | 0.000254 WETH (0.4818 €) | 0.000254 WETH | 3.53 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,549.178979 USDC | 0.528634 USDC | 0.000000 USDC | 0.006198 USDC | 0.522436 USDC (0.4806 €) | — | 3.37 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,089.934341 USDC | 0.438517 USDC | 0.000000 USDC | 0.006166 USDC | 0.432351 USDC (0.3978 €) | — | 3.97 | 0.200 (n=1186) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.530685 WETH | 0.000213 WETH | 0.000000 WETH | 0.000003 WETH | 0.000210 WETH (0.3973 €) | — | 3.97 | 0.200 (n=1186) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56009339 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.013967 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3969 €) | — | 4.20 | 0.200 (n=1186) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.015524 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.3790 €) | — | 3.59 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.581928 WETH | 0.000203 WETH | 0.000000 WETH | 0.000003 WETH | 0.000200 WETH (0.3789 €) | 0.000200 WETH | 3.43 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,207.822455 USDC | 0.417107 USDC | 0.000000 USDC | 0.006511 USDC | 0.410596 USDC (0.3777 €) | — | 3.40 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,031.033910 USDC | 0.403691 USDC | 0.000000 USDC | 0.006166 USDC | 0.397525 USDC (0.3657 €) | — | 3.86 | 0.200 (n=1186) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.501895 WETH | 0.000196 WETH | 0.000000 WETH | 0.000003 WETH | 0.000193 WETH (0.3652 €) | — | 3.85 | 0.200 (n=1186) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56009339 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.013744 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3651 €) | — | 3.92 | 0.200 (n=1186) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.480295 WETH | 0.000183 WETH | 0.000000 WETH | 0.000003 WETH | 0.000180 WETH (0.3420 €) | 0.000180 WETH | 3.76 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.013069 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3416 €) | — | 3.85 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 973.694435 USDC | 0.376714 USDC | 0.000000 USDC | 0.006198 USDC | 0.370516 USDC (0.3409 €) | — | 3.81 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.014568 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3373 €) | — | 3.42 | 0.200 (n=1186) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,126.112237 USDC | 0.373379 USDC | 0.000000 USDC | 0.006789 USDC | 0.366590 USDC (0.3373 €) | — | 3.26 | 0.200 (n=1186) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.552223 WETH | 0.000182 WETH | 0.000000 WETH | 0.000003 WETH | 0.000178 WETH (0.3369 €) | — | 3.23 | 0.200 (n=1186) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.20<0.75) |
| 56009339 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,245.386618 USDC | 0.366852 USDC | 0.000000 USDC | 0.004607 USDC | 0.362245 USDC (0.3333 €) | — | 2.91 | 0.081 (n=113) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 56009339 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.605957 WETH | 0.000179 WETH | 0.000000 WETH | 0.000002 WETH | 0.000176 WETH (0.3328 €) | — | 2.91 | 0.081 (n=113) | REJECTED | p_lower_below_threshold(0.08<0.75) |
| 55983017 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.012868 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3321 €) | — | 3.80 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.461055 WETH | 0.000178 WETH | 0.000000 WETH | 0.000003 WETH | 0.000175 WETH (0.3319 €) | — | 3.80 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 55983017 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 952.619448 USDC | 0.365900 USDC | 0.000000 USDC | 0.006198 USDC | 0.359702 USDC (0.3309 €) | — | 3.78 | 0.201 (n=1182) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56009339 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.016664 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3278 €) | — | 2.90 | 0.262 (n=1558) | REJECTED | p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 8039 ; taux observé 0.212 ; borne inférieure crédible (0.9) 0.206 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.6% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
