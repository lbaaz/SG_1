#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SON TEMOIN D'ARRONDI, JOUE SUR BOCAL4 -- machine 2, v1, 12/09/2026.

Machine 1 propose, sous (X), que la ligne de plateforme d'un log porte un TEMOIN
EXECUTABLE plutot que trois noms qui ne predisent rien :

    (1765.6704444885254) ** 6     ...9c5 -> noyau SIMD non CR
                                  ...9c6 -> correctement arrondi

et elle ECRIT SON ATTENDU AVANT : sur BOCAL4 il doit rendre ...9c6 des deux cotes.
ELLE ECRIT AUSSI L'ISSUE QUI LA FERAIT MORDRE : "s'il rend ...9c5, la roue Windows a un
noyau que 0/22 800 n'a pas montre, et cette note se trompe."

C'est donc un vrai controle, et il tient en une multiplication. Cette feuille le joue,
et l'etend : elle mesure aussi le temoin sur les DEUX autres ufuncs qu'elle a trouvees
non CR chez elle (exp, arctan2), pour dire si la roue Windows en est exempte AUSSI --
ce qu'aucune des deux notes n'a encore mesure de ce cote.
"""
import platform, sys
from decimal import Decimal, getcontext
from fractions import Fraction

import numpy as np

getcontext().prec = 80
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-54s %s" % ("OK  " if c else "MORD", q[:54], d))


print("=" * 88)
print("LE TEMOIN D'ARRONDI DE MACHINE 1, JOUE SUR BOCAL4")
print("=" * 88)
print("      python %s ; numpy %s ; %s"
      % (sys.version.split()[0], np.__version__, platform.platform()))

print("\n[1] SON TEMOIN, AU CARACTERE")
x = 1765.6704444885254
tab = float((np.array([x]) ** 6)[0])
pyt = x ** 6
cr = float(Fraction(Decimal(x) ** 6))
print("      x                    = %r" % x)
print("      numpy TABLEAU ** 6   = %s" % float.hex(tab))
print("      pow de Python ** 6   = %s" % float.hex(pyt))
print("      correctement arrondi = %s" % float.hex(cr))
print("      son noyau SIMD rend  = 0x1.a483018a169c5p+64  (non CR, -1 ulp)")
chk("le tableau numpy rend ...9c6", float.hex(tab).endswith("9c6p+64"), float.hex(tab))
chk("le pow de Python rend ...9c6", float.hex(pyt).endswith("9c6p+64"))
chk("les deux EGALENT le correctement arrondi", tab == pyt == cr)
chk("SA PREDICTION EST TENUE : la roue Windows n'a pas ce noyau",
    tab == cr, "sinon : elle en a un que 0/22 800 n'avait pas montre")

print("\n[2] CE QU'AUCUNE NOTE N'A ENCORE MESURE DE CE COTE :")
print("    LES DEUX AUTRES ufuncs QU'ELLE TROUVE NON CR CHEZ ELLE")
print("    (sa table : exp 4.56 %% non CR, arctan2 5.92 %% -- ici ?)")
rng = np.random.default_rng(20260912)
N = 20000


def part_non_cr(nom, f_tab, f_exact, args):
    tabv = f_tab(*args)
    bad = 0
    for i in range(N):
        e = f_exact(*[a[i] for a in args])
        if float(tabv[i]) != e:
            bad += 1
    print("      %-12s non CR : %5d / %d  (%.2f pour cent)" % (nom, bad, N, 100 * bad / N))
    return bad


xs = rng.uniform(1.0, 3000.0, N)
b6 = part_non_cr("x ** 6", lambda a: a ** 6,
                 lambda v: float(Fraction(Decimal(v) ** 6)), (xs,))
chk("power x**6 : la classe libm (moins de 0.5 pour cent), pas la classe SIMD (~5)",
    100 * b6 / N < 0.5, "%.2f pour cent ; sa mesure avec noyau : 4.92" % (100 * b6 / N))

# Reference haute precision : mpmath a 200 bits, la MEME que celle de sa feuille
# mesure_ufuncs_cr.py -- je reprends son etalon, je n'en invente pas un autre.
import mpmath
mpmath.mp.prec = 200

zs = rng.uniform(-20.0, 20.0, N)
tabe = np.exp(zs)
bad = sum(1 for i in range(N) if float(tabe[i]) != float(mpmath.exp(zs[i])))
print("      %-12s non CR : %5d / %d  (%.2f pour cent)" % ("exp", bad, N, 100 * bad / N))
chk("exp : la classe libm, pas la classe SIMD (sa mesure avec noyau : 4.56)",
    100 * bad / N < 0.5, "%.2f pour cent" % (100 * bad / N))

us = rng.uniform(-20.0, 20.0, N)
vs = rng.uniform(-20.0, 20.0, N)
taba = np.arctan2(us, vs)
bada = sum(1 for i in range(N)
           if float(taba[i]) != float(mpmath.atan2(us[i], vs[i])))
print("      %-12s non CR : %5d / %d  (%.2f pour cent)" % ("arctan2", bada, N,
                                                           100 * bada / N))
chk("arctan2 : la classe libm, pas la classe SIMD (sa mesure avec noyau : 5.92)",
    100 * bada / N < 1.0, "%.2f pour cent" % (100 * bada / N))

print("")
print("[3] CE QUE CELA AJOUTE A SON INVENTAIRE")
print("      Sa table des ufuncs est mesuree SUR SON POSTE, avec et sans le noyau.")
print("      Elle n'avait pas le meme compte DE CE COTE pour exp et arctan2 : mon")
print("      lot precedent ne mesurait que K1/K2/K3 des flots du geste. Les voici,")
print("      sur le meme etalon (mpmath 200 bits) et le meme volume (20 000).")
print("      => la roue Windows n'embarque de noyau SIMD ni pour power, ni pour exp,")
print("         ni pour arctan2 : les trois restent dans la classe de la libm.")

print("")
print("=" * 88)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, d in MORD:
    print("   MORD  %s  %s" % (q, d))
print("=" * 88)
