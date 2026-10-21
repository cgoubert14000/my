# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-21T22:15:49+00:00 ; durée 36.91 min ; blocs 52914691 → 52915799 (1098 vus)

## Connexion
- Requêtes RPC : 15141 ; erreurs : 0 ; latence p50/p95 : 117.6/970.5 ms
- Rafraîchissements d'état : 1099 ; âge des données au dernier bloc : 1.5 s ; changements de frais LP observés (pools à frais dynamiques) : 1344
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 15092 ; cycles déclenchés par événement : 1085 ; avance médiane sur le rafraîchissement multicall : 854 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,492.49 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 579 pools, 326 jetons, 22742 routes
- Par DEX : uniswap_v3 137, aerodrome 234 (quarantaine 2), aerodrome_slipstream 158, pancakeswap_v3 32, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 206 (rejetés 2) → 611 jetons ; pools candidats 3912 (énumérés 393, par paires 0), mesurés 581, sous le plancher de 10000.0 $ : 2 → gardés 579 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2492.485305, 'AERO': 0.830593, 'cbBTC': 84747.685068}
- Pools en quarantaine : 2 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52915947; aerodrome:fBOMB/cbBTC@0x3d36Cf: simulation failed ×5 (model/chain mismatch) — until block 52915947

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 158,094,255 | 2,492.486278 | 52915799 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 28,931,432 | 1.210586 | 52915799 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome | WETH/VVV | 3000 | 18,187,488 | 90.665285 | 52915799 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 17,718,470 | 0.029486 | 52915799 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,744,132 | 0.029438 | 52915799 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,630,738 | 0.029499 | 52915799 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,917,603 | 0.000012 | 52915799 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,876,271 | 2,492.873949 | 52915799 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 8,420,507 | 0.000012 | 52915799 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/USDC | 3000 | 8,358,970 | 2,493.385368 | 52915799 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 7,426,623 | 0.000012 | 52915799 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,420,362 | 0.001663 | 52915799 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 579 | 7,147,027 | 2,492.441884 | 52915799 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,673,772 | 0.029431 | 52915799 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | fBOMB/AERO | 10000 | 4,864,836 | 0.023224 | 52915799 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,592,538 | 2,492.671946 | 52915799 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,457,583 | 0.999948 | 52915799 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,246,514 | 0.000278 | 52915799 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/USDT | 406 | 4,184,083 | 2,495.565722 | 52915799 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | WETH/KTA | 3000 | 4,121,380 | 34,688.730789 | 52915799 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,336,025 | 2,996.099146 | 52915799 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/wstETH | 90 | 3,192,651 | 0.802246 | 52915799 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | WETH/VVV | 2727 | 2,873,492 | 90.688303 | 52915799 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,716,179 | 392.524190 | 52915799 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 2,340,232 | 0.000010 | 52915799 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,298,098 | 1,193,481.314505 | 52915799 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 2,283,877 | 0.915907 | 52915799 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,281,006 | 0.000012 | 52915799 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 2,115,928 | 1,045.035920 | 52915799 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 2,113,059 | 0.000012 | 52915799 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,030,750 | 1.383527 | 52915799 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,967,611 | 0.000000 | 52915799 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | weETH_04c0/WETH | 500 | 1,940,630 | 1.105712 | 52915799 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,858,686 | 15.920421 | 52915799 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| uniswap_v3 | XDP/USDC | 100 | 1,822,940 | 0.019004 | 52915799 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/AERO | 10000 | 1,809,418 | 1.202234 | 52915799 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| aerodrome | WETH/msETH (stable) | 500 | 1,718,002 | 2.310661 | 52915799 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,703,368 | 1.497063 | 52915799 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,683,194 | 3,017.689103 | 52915799 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,679,089 | 13,317.373422 | 52915799 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | cbETH/WETH | 60 | 1,572,485 | 1.142104 | 52915799 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,542 | 0.826835 | 52915799 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | EURC/USDC | 70 | 1,438,443 | 1.123379 | 52915799 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,405,985 | 0.004892 | 52915799 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | fBOMB/USDC | 10000 | 1,403,174 | 0.019677 | 52915799 | `0xFf8e0bD2d8F02904e7e18Dd00ea50aeC68f37A10` |
| uniswap_v3 | DRB/WETH | 10000 | 1,387,990 | 0.000000 | 52915799 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,356,600 | 0.000279 | 52915799 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome | WETH/cbBTC | 3000 | 1,325,505 | 0.029502 | 52915799 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,304,733 | 2,492.873907 | 52915799 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,278,350 | 23.105225 | 52915799 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome | USDC/NOCK | 3000 | 1,254,416 | 40.042849 | 52915799 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/WELL | 10000 | 1,252,702 | 1,073,321.750616 | 52915799 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/doginme | 10000 | 1,240,465 | 35,330,904.278284 | 52915799 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,232,698 | 63.948314 | 52915799 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/EDEL | 7000 | 1,215,386 | 71,998.111764 | 52915799 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,207,964 | 485,402.667813 | 52915799 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,175,696 | 0.436598 | 52915799 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |
| aerodrome_slipstream | msUSD/USDC | 500 | 1,149,576 | 0.886164 | 52915799 | `0x7501bc8Bb51616F79bfA524E464fb7B41f0B10fB` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,143,258 | 1.106154 | 52915799 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,118,214 | 20,906,688.151904 | 52915799 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |

## Recherche d'opportunités
- Cycles : 2183 ; routes examinées : 49645786 ; candidats optimisés : 330826 ; net attendu > 0 : 30 ; dernier cycle 242.6 ms
- Rejets (moteur) : {'spread_below_threshold': 48752315, 'liquidity_below_min': 449636, 'negative_expected_net': 330796, 'pool_quarantined': 110826, 'borrow_bound_too_small': 2183}
- Enregistrements de la session : 330826 ; net attendu > 0 : 30 ; simulés (eth_call de la vraie tx) : 17 (ok 0, échec 17) ; étiquettes ghost N+1 : 0/9 positives
- Décisions : {'REJECTED': 330826} ; motifs de rejet : {'negative_expected_net': 330796, 'p_lower_below_threshold': 28, 'price_impact': 11, 'reliability_not_demonstrated': 2, 'simulation_failed': 17}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52915567 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 31.983662 USDC | 0.077174 USDC | 0.000000 USDC | 0.005263 USDC | 0.071911 USDC (0.0662 €) | — | 22.48 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52915729 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 31.332892 USDC | 0.075372 USDC | 0.000000 USDC | 0.005264 USDC | 0.070108 USDC (0.0645 €) | — | 22.38 | 0.000 (n=17) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 52915437 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040504 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0581 €) | — | 6.25 | 0.109 (n=163) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 100.466132 USDC | 0.070583 USDC | 0.000000 USDC | 0.007495 USDC | 0.063088 USDC (0.0580 €) | — | 6.28 | 0.109 (n=163) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915437 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040412 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0577 €) | — | 6.23 | 0.133 (n=89) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 100.336417 USDC | 0.070164 USDC | 0.000000 USDC | 0.007495 USDC | 0.062669 USDC (0.0577 €) | — | 6.25 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.040023 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0571 €) | — | 6.23 | 0.109 (n=163) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.11<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 99.595363 USDC | 0.069558 USDC | 0.000000 USDC | 0.007495 USDC | 0.062063 USDC (0.0571 €) | — | 6.23 | 0.109 (n=163) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 52915437 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.039020 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0547 €) | — | 6.11 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 96.885708 USDC | 0.066862 USDC | 0.000000 USDC | 0.007495 USDC | 0.059367 USDC (0.0546 €) | — | 6.13 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[sushiswap_v3]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.033505 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0526 €) | — | 6.85 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[sushiswap_v3]→USDC | 83.007657 USDC | 0.064632 USDC | 0.000000 USDC | 0.007495 USDC | 0.057137 USDC (0.0526 €) | — | 6.88 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.011758 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0152 €) | — | 5.65 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 29.135738 USDC | 0.024005 USDC | 0.000000 USDC | 0.007495 USDC | 0.016510 USDC (0.0152 €) | — | 5.67 | 0.133 (n=89) | REJECTED | p_lower_below_threshold(0.13<0.75) |
| 52915437 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.022877 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0140 €) | — | 2.66 | 0.258 (n=102) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 57.126792 USDC | 0.022655 USDC | 0.000000 USDC | 0.007495 USDC | 0.015160 USDC (0.0139 €) | — | 2.65 | 0.258 (n=102) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 52915437 | WETH→[aerodrome]→USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH | 0.004364 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0077 €) | — | 7.73 | 0.034 (n=125) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52915437 | USDC→[aerodrome_slipstream]→VELVET→[aerodrome_slipstream]→WETH→[aerodrome]→USDC | 10.838698 USDC | 0.015527 USDC | 0.000000 USDC | 0.007151 USDC | 0.008376 USDC (0.0077 €) | — | 7.73 | 0.034 (n=125) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 52915249 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 22.004393 USDC | 0.010444 USDC | 0.000000 USDC | 0.005601 USDC | 0.004843 USDC (0.0045 €) | — | 2.20 | 0.024 (n=60) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 52915645 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.47 | 0.011 (n=125) | REJECTED | price_impact(215bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52915646 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.47 | 0.011 (n=126) | REJECTED | price_impact(215bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52915646 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.47 | 0.011 (n=126) | REJECTED | price_impact(215bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52915647 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.47 | 0.011 (n=126) | REJECTED | price_impact(215bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52915647 | cbBTC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→cbBTC | 0.000012 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0008 €) | — | 8.47 | 0.011 (n=126) | REJECTED | price_impact(215bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.01<0.75) |
| 52915344 | USDC→[aerodrome_slipstream]→AERO→[aerodrome]→fBOMB→[aerodrome]→USDC | 0.999999 USDC | 0.007312 USDC | 0.000000 USDC | 0.006808 USDC | 0.000504 USDC (0.0005 €) | — | 5.04 | 0.035 (n=123) | REJECTED | price_impact(205bps>150.0), simulation_failed:revert 0xa932492f, p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 1759 ; taux observé 0.099 ; borne inférieure crédible (0.9) 0.090 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 9.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
