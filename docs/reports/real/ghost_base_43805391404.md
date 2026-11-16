# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-16T06:06:56+00:00 ; durée 79.28 min ; blocs 58070361 → 58094166 (4217 vus)

## Connexion
- Requêtes RPC : 44468 ; erreurs : 190 ; latence p50/p95 : 455.6/1,430.7 ms
- Rafraîchissements d'état : 4217 ; âge des données au dernier bloc : 8.3 s ; changements de frais LP observés (pools à frais dynamiques) : 2566
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 6731 ; cycles déclenchés par événement : 2102 ; avance médiane sur le rafraîchissement multicall : 426 ms
- Gaz : base fee 0.005003 gwei ; prix ETH (pool le plus profond) : 1,811.18 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 434 pools, 253 jetons, 13190 routes
- Par DEX : uniswap_v3 128, aerodrome_slipstream 89, aerodrome 177, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 149 (rejetés 2) → 554 jetons ; pools candidats 3593 (énumérés 265, par paires 0), mesurés 436, sous le plancher de 10000.0 $ : 2 → gardés 434 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDC': 1.0, 'USDbC': 1.0, 'WETH': 1821.287183, 'cbBTC': 64792.015153, 'AERO': 0.418602}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 89,501,100 | 1,811.176461 | 58094190 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 17,155,542 | 0.028127 | 58094190 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,722,256 | 0.028057 | 58094190 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,492,275 | 90.644267 | 58094190 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 6,299,897 | 0.000016 | 58094190 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 5,843,453 | 1,811.282963 | 58094190 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,228,544 | 0.028133 | 58094190 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,933,730 | 1,811.124333 | 58094190 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | USDC/AERO | 3000 | 3,642,238 | 2.398185 | 58094190 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,388,444 | 0.999806 | 58094190 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 2,739,634 | 40,901.660826 | 58094190 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 131 | 2,447,694 | 1,811.271273 | 58094190 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2505 | 1,832,202 | 0.028069 | 58094190 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,701,642 | 1,148,367.853585 | 58094190 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | XDP/USDC | 100 | 1,662,984 | 0.017023 | 58094190 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| aerodrome_slipstream | USDC/cbBTC | 508 | 1,485,420 | 0.000016 | 58094190 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,456,853 | 0.841020 | 58094190 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,413,952 | 0.000000 | 58094190 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,307,875 | 0.006430 | 58094190 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,283,076 | 0.000016 | 58094190 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,231,575 | 440.764267 | 58094190 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,202,582 | 0.000016 | 58094190 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/SEND | 3000 | 1,061,498 | 86.238480 | 58094190 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,055,057 | 15,710.867603 | 58094190 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,039,147 | 1,812.731521 | 58094190 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | WETH/AERO | 3000 | 1,025,119 | 4,348.943757 | 58094190 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/VVV | 10000 | 1,009,660 | 90.815157 | 58094190 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v2 | WETH/USDC | 3000 | 1,001,117 | 1,811.432899 | 58094190 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| pancakeswap_v3 | WETH/USDC | 500 | 971,751 | 1,810.904278 | 58094190 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/VELVET | 100 | 967,611 | 20.886447 | 58094190 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/doginme | 10000 | 935,514 | 32,104,246.598593 | 58094190 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | USDC/VVV | 3000 | 877,368 | 0.049971 | 58094190 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/BRETT | 10000 | 839,502 | 539,306.645661 | 58094190 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 819,223 | 0.000000 | 58094190 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/MORPHO | 3000 | 815,114 | 1,042.553552 | 58094190 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/TOSHI | 10000 | 791,131 | 23,385,360.162870 | 58094190 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 789,625 | 0.001448 | 58094190 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/NOCK | 3000 | 723,296 | 89.908027 | 58094190 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | WETH/USDC | 10000 | 712,953 | 1,796.845964 | 58094190 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| pancakeswap_v3 | QUID/USDC | 100 | 685,661 | 0.041907 | 58094190 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 666,359 | 26.957295 | 58094190 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | WETH/USDC | 100 | 622,917 | 1,811.379548 | 58094190 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| aerodrome | WETH/wstETH | 3000 | 614,873 | 0.798558 | 58094190 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 595,301 | 0.445519 | 58094190 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 575,607 | 4,703,505.116121 | 58094190 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 566,676 | 4,347.574784 | 58094190 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | USDC/MAI (stable) | 3000 | 523,411 | 1.378857 | 58094190 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v2 | WETH/NPC | 3000 | 520,546 | 153,747.777185 | 58094190 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | WETH/BRETT | 3700 | 519,642 | 539,949.699382 | 58094190 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 500,443 | 0.444645 | 58094190 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| aerodrome | VIRTUAL/WETH | 10000 | 495,142 | 0.000246 | 58094190 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | FLOCK/USDC | 3000 | 483,768 | 0.030352 | 58094190 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,565 | 1.000671 | 58094190 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 450,627 | 0.000006 | 58094190 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3058 | 426,357 | 1,042.998273 | 58094190 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 413,011 | 0.057812 | 58094190 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 396,829 | 0.571854 | 58094190 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome | cbBTC/EDGE | 7000 | 387,850 | 891,577.398312 | 58094190 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| uniswap_v3 | WETH/uSOL | 3000 | 386,860 | 25.197117 | 58094190 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 378,071 | 352.478909 | 58094190 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 6318 ; routes examinées : 83334420 ; candidats optimisés : 1884 ; net attendu > 0 : 2 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 81381605, 'liquidity_below_min': 1536115, 'borrow_bound_too_small': 6318, 'negative_expected_net': 1882}
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
