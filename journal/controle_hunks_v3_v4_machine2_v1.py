#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LE DIFF v3 -> v4, REJOUE DE MA MAIN -- machine 2, v1, 12/09/2026.

Compte par POSITION (l'en-tete du diff est ses DEUX premieres lignes), jamais par
prefixe : c'est la faute que machine 1 vient de localiser a la racine, et que MA feuille
d'hier portait aussi -- '-- FIN ... --' devient '--- FIN ... --' une fois prefixee, et un
filtre qui ecarte '---' l'avale. Les opcodes bruts restent la reference ; les trois
comptes sont imprimes cote a cote pour que l'ecart RESTE VISIBLE s'il revient.

Regle 9 : une piece de diff ne vaut que si elle SE REJOUE. Machine 1 n'en envoie pas ;
elle annonce des nombres. Ceux-ci sont refaits ici, et les hunks imprimes en entier pour
que la verification porte sur du texte lu, non sur un resume.
"""
import difflib, os

RAC = r"D:\devs\bocal\BOCAL4"
V3 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3", "lot",
                  "journal_delta_nn_R4R5_v3.md")
V4 = os.path.join(RAC, "entrant_machine1_2026-09-12_acte_v4", "lot",
                  "journal_delta_nn_R4R5_v4.md")
a, b = open(V3, encoding="utf-8").read(), open(V4, encoding="utf-8").read()
A, B = a.splitlines(), b.splitlines()
print("=" * 84)
print("DIFF v3 -> v4, CONTEXTE 0, REJOUE PAR machine 2")
print("=" * 84)
print("v3 : %d lignes, %d octets" % (len(A), len(a.encode())))
print("v4 : %d lignes, %d octets" % (len(B), len(b.encode())))

sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
h = [o for o in sm.get_opcodes() if o[0] != 'equal']
plus = sum(j2 - j1 for t, i1, i2, j1, j2 in h)
moins = sum(i2 - i1 for t, i1, i2, j1, j2 in h)
u = list(difflib.unified_diff(A, B, n=0, lineterm=''))
corps = u[2:]
u_plus = sum(1 for l in corps if l.startswith('+'))
u_moins = sum(1 for l in corps if l.startswith('-'))
u_moins_prefixe = sum(1 for l in u if l.startswith('-') and not l.startswith('---'))
print("\nOPCODES BRUTS        : %d hunks, +%d / -%d" % (len(h), plus, moins))
print("UNIFIED, PAR POSITION: +%d / -%d" % (u_plus, u_moins))
print("UNIFIED, PAR PREFIXE : -%d   <-- la faute, si l'ecart n'est pas nul"
      % u_moins_prefixe)
print("annonce machine 1    : 6 hunks, +17 / -7")
for lib, cond in (("6 hunks", len(h) == 6), ("+17", plus == 17), ("-7", moins == 7),
                  ("position == opcodes", (u_plus, u_moins) == (plus, moins))):
    print("  [%s] %s" % ("OK  " if cond else "MORD", lib))

for n, (t, i1, i2, j1, j2) in enumerate(h, 1):
    print("\n" + "-" * 84)
    print("HUNK %d/%d  %s  v3[%d:%d] -> v4[%d:%d]  (-%d / +%d)"
          % (n, len(h), t, i1 + 1, i2, j1 + 1, j2, i2 - i1, j2 - j1))
    print("-" * 84)
    for l in A[i1:i2]:
        print("  - " + l)
    for l in B[j1:j2]:
        print("  + " + l)
