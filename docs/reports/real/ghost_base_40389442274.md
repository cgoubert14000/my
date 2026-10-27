# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-27T01:19:05+00:00 ; durée 328.4 min ; blocs 53127443 → 53137294 (9669 vus)

## Connexion
- Requêtes RPC : 112713 ; erreurs : 270 ; latence p50/p95 : 290.1/1,307.2 ms
- Rafraîchissements d'état : 9669 ; âge des données au dernier bloc : 3.06 s ; changements de frais LP observés (pools à frais dynamiques) : 12946
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 27627 ; cycles déclenchés par événement : 2991 ; avance médiane sur le rafraîchissement multicall : 516 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,322.40 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 531 pools, 306 jetons, 19514 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 130, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 190 (rejetés 2) → 595 jetons ; pools candidats 3792 (énumérés 342, par paires 0), mesurés 533, sous le plancher de 10000.0 $ : 2 → gardés 531 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2315.799118, 'cbBTC': 79865.457277, 'AERO': 0.681738}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 156,369,031 | 2,322.398052 | 53137294 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,066,171 | 0.029021 | 53137294 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,158,779 | 0.028948 | 53137294 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,457,027 | 0.000012 | 53137294 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,660,716 | 92.688249 | 53137294 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,340,752 | 2,325.654650 | 53137294 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,033,585 | 1.477998 | 53137294 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,969,156 | 0.001642 | 53137294 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,380,749 | 0.029022 | 53137294 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 609 | 5,254,231 | 2,326.472906 | 53137294 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,550,178 | 2,326.593857 | 53137294 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,211,842 | 0.999452 | 53137294 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,778,149 | 35,367.270835 | 53137294 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,363,950 | 2,322.614696 | 53137294 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,189,000 | 0.028964 | 53137294 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2733 | 2,507,704 | 92.713550 | 53137294 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 496 | 2,451,202 | 0.000012 | 53137294 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,120,247 | 1,216,380.983500 | 53137294 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,834,843 | 0.000000 | 53137294 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,829,304 | 0.018674 | 53137294 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,760,880 | 405.030596 | 53137294 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 1,688,635 | 0.000012 | 53137294 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,677,526 | 0.000012 | 53137294 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,664,678 | 0.000012 | 53137294 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,555,047 | 0.000266 | 53137294 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,879 | 0.005885 | 53137294 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,925 | 0.826518 | 53137294 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53137294 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,432,575 | 3,435.894534 | 53137294 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,369,593 | 13,961.027058 | 53137294 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,254,097 | 2,325.654314 | 53137294 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,237,245 | 0.000267 | 53137294 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | USDC/SEND | 3000 | 1,217,284 | 65.578051 | 53137294 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/AERO | 10000 | 1,209,670 | 3,444.389703 | 53137294 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | DRB/WETH | 10000 | 1,147,483 | 0.000000 | 53137294 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/doginme | 10000 | 1,141,147 | 36,897,323.998965 | 53137294 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | WETH/WELL | 10000 | 1,138,891 | 1,090,993.540534 | 53137294 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,108,303 | 498,160.432548 | 53137294 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,070,073 | 72,177.779810 | 53137294 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,061,772 | 20,349,863.765579 | 53137294 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 1,039,232 | 57.962408 | 53137294 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,034,096 | 17.253491 | 53137294 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 1,002,934 | 0.039861 | 53137294 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 952,253 | 2,317.651270 | 53137294 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 918,981 | 1,082.492907 | 53137294 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/msETH (stable) | 500 | 907,813 | 2.309155 | 53137294 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 897,133 | 0.000560 | 53137294 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,175 | 17.934831 | 53137294 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,211 | 92.264655 | 53137294 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 860,328 | 17.175510 | 53137294 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v2 | WETH/USDC | 3000 | 845,299 | 2,330.898329 | 53137294 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | QUID/USDC | 100 | 800,844 | 0.057536 | 53137294 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 798,248 | 0.000008 | 53137294 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/wstETH | 3000 | 786,305 | 0.803179 | 53137294 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 742,136 | 0.619362 | 53137294 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 734,492 | 4,720,034.061906 | 53137294 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 700,302 | 138,415.538833 | 53137294 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 699,631 | 0.615511 | 53137294 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 692,772 | 500,478.077707 | 53137294 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 675,646 | 0.109245 | 53137294 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 12659 ; routes examinées : 247027726 ; candidats optimisés : 830440 ; net attendu > 0 : 396 ; dernier cycle 345.3 ms
- Rejets (moteur) : {'spread_below_threshold': 242565283, 'liquidity_below_min': 3218481, 'negative_expected_net': 830044, 'unquotable': 268452, 'pool_quarantined': 129664, 'borrow_bound_too_small': 12637, 'cycle_budget_exhausted': 2690}
- Enregistrements de la session : 830440 ; net attendu > 0 : 396 ; simulés (eth_call de la vraie tx) : 52 (ok 11, échec 41) ; étiquettes ghost N+1 : 3/47 positives
- Décisions : {'REJECTED': 830440} ; motifs de rejet : {'below_safety_margin': 198, 'negative_expected_net': 830044, 'p_lower_below_threshold': 305, 'price_impact': 14, 'reliability_not_demonstrated': 91, 'simulation_failed': 41, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.023209 WETH | 0.000907 WETH | 0.000000 WETH | 0.000003 WETH | 0.000904 WETH (1.9240 €) | — | 389.33 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53128709 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 53.644555 USDC | 2.095475 USDC | 0.000000 USDC | 0.006955 USDC | 2.088520 USDC (1.9214 €) | — | 389.33 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.022925 WETH | 0.000895 WETH | 0.000000 WETH | 0.000003 WETH | 0.000892 WETH (1.8994 €) | — | 389.10 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53128709 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 53.015983 USDC | 2.070165 USDC | 0.000000 USDC | 0.007307 USDC | 2.062858 USDC (1.8978 €) | — | 389.10 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.022608 WETH | 0.000882 WETH | 0.000000 WETH | 0.000003 WETH | 0.000879 WETH (1.8717 €) | — | 388.80 | 0.000 (n=27) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53128709 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 52.260446 USDC | 2.038830 USDC | 0.000000 USDC | 0.006955 USDC | 2.031875 USDC (1.8693 €) | — | 388.80 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 47.739345 USDC | 1.869729 USDC | 0.000000 USDC | 0.006955 USDC | 1.862774 USDC (1.7138 €) | — | 390.20 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.020555 WETH | 0.000805 WETH | 0.000000 WETH | 0.000003 WETH | 0.000802 WETH (1.7078 €) | — | 390.19 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.018327 WETH | 0.000721 WETH | 0.000000 WETH | 0.000003 WETH | 0.000718 WETH (1.5298 €) | — | 392.01 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 42.364576 USDC | 1.667668 USDC | 0.000000 USDC | 0.006955 USDC | 1.660713 USDC (1.5279 €) | — | 392.01 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.018262 WETH | 0.000719 WETH | 0.000000 WETH | 0.000003 WETH | 0.000716 WETH (1.5243 €) | — | 392.01 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 42.219910 USDC | 1.662016 USDC | 0.000000 USDC | 0.006955 USDC | 1.655061 USDC (1.5227 €) | — | 392.01 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53128709 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 39.634488 USDC | 1.562977 USDC | 0.000000 USDC | 0.006955 USDC | 1.556022 USDC (1.4315 €) | — | 392.59 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53128709 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.017102 WETH | 0.000674 WETH | 0.000000 WETH | 0.000003 WETH | 0.000671 WETH (1.4296 €) | — | 392.59 | 0.000 (n=27) | REJECTED | reliability_not_demonstrated |
| 53135532 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 43.372987 USDC | 0.284533 USDC | 0.000000 USDC | 0.006971 USDC | 0.277562 USDC (0.2554 €) | — | 63.99 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53135532 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.018649 WETH | 0.000122 WETH | 0.000000 WETH | 0.000003 WETH | 0.000119 WETH (0.2547 €) | — | 63.99 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53135532 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 43.039027 USDC | 0.282588 USDC | 0.000000 USDC | 0.006971 USDC | 0.275617 USDC (0.2536 €) | — | 64.04 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53135532 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.018504 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2529 €) | — | 64.03 | 0.000 (n=28) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53135532 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 34.256223 USDC | 0.222738 USDC | 0.000000 USDC | 0.006971 USDC | 0.215767 USDC (0.1985 €) | — | 62.99 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53135532 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 34.221651 USDC | 0.222655 USDC | 0.000000 USDC | 0.006971 USDC | 0.215684 USDC (0.1984 €) | — | 63.03 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53135532 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.014722 WETH | 0.000096 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.1979 €) | — | 62.98 | 0.000 (n=28) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53135532 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.014707 WETH | 0.000096 WETH | 0.000000 WETH | 0.000003 WETH | 0.000093 WETH (0.1978 €) | — | 63.02 | 0.000 (n=20) | REJECTED | reliability_not_demonstrated |
| 53135532 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 32.787531 USDC | 0.218827 USDC | 0.000000 USDC | 0.006971 USDC | 0.211856 USDC (0.1949 €) | — | 64.61 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53135532 | WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.014093 WETH | 0.000094 WETH | 0.000000 WETH | 0.000003 WETH | 0.000091 WETH (0.1943 €) | — | 64.61 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53135532 | USDC→[sushiswap_v3]→WETH→[uniswap_v3]→BASECAT→[uniswap_v3]→USDC | 32.465193 USDC | 0.214838 USDC | 0.000000 USDC | 0.006971 USDC | 0.207867 USDC (0.1912 €) | — | 64.03 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 2775 ; taux observé 0.092 ; borne inférieure crédible (0.9) 0.085 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
