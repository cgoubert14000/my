# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-01T10:21:44+00:00 ; durée 321.21 min ; blocs 53359939 → 53369575 (9564 vus)

## Connexion
- Requêtes RPC : 109501 ; erreurs : 30 ; latence p50/p95 : 65.6/1,211.6 ms
- Rafraîchissements d'état : 9565 ; âge des données au dernier bloc : 0.23 s ; changements de frais LP observés (pools à frais dynamiques) : 6563
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 5585 ; cycles déclenchés par événement : 1058 ; avance médiane sur le rafraîchissement multicall : 398 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,268.21 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 502 pools, 289 jetons, 18760 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 114, aerodrome 206, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 178 (rejetés 2) → 583 jetons ; pools candidats 3742 (énumérés 318, par paires 0), mesurés 505, sous le plancher de 10000.0 $ : 3 → gardés 502 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2265.714788, 'cbBTC': 77709.69565, 'AERO': 0.641921}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,952,396 | 2,268.209480 | 53369575 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,185,537 | 0.029083 | 53369575 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,287,089 | 0.000013 | 53369575 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,137,627 | 0.029145 | 53369575 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,925,145 | 96.875393 | 53369575 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,900,265 | 2,269.762291 | 53369575 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,703,960 | 0.001600 | 53369575 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,738,211 | 1.559384 | 53369575 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,197,333 | 0.029095 | 53369575 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,106,541 | 0.998845 | 53369575 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,071,683 | 2,270.510692 | 53369575 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,949,336 | 2,270.701590 | 53369575 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,573,568 | 37,704.158103 | 53369575 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,706,226 | 0.029128 | 53369575 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2703 | 2,428,323 | 96.848488 | 53369575 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 2,191,662 | 0.000013 | 53369575 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome | WETH/FAI | 10000 | 2,086,367 | 1,198,268.797307 | 53369575 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,764,588 | 0.000000 | 53369575 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,717,773 | 0.017413 | 53369575 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,658,191 | 0.000013 | 53369575 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,589,560 | 0.000013 | 53369575 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,560,556 | 423.428828 | 53369575 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,537,008 | 1.499750 | 53369575 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,583 | 2,271.435142 | 53369575 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,455 | 0.825724 | 53369575 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,462 | 3,539.985074 | 53369575 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,412,022 | 2,274.390397 | 53369575 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,349,933 | 2,269.748326 | 53369575 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,327,887 | 0.005168 | 53369575 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,314,496 | 14,565.076197 | 53369575 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 1,309,566 | 0.000013 | 53369575 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,169,993 | 70.986459 | 53369575 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,125,029 | 35,808,422.324409 | 53369575 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,080,903 | 508,515.918646 | 53369575 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,069,792 | 0.000000 | 53369575 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,032,264 | 21,665,741.665826 | 53369575 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,002,949 | 96.637911 | 53369575 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,870 | 19.175575 | 53369575 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | USDC/VVV | 3000 | 989,734 | 0.042670 | 53369575 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/EDEL | 7000 | 972,937 | 82,965.778196 | 53369575 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/WELL | 10000 | 962,769 | 1,160,450.959796 | 53369575 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| aerodrome | USDC/NOCK | 3000 | 962,701 | 67.547628 | 53369575 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/MORPHO | 3000 | 948,644 | 980.780398 | 53369575 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 926,928 | 2,252.785569 | 53369575 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/AERO | 10000 | 877,660 | 3,515.307244 | 53369575 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | uXRP/WETH | 3000 | 868,091 | 0.000550 | 53369575 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 841,883 | 19.303539 | 53369575 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 819,922 | 0.060463 | 53369575 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 768,580 | 0.801881 | 53369575 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 737,830 | 0.000261 | 53369575 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 725,373 | 0.596963 | 53369575 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 717,593 | 4,720,908.286092 | 53369575 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 695,243 | 0.000008 | 53369575 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 683,480 | 138,907.069172 | 53369575 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 2126 | 668,929 | 510,677.252364 | 53369575 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 664,729 | 0.555651 | 53369575 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 660,964 | 2.338945 | 53369575 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 613,549 | 0.093280 | 53369575 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | WETH/bsdETH | 100 | 608,727 | 0.916346 | 53369575 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 557,944 | 981.045243 | 53369575 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |

## Recherche d'opportunités
- Cycles : 10622 ; routes examinées : 199268720 ; candidats optimisés : 765134 ; net attendu > 0 : 231 ; dernier cycle 174.4 ms
- Rejets (moteur) : {'spread_below_threshold': 195961707, 'liquidity_below_min': 2487159, 'negative_expected_net': 764903, 'borrow_bound_too_small': 33334, 'unquotable': 21240, 'cycle_budget_exhausted': 77}
- Enregistrements de la session : 765134 ; net attendu > 0 : 231 ; simulés (eth_call de la vraie tx) : 17 (ok 17, échec 0) ; étiquettes ghost N+1 : 6/17 positives
- Décisions : {'REJECTED': 765134} ; motifs de rejet : {'below_safety_margin': 196, 'negative_expected_net': 764903, 'p_lower_below_threshold': 231, 'stale_data': 6}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53366636 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.057875 WETH | 0.000021 WETH | 0.000000 WETH | 0.000003 WETH | 0.000018 WETH (0.0378 €) | 0.000018 WETH | 3.13 | 0.120 (n=512) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53366636 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001451 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0373 €) | 0.000001 cbBTC | 3.58 | 0.120 (n=512) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53366636 | cbBTC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.001051 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0287 €) | — | 3.81 | 0.120 (n=512) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53366636 | WETH→[pancakeswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→WETH | 0.043082 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0283 €) | 0.000014 WETH | 3.14 | 0.120 (n=512) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53368675 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC | 0.000247 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0179 €) | — | 10.14 | 0.090 (n=32) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53368675 | USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 20.360714 USDC | 0.025858 USDC | 0.000000 USDC | 0.006503 USDC | 0.019355 USDC (0.0178 €) | 0.019355 USDC | 9.51 | 0.090 (n=32) | REJECTED | p_lower_below_threshold(0.09<0.75) |
| 53368675 | USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 20.360714 USDC | 0.024860 USDC | 0.000000 USDC | 0.006503 USDC | 0.018357 USDC (0.0169 €) | 0.018357 USDC | 9.02 | 0.041 (n=161) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53368675 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC | 0.000239 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0165 €) | — | 9.63 | 0.041 (n=161) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53368675 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC | 0.000239 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0143 €) | — | 8.38 | 0.041 (n=161) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53368675 | USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 20.360713 USDC | 0.021880 USDC | 0.000000 USDC | 0.006503 USDC | 0.015377 USDC (0.0141 €) | 0.015377 USDC | 7.55 | 0.118 (n=196) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53363674 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 56.845764 USDC | 0.021322 USDC | 0.000000 USDC | 0.006808 USDC | 0.014514 USDC (0.0134 €) | — | 2.55 | 0.140 (n=666) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53363674 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.025143 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0133 €) | 0.000006 WETH | 2.55 | 0.140 (n=666) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53368675 | USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC→[uniswap_v3]→USDC | 18.504893 USDC | 0.019277 USDC | 0.000000 USDC | 0.006503 USDC | 0.012774 USDC (0.0118 €) | — | 6.90 | 0.118 (n=196) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53368675 | cbBTC→[uniswap_v3]→USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC | 0.000239 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0115 €) | — | 6.70 | 0.118 (n=196) | REJECTED | p_lower_below_threshold(0.12<0.75) |
| 53363674 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 39.801828 USDC | 0.018440 USDC | 0.000000 USDC | 0.006808 USDC | 0.011632 USDC (0.0107 €) | — | 2.92 | 0.140 (n=666) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53363674 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.017613 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0107 €) | 0.000005 WETH | 2.91 | 0.140 (n=666) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53363674 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome]→USDC | 48.437776 USDC | 0.017879 USDC | 0.000000 USDC | 0.006495 USDC | 0.011384 USDC (0.0105 €) | — | 2.35 | 0.282 (n=84) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 53363674 | WETH→[aerodrome]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.021424 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0105 €) | 0.000005 WETH | 2.34 | 0.282 (n=84) | REJECTED | p_lower_below_threshold(0.28<0.75) |
| 53363674 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 53.955722 USDC | 0.018102 USDC | 0.000000 USDC | 0.006808 USDC | 0.011294 USDC (0.0104 €) | — | 2.09 | 0.140 (n=666) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53363674 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.023776 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0104 €) | — | 2.10 | 0.140 (n=666) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 53360865 | WETH→[uniswap_v3]→AAVE→[pancakeswap_v3]→WETH | 0.023511 WETH | 0.000007 WETH | 0.000000 WETH | 0.000002 WETH | 0.000004 WETH (0.0093 €) | — | 1.90 | 0.043 (n=154) | REJECTED | below_safety_margin(4456871587155<4702111714852), p_lower_below_threshold(0.04<0.75) |
| 53363674 | USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 50.810858 USDC | 0.016237 USDC | 0.000000 USDC | 0.006808 USDC | 0.009429 USDC (0.0087 €) | — | 1.86 | 0.140 (n=666) | REJECTED | below_safety_margin(9429<10162), p_lower_below_threshold(0.14<0.75) |
| 53363674 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→AERO→[pancakeswap_v3]→WETH | 0.022583 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000004 WETH (0.0087 €) | — | 1.84 | 0.140 (n=666) | REJECTED | below_safety_margin(4160603303667<4516682702925), p_lower_below_threshold(0.14<0.75) |
| 53368675 | USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 13.393484 USDC | 0.012741 USDC | 0.000000 USDC | 0.006503 USDC | 0.006238 USDC (0.0057 €) | — | 4.66 | 0.246 (n=103) | REJECTED | p_lower_below_threshold(0.25<0.75) |
| 53368675 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→FLOCK→[aerodrome]→cbBTC | 0.000147 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0050 €) | — | 4.77 | 0.246 (n=103) | REJECTED | p_lower_below_threshold(0.25<0.75) |

## Fiabilité et décision
- Observations ghost : 4055 ; taux observé 0.130 ; borne inférieure crédible (0.9) 0.123 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 12.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
