# -*- coding: ascii -*-
"""TIRAGE DES CELLULES DU GEL "SOMMET" -- machine 1, v1, 2026-11-22. Aucun calcul : une regle.
Derive de tirage_vide_machine1_v1.py (registre) : meme hachage ; les creneaux, les listes, les cellules, le nombre de w2
par creneau (DEUX) et le nombre de rangs (dix) sont ceux de ce gel.
Le w2 du creneau s au rang r est l'element de numero ( int( sha256("<graine>|<s>|<r>") en hexadecimal, 16 ) modulo n_s )
de la liste CROISSANTE des w2 candidats du creneau (numerotee de 0) ; la chaine est codee en ASCII ; r s'ecrit en decimal.
Par creneau, dans l'ordre MP, PP, MG, PG : on parcourt les rangs 0, 1, 2, ... ; le w2 tire est RETENU s'il est ELIGIBLE
dans la table commune et s'il n'est pas deja retenu ; sinon on passe au rang suivant, pour le creneau entier. On s'arrete
a DEUX w2 retenus : le premier est "a", le second "b". Au plus dix rangs (0 a 9) ; au-dela : PAS DE GEL.
TABLE COMMUNE = ET des tables donnees : un w2 y est ELIGIBLE s'il l'est dans toutes ET si les trois nombres ecrits (g,
eta0, r_c) de ses sept cellules sont les memes dans toutes.
Format d'une table : JSON, creneaux -> <nom> -> candidats -> liste de {"w2": "<fraction irreductible>", "eligible":
true|false, "cellules": liste de {"kappa": "<decimal a quatre decimales>", "g": "<decimal a six chiffres>", "eta0":
"<decimal a six chiffres>", "r_c": <entier>, "eligible": true|false}}.
La graine est une suite de chiffres (0 a 9, au moins six) donnee par l'operateur APRES la certification de la regle.
Usage : python3 -I tirage_sommet_machine1_v1.py <graine> <table d'eligibilite.json> [<autre table.json> ...]
        python3 -I tirage_sommet_machine1_v1.py --autotest          (aucune table lue ; graine de demonstration, non numerique)
        python3 -I tirage_sommet_machine1_v1.py --demonstration <table.json> [<autre table.json> ...]
                                                                  (les tables sont lues ; graine de demonstration : CE N'EST PAS UN TIRAGE)"""
import sys, json, hashlib
from fractions import Fraction as F
ORDRE = ("MP", "PP", "MG", "PG"); RANGS = 10; PAR_CRENEAU = 2
KAPPAS = ("0.0363", "0.0530", "0.0800", "0.1300", "0.2000", "0.4000", "1.0000")
PAS = F(1, 100000)
LISTES = {"MP": sorted(F(2) - k * PAS for k in range(5, 21) if k != 10), "PP": sorted(F(2) + k * PAS for k in range(5, 21) if k != 10),
          "MG": sorted(F(2) - k * PAS for k in range(25, 50)), "PG": sorted(F(2) + k * PAS for k in range(25, 50))}

def numero(graine, s, r, n):
    return int(hashlib.sha256(("%s|%s|%d" % (graine, s, r)).encode("ascii")).hexdigest(), 16) % n

def tirer(graine, eligible, cellules_de):
    """eligible : (creneau, w2) -> bool ; cellules_de : (creneau, w2) -> liste de (kappa, g ecrit, eta0 ecrit, r_c).
    Rend la liste des cellules, ou None (PAS DE GEL), et le journal."""
    cellules = []; journal = []
    for s in ORDRE:
        L = sorted(LISTES[s]); pris = []
        for r in range(RANGS):
            w = L[numero(graine, s, r, len(L))]
            etat = "INELIGIBLE, rang suivant" if not eligible(s, w) else ("DEJA RETENU, rang suivant" if w in pris else "ELIGIBLE, retenu")
            journal.append("creneau %-2s rang %d : numero %2d sur %d -> w2 = %s (%.5f) : %s" % (s, r, numero(graine, s, r, len(L)), len(L), w, float(w), etat))
            if etat == "ELIGIBLE, retenu":
                pris.append(w)
            if len(pris) == PAR_CRENEAU:
                break
        if len(pris) < PAR_CRENEAU:
            return None, journal
        for lettre, w in zip("ab", pris):
            for i, (kappa, g, eta0, r_c) in enumerate(cellules_de(s, w)):
                cellules.append({"id": "%s%s%d" % (s, lettre, i + 1), "creneau": s, "w2": str(w), "kappa": kappa, "g": g, "eta0": eta0, "r_c": r_c})
    return cellules, journal

if sys.argv[1] == "--autotest":
    assert all(L == sorted(L) and len(set(L)) == len(L) for L in LISTES.values()) and [len(LISTES[s]) for s in ORDRE] == [15, 15, 25, 25]
    assert all((w * 100000).denominator == 1 for L in LISTES.values() for w in L)                          # au cent-millieme
    interdits = (F(2), F(20001, 10000), F(19999, 10000), F(3999, 2000), F(4001, 2000))                     # trois w2 sacrifies, deux lus au jumeau
    assert all(w not in interdits for L in LISTES.values() for w in L)
    assert all(F(5, 100000) <= abs(w - 2) <= F(20, 100000) for s in ("MP", "PP") for w in LISTES[s])
    assert all(F(25, 100000) <= abs(w - 2) <= F(49, 100000) for s in ("MG", "PG") for w in LISTES[s])
    assert all(w < 2 for s in ("MP", "MG") for w in LISTES[s]) and all(w > 2 for s in ("PP", "PG") for w in LISTES[s])
    g = "DEMONSTRATION"; toutes = lambda s, w: [(k, "g", "eta0", 18) for k in KAPPAS]
    for s in ORDRE:
        for r in range(3):
            h = hashlib.sha256(("%s|%s|%d" % (g, s, r)).encode("ascii")).hexdigest()
            print("sha256(\"%s|%s|%d\") = %s... ; modulo %2d = %2d -> w2 = %.5f" % (g, s, r, h[:16], len(LISTES[s]), numero(g, s, r, len(LISTES[s])),
                  float(sorted(LISTES[s])[numero(g, s, r, len(LISTES[s]))])))
    c1, j1 = tirer(g, lambda s, w: True, toutes); c2, j2 = tirer(g, lambda s, w: True, toutes); assert c1 == c2 and len(c1) == 56
    assert all(len(set(c["w2"] for c in c1 if c["creneau"] == s)) == 2 for s in ORDRE)                    # deux w2 distincts par creneau
    assert [c["id"] for c in c1[:8]] == ["MPa1", "MPa2", "MPa3", "MPa4", "MPa5", "MPa6", "MPa7", "MPb1"]
    premier = {s: F(next(c["w2"] for c in c1 if c["creneau"] == s)) for s in ORDRE}
    c3, j3 = tirer(g, lambda s, w: not (s == "MP" and w == premier["MP"]), toutes)                         # le premier w2 de MP declare ineligible
    assert premier["MP"] not in [F(c["w2"]) for c in c3 if c["creneau"] == "MP"] and c3[14:] == c1[14:]
    c4, j4 = tirer(g, lambda s, w: s != "PG", toutes); assert c4 is None                                   # un creneau sans candidat eligible : PAS DE GEL
    seul = sorted(LISTES["MG"])[0]
    c5, j5 = tirer(g, lambda s, w: s != "MG" or w == seul, toutes); assert c5 is None                      # un seul w2 eligible : pas deux w2 distincts
    assert all("DEJA RETENU" not in l or "MG" in l for l in j5)
    print("ids :", " ".join(c["id"] for c in c1))
    print("AUTOTEST : TIENT (determinisme, cinquante-six cellules, deux w2 distincts par creneau, rang suivant, arret sans deux candidats, listes)")
    sys.exit(0)
DEMO = sys.argv[1] == "--demonstration"
GRAINE, TABLES = ("DEMONSTRATION" if DEMO else sys.argv[1]), sys.argv[2:]
if not DEMO and not (GRAINE.isdigit() and GRAINE.isascii() and len(GRAINE) >= 6):
    print("ARRET : la graine doit etre une suite d'au moins six chiffres"); sys.exit(1)
if not TABLES:
    print("ARRET : aucune table d'eligibilite"); sys.exit(1)
el = {}; cel = {}; desaccords = []
for t in TABLES:
    T = json.load(open(t)); vus = set()
    for s in ORDRE:
        for c in T["creneaux"][s]["candidats"]:
            k = (s, F(c["w2"])); vus.add(k)
            cs = {str(x["kappa"]): (str(x["g"]), str(x["eta0"]), int(x["r_c"]), bool(x["eligible"])) for x in c["cellules"]}
            assert sorted(cs) == sorted(KAPPAS), "la table %s ne porte pas les sept cellules de w2 = %s" % (t, c["w2"])
            assert (not c["eligible"]) or all(v[3] for v in cs.values()), "table %s incoherente : w2 = %s eligible sans ses sept cellules" % (t, c["w2"])
            if k not in cel:
                el[k] = bool(c["eligible"]); cel[k] = cs
            else:
                el[k] = el[k] and bool(c["eligible"])
                for kap in cs:
                    if cs[kap][:3] != cel[k][kap][:3]:
                        desaccords.append("%s w2 = %s kappa = %s : (g, eta0, r_c) %s et %s" % (s, k[1], kap, cel[k][kap][:3], cs[kap][:3])); el[k] = False
    assert all(sorted(w for (s2, w) in vus if s2 == s) == sorted(LISTES[s]) for s in ORDRE), "la table %s ne porte pas les listes de la regle" % t
print("tables : %d ; w2 eligibles dans toutes : %s" % (len(TABLES), ", ".join("%s %d sur %d" % (s, sum(v for (s2, w), v in el.items() if s2 == s), len(LISTES[s])) for s in ORDRE)))
for d in desaccords:
    print("DESACCORD sur un nombre ecrit (le w2 est ineligible) : %s" % d)
cellules, journal = tirer(GRAINE, lambda s, w: el[(s, w)], lambda s, w: [(kap,) + cel[(s, w)][kap][:3] for kap in KAPPAS])
print("graine : %s" % GRAINE)
for l in journal:
    print(l)
if cellules is None:
    print("PAS DE GEL : un creneau n'a pas deux w2 eligibles distincts en dix rangs"); sys.exit(2)
for c in cellules:
    print("  %-5s w2 = %-14s kappa = %s  g = %s  eta0 = %s  r_c = %d" % (c["id"], c["w2"], c["kappa"], c["g"], c["eta0"], c["r_c"]))
print("%s : %d cellules, %d w2" % ("DEMONSTRATION, CE N'EST PAS UN TIRAGE" if DEMO else "TIRAGE", len(cellules), len(set(c["w2"] for c in cellules))))
