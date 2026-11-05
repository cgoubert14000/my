# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T15:48:00+00:00 ; durée 3.05 min ; blocs 53552072 → 53552166 (83 vus)

## Connexion
- Requêtes RPC : 1037 ; erreurs : 0 ; latence p50/p95 : 150.1/1,420.6 ms
- Rafraîchissements d'état : 83 ; âge des données au dernier bloc : 3.25 s ; changements de frais LP observés (pools à frais dynamiques) : 360
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4810 ; cycles déclenchés par événement : 139 ; avance médiane sur le rafraîchissement multicall : 518 ms
- Gaz : base fee 0.006242 gwei ; prix ETH (pool le plus profond) : 2,281.32 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 485 pools, 283 jetons, 19058 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 102, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3708 (énumérés 302, par paires 0), mesurés 488, sous le plancher de 10000.0 $ : 3 → gardés 485 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2284.245505, 'cbBTC': 76255.016176, 'AERO': 0.595113}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,954,051 | 2,281.321432 | 53552165 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,633,137 | 0.029900 | 53552165 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,165,712 | 0.029911 | 53552165 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,010,715 | 0.000013 | 53552165 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,986,191 | 2,276.091325 | 53552166 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,336,690 | 113.059303 | 53552165 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,470,725 | 0.001557 | 53552165 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,112,525 | 1.685989 | 53552165 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,072,453 | 0.029899 | 53552165 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,122,500 | 2,276.664553 | 53552166 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 202 | 4,019,962 | 0.998641 | 53552165 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,395,152 | 42,254.183235 | 53552165 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 654 | 3,309,305 | 2,276.014411 | 53552166 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,598,431 | 0.029904 | 53552165 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,132,293 | 1,160,500.715180 | 53552165 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,791,977 | 0.007066 | 53552165 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 592 | 1,771,434 | 0.000013 | 53552165 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,665,586 | 0.000000 | 53552165 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,651,035 | 0.016560 | 53552166 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,630,953 | 0.000013 | 53552166 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,547,180 | 1.435490 | 53552165 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,538,235 | 453.992447 | 53552165 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,519,866 | 0.000013 | 53552165 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,337 | 0.816776 | 53552165 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,373,981 | 3,834.137098 | 53552165 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,338,682 | 2,276.250806 | 53552165 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,338,289 | 2,275.481189 | 53552165 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,264,204 | 15,154.513227 | 53552165 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,196,153 | 2,276.335027 | 53552165 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,150,853 | 73.366745 | 53552165 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,113,254 | 37,718,593.558080 | 53552165 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,035,759 | 0.000000 | 53552165 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,031,300 | 581,115.502229 | 53552165 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,020,155 | 113.158734 | 53552165 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,004,430 | 23,003,409.905224 | 53552165 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 973,439 | 66.170673 | 53552165 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 960,891 | 21.327678 | 53552165 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 942,934 | 2,296.376092 | 53552165 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 939,989 | 1,074.829184 | 53552165 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 360 | 927,888 | 0.000013 | 53552165 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 898,211 | 98,403.823090 | 53552165 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 870,455 | 0.000548 | 53552165 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 831,087 | 0.049725 | 53552165 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 798,548 | 0.057134 | 53552165 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 798,372 | 3,833.115042 | 53552165 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 786,046 | 21.407928 | 53552165 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 774,072 | 0.799698 | 53552165 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 706,228 | 0.560957 | 53552165 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 699,725 | 5,029,134.689723 | 53552165 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 686,053 | 0.000245 | 53552165 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 683,903 | 140,600.605119 | 53552165 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 656,105 | 0.545470 | 53552165 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 646,702 | 0.000008 | 53552165 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2198 | 627,900 | 585,646.680815 | 53552165 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 612,281 | 0.914215 | 53552165 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 608,588 | 2.479668 | 53552165 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 552,145 | 811,145.848212 | 53552165 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | FLOCK/USDC | 3000 | 549,625 | 0.036944 | 53552165 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 535,971 | 0.081368 | 53552165 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/DRV | 3000 | 532,619 | 6,727.846030 | 53552165 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 221 ; routes examinées : 4211818 ; candidats optimisés : 28429 ; net attendu > 0 : 215 ; dernier cycle 451.8 ms
- Rejets (moteur) : {'spread_below_threshold': 4049276, 'liquidity_below_min': 133325, 'negative_expected_net': 28214, 'cycle_budget_exhausted': 788}
- Enregistrements de la session : 28429 ; net attendu > 0 : 215 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 28429} ; motifs de rejet : {'below_safety_margin': 215, 'negative_expected_net': 28214, 'p_lower_below_threshold': 174, 'reliability_not_demonstrated': 41}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53552124 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010531 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1005 €) | — | 1.36 | 0.169 (n=990) | REJECTED | below_safety_margin(143<210), p_lower_below_threshold(0.17<0.75) |
| 53552125 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010531 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1005 €) | — | 1.36 | 0.169 (n=990) | REJECTED | below_safety_margin(143<210), p_lower_below_threshold(0.17<0.75) |
| 53552124 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.369676 WETH | 0.000052 WETH | 0.000000 WETH | 0.000004 WETH | 0.000048 WETH (0.1002 €) | — | 1.29 | 0.169 (n=990) | REJECTED | below_safety_margin(47724687505048<73935145396600), p_lower_below_threshold(0.17<0.75) |
| 53552125 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.369676 WETH | 0.000052 WETH | 0.000000 WETH | 0.000004 WETH | 0.000048 WETH (0.1002 €) | — | 1.29 | 0.169 (n=990) | REJECTED | below_safety_margin(47724687505048<73935145396600), p_lower_below_threshold(0.17<0.75) |
| 53552124 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 797.030095 USDC | 0.118081 USDC | 0.000000 USDC | 0.009775 USDC | 0.108306 USDC (0.0996 €) | — | 1.36 | 0.169 (n=990) | REJECTED | below_safety_margin(108306<159406), p_lower_below_threshold(0.17<0.75) |
| 53552125 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 797.030095 USDC | 0.118081 USDC | 0.000000 USDC | 0.009775 USDC | 0.108306 USDC (0.0996 €) | — | 1.36 | 0.169 (n=990) | REJECTED | below_safety_margin(108306<159406), p_lower_below_threshold(0.17<0.75) |
| 53552124 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009681 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0822 €) | — | 1.21 | 0.030 (n=27) | REJECTED | below_safety_margin(117<193), reliability_not_demonstrated |
| 53552125 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.009681 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0822 €) | — | 1.21 | 0.030 (n=27) | REJECTED | below_safety_margin(117<193), reliability_not_demonstrated |
| 53552124 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.337575 WETH | 0.000043 WETH | 0.000000 WETH | 0.000004 WETH | 0.000039 WETH (0.0819 €) | — | 1.15 | 0.030 (n=27) | REJECTED | below_safety_margin(38984409816663<67514937849196), reliability_not_demonstrated |
| 53552125 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.337575 WETH | 0.000043 WETH | 0.000000 WETH | 0.000004 WETH | 0.000039 WETH (0.0819 €) | — | 1.15 | 0.030 (n=27) | REJECTED | below_safety_margin(38984409816663<67514937849196), reliability_not_demonstrated |
| 53552124 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 761.511216 USDC | 0.099005 USDC | 0.000000 USDC | 0.010223 USDC | 0.088782 USDC (0.0817 €) | — | 1.17 | 0.030 (n=27) | REJECTED | below_safety_margin(88782<152302), reliability_not_demonstrated |
| 53552125 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 761.511216 USDC | 0.099005 USDC | 0.000000 USDC | 0.010223 USDC | 0.088782 USDC (0.0817 €) | — | 1.17 | 0.030 (n=27) | REJECTED | below_safety_margin(88782<152302), reliability_not_demonstrated |
| 53552094 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.377697 WETH | 0.000043 WETH | 0.000000 WETH | 0.000005 WETH | 0.000039 WETH (0.0809 €) | — | 1.02 | 0.169 (n=990) | REJECTED | below_safety_margin(38517238762585<75539484499210), p_lower_below_threshold(0.17<0.75) |
| 53552094 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010559 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0809 €) | — | 1.09 | 0.169 (n=990) | REJECTED | below_safety_margin(115<211), p_lower_below_threshold(0.17<0.75) |
| 53552094 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.010559 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0809 €) | — | 1.09 | 0.169 (n=990) | REJECTED | below_safety_margin(115<211), p_lower_below_threshold(0.17<0.75) |
| 53552094 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.370453 WETH | 0.000043 WETH | 0.000000 WETH | 0.000005 WETH | 0.000038 WETH (0.0807 €) | — | 1.04 | 0.169 (n=990) | REJECTED | below_safety_margin(38424977488694<74090520069576), p_lower_below_threshold(0.17<0.75) |
| 53552094 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 874.372072 USDC | 0.097975 USDC | 0.000000 USDC | 0.010442 USDC | 0.087533 USDC (0.0805 €) | — | 1.00 | 0.169 (n=990) | REJECTED | below_safety_margin(87533<174874), p_lower_below_threshold(0.17<0.75) |
| 53552094 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 874.372072 USDC | 0.097975 USDC | 0.000000 USDC | 0.010482 USDC | 0.087493 USDC (0.0805 €) | — | 1.00 | 0.169 (n=990) | REJECTED | below_safety_margin(87493<174874), p_lower_below_threshold(0.17<0.75) |
| 53552148 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.153363 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0556 €) | — | 1.73 | 0.047 (n=232) | REJECTED | below_safety_margin(26503717233453<30672698535422), p_lower_below_threshold(0.05<0.75) |
| 53552094 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008078 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0556 €) | — | 0.98 | 0.169 (n=990) | REJECTED | below_safety_margin(79<161), p_lower_below_threshold(0.17<0.75) |
| 53552094 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008078 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0556 €) | — | 0.98 | 0.169 (n=990) | REJECTED | below_safety_margin(79<161), p_lower_below_threshold(0.17<0.75) |
| 53552148 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 348.057815 USDC | 0.067581 USDC | 0.000000 USDC | 0.007224 USDC | 0.060357 USDC (0.0555 €) | — | 1.73 | 0.047 (n=232) | REJECTED | below_safety_margin(60357<69611), p_lower_below_threshold(0.05<0.75) |
| 53552094 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.293602 WETH | 0.000031 WETH | 0.000000 WETH | 0.000005 WETH | 0.000026 WETH (0.0554 €) | — | 0.90 | 0.169 (n=990) | REJECTED | below_safety_margin(26360416509753<58720329639239), p_lower_below_threshold(0.17<0.75) |
| 53552094 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.286377 WETH | 0.000031 WETH | 0.000000 WETH | 0.000005 WETH | 0.000026 WETH (0.0553 €) | — | 0.92 | 0.169 (n=990) | REJECTED | below_safety_margin(26305803277713<57275306556741), p_lower_below_threshold(0.17<0.75) |
| 53552094 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 697.453713 USDC | 0.070126 USDC | 0.000000 USDC | 0.010442 USDC | 0.059684 USDC (0.0549 €) | — | 0.86 | 0.169 (n=990) | REJECTED | below_safety_margin(59684<139490), p_lower_below_threshold(0.17<0.75) |

## Fiabilité et décision
- Observations ghost : 5675 ; taux observé 0.157 ; borne inférieure crédible (0.9) 0.151 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
