# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T15:00:06+00:00 ; durée 49.01 min ; blocs 53919422 → 53934101 (1847 vus)

## Connexion
- Requêtes RPC : 28583 ; erreurs : 0 ; latence p50/p95 : 385.3/1,876.1 ms
- Rafraîchissements d'état : 1847 ; âge des données au dernier bloc : 9.96 s ; changements de frais LP observés (pools à frais dynamiques) : 2793
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1011 ; cycles déclenchés par événement : 405 ; avance médiane sur le rafraîchissement multicall : 707 ms
- Gaz : base fee 0.005004 gwei ; prix ETH (pool le plus profond) : 2,226.42 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 484 pools, 280 jetons, 17898 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 103, aerodrome 200, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3743 (énumérés 302, par paires 0), mesurés 487, sous le plancher de 10000.0 $ : 3 → gardés 484 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2229.592504, 'cbBTC': 75521.601442, 'AERO': 0.600396}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,534,299 | 2,226.416079 | 53934143 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,664,513 | 0.029508 | 53934143 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,334,478 | 0.000013 | 53934143 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,107,359 | 0.029461 | 53934143 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,966,460 | 2,226.797266 | 53934143 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,366,665 | 106.743150 | 53934143 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,439,159 | 0.001577 | 53934143 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,888,559 | 1.652238 | 53934143 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,709,644 | 0.029506 | 53934143 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,141,902 | 2,226.754730 | 53934143 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,976,905 | 0.998492 | 53934143 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,288,044 | 42,909.400608 | 53934143 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,192,620 | 2,226.498189 | 53934143 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,545,610 | 0.029479 | 53934143 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,071,797 | 1,170,614.944842 | 53934143 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,782,612 | 0.007292 | 53934143 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,730,663 | 0.000013 | 53934143 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,652,519 | 0.000013 | 53934143 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,641,372 | 0.016511 | 53934143 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,636,871 | 0.000000 | 53934143 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,161 | 1.444757 | 53934143 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,531,939 | 425.067336 | 53934143 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,525,292 | 0.000013 | 53934143 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,462,125 | 0.818407 | 53934143 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,381,935 | 3,675.990984 | 53934143 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,322,262 | 2,227.008858 | 53934143 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,320,424 | 2,227.027601 | 53934143 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,279,007 | 14,412.562584 | 53934143 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,167,696 | 2,226.775273 | 53934143 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,886 | 76.929838 | 53934143 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,091,559 | 37,125,668.529751 | 53934143 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,047,821 | 106.699255 | 53934143 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,022,416 | 555,053.604109 | 53934143 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,021,330 | 0.000000 | 53934143 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,805 | 22,407,018.411307 | 53934143 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 984,295 | 19.834806 | 53934143 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 935,302 | 1,063.197242 | 53934143 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 933,955 | 2,225.576719 | 53934143 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 920,738 | 0.000013 | 53934143 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 902,050 | 77.009844 | 53934143 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 862,389 | 101,672.565562 | 53934143 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | uXRP/WETH | 3000 | 836,723 | 0.000529 | 53934143 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 820,638 | 20.131730 | 53934143 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | USDC/VVV | 3000 | 809,689 | 0.048046 | 53934143 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 796,719 | 3,681.640183 | 53934143 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,150 | 0.055870 | 53934143 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 755,303 | 0.799699 | 53934143 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,308 | 0.579916 | 53934143 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 692,569 | 4,890,085.794790 | 53934143 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 688,377 | 0.000259 | 53934143 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 665,516 | 141,478.075784 | 53934143 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 653,549 | 0.536704 | 53934143 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 653,224 | 0.000008 | 53934143 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 627,930 | 551,037.281197 | 53934143 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 596,962 | 0.913997 | 53934143 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 585,167 | 2.472301 | 53934143 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 562,467 | 0.038251 | 53934143 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 530,326 | 862,862.494762 | 53934143 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| pancakeswap_v3 | ELSA/USDC | 100 | 527,111 | 0.079055 | 53934143 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 523,398 | 1,063.442154 | 53934143 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 2251 ; routes examinées : 40288398 ; candidats optimisés : 157746 ; net attendu > 0 : 199 ; dernier cycle 270.0 ms
- Rejets (moteur) : {'spread_below_threshold': 39584842, 'liquidity_below_min': 543202, 'negative_expected_net': 157547, 'borrow_bound_too_small': 2250, 'cycle_budget_exhausted': 358}
- Enregistrements de la session : 157746 ; net attendu > 0 : 199 ; simulés (eth_call de la vraie tx) : 10 (ok 10, échec 0) ; étiquettes ghost N+1 : 0/10 positives
- Décisions : {'REJECTED': 157746} ; motifs de rejet : {'below_safety_margin': 158, 'negative_expected_net': 157547, 'p_lower_below_threshold': 198, 'reliability_not_demonstrated': 1, 'stale_data': 45}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53927859 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.061437 WETH | 0.000039 WETH | 0.000000 WETH | 0.000004 WETH | 0.000035 WETH (0.0722 €) | 0.000035 WETH | 5.72 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 137.479491 USDC | 0.086928 USDC | 0.000000 USDC | 0.008505 USDC | 0.078423 USDC (0.0721 €) | — | 5.70 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.059145 WETH | 0.000039 WETH | 0.000000 WETH | 0.000004 WETH | 0.000035 WETH (0.0713 €) | 0.000035 WETH | 5.87 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 131.536756 USDC | 0.085978 USDC | 0.000000 USDC | 0.008505 USDC | 0.077473 USDC (0.0713 €) | — | 5.89 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.057789 WETH | 0.000036 WETH | 0.000000 WETH | 0.000003 WETH | 0.000032 WETH (0.0662 €) | 0.000032 WETH | 5.57 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 128.416148 USDC | 0.079646 USDC | 0.000000 USDC | 0.007727 USDC | 0.071919 USDC (0.0662 €) | — | 5.60 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.055677 WETH | 0.000035 WETH | 0.000000 WETH | 0.000004 WETH | 0.000032 WETH (0.0653 €) | — | 5.71 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 124.158088 USDC | 0.079082 USDC | 0.000000 USDC | 0.008116 USDC | 0.070966 USDC (0.0653 €) | — | 5.72 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 56.162098 USDC | 0.031542 USDC | 0.000000 USDC | 0.008505 USDC | 0.023037 USDC (0.0212 €) | — | 4.10 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.025081 WETH | 0.000014 WETH | 0.000000 WETH | 0.000004 WETH | 0.000010 WETH (0.0212 €) | — | 4.11 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.034858 WETH | 0.000014 WETH | 0.000000 WETH | 0.000004 WETH | 0.000010 WETH (0.0206 €) | — | 2.87 | 0.169 (n=1026) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53927859 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC | 78.067480 USDC | 0.030451 USDC | 0.000000 USDC | 0.008116 USDC | 0.022335 USDC (0.0205 €) | — | 2.86 | 0.169 (n=1026) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53927859 | WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.035592 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0201 €) | — | 2.75 | 0.169 (n=1026) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53927859 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→EURC→[uniswap_v3]→USDC | 79.177696 USDC | 0.029607 USDC | 0.000000 USDC | 0.007727 USDC | 0.021880 USDC (0.0201 €) | — | 2.76 | 0.169 (n=1026) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 53928347 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 147.185239 USDC | 0.029520 USDC | 0.000000 USDC | 0.007739 USDC | 0.021781 USDC (0.0200 €) | — | 1.48 | 0.236 (n=403) | REJECTED | below_safety_margin(21781<29437), p_lower_below_threshold(0.24<0.75) |
| 53928347 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.065882 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0200 €) | — | 1.47 | 0.236 (n=403) | REJECTED | below_safety_margin(9711808110655<13176493933192), p_lower_below_threshold(0.24<0.75) |
| 53927859 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC | 53.804214 USDC | 0.029339 USDC | 0.000000 USDC | 0.008116 USDC | 0.021223 USDC (0.0195 €) | — | 3.94 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53927859 | WETH→[pancakeswap_v3]→EURC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.024108 WETH | 0.000013 WETH | 0.000000 WETH | 0.000004 WETH | 0.000009 WETH (0.0195 €) | — | 3.94 | 0.151 (n=781) | REJECTED | p_lower_below_threshold(0.15<0.75) |
| 53928348 | USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 52.669734 USDC | 0.026646 USDC | 0.000000 USDC | 0.007753 USDC | 0.018893 USDC (0.0174 €) | — | 3.59 | 0.268 (n=362) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53928348 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→WETH | 0.023506 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0173 €) | 0.000008 WETH | 3.58 | 0.268 (n=362) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53928348 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 45.221209 USDC | 0.024466 USDC | 0.000000 USDC | 0.007753 USDC | 0.016713 USDC (0.0154 €) | — | 3.70 | 0.268 (n=362) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53928348 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.020324 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0153 €) | 0.000007 WETH | 3.66 | 0.268 (n=362) | REJECTED | p_lower_below_threshold(0.27<0.75) |
| 53928348 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 61.085979 USDC | 0.023848 USDC | 0.000000 USDC | 0.007753 USDC | 0.016095 USDC (0.0148 €) | — | 2.63 | 0.236 (n=403) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 53928348 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.027368 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0148 €) | 0.000007 WETH | 2.62 | 0.236 (n=403) | REJECTED | p_lower_below_threshold(0.24<0.75) |
| 53928348 | USDC→[uniswap_v3]→USDT→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 49.154550 USDC | 0.023447 USDC | 0.000000 USDC | 0.007753 USDC | 0.015694 USDC (0.0144 €) | — | 3.19 | 0.268 (n=362) | REJECTED | p_lower_below_threshold(0.27<0.75) |

## Fiabilité et décision
- Observations ghost : 5856 ; taux observé 0.158 ; borne inférieure crédible (0.9) 0.152 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
