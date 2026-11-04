# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-04T04:35:49+00:00 ; durée 246.29 min ; blocs 53481408 → 53488797 (7254 vus)

## Connexion
- Requêtes RPC : 83758 ; erreurs : 175 ; latence p50/p95 : 271.5/1,022.2 ms
- Rafraîchissements d'état : 7254 ; âge des données au dernier bloc : 2.41 s ; changements de frais LP observés (pools à frais dynamiques) : 15657
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 76782 ; cycles déclenchés par événement : 5222 ; avance médiane sur le rafraîchissement multicall : 333 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,258.09 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 490 pools, 282 jetons, 19430 routes
- Par DEX : uniswap_v3 139, aerodrome_slipstream 105, aerodrome 203, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 172 (rejetés 2) → 577 jetons ; pools candidats 3703 (énumérés 305, par paires 0), mesurés 493, sous le plancher de 10000.0 $ : 3 → gardés 490 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2264.542979, 'cbBTC': 77119.048638, 'AERO': 0.629628}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 149,777,561 | 2,258.091813 | 53488797 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,562,392 | 0.029446 | 53488797 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,364,089 | 0.000013 | 53488797 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,088,100 | 0.029464 | 53488797 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,973,432 | 2,252.414143 | 53488797 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,563,232 | 104.352422 | 53488797 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,502,858 | 0.001557 | 53488797 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,347,198 | 1.610986 | 53488797 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,746,285 | 0.029434 | 53488797 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,190,655 | 2,252.202562 | 53488797 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,034,386 | 0.999901 | 53488797 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,834,313 | 2,252.139618 | 53488797 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome | WETH/KTA | 3000 | 3,403,838 | 41,187.091687 | 53488797 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,651,981 | 0.029446 | 53488797 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,134,010 | 1,135,166.341200 | 53488797 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | WETH/VVV | 2796 | 2,055,279 | 104.381569 | 53488797 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome_slipstream | USDC/cbBTC | 580 | 1,799,761 | 0.000013 | 53488797 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,713,098 | 0.017386 | 53488797 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,662,335 | 0.006788 | 53488797 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,657,373 | 0.000000 | 53488797 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,606,031 | 0.000013 | 53488797 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,552,822 | 1.432992 | 53488797 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,535,345 | 441.294080 | 53488797 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,534,043 | 0.000013 | 53488797 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,498,750 | 2,258.223531 | 53488797 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,451,706 | 0.818329 | 53488797 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,403,355 | 3,633.810242 | 53488797 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,341,491 | 2,252.429854 | 53488797 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,332,124 | 2,258.344830 | 53488797 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,277,223 | 14,980.188232 | 53488797 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,158,309 | 72.425481 | 53488797 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,109,113 | 37,048,350.985269 | 53488797 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,035,195 | 559,119.421359 | 53488797 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,017,152 | 0.000000 | 53488797 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,015,614 | 22,173,343.364628 | 53488797 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 986,463 | 19.713281 | 53488797 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/EDEL | 7000 | 948,508 | 86,461.095069 | 53488797 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/MORPHO | 3000 | 944,449 | 1,049.098005 | 53488797 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/VVV | 10000 | 938,027 | 104.494270 | 53488797 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/cbBTC | 358 | 933,329 | 0.000013 | 53488797 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 932,075 | 72.060653 | 53488797 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 924,747 | 2,248.529703 | 53488797 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | WETH/WELL | 10000 | 915,548 | 1,268,935.423337 | 53488797 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | uXRP/WETH | 3000 | 869,975 | 0.000556 | 53488797 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 860,192 | 0.046355 | 53488797 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 832,760 | 3,609.286650 | 53488797 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 811,154 | 20.431997 | 53488797 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 788,728 | 0.055681 | 53488797 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 766,457 | 0.799140 | 53488797 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 729,561 | 0.579244 | 53488797 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 717,492 | 0.000257 | 53488797 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 699,764 | 4,924,585.364880 | 53488797 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 662,833 | 0.000008 | 53488797 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 657,690 | 148,855.640377 | 53488797 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | TIG/USDC | 10000 | 653,240 | 0.536801 | 53488797 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 650,230 | 2.360741 | 53488797 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 633,818 | 560,854.280191 | 53488797 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 606,770 | 0.914056 | 53488797 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 581,488 | 0.085908 | 53488797 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 554,612 | 0.037509 | 53488797 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 12475 ; routes examinées : 242389250 ; candidats optimisés : 845801 ; net attendu > 0 : 1662 ; dernier cycle 276.5 ms
- Rejets (moteur) : {'spread_below_threshold': 237367188, 'liquidity_below_min': 4159810, 'negative_expected_net': 844139, 'borrow_bound_too_small': 12441, 'cycle_budget_exhausted': 4010}
- Enregistrements de la session : 845801 ; net attendu > 0 : 1662 ; simulés (eth_call de la vraie tx) : 101 (ok 35, échec 66) ; étiquettes ghost N+1 : 15/83 positives
- Décisions : {'REJECTED': 845801} ; motifs de rejet : {'below_safety_margin': 940, 'negative_expected_net': 844139, 'p_lower_below_threshold': 1333, 'price_impact': 4, 'reliability_not_demonstrated': 329, 'sim_below_estimate': 10, 'simulated_net_nonpositive': 6, 'simulation_failed': 66, 'stale_data': 5}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53485970 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 2.700934 WETH | 0.003132 WETH | 0.000000 WETH | 0.000006 WETH | 0.003126 WETH (6.4400 €) | — | 11.58 | 0.099 (n=119) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 53485970 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.078963 cbBTC | 0.000092 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000092 cbBTC (6.4380 €) | — | 11.66 | 0.099 (n=119) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53485970 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 6,048.740913 USDC | 7.005580 USDC | 0.000000 USDC | 0.013466 USDC | 6.992114 USDC (6.4327 €) | — | 11.56 | 0.099 (n=119) | REJECTED | p_lower_below_threshold(0.10<0.75) |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→WETH | 0.304813 WETH | 0.002926 WETH | 0.000000 WETH | 0.000002 WETH | 0.002924 WETH (6.0426 €) | — | 95.92 | — (n=0) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008937 cbBTC | 0.000086 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000086 cbBTC (6.0418 €) | — | 96.36 | — (n=0) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008685 cbBTC | 0.000084 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000084 cbBTC (5.8833 €) | — | 96.55 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.297193 WETH | 0.002849 WETH | 0.000000 WETH | 0.000003 WETH | 0.002846 WETH (5.8817 €) | — | 95.76 | 0.001 (n=6) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53485940 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 669.262385 USDC | 6.386324 USDC | 0.000000 USDC | 0.007556 USDC | 6.378768 USDC (5.8685 €) | — | 95.31 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008637 cbBTC | 0.000083 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000083 cbBTC (5.8026 €) | — | 95.76 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.293823 WETH | 0.002810 WETH | 0.000000 WETH | 0.000003 WETH | 0.002807 WETH (5.8003 €) | — | 95.52 | 0.001 (n=8) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53485940 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 658.335703 USDC | 6.297702 USDC | 0.000000 USDC | 0.007556 USDC | 6.290146 USDC (5.7869 €) | — | 95.55 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008542 cbBTC | 0.000082 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000082 cbBTC (5.7584 €) | — | 96.08 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.291469 WETH | 0.002788 WETH | 0.000000 WETH | 0.000004 WETH | 0.002784 WETH (5.7544 €) | — | 95.53 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 653.649759 USDC | 6.251532 USDC | 0.000000 USDC | 0.008356 USDC | 6.243176 USDC (5.7437 €) | — | 95.51 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008570 cbBTC | 0.000082 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000081 cbBTC (5.7128 €) | — | 95.02 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.293823 WETH | 0.002766 WETH | 0.000000 WETH | 0.000003 WETH | 0.002763 WETH (5.7098 €) | — | 94.03 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 661.163621 USDC | 6.201346 USDC | 0.000000 USDC | 0.007556 USDC | 6.193790 USDC (5.6983 €) | — | 93.68 | 0.001 (n=8) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008569 cbBTC | 0.000081 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000081 cbBTC (5.6798 €) | — | 94.48 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.287303 WETH | 0.002750 WETH | 0.000000 WETH | 0.000004 WETH | 0.002746 WETH (5.6749 €) | — | 95.58 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC | 644.013970 USDC | 6.165153 USDC | 0.000000 USDC | 0.008356 USDC | 6.156797 USDC (5.6643 €) | — | 95.60 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC | 0.008521 cbBTC | 0.000081 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000081 cbBTC (5.6609 €) | — | 94.70 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.291469 WETH | 0.002741 WETH | 0.000000 WETH | 0.000003 WETH | 0.002737 WETH (5.6573 €) | — | 93.92 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | USDC→[pancakeswap_v3]→WETH→[aerodrome]→cbBTC→[pancakeswap_v3]→USDC | 652.325053 USDC | 6.145273 USDC | 0.000000 USDC | 0.007556 USDC | 6.137717 USDC (5.6467 €) | — | 94.09 | 0.001 (n=6) | REJECTED | reliability_not_demonstrated |
| 53485940 | cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH→[aerodrome]→cbBTC | 0.008557 cbBTC | 0.000080 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000080 cbBTC (5.6335 €) | — | 93.84 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |
| 53485940 | WETH→[aerodrome]→cbBTC→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.290673 WETH | 0.002728 WETH | 0.000000 WETH | 0.000003 WETH | 0.002724 WETH (5.6299 €) | — | 93.72 | 0.000 (n=23) | REJECTED | reliability_not_demonstrated |

## Fiabilité et décision
- Observations ghost : 5023 ; taux observé 0.169 ; borne inférieure crédible (0.9) 0.162 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.2% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
