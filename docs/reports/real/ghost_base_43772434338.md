# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-16T00:43:11+00:00 ; durée 94.47 min ; blocs 57968703 → 57997014 (4575 vus)

## Connexion
- Requêtes RPC : 46627 ; erreurs : 0 ; latence p50/p95 : 564.5/4,267.2 ms
- Rafraîchissements d'état : 4575 ; âge des données au dernier bloc : 13.71 s ; changements de frais LP observés (pools à frais dynamiques) : 3731
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 10116 ; cycles déclenchés par événement : 2772 ; avance médiane sur le rafraîchissement multicall : 384 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,814.57 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 436 pools, 254 jetons, 13240 routes
- Par DEX : uniswap_v3 130, aerodrome_slipstream 89, aerodrome 177, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 150 (rejetés 2) → 555 jetons ; pools candidats 3595 (énumérés 266, par paires 0), mesurés 439, sous le plancher de 10000.0 $ : 3 → gardés 436 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 1832.787355, 'cbBTC': 65216.094643, 'AERO': 0.438974}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 86,794,224 | 1,814.571997 | 57997014 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,123,899 | 0.027953 | 57997014 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,738,233 | 0.028023 | 57997014 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,515,213 | 90.344929 | 57997014 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,399,943 | 0.000015 | 57997014 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 5,847,423 | 1,810.630935 | 57997014 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,175,118 | 0.027943 | 57997014 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,745,541 | 1,810.022102 | 57997014 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 3,648,078 | 2.390513 | 57997014 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,415,952 | 0.999800 | 57997014 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,780,264 | 39,863.993686 | 57997014 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 293 | 2,456,544 | 1,810.643873 | 57997014 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2550 | 1,831,793 | 0.028006 | 57997014 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,708,274 | 1,143,745.550485 | 57997014 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,685,866 | 0.017407 | 57997014 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,501,113 | 0.000015 | 57997014 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,160 | 0.842105 | 57997014 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,418,307 | 0.000000 | 57997014 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,329,969 | 0.006618 | 57997014 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,288,707 | 0.000015 | 57997014 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,233,352 | 441.363640 | 57997014 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,209,562 | 0.000015 | 57997014 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/SEND | 3000 | 1,061,398 | 86.254682 | 57997014 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,059,997 | 15,767.827305 | 57997014 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,040,120 | 1,815.129490 | 57997014 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/AERO | 3000 | 1,018,150 | 4,330.490765 | 57997014 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 1,005,660 | 89.766064 | 57997014 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 1,002,013 | 1,815.049632 | 57997014 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 974,576 | 20.440519 | 57997014 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| pancakeswap_v3 | WETH/USDC | 500 | 972,794 | 1,810.587171 | 57997014 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 938,875 | 32,100,562.945678 | 57997014 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 863,977 | 0.049873 | 57997014 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/BRETT | 10000 | 840,894 | 539,639.944917 | 57997014 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/MORPHO | 3000 | 818,178 | 1,039.130078 | 57997014 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | DRB/WETH | 10000 | 815,962 | 0.000000 | 57997014 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 795,674 | 0.001447 | 57997014 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 793,582 | 23,337,287.804195 | 57997014 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 721,725 | 90.299826 | 57997014 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 714,701 | 1,823.270659 | 57997014 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | QUID/USDC | 100 | 707,947 | 0.044578 | 57997014 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4545 | 671,560 | 26.677023 | 57997014 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 100 | 626,802 | 1,810.282460 | 57997014 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 616,026 | 0.798557 | 57997014 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 606,689 | 0.462098 | 57997014 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 576,168 | 4,711,597.511422 | 57997014 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 568,120 | 4,306.046019 | 57997014 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/NPC | 3000 | 531,520 | 148,003.834108 | 57997014 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | USDC/MAI (stable) | 3000 | 523,411 | 1.378857 | 57997014 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3784 | 520,434 | 537,003.240571 | 57997014 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 502,488 | 0.448807 | 57997014 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 496,070 | 0.000246 | 57997014 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | FLOCK/USDC | 3000 | 486,285 | 0.030588 | 57997014 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 452,600 | 0.000006 | 57997014 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/USDT | 8 | 452,381 | 1.000547 | 57997014 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 427,893 | 1,039.156162 | 57997014 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 418,654 | 0.058754 | 57997014 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 398,457 | 0.570826 | 57997014 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 389,931 | 893,440.669603 | 57997014 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 389,020 | 25.036464 | 57997014 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | WETH/msETH (stable) | 500 | 378,899 | 2.326238 | 57997014 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 7346 ; routes examinées : 97261040 ; candidats optimisés : 3257 ; net attendu > 0 : 0 ; dernier cycle 1768.8 ms
- Rejets (moteur) : {'spread_below_threshold': 95084189, 'liquidity_below_min': 1582250, 'borrow_bound_too_small': 7346, 'negative_expected_net': 3257, 'cycle_budget_exhausted': 294}
- Enregistrements de la session : 3 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 3} ; motifs de rejet : {'negative_expected_net': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

_Aucun candidat à net positif. Les 10 plus proches de la rentabilité (net attendu négatif) :_

| Bloc | Route | Montant | Brut | Frais flash | Gaz (dont L1) | Net attendu (€) | Marge (bps) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 57994301 | cbBTC→[aerodrome]→tBTC→[uniswap_v3]→cbBTC | 0.000015 cbBTC | -0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | -0.0036 | -39.14 |
| 57993473 | USDC→[pancakeswap_v3]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.000392 USDC | 0.000000 USDC | 0.005255 USDC | -0.0052 | -56.47 |
| 57994301 | USDC→[aerodrome_slipstream]→cbBTC→[aerodrome]→tBTC→[aerodrome_slipstream]→USDC | 0.999999 USDC | -0.002988 USDC | 0.000000 USDC | 0.005264 USDC | -0.0076 | -82.52 |

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
