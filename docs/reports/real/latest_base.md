# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-31T18:16:38+00:00 ; durée 27.6 min ; blocs 53339794 → 53340623 (827 vus)

## Connexion
- Requêtes RPC : 9858 ; erreurs : 0 ; latence p50/p95 : 222.6/1,038.8 ms
- Rafraîchissements d'état : 827 ; âge des données au dernier bloc : 4.17 s ; changements de frais LP observés (pools à frais dynamiques) : 1103
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7043 ; cycles déclenchés par événement : 1198 ; avance médiane sur le rafraîchissement multicall : 520 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,248.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 506 pools, 291 jetons, 18722 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 115, aerodrome 206, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 179 (rejetés 2) → 584 jetons ; pools candidats 3790 (énumérés 319, par paires 0), mesurés 509, sous le plancher de 10000.0 $ : 3 → gardés 506 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2248.577307, 'cbBTC': 77558.902259, 'AERO': 0.633591}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,238,465 | 2,248.817661 | 53340624 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,054,916 | 0.029044 | 53340624 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,282,160 | 0.000013 | 53340624 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,046,090 | 0.029054 | 53340624 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,857,798 | 2,254.495859 | 53340624 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,845,746 | 97.353746 | 53340624 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,689,298 | 0.001616 | 53340624 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,755,188 | 1.559555 | 53340624 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,242,286 | 0.029052 | 53340624 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,076,952 | 0.998830 | 53340624 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,065,685 | 2,254.908899 | 53340624 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,053,239 | 2,254.732144 | 53340624 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,541,407 | 37,738.444924 | 53340624 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,684,021 | 0.029042 | 53340624 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2730 | 2,399,749 | 97.350584 | 53340624 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,066,928 | 1,200,126.211824 | 53340624 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,970,998 | 0.000013 | 53340624 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,756,520 | 0.000000 | 53340624 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,720,796 | 0.017453 | 53340624 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,640,308 | 0.000013 | 53340624 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v2 | WETH/USDC | 3000 | 1,593,789 | 2,251.029909 | 53340624 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,582,183 | 0.000013 | 53340624 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,549,052 | 421.554046 | 53340624 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,920 | 1.490152 | 53340624 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,340 | 0.825844 | 53340624 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,429,321 | 3,516.339465 | 53340624 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,410,992 | 2,257.602538 | 53340624 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,358,202 | 2,253.995391 | 53340624 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,330,557 | 0.005233 | 53340624 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,306,519 | 14,502.372507 | 53340624 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,306,246 | 0.000013 | 53340624 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,174,369 | 70.458427 | 53340624 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,117,349 | 35,670,348.390630 | 53340624 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,061,246 | 515,108.685390 | 53340624 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,044,353 | 0.000000 | 53340624 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,021,533 | 21,718,776.567159 | 53340624 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,011,468 | 75,457.531788 | 53340624 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,000,379 | 18.928335 | 53340624 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 992,125 | 96.789316 | 53340624 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 978,579 | 0.043177 | 53340624 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 964,231 | 67.333078 | 53340624 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 940,079 | 1,196,421.134446 | 53340624 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 939,156 | 946.435111 | 53340624 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 922,845 | 2,236.005346 | 53340624 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 875,913 | 3,535.754982 | 53340624 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 863,750 | 0.000552 | 53340624 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4505 | 843,841 | 19.232388 | 53340624 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 831,238 | 0.062270 | 53340624 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 761,447 | 0.803065 | 53340624 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 733,292 | 0.000262 | 53340624 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 727,606 | 4,513,319.317507 | 53340624 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,329 | 0.590747 | 53340624 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 693,243 | 0.000008 | 53340624 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 670,783 | 141,747.080111 | 53340624 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 661,813 | 2.335058 | 53340624 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2111 | 658,623 | 518,543.505590 | 53340624 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 634,676 | 0.509052 | 53340624 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 620,693 | 0.094979 | 53340624 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 603,309 | 0.916995 | 53340624 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2754 | 563,317 | 946.601694 | 53340624 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 2024 ; routes examinées : 37893328 ; candidats optimisés : 166075 ; net attendu > 0 : 87 ; dernier cycle 283.8 ms
- Rejets (moteur) : {'spread_below_threshold': 37217870, 'liquidity_below_min': 503235, 'negative_expected_net': 165988, 'unquotable': 4046, 'borrow_bound_too_small': 2023, 'cycle_budget_exhausted': 79}
- Enregistrements de la session : 166075 ; net attendu > 0 : 87 ; simulés (eth_call de la vraie tx) : 15 (ok 2, échec 13) ; étiquettes ghost N+1 : 0/11 positives
- Décisions : {'REJECTED': 166075} ; motifs de rejet : {'below_safety_margin': 51, 'negative_expected_net': 165988, 'p_lower_below_threshold': 87, 'simulation_failed': 13}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53340061 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 103.989966 USDC | 0.077116 USDC | 0.000000 USDC | 0.007108 USDC | 0.070008 USDC (0.0644 €) | — | 6.73 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340061 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.046261 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000031 WETH (0.0643 €) | — | 6.71 | 0.117 (n=492) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340061 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 106.687879 USDC | 0.075727 USDC | 0.000000 USDC | 0.007108 USDC | 0.068619 USDC (0.0631 €) | — | 6.43 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340061 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 106.807714 USDC | 0.075616 USDC | 0.000000 USDC | 0.007108 USDC | 0.068508 USDC (0.0630 €) | — | 6.41 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340061 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.047395 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0630 €) | — | 6.42 | 0.117 (n=492) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340061 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.047439 WETH | 0.000034 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0629 €) | — | 6.41 | 0.117 (n=492) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340396 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 104.600703 USDC | 0.069172 USDC | 0.000000 USDC | 0.007111 USDC | 0.062061 USDC (0.0571 €) | — | 5.93 | 0.116 (n=498) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340396 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.046472 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0570 €) | — | 5.92 | 0.116 (n=498) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340061 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 101.331996 USDC | 0.068818 USDC | 0.000000 USDC | 0.007108 USDC | 0.061710 USDC (0.0568 €) | — | 6.09 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340061 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.044937 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0567 €) | — | 6.09 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340061 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 101.181647 USDC | 0.067919 USDC | 0.000000 USDC | 0.007108 USDC | 0.060811 USDC (0.0559 €) | — | 6.01 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340061 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.044953 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0558 €) | — | 6.00 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340377 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 102.471554 USDC | 0.065639 USDC | 0.000000 USDC | 0.007111 USDC | 0.058528 USDC (0.0538 €) | — | 5.71 | 0.117 (n=495) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340377 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.045594 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0537 €) | — | 5.69 | 0.117 (n=495) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340396 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 99.946351 USDC | 0.063071 USDC | 0.000000 USDC | 0.007111 USDC | 0.055960 USDC (0.0515 €) | — | 5.60 | 0.116 (n=498) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340396 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.044435 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0514 €) | — | 5.59 | 0.116 (n=498) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340377 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 91.781722 USDC | 0.057217 USDC | 0.000000 USDC | 0.007111 USDC | 0.050106 USDC (0.0461 €) | — | 5.46 | 0.117 (n=495) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340377 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.040832 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0460 €) | — | 5.44 | 0.117 (n=495) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340377 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 94.439688 USDC | 0.056137 USDC | 0.000000 USDC | 0.007111 USDC | 0.049026 USDC (0.0451 €) | — | 5.19 | 0.117 (n=495) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340377 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.041988 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0450 €) | — | 5.18 | 0.117 (n=495) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340061 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 67.737080 USDC | 0.054775 USDC | 0.000000 USDC | 0.007108 USDC | 0.047667 USDC (0.0439 €) | — | 7.04 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340061 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.030092 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0438 €) | — | 7.03 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340396 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 86.708680 USDC | 0.051383 USDC | 0.000000 USDC | 0.007111 USDC | 0.044272 USDC (0.0407 €) | — | 5.11 | 0.116 (n=498) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53340396 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.038674 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0406 €) | — | 5.08 | 0.116 (n=498) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53340061 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 76.767107 USDC | 0.048968 USDC | 0.000000 USDC | 0.007108 USDC | 0.041860 USDC (0.0385 €) | — | 5.45 | 0.117 (n=492) | REJECTED | p_lower_below_threshold(0.12<0.75) |

## Fiabilité et décision
- Observations ghost : 3981 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
