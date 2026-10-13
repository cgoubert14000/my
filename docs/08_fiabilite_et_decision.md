# 08 — Système de fiabilité, calcul du net et décision de maturité

## 1. Les cinq niveaux de profit (tous affichés, jamais confondus)

| Niveau | Définition | Source |
|---|---|---|
| Brut théorique | `montant_sortie − montant_emprunté` sur les courbes exactes des pools (frais de swap inclus) | maths V2/V3/Solidly bit-exact |
| Net prévu | brut − frais de flash loan − gaz (unités × prix + données L1) converti en token au prix du pool le plus profond − marge de sécurité | `FeeCalculator.breakdown` |
| Net simulé | profit renvoyé par `eth_call` de la vraie transaction sur le contrat au bloc N − gaz | `Simulator` |
| Net réalisé | delta de solde réel après inclusion − gaz payé (reçu) ; négatif = gaz perdu si revert | reçus de transaction |
| Cumulé | somme des nets réalisés **y compris** le gaz des échecs ; en ghost : somme des nets re-simulés au bloc N+1 | registre SQLite |

## 2. Probabilité de succès : définition et estimation

**Succès** = le net re-simulé au bloc N+1 (le plus tôt où une transaction décidée au bloc N peut être incluse) est
strictement positif. C'est exactement ce que subit une transaction réelle ; c'est donc ce que le mode ghost mesure,
pour **chaque** opportunité positive détectée (déduplication : une observation par route et par fenêtre de 30 blocs
pour qu'un écart persistant ne compte pas 30 fois). Les négatifs sont conservés.

Estimation **sans ML en substitut de simulation** :

1. Par segment (marge en bps × nombre de sauts × combinaison de types de pools), loi Beta-binomiale avec a priori de
   Jeffreys ; on utilise la **borne inférieure** de l'intervalle crédible à 90 %. Sous 30 observations dans le segment,
   le statut est « FIABILITÉ NON DÉMONTRÉE — DONNÉES INSUFFISANTES » et aucune probabilité n'est affichée comme acquise.
2. Une régression logistique (marge, impact, sauts, âge des données, gaz relatif, heure) est ajustée dès 200
   observations avec **validation sur 30 % de données retenues** (Brier et ECE comparés au modèle par segments). Elle
   n'est utilisée que si elle fait mieux sur le holdout **et** jamais pour relever une estimation au-dessus de la borne
   du segment (on prend le minimum). Sur le devnet : holdout 129, Brier 0,223 vs 0,218 → le modèle par segments reste
   en vigueur, ce qui est écrit tel quel dans le rapport.
3. Dérive : si le taux de succès observé sur les 50 dernières observations est inférieur de plus de 15 points à la
   borne qui avait été utilisée pour décider, `model_calibrated` passe au rouge et le réel est suspendu.

Taille d'échantillon : pour qu'une borne inférieure à 90 % atteigne 75 %, il faut par exemple 12 observations à 100 %
de succès, ≈ 125 observations à 80 %, et c'est **impossible** si le taux réel est ≤ 75 % (le rapport l'écrit alors :
« n requis : impossible (taux ≤ seuil) »). Sur le devnet, le taux mesuré est ≈ 66–70 % → statut FIABILITÉ INSUFFISANTE,
ce qui est le comportement attendu et non un défaut à corriger en baissant le seuil.

## 3. Sélection

Pour chaque bloc : routes 2 et 3 sauts → optimisation du montant (grille + nombre d'or, bornée par 25 % de la
profondeur et 150 bps d'impact) → net prévu → simulation des 3 meilleurs → estimation de `p_inf` → espérance
`p_inf × net − (1 − p_inf) × coût d'échec` → classement. Motifs de rejet explicites (écart sous le seuil, net négatif,
impact, liquidité, données périmées, simulation échouée, `p_inf` sous 75 %, non vérifié…).

## 4. Statuts de maturité (calculés, jamais saisis)

| Statut | Condition |
|---|---|
| APPRENTISSAGE | moins de 30 observations |
| SIMULATION | critères techniques verts, fiabilité en cours de démonstration |
| FIABILITÉ INSUFFISANTE | ≥ 30 observations mais borne inférieure < 75 % |
| PRÊT POUR TEST RÉEL LIMITÉ | tous les critères verts **et** politique valide **et** signer disponible (sinon « PRÊT POUR TEST RÉEL — AUTORISATION FINANCIÈRE MANQUANTE ») |
| MODE RÉEL ACTIF | activé manuellement depuis PRÊT ; chaque envoi re-vérifie tout |
| SUSPENDU | kill switch, échecs consécutifs, perte cumulée, budget, politique expirée, dérive, données périmées ; reprise manuelle |

Les seuils (75 %, 90 %, 30 observations, tolérance de dérive) ne font pas partie des paramètres que l'auto-correction
peut modifier.

## 5. Auto-correction (OBSERVER → DIAGNOSTIQUER → MODIFIER → TESTER → COMPARER → ACCEPTER/ROLLBACK)

* Observations : simulations sous l'estimation, ratio gaz estimé/modèle, candidats non quotables, taux ghost sous le
  seuil, latence du cycle, taux par segment.
* Changements possibles : uniquement `TunableParams.ALLOWED_KEYS` (seuil d'écart, marge de sécurité, modèle de gaz,
  fraction de profondeur, âge max des données, points de grille…).
* Test : le candidat est écrit sur une **branche git** du dépôt interne `data/selfcorr` ; la référence (`main`) n'est
  jamais modifiée avant acceptation.
* Comparaison : référence et candidat tournent **sur les mêmes blocs** ; chacun choisit son meilleur candidat au bloc N,
  re-simulé au bloc N+1 ; score = net N+1 en € − coût d'échec. Acceptation seulement si ≥ 5 blocs, score candidat >
  référence × 1,01 et pas plus d'échecs ; puis validation sur de nouveaux blocs (holdout) avec rollback automatique.
* Tout est journalisé (`/api/changes`, onglet Laboratoire) avec la référence git.
