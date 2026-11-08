# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T15:06:58+00:00 ; durée 216.15 min ; blocs 54735330 → 54800147 (11342 vus)

## Connexion
- Requêtes RPC : 151168 ; erreurs : 8 ; latence p50/p95 : 469.1/1,419.7 ms
- Rafraîchissements d'état : 11342 ; âge des données au dernier bloc : 8.17 s ; changements de frais LP observés (pools à frais dynamiques) : 3322
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
| uniswap_v3 | WETH/USDC | 3000 | 145,484,087 | 2,236.975372 | 54800174 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,888,782 | 0.029468 | 54800174 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,254,308 | 0.000013 | 54800174 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,169,039 | 0.029508 | 54800174 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,535,453 | 2,238.061432 | 54800174 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,367,076 | 107.725806 | 54800174 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,408,820 | 0.001543 | 54800174 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,167,821 | 0.029456 | 54800174 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,778,508 | 1.684514 | 54800174 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,237,826 | 2,237.816389 | 54800174 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,995,289 | 0.999409 | 54800174 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,280,744 | 43,510.373251 | 54800174 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,176,096 | 2,238.054226 | 54800174 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,449,999 | 0.029491 | 54800174 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,094,229 | 1,156,565.173414 | 54800174 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,740,326 | 0.000013 | 54800174 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,648,403 | 0.000013 | 54800174 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,619,692 | 0.000000 | 54800174 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,596,085 | 0.006255 | 54800174 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | XDP/USDC | 100 | 1,555,873 | 0.015372 | 54800174 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,515,628 | 447.904312 | 54800174 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,510,411 | 0.000013 | 54800174 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,315 | 1.409694 | 54800174 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,404 | 0.824203 | 54800174 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,376,626 | 3,776.566075 | 54800174 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,550 | 2,240.793010 | 54800174 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,295,490 | 2,243.905508 | 54800174 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,258,185 | 15,202.223925 | 54800174 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,172,713 | 2,238.221185 | 54800174 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54800174 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,097,806 | 37,112,829.904536 | 54800174 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,041,100 | 107.300876 | 54800174 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,005,418 | 591,455.255340 | 54800174 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 984,615 | 23,001,682.493794 | 54800174 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 967,329 | 20.897212 | 54800174 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 963,576 | 0.000000 | 54800174 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 936,526 | 2,228.787462 | 54800174 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 927,341 | 1,077.790756 | 54800174 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 926,968 | 0.000013 | 54800174 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 919,229 | 74.158461 | 54800174 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 864,705 | 102,030.046449 | 54800174 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 824,748 | 0.048146 | 54800174 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 784,889 | 0.055086 | 54800174 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 780,974 | 3,749.146310 | 54800174 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 771,842 | 21.981608 | 54800174 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 758,835 | 0.799805 | 54800174 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 711,729 | 0.557834 | 54800174 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 681,547 | 5,099,273.865922 | 54800174 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 681,315 | 0.000251 | 54800174 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 669,763 | 0.566486 | 54800174 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 649,666 | 0.000008 | 54800174 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 645,886 | 151,686.000638 | 54800174 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 610,394 | 595,888.173158 | 54800174 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 577,387 | 0.039611 | 54800174 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 555,082 | 2.471831 | 54800174 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 522,036 | 898,861.251831 | 54800174 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 518,668 | 1,078.117684 | 54800174 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 518,247 | 0.077054 | 54800174 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 515,710 | 2,237.733630 | 54800174 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 513,517 | 6,959.041456 | 54800174 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 11343 ; routes examinées : 199341882 ; candidats optimisés : 619143 ; net attendu > 0 : 116 ; dernier cycle 288.2 ms
- Rejets (moteur) : {'spread_below_threshold': 196201721, 'liquidity_below_min': 2520640, 'negative_expected_net': 619027, 'cycle_budget_exhausted': 378}
- Enregistrements de la session : 619143 ; net attendu > 0 : 116 ; simulés (eth_call de la vraie tx) : 29 (ok 24, échec 5) ; étiquettes ghost N+1 : 6/29 positives
- Décisions : {'REJECTED': 619143} ; motifs de rejet : {'below_safety_margin': 67, 'negative_expected_net': 619027, 'p_lower_below_threshold': 107, 'reliability_not_demonstrated': 9, 'simulation_failed': 5, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54795865 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,312.919690 USDC | 0.156719 USDC | 0.000000 USDC | 0.007742 USDC | 0.148977 USDC (0.1371 €) | — | 1.13 | 0.029 (n=28) | REJECTED | below_safety_margin(148977<262583), reliability_not_demonstrated |
| 54795865 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.017636 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1369 €) | — | 1.11 | 0.029 (n=28) | REJECTED | below_safety_margin(196<352), reliability_not_demonstrated |
| 54795865 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.602596 WETH | 0.000070 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1368 €) | — | 1.10 | 0.029 (n=28) | REJECTED | below_safety_margin(66488296471532<120519195077668), reliability_not_demonstrated |
| 54752261 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 53.033191 USDC | 0.081325 USDC | 0.000000 USDC | 0.005016 USDC | 0.076309 USDC (0.0702 €) | — | 14.39 | 0.000 (n=104) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54795865 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 659.335242 USDC | 0.077419 USDC | 0.000000 USDC | 0.007063 USDC | 0.070356 USDC (0.0647 €) | — | 1.07 | 0.182 (n=1075) | REJECTED | below_safety_margin(70356<131867), p_lower_below_threshold(0.18<0.75) |
| 54795865 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.290179 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0644 €) | — | 1.08 | 0.182 (n=1075) | REJECTED | below_safety_margin(31303510620346<58035753397142), p_lower_below_threshold(0.18<0.75) |
| 54795865 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.008242 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0642 €) | — | 1.12 | 0.182 (n=1075) | REJECTED | below_safety_margin(92<164), p_lower_below_threshold(0.18<0.75) |
| 54795891 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.007171 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0447 €) | — | 0.89 | 0.182 (n=1075) | REJECTED | below_safety_margin(64<143), p_lower_below_threshold(0.18<0.75) |
| 54795891 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 546.617845 USDC | 0.055632 USDC | 0.000000 USDC | 0.007063 USDC | 0.048569 USDC (0.0447 €) | — | 0.89 | 0.182 (n=1075) | REJECTED | below_safety_margin(48569<109323), p_lower_below_threshold(0.18<0.75) |
| 54795891 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.247145 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0446 €) | — | 0.88 | 0.182 (n=1075) | REJECTED | below_safety_margin(21682871203814<49428913014412), p_lower_below_threshold(0.18<0.75) |
| 54795865 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.004958 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0314 €) | — | 0.91 | 0.182 (n=1075) | REJECTED | below_safety_margin(45<99), p_lower_below_threshold(0.18<0.75) |
| 54795865 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.185116 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0311 €) | — | 0.82 | 0.182 (n=1075) | REJECTED | below_safety_margin(15115540720302<37023254389355), p_lower_below_threshold(0.18<0.75) |
| 54795865 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 376.681616 USDC | 0.040998 USDC | 0.000000 USDC | 0.007402 USDC | 0.033596 USDC (0.0309 €) | — | 0.89 | 0.182 (n=1075) | REJECTED | below_safety_margin(33596<75336), p_lower_below_threshold(0.18<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 13.194369 USDC | 0.033147 USDC | 0.000000 USDC | 0.007052 USDC | 0.026095 USDC (0.0240 €) | — | 19.78 | 0.073 (n=161) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54765034 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005888 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0239 €) | 0.000012 WETH | 19.79 | 0.073 (n=161) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 13.064750 USDC | 0.032618 USDC | 0.000000 USDC | 0.007052 USDC | 0.025566 USDC (0.0235 €) | — | 19.57 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005853 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0235 €) | 0.000011 WETH | 19.50 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 13.045392 USDC | 0.032484 USDC | 0.000000 USDC | 0.007052 USDC | 0.025432 USDC (0.0234 €) | — | 19.50 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005844 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0233 €) | 0.000011 WETH | 19.43 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 12.503198 USDC | 0.030778 USDC | 0.000000 USDC | 0.007052 USDC | 0.023726 USDC (0.0218 €) | — | 18.98 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005590 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0218 €) | — | 18.95 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54795891 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.155450 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0189 €) | — | 0.59 | 0.182 (n=1075) | REJECTED | below_safety_margin(9191096307420<31089951549577), p_lower_below_threshold(0.18<0.75) |
| 54795891 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003928 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0189 €) | — | 0.69 | 0.182 (n=1075) | REJECTED | below_safety_margin(27<78), p_lower_below_threshold(0.18<0.75) |
| 54795891 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 346.205657 USDC | 0.027823 USDC | 0.000000 USDC | 0.007402 USDC | 0.020421 USDC (0.0188 €) | — | 0.59 | 0.182 (n=1075) | REJECTED | below_safety_margin(20421<69241), p_lower_below_threshold(0.18<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 11.631050 USDC | 0.026180 USDC | 0.000000 USDC | 0.006405 USDC | 0.019775 USDC (0.0182 €) | — | 17.00 | 0.064 (n=182) | REJECTED | p_lower_below_threshold(0.06<0.75) |

## Fiabilité et décision
- Observations ghost : 6217 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
