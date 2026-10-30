# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T14:53:05+00:00 ; durée 71.17 min ; blocs 53289181 → 53291316 (2128 vus)

## Connexion
- Requêtes RPC : 25734 ; erreurs : 0 ; latence p50/p95 : 68.1/488.0 ms
- Rafraîchissements d'état : 2129 ; âge des données au dernier bloc : 1.38 s ; changements de frais LP observés (pools à frais dynamiques) : 6561
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55381 ; cycles déclenchés par événement : 2487 ; avance médiane sur le rafraîchissement multicall : 843 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,229.28 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,929,682 | 2,229.278587 | 53291316 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,881,314 | 0.028969 | 53291316 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,567,491 | 0.000013 | 53291316 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,007,219 | 0.028933 | 53291316 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,158,197 | 2,232.120219 | 53291316 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,780,343 | 99.360067 | 53291316 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,625,735 | 0.001605 | 53291316 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,071,181 | 1.604989 | 53291316 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,533,712 | 0.028958 | 53291316 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 564 | 4,170,081 | 2,231.337573 | 53291316 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,048,102 | 0.999937 | 53291316 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,044,987 | 2,231.353074 | 53291316 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,551,593 | 36,873.217678 | 53291316 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,749,484 | 0.028946 | 53291316 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2745 | 2,340,585 | 99.383164 | 53291316 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,043,682 | 1,206,344.208581 | 53291316 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 568 | 1,912,831 | 0.000013 | 53291316 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,763,239 | 0.018152 | 53291316 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,708,078 | 0.000000 | 53291316 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,676,095 | 418.457050 | 53291316 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,658,335 | 0.000013 | 53291316 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,560,923 | 0.000013 | 53291316 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,519,757 | 2,229.270340 | 53291316 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,463,389 | 1.643209 | 53291316 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 1,460,681 | 0.000013 | 53291316 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,334 | 0.825312 | 53291316 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,403,942 | 3,581.967578 | 53291316 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,312,201 | 2,232.047654 | 53291316 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,300,769 | 14,444.523360 | 53291316 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,269,820 | 0.005004 | 53291316 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,053 | 70.018466 | 53291316 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,099,794 | 36,289,473.124265 | 53291316 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,051,473 | 515,838.493842 | 53291316 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,029,869 | 21,083,127.034335 | 53291316 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,011,031 | 74,252.329242 | 53291316 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | DRB/WETH | 10000 | 1,006,831 | 0.000000 | 53291316 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | WETH/USDC | 3000 | 1,006,651 | 2,228.742646 | 53291316 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,098 | 19.273722 | 53291316 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 968,793 | 99.827001 | 53291316 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 963,936 | 67.373610 | 53291316 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 951,162 | 0.044529 | 53291316 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 926,950 | 1,209,275.316210 | 53291316 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 918,229 | 2,228.113244 | 53291316 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,718 | 1,078.637537 | 53291316 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 863,812 | 3,587.716388 | 53291316 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 857,441 | 0.000554 | 53291316 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 833,690 | 19.579422 | 53291316 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 807,930 | 0.058583 | 53291316 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 793,388 | 17.771720 | 53291316 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 754,572 | 0.803616 | 53291316 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 727,728 | 0.000260 | 53291316 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 712,164 | 0.584379 | 53291316 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 710,513 | 4,650,175.633781 | 53291316 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 691,798 | 0.000008 | 53291316 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 679,098 | 2.330640 | 53291316 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 653,147 | 146,855.665064 | 53291316 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 652,634 | 517,139.218563 | 53291316 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 632,759 | 0.506062 | 53291316 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 606,294 | 0.091687 | 53291316 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 599,548 | 0.914674 | 53291316 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 4615 ; routes examinées : 86475870 ; candidats optimisés : 530317 ; net attendu > 0 : 2130 ; dernier cycle 207.0 ms
- Rejets (moteur) : {'spread_below_threshold': 84126400, 'liquidity_below_min': 1452236, 'negative_expected_net': 528187, 'pool_quarantined': 338566, 'unquotable': 22863, 'borrow_bound_too_small': 4613, 'cycle_budget_exhausted': 875}
- Enregistrements de la session : 530317 ; net attendu > 0 : 2130 ; simulés (eth_call de la vraie tx) : 85 (ok 45, échec 40) ; étiquettes ghost N+1 : 14/58 positives
- Décisions : {'REJECTED': 530317} ; motifs de rejet : {'below_safety_margin': 1806, 'negative_expected_net': 528187, 'p_lower_below_threshold': 1898, 'reliability_not_demonstrated': 232, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 2, 'simulation_failed': 40}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53289560 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 140.927016 USDC | 0.310023 USDC | 0.000000 USDC | 0.006770 USDC | 0.303253 USDC (0.2790 €) | — | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.063562 WETH | 0.000140 WETH | 0.000000 WETH | 0.000003 WETH | 0.000137 WETH (0.2783 €) | 0.000137 WETH | 21.52 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 134.625773 USDC | 0.296283 USDC | 0.000000 USDC | 0.007106 USDC | 0.289177 USDC (0.2660 €) | — | 21.48 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.060712 WETH | 0.000134 WETH | 0.000000 WETH | 0.000003 WETH | 0.000130 WETH (0.2653 €) | 0.000130 WETH | 21.48 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 111.503746 USDC | 0.272062 USDC | 0.000000 USDC | 0.006770 USDC | 0.265292 USDC (0.2441 €) | — | 23.79 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.050283 WETH | 0.000123 WETH | 0.000000 WETH | 0.000003 WETH | 0.000120 WETH (0.2434 €) | 0.000120 WETH | 23.79 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 110.539928 USDC | 0.269722 USDC | 0.000000 USDC | 0.006770 USDC | 0.262952 USDC (0.2419 €) | — | 23.79 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.049846 WETH | 0.000122 WETH | 0.000000 WETH | 0.000003 WETH | 0.000119 WETH (0.2413 €) | — | 23.79 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53289898 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→USDC | 1,075.433514 USDC | 0.229695 USDC | 0.000000 USDC | 0.005769 USDC | 0.223926 USDC (0.2060 €) | — | 2.08 | 0.008 (n=36) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.01<0.75) |
| 53289560 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 94.442109 USDC | 0.227270 USDC | 0.000000 USDC | 0.006770 USDC | 0.220500 USDC (0.2029 €) | — | 23.35 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.042577 WETH | 0.000102 WETH | 0.000000 WETH | 0.000003 WETH | 0.000099 WETH (0.2023 €) | — | 23.35 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 87.250859 USDC | 0.224754 USDC | 0.000000 USDC | 0.007106 USDC | 0.217648 USDC (0.2002 €) | — | 24.95 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.039317 WETH | 0.000101 WETH | 0.000000 WETH | 0.000003 WETH | 0.000098 WETH (0.1996 €) | — | 24.94 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289479 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.135000 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1819 €) | — | 6.62 | 0.161 (n=223) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 297.734168 USDC | 0.204126 USDC | 0.000000 USDC | 0.006774 USDC | 0.197352 USDC (0.1816 €) | — | 6.63 | 0.161 (n=223) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53290065 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,007.174039 USDC | 0.113535 USDC | 0.000000 USDC | 0.005397 USDC | 0.108138 USDC (0.0995 €) | — | 1.07 | 0.042 (n=141) | REJECTED | below_safety_margin(108138<201434), p_lower_below_threshold(0.04<0.75) |
| 53290065 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.012476 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0990 €) | — | 1.12 | 0.042 (n=141) | REJECTED | below_safety_margin(140<249), p_lower_below_threshold(0.04<0.75) |
| 53289479 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.061663 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0852 €) | — | 6.79 | 0.107 (n=445) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 135.978925 USDC | 0.099193 USDC | 0.000000 USDC | 0.006774 USDC | 0.092419 USDC (0.0850 €) | — | 6.80 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53289560 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC | 33.921099 USDC | 0.093310 USDC | 0.000000 USDC | 0.006770 USDC | 0.086540 USDC (0.0796 €) | — | 25.51 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289560 | WETH→[uniswap_v3]→FLOCK→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.015253 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0792 €) | — | 25.50 | 0.000 (n=40) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53289479 | WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.058310 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0772 €) | — | 6.50 | 0.107 (n=445) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC | 128.804160 USDC | 0.090490 USDC | 0.000000 USDC | 0.006774 USDC | 0.083716 USDC (0.0770 €) | — | 6.50 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53290939 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 260.734617 USDC | 0.089992 USDC | 0.000000 USDC | 0.007121 USDC | 0.082871 USDC (0.0762 €) | — | 3.18 | 0.106 (n=450) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53290939 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.116274 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0759 €) | — | 3.19 | 0.106 (n=450) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |

## Fiabilité et décision
- Observations ghost : 3708 ; taux observé 0.118 ; borne inférieure crédible (0.9) 0.111 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
