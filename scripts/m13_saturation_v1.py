r"""# GEL M13 v3 — BALAYAGE DE SATURATION : s\*(ω₂) à p = 4 À TRAVERS 3:1

**Machine 1, 02/08/2026 — v3, éditions de la certification v2**
(`m13_certification_croisee_v2.md` : fond certifié, deux corrections
éditoriales + deux notes). Changements v2 → v3, tous éditoriaux : **C-2**
le prime est retiré — un seul nom, P-M13a, partout ; **C-1** l'empreinte
du `.log` v1 passée en canonique NFC+LF ; **§7** « deux valeurs
distinctes » (le « trois » venait d'une synthèse machine 2, corrigée par
elle-même — cert. v2 §6) ; **N-5** règle d'égalité à l'argmin déclarée
(règle 15) ; **N-6** « toute issue, y compris NON CLASSÉ » au §5 ; la
mention « verbatim » corrigée — le critère est la forme **durcie**
(deux voisins, B_inst par paire), re-testée 5/5 sur son propre texte
(cert. v2 §2, marge minimale 406×). **Aucune dérivation, aucun compte,
aucune branche ne change.** Intouchés : §1, §2, §4, §5 (hors N-6),
recherches = 13, balayages = 10. Certification à vue attendue, puis feu
E19.

## 1. Objet et cible épistémique (exigence re-dérivation m2 §8.1)

Tester **H-SAT** — la saturation du canal 3:1 au degré 4 — et, à travers
elle, l'étage B au site 3:1. La règle de sélection nue (rang (1,1), le
couplage maximal) prédit ici le canyon le plus profond du jeu ; H-SAT
prédit son absence. **L'étage A n'est pas testé par cette manche.**
Un seul degré (p = 4), un seul signe (+1, P-M12e), aucune combinaison E.

## 2. Les deux branches, écrites d'avance

- **Branche LISSE** : profil sans creux au sens de P-M13a ⇒ H-SAT est
  **mesurée dans la chaîne** ; le groupe 3:1 de M12 est expliqué ; second
  test favorable de l'étage B. La lecture du §3 de la note P1 v2 passe de
  « 8 prédits + 3 accommodés » à « 8 prédits + 3 expliqués par un
  mécanisme mesuré ».
- **Branche CANYON** : creux au sens de P-M13a ⇒ **H-SAT est morte** ; la
  lecture du groupe 3:1 s'effondre et avec elle 3 des 11 signes de la
  confrontation ; l'étage A reste intact ; le mécanisme du signe est à
  reconstruire au site 3:1.

## 3. Attente gelée du rédacteur (machine 1, avant tout calcul)

**Branche LISSE.** Profil strictement croissant sur toute la fenêtre ;
|écart de ln s\* à la corde des deux bords, évalué en 3.00| < 0.05 ;
aucune ligne exclue par G6 ; les fenêtres grossières vides sur les 9
lignes (p pair, précédent ad8dd209/M12 : 15/15 vides).

**Provenance déclarée (règle de provenance, m2-§8.6)** : cette attente
n'est **pas** indépendante — les trois points p = 4 de M12 (2.72, 2.78,
2.80) sont déjà strictement croissants et sans approche de canyon ; c'est
la donnée qui a motivé la manche. L'attente est une extrapolation de
l'entraînement, la manche en est le test.

## 4. Géométrie

- **Fenêtre** : ω₂ ∈ [2.85, 3.15] — hors du domaine gelé de M12
  ([1.73, 2.82]) : M13 déclare **son propre domaine**. Une seule famille
  d'ordre ≤ 12 vit dans la fenêtre : 3/1 (q = 4, rayon 0.12) — la fenêtre
  isole le site.
- **Neuf points** : 2.85, 2.90, 2.94, 2.97, 3.00, 3.03, 3.06, 3.10, 3.15.
  Les points de [2.88, 3.12] sont **dans le rayon de 3:1 — échantillonnage
  délibéré, déclaré** (précédent : gel M12 v4, ligne 420). 2.85 et 3.15
  sont R-2′-propres et servent de bords de corde.
- **Signe** : +1 seul au programme (P-M12e — r_s = 1 par démonstration,
  reproduite au bit par le pilote et le run M12). Une ligne de régression
  G8 au point 3.00 (les deux signes) re-vérifie la parité dans la fenêtre
  neuve.
- **Recherche** : géométrie de recherche M12 héritée (bissection, pas
  final ≤ plafond G5, fenêtres fine [0.90 s\*, 1.05 s\*] et grossière
  [LO0, 0.90 s\*], résolutions consignées par ligne — correctif E27,
  parade d'indice 40 par ligne). **Borne haute initiale HI0 = 20**,
  déclarée (s\* attendu croissant au-delà de 8 dans la fenêtre ; la borne
  n'est pas un seuil de garde, seulement un cadre de bissection — si un
  s\* la dépasse, la ligne est consignée BORNE_ATTEINTE et non recevable,
  jamais silencieusement tronquée).

## 5. LA PERTE EST UNE DONNÉE (exigence m2 §8.2)

Le mécanisme d'exclusion G6 (explosion sous 0.98 s\*) est **corrélé au
signal cherché** : si un canyon existe, les lignes proches de 3.00 sont
les plus susceptibles de mourir. Pré-déclaration :

- Toute explosion sous seuil est consignée avec sa position, sa fenêtre
  (fine/grossière) et sa marge — comme dans l'artefact M12.
- **Branche de lecture des pertes, écrite d'avance** : si ≥ 2 exclusions
  G6 tombent sur des points à d ≤ 0.06 de 3.00 et aucune à d > 0.06,
  la manche est lue « STRUCTURE SOUS-SEUIL AU SITE 3:1 » — un résultat,
  consigné séparément de P-M13a, compatible avec **toute issue**
  de P-M13a sur les survivants, y compris NON CLASSÉ. Ni preuve de canyon, ni attrition simple.
- Pertes éparses (sans le motif ci-dessus) : attrition simple, consignée.
- **Plancher** : P-M13a exige m ≥ 7 survivants ET les deux bords de corde
  (2.85, 3.15) survivants. Sinon : NON CONCLUANT DE GÉOMÉTRIE, aucune
  lecture, et la manche suivante redessine la fenêtre.

## 6. Portes

- **P-M13a — le creux, critère ORDINAL** (correctif machine 2, **durci**
  par machine 1 — deux voisins, B_inst par paire — et re-testé 5/5 sur le
  texte durci, certification v2 §2 ; marge minimale 406 × le seuil
  instrumental majoré). Sur les survivants, en ln s\* :
  **CANYON** ssi le profil possède un minimum **intérieur** avec
  argmin ∈ [2.94, 3.06], **et** la chute est résolue par l'instrument des
  **deux** côtés : ln s\*(argmin) ≤ ln s\*(voisin) − 10·B_inst pour chacun
  des deux voisins survivants, avec **B_inst = (pas/s\*)(argmin) +
  (pas/s\*)(voisin)** — somme linéaire des incertitudes des deux lignes
  comparées (forme dérivée, règle 13 ; ordre de grandeur 1e-6 contre des
  structures attendues de 0.1 à 2.7 : cinq à sept ordres de marge, et le
  seuil ne dépend d'aucune quantité que la mesure puisse gonfler).
  **LISSE** ssi le profil est **strictement monotone** sur les survivants.
  **Tout autre motif : NON CLASSÉ** — motif intégral publié (profil,
  argmin, marges), aucune lecture.
  **PAS contre CREUX, par construction** : une marche monotone est classée
  LISSE et consignée ; seule une descente-remontée résolue est un CREUX.
  **Égalité à l'argmin (N-5, règle 15)** : deux points intérieurs sont ex
  æquo si |Δln s\*| ≤ B_inst de leur paire (tolérance déclarée, entrées
  flottantes) ; le verdict CANYON exige que **tous** les ex æquo du
  minimum soient dans [2.94, 3.06] — sinon NON CLASSÉ, motif publié.
  Aucun seuil de lissité n'existe — le défaut de la v1 (B_lisse calculé
  sur des flancs qui sont dans le canyon, seuil anti-corrélé à l'effet,
  2/5 au test négatif) est retiré avec le seuil lui-même.
- **Fait antérieur, consigné (certification v1, §9)** : dans l'artefact
  M12 (`fa109da9`), entre ω₂ = 2.55 et 2.67, **s\*₄ passe de 2.8812 à
  7.4626 — un facteur 2.59** — seul des trois degrés, sans aucune famille
  de rang (1, 1) au catalogue pour p = 4 dans [1.73, 2.82] ; et le « saut
  de E » de la note P1 en est à 101 % le canal 4 (décomposition
  +1.0155 − 0.2829 + 0.2681 = +1.0007). Conséquence de conception : **le
  fond de s\*₄ n'est pas présumé lisse** sur une largeur de 0.30 ; un pas
  dans la fenêtre M13 romprait une corde sans être un creux — c'est
  précisément ce que le critère ordinal absorbe. Ni preuve, ni oubli.
- **P-M13b — consignation, hors porte.** Le profil complet (9 valeurs ou
  moins), les fenêtres G6 par ligne, la structure sous-seuil éventuelle.
  Matière pour la manche P1, pour A(ω₂), et pour la localisation
  éventuelle du pas de s\*₄.

## 7. Gardes et comptes

- **G1′ (custody)** : rejouer 4|2.80|+1 du run M12 ; **cible nommée au
  champ** : `resultats.carte['4|2.800000000000'].sF` de `m12_results.json`
  (`fa109da9`) **= 8.129205119847189**, écart absolu exigé 0.0 (bit). La
  ligne porte **deux** valeurs distinctes dans l'artefact (carte.sF =
  sP.s = G4.s_dt d'une part ; G4.s_dt2 = 8.130084754569644 de l'autre —
  compte corrigé, cert. v2 §6) ; le champ lève l'ambiguïté (bloquant B-3).
- **G3** : erreur backward ≤ 1e-12 à chaque re-liaison (une seule attendue,
  P = 4 ; consignée avec étiquette — recommandation r4 appliquée).
- **G4** : dt/2 sur la ligne d'échelle de force maximale g·s\*³,
  **déterminée au run** sur les s\* mesurés ; « 3.15 » est une **attente**,
  pas une désignation. Écart en forme ratio |s_dt2/s_dt − 1|, convention
  identifiée sur le primaire M12.
- **G5** : pas final ≤ 1e-5, consigné par ligne.
- **G6** : primauté de s\*, fenêtres et parade d'indice 40 héritées M12.
- **G7** : sans objet (un seul degré) — déclaré, pas omis.
- **G8** : au point 3.00, les deux signes — G8a écart au bit, G8b
  structure ; moitiés grossières attendues vides (p pair).
- **G2** : une recherche neuve à 2g au point 3.00, |K2/K1 − 1| consigné.
- **G9** : constructeurs de consignations complets avant run.
- **Selftest à contre-exemples (obligatoire, bloquant)** : le `--selftest`
  du script **rejoue les cinq profils d'archive** (p = 3, 5, 7 à 2:1 :
  CANYON attendu ; p = 4, 6 : LISSE attendu) à travers le classifieur
  P-M13a et **exige 5/5**, en échec bloquant. Ces profils sont des
  **vecteurs de test du code**, pas des données d'argument : aucun chiffre
  M5/M6 n'entre dans un résultat M13 — déclaré ici. Premier contrôle de la
  campagne à embarquer cinq contre-exemples à réponse connue (esprit
  S_TEMOIN_DIVERGENT du pilote).
- **Comptes dérivés** : recherches attendues = 9 (programme) + 1 (G8, −1)
  + 1 (G1′) + 1 (G4) + 1 (G2) = **13** ; **balayages attendus = 10**
  (9 programme, dont 3.00|+1, + 1 ligne G8 −1 — la ligne 3.00|+1 de G8
  **est** le 5ᵉ point du programme, bloquant B-4 corrigé). Forme
  « comptés + sautés == attendus ».
- **Moteur** : `m9_replication_v1.py` (`c8ed357b`), inchangé. Script :
  gabarit m12_ponctuel, réduit à un degré ; pré-vol à moteur factice
  obligatoire, branches de perte parcourues, **joué par machine 2**
  (détentrice des sources — seule forme opposable).

## 8. Ce que cette manche n'établit pas

Rien sur l'étage A (non visé) ; rien sur les magnitudes de E ; rien sur
8/3 ni 5:2 ; rien hors de [2.85, 3.15] ; et la branche LISSE ne dérive pas
le **mécanisme** de la saturation — elle la mesure. Un NON CLASSÉ ou un
NON CONCLUANT DE GÉOMÉTRIE n'est pas une réfutation de H-SAT.

## 9. Chaîne

Parent : gel M12 v4 `bf9866a7` (cert. `f10ffcf3`) — géométrie de recherche,
fenêtres, parade d'indice 40, convention d'empreinte B. Note source :
`note_derivation_P1_signes_E_v3.md`. Re-dérivation machine 2 :
`p1_re_derivation_machine2_v1.md` (`97c02eab`). Certification croisée v1
(NON CERTIFIÉ, quatre bloquants, correctif P-M13a testé 5/5) :
`m13_certification_croisee_v1.md` (`9ad5689b`), `.py` (`9e780287`),
`.log` (canonique NFC+LF `d8e60b61` ; brute `d788e3c4`, octet 0xa7 Latin-1, décodage utf-8/replace). Artefact custody : `m12_results.json` (`fa109da9`).
L'empreinte de ce gel : au message de livraison ; celle de la version
certifiée fera foi.

---

*Fin du gel M13 v3. Machine 2 : six éditions éditoriales de la cert. v2,
zéro changement de fond — certification à vue, puis feu vert E19.*
"""
# =====================================================================
# m13_saturation_v1.py -- BALAYAGE DE SATURATION : s*(w2) a p = 4 a
# travers 3:1. 13 recherches, 10 balayages, deux minutes.
# ---------------------------------------------------------------------
# Le gel jumeau (docstring ci-dessus) est le bloc CERTIFIE
# gel_m13_balayage_saturation_v3.md (certification a vue, cert. v3,
# empreinte citee E19-1) ; empreinte recalculee au demarrage depuis le
# fichier source (bloc + saut final, convention B) et confrontee a
# SHA_GEL_M13.
# TOUT L'OUTILLAGE est IMPORTE du script pilote CERTIFIE
# m12_pilote_v3.py, charge par empreinte, gel jumeau propre re-verifie a
# l'import (custody transitive) : moteur (charger_moteur -> m9), rebind +
# G3, mesurer, balayer (verbatim lignee), enrichir_g6 (temoins S4/S6,
# double temoin indice 40), g8b, garde de domaine, sauver, comptage
# exhaustif (P.CPT), pas_final.
# ECARTS AU GABARIT m12_ponctuel_v2.py (c5659f52), DECLARES :
#   (i)   UN SEUL degre, UN SEUL rebind : G1' lie P = 4 et le programme,
#         G8, G2 et G4 le partagent (gel Sec.7/G3 : "une seule attendue").
#         Le gabarit re-liait avant G4 ; ici P est inchange, aucune
#         re-liaison -- consigne en meta.declarations.
#   (ii)  G2 et G4 : CONSIGNATION SANS PORTE. Le gel v3 ecrit "consigne"
#         et ne declare AUCUN seuil pour l'un ni l'autre ; le script
#         publie les ecarts et n'exclut pas. Le gel fait foi.
#   (iii) BORNE HI0 = 20 (gel Sec.4) : le bracket du moteur s'elargit tout
#         seul (m9 : LO0=0.05, HI0=6.0, x4 jusqu'a 8 fois) ; la borne du
#         gel est une RECEVABILITE de script -- s > 20 => ligne consignee
#         BORNE_ATTEINTE, non recevable, s conserve, jamais tronque.
#   (iv)  Pas de section E : la quantite de profil est le CLASSEMENT
#         P-M13a ; chaque enregistrement G6 porte un renvoi.
#   (v)   Le champ de duree porte son perimetre DANS SON NOM (lecon
#         D1-2) : duree_des_mesures_carte_s, n explicite.
# OBLIGATIONS TENUES (cert. croisee v3, sequence 1-6) :
#   docstring jumeau extrait du gel et re-verifie au demarrage ; moteur
#   c8ed357b inchange ; --selftest avec LES CINQ CONTRE-EXEMPLES
#   D'ARCHIVE, 5/5, echec bloquant, plus les vecteurs de branches ;
#   pre-vol a moteur factice, TOUTES les branches de perte parcourues --
#   LISSE, CANYON, STRUCTURE SOUS-SEUIL, NON CLASSE, BORNE_ATTEINTE +
#   NON CONCLUANT DE GEOMETRIE, G5 -- en SIX scenarios enchaines par une
#   seule commande ; le pre-vol OPPOSABLE est celui de la machine qui
#   detient les sources.
# ANTI-FRANKEN : aucun chiffre de M5/M6 n'entre dans un resultat M13
# (les cinq profils d'archive sont des VECTEURS DE TEST DU CODE, gel
# Sec.7) ; la seule lecture de m12_results.json est la cible de G1',
# champ nomme.
# =====================================================================

import argparse, hashlib, importlib.util, json, math, os, sys
from fractions import Fraction

import numpy as np

MARQ_DEBUT = "# GEL M13 v3 " + "\u2014 BALAYAGE DE SATURATION"
MARQ_FIN = "puis feu vert E19." + "*"

# ---- empreintes gelees (COMPLETES) -----------------------------------
SHA_GEL_M13 = "26c5a4454f0dff55ab451a9987638cf6d6db4ba1fd2962cd9f0063c38114a2c3"
SHA_PILOTE = "663b17e2955c79c09f1b6c0fb4443cd0c1f98be0db03ef089f5df682018ce905"
SHA_M12_JSON = "fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1"

# ---- protocole (gel M13 v3) ------------------------------------------
POINTS = [2.85, 2.90, 2.94, 2.97, 3.00, 3.03, 3.06, 3.10, 3.15]
DEGRE = 4
G8_POINT = 3.00
G2_POINT = 3.00
G1P_LIGNE = (2.80, 4, +1)                   # ligne du RUN M12, hors fenetre
G1P_CHAMP = "resultats.carte['4|2.800000000000'].sF"
G1P_CIBLE = 8.129205119847189               # gel Sec.7, valeur au bit
HI0_M13 = 20.0                              # gel Sec.4 -- recevabilite script
FEN_LO, FEN_HI = 2.94, 3.06                 # fenetre CANYON, gel Sec.6
K_CHUTE = 10
M_MIN = 7                                   # plancher, gel Sec.5
BORDS = (2.85, 3.15)
D_SITE = 0.06                               # motif STRUCTURE SOUS-SEUIL
TOL_APPART = 1e-09
EPS = 1e-12

# ---- programme fige, forme derivee -----------------------------------
RECH_ATTENDUES = (len(POINTS)               # programme, signe +1
                  + 1                       # G8, signe -1 en 3.00
                  + 1                       # G1'
                  + 1                       # G4
                  + 1)                      # G2
assert RECH_ATTENDUES == 13, "programme fige : 13 recherches (gel Sec.7)"
BAL_ATTENDUS = len(POINTS) + 1              # 3.00|+1 EST le 5e point du programme
assert BAL_ATTENDUS == 10, "balayages : 10 (bloquant B-4 de la cert. v1)"
assert G8_POINT in POINTS and G2_POINT in POINTS
assert all(w in POINTS for w in BORDS)
FOUT = os.path.join("out", "m13_results.json")

SCENARIOS_PREVOL = ("lisse", "canyon", "structure_sous_seuil",
                    "non_classe", "borne_geometrie", "g5")


# =====================================================================
# 1. GEL JUMEAU (convention B) et CHARGEMENT DU PILOTE (custody
#    transitive)
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
        print("Gel jumeau M13 v3 : sha %s -> %s"
              % (h[:16] + "...", "CONCORDANT" if h == SHA_GEL_M13 else "DISCORDANT"))
    if h != SHA_GEL_M13:
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
    P.certifier_gel(verbeux=False)      # custody transitive : gel pilote 03e29c86
    if verbeux:
        print("  gel jumeau du pilote re-verifie (03e29c86...) : CONCORDANT")
    for k in ("recherches", "balayages", "sautees", "balayages_sautes"):
        P.CPT[k] = 0
    return P


def charger_cible_g1p(prevol, rep_prevol, P):
    """Cible de G1' : le CHAMP NOMME du JSON M12, empreinte COMPLETE
    exigee en REEL, ET egalite au bit avec la valeur inscrite au gel --
    le champ est LU, la valeur du gel est CONFRONTEE, rien n'est
    affirme. En PREVOL : source reelle si conforme, sinon synthetique
    avec banniere (repetition)."""
    chemin = os.path.join("out", "m12_results.json")

    def lire(pth):
        j = json.load(open(pth, encoding="utf-8"))
        return float(j["resultats"]["carte"][P.cle(4, 2.80)]["sF"])

    if os.path.exists(chemin) and _sha(chemin) == SHA_M12_JSON:
        v = lire(chemin)
        if v != G1P_CIBLE:
            sys.exit("ARRET G1' : le champ %s lu (%r) != valeur du gel (%r)"
                     % (G1P_CHAMP, v, G1P_CIBLE))
        return v, {"statut": "REELLE", "sha256": SHA_M12_JSON,
                   "champ": G1P_CHAMP, "valeur_gel": G1P_CIBLE}
    if not prevol:
        sys.exit("ARRET : %s absent ou d'empreinte non conforme (exigee %s)"
                 % (chemin, SHA_M12_JSON))
    p = os.path.join(rep_prevol, "m12_results.json")
    if not os.path.exists(p):
        sys.exit("ARRET PREVOL : ni JSON M12 reel conforme, ni synthetique dans %s"
                 % rep_prevol)
    print("=" * 70)
    print("PREVOL : cible G1' SYNTHETIQUE (%s) -- empreinte HORS REGISTRE." % p)
    print("Le pre-vol OPPOSABLE est celui de la machine qui detient les")
    print("sources certifiees ; ceci est une REPETITION.")
    print("=" * 70)
    return lire(p), {"statut": "SYNTHETIQUE_PREVOL", "sha256": _sha(p),
                     "champ": G1P_CHAMP, "valeur_gel": G1P_CIBLE}


# =====================================================================
# 2. MOTEUR FACTICE DU PRE-VOL -- SIX SCENARIOS, TOUTES LES BRANCHES
# =====================================================================

def fabriquer_factice(scenario, val_g1p):
    """Valeurs SYNTHETIQUES, AUCUNE physique. Chaque scenario exerce une
    branche que le run reel pourrait emprunter :
      lisse                : croissant strict -> LISSE (nominal ; G8a/b,
                             G2 K-invariance exacte, G4 ecart 0)
      canyon               : creux resolu en 3.00 -> CANYON
      structure_sous_seuil : 2 exclusions G6 a d <= 0.06, aucune au-dela
                             -> lecture Sec.5 + LISSE sur survivants
      non_classe           : minimum interieur en 2.90 -> NON CLASSE
      borne_geometrie      : s(3.15) = 25 > HI0 -> BORNE_ATTEINTE, bord
                             perdu -> NON CONCLUANT DE GEOMETRIE
      g5                   : pas > plafond en 2.90 -> perte G5 eparse,
                             LISSE sur les 8 survivants"""
    module = {"m": None}

    def base(w):
        if scenario == "canyon":
            return 7.0 - 4.0 * math.exp(-((w - 3.00) / 0.04) ** 2) + 2.0 * (w - 2.85)
        if scenario == "non_classe":
            return 7.0 - 4.0 * math.exp(-((w - 2.90) / 0.03) ** 2) + 2.0 * (w - 2.85)
        if scenario == "borne_geometrie" and abs(w - 3.15) < 1e-9:
            return 25.0
        return 6.0 + 4.0 * (w - 2.85)       # croissant strict, < HI0

    def s_de(p, w, sgn):
        if (w, p, sgn) == G1P_LIGNE:
            return val_g1p
        return base(w)                      # p = 4 : identique aux deux signes

    def chercher(w2, sgn=1, dt=None, g=None):
        m = module["m"]
        v = s_de(m.P, w2, sgn)
        if g is not None and g > 0.075:     # branche 2g : K-invariance exacte
            return v * 2.0 ** (-1.0 / (m.P - 2)), "OK|pas=6.03e-07"
        if scenario == "g5" and abs(w2 - 2.90) < 1e-9:
            return v, "OK|pas=2.00e-05"     # > plafond G5 : tue
        return v, "OK|pas=6.03e-07"

    def integrer(w2, s_arr, sgn=1, dt=None, g=None):
        m = module["m"]
        th = s_de(m.P, w2, sgn)
        if scenario == "structure_sous_seuil" and \
                min(abs(w2 - 2.97), abs(w2 - 3.03)) < 1e-9:
            return np.asarray(s_arr, float) >= 0.5 * th   # explose sous seuil
        return np.asarray(s_arr, float) >= th
    return {"chercher": chercher, "integrer": integrer, "module": module}


# =====================================================================
# 3. ASSEMBLAGE D'UNE LIGNE M13 (p = 4 : un seul signe hors 3.00 --
#    P-M12e ; borne HI0 en recevabilite, jamais en troncature)
# =====================================================================

MOTIF_P4 = ("P-M12e : r_s = 1 par demonstration (M11, reproduite au bit "
            "par le pilote) ; un seul signe au programme")


def appliquer_borne(m):
    """Gel Sec.4 : s > HI0 -> BORNE_ATTEINTE, non recevable, s CONSERVE."""
    if m.get("recevable") and m.get("s") is not None and m["s"] > HI0_M13:
        m["recevable"] = False
        m["motif_exclusion"] = ("BORNE_ATTEINTE : s = %r > HI0 = %r "
                                "(gel M13 v3, Sec.4) -- consigne, jamais "
                                "tronque" % (m["s"], HI0_M13))
    return m


def assembler_ligne_m13(w, v):
    sP, sM = v["sP"], v.get("sM")
    if sM is None:
        v["sM"] = None
        v["sM_motif"] = MOTIF_P4
        if sP["recevable"]:
            v["sF"] = sP["s"]
        else:
            v["sF"] = None
            v["sF_motif"] = sP["motif_exclusion"] or "recherche non recevable"
        v["frag"] = None
        v["frag_motif"] = MOTIF_P4
        v["asym"] = None
        v["asym_motif"] = MOTIF_P4
        return
    if sP["recevable"] and sM["recevable"]:
        v["sF"] = min(sP["s"], sM["s"])
        v["frag"] = 1 if sP["s"] <= sM["s"] else -1
        v["asym"] = sP["s"] / sM["s"]
    else:
        motif = sP["motif_exclusion"] or sM["motif_exclusion"] or "non recevable"
        for ch in ("sF", "frag", "asym"):
            v[ch] = None
            v[ch + "_motif"] = motif


def mecanisme_de(motif):
    return "BORNE_ATTEINTE" if motif.startswith("BORNE_ATTEINTE") else "G5"


# =====================================================================
# 4. CLASSIFIEUR P-M13a (gel Sec.6 ; teste 13/13 par le --selftest de ce
#    fichier. La v1 citait ici une empreinte de module pre-livre
#    (e5754a2e) que machine 2 ne detient pas et ne peut donc pas
#    verifier : mention retiree -- une empreinte citee doit etre
#    verifiable. Ecart au gel Sec.6 sur les ex aequo : voir
#    meta.declarations.classement_ex_aequo.)
# =====================================================================

def classer_pm13a(w2s, s, pas, w_lo=FEN_LO, w_hi=FEN_HI, K=K_CHUTE):
    """P-M13a (gel M13 v3 Sec.6). Entrees : w2s tries, s[w], pas[w] des
    SURVIVANTS. Retour : (verdict, consignation)."""
    c = {"profil": [(w, s[w]) for w in w2s], "fenetre": [w_lo, w_hi]}
    ln = {w: math.log(s[w]) for w in w2s}
    n = len(w2s)
    croiss = all(ln[w2s[i]] < ln[w2s[i + 1]] for i in range(n - 1))
    decroiss = all(ln[w2s[i]] > ln[w2s[i + 1]] for i in range(n - 1))
    if croiss or decroiss:
        c["motif"] = ("strictement monotone ("
                      + ("croissant" if croiss else "decroissant") + ")")
        return "LISSE", c
    interieur = w2s[1:-1]
    B = lambda a, b: pas[a] / s[a] + pas[b] / s[b]
    w_min = min(interieur, key=lambda w: ln[w])
    exaequo = sorted(w for w in interieur if abs(ln[w] - ln[w_min]) <= B(w, w_min))
    c["argmin"], c["ex_aequo"] = w_min, exaequo
    c["resolution_bloc"] = ("chute testee aux deux bords du bloc d'ex aequo "
                            "contre leurs voisins exterieurs (N-5)")
    if not all(w_lo <= w <= w_hi for w in exaequo):
        c["motif"] = "ex aequo/argmin hors fenetre [%s, %s]" % (w_lo, w_hi)
        return "NON CLASSE", c
    wl, wr = exaequo[0], exaequo[-1]
    vg = max(w for w in w2s if w < wl)
    vd = min(w for w in w2s if w > wr)
    marges, ok = {}, True
    for bord, voisin, cote in ((wl, vg, "gauche"), (wr, vd, "droite")):
        b = B(bord, voisin)
        marges[cote] = (ln[voisin] - ln[bord]) / (K * b)
        if not (ln[bord] <= ln[voisin] - K * b):
            ok = False
    c["marges_sur_10B"] = marges
    if ok:
        c["motif"] = "minimum interieur en fenetre, chute resolue des deux cotes"
        return "CANYON", c
    c["motif"] = "chute non resolue par l'instrument"
    return "NON CLASSE", c


def lire_pertes_site(pertes_g6):
    """Gel Sec.5 : >= 2 exclusions G6 a d <= 0.06 de 3.00 et aucune
    au-dela -> STRUCTURE SOUS-SEUIL AU SITE 3:1."""
    site = sorted(w for w in pertes_g6 if abs(w - 3.00) <= D_SITE + EPS)
    hors = sorted(w for w in pertes_g6 if abs(w - 3.00) > D_SITE + EPS)
    lu = len(site) >= 2 and not hors
    return {"lecture": ("STRUCTURE SOUS-SEUIL AU SITE 3:1" if lu
                        else "attrition simple" if pertes_g6 else "aucune perte G6"),
            "site_d_inf_0.06": site, "hors_site": hors,
            "note": "consigne SEPAREMENT de P-M13a ; compatible avec toute "
                    "issue de P-M13a, y compris NON CLASSE (gel Sec.5)"}


# =====================================================================
# 5. G9 -- COUVERTURE M13 (champ existant, null motive)
# =====================================================================

REQUIS_MESURE = ("s", "note", "recevable", "motif_exclusion", "duree_s")
REQUIS_CARTE = ("sP", "sM", "sF", "frag", "asym")
NULLABLES_CARTE = ("sM", "sF", "frag", "asym")
REQUIS_CLASSEMENT = ("verdict", "consignation", "plancher")


def g9_verifier_m13(res):
    defauts = []
    for k, v in res["resultats"]["carte"].items():
        for ch in REQUIS_CARTE:
            if ch not in v:
                defauts.append("carte[%s] : champ absent %s" % (k, ch))
                continue
            if v[ch] is None:
                if ch not in NULLABLES_CARTE:
                    defauts.append("carte[%s] : %s null non admissible" % (k, ch))
                elif not v.get(ch + "_motif"):
                    defauts.append("carte[%s] : %s null SANS motif" % (k, ch))
        for sk in ("sP", "sM"):
            m = v.get(sk)
            if not isinstance(m, dict):
                continue
            for ch in REQUIS_MESURE:
                if ch not in m:
                    defauts.append("carte[%s].%s : champ absent %s" % (k, sk, ch))
            if m.get("s") is None and not m.get("motif_exclusion"):
                defauts.append("carte[%s].%s : s null SANS motif" % (k, sk))
    for k, b in res["resultats"]["G6"].items():
        for ch in ("n_gros", "n_fin", "exclue", "ilots", "ilots_au_dessus",
                   "premiere_retombee_en_s", "pas_final_recherche",
                   "ecart_absolu_indice_40_au_seuil",
                   "indice_40_compte_comme_sous_seuil"):
            if ch not in b:
                defauts.append("G6[%s] : champ absent %s" % (k, ch))
                continue
            if b[ch] is None and not b.get(ch + "_motif"):
                defauts.append("G6[%s] : %s null SANS motif" % (k, ch))
    cl = res["resultats"].get("classement")
    if cl is not None:
        for ch in REQUIS_CLASSEMENT:
            if ch not in cl:
                defauts.append("classement : champ absent %s" % ch)
    return defauts


def _record_synthetique(P):
    """G9 avant-run : une ligne double signe (3.00), une ligne simple
    signe, un balayage, un classement -- par LES MEMES constructeurs."""
    from types import SimpleNamespace
    res = {"resultats": {"carte": {}, "G6": {}, "classement": None}}
    fake = {"s": 1.234, "note": "OK|pas=6.03e-07", "recevable": True,
            "motif_exclusion": "", "duree_s": 0.0}
    v2s = {"sP": dict(fake), "sM": dict(fake)}
    assembler_ligne_m13(9.99, v2s)
    res["resultats"]["carte"][P.cle(4, 9.99)] = v2s
    v1s = {"sP": dict(fake, s=1.334)}
    assembler_ligne_m13(9.98, v1s)
    res["resultats"]["carte"][P.cle(4, 9.98)] = v1s
    ns = SimpleNamespace(LO0=0.05,
                         integrer=lambda w2, s, sgn=1, dt=None, g=None:
                         np.asarray(s, float) >= 1.234)
    cpt0 = dict(P.CPT)
    bal = P.enrichir_g6(P.balayer(ns, 9.99, +1, 1.234), 1.234, fake["note"])
    P.CPT.update(cpt0)
    res["resultats"]["G6"][P.cle(4, 9.99) + "|+1"] = bal
    v, c = classer_pm13a([1.0, 2.0, 3.0], {1.0: 2.0, 2.0: 2.1, 3.0: 2.2},
                         {1.0: 1e-6, 2.0: 1e-6, 3.0: 1e-6}, 1.5, 2.5)
    res["resultats"]["classement"] = {"verdict": v, "consignation": c,
                                      "plancher": {"statut": "synthetique"}}
    return res


# =====================================================================
# 6. SELFTEST -- il mord : cinq contre-exemples d'archive (bloquant,
#    gel Sec.7) + vecteurs de branches (module pre-livre, 13/13)
# =====================================================================

PAS_PLAFOND = 1e-5   # plafond G5 : B_inst majore, sens defavorable au CANYON

ARCHIVES = {  # vecteurs de TEST DU CODE (M5/M6) -- jamais donnees d'argument
    3: ([1.90, 1.95, 2.00, 2.05, 2.10], [1.9202, 1.1140, 0.5243, 3.2470, 33.8170], "CANYON"),
    4: ([1.90, 1.95, 2.00, 2.05, 2.10], [2.3997, 2.5173, 2.6019, 2.6817, 2.7545], "LISSE"),
    5: ([1.90, 1.95, 2.00, 2.05, 2.10], [0.6131, 0.5204, 0.3749, 0.8303, 1.1383], "CANYON"),
    6: ([1.90, 1.95, 2.00, 2.05, 2.10], [0.9403, 0.9684, 1.0143, 1.0314, 1.1022], "LISSE"),
    7: ([1.90, 1.95, 2.00, 2.05, 2.10], [0.5145, 0.4740, 0.3923, 0.6556, 0.7980], "CANYON"),
}


def _prof(vals):
    return dict(zip(POINTS, vals))


SYNTHETIQUES = [
    ("croissant strict (attendu du redacteur, gel Sec.3)",
     POINTS, _prof([2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6]), "LISSE"),
    ("marche monotone (PAS, fait s*4 -- jamais un CREUX)",
     POINTS, _prof([2.0, 2.1, 2.2, 2.3, 5.9, 6.0, 6.1, 6.2, 6.3]), "LISSE"),
    ("decroissant strict",
     POINTS, _prof([3.6, 3.4, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0]), "LISSE"),
    ("creux resolu au site -> CANYON",
     POINTS, _prof([3.0, 2.9, 2.4, 1.8, 1.2, 1.9, 2.5, 3.1, 3.3]), "CANYON"),
    ("ex aequo EXACT (3.00, 3.03), tous en fenetre -> CANYON",
     POINTS, _prof([3.0, 2.9, 2.4, 1.8, 1.2, 1.2, 2.5, 3.1, 3.3]), "CANYON"),
    ("ex aequo a cheval (3.06 dedans, 3.10 dehors) -> NON CLASSE",
     POINTS, _prof([3.0, 2.9, 2.8, 2.7, 2.6, 2.5, 1.2, 1.2, 3.3]), "NON CLASSE"),
    ("minimum interieur HORS fenetre (2.90) -> NON CLASSE",
     POINTS, _prof([3.0, 1.2, 2.4, 2.6, 2.8, 2.9, 3.0, 3.1, 3.3]), "NON CLASSE"),
    ("chute non resolue : voisins a 3e-5 du min, entre B et 10B",
     POINTS, _prof([3.0 * math.exp(k) for k in
                    (1e-4, 7e-5, 4e-5, 3e-5, 0.0, 3e-5, 4e-5, 7e-5, 1e-4)]),
     "NON CLASSE"),
]


def selftest_classifieur():
    echecs = 0
    print("[A] CINQ CONTRE-EXEMPLES D'ARCHIVE (bloquant, 5/5 exige -- gel Sec.7)")
    print("    vecteurs de test du code ; aucun chiffre M5/M6 n'entre dans un")
    print("    resultat M13 ; fenetre analogue [1.96, 2.04] ; pas = plafond G5.")
    for p in sorted(ARCHIVES):
        ws, vals, attendu = ARCHIVES[p]
        s = dict(zip(ws, vals))
        pas = {w: PAS_PLAFOND for w in ws}
        v, c = classer_pm13a(ws, s, pas, 1.96, 2.04)
        ok = (v == attendu)
        echecs += (not ok)
        m = c.get("marges_sur_10B")
        mm = "" if not m else "  marges/10B: %.3g, %.3g" % (m["gauche"], m["droite"])
        print("  p=%d  attendu %-10s obtenu %-10s %s%s"
              % (p, attendu, v, "OK" if ok else "ECHEC", mm))
    print("[B] %d VECTEURS SYNTHETIQUES (couverture des branches, bloquant)"
          % len(SYNTHETIQUES))
    for nom, ws, s, attendu in SYNTHETIQUES:
        pas = {w: PAS_PLAFOND for w in ws}
        v, c = classer_pm13a(ws, s, pas)
        ok = (v == attendu)
        echecs += (not ok)
        print("  [%s] %s\n          -> %s (%s)"
              % ("OK   " if ok else "ECHEC", nom, v, c["motif"]))
    n = len(ARCHIVES) + len(SYNTHETIQUES)
    print("classifieur : %d/%d" % (n - echecs, n))
    return echecs


def selftest():
    from types import SimpleNamespace
    print("=" * 70)
    print("SELFTEST m13_saturation_v1.py")
    print("=" * 70)
    certifier_gel()
    P = charger_pilote(verbeux=False)
    print("pilote importe par empreinte, gel pilote re-verifie")

    print("\n[1] programme fige, DERIVE (jamais affirme)")
    assert RECH_ATTENDUES == 13 and BAL_ATTENDUS == 10
    assert len(POINTS) == 9 and len(set(POINTS)) == 9
    assert POINTS == sorted(POINTS)
    print("    13 recherches (9+1+1+1+1), 10 balayages (9 programme + 1 G8) ;")
    print("    9 points tries, distincts")

    print("\n[2] grille et fenetre : centiemes exacts, symetrie, bords propres")
    cents = [round(w * 100) for w in POINTS]
    assert all(abs(w - c / 100.0) <= TOL_APPART for w, c in zip(POINTS, cents))
    assert min(b - a for a, b in zip(cents, cents[1:])) == 3
    assert [c - 300 for c in cents] == [-15, -10, -6, -3, 0, 3, 6, 10, 15]
    assert min(abs(G1P_LIGNE[0] - w) for w in POINTS) > TOL_APPART
    print("    espacement minimal 0.03 ; ecarts a 3.00 symetriques ; G1'")
    print("    (2.80) hors fenetre PAR CONSTRUCTION -- exempte de rule-11")

    print("\n[3] classifieur P-M13a : archives 5/5 + branches (BLOQUANT)")
    ech = selftest_classifieur()
    assert ech == 0, "%d echec(s) au classifieur -- BLOQUANT (gel Sec.7)" % ech

    print("\n[4] geometrie de balayage, via le module PILOTE importe")
    ns = SimpleNamespace(LO0=0.05,
                         integrer=lambda w2, s, sgn=1, dt=None, g=None:
                         np.zeros(np.asarray(s).shape, bool))
    cpt0 = dict(P.CPT)
    assert P.balayer(ns, 9.9, +1, 0.47)["n_gros"] == 160
    assert P.balayer(ns, 9.9, +1, 2.05)["n_gros"] == 177
    assert P.balayer(ns, 9.9, +1, 2.05)["n_fin"] == 76
    P.CPT.update(cpt0)
    assert not P.verifier_domaine(1.0 / 18.0)[0] and P.verifier_domaine(0.0556)[0]
    print("    vecteurs 160 / 177 / 76 ; domaine strict s* > 1/18")

    print("\n[5] borne HI0 : recevabilite, s conserve, mecanisme nomme")
    m = appliquer_borne({"s": 25.0, "note": "OK|pas=6.03e-07",
                         "recevable": True, "motif_exclusion": "", "duree_s": 0.0})
    assert not m["recevable"] and m["s"] == 25.0
    assert m["motif_exclusion"].startswith("BORNE_ATTEINTE")
    assert mecanisme_de(m["motif_exclusion"]) == "BORNE_ATTEINTE"
    m2 = appliquer_borne({"s": 8.2, "recevable": True, "motif_exclusion": ""})
    assert m2["recevable"]
    print("    s=25 -> non recevable, s conserve ; s=8.2 -> intact")

    print("\n[6] lecture des pertes (gel Sec.5) : le motif mord et ne deborde pas")
    l1 = lire_pertes_site({2.97, 3.03})
    l2 = lire_pertes_site({2.97, 3.10})
    l3 = lire_pertes_site({2.97})
    l4 = lire_pertes_site(set())
    assert l1["lecture"].startswith("STRUCTURE")
    assert not l2["lecture"].startswith("STRUCTURE")
    assert not l3["lecture"].startswith("STRUCTURE")
    assert l4["lecture"] == "aucune perte G6"
    print("    {2.97,3.03} -> STRUCTURE ; {2.97,3.10} -> non ; {2.97} -> non ;")
    print("    vide -> aucune perte")

    print("\n[7] plancher : m >= 7 ET les deux bords survivants")
    ok_p = plancher_ok(POINTS)
    ko_m = plancher_ok(POINTS[:6])
    ko_b = plancher_ok([w for w in POINTS if w != 3.15])
    assert ok_p[0] and not ko_m[0] and not ko_b[0]
    print("    9 survivants -> OK ; 6 -> NON CONCLUANT ; bord 3.15 perdu -> NON")

    print("\n[8] G9-M13 : couverture, et defauts DETECTES")
    r = _record_synthetique(P)
    assert g9_verifier_m13(r) == []
    r2 = _record_synthetique(P)
    del r2["resultats"]["carte"][P.cle(4, 9.99)]["sF"]
    r3 = _record_synthetique(P)
    r3["resultats"]["carte"][P.cle(4, 9.98)]["sM"] = None
    r3["resultats"]["carte"][P.cle(4, 9.98)].pop("sM_motif", None)
    d2, d3 = g9_verifier_m13(r2), g9_verifier_m13(r3)
    assert d2 and d3
    print("    conforme : 0 ; sF supprime : %d ; sM null nu : %d" % (len(d2), len(d3)))

    print("\n[9] G1' : l'exactitude au bit est testable ; cible du gel litterale")
    # CORRECTION machine 2 (cert. script v1, bloquant) : la v1 ecrivait
    # 8.129205119847188 comme "valeur differente" -- or l'ulp a 8.129 vaut
    # 1.7763568394002505e-15 et l'ecart ecrit valait 1e-15, SOUS l'ulp : les
    # deux litteraux sont LE MEME double (0x1.042272c68705ap+3). Le test
    # negatif ne testait rien. Forme DERIVEE, juste meme si la cible change.
    voisin_bas = math.nextafter(G1P_CIBLE, -math.inf)
    voisin_haut = math.nextafter(G1P_CIBLE, math.inf)
    assert (G1P_CIBLE - 8.129205119847189) == 0.0
    assert voisin_bas != G1P_CIBLE and voisin_haut != G1P_CIBLE
    assert (G1P_CIBLE - voisin_bas) != 0.0
    assert (G1P_CIBLE - voisin_haut) != 0.0
    assert (G1P_CIBLE - 8.129205119847188) == 0.0, \
        "temoin du defaut v1 : ce litteral EST le meme double que la cible"
    print("    egal -> 0.0 exact ; voisins %r / %r -> detectes (ulp = %r)"
          % (voisin_bas, voisin_haut, math.ulp(G1P_CIBLE)))
    print("    temoin embarque : 8.129205119847188 est le MEME double (defaut v1)")

    print("\nSELFTEST : TOUT PASSE (9 sections).")
    return 0


def plancher_ok(survivants):
    if len(survivants) < M_MIN:
        return False, "m = %d < %d" % (len(survivants), M_MIN)
    for b in BORDS:
        if b not in survivants:
            return False, "bord de fenetre %.2f perdu" % b
    return True, "m = %d >= %d, bords (%.2f, %.2f) survivants" % (
        len(survivants), M_MIN, BORDS[0], BORDS[1])


# =====================================================================
# 7. PIPELINE (un scenario = un JSON ; le REEL est un scenario unique)
# =====================================================================

def run_pipeline(P, a, val_g1p, meta_g1p, fout, mode, scenario=None):
    for k in ("recherches", "balayages", "sautees", "balayages_sautes"):
        P.CPT[k] = 0
    factice = fabriquer_factice(scenario, val_g1p) if scenario else None
    m9 = P.charger_moteur(a.moteur, factice=factice)
    d = g9_verifier_m13(_record_synthetique(P))
    if d:
        sys.exit("ARRET G9 (avant le run) :\n  " + "\n  ".join(d))
    print("G9 avant-run : constructeurs de consignations COMPLETS.")
    for w in (G8_POINT, G2_POINT):
        if min(abs(w - x) for x in POINTS) > TOL_APPART:
            sys.exit("ARRET rule-11 : %r hors programme" % w)
    print("rule-11 : 9 points du programme, ancres G8/G2 (3.00) incluses ;")
    print("  G1' rejoue une ligne du RUN M12 (2.80) -- hors fenetre par construction.")

    res = {"meta": {"gel_sha256_bloc": SHA_GEL_M13,
                    "pilote_sha256": SHA_PILOTE,
                    "m12_json_sha256_attendu": SHA_M12_JSON,
                    "cible_g1p": meta_g1p, "mode": mode,
                    "convention_empreinte": "B -- bloc saut final inclus = fichier",
                    "declarations": {
                        "etage_cible": "H-SAT et etage B au site 3:1 ; "
                                       "l'etage A n'est PAS teste (gel Sec.1)",
                        "rebind_unique": "P = 4 unique : G1' lie le "
                                         "programme, G8, G2 et G4 ; aucune "
                                         "re-liaison avant G4 (P inchange) "
                                         "-- ecart au gabarit, declare",
                        "borne": "HI0 = 20 en RECEVABILITE de script ; "
                                 "BORNE_ATTEINTE consigne, s conserve, "
                                 "jamais tronque (gel Sec.4)",
                        "G8": "3.00, deux signes ; moitie grossiere "
                              "ATTENDUE VIDE a p=4 (pre-declare)",
                        "G2_G4_sans_porte": "le gel v3 ecrit CONSIGNE et ne "
                              "declare aucun seuil pour G2 ni G4 : ecarts "
                              "publies, aucune exclusion -- le gel fait foi",
                        "selftest_vecteurs": "5 profils d'archive = vecteurs "
                              "de TEST DU CODE ; aucun chiffre M5/M6 dans "
                              "un resultat M13 (gel Sec.7)",
                        "provenance_attente": "les trois points p=4 de M12 "
                              "(2.72-2.80) motivent l'attente LISSE "
                              "(gel Sec.3, regle de provenance)",
                        "classement_emplacement": "quantite de PROFIL : vit "
                              "dans resultats.classement ; chaque G6 porte "
                              "un renvoi",
                        "classement_ex_aequo": "AJOUT DECLARE a la regle "
                              "gelee (cert. script v1, machine 2) : le gel "
                              "Sec.6 ecrit 'la chute resolue pour chacun des "
                              "deux voisins survivants' DE L'ARGMIN ; le "
                              "script teste les bords du BLOC d'ex aequo "
                              "contre leurs voisins EXTERIEURS. Sans ex "
                              "aequo les deux lectures coincident. Avec, "
                              "elles divergent (le gel litteral rend NON "
                              "CLASSE, le script CANYON) : direction NON "
                              "conservatrice, motif = la lecture litterale "
                              "viderait N-5 de son sens, un creux a fond "
                              "plat restant un creux. Cas INATTEIGNABLE : "
                              "tolerance d'ex aequo instrumentale (~1e-6 "
                              "relatif) contre un ecart inter-points de 3 a "
                              "4 ordres au-dessus, meme au fond d'un creux. "
                              "Champ 'resolution_bloc' publie par "
                              "consignation.",
                        "editions_machine2": "le script a ete edite par "
                              "machine 2 apres sa certification v1, sur "
                              "demande explicite : [9] du selftest "
                              "(nextafter), cette declaration, denominateur "
                              "d'attrition, commentaire d'empreinte non "
                              "verifiable. AUCUNE edition ne touche le "
                              "chemin de mesure, les gardes, le "
                              "classifieur, la geometrie ni le gel jumeau. "
                              "Ecart a la repartition machine1/machine2, "
                              "CONSIGNE."},
                    "G3_par_degre": [], "gardes": [], "exclusions": {}},
           "resultats": {"carte": {}, "G6": {}, "G8": {}, "G2": {}, "G4": {},
                         "G1p": {}, "classement": None,
                         "structure_sous_seuil": None},
           "verdict": {}, "resume": {}}
    jg3 = res["meta"]["G3_par_degre"]
    if scenario:
        res["meta"]["prevol_scenario"] = scenario
    carte = res["resultats"]["carte"]
    excl = res["meta"]["exclusions"]

    def sauve():
        P.sauver(res, fout)

    def plan_signes(w):
        return [(+1, "sP")] + ([(-1, "sM")] if abs(w - G8_POINT) <= TOL_APPART
                               else [])

    # ---- G1' D'ABORD (bloquante ; UNIQUE re-liaison P = 4) ------------
    print("\n--- G1' custody : rejeu au bit de (2.80, p=4, +1) ---")
    P.rebind(m9, 4, jg3)
    if jg3:
        jg3[-1]["etiquette"] = ("G1' (rejeu 4|2.80|+1) -- lie aussi le "
                                "programme, G8, G2 et G4 (P=4 unique, gel Sec.7)")
    r = P.mesurer(m9, 2.80, +1)
    ec = (r["s"] - val_g1p) if r["s"] is not None else None
    res["resultats"]["G1p"] = {"ligne": "4|2.80|+1", "champ_cible": G1P_CHAMP,
                               "mesure": r, "cible": val_g1p,
                               "ecart_absolu": ec,
                               "verdict": "PASSE" if ec == 0.0 else "ECHEC"}
    sauve()
    if ec != 0.0:
        sys.exit("ARRET G1' : ecart %r != 0 -- la chaine de custody est rompue." % ec)
    print("  ecart absolu = 0.0 EXACT : custody intacte.")

    # ---- programme : 9 mesures (+1), G8 (-1) en 3.00, borne HI0 -------
    print("\n--- programme p = 4, neuf points, borne HI0 = %g ---" % HI0_M13)
    for w in POINTS:
        v = carte.setdefault(P.cle(4, w), {})
        for sgn, k in plan_signes(w):
            m = appliquer_borne(P.mesurer(m9, w, sgn))
            if sgn < 0:
                m["role"] = "regression_G8"
            v[k] = m
            sauve()
        assembler_ligne_m13(w, v)
        if v["sF"] is None:
            mot = v["sF_motif"]
            excl.setdefault(P.cle(4, w), []).append(
                "%s : %s" % (mecanisme_de(mot), mot))
        if abs(w - G8_POINT) <= TOL_APPART and v.get("sM") \
                and v["sP"]["recevable"] and v["sM"]["recevable"]:
            e8 = v["sP"]["s"] - v["sM"]["s"]
            res["resultats"]["G8"].setdefault(P.cle(4, w), {})["G8a"] = {
                "ecart_absolu": e8, "verdict": "OK" if e8 == 0.0 else "ECHEC"}
            if e8 != 0.0:
                sauve()
                sys.exit("ARRET G8a : sP - sM = %r != 0 en w2=%.2f" % (e8, w))
        sauve()

    # ---- balayages : 10 lignes, G6, G8b -------------------------------
    for w in POINTS:
        v = carte[P.cle(4, w)]
        plan = plan_signes(w)
        if not all(v[k]["recevable"] for _, k in plan):
            P.CPT["balayages_sautes"] += len(plan)
            res["meta"]["gardes"].append(
                "G6 %s : %d balayage(s) SAUTE(S), ligne non recevable"
                % (P.cle(4, w), len(plan)))
            sauve()
            continue
        bg = {}
        for sgn, k in plan:
            ok, motif = P.verifier_domaine(v[k]["s"])
            if not ok:
                res["meta"]["gardes"].append("DOMAINE %s : %s" % (P.cle(4, w), motif))
                sauve()
                sys.exit("ARRET domaine : " + motif)
            bal = P.balayer(m9, w, sgn, v[k]["s"])
            P.enrichir_g6(bal, v[k]["s"], v[k]["note"])
            bal["g8b_grossier_attendu"] = ("VIDE (pre-declare avant mesure, "
                                           "gel Sec.7/G8)")
            if bal["gros_explosifs"] > 0:
                res["meta"]["gardes"].append(
                    "FAIT NEUF : moitie grossiere a MORDU a p=4, w2=%.2f "
                    "sgn=%+d (%d explosif(s))" % (w, sgn, bal["gros_explosifs"]))
            bal["classement_renvoi"] = ("quantite de PROFIL : voir "
                                        "resultats.classement")
            bg[k] = bal
            res["resultats"]["G6"][P.cle(4, w) + "|%+d" % sgn] = bal
            if bal["exclue"]:
                excl.setdefault(P.cle(4, w), []).append(
                    "G6 sgn=%+d explosion sous seuil" % sgn)
        if abs(w - G8_POINT) <= TOL_APPART and len(bg) == 2:
            g8 = P.g8b(bg["sP"], bg["sM"])
            res["resultats"]["G8"].setdefault(P.cle(4, w), {})["G8b"] = g8
            if (g8["grossier"]["deviations"] != 0 or g8["fin"]["deviations"] != 0
                    or not g8["ilots_identiques"] or not g8["retombee_identique"]):
                sauve()
                sys.exit("ARRET G8b : masques non identiques en w2=%.2f" % w)
        sauve()

    # ---- G2 : une recherche a 2g, CONSIGNATION SANS PORTE -------------
    base = carte[P.cle(4, G2_POINT)].get("sP")
    r2 = P.mesurer(m9, G2_POINT, +1, g=2 * m9.G_REF)
    if base and base["recevable"] and r2["recevable"]:
        ratio = 2.0 * (r2["s"] / base["s"]) ** (DEGRE - 2)
        rm = None
    else:
        ratio, rm = None, "base ou 2g non recevable"
    res["resultats"]["G2"]["4|+1"] = {
        "w2": G2_POINT, "g": "2g", "mesure": r2, "K2_sur_K1": ratio,
        "ratio_motif": rm,
        "statut": "CONSIGNE (le gel v3 ne declare pas de seuil ; aucune "
                  "exclusion -- meta.declarations.G2_G4_sans_porte)"}
    sauve()

    # ---- G4 : dt/2 sur l'echelle de force maximale, AU RUN ------------
    print("\n--- G4 : dt/2 sur l'echelle de force maximale (determinee au run) ---")
    best = None
    for w in POINTS:
        v = carte[P.cle(4, w)]
        if v["sP"]["recevable"]:
            e = m9.G_REF * v["sP"]["s"] ** (DEGRE - 1)
            if best is None or e > best[0]:
                best = (e, w, v["sP"]["s"])
    if best is None:
        P.CPT["sautees"] += 1
        res["meta"]["gardes"].append("G4 : recherche SAUTEE (rien de recevable)")
    else:
        _, w4, sref = best
        r4 = P.mesurer(m9, w4, +1, dt=m9.DT / 2)
        ec4 = abs(r4["s"] / sref - 1.0) if r4["recevable"] else None
        res["resultats"]["G4"] = {
            "p": DEGRE, "w2": w4, "sgn": +1, "s_dt": sref, "s_dt2": r4["s"],
            "duree_s": r4["duree_s"], "ecart": ec4,
            "ecart_motif": None if ec4 is not None else r4["motif_exclusion"],
            "forme": "|s_dt2/s_dt - 1| (ratio, convention du primaire M12)",
            "statut": "CONSIGNE (le gel v3 ne declare pas de seuil ; "
                      "aucune exclusion)",
            "attente_gel": "ligne attendue : 3.15 (gel Sec.7 -- attente, "
                           "pas designation)"}
        print("  G4 sur 4|%.2f|+1 : ecart %s" % (w4,
              "%.3e" % ec4 if ec4 is not None else "NON EVALUABLE"))
    sauve()

    # ---- pertes, plancher, classement, lectures -----------------------
    print("\n--- classement P-M13a sur les survivants ---")
    survivants = [w for w in POINTS
                  if carte[P.cle(4, w)]["sF"] is not None
                  and P.cle(4, w) not in excl]
    pertes_g6 = {w for w in POINTS
                 if any(s.startswith("G6") for s in excl.get(P.cle(4, w), []))}
    res["resultats"]["structure_sous_seuil"] = lire_pertes_site(pertes_g6)
    okp, motp = plancher_ok(survivants)
    if not okp:
        res["resultats"]["classement"] = {
            "verdict": "NON CONCLUANT DE GEOMETRIE",
            "consignation": {"motif": motp,
                             "survivants": survivants},
            "plancher": {"statut": "ECHEC", "motif": motp}}
        va = "NON CONCLUANT DE GEOMETRIE"
        detail = motp + " -- aucune lecture ; la manche suivante redessine " \
                        "la fenetre (gel Sec.5)"
    else:
        smap = {w: carte[P.cle(4, w)]["sF"] for w in survivants}
        pmap = {w: P.pas_final(carte[P.cle(4, w)]["sP"]["note"])
                for w in survivants}
        va, cons = classer_pm13a(survivants, smap, pmap)
        res["resultats"]["classement"] = {
            "verdict": va, "consignation": cons,
            "plancher": {"statut": "OK", "motif": motp}}
        detail = cons["motif"]
    verdict = {"m": len(survivants), "P_M13a": va, "detail": detail,
               "lecture_pertes": res["resultats"]["structure_sous_seuil"]["lecture"]}
    if mode == "PREVOL":
        verdict = {("PREVOL_SYNTHETIQUE_" + k): v for k, v in verdict.items()}
        print("=" * 70)
        print("PREVOL : le 'verdict' ci-dessous est SYNTHETIQUE -- AUCUNE PHYSIQUE.")
        print("=" * 70)
    res["verdict"] = verdict

    # ---- resume -------------------------------------------------------
    pertes = dict(excl)
    ventil = {g: sum(1 for ms in pertes.values()
                     if any(s.startswith(g) for s in ms))
              for g in ("G5", "G6", "BORNE_ATTEINTE")}
    durees = [carte[P.cle(4, w)][k]["duree_s"]
              for w in POINTS for _, k in plan_signes(w)]
    res["resume"] = {
        "m": len(survivants), "points_perdus": sorted(pertes),
        "pertes_par_mecanisme": ventil,
        "pertes_par_mecanisme_note": "ventilation par MECANISME, pas une "
            "partition (une ligne peut porter plusieurs motifs)",
        "attrition_9": {"points_perdus": len(pertes), "sur": len(POINTS),
                        "perimetre": "POINTS du programme perdus sur les 9 "
                                     "points ; le denominateur etait 10 "
                                     "(balayages) en v1 -- unites melangees, "
                                     "corrige (cert. script v1, N-1)",
                        "statut": "FAIT consigne"},
        "duree_des_mesures_carte_s": {"n": len(durees),
                                      "total": float(sum(durees)),
                                      "moyenne": float(sum(durees) /
                                                       max(1, len(durees))),
                                      "perimetre": "les mesures de la carte "
                                          "(programme + G8) ; G1', G2, G4 "
                                          "non compris -- le nom porte le "
                                          "perimetre (lecon D1-2)"},
    }
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
    d = g9_verifier_m13(res)
    if d:
        sauve()
        sys.exit("ARRET G9 (apres run) : %d defaut(s) :\n  %s"
                 % (len(d), "\n  ".join(d)))
    sauve()
    if P.CPT["recherches"] + P.CPT["sautees"] != RECH_ATTENDUES:
        sys.exit("ARRET : %d + %d recherches != %d"
                 % (P.CPT["recherches"], P.CPT["sautees"], RECH_ATTENDUES))
    if P.CPT["balayages"] + P.CPT["balayages_sautes"] != BAL_ATTENDUS:
        sys.exit("ARRET : %d + %d balayages != %d"
                 % (P.CPT["balayages"], P.CPT["balayages_sautes"], BAL_ATTENDUS))
    print("\nEcrit : %s" % fout)
    print("Recherches : %d + %d = %d / %d | balayages : %d + %d = %d / %d"
          % (P.CPT["recherches"], P.CPT["sautees"],
             P.CPT["recherches"] + P.CPT["sautees"], RECH_ATTENDUES,
             P.CPT["balayages"], P.CPT["balayages_sautes"],
             P.CPT["balayages"] + P.CPT["balayages_sautes"], BAL_ATTENDUS))
    print("m = %d | %s" % (len(survivants),
          res["verdict"].get("P_M13a",
              res["verdict"].get("PREVOL_SYNTHETIQUE_P_M13a"))))
    print("lecture des pertes : %s"
          % res["resultats"]["structure_sous_seuil"]["lecture"])
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

    bloc, hgel = certifier_gel()
    P = charger_pilote(a.pilote)
    val_g1p, meta_g1p = charger_cible_g1p(a.prevol, a.sources_prevol, P)

    if a.prevol:
        print("=" * 70)
        print("PREVOL : %d scenarios enchaines -- toutes les branches de "
              "perte" % len(SCENARIOS_PREVOL))
        print("=" * 70)
        for sc in SCENARIOS_PREVOL:
            fout = os.path.join("out", "m13_PREVOL_%s.json" % sc)
            assert fout != FOUT, "le pre-vol n'ecrit JAMAIS le fichier reel"
            print("\n" + "#" * 70)
            print("# SCENARIO PREVOL : %s" % sc)
            print("#" * 70)
            run_pipeline(P, a, val_g1p, meta_g1p, fout, "PREVOL", scenario=sc)
        print("\nPREVOL : %d scenarios termines." % len(SCENARIOS_PREVOL))
        return

    run_pipeline(P, a, val_g1p, meta_g1p, FOUT, "REEL")


if __name__ == "__main__":
    main()
