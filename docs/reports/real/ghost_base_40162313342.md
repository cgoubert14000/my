# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T06:17:34+00:00 ; durée 98.14 min ; blocs 53056902 → 53059851 (2887 vus)

## Connexion
- Requêtes RPC : 35697 ; erreurs : 0 ; latence p50/p95 : 267.0/892.7 ms
- Rafraîchissements d'état : 2887 ; âge des données au dernier bloc : 3.38 s ; changements de frais LP observés (pools à frais dynamiques) : 3172
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 27560 ; cycles déclenchés par événement : 3589 ; avance médiane sur le rafraîchissement multicall : 457 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,351.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 309 jetons, 19696 routes
- Par DEX : uniswap_v3 144, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 349, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2361.63016, 'cbBTC': 80803.612106, 'AERO': 0.690594}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,981,211 | 2,351.226481 | 53059852 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,336,712 | 0.029161 | 53059852 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,239,225 | 0.029192 | 53059852 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,527,042 | 0.000012 | 53059852 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,990,341 | 95.209676 | 53059852 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,428,162 | 2,348.421211 | 53059852 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,626,734 | 1.471240 | 53059852 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,038,824 | 0.001650 | 53059852 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 579 | 5,654,132 | 2,349.105710 | 53059852 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,464,716 | 0.029153 | 53059852 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,449,680 | 2,348.811693 | 53059852 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,242,629 | 0.999832 | 53059852 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,896,223 | 34,482.929494 | 53059852 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,799,856 | 2,351.235945 | 53059852 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,266,726 | 0.029205 | 53059852 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,856,425 | 0.000012 | 53059852 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2709 | 2,524,777 | 95.244645 | 53059852 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,227,491 | 411.091352 | 53059852 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,134,931 | 1,229,675.520279 | 53059852 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,904,803 | 0.000000 | 53059852 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,904,671 | 0.000012 | 53059852 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | XDP/USDC | 100 | 1,789,007 | 0.018010 | 53059852 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,732,544 | 0.000012 | 53059852 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,721,408 | 0.000012 | 53059852 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,580,470 | 0.000265 | 53059852 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53059852 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53059852 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,452,926 | 0.005520 | 53059852 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,365 | 3,457.168168 | 53059852 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,374,286 | 14,090.817306 | 53059852 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,296,832 | 2,348.403654 | 53059852 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,266,183 | 3,445.976476 | 53059852 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,249,476 | 0.000264 | 53059852 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,545 | 65.014830 | 53059852 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,178,564 | 0.000000 | 53059852 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,171,302 | 35,446,293.114047 | 53059852 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,134,454 | 1,127,010.600220 | 53059852 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,129,739 | 491,864.954002 | 53059852 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,086,400 | 53.068695 | 53059852 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,040,919 | 16.946026 | 53059852 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,040,168 | 78,309.972192 | 53059852 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,038,948 | 21,489,605.354605 | 53059852 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 967,369 | 0.040546 | 53059852 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 951,699 | 17.165105 | 53059852 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/USDC | 10000 | 927,751 | 2,344.953414 | 53059852 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 926,301 | 2.309502 | 53059852 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 907,200 | 1,120.943134 | 53059852 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 901,670 | 0.000551 | 53059852 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,149 | 17.853711 | 53059852 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,410 | 95.781970 | 53059852 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 850,366 | 2,351.316302 | 53059852 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 812,896 | 0.000008 | 53059852 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 802,961 | 1.105854 | 53059852 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 796,090 | 0.803130 | 53059852 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,394 | 0.056571 | 53059852 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 750,010 | 4,638,629.884420 | 53059852 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,872 | 0.620032 | 53059852 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v3 | TIG/USDC | 10000 | 734,109 | 0.674837 | 53059852 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 720,849 | 133,874.037105 | 53059852 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 706,260 | 494,681.848733 | 53059852 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 6475 ; routes examinées : 127531600 ; candidats optimisés : 342546 ; net attendu > 0 : 319 ; dernier cycle 48.0 ms
- Rejets (moteur) : {'spread_below_threshold': 125597444, 'liquidity_below_min': 1534086, 'negative_expected_net': 342227, 'pool_quarantined': 43624, 'borrow_bound_too_small': 11607, 'unquotable': 1930, 'cycle_budget_exhausted': 363}
- Enregistrements de la session : 342546 ; net attendu > 0 : 319 ; simulés (eth_call de la vraie tx) : 25 (ok 2, échec 23) ; étiquettes ghost N+1 : 0/24 positives
- Décisions : {'REJECTED': 342546} ; motifs de rejet : {'below_safety_margin': 240, 'negative_expected_net': 342227, 'p_lower_below_threshold': 259, 'price_impact': 2, 'reliability_not_demonstrated': 60, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 23, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53059762 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.045473 WETH | 0.000517 WETH | 0.000000 WETH | 0.000003 WETH | 0.000514 WETH (1.1111 €) | — | 112.96 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53059762 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 106.790468 USDC | 1.213388 USDC | 0.000000 USDC | 0.007062 USDC | 1.206326 USDC (1.1098 €) | — | 112.96 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |
| 53059762 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.045275 WETH | 0.000514 WETH | 0.000000 WETH | 0.000003 WETH | 0.000511 WETH (1.1050 €) | — | 112.83 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53059762 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 106.337676 USDC | 1.206901 USDC | 0.000000 USDC | 0.007062 USDC | 1.199839 USDC (1.1039 €) | — | 112.83 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53059762 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.043425 WETH | 0.000511 WETH | 0.000000 WETH | 0.000003 WETH | 0.000508 WETH (1.0987 €) | — | 116.96 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53059762 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 101.982626 USDC | 1.199856 USDC | 0.000000 USDC | 0.007062 USDC | 1.192794 USDC (1.0974 €) | — | 116.96 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53059762 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.043383 WETH | 0.000509 WETH | 0.000000 WETH | 0.000003 WETH | 0.000506 WETH (1.0948 €) | — | 116.66 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |
| 53059762 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 101.889432 USDC | 1.195688 USDC | 0.000000 USDC | 0.007062 USDC | 1.188626 USDC (1.0935 €) | — | 116.66 | 0.001 (n=13) | REJECTED | reliability_not_demonstrated |
| 53059762 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.043246 WETH | 0.000494 WETH | 0.000000 WETH | 0.000003 WETH | 0.000491 WETH (1.0614 €) | — | 113.47 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53059762 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 101.601462 USDC | 1.159887 USDC | 0.000000 USDC | 0.007062 USDC | 1.152825 USDC (1.0606 €) | — | 113.47 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53059762 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.042179 WETH | 0.000491 WETH | 0.000000 WETH | 0.000003 WETH | 0.000488 WETH (1.0565 €) | — | 115.79 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53059762 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 99.123053 USDC | 1.154841 USDC | 0.000000 USDC | 0.007062 USDC | 1.147779 USDC (1.0560 €) | — | 115.79 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53059762 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC | 91.717702 USDC | 1.045760 USDC | 0.000000 USDC | 0.007062 USDC | 1.038698 USDC (0.9556 €) | — | 113.25 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53059762 | WETH→[uniswap_v3]→SUP→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.038943 WETH | 0.000444 WETH | 0.000000 WETH | 0.000003 WETH | 0.000441 WETH (0.9540 €) | — | 113.25 | 0.000 (n=16) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 101.966309 USDC | 0.861736 USDC | 0.000000 USDC | 0.007094 USDC | 0.854642 USDC (0.7863 €) | — | 83.82 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 102.137640 USDC | 0.861683 USDC | 0.000000 USDC | 0.007094 USDC | 0.854589 USDC (0.7862 €) | — | 83.67 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.043138 WETH | 0.000364 WETH | 0.000000 WETH | 0.000003 WETH | 0.000361 WETH (0.7854 €) | — | 83.80 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058175 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.043243 WETH | 0.000364 WETH | 0.000000 WETH | 0.000003 WETH | 0.000361 WETH (0.7853 €) | — | 83.58 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 101.555983 USDC | 0.851676 USDC | 0.000000 USDC | 0.007094 USDC | 0.844582 USDC (0.7770 €) | — | 83.16 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.042977 WETH | 0.000360 WETH | 0.000000 WETH | 0.000003 WETH | 0.000357 WETH (0.7762 €) | — | 83.12 | 0.001 (n=14) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 100.467649 USDC | 0.834113 USDC | 0.000000 USDC | 0.007094 USDC | 0.827019 USDC (0.7609 €) | — | 82.32 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.042568 WETH | 0.000353 WETH | 0.000000 WETH | 0.000003 WETH | 0.000350 WETH (0.7602 €) | — | 82.19 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 99.866315 USDC | 0.824586 USDC | 0.000000 USDC | 0.007094 USDC | 0.817492 USDC (0.7521 €) | — | 81.86 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53058175 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.042269 WETH | 0.000349 WETH | 0.000000 WETH | 0.000003 WETH | 0.000346 WETH (0.7515 €) | — | 81.83 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53058175 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 98.364297 USDC | 0.821963 USDC | 0.000000 USDC | 0.007094 USDC | 0.814869 USDC (0.7497 €) | — | 82.84 | 0.001 (n=14) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2378 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.088 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
