# -*- coding: ascii -*-
"""NOTATION, par machine 1, de la qualification "Q" du lecteur au sommet (lot c58c2b3f533c516b de machine 2), depuis ses
dix sorties JSON lues comme des donnees. Rien de son lot n'est execute ni importe. Le juge est juger_etat de la feuille
DEPOSEE (registre public, scripts/lecture_lecteur_gel_loi_machine1_v1.py), chargee au canon controle et appelee telle quelle,
avec g_dep3 = None. Attendus Q-1 a Q-5 et clause de tort : ceux de ma note 1e3bcbb42899069e, section 8.3, a la lettre.
Aucune fenetre n'est desserree.
Usage : python3 -I -B note_Q_sommet_machine1_v1.py <dossier Q_sorties> <feuille deposee>"""
import sys, os, json, math, hashlib, unicodedata, importlib.util
DOS, FEUILLE = sys.argv[1], sys.argv[2]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
assert canon_B(FEUILLE) == "83701094e6a2b965", canon_B(FEUILLE)
spec = importlib.util.spec_from_file_location("feuille", FEUILLE); FE = importlib.util.module_from_spec(spec); spec.loader.exec_module(FE)
print("feuille deposee au canon 83701094e6a2b965 : oui ; juger_etat appele tel quel")
# mes cibles (colonne G3* de la section 6.2) et mes eta0 (section 8.1), recopies de ma note
POINTS = [("Qa", "2", "2.5e-4", 1.36076e-05, 9.73875e-04), ("Qc", "2", "1e-3", 5.44311e-05, 3.89550e-03), ("Qd", "2", "2e-3", 1.08861e-04, 7.79100e-03),
          ("Qe", "20001/10000", "3e-4", 1.20924e-05, 1.16821e-03), ("Qf", "20001/10000", "1.5e-4", 2.91470e-06, 5.84106e-04)]
GEOM = {"A": ("F2", 18, 80), "B": ("F2", 18, 100), "C": ("F1", 18, 100), "D": ("F2", 28, 80)}
LISTES = {"A": (-2, -1, 0), "B": (-2, -1, 0), "C": (0, 1, 2), "D": (-3, -2, -1)}
res, suivies, total = {}, 0, 0
for (pid, w2, g, G3, eta0) in POINTS:
    f = json.load(open(os.path.join(DOS, "lect2D_%s_fantome.json" % pid)))
    j = json.load(open(os.path.join(DOS, "lect2D_%s_jumeau.json" % pid)))
    for s, signe in ((f, -1), (j, +1)):
        c = s["cellule"]; L = s["lecture"]
        assert str(c["w2"]) == w2 and float(c["g"]) == float(g) and c["r_c"] == 18 and c["m"] == 0, (pid, c)
        assert abs(float(c["eta0"]) / eta0 - 1.0) < 1e-12, (pid, c["eta0"], eta0)
        assert L["signe"] == signe and L["site"] == [0, 0] and L["E_depart"] == 0.0, pid
        assert s["source_bloc_canon"] == "d5cc48f48e37af99" and s["moteur_canon"] == "82a0be882568fe0c", pid
        for a, (forme, bord, couches) in GEOM.items():
            x = L["absorbeurs"][a]
            assert (x["forme"], x["bord"], x["couches"]) == (forme, bord, couches), (pid, a, x)
            assert sorted(int(k) for k in L["traj"][a]) == list(range(-3, 9)), (pid, a)
            total += 12; suivies += sum(1 for k in L["traj"][a] if L["traj"][a][k]["suivi"])
    J = FE.juger_etat(f["lecture"]["traj"], None)
    P = J["plateaux"]
    gj = [j["lecture"]["traj"][a][k] for a in "ABCD" for k in j["lecture"]["traj"][a]]
    temoin = all(x["suivi"] for x in gj) and (P["A"]["statut"] == "PLATEAU") and max(x["gamma"] for x in gj) <= 1e-6 * P["A"]["Gamma_pl"]
    pa = P["A"]
    poids_fen = min(f["lecture"]["traj"]["A"][str(k)]["poids_site"] for k in range(pa["k0"], pa["k0"] + 5)) if pa["statut"] == "PLATEAU" else float("nan")
    plat = [k for k in range(-3, 9) if f["lecture"]["traj"]["A"][str(k)]["suivi"] and abs(f["lecture"]["traj"]["A"][str(k)]["gamma"] / pa["Gamma_pl"] - 1.0) <= 0.005]
    res[pid] = {"J": J, "G3": G3, "g": float(g), "temoin": temoin, "jumeau_max": max(x["gamma"] for x in gj), "poids_fen": poids_fen, "plat": plat}
    print("=== %s  w2 = %s  g = %s  eta0 = %.5e  statut %s ; echecs %s ; non lisibles %s" % (pid, w2, g, eta0, J["statut"], J["echecs"], J["non_lisibles"]))
    for a in "ABCD":
        p = P[a]
        print("    %s : %-8s k0 = %+d  etalement %.4f  Gamma_pl = %.5e  ln(Gamma_pl / G3*) = %+.5f%s" % (a, p["statut"], p["k0"], p["etalement"], p["Gamma_pl"], math.log(p["Gamma_pl"] / G3),
              ("  |ln(X / A)| = %.4f" % p["ecart_ln_A"]) if "ecart_ln_A" in p else ""))
    print("    Gamma_pl(A) / g = %.6f ; ln(Gamma_pl / G3*) = %+.5f ; poids du site dans la fenetre de A >= %.4f ; plat a 0.005 sous A aux barreaux %s" % (
        pa["Gamma_pl"] / float(g), math.log(pa["Gamma_pl"] / G3), poids_fen, plat))
    print("    jumeau : %d lectures suivies sur %d ; plus grande largeur %.3e (%.2e Gamma_pl) ; temoin %s" % (sum(x["suivi"] for x in gj), len(gj), res[pid]["jumeau_max"],
          res[pid]["jumeau_max"] / pa["Gamma_pl"], "TIENT" if temoin else "NE TIENT PAS"))
print()
print("lectures suivies : %d sur %d" % (suivies, total))
print("=== MES ATTENDUS, A LA LETTRE")
q = {p: res[p]["J"]["statut"] == "QUALIFIE" for p in res}
Q1 = all(q.values())
print("Q-1  les cinq points QUALIFIES : %s (%s)" % ("TENU" if Q1 else "TOMBE", " ; ".join("%s %s" % (p, res[p]["J"]["statut"]) for p in res)))
ec = {p: abs(math.log(res[p]["J"]["plateaux"]["A"]["Gamma_pl"] / res[p]["G3"])) for p in res if q[p]}
Q2 = all(v <= 0.010 for v in ec.values()) and len(ec) > 0
print("Q-2  |ln(Gamma_pl / G3*)| <= 0.010 a chaque point qualifie : %s (%s ; plus grand %.5f)" % ("TENU" if Q2 else "TOMBE", " ; ".join("%s %.5f" % (p, ec[p]) for p in ec), max(ec.values())))
Q3 = all(res[p]["temoin"] for p in res)
print("Q-3  le temoin tient aux cinq points : %s (plus grande largeur du jumeau rapportee au plateau : %.2e)" % ("TENU" if Q3 else "TOMBE", max(res[p]["jumeau_max"] / res[p]["J"]["plateaux"]["A"]["Gamma_pl"] for p in res)))
fen = [(p, a, res[p]["J"]["plateaux"][a].get("k0")) for p in res for a in "ABCD"]
dans = [x for x in fen if x[2] in LISTES[x[1]]]
Q4 = len(dans) >= 16
print("Q-4  fenetres dans mes listes : %d sur %d (il en faut 16) : %s ; hors liste : %s" % (len(dans), len(fen), "TENU" if Q4 else "TOMBE", [(p, a, k) for (p, a, k) in fen if k not in LISTES[a]]))
if q["Qa"] and q["Qd"]:
    r5 = abs(math.log((res["Qd"]["J"]["plateaux"]["A"]["Gamma_pl"] / res["Qd"]["g"]) / (res["Qa"]["J"]["plateaux"]["A"]["Gamma_pl"] / res["Qa"]["g"])))
    Q5 = r5 <= 0.005
    print("Q-5  |ln[(Gamma_pl / g)(Q-d) / (Gamma_pl / g)(Q-a)]| = %.5f (<= 0.005) : %s" % (r5, "TENU" if Q5 else "TOMBE"))
else:
    Q5 = None; print("Q-5  non evaluable")
tort = any(v > 0.02 for v in ec.values()) or sum(1 for p in res if res[p]["J"]["plateaux"]["A"]["statut"] != "PLATEAU") >= 2
print("TORT : point qualifie a plus de 0.02 : %d ; points sans plateau sous A : %d -> %s" % (sum(v > 0.02 for v in ec.values()), sum(1 for p in res if res[p]["J"]["plateaux"]["A"]["statut"] != "PLATEAU"), "REALISE" if tort else "NON REALISE"))
print("plus grand |ln(X / A)| sur les quinze (point, absorbeur B, C, D) : %.4f" % max(res[p]["J"]["plateaux"][a]["ecart_ln_A"] for p in res for a in "BCD"))
print("barreaux plats a 0.005 sous A, communs aux cinq points : %s" % sorted(set.intersection(*[set(res[p]["plat"]) for p in res])))
print("=== BILAN : Q-1 %s ; Q-2 %s ; Q-3 %s ; Q-4 %s ; Q-5 %s ; tort %s" % (tuple(("TENU" if x else "TOMBE") for x in (Q1, Q2, Q3, Q4, Q5)) + ("REALISE" if tort else "NON REALISE",)))
