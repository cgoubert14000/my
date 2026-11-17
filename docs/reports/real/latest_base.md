# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-17T02:04:53+00:00 ; durée 262.11 min ; blocs 58374920 → 58453553 (13121 vus)

## Connexion
- Requêtes RPC : 144241 ; erreurs : 0 ; latence p50/p95 : 422.8/1,588.8 ms
- Rafraîchissements d'état : 13121 ; âge des données au dernier bloc : 7.76 s ; changements de frais LP observés (pools à frais dynamiques) : 7493
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 13091 ; cycles déclenchés par événement : 5821 ; avance médiane sur le rafraîchissement multicall : 398 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,818.85 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 436 pools, 254 jetons, 13240 routes
- Par DEX : uniswap_v3 127, aerodrome_slipstream 92, aerodrome 177, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 151 (rejetés 2) → 556 jetons ; pools candidats 3608 (énumérés 268, par paires 0), mesurés 438, sous le plancher de 10000.0 $ : 2 → gardés 436 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1822.30502, 'cbBTC': 65274.105098, 'AERO': 0.438839}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 89,113,932 | 1,818.851353 | 58453577 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 20,745,880 | 1,822.631199 | 58453577 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,568,293 | 0.028117 | 58453577 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,908,095 | 0.028061 | 58453577 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,945,509 | 0.000015 | 58453577 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| aerodrome | WETH/VVV | 3000 | 6,564,322 | 89.418517 | 58453577 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,191,167 | 0.028126 | 58453577 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,034,170 | 1,823.080389 | 58453577 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 3,685,241 | 2.285123 | 58453577 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,405,298 | 0.998956 | 58453577 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,765,398 | 40,484.012250 | 58453577 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 224 | 2,454,274 | 1,823.094962 | 58453577 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,801,460 | 0.028075 | 58453577 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,717,812 | 1,136,420.732051 | 58453577 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,630,157 | 0.016517 | 58453577 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 544 | 1,498,269 | 0.000015 | 58453577 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,082 | 0.842570 | 58453577 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,381,351 | 0.000000 | 58453577 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,378,417 | 0.000015 | 58453577 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,298,006 | 0.006342 | 58453577 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,238,680 | 438.704517 | 58453577 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,214,628 | 0.000015 | 58453577 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,062,072 | 15,614.038488 | 58453577 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,060,353 | 86.424836 | 58453577 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome | WETH/USDC | 3000 | 1,041,335 | 1,821.298152 | 58453577 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/VVV | 10000 | 1,031,930 | 89.746997 | 58453577 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/AERO | 3000 | 1,021,451 | 4,165.665286 | 58453577 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,003,327 | 1,822.216416 | 58453577 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | USDC/VELVET | 100 | 996,993 | 19.123167 | 58453577 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/doginme | 10000 | 932,468 | 32,904,714.021319 | 58453577 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 912,534 | 0.000000 | 58453577 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | USDC/VVV | 3000 | 889,097 | 0.049084 | 58453577 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/NOCK | 3000 | 849,458 | 65.184859 | 58453577 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 847,620 | 532,325.965052 | 58453577 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/MORPHO | 3000 | 805,410 | 1,037.969024 | 58453577 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/TOSHI | 10000 | 800,744 | 23,523,483.996982 | 58453577 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 795,026 | 0.001455 | 58453577 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/USDC | 500 | 768,651 | 1,822.466893 | 58453577 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/USDC | 10000 | 717,887 | 1,819.464844 | 58453577 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | QUID/USDC | 100 | 702,449 | 0.043892 | 58453577 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4570 | 662,491 | 27.180956 | 58453577 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 100 | 624,522 | 1,822.995170 | 58453577 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 617,431 | 0.798682 | 58453577 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 592,254 | 0.440966 | 58453577 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/AERO | 10000 | 581,758 | 4,189.716596 | 58453577 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 571,359 | 4,815,022.282448 | 58453577 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome_slipstream | WETH/BRETT | 3715 | 525,506 | 533,310.816560 | 58453577 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | USDC/MAI (stable) | 3000 | 524,850 | 1.372316 | 58453577 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 522,341 | 154,052.200628 | 58453577 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 493,259 | 0.000242 | 58453577 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | FLOCK/USDC | 3000 | 491,963 | 0.031102 | 58453577 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 486,552 | 0.439086 | 58453577 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 463,583 | 0.000007 | 58453577 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,819 | 1.000737 | 58453577 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | WETH/MORPHO | 3034 | 430,119 | 1,038.136833 | 58453577 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 420,482 | 0.059049 | 58453577 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 400,216 | 0.574380 | 58453577 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 389,694 | 885,747.379368 | 58453577 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 388,793 | 25.145254 | 58453577 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | WETH/msETH (stable) | 500 | 379,071 | 2.332806 | 58453577 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 18941 ; routes examinées : 249626960 ; candidats optimisés : 7413 ; net attendu > 0 : 0 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 244200968, 'liquidity_below_min': 4111136, 'borrow_bound_too_small': 18854, 'negative_expected_net': 7413}
- Enregistrements de la session : 0 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {} ; motifs de rejet : {}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Fiabilité et décision
- Observations ghost : 8573 ; taux observé 0.227 ; borne inférieure crédible (0.9) 0.221 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
