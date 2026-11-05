# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-05T05:46:16+00:00 ; durée 73.6 min ; blocs 53531902 → 53534111 (2187 vus)

## Connexion
- Requêtes RPC : 23464 ; erreurs : 0 ; latence p50/p95 : 305.5/1,588.1 ms
- Rafraîchissements d'état : 2187 ; âge des données au dernier bloc : 6.3 s ; changements de frais LP observés (pools à frais dynamiques) : 2867
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 0 ; cycles déclenchés par événement : 0 ; avance médiane sur le rafraîchissement multicall : — ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,423.45 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 500 pools, 288 jetons, 19590 routes
- Par DEX : uniswap_v3 143, aerodrome_slipstream 108, aerodrome 205, pancakeswap_v3 29, uniswap_v2 12, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 175 (rejetés 2) → 580 jetons ; pools candidats 3707 (énumérés 311, par paires 0), mesurés 503, sous le plancher de 10000.0 $ : 3 → gardés 500 (max 1500) ; prix des hubs : {'USDC': 1.0, 'USDbC': 1.0, 'DAI': 1.0, 'WETH': 2423.443645, 'cbBTC': 80372.656982, 'AERO': 0.644397}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 154,718,341 | 2,423.448069 | 53534112 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,316,407 | 0.030118 | 53534112 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,670,188 | 0.030091 | 53534112 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,285,660 | 0.000012 | 53534112 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 8,314,689 | 2,419.660379 | 53534112 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,816,653 | 112.398268 | 53534112 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,832,886 | 0.001560 | 53534112 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 5,398,631 | 0.030106 | 53534112 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 5,349,775 | 1.545271 | 53534112 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,415,350 | 2,418.692546 | 53534112 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,235,316 | 0.999062 | 53534112 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,682,957 | 40,521.849596 | 53534112 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 818 | 3,468,922 | 2,418.850506 | 53534112 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,749,956 | 0.030099 | 53534112 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 2,261,427 | 1,164,309.449368 | 53534112 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,868,442 | 0.007003 | 53534112 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/cbBTC | 532 | 1,825,524 | 0.000012 | 53534112 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,775,841 | 0.000000 | 53534112 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | XDP/USDC | 100 | 1,761,796 | 0.018111 | 53534112 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,687,349 | 0.000012 | 53534112 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,642,640 | 446.235521 | 53534112 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,554,083 | 0.000012 | 53534112 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,524,438 | 1.472013 | 53534112 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,483,612 | 3,742.546510 | 53534112 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,457,178 | 0.816347 | 53534112 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,425,723 | 2,419.665895 | 53534112 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | WETH/USDC | 3000 | 1,379,887 | 2,426.036509 | 53534112 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v2 | WETH/USDC | 3000 | 1,379,273 | 2,423.159228 | 53534112 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,347,292 | 14,808.422257 | 53534112 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| uniswap_v3 | WETH/doginme | 10000 | 1,187,041 | 37,372,295.285261 | 53534112 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome | USDC/SEND | 3000 | 1,151,294 | 73.310640 | 53534112 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | DRB/WETH | 10000 | 1,150,036 | 0.000000 | 53534112 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,108,783 | 560,991.868008 | 53534112 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 1,078,172 | 111.631213 | 53534112 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,067,204 | 23,018,393.135731 | 53534112 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 995,542 | 1,080.393257 | 53534112 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| aerodrome_slipstream | USDC/VELVET | 100 | 989,151 | 19.558253 | 53534112 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | USDC/NOCK | 3000 | 984,459 | 64.696877 | 53534112 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/cbBTC | 356 | 964,778 | 0.000012 | 53534112 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome | WETH/EDEL | 7000 | 957,235 | 97,773.851460 | 53534112 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| uniswap_v3 | WETH/USDC | 10000 | 957,097 | 2,419.823218 | 53534112 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | uXRP/WETH | 3000 | 918,214 | 0.000537 | 53534112 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| uniswap_v3 | USDC/VVV | 3000 | 866,163 | 0.046478 | 53534112 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome | WETH/AERO | 10000 | 859,521 | 3,767.676292 | 53534112 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4540 | 832,433 | 19.679860 | 53534112 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 824,228 | 0.061126 | 53534112 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 822,701 | 0.798911 | 53534112 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 750,734 | 0.594422 | 53534112 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 740,482 | 5,067,420.640730 | 53534112 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 740,108 | 135,468.986692 | 53534112 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 732,994 | 0.000247 | 53534112 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | AERO/cbBTC | 2700 | 695,787 | 0.000008 | 53534112 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 679,263 | 564,725.221565 | 53534112 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | TIG/USDC | 10000 | 671,890 | 0.570909 | 53534112 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/bsdETH | 100 | 650,346 | 0.914439 | 53534112 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome | WETH/msETH (stable) | 500 | 645,709 | 2.484153 | 53534112 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| pancakeswap_v3 | ELSA/USDC | 100 | 610,056 | 0.102600 | 53534112 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 603,646 | 0.090786 | 53534112 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| aerodrome | cbBTC/EDGE | 7000 | 587,609 | 792,379.306984 | 53534112 | `0x594b83709464A83F37aC77E69DDD447a8A33c0EE` |
| aerodrome | WETH/DRV | 3000 | 572,518 | 6,570.895309 | 53534112 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |

## Recherche d'opportunités
- Cycles : 2186 ; routes examinées : 42823740 ; candidats optimisés : 123879 ; net attendu > 0 : 9 ; dernier cycle 332.7 ms
- Rejets (moteur) : {'spread_below_threshold': 42323219, 'liquidity_below_min': 376628, 'negative_expected_net': 123870, 'cycle_budget_exhausted': 14}
- Enregistrements de la session : 123879 ; net attendu > 0 : 9 ; simulés (eth_call de la vraie tx) : 5 (ok 5, échec 0) ; étiquettes ghost N+1 : 0/5 positives
- Décisions : {'REJECTED': 123879} ; motifs de rejet : {'below_safety_margin': 4, 'negative_expected_net': 123870, 'p_lower_below_threshold': 9, 'stale_data': 2}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53533889 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 47.867526 USDC | 0.057843 USDC | 0.000000 USDC | 0.005441 USDC | 0.052402 USDC (0.0482 €) | 0.052402 USDC | 10.95 | 0.000 (n=83) | REJECTED | p_lower_below_threshold(0.00<0.75) |
| 53533483 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 26.495646 USDC | 0.017835 USDC | 0.000000 USDC | 0.005443 USDC | 0.012392 USDC (0.0114 €) | 0.012392 USDC | 4.68 | 0.031 (n=266) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53533641 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 23.857983 USDC | 0.014443 USDC | 0.000000 USDC | 0.005442 USDC | 0.009001 USDC (0.0083 €) | 0.009001 USDC | 3.77 | 0.031 (n=267) | REJECTED | p_lower_below_threshold(0.03<0.75) |
| 53532801 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 21.020314 USDC | 0.011264 USDC | 0.000000 USDC | 0.005450 USDC | 0.005814 USDC (0.0053 €) | 0.005814 USDC | 2.77 | 0.042 (n=215) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53533332 | USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC→[pancakeswap_v3]→USDC | 62.528905 USDC | 0.012954 USDC | 0.000000 USDC | 0.007282 USDC | 0.005672 USDC (0.0052 €) | — | 0.91 | 0.178 (n=915) | REJECTED | below_safety_margin(5672<12505), stale_data(4128ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53533332 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→AERO→[aerodrome_slipstream]→cbBTC | 0.000858 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0044 €) | — | 0.70 | 0.178 (n=915) | REJECTED | below_safety_margin(6<17), stale_data(4123ms>4000.0), p_lower_below_threshold(0.18<0.75) |
| 53532510 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 19.484318 USDC | 0.009709 USDC | 0.000000 USDC | 0.005500 USDC | 0.004209 USDC (0.0039 €) | 0.004209 USDC | 2.16 | 0.043 (n=214) | REJECTED | p_lower_below_threshold(0.04<0.75) |
| 53533562 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 17.226311 USDC | 0.007590 USDC | 0.000000 USDC | 0.005442 USDC | 0.002148 USDC (0.0020 €) | — | 1.25 | 0.042 (n=216) | REJECTED | below_safety_margin(2148<3445), p_lower_below_threshold(0.04<0.75) |
| 53532434 | USDC→[aerodrome_slipstream]→PLAY→[pancakeswap_v3]→USDC | 16.378652 USDC | 0.006727 USDC | 0.000000 USDC | 0.005522 USDC | 0.001205 USDC (0.0011 €) | — | 0.74 | 0.043 (n=214) | REJECTED | below_safety_margin(1205<3275), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 5311 ; taux observé 0.161 ; borne inférieure crédible (0.9) 0.155 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 15.5% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
