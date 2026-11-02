# Session ghost — Base (chain id 8453)

**Réseau réel** — RPC `base-rpc.publicnode.com` — adresses vérifiées en direct : True
Généré le 2026-11-02T14:47:13+00:00 ; durée 3.03 min ; blocs 53420649 → 53420743 (92 vus)

## Connexion
- Requêtes RPC : 1112 ; erreurs : 0 ; latence p50/p95 : 127.8/1,472.7 ms
- Rafraîchissements d'état : 93 ; âge des données au dernier bloc : 0.51 s ; changements de frais LP observés (pools à frais dynamiques) : 209
- Flux d'événements (WebSocket Swap/Sync) : connecté ; événements appliqués : 1477 ; cycles déclenchés par événement : 132 ; avance médiane sur le rafraîchissement multicall : 409 ms
- Gaz : base fee 0.005000 gwei ; prix ETH (pool le plus profond) : 2,287.70 $
- Fournisseurs de flash loan : MORPHO 0.0 bps (vérifié=True), BALANCER_V2 0.0 bps (vérifié=True), AAVE_V3 5.0 bps (vérifié=True)

## Univers suivi : 494 pools, 286 jetons, 18656 routes
- Par DEX : uniswap_v3 138, aerodrome_slipstream 108, aerodrome 204, pancakeswap_v3 30, uniswap_v2 11, sushiswap_v2 1, sushiswap_v3 2
- Découverte : jetons config 7 + listes publiques 400 + énumération des factories 174 (rejetés 2) → 579 jetons ; pools candidats 3706 (énumérés 310, par paires 0), mesurés 497, sous le plancher de 10000.0 $ : 3 → gardés 494 (max 1500) ; prix des hubs : {'DAI': 1.0, 'USDbC': 1.0, 'USDC': 1.0, 'WETH': 2287.70349, 'cbBTC': 77760.832568, 'AERO': 0.623017}
- Pools en quarantaine : 0

## Pools les plus profonds (150 affichés) — état au bloc indiqué

| DEX | Paire | Frais (ppm) | Profondeur ($) | Prix (token1 par token0) | Bloc | Adresse |
|---|---|---:|---:|---:|---:|---|
| uniswap_v3 | WETH/USDC | 3000 | 151,640,321 | 2,287.703491 | 53420743 | `0x6c561B446416E1A00E8E93E221854d6eA4171372` |
| uniswap_v3 | WETH/cbBTC | 500 | 16,379,430 | 0.029411 | 53420743 | `0x7AeA2E8A3843516afa07293a10Ac8E49906dabD1` |
| uniswap_v3 | USDC/cbBTC | 500 | 9,281,628 | 0.000013 | 53420743 | `0xfBB6Eed8e7aa03B138556eeDaF5D271A5E1e43ef` |
| uniswap_v3 | WETH/cbBTC | 3000 | 9,211,357 | 0.029363 | 53420743 | `0x8c7080564B5A792A33Ef2FD473fbA6364d5495e5` |
| uniswap_v3 | WETH/USDC | 500 | 7,964,367 | 2,289.731698 | 53420743 | `0xd0b53D9277642d899DF5C87A3966A349A798F224` |
| aerodrome | WETH/VVV | 3000 | 7,735,703 | 103.188231 | 53420743 | `0x01784ef301D79e4B2DF3a21ad9a536d4cF09A5Ce` |
| uniswap_v3 | JITOSOL/cbBTC | 100 | 6,657,087 | 0.001586 | 53420743 | `0xe2B8c33AE97658ceaD06AfD47c7F3857e5851871` |
| aerodrome | USDC/AERO | 3000 | 5,471,681 | 1.605324 | 53420743 | `0x6cDcb1C4A4D1C3C6d054b27AC5B77e89eAFb971d` |
| pancakeswap_v3 | WETH/cbBTC | 100 | 4,783,383 | 0.029421 | 53420743 | `0xC211e1f853A898Bd1302385CCdE55f33a8C4B3f3` |
| aerodrome_slipstream | cbBTC/LBTC | 200 | 4,091,844 | 0.999940 | 53420743 | `0xA44D3Bb767d953711EA4Bce8C0F01f4d7D299aF6` |
| aerodrome_slipstream | WETH/USDC | 150 | 4,054,992 | 2,289.600811 | 53420743 | `0xb2cc224c1c9feE385f8ad6a55b4d94E92359DC59` |
| pancakeswap_v3 | WETH/USDC | 100 | 3,993,779 | 2,289.264108 | 53420743 | `0x72AB388E2E2F6FaceF59E3C3FA2C4E29011c2D38` |
| aerodrome | WETH/KTA | 3000 | 3,557,415 | 38,704.142431 | 53420743 | `0xd9eDC75a3a797Ec92Ca370F19051BAbebfb2edEe` |
| aerodrome_slipstream | WETH/cbBTC | 2500 | 2,673,352 | 0.029376 | 53420743 | `0x70aCDF2Ad0bf2402C957154f944c19Ef4e1cbAE1` |
| aerodrome_slipstream | WETH/VVV | 2718 | 2,348,897 | 103.214825 | 53420743 | `0x7eC6C9D993D9832Aa654593f2Dbc21303650Bc6c` |
| aerodrome | WETH/FAI | 10000 | 2,225,675 | 1,071,137.708557 | 53420743 | `0x5447F7FE76894d98753A0A6d69B9cb840037c13D` |
| aerodrome_slipstream | USDC/cbBTC | 424 | 2,115,662 | 0.000013 | 53420743 | `0x4e962BB3889Bf030368F56810A9c96B83CB3E778` |
| uniswap_v3 | XDP/USDC | 100 | 1,750,899 | 0.018004 | 53420743 | `0x2dF380544B88AdB3ad0A94100dcC45fd705aAE2d` |
| uniswap_v3 | BNKR/WETH | 10000 | 1,701,289 | 0.000000 | 53420743 | `0xAEC085E5A5CE8d96A7bDd3eB3A62445d4f6CE703` |
| pancakeswap_v3 | USDC/cbBTC | 100 | 1,665,212 | 0.000013 | 53420743 | `0xb94b22332ABf5f89877A14Cc88f2aBC48c34B3Df` |
| uniswap_v3 | USDC/cbBTC | 3000 | 1,574,828 | 0.000013 | 53420743 | `0xeC558e484cC9f2210714E345298fdc53B253c27D` |
| aerodrome_slipstream | WETH/ZEN | 1500 | 1,555,997 | 440.397909 | 53420743 | `0x0392B12a1cEb0cd13af5Ea448CF5586EA609852D` |
| uniswap_v2 | WETH/USDC | 3000 | 1,508,291 | 2,287.426541 | 53420743 | `0x88A43bbDF9D098eEC7bCEda4e2494615dfD9bB9C` |
| aerodrome | USDC/MAI (stable) | 3000 | 1,484,903 | 1.552316 | 53420743 | `0x2a1463CeBE85315224c536AfD389b381B43F3206` |
| aerodrome_slipstream | USDC/ZCHF | 500 | 1,453,373 | 0.823555 | 53420743 | `0x80891885537e20E240987385490017Fc03D9d7Ed` |
| uniswap_v3 | WETH/AERO | 3000 | 1,423,391 | 3,672.038435 | 53420743 | `0x3d5D143381916280ff91407FeBEB52f2b60f33Cf` |
| aerodrome | WETH/USDC | 3000 | 1,360,108 | 2,290.289759 | 53420743 | `0xcDAC0d6c6C59727a65F871236188350531885C43` |
| uniswap_v3 | CLANKER/WETH | 10000 | 1,327,500 | 0.005089 | 53420743 | `0xC1a6FBeDAe68E1472DbB91FE29B51F7a0Bd44F97` |
| pancakeswap_v3 | WETH/USDC | 500 | 1,323,498 | 2,289.610650 | 53420743 | `0xB775272E537cc670C65DC852908aD47015244EaF` |
| aerodrome_slipstream | USDC/cbBTC | 336 | 1,302,577 | 0.000013 | 53420743 | `0x3e66e55e97ce60096f74b7C475e8249f2D31a9fb` |
| aerodrome_slipstream | cbBTC/ZEN | 2500 | 1,295,475 | 14,962.689472 | 53420743 | `0x47f9e291bb766Fc307Ad7BBa4f29f3Eab6A97101` |
| aerodrome | USDC/SEND | 3000 | 1,169,096 | 71.095034 | 53420743 | `0x69bc1d350fE13F499c6AedEd2C5eA9471b2a599A` |
| uniswap_v3 | WETH/doginme | 10000 | 1,114,964 | 37,784,022.857038 | 53420743 | `0xADE9BcD4b968EE26Bed102dd43A55f6A8c2416df` |
| uniswap_v3 | WETH/BRETT | 10000 | 1,067,498 | 532,792.816358 | 53420743 | `0xBA3F945812a83471d709BCe9C3CA699A19FB46f7` |
| uniswap_v3 | DRB/WETH | 10000 | 1,067,201 | 0.000000 | 53420743 | `0x5116773e18A9C7bB03EBB961b38678E45E238923` |
| uniswap_v3 | WETH/TOSHI | 10000 | 1,010,107 | 22,862,394.515506 | 53420743 | `0x4b0Aaf3EBb163dd45F663b38b6d93f6093EBC2d3` |
| aerodrome | WETH/EDEL | 7000 | 987,455 | 81,898.664306 | 53420743 | `0x566beE7EF7b39f29d150AB3be6b6242C17CC5A31` |
| aerodrome_slipstream | USDC/VELVET | 100 | 983,239 | 19.901896 | 53420743 | `0x6b0F53cbD9272D8117e9535FE25371dedF39a1bE` |
| aerodrome | WETH/WELL | 10000 | 950,378 | 1,208,757.390380 | 53420743 | `0x89D0F320ac73dd7d9513FFC5bc58D1161452a657` |
| uniswap_v3 | WETH/VVV | 10000 | 934,280 | 102.727150 | 53420743 | `0x1D2bdB7117a5A7D7fE4c1d95681a92e4Df13bB69` |
| uniswap_v3 | WETH/MORPHO | 3000 | 926,635 | 1,036.153197 | 53420743 | `0x2F42Df4aF5312B492E9d7F7b2110D9c7bf2D9e4F` |
| uniswap_v3 | WETH/USDC | 10000 | 926,598 | 2,291.133952 | 53420743 | `0x0b1C2DCbBfA744ebD3fC17fF1A96A1E1Eb4B2d69` |
| aerodrome | USDC/NOCK | 3000 | 905,104 | 76.418701 | 53420743 | `0x85f1Aa3a70fEdd1C52705c15BAEd143e675CD626` |
| uniswap_v3 | USDC/VVV | 3000 | 896,699 | 0.045155 | 53420743 | `0x67A11022B7B6ed66f81233F6C8Ed6e48F7826530` |
| uniswap_v3 | uXRP/WETH | 3000 | 871,991 | 0.000544 | 53420743 | `0xc8da14d7467814A91384796Db3cA2c273b30B361` |
| aerodrome | WETH/AERO | 10000 | 860,534 | 3,659.352431 | 53420743 | `0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6` |
| aerodrome_slipstream | USDC/SAPIEN | 4520 | 829,113 | 19.764125 | 53420743 | `0x80Cc08712Aa61cE9dc7604F9cE7560A25094B862` |
| pancakeswap_v3 | QUID/USDC | 100 | 796,351 | 0.056826 | 53420743 | `0x07C4bc0F5fb6Cb069124DF3e1aE0B8fD8148ccC4` |
| aerodrome | WETH/wstETH | 3000 | 775,180 | 0.801881 | 53420743 | `0xA6385c73961dd9C58db2EF0c4EB98cE4B60651e8` |
| aerodrome | VIRTUAL/WETH | 10000 | 731,081 | 0.000258 | 53420743 | `0x21594b992F68495dD28d605834b58889d0a727c7` |
| uniswap_v3 | VIRTUAL/USDC | 3000 | 723,502 | 0.587222 | 53420743 | `0x529d2863a1521d0b57db028168fdE2E97120017C` |
| uniswap_v2 | WETH/KEYCAT | 3000 | 706,351 | 4,958,934.375600 | 53420743 | `0x377FeeeD4820B3B28D1ab429509e7A0789824fCA` |
| uniswap_v2 | WETH/NPC | 3000 | 691,070 | 138,314.377097 | 53420743 | `0x3F413FcCAEa59b8053d605AEa7ae847C02ed5D95` |
| aerodrome_slipstream | AERO/cbBTC | 750 | 681,533 | 0.000008 | 53420743 | `0xdFe5F275020def30993f042174Fc2D335678b626` |
| uniswap_v3 | TIG/USDC | 10000 | 671,808 | 0.571996 | 53420743 | `0x5280d5E63b416277d0F81FAe54Bb1e0444cAbDAA` |
| aerodrome | WETH/msETH (stable) | 500 | 662,819 | 2.340905 | 53420743 | `0xDE4FB30cCC2f1210FcE2c8aD66410C586C8D1f9A` |
| aerodrome_slipstream | WETH/BRETT | 2114 | 658,473 | 534,444.849979 | 53420743 | `0x4e829F8A5213c42535AB84AA40BD4aDCCE9cBa02` |
| aerodrome | WETH/bsdETH | 100 | 614,362 | 0.915143 | 53420743 | `0x6B87B8663eE63191887F18225F79D9eEb2DE0d34` |
| aerodrome_slipstream | AVNT/USDC | 2700 | 594,509 | 0.088867 | 53420743 | `0xe30d5BF485F7476AC15884a28ffb3C9cEA635DCB` |
| uniswap_v3 | FLOCK/USDC | 3000 | 556,930 | 0.037829 | 53420743 | `0x7AF45dfaF2fDEA139B2295f37fFea2E16e6Fd8BA` |

## Recherche d'opportunités
- Cycles : 224 ; routes examinées : 4178944 ; candidats optimisés : 14817 ; net attendu > 0 : 55 ; dernier cycle 154.2 ms
- Rejets (moteur) : {'spread_below_threshold': 4114814, 'liquidity_below_min': 46936, 'negative_expected_net': 14762, 'unquotable': 2088, 'borrow_bound_too_small': 223}
- Enregistrements de la session : 14817 ; net attendu > 0 : 55 ; simulés (eth_call de la vraie tx) : 3 (ok 0, échec 3) ; étiquettes ghost N+1 : 0/3 positives
- Décisions : {'REJECTED': 14817} ; motifs de rejet : {'below_safety_margin': 36, 'negative_expected_net': 14762, 'p_lower_below_threshold': 46, 'reliability_not_demonstrated': 9, 'simulation_failed': 3}

## Meilleures opportunités de la session (net attendu, toutes charges déduites)

| Bloc | Route | Montant emprunté | Brut | Frais flash | Gaz (dont L1) | Net attendu | Net simulé | Marge (bps) | p (borne inf.) | Décision | Motifs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[pancakeswap_v3]→USDC | 58.391897 USDC | 0.034971 USDC | 0.000000 USDC | 0.006209 USDC | 0.028762 USDC (0.0265 €) | — | 4.93 | 0.351 (n=1) | REJECTED | reliability_not_demonstrated |
| 53420688 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.025648 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000013 WETH (0.0264 €) | — | 4.90 | 0.351 (n=1) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[uniswap_v3]→USDC | 56.943825 USDC | 0.033837 USDC | 0.000000 USDC | 0.006209 USDC | 0.027628 USDC (0.0254 €) | — | 4.85 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 53420688 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.024771 WETH | 0.000015 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0254 €) | — | 4.87 | 0.060 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 56.185797 USDC | 0.032622 USDC | 0.000000 USDC | 0.006209 USDC | 0.026413 USDC (0.0243 €) | — | 4.70 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 53420688 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.024699 WETH | 0.000014 WETH | 0.000000 WETH | 0.000003 WETH | 0.000012 WETH (0.0243 €) | — | 4.67 | 0.060 (n=5) | REJECTED | simulation_failed:FlashRepaymentImpossible, reliability_not_demonstrated |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[pancakeswap_v3]→USDC | 87.848830 USDC | 0.029016 USDC | 0.000000 USDC | 0.006919 USDC | 0.022097 USDC (0.0203 €) | — | 2.52 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.038423 WETH | 0.000013 WETH | 0.000000 WETH | 0.000003 WETH | 0.000010 WETH (0.0203 €) | — | 2.51 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[uniswap_v3]→USDC | 81.439571 USDC | 0.026704 USDC | 0.000000 USDC | 0.006919 USDC | 0.019785 USDC (0.0182 €) | — | 2.43 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.035630 WETH | 0.000012 WETH | 0.000000 WETH | 0.000003 WETH | 0.000009 WETH (0.0182 €) | — | 2.43 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 82.825229 USDC | 0.025522 USDC | 0.000000 USDC | 0.006919 USDC | 0.018603 USDC (0.0171 €) | — | 2.25 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.036045 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0171 €) | — | 2.25 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH→[aerodrome_slipstream]→USDC | 43.646836 USDC | 0.024409 USDC | 0.000000 USDC | 0.006209 USDC | 0.018200 USDC (0.0167 €) | — | 4.17 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 53420688 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v2]→WETH | 0.019177 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0167 €) | — | 4.15 | 0.060 (n=5) | REJECTED | reliability_not_demonstrated |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[pancakeswap_v3]→USDC | 77.683918 USDC | 0.024592 USDC | 0.000000 USDC | 0.006919 USDC | 0.017673 USDC (0.0163 €) | — | 2.27 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | WETH→[pancakeswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.034185 WETH | 0.000011 WETH | 0.000000 WETH | 0.000003 WETH | 0.000008 WETH (0.0162 €) | — | 2.26 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420657 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→WETH | 0.233301 WETH | 0.000009 WETH | 0.000000 WETH | 0.000002 WETH | 0.000007 WETH (0.0151 €) | — | 0.31 | 0.039 (n=170) | REJECTED | below_safety_margin(7180686752088<46660133402645), p_lower_below_threshold(0.04<0.75) |
| 53420657 | USDC→[pancakeswap_v3]→WETH→[aerodrome_slipstream]→USDC | 531.605419 USDC | 0.021579 USDC | 0.000000 USDC | 0.005172 USDC | 0.016407 USDC (0.0151 €) | — | 0.31 | 0.039 (n=170) | REJECTED | below_safety_margin(16407<106321), p_lower_below_threshold(0.04<0.75) |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[uniswap_v3]→USDC | 72.504741 USDC | 0.022742 USDC | 0.000000 USDC | 0.006919 USDC | 0.015823 USDC (0.0146 €) | — | 2.18 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.031560 WETH | 0.000010 WETH | 0.000000 WETH | 0.000003 WETH | 0.000007 WETH (0.0145 €) | — | 2.19 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH→[aerodrome_slipstream]→USDC | 72.917943 USDC | 0.021507 USDC | 0.000000 USDC | 0.006919 USDC | 0.014588 USDC (0.0134 €) | — | 2.00 | 0.186 (n=812) | REJECTED | p_lower_below_threshold(0.19<0.75) |
| 53420688 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[uniswap_v3]→WETH | 0.032048 WETH | 0.000009 WETH | 0.000000 WETH | 0.000003 WETH | 0.000006 WETH (0.0134 €) | — | 1.99 | 0.186 (n=812) | REJECTED | below_safety_margin(6372122213193<6409565128938), p_lower_below_threshold(0.19<0.75) |
| 53420688 | USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH→[aerodrome_slipstream]→USDC | 45.827957 USDC | 0.013340 USDC | 0.000000 USDC | 0.006919 USDC | 0.006421 USDC (0.0059 €) | — | 1.40 | 0.186 (n=812) | REJECTED | below_safety_margin(6421<9165), p_lower_below_threshold(0.19<0.75) |
| 53420688 | WETH→[aerodrome_slipstream]→USDC→[pancakeswap_v3]→VIRTUAL→[aerodrome_slipstream]→WETH | 0.020203 WETH | 0.000006 WETH | 0.000000 WETH | 0.000003 WETH | 0.000003 WETH (0.0059 €) | — | 1.39 | 0.186 (n=812) | REJECTED | below_safety_margin(2805645364796<4040625347703), p_lower_below_threshold(0.19<0.75) |
| 53420713 | WETH→[uniswap_v3]→USDC→[pancakeswap_v3]→WETH | 0.075929 WETH | 0.000005 WETH | 0.000000 WETH | 0.000002 WETH | 0.000002 WETH (0.0051 €) | — | 0.32 | 0.039 (n=170) | REJECTED | below_safety_margin(2420430990762<15185876907516), p_lower_below_threshold(0.04<0.75) |

## Fiabilité et décision
- Observations ghost : 4644 ; taux observé 0.170 ; borne inférieure crédible (0.9) 0.163 ; seuil 0.75 → **FIABILITÉ INSUFFISANTE**
- Statut de maturité : **FIABILITÉ INSUFFISANTE** — borne inférieure 16.3% < 75%
- Critères : ✅ chain_verified; ❌ tests_passed; ❌ contract_tested; ❌ financial_math_validated; ✅ no_critical_issues; ❌ simulations_realistic; ✅ reliability_documented; ❌ p_success_ge_threshold; ✅ emergency_stop_ok; ❌ budget_and_limits_configured; ❌ signer_available; ✅ data_fresh; ✅ model_calibrated

Fichiers : `*.json` (tout l'état), `*_opportunities.csv.gz` (candidats avec toutes les colonnes de coût : tous les positifs/simulés/étiquetés, puis les meilleurs négatifs, 30 000 lignes max — l'intégralité reste dans la base SQLite de la session).

Aucune transaction n'a été signée ni envoyée pendant cette session (mode ghost, lecture seule).
