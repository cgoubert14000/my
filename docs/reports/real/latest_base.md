# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-06T03:06:13+00:00 ; durée 6.1 min ; blocs 53718130 → 53719956 (211 vus)

## Connexion
- Requêtes RPC : 3861 ; erreurs : 0 ; latence p50/p95 : 364.1/1,200.6 ms
- Rafraîchissements d'état : 211 ; âge des données au dernier bloc : 7.72 s ; changements de frais LP observés (pools à frais dynamiques) : 125
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 359 ; cycles déclenchés par événement : 121 ; avance médiane sur le rafraîchissement multicall : 344 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,237.24 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 488 pools, 283 jetons, 18176 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 104, aerodrome 201, pancakeswap_v3 31, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3755 (énumérés 304, par paires 0), mesurés 491, sous le plancher de 10000.0 $ : 3 → gardés 488 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2237.238829, 'cbBTC': 76116.143211, 'AERO': 0.590143}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 146,256,969 | 2,237.238847 | 53719979 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,545,612 | 0.029436 | 53719979 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,088,369 | 0.029375 | 53719979 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,879,898 | 0.000013 | 53719979 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,964,922 | 2,240.773588 | 53719979 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,429,284 | 106.038430 | 53719979 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,436,597 | 0.001553 | 53719979 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,038,941 | 1.691426 | 53719979 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,705,392 | 0.029437 | 53719979 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,115,178 | 2,241.445109 | 53719979 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,004,326 | 0.998657 | 53719979 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,317,124 | 42,571.256347 | 53719979 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,213,691 | 2,241.556269 | 53719979 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,562,101 | 0.029395 | 53719979 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,082,151 | 1,170,297.440977 | 53719979 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,886,419 | 0.007758 | 53719979 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,751,090 | 0.000013 | 53719979 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,646,240 | 0.000000 | 53719979 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,641,443 | 0.000013 | 53719979 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,637,558 | 0.016448 | 53719979 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,529,107 | 1.457700 | 53719979 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,522,924 | 440.463470 | 53719979 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,521,677 | 0.000013 | 53719979 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,000 | 0.816940 | 53719979 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,363,933 | 3,792.251679 | 53719979 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,325,421 | 2,237.675304 | 53719979 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,324,033 | 2,244.275857 | 53719979 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,267,536 | 14,976.665087 | 53719979 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,165,102 | 2,240.733753 | 53719979 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,791 | 76.942850 | 53719979 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,094,587 | 37,415,085.623295 | 53719979 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,055,589 | 106.090428 | 53719979 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,015,691 | 573,888.638322 | 53719979 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,004,391 | 0.000000 | 53719979 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 995,746 | 22,588,921.913143 | 53719979 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 971,432 | 20.630416 | 53719979 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 944,716 | 1,053.494207 | 53719979 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 938,553 | 71.181677 | 53719979 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 934,816 | 2,225.341209 | 53719979 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 330 | 926,123 | 0.000013 | 53719979 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 872,803 | 100,228.014147 | 53719979 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 851,745 | 0.047298 | 53719979 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 850,358 | 0.000541 | 53719979 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 791,693 | 21.187952 | 53719979 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/AERO | 10000 | 789,356 | 3,818.846272 | 53719979 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| pancakeswap_v3 | QUID/USDC | 100 | 785,186 | 0.055132 | 53719979 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 759,114 | 0.799699 | 53719979 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 714,810 | 0.570900 | 53719979 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 694,814 | 4,905,608.748298 | 53719979 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 683,357 | 0.000253 | 53719979 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/NPC | 3000 | 666,511 | 142,403.354527 | 53719979 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 653,693 | 0.536967 | 53719979 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 645,576 | 0.000008 | 53719979 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 619,937 | 569,465.689733 | 53719979 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 599,620 | 0.914740 | 53719979 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 597,219 | 2.477283 | 53719979 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,754 | 0.037457 | 53719979 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | cbBTC/EDGE | 7000 | 551,267 | 804,481.070181 | 53719979 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome_slipstream | WETH/MORPHO | 2727 | 529,375 | 1,053.035739 | 53719979 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 523,578 | 0.078524 | 53719979 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |

## Recherche d'opportunités
- Cycles : 331 ; routes examinées : 6016256 ; candidats optimisés : 19348 ; net attendu > 0 : 16 ; dernier cycle 106.5 ms
- Rejets (moteur) : {'spread_below_threshold': 5946786, 'liquidity_below_min': 49791, 'negative_expected_net': 19332, 'borrow_bound_too_small': 331}
- Enregistrements de la session : 19348 ; net attendu > 0 : 16 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 19348} ; motifs de rejet : {'below_safety_margin': 16, 'negative_expected_net': 19332, 'p_lower_below_threshold': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53719627 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.36 | 0.168 (n=1023) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.17<0.75) |
| 53719627 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.000824 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0021 €) | — | 0.36 | 0.168 (n=1023) | REJECTED | below_safety_margin(3<16), p_lower_below_threshold(0.17<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.030204 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.33 | 0.168 (n=1023) | REJECTED | below_safety_margin(998400457097<6040730406466), p_lower_below_threshold(0.17<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.030204 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0021 €) | — | 0.33 | 0.168 (n=1023) | REJECTED | below_safety_margin(998400457097<6040730406466), p_lower_below_threshold(0.17<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 73.774811 USDC | 0.008830 USDC | 0.000000 USDC | 0.006735 USDC | 0.002095 USDC (0.0019 €) | — | 0.28 | 0.168 (n=1023) | REJECTED | below_safety_margin(2095<14754), p_lower_below_threshold(0.17<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 73.774811 USDC | 0.008830 USDC | 0.000000 USDC | 0.006735 USDC | 0.002095 USDC (0.0019 €) | — | 0.28 | 0.168 (n=1023) | REJECTED | below_safety_margin(2095<14754), p_lower_below_threshold(0.17<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 42.144036 USDC | 0.008506 USDC | 0.000000 USDC | 0.006735 USDC | 0.001771 USDC (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(1771<8428), p_lower_below_threshold(0.24<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 42.144036 USDC | 0.008506 USDC | 0.000000 USDC | 0.006735 USDC | 0.001771 USDC (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(1771<8428), p_lower_below_threshold(0.24<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018871 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(786924803159<3774194771479), p_lower_below_threshold(0.24<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.018871 WETH | 0.000004 WETH | 0.000000 WETH | 0.000003 WETH | 0.000001 WETH (0.0016 €) | — | 0.42 | 0.237 (n=401) | REJECTED | below_safety_margin(786924803159<3774194771479), p_lower_below_threshold(0.24<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 99.256286 USDC | 0.006073 USDC | 0.000000 USDC | 0.005032 USDC | 0.001041 USDC (0.0010 €) | — | 0.10 | 0.054 (n=80) | REJECTED | below_safety_margin(1041<19851), p_lower_below_threshold(0.05<0.75) |
| 53719627 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 99.256286 USDC | 0.006073 USDC | 0.000000 USDC | 0.005032 USDC | 0.001041 USDC (0.0010 €) | — | 0.10 | 0.054 (n=80) | REJECTED | below_safety_margin(1041<19851), p_lower_below_threshold(0.05<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.045177 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0010 €) | — | 0.10 | 0.054 (n=80) | REJECTED | below_safety_margin(461864529887<9035394089864), p_lower_below_threshold(0.05<0.75) |
| 53719627 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.045177 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000000 WETH (0.0010 €) | — | 0.10 | 0.054 (n=80) | REJECTED | below_safety_margin(461864529887<9035394089864), p_lower_below_threshold(0.05<0.75) |
| 53719626 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 20.289487 USDC | 0.005758 USDC | 0.000000 USDC | 0.005031 USDC | 0.000727 USDC (0.0007 €) | — | 0.36 | 0.046 (n=234) | REJECTED | below_safety_margin(727<4057), p_lower_below_threshold(0.05<0.75) |
| 53719626 | USDC→[pancakeswap_v3]→ICNT→[uniswap_v3]→USDC | 20.289487 USDC | 0.005758 USDC | 0.000000 USDC | 0.005031 USDC | 0.000727 USDC (0.0007 €) | — | 0.36 | 0.046 (n=234) | REJECTED | below_safety_margin(727<4057), p_lower_below_threshold(0.05<0.75) |

## Fiabilité et décision
- Observations ghost : 5790 ; taux observé 0.159 ; borne inférieure crédible (0.9) 0.153 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
