# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T19:45:54+00:00 ; durée 98.86 min ; blocs 56150210 → 56179831 (5368 vus)

## Connexion
- Requêtes RPC : 65820 ; erreurs : 30 ; latence p50/p95 : 124.0/1,530.1 ms
- Rafraîchissements d'état : 5368 ; âge des données au dernier bloc : 9.25 s ; changements de frais LP observés (pools à frais dynamiques) : 3853
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 4176 ; cycles déclenchés par événement : 1368 ; avance médiane sur le rafraîchissement multicall : 370 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,077.56 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 462 pools, 267 jetons, 16678 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 100, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3639 (énumérés 284, par paires 0), mesurés 464, sous le plancher de 10000.0 $ : 2 → gardés 462 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2091.017157, 'cbBTC': 74374.029387, 'AERO': 0.55788}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 135,324,774 | 2,077.564685 | 56179854 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,582,119 | 0.027940 | 56179854 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,669,558 | 0.028003 | 56179854 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,553,602 | 0.000013 | 56179854 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,149,767 | 2,077.796595 | 56179854 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,982,061 | 103.159903 | 56179854 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,644,824 | 0.027932 | 56179854 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,296,945 | 1.803452 | 56179854 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,082,861 | 2,077.122979 | 56179854 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,918,040 | 0.998571 | 56179854 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,063,502 | 43,041.171578 | 56179854 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 123 | 2,923,476 | 2,077.238389 | 56179854 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,228,907 | 0.027989 | 56179854 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,975,297 | 1,121,348.046698 | 56179854 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 472 | 1,654,035 | 0.000013 | 56179854 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,624,012 | 0.016416 | 56179854 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,615,651 | 0.000013 | 56179854 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,570,274 | 0.000000 | 56179854 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,538,327 | 0.000013 | 56179854 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,507,037 | 0.006412 | 56179854 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,375 | 0.830201 | 56179854 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56179854 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,427,603 | 424.781472 | 56179854 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,283,929 | 3,741.874153 | 56179854 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,278,120 | 2,076.940000 | 56179854 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,233,531 | 15,168.943659 | 56179854 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,163,519 | 2,079.762964 | 56179854 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,135,982 | 2,077.677576 | 56179854 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56179854 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,050,813 | 33,778,785.269459 | 56179854 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,039,099 | 102.422348 | 56179854 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,756 | 21.202371 | 56179854 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 950,685 | 560,295.206893 | 56179854 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 924,817 | 0.001490 | 56179854 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 915,481 | 0.049675 | 56179854 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 913,766 | 23,053,289.280513 | 56179854 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 909,183 | 0.000013 | 56179854 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/MORPHO | 3000 | 887,610 | 1,025.015664 | 56179854 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 882,801 | 2,080.323257 | 56179854 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 867,039 | 0.000000 | 56179854 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 776,481 | 78.013640 | 56179854 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 767,846 | 0.052623 | 56179854 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 751,632 | 22.839341 | 56179854 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 738,519 | 120,651.297047 | 56179854 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 718,959 | 3,736.460573 | 56179854 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 703,881 | 0.801801 | 56179854 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 679,138 | 0.535943 | 56179854 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 666,973 | 4,599,757.694679 | 56179854 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 623,026 | 0.488803 | 56179854 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 608,571 | 147,672.084846 | 56179854 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 596,912 | 0.000007 | 56179854 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 586,903 | 0.000259 | 56179854 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2117 | 583,470 | 565,531.970858 | 56179854 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,202 | 0.038371 | 56179854 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 497,319 | 1,025.363052 | 56179854 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 465,233 | 0.067028 | 56179854 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 457,564 | 0.490793 | 56179854 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,442 | 1.000683 | 56179854 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 447,329 | 24.628722 | 56179854 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 442,176 | 908,282.838332 | 56179854 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 6733 ; routes examinées : 112292974 ; candidats optimisés : 440007 ; net attendu > 0 : 344 ; dernier cycle 222.5 ms
- Rejets (moteur) : {'spread_below_threshold': 110307425, 'liquidity_below_min': 1530180, 'negative_expected_net': 439663, 'borrow_bound_too_small': 12338, 'cycle_budget_exhausted': 2963, 'unquotable': 61}
- Enregistrements de la session : 440007 ; net attendu > 0 : 344 ; simulés (eth_call de la vraie tx) : 37 (ok 32, échec 5) ; étiquettes ghost N+1 : 5/33 positives
- Décisions : {'REJECTED': 440007} ; motifs de rejet : {'below_safety_margin': 217, 'negative_expected_net': 439663, 'p_lower_below_threshold': 338, 'reliability_not_demonstrated': 6, 'sim_below_estimate': 1, 'simulated_net_nonpositive': 1, 'simulation_failed': 5, 'stale_data': 66}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002971 cbBTC | 0.000003 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1669 €) | — | 8.21 | 0.144 (n=236) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56178863 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.106755 WETH | 0.000090 WETH | 0.000000 WETH | 0.000003 WETH | 0.000087 WETH (0.1668 €) | 0.000081 WETH | 8.18 | 0.144 (n=236) | REJECTED | p_lower_below_threshold(0.14<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.002669 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1313 €) | — | 7.19 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.092146 WETH | 0.000071 WETH | 0.000000 WETH | 0.000003 WETH | 0.000068 WETH (0.1308 €) | 0.000063 WETH | 7.43 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002515 cbBTC | 0.000002 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000002 cbBTC (0.1272 €) | — | 7.39 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.092157 WETH | 0.000069 WETH | 0.000000 WETH | 0.000003 WETH | 0.000066 WETH (0.1270 €) | 0.000061 WETH | 7.21 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001741 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0547 €) | — | 4.60 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.068100 WETH | 0.000032 WETH | 0.000000 WETH | 0.000003 WETH | 0.000029 WETH (0.0546 €) | — | 4.20 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[uniswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.068444 WETH | 0.000031 WETH | 0.000000 WETH | 0.000003 WETH | 0.000028 WETH (0.0535 €) | — | 4.09 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[uniswap_v3]→cbBTC | 0.001663 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0533 €) | — | 4.69 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→cbBTC | 0.001002 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0513 €) | — | 7.49 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[aerodrome_slipstream]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.039027 WETH | 0.000030 WETH | 0.000000 WETH | 0.000003 WETH | 0.000027 WETH (0.0512 €) | — | 6.87 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001333 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0479 €) | — | 5.25 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56178863 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→AERO→[pancakeswap_v3]→WETH | 0.051655 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0479 €) | — | 4.85 | 0.202 (n=1227) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56174132 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC | 0.010681 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0437 €) | — | 0.60 | 0.265 (n=1578) | REJECTED | below_safety_margin(64<213), p_lower_below_threshold(0.27<0.75) |
| 56174132 | USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 794.809726 USDC | 0.053596 USDC | 0.000000 USDC | 0.006384 USDC | 0.047212 USDC (0.0434 €) | — | 0.59 | 0.265 (n=1578) | REJECTED | below_safety_margin(47212<158961), p_lower_below_threshold(0.27<0.75) |
| 56167293 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.056066 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0433 €) | 0.000023 WETH | 4.03 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56174132 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.392586 WETH | 0.000026 WETH | 0.000000 WETH | 0.000003 WETH | 0.000023 WETH (0.0433 €) | — | 0.58 | 0.265 (n=1578) | REJECTED | below_safety_margin(22654727219442<78517201570312), p_lower_below_threshold(0.27<0.75) |
| 56167293 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 116.074313 USDC | 0.053249 USDC | 0.000000 USDC | 0.006285 USDC | 0.046964 USDC (0.0432 €) | — | 4.05 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.050025 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0364 €) | 0.000019 WETH | 3.79 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 103.494507 USDC | 0.045704 USDC | 0.000000 USDC | 0.006285 USDC | 0.039419 USDC (0.0363 €) | — | 3.81 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.050944 WETH | 0.000022 WETH | 0.000000 WETH | 0.000003 WETH | 0.000019 WETH (0.0359 €) | 0.000019 WETH | 3.68 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56167293 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→VIRTUAL→[pancakeswap_v3]→USDC | 105.432893 USDC | 0.045228 USDC | 0.000000 USDC | 0.006285 USDC | 0.038943 USDC (0.0358 €) | — | 3.69 | 0.203 (n=1224) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56162083 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.028201 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0199 €) | 0.000010 WETH | 3.66 | 0.310 (n=558) | REJECTED | stale_data(4023ms>4000.0), p_lower_below_threshold(0.31<0.75) |
| 56162083 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 58.652831 USDC | 0.027823 USDC | 0.000000 USDC | 0.006310 USDC | 0.021513 USDC (0.0198 €) | — | 3.67 | 0.310 (n=558) | REJECTED | stale_data(4029ms>4000.0), p_lower_below_threshold(0.31<0.75) |

## Fiabilité et décision
- Observations ghost : 8197 ; taux observé 0.216 ; borne inférieure crédible (0.9) 0.210 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.0% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ✅ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
