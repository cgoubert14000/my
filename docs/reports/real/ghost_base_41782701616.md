# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T07:48:26+00:00 ; durée 101.35 min ; blocs 53491535 → 53494579 (3027 vus)

## Connexion
- Requêtes RPC : 34257 ; erreurs : 0 ; latence p50/p95 : 254.7/1,224.3 ms
- Rafraîchissements d'état : 3028 ; âge des données au dernier bloc : 0.82 s ; changements de frais LP observés (pools à frais dynamiques) : 4807
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1342 ; cycles déclenchés par événement : 180 ; avance médiane sur le rafraîchissement multicall : 611 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,303.55 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 284 jetons, 19492 routes
- Par DEX : uniswap_v3 141, aerodrome_slipstream 106, aerodrome 204, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 173 (rejetés 2) → 578 jetons ; pools candidats 3704 (énumérés 307, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2296.568203, 'cbBTC': 77781.37292, 'AERO': 0.62987}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,734,542 | 2,303.546859 | 53494579 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,864,497 | 0.029523 | 53494579 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,278,337 | 0.029470 | 53494579 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,157,000 | 0.000013 | 53494579 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,092,683 | 2,306.266305 | 53494579 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 8,080,373 | 95.140526 | 53494579 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,622,933 | 0.001560 | 53494579 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,375,765 | 1.578746 | 53494579 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,837,959 | 0.029519 | 53494579 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,210,907 | 2,306.375759 | 53494579 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,104,992 | 0.999894 | 53494579 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 862 | 3,890,666 | 2,306.713348 | 53494579 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,463,150 | 41,406.355850 | 53494579 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,702,215 | 0.029478 | 53494579 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2712 | 2,211,459 | 95.171921 | 53494579 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,167,325 | 1,145,289.514427 | 53494579 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 520 | 1,820,992 | 0.000013 | 53494579 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,730,107 | 0.017677 | 53494579 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,687,985 | 0.000000 | 53494579 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,685,700 | 0.006732 | 53494579 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,625,530 | 0.000013 | 53494579 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,575,872 | 432.423990 | 53494579 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,822 | 1.432992 | 53494579 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,552,634 | 0.000013 | 53494579 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,455,444 | 0.817942 | 53494579 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,435,573 | 3,632.610744 | 53494579 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,364,334 | 2,306.783093 | 53494579 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,345,133 | 2,303.338763 | 53494579 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,344,524 | 2,303.474580 | 53494579 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,312,387 | 14,689.887759 | 53494579 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,309 | 72.425481 | 53494579 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,130,734 | 37,119,276.868669 | 53494579 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,060,562 | 552,261.921665 | 53494579 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,042,090 | 0.000000 | 53494579 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,314 | 22,200,681.403136 | 53494579 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/VVV | 10000 | 1,007,172 | 95.691150 | 53494579 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,004,872 | 18.690538 | 53494579 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 971,996 | 1,035.225856 | 53494579 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/EDEL | 7000 | 960,632 | 87,720.182354 | 53494579 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/cbBTC | 350 | 946,221 | 0.000013 | 53494579 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/WELL | 10000 | 934,271 | 1,268,138.692297 | 53494579 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/USDC | 10000 | 931,234 | 2,287.059434 | 53494579 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 931,188 | 0.041237 | 53494579 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 924,885 | 73.185421 | 53494579 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | uXRP/WETH | 3000 | 881,551 | 0.000550 | 53494579 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 849,358 | 3,625.917024 | 53494579 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4575 | 826,809 | 19.864946 | 53494579 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,734 | 0.056276 | 53494579 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 781,886 | 0.799140 | 53494579 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 741,217 | 0.594102 | 53494579 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,974 | 0.000257 | 53494579 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 714,941 | 4,909,647.483770 | 53494579 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 677,236 | 146,103.673767 | 53494579 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 676,117 | 0.000008 | 53494579 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 652,870 | 0.536249 | 53494579 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2093 | 650,792 | 547,735.798898 | 53494579 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 646,285 | 2.453307 | 53494579 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome | WETH/bsdETH | 100 | 618,985 | 0.914056 | 53494579 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 610,942 | 0.092548 | 53494579 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 586,273 | 0.040835 | 53494579 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 3207 ; routes examinées : 62510844 ; candidats optimisés : 195727 ; net attendu > 0 : 134 ; dernier cycle 313.2 ms
- Rejets (moteur) : {'spread_below_threshold': 61429743, 'liquidity_below_min': 881790, 'negative_expected_net': 195593, 'borrow_bound_too_small': 3203, 'cycle_budget_exhausted': 328}
- Enregistrements de la session : 195727 ; net attendu > 0 : 134 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 195727} ; motifs de rejet : {'below_safety_margin': 61, 'negative_expected_net': 195593, 'p_lower_below_threshold': 131, 'reliability_not_demonstrated': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53494541 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 396.927215 USDC | 0.070121 USDC | 0.000000 USDC | 0.007272 USDC | 0.062849 USDC (0.0578 €) | — | 1.58 | 0.256 (n=350) | REJECTED | below_safety_margin(62849<79385), p_lower_below_threshold(0.26<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004907 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0574 €) | — | 1.63 | 0.256 (n=350) | REJECTED | below_safety_margin(80<98), p_lower_below_threshold(0.26<0.75) |
| 53494541 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.171917 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0574 €) | — | 1.58 | 0.256 (n=350) | REJECTED | below_safety_margin(27092060689453<34383492694631), p_lower_below_threshold(0.26<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002332 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0431 €) | — | 2.57 | 0.183 (n=877) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53494541 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 192.043443 USDC | 0.053695 USDC | 0.000000 USDC | 0.006922 USDC | 0.046773 USDC (0.0430 €) | — | 2.44 | 0.183 (n=877) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53494541 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.091948 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0429 €) | 0.000020 WETH | 2.20 | 0.183 (n=877) | REJECTED | p_lower_below_threshold(0.18<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001113 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0416 €) | — | 5.21 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 99.787582 USDC | 0.051811 USDC | 0.000000 USDC | 0.006922 USDC | 0.044889 USDC (0.0413 €) | — | 4.50 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.044572 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0409 €) | 0.000019 WETH | 4.34 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 78.349042 USDC | 0.044388 USDC | 0.000000 USDC | 0.006922 USDC | 0.037466 USDC (0.0345 €) | — | 4.78 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.034068 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0344 €) | 0.000016 WETH | 4.77 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[uniswap_v3]→EURC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 76.885486 USDC | 0.043631 USDC | 0.000000 USDC | 0.006922 USDC | 0.036709 USDC (0.0338 €) | — | 4.77 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→EURC→[pancakeswap_v3]→WETH | 0.033473 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0337 €) | — | 4.75 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 77.394326 USDC | 0.043498 USDC | 0.000000 USDC | 0.006922 USDC | 0.036576 USDC (0.0336 €) | — | 4.73 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→EURC→[pancakeswap_v3]→WETH | 0.033685 WETH | 0.000019 WETH | 0.000000 WETH | 0.000003 WETH | 0.000016 WETH (0.0336 €) | — | 4.71 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC | 0.001088 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0330 €) | — | 4.23 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 85.932718 USDC | 0.042640 USDC | 0.000000 USDC | 0.006922 USDC | 0.035718 USDC (0.0329 €) | — | 4.16 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→cbBTC→[uniswap_v3]→WETH | 0.044571 WETH | 0.000018 WETH | 0.000000 WETH | 0.000003 WETH | 0.000015 WETH (0.0324 €) | — | 3.43 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 84.290656 USDC | 0.038155 USDC | 0.000000 USDC | 0.006922 USDC | 0.031233 USDC (0.0287 €) | — | 3.71 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC | 0.001088 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0287 €) | — | 3.68 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→cbBTC→[uniswap_v3]→WETH | 0.039648 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0284 €) | — | 3.39 | 0.290 (n=322) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53494541 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001088 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0273 €) | — | 3.49 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | cbBTC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC | 0.001078 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0273 €) | — | 3.53 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 82.621603 USDC | 0.036138 USDC | 0.000000 USDC | 0.006922 USDC | 0.029216 USDC (0.0269 €) | — | 3.54 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53494541 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.036892 WETH | 0.000016 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0268 €) | — | 3.44 | 0.161 (n=630) | REJECTED | p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 5048 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
