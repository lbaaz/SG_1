#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA SURFACE D'EXPOSITION, MESUREE SUR LE REGISTRE DEPOSE -- machine 2, v1, 12/09/2026.

Sa note d'exposition repond depuis SON poste (quelles ufuncs, quels chemins de code).
Cette feuille repond depuis LE REGISTRE : combien de scripts deposes de sa plume peuvent
avoir appele le moteur, et -- surtout -- ce que le registre permet ou NON de dater.

Elle compte 19 journaux citant Windows ; je compte ici sur un autre denominateur (les
.log deposes) et je le dis, pour que les deux nombres ne se contredisent pas en prose.

Le chemin du clone est un ARGUMENT.
"""
import os, re, sys

if len(sys.argv) < 2:
    sys.exit("usage : surface_exposition_registre_machine2_v1.py <clone frais>")
CL = sys.argv[1]
OK = []


def chk(q, c, d=''):
    OK.append(bool(c))
    print("  [%s] %-54s %s" % ("OK  " if c else "--  ", q[:54], d))


fics = []
for r, d, fs in os.walk(CL):
    if ".git" in r:
        continue
    for f in fs:
        fics.append(os.path.join(r, f))
logs = [p for p in fics if p.endswith(".log")]
pys = [p for p in fics if p.endswith(".py")]

print("=" * 88)
print("SURFACE D'EXPOSITION, MESUREE SUR LE REGISTRE DEPOSE")
print("=" * 88)

print("\n[1] CE QUE LE REGISTRE PERMET DE DATER -- ET IL NE LE PERMET PAS")
def contient(p, motif):
    try:
        return bool(re.search(motif, open(p, encoding="utf-8", errors="replace").read(),
                              re.I))
    except Exception:
        return False


np_ = [p for p in logs if contient(p, r"numpy\s*[:= ]\s*\d+\.\d+")]
py_ = [p for p in logs if contient(p, r"python\s*[:= ]?\s*3\.\d+\.\d+")]
di_ = [p for p in logs if contient(p, r"X86_V\d|AVX512|show_runtime")]
print("      .log deposes au registre              : %d" % len(logs))
print("      qui nomment une version de numpy      : %d" % len(np_))
print("      qui nomment une version de python     : %d" % len(py_))
print("      qui nomment un niveau de dispatch     : %d" % len(di_))
chk("le registre ne permet PAS de dater l'exposition", len(di_) == 0,
    "aucun log ne porte de niveau de dispatch : c'est la mesure qui fonde sa regle (X)")

print("\n[2] LA SURFACE DE MACHINE 1 DANS LE REGISTRE")
m1 = [p for p in pys if "machine1" in os.path.basename(p)]
m2 = [p for p in pys if "machine2" in os.path.basename(p)]
autres = [p for p in pys if p not in m1 and p not in m2]


def charge_moteur(p):
    return contient(p, r"m9_replication|charger_moteur")


cm1 = [p for p in m1 if charge_moteur(p)]
cm2 = [p for p in m2 if charge_moteur(p)]
print("      scripts .py deposes                   : %d" % len(pys))
print("        de plume machine 1                  : %d" % len(m1))
print("        de plume machine 2                  : %d" % len(m2))
print("        sans plume au nom                   : %d" % len(autres))
print("      QUI CHARGENT LE MOTEUR : m1 %d | m2 %d" % (len(cm1), len(cm2)))
for p in sorted(cm1):
    print("        m1 -> %s" % os.path.basename(p))
chk("la surface de machine 1 se reduit au BANC de la constante A",
    all("banc_qualification" in os.path.basename(p) for p in cm1) and len(cm1) > 0,
    "%d scripts sur %d de sa plume" % (len(cm1), len(m1)))
print("      PORTEE : classement par le NOM du fichier et detection par MOTIF -- deux")
print("      approximations, dites comme telles. Un script sans plume au nom qui")
print("      chargerait le moteur n'est pas attribue ici.")

print("\n[3] POURQUOI UN VERDICT DE MANCHE N'EST PAS SENSIBLE A UN ulp")
pas = 0.014144576281064155
print("      pas de grille (relatif)               : %.4e" % pas)
print("      ulp relatif                           : %.4e" % 2 ** -52)
print("      rapport                               : %.2e" % (pas / 2 ** -52))
print("      Un seuil s* = min(noeuds explosifs) ne bouge que si un noeud CHANGE DE")
print("      CLASSE. C'est un evenement discret, pas une derive : il demande un noeud")
print("      marginal dans sa fenetre. La ou le noyau a mordu -- 7|1.73 -- la lecture")
print("      n'est pas un seuil de grille mais une grandeur COMPENSEE amplifiee par")
print("      R = 5.9e+07 : quatorze ordres plus sensible. La campagne n'a qu'un banc")
print("      de cette nature, et c'est celui-la.")

print("\n[4] CE QUI RESTE A RE-LIRE, ET CE N'EST PAS UN RESULTAT MAIS UNE PREUVE")
print("      Une egalite AU BIT entre machines qui a TENU est desormais une preuve")
print("      plus faible qu'elle n'en avait l'air : elle a pu tenir parce que la")
print("      chaine n'appelle aucun ** de tableau (robuste), ou parce qu'aucun")
print("      basculement n'est tombe dessus (fortuit). Les deux se separent par une")
print("      mesure, et son diagnostic v2 est deja l'instrument : cas durs et")
print("      basculements par flot.")
print("      L'ITEM NOMME : 'N-70 v2 contre-derivee et REPRODUITE AU BIT des deux")
print("      cotes' -- c'est une grandeur de BANC, et le banc est le seul de ses")
print("      scripts deposes qui charge le moteur.")
print("      Sa note d'exposition dit que la chaine constante A a tenu au bit partout")
print("      sauf 7|1.73 : c'est le FAIT. Ce qui manque est POURQUOI, et un rejeu du")
print("      banc sans le noyau le donne en un geste.")

print("\n" + "=" * 88)
print("mesures : %d ; aucune n'est un verdict de gel" % len(OK))
print("=" * 88)
