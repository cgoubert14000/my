# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T11:15:02+00:00 ; durée 159.64 min ; blocs 53818717 → 53866587 (9668 vus)

## Connexion
- Requêtes RPC : 128141 ; erreurs : 3 ; latence p50/p95 : 254.1/994.4 ms
- Rafraîchissements d'état : 9668 ; âge des données au dernier bloc : 6.28 s ; changements de frais LP observés (pools à frais dynamiques) : 4965
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 8206 ; cycles déclenchés par événement : 3894 ; avance médiane sur le rafraîchissement multicall : 322 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,237.78 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 281 jetons, 17914 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 103, aerodrome 201, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3751 (énumérés 303, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.035754, 'cbBTC': 75513.528915, 'AERO': 0.590274}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,312,718 | 2,237.779328 | 53866608 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,742,505 | 0.029403 | 53866608 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,404,022 | 0.000013 | 53866608 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,144,337 | 0.029418 | 53866608 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,005,628 | 2,232.314548 | 53866608 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,409,776 | 106.584384 | 53866608 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,440,866 | 0.001550 | 53866608 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,061,933 | 1.672706 | 53866608 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,739,542 | 0.029412 | 53866608 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,113,499 | 2,232.754522 | 53866608 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,011,820 | 0.998447 | 53866608 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,309,924 | 42,777.327955 | 53866608 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,207,829 | 2,232.837559 | 53866608 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,561,331 | 0.029434 | 53866608 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,082,372 | 1,170,614.944842 | 53866608 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,806,444 | 0.007370 | 53866608 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 460 | 1,741,199 | 0.000013 | 53866608 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,662,943 | 0.000013 | 53866608 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,647,325 | 0.016594 | 53866608 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,641,613 | 0.000000 | 53866608 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53866608 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,533,941 | 0.000013 | 53866608 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,529,936 | 434.349400 | 53866608 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,909 | 0.818149 | 53866608 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,373,970 | 3,741.939862 | 53866608 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,608 | 2,237.642170 | 53866608 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,323,869 | 2,238.094088 | 53866608 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,276,526 | 14,800.773276 | 53866608 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,174,717 | 2,232.372147 | 53866608 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,886 | 76.929838 | 53866608 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,095,368 | 37,365,983.089756 | 53866608 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,054,339 | 107.346492 | 53866608 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,023,768 | 561,148.793348 | 53866608 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,009,595 | 0.000000 | 53866608 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,007,274 | 22,433,261.257503 | 53866608 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 987,910 | 19.627993 | 53866608 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 936,562 | 2,225.328831 | 53866608 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 935,072 | 1,069.101330 | 53866608 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 338 | 927,358 | 0.000013 | 53866608 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 897,607 | 77.824038 | 53866608 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 865,199 | 102,046.934081 | 53866608 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 844,178 | 0.000533 | 53866608 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 813,884 | 0.047670 | 53866608 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 811,935 | 20.449238 | 53866608 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 795,402 | 0.056654 | 53866608 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 793,851 | 3,767.031016 | 53866608 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 759,158 | 0.799699 | 53866608 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,233 | 0.575901 | 53866608 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,266 | 4,915,959.224125 | 53866608 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 687,803 | 0.000256 | 53866608 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 661,707 | 144,566.194188 | 53866608 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 656,722 | 0.541700 | 53866608 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 650,448 | 0.000008 | 53866608 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2105 | 627,522 | 555,911.096141 | 53866608 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 599,954 | 0.914164 | 53866608 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 588,153 | 2.472301 | 53866608 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 562,066 | 0.038211 | 53866608 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 529,311 | 875,308.438588 | 53866608 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 528,622 | 0.079474 | 53866608 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 523,462 | 1,069.357246 | 53866608 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 13561 ; routes examinées : 242931754 ; candidats optimisés : 663761 ; net attendu > 0 : 98 ; dernier cycle 204.6 ms
- Rejets (moteur) : {'spread_below_threshold': 239020012, 'liquidity_below_min': 3234420, 'negative_expected_net': 663663, 'borrow_bound_too_small': 13561}
- Enregistrements de la session : 663761 ; net attendu > 0 : 98 ; simulés (eth_call de la vraie tx) : 16 (ok 6, échec 10) ; étiquettes ghost N+1 : 0/14 positives
- Décisions : {'REJECTED': 663761} ; motifs de rejet : {'below_safety_margin': 82, 'negative_expected_net': 663663, 'p_lower_below_threshold': 91, 'reliability_not_demonstrated': 7, 'simulation_failed': 10, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 384.664259 USDC | 0.052147 USDC | 0.000000 USDC | 0.005375 USDC | 0.046772 USDC (0.0430 €) | — | 1.22 | 0.054 (n=80) | REJECTED | below_safety_margin(46772<76932), p_lower_below_threshold(0.05<0.75) |
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 384.664259 USDC | 0.052147 USDC | 0.000000 USDC | 0.005375 USDC | 0.046772 USDC (0.0430 €) | — | 1.22 | 0.054 (n=80) | REJECTED | below_safety_margin(46772<76932), p_lower_below_threshold(0.05<0.75) |
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 343.755764 USDC | 0.045380 USDC | 0.000000 USDC | 0.005715 USDC | 0.039665 USDC (0.0365 €) | — | 1.15 | 0.054 (n=80) | REJECTED | below_safety_margin(39665<68751), p_lower_below_threshold(0.05<0.75) |
| 53848955 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 343.755764 USDC | 0.045380 USDC | 0.000000 USDC | 0.005715 USDC | 0.039665 USDC (0.0365 €) | — | 1.15 | 0.054 (n=80) | REJECTED | below_safety_margin(39665<68751), p_lower_below_threshold(0.05<0.75) |
| 53849808 | USDC→[aerodrome_slipstream]→CARV→[aerodrome_slipstream]→USDC | 27.854633 USDC | 0.033350 USDC | 0.000000 USDC | 0.005036 USDC | 0.028314 USDC (0.0260 €) | — | 10.16 | 0.000 (n=24) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53856814 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 50.437935 USDC | 0.031343 USDC | 0.000000 USDC | 0.005050 USDC | 0.026293 USDC (0.0242 €) | — | 5.21 | 0.027 (n=305) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53823058 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.007869 USDC | 0.030104 USDC | 0.000000 USDC | 0.005012 USDC | 0.025092 USDC (0.0231 €) | 0.025092 USDC | 5.12 | 0.028 (n=300) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53823641 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 47.715028 USDC | 0.028656 USDC | 0.000000 USDC | 0.005013 USDC | 0.023643 USDC (0.0218 €) | — | 4.96 | 0.028 (n=301) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 264.555975 USDC | 0.024400 USDC | 0.000000 USDC | 0.005038 USDC | 0.019362 USDC (0.0178 €) | — | 0.73 | 0.054 (n=80) | REJECTED | below_safety_margin(19362<52911), p_lower_below_threshold(0.05<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 264.555975 USDC | 0.024400 USDC | 0.000000 USDC | 0.005038 USDC | 0.019362 USDC (0.0178 €) | — | 0.73 | 0.054 (n=80) | REJECTED | below_safety_margin(19362<52911), p_lower_below_threshold(0.05<0.75) |
| 53844926 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 42.061624 USDC | 0.021572 USDC | 0.000000 USDC | 0.005032 USDC | 0.016540 USDC (0.0152 €) | — | 3.93 | 0.027 (n=303) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53845032 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.161073 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0151 €) | — | 0.45 | 0.046 (n=237) | REJECTED | below_safety_margin(7314038263273<32214619717753), p_lower_below_threshold(0.05<0.75) |
| 53845032 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.161073 WETH | 0.000010 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0151 €) | — | 0.45 | 0.046 (n=237) | REJECTED | below_safety_margin(7314038263273<32214619717753), p_lower_below_threshold(0.05<0.75) |
| 53845032 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 359.038236 USDC | 0.021383 USDC | 0.000000 USDC | 0.005033 USDC | 0.016350 USDC (0.0150 €) | — | 0.46 | 0.046 (n=237) | REJECTED | below_safety_margin(16350<71807), p_lower_below_threshold(0.05<0.75) |
| 53845032 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 359.038236 USDC | 0.021383 USDC | 0.000000 USDC | 0.005033 USDC | 0.016350 USDC (0.0150 €) | — | 0.46 | 0.046 (n=237) | REJECTED | below_safety_margin(16350<71807), p_lower_below_threshold(0.05<0.75) |
| 53859661 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 41.033317 USDC | 0.020692 USDC | 0.000000 USDC | 0.005051 USDC | 0.015641 USDC (0.0144 €) | — | 3.81 | 0.027 (n=307) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53859662 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 41.033317 USDC | 0.020692 USDC | 0.000000 USDC | 0.005051 USDC | 0.015641 USDC (0.0144 €) | — | 3.81 | 0.027 (n=307) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53846022 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 27.273646 USDC | 0.019331 USDC | 0.000000 USDC | 0.005034 USDC | 0.014297 USDC (0.0132 €) | 0.014297 USDC | 5.24 | 0.027 (n=304) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 223.293117 USDC | 0.018971 USDC | 0.000000 USDC | 0.005378 USDC | 0.013593 USDC (0.0125 €) | — | 0.61 | 0.054 (n=80) | REJECTED | below_safety_margin(13593<44658), p_lower_below_threshold(0.05<0.75) |
| 53838404 | USDC→[uniswap_v3]→EURC→[aerodrome_slipstream]→USDC | 223.293117 USDC | 0.018971 USDC | 0.000000 USDC | 0.005378 USDC | 0.013593 USDC (0.0125 €) | — | 0.61 | 0.054 (n=80) | REJECTED | below_safety_margin(13593<44658), p_lower_below_threshold(0.05<0.75) |
| 53859502 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 25.853974 USDC | 0.017378 USDC | 0.000000 USDC | 0.005051 USDC | 0.012327 USDC (0.0113 €) | 0.012327 USDC | 4.77 | 0.027 (n=306) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53840843 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 36.991359 USDC | 0.017072 USDC | 0.000000 USDC | 0.005034 USDC | 0.012038 USDC (0.0111 €) | — | 3.25 | 0.027 (n=302) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53847583 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.141967 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0103 €) | — | 0.35 | 0.046 (n=237) | REJECTED | below_safety_margin(5002093527211<28393329183727), p_lower_below_threshold(0.05<0.75) |
| 53847584 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.141967 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000005 WETH (0.0103 €) | — | 0.35 | 0.046 (n=237) | REJECTED | below_safety_margin(5002093527211<28393329183727), p_lower_below_threshold(0.05<0.75) |
| 53847583 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 317.426327 USDC | 0.016212 USDC | 0.000000 USDC | 0.005034 USDC | 0.011178 USDC (0.0103 €) | — | 0.35 | 0.046 (n=237) | REJECTED | below_safety_margin(11178<63485), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5815 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
