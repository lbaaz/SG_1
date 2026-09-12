#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LE REJEU EST-IL DETERMINISTE A MON POSTE ? -- machine 2, v1, 12/09/2026.

Sa section 4.3 appelle l'ecart entre machines un BRUIT. Un bruit n'est pas reproductible ;
une difference deterministe l'est. Les deux se separent par une mesure a un seul poste :
jouer DEUX FOIS le meme script, sur la meme machine, et comparer AU BIT.

L'issue qui ferait mordre est ecrite : si les deux runs different, meme d'un ulp, alors le
mot 'bruit' est justifie a mon poste et cette feuille ne conclut rien contre lui. S'ils
sont identiques au bit, le mot est faux -- ce qui separe les deux machines est une
difference DETERMINISTE, et une difference deterministe demande une cause, pas une
tolerance.

Les deux chemins de JSON sont des ARGUMENTS.
"""
import json, sys

if len(sys.argv) < 3:
    sys.exit("usage : controle_determinisme_machine2_v1.py <json rejeu1> <json rejeu2>")
a = json.load(open(sys.argv[1], encoding="utf-8"))
b = json.load(open(sys.argv[2], encoding="utf-8"))

print("=" * 84)
print("DEUX REJEUX AU MEME POSTE -- BRUIT OU DIFFERENCE DETERMINISTE ?")
print("=" * 84)
p = a.get("plateforme", {})
print("      poste : python %s ; numpy %s ; %s"
      % (p.get("python"), p.get("numpy"), p.get("platform")))

GRANDEURS = ("e", "R_composantes", "plancher_composantes", "ratio_seuil_du_flot",
             "tau_au_max", "err_rel_fin")
tout = True
print("\n[1] LES QUATRE FLOTS, SIX GRANDEURS CHACUN")
for k in range(4):
    lignes = []
    for q in GRANDEURS:
        x, y = a["flots"][k][q], b["flots"][k][q]
        tout &= (x == y)
        lignes.append("%s %s" % (q, "bit" if x == y else "DIFFERE"))
    print("      dt2/%-4d e = %r   %s"
          % (2 ** k, a["flots"][k]["e"],
             "les six au bit" if all("DIFFERE" not in l for l in lignes)
             else " | ".join(lignes)))

print("\n[2] LES TROIS PAIRES")
for i in range(3):
    x, y = a["paires"][i]["p_obs"], b["paires"][i]["p_obs"]
    tout &= (x == y)
    print("      paire %d : p_obs = %r   %s" % (i, x, "bit" if x == y else "DIFFERE"))

print("\n" + "=" * 84)
if tout:
    print("VERDICT : LES DEUX REJEUX SONT IDENTIQUES AU BIT.")
    print("  Mon poste est DETERMINISTE sur ce calcul. Le mot 'bruit' ne decrit donc pas")
    print("  ce qui separe les deux machines : c'est une difference DETERMINISTE entre")
    print("  deux plateformes, reproductible de chaque cote. Elle demande une cause.")
    print("  CE QUE CETTE FEUILLE NE DIT PAS : quelle cause. Aucune n'est proposee ici.")
else:
    print("VERDICT : LES DEUX REJEUX DIFFERENT -- le calcul n'est pas deterministe a mon")
    print("  poste, et le mot 'bruit' de sa section 4.3 est justifie. Cette feuille ne")
    print("  conclut rien contre lui.")
print("=" * 84)
