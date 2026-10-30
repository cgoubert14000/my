# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T13:54:04+00:00 ; durée 12.16 min ; blocs 53289181 → 53289548 (365 vus)

## Connexion
- Requêtes RPC : 4410 ; erreurs : 0 ; latence p50/p95 : 66.4/740.8 ms
- Rafraîchissements d'état : 366 ; âge des données au dernier bloc : 1.21 s ; changements de frais LP observés (pools à frais dynamiques) : 1126
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10986 ; cycles déclenchés par événement : 468 ; avance médiane sur le rafraîchissement multicall : 159 ms
- Gaz : base fee 0.005014 gwei ; prix ETH (pool le plus profond) : 2,211.85 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 498 pools, 287 jetons, 18738 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 206, pancakeswap_v3 28 (quarantaine 1), uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 177 (rejetés 2) → 582 jetons ; pools candidats 3726 (énumérés 317, par paires 0), mesurés 501, sous le plancher de 10000.0 $ : 3 → gardés 498 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2224.464255, 'cbBTC': 77004.393698, 'AERO': 0.620215}
- Pools en quarantaine : 1 — pancakeswap_v3:WETH/EURC@0xb4a43D: simulation failed ×5 (model/chain mismatch) — until block 53289779

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,165,804 | 2,211.846107 | 53289548 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,974,298 | 0.028868 | 53289548 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,531,442 | 0.000013 | 53289548 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,946,870 | 0.028860 | 53289548 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,056,369 | 2,214.951578 | 53289548 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,689,200 | 100.144739 | 53289548 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,615,783 | 0.001616 | 53289548 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,032,828 | 1.625795 | 53289548 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,492,923 | 0.028877 | 53289548 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 669 | 4,164,928 | 2,215.728039 | 53289548 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,030,532 | 0.999939 | 53289548 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,011,890 | 2,215.247825 | 53289548 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,525,046 | 36,847.581017 | 53289548 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,735,132 | 0.028852 | 53289548 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,311,909 | 100.181127 | 53289548 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,027,701 | 1,206,344.208581 | 53289548 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,907,794 | 0.000013 | 53289548 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,767,973 | 0.018240 | 53289548 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,688,893 | 0.000000 | 53289548 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,664,837 | 417.077897 | 53289548 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,653,047 | 0.000013 | 53289548 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,556,442 | 0.000013 | 53289548 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/USDC | 3000 | 1,527,014 | 2,211.773831 | 53289548 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,463,389 | 1.643209 | 53289548 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,455,725 | 0.000013 | 53289548 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,887 | 0.824971 | 53289548 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,388,826 | 3,594.744225 | 53289548 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,304,380 | 2,214.898115 | 53289548 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,294,995 | 14,460.147801 | 53289548 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,264,943 | 0.005028 | 53289548 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,178,067 | 70.016773 | 53289548 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,091,475 | 36,265,727.250085 | 53289548 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,043,251 | 515,837.991317 | 53289548 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,021,816 | 21,083,127.034335 | 53289548 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,003,355 | 74,225.152003 | 53289548 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v2 | WETH/USDC | 3000 | 1,002,690 | 2,211.748700 | 53289548 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 994,391 | 19.257259 | 53289548 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | DRB/WETH | 10000 | 993,787 | 0.000000 | 53289548 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 968,714 | 66.710609 | 53289548 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/VVV | 10000 | 952,368 | 99.903240 | 53289548 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 950,270 | 0.045320 | 53289548 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/WELL | 10000 | 919,702 | 1,209,274.366068 | 53289548 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 915,205 | 2,228.113244 | 53289548 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 870,086 | 1,083.811894 | 53289548 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/AERO | 10000 | 855,026 | 3,587.716388 | 53289548 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 852,165 | 0.000556 | 53289548 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 831,646 | 19.651882 | 53289548 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 810,809 | 0.059027 | 53289548 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 779,954 | 17.950100 | 53289548 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 748,672 | 0.803616 | 53289548 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 721,933 | 0.000260 | 53289548 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 707,206 | 0.576854 | 53289548 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 704,227 | 4,659,770.357888 | 53289548 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 685,374 | 0.000008 | 53289548 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 674,194 | 2.328550 | 53289548 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v2 | WETH/NPC | 3000 | 648,487 | 146,649.361801 | 53289548 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2129 | 647,527 | 516,290.426593 | 53289548 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 640,055 | 0.517461 | 53289548 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 603,859 | 0.091128 | 53289548 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 594,829 | 0.914771 | 53289548 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |

## Recherche d'opportunités
- Cycles : 833 ; routes examinées : 15608754 ; candidats optimisés : 94937 ; net attendu > 0 : 1018 ; dernier cycle 106.0 ms
- Rejets (moteur) : {'spread_below_threshold': 15184940, 'liquidity_below_min': 284192, 'negative_expected_net': 93919, 'pool_quarantined': 34608, 'unquotable': 8782, 'borrow_bound_too_small': 833, 'cycle_budget_exhausted': 462}
- Enregistrements de la session : 94937 ; net attendu > 0 : 1018 ; simulés (eth_call de la vraie tx) : 46 (ok 31, échec 15) ; étiquettes ghost N+1 : 11/28 positives
- Décisions : {'REJECTED': 94937} ; motifs de rejet : {'below_safety_margin': 796, 'negative_expected_net': 93919, 'p_lower_below_threshold': 941, 'reliability_not_demonstrated': 77, 'sim_below_estimate': 3, 'simulation_failed': 15}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53289479 | WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.135000 WETH | 0.000092 WETH | 0.000000 WETH | 0.000003 WETH | 0.000089 WETH (0.1819 €) | — | 6.62 | 0.161 (n=223) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→USDC | 297.734168 USDC | 0.204126 USDC | 0.000000 USDC | 0.006774 USDC | 0.197352 USDC (0.1816 €) | — | 6.63 | 0.161 (n=223) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53289479 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.061663 WETH | 0.000045 WETH | 0.000000 WETH | 0.000003 WETH | 0.000042 WETH (0.0852 €) | — | 6.79 | 0.107 (n=445) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 135.978925 USDC | 0.099193 USDC | 0.000000 USDC | 0.006774 USDC | 0.092419 USDC (0.0850 €) | — | 6.80 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53289479 | WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.058310 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0772 €) | — | 6.50 | 0.107 (n=445) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC | 128.804160 USDC | 0.090490 USDC | 0.000000 USDC | 0.006774 USDC | 0.083716 USDC (0.0770 €) | — | 6.50 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53289479 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.057665 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0741 €) | — | 6.31 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 127.005264 USDC | 0.087131 USDC | 0.000000 USDC | 0.006774 USDC | 0.080357 USDC (0.0739 €) | — | 6.33 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53289479 | WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.041336 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0514 €) | — | 6.11 | 0.161 (n=223) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[uniswap_v3]→USDC | 90.937528 USDC | 0.062848 USDC | 0.000000 USDC | 0.007110 USDC | 0.055738 USDC (0.0513 €) | — | 6.13 | 0.161 (n=223) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53289479 | WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.040806 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0505 €) | — | 6.08 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[pancakeswap_v3]→USDC | 90.104407 USDC | 0.061904 USDC | 0.000000 USDC | 0.007110 USDC | 0.054794 USDC (0.0504 €) | — | 6.08 | 0.107 (n=445) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 53289479 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.040216 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0489 €) | — | 5.98 | 0.161 (n=223) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 88.968658 USDC | 0.060176 USDC | 0.000000 USDC | 0.007110 USDC | 0.053066 USDC (0.0488 €) | — | 5.96 | 0.161 (n=223) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53289450 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.270767 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0376 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(18423171082899<54153435228351), p_lower_below_threshold(0.04<0.75) |
| 53289450 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.270767 WETH | 0.000021 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0376 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(18423171082899<54153435228351), p_lower_below_threshold(0.04<0.75) |
| 53289450 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 597.627664 USDC | 0.046181 USDC | 0.000000 USDC | 0.005422 USDC | 0.040759 USDC (0.0375 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(40759<119525), p_lower_below_threshold(0.04<0.75) |
| 53289450 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 597.627664 USDC | 0.046181 USDC | 0.000000 USDC | 0.005422 USDC | 0.040759 USDC (0.0375 €) | — | 0.68 | 0.042 (n=141) | REJECTED | below_safety_margin(40759<119525), p_lower_below_threshold(0.04<0.75) |
| 53289479 | cbBTC→[aerodrome]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000724 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0317 €) | — | 6.21 | 0.207 (n=83) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 53289479 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→USDC→[uniswap_v3]→WETH | 0.026428 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0317 €) | — | 5.89 | 0.207 (n=83) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 53289479 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome]→USDC | 62.618192 USDC | 0.040334 USDC | 0.000000 USDC | 0.006468 USDC | 0.033866 USDC (0.0312 €) | — | 5.41 | 0.207 (n=83) | REJECTED | p_lower_below_threshold(0.21<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069651 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | — | 1.78 | 0.163 (n=260) | REJECTED | below_safety_margin(12418220348479<13930177782132), p_lower_below_threshold(0.16<0.75) |
| 53289308 | WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.069651 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | — | 1.78 | 0.163 (n=260) | REJECTED | below_safety_margin(12418220348479<13930177782132), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 153.449517 USDC | 0.034317 USDC | 0.000000 USDC | 0.006814 USDC | 0.027503 USDC (0.0253 €) | — | 1.79 | 0.163 (n=260) | REJECTED | below_safety_margin(27503<30689), p_lower_below_threshold(0.16<0.75) |
| 53289308 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDT→[aerodrome_slipstream]→USDC | 153.449517 USDC | 0.034317 USDC | 0.000000 USDC | 0.006814 USDC | 0.027503 USDC (0.0253 €) | — | 1.79 | 0.163 (n=260) | REJECTED | below_safety_margin(27503<30689), p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 3678 ; taux observé 0.118 ; borne inférieure crédible (0.9) 0.112 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 11.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
