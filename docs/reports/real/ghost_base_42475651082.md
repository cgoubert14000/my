# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T15:47:43+00:00 ; durée 256.91 min ; blocs 54735330 → 54812370 (13239 vus)

## Connexion
- Requêtes RPC : 177203 ; erreurs : 33 ; latence p50/p95 : 453.9/1,422.6 ms
- Rafraîchissements d'état : 13239 ; âge des données au dernier bloc : 8.8 s ; changements de frais LP observés (pools à frais dynamiques) : 3681
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3 ; cycles déclenchés par événement : 2 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,236.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17574 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2233.787841, 'cbBTC': 75908.696855, 'AERO': 0.601233}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,504,303 | 2,236.975202 | 54812397 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,890,790 | 0.029459 | 54812397 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,291,253 | 0.000013 | 54812397 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,170,053 | 0.029508 | 54812397 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,535,457 | 2,238.629800 | 54812397 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,360,804 | 107.909451 | 54812397 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,411,897 | 0.001543 | 54812397 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,168,329 | 0.029463 | 54812397 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,785,243 | 1.679776 | 54812397 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,237,789 | 2,238.729631 | 54812397 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,996,398 | 0.999409 | 54812397 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,280,038 | 43,529.117317 | 54812397 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,176,093 | 2,238.692806 | 54812397 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,471,887 | 0.029491 | 54812397 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,094,229 | 1,156,565.173414 | 54812397 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,740,637 | 0.000013 | 54812397 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,648,839 | 0.000013 | 54812397 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,620,301 | 0.000000 | 54812397 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,607,136 | 0.006308 | 54812397 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,556,113 | 0.015376 | 54812397 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,515,868 | 447.675843 | 54812397 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,510,683 | 0.000013 | 54812397 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,468,118 | 1.431449 | 54812397 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,404 | 0.824203 | 54812397 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,378,963 | 3,766.361980 | 54812397 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,550 | 2,241.256617 | 54812397 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,295,490 | 2,245.053594 | 54812397 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,258,664 | 15,202.223925 | 54812397 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,172,716 | 2,238.403381 | 54812397 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54812397 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,979 | 37,198,309.032465 | 54812397 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,039,264 | 107.300793 | 54812397 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,005,103 | 592,011.578862 | 54812397 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 984,610 | 23,001,895.633916 | 54812397 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 967,445 | 20.903038 | 54812397 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 963,576 | 0.000000 | 54812397 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 936,526 | 2,228.787428 | 54812397 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 927,280 | 1,077.790796 | 54812397 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 927,189 | 0.000013 | 54812397 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,229 | 74.158461 | 54812397 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 864,705 | 102,030.046449 | 54812397 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 823,646 | 0.048246 | 54812397 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 784,219 | 0.054988 | 54812397 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 782,073 | 3,749.146310 | 54812397 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 771,709 | 21.986893 | 54812397 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 758,835 | 0.799805 | 54812397 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 711,365 | 0.557828 | 54812397 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 681,479 | 5,100,296.216846 | 54812397 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,111 | 0.000251 | 54812397 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 669,763 | 0.566486 | 54812397 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 650,899 | 0.000008 | 54812397 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 646,564 | 151,368.383688 | 54812397 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 610,094 | 595,663.521849 | 54812397 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 578,999 | 0.039779 | 54812397 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 555,082 | 2.471831 | 54812397 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 521,914 | 0.077741 | 54812397 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 521,871 | 899,673.035280 | 54812397 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 518,657 | 1,077.331382 | 54812397 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/USDC | 100 | 515,501 | 2,238.661185 | 54812397 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 512,634 | 6,983.016746 | 54812397 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 13240 ; routes examinées : 232679760 ; candidats optimisés : 721721 ; net attendu > 0 : 174 ; dernier cycle 291.0 ms
- Rejets (moteur) : {'spread_below_threshold': 229172294, 'liquidity_below_min': 2785325, 'negative_expected_net': 721547, 'cycle_budget_exhausted': 420}
- Enregistrements de la session : 721721 ; net attendu > 0 : 174 ; simulés (eth_call de la vraie tx) : 44 (ok 39, échec 5) ; étiquettes ghost N+1 : 6/44 positives
- Décisions : {'REJECTED': 721721} ; motifs de rejet : {'below_safety_margin': 76, 'negative_expected_net': 721547, 'p_lower_below_threshold': 165, 'reliability_not_demonstrated': 9, 'simulation_failed': 5, 'stale_data': 18}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54795865 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,312.919690 USDC | 0.156719 USDC | 0.000000 USDC | 0.007742 USDC | 0.148977 USDC (0.1371 €) | — | 1.13 | 0.029 (n=28) | REJECTED | below_safety_margin(148977<262583), reliability_not_demonstrated |
| 54795865 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017636 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1369 €) | — | 1.11 | 0.029 (n=28) | REJECTED | below_safety_margin(196<352), reliability_not_demonstrated |
| 54795865 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.602596 WETH | 0.000070 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1368 €) | — | 1.10 | 0.029 (n=28) | REJECTED | below_safety_margin(66488296471532<120519195077668), reliability_not_demonstrated |
| 54752261 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 53.033191 USDC | 0.081325 USDC | 0.000000 USDC | 0.005016 USDC | 0.076309 USDC (0.0702 €) | — | 14.39 | 0.000 (n=104) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54811352 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.064358 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0649 €) | 0.000032 WETH | 4.90 | 0.154 (n=847) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54795865 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 659.335242 USDC | 0.077419 USDC | 0.000000 USDC | 0.007063 USDC | 0.070356 USDC (0.0647 €) | — | 1.07 | 0.182 (n=1075) | REJECTED | below_safety_margin(70356<131867), p_lower_below_threshold(0.18<0.75) |
| 54795865 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.290179 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0644 €) | — | 1.08 | 0.182 (n=1075) | REJECTED | below_safety_margin(31303510620346<58035753397142), p_lower_below_threshold(0.18<0.75) |
| 54811352 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001817 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0643 €) | — | 5.06 | 0.154 (n=847) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54795865 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.008242 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0642 €) | — | 1.12 | 0.182 (n=1075) | REJECTED | below_safety_margin(92<164), p_lower_below_threshold(0.18<0.75) |
| 54811352 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001345 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0447 €) | — | 4.76 | 0.154 (n=847) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54795891 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.007171 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0447 €) | — | 0.89 | 0.182 (n=1075) | REJECTED | below_safety_margin(64<143), p_lower_below_threshold(0.18<0.75) |
| 54795891 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 546.617845 USDC | 0.055632 USDC | 0.000000 USDC | 0.007063 USDC | 0.048569 USDC (0.0447 €) | — | 0.89 | 0.182 (n=1075) | REJECTED | below_safety_margin(48569<109323), p_lower_below_threshold(0.18<0.75) |
| 54811352 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.051522 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0446 €) | 0.000022 WETH | 4.21 | 0.154 (n=847) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54795891 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.247145 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0446 €) | — | 0.88 | 0.182 (n=1075) | REJECTED | below_safety_margin(21682871203814<49428913014412), p_lower_below_threshold(0.18<0.75) |
| 54795865 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004958 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0314 €) | — | 0.91 | 0.182 (n=1075) | REJECTED | below_safety_margin(45<99), p_lower_below_threshold(0.18<0.75) |
| 54795865 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.185116 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0311 €) | — | 0.82 | 0.182 (n=1075) | REJECTED | below_safety_margin(15115540720302<37023254389355), p_lower_below_threshold(0.18<0.75) |
| 54795865 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 376.681616 USDC | 0.040998 USDC | 0.000000 USDC | 0.007402 USDC | 0.033596 USDC (0.0309 €) | — | 0.89 | 0.182 (n=1075) | REJECTED | below_safety_margin(33596<75336), p_lower_below_threshold(0.18<0.75) |
| 54811352 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.045366 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0284 €) | 0.000014 WETH | 3.04 | 0.154 (n=847) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 54811352 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001385 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0279 €) | — | 2.89 | 0.182 (n=1077) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 54801646 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→FLOCK→[uniswap_v3]→USDC | 18.934124 USDC | 0.035331 USDC | 0.000000 USDC | 0.006415 USDC | 0.028916 USDC (0.0266 €) | — | 15.27 | 0.125 (n=48) | REJECTED | stale_data(4127ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 54801646 | WETH→[aerodrome]→FLOCK→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.008508 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0266 €) | 0.000013 WETH | 15.19 | 0.125 (n=48) | REJECTED | stale_data(4124ms>4000.0), p_lower_below_threshold(0.13<0.75) |
| 54801646 | USDC→[aerodrome_slipstream]→WETH→[aerodrome]→FLOCK→[uniswap_v3]→USDC | 18.788314 USDC | 0.034667 USDC | 0.000000 USDC | 0.006415 USDC | 0.028252 USDC (0.0260 €) | — | 15.04 | 0.064 (n=182) | REJECTED | stale_data(4132ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54801646 | WETH→[aerodrome]→FLOCK→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.008416 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0260 €) | 0.000013 WETH | 15.00 | 0.064 (n=182) | REJECTED | stale_data(4130ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54801646 | USDC→[uniswap_v3]→WETH→[aerodrome]→FLOCK→[uniswap_v3]→USDC | 18.655207 USDC | 0.034340 USDC | 0.000000 USDC | 0.006415 USDC | 0.027925 USDC (0.0257 €) | — | 14.97 | 0.064 (n=182) | REJECTED | stale_data(4137ms>4000.0), p_lower_below_threshold(0.06<0.75) |
| 54801646 | WETH→[aerodrome]→FLOCK→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.008391 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0257 €) | 0.000012 WETH | 14.87 | 0.064 (n=182) | REJECTED | stale_data(4135ms>4000.0), p_lower_below_threshold(0.06<0.75) |

## Fiabilité et décision
- Observations ghost : 6232 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
