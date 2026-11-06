# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T09:27:17+00:00 ; durée 51.89 min ; blocs 53818717 → 53834274 (2254 vus)

## Connexion
- Requêtes RPC : 36470 ; erreurs : 0 ; latence p50/p95 : 281.5/1,133.7 ms
- Rafraîchissements d'état : 2254 ; âge des données au dernier bloc : 6.89 s ; changements de frais LP observés (pools à frais dynamiques) : 1778
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1804 ; cycles déclenchés par événement : 853 ; avance médiane sur le rafraîchissement multicall : 556 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,237.35 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 281 jetons, 17914 routes
- Par DEX : uniswap_v3 136, aerodrome_slipstream 103, aerodrome 201, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3751 (énumérés 303, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2226.035754, 'cbBTC': 75513.528915, 'AERO': 0.590274}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,146,883 | 2,237.352374 | 53834294 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,649,923 | 0.029447 | 53834294 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,383,179 | 0.000013 | 53834294 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,136,305 | 0.029418 | 53834294 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,003,179 | 2,242.272601 | 53834294 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,393,817 | 107.050297 | 53834294 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,430,923 | 0.001551 | 53834294 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,051,951 | 1.679486 | 53834294 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,707,004 | 0.029441 | 53834294 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,123,404 | 2,242.964481 | 53834294 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,005,132 | 0.998447 | 53834294 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,307,736 | 42,817.581001 | 53834294 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,207,359 | 2,243.018682 | 53834294 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,559,561 | 0.029434 | 53834294 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,080,583 | 1,172,181.068675 | 53834294 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,799,310 | 0.007311 | 53834294 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,739,112 | 0.000013 | 53834294 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,660,762 | 0.000013 | 53834294 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,645,130 | 0.016561 | 53834294 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,641,300 | 0.000000 | 53834294 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53834294 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,532,294 | 0.000013 | 53834294 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,523,170 | 440.489008 | 53834294 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,908 | 0.818149 | 53834294 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,370,368 | 3,764.439708 | 53834294 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,481 | 2,236.814305 | 53834294 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,323,994 | 2,237.180190 | 53834294 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,267,505 | 14,965.063188 | 53834294 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,172,473 | 2,242.227379 | 53834294 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,888 | 76.929483 | 53834294 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,095,101 | 37,372,003.705492 | 53834294 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,047,484 | 107.682096 | 53834294 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,022,094 | 563,513.421758 | 53834294 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,009,536 | 0.000000 | 53834294 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,001,277 | 22,582,648.446445 | 53834294 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 983,702 | 19.874996 | 53834294 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/USDC | 10000 | 936,482 | 2,225.328831 | 53834294 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 934,876 | 1,069.784010 | 53834294 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 926,318 | 73.074456 | 53834294 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 926,031 | 0.000013 | 53834294 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 862,619 | 102,619.127140 | 53834294 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 842,548 | 0.000532 | 53834294 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 811,862 | 20.451592 | 53834294 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 811,385 | 0.047751 | 53834294 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 792,174 | 3,784.714091 | 53834294 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 784,418 | 0.055023 | 53834294 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 759,013 | 0.799699 | 53834294 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 720,612 | 0.574382 | 53834294 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 693,203 | 4,929,151.147177 | 53834294 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 686,210 | 0.000255 | 53834294 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 660,080 | 145,221.436395 | 53834294 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 655,345 | 0.539549 | 53834294 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 648,379 | 0.000008 | 53834294 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 626,014 | 559,781.447745 | 53834294 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 599,820 | 0.914223 | 53834294 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 599,720 | 2.462288 | 53834294 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 560,925 | 0.038093 | 53834294 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 529,093 | 0.079604 | 53834294 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 526,049 | 885,216.830299 | 53834294 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 526,028 | 2,242.901892 | 53834294 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |

## Recherche d'opportunités
- Cycles : 3106 ; routes examinées : 55640884 ; candidats optimisés : 177813 ; net attendu > 0 : 25 ; dernier cycle 223.0 ms
- Rejets (moteur) : {'spread_below_threshold': 54786386, 'liquidity_below_min': 673579, 'negative_expected_net': 177788, 'borrow_bound_too_small': 3106}
- Enregistrements de la session : 177813 ; net attendu > 0 : 25 ; simulés (eth_call de la vraie tx) : 3 (ok 2, échec 1) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 177813} ; motifs de rejet : {'below_safety_margin': 22, 'negative_expected_net': 177788, 'p_lower_below_threshold': 25, 'simulation_failed': 1, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53823058 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 49.007869 USDC | 0.030104 USDC | 0.000000 USDC | 0.005012 USDC | 0.025092 USDC (0.0231 €) | 0.025092 USDC | 5.12 | 0.028 (n=300) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53823641 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 47.715028 USDC | 0.028656 USDC | 0.000000 USDC | 0.005013 USDC | 0.023643 USDC (0.0218 €) | — | 4.96 | 0.028 (n=301) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53831928 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 32.441807 USDC | 0.012869 USDC | 0.000000 USDC | 0.005039 USDC | 0.007830 USDC (0.0072 €) | 0.007830 USDC | 2.41 | 0.046 (n=234) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 53831480 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.603942 USDC | 0.010814 USDC | 0.000000 USDC | 0.005038 USDC | 0.005776 USDC (0.0053 €) | — | 1.95 | 0.046 (n=234) | REJECTED | below_safety_margin(5776<5920), p_lower_below_threshold(0.05<0.75) |
| 53831481 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.603942 USDC | 0.010814 USDC | 0.000000 USDC | 0.005038 USDC | 0.005776 USDC (0.0053 €) | — | 1.95 | 0.046 (n=234) | REJECTED | below_safety_margin(5776<5920), p_lower_below_threshold(0.05<0.75) |
| 53832143 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.379544 USDC | 0.010641 USDC | 0.000000 USDC | 0.005039 USDC | 0.005602 USDC (0.0052 €) | — | 1.91 | 0.046 (n=235) | REJECTED | below_safety_margin(5602<5875), p_lower_below_threshold(0.05<0.75) |
| 53832143 | USDC→[uniswap_v3]→ICNT→[pancakeswap_v3]→USDC | 29.379544 USDC | 0.010641 USDC | 0.000000 USDC | 0.005039 USDC | 0.005602 USDC (0.0052 €) | — | 1.91 | 0.046 (n=235) | REJECTED | below_safety_margin(5602<5875), p_lower_below_threshold(0.05<0.75) |
| 53822585 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.473769 USDC | 0.009535 USDC | 0.000000 USDC | 0.005012 USDC | 0.004523 USDC (0.0042 €) | — | 1.65 | 0.046 (n=234) | REJECTED | below_safety_margin(4523<5494), p_lower_below_threshold(0.05<0.75) |
| 53822586 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 27.473769 USDC | 0.009535 USDC | 0.000000 USDC | 0.005012 USDC | 0.004523 USDC (0.0042 €) | — | 1.65 | 0.046 (n=234) | REJECTED | below_safety_margin(4523<5494), p_lower_below_threshold(0.05<0.75) |
| 53831696 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 234.516533 USDC | 0.009403 USDC | 0.000000 USDC | 0.005040 USDC | 0.004363 USDC (0.0040 €) | — | 0.19 | 0.046 (n=234) | REJECTED | below_safety_margin(4363<46903), p_lower_below_threshold(0.05<0.75) |
| 53831696 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 234.516533 USDC | 0.009403 USDC | 0.000000 USDC | 0.005040 USDC | 0.004363 USDC (0.0040 €) | — | 0.19 | 0.046 (n=234) | REJECTED | below_safety_margin(4363<46903), p_lower_below_threshold(0.05<0.75) |
| 53831696 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.104185 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0040 €) | — | 0.19 | 0.046 (n=234) | REJECTED | below_safety_margin(1939454297856<20837019113688), p_lower_below_threshold(0.05<0.75) |
| 53831696 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.104185 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0040 €) | — | 0.19 | 0.046 (n=234) | REJECTED | below_safety_margin(1939454297856<20837019113688), p_lower_below_threshold(0.05<0.75) |
| 53828342 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 209.478301 USDC | 0.009147 USDC | 0.000000 USDC | 0.005030 USDC | 0.004117 USDC (0.0038 €) | — | 0.20 | 0.046 (n=234) | REJECTED | below_safety_margin(4117<41895), p_lower_below_threshold(0.05<0.75) |
| 53828342 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.094008 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0038 €) | — | 0.20 | 0.046 (n=234) | REJECTED | below_safety_margin(1835791606212<18801667074057), p_lower_below_threshold(0.05<0.75) |
| 53828894 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 30.937696 USDC | 0.005573 USDC | 0.000000 USDC | 0.005026 USDC | 0.000547 USDC (0.0005 €) | — | 0.18 | 0.054 (n=80) | REJECTED | below_safety_margin(547<6187), p_lower_below_threshold(0.05<0.75) |
| 53828894 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.013950 WETH | 0.000002 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0005 €) | — | 0.17 | 0.054 (n=80) | REJECTED | below_safety_margin(239182194707<2790097583785), p_lower_below_threshold(0.05<0.75) |
| 53830798 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 38.113931 USDC | 0.006997 USDC | 0.000000 USDC | 0.006734 USDC | 0.000263 USDC (0.0002 €) | — | 0.07 | 0.169 (n=1024) | REJECTED | below_safety_margin(263<7622), p_lower_below_threshold(0.17<0.75) |
| 53830798 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 38.113931 USDC | 0.006997 USDC | 0.000000 USDC | 0.006734 USDC | 0.000263 USDC (0.0002 €) | — | 0.07 | 0.169 (n=1024) | REJECTED | below_safety_margin(263<7622), stale_data(4665ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53830798 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.016916 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.06 | 0.169 (n=1024) | REJECTED | below_safety_margin(108406798609<3383266920409), p_lower_below_threshold(0.17<0.75) |
| 53830798 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.016916 WETH | 0.000003 WETH | 0.000000 WETH | 0.000003 WETH | 0.000000 WETH (0.0002 €) | — | 0.06 | 0.169 (n=1024) | REJECTED | below_safety_margin(108406798609<3383266920409), stale_data(4662ms>4000.0), p_lower_below_threshold(0.17<0.75) |
| 53832886 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.083976 USDC | 0.005257 USDC | 0.000000 USDC | 0.005038 USDC | 0.000219 USDC (0.0002 €) | — | 0.16 | 0.046 (n=235) | REJECTED | below_safety_margin(219<2816), p_lower_below_threshold(0.05<0.75) |
| 53832886 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.083976 USDC | 0.005257 USDC | 0.000000 USDC | 0.005038 USDC | 0.000219 USDC (0.0002 €) | — | 0.16 | 0.046 (n=235) | REJECTED | below_safety_margin(219<2816), p_lower_below_threshold(0.05<0.75) |
| 53832888 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.083976 USDC | 0.005257 USDC | 0.000000 USDC | 0.005038 USDC | 0.000219 USDC (0.0002 €) | — | 0.16 | 0.046 (n=235) | REJECTED | below_safety_margin(219<2816), p_lower_below_threshold(0.05<0.75) |
| 53832889 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 14.083976 USDC | 0.005257 USDC | 0.000000 USDC | 0.005038 USDC | 0.000219 USDC (0.0002 €) | — | 0.16 | 0.046 (n=235) | REJECTED | below_safety_margin(219<2816), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5804 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
