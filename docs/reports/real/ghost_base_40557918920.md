# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T21:01:34+00:00 ; durée 163.23 min ; blocs 53167873 → 53172771 (4858 vus)

## Connexion
- Requêtes RPC : 58073 ; erreurs : 407 ; latence p50/p95 : 157.3/868.7 ms
- Rafraîchissements d'état : 4859 ; âge des données au dernier bloc : 1.73 s ; changements de frais LP observés (pools à frais dynamiques) : 5303
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 29471 ; cycles déclenchés par événement : 4033 ; avance médiane sur le rafraîchissement multicall : 400 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,344.66 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 519 pools, 301 jetons, 18846 routes
- Par DEX : uniswap_v3 145, aerodrome 211, aerodrome_slipstream 120, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 185 (rejetés 2) → 590 jetons ; pools candidats 3771 (énumérés 330, par paires 0), mesurés 521, sous le plancher de 10000.0 $ : 2 → gardés 519 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2347.170972, 'cbBTC': 80539.356341, 'AERO': 0.69796}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,338,060 | 2,344.661709 | 53172771 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,613,701 | 0.029031 | 53172771 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,191,993 | 0.029104 | 53172771 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,643,558 | 0.000012 | 53172771 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,627,615 | 90.444869 | 53172771 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,425,222 | 2,342.346940 | 53172771 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,019,882 | 0.001636 | 53172771 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,953,001 | 1.441367 | 53172771 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,744,114 | 0.029025 | 53172771 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,081,967 | 2,343.168263 | 53172771 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,490,529 | 2,343.256823 | 53172771 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,254,131 | 0.998745 | 53172771 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,726,955 | 37,045.767506 | 53172771 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,965,106 | 0.029089 | 53172771 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,576,343 | 90.421463 | 53172771 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/USDC | 3000 | 2,364,143 | 2,346.573061 | 53172771 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,191,123 | 0.000012 | 53172771 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,140,124 | 1,216,890.965518 | 53172771 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,829,108 | 0.018687 | 53172771 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,811,068 | 0.000000 | 53172771 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,788,405 | 397.256997 | 53172771 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,697,554 | 0.000012 | 53172771 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,689,622 | 0.000012 | 53172771 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,686,507 | 0.000012 | 53172771 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,528,056 | 0.005882 | 53172771 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,576 | 0.826492 | 53172771 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,146 | 1.698043 | 53172771 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,451,148 | 3,374.582706 | 53172771 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,393,001 | 13,676.875206 | 53172771 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,252,287 | 0.000268 | 53172771 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,245,219 | 2,342.246620 | 53172771 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,201,196 | 67.346385 | 53172771 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,201,189 | 3,350.577850 | 53172771 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,185,024 | 0.000266 | 53172771 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | WETH/doginme | 10000 | 1,165,105 | 35,762,515.176186 | 53172771 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,162,100 | 1,067,456.215802 | 53172771 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | DRB/WETH | 10000 | 1,122,320 | 0.000000 | 53172771 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,117,655 | 506,095.379173 | 53172771 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,075,272 | 72,654.715290 | 53172771 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,049,162 | 16.593500 | 53172771 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,047,030 | 21,236,715.146711 | 53172771 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,046,991 | 57.106577 | 53172771 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 1,035,813 | 0.038628 | 53172771 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 943,725 | 2,331.655283 | 53172771 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 913,072 | 1,084.250556 | 53172771 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 906,616 | 0.000560 | 53172771 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/VVV | 10000 | 898,660 | 90.236249 | 53172771 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/msETH (stable) | 500 | 885,613 | 2.312202 | 53172771 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 882,615 | 17.859657 | 53172771 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v2 | WETH/USDC | 3000 | 848,791 | 2,345.161080 | 53172771 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 836,903 | 17.692889 | 53172771 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 808,120 | 0.000009 | 53172771 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 802,378 | 0.057767 | 53172771 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 793,843 | 0.803179 | 53172771 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 756,213 | 4,538,316.138986 | 53172771 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 751,314 | 0.626431 | 53172771 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/NPC | 3000 | 708,216 | 137,978.202574 | 53172771 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 693,729 | 504,592.596471 | 53172771 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 685,199 | 0.590835 | 53172771 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 673,774 | 0.108673 | 53172771 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 8891 ; routes examinées : 167559786 ; candidats optimisés : 515879 ; net attendu > 0 : 151 ; dernier cycle 105.6 ms
- Rejets (moteur) : {'spread_below_threshold': 164837012, 'liquidity_below_min': 2060674, 'negative_expected_net': 515728, 'borrow_bound_too_small': 145747, 'cycle_budget_exhausted': 474}
- Enregistrements de la session : 515879 ; net attendu > 0 : 151 ; simulés (eth_call de la vraie tx) : 8 (ok 0, échec 8) ; étiquettes ghost N+1 : 0/6 positives
- Décisions : {'REJECTED': 515879} ; motifs de rejet : {'below_safety_margin': 110, 'negative_expected_net': 515728, 'p_lower_below_threshold': 127, 'price_impact': 4, 'reliability_not_demonstrated': 24, 'simulation_failed': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53170773 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001644 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4731 €) | — | 38.81 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 134.135900 USDC | 0.521005 USDC | 0.000000 USDC | 0.007060 USDC | 0.513945 USDC (0.4728 €) | — | 38.32 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | cbBTC→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001631 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4694 €) | — | 38.80 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→USDC | 133.067463 USDC | 0.517115 USDC | 0.000000 USDC | 0.007060 USDC | 0.510055 USDC (0.4693 €) | — | 38.33 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001648 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4679 €) | — | 38.28 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 133.431064 USDC | 0.515365 USDC | 0.000000 USDC | 0.007060 USDC | 0.508305 USDC (0.4676 €) | — | 38.09 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→USDC | 133.431064 USDC | 0.514936 USDC | 0.000000 USDC | 0.007060 USDC | 0.507876 USDC (0.4672 €) | — | 38.06 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001601 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4672 €) | — | 39.36 | 0.000 (n=38) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 133.067463 USDC | 0.508658 USDC | 0.000000 USDC | 0.007060 USDC | 0.501598 USDC (0.4615 €) | — | 37.70 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53170773 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.001571 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4613 €) | — | 39.60 | 0.000 (n=26) | REJECTED | reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 76.346396 USDC | 0.489977 USDC | 0.000000 USDC | 0.007060 USDC | 0.482917 USDC (0.4443 €) | — | 63.25 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.032559 WETH | 0.000209 WETH | 0.000000 WETH | 0.000003 WETH | 0.000206 WETH (0.4443 €) | — | 63.26 | 0.000 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53170773 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.032524 WETH | 0.000208 WETH | 0.000000 WETH | 0.000003 WETH | 0.000205 WETH (0.4432 €) | — | 63.17 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 76.346698 USDC | 0.488816 USDC | 0.000000 USDC | 0.007060 USDC | 0.481756 USDC (0.4432 €) | — | 63.10 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53170773 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.032483 WETH | 0.000208 WETH | 0.000000 WETH | 0.000003 WETH | 0.000205 WETH (0.4430 €) | — | 63.22 | 0.000 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 76.104485 USDC | 0.488528 USDC | 0.000000 USDC | 0.007060 USDC | 0.481468 USDC (0.4430 €) | — | 63.26 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.032454 WETH | 0.000207 WETH | 0.000000 WETH | 0.000003 WETH | 0.000204 WETH (0.4408 €) | — | 62.97 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 76.043828 USDC | 0.486181 USDC | 0.000000 USDC | 0.007060 USDC | 0.479121 USDC (0.4408 €) | — | 63.01 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.032418 WETH | 0.000207 WETH | 0.000000 WETH | 0.000003 WETH | 0.000204 WETH (0.4402 €) | — | 62.94 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 75.923915 USDC | 0.485472 USDC | 0.000000 USDC | 0.007060 USDC | 0.478412 USDC (0.4401 €) | — | 63.01 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53170773 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.031836 WETH | 0.000205 WETH | 0.000000 WETH | 0.000003 WETH | 0.000202 WETH (0.4357 €) | — | 63.45 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 74.510141 USDC | 0.480501 USDC | 0.000000 USDC | 0.007060 USDC | 0.473441 USDC (0.4356 €) | — | 63.54 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.028332 WETH | 0.000183 WETH | 0.000000 WETH | 0.000003 WETH | 0.000179 WETH (0.3871 €) | — | 63.33 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 66.175604 USDC | 0.427415 USDC | 0.000000 USDC | 0.007416 USDC | 0.419999 USDC (0.3864 €) | — | 63.47 | 0.000 (n=29) | REJECTED | reliability_not_demonstrated |
| 53170773 | WETH→[uniswap_v2]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→WETH | 0.024671 WETH | 0.000123 WETH | 0.000000 WETH | 0.000003 WETH | 0.000120 WETH (0.2586 €) | — | 48.59 | — (n=0) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2862 ; taux observé 0.090 ; borne inférieure crédible (0.9) 0.083 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
