# -*- coding: ascii -*-
"""TIRAGE DES DOUZE POINTS DU GEL "LOI DE LA LARGEUR, ORDRE 3" -- machine 1, v1, 2026-11-15. Aucun calcul : une regle.
Le w2 du creneau s au rang r est l'element de numero ( int( sha256("<graine>|<s>|<r>") en hexadecimal, 16 ) modulo n_s )
de la liste CROISSANTE des w2 candidats du creneau (numerotee de 0) ; la chaine est codee en ASCII ; r s'ecrit en decimal.
Rang 0 d'abord ; si le w2 tire n'est pas ELIGIBLE, rang suivant, pour le creneau entier ; au plus cinq rangs (0 a 4) ;
au-dela : PAS DE GEL. Un w2 est ELIGIBLE s'il l'est dans TOUTES les tables donnees (table commune = ET des tables).
Format d'une table : JSON, creneaux -> <nom> -> candidats -> liste de {"w2": "<fraction irreductible>", "eligible": true|false}.
La graine est une suite de chiffres (0 a 9, au moins six) donnee par l'operateur APRES la certification de la regle.
Usage : python3 -I tirage_machine1_v1.py <graine> <table d'eligibilite.json> [<autre table.json> ...]
        python3 -I tirage_machine1_v1.py --autotest          (aucune table lue ; graine de demonstration, non numerique)"""
import sys, json, hashlib
from fractions import Fraction as F
ORDRE = ("N", "P", "BN", "BP"); RANGS = 5
CINQ = ["3/4", "5/6", "1", "6/5", "4/3"]; FACTEURS = {"N": CINQ, "P": CINQ, "BN": ["1"], "BP": ["1"]}
LISTES = {"N": [F(k, 1000) for k in range(1931, 1940)], "P": [F(k, 1000) for k in list(range(2031, 2040)) + list(range(2041, 2050))],
          "BN": [F(k, 1000) for k in list(range(1916, 1920)) + list(range(1921, 1925))], "BP": [F(k, 1000) for k in range(2061, 2070)]}

def numero(graine, s, r, n):
    return int(hashlib.sha256(("%s|%s|%d" % (graine, s, r)).encode("ascii")).hexdigest(), 16) % n

def tirer(graine, eligible):
    """eligible : fonction (creneau, w2 Fraction) -> bool. Rend la liste des douze cellules, ou None (PAS DE GEL)."""
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
        for i, f in enumerate(FACTEURS[s]):
            cellules.append({"id": s + (str(i + 1) if len(FACTEURS[s]) > 1 else ""), "creneau": s, "w2": str(pris), "facteur": f})
    return cellules, journal

if sys.argv[1] == "--autotest":
    assert all(L == sorted(L) and len(set(L)) == len(L) for L in LISTES.values()) and [len(LISTES[s]) for s in ORDRE] == [9, 18, 8, 9]
    assert all((w * 1000).denominator == 1 and (w * 100).denominator != 1 for L in LISTES.values() for w in L)   # au millieme, aucun centieme
    g = "DEMONSTRATION"
    for s in ORDRE:
        for r in range(2):
            h = hashlib.sha256(("%s|%s|%d" % (g, s, r)).encode("ascii")).hexdigest()
            print("sha256(\"%s|%s|%d\") = %s... ; modulo %2d = %2d -> w2 = %.3f" % (g, s, r, h[:16], len(LISTES[s]), numero(g, s, r, len(LISTES[s])), float(sorted(LISTES[s])[numero(g, s, r, len(LISTES[s]))])))
    c1, j1 = tirer(g, lambda s, w: True); c2, j2 = tirer(g, lambda s, w: True); assert c1 == c2 and len(c1) == 12
    assert c1[0]["w2"] == str(F(1935, 1000)) and c1[5]["w2"] == str(F(2048, 1000)) and c1[10]["w2"] == str(F(1918, 1000)) and c1[11]["w2"] == str(F(2069, 1000))
    c3, j3 = tirer(g, lambda s, w: not (s == "N" and w == F(1935, 1000)))                    # le rang 0 de N declare ineligible : rang 1
    assert c3[0]["w2"] == str(F(1931, 1000)) and c3[5:] == c1[5:]
    c4, j4 = tirer(g, lambda s, w: s != "BP"); assert c4 is None                              # un creneau sans candidat eligible : PAS DE GEL
    print("ids :", " ".join(c["id"] for c in c1))
    print("AUTOTEST : TIENT (determinisme, douze cellules, rang suivant, arret sans candidat)")
    sys.exit(0)
GRAINE, TABLES = sys.argv[1], sys.argv[2:]
if not (GRAINE.isdigit() and GRAINE.isascii() and len(GRAINE) >= 6):
    print("ARRET : la graine doit etre une suite d'au moins six chiffres"); sys.exit(1)
el = {}
for t in TABLES:
    T = json.load(open(t)); e1 = {(s, F(c["w2"])): bool(c["eligible"]) for s in ORDRE for c in T["creneaux"][s]["candidats"]}
    assert all(sorted(w for (s2, w) in e1 if s2 == s) == sorted(LISTES[s]) for s in ORDRE), "la table %s ne porte pas les listes de la regle" % t
    for k, v in e1.items():
        el[k] = el.get(k, True) and v
print("tables : %d ; w2 eligibles dans toutes : %s" % (len(TABLES), ", ".join("%s %d sur %d" % (s, sum(v for (s2, w), v in el.items() if s2 == s), len(LISTES[s])) for s in ORDRE)))
cellules, journal = tirer(GRAINE, lambda s, w: el[(s, w)])
print("graine : %s" % GRAINE)
for l in journal:
    print(l)
if cellules is None:
    print("PAS DE GEL : un creneau n'a pas de w2 eligible en cinq rangs"); sys.exit(2)
for c in cellules:
    print("  %-3s w2 = %-10s facteur %s" % (c["id"], c["w2"], c["facteur"]))
print("TIRAGE : douze cellules")
