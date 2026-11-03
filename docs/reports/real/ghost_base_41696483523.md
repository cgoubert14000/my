# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T22:57:30+00:00 ; durée 248.04 min ; blocs 53471207 → 53478648 (7258 vus)

## Connexion
- Requêtes RPC : 86604 ; erreurs : 808 ; latence p50/p95 : 129.3/1,877.4 ms
- Rafraîchissements d'état : 7259 ; âge des données au dernier bloc : 1.56 s ; changements de frais LP observés (pools à frais dynamiques) : 6329
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 63653 ; cycles déclenchés par événement : 6863 ; avance médiane sur le rafraîchissement multicall : 364 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,291.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107 (quarantaine 1), aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 1 — aerodrome_slipstream:USDC/PLAY@0xF2c832: simulation failed ×5 (model/chain mismatch) — until block 53478887

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,986,210 | 2,291.025124 | 53478648 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,774,047 | 0.029462 | 53478648 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,215,294 | 0.029450 | 53478648 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,074,969 | 0.000013 | 53478648 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,058,503 | 2,290.887189 | 53478648 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,808,723 | 100.894513 | 53478648 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,626,253 | 0.001572 | 53478648 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,408,318 | 1.579715 | 53478648 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,838,531 | 0.029451 | 53478648 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,192,071 | 2,291.258798 | 53478648 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,090,930 | 0.999913 | 53478648 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,879,513 | 2,291.353403 | 53478648 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,454,349 | 41,166.434262 | 53478648 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,690,269 | 0.029441 | 53478648 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,175,876 | 1,123,985.241900 | 53478648 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,140,418 | 100.850296 | 53478648 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,816,594 | 0.000013 | 53478648 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,739,304 | 0.017818 | 53478648 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,682,711 | 0.000000 | 53478648 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,628,477 | 0.000013 | 53478648 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,560,329 | 438.762250 | 53478648 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,556,267 | 0.000013 | 53478648 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53478648 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,546,114 | 0.006173 | 53478648 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | WETH/USDC | 3000 | 1,509,539 | 2,292.127145 | 53478648 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,800 | 0.821850 | 53478648 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,427,655 | 3,620.736164 | 53478648 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,342,292 | 2,295.694487 | 53478648 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,339,669 | 2,290.881903 | 53478648 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,298,516 | 14,908.242338 | 53478648 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,637 | 72.384430 | 53478648 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,125,674 | 36,934,354.391659 | 53478648 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,062,597 | 0.000000 | 53478648 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,060,241 | 545,632.690586 | 53478648 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,036,525 | 21,950,664.012046 | 53478648 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 998,148 | 19.051710 | 53478648 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 959,313 | 101.018638 | 53478648 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 956,840 | 87,458.574859 | 53478648 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 946,756 | 1,061.065001 | 53478648 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 943,378 | 0.000013 | 53478648 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 936,315 | 71.409532 | 53478648 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 929,102 | 2,282.122456 | 53478648 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 926,757 | 1,274,812.370254 | 53478648 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 893,310 | 0.044031 | 53478648 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 881,824 | 0.000555 | 53478648 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 848,377 | 3,641.184916 | 53478648 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 827,108 | 19.846237 | 53478648 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 797,987 | 0.057068 | 53478648 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 777,636 | 0.799140 | 53478648 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,816 | 0.593828 | 53478648 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 727,955 | 0.000257 | 53478648 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 720,993 | 4,775,008.146905 | 53478648 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 674,067 | 0.000008 | 53478648 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 669,903 | 147,668.300856 | 53478648 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 658,233 | 2.368619 | 53478648 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 654,495 | 0.538899 | 53478648 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 651,312 | 546,993.939174 | 53478648 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 615,398 | 0.914716 | 53478648 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 588,882 | 0.087543 | 53478648 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 567,069 | 0.038818 | 53478648 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 14121 ; routes examinées : 274625208 ; candidats optimisés : 742617 ; net attendu > 0 : 589 ; dernier cycle 202.9 ms
- Rejets (moteur) : {'spread_below_threshold': 270599487, 'liquidity_below_min': 3237282, 'negative_expected_net': 742028, 'unquotable': 28220, 'borrow_bound_too_small': 14110, 'pool_quarantined': 2940, 'cycle_budget_exhausted': 552}
- Enregistrements de la session : 742617 ; net attendu > 0 : 589 ; simulés (eth_call de la vraie tx) : 35 (ok 18, échec 17) ; étiquettes ghost N+1 : 0/27 positives
- Décisions : {'REJECTED': 742617} ; motifs de rejet : {'below_safety_margin': 526, 'negative_expected_net': 742028, 'p_lower_below_threshold': 576, 'reliability_not_demonstrated': 13, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 17, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53476657 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 137.053961 USDC | 3.316241 USDC | 0.000000 USDC | 0.004826 USDC | 3.311415 USDC (3.0465 €) | — | 241.61 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53477925 | WETH→[uniswap_v3]→CLANKER→[aerodrome_slipstream]→WETH | 0.006782 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1774 €) | 0.000084 WETH | 124.12 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53477925 | WETH→[uniswap_v3]→CLANKER→[aerodrome_slipstream]→WETH | 0.006782 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1774 €) | 0.000084 WETH | 124.12 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53472395 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.026252 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1137 €) | — | 20.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472362 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.020014 WETH | 0.000033 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0642 €) | — | 15.21 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53476424 | WETH→[aerodrome_slipstream]→ZRO→[uniswap_v3]→WETH | 0.010639 WETH | 0.000024 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0451 €) | — | 20.14 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53477292 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 46.827655 USDC | 0.053258 USDC | 0.000000 USDC | 0.005143 USDC | 0.048115 USDC (0.0443 €) | — | 10.27 | 0.000 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53476455 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 771.228037 USDC | 0.051205 USDC | 0.000000 USDC | 0.005140 USDC | 0.046065 USDC (0.0424 €) | — | 0.60 | 0.034 (n=197) | REJECTED | below_safety_margin(46065<154245), p_lower_below_threshold(0.03<0.75) |
| 53476455 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010013 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0422 €) | — | 0.59 | 0.034 (n=197) | REJECTED | below_safety_margin(59<200), p_lower_below_threshold(0.03<0.75) |
| 53477395 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001206 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0300 €) | 0.000000 cbBTC | 3.48 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53477395 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001206 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0300 €) | 0.000000 cbBTC | 3.48 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53477395 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 99.504389 USDC | 0.039456 USDC | 0.000000 USDC | 0.006883 USDC | 0.032573 USDC (0.0300 €) | 0.032573 USDC | 3.27 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53477395 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 99.504389 USDC | 0.039456 USDC | 0.000000 USDC | 0.006883 USDC | 0.032573 USDC (0.0300 €) | 0.032573 USDC | 3.27 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
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

## Fiabilité et décision
- Observations ghost : 4932 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.161 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
