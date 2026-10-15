# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-10-15T14:57:39+00:00 ; durée 89.06 min ; blocs 52640781 → 52643454 (2373 vus)

## Connexion
- Requêtes RPC : 31058 ; erreurs : 328 ; latence p50/p95 : 153.6/1,635.5 ms
- Rafraîchissements d'état : 2374 ; âge des données au dernier bloc : 2.35 s ; changements de frais LP observés (pools à frais dynamiques) : 13007
- Flux d'événements (WebSocket Swap/Sync) : non connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,389.13 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 570 pools, 326 jetons, 21328 routes
- Par DEX : uniswap_v3 136, aerodrome 235 (quarantaine 4), aerodrome_slipstream 152, pancakeswap_v3 30, uniswap_v2 14, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 205 (rejetés 2) → 610 jetons ; pools candidats 3864 (énumérés 389, par paires 0), mesurés 572, sous le plancher de 10000.0 $ : 2 → gardés 570 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2346.001193, 'AERO': 0.837627, 'cbBTC': 80168.530844}
- Pools en quarantaine : 4 — aerodrome:fBOMB/AERO@0xbBf71A: simulation failed ×5 (model/chain mismatch) — until block 52643481; aerodrome:fBOMB/USDC@0xFf8e0b: simulation failed ×5 (model/chain mismatch) — until block 52643481; aerodrome:WETH/fBOMB@0x4F9Dc2: simulation failed ×5 (model/chain mismatch) — until block 52643493; aerodrome:fBOMB/USDbC@0xC39566: simulation failed ×5 (model/chain mismatch) — until block 52643493

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 144,260,841 | 2,389.134149 | 52643454 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| aerodrome | USDC/AERO | 3000 | 44,999,753 | 1.136951 | 52643454 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| uniswap_v3 | WETH/cbBTC | 500 | 18,002,106 | 0.029245 | 52643454 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| aerodrome | WETH/VVV | 3000 | 16,398,234 | 97.623085 | 52643454 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 13,648,358 | 0.029207 | 52643454 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 10,395,429 | 0.029189 | 52643454 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,634,334 | 0.000012 | 52643454 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,983,152 | 2,392.817788 | 52643454 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/USDC | 3000 | 8,879,987 | 2,389.503653 | 52643454 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/cbBTC | 354 | 7,964,690 | 0.000012 | 52643454 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 7,173,968 | 0.001670 | 52643454 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | WETH/USDC | 803 | 7,128,567 | 2,392.437580 | 52643454 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | USDC/cbBTC | 580 | 6,345,498 | 0.000012 | 52643454 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,263,693 | 0.029257 | 52643454 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | VIRTUAL/WETH | 10000 | 4,611,661 | 0.000275 | 52643454 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/wstETH | 90 | 4,493,094 | 0.802388 | 52643454 | `0x861A2922bE165a5Bd41b1E482B49216b465e1B5F` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,299,137 | 0.999754 | 52643454 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | USDC/AERO | 10000 | 4,290,642 | 1.145141 | 52643454 | `0xBE00fF35AF70E8415D0eB605a286D8A45466A4c1` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,282,853 | 2,392.627997 | 52643454 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,922,197 | 35,192.145817 | 52643454 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome | WETH/AERO | 10000 | 3,503,934 | 2,736.814389 | 52643454 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | USDC/cbBTC | 3000 | 2,846,188 | 0.000012 | 52643454 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 2,695,172 | 400.992857 | 52643454 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | fBOMB/AERO | 10000 | 2,675,588 | 0.026140 | 52643454 | `0xbBf71AAD6E1F8D180D3B1D898528654c1d18b2fF` |
| aerodrome_slipstream | WETH/VVV | 2814 | 2,623,958 | 97.628157 | 52643454 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | cbETH/WETH | 60 | 2,496,385 | 1.141666 | 52643454 | `0x47cA96Ea59C13F72745928887f84C9F52C3D7348` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 2,471,074 | 0.000011 | 52643454 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/FAI | 10000 | 2,195,196 | 1,202,432.800442 | 52643454 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome | USDC/MAI (stable) | 3000 | 2,111,377 | 1.196132 | 52643454 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/USDT | 460 | 2,009,561 | 2,397.057352 | 52643454 | `0x9785eF59E2b499fB741674ecf6fAF912Df7b3C1b` |
| aerodrome | USDC/alUSDb (stable) | 500 | 2,008,820 | 1.403288 | 52643454 | `0x32d6Ec4400fBdd4085ce1e1664C48F8D21c4f9aa` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,990,570 | 0.000000 | 52643454 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | WETH/bsdETH | 100 | 1,805,777 | 0.916541 | 52643454 | `0x2ae9DF02539887d4EbcE0230168a302d34784c82` |
| uniswap_v3 | XDP/USDC | 100 | 1,788,840 | 0.019025 | 52643454 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,767,100 | 0.000012 | 52643454 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/AAVE | 3000 | 1,741,344 | 15.703516 | 52643454 | `0x4a79B0168296c0eF7b8F314973B82aD406a29f1B` |
| aerodrome | WETH/msETH (stable) | 500 | 1,692,083 | 2.304171 | 52643454 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,660,674 | 13,731.832028 | 52643454 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 1,503,787 | 2,716.289855 | 52643454 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | weETH_04c0/WETH | 500 | 1,477,179 | 1.105494 | 52643454 | `0x91F0f34916Ca4E2cCe120116774b0e4fA0cdcaA8` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,898 | 0.831211 | 52643454 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/AERO | 3000 | 1,353,036 | 2,717.625740 | 52643454 | `0x82321f3BEB69f503380D6B233857d5C43562e2D0` |
| uniswap_v3 | DRB/WETH | 10000 | 1,348,482 | 0.000000 | 52643454 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v2 | VIRTUAL/WETH | 3000 | 1,292,474 | 0.000277 | 52643454 | `0xE31c372a7Af875b3B5E0F3713B17ef51556da667` |
| aerodrome_slipstream | WETH/msETH | 500 | 1,290,502 | 1.131043 | 52643454 | `0x74F72788F4814D7fF3C49B44684aa98Eee140C0E` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,288,989 | 0.004676 | 52643454 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome | USDC/SEND | 3000 | 1,248,016 | 62.388256 | 52643454 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | EURC/USDC | 79 | 1,244,508 | 1.120465 | 52643454 | `0xE846373C1a92B167b4E9cd5d8E4d6B1Db9E90EC7` |
| aerodrome_slipstream | WETH/uSOL | 1500 | 1,242,106 | 22.995637 | 52643454 | `0x0225Ba893D5f8Ecd6d2022f9dEC59b34F61098A1` |
| aerodrome_slipstream | WETH/MORPHO | 2760 | 1,233,649 | 1,007.105827 | 52643454 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,204,803 | 2,392.827286 | 52643454 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,200,840 | 34,049,986.918176 | 52643454 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | weETH_04c0/WETH | 85 | 1,184,223 | 1.105591 | 52643454 | `0xbD3cd0D9d429b41F0a2e1C026552Bd598294d5E0` |
| aerodrome | WETH/cbBTC | 3000 | 1,150,407 | 0.029187 | 52643454 | `0x2578365B3dfA7FfE60108e181EFb79FeDdec2319` |
| aerodrome | WETH/WELL | 10000 | 1,143,174 | 1,184,408.402905 | 52643454 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,141,624 | 494,673.499808 | 52643454 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| aerodrome | WETH/EDEL | 7000 | 1,129,643 | 77,834.494231 | 52643454 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 1,126,670 | 49.647762 | 52643454 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,114,825 | 14.212295 | 52643454 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | msUSD/USDC (stable) | 500 | 1,105,619 | 0.435667 | 52643454 | `0xcEFC8B799a8EE5D9b312aeca73262645D664AaF7` |

## Recherche d'opportunités
- Cycles : 2373 ; routes examinées : 50611344 ; candidats optimisés : 351434 ; net attendu > 0 : 904 ; dernier cycle 307.1 ms
- Rejets (moteur) : {'spread_below_threshold': 49721139, 'liquidity_below_min': 436695, 'negative_expected_net': 350530, 'borrow_bound_too_small': 51203, 'pool_quarantined': 41092, 'unquotable': 5924, 'cycle_budget_exhausted': 3857}
- Enregistrements de la session : 351434 ; net attendu > 0 : 904 ; simulés (eth_call de la vraie tx) : 60 (ok 49, échec 11) ; étiquettes ghost N+1 : 3/50 positives
- Décisions : {'REJECTED': 351434} ; motifs de rejet : {'below_safety_margin': 534, 'negative_expected_net': 350530, 'p_lower_below_threshold': 367, 'price_impact': 27, 'reliability_not_demonstrated': 537, 'simulation_failed': 11, 'stale_data': 113}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 442.062489 USDC | 0.298836 USDC | 0.000000 USDC | 0.008229 USDC | 0.290607 USDC (0.2674 €) | — | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.186091 WETH | 0.000126 WETH | 0.000000 WETH | 0.000003 WETH | 0.000122 WETH (0.2667 €) | 0.000122 WETH | 6.57 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 420.852464 USDC | 0.288482 USDC | 0.000000 USDC | 0.007844 USDC | 0.280638 USDC (0.2582 €) | — | 6.67 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642035 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.177158 WETH | 0.000121 WETH | 0.000000 WETH | 0.000003 WETH | 0.000118 WETH (0.2575 €) | 0.000118 WETH | 6.66 | 0.164 (n=42) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 52642968 | WETH→[aerodrome_slipstream]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.021903 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1910 €) | 0.000087 WETH | 39.89 | 0.102 (n=3) | REJECTED | reliability_not_demonstrated |
| 52642968 | WETH→[pancakeswap_v3]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.021775 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1903 €) | 0.000087 WETH | 40.00 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |
| 52642968 | WETH→[uniswap_v3]→AERO→[aerodrome]→BRETT→[uniswap_v3]→WETH | 0.020798 WETH | 0.000082 WETH | 0.000000 WETH | 0.000003 WETH | 0.000079 WETH (0.1724 €) | 0.000079 WETH | 37.92 | 0.102 (n=3) | REJECTED | reliability_not_demonstrated |
| 52642035 | USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 307.929676 USDC | 0.182750 USDC | 0.000000 USDC | 0.007844 USDC | 0.174906 USDC (0.1609 €) | — | 5.68 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52642035 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→XSGD→[aerodrome_slipstream]→WETH | 0.129817 WETH | 0.000077 WETH | 0.000000 WETH | 0.000003 WETH | 0.000074 WETH (0.1606 €) | 0.000074 WETH | 5.67 | 0.346 (n=16) | REJECTED | reliability_not_demonstrated |
| 52641554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.516716 WETH | 0.000075 WETH | 0.000000 WETH | 0.000003 WETH | 0.000071 WETH (0.1533 €) | — | 1.38 | 0.104 (n=35) | REJECTED | below_safety_margin(71433138643533<103343199871391), p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,203.605774 USDC | 0.174400 USDC | 0.000000 USDC | 0.008097 USDC | 0.166303 USDC (0.1530 €) | — | 1.38 | 0.104 (n=35) | REJECTED | below_safety_margin(166303<240721), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.014139 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1524 €) | — | 1.46 | 0.104 (n=35) | REJECTED | below_safety_margin(207<282), p_lower_below_threshold(0.10<0.75) |
| 52642035 | USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 127.730473 USDC | 0.143476 USDC | 0.000000 USDC | 0.007844 USDC | 0.135632 USDC (0.1248 €) | — | 10.62 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52642035 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→EDGE→[aerodrome_slipstream]→cbBTC | 0.001450 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1246 €) | — | 11.52 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52641540 | cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005031 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1224 €) | — | 3.30 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→tBTC→[aerodrome_slipstream]→USDC | 413.140761 USDC | 0.140506 USDC | 0.000000 USDC | 0.007578 USDC | 0.132928 USDC (0.1223 €) | 0.132928 USDC | 3.22 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005161 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1180 €) | — | 3.10 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 421.139371 USDC | 0.135164 USDC | 0.000000 USDC | 0.007578 USDC | 0.127586 USDC (0.1174 €) | 0.127586 USDC | 3.03 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.005049 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1173 €) | — | 3.15 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52641540 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→tBTC→[aerodrome_slipstream]→USDC | 416.610436 USDC | 0.134859 USDC | 0.000000 USDC | 0.007938 USDC | 0.126921 USDC (0.1168 €) | 0.126921 USDC | 3.05 | 0.182 (n=38) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 52642035 | USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 144.097131 USDC | 0.131193 USDC | 0.000000 USDC | 0.007844 USDC | 0.123349 USDC (0.1135 €) | — | 8.56 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52642035 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WBTC→[uniswap_v3]→cbBTC | 0.001668 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1134 €) | — | 9.11 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 52641554 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.305120 WETH | 0.000056 WETH | 0.000000 WETH | 0.000003 WETH | 0.000053 WETH (0.1134 €) | — | 1.73 | 0.104 (n=35) | REJECTED | below_safety_margin(52823489579169<61024098255965), p_lower_below_threshold(0.10<0.75) |
| 52641554 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 710.150344 USDC | 0.131013 USDC | 0.000000 USDC | 0.008097 USDC | 0.122916 USDC (0.1131 €) | — | 1.73 | 0.104 (n=35) | REJECTED | below_safety_margin(122916<142030), p_lower_below_threshold(0.10<0.75) |
| 52641554 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.008247 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1127 €) | — | 1.86 | 0.104 (n=35) | REJECTED | below_safety_margin(153<164), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 328 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.143 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 14.3% < 75%
- Critères : ✅ chain_verified; ✅ tests_passed; ✅ contract_tested; ✅ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
