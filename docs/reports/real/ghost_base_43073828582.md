# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-11T18:43:59+00:00 ; durée 36.94 min ; blocs 56150210 → 56161266 (1782 vus)

## Connexion
- Requêtes RPC : 23785 ; erreurs : 30 ; latence p50/p95 : 127.1/1,587.2 ms
- Rafraîchissements d'état : 1782 ; âge des données au dernier bloc : 8.84 s ; changements de frais LP observés (pools à frais dynamiques) : 1468
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 3045 ; cycles déclenchés par événement : 944 ; avance médiane sur le rafraîchissement multicall : 406 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,090.88 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 462 pools, 267 jetons, 16678 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 100, aerodrome 187, pancakeswap_v3 27, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 161 (rejetés 2) → 566 jetons ; pools candidats 3639 (énumérés 284, par paires 0), mesurés 464, sous le plancher de 10000.0 $ : 2 → gardés 462 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2091.017157, 'cbBTC': 74374.029387, 'AERO': 0.55788}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 135,819,772 | 2,090.879197 | 56161296 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,673,492 | 0.028013 | 56161296 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,718,956 | 0.028050 | 56161296 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | USDC/cbBTC | 500 | 8,577,881 | 0.000013 | 56161296 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/USDC | 500 | 7,187,675 | 2,086.420213 | 56161296 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,071,946 | 101.847192 | 56161296 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,671,811 | 0.028006 | 56161296 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,303,582 | 1.799378 | 56161296 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 4,102,010 | 2,086.342841 | 56161296 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,932,880 | 0.998575 | 56161296 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,082,754 | 43,051.799990 | 56161296 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 138 | 2,941,652 | 2,086.142064 | 56161296 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,247,312 | 0.028063 | 56161296 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,987,956 | 1,121,348.046698 | 56161296 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 448 | 1,660,932 | 0.000013 | 56161296 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,634,757 | 0.000000 | 56161296 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,620,250 | 0.000013 | 56161296 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | XDP/USDC | 100 | 1,618,855 | 0.016339 | 56161296 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,541,755 | 0.000013 | 56161296 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,501,396 | 0.006366 | 56161296 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,464,753 | 0.828862 | 56161296 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,438,938 | 422.524892 | 56161296 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,438,232 | 1.405931 | 56161296 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,288,665 | 3,754.082969 | 56161296 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,282,195 | 2,091.029005 | 56161296 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,242,523 | 15,046.643989 | 56161296 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,167,241 | 2,091.994049 | 56161296 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,142,292 | 2,086.058993 | 56161296 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome | USDC/SEND | 3000 | 1,060,556 | 86.391696 | 56161296 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,057,548 | 33,778,785.269459 | 56161296 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/VVV | 10000 | 1,053,368 | 101.897619 | 56161296 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| aerodrome_slipstream | USDC/VELVET | 100 | 967,717 | 20.873596 | 56161296 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 957,587 | 558,918.447535 | 56161296 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 930,683 | 0.001498 | 56161296 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | USDC/VVV | 3000 | 928,985 | 0.048822 | 56161296 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 922,640 | 0.000013 | 56161296 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | WETH/TOSHI | 10000 | 919,622 | 23,053,289.280513 | 56161296 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| uniswap_v3 | WETH/MORPHO | 3000 | 893,835 | 1,023.806833 | 56161296 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 885,126 | 2,080.323257 | 56161296 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 869,550 | 0.000000 | 56161296 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | USDC/NOCK | 3000 | 779,316 | 77.447084 | 56161296 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| pancakeswap_v3 | QUID/USDC | 100 | 768,948 | 0.052780 | 56161296 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 756,197 | 22.647588 | 56161296 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| aerodrome | WETH/EDEL | 7000 | 744,166 | 120,355.005794 | 56161296 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | WETH/AERO | 10000 | 722,080 | 3,732.302618 | 56161296 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 708,392 | 0.801801 | 56161296 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 682,961 | 0.540083 | 56161296 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 669,271 | 4,626,603.291417 | 56161296 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 623,846 | 0.490044 | 56161296 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| uniswap_v2 | WETH/NPC | 3000 | 614,264 | 146,808.991400 | 56161296 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 1025 | 598,363 | 0.000007 | 56161296 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| aerodrome | VIRTUAL/WETH | 10000 | 590,664 | 0.000259 | 56161296 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2090 | 587,958 | 563,014.977324 | 56161296 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 566,883 | 0.038443 | 56161296 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2718 | 500,823 | 1,024.136633 | 56161296 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| pancakeswap_v3 | ELSA/USDC | 100 | 468,550 | 0.067641 | 56161296 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | USDC/MORPHO | 10000 | 459,966 | 0.490200 | 56161296 | `0x2043B296fFC6b2d3bf4A3F3167d2Afb3B0FBdbEE` |
| aerodrome_slipstream | USDC/USDT | 8 | 454,445 | 1.000640 | 56161296 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |
| uniswap_v3 | WETH/uSOL | 3000 | 450,226 | 24.625098 | 56161296 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 443,722 | 317.476230 | 56161296 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |

## Recherche d'opportunités
- Cycles : 2720 ; routes examinées : 45364160 ; candidats optimisés : 163557 ; net attendu > 0 : 109 ; dernier cycle 2278.1 ms
- Rejets (moteur) : {'spread_below_threshold': 44798670, 'liquidity_below_min': 395701, 'negative_expected_net': 163448, 'borrow_bound_too_small': 5394, 'cycle_budget_exhausted': 838}
- Enregistrements de la session : 163557 ; net attendu > 0 : 109 ; simulés (eth_call de la vraie tx) : 4 (ok 4, échec 0) ; étiquettes ghost N+1 : 0/4 positives
- Décisions : {'REJECTED': 163557} ; motifs de rejet : {'below_safety_margin': 94, 'negative_expected_net': 163448, 'p_lower_below_threshold': 109, 'stale_data': 32}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 56155469 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.128143 WETH | 0.000008 WETH | 0.000000 WETH | 0.000002 WETH | 0.000006 WETH (0.0118 €) | — | 0.48 | 0.104 (n=360) | REJECTED | below_safety_margin(6134935291529<25628564916203), p_lower_below_threshold(0.10<0.75) |
| 56155469 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 266.735383 USDC | 0.017544 USDC | 0.000000 USDC | 0.004724 USDC | 0.012820 USDC (0.0118 €) | — | 0.48 | 0.104 (n=360) | REJECTED | below_safety_margin(12820<53347), p_lower_below_threshold(0.10<0.75) |
| 56156957 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 178.563790 USDC | 0.017354 USDC | 0.000000 USDC | 0.006316 USDC | 0.011038 USDC (0.0102 €) | — | 0.62 | 0.164 (n=42) | REJECTED | below_safety_margin(11038<35712), p_lower_below_threshold(0.16<0.75) |
| 56156958 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 178.563790 USDC | 0.017354 USDC | 0.000000 USDC | 0.006316 USDC | 0.011038 USDC (0.0102 €) | — | 0.62 | 0.164 (n=42) | REJECTED | below_safety_margin(11038<35712), p_lower_below_threshold(0.16<0.75) |
| 56156957 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.095322 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0099 €) | — | 0.54 | 0.164 (n=42) | REJECTED | below_safety_margin(5142077366402<19064325969853), p_lower_below_threshold(0.16<0.75) |
| 56156958 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.095322 WETH | 0.000008 WETH | 0.000000 WETH | 0.000003 WETH | 0.000005 WETH (0.0099 €) | — | 0.54 | 0.164 (n=42) | REJECTED | below_safety_margin(5142077366402<19064325969853), p_lower_below_threshold(0.16<0.75) |
| 56156957 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002029 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0096 €) | — | 0.69 | 0.164 (n=42) | REJECTED | below_safety_margin(14<40), p_lower_below_threshold(0.16<0.75) |
| 56156958 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.002029 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0096 €) | — | 0.69 | 0.164 (n=42) | REJECTED | below_safety_margin(14<40), p_lower_below_threshold(0.16<0.75) |
| 56158255 | WETH→[pancakeswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.005327 WETH | 0.000007 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0067 €) | 0.000003 WETH | 6.56 | 0.203 (n=1218) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56158255 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 11.149646 USDC | 0.013606 USDC | 0.000000 USDC | 0.006311 USDC | 0.007295 USDC (0.0067 €) | — | 6.54 | 0.203 (n=1218) | REJECTED | p_lower_below_threshold(0.20<0.75) |
| 56158255 | WETH→[uniswap_v3]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.005200 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0060 €) | 0.000003 WETH | 6.01 | 0.311 (n=556) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56158255 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 10.796325 USDC | 0.012824 USDC | 0.000000 USDC | 0.006311 USDC | 0.006513 USDC (0.0060 €) | — | 6.03 | 0.311 (n=556) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56158628 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.078199 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 0.38 | 0.164 (n=42) | REJECTED | below_safety_margin(2987688879603<15639872176743), p_lower_below_threshold(0.16<0.75) |
| 56158627 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.078199 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0057 €) | — | 0.38 | 0.164 (n=42) | REJECTED | below_safety_margin(2986285681158<15639872176743), p_lower_below_threshold(0.16<0.75) |
| 56158628 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 161.660073 USDC | 0.012443 USDC | 0.000000 USDC | 0.006315 USDC | 0.006128 USDC (0.0056 €) | — | 0.38 | 0.164 (n=42) | REJECTED | below_safety_margin(6128<32332), p_lower_below_threshold(0.16<0.75) |
| 56158627 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 161.660073 USDC | 0.012443 USDC | 0.000000 USDC | 0.006318 USDC | 0.006125 USDC (0.0056 €) | — | 0.38 | 0.164 (n=42) | REJECTED | below_safety_margin(6125<32332), p_lower_below_threshold(0.16<0.75) |
| 56158255 | WETH→[aerodrome_slipstream]→USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH | 0.005112 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | 0.000003 WETH | 5.68 | 0.311 (n=556) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56158255 | USDC→[uniswap_v3]→SUP→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 10.608285 USDC | 0.012366 USDC | 0.000000 USDC | 0.006311 USDC | 0.006055 USDC (0.0056 €) | — | 5.71 | 0.311 (n=556) | REJECTED | p_lower_below_threshold(0.31<0.75) |
| 56158597 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.053251 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | — | 0.54 | 0.265 (n=1577) | REJECTED | below_safety_margin(2893192512167<10650224019242), p_lower_below_threshold(0.27<0.75) |
| 56158598 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.053251 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | — | 0.54 | 0.265 (n=1577) | REJECTED | below_safety_margin(2893192512167<10650224019242), p_lower_below_threshold(0.27<0.75) |
| 56158599 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.053251 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | — | 0.54 | 0.265 (n=1577) | REJECTED | below_safety_margin(2893192512167<10650224019242), p_lower_below_threshold(0.27<0.75) |
| 56158600 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.053251 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | — | 0.54 | 0.265 (n=1577) | REJECTED | below_safety_margin(2893192512167<10650224019242), stale_data(5147ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56158625 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH | 0.053251 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0056 €) | — | 0.54 | 0.265 (n=1577) | REJECTED | below_safety_margin(2889867637781<10650224019242), stale_data(7046ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56158625 | cbBTC→[pancakeswap_v3]→USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001275 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0055 €) | — | 0.63 | 0.265 (n=1577) | REJECTED | below_safety_margin(8<25), stale_data(7033ms>4000.0), p_lower_below_threshold(0.27<0.75) |
| 56158627 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.001823 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC (0.0055 €) | — | 0.44 | 0.164 (n=42) | REJECTED | below_safety_margin(8<36), p_lower_below_threshold(0.16<0.75) |

## Fiabilité et décision
- Observations ghost : 8168 ; taux observé 0.216 ; borne inférieure crédible (0.9) 0.211 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 21.1% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
