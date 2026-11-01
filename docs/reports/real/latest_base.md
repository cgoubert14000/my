# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T03:49:09+00:00 ; durée 264.39 min ; blocs 53349866 → 53357796 (7882 vus)

## Connexion
- Requêtes RPC : 94728 ; erreurs : 0 ; latence p50/p95 : 67.7/999.0 ms
- Rafraîchissements d'état : 7882 ; âge des données au dernier bloc : 2.77 s ; changements de frais LP observés (pools à frais dynamiques) : 6144
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 56376 ; cycles déclenchés par événement : 7429 ; avance médiane sur le rafraîchissement multicall : 474 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,265.71 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 503 pools, 291 jetons, 18668 routes
- Par DEX : uniswap_v3 140, aerodrome_slipstream 114, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3742 (énumérés 319, par paires 0), mesurés 506, sous le plancher de 10000.0 $ : 3 → gardés 503 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2257.094934, 'cbBTC': 77437.995276, 'AERO': 0.643751}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,902,780 | 2,265.713356 | 53357797 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,138,667 | 0.029171 | 53357797 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,356,989 | 0.000013 | 53357797 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,097,097 | 0.029145 | 53357797 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,949,594 | 96.132326 | 53357797 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,894,896 | 2,265.698638 | 53357797 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,693,718 | 0.001608 | 53357797 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,766,068 | 1.549061 | 53357797 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,274,237 | 0.029167 | 53357797 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,089,523 | 0.998851 | 53357797 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,070,753 | 2,265.507917 | 53357797 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,967,218 | 2,265.717653 | 53357797 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,562,127 | 37,863.287057 | 53357797 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,701,408 | 0.029159 | 53357797 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,434,147 | 96.164802 | 53357797 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,185,678 | 0.000013 | 53357797 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,082,400 | 1,200,192.118148 | 53357797 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,764,459 | 0.000000 | 53357797 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,712,363 | 0.017328 | 53357797 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,677,182 | 0.000013 | 53357797 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,585,080 | 0.000013 | 53357797 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,557,272 | 424.855438 | 53357797 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,546,920 | 1.490152 | 53357797 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,507,899 | 2,266.826599 | 53357797 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,383 | 0.825799 | 53357797 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,439,918 | 3,508.545184 | 53357797 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,412,136 | 2,271.551787 | 53357797 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,351,669 | 2,265.694568 | 53357797 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,329,031 | 0.005180 | 53357797 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,308,821 | 14,567.887119 | 53357797 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,307,209 | 0.000013 | 53357797 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,174,072 | 70.494059 | 53357797 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,145,535 | 33,818,806.668200 | 53357797 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,070,927 | 513,798.764002 | 53357797 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,055,529 | 0.000000 | 53357797 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,963 | 21,602,616.147259 | 53357797 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 1,008,581 | 77,035.082640 | 53357797 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,795 | 95.662241 | 53357797 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 992,292 | 0.042438 | 53357797 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/VELVET | 100 | 991,119 | 19.442400 | 53357797 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 968,534 | 66.736355 | 53357797 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 963,722 | 1,155,608.772485 | 53357797 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 948,699 | 972.158493 | 53357797 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 925,635 | 2,249.741211 | 53357797 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 881,501 | 3,494.994793 | 53357797 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 865,543 | 0.000547 | 53357797 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4515 | 838,815 | 19.410903 | 53357797 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 825,068 | 0.061280 | 53357797 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 767,168 | 0.803065 | 53357797 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,675 | 0.000261 | 53357797 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,825 | 0.593102 | 53357797 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 714,565 | 4,750,398.059902 | 53357797 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 696,241 | 0.000008 | 53357797 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 676,303 | 141,552.406150 | 53357797 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 664,646 | 512,870.778409 | 53357797 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 660,371 | 2.338238 | 53357797 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 659,572 | 0.547546 | 53357797 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 612,084 | 0.092945 | 53357797 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 608,071 | 0.916303 | 53357797 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2715 | 558,147 | 971.917938 | 53357797 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 15310 ; routes examinées : 285807080 ; candidats optimisés : 852222 ; net attendu > 0 : 290 ; dernier cycle 178.7 ms
- Rejets (moteur) : {'spread_below_threshold': 280878508, 'liquidity_below_min': 4012236, 'negative_expected_net': 851932, 'unquotable': 48564, 'borrow_bound_too_small': 15306, 'cycle_budget_exhausted': 244}
- Enregistrements de la session : 852222 ; net attendu > 0 : 290 ; simulés (eth_call de la vraie tx) : 6 (ok 6, échec 0) ; étiquettes ghost N+1 : 3/3 positives
- Décisions : {'REJECTED': 852222} ; motifs de rejet : {'below_safety_margin': 274, 'negative_expected_net': 851932, 'p_lower_below_threshold': 290}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53354648 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 81.773567 USDC | 0.017131 USDC | 0.000000 USDC | 0.006803 USDC | 0.010328 USDC (0.0095 €) | — | 1.26 | 0.141 (n=665) | REJECTED | below_safety_margin(10328<16354), p_lower_below_threshold(0.14<0.75) |
| 53354648 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.036237 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0095 €) | — | 1.25 | 0.141 (n=665) | REJECTED | below_safety_margin(4537085912177<7247457219089), p_lower_below_threshold(0.14<0.75) |
| 53353989 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 195.744242 USDC | 0.014192 USDC | 0.000000 USDC | 0.005078 USDC | 0.009114 USDC (0.0084 €) | — | 0.47 | 0.043 (n=154) | REJECTED | below_safety_margin(9114<39148), p_lower_below_threshold(0.04<0.75) |
| 53353989 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 195.744242 USDC | 0.014192 USDC | 0.000000 USDC | 0.005078 USDC | 0.009114 USDC (0.0084 €) | — | 0.47 | 0.043 (n=154) | REJECTED | below_safety_margin(9114<39148), p_lower_below_threshold(0.04<0.75) |
| 53353989 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.086248 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0084 €) | — | 0.47 | 0.043 (n=154) | REJECTED | below_safety_margin(4015419952537<17249699264583), p_lower_below_threshold(0.04<0.75) |
| 53353989 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.086248 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0084 €) | — | 0.47 | 0.043 (n=154) | REJECTED | below_safety_margin(4015419952537<17249699264583), p_lower_below_threshold(0.04<0.75) |
| 53353790 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 89.226461 USDC | 0.015337 USDC | 0.000000 USDC | 0.006807 USDC | 0.008530 USDC (0.0078 €) | — | 0.96 | 0.189 (n=283) | REJECTED | below_safety_margin(8530<17845), p_lower_below_threshold(0.19<0.75) |
| 53353790 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 89.226461 USDC | 0.015337 USDC | 0.000000 USDC | 0.006807 USDC | 0.008530 USDC (0.0078 €) | — | 0.96 | 0.189 (n=283) | REJECTED | below_safety_margin(8530<17845), p_lower_below_threshold(0.19<0.75) |
| 53353790 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.039464 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0078 €) | — | 0.95 | 0.189 (n=283) | REJECTED | below_safety_margin(3752521863228<7892883045608), p_lower_below_threshold(0.19<0.75) |
| 53353790 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.039464 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0078 €) | — | 0.95 | 0.189 (n=283) | REJECTED | below_safety_margin(3752521863228<7892883045608), p_lower_below_threshold(0.19<0.75) |
| 53353790 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 95.702758 USDC | 0.014858 USDC | 0.000000 USDC | 0.006807 USDC | 0.008051 USDC (0.0074 €) | — | 0.84 | 0.141 (n=665) | REJECTED | below_safety_margin(8051<19140), p_lower_below_threshold(0.14<0.75) |
| 53353790 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 95.702758 USDC | 0.014858 USDC | 0.000000 USDC | 0.006807 USDC | 0.008051 USDC (0.0074 €) | — | 0.84 | 0.141 (n=665) | REJECTED | below_safety_margin(8051<19140), p_lower_below_threshold(0.14<0.75) |
| 53353790 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.042314 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0074 €) | — | 0.84 | 0.141 (n=665) | REJECTED | below_safety_margin(3540901357682<8462845750558), p_lower_below_threshold(0.14<0.75) |
| 53353790 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.042314 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0074 €) | — | 0.84 | 0.141 (n=665) | REJECTED | below_safety_margin(3540901357682<8462845750558), p_lower_below_threshold(0.14<0.75) |
| 53354648 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 70.310722 USDC | 0.013791 USDC | 0.000000 USDC | 0.006803 USDC | 0.006988 USDC (0.0064 €) | — | 0.99 | 0.141 (n=665) | REJECTED | below_safety_margin(6988<14062), p_lower_below_threshold(0.14<0.75) |
| 53353785 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000743 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0064 €) | — | 1.21 | 0.189 (n=283) | REJECTED | below_safety_margin(9<14), p_lower_below_threshold(0.19<0.75) |
| 53353786 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000743 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0064 €) | — | 1.21 | 0.189 (n=283) | REJECTED | below_safety_margin(9<14), p_lower_below_threshold(0.19<0.75) |
| 53353786 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.000743 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0064 €) | — | 1.21 | 0.189 (n=283) | REJECTED | below_safety_margin(9<14), p_lower_below_threshold(0.19<0.75) |
| 53354648 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.031011 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0064 €) | — | 0.99 | 0.141 (n=665) | REJECTED | below_safety_margin(3067130329036<6202188619538), p_lower_below_threshold(0.14<0.75) |
| 53353785 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000625 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.28 | 0.141 (n=665) | REJECTED | below_safety_margin(8<12), p_lower_below_threshold(0.14<0.75) |
| 53353786 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000625 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.28 | 0.141 (n=665) | REJECTED | below_safety_margin(8<12), p_lower_below_threshold(0.14<0.75) |
| 53353786 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.000625 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0057 €) | — | 1.28 | 0.141 (n=665) | REJECTED | below_safety_margin(8<12), p_lower_below_threshold(0.14<0.75) |
| 53353785 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 69.248805 USDC | 0.012971 USDC | 0.000000 USDC | 0.006788 USDC | 0.006183 USDC (0.0057 €) | — | 0.89 | 0.189 (n=283) | REJECTED | below_safety_margin(6183<13849), p_lower_below_threshold(0.19<0.75) |
| 53353786 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 69.248805 USDC | 0.012971 USDC | 0.000000 USDC | 0.006788 USDC | 0.006183 USDC (0.0057 €) | — | 0.89 | 0.189 (n=283) | REJECTED | below_safety_margin(6183<13849), p_lower_below_threshold(0.19<0.75) |
| 53353786 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 69.248805 USDC | 0.012971 USDC | 0.000000 USDC | 0.006788 USDC | 0.006183 USDC (0.0057 €) | — | 0.89 | 0.189 (n=283) | REJECTED | below_safety_margin(6183<13849), p_lower_below_threshold(0.19<0.75) |

## Fiabilité et décision
- Observations ghost : 4035 ; taux observé 0.129 ; borne inférieure crédible (0.9) 0.122 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
