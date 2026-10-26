# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-26T15:20:39+00:00 ; durée 67.54 min ; blocs 53117317 → 53119345 (1856 vus)

## Connexion
- Requêtes RPC : 23654 ; erreurs : 55 ; latence p50/p95 : 95.6/922.2 ms
- Rafraîchissements d'état : 1857 ; âge des données au dernier bloc : 2.47 s ; changements de frais LP observés (pools à frais dynamiques) : 5874
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 30421 ; cycles déclenchés par événement : 2616 ; avance médiane sur le rafraîchissement multicall : 1,076 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,325.98 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 529 pools, 304 jetons, 19426 routes
- Par DEX : uniswap_v3 143, aerodrome 213, aerodrome_slipstream 128, pancakeswap_v3 29, uniswap_v2 13, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 189 (rejetés 2) → 594 jetons ; pools candidats 3787 (énumérés 341, par paires 0), mesurés 532, sous le plancher de 10000.0 $ : 3 → gardés 529 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2307.602823, 'cbBTC': 79842.460004, 'AERO': 0.67568}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 136,680,356 | 2,325.977623 | 53119344 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,786,494 | 0.028954 | 53119344 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,197,382 | 0.028964 | 53119344 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,494,518 | 0.000012 | 53119344 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 8,891,209 | 92.595670 | 53119344 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 8,335,221 | 2,331.890515 | 53119345 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | USDC/AERO | 3000 | 7,165,156 | 1.450270 | 53119344 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,031,997 | 0.001659 | 53119344 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 833 | 5,349,744 | 2,332.127567 | 53119345 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,341,938 | 0.028963 | 53119344 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,471,203 | 2,331.896490 | 53119344 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,227,825 | 0.999582 | 53119344 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,814,964 | 34,794.971710 | 53119344 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/USDC | 3000 | 3,368,841 | 2,325.844995 | 53119344 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 3,200,973 | 0.028949 | 53119344 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,510,410 | 92.576358 | 53119344 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 556 | 2,480,062 | 0.000012 | 53119344 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,128,900 | 1,210,234.968788 | 53119344 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,898,111 | 0.000012 | 53119344 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,888,982 | 0.000000 | 53119344 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,820,962 | 0.018526 | 53119344 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,764,789 | 403.946458 | 53119344 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,717,615 | 0.000012 | 53119344 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 1,701,154 | 0.000012 | 53119344 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | VIRTUAL/WETH | 10000 | 1,557,417 | 0.000266 | 53119344 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,511,963 | 0.005866 | 53119344 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,740 | 0.826149 | 53119344 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,453,150 | 1.698035 | 53119344 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,449,381 | 3,373.743002 | 53119344 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,374,958 | 13,949.370923 | 53119344 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,239,039 | 0.000268 | 53119344 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/AERO | 10000 | 1,223,291 | 3,383.058655 | 53119344 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/SEND | 3000 | 1,221,560 | 65.119739 | 53119344 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,213,379 | 2,331.889287 | 53119344 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | DRB/WETH | 10000 | 1,171,507 | 0.000000 | 53119344 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/WELL | 10000 | 1,141,309 | 1,089,725.509332 | 53119344 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,134,524 | 37,656,452.661386 | 53119344 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,111,157 | 496,861.328423 | 53119344 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,070,714 | 20,109,343.123032 | 53119344 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,068,382 | 72,634.597986 | 53119344 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,055,194 | 56.254221 | 53119344 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,033,310 | 17.288739 | 53119344 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 979,405 | 0.039727 | 53119344 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/USDC | 10000 | 943,393 | 2,311.179728 | 53119344 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/msETH (stable) | 500 | 909,373 | 2.308543 | 53119344 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | uXRP/WETH | 3000 | 896,373 | 0.000557 | 53119344 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | WETH/MORPHO | 3000 | 895,718 | 1,121.577336 | 53119344 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 890,215 | 16.883762 | 53119344 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 880,906 | 17.908706 | 53119344 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/VVV | 10000 | 873,961 | 92.380528 | 53119344 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 845,913 | 2,325.581164 | 53119344 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 808,441 | 0.000009 | 53119344 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | QUID/USDC | 100 | 799,433 | 0.057317 | 53119345 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 787,536 | 0.803142 | 53119344 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 748,321 | 0.624469 | 53119344 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 734,083 | 4,739,579.479820 | 53119344 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 703,708 | 137,516.062161 | 53119344 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 703,238 | 0.621666 | 53119344 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2138 | 694,768 | 493,394.668641 | 53119344 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 685,287 | 0.111836 | 53119344 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |

## Recherche d'opportunités
- Cycles : 4472 ; routes examinées : 86873072 ; candidats optimisés : 290634 ; net attendu > 0 : 630 ; dernier cycle 159.7 ms
- Rejets (moteur) : {'spread_below_threshold': 85352679, 'liquidity_below_min': 1173373, 'negative_expected_net': 290004, 'unquotable': 51914, 'borrow_bound_too_small': 4472}
- Enregistrements de la session : 290634 ; net attendu > 0 : 630 ; simulés (eth_call de la vraie tx) : 29 (ok 7, échec 22) ; étiquettes ghost N+1 : 0/24 positives
- Décisions : {'REJECTED': 290634} ; motifs de rejet : {'below_safety_margin': 571, 'negative_expected_net': 290004, 'p_lower_below_threshold': 543, 'price_impact': 4, 'reliability_not_demonstrated': 87, 'simulation_failed': 22, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53118454 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,957.544562 USDC | 0.246475 USDC | 0.000000 USDC | 0.005575 USDC | 0.240900 USDC (0.2216 €) | — | 1.23 | 0.022 (n=95) | REJECTED | below_safety_margin(240900<391508), p_lower_below_threshold(0.02<0.75) |
| 53118454 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.844193 WETH | 0.000106 WETH | 0.000000 WETH | 0.000002 WETH | 0.000104 WETH (0.2214 €) | — | 1.23 | 0.022 (n=95) | REJECTED | below_safety_margin(103914578896718<168838500260664), p_lower_below_threshold(0.02<0.75) |
| 53118454 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 1,607.937014 USDC | 0.166668 USDC | 0.000000 USDC | 0.005224 USDC | 0.161444 USDC (0.1485 €) | — | 1.00 | 0.022 (n=95) | REJECTED | below_safety_margin(161444<321587), p_lower_below_threshold(0.02<0.75) |
| 53118454 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.695940 WETH | 0.000072 WETH | 0.000000 WETH | 0.000002 WETH | 0.000070 WETH (0.1484 €) | — | 1.00 | 0.022 (n=95) | REJECTED | below_safety_margin(69637879384958<139188046494659), p_lower_below_threshold(0.02<0.75) |
| 53117984 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 86.226081 USDC | 0.161516 USDC | 0.000000 USDC | 0.005222 USDC | 0.156294 USDC (0.1438 €) | — | 18.13 | 0.000 (n=52) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53118377 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,240.658245 USDC | 0.099339 USDC | 0.000000 USDC | 0.005572 USDC | 0.093767 USDC (0.0863 €) | — | 0.76 | 0.022 (n=95) | REJECTED | below_safety_margin(93767<248131), p_lower_below_threshold(0.02<0.75) |
| 53118377 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.537206 WETH | 0.000043 WETH | 0.000000 WETH | 0.000002 WETH | 0.000040 WETH (0.0860 €) | — | 0.75 | 0.022 (n=95) | REJECTED | below_safety_margin(40441239565660<107441233745586), p_lower_below_threshold(0.02<0.75) |
| 53118362 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 65.570830 USDC | 0.094423 USDC | 0.000000 USDC | 0.005574 USDC | 0.088849 USDC (0.0817 €) | — | 13.55 | 0.000 (n=53) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53118672 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 1,075.879526 USDC | 0.073838 USDC | 0.000000 USDC | 0.005580 USDC | 0.068258 USDC (0.0628 €) | — | 0.63 | 0.022 (n=95) | REJECTED | below_safety_margin(68258<215175), p_lower_below_threshold(0.02<0.75) |
| 53118672 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.463700 WETH | 0.000032 WETH | 0.000000 WETH | 0.000002 WETH | 0.000029 WETH (0.0626 €) | — | 0.63 | 0.022 (n=95) | REJECTED | below_safety_margin(29392559242787<92740000945717), p_lower_below_threshold(0.02<0.75) |
| 53119274 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 182.229676 USDC | 0.053224 USDC | 0.000000 USDC | 0.007044 USDC | 0.046180 USDC (0.0425 €) | — | 2.53 | 0.135 (n=353) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53119274 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.078221 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0423 €) | — | 2.53 | 0.135 (n=353) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 53117512 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 166.418370 USDC | 0.044255 USDC | 0.000000 USDC | 0.001203 USDC | 0.043052 USDC (0.0396 €) | — | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53117512 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.071718 WETH | 0.000019 WETH | 0.000000 WETH | 0.000001 WETH | 0.000019 WETH (0.0395 €) | 0.000019 WETH | 2.59 | 0.138 (n=346) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53118960 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 865.525455 USDC | 0.047081 USDC | 0.000000 USDC | 0.005251 USDC | 0.041830 USDC (0.0385 €) | — | 0.48 | 0.022 (n=95) | REJECTED | below_safety_margin(41830<173105), p_lower_below_threshold(0.02<0.75) |
| 53118960 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.373401 WETH | 0.000020 WETH | 0.000000 WETH | 0.000002 WETH | 0.000018 WETH (0.0384 €) | — | 0.48 | 0.022 (n=95) | REJECTED | below_safety_margin(17969937081783<74680190359091), p_lower_below_threshold(0.02<0.75) |
| 53119210 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002571 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0347 €) | — | 1.83 | 0.135 (n=353) | REJECTED | below_safety_margin(47<51), p_lower_below_threshold(0.14<0.75) |
| 53119210 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.089616 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0343 €) | — | 1.79 | 0.135 (n=353) | REJECTED | below_safety_margin(16062746396440<17923288089141), p_lower_below_threshold(0.14<0.75) |
| 53119210 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 198.958834 USDC | 0.043925 USDC | 0.000000 USDC | 0.007059 USDC | 0.036866 USDC (0.0339 €) | — | 1.85 | 0.135 (n=353) | REJECTED | below_safety_margin(36866<39791), p_lower_below_threshold(0.14<0.75) |
| 53118747 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 839.782713 USDC | 0.041562 USDC | 0.000000 USDC | 0.007354 USDC | 0.034208 USDC (0.0315 €) | — | 0.41 | 0.136 (n=351) | REJECTED | below_safety_margin(34208<167956), p_lower_below_threshold(0.14<0.75) |
| 53118747 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.359716 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0313 €) | — | 0.41 | 0.136 (n=351) | REJECTED | below_safety_margin(14677020686980<71943233165201), p_lower_below_threshold(0.14<0.75) |
| 53118747 | cbBTC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.009808 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0310 €) | — | 0.43 | 0.136 (n=351) | REJECTED | below_safety_margin(42<196), p_lower_below_threshold(0.14<0.75) |
| 53118438 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 103.765844 USDC | 0.040232 USDC | 0.000000 USDC | 0.006988 USDC | 0.033244 USDC (0.0306 €) | — | 3.20 | 0.087 (n=284) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53118437 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 103.765844 USDC | 0.040232 USDC | 0.000000 USDC | 0.006988 USDC | 0.033244 USDC (0.0306 €) | — | 3.20 | 0.087 (n=284) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.09<0.75) |
| 53118438 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001142 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0302 €) | — | 3.59 | 0.087 (n=284) | REJECTED | p_lower_below_threshold(0.09<0.75) |

## Fiabilité et décision
- Observations ghost : 2648 ; taux observé 0.094 ; borne inférieure crédible (0.9) 0.087 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 8.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
