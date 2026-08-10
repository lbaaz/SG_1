# -*- coding: utf-8 -*-
"""PRE-ENREGISTREMENT M9 -- PREMIER TEST PROPRE DU +1.00 DE M3 (p=5,
CONVENTION (f) INTEGRALE)
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF ;
nom de fichier versionne conformement a la regle E19 -- version v2)

HISTORIQUE DU GEL
  v1, sha256 4e80db1b3e7eb48735c305ab350d350809661d64cf4db2aac2245011918de05c
  RETIREE A LA CERTIFICATION (audit pre-feu machine 2 du 26/07, defaut
  D-M9-1) : le signe de l'etat initial n'etait pas declare ('s0 = 0.7
  s_cible'), alors que les quatre T de reference de M3 sont TOUS mesures a
  sgn = frag = -1 (m3_parite_2, island_state(sgn*0.7*st)) et que la lignee
  m7/m8 (source des moteurs) implemente s0 positif sans signe
  (corps_m7 lignes 355/371/199, verifie machine 1). Materiel :
  T(+1)/T(-1) = 0.406 a 2.85 -- un M9 en +1 garantissait une fausse alerte
  P-M9c et rendait fausse la clause (e). Premiere application de la regle
  E19 : le defaut est mort avant la premiere ligne de code.
  v2 : (1) s0 signe cote fragile (texte en ETAGE 2) et programme G5 exprime
  en sgn_F ; (2) sqrt2 promue QUATRIEME ancre bloquante de G1a (valeurs
  transmises par l'audit pre-feu), G1c supprimee (absorbee) ; (3) ecart
  s_cible json-M3 vs forme fermee declare en (h), decouvert par la
  verification machine 1 de l'audit ; (4) attente retourne declassee en
  ordre de grandeur. AUCUNE porte ni aucun seuil modifies. Aucun numero
  d'erratum reserve (regle E18). AUCUN code avant qu'un message de
  certification croisee cite l'empreinte du PRESENT bloc v2 (regle E19).
  Le script s'appellera m9_replication_v1.py.

DECISION D3 (arbitrage humain du 26/07, ANTERIEUR a la redaction de ce bloc,
consigne au journal delta 24)
  La clause de M8 v1  interdit d'empiler une troisieme manche quantique sans
  changer d'estimateur  visait, par sa derivation, la REPETITION DU MEME
  TEST. Or il est etabli (S23) que M8 n'a pas execute les systemes de M3 :
  trois points canoniques sur quatre tournaient a un couplage different
  (x1.40 / x1.63 / x1.89). M9 en convention (f) est donc le PREMIER test du
  +1.00 de M3, pas un empilement. Lecture B adoptee A DEUX, avec deux
  compensations GELEES :
  (C1) l'observable differentielle (systeme a signe retourne) est mesuree et
       consignee aux SIX points -- le chantier estimateur avance dans la
       meme manche ;
  (C2) si M9 sort NON CONCLUANT, la clause se REARME a pleine force : aucune
       manche quantique supplementaire, a QUELQUE degre que ce soit, sans un
       estimateur change ET muni d'une derivation. Pas de lecture B deux
       fois.

QUESTION
--------
rho(T, K5) = +1.00 mesure par M3 sur 4 points (p = 0.042, marginal) : ce
signe se confirme-t-il avec puissance (6 points, p <= 0.029, deux
troncatures) quand la carte classique, la calibration et l'etat initial
utilisent la MEME definition du seuil que M3 (sF = min des deux signes) ?

DERIVATIONS PREALABLES (faits verifies avant gel)
-------------------------------------------------
(a) CONVENTION (f), gelee pour TOUTE la manche : s* = min( s*(sgn=+1),
    s*(sgn=-1) ) -- garde-fou M1 pour degre impair, et definition de la
    carte sF de M3. Asymetries r_s = s*(+1)/s*(-1) consignees partout,
    AUCUNE porte dessus. Donnee p=7 (S24) : le cote fragile peut S'INVERSER
    en w2 (-18.9 % a 1.80) et atteindre 38 % (2.40) -- les deux signes sont
    donc indispensables aussi aux points neufs 1.80 et 2.40. Donnee p=3
    (audit du 26/07) : frag = +1 sauf a 2.85 -- la non-uniformite du cote
    fragile est generique, d'ou la forme 'sgn_F par point' de ce gel.
(b) NULLES EXACTES DE SPEARMAN (enumerees, M8 v1) : n=6 : P(rho >= +0.80)
    = 0.0292 ; n=5 : P(rho >= +0.90) = 0.0417 ; n=4 : au mieux 0.0417.
    ECHELLE ADAPTATIVE gelee : seuil +-0.80 si n_retenu = 6 ; +-0.90 si
    n_retenu = 5 ; n_retenu <= 4 -> ECHEC DE DESIGN (pas un verdict
    physique), redesign obligatoire.
(c) COQUILLE FIXE 35 <= max(n1,n2) <= 45 (891 etats a tout N >= 46).
    Tampon a p=5 : 2 sauts (N=56), 3.6 sauts (N=64). Precedent M8 :
    rho(T56,T64) = +1.00 -- la resolution de rang est acquise a p=5.
(d) AUCUN TEMOIN BORNE a p impair (M7-(d), inchange). FREE (g=0) teste le
    pipeline, pas la dynamique. Le retourne est NON borne : il borne le
    canal generique x^5, il n'est pas un controle borne.
(e) ANTI-FRANKEN-RHO (S23, gelee) : le rho de M9 n'utilise QUE la carte de
    M9. En revanche T_M9/T_M3 aux canoniques est desormais LEGITIME et
    central : par construction (meme carte sF, meme calibration, MEME COTE de
    deplacement initial sgn_F), M9 refait les systemes de M3 -- c'est le
    point de toute la manche.
(f) CALIBRATION : nbar1 = 7 ; s_cible = sqrt(14 Delta)/(1+w2^2) ;
    g_cal = K5_min / s_cible^3 avec K5_min = 0.05 x sF^3.
(g) ANCRES DISPONIBLES (provenance machine 2, m3_calib.json, S23) :
    sP/sM : 1.35 : 0.34921/0.31011 ; 2.00 : 0.37477/0.37401 ;
    2.85 : 3.19542/2.58573 ; sqrt2 : 0.38604/0.32665 (asym 18.18 %,
    frag = -1 ; transmis par l'audit pre-feu machine 2 du 26/07 -> ANCRE,
    cf. G1a). 1.80, 2.40 : AUCUNE ancre (points neufs en convention (f)).
(h) ECART DECLARE (decouvert en verifiant l'audit) : les s_cible STOCKES
    par M3 excedent la forme fermee (f) d'un facteur UNIFORME x1.00285
    (mesure aux trois points via g = K/s_cible^3 : formule 8.5807e-4 /
    1.2013e-3 / 0.65905 contre json 8.5080e-4 / 1.1911e-3 / 0.65344, soit
    -0.85 % sur g ; equivalent nbar = 7.04). Cause NON identifiee, a lire
    dans le code de calibration M3. Propagation pire cas sur T : ~3.4 %
    (dlnT/dlng ~ 4 mesure), sous G5 (+-5 %) et sous la fenetre P-M9c
    [0.80, 1.25]. M9 utilise la FORME FERMEE (f) partout (uniformite aux
    points neufs) ; l'ecart aux canoniques est consigne par point.

ETAGE 1 -- CLASSIQUE : LA CARTE sF SUR SIX POINTS
-------------------------------------------------
w2 dans {1.35, sqrt(2), 1.80, 2.00, 2.40, 2.85}, g = 0.05, DEUX signes,
passe dense n = 96 partout.

P-M9-pre  ORDONNANCEMENT (porte prealable, miroir de P-M7a/P-M8-pre)
  argmin K5_min != 2.00 -> LIEN CONFIRME, la prediction rho > 0 conserve sa
    derivation. [attendu : carte sF de M3 donne 1.49e-3 (1.35) < 2.62e-3
    (2.00) sur les canoniques.]
  argmin K5_min = 2.00 -> LIEN REFUTE ; l'etage 2 TOURNE sans prediction,
    interdiction de re-deriver un signe apres coup (lecon E15).

ETAGE 2 -- QUANTIQUE
--------------------
H = -w1 n1 + w2 n2 + (g/5) x^5, diagonalisation exacte, N = 56 et 64.
Etat initial : coherent apparie DU COTE FRAGILE (correction D-M9-1) :
s0 = sgn_F x 0.7 x s_cible, ou sgn_F est le signe realisant le minimum de
la carte sF au point, FIGE depuis la carte a g = 0.05 et consigne par
point -- la regle de M3 (island_state(sgn*0.7*st), sgn = frag). MEME s0
(meme sgn_F) pour GHOST, RETOURNE et FREE. Si le double-signe de G5 revele
un cote fragile different a g_cal, l'ecart est CONSIGNE (aucune porte) ;
la definition reste celle de la carte a g = 0.05, comme M3.
Observable : T_shell.

P-M9a  PORTE PRINCIPALE -- rho de Spearman entre T_shell et K5_min, points
       retenus, AUX DEUX troncatures ; seuil selon (b).
  rho >= seuil AUX DEUX N -> PREMIER SOUTIEN PUISSANTE de la jambe
    quantique de H-PROFONDEUR, et replication du signe de M3.
    [derivation : carte ordonnee par le fond (P-M9-pre) => T suit le fond
     => positif ; M3, coherent sur ses propres systemes (S23), predisait
     le signe.]
  rho <= -seuil AUX DEUX N -> REFUTATION, et cette fois LEGITIME : memes
    systemes que M3 par construction => le +1.00 de M3 est requalifie
    (bruit de petit n) ET la jambe quantique tombe. Les deux consequences
    sont ecrites d'avance.
    [derivation : anti-correlation puissantee avec un creux qui n'ordonne
     pas la carte contredit le coeur de l'hypothese.]
  Tout le reste -> NON CONCLUANT, et LA COMPENSATION C2 SE DECLENCHE :
    rearme de la clause anti-empilement a pleine force (texte en D3).
  ANTI-ARRET-OPTIONNEL : rho dans [0.60, seuil) ne prolonge RIEN.
  Le p exact est reporte dans tous les cas, enumere sur le n effectif.

P-M9b  COMPENSATION C1 -- CANAL GENERIQUE (consigne, AUCUNE porte)
  T_retourne aux SIX points, N = 64. Fourche de lecture PRE-DECLAREE
  (heritee de M8 v1, point par point, PAS de mediane) :
    T_ghost/T_retourne >= 10 partout -> contraste fantome grand a p=5 ;
    <= 3 quelque part -> le caveat cause (2) s'attache au verdict P-M9a ;
    entre : consigne sans lecture.
  En sus, pour le chantier estimateur (C1) : le profil complet
  {T_ghost, T_retourne, g_cal} par point est consigne au JSON -- matiere du
  futur estimateur derive, aucune interpretation gelee ici.

P-M9c  LA REPLICATION DIRECTE (consigne, lecture pre-declaree, AUCUNE porte)
  (i) rho sur le sous-ensemble canonique {1.35, sqrt2, 2.00, 2.85} --
      comparaison de forme a M3 (rappel : n=4, p >= 0.042, non testable
      en soi).
  (ii) T_M9 / T_M3 aux quatre canoniques, N = 64 (T_M3 : 4.2597e-3 /
      8.2337e-3 / 1.0636e-2 / 1.7406e-2, S23). Lecture pre-declaree :
      ratios TOUS dans [0.80, 1.25] -> le protocole refait les systemes de
      M3 (offset de code uniforme tolere) ; motif NON uniforme -> ALERTE,
      investigation avant toute interpretation de P-M9a. Comparaison
      croisee entre codes : elle alerte, elle ne conclut pas.

P-M9d  OPERATIONNALISATION (consigne, AUCUNE porte)
  rho(T, C5_min) avec C5 = K5_min/[(w2-1)^2(1+w2)], rapporte a cote.
  K5_min seul est la porte (anti double-dipping).

P-M9-null  PIPELINE (porte)
  FREE (g=0) a w2 = 1.35 et 2.85, N = 64 : T_shell < 1e-12 -> PASSE, sinon
  ARRET. Teste base et recouvrements, pas la dynamique (cf. (d)).

GARDES
------
  G1a ANCRES M3 (bloquantes) : sP ET sM compares aux valeurs de (g) aux
     QUATRE points ancres (1.35, sqrt2, 2.00, 2.85), tolerance +-2 % PAR
     SIGNE. Echec d'un cote -> ARRET, investigation (croise entre codes :
     bloque, ne conclut pas).
  G1b REGRESSION M8 (bloquante) : s*(+1) de M9 vs M8 aux six points,
     tolerance +-2 % (implementations differentes du meme protocole ;
     precedent jet/modes : <= 0.8 %).
  G2 INVARIANCE : K5_min a 2g sur w2 = 1.35 et 2.85 (les DEUX signes a 2g,
     soit 4 recherches), tolerance 10 %, reprise dense sinon ligne EXCLUE.
  G3 IDENTITE DE FORCE : erreur BACKWARD <= 1e-12.
  G4 PAS DE TEMPS : dt/2 sur la ligne qui maximise g_cal x sF^4 (echelle de
     force, lecon M6) ; ecart <= 2 % sinon ligne NON FIABLE.
  G5 CALIBRATION : re-mesure de s* a g_cal ; aux points ou l'asym a
     g = 0.05 depasse 2 %, la re-mesure court les DEUX signes et compare
     s*_min ; |s*_min - s_cible|/s_cible <= 5 % sinon point EXCLU de rho.
  G6 REPRESENTABILITE : queue de l'etat coherent < 1e-8 sinon EXCLU.
  G7 TRONCATURE : T56/T64 par point ET rho(T56, T64), consignes, aucune
     porte ; diagnostic obligatoire si NON CONCLUANT.

PROGRAMME FIGE
--------------
  Classique : carte 6 x 2 signes (12) ; G2 a 2g x 2 signes x 2 points (4) ;
    G5 : 6 en signe sgn_F, doublees (autre signe) aux points d'asym > 2 %
    (attendu +4 a +5, sqrt2 desormais connue a 18 %) ;
    G4 (1). Soit 23 a 28 recherches, passe dense n = 96 partout.
  Quantique : GHOST 6 x {56, 64} (12) ; retourne 6 x {64} (6) ;
    FREE 2 x {64} (2). Soit 20 diagonalisations.
  Cout annonce : ~15 min machine 2.

ENCHAINEMENTS PRE-DECLARES
  CONFIRMEE -> premier soutien puissante ; la conditionnelle p=7 (S17-bis)
    reste armee ; la manche suivante est le redesign p=7, nourri du profil
    C1.
  REFUTEE -> +1.00 de M3 requalifie (legitimement, memes systemes) ET jambe
    quantique morte ; pivot classique (derivation de r, bord droit (3,1)).
  NON CONCLUANT -> C2 : rearme integral. Plus aucune manche quantique sans
    estimateur change et derive.

MES ATTENTES (pour pouvoir avoir tort de mon propre fait)
  Je ne designe PAS d'issue favorite : CONFIRMEE et NON CONCLUANT me
  paraissent comparables. Chiffres : rho canonique +0.6 a +1.0 si le signal
  M3 est reel ; rho 6 points +0.3 a +0.9. T_M9/T_M3 canoniques dans
  [0.85, 1.15], motif uniforme. Asymetries a 1.80 et 2.40 : 5 a 40 %, cote
  fragile possiblement inverse a 1.80 comme a p=7. T_retourne(2.00) : ordre de
  grandeur 1e-12 attendu SI le cote du deplacement (sgn_F(2.00) = -1, la ou
  M8 mesurait +1) ne change pas le canal generique -- sensibilite au cote
  inconnue, consignation quoi qu'il arrive. Exclusions : 0 ou 1.

LIMITATIONS DECLAREES
  - n = 6 au mieux ; mediateur (C vs g_eff) non identifie : test d'un
    SIGNE, pas d'un mecanisme.
  - Ensemble diagonal suppose non degenere (jamais audite) ; parite non
    conservee a p impair.
  - Aucun temoin dynamique borne (cf. (d)).
  - Magnitudes de T non convergees (S8) ; seul le rang est revendique,
    accord des deux troncatures exige.
  - Ne jamais multiplier les p des deux troncatures (correlees).
  - Les comparaisons inter-manches portent leurs etiquettes de convention
    (lecon E20) : tout chiffre de ce gel est min-convention sauf mention.

IMPLEMENTATION
  m9_replication_v1.py, moteurs repris de la lignee m7/m8 machine 1, ecrit
  uniquement out/m9_results.json (incremental). Gel jumeau dans le
  docstring, bloc de "PRE-ENREGISTREMENT M9" a "=== FIN DU GEL M9 ===
"""

GEL_SHA256_ATTENDU = "90019ebabde24e912ed0415da0e2068d9a27d8404a4aaa6e944fc2463e0f4c70"
MARQ_DEBUT = "PRE-" + "ENREGISTREMENT M9"
MARQ_FIN = "=== FIN DU GEL M9 " + "==="

import argparse, hashlib, itertools, json, os, sys, time, unicodedata
from math import comb, sqrt, log

import numpy as np
from scipy.special import gammaln
import scipy.sparse as sp

# =====================================================================
# 0. CERTIFICATION DU GEL JUMEAU (convention M6/M7/M8 : premiere occurrence)
# =====================================================================

def canon(t):
    return unicodedata.normalize("NFC", t).replace("\r\n", "\n").replace("\r", "\n")

def certifier_gel():
    ch = os.path.abspath(__file__)
    src = open(ch, "r", encoding="utf-8").read()
    blk = canon(src[src.index(MARQ_DEBUT): src.index(MARQ_FIN) + len(MARQ_FIN)])
    hb = hashlib.sha256(blk.encode()).hexdigest()
    hf = hashlib.sha256(canon(src).encode()).hexdigest()
    print("=" * 78)
    print("CERTIFICATION DU GEL M9 v2")
    print("=" * 78)
    print("  bloc portes         : %d lignes, ASCII pur : %s" % (blk.count("\n") + 1, blk.isascii()))
    print("  sha256 bloc         : %s" % hb)
    print("  sha256 bloc attendu : %s" % GEL_SHA256_ATTENDU)
    print("  sha256 fichier      : %s" % hf)
    print("  certification croisee machine 2 : m9_certification_croisee_v2.md (26/07)")
    if hb != GEL_SHA256_ATTENDU:
        sys.exit("\nARRET : bloc de gel non conforme a l'empreinte certifiee.")
    print("  VERDICT             : GEL CONFORME\n")
    return hb, hf

# =====================================================================
# 1. PARAMETRES GELES (v2)
# =====================================================================

P = 5
W1 = 1.0
G_REF = 0.05
DT, T_MAX, CAP = 0.006, 400.0, 1.0e4
NGRID, NPASSES, NDENSE = 48, 3, 96
LO0, HI0, MAX_ELARG = 0.05, 6.0, 8
SQ2 = sqrt(2.0)
W2S = [1.35, SQ2, 1.80, 2.00, 2.40, 2.85]
CANON = [1.35, SQ2, 2.00, 2.85]
NBAR = 7.0                      # forme fermee (f) ; ecart (h) declare vs M3 (7.04)
FACTEUR_H_S = 1.002853          # sqrt(7.04/7) -- cause identifiee (certification)
RHO_AMP = 0.7
NS = [56, 64]
SHELL_LO, SHELL_HI = 35, 45
SEUILS_RHO = {6: 0.80, 5: 0.90}     # echelle adaptative (b)
SEUIL_NULL = 1e-12
PTS_CTRL = [1.35, 2.85]
TOL_G1A = TOL_G1B = 0.02
TOL_G2, TOL_G4, TOL_G5, TOL_G6 = 0.10, 0.02, 0.05, 1e-8
ASYM_DOUBLE = 0.02
FEN_M9C = (0.80, 1.25)

ANCRES_G1A = {1.35: (0.34921, 0.31011), SQ2: (0.38604, 0.32665),
              2.00: (0.37477, 0.37401), 2.85: (3.19542, 2.58573)}   # sP, sM (m3_calib)
ANCRES_G1B = {1.35: 0.34647914441430433, SQ2: 0.3844714410203195,
              1.80: 0.6668205807758855, 2.00: 0.37450207514104217,
              2.40: 2.962927335338433, 2.85: 3.1946942797889326}    # M8 sgn=+1
T_M3_N64 = {1.35: 4.2597e-3, SQ2: 8.2337e-3, 2.00: 1.0636e-2, 2.85: 1.7406e-2}

def key(w):
    return "%.6f" % w

# =====================================================================
# 2. CLASSIQUE (lignee m7/m8, p = 5)
# =====================================================================

def grad_explicite(x1, x2, g=G_REF):
    d1 = np.zeros_like(x1); d2 = np.zeros_like(x2)
    e1 = np.zeros_like(x1); e2 = np.zeros_like(x2)
    for a in range(P + 1):
        b = P - a
        c = g * comb(P, a) / P
        if a >= 1:
            t = c * a * x1 ** (a - 1) * x2 ** b; d1 += t; e1 += np.abs(t)
        if b >= 1:
            t = c * b * x1 ** a * x2 ** (b - 1); d2 += t; e2 += np.abs(t)
    return d1, d2, e1, e2

def grad_rapide(x1, x2, g):
    base = g * (x1 + x2) ** (P - 1)
    return base, base

def garde_G3():
    rng = np.random.default_rng(20260726)
    x1 = rng.uniform(-2, 2, 4096); x2 = rng.uniform(-2, 2, 4096)
    dl1, dl2, e1, e2 = grad_explicite(x1, x2)
    dr1, dr2 = grad_rapide(x1, x2, G_REF)
    e = max(np.max(np.abs(dl1 - dr1) / (e1 + 1e-300)),
            np.max(np.abs(dl2 - dr2) / (e2 + 1e-300)))
    print("G3 : erreur backward max = %.3e (tolerance 1e-12) -> %s\n"
          % (e, "PASSE" if e <= 1e-12 else "ECHEC"))
    if e > 1e-12:
        sys.exit("ARRET G3.")

def integrer(w2, s_arr, sgn=1, dt=DT, g=G_REF):
    delta = w2 * w2 - W1 * W1
    s_arr = np.asarray(s_arr, float)
    x1 = sgn * s_arr * (1 + w2 * w2) / delta
    x2 = -sgn * s_arr * (1 + W1 * W1) / delta
    v1 = np.zeros_like(x1); v2 = np.zeros_like(x2)
    expl = np.zeros(s_arr.shape, bool)
    def acc(a1, a2):
        d1, d2 = grad_rapide(a1, a2, g)
        return -W1 * W1 * a1 + d1 / delta, -w2 * w2 * a2 - d2 / delta
    with np.errstate(over="ignore", invalid="ignore"):
        for _ in range(int(round(T_MAX / dt))):
            k1v1, k1v2 = acc(x1, x2); k1x1, k1x2 = v1, v2
            k2v1, k2v2 = acc(x1 + .5 * dt * k1x1, x2 + .5 * dt * k1x2)
            k2x1, k2x2 = v1 + .5 * dt * k1v1, v2 + .5 * dt * k1v2
            k3v1, k3v2 = acc(x1 + .5 * dt * k2x1, x2 + .5 * dt * k2x2)
            k3x1, k3x2 = v1 + .5 * dt * k2v1, v2 + .5 * dt * k2v2
            k4v1, k4v2 = acc(x1 + dt * k3x1, x2 + dt * k3x2)
            k4x1, k4x2 = v1 + dt * k3v1, v2 + dt * k3v2
            x1 = x1 + dt / 6 * (k1x1 + 2 * k2x1 + 2 * k3x1 + k4x1)
            x2 = x2 + dt / 6 * (k1x2 + 2 * k2x2 + 2 * k3x2 + k4x2)
            v1 = v1 + dt / 6 * (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1)
            v2 = v2 + dt / 6 * (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2)
            bad = (~np.isfinite(x1)) | (~np.isfinite(x2)) | \
                  (np.maximum(np.abs(x1), np.abs(x2)) > CAP)
            if bad.any():
                expl |= bad
                if expl.all():
                    break
                x1 = np.where(expl, 0., x1); x2 = np.where(expl, 0., x2)
                v1 = np.where(expl, 0., v1); v2 = np.where(expl, 0., v2)
    return expl

def chercher_seuil(w2, sgn=1, dt=DT, g=G_REF):
    lo, hi = LO0, HI0
    for _ in range(MAX_ELARG):
        s = np.linspace(lo, hi, NGRID)
        ex = integrer(w2, s, sgn, dt, g)
        if ex.any():
            break
        lo, hi = hi, hi * 4
    else:
        return None, "ECHEC_HAUT"
    nb = 0
    while ex[0] and nb < MAX_ELARG:
        hi, lo = lo, lo / 4
        s = np.linspace(lo, hi, NGRID); ex = integrer(w2, s, sgn, dt, g); nb += 1
        if not ex.any():
            return None, "ECHEC_BAS"
    for _ in range(NPASSES - 1):
        i = int(np.argmax(ex))
        if i == 0:
            break
        lo, hi = s[i - 1], s[i]
        s = np.linspace(lo, hi, NGRID); ex = integrer(w2, s, sgn, dt, g)
        if not ex.any():
            s = np.array([hi]); ex = np.array([True]); break
    i = int(np.argmax(ex))
    lo_d, hi_d = (s[i - 1] if i > 0 else lo), s[i]
    s = np.linspace(lo_d, hi_d, NDENSE); ex = integrer(w2, s, sgn, dt, g)
    if not ex.any():
        return float(hi_d), "DENSE_SANS_EXPLOSION"
    return float(s[int(np.argmax(ex))]), "OK|pas=%.2e" % (s[1] - s[0])

# =====================================================================
# 3. QUANTIQUE (s0 SIGNE cote fragile -- correction D-M9-1)
# =====================================================================

def etat_coherent(alpha, N):
    n = np.arange(N)
    if alpha == 0:
        c = np.zeros(N); c[0] = 1.0; return c, 0.0
    lc = -0.5 * alpha * alpha + n * log(abs(alpha)) - 0.5 * gammaln(n + 1)
    c = np.exp(lc)
    if alpha < 0:
        c = c * (-1.0) ** n
    return c, max(1.0 - float(np.sum(c * c)), 0.0)

def hamiltonien(w2, g, N, signe_fantome=-1):
    delta = w2 * w2 - W1 * W1
    def xmat(w):
        a = sp.diags(np.sqrt(np.arange(1, N)), 1, format="csr")
        return (a + a.T) / sqrt(2 * delta * w)
    I = sp.identity(N, format="csr")
    X = sp.kron(xmat(W1), I, format="csr") + sp.kron(I, xmat(w2), format="csr")
    n1 = np.repeat(np.arange(N), N).astype(float)
    n2 = np.tile(np.arange(N), N).astype(float)
    H = sp.diags(signe_fantome * W1 * n1 + w2 * n2, format="csr")
    if g != 0.0:
        Xp = X.copy()
        for _ in range(P - 1):
            Xp = (Xp @ X).tocsr()
        H = H + (g / P) * Xp
    return np.asarray(H.todense()), n1, n2

def t_shell(w2, g, N, s_signe, signe_fantome=-1):
    """s_signe = sgn_F * 0.7 * s_cible (SIGNE, D-M9-1). A1/A2 lineaires en s."""
    delta = w2 * w2 - W1 * W1
    A1 = s_signe * (1 + w2 * w2) / delta
    A2 = -s_signe * (1 + W1 * W1) / delta
    a1 = A1 * sqrt(delta * W1 / 2); a2 = A2 * sqrt(delta * w2 / 2)
    c1, q1 = etat_coherent(a1, N); c2, q2 = etat_coherent(a2, N)
    psi = np.outer(c1, c2).ravel(); psi = psi / np.linalg.norm(psi)
    H, n1, n2 = hamiltonien(w2, g, N, signe_fantome)
    w, V = np.linalg.eigh(H); del H
    m = (np.maximum(n1, n2) >= SHELL_LO) & (np.maximum(n1, n2) <= SHELL_HI)
    wS = np.einsum("ij,ij->j", V[m, :], V[m, :])
    c = V.T @ psi; del V
    return float(np.sum(c * c * wS)), max(q1, q2)

# =====================================================================
# 4. SPEARMAN + NULLE EXACTE
# =====================================================================

def rangs(v):
    return np.argsort(np.argsort(np.asarray(v, float))).astype(float)

def spearman(x, y):
    n = len(x); d2 = float(np.sum((rangs(x) - rangs(y)) ** 2))
    return 1 - 6 * d2 / (n * (n * n - 1))

def p_exact(r, n):
    vals = np.array([1 - 6 * sum((a - b) ** 2 for a, b in zip(range(n), pm)) / (n * (n * n - 1))
                     for pm in itertools.permutations(range(n))])
    return float((vals >= r - 1e-12).mean()) if r >= 0 else float((vals <= r + 1e-12).mean())

# =====================================================================
# 5. MAIN
# =====================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out")
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()

    hb, hf = certifier_gel()
    garde_G3()

    if args.smoke:
        print("PRE-VOL (--smoke) : n'ecrit rien, ne conclut rien.\n")
        t0 = time.time()
        sp_, nP = chercher_seuil(2.00, +1)
        sm_, nM = chercher_seuil(2.00, -1)
        aP, aM = ANCRES_G1A[2.00]
        print("  s*(2.00, +1) = %.5f [%s]  ancre sP %.5f  ecart %+.2f %%"
              % (sp_, nP.split("|")[0], aP, 100 * (sp_ - aP) / aP))
        print("  s*(2.00, -1) = %.5f [%s]  ancre sM %.5f  ecart %+.2f %%"
              % (sm_, nM.split("|")[0], aM, 100 * (sm_ - aM) / aM))
        sF = min(sp_, sm_); frag = 1 if sp_ <= sm_ else -1
        d = 2.00 ** 2 - 1
        s_c = sqrt(2 * NBAR * d) / (1 + 2.00 ** 2)
        g_c = (G_REF * sF ** 3) / s_c ** 3
        s0 = frag * RHO_AMP * s_c
        print("  sF=%.5f frag=%+d  s_cible=%.5f  g_cal=%.5e  s0=%+.5f"
              % (sF, frag, s_c, g_c, s0))
        t1 = time.time()
        T, q = t_shell(2.00, g_c, 56, s0)
        print("  T_shell(N=56, s0 signe) = %.5e  queue=%.1e  (%.0f s)"
              % (T, q, time.time() - t1))
        Tf, _ = t_shell(2.00, 0.0, 64, s0)
        print("  FREE (N=64) : T = %.3e (seuil %.0e)" % (Tf, SEUIL_NULL))
        print("  duree pre-vol %.0f s" % (time.time() - t0))
        return

    os.makedirs(args.out, exist_ok=True)
    fout = os.path.join(args.out, "m9_results.json")
    meta = {"manche": "M9", "gel_sha256_bloc": hb, "sha256_fichier_script": hf,
            "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "parametres": dict(p=P, w1=W1, g_ref=G_REF, dt=DT, T=T_MAX, cap=CAP,
                               ngrid=NGRID, ndense=NDENSE, w2s=W2S, ns=NS,
                               nbar=NBAR, facteur_h_s=FACTEUR_H_S, rho_amp=RHO_AMP,
                               shell=[SHELL_LO, SHELL_HI]),
            "ancres_G1a": {key(w): v for w, v in ANCRES_G1A.items()},
            "ancres_G1b_M8": {key(w): v for w, v in ANCRES_G1B.items()},
            "T_M3_N64": {key(w): v for w, v in T_M3_N64.items()},
            "gardes": [], "exclusions": []}
    R = {"carte": {}, "calibration": {}, "quantique": {}}
    def sauver():
        json.dump({"meta": meta, "resultats": R}, open(fout, "w", encoding="utf-8"),
                  indent=1, sort_keys=True)

    # ---------------- ETAGE 1 : carte deux signes ----------------
    print("=" * 78); print("ETAGE 1 -- CARTE sF, DEUX SIGNES (convention (f))"); print("=" * 78)
    for w2 in W2S:
        t0 = time.time()
        sp_, nP = chercher_seuil(w2, +1)
        sm_, nM = chercher_seuil(w2, -1)
        sF = min(sp_, sm_); frag = 1 if sp_ <= sm_ else -1
        R["carte"][key(w2)] = dict(w2=w2, sP=sp_, sM=sm_, sF=sF, frag=frag,
                                   asym=sp_ / sm_, K5=G_REF * sF ** 3,
                                   note_P=nP, note_M=nM)
        print("  w2=%.4f  sP=%.5f sM=%.5f  sF=%.5f frag=%+d asym=%+.2f %%  (%.0f s)"
              % (w2, sp_, sm_, sF, frag, 100 * (sp_ / sm_ - 1), time.time() - t0))
        sauver()

    # G1a : ancres sP ET sM, +-2 % par signe, ARRET
    for w2, (aP, aM) in ANCRES_G1A.items():
        c = R["carte"][key(w2)]
        eP = abs(c["sP"] - aP) / aP; eM = abs(c["sM"] - aM) / aM
        ok = eP <= TOL_G1A and eM <= TOL_G1A
        meta["gardes"].append("G1a w2=%.4f : sP %.5f vs %.5f (%.2f %%) | sM %.5f vs %.5f (%.2f %%) -> %s"
                              % (w2, c["sP"], aP, 100 * eP, c["sM"], aM, 100 * eM,
                                 "PASSE" if ok else "ARRET"))
        if not ok:
            sauver(); sys.exit("ARRET G1a (w2=%.4f) : investigation." % w2)
    # G1b : regression M8 (+1), 6 points, ARRET
    for w2, a in ANCRES_G1B.items():
        c = R["carte"][key(w2)]
        e = abs(c["sP"] - a) / a
        meta["gardes"].append("G1b w2=%.4f : sP %.5f vs M8 %.5f (%.2f %%) -> %s"
                              % (w2, c["sP"], a, 100 * e, "PASSE" if e <= TOL_G1B else "ARRET"))
        if e > TOL_G1B:
            sauver(); sys.exit("ARRET G1b (w2=%.4f)." % w2)

    K5 = {w: R["carte"][key(w)]["K5"] for w in W2S}
    kmin = min(K5, key=lambda w: K5[w])
    pre_ok = abs(kmin - 2.00) > 1e-9
    meta["verdict_P_M9_pre"] = "LIEN CONFIRME" if pre_ok else "LIEN REFUTE"
    meta["gardes"].append("P-M9-pre : argmin K5_min a w2=%.4f -> %s" % (kmin, meta["verdict_P_M9_pre"]))
    print("\n  P-M9-pre : argmin K5_min = %.4f -> %s" % (kmin, meta["verdict_P_M9_pre"]))
    if not pre_ok:
        print("  (etage 2 SANS prediction ; interdiction de re-deriver, lecon E15)")

    # G2 : invariance a 2g, deux signes, 2 points
    exclus = set()
    for w2 in PTS_CTRL:
        s2p, _ = chercher_seuil(w2, +1, g=2 * G_REF)
        s2m, _ = chercher_seuil(w2, -1, g=2 * G_REF)
        K2 = 2 * G_REF * min(s2p, s2m) ** 3
        ec = abs(K2 - K5[w2]) / K5[w2]
        ok = ec <= TOL_G2
        meta["gardes"].append("G2 w2=%.4f : K(g)=%.6g K(2g)=%.6g ecart %.2f %% -> %s"
                              % (w2, K5[w2], K2, 100 * ec, "PASSE" if ok else "LIGNE EXCLUE"))
        if not ok:
            exclus.add(w2); meta["exclusions"].append(dict(w2=w2, garde="G2", ecart=ec))
        sauver()

    # ---------------- Calibration + G5 + G4 ----------------
    print("\n  Calibration (forme fermee (f), nbar = %.1f ; ecart (h) consigne) :" % NBAR)
    for w2 in W2S:
        c = R["carte"][key(w2)]
        d = w2 * w2 - 1
        s_c = sqrt(2 * NBAR * d) / (1 + w2 * w2)
        g_c = K5[w2] / s_c ** 3
        s1, _ = chercher_seuil(w2, c["frag"], g=g_c)
        deux = abs(c["asym"] - 1) > ASYM_DOUBLE
        if deux:
            s2, _ = chercher_seuil(w2, -c["frag"], g=g_c)
            s_min_cal = min(s1, s2)
            frag_cal = c["frag"] if s1 <= s2 else -c["frag"]
        else:
            s2, s_min_cal, frag_cal = None, s1, c["frag"]
        e5 = abs(s_min_cal - s_c) / s_c
        ok = e5 <= TOL_G5
        R["calibration"][key(w2)] = dict(w2=w2, s_cible=s_c, g_cal=g_c,
                                         g_cal_equiv_M3=g_c / FACTEUR_H_S ** 3,
                                         s_frag=s1, s_autre=s2, s_min_cal=s_min_cal,
                                         frag_cal=frag_cal, ecart_G5=e5,
                                         s0=c["frag"] * RHO_AMP * s_c)
        note = "" if frag_cal == c["frag"] else "  [COTE FRAGILE DIFFERENT a g_cal : consigne]"
        print("    w2=%.4f  s_cible=%.4f  g_cal=%.5e  s*_min(g_cal)=%.4f  ecart %.2f %% -> %s%s"
              % (w2, s_c, g_c, s_min_cal, 100 * e5, "OK" if ok else "EXCLU", note))
        if not ok:
            exclus.add(w2); meta["exclusions"].append(dict(w2=w2, garde="G5", ecart=e5))
        sauver()

    raid = {w: R["calibration"][key(w)]["g_cal"] * R["carte"][key(w)]["sF"] ** 4 for w in W2S}
    wst = max(raid, key=lambda w: raid[w])
    cal = R["calibration"][key(wst)]
    s_h, _ = chercher_seuil(wst, R["carte"][key(wst)]["frag"], dt=DT / 2, g=cal["g_cal"])
    e4 = abs(s_h - cal["s_frag"]) / cal["s_frag"]
    meta["gardes"].append("G4 ligne la plus raide (g_cal sF^4) w2=%.4f : s*(dt)=%.5f s*(dt/2)=%.5f "
                          "ecart %.3f %% -> %s" % (wst, cal["s_frag"], s_h, 100 * e4,
                                                   "PASSE" if e4 <= TOL_G4 else "NON FIABLE"))
    sauver()

    # ---------------- ETAGE 2 : quantique ----------------
    print("\n" + "=" * 78); print("ETAGE 2 -- QUANTIQUE (s0 signe cote fragile)"); print("=" * 78)
    for w2 in W2S:
        cal = R["calibration"][key(w2)]
        s0 = cal["s0"]
        for N in NS:
            t0 = time.time()
            T, q = t_shell(w2, cal["g_cal"], N, s0)
            if q > TOL_G6 and w2 not in exclus:
                exclus.add(w2); meta["exclusions"].append(dict(w2=w2, garde="G6", queue=q))
            R["quantique"]["ghost|%s|%d" % (key(w2), N)] = dict(w2=w2, N=N, T=T, queue=q,
                                                               g=cal["g_cal"], s0=s0)
            print("  GHOST w2=%.4f N=%d s0=%+.4f : T=%.5e queue=%.1e (%.0f s)"
                  % (w2, N, s0, T, q, time.time() - t0))
            sauver()
        Tr, _ = t_shell(w2, cal["g_cal"], 64, s0, signe_fantome=+1)
        R["quantique"]["retourne|%s|64" % key(w2)] = dict(w2=w2, N=64, T=Tr, s0=s0)
        Tg = R["quantique"]["ghost|%s|64" % key(w2)]["T"]
        print("    retourne : T=%.5e | Q = T_ghost/T_ret = %.4g" % (Tr, Tg / Tr if Tr else float("inf")))
        sauver()

    for w2 in PTS_CTRL:
        cal = R["calibration"][key(w2)]
        Tf, _ = t_shell(w2, 0.0, 64, cal["s0"])
        R["quantique"]["free|%s|64" % key(w2)] = dict(w2=w2, N=64, T=Tf)
        st = "PASSE" if Tf < SEUIL_NULL else "ECHEC -> ARRET"
        meta["gardes"].append("P-M9-null FREE w2=%.4f : T=%.3e -> %s" % (w2, Tf, st))
        print("  FREE w2=%.4f : T=%.3e -> %s" % (w2, Tf, st))
        if Tf >= SEUIL_NULL:
            sauver(); sys.exit("ARRET P-M9-null.")
        sauver()

    # ---------------- PORTES ----------------
    print("\n" + "=" * 78); print("PORTES (mecaniques)"); print("=" * 78)
    ret = [w for w in W2S if w not in exclus]
    n_ret = len(ret)
    print("  points retenus : %d / 6 %s" % (n_ret, ("(exclus : %s)" % sorted(exclus)) if exclus else ""))
    meta["rho"] = {}
    Kv = [K5[w] for w in ret]
    Cv = [K5[w] / ((w - 1) ** 2 * (1 + w)) for w in ret]
    for N in NS:
        Tv = [R["quantique"]["ghost|%s|%d" % (key(w), N)]["T"] for w in ret]
        rk, rc = spearman(Tv, Kv), spearman(Tv, Cv)
        meta["rho"]["retenus|N%d" % N] = dict(n=n_ret, rho_K=rk, p_K=p_exact(rk, n_ret),
                                              rho_C=rc, p_C=p_exact(rc, n_ret))
        print("  N=%d (n=%d) : rho(T,K5_min) = %+.4f p=%.4f | rho(T,C5) = %+.4f p=%.4f"
              % (N, n_ret, rk, p_exact(rk, n_ret), rc, p_exact(rc, n_ret)))
    can_ret = [w for w in CANON if w in ret]
    for N in NS:
        Tv = [R["quantique"]["ghost|%s|%d" % (key(w), N)]["T"] for w in can_ret]
        Kc = [K5[w] for w in can_ret]
        rk = spearman(Tv, Kc)
        meta["rho"]["canoniques|N%d" % N] = dict(n=len(can_ret), rho_K=rk,
                                                 p_K=p_exact(rk, len(can_ret)))
        print("  canoniques N=%d (n=%d) : rho(T,K5_min) = %+.4f p=%.4f"
              % (N, len(can_ret), rk, p_exact(rk, len(can_ret))))

    # P-M9a
    if n_ret >= 5:
        seuil = SEUILS_RHO[n_ret]
        r56 = meta["rho"]["retenus|N56"]["rho_K"]; r64 = meta["rho"]["retenus|N64"]["rho_K"]
        if r56 >= seuil and r64 >= seuil:
            va = "REPLICATION CONFIRMEE -- premier soutien puissante de la jambe quantique"
        elif r56 <= -seuil and r64 <= -seuil:
            va = "REFUTATION (legitime : memes systemes que M3) -- +1.00 requalifie ET jambe morte"
        else:
            va = "NON CONCLUANT -> COMPENSATION C2 : rearme integral de la clause anti-empilement"
        print("\n  P-M9a (seuil +-%.2f, n=%d) : %+.4f / %+.4f -> %s" % (seuil, n_ret, r56, r64, va))
        if 0.60 <= min(r56, r64) < seuil:
            print("  ANTI-ARRET-OPTIONNEL : aucune prolongation de M9.")
    else:
        va = "ECHEC DE DESIGN (n_retenu <= 4) -- pas un verdict physique ; redesign obligatoire"
        print("\n  P-M9a : %s" % va)
    meta["verdict_P_M9a"] = va

    # P-M9b
    Q = {w: R["quantique"]["ghost|%s|64" % key(w)]["T"] /
            R["quantique"]["retourne|%s|64" % key(w)]["T"] for w in W2S}
    meta["P_M9b_Q"] = {key(w): Q[w] for w in W2S}
    bas = [w for w in W2S if Q[w] <= 3.0]
    if all(Q[w] >= 10.0 for w in W2S):
        vb = "contraste fantome grand a p=5 (>= 10 partout)"
    elif bas:
        vb = "branche '<= 3 quelque part' DECLENCHEE (%s) -> caveat cause (2) sur P-M9a" % \
             ", ".join("%.4g" % w for w in bas)
    else:
        vb = "zone intermediaire : consigne sans lecture"
    print("  P-M9b : Q = " + " / ".join("%.3g" % Q[w] for w in W2S))
    print("          -> %s" % vb)
    meta["verdict_P_M9b"] = vb

    # P-M9c : replication directe
    print("  P-M9c : T_M9/T_M3 aux canoniques (N=64), fenetre pre-declaree [%.2f, %.2f] :"
          % FEN_M9C)
    ratios = {}
    alerte = False
    for w in CANON:
        r = R["quantique"]["ghost|%s|64" % key(w)]["T"] / T_M3_N64[w]
        ratios[key(w)] = r
        dedans = FEN_M9C[0] <= r <= FEN_M9C[1]
        alerte = alerte or not dedans
        print("    w2=%.4f : %.3f %s" % (w, r, "" if dedans else "  <- HORS FENETRE"))
    meta["P_M9c_ratios"] = ratios
    meta["P_M9c_alerte"] = alerte
    if alerte:
        print("    ALERTE pre-declaree : investigation avant toute interpretation de P-M9a.")
    else:
        print("    -> le protocole refait les systemes de M3 (offset uniforme tolere).")

    # G7
    Tv56 = [R["quantique"]["ghost|%s|56" % key(w)]["T"] for w in ret]
    Tv64 = [R["quantique"]["ghost|%s|64" % key(w)]["T"] for w in ret]
    meta["gardes"].append("G7 rho(T56,T64) retenus = %+.2f [consigne]" % spearman(Tv56, Tv64))
    for w in W2S:
        meta["gardes"].append("   G7 w2=%.4f : T56/T64 = %.3f"
                              % (w, R["quantique"]["ghost|%s|56" % key(w)]["T"] /
                                 R["quantique"]["ghost|%s|64" % key(w)]["T"]))

    print("\n" + "=" * 78); print("GARDES"); print("=" * 78)
    for l in meta["gardes"]:
        print("  " + l)
    sauver()
    print("\nEcrit : %s" % fout)
    print("sha256 du JSON : %s" % hashlib.sha256(open(fout, "rb").read()).hexdigest())

if __name__ == "__main__":
    main()
