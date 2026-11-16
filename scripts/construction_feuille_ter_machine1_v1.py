# -*- coding: ascii -*-
"""Construit la feuille ter : le gabarit, ou sont poses le canon de la sonde et celui de la reference des ancres.
Usage : <gabarit> <sonde.py> <reference_ancres.json> <sortie.py>"""
import sys, hashlib, unicodedata
def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
g = open(sys.argv[1]).read()
assert g.count("@@CANON_SONDE@@") == 1 and g.count("@@CANON_REFERENCE_ANCRES@@") == 1
s = g.replace("@@CANON_SONDE@@", canon(sys.argv[2])).replace("@@CANON_REFERENCE_ANCRES@@", canon(sys.argv[3]))
s.encode("ascii")
open(sys.argv[4], "w", newline="\n").write(s)
print("ecrit", sys.argv[4], "; sonde", canon(sys.argv[2]), "; reference des ancres", canon(sys.argv[3]), "; feuille", canon(sys.argv[4]))
