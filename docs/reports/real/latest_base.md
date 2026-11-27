# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-27T09:54:37+00:00 ; durée 170.55 min ; blocs 62863321 → 62914485 (12913 vus)

## Connexion
- Requêtes RPC : 114235 ; erreurs : 72 ; latence p50/p95 : 764.5/1,554.9 ms
- Rafraîchissements d'état : 12913 ; âge des données au dernier bloc : 5.63 s ; changements de frais LP observés (pools à frais dynamiques) : 4306
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 13683 ; cycles déclenchés par événement : 6129 ; avance médiane sur le rafraîchissement multicall : 128 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,731.34 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 427 pools, 250 jetons, 12816 routes
- Par DEX : uniswap_v3 129, aerodrome 171, aerodrome_slipstream 89, pancakeswap_v3 26, uniswap_v2 10, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 147 (rejetés 2) → 552 jetons ; pools candidats 3594 (énumérés 258, par paires 0), mesurés 429, sous le plancher de 10000.0 $ : 2 → gardés 427 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 1734.50033, 'cbBTC': 61667.00593, 'AERO': 0.409237}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 96,768,671 | 1,731.340740 | 62914485 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 23,491,368 | 0.028063 | 62914485 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,605,373 | 0.028090 | 62914485 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,366,748 | 63.812608 | 62914485 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,304,542 | 1,729.238481 | 62914485 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,938,733 | 0.000016 | 62914485 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,136,188 | 0.028058 | 62914485 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,289,366 | 2.438263 | 62914485 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,246,734 | 0.999680 | 62914485 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,065,322 | 1,728.999456 | 62914485 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,703,963 | 38,367.701613 | 62914485 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 100 | 2,210,628 | 1,728.988224 | 62914485 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,983,638 | 0.000016 | 62914485 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,890,098 | 0.028080 | 62914485 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,661,513 | 1,100,661.201435 | 62914485 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,461,077 | 0.834779 | 62914485 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,314,774 | 0.000000 | 62914485 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 1,289,388 | 0.000016 | 62914485 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,255,013 | 10.738578 | 62914485 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,209,968 | 0.006145 | 62914485 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,143,910 | 0.000016 | 62914485 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/VVV | 3000 | 1,122,492 | 0.036864 | 62914485 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/SEND | 3000 | 1,061,587 | 86.223966 | 62914485 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,034,258 | 449.193693 | 62914485 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 1,023,201 | 63.833140 | 62914485 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,003,524 | 16,022.174436 | 62914485 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 988,367 | 1,731.529358 | 62914485 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 970,039 | 4,226.179079 | 62914485 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 903,666 | 31,506,286.460439 | 62914485 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 865,644 | 0.000000 | 62914485 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 807,925 | 20,930,770.794602 | 62914485 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 797,600 | 67.253703 | 62914485 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 795,473 | 551,293.905940 | 62914485 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 786,198 | 0.001564 | 62914485 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 776,671 | 1,035.970797 | 62914485 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | uXRP/WETH | 3000 | 699,827 | 0.000625 | 62914485 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/USDC | 3000 | 698,471 | 1,732.957541 | 62914485 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 697,041 | 25.789393 | 62914485 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 679,408 | 0.041157 | 62914485 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | XDP/USDC | 100 | 675,954 | 0.012970 | 62914485 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/USDC | 100 | 604,236 | 1,728.912585 | 62914485 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | WETH/USDC | 500 | 600,837 | 1,729.155235 | 62914485 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| pancakeswap_v3 | ELSA/USDC | 100 | 587,747 | 0.092323 | 62914485 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome | WETH/wstETH | 3000 | 587,198 | 0.800091 | 62914485 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 564,521 | 4,490,557.481822 | 62914485 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 560,726 | 0.394893 | 62914485 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/AERO | 10000 | 529,764 | 4,216.991152 | 62914485 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 508,782 | 0.030211 | 62914485 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| uniswap_v2 | WETH/NPC | 3000 | 493,742 | 157,444.872643 | 62914485 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 492,341 | 552,292.316853 | 62914485 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | WETH/USDC | 10000 | 466,472 | 1,734.192666 | 62914485 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 11 | 452,408 | 1.001519 | 62914485 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | USDC/MAI (stable) | 3000 | 443,218 | 1.386525 | 62914485 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 438,293 | 0.000007 | 62914485 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 408,155 | 1,035.888573 | 62914485 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 391,407 | 21.673204 | 62914485 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 381,019 | 356.287988 | 62914485 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | cbBTC/EDGE | 7000 | 380,520 | 839,487.122226 | 62914485 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 357,053 | 0.053011 | 62914485 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/DEGEN | 3000 | 349,223 | 2,542,893.459607 | 62914485 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 19041 ; routes examinées : 38448 ; candidats optimisés : 0 ; net attendu > 0 : 0 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 37482, 'liquidity_below_min': 693, 'borrow_bound_too_small': 3}
- Enregistrements de la session : 0 ; net attendu > 0 : 0 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {} ; motifs de rejet : {}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Fiabilité et décision
- Observations ghost : 8789 ; taux observé 0.233 ; borne inférieure crédible (0.9) 0.227 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 22.7% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
