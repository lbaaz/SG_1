#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LE DIFF v2 -> v3 DE L'ACTE R4/R5, REJOUE DE MA MAIN -- machine 2, v1, 11/09/2026.

Regle 9 du 11/09 : une piece de diff ne vaut que si elle SE REJOUE. Machine 1 ne m'a
PAS envoye de fichier de diff cette fois -- elle annonce des NOMBRES dans sa note et
son manifeste : 10 hunks a contexte 0, +55 / -10 lignes, 5 de fond, 5 administratifs.
Cette feuille refait le diff et confronte ces nombres, puis IMPRIME les hunks pour que
la certification porte sur du texte lu, pas sur un resume.

D-CERT-4 (defaut paye au diff v1->v2) : splitlines() ne compte pas le saut de ligne
final ; je compte donc aussi les octets et la derniere ligne separement.
"""
import difflib, os

RAC = r"D:\devs\bocal\BOCAL4"
V2 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5_v2", "lot",
                  "journal_delta_nn_R4R5_v2.md")
V3 = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_v3", "lot",
                  "journal_delta_nn_R4R5_v3.md")

a = open(V2, encoding="utf-8").read()
b = open(V3, encoding="utf-8").read()
A, B = a.splitlines(), b.splitlines()

print("=" * 84)
print("DIFF v2 -> v3, CONTEXTE 0, REJOUE PAR machine 2")
print("=" * 84)
print("v2 : %d lignes, %d octets, fin de fichier %s"
      % (len(A), len(a.encode()), "LF" if a.endswith("\n") else "SANS LF"))
print("v3 : %d lignes, %d octets, fin de fichier %s"
      % (len(B), len(b.encode()), "LF" if b.endswith("\n") else "SANS LF"))

sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
hunks = [op for op in sm.get_opcodes() if op[0] != 'equal']
plus = sum(j2 - j1 for tag, i1, i2, j1, j2 in hunks)
moins = sum(i2 - i1 for tag, i1, i2, j1, j2 in hunks)
print("\nHUNKS : %d      +%d / -%d lignes" % (len(hunks), plus, moins))
print("annonce machine 1 : 10 hunks, +55 / -10")
print("  [%s] compte de hunks" % ("OK  " if len(hunks) == 10 else "MORD"))
print("  [%s] +55" % ("OK  " if plus == 55 else "MORD"))
print("  [%s] -10" % ("OK  " if moins == 10 else "MORD"))

for n, (tag, i1, i2, j1, j2) in enumerate(hunks, 1):
    print("\n" + "-" * 84)
    print("HUNK %d/%d  %s  v2[%d:%d] -> v3[%d:%d]   (-%d / +%d)"
          % (n, len(hunks), tag, i1 + 1, i2, j1 + 1, j2, i2 - i1, j2 - j1))
    print("-" * 84)
    for l in A[i1:i2]:
        print("  - " + l)
    for l in B[j1:j2]:
        print("  + " + l)
