# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-03T23:54:25+00:00 ; durée 304.95 min ; blocs 53471207 → 53480355 (8919 vus)

## Connexion
- Requêtes RPC : 106117 ; erreurs : 825 ; latence p50/p95 : 176.3/1,265.3 ms
- Rafraîchissements d'état : 8920 ; âge des données au dernier bloc : 0.97 s ; changements de frais LP observés (pools à frais dynamiques) : 7742
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 77782 ; cycles déclenchés par événement : 8660 ; avance médiane sur le rafraîchissement multicall : 436 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,287.82 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 493 pools, 285 jetons, 19448 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 107, aerodrome 205, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 309, par paires 0), mesurés 496, sous le plancher de 10000.0 $ : 3 → gardés 493 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'DAI': 1.0, 'USDC': 1.0, 'WETH': 2294.78828, 'cbBTC': 77607.185431, 'AERO': 0.633493}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 150,850,397 | 2,287.821399 | 53480355 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,772,667 | 0.029388 | 53480355 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,213,505 | 0.029450 | 53480355 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,080,606 | 0.000013 | 53480355 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,050,807 | 2,282.111261 | 53480355 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,817,810 | 100.378769 | 53480355 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,627,361 | 0.001569 | 53480355 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,419,535 | 1.573182 | 53480355 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,836,307 | 0.029395 | 53480355 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,186,996 | 2,281.322664 | 53480355 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,095,485 | 0.999907 | 53480355 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,874,117 | 2,281.433300 | 53480355 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,462,331 | 40,862.300708 | 53480355 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,688,592 | 0.029440 | 53480355 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,161,786 | 1,135,502.765144 | 53480355 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2700 | 2,143,414 | 100.369407 | 53480355 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,817,953 | 0.000013 | 53480355 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,742,688 | 0.017882 | 53480355 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,679,647 | 0.000000 | 53480355 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,646,774 | 0.006665 | 53480355 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,629,250 | 0.000013 | 53480355 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,562,126 | 435.062174 | 53480355 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,557,242 | 0.000013 | 53480355 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,554,793 | 1.429892 | 53480355 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,503 | 2,287.872437 | 53480355 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,814 | 0.821835 | 53480355 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,430,346 | 3,585.264802 | 53480355 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,341,351 | 2,288.206975 | 53480355 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,338,396 | 2,282.147383 | 53480355 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,303,285 | 14,827.442738 | 53480355 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,466 | 72.405863 | 53480355 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,119,947 | 36,934,354.391659 | 53480355 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 1,067,417 | 0.000000 | 53480355 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,058,756 | 545,635.926932 | 53480355 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,035,076 | 21,950,664.012046 | 53480355 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,000,291 | 18.935092 | 53480355 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/VVV | 10000 | 960,849 | 101.018619 | 53480355 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/EDEL | 7000 | 958,528 | 86,906.959027 | 53480355 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 951,536 | 1,061.671321 | 53480355 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 944,195 | 0.000013 | 53480355 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 936,466 | 71.386386 | 53480355 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 928,655 | 2,282.122456 | 53480355 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 925,534 | 1,274,612.572122 | 53480355 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | USDC/VVV | 3000 | 893,859 | 0.043876 | 53480355 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 880,155 | 0.000557 | 53480355 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 849,539 | 3,611.587591 | 53480355 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 827,108 | 19.846237 | 53480355 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 801,419 | 0.057588 | 53480355 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 776,548 | 0.799140 | 53480355 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 737,004 | 0.592507 | 53480355 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 726,939 | 0.000257 | 53480355 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 711,197 | 4,893,925.686914 | 53480355 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 675,978 | 0.000008 | 53480355 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 669,266 | 147,536.479438 | 53480355 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | WETH/msETH (stable) | 500 | 657,312 | 2.368619 | 53480355 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | TIG/USDC | 10000 | 652,783 | 0.536208 | 53480355 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 650,400 | 545,628.829201 | 53480355 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,537 | 0.914716 | 53480355 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 593,723 | 0.088624 | 53480355 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,350 | 0.038742 | 53480355 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 17579 ; routes examinées : 341876392 ; candidats optimisés : 899286 ; net attendu > 0 : 602 ; dernier cycle 264.8 ms
- Rejets (moteur) : {'spread_below_threshold': 336998208, 'liquidity_below_min': 3920667, 'negative_expected_net': 898684, 'unquotable': 35132, 'borrow_bound_too_small': 17566, 'pool_quarantined': 4892, 'cycle_budget_exhausted': 591}
- Enregistrements de la session : 899286 ; net attendu > 0 : 602 ; simulés (eth_call de la vraie tx) : 40 (ok 22, échec 18) ; étiquettes ghost N+1 : 0/30 positives
- Décisions : {'REJECTED': 899286} ; motifs de rejet : {'below_safety_margin': 534, 'negative_expected_net': 898684, 'p_lower_below_threshold': 589, 'reliability_not_demonstrated': 13, 'sim_below_estimate': 2, 'simulated_net_nonpositive': 2, 'simulation_failed': 18, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53476657 | USDC→[uniswap_v3]→OWB→[aerodrome]→USDC | 137.053961 USDC | 3.316241 USDC | 0.000000 USDC | 0.004826 USDC | 3.311415 USDC (3.0465 €) | — | 241.61 | 0.000 (n=16) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53477925 | WETH→[uniswap_v3]→CLANKER→[aerodrome_slipstream]→WETH | 0.006782 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1774 €) | 0.000084 WETH | 124.12 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53477925 | WETH→[uniswap_v3]→CLANKER→[aerodrome_slipstream]→WETH | 0.006782 WETH | 0.000086 WETH | 0.000000 WETH | 0.000002 WETH | 0.000084 WETH (0.1774 €) | 0.000084 WETH | 124.12 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53472395 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.026252 WETH | 0.000056 WETH | 0.000000 WETH | 0.000002 WETH | 0.000054 WETH (0.1137 €) | — | 20.53 | 0.001 (n=11) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53472362 | WETH→[aerodrome_slipstream]→CLANKER→[uniswap_v3]→WETH | 0.020014 WETH | 0.000033 WETH | 0.000000 WETH | 0.000002 WETH | 0.000030 WETH (0.0642 €) | — | 15.21 | 0.001 (n=13) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53476424 | WETH→[aerodrome_slipstream]→ZRO→[uniswap_v3]→WETH | 0.010639 WETH | 0.000024 WETH | 0.000000 WETH | 0.000002 WETH | 0.000021 WETH (0.0451 €) | — | 20.14 | 0.001 (n=12) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53477292 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 46.827655 USDC | 0.053258 USDC | 0.000000 USDC | 0.005143 USDC | 0.048115 USDC (0.0443 €) | — | 10.27 | 0.000 (n=78) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.00<0.75) |
| 53476455 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 771.228037 USDC | 0.051205 USDC | 0.000000 USDC | 0.005140 USDC | 0.046065 USDC (0.0424 €) | — | 0.60 | 0.034 (n=197) | REJECTED | below_safety_margin(46065<154245), p_lower_below_threshold(0.03<0.75) |
| 53476455 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010013 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0422 €) | — | 0.59 | 0.034 (n=197) | REJECTED | below_safety_margin(59<200), p_lower_below_threshold(0.03<0.75) |
| 53477395 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001206 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0300 €) | 0.000000 cbBTC | 3.48 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53477395 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.001206 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0300 €) | 0.000000 cbBTC | 3.48 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53477395 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 99.504389 USDC | 0.039456 USDC | 0.000000 USDC | 0.006883 USDC | 0.032573 USDC (0.0300 €) | 0.032573 USDC | 3.27 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53477395 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 99.504389 USDC | 0.039456 USDC | 0.000000 USDC | 0.006883 USDC | 0.032573 USDC (0.0300 €) | 0.032573 USDC | 3.27 | 0.158 (n=610) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53475795 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 19.939998 USDC | 0.035428 USDC | 0.000000 USDC | 0.004826 USDC | 0.030602 USDC (0.0282 €) | — | 15.35 | 0.010 (n=29) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000502 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0243 €) | — | 6.77 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474176 | USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 37.177276 USDC | 0.033271 USDC | 0.000000 USDC | 0.006868 USDC | 0.026403 USDC (0.0243 €) | 0.026403 USDC | 7.10 | 0.159 (n=606) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC | 61.786427 USDC | 0.031613 USDC | 0.000000 USDC | 0.007215 USDC | 0.024398 USDC (0.0224 €) | — | 3.95 | 0.159 (n=607) | REJECTED | p_lower_below_threshold(0.16<0.75) |
| 53474568 | WETH→[pancakeswap_v3]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.027157 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0224 €) | — | 3.92 | 0.159 (n=607) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.16<0.75) |
| 53476025 | USDC→[pancakeswap_v3]→PLAY→[aerodrome_slipstream]→USDC | 34.625441 USDC | 0.029251 USDC | 0.000000 USDC | 0.005141 USDC | 0.024110 USDC (0.0222 €) | — | 6.96 | 0.034 (n=242) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |
| 53475911 | cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.001166 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0207 €) | 0.000000 cbBTC | 2.49 | 0.259 (n=342) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 53475911 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[uniswap_v3]→USDC | 90.505089 USDC | 0.029717 USDC | 0.000000 USDC | 0.007227 USDC | 0.022490 USDC (0.0207 €) | 0.022490 USDC | 2.48 | 0.259 (n=342) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |
| 53474176 | cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→MAMO→[aerodrome_slipstream]→cbBTC | 0.000396 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0200 €) | — | 7.06 | 0.291 (n=315) | REJECTED | p_lower_below_threshold(0.29<0.75) |

## Fiabilité et décision
- Observations ghost : 4935 ; taux observé 0.168 ; borne inférieure crédible (0.9) 0.161 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
