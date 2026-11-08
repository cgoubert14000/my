# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-08T13:42:51+00:00 ; durée 132.05 min ; blocs 54735330 → 54774927 (7287 vus)

## Connexion
- Requêtes RPC : 96385 ; erreurs : 5 ; latence p50/p95 : 293.3/1,401.5 ms
- Rafraîchissements d'état : 7287 ; âge des données au dernier bloc : 7.67 s ; changements de frais LP observés (pools à frais dynamiques) : 2078
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3 ; cycles déclenchés par événement : 2 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,236.97 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 470 pools, 276 jetons, 17574 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 96, aerodrome 197, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 168 (rejetés 2) → 573 jetons ; pools candidats 3668 (énumérés 291, par paires 0), mesurés 473, sous le plancher de 10000.0 $ : 3 → gardés 470 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2233.787841, 'cbBTC': 75908.696855, 'AERO': 0.601233}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,448,045 | 2,236.970068 | 54774951 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,891,790 | 0.029470 | 54774951 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,248,599 | 0.000013 | 54774951 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,168,648 | 0.029508 | 54774951 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,532,400 | 2,235.043941 | 54774951 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,368,687 | 107.678278 | 54774951 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,407,322 | 0.001542 | 54774951 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,167,621 | 0.029459 | 54774951 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,793,510 | 1.685363 | 54774951 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,187,679 | 2,234.426362 | 54774951 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,994,944 | 0.999364 | 54774951 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,285,477 | 43,384.927611 | 54774951 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,175,901 | 2,234.542170 | 54774951 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,453,236 | 0.029491 | 54774951 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,098,348 | 1,152,023.747540 | 54774951 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 484 | 1,740,192 | 0.000013 | 54774951 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,646,605 | 0.000013 | 54774951 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,632,110 | 0.006427 | 54774951 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,619,686 | 0.000000 | 54774951 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,560,243 | 0.015432 | 54774951 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,515,085 | 448.413587 | 54774951 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,510,316 | 0.000013 | 54774951 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,481,315 | 1.409694 | 54774951 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,403 | 0.824204 | 54774951 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,376,158 | 3,770.398561 | 54774951 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,547 | 2,239.906380 | 54774951 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,296,439 | 2,240.754691 | 54774951 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,257,475 | 15,202.124543 | 54774951 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,176,801 | 2,235.172393 | 54774951 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,360 | 77.001845 | 54774951 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,096,635 | 37,233,040.150614 | 54774951 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,040,706 | 106.924819 | 54774951 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,007,630 | 587,573.856908 | 54774951 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 978,176 | 23,253,793.049630 | 54774951 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 968,477 | 20.822368 | 54774951 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 963,564 | 0.000000 | 54774951 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/USDC | 10000 | 936,525 | 2,228.787480 | 54774951 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 931,821 | 1,070.868792 | 54774951 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 346 | 926,882 | 0.000013 | 54774951 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 922,440 | 73.643064 | 54774951 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 864,055 | 102,183.130833 | 54774951 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 824,992 | 0.048130 | 54774951 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| pancakeswap_v3 | QUID/USDC | 100 | 786,829 | 0.055372 | 54774951 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 781,173 | 3,746.240174 | 54774951 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 773,368 | 21.920791 | 54774951 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 758,833 | 0.799805 | 54774951 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 713,999 | 0.560616 | 54774951 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 682,645 | 0.000252 | 54774951 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 681,841 | 5,094,852.040714 | 54774951 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 669,763 | 0.566486 | 54774951 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 649,404 | 0.000008 | 54774951 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 644,939 | 152,129.716344 | 54774951 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 612,498 | 592,033.131419 | 54774951 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 574,755 | 0.039334 | 54774951 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 555,081 | 2.471831 | 54774951 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 526,384 | 878,850.269415 | 54774951 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 521,520 | 1,071.210548 | 54774951 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 521,166 | 0.077661 | 54774951 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 515,687 | 2,234.475294 | 54774951 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 514,757 | 6,925.527734 | 54774951 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 7288 ; routes examinées : 128079312 ; candidats optimisés : 395952 ; net attendu > 0 : 56 ; dernier cycle 444.0 ms
- Rejets (moteur) : {'spread_below_threshold': 126275331, 'liquidity_below_min': 1407738, 'negative_expected_net': 395896, 'cycle_budget_exhausted': 291}
- Enregistrements de la session : 395952 ; net attendu > 0 : 56 ; simulés (eth_call de la vraie tx) : 20 (ok 15, échec 5) ; étiquettes ghost N+1 : 3/20 positives
- Décisions : {'REJECTED': 395952} ; motifs de rejet : {'below_safety_margin': 21, 'negative_expected_net': 395896, 'p_lower_below_threshold': 53, 'reliability_not_demonstrated': 3, 'simulation_failed': 5, 'stale_data': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54752261 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 53.033191 USDC | 0.081325 USDC | 0.000000 USDC | 0.005016 USDC | 0.076309 USDC (0.0702 €) | — | 14.39 | 0.000 (n=104) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 13.194369 USDC | 0.033147 USDC | 0.000000 USDC | 0.007052 USDC | 0.026095 USDC (0.0240 €) | — | 19.78 | 0.073 (n=161) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54765034 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005888 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0239 €) | 0.000012 WETH | 19.79 | 0.073 (n=161) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 13.064750 USDC | 0.032618 USDC | 0.000000 USDC | 0.007052 USDC | 0.025566 USDC (0.0235 €) | — | 19.57 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005853 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0235 €) | 0.000011 WETH | 19.50 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 13.045392 USDC | 0.032484 USDC | 0.000000 USDC | 0.007052 USDC | 0.025432 USDC (0.0234 €) | — | 19.50 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005844 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0233 €) | 0.000011 WETH | 19.43 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 12.503198 USDC | 0.030778 USDC | 0.000000 USDC | 0.007052 USDC | 0.023726 USDC (0.0218 €) | — | 18.98 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005590 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0218 €) | — | 18.95 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 11.631050 USDC | 0.026180 USDC | 0.000000 USDC | 0.006405 USDC | 0.019775 USDC (0.0182 €) | — | 17.00 | 0.064 (n=182) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 54765034 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005218 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0182 €) | — | 16.93 | 0.064 (n=182) | REJECTED | p_lower_below_threshold(0.06<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 11.391643 USDC | 0.024800 USDC | 0.000000 USDC | 0.006713 USDC | 0.018087 USDC (0.0166 €) | — | 15.88 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.005096 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0166 €) | — | 15.86 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 11.086066 USDC | 0.023474 USDC | 0.000000 USDC | 0.006713 USDC | 0.016761 USDC (0.0154 €) | — | 15.12 | 0.073 (n=161) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54765034 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.004934 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0154 €) | — | 15.18 | 0.073 (n=161) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54751069 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 43.009373 USDC | 0.020298 USDC | 0.000000 USDC | 0.005015 USDC | 0.015283 USDC (0.0141 €) | 0.015283 USDC | 3.55 | 0.038 (n=377) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54765034 | USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 10.399086 USDC | 0.021106 USDC | 0.000000 USDC | 0.006713 USDC | 0.014393 USDC (0.0132 €) | — | 13.84 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54765034 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→TIG→[aerodrome_slipstream]→WETH | 0.004671 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0132 €) | — | 13.77 | 0.028 (n=102) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54763145 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 41.957568 USDC | 0.019038 USDC | 0.000000 USDC | 0.005016 USDC | 0.014022 USDC (0.0129 €) | 0.014022 USDC | 3.34 | 0.037 (n=380) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54769520 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 39.901717 USDC | 0.017278 USDC | 0.000000 USDC | 0.005023 USDC | 0.012255 USDC (0.0113 €) | — | 3.07 | 0.037 (n=381) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 54750059 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 19.333266 USDC | 0.015937 USDC | 0.000000 USDC | 0.005015 USDC | 0.010922 USDC (0.0100 €) | 0.010922 USDC | 5.65 | 0.075 (n=101) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 54762138 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 23.132441 USDC | 0.015539 USDC | 0.000000 USDC | 0.005015 USDC | 0.010524 USDC (0.0097 €) | 0.010524 USDC | 4.55 | 0.038 (n=378) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54739538 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 36.431398 USDC | 0.014605 USDC | 0.000000 USDC | 0.005015 USDC | 0.009590 USDC (0.0088 €) | 0.009590 USDC | 2.63 | 0.049 (n=273) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 54762451 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 22.008968 USDC | 0.014002 USDC | 0.000000 USDC | 0.005015 USDC | 0.008987 USDC (0.0083 €) | 0.008987 USDC | 4.08 | 0.037 (n=379) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 54759397 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 34.095867 USDC | 0.012875 USDC | 0.000000 USDC | 0.005014 USDC | 0.007861 USDC (0.0072 €) | — | 2.31 | 0.048 (n=277) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 6208 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
