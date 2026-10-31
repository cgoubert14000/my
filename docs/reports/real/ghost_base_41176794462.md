# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T07:36:51+00:00 ; durée 61.48 min ; blocs 53319584 → 53321430 (1841 vus)

## Connexion
- Requêtes RPC : 21700 ; erreurs : 0 ; latence p50/p95 : 193.8/1,093.3 ms
- Rafraîchissements d'état : 1841 ; âge des données au dernier bloc : 3.29 s ; changements de frais LP observés (pools à frais dynamiques) : 1522
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 13454 ; cycles déclenchés par événement : 1624 ; avance médiane sur le rafraîchissement multicall : 477 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,240.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 290 jetons, 18766 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 115, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3730 (énumérés 320, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2240.565044, 'cbBTC': 77162.459811, 'AERO': 0.625673}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,943,690 | 2,240.566936 | 53321431 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,992,868 | 0.029015 | 53321431 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,256,317 | 0.000013 | 53321431 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,015,122 | 0.029063 | 53321431 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,179,591 | 2,241.378354 | 53321431 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,687,950 | 100.726907 | 53321431 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,672,394 | 0.001616 | 53321431 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,886,561 | 1.602533 | 53321431 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,478,868 | 0.029005 | 53321431 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,123,849 | 2,240.851957 | 53321431 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,112,553 | 2,240.785388 | 53321431 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,060,849 | 1.000001 | 53321431 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,541,148 | 37,467.635373 | 53321431 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,747,209 | 0.029045 | 53321431 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,333,358 | 100.708742 | 53321431 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,054,307 | 1,206,019.129455 | 53321431 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,972,879 | 0.000013 | 53321431 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,751,314 | 0.000000 | 53321431 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,710,138 | 0.017257 | 53321431 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,676,547 | 424.511055 | 53321431 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,639,252 | 0.000013 | 53321431 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,590,828 | 2,241.609965 | 53321431 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,579,060 | 0.000013 | 53321431 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,540,980 | 1.502063 | 53321431 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/USDC | 3000 | 1,523,040 | 2,247.471884 | 53321431 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,358 | 0.825821 | 53321431 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,425,396 | 0.000013 | 53321431 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/AERO | 3000 | 1,418,714 | 3,590.305722 | 53321431 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,333,731 | 0.005248 | 53321431 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,298,635 | 14,584.216380 | 53321431 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,281,219 | 2,241.476096 | 53321431 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,176,817 | 70.165644 | 53321431 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,112,724 | 35,677,478.940151 | 53321431 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,686 | 513,309.025665 | 53321431 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,034,690 | 21,100,335.940655 | 53321431 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,019,208 | 73,807.695107 | 53321431 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 992,529 | 19.362083 | 53321431 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 978,699 | 0.000000 | 53321431 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/VVV | 10000 | 966,171 | 100.544357 | 53321431 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | USDC/NOCK | 3000 | 960,678 | 67.831393 | 53321431 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 950,994 | 0.044915 | 53321431 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 930,119 | 1,213,242.460882 | 53321431 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 920,025 | 2,235.963257 | 53321431 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 902,937 | 1,059.164650 | 53321431 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 862,495 | 3,585.793582 | 53321431 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 861,509 | 0.000553 | 53321431 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 846,054 | 19.152690 | 53321431 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 821,298 | 0.060664 | 53321431 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 758,759 | 0.802842 | 53321431 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 734,709 | 0.000265 | 53321431 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,645 | 0.591198 | 53321431 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 724,103 | 4,523,498.946066 | 53321431 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 681,834 | 0.000008 | 53321431 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 660,020 | 2.331780 | 53321431 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 659,926 | 145,365.760640 | 53321431 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 657,690 | 516,022.969830 | 53321431 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 626,810 | 0.496993 | 53321431 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 614,429 | 0.093516 | 53321431 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 601,982 | 0.916505 | 53321431 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2736 | 546,136 | 1,059.488940 | 53321431 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 3464 ; routes examinées : 65005424 ; candidats optimisés : 173802 ; net attendu > 0 : 128 ; dernier cycle 99.0 ms
- Rejets (moteur) : {'spread_below_threshold': 63863306, 'liquidity_below_min': 957924, 'negative_expected_net': 173674, 'unquotable': 6928, 'borrow_bound_too_small': 3464}
- Enregistrements de la session : 173802 ; net attendu > 0 : 128 ; simulés (eth_call de la vraie tx) : 8 (ok 5, échec 3) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 173802} ; motifs de rejet : {'below_safety_margin': 92, 'negative_expected_net': 173674, 'p_lower_below_threshold': 124, 'reliability_not_demonstrated': 4, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 75.212964 USDC | 0.037095 USDC | 0.000000 USDC | 0.006740 USDC | 0.030355 USDC (0.0279 €) | — | 4.04 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 75.212964 USDC | 0.037095 USDC | 0.000000 USDC | 0.006740 USDC | 0.030355 USDC (0.0279 €) | — | 4.04 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.033693 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0279 €) | 0.000014 WETH | 4.02 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.033693 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0279 €) | — | 4.02 | 0.174 (n=238) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 73.149899 USDC | 0.033100 USDC | 0.000000 USDC | 0.006740 USDC | 0.026360 USDC (0.0243 €) | — | 3.60 | 0.119 (n=487) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 73.149899 USDC | 0.033100 USDC | 0.000000 USDC | 0.006740 USDC | 0.026360 USDC (0.0243 €) | — | 3.60 | 0.119 (n=487) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53321361 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.032654 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0242 €) | 0.000012 WETH | 3.60 | 0.119 (n=487) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53321361 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.032654 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0242 €) | — | 3.60 | 0.119 (n=487) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 71.351397 USDC | 0.031343 USDC | 0.000000 USDC | 0.006740 USDC | 0.024603 USDC (0.0226 €) | — | 3.45 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 71.351397 USDC | 0.031343 USDC | 0.000000 USDC | 0.006740 USDC | 0.024603 USDC (0.0226 €) | — | 3.45 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.031894 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0226 €) | 0.000011 WETH | 3.44 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.031894 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0226 €) | — | 3.44 | 0.174 (n=238) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.17<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 70.949596 USDC | 0.031200 USDC | 0.000000 USDC | 0.006740 USDC | 0.024460 USDC (0.0225 €) | — | 3.45 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 70.949596 USDC | 0.031200 USDC | 0.000000 USDC | 0.006740 USDC | 0.024460 USDC (0.0225 €) | — | 3.45 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.031863 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0225 €) | — | 3.43 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.031863 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0225 €) | — | 3.43 | 0.174 (n=238) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 71.309372 USDC | 0.031179 USDC | 0.000000 USDC | 0.006740 USDC | 0.024439 USDC (0.0225 €) | — | 3.43 | 0.119 (n=487) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 71.309372 USDC | 0.031179 USDC | 0.000000 USDC | 0.006740 USDC | 0.024439 USDC (0.0225 €) | — | 3.43 | 0.119 (n=487) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53321361 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.031857 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0225 €) | — | 3.42 | 0.119 (n=487) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53321361 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.031857 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0225 €) | — | 3.42 | 0.119 (n=487) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 62.681656 USDC | 0.029354 USDC | 0.000000 USDC | 0.006431 USDC | 0.022923 USDC (0.0211 €) | — | 3.66 | 0.114 (n=188) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 62.681656 USDC | 0.029354 USDC | 0.000000 USDC | 0.006431 USDC | 0.022923 USDC (0.0211 €) | — | 3.66 | 0.114 (n=188) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53321361 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.028211 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0211 €) | — | 3.63 | 0.114 (n=188) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53321361 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→WETH | 0.028211 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0211 €) | — | 3.63 | 0.114 (n=188) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53321361 | USDC→[uniswap_v3]→AERO→[aerodrome]→USDC | 65.372911 USDC | 0.023932 USDC | 0.000000 USDC | 0.004727 USDC | 0.019205 USDC (0.0177 €) | — | 2.94 | 0.236 (n=16) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 3911 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
