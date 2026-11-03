# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T06:16:04+00:00 ; durée 257.79 min ; blocs 53440871 → 53448604 (7582 vus)

## Connexion
- Requêtes RPC : 87522 ; erreurs : 75 ; latence p50/p95 : 271.1/1,913.0 ms
- Rafraîchissements d'état : 7582 ; âge des données au dernier bloc : 2.86 s ; changements de frais LP observés (pools à frais dynamiques) : 8111
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 55428 ; cycles déclenchés par événement : 7815 ; avance médiane sur le rafraîchissement multicall : 496 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,245.02 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 285 jetons, 18224 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 202, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 308, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2253.967555, 'cbBTC': 77042.637438, 'AERO': 0.602257}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,586,252 | 2,245.018077 | 53448605 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,095,632 | 0.029349 | 53448605 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,050,037 | 0.029314 | 53448605 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,950,679 | 0.000013 | 53448605 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,827,803 | 2,241.905991 | 53448605 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,531,340 | 104.834843 | 53448605 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,503,710 | 0.001565 | 53448605 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,339,796 | 1.667687 | 53448605 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,768,058 | 0.029360 | 53448605 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,141,302 | 2,242.521737 | 53448605 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,024,549 | 0.999878 | 53448605 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,895,251 | 2,242.606146 | 53448605 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,455,454 | 39,504.393458 | 53448605 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,677,116 | 0.029323 | 53448605 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,146,121 | 1,109,431.730697 | 53448605 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,024,511 | 0.000013 | 53448605 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2700 | 1,978,872 | 104.804925 | 53448605 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,757,009 | 0.018136 | 53448605 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,653,779 | 0.000000 | 53448605 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,633,822 | 0.000013 | 53448605 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,241 | 1.436173 | 53448605 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,536,529 | 0.000013 | 53448605 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,523,444 | 443.830794 | 53448605 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,494,173 | 2,245.245554 | 53448605 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,013 | 0.822541 | 53448605 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,377,416 | 3,737.269426 | 53448605 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,346,897 | 2,245.633183 | 53448605 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,305,062 | 2,241.995277 | 53448605 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,274,490 | 0.004956 | 53448605 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,268,626 | 15,116.875288 | 53448605 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,253,774 | 0.000013 | 53448605 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,164,539 | 71.652617 | 53448605 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,348 | 37,666,443.185126 | 53448605 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,041,150 | 542,355.496536 | 53448605 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,004,694 | 0.000000 | 53448605 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 997,853 | 22,613,379.746184 | 53448605 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 976,142 | 20.333876 | 53448605 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 952,465 | 84,754.067292 | 53448605 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 921,376 | 2,257.234778 | 53448605 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 911,584 | 1,265,256.912781 | 53448605 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 907,603 | 104.470378 | 53448605 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 898,612 | 1,060.208782 | 53448605 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 883,727 | 80.160700 | 53448605 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,279 | 0.000553 | 53448605 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 853,933 | 0.046670 | 53448605 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 821,060 | 3,725.146765 | 53448605 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4525 | 811,315 | 20.415766 | 53448605 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 783,568 | 0.054922 | 53448605 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 762,097 | 0.798978 | 53448605 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 721,427 | 0.574782 | 53448605 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 714,464 | 0.000258 | 53448605 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 707,899 | 4,755,716.516617 | 53448605 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 659,972 | 0.547712 | 53448605 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 659,375 | 146,340.933100 | 53448605 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 650,702 | 2.337947 | 53448605 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 649,682 | 0.000008 | 53448605 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2159 | 640,209 | 542,263.546291 | 53448605 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 602,996 | 0.914848 | 53448605 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,817 | 0.086887 | 53448605 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 546,164 | 0.036701 | 53448605 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 15396 ; routes examinées : 280576704 ; candidats optimisés : 753058 ; net attendu > 0 : 471 ; dernier cycle 280.8 ms
- Rejets (moteur) : {'spread_below_threshold': 276345316, 'liquidity_below_min': 3417186, 'negative_expected_net': 752587, 'unquotable': 40794, 'borrow_bound_too_small': 15384, 'pool_quarantined': 4194, 'cycle_budget_exhausted': 772}
- Enregistrements de la session : 753058 ; net attendu > 0 : 471 ; simulés (eth_call de la vraie tx) : 21 (ok 4, échec 17) ; étiquettes ghost N+1 : 0/20 positives
- Décisions : {'REJECTED': 753058} ; motifs de rejet : {'below_safety_margin': 396, 'negative_expected_net': 752587, 'p_lower_below_threshold': 428, 'reliability_not_demonstrated': 43, 'simulation_failed': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53447168 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.187611 WETH | 0.000429 WETH | 0.000000 WETH | 0.000003 WETH | 0.000426 WETH (0.8821 €) | 0.000426 WETH | 22.71 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 421.563181 USDC | 0.964857 USDC | 0.000000 USDC | 0.006793 USDC | 0.958064 USDC (0.8814 €) | — | 22.73 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.184543 WETH | 0.000421 WETH | 0.000000 WETH | 0.000003 WETH | 0.000418 WETH (0.8650 €) | 0.000418 WETH | 22.63 | 0.013 (n=62) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 414.824989 USDC | 0.946134 USDC | 0.000000 USDC | 0.006793 USDC | 0.939341 USDC (0.8642 €) | — | 22.64 | 0.013 (n=62) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53447168 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.184716 WETH | 0.000415 WETH | 0.000000 WETH | 0.000003 WETH | 0.000412 WETH (0.8528 €) | 0.000412 WETH | 22.30 | 0.013 (n=62) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 415.298544 USDC | 0.933293 USDC | 0.000000 USDC | 0.007134 USDC | 0.926159 USDC (0.8521 €) | — | 22.30 | 0.013 (n=62) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53447168 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.183725 WETH | 0.000410 WETH | 0.000000 WETH | 0.000003 WETH | 0.000407 WETH (0.8427 €) | — | 22.15 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 413.163149 USDC | 0.921998 USDC | 0.000000 USDC | 0.006793 USDC | 0.915205 USDC (0.8420 €) | — | 22.15 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.177387 WETH | 0.000405 WETH | 0.000000 WETH | 0.000003 WETH | 0.000402 WETH (0.8334 €) | — | 22.69 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 398.360297 USDC | 0.911662 USDC | 0.000000 USDC | 0.006793 USDC | 0.904869 USDC (0.8325 €) | — | 22.71 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | WETH→[aerodrome]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.151282 WETH | 0.000352 WETH | 0.000000 WETH | 0.000003 WETH | 0.000349 WETH (0.7234 €) | — | 23.09 | 0.013 (n=62) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 339.448284 USDC | 0.791148 USDC | 0.000000 USDC | 0.006140 USDC | 0.785008 USDC (0.7222 €) | — | 23.13 | 0.013 (n=62) | REJECTED | p_lower_below_threshold(0.01<0.75) |
| 53447168 | WETH→[sushiswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.111339 WETH | 0.000248 WETH | 0.000000 WETH | 0.000003 WETH | 0.000246 WETH (0.5086 €) | — | 22.06 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 249.664863 USDC | 0.557758 USDC | 0.000000 USDC | 0.006451 USDC | 0.551307 USDC (0.5072 €) | — | 22.08 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | WETH→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.137416 WETH | 0.000223 WETH | 0.000000 WETH | 0.000002 WETH | 0.000221 WETH (0.4572 €) | — | 16.07 | 0.000 (n=74) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53447168 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.095876 WETH | 0.000221 WETH | 0.000000 WETH | 0.000003 WETH | 0.000218 WETH (0.4518 €) | — | 22.76 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 214.936295 USDC | 0.496024 USDC | 0.000000 USDC | 0.006451 USDC | 0.489573 USDC (0.4504 €) | — | 22.78 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53444910 | WETH→[aerodrome]→MOR→[uniswap_v3]→WETH | 0.027022 WETH | 0.000160 WETH | 0.000000 WETH | 0.000002 WETH | 0.000158 WETH (0.3261 €) | — | 58.33 | 0.001 (n=15) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53447168 | WETH→[uniswap_v3]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.096408 WETH | 0.000112 WETH | 0.000000 WETH | 0.000003 WETH | 0.000109 WETH (0.2258 €) | — | 11.31 | 0.137 (n=38) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 215.921118 USDC | 0.251085 USDC | 0.000000 USDC | 0.006451 USDC | 0.244634 USDC (0.2251 €) | — | 11.33 | 0.137 (n=38) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53447168 | WETH→[uniswap_v2]→USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.079665 WETH | 0.000095 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.1922 €) | — | 11.65 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53447168 | USDC→[aerodrome]→AERO→[pancakeswap_v3]→WETH→[uniswap_v2]→USDC | 178.528913 USDC | 0.213883 USDC | 0.000000 USDC | 0.005752 USDC | 0.208131 USDC (0.1915 €) | — | 11.66 | 0.002 (n=3) | REJECTED | reliability_not_demonstrated |
| 53447168 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.023100 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1834 €) | — | 38.35 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | WETH→[uniswap_v3]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.025084 WETH | 0.000091 WETH | 0.000000 WETH | 0.000003 WETH | 0.000088 WETH (0.1816 €) | — | 34.96 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |
| 53447168 | WETH→[aerodrome_slipstream]→VIRTUAL→[aerodrome]→AERO→[pancakeswap_v3]→WETH | 0.024963 WETH | 0.000089 WETH | 0.000000 WETH | 0.000003 WETH | 0.000086 WETH (0.1790 €) | — | 34.64 | 0.064 (n=13) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4797 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
