# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T13:01:27+00:00 ; durée 326.38 min ; blocs 53450975 → 53460765 (8633 vus)

## Connexion
- Requêtes RPC : 101170 ; erreurs : 0 ; latence p50/p95 : 275.6/1,042.3 ms
- Rafraîchissements d'état : 8633 ; âge des données au dernier bloc : 4.79 s ; changements de frais LP observés (pools à frais dynamiques) : 10569
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 28469 ; cycles déclenchés par événement : 3004 ; avance médiane sur le rafraîchissement multicall : 528 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,276.61 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 491 pools, 284 jetons, 18380 routes
- Par DEX : uniswap_v3 137, aerodrome_slipstream 107, aerodrome 202, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3753 (énumérés 307, par paires 0), mesurés 494, sous le plancher de 10000.0 $ : 3 → gardés 491 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 2251.332101, 'cbBTC': 76780.974774, 'AERO': 0.596875}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,969,669 | 2,276.608473 | 53460766 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,422,709 | 0.029494 | 53460766 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,134,087 | 0.029425 | 53460766 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,993,793 | 0.000013 | 53460766 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,914,943 | 2,278.763620 | 53460766 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,669,122 | 103.967124 | 53460766 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,581,647 | 0.001573 | 53460766 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,354,986 | 1.624924 | 53460766 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,832,828 | 0.029492 | 53460766 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,171,575 | 2,278.658970 | 53460766 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,061,656 | 0.999818 | 53460766 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,900,066 | 2,278.455956 | 53460766 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,500,693 | 39,580.803877 | 53460766 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,701,821 | 0.029440 | 53460766 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,160,923 | 1,125,297.120203 | 53460766 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,082,885 | 103.947526 | 53460766 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,808,353 | 0.000013 | 53460766 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,737,209 | 0.017785 | 53460766 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,672,922 | 0.000000 | 53460766 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,634,703 | 0.000013 | 53460766 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,549,534 | 439.567029 | 53460766 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,547,847 | 1.441695 | 53460766 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,546,322 | 0.000013 | 53460766 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,504,665 | 2,276.695769 | 53460766 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,640 | 0.821375 | 53460766 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,407,537 | 3,694.654348 | 53460766 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,340,597 | 2,283.901986 | 53460766 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,328,950 | 0.005115 | 53460766 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,317,646 | 2,278.879655 | 53460766 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,288,396 | 14,923.054475 | 53460766 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 1,233,240 | 0.000013 | 53460766 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/SEND | 3000 | 1,164,536 | 71.652959 | 53460766 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,120,326 | 36,820,465.438368 | 53460766 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,055,628 | 542,609.200358 | 53460766 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,019,609 | 22,327,199.391956 | 53460766 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | DRB/WETH | 10000 | 1,014,573 | 0.000000 | 53460766 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome_slipstream | USDC/VELVET | 100 | 993,360 | 19.316773 | 53460766 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 958,786 | 86,010.681515 | 53460766 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/VVV | 10000 | 932,332 | 104.707170 | 53460766 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/USDC | 10000 | 927,612 | 2,260.589031 | 53460766 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 927,352 | 1,257,245.290092 | 53460766 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/MORPHO | 3000 | 920,040 | 1,077.206699 | 53460766 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 904,283 | 76.557805 | 53460766 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 877,712 | 0.045594 | 53460766 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 871,423 | 0.000559 | 53460766 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 837,336 | 3,720.475675 | 53460766 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 821,154 | 20.059249 | 53460766 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 792,465 | 0.056239 | 53460766 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 772,749 | 0.799125 | 53460766 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 727,085 | 0.588854 | 53460766 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 722,810 | 0.000257 | 53460766 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 714,467 | 4,801,310.055786 | 53460766 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 666,107 | 147,468.360410 | 53460766 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 662,548 | 0.000008 | 53460766 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | WETH/msETH (stable) | 500 | 660,321 | 2.335509 | 53460766 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 655,482 | 0.540600 | 53460766 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 649,075 | 539,560.440854 | 53460766 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 611,559 | 0.914615 | 53460766 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 593,468 | 0.088580 | 53460766 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 564,230 | 0.038509 | 53460766 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 11636 ; routes examinées : 213869680 ; candidats optimisés : 804007 ; net attendu > 0 : 388 ; dernier cycle 74.7 ms
- Rejets (moteur) : {'spread_below_threshold': 209657385, 'liquidity_below_min': 3344041, 'negative_expected_net': 803619, 'unquotable': 49902, 'borrow_bound_too_small': 11614, 'cycle_budget_exhausted': 1561, 'pool_quarantined': 1170}
- Enregistrements de la session : 804007 ; net attendu > 0 : 388 ; simulés (eth_call de la vraie tx) : 40 (ok 18, échec 22) ; étiquettes ghost N+1 : 6/34 positives
- Décisions : {'REJECTED': 804007} ; motifs de rejet : {'below_safety_margin': 261, 'negative_expected_net': 803619, 'p_lower_below_threshold': 334, 'price_impact': 8, 'reliability_not_demonstrated': 54, 'sim_below_estimate': 2, 'simulation_failed': 22}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53460593 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 75.228616 USDC | 2.517209 USDC | 0.000000 USDC | 0.006545 USDC | 2.510664 USDC (2.3098 €) | — | 333.74 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53460593 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.032991 WETH | 0.001104 WETH | 0.000000 WETH | 0.000003 WETH | 0.001101 WETH (2.3061 €) | — | 333.74 | 0.001 (n=7) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53460593 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 74.382431 USDC | 2.489630 USDC | 0.000000 USDC | 0.006545 USDC | 2.483085 USDC (2.2844 €) | — | 333.83 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53460593 | WETH→[uniswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.032632 WETH | 0.001092 WETH | 0.000000 WETH | 0.000003 WETH | 0.001089 WETH (2.2816 €) | — | 333.83 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53460593 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 73.226557 USDC | 2.452790 USDC | 0.000000 USDC | 0.006545 USDC | 2.446245 USDC (2.2505 €) | — | 334.07 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53460593 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.032114 WETH | 0.001076 WETH | 0.000000 WETH | 0.000003 WETH | 0.001073 WETH (2.2470 €) | — | 334.06 | 0.000 (n=21) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53460593 | WETH→[aerodrome_slipstream]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.027600 WETH | 0.000923 WETH | 0.000000 WETH | 0.000003 WETH | 0.000920 WETH (1.9264 €) | — | 333.24 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53460593 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 62.553784 USDC | 2.091064 USDC | 0.000000 USDC | 0.006545 USDC | 2.084519 USDC (1.9178 €) | — | 333.24 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53460593 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 59.399123 USDC | 1.996500 USDC | 0.000000 USDC | 0.006545 USDC | 1.989955 USDC (1.8308 €) | — | 335.01 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53460593 | WETH→[uniswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.026056 WETH | 0.000876 WETH | 0.000000 WETH | 0.000003 WETH | 0.000873 WETH (1.8283 €) | — | 335.01 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53460593 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 59.180835 USDC | 1.990674 USDC | 0.000000 USDC | 0.006545 USDC | 1.984129 USDC (1.8254 €) | — | 335.27 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53460593 | WETH→[pancakeswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.025962 WETH | 0.000873 WETH | 0.000000 WETH | 0.000003 WETH | 0.000870 WETH (1.8231 €) | — | 335.26 | 0.001 (n=7) | REJECTED | reliability_not_demonstrated |
| 53460593 | WETH→[sushiswap_v3]→USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH | 0.024381 WETH | 0.000822 WETH | 0.000000 WETH | 0.000003 WETH | 0.000819 WETH (1.7152 €) | — | 335.88 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53460593 | USDC→[aerodrome]→NOCK→[uniswap_v3]→WETH→[sushiswap_v3]→USDC | 55.460387 USDC | 1.869344 USDC | 0.000000 USDC | 0.006545 USDC | 1.862799 USDC (1.7138 €) | — | 335.88 | 0.000 (n=21) | REJECTED | reliability_not_demonstrated |
| 53452260 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 464.024973 USDC | 1.037007 USDC | 0.000000 USDC | 0.006767 USDC | 1.030240 USDC (0.9478 €) | — | 22.20 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.205746 WETH | 0.000459 WETH | 0.000000 WETH | 0.000003 WETH | 0.000456 WETH (0.9457 €) | — | 22.18 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 464.198632 USDC | 1.034434 USDC | 0.000000 USDC | 0.006767 USDC | 1.027667 USDC (0.9455 €) | — | 22.14 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.205647 WETH | 0.000458 WETH | 0.000000 WETH | 0.000003 WETH | 0.000455 WETH (0.9433 €) | — | 22.14 | 0.000 (n=34) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 437.297961 USDC | 0.916744 USDC | 0.000000 USDC | 0.006767 USDC | 0.909977 USDC (0.8372 €) | — | 20.81 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.193724 WETH | 0.000406 WETH | 0.000000 WETH | 0.000003 WETH | 0.000403 WETH (0.8351 €) | — | 20.80 | 0.000 (n=48) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 424.663486 USDC | 0.877988 USDC | 0.000000 USDC | 0.006767 USDC | 0.871221 USDC (0.8015 €) | — | 20.52 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.188122 WETH | 0.000389 WETH | 0.000000 WETH | 0.000003 WETH | 0.000386 WETH (0.7994 €) | — | 20.51 | 0.000 (n=34) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC | 402.839523 USDC | 0.827841 USDC | 0.000000 USDC | 0.006767 USDC | 0.821074 USDC (0.7554 €) | — | 20.38 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53452260 | WETH→[uniswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.178425 WETH | 0.000367 WETH | 0.000000 WETH | 0.000003 WETH | 0.000364 WETH (0.7532 €) | — | 20.37 | 0.000 (n=48) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53459611 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 2,269.947919 USDC | 0.775012 USDC | 0.000000 USDC | 0.005868 USDC | 0.769144 USDC (0.7076 €) | — | 3.39 | 0.003 (n=2) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 4833 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
