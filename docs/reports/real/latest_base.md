# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-25T06:45:18+00:00 ; durée 125.88 min ; blocs 53056902 → 53060683 (3714 vus)

## Connexion
- Requêtes RPC : 46000 ; erreurs : 0 ; latence p50/p95 : 305.1/1,001.2 ms
- Rafraîchissements d'état : 3714 ; âge des données au dernier bloc : 3.54 s ; changements de frais LP observés (pools à frais dynamiques) : 3758
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 35132 ; cycles déclenchés par événement : 4396 ; avance médiane sur le rafraîchissement multicall : 497 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,348.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 541 pools, 309 jetons, 19696 routes
- Par DEX : uniswap_v3 144, aerodrome 216, aerodrome_slipstream 134, pancakeswap_v3 31, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 193 (rejetés 2) → 598 jetons ; pools candidats 3806 (énumérés 349, par paires 0), mesurés 543, sous le plancher de 10000.0 $ : 2 → gardés 541 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2361.63016, 'cbBTC': 80803.612106, 'AERO': 0.690594}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,855,331 | 2,348.213419 | 53060684 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,322,171 | 0.029127 | 53060684 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,263,005 | 0.029192 | 53060684 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,526,353 | 0.000012 | 53060684 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,972,852 | 95.340930 | 53060684 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,419,654 | 2,342.314001 | 53060684 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,620,309 | 1.469703 | 53060684 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,035,185 | 0.001648 | 53060684 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,651,321 | 2,341.496306 | 53060684 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,459,507 | 0.029115 | 53060684 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,446,075 | 2,341.386434 | 53060684 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,242,096 | 0.999832 | 53060684 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,891,762 | 34,473.508502 | 53060684 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,797,420 | 2,348.275987 | 53060684 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2530 | 3,258,843 | 0.029185 | 53060684 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 2,856,240 | 0.000012 | 53060684 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | WETH/VVV | 2721 | 2,520,073 | 95.367928 | 53060684 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,224,490 | 411.163581 | 53060684 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/FAI | 10000 | 2,132,195 | 1,229,675.520279 | 53060684 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,904,712 | 0.000012 | 53060684 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,902,362 | 0.000000 | 53060684 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,790,149 | 0.018025 | 53060684 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,732,434 | 0.000012 | 53060684 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,721,302 | 0.000012 | 53060684 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,578,445 | 0.000265 | 53060684 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,470,515 | 1.673913 | 53060684 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,464,555 | 0.005582 | 53060684 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,859 | 0.826892 | 53060684 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,437 | 3,445.582583 | 53060684 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,373,394 | 14,099.369288 | 53060684 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,295,174 | 2,342.359145 | 53060684 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,265,507 | 3,445.976476 | 53060684 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,247,875 | 0.000264 | 53060684 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,222,545 | 65.014830 | 53060684 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,174,051 | 0.000000 | 53060684 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,169,801 | 35,446,293.114047 | 53060684 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,133,046 | 1,126,920.303517 | 53060684 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,128,291 | 491,864.954002 | 53060684 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,065,920 | 55.127535 | 53060684 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 1,038,834 | 78,323.583136 | 53060684 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,037,778 | 17.085273 | 53060684 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,037,617 | 21,489,605.354605 | 53060684 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | USDC/VVV | 3000 | 966,047 | 0.040724 | 53060684 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 950,479 | 17.165105 | 53060684 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | WETH/USDC | 10000 | 927,265 | 2,344.953414 | 53060684 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 925,114 | 2.309502 | 53060684 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/MORPHO | 3000 | 907,353 | 1,120.791591 | 53060684 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 900,514 | 0.000551 | 53060684 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,149 | 17.853711 | 53060684 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 871,802 | 95.781970 | 53060684 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 849,821 | 2,348.214854 | 53060684 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 813,330 | 0.000008 | 53060684 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | weETH_04c0/WETH | 500 | 801,932 | 1.105854 | 53060684 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome | WETH/wstETH | 3000 | 795,070 | 0.803130 | 53060684 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,431 | 0.055237 | 53060684 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 746,161 | 0.619529 | 53060684 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 744,933 | 4,690,124.288701 | 53060684 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 734,109 | 0.674837 | 53060684 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 719,925 | 133,874.037105 | 53060684 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 705,355 | 494,726.875756 | 53060684 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |

## Recherche d'opportunités
- Cycles : 8109 ; routes examinées : 159714864 ; candidats optimisés : 431089 ; net attendu > 0 : 386 ; dernier cycle 144.0 ms
- Rejets (moteur) : {'spread_below_threshold': 157337519, 'liquidity_below_min': 1875989, 'negative_expected_net': 430703, 'pool_quarantined': 43624, 'borrow_bound_too_small': 23979, 'unquotable': 2092, 'cycle_budget_exhausted': 572}
- Enregistrements de la session : 431089 ; net attendu > 0 : 386 ; simulés (eth_call de la vraie tx) : 28 (ok 5, échec 23) ; étiquettes ghost N+1 : 0/27 positives
- Décisions : {'REJECTED': 431089} ; motifs de rejet : {'below_safety_margin': 294, 'negative_expected_net': 430703, 'p_lower_below_threshold': 315, 'price_impact': 2, 'reliability_not_demonstrated': 71, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 23, 'stale_data': 10}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53060653 | cbBTC→[aerodrome_slipstream]→EDGE→[aerodrome]→cbBTC | 0.004748 cbBTC | 0.000041 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000041 cbBTC (3.0238 €) | — | 85.83 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
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

## Fiabilité et décision
- Observations ghost : 2381 ; taux observé 0.095 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
