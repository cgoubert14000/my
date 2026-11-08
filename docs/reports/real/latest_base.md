# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T01:30:49+00:00 ; durée 73.48 min ; blocs 54533288 → 54555306 (3538 vus)

## Connexion
- Requêtes RPC : 47860 ; erreurs : 5 ; latence p50/p95 : 359.4/1,522.5 ms
- Rafraîchissements d'état : 3538 ; âge des données au dernier bloc : 11.49 s ; changements de frais LP observés (pools à frais dynamiques) : 1312
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2408 ; cycles déclenchés par événement : 1110 ; avance médiane sur le rafraîchissement multicall : 427 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,231.65 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17708 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2231.621019, 'cbBTC': 75753.631297, 'AERO': 0.627658}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,612,882 | 2,231.650118 | 54555336 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,827,395 | 0.029490 | 54555336 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,221,637 | 0.000013 | 54555336 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,148,045 | 0.029508 | 54555336 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,066,774 | 2,232.230132 | 54555336 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,307,773 | 108.960676 | 54555336 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,390,576 | 0.001544 | 54555336 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,146,071 | 0.029490 | 54555336 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,916,625 | 1.620277 | 54555336 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,218,040 | 2,232.214956 | 54555336 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,983,168 | 0.999135 | 54555336 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,326,151 | 42,129.215374 | 54555336 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,179,145 | 2,232.068213 | 54555336 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,541,718 | 0.029493 | 54555336 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,097,549 | 1,147,424.274597 | 54555336 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,736,668 | 0.000013 | 54555336 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,674,951 | 0.006655 | 54555336 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,652,203 | 0.000013 | 54555336 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,617,349 | 0.000000 | 54555336 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,587,404 | 0.015808 | 54555336 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,518,773 | 441.395594 | 54555336 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,503,081 | 0.000013 | 54555336 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,474,935 | 1.429457 | 54555336 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,111 | 0.819634 | 54555336 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,403,609 | 3,616.360873 | 54555336 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,323,921 | 2,235.853410 | 54555336 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,321,376 | 2,236.169838 | 54555336 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,262,651 | 14,952.152405 | 54555336 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,184,627 | 2,232.264976 | 54555336 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,406 | 76.995559 | 54555336 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,100,848 | 36,496,596.545796 | 54555336 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,039,965 | 109.174187 | 54555336 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,007,862 | 582,409.226340 | 54555336 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 985,656 | 22,865,729.300087 | 54555336 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 978,287 | 20.202999 | 54555336 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 958,601 | 0.000000 | 54555336 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 935,580 | 2,228.787514 | 54555336 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 934,266 | 1,064.846863 | 54555336 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 924,462 | 0.000013 | 54555336 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 913,024 | 75.169821 | 54555336 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 865,645 | 101,384.412590 | 54555336 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 814,323 | 0.048826 | 54555336 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 795,789 | 3,590.072617 | 54555336 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,203 | 0.055576 | 54555336 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 784,189 | 21.496631 | 54555336 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 757,029 | 0.799805 | 54555336 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,283 | 0.564516 | 54555336 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 690,614 | 4,942,153.044546 | 54555336 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,408 | 0.000253 | 54555336 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 674,715 | 0.574532 | 54555336 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 663,034 | 0.000008 | 54555336 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 637,402 | 155,001.651293 | 54555336 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2144 | 613,910 | 585,874.599141 | 54555336 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 586,536 | 2.472338 | 54555336 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 582,831 | 0.040178 | 54555336 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 522,744 | 1,065.077921 | 54555336 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | cbBTC/EDGE | 7000 | 517,805 | 906,733.564978 | 54555336 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 514,105 | 2,232.035846 | 54555336 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 512,835 | 6,944.363312 | 54555336 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 502,116 | 0.073922 | 54555336 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 4647 ; routes examinées : 82289076 ; candidats optimisés : 210982 ; net attendu > 0 : 28 ; dernier cycle 279.1 ms
- Rejets (moteur) : {'spread_below_threshold': 80876652, 'liquidity_below_min': 1196735, 'negative_expected_net': 210954, 'borrow_bound_too_small': 4647, 'cycle_budget_exhausted': 60}
- Enregistrements de la session : 210982 ; net attendu > 0 : 28 ; simulés (eth_call de la vraie tx) : 3 (ok 3, échec 0) ; étiquettes ghost N+1 : 2/3 positives
- Décisions : {'REJECTED': 210982} ; motifs de rejet : {'below_safety_margin': 25, 'negative_expected_net': 210954, 'p_lower_below_threshold': 28, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54551500 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000853 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0090 €) | — | 1.52 | 0.183 (n=1067) | REJECTED | below_safety_margin(13<17), p_lower_below_threshold(0.18<0.75) |
| 54551501 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000853 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0090 €) | — | 1.52 | 0.183 (n=1067) | REJECTED | below_safety_margin(13<17), p_lower_below_threshold(0.18<0.75) |
| 54551501 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.036255 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 1.15 | 0.183 (n=1067) | REJECTED | below_safety_margin(4185190097130<7251029877697), p_lower_below_threshold(0.18<0.75) |
| 54551500 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.036255 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0086 €) | — | 1.15 | 0.183 (n=1067) | REJECTED | below_safety_margin(4184205607098<7251029877697), p_lower_below_threshold(0.18<0.75) |
| 54546106 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 20.233310 USDC | 0.011384 USDC | 0.000000 USDC | 0.005009 USDC | 0.006375 USDC (0.0059 €) | 0.006375 USDC | 3.15 | 0.028 (n=351) | REJECTED | stale_data(5009ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 54540962 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000659 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0056 €) | — | 1.21 | 0.183 (n=1067) | REJECTED | below_safety_margin(8<13), p_lower_below_threshold(0.18<0.75) |
| 54540963 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000659 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0056 €) | — | 1.21 | 0.183 (n=1067) | REJECTED | below_safety_margin(8<13), p_lower_below_threshold(0.18<0.75) |
| 54540964 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000659 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0056 €) | — | 1.21 | 0.183 (n=1067) | REJECTED | below_safety_margin(8<13), p_lower_below_threshold(0.18<0.75) |
| 54540962 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 46.321402 USDC | 0.012280 USDC | 0.000000 USDC | 0.006705 USDC | 0.005575 USDC (0.0051 €) | — | 1.20 | 0.183 (n=1067) | REJECTED | below_safety_margin(5575<9264), p_lower_below_threshold(0.18<0.75) |
| 54540963 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 46.321402 USDC | 0.012280 USDC | 0.000000 USDC | 0.006705 USDC | 0.005575 USDC (0.0051 €) | — | 1.20 | 0.183 (n=1067) | REJECTED | below_safety_margin(5575<9264), p_lower_below_threshold(0.18<0.75) |
| 54540964 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 46.321402 USDC | 0.012280 USDC | 0.000000 USDC | 0.006705 USDC | 0.005575 USDC (0.0051 €) | — | 1.20 | 0.183 (n=1067) | REJECTED | below_safety_margin(5575<9264), p_lower_below_threshold(0.18<0.75) |
| 54538348 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.003415 WETH | 0.000002 WETH | 0.000000 WETH | 0.000000 WETH | 0.000002 WETH (0.0033 €) | 0.000002 WETH | 4.76 | 0.264 (n=176) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 54546949 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 12.959888 USDC | 0.006993 USDC | 0.000000 USDC | 0.005009 USDC | 0.001984 USDC (0.0018 €) | — | 1.53 | 0.051 (n=85) | REJECTED | below_safety_margin(1984<2591), p_lower_below_threshold(0.05<0.75) |
| 54546950 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 12.959888 USDC | 0.006993 USDC | 0.000000 USDC | 0.005009 USDC | 0.001984 USDC (0.0018 €) | — | 1.53 | 0.051 (n=85) | REJECTED | below_safety_margin(1984<2591), p_lower_below_threshold(0.05<0.75) |
| 54538348 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→VIRTUAL→[uniswap_v3]→WETH | 0.002508 WETH | 0.000001 WETH | 0.000000 WETH | 0.000000 WETH | 0.000001 WETH (0.0010 €) | 0.000001 WETH | 2.01 | 0.315 (n=122) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 54551696 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.015937 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0008 €) | — | 0.25 | 0.183 (n=1067) | REJECTED | below_safety_margin(405150671800<3187443343208), p_lower_below_threshold(0.18<0.75) |
| 54551500 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000427 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.23 | 0.183 (n=1067) | REJECTED | below_safety_margin(1<8), p_lower_below_threshold(0.18<0.75) |
| 54551501 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000427 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.23 | 0.183 (n=1067) | REJECTED | below_safety_margin(1<8), p_lower_below_threshold(0.18<0.75) |
| 54551696 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000596 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.17 | 0.183 (n=1067) | REJECTED | below_safety_margin(1<11), p_lower_below_threshold(0.18<0.75) |
| 54545550 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 33.417142 USDC | 0.008035 USDC | 0.000000 USDC | 0.007381 USDC | 0.000654 USDC (0.0006 €) | — | 0.20 | 0.183 (n=1067) | REJECTED | below_safety_margin(654<6683), stale_data(6279ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54545551 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 33.417142 USDC | 0.008035 USDC | 0.000000 USDC | 0.007381 USDC | 0.000654 USDC (0.0006 €) | — | 0.20 | 0.183 (n=1067) | REJECTED | below_safety_margin(654<6683), stale_data(6442ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54545551 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 33.494906 USDC | 0.008035 USDC | 0.000000 USDC | 0.007381 USDC | 0.000654 USDC (0.0006 €) | — | 0.20 | 0.183 (n=1067) | REJECTED | below_safety_margin(654<6698), p_lower_below_threshold(0.18<0.75) |
| 54545551 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.015119 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.19 | 0.183 (n=1067) | REJECTED | below_safety_margin(289646265446<3023844617732), p_lower_below_threshold(0.18<0.75) |
| 54545550 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.015004 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.19 | 0.183 (n=1067) | REJECTED | below_safety_margin(289510121232<3000718006133), stale_data(6274ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 54545551 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.015004 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0006 €) | — | 0.19 | 0.183 (n=1067) | REJECTED | below_safety_margin(289510121232<3000718006133), stale_data(6437ms>4000.0), p_lower_below_threshold(0.18<0.75) |

## Fiabilité et décision
- Observations ghost : 6120 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
