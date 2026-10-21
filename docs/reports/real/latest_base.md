# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T09:57:46+00:00 ; durée 308.92 min ; blocs 52884388 → 52893651 (8239 vus)

## Connexion
- Requêtes RPC : 110061 ; erreurs : 273 ; latence p50/p95 : 536.5/1,839.3 ms
- Rafraîchissements d'état : 8239 ; âge des données au dernier bloc : 3.24 s ; changements de frais LP observés (pools à frais dynamiques) : 16687
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 86773 ; cycles déclenchés par événement : 4236 ; avance médiane sur le rafraîchissement multicall : 1,175 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,456.83 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 580 pools, 328 jetons, 21464 routes
- Par DEX : uniswap_v3 137, aerodrome 236 (quarantaine 1), aerodrome_slipstream 158, pancakeswap_v3 31, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 208 (rejetés 2) → 613 jetons ; pools candidats 3925 (énumérés 396, par paires 0), mesurés 582, sous le plancher de 10000.0 $ : 2 → gardés 580 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2447.377823, 'AERO': 0.859444, 'cbBTC': 82692.945421}
- Pools en quarantaine : 1 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52893728

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,338,635 | 2,456.831300 | 52893652 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 38,398,836 | 1.188247 | 52893652 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,070,877 | 95.084957 | 52893652 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,553,763 | 0.029458 | 52893652 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 12,571,934 | 0.029514 | 52893652 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,449,020 | 0.029529 | 52893652 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,974,845 | 0.000012 | 52893652 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 8,919,264 | 0.000012 | 52893652 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | WETH/USDC | 500 | 8,798,128 | 2,455.895900 | 52893652 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,472,618 | 2,457.892980 | 52893652 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 8,215,988 | 0.000012 | 52893652 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | WETH/USDC | 654 | 7,913,210 | 2,455.037666 | 52893652 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,326,197 | 0.001670 | 52893652 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,627,264 | 0.029446 | 52893652 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 5,219,730 | 0.024822 | 52893652 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,739,237 | 0.000279 | 52893652 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,735,655 | 0.802394 | 52893652 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,444,440 | 2,454.914939 | 52893652 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,426,917 | 0.998741 | 52893652 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 4,056,499 | 34,791.780640 | 52893652 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDT | 418 | 3,612,885 | 2,458.890549 | 52893652 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/AERO | 10000 | 3,344,876 | 2,898.473147 | 52893652 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 3,099,195 | 1.179524 | 52893652 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,806,122 | 1,053.795334 | 52893652 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,766,505 | 95.021071 | 52893652 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,742,755 | 398.194798 | 52893652 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,545,144 | 1.142087 | 52893652 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,275,853 | 0.000012 | 52893652 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | WETH/FAI | 10000 | 2,250,806 | 1,209,488.803510 | 52893652 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,198,308 | 0.000010 | 52893652 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,080,570 | 0.000012 | 52893652 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,027,072 | 1.383640 | 52893652 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,958,698 | 0.000000 | 52893652 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,932,678 | 15.751210 | 52893652 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | weETH_04c0/WETH | 500 | 1,914,007 | 1.105697 | 52893652 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| uniswap_v3 | XDP/USDC | 100 | 1,811,821 | 0.019233 | 52893652 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,724,126 | 0.916061 | 52893652 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| aerodrome | fBOMB/USDC | 10000 | 1,716,003 | 0.021473 | 52893652 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,710,848 | 1.490009 | 52893652 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome | WETH/msETH (stable) | 500 | 1,695,958 | 2.310993 | 52893652 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | WETH/AERO | 3000 | 1,677,527 | 2,918.024336 | 52893652 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,642,503 | 13,489.328033 | 52893652 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,172 | 0.826524 | 52893652 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,399,113 | 1.122275 | 52893652 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,354,244 | 0.004793 | 52893652 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,339,295 | 0.000280 | 52893652 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| uniswap_v3 | DRB/WETH | 10000 | 1,327,213 | 0.000000 | 52893652 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/cbBTC | 3000 | 1,317,119 | 0.029528 | 52893652 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,288,857 | 2,455.976079 | 52893652 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,234,247 | 63.787842 | 52893652 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,229,494 | 34,790,527.077835 | 52893652 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,219,561 | 23.077108 | 52893652 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | WETH/EDEL | 7000 | 1,206,789 | 70,945.887477 | 52893652 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 1,201,136 | 1,134,303.455349 | 52893652 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,184,338 | 483,701.112498 | 52893652 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | USDC/NOCK | 3000 | 1,184,242 | 44.928738 | 52893652 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,181,616 | 0.436740 | 52893652 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,164,566 | 0.886295 | 52893652 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,162,719 | 1.106158 | 52893652 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,111,839 | 20,586,460.917356 | 52893652 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 12474 ; routes examinées : 267741936 ; candidats optimisés : 1548689 ; net attendu > 0 : 319 ; dernier cycle 272.6 ms
- Rejets (moteur) : {'spread_below_threshold': 263514326, 'liquidity_below_min': 1779518, 'negative_expected_net': 1548370, 'pool_quarantined': 881252, 'borrow_bound_too_small': 12449, 'cycle_budget_exhausted': 5702}
- Enregistrements de la session : 1548689 ; net attendu > 0 : 319 ; simulés (eth_call de la vraie tx) : 109 (ok 6, échec 103) ; étiquettes ghost N+1 : 1/48 positives
- Décisions : {'REJECTED': 1548689} ; motifs de rejet : {'below_safety_margin': 191, 'negative_expected_net': 1548370, 'p_lower_below_threshold': 302, 'price_impact': 193, 'reliability_not_demonstrated': 17, 'simulation_failed': 103, 'stale_data': 29}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52887788 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 76.776773 USDC | 0.127547 USDC | 0.000000 USDC | 0.005482 USDC | 0.122065 USDC (0.1123 €) | — | 15.90 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52890720 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 123.285577 USDC | 0.100092 USDC | 0.000000 USDC | 0.007360 USDC | 0.092732 USDC (0.0853 €) | — | 7.52 | 0.098 (n=146) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52890720 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.050473 WETH | 0.000041 WETH | 0.000000 WETH | 0.000003 WETH | 0.000038 WETH (0.0852 €) | — | 7.49 | 0.098 (n=146) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52890720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 118.379409 USDC | 0.093978 USDC | 0.000000 USDC | 0.007360 USDC | 0.086618 USDC (0.0797 €) | — | 7.32 | 0.145 (n=82) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52890720 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.048238 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0796 €) | — | 7.32 | 0.145 (n=82) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 52890720 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 110.301556 USDC | 0.079622 USDC | 0.000000 USDC | 0.007360 USDC | 0.072262 USDC (0.0665 €) | — | 6.55 | 0.145 (n=82) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52890720 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.044981 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0664 €) | — | 6.55 | 0.145 (n=82) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.14<0.75) |
| 52890720 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 105.339658 USDC | 0.073712 USDC | 0.000000 USDC | 0.007360 USDC | 0.066352 USDC (0.0610 €) | — | 6.30 | 0.098 (n=146) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52890720 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.043091 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0610 €) | — | 6.28 | 0.098 (n=146) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52887787 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 53.684559 USDC | 0.062580 USDC | 0.000000 USDC | 0.005482 USDC | 0.057098 USDC (0.0525 €) | — | 10.64 | 0.000 (n=43) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52890720 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 98.389513 USDC | 0.063287 USDC | 0.000000 USDC | 0.007360 USDC | 0.055927 USDC (0.0515 €) | — | 5.68 | 0.145 (n=82) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52890720 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.040132 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0514 €) | — | 5.68 | 0.145 (n=82) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52890732 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 49.668437 USDC | 0.053289 USDC | 0.000000 USDC | 0.005499 USDC | 0.047790 USDC (0.0440 €) | — | 9.62 | 0.000 (n=45) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52890720 | USDC→[sushiswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 75.481312 USDC | 0.051130 USDC | 0.000000 USDC | 0.007360 USDC | 0.043770 USDC (0.0403 €) | — | 5.80 | 0.145 (n=82) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52890720 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[sushiswap_v3]→WETH | 0.030784 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0402 €) | — | 5.79 | 0.145 (n=82) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 52888691 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 45.892851 USDC | 0.045720 USDC | 0.000000 USDC | 0.005481 USDC | 0.040239 USDC (0.0370 €) | — | 8.77 | 0.000 (n=44) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 52890712 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 66.239597 USDC | 0.028533 USDC | 0.000000 USDC | 0.007360 USDC | 0.021173 USDC (0.0195 €) | 0.021173 USDC | 3.20 | 0.099 (n=144) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52890712 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 66.239597 USDC | 0.028533 USDC | 0.000000 USDC | 0.007360 USDC | 0.021173 USDC (0.0195 €) | — | 3.20 | 0.099 (n=144) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52890712 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.027184 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0195 €) | 0.000009 WETH | 3.18 | 0.099 (n=144) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 52890712 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.027184 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0195 €) | — | 3.18 | 0.099 (n=144) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 52890712 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 62.475341 USDC | 0.025839 USDC | 0.000000 USDC | 0.007360 USDC | 0.018479 USDC (0.0170 €) | — | 2.96 | 0.286 (n=89) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 52890712 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC | 62.475341 USDC | 0.025839 USDC | 0.000000 USDC | 0.007360 USDC | 0.018479 USDC (0.0170 €) | — | 2.96 | 0.286 (n=89) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 52890712 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025389 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | 0.000008 WETH | 2.97 | 0.286 (n=89) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 52890712 | WETH→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.025389 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0170 €) | — | 2.97 | 0.286 (n=89) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.29<0.75) |
| 52888691 | USDC→[pancakeswap_v3]→PLAY→[aerodrome]→USDC | 14.917647 USDC | 0.021142 USDC | 0.000000 USDC | 0.005144 USDC | 0.015998 USDC (0.0147 €) | — | 10.72 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 1641 ; taux observé 0.100 ; borne inférieure crédible (0.9) 0.091 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
