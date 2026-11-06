# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T21:12:46+00:00 ; durée 58.52 min ; blocs 54028370 → 54045907 (3464 vus)

## Connexion
- Requêtes RPC : 43131 ; erreurs : 0 ; latence p50/p95 : 189.7/1,485.7 ms
- Rafraîchissements d'état : 3464 ; âge des données au dernier bloc : 8.14 s ; changements de frais LP observés (pools à frais dynamiques) : 1403
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3425 ; cycles déclenchés par événement : 1481 ; avance médiane sur le rafraîchissement multicall : 374 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,228.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 482 pools, 282 jetons, 17936 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3742 (énumérés 299, par paires 0), mesurés 485, sous le plancher de 10000.0 $ : 3 → gardés 482 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2228.731074, 'cbBTC': 75812.648558, 'AERO': 0.606832}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,064,608 | 2,228.731440 | 54045928 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,700,176 | 0.029390 | 54045928 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,504,283 | 0.000013 | 54045928 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,132,286 | 0.029445 | 54045928 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,985,438 | 2,227.657233 | 54045928 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,396,196 | 106.112722 | 54045928 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,423,727 | 0.001553 | 54045928 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,903,294 | 1.641826 | 54045928 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,744,587 | 0.029397 | 54045928 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,157,769 | 2,228.433949 | 54045928 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,996,815 | 0.998508 | 54045928 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,297,018 | 42,764.959274 | 54045928 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,191,822 | 2,228.445944 | 54045928 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,551,740 | 0.029425 | 54045928 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,077,323 | 1,166,818.518415 | 54045928 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,735,624 | 0.000013 | 54045928 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,730,802 | 0.006970 | 54045928 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,655,300 | 0.000013 | 54045928 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,654,780 | 0.000000 | 54045928 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,615,457 | 0.016121 | 54045928 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,561,643 | 0.000013 | 54045928 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54045928 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,532,050 | 426.604059 | 54045928 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,358 | 0.818979 | 54045928 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,389,006 | 3,655.283017 | 54045928 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,322,992 | 2,227.000524 | 54045928 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,321,111 | 2,233.861175 | 54045928 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,281,603 | 14,501.064137 | 54045928 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,165,079 | 2,227.542716 | 54045928 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,124,001 | 76.914118 | 54045928 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,094,098 | 37,082,489.982229 | 54045928 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,051,837 | 106.868792 | 54045928 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,023,707 | 554,471.546907 | 54045928 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,017,811 | 0.000000 | 54045928 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 996,965 | 22,508,235.864785 | 54045928 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 977,153 | 20.271934 | 54045928 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 941,532 | 1,054.875353 | 54045928 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 934,351 | 2,225.576719 | 54045928 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 925,012 | 0.000013 | 54045928 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 918,493 | 74.277404 | 54045928 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 881,989 | 97,406.400176 | 54045928 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 836,041 | 0.000527 | 54045928 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 814,109 | 0.047646 | 54045928 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 807,985 | 20.600439 | 54045928 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 799,643 | 3,683.102223 | 54045928 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 794,978 | 0.056590 | 54045928 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 756,089 | 0.799699 | 54045928 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 724,651 | 0.571485 | 54045928 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,296 | 4,876,170.485073 | 54045928 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 688,117 | 0.000258 | 54045928 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 664,415 | 0.553732 | 54045928 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 661,505 | 143,483.016798 | 54045928 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 657,502 | 0.000008 | 54045928 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 628,944 | 554,301.166334 | 54045928 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 586,743 | 0.040769 | 54045928 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | WETH/msETH (stable) | 500 | 585,930 | 2.471342 | 54045928 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | cbBTC/EDGE | 7000 | 528,037 | 870,487.161127 | 54045928 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 527,422 | 1,054.916322 | 54045928 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 524,505 | 0.078547 | 54045928 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 518,019 | 2,228.569844 | 54045928 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 4944 ; routes examinées : 88675584 ; candidats optimisés : 259185 ; net attendu > 0 : 20 ; dernier cycle 76.2 ms
- Rejets (moteur) : {'spread_below_threshold': 87144684, 'liquidity_below_min': 1266540, 'negative_expected_net': 259165, 'borrow_bound_too_small': 4943, 'cycle_budget_exhausted': 232}
- Enregistrements de la session : 259185 ; net attendu > 0 : 20 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 259185} ; motifs de rejet : {'below_safety_margin': 20, 'negative_expected_net': 259165, 'p_lower_below_threshold': 20}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54042831 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.102166 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(2470642400570<20433118273996), p_lower_below_threshold(0.05<0.75) |
| 54042832 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.102166 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(2470642400570<20433118273996), p_lower_below_threshold(0.05<0.75) |
| 54042831 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 226.836687 USDC | 0.010504 USDC | 0.000000 USDC | 0.005007 USDC | 0.005497 USDC (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(5497<45367), p_lower_below_threshold(0.05<0.75) |
| 54042832 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 226.836687 USDC | 0.010504 USDC | 0.000000 USDC | 0.005007 USDC | 0.005497 USDC (0.0051 €) | — | 0.24 | 0.047 (n=247) | REJECTED | below_safety_margin(5497<45367), p_lower_below_threshold(0.05<0.75) |
| 54029815 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 28.179939 USDC | 0.009524 USDC | 0.000000 USDC | 0.005016 USDC | 0.004508 USDC (0.0041 €) | — | 1.60 | 0.047 (n=247) | REJECTED | below_safety_margin(4508<5635), p_lower_below_threshold(0.05<0.75) |
| 54029969 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.735224 USDC | 0.009268 USDC | 0.000000 USDC | 0.005016 USDC | 0.004252 USDC (0.0039 €) | — | 1.53 | 0.047 (n=247) | REJECTED | below_safety_margin(4252<5547), p_lower_below_threshold(0.05<0.75) |
| 54029971 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.735224 USDC | 0.009268 USDC | 0.000000 USDC | 0.005016 USDC | 0.004252 USDC (0.0039 €) | — | 1.53 | 0.047 (n=247) | REJECTED | below_safety_margin(4252<5547), p_lower_below_threshold(0.05<0.75) |
| 54029970 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 27.735224 USDC | 0.009268 USDC | 0.000000 USDC | 0.005016 USDC | 0.004252 USDC (0.0039 €) | — | 1.53 | 0.047 (n=247) | REJECTED | below_safety_margin(4252<5547), p_lower_below_threshold(0.05<0.75) |
| 54029756 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.252967 USDC | 0.006188 USDC | 0.000000 USDC | 0.005016 USDC | 0.001172 USDC (0.0011 €) | — | 0.77 | 0.047 (n=247) | REJECTED | below_safety_margin(1172<3050), p_lower_below_threshold(0.05<0.75) |
| 54029756 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 15.252967 USDC | 0.006188 USDC | 0.000000 USDC | 0.005016 USDC | 0.001172 USDC (0.0011 €) | — | 0.77 | 0.047 (n=247) | REJECTED | below_safety_margin(1172<3050), p_lower_below_threshold(0.05<0.75) |
| 54029815 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 22.335596 USDC | 0.006084 USDC | 0.000000 USDC | 0.005016 USDC | 0.001068 USDC (0.0010 €) | — | 0.48 | 0.047 (n=247) | REJECTED | below_safety_margin(1068<4467), p_lower_below_threshold(0.05<0.75) |
| 54029815 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 22.335596 USDC | 0.006084 USDC | 0.000000 USDC | 0.005016 USDC | 0.001068 USDC (0.0010 €) | — | 0.48 | 0.047 (n=247) | REJECTED | below_safety_margin(1068<4467), p_lower_below_threshold(0.05<0.75) |
| 54035747 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 202.958491 USDC | 0.005874 USDC | 0.000000 USDC | 0.005017 USDC | 0.000857 USDC (0.0008 €) | — | 0.04 | 0.047 (n=247) | REJECTED | below_safety_margin(857<40591), p_lower_below_threshold(0.05<0.75) |
| 54035747 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 202.958491 USDC | 0.005874 USDC | 0.000000 USDC | 0.005017 USDC | 0.000857 USDC (0.0008 €) | — | 0.04 | 0.047 (n=247) | REJECTED | below_safety_margin(857<40591), p_lower_below_threshold(0.05<0.75) |
| 54035747 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002410 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.04 | 0.047 (n=247) | REJECTED | below_safety_margin(1<48), p_lower_below_threshold(0.05<0.75) |
| 54035747 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002410 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0007 €) | — | 0.04 | 0.047 (n=247) | REJECTED | below_safety_margin(1<48), p_lower_below_threshold(0.05<0.75) |
| 54042831 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.015833 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0004 €) | — | 0.11 | 0.047 (n=247) | REJECTED | below_safety_margin(177229853402<3166533105696), p_lower_below_threshold(0.05<0.75) |
| 54042832 | WETH→[sushiswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.015833 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0004 €) | — | 0.11 | 0.047 (n=247) | REJECTED | below_safety_margin(177229853402<3166533105696), p_lower_below_threshold(0.05<0.75) |
| 54042831 | USDC→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 34.999222 USDC | 0.005735 USDC | 0.000000 USDC | 0.005345 USDC | 0.000390 USDC (0.0004 €) | — | 0.11 | 0.047 (n=247) | REJECTED | below_safety_margin(390<6999), p_lower_below_threshold(0.05<0.75) |
| 54042832 | USDC→[pancakeswap_v3]→WETH→[sushiswap_v3]→USDC | 34.999222 USDC | 0.005735 USDC | 0.000000 USDC | 0.005345 USDC | 0.000390 USDC (0.0004 €) | — | 0.11 | 0.047 (n=247) | REJECTED | below_safety_margin(390<6999), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5897 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
