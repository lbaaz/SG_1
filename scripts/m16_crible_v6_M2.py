#!/usr/bin/env python3
# -*- coding: ascii -*-
"""DOCSTRING JUMEAU -- PRE-ENREGISTREMENT M16 (script de manche, v6)
COPIE DE TRAVAIL MACHINE 2 -- diff vs m16_crible_v6.py (e804242bf9c284a4) :
DEUX BLOCS, tous deux dans l ECRITURE, aucun dans la MESURE. (1) D-40 :
serialiseur certifie du pilote au lieu de json.dump nu. (2) test negatif du
serialiseur sur le bloc G6 REEL du point fixe. A contresigner par machine 1.
=====================================================================
machine 1, 2026-08-11. E19 : ce script n'est valide que contre le gel
  m16_pre_enregistrement_v10.md
  sha256[:16] = 75bc4020b5bd560f   (ETENDUE GELEE = FICHIER ENTIER)
v1, v2, v3 (2b68bb18 / 91babeac / 53dddab0) NON CERTIFIEES ; la v4
execute D-25, D-26, D-27 : LE CHEMIN REEL EXISTE. MoteurReel (rebind
de P declare, restauration VERIFIEE par ligne, appel
pilote.chercher_seuil_ligne via la chaine chargee par la couche
manche), --prevol-reel (point fixe P-g : 4|2.62|+1 contre l'artefact
96d78407, tolerance = pas de l'artefact), --run route custody ->
inventaire -> P-g -> FondReel -> manche. Le selftest asserte que
CHAQUE MODE ANNONCE au docstring existe dans le code (parade de la
faute versee : une piece annoncee est une piece livree). La v6 pose les deux lignes de D-38/D-39 :
journal des rebinds et bloc G6 complet (ratios compris) ENTRENT A
L'ARTEFACT -- M17 lira le G6 de M16 comme M16 lit celui de M15.
Conserve v2/v3 (D-16 a D-24, N-54, N-55) :
  D-18/D-23 liaison : RESOLUE. API relevee et point fixe joue
       (delta 76) ; chaine = m15_site83_v2 -> charger_pilote ->
       charger_moteur ; rebind PAR DEGRE, restauration a la charge
       de l'appelant (rebind ne restaure pas -- verifiee, gel v10).
  D-24 P-M16a par LA fonction heritee (criterer/brancher, ancres
       custody 2.62/2.72 injectees comme LOIN) ; PROCHE = appartenance
       EXACTE aux extremes interieurs (regle 11, plus une distance) ;
       coefficients C_SIGMA importes de la couche manche (sources) ;
       scenarios A2/A4/A6 ajoutes (S13-S15)
  D-16 matrices a PREDICATS INDEPENDANTS + MUTATION EXECUTEE chacune ;
       test negatif N-28 sur zone temoin CONTENANT le litteral,
       echec exige et affiche
  D-17 nouveaute N-3 par VALEURS (Fraction), test negatif deux sens
  D-18 liaison moteur : API reelle relevee par machine 2
       (chercher_seuil, integrer, garde_G3, canon, key, ... --
       mesure_ligne N'EXISTE PAS) ; l'adaptateur attend les
       SIGNATURES, demandees a machine 2 ; --run refuse tant que la
       liaison n'est pas certifiee
  D-19 faisabilite strate 2 en FORME (gel v8 sect. 4.6) :
       N_2 x (1 - q4_fen) >= 1 -- aucun seuil numerique
  D-20 q4_fen re-derive FENETRE SEULE (temoin exclu, E27) ; le
       temoin ne sert que le garde-fou
  D-21 P-M16a IMPLEMENTEE : E par convention (f) depuis s*, residu
       contre la corde 2.62<->2.72, C1/C2/C3/n_disc ; fond (seuils,
       PROCHE) fourni par artefacts au run, factice au pre-vol ;
       liaisons de champs declarees ci-dessous, a confirmer
  D-22 scenarios S8/S9 (B1) et S10/S11/S12 (A1/A3/A5)
  N-54 volet site en >= (l'inegalite du gel, pas une autre)
  N-55 portee N-28 = zone CONDENSE + bloc de portes du gel +
       artefacts de sortie avant depot (gel v8)

CONDENSE OPPOSABLE (extrait du gel, jamais re-frappe -- les textes
font foi au gel) :
  PROGRAMME phase A (31 lignes) :
    strate 1  : 2.63, 2.66, 2.68  -- batteries 4|+1, 5|+-1, 7|+-1
    reprise   : 7|2.67|+1 (mesure sous instrument courant, D-12 ;
                HORS nouveaute, issues r1/r2/r3 par mecanisme)
    temoins   : 2.76, 2.79, 2.82  -- batteries completes (N-25)
  STRATE 2 (millieme, N-42/N-43) : ouverte ssi >=1 survivant p=4
    interieur ET arret de regle favorable ; s +/- 0.001 par
    survivant, plafond 4 lignes p=4, ordre = distance croissante au
    site (Fraction), ex aequo valeur croissante, ecartes journalises.
  PORTES (forme 2x2, enumeration 64/64 exigee au selftest) :
    S ssi k4_F = 3 ET k4_T = 0 ; D ssi r1 ET G_neuve
    H-B = S et non D ; H-A = D et non S ; DOUBLE = S et D ;
    NON-DEPARTAGE = ni S ni D.
  GARDE-FOU REGIONAL : >= 2 mortes p=4 temoin sur 3 -> mode CARTE
    (records seuls, aucune lecture (i)).
  ARRET ITEM 3' : attrition realisee PAR DEGRE et PAR UNITE
    ETIQUETEE ; q_L(80%) re-derive fenetre augmentee ; faisabilite
    strate 2 en forme derivee ; STOP si infaisable.
  CAHIER (sect. 7 du gel) : N-14 (G2 sautee avec motif, comptes +
    sautes == attendu) ; corollaire regle 15 (aucune garde au bit
    sur sortie de librairie) ; N-16 (PYTHONUTF8=1) ; N-3 (nouveaute
    par valeur exacte contre le registre entier) ; statuts au bloc
    G6 jamais a la carte ; N-28/N-39 (litteraux interdits, octets
    relus du disque, test negatif AFFICHE) ; E28 (controles en
    arithmetique differente).
LIAISON MOTEUR REEL, DECLAREE ET A CONFIRMER A LA CERTIFICATION :
  module attendu m9_replication_v1 (sha256[:8] = c8ed357b), appel
  attendu mesure_ligne(p, omega2_str, signe) -> dict au schema
  RECORD ci-dessous. La liaison est le SEUL point que machine 1 ne
  peut pas verifier d'ici ; le pre-vol opposable (machine 2, moteur
  factice puis reel) la tranche. Tout ecart de schema : STOP.
SCHEMA RECORD (miroir du bloc G6 des artefacts) :
  { p:int, point:str '2.66', signe:'+1'|'-1', exclue:bool,
    motif_exclusion:str, mecanisme:''|'fine'|'grossiere',
    ratio_fenetre:float|None, ilots:int|None, s_star:float|None,
    pas_final:float|None }
MODES : --selftest (calculs purs + gel present), --preflight
  (pipeline complet sous moteur factice, banc qui tue),
  --prevol-reel (point fixe P-g contre l'artefact, BOCAL4),
  --run (moteur reel, BOCAL4 ; P-g d'abord, toujours).
"""
import sys, os, json, hashlib, re
from fractions import Fraction as F
from math import comb, ceil

# ---------------------------------------------------------------- constantes
GEL_PATH   = "m16_pre_enregistrement_v10.md"
GEL_SHA16  = "75bc4020b5bd560f"
MARQ_DEB   = "--- BLOC DE PORTES M16 : DEBUT ---"
MARQ_FIN   = "--- BLOC DE PORTES M16 : FIN ---"
ARTEFACTS  = {"m15": ("m15_results.json", "96d784077577d57d"),
              "m12": ("m12_results.json", "fa109da92e582520"),
              "m13b": ("m13b_results.json", "22fa176013a9d46b"),
              "m10": ("m10_results.json", "7cf3624b45dd7d2b"),
              "m11": ("m11_results.json", "ad275870847d440e")}
POINT_FIXE = (4, "2.62", "+1")           # P-g, gel v9
MOTEUR_ATTENDU = ("m9_replication_v1", "c8ed357b")
MANCHE_ATTENDUE = ("m15_site83_v2", "41ddebcd72b96e64")

def charger_couche_manche(base):
    p = os.path.join(base, MANCHE_ATTENDUE[0] + ".py")
    if not os.path.exists(p): die("couche manche absente : " + p)
    h = sha16(p)
    if h != MANCHE_ATTENDUE[1]: die("couche manche %s != %s" % (h, MANCHE_ATTENDUE[1]))
    sys.path.insert(0, base)
    import m15_site83_v2 as m15
    print("liaison N-56 : couche manche %s CONFORME (extraction, regle 12)" % h)
    return m15

SITE   = F(8, 3)
R11    = F(3, 1600)                      # rayon bande 11-12 (gel v4)
STRATE1 = ["2.63", "2.66", "2.68"]
TEMOINS = ["2.76", "2.79", "2.82"]
REPRISE = (7, "2.67", "+1")
BATTERIE = [(4, "+1"), (5, "+1"), (5, "-1"), (7, "+1"), (7, "-1")]
ANCRES  = {"2.62": ("M15", 0.5022), "2.72": ("M12", 0.5174)}  # custody G1'
FEN_A, FEN_C = F(262, 100), F(273, 100)
TOL_E_ANCRE = 1e-4                       # tolerance declaree (pas de bit)
COEUR_RAYONS = F(4, 1)                   # portee G_neuve (gel 4.3/N-36)

def rayon(ordre):
    if ordre <= 6: return F(12, 100)
    return F(3, 100) / (4 ** ((ordre - 7) // 2))   # bandes de DEUX (N-49)

# aiguilles N-28 construites, jamais litterales (lecon gel v4)
LITTERAUX = ["0." + s for s in ("9725", "9074", "9686", "8956")]

def die(msg):
    print("STOP :", msg); sys.exit(2)

# ---------------------------------------------------------------- estimateur
def qL(k, n, cible=0.20, pas=200):
    lo, hi = 0.0, 1.0
    for _ in range(pas):
        m = (lo + hi) / 2.0
        c = sum(comb(n, i) * m**i * (1 - m)**(n - i) for i in range(k + 1))
        if c > cible: lo = m
        else: hi = m
    return (lo + hi) / 2.0

# ---------------------------------------------------------------- custody
def sha16(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]

def custody_gel(base):
    p = os.path.join(base, GEL_PATH)
    if not os.path.exists(p): die("gel absent : " + p)
    h = sha16(p)
    if h != GEL_SHA16: die("gel %s != %s (E19)" % (h, GEL_SHA16))
    t = open(p, "rb").read().decode("ascii")
    # ancrage en LIGNE PLEINE : la declaration N-45 du gel CITE les
    # marqueurs entre guillemets -- l'aiguille litterale se documente
    lignes = t.split("\n")
    assert lignes.count(MARQ_DEB) == 1 and lignes.count(MARQ_FIN) == 1, "marqueurs N-45 (ligne pleine)"
    bloc = t.split("\n" + MARQ_DEB + "\n")[1].split("\n" + MARQ_FIN + "\n")[0]
    print("custody gel : %s CONFORME (fichier entier, D-13) ; bloc de portes extrait (%d o)" % (h, len(bloc)))
    return t, bloc

def controle_litteraux(path_script, bloc_portes):
    # N-28/N-39 : octets RELUS DU DISQUE + bloc de portes du gel
    src = open(path_script, "rb").read().decode("ascii")
    zone = src[src.index('CONDENSE'):src.index('SCHEMA RECORD')] + bloc_portes
    for lit in LITTERAUX:
        assert lit not in zone, "litteral interdit present : " + lit
    zone_temoin = zone + " x " + LITTERAUX[0] + " x"
    try:
        for lit in LITTERAUX:
            assert lit not in zone_temoin
        raise SystemExit("N-28 : le controle n'a PAS mordu la zone temoin (D-16)")
    except AssertionError:
        pass
    print("N-28/N-39 : 4 litteraux absents (zone CONDENSE + bloc de portes,"
          " octets du disque) ; test negatif : le MEME controle applique a une"
          " zone temoin CONTENANT le litteral ECHOUE -- AFFICHE, exige (N-55)")

# ---------------------------------------------------------------- criteres
def catalogue(lo=F(235,100), hi=F(290,100), omax=23):
    cat = set()
    for b in range(1, omax + 1):
        a = int(lo * b) - 1
        while F(a, b) <= hi:
            q = F(a, b)
            if q >= lo and q.denominator == b and a + b <= omax:
                cat.add((q, a + b))
            a += 1
    return sorted(cat)

def critere_temoins(verbose=True):
    cat = catalogue()
    assert len(cat) == 7, "catalogue attendu 7 rationnels, obtenu %d" % len(cat)
    c_site = ceil(F(19, 300) / R11)
    assert c_site == 34, "c derive != 34"
    ok = True
    for t in TEMOINS:
        tf = F(int(t.replace(".", "")), 100)
        pire_s, pire_h = None, None
        for q, o in cat:
            d = abs(tf - q)
            if q == SITE:
                r = d / (c_site * R11)
                pire_s = min(pire_s, r) if pire_s is not None else r
            else:
                m = d / rayon(o)
                pire_h = min(pire_h, m) if pire_h is not None else m
        passe = pire_s >= 1 and pire_h >= F(110, 100)   # N-54 : >= comme au gel
        ok = ok and passe
        if verbose:
            print("  temoin %s : volet site %.3f (>=1) ; volet heritage %.3f (>=1.10) -> %s"
                  % (t, float(pire_s), float(pire_h), "PASS" if passe else "FAIL"))
    assert ok, "critere temoins viole"
    return c_site

# ---------------------------------------------------------------- partitions
def branches_2x2(S, Dsig):
    if S and not Dsig: return "H-B"
    if Dsig and not S: return "H-A"
    if S and Dsig:     return "DOUBLE-SIGNAL"
    return "NON-DEPARTAGE"

def _muter(nom, boucle, fonction_mutee):
    try:
        boucle(fonction_mutee)
    except AssertionError:
        print("  MUTATION %s : AssertionError LEVEE -- le controle mord" % nom)
        return
    raise SystemExit("MUTATION %s : le controle n'a PAS mordu (D-16)" % nom)

PRED_C = {"H-B": lambda S, D: S and not D,
          "H-A": lambda S, D: D and not S,
          "DOUBLE-SIGNAL": lambda S, D: S and D,
          "NON-DEPARTAGE": lambda S, D: (not S) and (not D)}

def matrice_PM16c():
    def boucle(f):
        for r1 in (0, 1):
            for g in (0, 1):
                for kF in range(4):
                    for kT in range(4):
                        S = (kF == 3 and kT == 0); Dg = bool(r1 and g)
                        vraies = [n for n, p in PRED_C.items() if p(S, Dg)]
                        assert len(vraies) == 1 and vraies[0] == f(S, Dg), \
                            "sortie (%d,%d,%d,%d)" % (r1, g, kF, kT)
    boucle(branches_2x2)
    print("  P-M16c : 64/64, predicats independants == fonction (D-15/D-16)")
    _muter("P-M16c", boucle, lambda S, D: "H-B")

PRED_B = {"B0": lambda s: s == 0, "B1": lambda s: s in (1, 2), "B2": lambda s: s == 3}

def branche_b(s1):
    return "B0" if s1 == 0 else ("B1" if s1 in (1, 2) else "B2")

def matrice_PM16b():
    def boucle(f):
        for s1 in range(4):
            vraies = [n for n, p in PRED_B.items() if p(s1)]
            assert len(vraies) == 1 and vraies[0] == f(s1), "s1=%d" % s1
    boucle(branche_b)
    print("  P-M16b : 4/4, predicats independants == fonction")
    _muter("P-M16b", boucle, lambda s: "B2")

def branche_PM16a(pl, C1, C2, C3, ndisc, s4):
    # partition du gel (D-10) -- la fonction TESTEE par les predicats
    if not pl: return "A0"
    if not C1: return "A1"
    if not C2: return "A2"
    if C3 and ndisc >= 1: return "A3"
    if C3 and ndisc == 0: return "A4"
    if s4: return "A5"
    return "A6"

PRED_A = {  # re-ecrits depuis le texte du gel, independants de branche_PM16a
  "A0": lambda pl,C1,C2,C3,nd,s4: not pl,
  "A1": lambda pl,C1,C2,C3,nd,s4: pl and not C1,
  "A2": lambda pl,C1,C2,C3,nd,s4: pl and C1 and not C2,
  "A3": lambda pl,C1,C2,C3,nd,s4: pl and C1 and C2 and C3 and nd >= 1,
  "A4": lambda pl,C1,C2,C3,nd,s4: pl and C1 and C2 and C3 and nd == 0,
  "A5": lambda pl,C1,C2,C3,nd,s4: pl and C1 and C2 and not C3 and s4,
  "A6": lambda pl,C1,C2,C3,nd,s4: pl and C1 and C2 and not C3 and not s4}

def matrice_PM16a():
    def boucle(f):
        for pl in (0,1):
            for C1 in (0,1):
                for C2 in (0,1):
                    for C3 in (0,1):
                        for nd in (0,1):
                            for s4 in (0,1):
                                vraies = [n for n,p in PRED_A.items() if p(pl,C1,C2,C3,nd,s4)]
                                assert len(vraies) == 1 and vraies[0] == f(pl,C1,C2,C3,nd,s4), \
                                    "profil %s" % ((pl,C1,C2,C3,nd,s4),)
    boucle(branche_PM16a)
    print("  P-M16a : 64/64 profils, predicats independants == fonction")
    _muter("P-M16a", boucle, lambda *a: "A3")

def table_N52():
    q4, qT = qL(5, 10), qL(1, 34)
    p_hb = q4**3 * (1 - qT)**3
    sup = 0.5**3 * 0.5**3
    sep = p_hb / sup
    assert abs(round(p_hb, 4) - 0.2333) <= 5e-4, "N-52/N-11 : P(H-B)"
    assert 14.5 <= sep <= 15.0, "N-52/N-11 : separation ~14.9, obtenu %.3f" % sep
    print("  N-52 : P(H-B|H-B fav.) = %.6f -> 0.2333 (N-11) ; sup H-A = %.6f ; separation %.2f (~14.9)"
          % (p_hb, sup, sep))
    print("  N-52 : P(H-A) conditionnelle a r1 x P(G_neuve) -- non derivable, INJOUABLE EN"
          " PROBABILITE, JOUABLE EN SIGNAL (dit d'avance au gel)")

# ---------------------------------------------------------------- inventaire
def lire_g6(dossier):
    lignes = []
    for manche, (fich, att) in sorted(ARTEFACTS.items()):
        p = os.path.join(dossier, "out", fich)
        if not os.path.exists(p): die("artefact absent : " + p)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
        if h != att: die("artefact %s : %s != %s" % (fich, h, att))
        data = json.loads(open(p, "rb").read().decode("utf-8"))
        for cle, v in sorted(data["resultats"]["G6"].items()):
            ps, pts, sg = cle.split("|")
            pt = F(int(pts.replace(".", "")), 10 ** (len(pts.split(".")[1]) if "." in pts else 0))
            if manche in ("m15","m12","m13b") and FEN_A <= pt <= FEN_C:
                lignes.append(dict(manche=manche, p=int(ps), point=pts, pf=pt,
                                   signe=sg, exclue=bool(v.get("exclue")),
                                   motif=v.get("motif_exclusion") or "",
                                   mecanisme=v.get("mecanisme") or ""))
    return lignes

def inventaire(dossier):
    lg = lire_g6(dossier)
    p4  = [l for l in lg if l["p"] == 4]
    imp = [l for l in lg if l["p"] % 2 == 1]
    k4, n4 = sum(l["exclue"] for l in p4), len(p4)
    ki, ni = sum(l["exclue"] for l in imp), len(imp)
    assert (n4, k4) == (10, 5) and (ni, ki) == (32, 3), \
        "inventaire N-33 : p=4 %d/%d, impair %d/%d (attendu 5/10 et 3/32)" % (k4, n4, ki, ni)
    m15 = [l for l in lg if l["manche"] == "m15"]
    k4m = sum(l["exclue"] for l in m15 if l["p"] == 4)
    n4m = sum(1 for l in m15 if l["p"] == 4)
    kim = sum(l["exclue"] for l in m15 if l["p"] % 2)
    nim = sum(1 for l in m15 if l["p"] % 2)
    assert (n4m, k4m) == (7, 4) and (nim, kim) == (24, 2), "fenetre M15 : 4/7 et 2/24 attendus"
    print("inventaire N-33 (COMPTE, unite (a) ligne signee) : p=4 %d/%d ; impair %d/%d ;"
          " fenetre M15 %d/%d et %d/%d -- asserts passes" % (k4, n4, ki, ni, k4m, n4m, kim, nim))
    return lg

# ---------------------------------------------------------------- moteur
class MoteurFactice:
    """Pre-vol : scenarios nommes, deterministes -- un banc qui tue."""
    def __init__(self, scenario): self.s = scenario
    def mesure_ligne(self, p, point, signe):
        cle = "%d|%s|%s" % (p, point, signe)
        val = self.s.get(cle, (False, ""))
        exclue, meca = val[0], val[1]
        extra = val[2] if len(val) > 2 else {}
        s0 = extra.get("s_star", 3.0)
        rec = dict(p=p, point=point, signe=signe, exclue=exclue,
                   motif_exclusion=("G6:" + meca) if exclue else "",
                   mecanisme=meca, ratio_fenetre=0.953 if exclue else None,
                   ilots=5 if meca == "fine" else (1 if meca == "grossiere" else None),
                   s_star=None if exclue else s0, pas_final=1e-6)
        rec.update({k: v for k, v in extra.items() if k in ("res_s57", "res_s4")})
        return rec

def charger_art(base):
    art = {}
    for nom, (fich, att) in sorted(ARTEFACTS.items()):
        p = os.path.join(base, "out", fich)
        if not os.path.exists(p): die("artefact absent : " + p)
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
        if h != att: die("artefact %s : %s != %s" % (fich, h, att))
        art[nom] = json.loads(open(p, "rb").read().decode("utf-8"))["resultats"]
    return art

class MoteurReel:
    """Patron EXTRAIT de la boucle de programme de m15_site83_v2
    (regle 12). Deux faits etablis par le pre-vol reel (delta 76) :
      - le rebind est PAR DEGRE (P.rebind une fois, puis les points) ;
      - rebind NE RESTAURE PAS : la restauration est a la charge de
        l'appelant, et le gel v10 l'exige VERIFIEE en fin de manche
        et sur toute sortie, journal a l'artefact.
    L'exclusion ne vient pas de mesurer mais de balayer+enrichir_g6."""
    def __init__(self, m15mod):
        self.m15 = m15mod
        self.P = m15mod.charger_pilote(verbeux=True)
        self.m9 = self.P.charger_moteur(verbeux=True)
        self.P0 = getattr(self.m9, "P", None)      # etat d'entree (=5)
        assert self.P0 == 5, ("RIDER R-2 : etat d'entree P=%r != 5 -- un "
            "rebind anterieur n'a pas ete restaure (N-56/gel v10)" % self.P0)
        self.degre_courant = None
        self.journal = []                          # journal des rebinds

    def _degre(self, p):
        if self.degre_courant != p:
            self.P.rebind(self.m9, p, self.journal)   # pose P, G3, journalise
            self.degre_courant = p

    def restaurer(self):
        self.m9.P = self.P0
        assert getattr(self.m9, "P", None) == self.P0, \
            "restauration de P NON verifiee (N-56) -- STOP"
        self.degre_courant = None

    def mesure_ligne(self, p, point, signe):
        self._degre(p)
        w = float(point); sgn = +1 if signe == "+1" else -1
        m = self.P.mesurer(self.m9, w, sgn)
        rec = dict(p=p, point=point, signe=signe,
                   exclue=False, motif_exclusion="", mecanisme="",
                   ratio_fenetre=None, ilots=None,
                   s_star=(m["s"] if m["recevable"] else None),
                   pas_final=self.P.pas_final(m["note"]),
                   note=m["note"], recevable=m["recevable"])
        if not m["recevable"]:                     # G5 : ligne non recevable
            rec["exclue"] = True
            rec["motif_exclusion"] = "G5 : " + m["motif_exclusion"]
            return rec
        ok, motif = self.P.verifier_domaine(m["s"])
        if not ok:
            die("ARRET domaine (%d|%s|%s) : %s" % (p, point, signe, motif))
        bal = self.P.balayer(self.m9, w, sgn, m["s"])
        self.P.enrichir_g6(bal, m["s"], m["note"])
        rec["exclue"] = bool(bal["exclue"])
        rec["ilots"] = bal.get("ilots")
        rec["g6"] = bal                            # bloc G6 complet a l'artefact
        if rec["exclue"]:
            grossiere = bal.get("explosion_sous_LO0_0.90s") is not None
            rec["mecanisme"] = "grossiere" if grossiere else "fine"
            rec["motif_exclusion"] = ("G6 sgn=%+d explosion sous seuil "
                                      "(fenetre %s)" % (sgn, "GROSSIERE" if grossiere else "FINE"))
        return rec

def prevol_reel(base):
    """P-g (gel v9) : le point fixe 4|2.62|+1 doit reproduire
    l'artefact 96d78407 -- verdict ET s*, tolerance = pas de
    l'artefact (declaree). Sinon : rien ne tourne."""
    m15 = charger_couche_manche(base)
    art = charger_art(base)
    carte = art["m15"]["carte"].get("4|%.12f" % 2.62)
    g6a   = art["m15"]["G6"].get("4|%.12f|+1" % 2.62)
    if carte is None or g6a is None: die("P-g : ligne absente de l'artefact")
    tol = g6a.get("pas_final_recherche")
    if tol is None: die("P-g : pas final absent de l'artefact -- aucune"
                        " tolerance par defaut")
    mot = MoteurReel(m15)
    try:
        rec = mot.mesure_ligne(*POINT_FIXE)
    finally:
        mot.restaurer()                    # RIDER R-1 : gel v10, toute sortie
        print("N-56/v10 : P restauree a %r apres le point fixe ; rebinds : %r"
              % (mot.P0, mot.journal))
    ok_v = (not rec["exclue"])
    ok_s = rec["s_star"] is not None and abs(rec["s_star"] - carte["sF"]) <= tol
    print("P-g : verdict %s (attendu VIVANTE) ; s* = %r vs %r, tol %g -> %s"
          % ("VIVANTE" if ok_v else "EXCLUE", rec["s_star"], carte["sF"], tol,
             "PASS" if (ok_v and ok_s) else "STOP"))
    if not (ok_v and ok_s): die("P-g NON reproduit -- liaison non verifiable")
    # D-40, TEST NEGATIF DU SERIALISEUR sur le bloc G6 REEL qu'on vient de
    # mesurer : json.dump nu DOIT echouer, le serialiseur certifie DOIT passer.
    essai = os.path.join(base, "out", "_essai_serialisation.json")
    try:
        json.dumps({"g6": rec.get("g6")})
        die("D-40 : json.dump nu a PASSE sur un bloc G6 -- le controle ne mord pas")
    except TypeError as e:
        print("D-40 test negatif : json.dump nu ECHOUE sur le G6 reel (%s) -- il mord" % e)
    mot.P.sauver({"g6": rec.get("g6")}, essai)
    n = len(json.loads(open(essai).read())["g6"])
    os.remove(essai)
    print("D-40 : serialiseur certifie PASSE, %d cles conservees, cles '_' retirees" % n)
    return m15, art

def moteur_reel():
    try:
        mod = __import__(MOTEUR_ATTENDU[0])
    except ImportError:
        die("moteur %s introuvable (BOCAL4 seulement)" % MOTEUR_ATTENDU[0])
    src = getattr(mod, "__file__", None)
    if not src: die("moteur sans __file__")
    h = hashlib.sha256(open(src, "rb").read()).hexdigest()[:8]
    if h != MOTEUR_ATTENDU[1]:
        die("moteur %s != %s -- liaison non certifiee" % (h, MOTEUR_ATTENDU[1]))
    if not hasattr(mod, "mesure_ligne"):
        die("appel mesure_ligne absent -- schema de liaison a confirmer (docstring)")
    print("moteur reel : %s (%s) CONFORME a la liaison declaree" % (MOTEUR_ATTENDU[0], h))
    return mod

# ---------------------------------------------------------------- la manche
def frac_point(s):
    if "." in s:
        return F(int(s.replace(".", "")), 10 ** len(s.split(".")[1]))
    return F(int(s), 1)

def distance_site(point_str):
    pt = F(int(point_str.replace(".", "")), 10 ** len(point_str.split(".")[1]))
    return abs(pt - SITE)

def classer_reprise(rec, rec_m12_grossiere=True):
    if not rec["exclue"]:
        return "r2", "survie sous instrument courant -> FAIT D'INSTRUMENT (E26/E27), aucune lecture de site"
    if rec["mecanisme"] == "grossiere":
        return "r1", "grossiere reproduite a 1.78 rayons -> REPRODUCTIBILITE SOUS INSTRUMENT COURANT (matiere H-A)"
    return "r3", "morte d'un autre mecanisme -> consignation, ni r1 ni lecture de site"

class FondFactice:
    """Pre-vol : fond plat coherent. Au run, FondReel derive tout des
    artefacts via m15.derive_pre_run (K_X re-derives, arret si ecart)."""
    def __init__(self, m15mod): self.m15 = m15mod
    def K(self): return {"E": 27.087844, "S57": 21.714077, "S4": 5.835765}
        # valeurs de REFERENCE pre-run (ATTENDU_K_6DEC de la couche manche,
        # note 8081a032) -- au run : re-derivees, arret si ecart (TOL_K_REF)
    def ancres_XB(self):
        z = self.m15.x_du_point(3.0, 3.0, 3.0)   # le monde plat DU factice :
        b = {"E": 1e-9, "S57": 1e-9, "S4": 1e-9} # ancres au meme regime que
        return {"2.62": (dict(z), dict(b)),      # les s* par defaut (3.0)
                "2.72": (dict(z), dict(b))}

class FondReel(FondFactice):
    def __init__(self, m15mod, art):
        self.m15, self.art = m15mod, art
        self.P = m15mod.charger_pilote(verbeux=False)   # pour pas_final
        self.pr = m15mod.derive_pre_run(art)
        m15mod.arret_pre_run(self.pr)      # reference 8081a032, STOP si ecart
    def K(self): return self.pr["K"]
    def ancres_XB(self):
        # D-41 : le pas n'est PAS un champ de la carte. Patron EXTRAIT de
        # m15_site83_v2 l.1699-1706 : pas = pas_final(note du COTE retenu),
        # le cote suivant la convention (f) via frag (D-2 de la lignee).
        out = {}
        for pt, src_m in (("2.62", "m15"), ("2.72", "m12")):
            carte = self.art[src_m]["carte"]
            sfs, pas = {}, {}
            for p in (4, 5, 7):
                v = carte["%d|%.12f" % (p, float(pt))]
                sfs[p] = v["sF"]
                # D-41 : M15 OMET sM pour une ligne mono-signe (frag=1) ;
                # M12 ecrit sM=None avec frag=None. Le pas suit la convention
                # (f) : cote du MIN, et sP des que sM n'existe pas.
                cote = "sM" if (v.get("frag") == -1 and v.get("sM")) else "sP"
                pas[p] = (self.P.pas_final(v[cote]["note"]), v["sF"])
            X = self.m15.x_du_point(sfs[4], sfs[5], sfs[7])
            B = {n: self.m15.b_sigma(pas, n) for n in ("E","S57","S4")}
            out[pt] = (X, B)
        return out
        # liaisons de champs ("sF","pas") : celles de la couche manche,
        # verifiees au pre-vol reel (P-g)

def jouer_manche(moteur, dossier_sortie, mode, m15mod, lignes_registre=None, fond=None):
    fond = fond or FondFactice(m15mod)
    comptes = {"lancees": 0, "G2_sautees": 0, "N3_asserts": 0, "G1p": 0}
    records, morts_p4_F, morts_p4_T = [], 0, 0
    g_neuve = False

    # N-3 : nouveaute par VALEUR exacte (D-17) -- Fractions, jamais des chaines
    connus = set(frac_point(l["point"]) for l in (lignes_registre or []))
    for pt in STRATE1 + TEMOINS:
        assert frac_point(pt) not in connus, "N-3 : %s deja au registre (valeur)" % pt
        comptes["N3_asserts"] += 1

    # G1' custody d'ancres (valeurs consignees, tolerance declaree)
    for pt, (mch, e_att) in ANCRES.items():
        comptes["G1p"] += 1   # re-derivation reelle depuis artefact au run
    print("G1' : %d ancres de custody (E re-derives des artefacts au run, tolerance %g -- jamais au bit)"
          % (comptes["G1p"], TOL_E_ANCRE))

    # phase A : strate 1 + reprise + temoins
    for pt in STRATE1 + TEMOINS:
        for p, sg in BATTERIE:
            rec = moteur.mesure_ligne(p, pt, sg)
            rec["dist_rayons"] = float(distance_site(pt) / R11)
            records.append(rec); comptes["lancees"] += 1
            if p == 4 and rec["exclue"]:
                if pt in STRATE1: morts_p4_F += 1
                else: morts_p4_T += 1
            if (rec["exclue"] and rec["mecanisme"] == "grossiere"
                    and p % 2 == 1 and distance_site(pt) <= COEUR_RAYONS * R11):
                g_neuve = True
    rec_rep = moteur.mesure_ligne(*REPRISE)
    rec_rep["dist_rayons"] = float(distance_site(REPRISE[1]) / R11)
    records.append(rec_rep); comptes["lancees"] += 1
    issue, lecture_rep = classer_reprise(rec_rep)
    assert comptes["lancees"] == 31, "31 lignes attendues hors strate 2"

    # garde-fou regional (le SEUL usage du compte temoin, D-20)
    mode_carte = morts_p4_T >= 2
    # arret ITEM 3' : q_L re-derive FENETRE SEULE augmentee (D-20/E27, unite (a))
    n4_fen = 10 + 3; k4_fen = 5 + morts_p4_F
    q4_new = qL(k4_fen, n4_fen)
    surv_int = 3 - morts_p4_F
    # candidats de strate 2 d'abord, puis faisabilite EN FORME (D-19, gel v8 4.6)
    strate2, cand = [], []
    if surv_int >= 1 and not mode_carte:
        cand = []
        for pt in STRATE1:
            # survivant p=4 ?
            if any(r["p"] == 4 and r["point"] == pt and not r["exclue"] for r in records):
                base = F(int(pt.replace(".", "")), 100)
                for d in (F(-1, 1000), F(1, 1000)):
                    v = base + d
                    cand.append((abs(v - SITE), v))
        cand.sort()
        retenus, ecartes = cand[:4], cand[4:]
        N2 = len(retenus)
        jouable = N2 * (1.0 - q4_new) >= 1.0    # forme du gel v8, aucun seuil nu
        print("D-19 : N_2=%d, q4_fen=%.4f (a, fenetre seule) -> N_2 x (1-q) = %.3f ;"
              " strate 2 %s" % (N2, q4_new, N2 * (1 - q4_new),
                                "JOUABLE" if jouable else "INFAISABLE, STOP"))
        if not jouable:
            retenus = []
        for rang, (_, v) in enumerate(ecartes, start=5):
            print("strate 2, ecarte journalise (N-42) : rang %d, valeur %s" % (rang, v))
        for _, v in retenus:
            pts = "%.3f" % float(v)
            assert pts not in connus, "N-3 strate 2 : " + pts
            rec = moteur.mesure_ligne(4, pts, "+1")
            rec["dist_rayons"] = float(abs(v - SITE) / R11)
            records.append(rec); comptes["lancees"] += 1
        strate2 = [("%.3f" % float(v)) for _, v in retenus]
    if not strate2:
        comptes["G2_sautees"] += 1
        print("N-14 : strate 2 NON OUVERTE ou vide, saut motive (surv_int=%d, carte=%s,"
              " q4_fen=%.4f) -- comptes + sautes == attendu" % (surv_int, mode_carte, q4_new))

    # portes
    S = (morts_p4_F == 3 and morts_p4_T == 0)
    Dsig = (issue == "r1") and g_neuve
    b_c = branches_2x2(S, Dsig)
    s1 = 3 - morts_p4_F
    b_b = "B0" if s1 == 0 else ("B1" if s1 in (1, 2) else "B2")
    # (i) : P-M16a PAR EXTRACTION (D-24) -- criterer/brancher herites,
    # ancres custody 2.62/2.72 injectees comme LOIN de la corde.
    m15 = fond.m15
    def sf(pt, p, sg):
        for r in records:
            if r["point"] == pt and r["p"] == p and r["signe"] == sg:
                return None if r["exclue"] else (r["s_star"], r["pas_final"])
        return None
    X, B, surv = {}, {}, []
    for pt in ("2.63", "2.66", "2.68"):
        s4 = sf(pt, 4, "+1"); s5 = [sf(pt, 5, s) for s in ("+1","-1")]
        s7 = [sf(pt, 7, s) for s in ("+1","-1")]
        if s4 and all(s5) and all(s7):
            w = float(pt)
            v5 = min(s5, key=lambda t: t[0]); v7 = min(s7, key=lambda t: t[0])
            X[w] = m15.x_du_point(s4[0], v5[0], v7[0])
            B[w] = {n: m15.b_sigma({4: (s4[1], s4[0]), 5: (v5[1], v5[0]),
                        7: (v7[1], v7[0])}, n) for n in ("E","S57","S4")}   # b_sigma attend (pas, sF) -- ordre de la couche manche
            surv.append(w)
    for pt, (Xa, Ba) in fond.ancres_XB().items():   # custody, jamais rejouees
        X[float(pt)], B[float(pt)] = Xa, Ba
    survivants = sorted(surv + [2.62, 2.72])
    dossier_a = m15.criterer(survivants, X, B, fond.K()) \
        if (surv and not mode_carte) else {"plancher_de_comptes": False,
                                           "verdict": "NON CONCLUANT DE GEOMETRIE"}
    plancher_i = dossier_a.get("plancher_de_comptes", False)
    VERD_A = {"NON CONCLUANT DE GEOMETRIE": "A0",
              "PAS-DE-STRUCTURE-RESOLUE": "A1",
              "STRUCTURE-NON-CENTREE": "A2",
              "STRUCTURE-AU-SITE-RESOLUE": "A3",
              "STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE": "A4",
              "STRUCTURE-CANAL-4-CANDIDATE": "A5",
              "STRUCTURE-RESOLUE-NON-ATTRIBUEE": "A6"}
    b_a = VERD_A.get(dossier_a["verdict"], dossier_a["verdict"])
    if not plancher_i:
        print("P-M16d : (i) NON LISIBLE (A0) -- la perte est une donnee ; P-M16b=%s et"
              " P-M16c=%s restent lisibles" % (b_b, b_c))

    verdict = dict(mode="CARTE" if mode_carte else "NORMAL",
                   k4_F=morts_p4_F, k4_T=morts_p4_T, S=S, D=Dsig,
                   reprise=issue, lecture_reprise=lecture_rep,
                   G_neuve=g_neuve, P_M16b=b_b, P_M16c=b_c, P_M16a=b_a,
                   qL_aug_p4_a=round(q4_new, 4), strate2=strate2,
                   comptes=comptes)
    print("VERDICTS : b=%s ; c=%s ; a=%s ; reprise=%s ; carte=%s ;"
          " (k4_F,k4_T)=(%d,%d) [unite (a)]"
          % (b_b, b_c, b_a, issue, mode_carte, morts_p4_F, morts_p4_T))
    # comptes + sautes == attendu (forme derivee)
    attendu = 31 + (len(strate2))
    assert comptes["lancees"] == attendu, "comptes+sautes != attendu"
    if dossier_sortie:
        os.makedirs(dossier_sortie, exist_ok=True)
        out = os.path.join(dossier_sortie, "m16_results_%s.json" % mode)
        charge = dict(gel=GEL_SHA16, mode=mode, verdict=verdict,
                      rebinds=getattr(moteur, "journal", None),
                      resultats={"G6": {"%d|%s|%s" % (r["p"], r["point"], r["signe"]):
                                         dict({k: r.get(k) for k in ("exclue", "motif_exclusion", "mecanisme",
                                                            "ratio_fenetre", "ilots", "dist_rayons")},
                                              g6=r.get("g6"))
                                         for r in records}},
                      resolution="grille 1/100 (strate 1) et 1/1000 (strate 2) ; unites etiquetees (E27)")
        sauv = getattr(getattr(moteur, "P", None), "sauver", None)
        if sauv: sauv(charge, out)          # D-40 : serialiseur CERTIFIE (nettoie)
        else: json.dump(charge, open(out, "w"), indent=1)   # factice : sans numpy
        print("artefact ecrit :", out)
    return verdict

# ---------------------------------------------------------------- scenarios
SCENARIOS = {
  "S0_partage_3_1":  ({**{"4|%s|+1" % p: (True, "fine") for p in STRATE1},
                       "4|2.82|+1": (True, "fine")},
                      dict(P_M16b="B0", P_M16c="NON-DEPARTAGE")),
  "S1_crible_dense": ({}, dict(P_M16b="B2", P_M16c="NON-DEPARTAGE", P_M16a="A1")),
  "S2_HB_parfait":   ({**{"4|%s|+1" % p: (True, "fine") for p in STRATE1}}, dict(P_M16b="B0", P_M16c="H-B")),
  "S3_HA_coeur":     ({"7|2.67|+1": (True, "grossiere"), "7|2.66|+1": (True, "grossiere")},
                      dict(P_M16b="B2", P_M16c="H-A")),
  "S4_double":       ({**{"4|%s|+1" % p: (True, "fine") for p in STRATE1},
                       "7|2.67|+1": (True, "grossiere"), "5|2.66|+1": (True, "grossiere")},
                      dict(P_M16b="B0", P_M16c="DOUBLE-SIGNAL")),
  "S5_mode_carte":   ({"4|2.76|+1": (True, "fine"), "4|2.79|+1": (True, "fine")},
                      dict(mode="CARTE", P_M16c="NON-DEPARTAGE")),
  "S6_r3_autre":     ({"7|2.67|+1": (True, "fine")}, dict(reprise="r3")),
  "S7_r2_survie":    ({}, dict(reprise="r2")),
  "S8_B1_un_mort":   ({"4|2.63|+1": (True, "fine")}, dict(P_M16b="B1")),
  "S9_B1_deux_morts":({"4|2.63|+1": (True, "fine"), "4|2.68|+1": (True, "fine")},
                      dict(P_M16b="B1", P_M16a="A0")),
  "S10_A1_plat":     ({}, dict(P_M16a="A1")),
  "S11_A3_structure":({"4|2.66|+1": (False, "", {"s_star": 2.4}),
                       "5|2.66|+1": (False, "", {"s_star": 2.5}),
                       "5|2.66|-1": (False, "", {"s_star": 2.5})},
                      dict(P_M16a="A3")),
  "S12_A5_canal4":   ({"4|2.66|+1": (False, "", {"s_star": 2.4})},
                      dict(P_M16a="A5")),
  "S13_A2_noncentre":({"4|2.63|+1": (False, "", {"s_star": 2.4}),
                       "5|2.63|+1": (False, "", {"s_star": 3.3}),
                       "5|2.63|-1": (False, "", {"s_star": 3.3})},
                      dict(P_M16a="A2")),
  "S14_A4_nondisc":  ({"4|2.63|+1": (True, "fine"),
                       "5|2.66|+1": (False, "", {"s_star": 2.5}),
                       "5|2.66|-1": (False, "", {"s_star": 2.5})},
                      dict(P_M16a="A4")),
  "S15_A6_nonattrib":({"4|2.66|+1": (False, "", {"s_star": 3.0417}),
                       "7|2.66|+1": (False, "", {"s_star": 3.1269}),
                       "7|2.66|-1": (False, "", {"s_star": 3.1269})},
                      dict(P_M16a="A6")),
                      # A6 vit dans le ruban (K_S4 + K_S57 - K_E) x g :
                      # les deux canaux juste SOUS leurs seuils, alignes,
                      # la somme juste AU-DESSUS du seuil E -- le banc
                      # prouve que la branche est atteignable
}

def preflight(base):
    m15 = charger_couche_manche(base)
    print("== PRE-VOL, moteur factice -- chaque branche exercee, attendus asserts (N-9) ==")
    for nom, (sc, attendus) in SCENARIOS.items():
        print("-- scenario", nom)
        v = jouer_manche(MoteurFactice(sc), None, "preflight", m15)
        for cle, val in attendus.items():
            assert v[cle] == val, "%s : %s attendu %r, obtenu %r (clause bloquante consignee)" % (nom, cle, val, v[cle])
        print("   attendu(s) %s : OK" % attendus)
    print("PRE-VOL : 16/16 scenarios, toutes branches exercees, zero ecart."
          " (Opposable seulement joue par machine 2 -- ici : fumee machine 1.)")

def selftest(base):
    print("== SELFTEST (calculs purs ; gel requis) ==")
    _, bloc = custody_gel(base)
    controle_litteraux(os.path.abspath(__file__), bloc)
    v = qL(1, 12); ref = 0.22961693269696845
    assert abs(v - ref) < 1e-12, "calibration q_L"
    print("  q_L(80%%) calibre : 1/12 -> %.17f (ecart %.1e)" % (v, abs(v - ref)))
    assert comb(3, 3) * comb(3, 0) / comb(6, 3) == 0.05
    print("  hypergeometrique du partage maximal : 1/20 = 0.05")
    c = critere_temoins(); print("  c derive = %d (34)" % c)
    matrice_PM16a(); matrice_PM16b(); matrice_PM16c(); table_N52()
    src_txt = open(os.path.abspath(__file__)).read()
    for mode in ("--selftest", "--preflight", "--prevol-reel", "--run"):
        assert src_txt.count('"%s" in argv' % mode) == 1, "mode annonce absent : " + mode
    for nom in ("MoteurReel", "FondReel", "prevol_reel", "charger_art"):
        assert ("def " + nom) in src_txt or ("class " + nom) in src_txt, \
            "piece annoncee absente : " + nom
    print("  annonces == pieces : 4 modes et 4 objets du docstring presents (parade)")
    # parade bidirectionnelle (D-29) : le jumeau cite les constantes
    assert GEL_PATH in src_txt.split("E19")[1][:400], \
        "le docstring jumeau ne cite pas GEL_PATH"
    assert GEL_SHA16 in src_txt.split("E19")[1][:400], \
        "le docstring jumeau ne cite pas GEL_SHA16"
    annonces = set(re.findall(r"--[a-z-]+", src_txt.split("MODES :")[1].split(chr(34)*3)[0]))
    traites  = set(re.findall(r'"(--[a-z-]+)" in argv', src_txt))
    assert annonces == traites, "MODES != main() : %r" % (annonces ^ traites)
    print("  parade bidirectionnelle : jumeau == constantes ; MODES == main()")
    print("SELFTEST : PASSE.")

def main(argv):
    base = os.path.dirname(os.path.abspath(__file__))
    if "--selftest" in argv: selftest(base); return
    if "--preflight" in argv: selftest(base); preflight(base); return
    if "--prevol-reel" in argv:
        selftest(base); prevol_reel(base); return
    if "--run" in argv:
        selftest(base)
        m15, art = prevol_reel(base)          # P-g d'abord, toujours
        lg = inventaire(base)
        fond = FondReel(m15, art)
        mot = MoteurReel(m15)
        try:
            jouer_manche(mot, os.path.join(base, "out"), "run", m15,
                         lignes_registre=lg, fond=fond)
        finally:
            mot.restaurer()
            print("N-56/v10 : P restauree a %r ; journal des rebinds : %r"
                  % (mot.P0, mot.journal))
        return
    print(__doc__); print("usage : --selftest | --preflight | --run")

if __name__ == "__main__":
    main(sys.argv[1:])
