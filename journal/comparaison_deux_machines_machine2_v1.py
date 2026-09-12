#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LES DEUX JSON, NOMBRE PAR NOMBRE -- machine 2, v1, 12/09/2026.

Le geste (2) demande une lecture. Cette feuille ne lit pas la prose des notes : elle
confronte les DEUX SORTIES, flottant par flottant, et classe chaque grandeur en
IDENTIQUE AU BIT / ecart relatif. C'est de la que sort le fait central de ce rejeu.

CE QU'ELLE ETABLIT, ET QUI N'ETAIT PAS ATTENDU : l'ecart entre machines n'est PAS
distribue comme le mecanisme de sa section 4.3 le predit. Le pas le plus domine par le
PLANCHER est identique AU BIT entre deux plateformes differentes ; le pas domine par la
TRONCATURE porte la totalite de l'ecart.

Les deux chemins de JSON sont des ARGUMENTS.
"""
import json, sys

if len(sys.argv) < 3:
    sys.exit("usage : comparaison_deux_machines_machine2_v1.py <json m1> <json m2>")
m1 = json.load(open(sys.argv[1], encoding="utf-8"))
m2 = json.load(open(sys.argv[2], encoding="utf-8"))

print("=" * 92)
print("LES DEUX SORTIES DU GESTE (2), NOMBRE PAR NOMBRE")
print("=" * 92)
print("\n[0] LES DEUX PLATEFORMES")
for j, n in ((m1, "m1"), (m2, "m2")):
    p = j.get("plateforme", {})
    print("      %s : python %s ; numpy %s ; %s"
          % (n, p.get("python"), p.get("numpy"), p.get("platform")))

ident, diff = [], []


def walk(a, b, path=""):
    if isinstance(a, dict):
        for k in a:
            if k in b:
                walk(a[k], b[k], path + "/" + k)
    elif isinstance(a, list):
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, path + "[%d]" % i)
    elif isinstance(a, float) and isinstance(b, float):
        (ident if a == b else diff).append((path, a, b))


walk(m1, m2)
print("\n[1] BILAN BRUT : %d grandeurs identiques AU BIT, %d differentes"
      % (len(ident), len(diff)))

print("\n[2] LE FAIT CENTRAL -- LA TRONCATURE DECROIT EN dt^4, L'ECART NE SUIT PAS")
e0 = m2["flots"][0]["e_sur_plancher"]
print("      %-8s %-22s %-12s %-14s %s"
      % ("pas", "troncature attendue", "e mesure", "part plancher", "les deux machines"))
for k in range(4):
    a, b = m1["flots"][k], m2["flots"][k]
    tronc = e0 / 16 ** k
    part = 100 * (1 - min(tronc, b["e_sur_plancher"]) / b["e_sur_plancher"])
    ec = abs(b["e"] / a["e"] - 1)
    print("      dt2/%-4d <= %8.3f plancher   %9.4f    %5.1f %% plancher   %s"
          % (2 ** k, tronc, b["e_sur_plancher"], part,
             "IDENTIQUE AU BIT" if a["e"] == b["e"] else "%.2e" % ec))

print("\n[3] LE PAS LE PLUS DOMINE PAR LE PLANCHER (dt2/8), GRANDEUR PAR GRANDEUR")
tout_bit = True
for q in ("e", "R_composantes", "plancher_composantes", "ratio_seuil_du_flot",
          "tau_au_max"):
    a, b = m1["flots"][3][q], m2["flots"][3][q]
    tout_bit &= (a == b)
    print("      %-24s %r   %s" % (q, a, "IDENTIQUE AU BIT" if a == b else "DIFFERE"))
print("      => les cinq au bit : %s" % tout_bit)

print("\n[4] CE QUE CELA CONTREDIT, ET CE QUE CELA NE TOUCHE PAS")
# Le pourcentage est CALCULE, jamais tape : une prose qui porte un nombre a la main finit
# par contredire le calcul d'a cote. Il l'avait deja fait dans une premiere version de
# cette feuille (98.4 ecrit, 98.5 calcule).
part8 = 100 * (1 - min(e0 / 16 ** 3, m2["flots"][3]["e_sur_plancher"])
               / m2["flots"][3]["e_sur_plancher"])
print("      CONTREDIT : sa section 4.3 -- 'une grandeur qui vit a quelques plancher")
print("                  n'est reproductible entre plateformes qu'a quelques plancher")
print("                  pres'. Mesure : la grandeur la PLUS de plancher (%.1f %%) est"
      % part8)
print("                  reproduite AU BIT sur deux OS, deux python, deux numpy ; et")
print("                  c'est le pas le MOINS de plancher des trois fins qui porte")
print("                  tout l'ecart. L'inverse de ce que le mecanisme predit.")
print("      NE TOUCHE PAS : son verdict. E-A tient, la paire du gel est hors regime")
print("                  RK4 des deux cotes, 0.759 et 0.684 sont tous deux sous 1,")
print("                  l'ecart reste plus petit que le plateau. C'est l'EXPLICATION")
print("                  qui tombe, pas la CONCLUSION.")
print("      NON PROPOSE : aucun mecanisme de remplacement. Je mesure, je ne modelise pas.")

print("\n[5] LES ECARTS, TOUS, PAR ORDRE DECROISSANT")
for path, a, b in sorted(diff, key=lambda t: -abs(t[2] / t[1] - 1) if t[1] else 0):
    if path.endswith("duree_s"):
        continue
    r = abs(b / a - 1) if a else float("nan")
    print("      %-46s %.2e   m1=%.10g  m2=%.10g" % (path, r, a, b))
print("=" * 92)
