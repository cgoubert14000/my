# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T03:08:39+00:00 ; durée 70.37 min ; blocs 53440871 → 53442984 (2080 vus)

## Connexion
- Requêtes RPC : 24280 ; erreurs : 0 ; latence p50/p95 : 291.5/1,215.2 ms
- Rafraîchissements d'état : 2080 ; âge des données au dernier bloc : 4.14 s ; changements de frais LP observés (pools à frais dynamiques) : 2722
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 22208 ; cycles déclenchés par événement : 2739 ; avance médiane sur le rafraîchissement multicall : 565 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,249.07 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 285 jetons, 18224 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 108, aerodrome 202, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 308, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2253.967555, 'cbBTC': 77042.637438, 'AERO': 0.602257}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,748,455 | 2,249.067989 | 53442984 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,126,600 | 0.029329 | 53442984 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,066,332 | 0.029314 | 53442984 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,953,268 | 0.000013 | 53442984 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,838,280 | 2,248.183076 | 53442984 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,532,655 | 105.176709 | 53442984 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,523,834 | 0.001567 | 53442984 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,343,734 | 1.666901 | 53442984 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,754,901 | 0.029321 | 53442984 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,104,246 | 2,249.165184 | 53442984 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,034,474 | 0.999884 | 53442984 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,901,475 | 2,248.970243 | 53442984 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,446,486 | 39,853.646064 | 53442984 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,682,435 | 0.029323 | 53442984 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,137,947 | 1,121,968.336551 | 53442984 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 2,028,037 | 0.000013 | 53442984 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2709 | 1,978,296 | 105.157464 | 53442984 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | XDP/USDC | 100 | 1,770,253 | 0.018388 | 53442984 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,663,385 | 0.000000 | 53442984 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,602,999 | 0.000013 | 53442984 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,555,241 | 1.436173 | 53442984 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,538,747 | 0.000013 | 53442984 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,525,328 | 444.639079 | 53442984 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,495,516 | 2,249.310944 | 53442984 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,608 | 0.822379 | 53442984 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,379,814 | 3,749.265815 | 53442984 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,348,111 | 2,249.765546 | 53442984 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,307,466 | 2,248.197464 | 53442984 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,286,028 | 0.004999 | 53442984 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,270,366 | 15,156.099054 | 53442984 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 1,256,106 | 0.000013 | 53442984 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,168,739 | 71.138543 | 53442984 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,098,041 | 37,707,062.323865 | 53442984 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,043,012 | 542,378.997276 | 53442984 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,006,577 | 0.000000 | 53442984 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 999,557 | 22,617,196.530373 | 53442984 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 978,199 | 20.206913 | 53442984 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 954,577 | 84,684.293703 | 53442984 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 921,999 | 2,257.234891 | 53442984 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 912,474 | 1,267,349.544148 | 53442984 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 910,063 | 1,044.538347 | 53442984 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 905,649 | 104.470318 | 53442984 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 876,091 | 81.564074 | 53442984 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,697 | 0.000549 | 53442984 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 855,266 | 0.046754 | 53442984 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 822,304 | 3,725.146765 | 53442984 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 813,955 | 20.318194 | 53442984 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 791,203 | 0.056052 | 53442984 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 763,485 | 0.798949 | 53442984 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 722,461 | 0.574971 | 53442984 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 715,753 | 0.000258 | 53442984 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 700,480 | 4,874,329.229513 | 53442984 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,547 | 145,901.194426 | 53442984 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 659,972 | 0.547712 | 53442984 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 651,802 | 2.338342 | 53442984 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 650,296 | 0.000008 | 53442984 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2162 | 641,347 | 545,872.216564 | 53442984 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 604,084 | 0.914848 | 53442984 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 585,766 | 0.086880 | 53442984 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 547,342 | 0.036825 | 53442984 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 4818 ; routes examinées : 87803232 ; candidats optimisés : 242515 ; net attendu > 0 : 295 ; dernier cycle 161.8 ms
- Rejets (moteur) : {'spread_below_threshold': 86448469, 'liquidity_below_min': 1093059, 'negative_expected_net': 242220, 'unquotable': 13958, 'borrow_bound_too_small': 4813, 'cycle_budget_exhausted': 418}
- Enregistrements de la session : 242515 ; net attendu > 0 : 295 ; simulés (eth_call de la vraie tx) : 7 (ok 0, échec 7) ; étiquettes ghost N+1 : 0/7 positives
- Décisions : {'REJECTED': 242515} ; motifs de rejet : {'below_safety_margin': 284, 'negative_expected_net': 242220, 'p_lower_below_threshold': 278, 'reliability_not_demonstrated': 17, 'simulation_failed': 7}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53442750 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 45.296202 USDC | 0.104960 USDC | 0.000000 USDC | 0.005062 USDC | 0.099898 USDC (0.0919 €) | — | 22.05 | 0.001 (n=10) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53442864 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.011029 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0790 €) | — | 1.02 | 0.185 (n=839) | REJECTED | below_safety_margin(112<220), p_lower_below_threshold(0.19<0.75) |
| 53442864 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.401701 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0789 €) | — | 0.95 | 0.185 (n=839) | REJECTED | below_safety_margin(38094113610882<80340255564833), p_lower_below_threshold(0.19<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 920.782602 USDC | 0.092212 USDC | 0.000000 USDC | 0.006768 USDC | 0.085444 USDC (0.0786 €) | — | 0.93 | 0.185 (n=839) | REJECTED | below_safety_margin(85444<184156), p_lower_below_threshold(0.19<0.75) |
| 53442864 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.010076 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0748 €) | — | 1.05 | 0.185 (n=839) | REJECTED | below_safety_margin(106<201), p_lower_below_threshold(0.19<0.75) |
| 53442864 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.370100 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0745 €) | — | 0.97 | 0.185 (n=839) | REJECTED | below_safety_margin(35977094181516<74019905616955), p_lower_below_threshold(0.19<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 846.379396 USDC | 0.087446 USDC | 0.000000 USDC | 0.006768 USDC | 0.080678 USDC (0.0742 €) | — | 0.95 | 0.185 (n=839) | REJECTED | below_safety_margin(80678<169275), p_lower_below_threshold(0.19<0.75) |
| 53442864 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008895 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0699 €) | — | 1.11 | 0.037 (n=181) | REJECTED | below_safety_margin(99<177), p_lower_below_threshold(0.04<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 702.804983 USDC | 0.080699 USDC | 0.000000 USDC | 0.005057 USDC | 0.075642 USDC (0.0696 €) | — | 1.08 | 0.037 (n=181) | REJECTED | below_safety_margin(75642<140560), p_lower_below_threshold(0.04<0.75) |
| 53441531 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.209769 WETH | 0.000036 WETH | 0.000000 WETH | 0.000002 WETH | 0.000033 WETH (0.0690 €) | — | 1.59 | 0.037 (n=181) | REJECTED | below_safety_margin(33265543026060<41953740710885), p_lower_below_threshold(0.04<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 472.119583 USDC | 0.079943 USDC | 0.000000 USDC | 0.005060 USDC | 0.074883 USDC (0.0689 €) | — | 1.59 | 0.037 (n=181) | REJECTED | below_safety_margin(74883<94423), p_lower_below_threshold(0.04<0.75) |
| 53441531 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.171973 WETH | 0.000025 WETH | 0.000000 WETH | 0.000002 WETH | 0.000022 WETH (0.0463 €) | — | 1.30 | 0.026 (n=56) | REJECTED | below_safety_margin(22336456983429<34394668677693), p_lower_below_threshold(0.03<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 387.818691 USDC | 0.055336 USDC | 0.000000 USDC | 0.005060 USDC | 0.050276 USDC (0.0463 €) | — | 1.30 | 0.026 (n=56) | REJECTED | below_safety_margin(50276<77563), p_lower_below_threshold(0.03<0.75) |
| 53442864 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006417 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0423 €) | — | 0.93 | 0.037 (n=181) | REJECTED | below_safety_margin(60<128), p_lower_below_threshold(0.04<0.75) |
| 53442864 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 530.820876 USDC | 0.050816 USDC | 0.000000 USDC | 0.005057 USDC | 0.045759 USDC (0.0421 €) | — | 0.86 | 0.037 (n=181) | REJECTED | below_safety_margin(45759<106164), p_lower_below_threshold(0.04<0.75) |
| 53441962 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 477.566120 USDC | 0.050033 USDC | 0.000000 USDC | 0.005402 USDC | 0.044631 USDC (0.0411 €) | — | 0.93 | 0.037 (n=181) | REJECTED | below_safety_margin(44631<95513), p_lower_below_threshold(0.04<0.75) |
| 53441962 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.006516 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0410 €) | — | 0.89 | 0.037 (n=181) | REJECTED | below_safety_margin(58<130), p_lower_below_threshold(0.04<0.75) |
| 53441531 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.004073 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0290 €) | — | 1.01 | 0.186 (n=836) | REJECTED | below_safety_margin(41<81), p_lower_below_threshold(0.19<0.75) |
| 53442647 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.298712 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000014 WETH (0.0288 €) | — | 0.46 | 0.037 (n=181) | REJECTED | below_safety_margin(13869354100438<59742411794948), p_lower_below_threshold(0.04<0.75) |
| 53442648 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.298712 WETH | 0.000016 WETH | 0.000000 WETH | 0.000002 WETH | 0.000014 WETH (0.0288 €) | — | 0.46 | 0.037 (n=181) | REJECTED | below_safety_margin(13869354100438<59742411794948), p_lower_below_threshold(0.04<0.75) |
| 53442647 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 670.756842 USDC | 0.036613 USDC | 0.000000 USDC | 0.005406 USDC | 0.031207 USDC (0.0287 €) | — | 0.47 | 0.037 (n=181) | REJECTED | below_safety_margin(31207<134151), p_lower_below_threshold(0.04<0.75) |
| 53442648 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 670.756842 USDC | 0.036613 USDC | 0.000000 USDC | 0.005406 USDC | 0.031207 USDC (0.0287 €) | — | 0.47 | 0.037 (n=181) | REJECTED | below_safety_margin(31207<134151), p_lower_below_threshold(0.04<0.75) |
| 53441531 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 313.655980 USDC | 0.037662 USDC | 0.000000 USDC | 0.006772 USDC | 0.030890 USDC (0.0284 €) | — | 0.98 | 0.186 (n=836) | REJECTED | below_safety_margin(30890<62731), p_lower_below_threshold(0.19<0.75) |
| 53441531 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.125978 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0283 €) | — | 1.08 | 0.186 (n=836) | REJECTED | below_safety_margin(13655291199281<25195668185131), p_lower_below_threshold(0.19<0.75) |
| 53442757 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.053422 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0264 €) | — | 2.39 | 0.186 (n=836) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4784 ; taux observé 0.171 ; borne inférieure crédible (0.9) 0.164 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
