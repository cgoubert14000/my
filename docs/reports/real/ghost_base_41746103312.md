# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T03:10:30+00:00 ; durée 160.97 min ; blocs 53481408 → 53486238 (4734 vus)

## Connexion
- Requêtes RPC : 55646 ; erreurs : 145 ; latence p50/p95 : 321.5/995.7 ms
- Rafraîchissements d'état : 4734 ; âge des données au dernier bloc : 2.65 s ; changements de frais LP observés (pools à frais dynamiques) : 10723
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 70313 ; cycles déclenchés par événement : 4917 ; avance médiane sur le rafraîchissement multicall : 1,065 ms
- Gaz : base fee 0.007648 gwei ; prix ETH (pool le plus profond) : 2,229.54 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 282 jetons, 19430 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 105, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3703 (énumérés 305, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2264.542979, 'cbBTC': 77119.048638, 'AERO': 0.629628}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,410,690 | 2,229.543146 | 53486239 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,365,523 | 0.029428 | 53486238 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,986,531 | 0.029502 | 53486238 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,884,902 | 0.000013 | 53486238 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,896,697 | 2,228.925129 | 53486238 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,483,235 | 103.917136 | 53486238 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,428,870 | 0.001558 | 53486238 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,324,106 | 1.624991 | 53486238 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,687,078 | 0.029425 | 53486238 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,138,744 | 2,229.817145 | 53486238 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,985,772 | 0.999904 | 53486238 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,792,850 | 2,229.792113 | 53486238 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,364,475 | 41,097.255574 | 53486238 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,617,298 | 0.029431 | 53486238 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,107,030 | 1,135,166.341200 | 53486238 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2754 | 2,048,928 | 103.954029 | 53486238 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,784,542 | 0.000013 | 53486239 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,711,330 | 0.017325 | 53486238 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,655,746 | 0.006903 | 53486238 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,636,273 | 0.000000 | 53486238 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,591,360 | 0.000013 | 53486239 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53486238 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,521,142 | 0.000013 | 53486238 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,514,661 | 442.484592 | 53486238 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,489,226 | 2,230.851659 | 53486238 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,579 | 0.818329 | 53486239 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,388,880 | 3,623.352377 | 53486238 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,328,822 | 2,228.996443 | 53486238 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,324,151 | 2,230.546095 | 53486238 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,259,996 | 15,052.570066 | 53486238 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,309 | 72.425481 | 53486238 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,057 | 36,969,258.567437 | 53486238 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,023,592 | 556,784.932822 | 53486238 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,013,800 | 0.000000 | 53486238 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,002,801 | 22,173,343.364628 | 53486238 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 988,924 | 19.570338 | 53486238 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 938,710 | 86,057.426484 | 53486238 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 936,179 | 1,042.517206 | 53486238 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 927,420 | 103.218253 | 53486238 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 925,917 | 73.022431 | 53486238 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 923,880 | 0.000013 | 53486238 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 920,225 | 2,246.085611 | 53486238 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 904,052 | 1,268,712.501920 | 53486238 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | uXRP/WETH | 3000 | 856,231 | 0.000554 | 53486238 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 854,748 | 0.046694 | 53486238 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 824,754 | 3,609.281931 | 53486238 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4530 | 804,693 | 20.670130 | 53486238 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 783,601 | 0.054924 | 53486238 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 756,767 | 0.799140 | 53486238 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 722,078 | 0.569924 | 53486238 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 708,421 | 0.000257 | 53486238 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 692,094 | 4,907,814.301356 | 53486238 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 656,093 | 0.000008 | 53486239 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 652,317 | 0.535355 | 53486238 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 648,554 | 149,226.066592 | 53486238 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 642,677 | 2.357100 | 53486238 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 627,169 | 560,193.972084 | 53486238 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 599,108 | 0.914029 | 53486238 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 575,367 | 0.084575 | 53486238 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 550,674 | 0.037124 | 53486239 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 9650 ; routes examinées : 187499500 ; candidats optimisés : 657985 ; net attendu > 0 : 1547 ; dernier cycle 156.4 ms
- Rejets (moteur) : {'spread_below_threshold': 184046718, 'liquidity_below_min': 2781652, 'negative_expected_net': 656438, 'borrow_bound_too_small': 9623, 'cycle_budget_exhausted': 3447}
- Enregistrements de la session : 657981 ; net attendu > 0 : 1547 ; simulés (eth_call de la vraie tx) : 91 (ok 25, échec 66) ; étiquettes ghost N+1 : 15/73 positives
- Décisions : {'REJECTED': 657981} ; motifs de rejet : {'below_safety_margin': 842, 'negative_expected_net': 656434, 'p_lower_below_threshold': 1222, 'price_impact': 4, 'reliability_not_demonstrated': 325, 'sim_below_estimate': 10, 'simulated_net_nonpositive': 6, 'simulation_failed': 66, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53485970 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 2.700934 WETH | 0.003132 WETH | 0.000000 WETH | 0.000006 WETH | 0.003126 WETH (6.4400 €) | — | 11.58 | 0.099 (n=119) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53485970 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.078963 cbBTC | 0.000092 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000092 cbBTC (6.4380 €) | — | 11.66 | 0.099 (n=119) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53485970 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 6,048.740913 USDC | 7.005580 USDC | 0.000000 USDC | 0.013466 USDC | 6.992114 USDC (6.4327 €) | — | 11.56 | 0.099 (n=119) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.304813 WETH | 0.002926 WETH | 0.000000 WETH | 0.000002 WETH | 0.002924 WETH (6.0426 €) | — | 95.92 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008937 cbBTC | 0.000086 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000086 cbBTC (6.0418 €) | — | 96.36 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008685 cbBTC | 0.000084 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000084 cbBTC (5.8833 €) | — | 96.55 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.297193 WETH | 0.002849 WETH | 0.000000 WETH | 0.000003 WETH | 0.002846 WETH (5.8817 €) | — | 95.76 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53485940 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 669.262385 USDC | 6.386324 USDC | 0.000000 USDC | 0.007556 USDC | 6.378768 USDC (5.8685 €) | — | 95.31 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008637 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (5.8026 €) | — | 95.76 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.293823 WETH | 0.002810 WETH | 0.000000 WETH | 0.000003 WETH | 0.002807 WETH (5.8003 €) | — | 95.52 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53485940 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 658.335703 USDC | 6.297702 USDC | 0.000000 USDC | 0.007556 USDC | 6.290146 USDC (5.7869 €) | — | 95.55 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008542 cbBTC | 0.000082 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000082 cbBTC (5.7584 €) | — | 96.08 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.291469 WETH | 0.002788 WETH | 0.000000 WETH | 0.000004 WETH | 0.002784 WETH (5.7544 €) | — | 95.53 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 653.649759 USDC | 6.251532 USDC | 0.000000 USDC | 0.008356 USDC | 6.243176 USDC (5.7437 €) | — | 95.51 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008570 cbBTC | 0.000082 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000081 cbBTC (5.7128 €) | — | 95.02 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.293823 WETH | 0.002766 WETH | 0.000000 WETH | 0.000003 WETH | 0.002763 WETH (5.7098 €) | — | 94.03 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 661.163621 USDC | 6.201346 USDC | 0.000000 USDC | 0.007556 USDC | 6.193790 USDC (5.6983 €) | — | 93.68 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008569 cbBTC | 0.000081 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000081 cbBTC (5.6798 €) | — | 94.48 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.287303 WETH | 0.002750 WETH | 0.000000 WETH | 0.000004 WETH | 0.002746 WETH (5.6749 €) | — | 95.58 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 644.013970 USDC | 6.165153 USDC | 0.000000 USDC | 0.008356 USDC | 6.156797 USDC (5.6643 €) | — | 95.60 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008521 cbBTC | 0.000081 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000081 cbBTC (5.6609 €) | — | 94.70 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.291469 WETH | 0.002741 WETH | 0.000000 WETH | 0.000003 WETH | 0.002737 WETH (5.6573 €) | — | 93.92 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 652.325053 USDC | 6.145273 USDC | 0.000000 USDC | 0.007556 USDC | 6.137717 USDC (5.6467 €) | — | 94.09 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008557 cbBTC | 0.000080 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000080 cbBTC (5.6335 €) | — | 93.84 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.290673 WETH | 0.002728 WETH | 0.000000 WETH | 0.000003 WETH | 0.002724 WETH (5.6299 €) | — | 93.72 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 5013 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
