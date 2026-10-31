# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T23:14:48+00:00 ; durée 325.77 min ; blocs 53339794 → 53349564 (9514 vus)

## Connexion
- Requêtes RPC : 111950 ; erreurs : 0 ; latence p50/p95 : 110.3/887.3 ms
- Rafraîchissements d'état : 9515 ; âge des données au dernier bloc : 1.96 s ; changements de frais LP observés (pools à frais dynamiques) : 8030
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 63634 ; cycles déclenchés par événement : 9316 ; avance médiane sur le rafraîchissement multicall : 436 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,257.10 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 506 pools, 291 jetons, 18722 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 115, aerodrome 206, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 179 (rejetés 2) → 584 jetons ; pools candidats 3790 (énumérés 319, par paires 0), mesurés 509, sous le plancher de 10000.0 $ : 3 → gardés 506 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2248.577307, 'cbBTC': 77558.902259, 'AERO': 0.633591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,560,107 | 2,257.095473 | 53349564 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,114,472 | 0.029077 | 53349564 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,304,633 | 0.000013 | 53349564 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,073,886 | 0.029089 | 53349564 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,891,457 | 96.813270 | 53349564 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,870,522 | 2,251.806431 | 53349564 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,693,268 | 0.001610 | 53349564 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,760,637 | 1.551872 | 53349564 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,259,892 | 0.029082 | 53349564 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,087,104 | 0.998852 | 53349564 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,057,830 | 2,251.743979 | 53349564 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,954,653 | 2,251.752282 | 53349564 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,543,419 | 37,973.625876 | 53349564 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,693,153 | 0.029101 | 53349564 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2736 | 2,416,099 | 96.780608 | 53349564 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,073,929 | 1,200,829.160231 | 53349564 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,964,134 | 0.000013 | 53349564 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,762,774 | 0.000000 | 53349564 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,710,498 | 0.017289 | 53349564 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,658,471 | 0.000013 | 53349564 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,596,725 | 2,257.116885 | 53349564 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,584,535 | 0.000013 | 53349564 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,551,996 | 424.212403 | 53349564 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,920 | 1.490152 | 53349564 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,369 | 0.825814 | 53349564 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,744 | 3,495.094268 | 53349564 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,409,447 | 2,258.029679 | 53349564 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,345,206 | 2,251.500249 | 53349564 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,324,328 | 0.005182 | 53349564 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,307,087 | 14,584.985382 | 53349564 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,306,726 | 0.000013 | 53349564 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,174,224 | 70.475891 | 53349564 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,172,043 | 31,425,651.748122 | 53349564 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,065,523 | 515,513.273245 | 53349564 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,047,263 | 0.000000 | 53349564 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,029,034 | 21,602,616.147259 | 53349564 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,005,955 | 76,849.778517 | 53349564 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 998,391 | 97.198741 | 53349564 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 987,050 | 19.676740 | 53349564 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 984,839 | 0.042987 | 53349564 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 981,754 | 64.951151 | 53349564 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 951,413 | 1,176,701.828185 | 53349564 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 949,917 | 952.819177 | 53349564 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 924,223 | 2,242.032039 | 53349564 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 879,170 | 3,494.893415 | 53349564 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,072 | 0.000550 | 53349564 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 840,921 | 19.336048 | 53349564 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 837,202 | 0.063238 | 53349564 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 764,250 | 0.803065 | 53349564 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 735,734 | 0.000262 | 53349564 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,140 | 0.590446 | 53349564 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,213 | 4,589,269.360049 | 53349564 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 695,320 | 0.000008 | 53349564 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 673,046 | 141,838.129506 | 53349564 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 660,789 | 518,595.537407 | 53349564 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 658,180 | 2.336543 | 53349564 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 656,609 | 0.542933 | 53349564 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 615,752 | 0.093808 | 53349564 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 605,753 | 0.916319 | 53349564 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 557,804 | 953.022418 | 53349564 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 18830 ; routes examinées : 352535260 ; candidats optimisés : 1233397 ; net attendu > 0 : 928 ; dernier cycle 173.4 ms
- Rejets (moteur) : {'spread_below_threshold': 347059200, 'liquidity_below_min': 3927221, 'negative_expected_net': 1232469, 'pool_quarantined': 251622, 'unquotable': 44612, 'borrow_bound_too_small': 18827, 'cycle_budget_exhausted': 381}
- Enregistrements de la session : 1233397 ; net attendu > 0 : 928 ; simulés (eth_call de la vraie tx) : 88 (ok 11, échec 77) ; étiquettes ghost N+1 : 6/62 positives
- Décisions : {'REJECTED': 1233397} ; motifs de rejet : {'below_safety_margin': 480, 'negative_expected_net': 1232469, 'p_lower_below_threshold': 890, 'price_impact': 17, 'reliability_not_demonstrated': 38, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 1, 'simulation_failed': 77}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53347773 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 617.492790 USDC | 2.392625 USDC | 0.000000 USDC | 0.007470 USDC | 2.385155 USDC (2.1943 €) | — | 38.63 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.273395 WETH | 0.001059 WETH | 0.000000 WETH | 0.000003 WETH | 0.001055 WETH (2.1922 €) | — | 38.60 | 0.000 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53347773 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 615.967098 USDC | 2.373014 USDC | 0.000000 USDC | 0.007812 USDC | 2.365202 USDC (2.1760 €) | — | 38.40 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.272707 WETH | 0.001050 WETH | 0.000000 WETH | 0.000003 WETH | 0.001047 WETH (2.1738 €) | — | 38.38 | 0.000 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53347773 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 587.540721 USDC | 2.285317 USDC | 0.000000 USDC | 0.007812 USDC | 2.277505 USDC (2.0953 €) | — | 38.76 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.259982 WETH | 0.001011 WETH | 0.000000 WETH | 0.000003 WETH | 0.001007 WETH (2.0925 €) | — | 38.75 | 0.000 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53347773 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 564.177983 USDC | 1.989093 USDC | 0.000000 USDC | 0.007470 USDC | 1.981623 USDC (1.8231 €) | — | 35.12 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.249571 WETH | 0.000880 WETH | 0.000000 WETH | 0.000003 WETH | 0.000876 WETH (1.8201 €) | — | 35.11 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 556.423939 USDC | 1.957482 USDC | 0.000000 USDC | 0.007127 USDC | 1.950355 USDC (1.7943 €) | — | 35.05 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.246061 WETH | 0.000865 WETH | 0.000000 WETH | 0.000003 WETH | 0.000862 WETH (1.7912 €) | — | 35.04 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 439.235748 USDC | 1.530607 USDC | 0.000000 USDC | 0.007470 USDC | 1.523137 USDC (1.4013 €) | — | 34.68 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.193864 WETH | 0.000676 WETH | 0.000000 WETH | 0.000003 WETH | 0.000672 WETH (1.3968 €) | — | 34.69 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 454.942221 USDC | 1.284895 USDC | 0.000000 USDC | 0.007127 USDC | 1.277768 USDC (1.1755 €) | — | 28.09 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.200948 WETH | 0.000567 WETH | 0.000000 WETH | 0.000003 WETH | 0.000564 WETH (1.1720 €) | — | 28.08 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 332.911250 USDC | 1.278150 USDC | 0.000000 USDC | 0.006784 USDC | 1.271366 USDC (1.1697 €) | — | 38.19 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.146776 WETH | 0.000564 WETH | 0.000000 WETH | 0.000003 WETH | 0.000561 WETH (1.1644 €) | — | 38.19 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 440.323195 USDC | 1.237632 USDC | 0.000000 USDC | 0.007127 USDC | 1.230505 USDC (1.1321 €) | — | 27.95 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.194564 WETH | 0.000546 WETH | 0.000000 WETH | 0.000003 WETH | 0.000543 WETH (1.1284 €) | — | 27.92 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53347773 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 537.153111 USDC | 1.070431 USDC | 0.000000 USDC | 0.006784 USDC | 1.063647 USDC (0.9786 €) | — | 19.80 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53347773 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.237986 WETH | 0.000474 WETH | 0.000000 WETH | 0.000003 WETH | 0.000471 WETH (0.9776 €) | — | 19.78 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53347773 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 533.725684 USDC | 1.052730 USDC | 0.000000 USDC | 0.007127 USDC | 1.045603 USDC (0.9620 €) | — | 19.59 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53347773 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.236504 WETH | 0.000466 WETH | 0.000000 WETH | 0.000003 WETH | 0.000463 WETH (0.9610 €) | — | 19.56 | 0.067 (n=100) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53347773 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 495.222507 USDC | 0.994135 USDC | 0.000000 USDC | 0.007127 USDC | 0.987008 USDC (0.9080 €) | — | 19.93 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53347773 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.219226 WETH | 0.000440 WETH | 0.000000 WETH | 0.000003 WETH | 0.000437 WETH (0.9069 €) | — | 19.92 | 0.017 (n=85) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53347773 | USDC→[uniswap_v2]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 351.756208 USDC | 0.922222 USDC | 0.000000 USDC | 0.006426 USDC | 0.915796 USDC (0.8425 €) | — | 26.03 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4032 ; taux observé 0.128 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
