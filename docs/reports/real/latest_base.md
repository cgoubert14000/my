# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T18:26:56+00:00 ; durée 67.44 min ; blocs 53511708 → 53513733 (2010 vus)

## Connexion
- Requêtes RPC : 24162 ; erreurs : 128 ; latence p50/p95 : 168.2/788.9 ms
- Rafraîchissements d'état : 2011 ; âge des données au dernier bloc : 1.79 s ; changements de frais LP observés (pools à frais dynamiques) : 3250
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 16914 ; cycles déclenchés par événement : 2211 ; avance médiane sur le rafraîchissement multicall : 442 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,427.80 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 502 pools, 289 jetons, 19560 routes
- Par DEX : uniswap_v3 145, aerodrome_slipstream 107 (quarantaine 2), aerodrome 206 (quarantaine 1), pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 176 (rejetés 2) → 581 jetons ; pools candidats 3710 (énumérés 311, par paires 0), mesurés 505, sous le plancher de 10000.0 $ : 3 → gardés 502 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2427.762313, 'cbBTC': 80310.699989, 'AERO': 0.65591}
- Pools en quarantaine : 3 — aerodrome:WETH/msETH@0xDE4FB3: simulation failed ×5 (model/chain mismatch) — until block 53513992; aerodrome_slipstream:CLANKER/WETH@0xd23FE2: simulation failed ×5 (model/chain mismatch) — until block 53513989; aerodrome_slipstream:WETH/msETH@0x74F727: simulation failed ×5 (model/chain mismatch) — until block 53513992

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 155,215,678 | 2,427.799194 | 53513733 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,330,798 | 0.030199 | 53513733 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,684,954 | 0.030218 | 53513733 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,450,733 | 0.000012 | 53513733 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,355,128 | 2,433.514643 | 53513733 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,025,359 | 107.115113 | 53513733 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,831,691 | 0.001557 | 53513733 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,429,877 | 1.527641 | 53513733 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,984,713 | 0.030208 | 53513733 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,298,210 | 2,434.486218 | 53513733 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,239,442 | 0.999560 | 53513733 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,694,280 | 40,418.584406 | 53513733 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,487,929 | 2,434.359307 | 53513733 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,771,442 | 0.030203 | 53513733 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,290,195 | 1,139,327.995829 | 53513733 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 2,185,303 | 0.008665 | 53513733 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,830,674 | 0.000012 | 53513733 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,753,866 | 0.000000 | 53513733 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,752,826 | 0.017980 | 53513733 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,641,709 | 449.534687 | 53513733 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,630,443 | 0.000012 | 53513733 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,553,919 | 0.000012 | 53513733 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,522,741 | 1.474784 | 53513733 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,499,970 | 3,706.944116 | 53513733 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,440 | 0.816276 | 53513733 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,408,762 | 2,433.505653 | 53513733 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,380,935 | 2,431.387681 | 53513733 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,380,429 | 2,427.619500 | 53513733 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,344,771 | 14,887.735162 | 53513733 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,190,882 | 37,206,604.119382 | 53513733 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,157,988 | 72.465398 | 53513733 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,151,888 | 0.000000 | 53513733 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,111,648 | 559,739.880863 | 53513733 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,102,642 | 106.356526 | 53513733 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,069,070 | 23,018,538.652786 | 53513733 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,389 | 19.429802 | 53513733 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 990,370 | 1,088.436775 | 53513733 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/WELL | 10000 | 986,000 | 1,264,708.619179 | 53513733 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 985,994 | 64.395128 | 53513733 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 971,679 | 95,236.227494 | 53513733 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 968,416 | 0.000012 | 53513733 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/USDC | 10000 | 943,928 | 2,419.737204 | 53513733 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,475 | 0.000536 | 53513733 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 904,066 | 0.044025 | 53513733 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 869,424 | 3,680.941599 | 53513733 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 830,063 | 19.760068 | 53513733 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/wstETH | 3000 | 824,058 | 0.799146 | 53513733 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,170 | 0.057243 | 53513733 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 757,074 | 4,864,240.229114 | 53513733 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 751,463 | 0.602113 | 53513733 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 736,418 | 0.000248 | 53513733 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 736,034 | 137,409.120215 | 53513733 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 699,572 | 0.000008 | 53513733 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2132 | 681,217 | 564,177.089150 | 53513733 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 680,328 | 0.579627 | 53513733 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 651,561 | 0.914307 | 53513733 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 610,300 | 0.092346 | 53513733 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 569,532 | 0.039034 | 53513733 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/DRV | 3000 | 557,017 | 6,968.276175 | 53513733 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| aerodrome_slipstream | WETH/MORPHO | 2775 | 554,566 | 1,088.759359 | 53513733 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 4221 ; routes examinées : 82562760 ; candidats optimisés : 227568 ; net attendu > 0 : 280 ; dernier cycle 259.4 ms
- Rejets (moteur) : {'spread_below_threshold': 81217465, 'liquidity_below_min': 1100318, 'negative_expected_net': 227288, 'unquotable': 16618, 'pool_quarantined': 718}
- Enregistrements de la session : 227565 ; net attendu > 0 : 280 ; simulés (eth_call de la vraie tx) : 39 (ok 4, échec 35) ; étiquettes ghost N+1 : 0/35 positives
- Décisions : {'REJECTED': 227565} ; motifs de rejet : {'below_safety_margin': 193, 'negative_expected_net': 227285, 'p_lower_below_threshold': 242, 'reliability_not_demonstrated': 38, 'simulation_failed': 35, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53511943 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.122182 WETH | 0.000176 WETH | 0.000000 WETH | 0.000003 WETH | 0.000172 WETH (0.3851 €) | — | 14.11 | 0.092 (n=128) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53511943 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.003621 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3845 €) | — | 14.36 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53513623 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.007711 WETH | 0.000168 WETH | 0.000000 WETH | 0.000002 WETH | 0.000165 WETH (0.3694 €) | — | 214.46 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53513636 | WETH→[aerodrome_slipstream]→msETH→[aerodrome]→WETH | 0.015668 WETH | 0.000157 WETH | 0.000000 WETH | 0.000002 WETH | 0.000155 WETH (0.3461 €) | — | 98.90 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53511734 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.721090 WETH | 0.000150 WETH | 0.000000 WETH | 0.000002 WETH | 0.000147 WETH (0.3292 €) | — | 2.04 | 0.044 (n=208) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53511734 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,748.991565 USDC | 0.363408 USDC | 0.000000 USDC | 0.005881 USDC | 0.357527 USDC (0.3289 €) | — | 2.04 | 0.044 (n=208) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.04<0.75) |
| 53511943 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 186.251766 USDC | 0.277603 USDC | 0.000000 USDC | 0.008084 USDC | 0.269519 USDC (0.2480 €) | — | 14.47 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.076874 WETH | 0.000114 WETH | 0.000000 WETH | 0.000003 WETH | 0.000111 WETH (0.2479 €) | — | 14.44 | 0.092 (n=128) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53511943 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 182.791219 USDC | 0.267927 USDC | 0.000000 USDC | 0.007716 USDC | 0.260211 USDC (0.2394 €) | — | 14.24 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.075456 WETH | 0.000110 WETH | 0.000000 WETH | 0.000003 WETH | 0.000107 WETH (0.2393 €) | — | 14.20 | 0.092 (n=128) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53511943 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 177.235793 USDC | 0.258709 USDC | 0.000000 USDC | 0.007716 USDC | 0.250993 USDC (0.2309 €) | — | 14.16 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.072994 WETH | 0.000107 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2308 €) | — | 14.16 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.077140 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2294 €) | — | 13.31 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002254 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2293 €) | — | 13.75 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002657 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2293 €) | — | 11.67 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.097161 WETH | 0.000106 WETH | 0.000000 WETH | 0.000003 WETH | 0.000103 WETH (0.2290 €) | — | 10.55 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.093846 WETH | 0.000103 WETH | 0.000000 WETH | 0.000003 WETH | 0.000100 WETH (0.2233 €) | — | 10.66 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.002657 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.2233 €) | — | 11.37 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511734 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.502422 WETH | 0.000093 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1992 €) | — | 1.78 | 0.034 (n=24) | REJECTED | below_safety_margin(89184135546903<100484401015770), reliability_not_demonstrated |
| 53511734 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,220.153928 USDC | 0.224568 USDC | 0.000000 USDC | 0.008108 USDC | 0.216460 USDC (0.1991 €) | — | 1.77 | 0.034 (n=24) | REJECTED | below_safety_margin(216460<244030), reliability_not_demonstrated |
| 53511734 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.014562 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000003 cbBTC (0.1990 €) | — | 1.85 | 0.034 (n=24) | REJECTED | below_safety_margin(269<291), reliability_not_demonstrated |
| 53511943 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 160.503386 USDC | 0.205586 USDC | 0.000000 USDC | 0.007716 USDC | 0.197870 USDC (0.1820 €) | — | 12.33 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.066201 WETH | 0.000085 WETH | 0.000000 WETH | 0.000003 WETH | 0.000081 WETH (0.1819 €) | — | 12.30 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 155.899346 USDC | 0.195977 USDC | 0.000000 USDC | 0.007716 USDC | 0.188261 USDC (0.1732 €) | — | 12.08 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53511943 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.064447 WETH | 0.000081 WETH | 0.000000 WETH | 0.000003 WETH | 0.000077 WETH (0.1731 €) | — | 12.02 | 0.092 (n=128) | REJECTED | p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 5233 ; taux observé 0.163 ; borne inférieure crédible (0.9) 0.157 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
