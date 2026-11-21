# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-21T13:20:52+00:00 ; durée 272.42 min ; blocs 60302631 → 60384356 (23393 vus)

## Connexion
- Requêtes RPC : 197546 ; erreurs : 0 ; latence p50/p95 : 288.2/934.5 ms
- Rafraîchissements d'état : 23393 ; âge des données au dernier bloc : 6.84 s ; changements de frais LP observés (pools à frais dynamiques) : 13479
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1964 ; cycles déclenchés par événement : 439 ; avance médiane sur le rafraîchissement multicall : 263 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 1,669.75 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 404 pools, 244 jetons, 11726 routes
- Par DEX : uniswap_v3 118, aerodrome 167, aerodrome_slipstream 83, pancakeswap_v3 25, uniswap_v2 9, sushiswap_v2 1, sushiswap_v3 1
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 144 (rejetés 2) → 549 jetons ; pools candidats 3598 (énumérés 249, par paires 0), mesurés 406, sous le plancher de 10000.0 $ : 2 → gardés 404 (max 1500) ; prix des hubs : {'USDbC': 1.0, 'USDC': 1.0, 'DAI': 1.0, 'WETH': 1623.656287, 'cbBTC': 57839.4348, 'AERO': 0.38139}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 79,404,627 | 1,669.754489 | 60384375 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 20,664,223 | 0.028215 | 60384375 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/USDC | 500 | 9,957,139 | 1,668.624961 | 60384375 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| uniswap_v3 | WETH/cbBTC | 3000 | 7,262,750 | 0.028253 | 60384375 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| aerodrome | WETH/VVV | 3000 | 6,675,104 | 72.691372 | 60384375 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | USDC/cbBTC | 500 | 4,492,583 | 0.000017 | 60384375 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 3,855,048 | 0.028221 | 60384375 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 3,292,468 | 2.567465 | 60384375 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,115,376 | 0.998945 | 60384375 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| pancakeswap_v3 | WETH/USDC | 100 | 2,978,715 | 1,669.166977 | 60384375 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 2,511,509 | 41,365.837903 | 60384375 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 115 | 2,168,793 | 1,669.090980 | 60384375 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,787,780 | 0.000017 | 60384375 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 1,650,976 | 0.028242 | 60384375 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,616,995 | 1,080,896.278600 | 60384375 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,454,114 | 0.844220 | 60384375 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,276,131 | 0.000000 | 60384375 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| aerodrome_slipstream | USDC/cbBTC | 436 | 1,273,767 | 0.000017 | 60384375 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,164,230 | 0.006282 | 60384375 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,106,998 | 0.000017 | 60384375 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 1,061,127 | 16.133880 | 60384375 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/SEND | 3000 | 1,059,445 | 86.572965 | 60384375 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 986,590 | 469.471727 | 60384375 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 969,655 | 1,670.089183 | 60384375 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| uniswap_v3 | WETH/VVV | 10000 | 967,780 | 73.103899 | 60384375 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | USDC/VVV | 3000 | 946,734 | 0.043596 | 60384375 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 944,481 | 16,664.175482 | 60384375 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/AERO | 3000 | 929,022 | 4,284.044712 | 60384375 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v3 | WETH/doginme | 10000 | 865,554 | 32,152,927.066490 | 60384375 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 781,397 | 523,453.817000 | 60384375 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 761,925 | 0.000000 | 60384375 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 752,578 | 22,367,090.918228 | 60384375 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 748,164 | 0.001539 | 60384375 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/NOCK | 3000 | 747,664 | 76.537179 | 60384375 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4565 | 737,594 | 23.717317 | 60384375 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| uniswap_v3 | XDP/USDC | 100 | 724,616 | 0.014710 | 60384375 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | WETH/MORPHO | 3000 | 709,158 | 1,062.133784 | 60384375 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| pancakeswap_v3 | QUID/USDC | 100 | 700,679 | 0.043640 | 60384375 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/USDC | 3000 | 697,309 | 1,669.320363 | 60384375 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | uXRP/WETH | 3000 | 668,022 | 0.000609 | 60384375 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| pancakeswap_v3 | WETH/USDC | 500 | 619,491 | 1,668.534632 | 60384375 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/wstETH | 3000 | 566,910 | 0.798424 | 60384375 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | TIG/USDC | 10000 | 556,786 | 0.390895 | 60384375 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v3 | WETH/USDC | 100 | 553,878 | 1,669.102665 | 60384375 | `0xb4CB800910B228ED3d0834cF79D697127BBB00e5` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 532,993 | 4,672,663.507469 | 60384375 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| aerodrome | WETH/AERO | 10000 | 508,560 | 4,255.581103 | 60384375 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | WETH/BRETT | 4037 | 487,279 | 527,207.876550 | 60384375 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 486,755 | 0.030571 | 60384375 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| pancakeswap_v3 | ELSA/USDC | 100 | 466,576 | 0.066999 | 60384375 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/USDC | 10000 | 456,411 | 1,659.588506 | 60384375 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v2 | WETH/NPC | 3000 | 438,462 | 184,781.830872 | 60384375 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | USDC/MAI (stable) | 3000 | 423,916 | 1.534987 | 60384375 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 414,464 | 0.000007 | 60384375 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/MORPHO | 3166 | 386,629 | 1,062.300523 | 60384375 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| uniswap_v3 | WETH/uSOL | 3000 | 380,764 | 21.286657 | 60384375 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 367,786 | 829,602.063178 | 60384375 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | AWE/USDC | 3000 | 361,449 | 0.054325 | 60384375 | `0xcb7f520d18141E36956fE0b3A6Bc3D4F11245521` |
| uniswap_v3 | WETH/UNI | 10000 | 353,201 | 369.720085 | 60384375 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | WETH/VVV | 2733 | 352,885 | 72.724611 | 60384375 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| uniswap_v3 | WETH/DEGEN | 3000 | 343,973 | 2,485,946.581509 | 60384375 | `0xc9034c3E7F58003E6ae0C8438e7c8f4598d5ACAA` |

## Recherche d'opportunités
- Cycles : 23831 ; routes examinées : 279442306 ; candidats optimisés : 37131 ; net attendu > 0 : 14 ; dernier cycle 0.0 ms
- Rejets (moteur) : {'spread_below_threshold': 273250563, 'liquidity_below_min': 3921693, 'negative_expected_net': 37117, 'borrow_bound_too_small': 23831}
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
