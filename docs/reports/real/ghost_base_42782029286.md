# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-10T13:01:16+00:00 ; durée 274.83 min ; blocs 55544026 → 55626441 (13765 vus)

## Connexion
- Requêtes RPC : 199111 ; erreurs : 80 ; latence p50/p95 : 160.0/889.2 ms
- Rafraîchissements d'état : 13765 ; âge des données au dernier bloc : 7.0 s ; changements de frais LP observés (pools à frais dynamiques) : 7679
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 17381 ; cycles déclenchés par événement : 5266 ; avance médiane sur le rafraîchissement multicall : 409 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,091.73 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 469 pools, 272 jetons, 17808 routes
- Par DEX : uniswap_v3 134, aerodrome_slipstream 102, aerodrome 191, pancakeswap_v3 28, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 166 (rejetés 2) → 571 jetons ; pools candidats 3655 (énumérés 290, par paires 0), mesurés 471, sous le plancher de 10000.0 $ : 2 → gardés 469 (max 1500) ; prix des hubs : {'USDC': 1.0, 'DAI': 1.0, 'USDbC': 1.0, 'WETH': 2115.286044, 'cbBTC': 74654.762075, 'AERO': 0.563979}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 138,235,391 | 2,091.734201 | 55626459 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 15,369,358 | 0.028216 | 55626459 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,240,343 | 0.000013 | 55626459 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 8,687,810 | 0.028193 | 55626459 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,402,646 | 2,096.327059 | 55626459 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 6,990,614 | 104.538408 | 55626459 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,736,750 | 0.028228 | 55626459 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome | USDC/AERO | 3000 | 4,374,178 | 1.782293 | 55626459 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,973,793 | 2,096.219218 | 55626459 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 3,895,330 | 1.000003 | 55626459 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome | WETH/KTA | 3000 | 3,078,819 | 43,197.629727 | 55626459 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/USDC | 150 | 2,976,289 | 2,096.287941 | 55626459 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,306,648 | 0.028179 | 55626459 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome | WETH/FAI | 10000 | 1,994,660 | 1,114,733.552638 | 55626459 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,689,731 | 0.000013 | 55626459 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| aerodrome_slipstream | USDC/cbBTC | 412 | 1,662,773 | 0.000013 | 55626459 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,618,521 | 0.016337 | 55626459 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,584,761 | 0.006803 | 55626459 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,527,297 | 0.000000 | 55626459 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,494,193 | 0.000013 | 55626459 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,458,542 | 0.821625 | 55626459 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,445,638 | 419.797656 | 55626459 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,424,441 | 1.429325 | 55626459 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| uniswap_v3 | WETH/AERO | 3000 | 1,286,236 | 3,736.208642 | 55626459 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| uniswap_v2 | WETH/USDC | 3000 | 1,282,270 | 2,091.627621 | 55626459 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,240,879 | 14,899.714408 | 55626459 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | WETH/USDC | 3000 | 1,211,030 | 2,092.118673 | 55626459 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| aerodrome | USDC/SEND | 3000 | 1,106,901 | 79.308890 | 55626459 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,070,052 | 2,096.328675 | 55626459 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| uniswap_v3 | WETH/doginme | 10000 | 1,042,680 | 35,522,037.412105 | 55626459 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| aerodrome_slipstream | USDC/VELVET | 100 | 955,592 | 21.694187 | 55626459 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| uniswap_v3 | WETH/BRETT | 10000 | 953,915 | 566,580.736900 | 55626459 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | WETH/VVV | 10000 | 938,849 | 104.109115 | 55626459 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 923,861 | 0.001496 | 55626459 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| uniswap_v3 | WETH/TOSHI | 10000 | 922,269 | 22,956,648.961954 | 55626459 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome_slipstream | USDC/cbBTC | 334 | 921,064 | 0.000013 | 55626459 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| uniswap_v3 | USDC/VVV | 3000 | 913,695 | 0.049872 | 55626459 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | WETH/MORPHO | 3000 | 894,398 | 1,037.584494 | 55626459 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 882,131 | 2,103.143966 | 55626459 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| uniswap_v3 | DRB/WETH | 10000 | 877,426 | 0.000000 | 55626459 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| aerodrome | WETH/EDEL | 7000 | 792,165 | 106,297.937641 | 55626459 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome | USDC/NOCK | 3000 | 788,848 | 75.586761 | 55626459 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| aerodrome_slipstream | USDC/SAPIEN | 4500 | 773,967 | 21.914815 | 55626459 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 759,499 | 0.051450 | 55626459 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/AERO | 10000 | 732,465 | 3,752.968754 | 55626459 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome | WETH/wstETH | 3000 | 710,129 | 0.798536 | 55626459 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 657,987 | 0.538536 | 55626459 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 648,477 | 4,925,705.251731 | 55626459 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v3 | TIG/USDC | 10000 | 647,901 | 0.527167 | 55626459 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 609,946 | 0.000008 | 55626459 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v2 | WETH/NPC | 3000 | 591,278 | 158,394.075405 | 55626459 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome | VIRTUAL/WETH | 10000 | 588,043 | 0.000256 | 55626459 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| aerodrome_slipstream | WETH/BRETT | 2096 | 583,915 | 562,617.474147 | 55626459 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| uniswap_v3 | FLOCK/USDC | 3000 | 565,555 | 0.038332 | 55626459 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |
| aerodrome_slipstream | WETH/MORPHO | 2700 | 504,349 | 1,037.315865 | 55626459 | `0xB5F0b4aE66C14F7EFaA9aA1468E8FC536A3E288c` |
| aerodrome | WETH/DRV | 3000 | 489,798 | 6,688.289775 | 55626459 | `0xaC4e562d7C6108f971321F14238E24AE2cC398ac` |
| pancakeswap_v3 | ELSA/USDC | 100 | 475,556 | 0.068983 | 55626459 | `0x83f3ACa29Bc79B048B99C56013475570acc97ccF` |
| uniswap_v3 | WETH/uSOL | 3000 | 460,520 | 24.811704 | 55626459 | `0xab04A352D4EC8d0F1812A4E5EBe7807Fa67acD48` |
| uniswap_v3 | WETH/UNI | 10000 | 455,924 | 300.551971 | 55626459 | `0xAb365f161Dd501473a1ff0D2ef0dCE94E7398839` |
| aerodrome_slipstream | USDC/USDT | 8 | 455,824 | 1.001105 | 55626459 | `0xa41Bc0AFfbA7Fd420d186b84899d7ab2aC57fcD1` |

## Recherche d'opportunités
- Cycles : 19030 ; routes examinées : 338886240 ; candidats optimisés : 1141871 ; net attendu > 0 : 2900 ; dernier cycle 109.1 ms
- Rejets (moteur) : {'spread_below_threshold': 332507324, 'liquidity_below_min': 5189008, 'negative_expected_net': 1138971, 'borrow_bound_too_small': 31204, 'pool_quarantined': 12042, 'cycle_budget_exhausted': 2804, 'unquotable': 1984, 'no_price_reference': 3}
- Enregistrements de la session : 1141871 ; net attendu > 0 : 2900 ; simulés (eth_call de la vraie tx) : 160 (ok 79, échec 81) ; étiquettes ghost N+1 : 43/134 positives
- Décisions : {'REJECTED': 1141871} ; motifs de rejet : {'below_safety_margin': 2078, 'negative_expected_net': 1138971, 'p_lower_below_threshold': 2810, 'reliability_not_demonstrated': 90, 'sim_below_estimate': 5, 'simulated_net_nonpositive': 4, 'simulation_failed': 81, 'stale_data': 531}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 55553397 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004454 USDC | 4.084311 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553404 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004454 USDC | 4.084311 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553388 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004456 USDC | 4.084309 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553408 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004456 USDC | 4.084309 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55553410 | USDC→[aerodrome]→OWB→[uniswap_v3]→USDC | 141.602055 USDC | 4.088765 USDC | 0.000000 USDC | 0.004456 USDC | 4.084309 USDC (3.7576 €) | — | 288.44 | 0.000 (n=20) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.143238 WETH | 0.000377 WETH | 0.000000 WETH | 0.000003 WETH | 0.000374 WETH (0.7285 €) | — | 26.13 | 0.024 (n=60) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 302.705180 USDC | 0.796992 USDC | 0.000000 USDC | 0.006358 USDC | 0.790634 USDC (0.7274 €) | — | 26.12 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.141890 WETH | 0.000376 WETH | 0.000000 WETH | 0.000003 WETH | 0.000372 WETH (0.7249 €) | — | 26.25 | 0.024 (n=60) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.142907 WETH | 0.000375 WETH | 0.000000 WETH | 0.000003 WETH | 0.000372 WETH (0.7239 €) | — | 26.03 | 0.024 (n=60) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 299.512996 USDC | 0.793121 USDC | 0.000000 USDC | 0.006358 USDC | 0.786763 USDC (0.7238 €) | — | 26.27 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 301.719894 USDC | 0.792032 USDC | 0.000000 USDC | 0.006358 USDC | 0.785674 USDC (0.7228 €) | — | 26.04 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[aerodrome_slipstream]→WETH | 0.139239 WETH | 0.000362 WETH | 0.000000 WETH | 0.000003 WETH | 0.000359 WETH (0.6982 €) | — | 25.77 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 294.039094 USDC | 0.764215 USDC | 0.000000 USDC | 0.006358 USDC | 0.757857 USDC (0.6972 €) | — | 25.77 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[uniswap_v3]→WETH | 0.134225 WETH | 0.000349 WETH | 0.000000 WETH | 0.000003 WETH | 0.000346 WETH (0.6726 €) | — | 25.75 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[uniswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 283.401363 USDC | 0.737190 USDC | 0.000000 USDC | 0.007000 USDC | 0.730190 USDC (0.6718 €) | — | 25.77 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | USDC→[sushiswap_v3]→WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC | 199.001047 USDC | 0.528660 USDC | 0.000000 USDC | 0.006358 USDC | 0.522302 USDC (0.4805 €) | — | 26.25 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55544129 | WETH→[pancakeswap_v3]→AAVE→[uniswap_v3]→USDC→[sushiswap_v3]→WETH | 0.094206 WETH | 0.000250 WETH | 0.000000 WETH | 0.000003 WETH | 0.000247 WETH (0.4804 €) | — | 26.20 | 0.024 (n=60) | REJECTED | p_lower_below_threshold(0.02<0.75) |
| 55554362 | WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.852088 WETH | 0.000233 WETH | 0.000000 WETH | 0.000003 WETH | 0.000230 WETH (0.4471 €) | — | 2.70 | 0.045 (n=32) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.05<0.75) |
| 55554362 | cbBTC→[pancakeswap_v3]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.022980 cbBTC | 0.000007 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000007 cbBTC (0.4466 €) | — | 2.83 | 0.045 (n=32) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55554362 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[pancakeswap_v3]→USDC | 1,842.186115 USDC | 0.491461 USDC | 0.000000 USDC | 0.007227 USDC | 0.484234 USDC (0.4455 €) | — | 2.63 | 0.045 (n=32) | REJECTED | p_lower_below_threshold(0.05<0.75) |
| 55554456 | cbBTC→[uniswap_v3]→USDC→[pancakeswap_v3]→cbBTC | 0.021712 cbBTC | 0.000006 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000006 cbBTC (0.4017 €) | — | 2.70 | 0.080 (n=332) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 55554456 | USDC→[pancakeswap_v3]→cbBTC→[uniswap_v3]→USDC | 1,613.871749 USDC | 0.440562 USDC | 0.000000 USDC | 0.005734 USDC | 0.434828 USDC (0.4000 €) | — | 2.69 | 0.080 (n=332) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.08<0.75) |
| 55554362 | cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC | 0.017153 cbBTC | 0.000005 cbBTC | 0.000000 cbBTC | 0.000000 cbBTC | 0.000005 cbBTC (0.3437 €) | — | 2.92 | 0.224 (n=1365) | REJECTED | p_lower_below_threshold(0.22<0.75) |
| 55554362 | WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.614147 WETH | 0.000180 WETH | 0.000000 WETH | 0.000003 WETH | 0.000177 WETH (0.3435 €) | — | 2.88 | 0.224 (n=1365) | REJECTED | simulation_failed:FlashRepaymentImpossible, p_lower_below_threshold(0.22<0.75) |
| 55554362 | USDC→[pancakeswap_v3]→WETH→[pancakeswap_v3]→cbBTC→[aerodrome_slipstream]→USDC | 1,323.954739 USDC | 0.379192 USDC | 0.000000 USDC | 0.007227 USDC | 0.371965 USDC (0.3422 €) | — | 2.81 | 0.224 (n=1365) | REJECTED | p_lower_below_threshold(0.22<0.75) |

## Fiabilité et décision
- Observations ghost : 7425 ; taux observé 0.190 ; borne inférieure crédible (0.9) 0.184 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 18.4% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
