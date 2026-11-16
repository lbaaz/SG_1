# -*- coding: ascii -*-
"""Construit la sonde ter : le gabarit, ou le bloc du lecteur est insere TEL QUEL a la marque. Usage : <gabarit> <bloc> <sortie.py>"""
import sys
g = open(sys.argv[1]).read(); b = open(sys.argv[2]).read()
assert g.count("@@BLOC@@") == 1
s = g.replace("@@BLOC@@", b.rstrip("\n"))
s.encode("ascii")
open(sys.argv[3], "w", newline="\n").write(s)
print("ecrit", sys.argv[3], len(s.splitlines()), "lignes ; bloc present tel quel :", b.rstrip("\n") in s)
