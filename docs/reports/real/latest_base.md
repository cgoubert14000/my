# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T16:05:23+00:00 ; durée 232.56 min ; blocs 53329707 → 53336685 (6775 vus)

## Connexion
- Requêtes RPC : 79749 ; erreurs : 30 ; latence p50/p95 : 304.7/1,233.4 ms
- Rafraîchissements d'état : 6776 ; âge des données au dernier bloc : 1.57 s ; changements de frais LP observés (pools à frais dynamiques) : 7039
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 60466 ; cycles déclenchés par événement : 6790 ; avance médiane sur le rafraîchissement multicall : 482 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,246.03 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 290 jetons, 18658 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 113, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 318, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2242.796031, 'cbBTC': 77486.299825, 'AERO': 0.625959}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,568,208 | 2,246.029158 | 53336685 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,036,949 | 0.029020 | 53336685 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,287,469 | 0.000013 | 53336685 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,038,399 | 0.029054 | 53336685 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,871,417 | 96.555232 | 53336685 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,847,085 | 2,248.876355 | 53336685 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,685,541 | 0.001615 | 53336685 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,891,399 | 1.573285 | 53336685 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,300,417 | 0.029021 | 53336685 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,100,018 | 2,249.401542 | 53336685 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,075,291 | 0.998824 | 53336685 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,041,721 | 2,249.465431 | 53336685 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,538,134 | 37,714.590834 | 53336685 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,683,490 | 0.029042 | 53336685 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,406,045 | 96.577175 | 53336685 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,064,365 | 1,200,126.211824 | 53336685 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,968,393 | 0.000013 | 53336685 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,754,447 | 0.000000 | 53336685 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,726,099 | 0.017533 | 53336685 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,639,595 | 0.000013 | 53336685 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,592,799 | 2,248.728895 | 53336685 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,581,780 | 0.000013 | 53336685 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,774 | 1.482941 | 53336685 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,547,423 | 421.262678 | 53336685 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | WETH/USDC | 3000 | 1,471,826 | 2,254.754296 | 53336685 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,309 | 0.825876 | 53336685 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,421,566 | 3,539.377577 | 53336685 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,395,160 | 2,248.862883 | 53336685 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,345,144 | 0.005286 | 53336685 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 1,309,545 | 0.000013 | 53336685 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,305,887 | 14,500.759998 | 53336685 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,174,369 | 70.458427 | 53336685 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,120,471 | 35,240,976.602131 | 53336685 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,057,280 | 518,684.239424 | 53336685 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,034,219 | 0.000000 | 53336685 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,024,085 | 21,577,072.539196 | 53336685 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,012,754 | 75,079.400725 | 53336685 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 996,504 | 19.140102 | 53336685 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 995,184 | 96.789142 | 53336685 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 982,983 | 0.042918 | 53336685 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 969,916 | 66.546146 | 53336685 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 934,734 | 974.224151 | 53336685 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/WELL | 10000 | 933,144 | 1,211,271.107491 | 53336685 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 921,216 | 2,236.005346 | 53336685 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 871,535 | 3,544.352402 | 53336685 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 862,430 | 0.000553 | 53336685 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 846,887 | 19.125201 | 53336685 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 827,432 | 0.061659 | 53336685 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,608 | 0.802842 | 53336685 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 730,390 | 0.000261 | 53336685 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 726,887 | 4,510,996.491778 | 53336685 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 719,017 | 0.590323 | 53336685 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 689,748 | 0.000008 | 53336685 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 670,869 | 141,357.595318 | 53336685 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 661,014 | 2.334946 | 53336685 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 655,409 | 514,968.691037 | 53336685 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 628,981 | 0.500262 | 53336685 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 626,932 | 0.096470 | 53336685 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 604,196 | 0.914241 | 53336685 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2778 | 560,119 | 973.701972 | 53336685 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 13565 ; routes examinées : 253095770 ; candidats optimisés : 695906 ; net attendu > 0 : 319 ; dernier cycle 97.6 ms
- Rejets (moteur) : {'spread_below_threshold': 250073844, 'liquidity_below_min': 2282451, 'negative_expected_net': 695587, 'unquotable': 27012, 'borrow_bound_too_small': 13536, 'cycle_budget_exhausted': 3021}
- Enregistrements de la session : 695906 ; net attendu > 0 : 319 ; simulés (eth_call de la vraie tx) : 20 (ok 5, échec 15) ; étiquettes ghost N+1 : 1/15 positives
- Décisions : {'REJECTED': 695906} ; motifs de rejet : {'below_safety_margin': 261, 'negative_expected_net': 695587, 'p_lower_below_threshold': 301, 'reliability_not_demonstrated': 18, 'simulation_failed': 15}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 1,169.382766 USDC | 3.349481 USDC | 0.000000 USDC | 0.006775 USDC | 3.342706 USDC (3.0753 €) | — | 28.59 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.520561 WETH | 0.001491 WETH | 0.000000 WETH | 0.000003 WETH | 0.001488 WETH (3.0748 €) | — | 28.59 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.536835 WETH | 0.001165 WETH | 0.000000 WETH | 0.000003 WETH | 0.001162 WETH (2.4012 €) | — | 21.65 | 0.000 (n=28) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,204.187156 USDC | 2.616046 USDC | 0.000000 USDC | 0.007116 USDC | 2.608930 USDC (2.4002 €) | — | 21.67 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53335509 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.440282 WETH | 0.000976 WETH | 0.000000 WETH | 0.000003 WETH | 0.000973 WETH (2.0109 €) | — | 22.10 | 0.000 (n=42) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 988.126456 USDC | 2.190896 USDC | 0.000000 USDC | 0.006775 USDC | 2.184121 USDC (2.0094 €) | — | 22.10 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.422302 WETH | 0.000945 WETH | 0.000000 WETH | 0.000003 WETH | 0.000942 WETH (1.9460 €) | — | 22.30 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 947.639796 USDC | 2.120061 USDC | 0.000000 USDC | 0.006775 USDC | 2.113286 USDC (1.9442 €) | — | 22.30 | 0.000 (n=28) | REJECTED | reliability_not_demonstrated |
| 53335509 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.411280 WETH | 0.000883 WETH | 0.000000 WETH | 0.000003 WETH | 0.000879 WETH (1.8168 €) | — | 21.38 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 922.614280 USDC | 1.979736 USDC | 0.000000 USDC | 0.007798 USDC | 1.971938 USDC (1.8142 €) | — | 21.37 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 1.614710 WETH | 0.000372 WETH | 0.000000 WETH | 0.000002 WETH | 0.000369 WETH (0.7630 €) | — | 2.29 | 0.039 (n=152) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53335509 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 3,625.255582 USDC | 0.834698 USDC | 0.000000 USDC | 0.005405 USDC | 0.829293 USDC (0.7629 €) | — | 2.29 | 0.039 (n=152) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53335509 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.143528 WETH | 0.000321 WETH | 0.000000 WETH | 0.000003 WETH | 0.000318 WETH (0.6569 €) | — | 22.15 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 321.267429 USDC | 0.718649 USDC | 0.000000 USDC | 0.007116 USDC | 0.711533 USDC (0.6546 €) | — | 22.15 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.133456 WETH | 0.000285 WETH | 0.000000 WETH | 0.000003 WETH | 0.000282 WETH (0.5826 €) | — | 21.13 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | USDC→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 298.477340 USDC | 0.637680 USDC | 0.000000 USDC | 0.006775 USDC | 0.630905 USDC (0.5804 €) | — | 21.14 | 0.000 (n=42) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53335509 | WETH→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.289510 WETH | 0.000274 WETH | 0.000000 WETH | 0.000002 WETH | 0.000272 WETH (0.5622 €) | — | 9.40 | 0.001 (n=12) | REJECTED | reliability_not_demonstrated |
| 53335509 | WETH→[uniswap_v3]→MORPHO→[aerodrome_slipstream]→WETH | 0.087497 WETH | 0.000222 WETH | 0.000000 WETH | 0.000002 WETH | 0.000220 WETH (0.4541 €) | — | 25.11 | 0.001 (n=10) | REJECTED | reliability_not_demonstrated |
| 53336277 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 227.045518 USDC | 0.415783 USDC | 0.000000 USDC | 0.008473 USDC | 0.407310 USDC (0.3747 €) | — | 17.94 | 0.017 (n=83) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53336277 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.101120 WETH | 0.000185 WETH | 0.000000 WETH | 0.000004 WETH | 0.000181 WETH (0.3744 €) | — | 17.92 | 0.017 (n=83) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53336277 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 225.447587 USDC | 0.408839 USDC | 0.000000 USDC | 0.008473 USDC | 0.400366 USDC (0.3683 €) | — | 17.76 | 0.072 (n=93) | REJECTED | p_lower_below_threshold(0.07<0.75) |
| 53336277 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.100513 WETH | 0.000182 WETH | 0.000000 WETH | 0.000004 WETH | 0.000178 WETH (0.3680 €) | — | 17.72 | 0.072 (n=93) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.07<0.75) |
| 53336277 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 212.027435 USDC | 0.383988 USDC | 0.000000 USDC | 0.008814 USDC | 0.375174 USDC (0.3452 €) | — | 17.69 | 0.017 (n=83) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 53336277 | WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.094243 WETH | 0.000171 WETH | 0.000000 WETH | 0.000004 WETH | 0.000167 WETH (0.3448 €) | — | 17.70 | 0.017 (n=83) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 53336277 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDbC→[aerodrome_slipstream]→USDC | 190.873791 USDC | 0.294025 USDC | 0.000000 USDC | 0.008132 USDC | 0.285893 USDC (0.2630 €) | — | 14.98 | 0.017 (n=83) | REJECTED | p_lower_below_threshold(0.02<0.75) |

## Fiabilité et décision
- Observations ghost : 3960 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
