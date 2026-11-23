# -*- coding: ascii -*-
"""NOTATION, par machine 1, des quatre points "Q2" (lot 295b2b1549b076c2 de machine 2), depuis ses
huit sorties JSON lues comme des donnees. Rien de son lot n'est execute ni importe. Le juge est juger_etat de la feuille
DEPOSEE (registre public, scripts/lecture_lecteur_gel_loi_machine1_v1.py), chargee au canon controle et appelee telle quelle,
avec g_dep3 = None. Attendus Q2-1 a Q2-4 et clause de tort : ceux de ma note f59bdc4b2a8bc3d1, section 4, a la lettre.
Aucune fenetre n'est desserree.
Usage : python3 -I -B note_Q2_machine1_v1.py <dossier Q2_sorties> <feuille deposee> <dossier Q_sorties>"""
import sys, os, json, math, hashlib, unicodedata, importlib.util
DOS, FEUILLE = sys.argv[1], sys.argv[2]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
assert canon_B(FEUILLE) == "83701094e6a2b965", canon_B(FEUILLE)
spec = importlib.util.spec_from_file_location("feuille", FEUILLE); FE = importlib.util.module_from_spec(spec); spec.loader.exec_module(FE)
print("feuille deposee au canon 83701094e6a2b965 : oui ; juger_etat appele tel quel")
POINTS = [("Q2a", "20001/10000", "6e-5", 4.94622e-08, 2.33642e-04, 1, 20), ("Q2b", "20001/10000", "4e-5", 2.05449e-09, 1.55762e-04, 2, 22),
          ("Q2c", "19999/10000", "3e-4", 1.21071e-05, 1.16909e-03, 0, 18), ("Q2d", "19999/10000", "1.5e-4", 2.92086e-06, 5.84544e-04, 0, 18)]
# mes cibles, eta0, profondeurs et r_c : ceux de ma note f59bdc4b2a8bc3d1 ; plateaux de Q-e et Q-f : relus dans les JSON de Q
# absorbeurs : (forme, bord - r_c, couches) ; les bords sont r_c, r_c, r_c, r_c + 10
GEOM = {"A": ("F2", 0, 80), "B": ("F2", 0, 100), "C": ("F1", 0, 100), "D": ("F2", 10, 80)}
res, suivies, total = {}, 0, 0
for (pid, w2, g, G3, eta0, mb, rc) in POINTS:
    f = json.load(open(os.path.join(DOS, "lect2D_%s_fantome.json" % pid)))
    j = json.load(open(os.path.join(DOS, "lect2D_%s_jumeau.json" % pid)))
    for s, signe in ((f, -1), (j, +1)):
        c = s["cellule"]; L = s["lecture"]
        assert str(c["w2"]) == w2 and float(c["g"]) == float(g) and c["r_c"] == rc and c["m"] == mb, (pid, c)
        assert abs(float(c["eta0"]) / eta0 - 1.0) < 1e-12, (pid, c["eta0"], eta0)
        assert L["signe"] == signe and L["site"] == [0, 0] and L["E_depart"] == 0.0, pid
        assert s["source_bloc_canon"] == "d5cc48f48e37af99" and s["moteur_canon"] == "82a0be882568fe0c", pid
        for a, (forme, bord, couches) in GEOM.items():
            x = L["absorbeurs"][a]
            assert (x["forme"], x["bord"], x["couches"]) == (forme, rc + bord, couches), (pid, a, x)
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
print("Q2-1  les quatre points QUALIFIES : %s (%s)" % ("TENU" if Q1 else "TOMBE", " ; ".join("%s %s" % (p, res[p]["J"]["statut"]) for p in res)))
ec = {p: abs(math.log(res[p]["J"]["plateaux"]["A"]["Gamma_pl"] / res[p]["G3"])) for p in res if q[p]}
Q2 = all(v <= 0.002 for v in ec.values()) and len(ec) > 0
print("Q2-2  |ln(Gamma_pl / G3*)| <= 0.002 a chaque point qualifie : %s (%s ; plus grand %.5f)" % ("TENU" if Q2 else "TOMBE", " ; ".join("%s %.5f" % (p, ec[p]) for p in ec), max(ec.values())))
Q3 = all(res[p]["temoin"] for p in res)
print("Q2-3  le temoin tient aux quatre points : %s (plus grande largeur du jumeau rapportee au plateau : %.2e)" % ("TENU" if Q3 else "TOMBE", max(res[p]["jumeau_max"] / res[p]["J"]["plateaux"]["A"]["Gamma_pl"] for p in res)))
DOSQ = sys.argv[3]
def plateau_Q(pid):
    f = json.load(open(os.path.join(DOSQ, "lect2D_%s_fantome.json" % pid)))
    J = FE.juger_etat(f["lecture"]["traj"], None); assert J["statut"] == "QUALIFIE"
    return J["plateaux"]["A"]["Gamma_pl"]
ge, gf = plateau_Q("Qe"), plateau_Q("Qf")
r1 = math.log(res["Q2c"]["J"]["plateaux"]["A"]["Gamma_pl"] / ge); r2 = math.log(res["Q2d"]["J"]["plateaux"]["A"]["Gamma_pl"] / gf)
Q4 = q["Q2c"] and q["Q2d"] and (0.0007 <= r1 <= 0.0017) and (0.0016 <= r2 <= 0.0026)
print("Q2-4  ln[Gamma_pl(Q2-c) / Gamma_pl(Q-e)] = %+.5f dans [+0.0007, +0.0017] : %s ; ln[Gamma_pl(Q2-d) / Gamma_pl(Q-f)] = %+.5f dans [+0.0016, +0.0026] : %s -> %s" % (
    r1, "oui" if 0.0007 <= r1 <= 0.0017 else "NON", r2, "oui" if 0.0016 <= r2 <= 0.0026 else "NON", "TENU" if Q4 else "TOMBE"))
print("      plateaux de Q relus par la feuille : Q-e %.5e ; Q-f %.5e ; chaine : +0.00121 et +0.00211 ; ecarts des lectures a la chaine : %+.5f et %+.5f" % (ge, gf, r1 - 0.00121, r2 - 0.00211))
tort = any(v > 0.01 for v in ec.values()) or sum(1 for p in res if res[p]["J"]["plateaux"]["A"]["statut"] != "PLATEAU") >= 2 or r1 < 0 or r2 < 0
print("TORT : point qualifie a plus de 0.01 : %d ; points sans plateau sous A : %d ; rapport de signe negatif : %d -> %s" % (sum(v > 0.01 for v in ec.values()),
      sum(1 for p in res if res[p]["J"]["plateaux"]["A"]["statut"] != "PLATEAU"), int(r1 < 0) + int(r2 < 0), "REALISE" if tort else "NON REALISE"))
print("ln(Gamma_pl / G3*) signes, aux quatre points : %s" % " ; ".join("%s %+.5f" % (p, math.log(res[p]["J"]["plateaux"]["A"]["Gamma_pl"] / res[p]["G3"])) for p in res))
print("plus grand |ln(X / A)| sur les douze (point, absorbeur B, C, D) : %.4f" % max(res[p]["J"]["plateaux"][a]["ecart_ln_A"] for p in res for a in "BCD"))
print("barreaux plats a 0.005 sous A, communs aux quatre points : %s" % sorted(set.intersection(*[set(res[p]["plat"]) for p in res])))
print("=== BILAN : Q2-1 %s ; Q2-2 %s ; Q2-3 %s ; Q2-4 %s ; tort %s" % (tuple(("TENU" if x else "TOMBE") for x in (Q1, Q2, Q3, Q4)) + ("REALISE" if tort else "NON REALISE",)))
