# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T11:33:57+00:00 ; durée 57.99 min ; blocs 53370003 → 53371744 (1735 vus)

## Connexion
- Requêtes RPC : 20291 ; erreurs : 0 ; latence p50/p95 : 140.4/706.8 ms
- Rafraîchissements d'état : 1736 ; âge des données au dernier bloc : 1.21 s ; changements de frais LP observés (pools à frais dynamiques) : 909
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 7203 ; cycles déclenchés par événement : 1185 ; avance médiane sur le rafraîchissement multicall : 265 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,268.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 501 pools, 289 jetons, 18668 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 112, aerodrome 207, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3735 (énumérés 317, par paires 0), mesurés 504, sous le plancher de 10000.0 $ : 3 → gardés 501 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2268.223075, 'cbBTC': 77979.526152, 'AERO': 0.640175}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,958,130 | 2,268.234796 | 53371744 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,184,712 | 0.029107 | 53371744 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,285,195 | 0.000013 | 53371744 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,134,580 | 0.029145 | 53371744 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,930,825 | 96.738838 | 53371744 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,900,438 | 2,266.806216 | 53371744 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,697,475 | 0.001599 | 53371744 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,711,931 | 1.558078 | 53371744 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,194,811 | 0.029104 | 53371744 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,103,143 | 0.998845 | 53371744 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,072,313 | 2,266.206482 | 53371744 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,001,559 | 2,266.117941 | 53371744 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,570,173 | 37,776.751870 | 53371744 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,705,713 | 0.029128 | 53371744 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,429,974 | 96.777202 | 53371744 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 2,190,494 | 0.000013 | 53371744 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,087,147 | 1,197,399.229010 | 53371744 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,764,607 | 0.000000 | 53371744 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,722,206 | 0.017486 | 53371744 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,657,358 | 0.000013 | 53371744 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,587,022 | 0.000013 | 53371744 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,561,321 | 422.727555 | 53371744 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,008 | 1.499750 | 53371744 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,592 | 2,271.956801 | 53371744 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,455 | 0.825724 | 53371744 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,436,196 | 3,534.311763 | 53371744 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,411,316 | 2,271.182798 | 53371744 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,349,958 | 2,266.826604 | 53371744 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,327,902 | 0.005168 | 53371744 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,314,777 | 14,523.671250 | 53371744 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 1,308,798 | 0.000013 | 53371744 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,853 | 71.003503 | 53371744 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,119,722 | 36,325,008.007960 | 53371744 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,080,910 | 508,520.360494 | 53371744 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,066,230 | 0.000000 | 53371744 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,024,506 | 21,951,530.215130 | 53371744 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,003,669 | 96.637938 | 53371744 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,764 | 19.293096 | 53371744 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 990,693 | 0.042694 | 53371744 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 981,079 | 81,596.329410 | 53371744 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 962,768 | 1,160,479.829563 | 53371744 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 959,117 | 68.053341 | 53371744 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 949,858 | 983.135454 | 53371744 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 923,835 | 2,252.785569 | 53371744 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 877,400 | 3,523.410425 | 53371744 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 868,539 | 0.000551 | 53371744 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 841,881 | 19.303603 | 53371744 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 821,822 | 0.060763 | 53371744 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,588 | 0.801881 | 53371744 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 736,153 | 0.000260 | 53371744 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,178 | 0.595651 | 53371744 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,875 | 4,717,312.612310 | 53371744 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 695,329 | 0.000008 | 53371744 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 686,124 | 137,843.288317 | 53371744 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 668,936 | 510,443.522156 | 53371744 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 665,016 | 0.556103 | 53371744 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 660,914 | 2.339248 | 53371744 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 613,512 | 0.093271 | 53371744 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 608,714 | 0.916406 | 53371744 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2712 | 557,553 | 983.497086 | 53371744 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 2920 ; routes examinées : 54510560 ; candidats optimisés : 172045 ; net attendu > 0 : 44 ; dernier cycle 177.6 ms
- Rejets (moteur) : {'spread_below_threshold': 53911571, 'liquidity_below_min': 408184, 'negative_expected_net': 172001, 'borrow_bound_too_small': 12863, 'unquotable': 5838}
- Enregistrements de la session : 172045 ; net attendu > 0 : 44 ; simulés (eth_call de la vraie tx) : 4 (ok 0, échec 4) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 172045} ; motifs de rejet : {'below_safety_margin': 27, 'negative_expected_net': 172001, 'p_lower_below_threshold': 43, 'reliability_not_demonstrated': 1, 'simulation_failed': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53370189 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.053476 WETH | 0.000040 WETH | 0.000000 WETH | 0.000003 WETH | 0.000037 WETH (0.0779 €) | — | 6.98 | 0.119 (n=515) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 120.929741 USDC | 0.091510 USDC | 0.000000 USDC | 0.006816 USDC | 0.084694 USDC (0.0779 €) | — | 7.00 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.052830 WETH | 0.000039 WETH | 0.000000 WETH | 0.000003 WETH | 0.000036 WETH (0.0750 €) | — | 6.81 | 0.119 (n=515) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 119.611763 USDC | 0.088379 USDC | 0.000000 USDC | 0.006816 USDC | 0.081563 USDC (0.0750 €) | — | 6.82 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.050680 WETH | 0.000037 WETH | 0.000000 WETH | 0.000003 WETH | 0.000034 WETH (0.0716 €) | — | 6.77 | 0.119 (n=515) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 114.787888 USDC | 0.084935 USDC | 0.000000 USDC | 0.007160 USDC | 0.077775 USDC (0.0716 €) | — | 6.78 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.050140 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0672 €) | — | 6.42 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 113.467675 USDC | 0.079826 USDC | 0.000000 USDC | 0.006816 USDC | 0.073010 USDC (0.0672 €) | — | 6.43 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.045168 WETH | 0.000035 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0665 €) | — | 7.05 | 0.246 (n=103) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 102.053903 USDC | 0.078741 USDC | 0.000000 USDC | 0.006503 USDC | 0.072238 USDC (0.0665 €) | — | 7.08 | 0.246 (n=103) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53370189 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.031222 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0465 €) | — | 7.13 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 70.511686 USDC | 0.057294 USDC | 0.000000 USDC | 0.006816 USDC | 0.050478 USDC (0.0464 €) | — | 7.16 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[sushiswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.033520 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0451 €) | — | 6.45 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 75.759323 USDC | 0.056155 USDC | 0.000000 USDC | 0.007160 USDC | 0.048995 USDC (0.0451 €) | — | 6.47 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.038299 WETH | 0.000020 WETH | 0.000000 WETH | 0.000003 WETH | 0.000017 WETH (0.0363 €) | — | 4.55 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53370189 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 86.535461 USDC | 0.046289 USDC | 0.000000 USDC | 0.006816 USDC | 0.039473 USDC (0.0363 €) | — | 4.56 | 0.119 (n=515) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53371333 | WETH→[aerodrome]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.024359 WETH | 0.000011 WETH | 0.000000 WETH | 0.000002 WETH | 0.000009 WETH (0.0183 €) | — | 3.60 | 0.121 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.12<0.75) |
| 53370260 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.026968 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0059 €) | — | 1.05 | 0.142 (n=672) | REJECTED | below_safety_margin(2820643912854<5393575432839), p_lower_below_threshold(0.14<0.75) |
| 53370260 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.026968 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0059 €) | — | 1.05 | 0.142 (n=672) | REJECTED | below_safety_margin(2820643912854<5393575432839), p_lower_below_threshold(0.14<0.75) |
| 53370261 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.026968 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0059 €) | — | 1.05 | 0.142 (n=672) | REJECTED | below_safety_margin(2820643912854<5393575432839), p_lower_below_threshold(0.14<0.75) |
| 53370260 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000767 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.04 | 0.142 (n=672) | REJECTED | below_safety_margin(8<15), p_lower_below_threshold(0.14<0.75) |
| 53370260 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000767 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.04 | 0.142 (n=672) | REJECTED | below_safety_margin(8<15), p_lower_below_threshold(0.14<0.75) |
| 53370261 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.000767 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.04 | 0.142 (n=672) | REJECTED | below_safety_margin(8<15), p_lower_below_threshold(0.14<0.75) |
| 53371333 | WETH→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.018371 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0030 €) | — | 0.78 | 0.278 (n=85) | REJECTED | below_safety_margin(1429846209681<3674112973147), p_lower_below_threshold(0.28<0.75) |
| 53371333 | USDC→[uniswap_v3]→WETH→[aerodrome]→VIRTUAL→[pancakeswap_v3]→USDC | 41.319201 USDC | 0.010089 USDC | 0.000000 USDC | 0.006847 USDC | 0.003242 USDC (0.0030 €) | — | 0.78 | 0.278 (n=85) | REJECTED | below_safety_margin(3242<8263), p_lower_below_threshold(0.28<0.75) |

## Fiabilité et décision
- Observations ghost : 4059 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
