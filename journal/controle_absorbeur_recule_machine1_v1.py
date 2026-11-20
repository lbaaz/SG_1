# -*- coding: utf-8 -*-
# Controle venu APRES la lecture : un cinquieme absorbeur, hors lecteur depose (forme F2, bord recule de 30 : r_c + 30 = 54, boite 134),
# barreaux -2 a 2. Rend-il les memes densites que la mediane des quatre absorbeurs du lecteur ?
# Usage : python3 -I controle_absorbeur_recule_machine1_v1.py <lecture.json> <lisse_2d_E.json> <sortie.json>
import sys, json, math
L = json.load(open(sys.argv[1])); E = json.load(open(sys.argv[2])); X = L["X"]
ec = []
for i, x in enumerate(X):
    v = [math.log(E["k"][k]["rho_flux"][i]) for k in E["k"] if E["k"][k]["suivi"]]
    ec.append((x, sum(v) / len(v) - L["par_x"][i]["ln_rho_2d"], max(v) - min(v)))
print("absorbeur E (bord %d, boite %d, barreaux %s) : ln rho_E - ln rho_2D (mediane A, B, C, D), et etalement entre ses barreaux" % (E["bord"], E["N"], sorted(int(k) for k in E["k"])))
for x, d, e in ec: print("  x = %5.2f : %+.4f   (etalement %.4f)" % (x, d, e))
print("ecart au plus %.4f ; etalement au plus %.4f" % (max(abs(d) for _, d, _ in ec), max(e for _, _, e in ec)))
json.dump({"bord": E["bord"], "N": E["N"], "ecart_max": max(abs(d) for _, d, _ in ec), "etalement_max": max(e for _, _, e in ec), "par_x": ec}, open(sys.argv[3], "w"), indent=1)
