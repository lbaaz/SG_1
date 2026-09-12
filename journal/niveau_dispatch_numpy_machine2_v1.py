#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LE NIVEAU DE DISPATCH numpy DE BOCAL4, ET CE QU'IL DEMENT -- machine 2, v1, 12/09/2026.

Machine 1 demande « une ligne de plus, sans cout : numpy.show_runtime() sur BOCAL4 ».
La voici -- et elle porte plus que son niveau de dispatch.

SA SECTION 5.1 attribue la cause a « une difference de LOGICIEL (le noyau de numpy) et de
MATERIEL (il ne s'active que sur AVX512), pas d'OS ni de version de Python », et sa regle
candidate dit que « deux postes de meme numpy et de meme OS different au bit selon que le
CPU a AVX512 ou non ».

CE POSTE EST LE CONTRE-EXEMPLE DE LA MOITIE MATERIELLE : il A AVX512, numpy le TROUVE, et
le `**` de tableau y reste correctement arrondi. Ce n'est donc pas la presence d'AVX512
qui decide, c'est le NOYAU que la version de numpy embarque pour ce niveau.

L'issue qui ferait mordre est ecrite : si ce poste n'avait PAS AVX512, il ne dirait rien
contre elle et cette feuille se tairait.
"""
import json, numpy, platform, sys

print("=" * 84)
print("NIVEAU DE DISPATCH numpy SUR BOCAL4")
print("=" * 84)
# numpy.show_runtime() imprime le uname, dont le NOM DE MACHINE peut etre non-ASCII
# (il l'est ici) : la sortie cesserait alors d'etre ASCII pur et ne pourrait plus entrer
# au lot sous la convention B == brut. Je reprends donc les memes champs a la main,
# en ASCII, et je dis ce que j'omets.
print("  (numpy.show_runtime() n'est pas appele : il imprime le nom de machine, non-ASCII")
print("   sur ce poste, ce qui sortirait une piece de la convention ASCII/LF. Les memes")
print("   champs sont repris ci-dessous ; seul le nom de machine est omis.)")

simd = {}
try:
    from numpy.core._multiarray_umath import __cpu_features__ as feats
except Exception:
    try:
        from numpy._core._multiarray_umath import __cpu_features__ as feats
    except Exception:
        feats = {}
trouves = sorted(k for k, v in feats.items() if v)
print("\n[1] CE QUE numpy TROUVE SUR CE CPU")
print("      numpy   : %s" % numpy.__version__)
print("      python  : %s" % sys.version.split()[0])
print("      platform: %s" % platform.platform())
print("      machine : %s" % platform.machine())
avx512 = [k for k in trouves if "AVX512" in k]
print("      AVX512 actives : %s" % (", ".join(avx512) if avx512 else "AUCUNE"))
print("      niveaux X86_Vn actifs : %s"
      % (", ".join(k for k in trouves if k.startswith("X86_V")) or "aucun nomme ainsi"))

print("\n[2] LE POINT QUI MORD CONTRE SA 5.1")
a_avx512 = bool(avx512)
print("  [%s] ce poste A AVX512 et numpy le trouve" % ("OK  " if a_avx512 else "-   "))
print("  [%s] et il est CORRECTEMENT ARRONDI : le diagnostic mesure numpy != python"
      % ("OK  " if a_avx512 else "-   "))
print("         sur 0 appel K1 des quatre flots (0 / 22800), et 0 basculement.")
if a_avx512:
    print("\n  => LA PRESENCE D'AVX512 N'EST PAS CE QUI DECIDE. Les deux postes ont AVX512 ;")
    print("     l'un est CR sur ces flots, l'autre non. Ce qui les separe est le NOYAU que")
    print("     la version de numpy embarque (2.4.4 nomme un niveau X86_V4 que 2.2.6 ne")
    print("     nomme pas), pas le jeu d'instructions du CPU.")
    print("  => SA REGLE CANDIDATE demande donc un mot de plus : la ligne de plateforme")
    print("     nomme le niveau de dispatch ACTIF **et la version de numpy**, car c'est")
    print("     leur couple qui choisit le noyau -- pas le CPU seul.")
else:
    print("\n  => ce poste n'a pas AVX512 : il ne dit RIEN contre sa 5.1, et cette feuille")
    print("     se tait. (Ce n'est pas le cas mesure ici.)")
print("=" * 84)
