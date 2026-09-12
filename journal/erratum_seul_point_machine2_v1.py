#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ERRATUM DE MACHINE 2 : "LE SEUL POINT NON BIT-REPRODUCTIBLE" EST FAUX.
machine 2, v1, 12/09/2026.

Machine 1 demande (sa section 2) : R_ELLE porte-t-il, a 4|1.73 et 4|2.80, la classe
NOYAU ou la classe libm ? Et la phrase "le SEUL point non bit-reproductible" porte-t-elle
sur les quatre points NON LUS ou sur les neuf ?

Les deux se mesurent sur des fichiers que je detiens : son log de pre-vol v8 (la source
de R_ELLE) et le mien (la source de R_MOI). Les chemins sont des ARGUMENTS.

CE QUE CETTE FEUILLE ETABLIT CONTRE MOI : la phrase est FAUSSE, et pire que fausse --
elle vivait dans le CHAMP DE DETAIL d'un chk dont la condition testait tout autre chose
(que le porteur differe de plus de 5 pour cent). Une affirmation d'UNICITE n'a jamais ete
testee. Ecrite dans la condition, elle aurait MORDU des le premier passage.
"""
import re, sys

if len(sys.argv) < 3:
    sys.exit("usage : erratum_seul_point_machine2_v1.py <log prevol m1> <log prevol m2>")
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-56s %s" % ("OK  " if c else "MORD", q[:56], d))


def ratios(log):
    L = [l for l in open(log, encoding="utf-8") if "T2-" in l and "e/seuil" in l]
    return {re.search(r"T2-(\S+)", l).group(1):
            float(re.search(r"e/seuil=([0-9.]+)", l).group(1)) for l in L}


ELLE, MOI = ratios(sys.argv[1]), ratios(sys.argv[2])
ordre = sorted(ELLE, key=lambda c: (int(c.split("|")[0]), float(c.split("|")[1])))

print("=" * 92)
print("ERRATUM : LES NEUF CELLULES, ET NON UNE SEULE")
print("=" * 92)
print("\n[1] R_ELLE CONTRE R_MOI, LES NEUF")
print("      %-9s %10s %10s %9s   %s" % ("cellule", "R_ELLE", "R_MOI", "ecart %", "lue ?"))
diff, diff_lues = [], []
for k in ordre:
    e, m = ELLE[k], MOI[k]
    d = 100 * (e / m - 1)
    lue = not (e < 1 and m < 1)
    if e != m:
        diff.append(k)
        if lue:
            diff_lues.append(k)
    print("      %-9s %10.6f %10.6f %9.2f   %s"
          % (k, e, m, d, "LUE" if lue else "NON LUE (sous 1)"))
print("\n      cellules qui DIFFERENT : %d / %d  -> %s" % (len(diff), len(ordre), diff))
print("      dont LUES              : %d        -> %s" % (len(diff_lues), diff_lues))

print("\n[2] L'AFFIRMATION QUE MA FEUILLE PORTAIT")
print('      "c est le SEUL point non bit-reproductible de la campagne"')
chk("cette affirmation est VRAIE (elle exigerait 1 seule cellule differente)",
    len(diff) == 1,
    "FAUSSE : %d cellules different, dont %d LUES" % (len(diff), len(diff_lues)))
chk("elle serait vraie si on la restreignait aux cellules NON LUES",
    len([k for k in diff if ELLE[k] < 1 and MOI[k] < 1]) == 1,
    "parmi les quatre NON LUES, 7|1.73 est bien la seule qui differe")
print("      => LA PORTEE EXACTE : 7|1.73 est le seul point NON LU qui differe, et le")
print("         seul qui PORTE la borne. Il n'est pas le seul qui differe.")

print("\n[3] SA QUESTION : R_ELLE EST-IL CLASSE NOYAU OU CLASSE libm ?")
for k, noyau, libm in (("4|1.73", 1.613836, 1.651718), ("4|2.80", 2.379096, 2.272990),
                       ("7|1.73", 0.759266, 0.684192)):
    e, m = ELLE.get(k), MOI.get(k)
    cl_e = "NOYAU" if abs(e - noyau) < abs(e - libm) else "libm"
    cl_m = "NOYAU" if abs(m - noyau) < abs(m - libm) else "libm"
    print("      %-7s  R_ELLE = %.6f -> classe %-5s   R_MOI = %.6f -> classe %s"
          % (k, e, cl_e, m, cl_m))
    chk("%s : R_ELLE est classe NOYAU" % k, cl_e == "NOYAU")
    chk("%s : R_MOI est classe libm" % k, cl_m == "libm")
print("      => REPONSE : R_ELLE porte les valeurs du NOYAU aux trois cellules ou les")
print("         deux machines different. Son log du 28/08 est un log a noyau.")

print("\n[4] CE QUE CELA CHANGE, ET CE QUE CELA NE CHANGE PAS")
print("      NE CHANGE PAS : la borne retenue (INF = max(borne(R_MOI, True))) ne lit")
print("        aucun de ces nombres ; les trois cellules qui different ne la portent")
print("        pas non plus (elle est portee par le plus PETIT ratio, 7|1.73 = 0.684).")
print("      CHANGE : la PORTEE de ma phrase, et la lecture de la campagne qui s'y")
print("        appuyait. Deux cellules LUES -- 4|1.73 et 4|2.80 -- differaient entre les")
print("        machines sans que personne ne le remarque, parce que PERSONNE NE LES")
print("        COMPARAIT AU BIT : elles passaient leur lecture des deux cotes.")
print("      LA FAUTE DE FORME, qui est la vraie : l'affirmation vivait dans le CHAMP")
print("        DE DETAIL d'un chk dont la condition testait l'ECART DU PORTEUR. Un")
print("        champ de detail n'est pas teste. Ecrite en condition --")
print("        sum(1 for k in R_MOI if R_MOI[k] != R_ELLE[k]) == 1 -- elle MORDAIT.")

print("\n" + "=" * 92)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s" % q)
    print("         %s" % d)
print("(le premier mordant est l'erratum lui-meme : il DOIT mordre)")
print("=" * 92)
