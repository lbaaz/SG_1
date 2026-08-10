r"""# GEL M14 (P1-a) v2 — LE SPECTROMÈTRE 5:2 : le signe de E au cœur de la famille

**Machine 1, 02/08/2026 — v2, intègre la certification v1**
(`m14_certification_croisee_v1.md` : NON CERTIFIÉ, 1 bloquant + 1 chiffre
manquant + 3 notes). Changements : **P-M14b réécrit en critère propre sur
quantité SIGNÉE** (forme machine 2 — différences, jamais log ni rapport —
durcie d'une clause d'ex-æquo, donc **re-testée : 8/8 sur vecteurs E
signés**, dont le profil attendu de P8 et un creux traversant zéro ;
`m14_classifieur_E_test_negatif_v1.log`) ; **P8 chiffre
P(NON CONCLUANT)** sous hypothèses nommées, avec la sortie
pré-identifiée ; **ordre de sommation de B_E déclaré** (N-3) ;
parenthèse de fenêtre corrigée (N-1) ; note P1 v4 transmise avec ses
invariants (N-2). **Règle personnelle machine 1, adoptée au registre**
(2ᵉ instance de la faute « verbatim/inchangé ») : *plus jamais
« inchangé » sur un texte réutilisé sans un test exécuté de ce texte.*
Intouchés (certifiés v1) : P2, P3, P4, P5, P-M14a, P-M14c, comptes.
Gabarit `c5659f52` ; hérités M12 v4 / M13 v3 ; convention de clôture
ratifiée (delta 49.5). Aucun code avant certification (E19).

## P1 — Objet et cibles épistémiques (m2-§8.1, porte par porte)

La **dernière prédiction discriminante** de la note P1 v4 (`a056878b`) :
à la famille 5:2 (q = 7, rayon 0.03), le rang (1, 1) n'existe qu'à
p = 7 — p = 5 est relégué en (3, 1), p = 4 en (4, 2). Donc
E_rés = −1.25·|δ₇| + 2.25·|δ₅⁽³,¹⁾|, et **E plonge NÉGATIF au cœur de la
famille ssi |δ₅⁽³,¹⁾|/|δ₇| < 5/9** (forme dérivée, N-1). Les deux
négatifs de M12 (2.42 → −0.147, 2.55 → −0.483, recalculés de `fa109da9`)
sont les flancs de ce creux prédit.
**P-M14a teste la conjonction étage A + étage B(5:2)** — un échec tue
B(5:2) (l'étage A, acquis hors échantillon, n'est pas re-testé
isolément). **P-M14b** teste la forme (profondeur B-dépendante).
**P-M14c** est la mesure en chaîne du ratio (m2-§8.4), consignation.
Hors périmètre : 8/3 et la tension 2.67 (manche P1-b, double observable,
note v4 §6) ; le dessous criblé (48.3).

## P2 — Géométrie

- **Sept points** : 2.42, 2.46, 2.48, 2.50, 2.52, 2.54, 2.55.
  **Isolement forcé** : une seule famille d'ordre ≤ 12 vit dans
  [2.42, 2.56] — 5/2 (pour k/l dans la fenêtre avec k + l ≤ 12,
  l = 2 impose k = 5 ; l = 1, 3, 4, 5 sont vides). Distances au site en
  exact : 0.08, 0.04, 0.02, 0, 0.02, 0.04, 0.05 — **trois points INTRA
  (2.48, 2.50, 2.52), quatre propres, aucun sur le bord exact du rayon**
  (règle 15, leçon 2.88). Échantillonnage délibéré dans le rayon,
  déclaré (gel M12 v4, ligne 420).
- **Signes** : p = 4 → +1 seul (P-M12e) ; p = 5 et p = 7 → les deux
  signes, sF = min, frag/asym consignés (convention M12). G8 (p = 4, les
  deux signes) au point 2.50 ; moitié grossière attendue vide (p pair).
- **Recherche** : héritée intégralement ; HI0 = 20 (s\* attendus ≤ 3).

## P3 — Custody : G1′ + SIX ancres au bit

**G1′** : rejeu 4|2.80|+1, champ nommé
`resultats.carte['4|2.800000000000'].sF` de `fa109da9`
= 8.129205119847189, écart 0.0 exigé.
**Ancres de régression ×6** (gel M13b A4, étendu) : 2.42 et 2.55 sont des
points M12 aux trois degrés — leurs re-mesures doivent reproduire AU BIT :
4|2.42 = 2.95485882095895 ; 5|2.42 = 1.8274988454540801 ;
7|2.42 = 1.1059806188366135 ; 4|2.55 = 2.881241394133842 ;
5|2.55 = 2.2296999600027783 ; 7|2.55 = 1.2338202720520808.
Écart ≠ 0.0 → ARRET. **Sept verrous de chaîne dans une manche.**
Provenance déclarée : ces deux points et leurs E sont CONNUS — les portes
P-M14a/b vivent sur les points intra et 2.46/2.54, tous NEUFS pour E.

## P4 — LA PERTE EST UNE DONNÉE — consignation SANS porte structurelle

Leçons 47.6 et 48.5 appliquées d'emblée : **aucun motif structurel de
pertes n'est pré-enregistré** — le motif d'une structure se dérive de sa
physique supposée, pas d'un premier échantillon, et nous n'avons AUCUN
échantillon du sous-seuil à 5:2. Toute exclusion G6 est consignée avec
degré, zone (intra / flanc), fenêtre, position et marge ; la carte
(degré × zone) est publiée en P-M14c. Attention déclarée : à p = 7 —
le degré résonnant ici — le phénomène M13 (structuration sous seuil au
site) est plausible ; il sera matière, jamais verdict.

## P5 — Plancher en COMPTES (leçon 48.6 : aucun point nommé)

Un point est **E-valide** ssi ses cinq lignes (4|+1, 5|±1, 7|±1) sont
recevables et non exclues G6. Lecture autorisée ssi : **m_E ≥ 4 ; ≥ 1
E-valide à d ≥ 0.04 de chaque côté ; ≥ 1 E-valide intra.** Sinon : NON
CONCLUANT DE GÉOMÉTRIE, aucune lecture, la manche suivante redessine.
Bords du profil = extrêmes E-valides.

## P6 — Portes

- **P-M14a — LE SIGNE AU CŒUR (la prédiction inconditionnelle).**
  Sur chaque point intra E-valide : E = ln sF₄ − 2.25·ln sF₅ +
  1.25·ln sF₇ ; incertitude dérivée (règle 13) :
  **B_E = pas₄/sF₄ + 2.25·pas₅/sF₅ + 1.25·pas₇/sF₇** (somme linéaire,
  pas de chaque ligne depuis sa consignation).
  **NÉGATIF RÉSOLU** ssi TOUS les intra E-valides ont E < −10·B_E ⇒ la
  prédiction tient, B(5:2) avec elle. **POSITIF RÉSOLU** ssi AU MOINS UN
  intra E-valide a E > +10·B_E ⇒ **B(5:2) est MORT au site** — le terme
  (3, 1) n'est pas négligeable, |δ₅⁽³,¹⁾|/|δ₇| ≥ 5/9, et le contenu
  discriminant de la dérivation tombe. Tout autre motif : **NON CLASSÉ**,
  motif intégral publié (E, B_E, marges par point).
- **P-M14b′ — LA FORME (confirmatoire, B-dépendante) : CRITÈRE PROPRE
  SUR QUANTITÉ SIGNÉE** (bloquant de la cert. v1 : le classifieur M13
  prend des logs et divise par la valeur — E est signé et additif, il
  aurait planté sur la prédiction même). Sur le profil E(ω₂) des
  E-valides, **différences, jamais log ni rapport** :
  **CANYON-E** ssi E possède un minimum intérieur, argmin ∈ [2.48, 2.52]
  (fenêtre = les points intra, qui en sont les bornes ; ce qui est
  garanti par la grille : **aucun point sur le bord du RAYON**, d = 0.03
  — N-1), **et** E(bord du bloc) ≤ E(voisin) − 10·(B_E(bord) +
  B_E(voisin)) des **deux** côtés. **Ex æquo** (règle 15, transposée) :
  deux points intérieurs sont ex æquo ssi |ΔE| ≤ B_E(a) + B_E(b) ; le
  verdict CANYON-E exige tous les ex æquo du minimum dans la fenêtre.
  **MONOTONE-E** ssi E strictement monotone sur les E-valides. Tout
  autre motif : **NON CLASSÉ**, motif intégral publié. **Critère NEUF,
  donc testé avant gel : 8/8** sur vecteurs E signés (attente P8, creux
  traversant zéro, monotones, chute non résolue entre B et 10·B, argmin
  hors fenêtre, ex æquo à cheval et exact) —
  `m14_classifieur_E_test_negatif_v1.log`, empreinte au message.
  **Ordre de sommation de B_E, déclaré (N-3, convention de clôture)** :
  B_E = ((pas₄/sF₄) + 2.25·(pas₅/sF₅)) + 1.25·(pas₇/sF₇), évaluation
  gauche-droite telle qu'écrite ; concordance avec le σ_E_max de M12 :
  0 ulp à 2.42, 1 ulp à 2.55 (l'ordre de M12 n'était pas déclaré) —
  consignée. Toute comparaison inter-implémentations de B_E se fait dans
  l'ordre déclaré.
- **P-M14c — CONSIGNATION, hors porte.** Par degré : le profil ln sF_p
  et son écart à la corde de SES deux extrêmes E-valides (δ_p au point
  2.50) ; le ratio |δ₅|/|δ₇| si les deux sont résolus (chacun > 10 fois
  son incertitude propagée), sinon « δ₅ non résolu » avec sa borne —
  c'est la mesure en chaîne demandée par la re-dérivation (m2-§8.4), en
  consignation parce que les cordes sont le mécanisme B_lisse (bloquant
  B-1 de M13) : jamais un seuil, toujours une mesure publiée. La carte
  des pertes (P4). Frag/asym des degrés impairs.

## P7 — Gardes et comptes

G1′ + ancres ×6 (P3, ARRET au bit) ; G3 ≤ 1e-12, trois re-liaisons
étiquetées (p = 4, 5, 7 — r4) ; G4 dt/2 sur la ligne d'échelle de force
maximale g·s\*^(p−1) tous degrés confondus, **déterminée au run** ;
G5 pas ≤ 1e-5 ; G6 hérité intégral ; G7 : répercussion inter-degrés d'une
exclusion = le point perd son E (P5), déclaré ; G8 à (4, 2.50) ; G2 une
recherche à 2g sur 7|2.50|+1 (le degré résonnant), |K2/K1 − 1| consigné
sans porte (précédent M13) ; G9 constructeurs complets ; selftest : **les huit vecteurs E signés du
test négatif de P-M14b′** (rejoués à l'identique, 8/8 exigé) plus des
vecteurs des trois branches de P-M14a, bloquant — le classifieur M13
n'est pas importé par cette manche.
**Comptes dérivés** : recherches = 7×(1 + 2 + 2) + 1 (G8) + 1 (G1′) +
1 (G4) + 1 (G2) = **39** ; balayages = 35 + 1 = **36**. Les six ancres ne
sont PAS des recherches supplémentaires : ce sont six des 35 lignes du
programme, à double emploi déclaré.

## P8 — Attente gelée du rédacteur (machine 1, avant tout calcul)

Provenance déclarée : flancs M12 connus (−0.147, −0.483), extrapolation.
**P-M14a : NÉGATIF RÉSOLU, les trois intra.** **P-M14b : CANYON-E,
argmin 2.50.** Profondeur attendue |E(2.50)| entre 0.6 et 1.5 (flanc
gauche des canyons 2:1 : ~40 % de D à d = 0.05 ⇒ D ~ 0.483/0.40 ≈ 1.2).
P-M14c : δ₇ résolu, **δ₅ NON résolu** (rang (3,1)), ratio < 5/9 par
borne. Ancres 0.0 ×6. Pertes : 0 à 2, plausiblement à p = 7 intra,
plancher tenu.

**P(NON CONCLUANT DE GÉOMÉTRIE), chiffrée avant mesure** (chiffre
manquant de la cert. v1 ; E-validité = les CINQ lignes du point,
clause fragile = ≥ 1 intra sur 3 ; re-dérivée machine 1) :

| q (perte/ligne) | hypothèse | P(NON CONCLUANT) |
|---|---|---|
| 0.031 | taux M12, lignes R-2′-propres | **0.3 %** |
| 0.125 | taux M13b hors rayon (p = 4) | **11.6 %** |
| 0.556–0.600 | taux INTRA observé à p = 4 (3:1) | **94.9–97.0 %** |

**Le taux intra à 5:2 n'a jamais été mesuré** — c'est l'inconnue que la
manche lève, quel que soit le verdict. Le risque est **intrinsèque à la
question** : le signe au cœur exige un cœur, la clause intra ne peut pas
être affaiblie sans vider P-M14a. Déclaré en face : si le sous-seuil à
5:2 ressemble à celui de 3:1, la manche rend vraisemblablement NON
CONCLUANT — et ce résultat est alors **la première mesure du taux intra
à 5:2**, consignée. **Sortie pré-identifiée** (troisième plancher de
suite en point de rupture — motif nommé) : consignation « MORT INTRA »
avec la carte des pertes par degré (quel degré tue ?), puis la **voie
M13-L** — manche complémentaire à points intra neufs + lecture agrégée
mécanique, le chemin qui a fermé H-SAT. Aucun redessin à chaud.

## P9 — Ce que la manche n'établit pas

Rien sur 8/3 ni 2.67 (manche P1-b) ; rien sur l'étage A isolément ; rien
sur le mécanisme du criblé sous-seuil ; rien hors [2.42, 2.55] ; δ₅ non
résolu ne prouve pas zéro — il borne. Un NON CONCLUANT n'est pas une
réfutation.

## P10 — Chaîne

Parents : gel M12 v4 `bf9866a7` (géométrie, trois degrés), gel M13 v3
`26c5a445` (classifieur, HI0, selftest), gel M13b v1 `7a9b2809` (ancres
au bit), gel M13-L v1 `f779bbe3` + delta 49 `84ec1496` (convention de
clôture, RATIFIÉE). Note source : `note_derivation_P1_signes_E_v4.md`
(`a056878b`) — **transmise ce jour (N-2), à déposer sur BOCAL4** ;
invariants déclarés : la v4 ne modifie NI la table (r, j), NI la
condition 5/9, NI les coefficients — changements limités au statut de
H-SAT (mesurée), au §5 (l'arc M13 → M13-L), au falsifieur §8
(rétroactif) et aux notes R-1/R-2/R-3 intégrées. La certification P1 de
machine 2 (v3 + ses notes R) couvre donc la v4. Artefacts : `fa109da9` (G1′ + ancres + flancs),
`70fe5611`, `22fa1760`. Après certification : dépôt du script
(gabarit m12_ponctuel réduit à la fenêtre, ~39 recherches, ≈ 10 min),
selftest, pré-vol machine 2 (scénarios : attendu ; B-mort ; pertes-p7 ;
géométrie), run. Empreinte de ce gel : au message ; la version certifiée
fera foi.

---

*Fin du gel M14 (P1-a) v2. La dernière marche : soit les trois E du cœur
plongent et le mécanisme est complet — dérivé, contrôlé, hors échantillon,
mesuré — soit un seul remonte et le contenu discriminant tombe. Machine
2 : certification attendue, la v2 répond au bloquant par un critère testé 8/8 et au chiffre
manquant par la table de P8 — certification en diff attendue, puis
dépôt du script.*
"""
# =====================================================================
# m14_p1a_v1.py -- LE SPECTROMETRE 5:2 : le signe de E au coeur de la
# famille. 39 recherches, 36 balayages, ~10 minutes.
# ---------------------------------------------------------------------
# Gel jumeau (docstring ci-dessus) = gel M14 (P1-a) v2 CERTIFIE
# (273d0a53..., cert. croisee v2, feu E19-1) ; empreinte recalculee au
# demarrage (bloc + saut final, convention B). Outillage importe du
# pilote certifie (663b17e2), custody transitive. Moteur c8ed357b.
# ECARTS ET DECLARATIONS (tous en meta.declarations) :
#   (i)   ORDRE DES DEGRES : 4 (G1' + programme + G8), puis 5, puis 7 --
#         trois re-liaisons etiquetees (gel P7). G4 est determinee AU RUN
#         tous degres confondus : si sa ligne n'est pas au dernier degre
#         lie, une 4e re-liaison a lieu, ETIQUETEE -- ecart determine au
#         run, declare.
#   (ii)  SELFTEST DURCI SANS CHANGEMENT DE REGLE : les 8 vecteurs E du
#         gel P7 PLUS les 4 vecteurs [m2] de la certification v2
#         (minimum au bord, chute unilaterale, argmin sur borne, egalite
#         hors fenetre) = 12/12 exige, bloquant.
#   (iii) pas_p d'un point = le pas de la ligne qui FOURNIT sF_p (le
#         cote min aux degres impairs) -- deterministe, consigne.
#   (iv)  G2/G4 : consignation sans porte (precedent M13, gel P7).
#   (v)   Grossiere : pre-declaration ad8dd209 aux lignes p=4 seulement
#         (FAIT NEUF si mordue) ; aux degres impairs, consignation sans
#         pre-declaration (precedent : 2.67 fut la seule grossiere non
#         vide des 67 lignes M12).
#   (vi)  MORT INTRA : si le plancher casse par la clause intra, le
#         resultat est consigne comme PREMIERE MESURE du taux intra a
#         5:2, carte des pertes par degre publiee, sortie pre-identifiee
#         = voie M13-L (gel P8). Aucun redessin a chaud.
# =====================================================================

import argparse, hashlib, importlib.util, json, math, os, sys

import numpy as np

MARQ_DEBUT = "# GEL M14 (P1-a) v2 " + "\u2014 LE SPECTROM\u00c8TRE 5:2"
MARQ_FIN = "puis\nd\u00e9p\u00f4t du script." + "*"

SHA_GEL_M14 = "273d0a53f00cc118d2ffb50fd1a3c2dda3a1896c2bbfaf2f1b172f267c4e1ac6"
SHA_PILOTE = "663b17e2955c79c09f1b6c0fb4443cd0c1f98be0db03ef089f5df682018ce905"
SHA_M12_JSON = "fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1"

# ---- protocole (gel M14 v2) ------------------------------------------
POINTS = [2.42, 2.46, 2.48, 2.50, 2.52, 2.54, 2.55]
INTRA = [2.48, 2.50, 2.52]
FLANC_G = [w for w in POINTS if w <= 2.46]
FLANC_D = [w for w in POINTS if w >= 2.54]
DEGRES = [4, 5, 7]
COEFS = {4: 1.0, 5: -2.25, 7: 1.25}
FEN_LO, FEN_HI, K_CHUTE = 2.48, 2.52, 10
G8_POINT = 2.50                       # p = 4, les deux signes
G2_LIGNE = (7, 2.50, +1)              # 2g sur le degre resonnant
G1P_CHAMP = "resultats.carte['4|2.800000000000'].sF"
G1P_CIBLE = 8.129205119847189
ANCRES = {(4, 2.42): 2.95485882095895, (5, 2.42): 1.8274988454540801,
          (7, 2.42): 1.1059806188366135, (4, 2.55): 2.881241394133842,
          (5, 2.55): 2.2296999600027783, (7, 2.55): 1.2338202720520808}
HI0_M14 = 20.0
M_E_MIN = 4
TOL_APPART = 1e-09
EPS = 1e-12

def plan_signes(p, w):
    if p == 4:
        return [(+1, "sP")] + ([(-1, "sM")] if abs(w - G8_POINT) <= TOL_APPART else [])
    return [(+1, "sP"), (-1, "sM")]

RECH_ATTENDUES = (sum(len(plan_signes(p, w)) for p in DEGRES for w in POINTS)
                  + 1 + 1 + 1)        # G1' + G4 + G2 (G8 est déjà dans le plan)
assert RECH_ATTENDUES == 39, "programme fige : 39 recherches (gel P7)"
BAL_ATTENDUS = sum(len(plan_signes(p, w)) for p in DEGRES for w in POINTS)
assert BAL_ATTENDUS == 36, "balayages : 36 (gel P7)"
FOUT = os.path.join("out", "m14_results.json")
SCENARIOS_PREVOL = ("attendu", "b_mort", "pertes_p7", "geometrie")


# =====================================================================
# 1. GEL JUMEAU, PILOTE, CIBLE G1'
# =====================================================================

def _sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def certifier_gel(verbeux=True):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    if src.count(MARQ_FIN) != 1:
        sys.exit("ARRET invariant de cloture : terminateur x%d" % src.count(MARQ_FIN))
    bloc = src[src.index(MARQ_DEBUT): src.index(MARQ_FIN) + len(MARQ_FIN)] + "\n"
    h = hashlib.sha256(bloc.encode("utf-8")).hexdigest()
    if verbeux:
        print("Gel jumeau M14 v2 : sha %s -> %s"
              % (h[:16] + "...", "CONCORDANT" if h == SHA_GEL_M14 else "DISCORDANT"))
    if h != SHA_GEL_M14:
        sys.exit("ARRET E19 : le gel jumeau ne correspond pas a la version certifiee.")
    return bloc, h


def charger_pilote(chemin="m12_pilote_v3.py", verbeux=True):
    h = _sha(chemin)
    if verbeux:
        print("Script pilote %s -> %s" % (h[:24] + "...",
              "CONCORDANT" if h == SHA_PILOTE else "DISCORDANT"))
    if h != SHA_PILOTE:
        sys.exit("ARRET : le script pilote n'est pas celui que le gel designe.")
    spec = importlib.util.spec_from_file_location("m12_pilote", chemin)
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    P.certifier_gel(verbeux=False)
    if verbeux:
        print("  gel jumeau du pilote re-verifie (03e29c86...) : CONCORDANT")
    for k in ("recherches", "balayages", "sautees", "balayages_sautes"):
        P.CPT[k] = 0
    return P


def charger_cible_g1p(prevol, rep_prevol, P):
    chemin = os.path.join("out", "m12_results.json")

    def lire(pth):
        j = json.load(open(pth, encoding="utf-8"))
        return float(j["resultats"]["carte"][P.cle(4, 2.80)]["sF"])

    if os.path.exists(chemin) and _sha(chemin) == SHA_M12_JSON:
        v = lire(chemin)
        if v != G1P_CIBLE:
            sys.exit("ARRET G1' : champ lu (%r) != valeur du gel (%r)" % (v, G1P_CIBLE))
        return v, {"statut": "REELLE", "sha256": SHA_M12_JSON,
                   "champ": G1P_CHAMP, "valeur_gel": G1P_CIBLE}
    if not prevol:
        sys.exit("ARRET : %s absent ou non conforme (%s exige)" % (chemin, SHA_M12_JSON))
    p = os.path.join(rep_prevol, "m12_results.json")
    if not os.path.exists(p):
        sys.exit("ARRET PREVOL : ni JSON M12 reel conforme, ni synthetique dans %s" % rep_prevol)
    print("=" * 70)
    print("PREVOL : cible G1' SYNTHETIQUE (%s) -- REPETITION, non opposable." % p)
    print("=" * 70)
    return lire(p), {"statut": "SYNTHETIQUE_PREVOL", "sha256": _sha(p),
                     "champ": G1P_CHAMP, "valeur_gel": G1P_CIBLE}


# =====================================================================
# 2. QUANTITES DE LA MANCHE : B_E (ordre declare), E, assemblage
# =====================================================================

def calc_BE(sf, pas):
    """Gel P6, ordre DECLARE : ((t4 + t5) + t7), gauche-droite."""
    return ((pas[4] / sf[4]) + 2.25 * (pas[5] / sf[5])) + 1.25 * (pas[7] / sf[7])


def calc_E(sf):
    return math.log(sf[4]) - 2.25 * math.log(sf[5]) + 1.25 * math.log(sf[7])


MOTIF_P4 = ("P-M12e : r_s = 1 par demonstration (M11, reproduite au bit "
            "par le pilote) ; un seul signe au programme")


def appliquer_borne(m):
    if m.get("recevable") and m.get("s") is not None and m["s"] > HI0_M14:
        m["recevable"] = False
        m["motif_exclusion"] = ("BORNE_ATTEINTE : s = %r > HI0 = %r (gel M14 "
                                "v2, P2) -- consigne, jamais tronque" % (m["s"], HI0_M14))
    return m


def assembler_ligne(p, w, v):
    sP, sM = v["sP"], v.get("sM")
    if sM is None:
        v["sM"] = None
        v["sM_motif"] = MOTIF_P4
        if sP["recevable"]:
            v["sF"] = sP["s"]
            v["pas_sF"] = float(sP["note"].split("pas=")[1])
        else:
            v["sF"] = None
            v["sF_motif"] = sP["motif_exclusion"] or "recherche non recevable"
        v["frag"] = None
        v["frag_motif"] = MOTIF_P4
        v["asym"] = None
        v["asym_motif"] = MOTIF_P4
        return
    if sP["recevable"] and sM["recevable"]:
        cote = sP if sP["s"] <= sM["s"] else sM
        v["sF"] = cote["s"]
        v["pas_sF"] = float(cote["note"].split("pas=")[1])
        v["frag"] = 1 if sP["s"] <= sM["s"] else -1
        v["asym"] = sP["s"] / sM["s"]
    else:
        motif = sP["motif_exclusion"] or (sM["motif_exclusion"] if sM else "") \
            or "non recevable"
        for ch in ("sF", "frag", "asym"):
            v[ch] = None
            v[ch + "_motif"] = motif


def mecanisme_de(motif):
    return "BORNE_ATTEINTE" if motif.startswith("BORNE_ATTEINTE") else "G5"


# =====================================================================
# 3. P-M14b' -- CRITERE ORDINAL SIGNE (gel P6, teste 12/12)
# =====================================================================

def classer_E(w2s, E, BE, w_lo=FEN_LO, w_hi=FEN_HI, K=K_CHUTE):
    """Differences, jamais log ni rapport (bloquant cert. v1 leve)."""
    c = {"profil": [(w, E[w]) for w in w2s], "fenetre": [w_lo, w_hi]}
    n = len(w2s)
    croiss = all(E[w2s[i]] < E[w2s[i + 1]] for i in range(n - 1))
    decro = all(E[w2s[i]] > E[w2s[i + 1]] for i in range(n - 1))
    if croiss or decro:
        c["motif"] = ("strictement monotone ("
                      + ("croissant" if croiss else "decroissant") + ")")
        return "MONOTONE-E", c
    interieur = w2s[1:-1]
    w_min = min(interieur, key=lambda w: E[w])
    B = lambda a, b: BE[a] + BE[b]
    exaequo = sorted(w for w in interieur if abs(E[w] - E[w_min]) <= B(w, w_min))
    c["argmin"], c["ex_aequo"] = w_min, exaequo
    c["resolution_bloc"] = ("chute testee aux deux bords du bloc contre "
                            "leurs voisins exterieurs")
    if not all(w_lo <= w <= w_hi for w in exaequo):
        c["motif"] = "ex aequo/argmin hors fenetre [%s, %s]" % (w_lo, w_hi)
        return "NON CLASSE", c
    wl, wr = exaequo[0], exaequo[-1]
    vg = max(w for w in w2s if w < wl)
    vd = min(w for w in w2s if w > wr)
    marges, ok = {}, True
    for bord, voisin, cote in ((wl, vg, "gauche"), (wr, vd, "droite")):
        seuil = K * B(bord, voisin)
        marges[cote] = (E[voisin] - E[bord]) / seuil
        if not (E[bord] <= E[voisin] - seuil):
            ok = False
    c["marges_sur_seuil"] = marges
    if ok:
        c["motif"] = "minimum interieur en fenetre, chute resolue des deux cotes"
        return "CANYON-E", c
    c["motif"] = "chute non resolue par l'instrument"
    return "NON CLASSE", c


def porte_a(E_intra, BE_intra, K=K_CHUTE):
    """P-M14a : le signe au coeur. TOUS < -10B => NEGATIF RESOLU ;
    AU MOINS UN > +10B => POSITIF RESOLU ; sinon NON CLASSE."""
    # CORRECTIF machine 2 (cert. script v1, bloquant A) : les clefs etaient
    # les FLOTTANTS w2 ; le serialiseur du pilote refuse toute clef non-chaine
    # (TypeError: clef non-chaine 2.48) et le premier sauve() qui voit ce bloc
    # tombe APRES les 39 recherches. Meme defaut que le pilote M11 v2.
    detail = {"%.2f" % w: {"E": E_intra[w], "B_E": BE_intra[w],
                           "marge": E_intra[w] / (K * BE_intra[w])}
              for w in E_intra}
    if not E_intra:
        return "NON CLASSE", {"motif": "aucun point intra E-valide", "detail": detail}
    if any(E_intra[w] > K * BE_intra[w] for w in E_intra):
        return "POSITIF RESOLU", {
            "motif": "au moins un intra E-valide a E > +10.B_E : B(5:2) est "
                     "MORT au site, |d5(3,1)|/|d7| >= 5/9", "detail": detail}
    if all(E_intra[w] < -K * BE_intra[w] for w in E_intra):
        return "NEGATIF RESOLU", {
            "motif": "tous les intra E-valides ont E < -10.B_E : la "
                     "prediction tient, B(5:2) avec elle", "detail": detail}
    return "NON CLASSE", {"motif": "signes non resolus au coeur", "detail": detail}


def plancher_E(valides):
    if len(valides) < M_E_MIN:
        return False, "m_E = %d < %d" % (len(valides), M_E_MIN), None
    g = [w for w in valides if w in FLANC_G]
    d = [w for w in valides if w in FLANC_D]
    i = [w for w in valides if w in INTRA]
    if not g:
        return False, "aucun E-valide au flanc gauche (d >= 0.04)", None
    if not d:
        return False, "aucun E-valide au flanc droit (d >= 0.04)", None
    if not i:
        return False, "aucun E-valide intra", "MORT_INTRA"
    return True, ("m_E = %d ; flancs %d/%d ; intra %d" %
                  (len(valides), len(g), len(d), len(i))), None


# =====================================================================
# 4. SELFTEST -- 12 vecteurs E (8 du gel + 4 [m2] de la cert. v2),
#    branches P-M14a, comptes, grille, B_E a l'ulp
# =====================================================================

BE_TEST = 1.6e-06


def _p(vals):
    return dict(zip(POINTS, vals))


VECTEURS_E = [
    ("attente P8 : creux au coeur, argmin 2.50",
     _p([-0.147, -0.30, -0.70, -1.20, -0.70, -0.30, -0.483]), "CANYON-E"),
    ("creux traversant zero (mixte +/-)",
     _p([+0.20, +0.05, -0.40, -0.90, -0.35, +0.08, +0.15]), "CANYON-E"),
    ("monotone decroissant strict",
     _p([+0.30, +0.10, -0.05, -0.20, -0.35, -0.50, -0.60]), "MONOTONE-E"),
    ("monotone croissant strict",
     _p([-0.60, -0.45, -0.30, -0.15, 0.00, +0.15, +0.25]), "MONOTONE-E"),
    ("chute NON resolue (voisins a 5x le demi-seuil)",
     _p([-0.5 + 3e-5, -0.5 + 2e-5, -0.5 + 8e-6, -0.5, -0.5 + 8e-6,
         -0.5 + 2e-5, -0.5 + 3e-5]), "NON CLASSE"),
    ("argmin HORS fenetre (min en 2.46)",
     _p([-0.10, -0.90, -0.40, -0.30, -0.20, -0.10, -0.05]), "NON CLASSE"),
    ("ex aequo a cheval (2.52 et 2.54 au minimum)",
     _p([-0.10, -0.20, -0.30, -0.40, -0.90, -0.90, -0.05]), "NON CLASSE"),
    ("ex aequo EXACT (2.48, 2.50), tous en fenetre",
     _p([-0.10, -0.20, -0.90, -0.90, -0.40, -0.20, -0.05]), "CANYON-E"),
    ("[m2] minimum a un BORD du profil (2.55) : pas interieur",
     _p([-0.10, -0.20, -0.30, -0.25, -0.40, -0.60, -1.20]), "NON CLASSE"),
    ("[m2] chute resolue A GAUCHE seulement",
     _p([-0.10, -0.30, -0.60, -1.20, -1.20 + 5 * (2 * BE_TEST), -0.30, -0.10]),
     "NON CLASSE"),
    ("[m2] argmin PILE sur la borne de fenetre 2.48",
     _p([-0.10, -0.30, -1.20, -0.70, -0.50, -0.30, -0.10]), "CANYON-E"),
    ("[m2] egalite exacte hors fenetre : pas monotone",
     _p([-1.0, -0.8, -0.6, -0.4, -0.2, -0.2, 0.2]), "NON CLASSE"),
]


def selftest_classifieur_E():
    ech = 0
    print("[A] P-M14b' : 12 vecteurs E signes (8 du gel + 4 [m2] cert. v2), bloquant")
    for nom, E, att in VECTEURS_E:
        BE = {w: BE_TEST for w in POINTS}
        v, c = classer_E(POINTS, E, BE)
        ok = v == att
        ech += (not ok)
        print("  [%s] %s\n          -> %s (%s)"
              % ("OK   " if ok else "ECHEC", nom, v, c["motif"]))
    print("[B] P-M14a : les trois branches")
    BEi = {w: BE_TEST for w in INTRA}
    cas = [({w: -0.8 for w in INTRA}, "NEGATIF RESOLU"),
           ({2.48: -0.8, 2.50: +0.4, 2.52: -0.7}, "POSITIF RESOLU"),
           ({2.48: -0.8, 2.50: -5e-6, 2.52: -0.7}, "NON CLASSE"),
           ({}, "NON CLASSE")]
    for E, att in cas:
        v, c = porte_a(E, {w: BE_TEST for w in E} or BEi)
        ok = v == att
        ech += (not ok)
        print("  [%s] %-40s -> %s" % ("OK   " if ok else "ECHEC",
              str({k: round(x, 3) for k, x in E.items()}) or "aucun intra", v))
    print("[C] plancher_E : comptes, flancs, MORT_INTRA")
    tests = [(POINTS, True, None), (POINTS[:3], False, None),
             ([2.42, 2.46, 2.54, 2.55], False, "MORT_INTRA"),
             ([2.48, 2.50, 2.52, 2.54], False, None)]
    for pts, att_ok, att_flag in tests:
        ok_, mot, flag = plancher_E(pts)
        bon = (ok_ == att_ok and flag == att_flag)
        ech += (not bon)
        print("  [%s] %-34s -> %s%s" % ("OK   " if bon else "ECHEC", str(pts),
              "OK" if ok_ else "ECHEC", " [%s]" % flag if flag else ""))
    return ech


def selftest():
    print("=" * 70)
    print("SELFTEST m14_p1a_v1.py")
    print("=" * 70)
    certifier_gel()
    P = charger_pilote(verbeux=False)
    print("pilote importe par empreinte, gel pilote re-verifie")

    print("\n[1] programme fige, DERIVE")
    assert RECH_ATTENDUES == 39 and BAL_ATTENDUS == 36
    assert sorted(ANCRES) == [(4, 2.42), (4, 2.55), (5, 2.42),
                              (5, 2.55), (7, 2.42), (7, 2.55)]
    print("    39 recherches / 36 balayages ; six ancres declarees")

    print("\n[2] grille : distances exactes, aucun bord de rayon, G1' hors")
    from fractions import Fraction
    for w in POINTS:
        d = abs(Fraction(round(w * 100), 100) - Fraction(5, 2))
        assert d != Fraction(3, 100), "point sur le bord exact du rayon"
    assert [w for w in POINTS if abs(Fraction(round(w * 100), 100)
            - Fraction(5, 2)) < Fraction(3, 100)] == INTRA
    assert min(abs(2.80 - w) for w in POINTS) > TOL_APPART
    print("    3 intra exacts, 0 cas de bord (regle 15), 2.80 hors programme")

    print("\n[3] classifieurs et plancher (bloquant)")
    ech = selftest_classifieur_E()
    assert ech == 0, "%d echec(s) -- BLOQUANT (gel P7)" % ech

    print("\n[4] B_E : ordre declare, concordance M12 a l'ulp (consignee)")
    chemin = os.path.join("out", "m12_results.json")
    if os.path.exists(chemin) and _sha(chemin) == SHA_M12_JSON:
        d12 = json.load(open(chemin, encoding="utf-8"))
        for w, att in ((2.42, 0), (2.55, -1)):
            sf = {p: d12["resultats"]["carte"][P.cle(p, w)]["sF"] for p in DEGRES}
            pas = {p: float(d12["resultats"]["carte"][P.cle(p, w)]["sP"]
                            ["note"].split("pas=")[1]) for p in DEGRES}
            ref = d12["resultats"]["E"]["%.2f" % w]["sigma_E_max"]
            u = round((calc_BE(sf, pas) - ref) / math.ulp(ref))
            assert u == att, "B_E(%s) : %d ulp (attendu %d)" % (w, u, att)
            print("    B_E(%.2f) vs sigma_E_max M12 : %+d ulp (attendu)" % (w, u))
    else:
        print("    (JSON M12 absent : section jouee au run via G1')")

    print("\n[5] borne et E-validite")
    m = appliquer_borne({"s": 25.0, "recevable": True, "motif_exclusion": ""})
    assert not m["recevable"] and m["s"] == 25.0
    print("    s=25 -> BORNE_ATTEINTE non recevable, s conserve")

    print("\n[6] LES SEPT VERROUS DE CUSTODY : leur egalite au bit MORD-ELLE ?")
    # CORRECTIF machine 2 (cert. script v1, bloquant B) : la manche fait de
    # la custody son argument principal (sept verrous) et AUCUN test ne
    # montrait qu'un seul d'entre eux detecterait un ecart. Forme DERIVEE
    # (nextafter), juste meme si une cible change -- avec le temoin embarque
    # du defaut du script M13, ou le litteral "different" etait le MEME
    # double que la cible.
    verrous = [("G1p 4|2.80", G1P_CIBLE)]
    for (pp, ww), cc in sorted(ANCRES.items()):
        verrous.append(("ancre %d|%.2f" % (pp, ww), cc))
    for nom, cible in verrous:
        bas = math.nextafter(cible, -math.inf)
        haut = math.nextafter(cible, math.inf)
        assert (cible - cible) == 0.0, nom
        assert bas != cible and haut != cible, nom
        assert (cible - bas) != 0.0 and (cible - haut) != 0.0, nom
        print("    %-16s %r  ulp = %.3e  voisins detectes"
              % (nom, cible, math.ulp(cible)))
    assert (G1P_CIBLE - 8.129205119847188) == 0.0, (
        "temoin du defaut M13 : ce litteral EST le meme double que la cible")
    print("    temoin embarque : 8.129205119847188 est le MEME double que la")
    print("    cible G1p -- le test negatif du script M13 ne testait rien.")

    print("\n[7] G9 : la couverture DETECTE-T-ELLE une faute injectee ?")
    r0 = _record_synthetique(P)
    assert g9_verifier(r0) == [], "record conforme : 0 defaut attendu"
    r1 = _record_synthetique(P)
    del r1["resultats"]["carte"][P.cle(4, 9.98)]["sF"]
    r2 = _record_synthetique(P)
    r2["resultats"]["carte"][P.cle(7, 9.99)]["asym"] = None
    r2["resultats"]["carte"][P.cle(7, 9.99)].pop("asym_motif", None)
    r3 = _record_synthetique(P)
    r3["resultats"]["E"]["9.99"] = {"E": None}
    d1, d2, d3 = g9_verifier(r1), g9_verifier(r2), g9_verifier(r3)
    assert d1 and d2 and d3, "G9 n a pas detecte une faute injectee"
    print("    conforme : 0 ; sF supprime : %d ; asym null nu : %d ; E null nu : %d"
          % (len(d1), len(d2), len(d3)))

    print("\n[8] geometrie de balayage, via le module PILOTE importe")
    from types import SimpleNamespace
    ns = SimpleNamespace(LO0=0.05, integrer=lambda w2, s, sgn=1, dt=None, g=None:
                         np.zeros(np.asarray(s).shape, bool))
    cpt0 = dict(P.CPT)
    assert P.balayer(ns, 9.9, +1, 0.47)["n_gros"] == 160
    assert P.balayer(ns, 9.9, +1, 2.05)["n_gros"] == 177
    assert P.balayer(ns, 9.9, +1, 2.05)["n_fin"] == 76
    P.CPT.update(cpt0)
    assert not P.verifier_domaine(1.0 / 18.0)[0] and P.verifier_domaine(0.0556)[0]
    print("    vecteurs 160 / 177 / 76 ; domaine strict s* > 1/18")

    print("\nSELFTEST : TOUT PASSE (8 sections).")
    return 0


# =====================================================================
# 5. MOTEUR FACTICE -- QUATRE SCENARIOS (gel P10)
# =====================================================================

def fabriquer_factice(scenario, val_g1p):
    """Valeurs SYNTHETIQUES, aucune physique. Les six ancres sont servies
    AU BIT (sinon ARRET legitime). E est pilote par une cible E_t(w) ;
    s4, s5 = interpolations lineaires entre leurs ancres ; s7 en est
    DEDUIT : s7 = exp((E_t - ln s4 + 2.25 ln s5)/1.25)."""
    module = {"m": None}
    E_ATT = _p([-0.147267, -0.30, -0.70, -1.20, -0.70, -0.30, -0.483335])
    E_BM = _p([-0.147267, -0.05, +0.25, +0.40, +0.22, -0.08, -0.483335])
    E_t = E_BM if scenario == "b_mort" else E_ATT

    def interp(p, w):
        a, b = ANCRES[(p, 2.42)], ANCRES[(p, 2.55)]
        return a + (b - a) * (w - 2.42) / (2.55 - 2.42)

    def s_de(p, w, sgn):
        if (p, w) in ANCRES:
            return ANCRES[(p, w)]
        if p == 4 and abs(w - 2.80) < 1e-9:
            return val_g1p
        if p in (4, 5):
            return interp(p, w)
        return math.exp((E_t[w] - math.log(interp(4, w))
                         + 2.25 * math.log(interp(5, w))) / 1.25)

    def chercher(w2, sgn=1, dt=None, g=None):
        m = module["m"]
        v = s_de(m.P, w2, sgn)
        if g is not None and g > 0.075:
            return v * 2.0 ** (-1.0 / (m.P - 2)), "OK|pas=6.03e-07"
        if scenario == "geometrie" and m.P == 5 and \
                min(abs(w2 - 2.42), abs(w2 - 2.46), abs(w2 - 2.54)) < 1e-9:
            return v, "OK|pas=2.00e-05"      # G5 : trois points de flanc perdent E
        return v, "OK|pas=6.03e-07"

    def integrer(w2, s_arr, sgn=1, dt=None, g=None):
        m = module["m"]
        th = s_de(m.P, w2, sgn)
        if scenario == "pertes_p7" and m.P == 7 and \
                min(abs(w2 - x) for x in INTRA) < 1e-9:
            return np.asarray(s_arr, float) >= 0.5 * th   # G6 tue les intra a p=7
        return np.asarray(s_arr, float) >= th
    return {"chercher": chercher, "integrer": integrer, "module": module}


# =====================================================================
# 6. G9 -- couverture (reprise M13, etendue aux blocs E et portes)
# =====================================================================

def g9_verifier(res):
    defauts = []
    for k, v in res["resultats"]["carte"].items():
        for ch in ("sP", "sM", "sF", "frag", "asym"):
            if ch not in v:
                defauts.append("carte[%s] : champ absent %s" % (k, ch))
            elif v[ch] is None and ch != "sP" and not v.get(ch + "_motif"):
                defauts.append("carte[%s] : %s null SANS motif" % (k, ch))
    for k, b in res["resultats"]["G6"].items():
        for ch in ("n_gros", "n_fin", "exclue", "pas_final_recherche",
                   "indice_40_compte_comme_sous_seuil"):
            if ch not in b:
                defauts.append("G6[%s] : champ absent %s" % (k, ch))
    for w, e in res["resultats"]["E"].items():
        if e.get("E") is None and not e.get("motif"):
            defauts.append("E[%s] : null SANS motif" % w)
    return defauts


def _record_synthetique(P):
    res = {"resultats": {"carte": {}, "G6": {}, "E": {}}}
    fake = {"s": 1.234, "note": "OK|pas=6.03e-07", "recevable": True,
            "motif_exclusion": "", "duree_s": 0.0}
    v2s = {"sP": dict(fake), "sM": dict(fake, s=1.235)}
    assembler_ligne(7, 9.99, v2s)
    res["resultats"]["carte"][P.cle(7, 9.99)] = v2s
    v1s = {"sP": dict(fake)}
    assembler_ligne(4, 9.98, v1s)
    res["resultats"]["carte"][P.cle(4, 9.98)] = v1s
    from types import SimpleNamespace
    ns = SimpleNamespace(LO0=0.05, integrer=lambda w2, s, sgn=1, dt=None, g=None:
                         np.asarray(s, float) >= 1.234)
    cpt0 = dict(P.CPT)
    bal = P.enrichir_g6(P.balayer(ns, 9.99, +1, 1.234), 1.234, fake["note"])
    P.CPT.update(cpt0)
    res["resultats"]["G6"][P.cle(7, 9.99) + "|+1"] = bal
    res["resultats"]["E"]["9.99"] = {"E": None, "motif": "synthetique"}
    return res


# =====================================================================
# 7. PIPELINE
# =====================================================================

def run_pipeline(P, a, val_g1p, meta_g1p, fout, mode, scenario=None):
    for k in ("recherches", "balayages", "sautees", "balayages_sautes"):
        P.CPT[k] = 0
    factice = fabriquer_factice(scenario, val_g1p) if scenario else None
    m9 = P.charger_moteur(a.moteur, factice=factice)
    d = g9_verifier(_record_synthetique(P))
    if d:
        sys.exit("ARRET G9 (avant run) :\n  " + "\n  ".join(d))
    print("G9 avant-run : constructeurs COMPLETS.")
    res = {"meta": {"gel_sha256_bloc": SHA_GEL_M14, "pilote_sha256": SHA_PILOTE,
                    "m12_json_sha256_attendu": SHA_M12_JSON,
                    "cible_g1p": meta_g1p, "mode": mode,
                    "convention_empreinte": "B ; cloture au bit : forme "
                        "canonique LF, etiquettes normalisees, date omise "
                        "(delta 49.5, ratifiee)",
                    "declarations": {
                        "editions_machine2": (
                            "le script a ete edite par machine 2 apres sa "
                            "certification v1, sur demande explicite : (A) clefs "
                            "de porte_a.detail formatees -- le serialiseur du "
                            "pilote refuse les clefs flottantes et le run "
                            "plantait APRES les 39 recherches (meme defaut que "
                            "le pilote M11 v2) ; (B) selftest : section [6] "
                            "detection sur les SEPT verrous de custody "
                            "(nextafter, temoin du defaut M13 embarque), [7] "
                            "detection G9 sur faute injectee, [8] vecteurs de "
                            "geometrie de balayage. AUCUNE edition ne touche le "
                            "chemin de mesure, les portes, le classifieur, les "
                            "comptes ni le gel jumeau. Ecart a la repartition "
                            "machine1/machine2, CONSIGNE."),
                        "cibles": "P-M14a : etage A + B(5:2), conjonction ; "
                                  "P-M14b' : forme, B-dependante ; P-M14c : "
                                  "consignation (gel P1)",
                        "ordre_B_E": "((pas4/sF4) + 2.25*(pas5/sF5)) + "
                                     "1.25*(pas7/sF7), gauche-droite (gel P6)",
                        "pas_sF": "pas d'un point = pas de la ligne qui "
                                  "fournit sF (cote min aux degres impairs)",
                        "rebind": "trois re-liaisons programme (4, 5, 7) ; "
                                  "une 4e si la ligne G4 change de degre -- "
                                  "determinee au run, etiquetee",
                        "G2_G4_sans_porte": "consignation, aucun seuil au gel",
                        "grossiere": "pre-declaration ad8dd209 aux lignes "
                                     "p=4 (FAIT NEUF si mordue) ; degres "
                                     "impairs : consignation simple",
                        "selftest_durci": "8 vecteurs du gel + 4 [m2] de la "
                                          "cert. v2 = 12/12, sans changement "
                                          "de regle",
                        "sortie_pre_identifiee": "MORT INTRA => premiere "
                            "mesure du taux intra a 5:2, carte par degre, "
                            "voie M13-L ; aucun redessin a chaud (gel P8)"},
                    "G3_par_degre": [], "gardes": [], "exclusions": {}},
           "resultats": {"carte": {}, "G6": {}, "G8": {}, "G2": {}, "G4": {},
                         "G1p": {}, "ancres_regression": {}, "E": {},
                         "portes": {}, "P_M14c": {}},
           "verdict": {}, "resume": {}}
    if scenario:
        res["meta"]["prevol_scenario"] = scenario
    jg3 = res["meta"]["G3_par_degre"]
    carte, excl = res["resultats"]["carte"], res["meta"]["exclusions"]

    def sauve():
        P.sauver(res, fout)

    # ---- G1' (rebind 4, bloquante) ------------------------------------
    print("\n--- G1' custody : rejeu au bit de (2.80, p=4, +1) ---")
    P.rebind(m9, 4, jg3)
    jg3[-1]["etiquette"] = "p=4 : G1' + programme + G8"
    r = P.mesurer(m9, 2.80, +1)
    ec = (r["s"] - val_g1p) if r["s"] is not None else None
    res["resultats"]["G1p"] = {"ligne": "4|2.80|+1", "champ_cible": G1P_CHAMP,
                               "mesure": r, "cible": val_g1p, "ecart_absolu": ec,
                               "verdict": "PASSE" if ec == 0.0 else "ECHEC"}
    sauve()
    if ec != 0.0:
        sys.exit("ARRET G1' : ecart %r != 0" % ec)
    print("  ecart absolu = 0.0 EXACT : custody intacte.")

    # ---- programme : degre par degre, ancres au bit -------------------
    for p in DEGRES:
        if p != 4:
            P.rebind(m9, p, jg3)
            jg3[-1]["etiquette"] = "p=%d : programme" % p
        print("\n--- programme p = %d ---" % p)
        for w in POINTS:
            v = carte.setdefault(P.cle(p, w), {})
            for sgn, k in plan_signes(p, w):
                m = appliquer_borne(P.mesurer(m9, w, sgn))
                if p == 4 and sgn < 0:
                    m["role"] = "regression_G8"
                v[k] = m
                sauve()
            assembler_ligne(p, w, v)
            if v["sF"] is None:
                excl.setdefault(P.cle(p, w), []).append(
                    "%s : %s" % (mecanisme_de(v["sF_motif"]), v["sF_motif"]))
            if (p, w) in ANCRES and v["sF"] is not None:
                ecA = v["sF"] - ANCRES[(p, w)]
                res["resultats"]["ancres_regression"][P.cle(p, w)] = {
                    "cible_m12": ANCRES[(p, w)], "ecart_absolu": ecA,
                    "verdict": "PASSE" if ecA == 0.0 else "ECHEC",
                    "source": "m12_results.json fa109da9 (gel P3)"}
                if ecA != 0.0:
                    sauve()
                    sys.exit("ARRET ancre : %r en %d|%.2f" % (ecA, p, w))
            if p == 4 and abs(w - G8_POINT) <= TOL_APPART and v.get("sM") \
                    and v["sP"]["recevable"] and v["sM"]["recevable"]:
                e8 = v["sP"]["s"] - v["sM"]["s"]
                res["resultats"]["G8"].setdefault(P.cle(4, w), {})["G8a"] = {
                    "ecart_absolu": e8, "verdict": "OK" if e8 == 0.0 else "ECHEC"}
                if e8 != 0.0:
                    sauve()
                    sys.exit("ARRET G8a : %r" % e8)
            sauve()
        # balayages du degre
        for w in POINTS:
            v = carte[P.cle(p, w)]
            plan = plan_signes(p, w)
            if not all(v[k]["recevable"] for _, k in plan):
                P.CPT["balayages_sautes"] += len(plan)
                res["meta"]["gardes"].append("G6 %s : %d balayage(s) SAUTE(S)"
                                             % (P.cle(p, w), len(plan)))
                sauve()
                continue
            bg = {}
            for sgn, k in plan:
                ok, motif = P.verifier_domaine(v[k]["s"])
                if not ok:
                    sauve()
                    sys.exit("ARRET domaine : " + motif)
                bal = P.enrichir_g6(P.balayer(m9, w, sgn, v[k]["s"]),
                                    v[k]["s"], v[k]["note"])
                if p == 4:
                    bal["grossiere_pre_declaration"] = "ad8dd209 : VIDE attendue"
                    if bal["gros_explosifs"] > 0:
                        res["meta"]["gardes"].append(
                            "FAIT NEUF : grossiere a MORDU a p=4, w2=%.2f "
                            "sgn=%+d" % (w, sgn))
                else:
                    bal["grossiere_pre_declaration"] = (
                        "aucune (degre impair ; precedent 2.67)")
                bg[k] = bal
                res["resultats"]["G6"][P.cle(p, w) + "|%+d" % sgn] = bal
                if bal["exclue"]:
                    excl.setdefault(P.cle(p, w), []).append(
                        "G6 sgn=%+d explosion sous seuil" % sgn)
            if p == 4 and abs(w - G8_POINT) <= TOL_APPART and len(bg) == 2:
                g8 = P.g8b(bg["sP"], bg["sM"])
                res["resultats"]["G8"].setdefault(P.cle(4, w), {})["G8b"] = g8
                if (g8["grossier"]["deviations"] != 0 or g8["fin"]["deviations"] != 0
                        or not g8["ilots_identiques"] or not g8["retombee_identique"]):
                    sauve()
                    sys.exit("ARRET G8b en w2=%.2f" % w)
            sauve()

    # ---- G2 : 2g sur 7|2.50|+1 (courant : p=7) ------------------------
    p2, w2g, s2g = G2_LIGNE
    base = carte[P.cle(p2, w2g)].get("sP")
    r2 = P.mesurer(m9, w2g, s2g, g=2 * m9.G_REF)
    if base and base["recevable"] and r2["recevable"]:
        ratio = 2.0 * (r2["s"] / base["s"]) ** (p2 - 2)
        rm = None
    else:
        ratio, rm = None, "base ou 2g non recevable"
    res["resultats"]["G2"]["%d|%+d" % (p2, s2g)] = {
        "w2": w2g, "g": "2g", "mesure": r2, "K2_sur_K1": ratio,
        "ratio_motif": rm, "statut": "CONSIGNE (aucun seuil au gel)"}
    sauve()

    # ---- G4 : dt/2, echelle de force max tous degres, AU RUN ----------
    best = None
    for p in DEGRES:
        for w in POINTS:
            v = carte[P.cle(p, w)]
            if v["sF"] is not None:
                e = m9.G_REF * v["sF"] ** (p - 1)
                if best is None or e > best[0]:
                    best = (e, p, w, v["sF"])
    if best is None:
        P.CPT["sautees"] += 1
        res["meta"]["gardes"].append("G4 : SAUTEE (rien de recevable)")
    else:
        _, p4_, w4, sref = best
        if p4_ != m9.P:
            P.rebind(m9, p4_, jg3)
            jg3[-1]["etiquette"] = ("G4 : 4e re-liaison (ligne %d|%.2f, "
                                    "determinee au run -- declaree)" % (p4_, w4))
        r4 = P.mesurer(m9, w4, +1, dt=m9.DT / 2)
        ec4 = abs(r4["s"] / sref - 1.0) if r4["recevable"] else None
        res["resultats"]["G4"] = {
            "p": p4_, "w2": w4, "s_dt": sref, "s_dt2": r4["s"],
            "duree_s": r4["duree_s"], "ecart": ec4,
            "ecart_motif": None if ec4 is not None else r4["motif_exclusion"],
            "forme": "|s_dt2/s_dt - 1| (ratio)",
            "statut": "CONSIGNE (aucun seuil au gel)"}
        print("\n--- G4 sur %d|%.2f|+1 : ecart %s ---" % (p4_, w4,
              "%.3e" % ec4 if ec4 is not None else "NON EVALUABLE"))
    sauve()

    # ---- E, plancher, portes, consignations ---------------------------
    print("\n--- E, plancher, portes ---")
    Ev, BEv = {}, {}
    for w in POINTS:
        lignes_ok = True
        for p in DEGRES:
            v = carte[P.cle(p, w)]
            if v["sF"] is None or P.cle(p, w) in excl:
                lignes_ok = False
        if lignes_ok:
            sf = {p: carte[P.cle(p, w)]["sF"] for p in DEGRES}
            pas = {p: carte[P.cle(p, w)]["pas_sF"] for p in DEGRES}
            Ev[w], BEv[w] = calc_E(sf), calc_BE(sf, pas)
            res["resultats"]["E"]["%.2f" % w] = {
                "E": Ev[w], "B_E": BEv[w], "valide": True,
                "zone": "intra" if w in INTRA else "flanc"}
        else:
            mots = sorted({m.split(" :")[0] for p in DEGRES
                           for m in excl.get(P.cle(p, w), [])}) or ["ligne sans sF"]
            res["resultats"]["E"]["%.2f" % w] = {
                "E": None, "valide": False, "zone": "intra" if w in INTRA else "flanc",
                "motif": "G7 : lignes perdues (%s) -- le point perd son E"
                         % ", ".join(mots)}
    valides = sorted(Ev)
    okp, motp, flag = plancher_E(valides)
    if not okp:
        va, ca = "NON CONCLUANT DE GEOMETRIE", {"motif": motp}
        vb, cb = "NON CONCLUANT DE GEOMETRIE", {"motif": motp}
    else:
        va, ca = porte_a({w: Ev[w] for w in valides if w in INTRA},
                         {w: BEv[w] for w in valides if w in INTRA})
        vb, cb = classer_E(valides, Ev, BEv)
    res["resultats"]["portes"] = {
        "P_M14a": {"verdict": va, "consignation": ca},
        "P_M14b": {"verdict": vb, "consignation": cb},
        "plancher": {"statut": "OK" if okp else "ECHEC", "motif": motp,
                     "E_valides": valides,
                     "mort_intra": bool(flag == "MORT_INTRA")}}
    # P-M14c : cordes en consignation
    c14 = {"pertes_par_degre_zone": {}, "delta_par_degre": {}}
    for p in DEGRES:
        perdus = [w for w in POINTS if carte[P.cle(p, w)]["sF"] is None
                  or P.cle(p, w) in excl]
        c14["pertes_par_degre_zone"]["p%d" % p] = {
            "intra": [w for w in perdus if w in INTRA],
            "flanc": [w for w in perdus if w not in INTRA]}
        vivants = [w for w in valides]
        if len(vivants) >= 2 and 2.50 in vivants:
            wl, wr = vivants[0], vivants[-1]
            L = {w: math.log(carte[P.cle(p, w)]["sF"]) for w in (wl, 2.50, wr)}
            corde = L[wl] + (L[wr] - L[wl]) * (2.50 - wl) / (wr - wl)
            c14["delta_par_degre"]["p%d" % p] = {
                "delta_2.50": L[2.50] - corde, "corde": [wl, wr],
                "statut": "CONSIGNATION -- jamais un seuil (gel P6/P-M14c)"}
        else:
            c14["delta_par_degre"]["p%d" % p] = {
                "delta_2.50": None, "motif": "2.50 non E-valide ou corde impossible"}
    d5 = c14["delta_par_degre"]["p5"].get("delta_2.50")
    d7 = c14["delta_par_degre"]["p7"].get("delta_2.50")
    if d5 is not None and d7 is not None and d7 != 0.0:
        c14["ratio_d5_sur_d7"] = {"valeur": abs(d5) / abs(d7),
                                  "seuil_derive": "5/9 = 0.5556 (gel P1)",
                                  "statut": "CONSIGNATION"}
    res["resultats"]["P_M14c"] = c14

    verdict = {"m_E": len(valides), "P_M14a": va, "P_M14b": vb,
               "detail_a": ca["motif"], "detail_b": cb["motif"],
               "mort_intra": bool(flag == "MORT_INTRA")}
    if flag == "MORT_INTRA":
        verdict["consignation_mort_intra"] = (
            "PREMIERE MESURE du taux intra a 5:2 : les points intra ont "
            "perdu leur E ; carte par degre en P_M14c ; sortie "
            "pre-identifiee = voie M13-L (gel P8)")
    if mode == "PREVOL":
        verdict = {("PREVOL_SYNTHETIQUE_" + k): v for k, v in verdict.items()}
        print("=" * 70)
        print("PREVOL : verdict SYNTHETIQUE -- AUCUNE PHYSIQUE.")
        print("=" * 70)
    res["verdict"] = verdict

    pertes = dict(excl)
    res["resume"] = {
        "m_E": len(valides), "lignes_perdues": sorted(pertes),
        "pertes_par_mecanisme": {g: sum(1 for ms in pertes.values()
                                        if any(s.startswith(g) for s in ms))
                                 for g in ("G5", "G6", "BORNE_ATTEINTE")},
        "attrition_lignes": {"perdues": len(pertes), "sur": BAL_ATTENDUS,
                             "perimetre": "LIGNES (p|w|sgn assemblees en p|w)"},
        "duree_des_mesures_carte_s": None}
    durees = [carte[P.cle(p, w)][k]["duree_s"] for p in DEGRES for w in POINTS
              for _, k in plan_signes(p, w)]
    res["resume"]["duree_des_mesures_carte_s"] = {
        "n": len(durees), "total": float(sum(durees)),
        "perimetre": "les 36 mesures de la carte ; G1', G2, G4 non compris"}
    dtmod = __import__("datetime")
    res["meta"]["date_utc"] = dtmod.datetime.now(dtmod.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    res["meta"]["script_sha256"] = _sha(os.path.abspath(__file__))
    res["meta"]["recherches"] = {"comptees": P.CPT["recherches"],
                                 "sautees": P.CPT["sautees"],
                                 "attendues": RECH_ATTENDUES}
    res["meta"]["balayages"] = {"comptes": P.CPT["balayages"],
                                "sautes": P.CPT["balayages_sautes"],
                                "attendus": BAL_ATTENDUS}
    d = g9_verifier(res)
    if d:
        sauve()
        sys.exit("ARRET G9 (apres run) : %d defaut(s) :\n  %s"
                 % (len(d), "\n  ".join(d)))
    sauve()
    if P.CPT["recherches"] + P.CPT["sautees"] != RECH_ATTENDUES:
        sys.exit("ARRET : %d+%d recherches != %d"
                 % (P.CPT["recherches"], P.CPT["sautees"], RECH_ATTENDUES))
    if P.CPT["balayages"] + P.CPT["balayages_sautes"] != BAL_ATTENDUS:
        sys.exit("ARRET : %d+%d balayages != %d"
                 % (P.CPT["balayages"], P.CPT["balayages_sautes"], BAL_ATTENDUS))
    print("\nEcrit : %s" % fout)
    print("Recherches : %d+%d=%d/%d | balayages : %d+%d=%d/%d"
          % (P.CPT["recherches"], P.CPT["sautees"],
             P.CPT["recherches"] + P.CPT["sautees"], RECH_ATTENDUES,
             P.CPT["balayages"], P.CPT["balayages_sautes"],
             P.CPT["balayages"] + P.CPT["balayages_sautes"], BAL_ATTENDUS))
    ka = "P_M14a" if mode != "PREVOL" else "PREVOL_SYNTHETIQUE_P_M14a"
    kb = "P_M14b" if mode != "PREVOL" else "PREVOL_SYNTHETIQUE_P_M14b"
    print("m_E = %d | P-M14a : %s | P-M14b' : %s"
          % (len(valides), res["verdict"][ka], res["verdict"][kb]))
    print("sha256 du JSON : %s" % _sha(fout))


# =====================================================================
# 8. RUN
# =====================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--prevol", action="store_true")
    ap.add_argument("--pilote", default="m12_pilote_v3.py")
    ap.add_argument("--moteur", default="m9_replication_v1.py")
    ap.add_argument("--sources-prevol", default="prevol_sources")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    certifier_gel()
    P = charger_pilote(a.pilote)
    val_g1p, meta_g1p = charger_cible_g1p(a.prevol, a.sources_prevol, P)
    if a.prevol:
        print("=" * 70)
        print("PREVOL : %d scenarios -- toutes les branches" % len(SCENARIOS_PREVOL))
        print("=" * 70)
        for sc in SCENARIOS_PREVOL:
            fout = os.path.join("out", "m14_PREVOL_%s.json" % sc)
            assert fout != FOUT
            print("\n" + "#" * 70)
            print("# SCENARIO PREVOL : %s" % sc)
            print("#" * 70)
            run_pipeline(P, a, val_g1p, meta_g1p, fout, "PREVOL", scenario=sc)
        print("\nPREVOL : %d scenarios termines." % len(SCENARIOS_PREVOL))
        return
    run_pipeline(P, a, val_g1p, meta_g1p, FOUT, "REEL")


if __name__ == "__main__":
    main()
