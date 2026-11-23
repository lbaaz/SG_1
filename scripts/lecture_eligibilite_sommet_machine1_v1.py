# -*- coding: ascii -*-
"""LECTURE DE LA TABLE D'ELIGIBILITE DU GEL "SOMMET" -- machine 1, v1, 2026-11-22. Aucun calcul de chaine : une lecture.
Lit la sortie de eligibilite_sommet_machine1_v1.py (et, si elle est donnee, la meme sous l'autre reglage de numpy),
imprime la table par w2 et les comptes par kappa, et ecrit la table de machine 1 au format de la regle :
creneaux -> <nom> -> candidats -> liste de {"w2", "eligible", "cellules": liste de {"kappa", "g", "eta0", "r_c", "eligible"}}.
Usage : python3 -I lecture_eligibilite_sommet_machine1_v1.py <eligibilite.json> <table de sortie.json> [<eligibilite autre reglage.json>]"""
import sys, json, math
from fractions import Fraction as F
ORDRE = ("MP", "PP", "MG", "PG")
T = json.load(open(sys.argv[1])); SORTIE = sys.argv[2]
AUTRE = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else None
KAPPAS = [k for (k, c) in T["regle"]["kappas"]]; CIBLE = {k: c for (k, c) in T["regle"]["kappas"]}
print("regle lue : seuil d'etendue %s ; garde e_bord %s ; M_facteur %s ; kappa_3 %s ; %d variantes" % (
    T["regle"]["seuil_etendue"], T["regle"]["garde_e_bord"], T["regle"]["M_facteur"], T["regle"]["kappa_3"], len(T["regle"]["variantes"])))
table = {"creneaux": {}}; toutes = []
for s in ORDRE:
    C = T["creneaux"][s]["candidats"]
    print("creneau %s : %d w2 eligibles sur %d" % (s, sum(c["eligible"] for c in C), len(C)))
    cands = []
    for c in C:
        w = F(c["w2"]); assert [x["kappa"] for x in c["cellules"]] == KAPPAS
        print("  %.5f  %s  %s" % (float(w), " ".join(("%.4f" % x["etendue"]) + ("" if x["eligible"] else "!") for x in c["cellules"]), "ELIGIBLE" if c["eligible"] else "INELIGIBLE"))
        cands.append({"w2": c["w2"], "eligible": c["eligible"], "cellules": [{"kappa": x["kappa"], "g": x["g"], "eta0": x["eta0"], "r_c": x["r_c"], "eligible": x["eligible"]} for x in c["cellules"]]})
        for x in c["cellules"]:
            toutes.append(dict(x, creneau=s, w2=w, d=abs(float(w) - 2.0)))
    table["creneaux"][s] = {"candidats": cands}
n = len(toutes); nw = sum(len(T["creneaux"][s]["candidats"]) for s in ORDRE)
print()
print("cellules candidates : %d (%d w2 x %d kappa) ; eligibles : %d ; w2 eligibles : %d sur %d" % (n, nw, len(KAPPAS), sum(x["eligible"] for x in toutes),
      sum(c["eligible"] for s in ORDRE for c in T["creneaux"][s]["candidats"]), nw))
print("motifs d'ineligibilite : %s" % (sorted(set(x.get("motif", "") for x in toutes if not x["eligible"])) or "aucun"))
print("barriere vide (m_bord pose a 0) : %d cellules ; m_bord different de la cible : %d" % (sum(x["barriere_vide"] for x in toutes), sum(x["m_bord"] != x["cible"] for x in toutes)))
print("kappa   cible  m_bord  r_c  N max  etendue  e_bord  g                         G3*                       Phi = G3* / |d|           etalement  G3* / g                 poids  m*")
print("               trouve              max      max     de ... a ...              de ... a ...              de ... a ...              de ln Phi  de ... a ...            min    de ... a ...")
for k in KAPPAS:
    L = [x for x in toutes if x["kappa"] == k]; lp = [x["ln_Phi"] for x in L]
    print("%s  %d      %-6s  %-3s  %-5d  %.4f   %.3f   %.5e a %.5e  %.5e a %.5e  %.5e a %.5e  %.4f     %.4e a %.4e  %.4f  %d a %d" % (
        k, CIBLE[k], "/".join(str(v) for v in sorted(set(x["m_bord"] for x in L))), "/".join(str(v) for v in sorted(set(x["r_c"] for x in L))), max(x["r_c"] for x in L) + 100,
        max(x["etendue"] for x in L), max(x["e_bord"] for x in L), min(float(x["g"]) for x in L), max(float(x["g"]) for x in L),
        math.exp(min(x["ln_G3"] for x in L)), math.exp(max(x["ln_G3"] for x in L)), math.exp(min(lp)), math.exp(max(lp)), max(lp) - min(lp),
        min(math.exp(x["ln_G3"]) / float(x["g"]) for x in L), max(math.exp(x["ln_G3"]) / float(x["g"]) for x in L), min(x["poids_min"] for x in L),
        min(x["m_etoile"] for x in L), max(x["m_etoile"] for x in L)))
print("plus grande etendue : %.4f (seuil %s) ; plus petit poids du site 0 : %.4f ; methodes : %s" % (max(x["etendue"] for x in toutes), T["regle"]["seuil_etendue"],
      min(x["poids_min"] for x in toutes), sorted(set(m for x in toutes for m in x["methodes"]))))
print("couplages ecrits : de %.5e a %.5e ; largeurs predites G3* : de %.5e a %.5e" % (min(float(x["g"]) for x in toutes), max(float(x["g"]) for x in toutes),
      math.exp(min(x["ln_G3"] for x in toutes)), math.exp(max(x["ln_G3"] for x in toutes))))
print("|ln(G3 / G1)| : plus grand %.5f ; |ln(G3 / G2)| : plus grand %.5f ; par kappa, plus grand |ln(G3 / G1)| : %s" % (max(abs(x["ln_G3"] - x["ln_G1"]) for x in toutes),
      max(abs(x["ln_G3"] - x["ln_G2"]) for x in toutes), " ; ".join("%s %.5f" % (k, max(abs(x["ln_G3"] - x["ln_G1"]) for x in toutes if x["kappa"] == k)) for k in KAPPAS)))
print("eta0 : le second terme du max (la regle en absolu) l'emporte a %d cellules sur %d ; eta0 / |w2 - 2| de %.4f a %.4f ; eta0 / g de %.4f a %.4f" % (
      sum(float(x["eta0"]) > x["d"] * (1 + 1e-9) for x in toutes), n, min(float(x["eta0"]) / x["d"] for x in toutes), max(float(x["eta0"]) / x["d"] for x in toutes),
      min(float(x["eta0"]) / float(x["g"]) for x in toutes), max(float(x["eta0"]) / float(x["g"]) for x in toutes)))
print("cellules ou m* <= r_c / 2 (les absorbeurs du lecteur commenceraient au-dela de m*) : %d" % sum(x["m_etoile"] <= x["r_c"] // 2 for x in toutes))
print("cellules ou G3* depasse 1.08861e-04 (le plus grand plateau qualifie, Q-d) : %d ; plus grand rapport : %.2f" % (sum(math.exp(x["ln_G3"]) > 1.08861e-04 for x in toutes),
      math.exp(max(x["ln_G3"] for x in toutes)) / 1.08861e-04))
print("cellules ou G3* est sous 2.05518e-09 (le plus petit plateau qualifie au sommet, Q2-b) : %d ; plus petit rapport : %.3f" % (sum(math.exp(x["ln_G3"]) < 2.05518e-09 for x in toutes),
      math.exp(min(x["ln_G3"] for x in toutes)) / 2.05518e-09))
signe = []
for s_m, s_p in (("MP", "PP"), ("MG", "PG")):
    for cm in T["creneaux"][s_m]["candidats"]:
        wm = F(cm["w2"]); cp = next(c for c in T["creneaux"][s_p]["candidats"] if F(c["w2"]) - 2 == 2 - wm)
        for xm, xp in zip(cm["cellules"], cp["cellules"]):
            signe.append((xm["kappa"], xm["ln_Phi"] - xp["ln_Phi"]))
print("le signe, a kappa egal et |w2 - 2| egal : ln[Phi(delta < 0) / Phi(delta > 0)] de %+.5f a %+.5f sur %d paires ; par kappa, du plus petit au plus grand : %s" % (
      min(v for (k, v) in signe), max(v for (k, v) in signe), len(signe), " ; ".join("%s %+.5f a %+.5f" % (k, min(v for (k2, v) in signe if k2 == k), max(v for (k2, v) in signe if k2 == k)) for k in KAPPAS)))
if AUTRE is not None:
    ch_el = ch_nb = 0; pire = 0.0
    for s in ORDRE:
        for c, c2 in zip(T["creneaux"][s]["candidats"], AUTRE["creneaux"][s]["candidats"]):
            assert c["w2"] == c2["w2"]; ch_el += c["eligible"] != c2["eligible"]
            for x, y in zip(c["cellules"], c2["cellules"]):
                ch_el += x["eligible"] != y["eligible"]; ch_nb += (x["g"], x["eta0"], x["r_c"]) != (y["g"], y["eta0"], y["r_c"]); pire = max(pire, abs(x["ln_G3"] - y["ln_G3"]))
    print("sous l'autre reglage de numpy : %d eligibilite changee, %d nombre ecrit change, plus grand ecart sur ln G3 %.1e" % (ch_el, ch_nb, pire))
json.dump(table, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s" % SORTIE)
