# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-26T20:58:58+00:00 ; durée 76.14 min ; blocs 62658936 → 62681789 (4839 vus)

## Connexion
- Requêtes RPC : 47891 ; erreurs : 0 ; latence p50/p95 : 435.5/1,406.3 ms
- Rafraîchissements d'état : 4839 ; âge des données au dernier bloc : 5.0 s ; changements de frais LP observés (pools à frais dynamiques) : 1173
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3848 ; cycles déclenchés par événement : 1863 ; avance médiane sur le rafraîchissement multicall : 312 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,701.80 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 427 pools, 249 jetons, 13000 routes
- Par DEX : uniswap_v3 130, aerodrome 170, aerodrome_slipstream 89, pancakeswap_v3 26, uniswap_v2 10, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 146 (rejetés 2) → 551 jetons ; pools candidats 3593 (énumérés 257, par paires 0), mesurés 429, sous le plancher de 10000.0 $ : 2 → gardés 427 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 1700.825577, 'cbBTC': 60627.469342, 'AERO': 0.39835}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 95,377,357 | 1,701.800453 | 62681789 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 23,321,865 | 0.028055 | 62681789 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,482,752 | 0.028049 | 62681789 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 7,242,919 | 63.779744 | 62681789 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | WETH/USDC | 500 | 7,190,850 | 1,703.055069 | 62681789 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | USDC/cbBTC | 500 | 5,944,740 | 0.000016 | 62681789 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,981,636 | 0.028053 | 62681789 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,254,438 | 2.491708 | 62681789 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,193,159 | 0.998736 | 62681789 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,005,386 | 1,702.451974 | 62681789 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,664,587 | 38,173.289809 | 62681789 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 115 | 2,184,654 | 1,702.624398 | 62681789 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,944,569 | 0.000017 | 62681789 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,858,143 | 0.028059 | 62681789 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,634,584 | 1,098,750.125997 | 62681789 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,459,322 | 0.834601 | 62681789 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,289,032 | 0.000000 | 62681789 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 400 | 1,243,842 | 0.000016 | 62681789 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,212,491 | 11.615459 | 62681789 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,163,989 | 0.006128 | 62681789 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,136,489 | 0.000016 | 62681789 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/VVV | 3000 | 1,102,028 | 0.037462 | 62681789 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | USDC/SEND | 3000 | 1,061,564 | 86.227648 | 62681789 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,016,546 | 449.212206 | 62681789 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | WETH/VVV | 10000 | 986,669 | 63.443411 | 62681789 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 986,471 | 16,047.576922 | 62681789 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v2 | WETH/USDC | 3000 | 979,882 | 1,701.223378 | 62681789 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/AERO | 3000 | 961,628 | 4,241.978755 | 62681789 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 894,894 | 30,903,633.565203 | 62681789 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | DRB/WETH | 10000 | 865,087 | 0.000000 | 62681789 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 802,408 | 20,551,816.568224 | 62681789 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | USDC/NOCK | 3000 | 793,752 | 67.907345 | 62681789 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/BRETT | 10000 | 786,696 | 541,669.461958 | 62681789 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 766,831 | 0.001539 | 62681789 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/MORPHO | 3000 | 758,112 | 1,047.074077 | 62681789 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome | WETH/USDC | 3000 | 694,251 | 1,707.621128 | 62681789 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 693,949 | 25.942645 | 62681789 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 686,146 | 0.041921 | 62681789 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| uniswap_v3 | uXRP/WETH | 3000 | 683,884 | 0.000618 | 62681789 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | XDP/USDC | 100 | 668,986 | 0.012721 | 62681789 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | ELSA/USDC | 100 | 612,569 | 0.099783 | 62681789 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 100 | 605,090 | 1,702.405554 | 62681789 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| pancakeswap_v3 | WETH/USDC | 500 | 597,699 | 1,703.266969 | 62681789 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/wstETH | 3000 | 577,837 | 0.798292 | 62681789 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 565,768 | 0.401670 | 62681789 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 559,393 | 4,418,007.170887 | 62681789 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 519,565 | 4,264.898541 | 62681789 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| uniswap_v3 | FLOCK/USDC | 3000 | 501,522 | 0.029577 | 62681789 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 488,385 | 541,181.531051 | 62681789 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v2 | WETH/NPC | 3000 | 483,430 | 158,648.270082 | 62681789 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| uniswap_v3 | WETH/USDC | 10000 | 464,080 | 1,689.802071 | 62681789 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,534 | 1.001471 | 62681789 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome | USDC/MAI (stable) | 3000 | 443,218 | 1.386525 | 62681789 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 442,641 | 0.000007 | 62681789 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 398,215 | 1,048.412049 | 62681789 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 384,291 | 21.728243 | 62681789 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | USDC/REPPO | 3000 | 379,264 | 91.587262 | 62681789 | `0xdf7470b0Fc66F216aD687416958C115e72AaD1fb` |
| aerodrome | cbBTC/EDGE | 7000 | 373,223 | 847,257.314397 | 62681789 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/UNI | 10000 | 372,170 | 365.285619 | 62681789 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome | AWE/USDC | 3000 | 356,552 | 0.052863 | 62681789 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |

## Recherche d'opportunités
- Cycles : 6701 ; routes examinées : 87113000 ; candidats optimisés : 9877 ; net attendu > 0 : 0 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 85822172, 'liquidity_below_min': 928965, 'negative_expected_net': 9877, 'borrow_bound_too_small': 6701}
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
