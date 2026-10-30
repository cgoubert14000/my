# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-30T02:52:34+00:00 ; durée 24.43 min ; blocs 53268968 → 53269702 (733 vus)

## Connexion
- Requêtes RPC : 8983 ; erreurs : 0 ; latence p50/p95 : 73.0/1,019.2 ms
- Rafraîchissements d'état : 734 ; âge des données au dernier bloc : 1.53 s ; changements de frais LP observés (pools à frais dynamiques) : 1921
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15651 ; cycles déclenchés par événement : 830 ; avance médiane sur le rafraîchissement multicall : 831 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,208.95 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 492 pools, 287 jetons, 18448 routes
- Par DEX : uniswap_v3 134, aerodrome 205, aerodrome_slipstream 111, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 314, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 2 → gardés 492 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2206.596047, 'cbBTC': 77084.188033, 'AERO': 0.611873}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 148,332,709 | 2,208.946683 | 53269702 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,936,576 | 0.028582 | 53269702 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,458,029 | 0.000013 | 53269702 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,970,676 | 0.028657 | 53269702 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,017,681 | 2,205.877144 | 53269702 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,724,074 | 99.100420 | 53269702 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,658,779 | 0.001607 | 53269702 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 6,033,733 | 1.634095 | 53269702 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,520,286 | 0.028583 | 53269702 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | WETH/USDC | 743 | 4,206,865 | 2,205.361503 | 53269702 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,124,719 | 2,206.565146 | 53269702 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,541,795 | 1.000384 | 53269702 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,483,024 | 37,643.170349 | 53269702 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2515 | 2,742,599 | 0.028638 | 53269702 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2748 | 2,291,902 | 99.132586 | 53269702 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,016,701 | 1,216,345.078767 | 53269702 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,923,057 | 0.000013 | 53269702 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,740,378 | 0.017809 | 53269702 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,665,562 | 414.803764 | 53269702 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,652,575 | 0.000000 | 53269702 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,637,292 | 0.000013 | 53269702 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,612,131 | 0.000013 | 53269702 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | WETH/USDC | 3000 | 1,532,543 | 2,209.703119 | 53269702 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,464,839 | 1.641584 | 53269702 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/cbBTC | 352 | 1,464,566 | 0.000013 | 53269702 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,984 | 0.826796 | 53269702 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,329,346 | 3,602.705749 | 53269702 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,576 | 14,506.194013 | 53269702 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,293,061 | 0.005171 | 53269702 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,268,646 | 2,205.779916 | 53269702 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,178,295 | 69.989676 | 53269702 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,153,182 | 0.000256 | 53269702 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | WETH/doginme | 10000 | 1,089,180 | 36,519,405.774328 | 53269702 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,038,029 | 520,216.718100 | 53269702 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,008,648 | 73,255.617666 | 53269702 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,003,849 | 18.741767 | 53269702 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 1,002,032 | 2,208.827063 | 53269702 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/TOSHI | 10000 | 993,360 | 22,058,879.534593 | 53269702 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 985,038 | 0.000000 | 53269702 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | VIRTUAL/WETH | 10000 | 966,763 | 0.000254 | 53269702 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | USDC/VVV | 3000 | 959,480 | 0.044936 | 53269702 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/VVV | 10000 | 945,844 | 99.589834 | 53269702 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/AERO | 10000 | 934,103 | 3,594.057929 | 53269702 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/NOCK | 3000 | 933,901 | 71.776241 | 53269702 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 912,903 | 2,201.188701 | 53269702 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 903,099 | 1,250,860.332727 | 53269702 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 855,335 | 1,099.094070 | 53269702 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 845,541 | 0.000549 | 53269702 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 832,522 | 19.616386 | 53269702 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 812,998 | 0.059369 | 53269702 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 767,180 | 18.246632 | 53269702 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/wstETH | 3000 | 747,690 | 0.803616 | 53269702 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 696,985 | 4,744,282.923830 | 53269702 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 693,839 | 0.563645 | 53269702 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 684,926 | 0.000008 | 53269702 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 673,007 | 2.330114 | 53269702 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2135 | 643,758 | 517,343.216256 | 53269702 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 643,388 | 0.522768 | 53269702 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 633,426 | 153,260.864139 | 53269702 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 601,908 | 0.090710 | 53269702 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 1563 ; routes examinées : 28834224 ; candidats optimisés : 186832 ; net attendu > 0 : 203 ; dernier cycle 378.9 ms
- Rejets (moteur) : {'spread_below_threshold': 28199601, 'liquidity_below_min': 443102, 'negative_expected_net': 186629, 'unquotable': 3126, 'borrow_bound_too_small': 1563}
- Enregistrements de la session : 186832 ; net attendu > 0 : 203 ; simulés (eth_call de la vraie tx) : 25 (ok 17, échec 8) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 186832} ; motifs de rejet : {'below_safety_margin': 152, 'negative_expected_net': 186629, 'p_lower_below_threshold': 193, 'reliability_not_demonstrated': 10, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 2, 'simulation_failed': 8}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53269162 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 884.830547 USDC | 0.122047 USDC | 0.000000 USDC | 0.007241 USDC | 0.114806 USDC (0.1056 €) | — | 1.30 | 0.001 (n=14) | REJECTED | below_safety_margin(114806<176966), reliability_not_demonstrated |
| 53269162 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.012045 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.1056 €) | — | 1.24 | 0.001 (n=14) | REJECTED | below_safety_margin(149<240), reliability_not_demonstrated |
| 53269162 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.421345 WETH | 0.000055 WETH | 0.000000 WETH | 0.000003 WETH | 0.000052 WETH (0.1055 €) | — | 1.23 | 0.001 (n=14) | REJECTED | below_safety_margin(51939327494826<84268925462009), reliability_not_demonstrated |
| 53269162 | WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.367867 WETH | 0.000029 WETH | 0.000000 WETH | 0.000003 WETH | 0.000026 WETH (0.0524 €) | — | 0.70 | 0.135 (n=540) | REJECTED | below_safety_margin(25826590791060<73573344629983), p_lower_below_threshold(0.13<0.75) |
| 53269162 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.010214 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0524 €) | — | 0.72 | 0.135 (n=540) | REJECTED | below_safety_margin(74<204), p_lower_below_threshold(0.13<0.75) |
| 53269162 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 830.311808 USDC | 0.064150 USDC | 0.000000 USDC | 0.007241 USDC | 0.056909 USDC (0.0524 €) | — | 0.69 | 0.135 (n=540) | REJECTED | below_safety_margin(56909<166062), p_lower_below_threshold(0.13<0.75) |
| 53269591 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.045064 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0381 €) | — | 4.16 | 0.104 (n=406) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53269591 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 99.343616 USDC | 0.048488 USDC | 0.000000 USDC | 0.007094 USDC | 0.041394 USDC (0.0381 €) | — | 4.17 | 0.104 (n=406) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269591 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.048697 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0360 €) | — | 3.63 | 0.104 (n=406) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53269591 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 107.211747 USDC | 0.046128 USDC | 0.000000 USDC | 0.007094 USDC | 0.039034 USDC (0.0359 €) | — | 3.64 | 0.104 (n=406) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269591 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.045310 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0307 €) | — | 3.33 | 0.104 (n=406) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53269591 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 99.507608 USDC | 0.040386 USDC | 0.000000 USDC | 0.007094 USDC | 0.033292 USDC (0.0306 €) | — | 3.35 | 0.104 (n=406) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269162 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.006670 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0298 €) | — | 0.63 | 0.135 (n=540) | REJECTED | below_safety_margin(42<133), p_lower_below_threshold(0.13<0.75) |
| 53269162 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 487.452476 USDC | 0.039546 USDC | 0.000000 USDC | 0.007241 USDC | 0.032305 USDC (0.0297 €) | — | 0.66 | 0.135 (n=540) | REJECTED | below_safety_margin(32305<97490), p_lower_below_threshold(0.13<0.75) |
| 53269591 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.045313 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0297 €) | — | 3.22 | 0.104 (n=406) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269591 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 99.343616 USDC | 0.039330 USDC | 0.000000 USDC | 0.007094 USDC | 0.032236 USDC (0.0297 €) | — | 3.24 | 0.104 (n=406) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269162 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.239056 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0294 €) | — | 0.61 | 0.135 (n=540) | REJECTED | below_safety_margin(14483656303795<47811171553980), p_lower_below_threshold(0.13<0.75) |
| 53269167 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 61.603977 USDC | 0.039194 USDC | 0.000000 USDC | 0.007266 USDC | 0.031928 USDC (0.0294 €) | — | 5.18 | 0.105 (n=401) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269167 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 61.603977 USDC | 0.039194 USDC | 0.000000 USDC | 0.007266 USDC | 0.031928 USDC (0.0294 €) | — | 5.18 | 0.105 (n=401) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269167 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.027943 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0294 €) | 0.000014 WETH | 5.18 | 0.105 (n=401) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269167 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.027943 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0294 €) | — | 5.18 | 0.105 (n=401) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53269591 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.041993 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0257 €) | — | 3.01 | 0.104 (n=406) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269591 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 92.159523 USDC | 0.034972 USDC | 0.000000 USDC | 0.007094 USDC | 0.027878 USDC (0.0256 €) | — | 3.02 | 0.104 (n=406) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269167 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 54.821248 USDC | 0.030757 USDC | 0.000000 USDC | 0.007266 USDC | 0.023491 USDC (0.0216 €) | — | 4.29 | 0.105 (n=401) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53269167 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 54.821248 USDC | 0.030757 USDC | 0.000000 USDC | 0.007266 USDC | 0.023491 USDC (0.0216 €) | — | 4.29 | 0.105 (n=401) | REJECTED | p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 3490 ; taux observé 0.113 ; borne inférieure crédible (0.9) 0.107 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 10.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
