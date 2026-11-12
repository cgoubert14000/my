# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-12T00:20:47+00:00 ; durée 36.58 min ; blocs 56251356 → 56262315 (1828 vus)

## Connexion
- Requêtes RPC : 25190 ; erreurs : 0 ; latence p50/p95 : 187.7/1,236.9 ms
- Rafraîchissements d'état : 1829 ; âge des données au dernier bloc : 6.32 s ; changements de frais LP observés (pools à frais dynamiques) : 1503
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3136 ; cycles déclenchés par événement : 1004 ; avance médiane sur le rafraîchissement multicall : 487 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,053.46 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 458 pools, 265 jetons, 15592 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 98, aerodrome 186, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 159 (rejetés 2) → 564 jetons ; pools candidats 3626 (énumérés 281, par paires 0), mesurés 460, sous le plancher de 10000.0 $ : 2 → gardés 458 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2049.11291, 'cbBTC': 73781.879924, 'AERO': 0.537258}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,392,946 | 2,053.463412 | 56262318 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,437,326 | 0.027804 | 56262318 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,622,594 | 0.027789 | 56262318 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,526,571 | 0.000014 | 56262318 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,095,154 | 2,056.400241 | 56262318 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,867,025 | 104.185128 | 56262318 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,587,438 | 0.027814 | 56262318 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,239,935 | 1.850555 | 56262318 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,018,589 | 2,056.726039 | 56262318 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,891,466 | 0.998581 | 56262318 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,030,336 | 42,973.758515 | 56262318 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 216 | 2,893,925 | 2,056.516076 | 56262318 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,205,032 | 0.027775 | 56262318 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,949,047 | 1,125,188.542308 | 56262318 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,649,502 | 0.000014 | 56262318 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,619,738 | 0.016351 | 56262318 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,608,209 | 0.000014 | 56262318 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,570,599 | 0.000000 | 56262318 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,546,785 | 0.006710 | 56262318 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,531,762 | 0.000014 | 56262318 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,447 | 0.830438 | 56262318 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,437,836 | 1.406597 | 56262318 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,408,084 | 427.940857 | 56262318 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,711 | 2,053.713625 | 56262318 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 1,257,985 | 3,802.825819 | 56262318 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,218,541 | 15,397.493097 | 56262318 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,751 | 2,055.572201 | 56262318 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,126,821 | 2,056.338452 | 56262318 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56262318 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,041,779 | 33,582,000.173247 | 56262318 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,023,019 | 104.619559 | 56262318 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 964,139 | 21.109860 | 56262318 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 935,726 | 567,203.081441 | 56262318 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 915,497 | 0.001480 | 56262318 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 348 | 903,629 | 0.000014 | 56262318 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 900,224 | 0.050659 | 56262318 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 896,190 | 23,358,136.408828 | 56262318 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/USDC | 10000 | 878,529 | 2,054.856011 | 56262318 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 874,591 | 1,030.874965 | 56262318 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 858,211 | 0.000000 | 56262318 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 782,135 | 76.889793 | 56262318 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 761,735 | 0.051759 | 56262318 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 748,396 | 22.978263 | 56262318 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 744,165 | 116,086.409769 | 56262318 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 705,527 | 3,786.866427 | 56262318 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 695,716 | 0.801801 | 56262318 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 666,949 | 0.528738 | 56262318 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 648,349 | 4,756,083.453533 | 56262318 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 616,756 | 0.478774 | 56262318 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 601,279 | 147,804.599882 | 56262318 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 585,706 | 0.000007 | 56262318 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 575,771 | 0.000257 | 56262318 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 573,045 | 563,185.103004 | 56262318 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 558,141 | 0.037532 | 56262318 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2709 | 488,172 | 1,030.079647 | 56262318 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 465,061 | 0.066992 | 56262318 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | USDC/USDT | 8 | 453,786 | 1.000937 | 56262318 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | USDC/MORPHO | 10000 | 445,751 | 0.502364 | 56262318 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| uniswap_v3 | WETH/uSOL | 3000 | 440,499 | 24.808159 | 56262318 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 439,545 | 904,519.367544 | 56262318 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 2829 ; routes examinées : 44109768 ; candidats optimisés : 223137 ; net attendu > 0 : 90 ; dernier cycle 203.0 ms
- Rejets (moteur) : {'spread_below_threshold': 43169213, 'liquidity_below_min': 714206, 'negative_expected_net': 223047, 'borrow_bound_too_small': 2818, 'cycle_budget_exhausted': 394}
- Enregistrements de la session : 223137 ; net attendu > 0 : 90 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 0/2 positives
- Décisions : {'REJECTED': 223137} ; motifs de rejet : {'below_safety_margin': 88, 'negative_expected_net': 223047, 'p_lower_below_threshold': 80, 'reliability_not_demonstrated': 10, 'simulation_failed': 1, 'stale_data': 16}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56252219 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252220 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 310.545098 USDC | 0.024609 USDC | 0.000000 USDC | 0.004606 USDC | 0.020003 USDC (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(20003<62109), p_lower_below_threshold(0.10<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.151840 WETH | 0.000012 WETH | 0.000000 WETH | 0.000002 WETH | 0.000010 WETH (0.0184 €) | — | 0.64 | 0.103 (n=364) | REJECTED | below_safety_margin(9758427752881<30368070316317), p_lower_below_threshold(0.10<0.75) |
| 56258818 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→WETH | 0.028626 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0137 €) | — | 2.53 | 0.103 (n=364) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.10<0.75) |
| 56252219 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252220 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 143.484105 USDC | 0.012065 USDC | 0.000000 USDC | 0.004917 USDC | 0.007148 USDC (0.0066 €) | — | 0.50 | 0.087 (n=116) | REJECTED | below_safety_margin(7148<28696), p_lower_below_threshold(0.09<0.75) |
| 56252219 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56252220 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.070478 WETH | 0.000006 WETH | 0.000000 WETH | 0.000002 WETH | 0.000003 WETH (0.0066 €) | — | 0.49 | 0.087 (n=116) | REJECTED | below_safety_margin(3486419375392<14095681478295), p_lower_below_threshold(0.09<0.75) |
| 56255772 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 39.914714 USDC | 0.011309 USDC | 0.000000 USDC | 0.006196 USDC | 0.005113 USDC (0.0047 €) | — | 1.28 | 0.344 (n=610) | REJECTED | below_safety_margin(5113<7982), p_lower_below_threshold(0.34<0.75) |
| 56255772 | USDC→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC | 39.914714 USDC | 0.011309 USDC | 0.000000 USDC | 0.006196 USDC | 0.005113 USDC (0.0047 €) | — | 1.28 | 0.344 (n=610) | REJECTED | below_safety_margin(5113<7982), p_lower_below_threshold(0.34<0.75) |
| 56255772 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.019372 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 1.28 | 0.344 (n=610) | REJECTED | below_safety_margin(2483523055206<3874347793617), p_lower_below_threshold(0.34<0.75) |
| 56255772 | WETH→[aerodrome_slipstream]→USDT→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.019372 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000002 WETH (0.0047 €) | — | 1.28 | 0.344 (n=610) | REJECTED | below_safety_margin(2483523055206<3874347793617), p_lower_below_threshold(0.34<0.75) |
| 56257743 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 148.015939 USDC | 0.009237 USDC | 0.000000 USDC | 0.004615 USDC | 0.004622 USDC (0.0043 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(4622<29603), p_lower_below_threshold(0.10<0.75) |
| 56257743 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 148.015939 USDC | 0.009237 USDC | 0.000000 USDC | 0.004615 USDC | 0.004622 USDC (0.0043 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(4622<29603), p_lower_below_threshold(0.10<0.75) |
| 56257740 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 148.015939 USDC | 0.009237 USDC | 0.000000 USDC | 0.004616 USDC | 0.004621 USDC (0.0043 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(4621<29603), p_lower_below_threshold(0.10<0.75) |
| 56257740 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 148.015939 USDC | 0.009237 USDC | 0.000000 USDC | 0.004616 USDC | 0.004621 USDC (0.0043 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(4621<29603), p_lower_below_threshold(0.10<0.75) |
| 56257741 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 148.015939 USDC | 0.009237 USDC | 0.000000 USDC | 0.004616 USDC | 0.004621 USDC (0.0043 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(4621<29603), p_lower_below_threshold(0.10<0.75) |
| 56257742 | USDC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 148.015939 USDC | 0.009237 USDC | 0.000000 USDC | 0.004616 USDC | 0.004621 USDC (0.0043 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(4621<29603), p_lower_below_threshold(0.10<0.75) |
| 56257743 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072301 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0042 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(2247081482278<14460278246839), p_lower_below_threshold(0.10<0.75) |
| 56257743 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072301 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0042 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(2247081482278<14460278246839), p_lower_below_threshold(0.10<0.75) |
| 56257740 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072301 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0042 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(2246780277682<14460278246839), p_lower_below_threshold(0.10<0.75) |
| 56257741 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072301 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0042 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(2246780277682<14460278246839), p_lower_below_threshold(0.10<0.75) |
| 56257742 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072301 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0042 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(2246780277682<14460278246839), p_lower_below_threshold(0.10<0.75) |
| 56257740 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.072301 WETH | 0.000004 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0042 €) | — | 0.31 | 0.103 (n=364) | REJECTED | below_safety_margin(2246506318932<14460278246839), p_lower_below_threshold(0.10<0.75) |

## Fiabilité et décision
- Observations ghost : 8236 ; taux observé 0.217 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
