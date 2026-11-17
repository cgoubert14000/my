# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-17T15:51:48+00:00 ; durée 76.12 min ; blocs 58678790 → 58701625 (3768 vus)

## Connexion
- Requêtes RPC : 41787 ; erreurs : 0 ; latence p50/p95 : 477.3/1,289.3 ms
- Rafraîchissements d'état : 3768 ; âge des données au dernier bloc : 8.1 s ; changements de frais LP observés (pools à frais dynamiques) : 4765
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 11233 ; cycles déclenchés par événement : 2521 ; avance médiane sur le rafraîchissement multicall : 384 ms
- Gaz : base fee 0.007228 gwei ; prix ETH (pool le plus profond) : 1,758.58 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 440 pools, 254 jetons, 13260 routes
- Par DEX : uniswap_v3 131, aerodrome_slipstream 92, aerodrome 177, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 150 (rejetés 2) → 555 jetons ; pools candidats 3599 (énumérés 268, par paires 0), mesurés 442, sous le plancher de 10000.0 $ : 2 → gardés 440 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1818.856829, 'cbBTC': 64998.173708, 'AERO': 0.450056}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 87,699,894 | 1,758.582957 | 58701649 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/USDC | 500 | 23,336,410 | 1,754.889275 | 58701649 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,183,316 | 0.027655 | 58701649 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,678,812 | 0.027648 | 58701649 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,517,657 | 84.542432 | 58701649 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,774,180 | 0.000016 | 58701649 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,017,052 | 0.027665 | 58701649 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,673,049 | 2.291689 | 58701649 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,496,054 | 1,755.071407 | 58701649 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,346,796 | 0.999848 | 58701649 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,725,492 | 38,961.608985 | 58701649 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 720 | 2,381,455 | 1,755.141103 | 58701649 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,850,516 | 0.000016 | 58701649 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2605 | 1,727,254 | 0.027656 | 58701649 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,656,819 | 1,142,004.320152 | 58701649 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 600 | 1,478,104 | 0.000016 | 58701649 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,452,251 | 0.843423 | 58701649 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,352,934 | 0.000016 | 58701649 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,334,381 | 0.000000 | 58701649 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,241,273 | 0.006353 | 58701649 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,202,751 | 432.626034 | 58701649 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/SEND | 3000 | 1,059,590 | 86.549272 | 58701649 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,043,071 | 15,652.746441 | 58701649 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/VVV | 10000 | 1,030,586 | 84.552403 | 58701649 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome | WETH/USDC | 3000 | 1,022,867 | 1,758.843047 | 58701649 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/AERO | 3000 | 1,008,904 | 4,020.657520 | 58701649 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/VELVET | 100 | 995,201 | 19.222880 | 58701649 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v2 | WETH/USDC | 3000 | 986,673 | 1,759.203673 | 58701649 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | USDC/VVV | 3000 | 902,673 | 0.048133 | 58701649 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/doginme | 10000 | 902,269 | 33,032,997.722590 | 58701649 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 883,894 | 0.000000 | 58701649 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 821,901 | 526,169.176922 | 58701649 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | XDP/USDC | 100 | 792,979 | 0.017404 | 58701649 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/TOSHI | 10000 | 789,268 | 22,343,344.361317 | 58701649 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 785,685 | 0.001470 | 58701649 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 766,175 | 1,029.417632 | 58701649 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | USDC/NOCK | 3000 | 761,493 | 73.782616 | 58701649 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 710,143 | 1,771.014717 | 58701649 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | WETH/USDC | 500 | 709,874 | 1,754.962524 | 58701649 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | QUID/USDC | 100 | 708,619 | 0.044654 | 58701649 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4965 | 658,060 | 27.431037 | 58701649 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 100 | 629,613 | 1,755.118155 | 58701649 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 596,955 | 0.798721 | 58701649 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 587,362 | 0.433942 | 58701649 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/AERO | 10000 | 571,213 | 4,031.051431 | 58701649 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 557,360 | 4,730,975.191196 | 58701649 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | USDC/MAI (stable) | 3000 | 524,850 | 1.372316 | 58701649 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | WETH/BRETT | 3727 | 511,208 | 528,873.940031 | 58701649 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 503,392 | 155,071.509524 | 58701649 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | FLOCK/USDC | 3000 | 492,433 | 0.031139 | 58701649 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome | VIRTUAL/WETH | 10000 | 475,794 | 0.000241 | 58701649 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 460,472 | 0.000007 | 58701649 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | USDC/USDT | 11 | 454,932 | 1.000951 | 58701649 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| pancakeswap_v3 | ELSA/USDC | 100 | 423,132 | 0.059472 | 58701649 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | WETH/MORPHO | 3100 | 418,422 | 1,029.853556 | 58701649 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | USDC/MORPHO | 10000 | 391,300 | 0.581874 | 58701649 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 386,119 | 876,031.248744 | 58701649 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 386,084 | 24.733461 | 58701649 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 378,406 | 338.487378 | 58701649 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | WETH/msETH (stable) | 500 | 364,363 | 2.333236 | 58701649 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |

## Recherche d'opportunités
- Cycles : 6288 ; routes examinées : 83378880 ; candidats optimisés : 3186 ; net attendu > 0 : 0 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 81036987, 'liquidity_below_min': 1662299, 'borrow_bound_too_small': 6288, 'negative_expected_net': 3186}
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
