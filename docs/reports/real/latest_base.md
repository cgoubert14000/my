# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T22:08:56+00:00 ; durée 114.68 min ; blocs 54028370 → 54062740 (6587 vus)

## Connexion
- Requêtes RPC : 82543 ; erreurs : 0 ; latence p50/p95 : 234.0/1,529.4 ms
- Rafraîchissements d'état : 6587 ; âge des données au dernier bloc : 8.55 s ; changements de frais LP observés (pools à frais dynamiques) : 2697
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6896 ; cycles déclenchés par événement : 2806 ; avance médiane sur le rafraîchissement multicall : 497 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,244.20 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 282 jetons, 17936 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3742 (énumérés 299, par paires 0), mesurés 485, sous le plancher de 10000.0 $ : 3 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2228.731074, 'cbBTC': 75812.648558, 'AERO': 0.606832}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,634,659 | 2,244.204206 | 54062765 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,815,338 | 0.029494 | 54062765 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,412,735 | 0.000013 | 54062765 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,183,437 | 0.029484 | 54062765 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,028,726 | 2,240.244242 | 54062765 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,425,570 | 106.741769 | 54062765 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,451,625 | 0.001556 | 54062765 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,930,637 | 1.616377 | 54062765 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,755,758 | 0.029481 | 54062765 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,170,927 | 2,239.915374 | 54062765 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,010,384 | 0.998508 | 54062765 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,346,519 | 42,087.524369 | 54062765 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,210,137 | 2,240.028609 | 54062765 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2510 | 2,566,774 | 0.029497 | 54062765 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,091,745 | 1,166,818.518415 | 54062765 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,748,377 | 0.006996 | 54062765 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,739,842 | 0.000013 | 54062765 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,665,035 | 0.000000 | 54062765 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,659,414 | 0.000013 | 54062765 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,620,695 | 0.016197 | 54062765 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54062765 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,541,891 | 0.000013 | 54062765 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,541,234 | 427.997941 | 54062765 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,358 | 0.818979 | 54062765 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,405,910 | 3,627.256758 | 54062765 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,327,585 | 2,244.009387 | 54062765 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,688 | 2,244.498143 | 54062765 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,286,109 | 14,511.898095 | 54062765 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,169,090 | 2,240.529362 | 54062765 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,122,706 | 77.091623 | 54062765 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,103,327 | 36,916,209.311164 | 54062765 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,055,248 | 106.727256 | 54062765 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,030,812 | 554,474.428336 | 54062765 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,024,847 | 0.000000 | 54062765 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,000,350 | 22,508,235.864785 | 54062765 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 976,142 | 20.334522 | 54062765 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 947,379 | 1,056.046303 | 54062765 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 936,995 | 2,228.788696 | 54062765 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 927,677 | 0.000013 | 54062765 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 921,109 | 73.856041 | 54062765 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 886,973 | 97,656.617423 | 54062765 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 841,552 | 0.000527 | 54062765 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 814,785 | 0.047662 | 54062765 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 808,707 | 3,653.941789 | 54062765 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4550 | 805,606 | 20.689431 | 54062765 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,726 | 0.056552 | 54062765 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 761,338 | 0.799699 | 54062765 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 726,055 | 0.572110 | 54062765 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 698,588 | 4,883,566.395016 | 54062765 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 691,308 | 0.000257 | 54062765 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 666,439 | 0.556929 | 54062765 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 664,918 | 143,993.853267 | 54062765 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 664,298 | 0.000008 | 54062765 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 633,311 | 555,743.443553 | 54062765 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 589,879 | 2.472072 | 54062765 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 587,007 | 0.040795 | 54062765 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 530,656 | 1,056.501319 | 54062765 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 529,452 | 871,096.873719 | 54062765 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 524,908 | 0.078610 | 54062765 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 520,884 | 2,239.977828 | 54062765 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 9392 ; routes examinées : 168454912 ; candidats optimisés : 515745 ; net attendu > 0 : 171 ; dernier cycle 104.0 ms
- Rejets (moteur) : {'spread_below_threshold': 165556078, 'liquidity_below_min': 2357496, 'negative_expected_net': 515574, 'pool_quarantined': 15484, 'borrow_bound_too_small': 9388, 'cycle_budget_exhausted': 721}
- Enregistrements de la session : 515745 ; net attendu > 0 : 171 ; simulés (eth_call de la vraie tx) : 25 (ok 6, échec 19) ; étiquettes ghost N+1 : 5/9 positives
- Décisions : {'REJECTED': 515745} ; motifs de rejet : {'below_safety_margin': 145, 'negative_expected_net': 515574, 'p_lower_below_threshold': 168, 'price_impact': 15, 'reliability_not_demonstrated': 3, 'simulation_failed': 19, 'stale_data': 25}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54060684 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 837.885496 USDC | 0.111051 USDC | 0.000000 USDC | 0.005054 USDC | 0.105997 USDC (0.0975 €) | — | 1.27 | 0.047 (n=247) | REJECTED | below_safety_margin(105997<167577), p_lower_below_threshold(0.05<0.75) |
| 54060684 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.374447 WETH | 0.000050 WETH | 0.000000 WETH | 0.000002 WETH | 0.000047 WETH (0.0972 €) | — | 1.26 | 0.047 (n=247) | REJECTED | below_safety_margin(47277268623202<74889389706557), p_lower_below_threshold(0.05<0.75) |
| 54060684 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 757.927748 USDC | 0.070574 USDC | 0.000000 USDC | 0.006764 USDC | 0.063810 USDC (0.0587 €) | — | 0.84 | 0.029 (n=28) | REJECTED | below_safety_margin(63810<151585), reliability_not_demonstrated |
| 54060684 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008755 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0585 €) | — | 0.96 | 0.029 (n=28) | REJECTED | below_safety_margin(84<175), reliability_not_demonstrated |
| 54060684 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.329385 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0581 €) | — | 0.86 | 0.029 (n=28) | REJECTED | below_safety_margin(28267304274076<65877091333329), reliability_not_demonstrated |
| 54057958 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 68.807723 USDC | 0.056511 USDC | 0.000000 USDC | 0.005004 USDC | 0.051507 USDC (0.0474 €) | — | 7.49 | 0.026 (n=319) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 54060684 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 304.872182 USDC | 0.038933 USDC | 0.000000 USDC | 0.005395 USDC | 0.033538 USDC (0.0309 €) | — | 1.10 | 0.053 (n=82) | REJECTED | below_safety_margin(33538<60974), p_lower_below_threshold(0.05<0.75) |
| 54060684 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.136291 WETH | 0.000017 WETH | 0.000000 WETH | 0.000002 WETH | 0.000015 WETH (0.0308 €) | — | 1.10 | 0.053 (n=82) | REJECTED | below_safety_margin(14951957098203<27258137402606), p_lower_below_threshold(0.05<0.75) |
| 54060684 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 242.850703 USDC | 0.021390 USDC | 0.000000 USDC | 0.006764 USDC | 0.014626 USDC (0.0135 €) | — | 0.60 | 0.171 (n=1029) | REJECTED | below_safety_margin(14626<48570), p_lower_below_threshold(0.17<0.75) |
| 54060684 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0132 €) | — | 0.63 | 0.171 (n=1029) | REJECTED | below_safety_margin(19<60), p_lower_below_threshold(0.17<0.75) |
| 54060684 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.102975 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0130 €) | — | 0.61 | 0.171 (n=1029) | REJECTED | below_safety_margin(6327976085958<20595093319702), p_lower_below_threshold(0.17<0.75) |
| 54061009 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 54.641064 USDC | 0.014553 USDC | 0.000000 USDC | 0.007085 USDC | 0.007468 USDC (0.0069 €) | — | 1.37 | 0.171 (n=1029) | REJECTED | below_safety_margin(7468<10928), stale_data(4456ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 54061009 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.024444 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0068 €) | — | 1.35 | 0.171 (n=1029) | REJECTED | below_safety_margin(3311770877831<4888700126205), stale_data(4451ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 54061009 | USDC→[uniswap_v3]→EURC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 52.789078 USDC | 0.013445 USDC | 0.000000 USDC | 0.007085 USDC | 0.006360 USDC (0.0059 €) | — | 1.20 | 0.171 (n=1029) | REJECTED | below_safety_margin(6360<10557), stale_data(4475ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 54061009 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→EURC→[pancakeswap_v3]→WETH | 0.023738 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0058 €) | — | 1.19 | 0.171 (n=1029) | REJECTED | below_safety_margin(2819339674783<4747581149832), stale_data(4470ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 54060971 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 53.398462 USDC | 0.013024 USDC | 0.000000 USDC | 0.006790 USDC | 0.006234 USDC (0.0057 €) | — | 1.17 | 0.237 (n=405) | REJECTED | below_safety_margin(6234<10679), p_lower_below_threshold(0.24<0.75) |
| 54060972 | USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 53.398462 USDC | 0.013024 USDC | 0.000000 USDC | 0.006790 USDC | 0.006234 USDC (0.0057 €) | — | 1.17 | 0.237 (n=405) | REJECTED | below_safety_margin(6234<10679), p_lower_below_threshold(0.24<0.75) |
| 54060971 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.023878 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 1.16 | 0.237 (n=405) | REJECTED | below_safety_margin(2767591186571<4775627268477), p_lower_below_threshold(0.24<0.75) |
| 54060972 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→LCAP→[aerodrome_slipstream]→WETH | 0.023878 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 1.16 | 0.237 (n=405) | REJECTED | below_safety_margin(2767591186571<4775627268477), p_lower_below_threshold(0.24<0.75) |
| 54042831 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.102166 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(2470642400570<20433118273996), p_lower_below_threshold(0.05<0.75) |
| 54042832 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.102166 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(2470642400570<20433118273996), p_lower_below_threshold(0.05<0.75) |
| 54042831 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 226.836687 USDC | 0.010504 USDC | 0.000000 USDC | 0.005007 USDC | 0.005497 USDC (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(5497<45367), p_lower_below_threshold(0.05<0.75) |
| 54042832 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 226.836687 USDC | 0.010504 USDC | 0.000000 USDC | 0.005007 USDC | 0.005497 USDC (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(5497<45367), p_lower_below_threshold(0.05<0.75) |
| 54060971 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 51.178301 USDC | 0.012072 USDC | 0.000000 USDC | 0.006790 USDC | 0.005282 USDC (0.0049 €) | — | 1.03 | 0.237 (n=405) | REJECTED | below_safety_margin(5282<10235), p_lower_below_threshold(0.24<0.75) |
| 54060972 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 51.178301 USDC | 0.012072 USDC | 0.000000 USDC | 0.006790 USDC | 0.005282 USDC (0.0049 €) | — | 1.03 | 0.237 (n=405) | REJECTED | below_safety_margin(5282<10235), p_lower_below_threshold(0.24<0.75) |

## Fiabilité et décision
- Observations ghost : 5906 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
