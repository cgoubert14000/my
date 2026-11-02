# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T15:02:27+00:00 ; durée 18.27 min ; blocs 53420649 → 53421198 (548 vus)

## Connexion
- Requêtes RPC : 6506 ; erreurs : 0 ; latence p50/p95 : 94.5/1,173.5 ms
- Rafraîchissements d'état : 548 ; âge des données au dernier bloc : 4.14 s ; changements de frais LP observés (pools à frais dynamiques) : 1060
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8748 ; cycles déclenchés par événement : 740 ; avance médiane sur le rafraîchissement multicall : 421 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,287.70 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18656 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2287.70349, 'cbBTC': 77760.832568, 'AERO': 0.623017}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,659,934 | 2,287.702240 | 53421199 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,380,117 | 0.029405 | 53421199 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,282,692 | 0.000013 | 53421199 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,212,136 | 0.029363 | 53421199 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,964,488 | 2,283.960725 | 53421199 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,736,027 | 103.174772 | 53421199 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,656,394 | 0.001585 | 53421199 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,470,431 | 1.606057 | 53421199 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,793,289 | 0.029398 | 53421199 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,092,599 | 0.999940 | 53421199 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 654 | 4,055,041 | 2,284.036646 | 53421199 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,993,872 | 2,283.785734 | 53421199 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,560,483 | 38,637.429055 | 53421199 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,673,491 | 0.029376 | 53421199 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,349,079 | 103.211774 | 53421199 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,237,866 | 1,059,497.581810 | 53421199 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,115,984 | 0.000013 | 53421199 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,745,770 | 0.017915 | 53421199 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,701,285 | 0.000000 | 53421199 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,664,584 | 0.000013 | 53421199 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,575,005 | 0.000013 | 53421199 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,555,996 | 440.397909 | 53421199 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,291 | 2,287.432671 | 53421199 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53421199 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,373 | 0.823555 | 53421199 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,422,997 | 3,672.038434 | 53421199 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,360,108 | 2,288.658952 | 53421199 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,327,499 | 0.005089 | 53421199 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,323,526 | 2,283.958672 | 53421199 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,302,775 | 0.000013 | 53421199 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,295,610 | 14,962.689472 | 53421199 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,133 | 71.090555 | 53421199 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,107,141 | 38,432,077.980862 | 53421199 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,067,499 | 532,789.443667 | 53421199 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,062,321 | 0.000000 | 53421199 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,010,106 | 22,862,394.515506 | 53421199 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 987,454 | 81,898.664306 | 53421199 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 985,073 | 19.806643 | 53421199 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 950,387 | 1,208,732.436207 | 53421199 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 934,361 | 102.727177 | 53421199 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 926,594 | 2,291.133952 | 53421199 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 925,882 | 1,036.632263 | 53421199 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 905,509 | 76.350330 | 53421199 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 896,792 | 0.045169 | 53421199 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 871,990 | 0.000544 | 53421199 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 860,338 | 3,659.352431 | 53421199 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4555 | 827,933 | 19.806604 | 53421199 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,501 | 0.056849 | 53421199 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 775,179 | 0.801881 | 53421199 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,081 | 0.000258 | 53421199 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,530 | 0.585565 | 53421199 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 706,560 | 4,955,999.570793 | 53421199 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 691,070 | 138,314.377097 | 53421199 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 681,397 | 0.000008 | 53421199 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 671,808 | 0.571996 | 53421199 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 662,819 | 2.340905 | 53421199 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 658,476 | 535,027.176112 | 53421199 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,362 | 0.915143 | 53421199 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 593,639 | 0.088671 | 53421199 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,930 | 0.037829 | 53421199 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 1287 ; routes examinées : 24010272 ; candidats optimisés : 92442 ; net attendu > 0 : 320 ; dernier cycle 155.4 ms
- Rejets (moteur) : {'spread_below_threshold': 23212169, 'liquidity_below_min': 382418, 'pool_quarantined': 314352, 'negative_expected_net': 92122, 'unquotable': 7604, 'borrow_bound_too_small': 1287}
- Enregistrements de la session : 92442 ; net attendu > 0 : 320 ; simulés (eth_call de la vraie tx) : 16 (ok 9, échec 7) ; étiquettes ghost N+1 : 3/10 positives
- Décisions : {'REJECTED': 92442} ; motifs de rejet : {'below_safety_margin': 230, 'negative_expected_net': 92122, 'p_lower_below_threshold': 284, 'reliability_not_demonstrated': 36, 'simulation_failed': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53420906 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.015164 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1868 €) | — | 1.72 | 0.039 (n=170) | REJECTED | below_safety_margin(261<303), p_lower_below_threshold(0.04<0.75) |
| 53420906 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 1,239.328545 USDC | 0.207693 USDC | 0.000000 USDC | 0.005181 USDC | 0.202512 USDC (0.1863 €) | — | 1.63 | 0.039 (n=170) | REJECTED | below_safety_margin(202512<247865), p_lower_below_threshold(0.04<0.75) |
| 53420792 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 176.248588 USDC | 0.115731 USDC | 0.000000 USDC | 0.006923 USDC | 0.108808 USDC (0.1001 €) | — | 6.17 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.077017 WETH | 0.000051 WETH | 0.000000 WETH | 0.000003 WETH | 0.000048 WETH (0.1000 €) | — | 6.17 | 0.159 (n=583) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53420792 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 175.262713 USDC | 0.114709 USDC | 0.000000 USDC | 0.006923 USDC | 0.107786 USDC (0.0992 €) | — | 6.15 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.076663 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.0991 €) | — | 6.14 | 0.159 (n=583) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53420792 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 168.724427 USDC | 0.114430 USDC | 0.000000 USDC | 0.007270 USDC | 0.107160 USDC (0.0986 €) | — | 6.35 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.073869 WETH | 0.000050 WETH | 0.000000 WETH | 0.000003 WETH | 0.000047 WETH (0.0985 €) | — | 6.34 | 0.159 (n=583) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53420792 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 153.879668 USDC | 0.095842 USDC | 0.000000 USDC | 0.007270 USDC | 0.088572 USDC (0.0815 €) | — | 5.76 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.067387 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000039 WETH (0.0814 €) | — | 5.74 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 148.846908 USDC | 0.095583 USDC | 0.000000 USDC | 0.007617 USDC | 0.087966 USDC (0.0809 €) | — | 5.91 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.065098 WETH | 0.000042 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0809 €) | — | 5.90 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 153.704296 USDC | 0.094956 USDC | 0.000000 USDC | 0.007270 USDC | 0.087686 USDC (0.0807 €) | — | 5.70 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.067199 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0806 €) | — | 5.70 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 119.046001 USDC | 0.089091 USDC | 0.000000 USDC | 0.006923 USDC | 0.082168 USDC (0.0756 €) | — | 6.90 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.052130 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0755 €) | — | 6.88 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 108.181874 USDC | 0.077157 USDC | 0.000000 USDC | 0.007270 USDC | 0.069887 USDC (0.0643 €) | — | 6.46 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.047365 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0642 €) | — | 6.44 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420906 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.008175 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0623 €) | — | 1.06 | 0.015 (n=19) | REJECTED | below_safety_margin(87<163), reliability_not_demonstrated |
| 53420906 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.285661 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0620 €) | — | 1.03 | 0.015 (n=19) | REJECTED | below_safety_margin(29436209569379<57132218264996), reliability_not_demonstrated |
| 53420906 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 694.865647 USDC | 0.073839 USDC | 0.000000 USDC | 0.006928 USDC | 0.066911 USDC (0.0616 €) | — | 0.96 | 0.015 (n=19) | REJECTED | below_safety_margin(66911<138973), reliability_not_demonstrated |
| 53420792 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC | 137.527989 USDC | 0.070619 USDC | 0.000000 USDC | 0.006923 USDC | 0.063696 USDC (0.0586 €) | — | 4.63 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420792 | WETH→[aerodrome_slipstream]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.060328 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0585 €) | — | 4.61 | 0.159 (n=583) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53420906 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.286447 WETH | 0.000029 WETH | 0.000000 WETH | 0.000002 WETH | 0.000027 WETH (0.0564 €) | — | 0.93 | 0.001 (n=7) | REJECTED | below_safety_margin(26778323994175<57289380552324), reliability_not_demonstrated |
| 53420906 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 652.297454 USDC | 0.066339 USDC | 0.000000 USDC | 0.005181 USDC | 0.061158 USDC (0.0563 €) | — | 0.94 | 0.001 (n=7) | REJECTED | below_safety_margin(61158<130459), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4651 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
