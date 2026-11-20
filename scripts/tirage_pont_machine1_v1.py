# -*- coding: ascii -*-
"""TIRAGE DES CELLULES DU GEL "PONT" -- machine 1, v1, 2026-11-17. Aucun calcul : une regle.
Derive de tirage_vide_machine1_v1.py (registre, cc1b2df637a9f3cd) : memes hachage, rangs et arrets ; creneaux, listes et
cellules sont ceux de ce gel (deux creneaux, huit w2 chacun, trois profondeurs, aucune cellule "profonde").
Le w2 du creneau s au rang r est l'element de numero ( int( sha256("<graine>|<s>|<r>") en hexadecimal, 16 ) modulo n_s )
de la liste CROISSANTE des w2 candidats du creneau (numerotee de 0) ; la chaine est codee en ASCII ; r s'ecrit en decimal.
Rang 0 d'abord ; si le w2 tire n'est pas ELIGIBLE, rang suivant, pour le creneau entier ; au plus cinq rangs (0 a 4) ;
au-dela : PAS DE GEL. TABLE COMMUNE = ET des tables donnees : un w2 y est ELIGIBLE s'il l'est dans toutes ET si les
couplages ecrits de ses trois cellules sont les memes dans toutes.
Format d'une table : JSON, creneaux -> <nom> -> candidats -> liste de {"w2": "<fraction irreductible>", "eligible":
true|false, "cellules": liste de {"m": <entier>, "g": "<decimal a six chiffres>", "eligible": true|false}}.
La graine est une suite de chiffres (0 a 9, au moins six) donnee par l'operateur APRES la certification de la regle.
Usage : python3 -I tirage_pont_machine1_v1.py <graine> <table d'eligibilite.json> [<autre table.json> ...]
        python3 -I tirage_pont_machine1_v1.py --autotest          (aucune table lue ; graine de demonstration, non numerique)
        python3 -I tirage_pont_machine1_v1.py --demonstration <table.json> [<autre table.json> ...]
                                                                  (les tables sont lues ; graine de demonstration : CE N'EST PAS UN TIRAGE)"""
import sys, json, hashlib
from fractions import Fraction as F
ORDRE = ("MG", "PG"); RANGS = 5
PROFONDEURS = (3, 4, 5)
EXCLUS = (F(1982, 1000), F(2017, 1000))
LISTES = {"MG": [F(k, 1000) for k in range(1981, 1990) if F(k, 1000) not in EXCLUS],
          "PG": [F(k, 1000) for k in range(2011, 2020) if F(k, 1000) not in EXCLUS]}

def numero(graine, s, r, n):
    return int(hashlib.sha256(("%s|%s|%d" % (graine, s, r)).encode("ascii")).hexdigest(), 16) % n

def tirer(graine, eligible, cellules_de):
    """eligible : (creneau, w2) -> bool ; cellules_de : (creneau, w2) -> liste de (m, g ecrit).
    Rend la liste des cellules, ou None (PAS DE GEL), et le journal."""
    cellules = []; journal = []
    for s in ORDRE:
        L = sorted(LISTES[s]); pris = None
        for r in range(RANGS):
            w = L[numero(graine, s, r, len(L))]; ok = eligible(s, w)
            journal.append("creneau %-2s rang %d : numero %d sur %d -> w2 = %s (%.3f) : %s" % (s, r, numero(graine, s, r, len(L)), len(L), w, float(w), "ELIGIBLE, retenu" if ok else "INELIGIBLE, rang suivant"))
            if ok:
                pris = w; break
        if pris is None:
            return None, journal
        for (m, g) in cellules_de(s, pris):
            cellules.append({"id": "%s%d" % (s, m), "creneau": s, "w2": str(pris), "m": m, "g": g})
    return cellules, journal

if sys.argv[1] == "--autotest":
    assert all(L == sorted(L) and len(set(L)) == len(L) for L in LISTES.values()) and [len(LISTES[s]) for s in ORDRE] == [8, 8]
    assert all((w * 1000).denominator == 1 and (w * 100).denominator != 1 for L in LISTES.values() for w in L)   # au millieme, aucun centieme
    assert all(F(1, 100) < abs(w - 2) < F(2, 100) for L in LISTES.values() for w in L) and not any(w in EXCLUS for L in LISTES.values() for w in L)
    g = "DEMONSTRATION"; toutes = lambda s, w: [(m, "g") for m in PROFONDEURS]
    assert hashlib.sha256(b"DEMONSTRATION|MG|0").hexdigest()[:16] == "8254e7d473dd8e66"      # la valeur ecrite dans les deux gels deposes
    for s in ORDRE:
        for r in range(2):
            h = hashlib.sha256(("%s|%s|%d" % (g, s, r)).encode("ascii")).hexdigest()
            print("sha256(\"%s|%s|%d\") = %s... ; modulo %2d = %2d -> w2 = %.3f" % (g, s, r, h[:16], len(LISTES[s]), numero(g, s, r, len(LISTES[s])), float(sorted(LISTES[s])[numero(g, s, r, len(LISTES[s]))])))
    c1, j1 = tirer(g, lambda s, w: True, toutes); c2, j2 = tirer(g, lambda s, w: True, toutes); assert c1 == c2 and len(c1) == 6
    w_mg0 = sorted(LISTES["MG"])[numero(g, "MG", 0, 8)]; w_mg1 = sorted(LISTES["MG"])[numero(g, "MG", 1, 8)]
    assert c1[0]["w2"] == str(w_mg0) and [c["id"] for c in c1] == ["MG3", "MG4", "MG5", "PG3", "PG4", "PG5"]
    c3, j3 = tirer(g, lambda s, w: not (s == "MG" and w == w_mg0), toutes)                    # le rang 0 de MG declare ineligible : rang suivant
    assert c3 is not None and c3[0]["w2"] != str(w_mg0) and c3[3:] == c1[3:] and any("INELIGIBLE" in l for l in j3)
    c4, j4 = tirer(g, lambda s, w: s != "PG", toutes); assert c4 is None and len(j4) == 1 + RANGS  # un creneau sans candidat eligible : PAS DE GEL
    print("ids :", " ".join(c["id"] for c in c1))
    print("AUTOTEST : TIENT (listes, determinisme, six cellules, rang suivant, arret sans candidat)")
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
            cs = {int(x["m"]): (str(x["g"]), bool(x["eligible"])) for x in c["cellules"]}
            assert sorted(cs) == sorted(PROFONDEURS), "la table %s ne porte pas les trois cellules de w2 = %s" % (t, c["w2"])
            assert bool(c["eligible"]) == all(v[1] for v in cs.values()), "table incoherente a w2 = %s" % c["w2"]
            if k not in cel:
                el[k] = bool(c["eligible"]); cel[k] = cs
            else:
                el[k] = el[k] and bool(c["eligible"])
                for m in cs:
                    if cs[m][0] != cel[k][m][0]:
                        desaccords.append("%s w2 = %s m = %d : couplages %s et %s" % (s, k[1], m, cel[k][m][0], cs[m][0])); el[k] = False
                    cel[k][m] = (cel[k][m][0], cel[k][m][1] and cs[m][1])
    assert all(sorted(w for (s2, w) in vus if s2 == s) == sorted(LISTES[s]) for s in ORDRE), "la table %s ne porte pas les listes de la regle" % t
print("tables : %d ; w2 eligibles dans toutes : %s" % (len(TABLES), ", ".join("%s %d sur %d" % (s, sum(v for (s2, w), v in el.items() if s2 == s), len(LISTES[s])) for s in ORDRE)))
for d in desaccords:
    print("DESACCORD de couplage (le w2 est ineligible) : %s" % d)
cellules, journal = tirer(GRAINE, lambda s, w: el[(s, w)], lambda s, w: [(m, cel[(s, w)][m][0]) for m in PROFONDEURS])
print("graine : %s" % GRAINE)
for l in journal:
    print(l)
if cellules is None:
    print("PAS DE GEL : un creneau n'a pas de w2 eligible en cinq rangs"); sys.exit(2)
for c in cellules:
    print("  %-4s w2 = %-10s m = %d g = %s" % (c["id"], c["w2"], c["m"], c["g"]))
print("%s : %d cellules" % ("DEMONSTRATION, CE N'EST PAS UN TIRAGE" if DEMO else "TIRAGE", len(cellules)))
