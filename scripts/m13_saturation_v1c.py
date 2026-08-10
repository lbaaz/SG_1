r"""# GEL M13b v1 — AMENDEMENTS AU GEL M13 v3 (`26c5a445`, certifié)

**Machine 1, 02/08/2026. FORME DIFF** : tout ce qui n'est pas amendé
ci-dessous vaut TEL QUEL au gel M13 v3 — géométrie de balayage, gardes,
convention B, moteur `c8ed357b`, pilote `663b17e2`, borne HI0 = 20,
classifieur P-M13a (fenêtre [2.94, 3.06], K = 10, ex æquo N-5), G1′
(2.80, champ nommé, `fa109da9`), G2/G4 en consignation sans porte,
selftest cinq contre-exemples. Certification attendue : **à vue** (une
ligne). Aucun code avant (E19) ; le script est un PATCH v1b → v1c,
appliqué et consigné par machine 2 (précédent v1b, écart de répartition
déclaré).

## A1 — Objet : DEUX portes (delta 47, option (i))

**P-M13b-a (H-SAT, inchangée sur le fond)** : le classifieur P-M13a du
gel v3, appliqué à TOUS les survivants. **Résolution déclarée d'avance**
en deux sous-branches, consignées avec le verdict :
- **a-fort** : ≥ 2 points intra-rayon survivent → la fenêtre CANYON est
  résolue par des mesures au site.
- **a-faible** : tous les intra meurent → le verdict (LISSE attendu) vaut
  **à la résolution du rayon** : un creux plus étroit que 0.12 n'est pas
  exclu par s\* — et c'est P-M13b-b qui porte le site.

**P-M13b-b (structure sous-seuil, PRÉ-ENREGISTRÉE, points NEUFS)** :
STRUCTURE SOUS-SEUIL AU SITE 3:1 ssi, sur les cinq points intra NEUFS :
**≥ 3 exclusions G6, formant un bloc contigu en ω₂, toutes à
d ≤ rayon(ordre 4) = 0.12 — le site est DÉRIVÉ du catalogue R-2′ (leçon
47.6), plus aucun nombre inventé — ET zéro exclusion G6 hors rayon.**
Tout autre motif : publié, sans lecture. Les cinq morts de M13
([2.90, 3.03], `70fe5611`) sont la PROVENANCE déclarée de cette porte ;
ils n'entrent pas dans son évaluation.

## A2 — Points (17 recherches, 14 balayages)

- **Huit HORS rayon** (marge R-2′ ≥ 1.10 × 0.12 vérifiée, toutes
  fractions d'ordre ≤ 12) : **2.70, 2.74, 2.78, 2.85, 3.15, 3.22, 3.26,
  3.30.** Ils portent le plancher, la corde et la monotonie.
- **Cinq INTRA rayon, NEUFS** (jamais mesurés — la grille M13 était
  {2.90, 2.94, 2.97, 3.00, 3.03}) : **2.89, 2.92, 2.96, 3.02, 3.05.**
  Ils portent P-M13b-b ; leurs s\*, s'ils survivent, nourrissent a-fort.
- Fenêtre totale [2.70, 3.30] ; une seule famille d'ordre ≤ 12 dedans
  (3/1) — vérifié : 8/3 = 2.667 est hors fenêtre, 11/4, 16/5, 13/4,
  10/3 sont d'ordre > 12.

## A3 — Plancher et bords (remplace le §5 du gel v3)

P-M13b-a exige : **m_hors ≥ 7 sur les huit points hors rayon**, ET les
deux bords (2.70, 3.30) survivants. Les intra ne comptent ni pour ni
contre le plancher. Sinon : NON CONCLUANT DE GÉOMÉTRIE, aucune lecture
d'aucune porte. La lecture « attrition simple / structure » du §5 v3 est
REMPLACÉE par P-M13b-b.

## A4 — Ancres de régression gratuites (custody ×3)

2.85 et 3.15 ont été mesurés par M13 sous la MÊME chaîne et la MÊME
géométrie (`70fe5611`). Leurs nouvelles mesures doivent reproduire
**au bit** : s\*(2.85) = 8.24916028645919 ; s\*(3.15) = 9.970764210546593.
Écart ≠ 0.0 → ARRET (même statut que G1′). Trois verrous de custody pour
le prix d'un.

## A5 — Gardes déplacées

**G8** : au point **2.85** (survivant M13, hors bande morte), deux
signes ; moitié grossière attendue vide, inchangé. **G2** : au point
3.00 ?  Non — 3.00 n'est plus au programme ; G2 à **2.85** (la base et
la 2g partagent le rang, comme M12 rang 1). **G4** : échelle de force
maximale au run ; attente : 3.30. **G1′** : inchangé (2.80, hors
programme — 2.78 et 2.85 en sont distincts).

## A6 — Comptes, forme dérivée

Recherches = 13 (programme) + 1 (G8, −1 à 2.85) + 1 (G1′) + 1 (G4) +
1 (G2) = **17**. Balayages = 13 + 1 = **14**. Formes
« comptés + sautés == attendus ».

## A7 — Attente gelée du rédacteur (machine 1, avant tout calcul)

Hors rayon : 8/8 survivent, profil strictement croissant, ancres 2.85 et
3.15 à 0.0 exact. Intra : **5/5 meurent par G6, fenêtre fine, entre 0.90
et 0.98 s\*** (le motif de M13). P-M13b-b : **STRUCTURE tire.**
P-M13b-a : **LISSE en sous-branche a-faible.** Provenance : entièrement
extrapolée de M13 (`70fe5611`) — déclarée, règle de provenance.

## A8 — Conséquences par branche, écrites d'avance

- LISSE (a-faible) + STRUCTURE : **H-SAT est mesurée à la résolution du
  rayon, et le site est établi comme structuré SOUS le seuil.** Le groupe
  3:1 de la note P1 passe d'« accommodé » à « expliqué par un mécanisme
  mesuré : saturation du seuil + structure sous-seuil » — la forme
  raffinée de H-SAT. Le rapprochement 47.4 (2.67/M12) devient une
  question dérivable, toujours pas un résultat.
- LISSE (a-fort) : H-SAT mesurée au site même — plus fort.
- CANYON : H-SAT morte, trois signes tombent (inchangé du gel v3).
- STRUCTURE ne tire pas : le bloc M13 était un accident de tirage ou la
  bande a bougé — publié, et la note P1 garde son trou.
- NON CONCLUANT DE GÉOMÉTRIE : redessiner encore ; aucun des deux runs
  n'aura menti.

## A9 — Chaîne

Parent : gel M13 v3 `26c5a445` (cert. `b1ff00be`) ; artefacts de
provenance : `70fe5611` (M13), `fa109da9` (M12) ; delta 47 `535a49e8`.
Patch v1b → v1c : spécification jointe (`m13b_patch_v1c_spec.md`),
appliquée par machine 2, éditions consignées dans
`meta.declarations.editions_machine2`. Pré-vol RÉDUIT aux branches
neuves : deux scénarios (attendu ; géométrie) — les six de v1b restent
opposables pour le chemin inchangé. Empreinte de ce gel : au message ;
la version certifiée fera foi.
"""
# =====================================================================
# m13_saturation_v1c.py -- M13b : SATURATION 3:1, huit points HORS rayon
# + cinq INTRA NEUFS. 17 recherches, 14 balayages (gel M13b v1).
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

MARQ_DEBUT = "# GEL M13b v1 " + "— AMENDEMENTS AU GEL"
MARQ_FIN = "la version certifi" + "ée fera foi."

# ---- empreintes gelees (COMPLETES) -----------------------------------
SHA_GEL_M13 = "7a9b2809c8edeadf995d7decaa01407c6d6640bc77aca641785a41345f6d51b7"
SHA_PILOTE = "663b17e2955c79c09f1b6c0fb4443cd0c1f98be0db03ef089f5df682018ce905"
SHA_M12_JSON = "fa109da92e582520cfcb63b46bc41fa7d4b62295891f413bb97c6095b2fe59b1"

# ---- protocole (gel M13 v3) ------------------------------------------
POINTS_HORS = [2.70, 2.74, 2.78, 2.85, 3.15, 3.22, 3.26, 3.30]
POINTS_INTRA = [2.89, 2.92, 2.96, 3.02, 3.05]          # NEUFS (gel A2)
POINTS = sorted(POINTS_HORS + POINTS_INTRA)
RAYON_SITE = 0.12          # DERIVE du catalogue R-2' (ordre 4) -- gel A1
ANCRES_M13 = {2.85: 8.24916028645919, 3.15: 9.970764210546593}   # 70fe5611
DEGRE = 4
G8_POINT = 2.85
G2_POINT = 2.85
G1P_LIGNE = (2.80, 4, +1)                   # ligne du RUN M12, hors fenetre
G1P_CHAMP = "resultats.carte['4|2.800000000000'].sF"
G1P_CIBLE = 8.129205119847189               # gel Sec.7, valeur au bit
HI0_M13 = 20.0                              # gel Sec.4 -- recevabilite script
FEN_LO, FEN_HI = 2.94, 3.06                 # fenetre CANYON, gel Sec.6
K_CHUTE = 10
M_MIN = 7                                   # sur POINTS_HORS (gel A3)
BORDS = (2.70, 3.30)
# D_SITE SUPPRIME : le site est DERIVE (RAYON_SITE), lecon 47.6
TOL_APPART = 1e-09
EPS = 1e-12

# ---- programme fige, forme derivee -----------------------------------
RECH_ATTENDUES = (len(POINTS)               # programme, signe +1
                  + 1                       # G8, signe -1 en 2.85
                  + 1                       # G1'
                  + 1                       # G4
                  + 1)                      # G2
assert RECH_ATTENDUES == 17, "programme fige : 17 recherches (gel A6)"
BAL_ATTENDUS = len(POINTS) + 1              # 2.85|+1 EST deja au programme
assert BAL_ATTENDUS == 14, "balayages : 14 (gel A6)"
assert set(ANCRES_M13) <= set(POINTS_HORS)         # rule-11, par valeur
assert not (set(POINTS_INTRA) & {2.90, 2.94, 2.97, 3.00, 3.03})   # NEUFS
assert all(abs(w - 3.00) <= RAYON_SITE + 1e-12 for w in POINTS_INTRA)
assert G8_POINT in POINTS and G2_POINT in POINTS
assert all(w in POINTS for w in BORDS)
FOUT = os.path.join("out", "m13b_results.json")

SCENARIOS_PREVOL = ("attendu", "geometrie")   # gel A9 : prevol REDUIT


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
        print("Gel jumeau M13b v1 : sha %s -> %s"
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
# 2. MOTEUR FACTICE DU PRE-VOL -- DEUX SCENARIOS NEUFS (gel A9)
# =====================================================================

def fabriquer_factice(scenario, val_g1p):
    """Valeurs SYNTHETIQUES, AUCUNE physique. Pre-vol REDUIT aux branches
    NEUVES (gel A9) -- les six scenarios de v1b restent opposables pour le
    chemin inchange (prevol_m13_machine2_v2.log) :
      attendu   : les 8 hors survivent, croissants, ancres 2.85/3.15
                  servies AU BIT ; les 5 intra tues par G6 fenetre fine
                  -> STRUCTURE (P-M13b-b) + LISSE a-faible (P-M13b-a)
      geometrie : 2.70 et 2.74 tues par G5 -> plancher casse
                  -> NON CONCLUANT DE GEOMETRIE"""
    module = {"m": None}

    # Le factice doit servir les ancres AU BIT *et* rester strictement
    # croissant : une droite lineaire quelconque briserait la monotonie
    # aux deux points d'ancrage (defaut trouve au pre-vol v1). On prend
    # donc la droite qui PASSE par les deux ancres.
    _A1, _A2 = 2.85, 3.15
    _PENTE = (ANCRES_M13[_A2] - ANCRES_M13[_A1]) / (_A2 - _A1)

    def base(w):
        for a, val in ANCRES_M13.items():          # ancres AU BIT (gel A4)
            if abs(w - a) < 1e-9:
                return val
        return ANCRES_M13[_A1] + _PENTE * (w - _A1)   # croissant strict, < HI0

    def s_de(p, w, sgn):
        if (w, p, sgn) == G1P_LIGNE:
            return val_g1p
        return base(w)                             # p = 4 : identique aux 2 signes

    def chercher(w2, sgn=1, dt=None, g=None):
        m = module["m"]
        v = s_de(m.P, w2, sgn)
        if g is not None and g > 0.075:            # branche 2g : K-invariance
            return v * 2.0 ** (-1.0 / (m.P - 2)), "OK|pas=6.03e-07"
        if scenario == "geometrie" and min(abs(w2 - 2.70), abs(w2 - 2.74)) < 1e-9:
            return v, "OK|pas=2.00e-05"            # > plafond G5 : tue
        return v, "OK|pas=6.03e-07"

    def integrer(w2, s_arr, sgn=1, dt=None, g=None):
        m = module["m"]
        th = s_de(m.P, w2, sgn)
        if scenario == "attendu" and any(abs(w2 - w) < 1e-9 for w in POINTS_INTRA):
            return np.asarray(s_arr, float) >= 0.94 * th   # explose sous 0.98 s*
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


def porte_b(pertes_g6):
    """P-M13b-b (gel A1) : STRUCTURE SOUS-SEUIL AU SITE 3:1 ssi, sur les
    CINQ points intra NEUFS : >= 3 exclusions G6, formant un bloc CONTIGU
    en w2, toutes a d <= rayon(ordre 4) = 0.12 -- site DERIVE du catalogue
    R-2' -- ET zero exclusion G6 hors rayon."""
    intra = sorted(w for w in pertes_g6 if w in POINTS_INTRA)
    hors = sorted(w for w in pertes_g6 if w in POINTS_HORS)
    contigu = bool(intra) and intra == [w for w in POINTS_INTRA
                                        if intra[0] <= w <= intra[-1]]
    dedans = all(abs(w - 3.00) <= RAYON_SITE + EPS for w in intra)
    tire = len(intra) >= 3 and contigu and dedans and not hors
    return {"lecture": ("STRUCTURE SOUS-SEUIL AU SITE 3:1" if tire else
                        "motif non atteint" if pertes_g6 else "aucune perte G6"),
            "intra_perdus": intra, "hors_perdus": hors,
            "contigu": contigu, "tous_dans_le_rayon": dedans,
            "site": "d <= rayon(ordre 4) = %.2f, DERIVE du catalogue R-2'"
                    % RAYON_SITE,
            "provenance": "bloc [2.90, 3.03] de M13 (70fe5611) -- motive "
                          "cette porte ; n'entre PAS dans son evaluation "
                          "(les cinq intra sont NEUFS)"}


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


SYNTHETIQUES = [   # grille M13b : 13 points, fenetre CANYON [2.94, 3.06]
    ("croissant strict (attente du redacteur, gel A7)",
     POINTS, _prof([2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6,
                    2.7, 2.8, 2.9, 3.0, 3.1, 3.2]), "LISSE"),
    ("marche monotone (PAS, fait s*4 de M12 -- jamais un CREUX)",
     POINTS, _prof([2.0, 2.1, 2.2, 2.3, 5.9, 6.0, 6.1,
                    6.2, 6.3, 6.4, 6.5, 6.6, 6.7]), "LISSE"),
    ("decroissant strict",
     POINTS, _prof([3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6,
                    2.5, 2.4, 2.3, 2.2, 2.1, 2.0]), "LISSE"),
    ("creux resolu au site (2.96, intra) -> CANYON",
     POINTS, _prof([3.0, 2.95, 2.9, 2.85, 2.6, 2.2, 1.2,
                    2.0, 2.4, 2.8, 3.0, 3.1, 3.2]), "CANYON"),
    ("ex aequo EXACT (2.96, 3.02), tous en fenetre -> CANYON",
     POINTS, _prof([3.0, 2.95, 2.9, 2.85, 2.6, 2.2, 1.2,
                    1.2, 2.4, 2.8, 3.0, 3.1, 3.2]), "CANYON"),
    ("ex aequo a cheval (3.05 dedans, 3.15 dehors) -> NON CLASSE",
     POINTS, _prof([3.0, 2.95, 2.9, 2.85, 2.8, 2.7, 2.6,
                    2.5, 1.2, 1.2, 3.0, 3.1, 3.2]), "NON CLASSE"),
    ("minimum interieur HORS fenetre (2.89, intra) -> NON CLASSE",
     POINTS, _prof([3.0, 2.95, 2.9, 2.85, 1.2, 2.4, 2.6,
                    2.7, 2.8, 2.9, 3.0, 3.1, 3.2]), "NON CLASSE"),
    ("chute non resolue : voisins a 3e-5 du min, entre B et 10B",
     POINTS, _prof([3.0 * math.exp(k) for k in
                    (2e-4, 1.5e-4, 1e-4, 8e-5, 5e-5, 3e-5, 0.0,
                     3e-5, 5e-5, 8e-5, 1e-4, 1.5e-4, 2e-4)]), "NON CLASSE"),
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
    print("SELFTEST m13_saturation_v1c.py -- gel M13b v1")
    print("=" * 70)
    certifier_gel()
    P = charger_pilote(verbeux=False)
    print("pilote importe par empreinte, gel pilote re-verifie")

    print("\n[1] programme fige, DERIVE (jamais affirme)")
    assert RECH_ATTENDUES == 17 and BAL_ATTENDUS == 14
    assert len(POINTS) == 13 and len(set(POINTS)) == 13
    assert POINTS == sorted(POINTS)
    print("    17 recherches (13+1+1+1+1), 14 balayages (13 programme + 1 G8) ;")
    print("    13 points tries, distincts ; 8 hors rayon + 5 intra")

    print("\n[2] grille : centiemes exacts, intra NEUFS, hors R-2'-propres")
    cents = [round(w * 100) for w in POINTS]
    assert all(abs(w - c / 100.0) <= TOL_APPART for w, c in zip(POINTS, cents))
    assert len(POINTS) == 13 and len(set(POINTS)) == 13
    assert not (set(POINTS_INTRA) & {2.90, 2.94, 2.97, 3.00, 3.03})
    assert all(abs(w - 3.00) <= RAYON_SITE + EPS for w in POINTS_INTRA)
    assert all(abs(w - 3.00) >= 1.10 * RAYON_SITE - EPS for w in POINTS_HORS)
    assert set(ANCRES_M13) <= set(POINTS_HORS)
    assert min(abs(G1P_LIGNE[0] - w) for w in POINTS) > TOL_APPART
    assert all(min(abs(x - w) for w in POINTS) <= TOL_APPART
               for x in (G8_POINT, G2_POINT) + BORDS)
    print("    13 points ; 5 intra NEUFS dans le rayon 0.12 ; 8 hors a")
    print("    d >= 1.10 x 0.12 ; ancres/G8/G2/bords dans la grille par")
    print("    VALEUR (rule-11) ; G1' (2.80) hors programme")

    print("\n[3] classifieur P-M13b-a : archives 5/5 + branches (BLOQUANT)")
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

    print("\n[6] P-M13b-b : la porte mord et ne deborde pas")
    b1 = porte_b({2.92, 2.96, 3.02})
    b2 = porte_b({2.92, 2.96, 3.02, 2.74})
    b3 = porte_b({2.89, 3.05})
    b4 = porte_b({2.92, 2.96})
    b5 = porte_b(set(POINTS_INTRA))
    b6 = porte_b(set())
    assert b1["lecture"].startswith("STRUCTURE"), "bloc contigu de 3 -> STRUCTURE"
    assert not b2["lecture"].startswith("STRUCTURE"), "une perte HORS rayon -> non"
    assert not b3["lecture"].startswith("STRUCTURE"), "non contigu -> non"
    assert not b4["lecture"].startswith("STRUCTURE"), "2 < 3 -> non"
    assert b5["lecture"].startswith("STRUCTURE"), "les cinq -> STRUCTURE"
    assert b6["lecture"] == "aucune perte G6"
    print("    {2.92,2.96,3.02} -> STRUCTURE ; +2.74 (hors rayon) -> non ;")
    print("    {2.89,3.05} non contigu -> non ; 2 < 3 -> non ;")
    print("    les cinq -> STRUCTURE ; vide -> aucune perte")

    print("\n[7] plancher : m_hors >= 7 sur les HUIT hors, ET les deux bords")
    assert plancher_ok(POINTS)[0]
    assert plancher_ok(POINTS_HORS)[0]
    assert not plancher_ok(POINTS_HORS[:6])[0]
    assert not plancher_ok([w for w in POINTS_HORS if w != 2.70])[0]
    assert not plancher_ok(POINTS_INTRA + POINTS_HORS[:6])[0]
    print("    8 hors -> OK ; 6 hors -> NON ; bord 2.70 perdu -> NON ;")
    print("    les intra ne comptent ni pour ni contre le plancher")

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
    for _a, _val in ANCRES_M13.items():
        assert (_val - _val) == 0.0
        assert (_val - math.nextafter(_val, math.inf)) != 0.0
    print("    ancres M13 %s : egalite au bit testable de la meme facon"
          % sorted(ANCRES_M13))

    print("\nSELFTEST M13b : TOUT PASSE (9 sections).")
    return 0


def plancher_ok(survivants):
    """Gel A3 : m_hors >= 7 sur les HUIT points hors rayon, ET les deux
    bords (2.70, 3.30). Les intra ne comptent ni pour ni contre."""
    sh = [w for w in survivants if w in POINTS_HORS]
    if len(sh) < M_MIN:
        return False, "m_hors = %d < %d (sur %d points hors rayon)" % (
            len(sh), M_MIN, len(POINTS_HORS))
    for b in BORDS:
        if b not in sh:
            return False, "bord de fenetre %.2f perdu" % b
    return True, "m_hors = %d >= %d, bords (%.2f, %.2f) survivants" % (
        len(sh), M_MIN, BORDS[0], BORDS[1])


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
    print("rule-11 : 13 points du programme, ancres G8/G2 (2.85) incluses ;")
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

    # ---- programme : 13 mesures (+1), G8 (-1) en 2.85, borne HI0 -----
    print("\n--- programme p = 4, treize points, borne HI0 = %g ---" % HI0_M13)
    for w in POINTS:
        v = carte.setdefault(P.cle(4, w), {})
        for sgn, k in plan_signes(w):
            m = appliquer_borne(P.mesurer(m9, w, sgn))
            if sgn < 0:
                m["role"] = "regression_G8"
            v[k] = m
            sauve()
        assembler_ligne_m13(w, v)
        if w in ANCRES_M13 and v["sP"]["recevable"]:
            ecA = v["sP"]["s"] - ANCRES_M13[w]
            res["resultats"].setdefault("ancres_regression", {})[P.cle(4, w)] = {
                "cible_m13": ANCRES_M13[w], "ecart_absolu": ecA,
                "verdict": "PASSE" if ecA == 0.0 else "ECHEC",
                "source": "m13_results.json 70fe5611 -- meme chaine, meme "
                          "geometrie (gel A4)"}
            if ecA != 0.0:
                sauve()
                sys.exit("ARRET ancre M13 : ecart %r en w2=%.2f" % (ecA, w))
            print("  ancre M13 %.2f : ecart 0.0 EXACT" % w)
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
    res["resultats"]["structure_sous_seuil"] = porte_b(pertes_g6)
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
    intra_surv = [w for w in survivants if w in POINTS_INTRA]
    res["resultats"]["classement"]["resolution"] = (
        "a-fort (%d intra survivants) : la fenetre CANYON est resolue par "
        "des mesures AU SITE" % len(intra_surv) if len(intra_surv) >= 2
        else "a-faible (%d intra survivant(s)) : verdict A LA RESOLUTION DU "
             "RAYON (0.12) ; un creux plus etroit n'est PAS exclu par s* -- "
             "P-M13b-b porte le site (gel A1)" % len(intra_surv))
    verdict = {"m": len(survivants),
               "m_hors": len([w for w in survivants if w in POINTS_HORS]),
               "P_M13b_a": va, "detail": detail,
               "resolution": res["resultats"]["classement"]["resolution"],
               "P_M13b_b": res["resultats"]["structure_sous_seuil"]["lecture"]}
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
    print("m = %d (dont %d hors rayon) | P-M13b-a : %s" % (
        len(survivants), len([w for w in survivants if w in POINTS_HORS]),
        res["verdict"].get("P_M13b_a",
            res["verdict"].get("PREVOL_SYNTHETIQUE_P_M13b_a"))))
    print("  resolution : %s" % res["resultats"]["classement"]["resolution"])
    print("P-M13b-b : %s"
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
