# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-29T13:14:51+00:00 ; durée 220.17 min ; blocs 53238564 → 53245167 (6572 vus)

## Connexion
- Requêtes RPC : 79521 ; erreurs : 120 ; latence p50/p95 : 199.1/1,190.5 ms
- Rafraîchissements d'état : 6572 ; âge des données au dernier bloc : 3.53 s ; changements de frais LP observés (pools à frais dynamiques) : 7389
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 56795 ; cycles déclenchés par événement : 6657 ; avance médiane sur le rafraîchissement multicall : 497 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,321.53 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 513 pools, 295 jetons, 18990 routes
- Par DEX : uniswap_v3 144, aerodrome_slipstream 118, aerodrome 209, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 181 (rejetés 2) → 586 jetons ; pools candidats 3754 (énumérés 326, par paires 0), mesurés 515, sous le plancher de 10000.0 $ : 2 → gardés 513 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2317.952116, 'cbBTC': 80065.266817, 'AERO': 0.676266}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 157,165,600 | 2,321.528623 | 53245168 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,417,866 | 0.029035 | 53245168 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,691,328 | 0.000012 | 53245168 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,378,279 | 0.028962 | 53245168 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,237,557 | 2,324.025282 | 53245168 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,203,681 | 97.052845 | 53245168 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,963,958 | 0.001642 | 53245168 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,629,731 | 1.457921 | 53245168 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,748,317 | 0.029033 | 53245168 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 564 | 4,764,962 | 2,323.980675 | 53245168 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,396,037 | 2,323.796324 | 53245168 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,209,978 | 0.998875 | 53245168 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,665,124 | 37,549.088115 | 53245168 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,872,572 | 0.028976 | 53245168 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2715 | 2,490,809 | 97.079772 | 53245168 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,331,156 | 0.000012 | 53245168 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,120,923 | 1,214,695.556270 | 53245168 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | WETH/USDC | 3000 | 1,816,234 | 2,325.652032 | 53245168 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | XDP/USDC | 100 | 1,783,095 | 0.018509 | 53245168 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,768,618 | 402.341086 | 53245168 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,768,003 | 0.000000 | 53245168 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,708,220 | 0.000012 | 53245168 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,696,391 | 0.000012 | 53245168 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,598,260 | 0.000012 | 53245168 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,514,127 | 1.588199 | 53245168 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,794 | 0.827753 | 53245168 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,439,217 | 3,391.768796 | 53245168 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,399,508 | 0.005359 | 53245168 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,372,863 | 13,869.205319 | 53245168 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,260,597 | 2,324.021032 | 53245168 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,232,262 | 0.000264 | 53245168 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,189,401 | 68.688793 | 53245168 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,143,793 | 36,689,161.244872 | 53245168 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,139,482 | 0.000263 | 53245168 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome | WETH/WELL | 10000 | 1,134,671 | 1,096,974.389815 | 53245168 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,102,679 | 504,998.585982 | 53245168 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,090,275 | 0.000000 | 53245168 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/AERO | 10000 | 1,054,479 | 3,413.342265 | 53245168 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,053,523 | 21,687,126.272257 | 53245168 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,052,229 | 16.463552 | 53245168 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 1,047,510 | 74,987.145831 | 53245168 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,026,011 | 2,321.363082 | 53245168 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/VVV | 3000 | 1,025,681 | 0.041787 | 53245168 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 1,005,932 | 61.864439 | 53245168 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 997,208 | 97.590322 | 53245168 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 935,835 | 2,314.580420 | 53245168 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 917,171 | 1,063.436562 | 53245168 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 892,318 | 0.000554 | 53245168 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 868,668 | 18.339675 | 53245168 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 859,990 | 0.067038 | 53245168 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/msETH (stable) | 500 | 859,114 | 2.325336 | 53245168 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 841,194 | 17.447478 | 53245168 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 785,701 | 0.803812 | 53245168 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 743,677 | 0.000009 | 53245168 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 743,271 | 0.614661 | 53245168 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 742,706 | 4,613,664.883525 | 53245168 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 691,263 | 142,070.719438 | 53245168 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 686,951 | 501,362.160001 | 53245168 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 643,514 | 0.523311 | 53245168 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 632,349 | 0.098060 | 53245168 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 13228 ; routes examinées : 251199720 ; candidats optimisés : 792194 ; net attendu > 0 : 390 ; dernier cycle 295.1 ms
- Rejets (moteur) : {'spread_below_threshold': 247367325, 'liquidity_below_min': 2995943, 'negative_expected_net': 791804, 'unquotable': 31030, 'borrow_bound_too_small': 13228}
- Enregistrements de la session : 792194 ; net attendu > 0 : 390 ; simulés (eth_call de la vraie tx) : 30 (ok 17, échec 13) ; étiquettes ghost N+1 : 1/22 positives
- Décisions : {'REJECTED': 792194} ; motifs de rejet : {'below_safety_margin': 276, 'negative_expected_net': 791804, 'p_lower_below_threshold': 335, 'reliability_not_demonstrated': 55, 'simulation_failed': 13, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53243832 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 4,670.875033 USDC | 1.292294 USDC | 0.000000 USDC | 0.006270 USDC | 1.286024 USDC (1.1831 €) | — | 2.75 | 0.031 (n=115) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53243832 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 2.012810 WETH | 0.000556 WETH | 0.000000 WETH | 0.000003 WETH | 0.000554 WETH (1.1822 €) | — | 2.75 | 0.031 (n=115) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53241591 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,047.737281 USDC | 0.427881 USDC | 0.000000 USDC | 0.008033 USDC | 0.419848 USDC (0.3863 €) | — | 2.05 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53241591 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.025087 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3860 €) | — | 2.09 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53241591 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.895639 WETH | 0.000184 WETH | 0.000000 WETH | 0.000003 WETH | 0.000181 WETH (0.3859 €) | — | 2.02 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53243832 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 1,320.173909 USDC | 0.187829 USDC | 0.000000 USDC | 0.005213 USDC | 0.182616 USDC (0.1680 €) | — | 1.38 | 0.031 (n=115) | REJECTED | below_safety_margin(182616<264034), p_lower_below_threshold(0.03<0.75) |
| 53243832 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.569187 WETH | 0.000081 WETH | 0.000000 WETH | 0.000002 WETH | 0.000079 WETH (0.1678 €) | — | 1.38 | 0.031 (n=115) | REJECTED | below_safety_margin(78587161392028<113837453575124), p_lower_below_threshold(0.03<0.75) |
| 53241698 | USDC→[pancakeswap_v3]→USDT→[aerodrome_slipstream]→USDC | 2,678.487586 USDC | 0.183550 USDC | 0.000000 USDC | 0.005213 USDC | 0.178337 USDC (0.1641 €) | — | 0.67 | 0.031 (n=114) | REJECTED | below_safety_margin(178337<535697), stale_data(4055ms>4000.0), p_lower_below_threshold(0.03<0.75) |
| 53243832 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.025565 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1590 €) | — | 0.84 | 0.116 (n=433) | REJECTED | below_safety_margin(216<511), p_lower_below_threshold(0.12<0.75) |
| 53243832 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 2,082.075377 USDC | 0.179604 USDC | 0.000000 USDC | 0.006976 USDC | 0.172628 USDC (0.1588 €) | — | 0.83 | 0.116 (n=433) | REJECTED | below_safety_margin(172628<416415), p_lower_below_threshold(0.12<0.75) |
| 53243832 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.902805 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1587 €) | — | 0.82 | 0.116 (n=433) | REJECTED | below_safety_margin(74308574129412<180561070392077), p_lower_below_threshold(0.12<0.75) |
| 53241591 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,129.916305 USDC | 0.155581 USDC | 0.000000 USDC | 0.006976 USDC | 0.148605 USDC (0.1367 €) | — | 1.32 | 0.116 (n=433) | REJECTED | below_safety_margin(148605<225983), p_lower_below_threshold(0.12<0.75) |
| 53241591 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.474908 WETH | 0.000067 WETH | 0.000000 WETH | 0.000003 WETH | 0.000064 WETH (0.1364 €) | — | 1.34 | 0.116 (n=433) | REJECTED | below_safety_margin(63867422503409<94981669565194), p_lower_below_threshold(0.12<0.75) |
| 53241591 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.013036 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1363 €) | — | 1.42 | 0.116 (n=433) | REJECTED | below_safety_margin(185<260), p_lower_below_threshold(0.12<0.75) |
| 53243832 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 546.384942 USDC | 0.112676 USDC | 0.000000 USDC | 0.005917 USDC | 0.106759 USDC (0.0982 €) | — | 1.95 | 0.010 (n=28) | REJECTED | below_safety_margin(106759<109276), reliability_not_demonstrated |
| 53243832 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.235949 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000046 WETH (0.0981 €) | — | 1.95 | 0.010 (n=28) | REJECTED | below_safety_margin(45939997327107<47189791179572), reliability_not_demonstrated |
| 53240395 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 158.328234 USDC | 0.095113 USDC | 0.000000 USDC | 0.006969 USDC | 0.088144 USDC (0.0811 €) | — | 5.57 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.068238 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0809 €) | 0.000038 WETH | 5.56 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 142.168352 USDC | 0.084555 USDC | 0.000000 USDC | 0.006969 USDC | 0.077586 USDC (0.0714 €) | — | 5.46 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53240395 | WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.061509 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000033 WETH (0.0712 €) | 0.000033 WETH | 5.43 | 0.098 (n=336) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53241591 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 472.285882 USDC | 0.081642 USDC | 0.000000 USDC | 0.005564 USDC | 0.076078 USDC (0.0700 €) | — | 1.61 | 0.031 (n=113) | REJECTED | below_safety_margin(76078<94457), p_lower_below_threshold(0.03<0.75) |
| 53241591 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.204018 WETH | 0.000035 WETH | 0.000000 WETH | 0.000002 WETH | 0.000033 WETH (0.0699 €) | — | 1.60 | 0.031 (n=113) | REJECTED | below_safety_margin(32728571544694<40803505604798), p_lower_below_threshold(0.03<0.75) |
| 53240395 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC | 141.519830 USDC | 0.082593 USDC | 0.000000 USDC | 0.007321 USDC | 0.075272 USDC (0.0693 €) | — | 5.32 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | WETH→[uniswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.061011 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0691 €) | 0.000032 WETH | 5.31 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53240395 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 128.279120 USDC | 0.073907 USDC | 0.000000 USDC | 0.007321 USDC | 0.066586 USDC (0.0613 €) | — | 5.19 | 0.138 (n=187) | REJECTED | p_lower_below_threshold(0.14<0.75) |

## Fiabilité et décision
- Observations ghost : 3123 ; taux observé 0.099 ; borne inférieure crédible (0.9) 0.093 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
