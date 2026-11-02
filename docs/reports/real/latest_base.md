# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T13:57:47+00:00 ; durée 289.58 min ; blocs 53410569 → 53419255 (8614 vus)

## Connexion
- Requêtes RPC : 104597 ; erreurs : 15 ; latence p50/p95 : 151.1/700.4 ms
- Rafraîchissements d'état : 8614 ; âge des données au dernier bloc : 2.15 s ; changements de frais LP observés (pools à frais dynamiques) : 8201
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 52973 ; cycles déclenchés par événement : 6741 ; avance médiane sur le rafraîchissement multicall : 853 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,290.17 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18438 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108 (quarantaine 1), aerodrome 204, pancakeswap_v3 31, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3754 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2295.27604, 'cbBTC': 78216.642548, 'AERO': 0.6263}
- Pools en quarantaine : 1 — aerodrome_slipstream:WETH/USDT@0x9785eF: simulation failed ×5 (model/chain mismatch) — until block 53419395

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,720,976 | 2,290.173571 | 53419255 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,407,083 | 0.029364 | 53419255 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,296,652 | 0.000013 | 53419255 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,221,865 | 0.029363 | 53419255 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,970,373 | 2,286.326477 | 53419255 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,757,114 | 102.841103 | 53419255 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,673,989 | 0.001585 | 53419255 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,482,200 | 1.599169 | 53419255 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,798,293 | 0.029365 | 53419255 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,102,782 | 0.999940 | 53419255 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 549 | 4,058,244 | 2,286.431390 | 53419255 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,006,098 | 2,286.765659 | 53419255 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,565,680 | 38,608.167199 | 53419255 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,678,618 | 0.029376 | 53419255 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,356,023 | 102.869105 | 53419255 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,121,668 | 1,181,275.467329 | 53419255 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 2,119,152 | 0.000013 | 53419255 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,749,818 | 0.017985 | 53419255 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,703,127 | 0.000000 | 53419255 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,667,900 | 0.000013 | 53419255 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,584,530 | 0.000013 | 53419255 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,558,814 | 439.332756 | 53419255 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,509,104 | 2,288.635762 | 53419255 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53419255 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,373 | 0.823555 | 53419255 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,427,286 | 3,660.657979 | 53419255 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,360,936 | 2,289.874799 | 53419255 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,324,106 | 2,286.956427 | 53419255 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,323,989 | 0.005089 | 53419255 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,305,025 | 0.000013 | 53419255 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,299,403 | 14,949.000330 | 53419255 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,096 | 71.095034 | 53419255 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,120,422 | 37,345,827.143251 | 53419255 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,068,649 | 532,793.888467 | 53419255 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,065,186 | 0.000000 | 53419255 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,019,136 | 22,560,368.053729 | 53419255 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 988,521 | 81,898.664306 | 53419255 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 985,475 | 19.769581 | 53419255 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 952,028 | 1,207,174.117601 | 53419255 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 937,442 | 102.491321 | 53419255 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,486 | 1,029.049148 | 53419255 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 926,961 | 2,291.133952 | 53419255 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 907,611 | 75.997032 | 53419255 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 899,686 | 0.044982 | 53419255 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 872,938 | 0.000544 | 53419255 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 862,653 | 3,659.352431 | 53419255 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 829,315 | 19.756809 | 53419255 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,631 | 0.056568 | 53419255 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 776,017 | 0.801881 | 53419255 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 732,483 | 0.000259 | 53419255 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,997 | 0.590455 | 53419255 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 706,891 | 4,962,034.097085 | 53419255 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 692,768 | 137,933.735598 | 53419255 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 683,841 | 0.000008 | 53419255 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 670,339 | 0.569624 | 53419255 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 663,535 | 2.340905 | 53419255 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 659,177 | 532,610.004929 | 53419255 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 615,026 | 0.915143 | 53419255 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 598,093 | 0.089680 | 53419255 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,918 | 0.037828 | 53419255 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 15354 ; routes examinées : 283097052 ; candidats optimisés : 1205277 ; net attendu > 0 : 18238 ; dernier cycle 161.7 ms
- Rejets (moteur) : {'spread_below_threshold': 276568204, 'liquidity_below_min': 4735099, 'negative_expected_net': 1187039, 'pool_quarantined': 465654, 'unquotable': 102248, 'borrow_bound_too_small': 15342, 'cycle_budget_exhausted': 5228}
- Enregistrements de la session : 1205277 ; net attendu > 0 : 18238 ; simulés (eth_call de la vraie tx) : 2186 (ok 2080, échec 106) ; étiquettes ghost N+1 : 173/242 positives
- Décisions : {'REJECTED': 1205277} ; motifs de rejet : {'below_safety_margin': 12069, 'negative_expected_net': 1187039, 'p_lower_below_threshold': 17326, 'reliability_not_demonstrated': 912, 'sim_below_estimate': 154, 'simulated_net_nonpositive': 42, 'simulation_failed': 106, 'stale_data': 295}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53410595 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,447.032586 USDC | 0.157806 USDC | 0.000000 USDC | 0.005510 USDC | 0.152296 USDC (0.1401 €) | — | 1.05 | 0.040 (n=168) | REJECTED | below_safety_margin(152296<289406), p_lower_below_threshold(0.04<0.75) |
| 53410595 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.630564 WETH | 0.000069 WETH | 0.000000 WETH | 0.000002 WETH | 0.000066 WETH (0.1399 €) | — | 1.05 | 0.040 (n=168) | REJECTED | below_safety_margin(66270678981474<126112801891045), p_lower_below_threshold(0.04<0.75) |
| 53418669 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 249.976022 USDC | 0.099924 USDC | 0.000000 USDC | 0.007302 USDC | 0.092622 USDC (0.0852 €) | — | 3.71 | 0.152 (n=566) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53418669 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.108800 WETH | 0.000043 WETH | 0.000000 WETH | 0.000003 WETH | 0.000040 WETH (0.0849 €) | — | 3.70 | 0.152 (n=566) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53418287 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006257 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0794 €) | — | 1.77 | 0.162 (n=763) | REJECTED | below_safety_margin(111<125), p_lower_below_threshold(0.16<0.75) |
| 53418287 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.234971 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0793 €) | — | 1.61 | 0.162 (n=763) | REJECTED | below_safety_margin(37745054078162<46994195960298), p_lower_below_threshold(0.16<0.75) |
| 53418287 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 519.357228 USDC | 0.092905 USDC | 0.000000 USDC | 0.006877 USDC | 0.086028 USDC (0.0791 €) | — | 1.66 | 0.162 (n=763) | REJECTED | below_safety_margin(86028<103871), p_lower_below_threshold(0.16<0.75) |
| 53418669 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 293.787128 USDC | 0.087577 USDC | 0.000000 USDC | 0.007302 USDC | 0.080275 USDC (0.0739 €) | — | 2.73 | 0.177 (n=782) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53418669 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.127989 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0736 €) | — | 2.73 | 0.177 (n=782) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.18<0.75) |
| 53416066 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 54.237506 USDC | 0.072941 USDC | 0.000000 USDC | 0.005138 USDC | 0.067803 USDC (0.0624 €) | 0.067803 USDC | 12.50 | 0.000 (n=66) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53416066 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 54.237506 USDC | 0.072941 USDC | 0.000000 USDC | 0.005138 USDC | 0.067803 USDC (0.0624 €) | — | 12.50 | 0.000 (n=66) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53418669 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 107.921444 USDC | 0.075247 USDC | 0.000000 USDC | 0.007652 USDC | 0.067595 USDC (0.0622 €) | — | 6.26 | 0.152 (n=566) | REJECTED | stale_data(5857ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53418669 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.046992 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0620 €) | — | 6.25 | 0.152 (n=566) | REJECTED | stale_data(5851ms>4000.0), simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.15<0.75) |
| 53418287 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.205323 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000029 WETH (0.0615 €) | — | 1.43 | 0.006 (n=53) | REJECTED | below_safety_margin(29289142645448<41064652696245), p_lower_below_threshold(0.01<0.75) |
| 53418287 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 466.788980 USDC | 0.071812 USDC | 0.000000 USDC | 0.005139 USDC | 0.066673 USDC (0.0613 €) | — | 1.43 | 0.006 (n=53) | REJECTED | below_safety_margin(66673<93357), p_lower_below_threshold(0.01<0.75) |
| 53418659 | USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 123.236499 USDC | 0.073230 USDC | 0.000000 USDC | 0.006885 USDC | 0.066345 USDC (0.0610 €) | — | 5.38 | 0.152 (n=566) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53418659 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→EURC→[aerodrome_slipstream]→cbBTC | 0.001348 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0608 €) | — | 6.31 | 0.152 (n=566) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53418669 | USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 100.195036 USDC | 0.065387 USDC | 0.000000 USDC | 0.007652 USDC | 0.057735 USDC (0.0531 €) | — | 5.76 | 0.152 (n=566) | REJECTED | stale_data(5896ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53418669 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→USDT→[uniswap_v3]→WETH | 0.043484 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0529 €) | — | 5.77 | 0.152 (n=566) | REJECTED | stale_data(5890ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53418669 | USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 99.603026 USDC | 0.063831 USDC | 0.000000 USDC | 0.007652 USDC | 0.056179 USDC (0.0517 €) | — | 5.64 | 0.152 (n=566) | REJECTED | stale_data(5938ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53418669 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→USDT→[uniswap_v3]→WETH | 0.043219 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0515 €) | — | 5.65 | 0.152 (n=566) | REJECTED | stale_data(5933ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 53418287 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003857 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0508 €) | — | 1.84 | 0.162 (n=763) | REJECTED | below_safety_margin(71<77), p_lower_below_threshold(0.16<0.75) |
| 53418287 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.142926 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0507 €) | — | 1.69 | 0.162 (n=763) | REJECTED | below_safety_margin(24150267826672<28585240974696), p_lower_below_threshold(0.16<0.75) |
| 53418287 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 324.971692 USDC | 0.061862 USDC | 0.000000 USDC | 0.006877 USDC | 0.054985 USDC (0.0506 €) | — | 1.69 | 0.162 (n=763) | REJECTED | below_safety_margin(54985<64994), p_lower_below_threshold(0.16<0.75) |
| 53410636 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.350589 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0500 €) | — | 0.67 | 0.000 (n=18) | REJECTED | below_safety_margin(23656194212510<70117861151909), reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4589 ; taux observé 0.165 ; borne inférieure crédible (0.9) 0.158 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
