# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-28T05:39:50+00:00 ; durée 9.11 min ; blocs 53188044 → 53188321 (272 vus)

## Connexion
- Requêtes RPC : 3220 ; erreurs : 0 ; latence p50/p95 : 204.4/1,464.4 ms
- Rafraîchissements d'état : 273 ; âge des données au dernier bloc : 0.93 s ; changements de frais LP observés (pools à frais dynamiques) : 219
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2166 ; cycles déclenchés par événement : 313 ; avance médiane sur le rafraîchissement multicall : 438 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,356.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 521 pools, 302 jetons, 18962 routes
- Par DEX : uniswap_v3 147, aerodrome_slipstream 121, aerodrome 210, pancakeswap_v3 28, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 184 (rejetés 2) → 589 jetons ; pools candidats 3762 (énumérés 330, par paires 0), mesurés 523, sous le plancher de 10000.0 $ : 2 → gardés 521 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2356.459313, 'cbBTC': 80857.377983, 'AERO': 0.694089}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,182,583 | 2,356.418966 | 53188321 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,703,768 | 0.029089 | 53188321 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,648,690 | 0.000012 | 53188321 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,497,190 | 0.029105 | 53188321 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,432,813 | 2,350.518091 | 53188321 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,365,537 | 96.334359 | 53188321 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,066,384 | 0.001647 | 53188321 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,867,630 | 1.442155 | 53188321 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,747,217 | 0.029077 | 53188321 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 5,048,291 | 2,350.216056 | 53188321 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,481,349 | 2,350.178132 | 53188321 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,265,294 | 0.998870 | 53188321 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,771,026 | 36,548.742805 | 53188321 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,966,618 | 0.029116 | 53188321 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2781 | 2,528,263 | 96.372415 | 53188321 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,459,980 | 0.000012 | 53188321 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,151,011 | 1,216,715.810354 | 53188321 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 2,075,024 | 2,356.674248 | 53188321 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,842,760 | 0.019037 | 53188321 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,830,947 | 0.000000 | 53188321 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,800,182 | 395.082430 | 53188321 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,700,567 | 0.000012 | 53188321 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,693,654 | 0.000012 | 53188321 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,693,080 | 0.000012 | 53188321 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,528,958 | 0.005851 | 53188321 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,280 | 1.658893 | 53188321 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,208 | 0.826416 | 53188321 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,454,981 | 3,393.522974 | 53188321 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,400,939 | 13,571.534533 | 53188321 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,261,200 | 0.000269 | 53188321 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,242,681 | 2,350.461197 | 53188321 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/AERO | 10000 | 1,201,813 | 3,369.352247 | 53188321 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,194,235 | 68.133836 | 53188321 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,192,220 | 0.000267 | 53188321 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,168,165 | 1,067,022.071576 | 53188321 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,165,891 | 36,230,754.358062 | 53188321 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,138,743 | 0.000000 | 53188321 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,130,087 | 498,229.837341 | 53188321 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,083,801 | 72,227.288837 | 53188321 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,063,762 | 21,141,464.036905 | 53188321 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,058,037 | 55.920422 | 53188321 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,047,629 | 16.659265 | 53188321 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,000,674 | 0.040999 | 53188321 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 999,432 | 95.658936 | 53188321 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 945,627 | 2,342.370626 | 53188321 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 933,515 | 1,061.435946 | 53188321 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 910,763 | 0.000560 | 53188321 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/msETH (stable) | 500 | 889,794 | 2.313211 | 53188321 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 883,507 | 17.831077 | 53188321 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 851,589 | 17.463606 | 53188321 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 850,936 | 2,356.529298 | 53188321 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 808,208 | 0.058660 | 53188321 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 797,824 | 0.803180 | 53188321 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 756,586 | 0.631577 | 53188321 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 755,754 | 0.000009 | 53188321 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 754,985 | 4,599,041.008140 | 53188321 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 714,100 | 137,102.136989 | 53188321 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2147 | 702,000 | 499,310.281777 | 53188321 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 679,956 | 0.582389 | 53188321 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 672,139 | 0.108225 | 53188321 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 585 ; routes examinées : 11092770 ; candidats optimisés : 31866 ; net attendu > 0 : 39 ; dernier cycle 149.3 ms
- Rejets (moteur) : {'spread_below_threshold': 10923831, 'liquidity_below_min': 128246, 'negative_expected_net': 31827, 'borrow_bound_too_small': 8760}
- Enregistrements de la session : 31866 ; net attendu > 0 : 39 ; simulés (eth_call de la vraie tx) : 4 (ok 0, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 31866} ; motifs de rejet : {'below_safety_margin': 1, 'negative_expected_net': 31827, 'p_lower_below_threshold': 26, 'price_impact': 2, 'reliability_not_demonstrated': 13, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.003143 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1141 €) | — | 167.43 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.383964 USDC | 0.131180 USDC | 0.000000 USDC | 0.007438 USDC | 0.123742 USDC (0.1138 €) | — | 167.58 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.003145 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1135 €) | — | 166.40 | 0.000 (n=23) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.003145 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1134 €) | — | 166.34 | 0.000 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.386026 USDC | 0.130499 USDC | 0.000000 USDC | 0.007438 USDC | 0.123061 USDC (0.1132 €) | — | 166.61 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.386509 USDC | 0.130461 USDC | 0.000000 USDC | 0.007438 USDC | 0.123023 USDC (0.1132 €) | — | 166.55 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.003142 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1128 €) | — | 165.64 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.384617 USDC | 0.129822 USDC | 0.000000 USDC | 0.007438 USDC | 0.122384 USDC (0.1126 €) | — | 165.73 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.003131 WETH | 0.000054 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1092 €) | — | 160.87 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.357162 USDC | 0.126296 USDC | 0.000000 USDC | 0.007796 USDC | 0.118500 USDC (0.1090 €) | — | 161.07 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.003122 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1081 €) | — | 159.73 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.346989 USDC | 0.124810 USDC | 0.000000 USDC | 0.007438 USDC | 0.117372 USDC (0.1080 €) | — | 159.76 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.003122 WETH | 0.000053 WETH | 0.000000 WETH | 0.000003 WETH | 0.000050 WETH (0.1080 €) | — | 159.50 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 7.347537 USDC | 0.124642 USDC | 0.000000 USDC | 0.007438 USDC | 0.117204 USDC (0.1078 €) | — | 159.51 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 6.829681 USDC | 0.093763 USDC | 0.000000 USDC | 0.007438 USDC | 0.086325 USDC (0.0794 €) | — | 126.40 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[uniswap_v2]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 6.818773 USDC | 0.093010 USDC | 0.000000 USDC | 0.006707 USDC | 0.086303 USDC (0.0794 €) | — | 126.57 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.002890 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0792 €) | — | 126.36 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v2]→WETH | 0.002885 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0791 €) | — | 126.54 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[aerodrome]→WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC | 6.829772 USDC | 0.089096 USDC | 0.000000 USDC | 0.007113 USDC | 0.081983 USDC (0.0754 €) | — | 120.04 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→USDC→[aerodrome]→WETH | 0.002888 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0751 €) | — | 120.00 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53188189 | USDC→[uniswap_v3]→TIG→[aerodrome_slipstream]→USDC | 2.566552 USDC | 0.024875 USDC | 0.000000 USDC | 0.005291 USDC | 0.019584 USDC (0.0180 €) | — | 76.30 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[uniswap_v3]→TIG→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.001005 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0134 €) | — | 61.36 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→TIG→[aerodrome_slipstream]→USDC | 2.362732 USDC | 0.021562 USDC | 0.000000 USDC | 0.007081 USDC | 0.014481 USDC (0.0133 €) | — | 61.29 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53188189 | WETH→[uniswap_v3]→TIG→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.001011 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0131 €) | — | 59.79 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53188189 | WETH→[uniswap_v3]→TIG→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.001010 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0131 €) | — | 59.75 | 0.000 (n=32) | REJECTED | p_lower_below_threshold(0.00<0.75) |

## Fiabilité et décision
- Observations ghost : 2896 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
