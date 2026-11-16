# -*- coding: ascii -*-
"""COMPARAISON DU REJEU DE MACHINE 1 AU RUN -- machine 1, v1, 2026-11-16. Arithmetique sur des fichiers ; aucun calcul.
Entrees : le verdict d'ordre 3 du run (feuille jouee par machine 2 sur BOCAL4), celui que machine 1 rejoue sur les memes
fichiers, et les deux verdicts du lecteur (run, rejeu). Rend : identite des issues, des comptes, des statuts ; plus grands
ecarts de chaine entre machines ; plus petites marges d'un etat juge a une garde et a sa tolerance ; signes ; ordre 3
contre ordre 2 ; etats exclus ; etats hors du domaine.
Usage : python3 -I comparaison_rejeu_machine1_v1.py <verdict_ordre3 du run> <verdict_ordre3 rejoue> <verdict_ter du run>
        <verdict_ter rejoue> <sortie.json>"""
import sys, json, math
RUN, REJ, VRUN, VREJ, SORTIE = sys.argv[1:6]
A = json.load(open(RUN)); B = json.load(open(REJ)); VA = json.load(open(VRUN)); VB = json.load(open(VREJ)); out = {}
def med(v):
    v = sorted(v); n = len(v); return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])
# 1. lecteur : statuts et largeurs de plateau
n = 0; pire = 0.0; memes = True
for pid in VA["points"]:
    ea = {e["rang"]: e for e in VA["points"][pid]["etats"]}; eb = {e["rang"]: e for e in VB["points"][pid]["etats"]}
    memes = memes and sorted(ea) == sorted(eb)
    for r in ea:
        memes = memes and ea[r]["statut"] == eb[r]["statut"]; n += 1
        for x in ea[r]["plateaux"]:
            if "Gamma_pl" in ea[r]["plateaux"][x] and "Gamma_pl" in eb[r]["plateaux"][x]:
                pire = max(pire, abs(ea[r]["plateaux"][x]["Gamma_pl"] / eb[r]["plateaux"][x]["Gamma_pl"] - 1.0))
nq = sum(e["statut"] == "QUALIFIE" for p in VA["points"].values() for e in p["etats"])
print("LECTEUR : %d etats lus, %d QUALIFIES ; memes etats et memes statuts au run et au rejeu : %s ; plus grand ecart relatif d'une largeur de plateau : %.1e ; verdict du lecteur au run : %s" % (
    n, nq, "oui" if memes else "non", pire, VA.get("verdict")))
out["lecteur"] = {"lus": n, "qualifies": nq, "memes_statuts": memes, "pire_ecart_plateau": pire, "verdict": VA.get("verdict"), "instrument": VA.get("instrument")}
# 2. feuille d'ordre 3 : issues, comptes, etat par etat
iss = all(A[k]["issue"] == B[k]["issue"] and A[k]["tombees"] == B[k]["tombees"] for k in ("E1", "E2", "E1B", "E3")); cpt = A["comptes"] == B["comptes"]
ca = {c["id"]: c for c in A["cellules"]}; cb = {c["id"]: c for c in B["cellules"]}; cel = True; p3 = p2 = pe = ps = 0.0; etats = []
for i in ca:
    for k in ("n_lus", "n_juges", "n_domaine", "n_hors", "exploitable", "E1", "E2", "E3", "exclus"):
        cel = cel and ca[i][k] == cb[i][k]
    xa = {e["rang"]: e for e in ca[i]["etats"]}; xb = {e["rang"]: e for e in cb[i]["etats"]}
    for r in xa:
        a, b = xa[r], xb[r]; cel = cel and a["exclu"] == b["exclu"]
        if a["exclu"] is None and b["exclu"] is None:
            cel = cel and a["dans_le_domaine"] == b["dans_le_domaine"]
            p2 = max(p2, abs(a["ln_q2"] - b["ln_q2"])); pe = max(pe, abs(a["e_bord"] - b["e_bord"]))
            if a["ln_q3"] is not None and b["ln_q3"] is not None:
                p3 = max(p3, abs(a["ln_q3"] - b["ln_q3"]))
            if a["stab3"] is not None and b["stab3"] is not None:
                ps = max(ps, abs(a["stab3"] - b["stab3"]))
            etats.append((i, ca[i]["creneau"], ca[i]["delta"], a, b))
print("FEUILLE D'ORDRE 3 : issues du run : E1 %s, E2 %s, E1B %s, E3 %s ; memes issues au rejeu : %s ; memes comptes (%d lus, %d juges, %d du domaine, %d hors) : %s ; memes cellules, exclusions et domaines, etat par etat : %s" % (
    A["E1"]["issue"], A["E2"]["issue"], A["E1B"]["issue"], A["E3"]["issue"], "oui" if iss else "non", A["comptes"]["lus"], A["comptes"]["juges"], A["comptes"]["domaine"], A["comptes"]["hors"], "oui" if cpt else "non", "oui" if cel else "non"))
print("   plus grands ecarts entre machines, sur %d etats juges : ln q3 %.1e ; ln q2 %.1e ; e_bord %.1e ; stabilite %.1e" % (len(etats), p3, p2, pe, ps))
out["feuille"] = {"issues": {k: A[k]["issue"] for k in ("E1", "E2", "E1B", "E3")}, "memes_issues": iss, "memes_comptes": cpt, "memes_etats": cel, "comptes": A["comptes"], "ecart_ln_q3": p3, "ecart_ln_q2": p2,
                  "ecart_e_bord": pe, "ecart_stab": ps}
# 3. marges (lecture du run et lecture du rejeu)
def marges(idx):
    m_T = min((e[idx]["tolerance"] - abs(e[idx]["ln_q3"]), e[0], e[idx]["rang"], e[idx]["n1"], e[idx]["n2"], abs(e[idx]["ln_q3"]), e[idx]["tolerance"]) for e in etats if e[idx]["dans_le_domaine"])
    m_e = min((abs(0.7 - e[idx]["e_bord"]), e[0], e[idx]["rang"]) for e in etats)
    m_s = min((abs(0.05 - e[idx]["stab3"]), e[0], e[idx]["rang"]) for e in etats if e[idx]["stab3"] is not None)
    m_c = min((abs(0.3 - e[idx]["e_bord"]), e[0], e[idx]["rang"]) for e in etats if e[idx]["dans_le_domaine"])
    return m_T, m_e, m_s, m_c
for nom, idx in (("run", 3), ("rejeu", 4)):
    m_T, m_e, m_s, m_c = marges(idx)
    print("MARGES (%s) : a la tolerance, la plus petite : %+.6f a %s rang %d (%d,%d) : |ln q3| = %.6f pour T = %.2f ; a la garde e_bord 0.7 : %.4f (%s rang %d) ; a la garde de stabilite 0.05 : %.4f (%s rang %d) ; a la frontiere e_bord 0.3 des tolerances : %.4f (%s rang %d)" % (
        nom, m_T[0], m_T[1], m_T[2], m_T[3], m_T[4], m_T[5], m_T[6], m_e[0], m_e[1], m_e[2], m_s[0], m_s[1], m_s[2], m_c[0], m_c[1], m_c[2]))
    out["marges_" + nom] = {"tolerance": m_T, "e_bord": m_e, "stabilite": m_s, "classe": m_c}
# 4. par cellule (lecture du run)
print("PAR CELLULE (run) : juges / domaine / hors ; ln q3 du domaine (min, mediane, max) ; ln q2 du domaine (mediane) ; ordre 3 plus pres / domaine ; marge de la cellule a sa tolerance ; e_bord max du domaine ; exclus")
out["cellules"] = []
for i in ca:
    dom = [e[3] for e in etats if e[0] == i and e[3]["dans_le_domaine"]]; hors = [e[3] for e in etats if e[0] == i and not e[3]["dans_le_domaine"]]
    q3 = [e["ln_q3"] for e in dom]; marge = min(e["tolerance"] - abs(e["ln_q3"]) for e in dom)
    r = {"id": i, "juges": len(dom) + len(hors), "domaine": len(dom), "hors": len(hors), "q3_min": min(q3), "q3_med": med(q3), "q3_max": max(q3), "q2_med": med([e["ln_q2"] for e in dom]),
         "plus_pres": sum(e["ordre3_plus_pres"] for e in dom), "marge": marge, "e_bord_max": max(e["e_bord"] for e in dom), "n_neg": sum(x < 0 for x in q3), "n_pos": sum(x > 0 for x in q3),
         "exclus": ca[i]["exclus"], "pire_q2": max(abs(e["ln_q2"]) for e in dom + hors), "bande": ca[i]["bande"],
         "hors_q3_pire": sum(1 for e in hors if e["ln_q3"] is None or abs(e["ln_q3"]) > abs(e["ln_q2"])), "hors_q2_max": max([abs(e["ln_q2"]) for e in hors]) if hors else None,
         "hors_q3_max": max([abs(e["ln_q3"]) for e in hors if e["ln_q3"] is not None]) if hors else None, "au_dela_0603": sum(e["e_bord"] > 0.603 for e in dom)}
    out["cellules"].append(r)
    print("  %-3s %2d / %2d / %2d ; ln q3 %+.4f %+.4f %+.4f ; ln q2 %+.4f ; %2d / %2d ; marge %+.4f ; e_bord max %.3f (au-dela de 0.603 : %d) ; exclus %s%s" % (
        i, r["juges"], r["domaine"], r["hors"], r["q3_min"], r["q3_med"], r["q3_max"], r["q2_med"], r["plus_pres"], r["domaine"], marge, r["e_bord_max"], r["au_dela_0603"], r["exclus"],
        (" ; hors du domaine : ordre 3 plus loin que l'ordre 2 a %d sur %d, |ln q2| max %.3f, |ln q3| max %.3f" % (r["hors_q3_pire"], r["hors"], r["hors_q2_max"], r["hors_q3_max"])) if hors else ""))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True, default=list)
