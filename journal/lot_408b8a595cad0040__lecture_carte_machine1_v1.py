# -*- coding: ascii -*-
"""LECTURE DE LA CARTE -- machine 1, v1, 2026-11-16. Hors chaine. Lit carte_v1.json, ne calcule aucune largeur.
Usage : python3 -I lecture_carte_machine1_v1.py <carte.json> <sortie.json>"""
import sys, json
ENTREE, SORTIE = sys.argv[1:3]
J = json.load(open(ENTREE)); P = J["points"]
STAB_MAX = 0.05
out = {"comptes": {}, "tables": {}, "stable_jusqu_a": {}, "bornes": {}}
calc = [p for p in P if not p["vide"]]
out["comptes"] = {"points": len(P), "calcules": len(calc), "non_calcules": len(P) - len(calc),
                  "voie_flux": sum(1 for p in calc if p["voie3"] == "flux"), "voie_mp": sum(1 for p in calc if p["voie3"] != "flux")}
print("points : %d ; calcules : %d ; non calcules : %d ; largeur d'ordre 3 par le flux : %d, par la precision arbitraire : %d" % (
    len(P), len(calc), len(P) - len(calc), out["comptes"]["voie_flux"], out["comptes"]["voie_mp"]))
print("controles de la carte :", J["controles"])
MS = sorted(set(p["m_cible"] for p in P)); ES = sorted(set(p["e_cible"] for p in P))
for (n1, n2) in ((0, 0), (6, 2)):
    cle = "%d,%d" % (n1, n2); out["tables"][cle] = []; out["stable_jusqu_a"][cle] = {}
    print(); print("etiquette (%d, %d) : r3 = ln(Gamma_3 / (|delta| Phi)) a delta < 0 | a delta > 0 ; * : chaine d'ordre 3 instable sous son absorbeur (stab3 > %.2f)" % (n1, n2, STAB_MAX))
    print("  m_cible  -ln Phi  " + "".join("   e = %-5.3f           " % e for e in ES))
    for m in MS:
        txt = ""; lnphi = None
        for e in ES:
            cases = []
            for sg in (-1, 1):
                q = [p for p in P if p["n1"] == n1 and p["n2"] == n2 and p["m_cible"] == m and p["e_cible"] == e and (p["delta"] < 0) == (sg < 0)]
                assert len(q) == 1
                q = q[0]
                if q["vide"] or q["r3"] is None:
                    cases.append("   -    "); continue
                lnphi = q["ln_Phi"]
                inst = q["stab3"] is None or q["stab3"] > STAB_MAX
                cases.append("%+.3f%s" % (q["r3"], "*" if inst else " "))
                out["tables"][cle].append({"m_cible": m, "e_cible": e, "signe": sg, "delta": q["delta"], "m_bord": q["m_bord"], "e_bord": q["e_bord"], "r2": q["r2"], "r3": q["r3"], "stab3": q["stab3"], "instable": inst})
            txt += "  %s|%s  " % (cases[0], cases[1])
        print("  %4d    %7.1f  %s" % (m, -lnphi, txt))
        # plus grand e_cible tel que la chaine soit stable aux deux signes pour lui et tous les plus petits
        dernier = None
        for e in ES:
            q = [x for x in out["tables"][cle] if x["m_cible"] == m and x["e_cible"] == e]
            if len(q) == 2 and not any(x["instable"] for x in q):
                dernier = e
            else:
                break
        out["stable_jusqu_a"][cle][str(m)] = dernier
    print("  stable (aux deux signes, sans trou) jusqu'a e_cible : " + " ; ".join("m = %s : %s" % (m, out["stable_jusqu_a"][cle][str(m)]) for m in MS))
    st = [x for x in out["tables"][cle] if not x["instable"]]
    for (mlo, elo, ehi) in ((12, 0.0, 0.75), (24, 0.0, 1.2)):
        s = [x for x in st if x["m_cible"] >= mlo and elo <= x["e_cible"] <= ehi and x["e_cible"] <= (0.7 if ehi < 1 else 1.0)]
        if s:
            pire = max(s, key=lambda x: abs(x["r3"])); ec = max(abs(x["r3"] - x["r2"]) for x in s)
            out["bornes"]["%s_m%d_e%.1f" % (cle, mlo, min(ehi, 1.0))] = {"n": len(s), "pire_r3": pire["r3"], "a": [pire["m_cible"], pire["e_cible"], pire["signe"]], "pire_r3_moins_r2": ec}
            print("  points stables, m_cible >= %d, e_cible <= %.1f : %d ; plus grand |r3| = %.3f (m_cible %d, e_cible %.3f, signe %+d) ; plus grand |r3 - r2| = %.3f" % (
                mlo, 0.7 if ehi < 1 else 1.0, len(s), abs(pire["r3"]), pire["m_cible"], pire["e_cible"], pire["signe"], ec))
inst = [x for c in out["tables"] for x in out["tables"][c] if x["instable"]]
out["instables"] = {"n": len(inst), "delta_abs_min": min(abs(x["delta"]) for x in inst), "m_bord_max": max(x["m_bord"] for x in inst)}
print(); print("points instables : %d ; leur plus petit |delta| : %.4f ; leur plus grand m_bord : %d" % (len(inst), out["instables"]["delta_abs_min"], out["instables"]["m_bord_max"]))
stab = [x for c in out["tables"] for x in out["tables"][c] if not x["instable"]]
print("points stables : %d ; leur plus grand |delta| : %.4f ; leur plus grand e_bord : %.3f" % (len(stab), max(abs(x["delta"]) for x in stab), max(x["e_bord"] for x in stab)))
out["stables"] = {"n": len(stab), "delta_abs_max": max(abs(x["delta"]) for x in stab), "e_bord_max": max(x["e_bord"] for x in stab)}
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
