# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T18:28:38+00:00 ; durée 21.59 min ; blocs 56150210 → 56156665 (769 vus)

## Connexion
- Requêtes RPC : 12766 ; erreurs : 30 ; latence p50/p95 : 159.3/1,703.6 ms
- Rafraîchissements d'état : 769 ; âge des données au dernier bloc : 9.17 s ; changements de frais LP observés (pools à frais dynamiques) : 824
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 2781 ; cycles déclenchés par événement : 879 ; avance médiane sur le rafraîchissement multicall : 391 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,090.88 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 462 pools, 267 jetons, 16678 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 100, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3639 (énumérés 284, par paires 0), mesurés 464, sous le plancher de 10000.0 $ : 2 → gardés 462 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2091.017157, 'cbBTC': 74374.029387, 'AERO': 0.55788}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 135,809,918 | 2,090.878407 | 56156691 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,671,181 | 0.028043 | 56156691 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,716,361 | 0.028050 | 56156691 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,572,180 | 0.000013 | 56156691 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,187,681 | 2,086.813060 | 56156691 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,053,888 | 102.369233 | 56156691 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,671,250 | 0.028031 | 56156691 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,308,217 | 1.796770 | 56156691 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,101,971 | 2,085.996397 | 56156691 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,928,691 | 0.998575 | 56156691 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,082,753 | 43,051.799990 | 56156691 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 216 | 2,941,547 | 2,086.029607 | 56156691 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,246,937 | 0.028063 | 56156691 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,987,955 | 1,121,348.046698 | 56156691 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,659,646 | 0.000013 | 56156691 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,619,006 | 0.000013 | 56156691 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,617,078 | 0.016311 | 56156691 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,590,921 | 0.000000 | 56156691 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,540,748 | 0.000013 | 56156691 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,510,698 | 0.006376 | 56156691 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,465,229 | 0.828374 | 56156691 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,439,309 | 422.141732 | 56156691 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,438,232 | 1.405931 | 56156691 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,290,380 | 3,751.609275 | 56156691 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,282,194 | 2,091.044174 | 56156691 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,242,266 | 15,021.650958 | 56156691 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,167,241 | 2,092.704372 | 56156691 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,142,280 | 2,087.049212 | 56156691 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56156691 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,057,547 | 33,778,785.269459 | 56156691 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,050,553 | 101.897600 | 56156691 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 969,292 | 20.771272 | 56156691 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 957,587 | 558,917.719069 | 56156691 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 929,748 | 0.001498 | 56156691 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 925,359 | 0.048967 | 56156691 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 332 | 921,746 | 0.000013 | 56156691 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 919,622 | 23,053,289.280513 | 56156691 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 894,242 | 1,022.881844 | 56156691 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 885,126 | 2,080.323257 | 56156691 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 870,101 | 0.000000 | 56156691 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 779,316 | 77.447084 | 56156691 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 768,948 | 0.052780 | 56156691 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 756,888 | 22.618787 | 56156691 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 744,166 | 120,355.005794 | 56156691 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 722,855 | 3,732.302618 | 56156691 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 707,890 | 0.802938 | 56156691 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 682,949 | 0.541243 | 56156691 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 666,451 | 4,665,730.979330 | 56156691 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 623,921 | 0.490064 | 56156691 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 616,162 | 145,904.379541 | 56156691 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 598,964 | 0.000007 | 56156691 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 590,664 | 0.000259 | 56156691 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2099 | 587,958 | 563,158.959065 | 56156691 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,883 | 0.038443 | 56156691 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2703 | 501,065 | 1,023.106390 | 56156691 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 470,349 | 0.067974 | 56156691 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 460,254 | 0.490200 | 56156691 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,448 | 1.000626 | 56156691 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 450,226 | 24.625098 | 56156691 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| aerodrome | cbBTC/EDGE | 7000 | 444,144 | 908,282.838332 | 56156691 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |

## Recherche d'opportunités
- Cycles : 1647 ; routes examinées : 27468666 ; candidats optimisés : 105164 ; net attendu > 0 : 10 ; dernier cycle 274.9 ms
- Rejets (moteur) : {'spread_below_threshold': 27127313, 'liquidity_below_min': 232723, 'negative_expected_net': 105154, 'borrow_bound_too_small': 3283, 'cycle_budget_exhausted': 183}
- Enregistrements de la session : 105164 ; net attendu > 0 : 10 ; simulés (eth_call de la vraie tx) : 0 (ok 0, échec 0) ; étiquettes ghost N+1 : 0/0 positives
- Décisions : {'REJECTED': 105164} ; motifs de rejet : {'below_safety_margin': 10, 'negative_expected_net': 105154, 'p_lower_below_threshold': 10, 'stale_data': 4}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56155469 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.128143 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0118 €) | — | 0.48 | 0.104 (n=360) | REJECTED | below_safety_margin(6134935291529<25628564916203), p_lower_below_threshold(0.10<0.75) |
| 56155469 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 266.735383 USDC | 0.017544 USDC | 0.000000 USDC | 0.004724 USDC | 0.012820 USDC (0.0118 €) | — | 0.48 | 0.104 (n=360) | REJECTED | below_safety_margin(12820<53347), p_lower_below_threshold(0.10<0.75) |
| 56155469 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→WETH | 0.046585 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0016 €) | — | 0.18 | 0.081 (n=113) | REJECTED | below_safety_margin(818139488322<9316945262116), p_lower_below_threshold(0.08<0.75) |
| 56155469 | USDC→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 95.985568 USDC | 0.006432 USDC | 0.000000 USDC | 0.004724 USDC | 0.001708 USDC (0.0016 €) | — | 0.18 | 0.081 (n=113) | REJECTED | below_safety_margin(1708<19197), p_lower_below_threshold(0.08<0.75) |
| 56153580 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.051378 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0015 €) | — | 0.15 | 0.104 (n=360) | REJECTED | below_safety_margin(764035565454<10275654213879), stale_data(4649ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56153580 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.051378 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0015 €) | — | 0.15 | 0.104 (n=360) | REJECTED | below_safety_margin(764035565454<10275654213879), stale_data(4991ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56153580 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 106.665273 USDC | 0.006303 USDC | 0.000000 USDC | 0.004711 USDC | 0.001592 USDC (0.0015 €) | — | 0.15 | 0.104 (n=360) | REJECTED | below_safety_margin(1592<21333), stale_data(4656ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56153580 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 106.665273 USDC | 0.006303 USDC | 0.000000 USDC | 0.004711 USDC | 0.001592 USDC (0.0015 €) | — | 0.15 | 0.104 (n=360) | REJECTED | below_safety_margin(1592<21333), stale_data(4999ms>4000.0), p_lower_below_threshold(0.10<0.75) |
| 56152452 | WETH→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.045326 WETH | 0.000003 WETH | 0.000000 WETH | 0.000002 WETH | 0.000001 WETH (0.0012 €) | — | 0.14 | 0.081 (n=113) | REJECTED | below_safety_margin(646975011998<9065164434799), p_lower_below_threshold(0.08<0.75) |
| 56152452 | USDC→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 93.908586 USDC | 0.006051 USDC | 0.000000 USDC | 0.004710 USDC | 0.001341 USDC (0.0012 €) | — | 0.14 | 0.081 (n=113) | REJECTED | below_safety_margin(1341<18781), p_lower_below_threshold(0.08<0.75) |

## Fiabilité et décision
- Observations ghost : 8164 ; taux observé 0.216 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
