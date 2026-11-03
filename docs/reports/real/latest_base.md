# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T21:57:42+00:00 ; durée 188.23 min ; blocs 53471207 → 53476854 (5500 vus)

## Connexion
- Requêtes RPC : 65591 ; erreurs : 633 ; latence p50/p95 : 166.8/1,209.3 ms
- Rafraîchissements d'état : 5501 ; âge des données au dernier bloc : 2.05 s ; changements de frais LP observés (pools à frais dynamiques) : 5459
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 50837 ; cycles déclenchés par événement : 5031 ; avance médiane sur le rafraîchissement multicall : 381 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,291.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,623,970 | 2,291.025169 | 53476854 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,413,820 | 0.029460 | 53476854 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,215,525 | 0.029450 | 53476854 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,076,357 | 0.000013 | 53476854 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,055,194 | 2,293.053096 | 53476854 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,816,936 | 100.682618 | 53476854 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,629,101 | 0.001573 | 53476854 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,405,598 | 1.581305 | 53476854 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,838,727 | 0.029454 | 53476854 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,174,769 | 2,292.859040 | 53476854 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,091,151 | 0.999913 | 53476854 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,879,467 | 2,292.714753 | 53476854 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,451,078 | 41,244.504045 | 53476854 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,691,470 | 0.029441 | 53476854 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,175,876 | 1,123,985.241900 | 53476854 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2706 | 2,142,809 | 100.680675 | 53476854 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,816,523 | 0.000013 | 53476854 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,738,744 | 0.017809 | 53476854 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,682,744 | 0.000000 | 53476854 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,628,507 | 0.000013 | 53476854 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,560,478 | 438.613399 | 53476854 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,556,315 | 0.000013 | 53476854 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53476854 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,537,740 | 0.006133 | 53476854 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | WETH/USDC | 3000 | 1,509,539 | 2,290.951219 | 53476854 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,800 | 0.821850 | 53476854 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,426,831 | 3,622.403033 | 53476854 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,342,293 | 2,298.924176 | 53476854 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,339,660 | 2,293.010247 | 53476854 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,298,742 | 14,892.096077 | 53476854 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,197,023 | 0.000013 | 53476854 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,158,637 | 72.384430 | 53476854 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,128,533 | 36,822,127.565791 | 53476854 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,060,244 | 545,627.257903 | 53476854 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,059,559 | 0.000000 | 53476854 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,525 | 21,950,664.012046 | 53476854 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,000,825 | 18.906153 | 53476854 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 960,474 | 101.018579 | 53476854 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 950,291 | 1,055.355040 | 53476854 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 949,401 | 88,834.136125 | 53476854 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 940,082 | 70.838342 | 53476854 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 929,102 | 2,282.122456 | 53476854 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 926,665 | 1,275,067.388968 | 53476854 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 894,609 | 0.043910 | 53476854 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 878,691 | 0.000556 | 53476854 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 847,951 | 3,646.232124 | 53476854 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 826,813 | 19.856792 | 53476854 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,049 | 0.057228 | 53476854 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 777,636 | 0.799140 | 53476854 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 738,722 | 0.595689 | 53476854 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 728,517 | 0.000257 | 53476854 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 720,161 | 4,786,021.092988 | 53476854 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 673,700 | 0.000008 | 53476854 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 670,903 | 147,225.450667 | 53476854 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 665,070 | 0.555673 | 53476854 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 658,233 | 2.368619 | 53476854 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 651,315 | 546,778.451548 | 53476854 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 615,398 | 0.914716 | 53476854 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 590,192 | 0.087827 | 53476854 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,703 | 0.038780 | 53476854 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 10531 ; routes examinées : 204806888 ; candidats optimisés : 596343 ; net attendu > 0 : 545 ; dernier cycle 94.9 ms
- Rejets (moteur) : {'spread_below_threshold': 201643150, 'liquidity_below_min': 2535478, 'negative_expected_net': 595798, 'unquotable': 21050, 'borrow_bound_too_small': 10525, 'cycle_budget_exhausted': 342}
- Enregistrements de la session : 596343 ; net attendu > 0 : 545 ; simulés (eth_call de la vraie tx) : 22 (ok 10, échec 12) ; étiquettes ghost N+1 : 0/18 positives
- Décisions : {'REJECTED': 596343} ; motifs de rejet : {'below_safety_margin': 497, 'negative_expected_net': 595798, 'p_lower_below_threshold': 537, 'reliability_not_demonstrated': 8, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 12, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53476657 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 137.053961 USDC | 3.316241 USDC | 0.000000 USDC | 0.004826 USDC | 3.311415 USDC (3.0465 €) | — | 241.61 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472395 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.026252 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1137 €) | — | 20.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472362 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.020014 WETH | 0.000033 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0642 €) | — | 15.21 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53476424 | WETH→[aerodrome_slipstream]→ZRO→[uniswap_v3]→WETH | 0.010639 WETH | 0.000024 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0451 €) | — | 20.14 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53476455 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 771.228037 USDC | 0.051205 USDC | 0.000000 USDC | 0.005140 USDC | 0.046065 USDC (0.0424 €) | — | 0.60 | 0.034 (n=197) | REJECTED | below_safety_margin(46065<154245), p_lower_below_threshold(0.03<0.75) |
| 53476455 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010013 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0422 €) | — | 0.59 | 0.034 (n=197) | REJECTED | below_safety_margin(59<200), p_lower_below_threshold(0.03<0.75) |
| 53475795 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 19.939998 USDC | 0.035428 USDC | 0.000000 USDC | 0.004826 USDC | 0.030602 USDC (0.0282 €) | — | 15.35 | 0.010 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 61.786427 USDC | 0.031613 USDC | 0.000000 USDC | 0.007215 USDC | 0.024398 USDC (0.0224 €) | — | 3.95 | 0.159 (n=607) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.027157 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0224 €) | — | 3.92 | 0.159 (n=607) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53476025 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 34.625441 USDC | 0.029251 USDC | 0.000000 USDC | 0.005141 USDC | 0.024110 USDC (0.0222 €) | — | 6.96 | 0.034 (n=242) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53475911 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001166 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0207 €) | 0.000000 cbBTC | 2.49 | 0.259 (n=342) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 53475911 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 90.505089 USDC | 0.029717 USDC | 0.000000 USDC | 0.007227 USDC | 0.022490 USDC (0.0207 €) | 0.022490 USDC | 2.48 | 0.259 (n=342) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 34.134904 USDC | 0.028597 USDC | 0.000000 USDC | 0.006868 USDC | 0.021729 USDC (0.0200 €) | 0.021729 USDC | 6.37 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 34.134904 USDC | 0.028597 USDC | 0.000000 USDC | 0.006868 USDC | 0.021729 USDC (0.0200 €) | — | 6.37 | 0.291 (n=315) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 53474568 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 48.971145 USDC | 0.026206 USDC | 0.000000 USDC | 0.007215 USDC | 0.018991 USDC (0.0175 €) | — | 3.88 | 0.159 (n=607) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.021535 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0174 €) | -0.000002 WETH | 3.85 | 0.159 (n=607) | REJECTED | sim_below_estimate(901946496553<11449691792594), simulated_net_nonpositive, p_lower_below_threshold(0.16<0.75) |
| 53475911 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000911 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0157 €) | — | 2.42 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53475911 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 74.605229 USDC | 0.024220 USDC | 0.000000 USDC | 0.007227 USDC | 0.016993 USDC (0.0156 €) | 0.016993 USDC | 2.28 | 0.185 (n=853) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53474568 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 52.765461 USDC | 0.023825 USDC | 0.000000 USDC | 0.007215 USDC | 0.016610 USDC (0.0153 €) | — | 3.15 | 0.159 (n=607) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 4923 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
