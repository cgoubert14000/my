# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T02:48:40+00:00 ; durée 92.61 min ; blocs 55846916 → 55874681 (6583 vus)

## Connexion
- Requêtes RPC : 73438 ; erreurs : 35 ; latence p50/p95 : 125.3/1,139.4 ms
- Rafraîchissements d'état : 6583 ; âge des données au dernier bloc : 4.32 s ; changements de frais LP observés (pools à frais dynamiques) : 3713
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 510 ; cycles déclenchés par événement : 224 ; avance médiane sur le rafraîchissement multicall : 444 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,054.71 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 459 pools, 268 jetons, 15492 routes
- Par DEX : uniswap_v3 133, aerodrome_slipstream 97, aerodrome 189, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 162 (rejetés 2) → 567 jetons ; pools candidats 3634 (énumérés 283, par paires 0), mesurés 461, sous le plancher de 10000.0 $ : 2 → gardés 459 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2047.571772, 'cbBTC': 73300.62757, 'AERO': 0.541198}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,022,291 | 2,054.709699 | 55874681 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,352,835 | 0.027971 | 55874681 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,554,238 | 0.027922 | 55874681 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,318,900 | 0.000014 | 55874681 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,067,870 | 2,059.514538 | 55874681 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,787,483 | 106.777316 | 55874681 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,335,308 | 0.027966 | 55874681 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,264,089 | 1.846941 | 55874681 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,896,111 | 2,059.808828 | 55874681 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,866,585 | 0.998998 | 55874681 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,061,907 | 42,143.328797 | 55874681 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,926,160 | 2,059.923026 | 55874681 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,285,444 | 0.027937 | 55874681 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,953,599 | 1,121,311.176185 | 55874681 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,677,691 | 0.000014 | 55874681 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 1,614,716 | 0.000014 | 55874681 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,614,157 | 0.016270 | 55874681 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,562,726 | 0.000000 | 55874681 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,527,898 | 0.006634 | 55874681 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,952 | 0.824067 | 55874681 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,435,114 | 1.411180 | 55874681 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,422,359 | 0.000014 | 55874681 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,421,837 | 414.142066 | 55874681 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,351,615 | 2,059.701330 | 55874681 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,978 | 2,054.447166 | 55874681 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,261,919 | 3,799.814438 | 55874681 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,232,500 | 14,821.375827 | 55874681 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,157,324 | 2,054.453037 | 55874681 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,063,864 | 85.855202 | 55874681 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,052,865 | 32,637,140.732432 | 55874681 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 959,980 | 21.390298 | 55874681 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 943,708 | 555,014.491652 | 55874681 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 943,339 | 107.254828 | 55874681 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 911,767 | 0.001484 | 55874681 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 910,024 | 22,793,699.651296 | 55874681 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 344 | 908,738 | 0.000014 | 55874681 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 879,716 | 1,023.712864 | 55874681 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 878,430 | 2,046.596008 | 55874681 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | USDC/VVV | 3000 | 876,747 | 0.051816 | 55874681 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | DRB/WETH | 10000 | 861,774 | 0.000000 | 55874681 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 768,940 | 79.551263 | 55874681 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 764,625 | 22.298074 | 55874681 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 761,674 | 0.051754 | 55874681 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/EDEL | 7000 | 751,697 | 113,909.477340 | 55874681 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 706,996 | 3,772.891608 | 55874681 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 695,645 | 0.802938 | 55874681 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 661,032 | 0.533249 | 55874681 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 652,003 | 4,702,956.843574 | 55874681 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 627,155 | 0.495138 | 55874681 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 594,686 | 151,217.378339 | 55874681 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 585,237 | 0.000007 | 55874681 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 580,097 | 0.000259 | 55874681 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 579,853 | 557,929.034286 | 55874681 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 557,715 | 0.037505 | 55874681 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 492,271 | 1,024.013167 | 55874681 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 467,900 | 0.067534 | 55874681 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 461,654 | 0.496352 | 55874681 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,047 | 1.001057 | 55874681 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/UNI | 10000 | 442,354 | 305.890640 | 55874681 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 441,209 | 896,087.714829 | 55874681 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 6806 ; routes examinées : 105438552 ; candidats optimisés : 597120 ; net attendu > 0 : 1024 ; dernier cycle 221.0 ms
- Rejets (moteur) : {'spread_below_threshold': 102986351, 'liquidity_below_min': 1834232, 'negative_expected_net': 596096, 'borrow_bound_too_small': 10839, 'cycle_budget_exhausted': 9960}
- Enregistrements de la session : 597117 ; net attendu > 0 : 1024 ; simulés (eth_call de la vraie tx) : 37 (ok 31, échec 6) ; étiquettes ghost N+1 : 13/30 positives
- Décisions : {'REJECTED': 597117} ; motifs de rejet : {'below_safety_margin': 901, 'negative_expected_net': 596093, 'p_lower_below_threshold': 987, 'reliability_not_demonstrated': 37, 'sim_below_estimate': 3, 'simulated_net_nonpositive': 3, 'simulation_failed': 6, 'stale_data': 14}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55854227 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 412.007847 USDC | 0.098781 USDC | 0.000000 USDC | 0.006174 USDC | 0.092607 USDC (0.0852 €) | — | 2.25 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.198394 WETH | 0.000048 WETH | 0.000000 WETH | 0.000003 WETH | 0.000045 WETH (0.0848 €) | 0.000045 WETH | 2.26 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.005463 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0847 €) | — | 2.29 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.004451 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0664 €) | — | 2.20 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.161267 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0663 €) | 0.000035 WETH | 2.18 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 328.352486 USDC | 0.078084 USDC | 0.000000 USDC | 0.006174 USDC | 0.071910 USDC (0.0662 €) | — | 2.19 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 330.106605 USDC | 0.067840 USDC | 0.000000 USDC | 0.006174 USDC | 0.061666 USDC (0.0567 €) | — | 1.87 | 0.256 (n=1538) | REJECTED | below_safety_margin(61666<66021), p_lower_below_threshold(0.26<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.151824 WETH | 0.000033 WETH | 0.000000 WETH | 0.000003 WETH | 0.000030 WETH (0.0567 €) | — | 1.98 | 0.256 (n=1538) | REJECTED | below_safety_margin(29997961983564<30364700178971), p_lower_below_threshold(0.26<0.75) |
| 55854227 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.003968 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0563 €) | — | 2.09 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 337.979524 USDC | 0.063752 USDC | 0.000000 USDC | 0.006174 USDC | 0.057578 USDC (0.0530 €) | — | 1.70 | 0.256 (n=1538) | REJECTED | below_safety_margin(57578<67595), p_lower_below_threshold(0.26<0.75) |
| 55854227 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.004291 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0529 €) | — | 1.82 | 0.256 (n=1538) | REJECTED | below_safety_margin(78<85), p_lower_below_threshold(0.26<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.151806 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0526 €) | — | 1.83 | 0.256 (n=1538) | REJECTED | below_safety_margin(27820234918570<30361261596717), p_lower_below_threshold(0.26<0.75) |
| 55854561 | USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 80.117292 USDC | 0.055380 USDC | 0.000000 USDC | 0.006607 USDC | 0.048773 USDC (0.0449 €) | — | 6.09 | 0.307 (n=529) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 55854561 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→USDbC→[uniswap_v3]→WETH | 0.038926 WETH | 0.000027 WETH | 0.000000 WETH | 0.000003 WETH | 0.000024 WETH (0.0448 €) | — | 6.07 | 0.307 (n=529) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.31<0.75) |
| 55854227 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.002216 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0441 €) | — | 2.93 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.086645 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0439 €) | 0.000023 WETH | 2.68 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854227 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 182.359731 USDC | 0.053612 USDC | 0.000000 USDC | 0.006174 USDC | 0.047438 USDC (0.0436 €) | — | 2.60 | 0.113 (n=39) | REJECTED | p_lower_below_threshold(0.11<0.75) |
| 55854561 | USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 63.751067 USDC | 0.051378 USDC | 0.000000 USDC | 0.006001 USDC | 0.045377 USDC (0.0417 €) | — | 7.12 | 0.168 (n=301) | REJECTED | p_lower_below_threshold(0.17<0.75) |
| 55854561 | WETH→[uniswap_v3]→USDC→[aerodrome]→LCAP→[aerodrome_slipstream]→WETH | 0.030941 WETH | 0.000025 WETH | 0.000000 WETH | 0.000003 WETH | 0.000022 WETH (0.0416 €) | -0.000000 WETH | 7.10 | 0.168 (n=301) | REJECTED | sim_below_estimate(2862163301792<24885619567267), simulated_net_nonpositive, p_lower_below_threshold(0.17<0.75) |
| 55868683 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.149417 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0397 €) | — | 1.41 | 0.257 (n=1541) | REJECTED | below_safety_margin(21064824723067<29883348685593), p_lower_below_threshold(0.26<0.75) |
| 55868683 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 303.950942 USDC | 0.049681 USDC | 0.000000 USDC | 0.006812 USDC | 0.042869 USDC (0.0394 €) | — | 1.41 | 0.257 (n=1541) | REJECTED | below_safety_margin(42869<60790), p_lower_below_threshold(0.26<0.75) |
| 55854227 | USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 183.822277 USDC | 0.049060 USDC | 0.000000 USDC | 0.006486 USDC | 0.042574 USDC (0.0392 €) | — | 2.32 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55868683 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.003765 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0391 €) | — | 1.54 | 0.257 (n=1541) | REJECTED | below_safety_margin(58<75), p_lower_below_threshold(0.26<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→USDT→[uniswap_v3]→WETH | 0.089303 WETH | 0.000024 WETH | 0.000000 WETH | 0.000003 WETH | 0.000021 WETH (0.0390 €) | — | 2.31 | 0.256 (n=1538) | REJECTED | p_lower_below_threshold(0.26<0.75) |
| 55854227 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.152012 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0374 €) | — | 1.30 | 0.256 (n=1538) | REJECTED | below_safety_margin(19784321558651<30402399223959), p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 7962 ; taux observé 0.210 ; borne inférieure crédible (0.9) 0.204 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
