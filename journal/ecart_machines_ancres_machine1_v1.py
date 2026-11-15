# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. Pour la tolerance de la garde G-8 : l'ecart entre machines de la
# chaine du moteur (-2 Im E) aux deux etats d'ancre, JSON du run precedent de machine 2 contre l'essai a blanc de machine 1.
# usage : python3 -I ecart_machines_ancres_machine1_v1.py <sonde_domaine_G1.json de machine 2> <essai de machine 1>
import sys, json
m2 = json.load(open(sys.argv[1], encoding="ascii")); m1 = json.load(open(sys.argv[2], encoding="ascii"))
pire = 0.0
for pid, lab in (("A1", (7, 2)), ("A2", (8, 2))):
    a = [e for p in m2["points"] if p["id"] == pid for e in p["etats"] if (e["n1"], e["n2"]) == lab]
    b = [e for p in m1["points"] if p["id"] == pid for e in p["etats"] if (e["n1"], e["n2"]) == lab]
    assert len(a) == 1 and len(b) == 1
    ec = [abs(x / y - 1.0) for x, y in zip(a[0]["chaine"]["gammas"], b[0]["chaine"]["gammas"])]
    pire = max(pire, max(ec))
    print("%s (%d,%d) chaine du moteur aux quatre eta, machine 2 / machine 1 - 1 en valeur absolue : %s" % (
        pid, lab[0], lab[1], " ".join("%.1e" % x for x in ec)))
    print("   Gamma_2D(3) : %.1e ; E_re : %.1e en absolu" % (abs(a[0]["Gamma_2D"]["3"] / b[0]["Gamma_2D"]["3"] - 1.0), abs(a[0]["E_re"] - b[0]["E_re"])))
print("plus grand ecart de chaine entre machines aux deux etats d'ancre : %.1e ; tolerance de G-8 : 1e-3" % pire)
