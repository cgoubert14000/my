# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T14:02:45+00:00 ; durée 92.02 min ; blocs 56049289 → 56076890 (2120 vus)

## Connexion
- Requêtes RPC : 33782 ; erreurs : 80 ; latence p50/p95 : 629.1/2,624.7 ms
- Rafraîchissements d'état : 2120 ; âge des données au dernier bloc : 10.71 s ; changements de frais LP observés (pools à frais dynamiques) : 1908
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1355 ; cycles déclenchés par événement : 531 ; avance médiane sur le rafraîchissement multicall : 893 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,053.11 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 460 pools, 267 jetons, 15580 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 99, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3638 (énumérés 283, par paires 0), mesurés 462, sous le plancher de 10000.0 $ : 2 → gardés 460 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2055.911323, 'cbBTC': 73875.741474, 'AERO': 0.535737}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 134,209,817 | 2,053.108441 | 56076890 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,335,856 | 0.027883 | 56076890 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,565,985 | 0.027840 | 56076890 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,407,280 | 0.000014 | 56076890 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,085,353 | 2,058.315450 | 56076890 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,854,052 | 104.543735 | 56076890 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| aerodrome | USDC/AERO | 3000 | 4,279,734 | 1.823953 | 56076890 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,274,198 | 0.027889 | 56076890 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,037,991 | 2,058.757949 | 56076890 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,869,235 | 1.000003 | 56076890 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,042,845 | 42,606.454411 | 56076890 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,916,940 | 2,058.825629 | 56076890 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,208,339 | 0.027826 | 56076890 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,951,005 | 1,122,542.542992 | 56076890 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,645,203 | 0.000014 | 56076890 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,613,777 | 0.016263 | 56076890 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,599,446 | 0.000014 | 56076890 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,548,964 | 0.000000 | 56076890 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,528,680 | 0.000014 | 56076890 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,513,585 | 0.006541 | 56076890 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,571 | 0.826998 | 56076890 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,458,000 | 1.373193 | 56076890 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,416,527 | 418.722894 | 56076890 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/AERO | 3000 | 1,272,467 | 3,768.984833 | 56076890 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,270,514 | 2,052.695995 | 56076890 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,228,060 | 15,026.871935 | 56076890 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,156,651 | 2,057.031170 | 56076890 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,126,871 | 2,058.118333 | 56076890 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,862 | 86.341789 | 56076890 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,044,435 | 33,332,866.804384 | 56076890 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,001,532 | 105.258037 | 56076890 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 962,392 | 21.226641 | 56076890 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 941,995 | 555,979.142364 | 56076890 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 919,326 | 0.001502 | 56076890 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome_slipstream | USDC/cbBTC | 340 | 911,018 | 0.000014 | 56076890 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 904,670 | 0.050785 | 56076890 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/TOSHI | 10000 | 902,600 | 23,083,926.203551 | 56076890 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 885,490 | 1,011.412344 | 56076890 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 878,134 | 2,050.503253 | 56076890 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 865,674 | 0.000000 | 56076890 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 770,384 | 79.253324 | 56076890 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 766,193 | 0.052388 | 56076890 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 758,414 | 22.554487 | 56076890 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 736,105 | 118,601.063634 | 56076890 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 710,704 | 3,796.845816 | 56076890 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 695,103 | 0.802938 | 56076890 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 673,985 | 0.539283 | 56076890 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 655,868 | 4,644,644.925936 | 56076890 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 622,790 | 0.488472 | 56076890 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 613,855 | 141,712.046585 | 56076890 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 589,569 | 0.000007 | 56076890 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 580,970 | 0.000260 | 56076890 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 578,909 | 552,730.228239 | 56076890 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 562,913 | 0.038032 | 56076890 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2706 | 494,810 | 1,011.182310 | 56076890 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 464,086 | 0.066823 | 56076890 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 458,002 | 0.492814 | 56076890 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 11 | 454,344 | 1.000808 | 56076890 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 442,410 | 24.594013 | 56076890 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 436,348 | 915,629.438825 | 56076890 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 2650 ; routes examinées : 41287000 ; candidats optimisés : 206817 ; net attendu > 0 : 250 ; dernier cycle 470.8 ms
- Rejets (moteur) : {'spread_below_threshold': 40340185, 'liquidity_below_min': 732908, 'negative_expected_net': 206567, 'borrow_bound_too_small': 5268, 'cycle_budget_exhausted': 1822}
- Enregistrements de la session : 206817 ; net attendu > 0 : 250 ; simulés (eth_call de la vraie tx) : 16 (ok 12, échec 4) ; étiquettes ghost N+1 : 13/13 positives
- Décisions : {'REJECTED': 206817} ; motifs de rejet : {'below_safety_margin': 207, 'negative_expected_net': 206567, 'p_lower_below_threshold': 246, 'reliability_not_demonstrated': 4, 'simulation_failed': 4, 'stale_data': 147}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56074333 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 1,417.541523 USDC | 0.167700 USDC | 0.000000 USDC | 0.004930 USDC | 0.162770 USDC (0.1497 €) | — | 1.15 | 0.100 (n=358) | REJECTED | below_safety_margin(162770<283508), stale_data(11063ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56074333 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.691457 WETH | 0.000082 WETH | 0.000000 WETH | 0.000002 WETH | 0.000079 WETH (0.1496 €) | — | 1.15 | 0.100 (n=358) | REJECTED | below_safety_margin(79268886025357<138291377737077), stale_data(11054ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56074333 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.291669 WETH | 0.000038 WETH | 0.000000 WETH | 0.000003 WETH | 0.000035 WETH (0.0660 €) | — | 1.20 | 0.263 (n=1562) | REJECTED | below_safety_margin(34962597040753<58333742637478), stale_data(10909ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 588.846026 USDC | 0.078366 USDC | 0.000000 USDC | 0.006803 USDC | 0.071563 USDC (0.0658 €) | — | 1.22 | 0.263 (n=1562) | REJECTED | below_safety_margin(71563<117769), stale_data(10920ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.007405 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0658 €) | — | 1.31 | 0.263 (n=1562) | REJECTED | below_safety_margin(97<148), stale_data(10897ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 488.192091 USDC | 0.060994 USDC | 0.000000 USDC | 0.004930 USDC | 0.056064 USDC (0.0516 €) | — | 1.15 | 0.100 (n=358) | REJECTED | below_safety_margin(56064<97638), stale_data(10991ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56074333 | WETH→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.238776 WETH | 0.000030 WETH | 0.000000 WETH | 0.000002 WETH | 0.000027 WETH (0.0515 €) | — | 1.14 | 0.100 (n=358) | REJECTED | below_safety_margin(27298970575731<47755249085870), stale_data(10983ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56074333 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.306740 WETH | 0.000028 WETH | 0.000000 WETH | 0.000003 WETH | 0.000025 WETH (0.0465 €) | — | 0.80 | 0.147 (n=41) | REJECTED | below_safety_margin(24617738065776<61348096760279), stale_data(11209ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 56074333 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC | 585.652182 USDC | 0.057050 USDC | 0.000000 USDC | 0.006803 USDC | 0.050247 USDC (0.0462 €) | — | 0.86 | 0.147 (n=41) | REJECTED | below_safety_margin(50247<117130), stale_data(11221ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 56074333 | cbBTC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.008451 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0461 €) | — | 0.80 | 0.147 (n=41) | REJECTED | below_safety_margin(68<169), stale_data(11196ms>4000.0), p_lower_below_threshold(0.15<0.75) |
| 56074333 | USDC→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 358.021609 USDC | 0.052443 USDC | 0.000000 USDC | 0.004618 USDC | 0.047825 USDC (0.0440 €) | — | 1.34 | 0.081 (n=113) | REJECTED | below_safety_margin(47825<71604), stale_data(10876ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56074333 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.174347 WETH | 0.000026 WETH | 0.000000 WETH | 0.000002 WETH | 0.000023 WETH (0.0440 €) | — | 1.34 | 0.081 (n=113) | REJECTED | below_safety_margin(23290782412628<34869335876803), stale_data(10871ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56074333 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC | 0.003784 cbBTC | 0.000001 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000001 cbBTC (0.0387 €) | — | 1.51 | 0.263 (n=1562) | REJECTED | below_safety_margin(57<75), stale_data(10787ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH | 0.147182 WETH | 0.000023 WETH | 0.000000 WETH | 0.000003 WETH | 0.000020 WETH (0.0385 €) | — | 1.38 | 0.263 (n=1562) | REJECTED | below_safety_margin(20383665579325<29436443254564), stale_data(10780ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | USDC→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 279.378957 USDC | 0.047931 USDC | 0.000000 USDC | 0.006180 USDC | 0.041751 USDC (0.0384 €) | — | 1.49 | 0.263 (n=1562) | REJECTED | below_safety_margin(41751<55875), stale_data(10794ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 263.045830 USDC | 0.040327 USDC | 0.000000 USDC | 0.004618 USDC | 0.035709 USDC (0.0329 €) | — | 1.36 | 0.081 (n=113) | REJECTED | below_safety_margin(35709<52609), stale_data(10854ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56074333 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.128941 WETH | 0.000020 WETH | 0.000000 WETH | 0.000002 WETH | 0.000017 WETH (0.0328 €) | — | 1.35 | 0.081 (n=113) | REJECTED | below_safety_margin(17388279876011<25788207762325), stale_data(10849ms>4000.0), p_lower_below_threshold(0.08<0.75) |
| 56049891 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.168890 WETH | 0.000017 WETH | 0.000000 WETH | 0.000003 WETH | 0.000014 WETH (0.0267 €) | — | 0.84 | 0.262 (n=1560) | REJECTED | below_safety_margin(14139452649186<33778000811495), stale_data(5505ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | cbBTC→[pancakeswap_v3]→USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC | 0.004526 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0265 €) | — | 0.86 | 0.262 (n=1560) | REJECTED | below_safety_margin(39<90), stale_data(5512ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 359.906777 USDC | 0.034977 USDC | 0.000000 USDC | 0.006210 USDC | 0.028767 USDC (0.0265 €) | — | 0.80 | 0.262 (n=1560) | REJECTED | below_safety_margin(28767<71981), stale_data(5520ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH | 0.125656 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0221 €) | — | 0.93 | 0.263 (n=1562) | REJECTED | below_safety_margin(11705727450796<25131251744432), stale_data(11031ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | USDC→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC | 235.108598 USDC | 0.029998 USDC | 0.000000 USDC | 0.006180 USDC | 0.023818 USDC (0.0219 €) | — | 1.01 | 0.263 (n=1562) | REJECTED | below_safety_margin(23818<47021), stale_data(11046ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56074333 | cbBTC→[pancakeswap_v3]→WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.003131 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0217 €) | — | 1.02 | 0.263 (n=1562) | REJECTED | below_safety_margin(32<62), stale_data(11038ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[aerodrome_slipstream]→WETH | 0.131279 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000011 WETH (0.0204 €) | — | 0.82 | 0.262 (n=1560) | REJECTED | below_safety_margin(10785261854409<26255881789766), stale_data(5478ms>4000.0), p_lower_below_threshold(0.26<0.75) |
| 56049891 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 279.774953 USDC | 0.027730 USDC | 0.000000 USDC | 0.006210 USDC | 0.021520 USDC (0.0198 €) | — | 0.77 | 0.262 (n=1560) | REJECTED | below_safety_margin(21520<55954), stale_data(5492ms>4000.0), p_lower_below_threshold(0.26<0.75) |

## Fiabilité et décision
- Observations ghost : 8070 ; taux observé 0.213 ; borne inférieure crédible (0.9) 0.208 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 20.8% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
