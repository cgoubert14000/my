# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-07T07:53:00+00:00 ; durée 24.48 min ; blocs 54230643 → 54237978 (1246 vus)

## Connexion
- Requêtes RPC : 16040 ; erreurs : 75 ; latence p50/p95 : 333.8/1,678.4 ms
- Rafraîchissements d'état : 1246 ; âge des données au dernier bloc : 9.22 s ; changements de frais LP observés (pools à frais dynamiques) : 293
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 811 ; cycles déclenchés par événement : 360 ; avance médiane sur le rafraîchissement multicall : 400 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,241.23 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 476 pools, 279 jetons, 17784 routes
- Par DEX : uniswap_v3 135, aerodrome_slipstream 99, aerodrome 198, pancakeswap_v3 29, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 3
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 170 (rejetés 2) → 575 jetons ; pools candidats 3720 (énumérés 295, par paires 0), mesurés 479, sous le plancher de 10000.0 $ : 3 → gardés 476 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 2241.234025, 'cbBTC': 75952.6335, 'AERO': 0.608777}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 145,996,868 | 2,241.233960 | 54238006 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,802,881 | 0.029527 | 54238006 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,327,357 | 0.000013 | 54238006 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,173,298 | 0.029513 | 54238006 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 8,021,631 | 2,243.282383 | 54238006 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,398,094 | 107.251647 | 54238006 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,428,368 | 0.001553 | 54238006 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 4,886,680 | 1.643825 | 54238006 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,768,986 | 0.029521 | 54238006 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,228,133 | 2,244.177114 | 54238006 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,000,625 | 0.998507 | 54238006 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,316,959 | 42,727.676186 | 54238006 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 3,204,254 | 2,244.154611 | 54238006 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,562,184 | 0.029528 | 54238006 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,098,060 | 1,156,736.421986 | 54238006 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,742,424 | 0.000013 | 54238006 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,705,776 | 0.006780 | 54238006 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,660,209 | 0.000000 | 54238006 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,632,435 | 0.000013 | 54238006 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,618,620 | 0.016160 | 54238006 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,545,442 | 1.431595 | 54238006 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,532,826 | 434.133968 | 54238006 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,509,146 | 0.000013 | 54238006 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,460,378 | 0.819350 | 54238006 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,391,423 | 3,686.085509 | 54238006 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,326,726 | 2,245.843789 | 54238006 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | WETH/USDC | 3000 | 1,325,173 | 2,249.533444 | 54238006 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,276,032 | 14,693.464833 | 54238006 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,192,696 | 2,243.282383 | 54238006 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,123,702 | 76.955062 | 54238006 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,111,046 | 36,091,326.806861 | 54238006 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,050,456 | 107.127048 | 54238006 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,027,479 | 557,560.280946 | 54238006 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,001,740 | 0.000000 | 54238006 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 998,655 | 22,522,526.287595 | 54238006 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/VELVET | 100 | 985,755 | 19.754406 | 54238006 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/MORPHO | 3000 | 941,692 | 1,059.034289 | 54238006 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 937,846 | 2,228.788739 | 54238006 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/cbBTC | 342 | 926,801 | 0.000013 | 54238006 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | USDC/NOCK | 3000 | 915,815 | 74.712357 | 54238006 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome | WETH/EDEL | 7000 | 881,529 | 98,605.174214 | 54238006 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | USDC/VVV | 3000 | 811,841 | 0.047831 | 54238006 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 801,391 | 3,680.501020 | 54238006 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 799,839 | 20.897311 | 54238006 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 790,856 | 0.055972 | 54238006 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 760,330 | 0.799699 | 54238006 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 720,858 | 0.569273 | 54238006 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 697,754 | 4,882,610.985388 | 54238006 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | VIRTUAL/WETH | 10000 | 685,335 | 0.000253 | 54238006 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | TIG/USDC | 10000 | 671,668 | 0.565228 | 54238006 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 660,660 | 145,479.938352 | 54238006 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 657,270 | 0.000008 | 54238006 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 630,652 | 558,042.164898 | 54238006 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/msETH (stable) | 500 | 588,883 | 2.473403 | 54238006 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| uniswap_v3 | FLOCK/USDC | 3000 | 578,442 | 0.039876 | 54238006 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 529,039 | 1,058.637919 | 54238006 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 525,598 | 0.078716 | 54238006 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | cbBTC/EDGE | 7000 | 523,733 | 895,564.580693 | 54238006 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/USDC | 100 | 515,814 | 2,244.210647 | 54238006 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/DRV | 3000 | 514,479 | 6,959.444540 | 54238006 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 1605 ; routes examinées : 28543320 ; candidats optimisés : 61069 ; net attendu > 0 : 2 ; dernier cycle 97.7 ms
- Rejets (moteur) : {'spread_below_threshold': 28267230, 'liquidity_below_min': 213345, 'negative_expected_net': 61067, 'borrow_bound_too_small': 1603, 'cycle_budget_exhausted': 73}
- Enregistrements de la session : 61069 ; net attendu > 0 : 2 ; simulés (eth_call de la vraie tx) : 2 (ok 1, échec 1) ; étiquettes ghost N+1 : 0/1 positives
- Décisions : {'REJECTED': 61069} ; motifs de rejet : {'negative_expected_net': 61067, 'p_lower_below_threshold': 2, 'simulation_failed': 1}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | 0.009649 USDC | 4.10 | 0.025 (n=328) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 54231076 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.543309 USDC | 0.014681 USDC | 0.000000 USDC | 0.005032 USDC | 0.009649 USDC (0.0089 €) | — | 4.10 | 0.025 (n=328) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.03<0.75) |

## Fiabilité et décision
- Observations ghost : 5956 ; taux observé 0.160 ; borne inférieure crédible (0.9) 0.154 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
