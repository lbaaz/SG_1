# -*- coding: ascii -*-
# ECRIT L'ACTE DE LA QUALIFICATION E-B (journal_delta_nn_qualification_EB_v1.md).
# Aucun nombre MESURE et aucun canon n'est tape : les nombres sont relus des
# pieces citees, les statuts sont ceux que rend la feuille de lecture certifiee
# (b3ac958a1a2b915b) rejouee ici, et chaque canon tape est un ATTENDU affirme
# contre le canon recalcule du fichier. Le texte (prose, seuils du gel, noms)
# est de la plume.
# Arguments : <pieces m1> <racine des recus> <clone du registre> <journal du
#             rejeu ponctuel> <sortie>
import sys, os, json, re, hashlib, unicodedata, importlib.util, textwrap

W, RECU, REG, REJEU, SORTIE = sys.argv[1:6]
V = {}


def cB(chemin):
    o = open(chemin, "rb").read()
    t = unicodedata.normalize("NFC", o.decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


NUIT = RECU + "/recu_nuit1/nuit_EB_etage1"
REF = RECU + "/recu_m2_ref"
PIECES = [  # (cle, chemin, canon attendu ou None)
    ("moteur", REG + "/scripts/m17_chaine_v17.py", "82a0be882568fe0c"),
    ("gel_m17", REG + "/gels/m17_pre_enregistrement_quantique_v12_b2.md", "20950e52e7d63225"),
    ("man_run", REG + "/journal/manche_m17_v17_MANIFEST_machine2.txt", "4aecd0e2b23bc818"),
    ("acte93", REG + "/journal/journal_delta_93_constante_A_mesure_v2.md", "bd043b738d0f9d39"),
    ("predecl", W + "/lot/lecture_predeclaree_piste0_etape0_machine1_v1.md", "20cbc762d58ce1ca"),
    ("e0_json", W + "/lot/lecture_piste0_etape0_machine1_v2.json", "37169cd7d595c575"),
    ("note_e0", W + "/lot/note_machine1_piste0_etape0_v1.md", "2d246b2a5c60c244"),
    ("gel_v1", W + "/qualification_EB_pre_enregistrement_v1.md", "8603af9d4f63e9dc"),
    ("gel_v2", W + "/qualification_EB_pre_enregistrement_v2.md", "cde0cd11a763f26d"),
    ("constr_gel", W + "/construction_gel_EB_v2_machine1_v1.py", None),
    ("wkb", W + "/estimation_TP_wkb_machine1_v1.py", "3eeb30328f9c542c"),
    ("sonde_v1", W + "/sonde_qualification_EB_machine1_v1.py", "214ea376cbf540a4"),
    ("sonde_v2", W + "/sonde_qualification_EB_machine1_v2.py", "facc7536ba4637cb"),
    ("banc_v1", W + "/banc_qui_tue_qualification_EB_machine1_v1.py", "666e69f11bc1f72c"),
    ("banc_v2", W + "/banc_qui_tue_qualification_EB_machine1_v2.py", "4e46744fe4e8a8be"),
    ("lecture", W + "/lecture_qualification_EB_machine1_v1.py", "b3ac958a1a2b915b"),
    ("constr_sonde", W + "/construction_sonde_banc_v2_machine1_v1.py", None),
    ("fumee", W + "/lot_sonde/fumee/fumee_reelle_39_20.log", None),
    ("prevol_tn", W + "/lot_sonde_v2/prevol_v2/lecture_etage1.log", None),
    ("ref_script", REF + "/reference_TP_rotation_complexe_machine2_v1.py", "5fd3a1897ca0442a"),
    ("ref_jet", REF + "/reference_TP_rotation_complexe_machine2_v1_premier_jet.py", "af73dfe9a648960a"),
    ("ref_liste", REF + "/tp_retenus_machine2_v1.json", "69b3bab3bb8480b7"),
    ("ref_table", REF + "/tp_reference_machine2_v1.json", "4d51dd58ef456fe9"),
    ("ref_calculs", REF + "/tp_reference_machine2_v1_calculs.json", "fe25da36c3ad27fd"),
    ("nuit_json", NUIT + "/sonde_etage1.json", "ab31334aea5c444a"),
    ("nuit_log", NUIT + "/sonde_etage1.log", "edafd162f58f9720"),
    ("nuit_console", NUIT + "/console_etage1.log", "baaccd2b3cad5a5b"),
    ("nuit_verdict", NUIT + "/verdict_etage1.json", "aef856818424689a"),
    ("nuit_lecture", NUIT + "/lecture_etage1.log", "94e008b420e3ba38"),
    ("rejeu", REJEU, None),
    # notes d'echange
    ("n_m2_gel1", RECU + "/recu_m2_cert/POUR_MACHINE1_certification_gel_EB_v1_machine2_v1.md", "0d11d6866e3c5f37"),
    ("n_m2_gel2", RECU + "/recu_m2_v2cert/lot_3b388a98d30695e3/POUR_MACHINE1_certification_gel_EB_v2_machine2_v1.md", "a872e3d0e9000222"),
    ("n_m2_sonde1", RECU + "/recu_m2_sonde/POUR_MACHINE1_certification_sonde_EB_v1_machine2_v1.md", None),
    ("n_m2_sonde2", RECU + "/recu_m2_v2cert/POUR_MACHINE1_certification_sonde_EB_v2_machine2_v1.md", None),
    ("n_m2_ref", REF + "/POUR_MACHINE1_reference_TP_machine2_v1.md", "fb72930ce5edb9fa"),
    ("n_m2_nuit", RECU + "/recu_nuit1/POUR_MACHINE1_resultat_etage1_nuit_EB_machine2_v1.md", "d180e7c6eef55ca6"),
    ("n_m1_gel2", W + "/POUR_MACHINE2_reponse_certification_gel_EB_v1_machine1_v1.md", "5bb8b9c40549fa62"),
    ("n_m1_sonde1", W + "/POUR_MACHINE2_sonde_EB_v1_machine1_v1.md", "9eafade05b150c7b"),
    ("n_m1_sonde2", W + "/POUR_MACHINE2_sonde_EB_v2_machine1_v1.md", "fc80b132e4d2ce9d"),
    ("n_m1_ref", RECU + "/cert_ref/POUR_MACHINE2_certification_reference_TP_machine1_v1.md", "0426e04ffcbcb953"),
    # lots, par leur manifeste
    ("lot_e0", W + "/lot/MANIFEST_lot_machine1_piste0_etape0_v1.txt", "94c3749c83d4b044"),
    ("lot_cert_gel1", RECU + "/recu_m2_cert/MANIFEST_lot_machine2_certification_gel_EB_v1_v1.txt", "113e5b84238203de"),
    ("lot_gel2", W + "/lot_v2/MANIFEST_lot_machine1_gel_EB_v2_v1.txt", "6bea6ffe7db2b272"),
    ("lot_cert_gel2", RECU + "/recu_m2_v2cert/lot_3b388a98d30695e3/MANIFEST_lot_machine2_certification_gel_EB_v2_v1.txt", "3b388a98d30695e3"),
    ("lot_sonde1", W + "/lot_sonde/MANIFEST_lot_machine1_sonde_EB_v1_v1.txt", "c294e7d5a2e8865a"),
    ("lot_cert_sonde1", RECU + "/recu_m2_sonde/MANIFEST_lot_machine2_certification_sonde_EB_v1_v1.txt", "123880c93b810d35"),
    ("lot_sonde2", W + "/lot_sonde_v2/MANIFEST_lot_machine1_sonde_EB_v2_v1.txt", "413d6ee565697278"),
    ("lot_cert_sonde2", RECU + "/recu_m2_v2cert/MANIFEST_lot_machine2_certification_sonde_EB_v2_v1.txt", "6bed68e12ec21e18"),
    ("lot_ref", REF + "/MANIFEST_lot_machine2_reference_TP_v1.txt", "a6c9daf3f3da3e41"),
    ("lot_cert_ref", RECU + "/cert_ref/lot_cert/MANIFEST_lot_machine1_certification_reference_TP_v1.txt", "7b64b1b7d86c0591"),
    ("lot_nuit", RECU + "/recu_nuit1/MANIFEST_lot_machine2_resultat_etage1_nuit_EB_v1.txt", "72f65ad8a898fbb5"),
]
for cle, chemin, att in PIECES:
    c = cB(chemin)
    assert att is None or c == att, "canon : %s rend %s, attendu %s" % (chemin, c, att)
    V["c_" + cle] = c
print("canons relus : %d, dont %d affirmes contre un attendu" % (
    len(PIECES), sum(1 for p in PIECES if p[2])))

# ---------------------------------------------------------------- la nuit, par la feuille certifiee
s1 = json.load(open(NUIT + "/sonde_etage1.json"))
vm2 = json.load(open(NUIT + "/verdict_etage1.json"))
ref = json.load(open(REF + "/tp_reference_machine2_v1.json"))
spec = importlib.util.spec_from_file_location("lec", W + "/lecture_qualification_EB_machine1_v1.py")
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
so = sys.stdout
sys.stdout = open(os.devnull, "w")
try:
    verdict, motifs, det = L.juger_etage1(s1, ref)
    okst, TS = L.selftest()
    jg = L.selection_gel(ref["balayage"])
finally:
    sys.stdout = so
assert verdict == vm2["etage1"] == "NE TIENT PAS" and motifs == vm2["motifs"], (verdict, motifs)
assert json.dumps(det, sort_keys=True) == json.dumps(vm2["detail"], sort_keys=True), "detail feuille m1 != m2"
assert s1["gel"] == V["c_gel_v2"] and s1["moteur"] == V["c_moteur"]
assert s1["prevol"] is False and s1["mutation"] is None and s1["GQ10"] is True
assert vm2["canon_sonde_etage1"] == V["c_nuit_json"] and vm2["canon_reference"] == V["c_ref_table"]
assert all(s1["GQ3"].values()) and len(s1["GQ3"]) == 6
for cle in s1["TP"]:
    for cfg in s1["TP"][cle]["traj"]:
        for rec in s1["TP"][cle]["traj"][cfg].values():
            assert rec["identite_reprise"]["sonde"] == V["c_sonde_v2"]
V["verdict1"] = verdict
V["motifs"] = " ; ".join("'%s'" % m for m in motifs)
V["cascade"] = L.cascade(vm2, None, {})
assert V["cascade"] == "NON CONCLUANT D'INSTRUMENT"
assert okst
V["selftest"] = "%d tenus sur %d" % (sum(1 for x in TS if x[1]), len(TS))
js = sorted(v["j"] for v in s1["TP"].values())
jr = sorted(r["j"] for r in ref["retenus"])
assert js == jr == jg == [6, 8], (js, jr, jg)
V["selection"] = str(js)
con = open(NUIT + "/console_etage1.log", encoding="utf-8").read()
m = re.search(r"CODE DE SORTIE ETAGE 1 = (\d+)\s*\n\w+ +\w+ +(\d+) +(\d\d):(\d\d):\d\d +(\d{4})", con)
assert m and m.group(1) == "0" and (m.group(2), m.group(5)) == ("12", "2026")
V["code"], V["fin"] = m.group(1), "%sh%s" % (m.group(3), m.group(4))
pf = s1["plateforme"]
V["plat"] = "%s %s, python %s, numpy %s" % (pf["systeme"], pf["machine"], pf["python"], pf["numpy"])
assert pf["temoin_lecture"] == "CR"
pl = [abs(x) for d in s1["GQ5"].values() for x in d.values()]
V["plancher"], V["n_plancher"] = "%.3e" % max(pl), "%d" % len(pl)
c = s1["comptes"]
assert c["TP"]["repris"] == c["TN"]["repris"] == c["plancher"]["repris"] == 0
V["tp_joues"], V["pl_joues"] = "%d" % c["TP"]["joues"], "%d" % c["plancher"]["joues"]
V["tn_joues"], V["tn_sautes"] = "%d" % c["TN"]["joues"], "%d" % c["TN"]["sautes"]
V["joues"] = "%d" % (c["TP"]["joues"] + c["plancher"]["joues"] + c["TN"]["joues"])
assert c["TP"]["joues"] + c["plancher"]["joues"] + c["TN"]["joues"] + c["TN"]["sautes"] == 105
assert s1["hors_manifeste"] == ["pt_39_20_f100.zip"]

bal = {r["j"]: r for r in ref["balayage"]}
MOTS = {2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 9: "neuf"}
CFG = (("F1G20", "G20"), ("F1G30", "G30"))
SER, REL = {}, {}
bloc_tp, tab_a, tab_b, bloc_pal, bloc_pas, bloc_gl = [], [], [], [], [], []
k3, km2, gl_dev, asym = [], [], [], []
for cle, j in (("j06", 6), ("j08", 8)):
    r = bal[j]
    assert s1["TP"][cle]["g"] == r["g"]
    bloc_tp.append("  j = %d, g = %.5f, Gamma_ref %.4e, u_ref %.1e, tau_TP = tau + u_ref = %.4f" % (
        j, r["g"], r["Gamma_ref"], r["u_ref"], 0.05 + r["u_ref"]))
    for cfg, g in CFG:
        tr = s1["TP"][cle]["traj"][cfg]
        assert sorted(int(k) for k in tr) == list(range(-2, 13))
        ser = L.serie(tr)
        for k, x in ser.items():          # un "non lisible" du temoin = sous le plancher, suivi tenu
            if x is None:
                e = tr[str(k)]["etats"][0]
                assert e["suivi"] and e["gamma"] <= 1e-12
        rel = {k: (ser[k] / r["Gamma_ref"] if ser[k] is not None else None) for k in ser}
        SER[(j, g)], REL[(j, g)] = ser, rel
        p = det["TP"][cle][cfg]
        if p["statut"] == "PLATEAU":
            assert p["tient"]
            bloc_tp.append("    %s : PLATEAU, k0 = %d, Gamma_pl %.4e, etalement %.4f, |ln| = %.4f"
                           "    -> TIENT" % (g, p["k0"], p["Gamma_pl"], p["etalement"], p["ecart_ln"]))
            V["pc_%s_%s" % (cle, g)] = "%.1f" % (100.0 * p["ecart_ln"])
            V["etal_%s_%s" % (cle, g)] = "%.4f" % p["etalement"]
        else:
            assert p["statut"] == "PAS DE PLATEAU" and not p["tient"]
            bloc_tp.append("    %s : PAS DE PLATEAU ; meilleure fenetre de cinq k0 = %d, etalement"
                           " %.4f     -> NE TIENT PAS" % (g, p["k0"], p["etalement"]))
            V["etal_%s_%s" % (cle, g)] = "%.4f" % p["etalement"]
        f = lambda k: ("%6.3f" % rel[k]) if rel[k] is not None else "   -  "
        tab_a.append(("    j = %d  %s      %s" % (j, g, " ".join(f(k) for k in range(-2, 6)))).rstrip())
        tab_b.append(("    j = %d  %s      %s" % (j, g, " ".join(f(k) for k in range(6, 13)))).rstrip())
        # plus longue suite de valeurs consecutives a 5 pour cent pres (lecture apres coup)
        ks = sorted(ser)
        best = (0, None, None)
        for a in range(len(ks)):
            for b in range(a, len(ks)):
                v = [ser[k] for k in ks[a:b + 1]]
                if all(x is not None for x in v) and max(v) <= 1.05 * min(v) and b - a + 1 > best[0]:
                    best = (b - a + 1, (ks[a], ks[b]), max(v) / min(v) - 1.0)
        assert best[1][0] == -2
        bloc_pal.append("      j = %d  %s : %s valeurs, k = %d a %d, etalement %.4f" % (
            j, g, MOTS[best[0]], best[1][0], best[1][1], best[2]))
        V["n_%s_%s" % (cle, g)] = MOTS[best[0]]
        k3.append(rel[3])
        km2.append(abs(rel[-2] - 1.0))
        # pas de descente, convention du moteur : |G_k - G_(k-1)| / G_(k-1)
        pas = {k: abs(ser[k] - ser[k - 1]) / ser[k - 1] for k in ks[1:]
               if ser[k] is not None and ser[k - 1] is not None}
        acc = pas[2] < 0.05 and pas[3] < 0.05
        assert not acc
        bloc_pas.append("      j = %d  %s : pas %.3f, %.3f, %.3f    -> REFUSE" % (j, g, pas[1], pas[2], pas[3]))
        gl = [k for k in range(0, 13) if k in pas and (k - 1) in pas and pas[k] < 0.05 and pas[k - 1] < 0.05]
        gl_dev += [abs(rel[k] - 1.0) for k in gl]
        bloc_gl.append("      j = %d  %s : accepte k = %s  (Gamma / Gamma_ref : %s)" % (
            j, g, ", ".join("%d" % k for k in gl), ", ".join("%.3f" % rel[k] for k in gl)))
        asym += [ser[k + 1] / ser[k] for k in range(8, 12) if ser[k + 1] is not None and ser[k] is not None]
        if (j, g) == (6, "G30"):
            kb = max((k for k in rel if rel[k] is not None), key=lambda k: rel[k])
            V["bosse"], V["bosse_k"] = "%.2f" % rel[kb], "%d" % kb
entete_a = "    %-16s" % "k =" + " ".join("%6d" % k for k in range(-2, 6))
entete_b = "    %-16s" % "k =" + " ".join("%6d" % k for k in range(6, 13))
V["bloc_tp"] = "\n".join(bloc_tp)
V["bloc_tab"] = "\n".join([entete_a] + tab_a + [entete_b] + tab_b)
V["bloc_pal"] = "\n".join(bloc_pal)
V["bloc_pas"] = "\n".join(bloc_pas)
V["bloc_gl"] = "\n".join(bloc_gl)
V["km2_max"] = "%.1f" % (100.0 * max(km2))
V["k3_min"], V["k3_max"] = "%.2f" % min(k3), "%.2f" % max(k3)
V["k3_liste"] = ", ".join("%.3f" % x for x in k3)
V["gl_max"] = "%.1f" % (100.0 * max(gl_dev))
V["asym_min"], V["asym_max"] = "%.3f" % min(asym), "%.3f" % max(asym)
V["uref_j06_pc"] = "%.1f" % (100.0 * bal[6]["u_ref"])
V["gref_j06"], V["gref_j08"] = "%.3e" % bal[6]["Gamma_ref"], "%.3e" % bal[8]["Gamma_ref"]
dur = {g: [rec["duree_s"] for cle in s1["TP"] for rec in s1["TP"][cle]["traj"][cfg].values()] for cfg, g in CFG}
V["dur60"], V["dur70"] = "%.0f" % (sum(dur["G20"]) / len(dur["G20"])), "%.0f" % (sum(dur["G30"]) / len(dur["G30"]))

# ---------------------------------------------------------------- le temoin negatif
tn = s1["TN"]
assert det["TN"] == "NON JOUE"
assert sorted(k for k, r in tn["traj"].items() if not r["saute"]) == ["2", "3", "4"]
assert sum(1 for r in tn["traj"].values() if r["saute"]) == c["TN"]["sautes"] == 12
V["tn_cands"] = ", ".join("(%d, %d)" % tuple(x) for x in tn["candidats"])
V["tn_g3"] = ", ".join("%.3f" % e["gamma"] for e in tn["traj"]["3"]["etats"])
ov = [e["ov"] for k in ("2", "4") for e in tn["traj"][k]["etats"]]
assert all(o is not None and o < 0.90 for o in ov) and not any(
    e["suivi"] for k in ("2", "4") for e in tn["traj"][k]["etats"])
V["tn_ov_min"], V["tn_ov_max"] = "%.3f" % min(ov), "%.3f" % max(ov)
pv = open(W + "/lot_sonde_v2/prevol_v2/lecture_etage1.log", encoding="utf-8").read()
m = re.search(r"TN candidat 0 \[(\d+), (\d+)\] : PAS DE PLATEAU \(etalement ([0-9.]+)\)\nTN : PAS DE PLATEAU", pv)
assert m
V["tn_prevol"] = "(%s, %s), etalement %s" % m.groups()
for cfg, cle in (("F1G20", "pv_e20"), ("F1G30", "pv_e30")):
    m = re.search(r"TP j08 g = 0\.10000 %s : PAS DE PLATEAU Gamma_pl \S+ etalement ([0-9.]+) " % cfg, pv)
    V[cle] = "%.1f" % float(m.group(1))
assert "'G-Q5', 'TP ne tient pas a j08'" in pv and "PRE-VOL : geometrie reduite" in pv
sl = open(NUIT + "/sonde_etage1.log", encoding="utf-8").read()
assert "G-Q1 moteur m17_chaine_v17.py canon 82a0be882568fe0c : OK" in sl
assert "G-Q2 run : 36 au canon et a la taille == 36 lignes du manifeste (attendu 36)" in sl
mr = open(REG + "/journal/manche_m17_v17_MANIFEST_machine2.txt", encoding="utf-8").read()
assert len(re.findall(r"(?m)^[0-9a-f]{16} ", mr)) == 36

# ---------------------------------------------------------------- l'etape 0
e0 = json.load(open(W + "/lot/lecture_piste0_etape0_machine1_v2.json"))
PT = ["1.95", "1.97", "1.98", "2.02", "2.03", "2.05"]
pts = e0["points"]
G = [pts[w]["G"] for w in PT]
V["grun"] = ", ".join("%.3e" % x for x in G)
V["grun_min"], V["grun_max"] = "%.3e" % min(G), "%.3e" % max(G)
V["E_run"] = "%.4f" % e0["L1"]["E"]
assert e0["L1"]["tient"] and not e0["L2_L3"]["L2"] and e0["L2_L3"]["L3"]
assert not e0["L4"]["tient"] and not e0["L5"]["tient"]
V["B_max"] = "%.4f" % max(e0["L1"]["B"].values())
V["rho"] = e0["L4"]["rho_G_Gp"]
q = [pts[w]["q"] for w in PT]
V["q_min"], V["q_max"] = "%.1e" % min(q), "%.1e" % max(q)
V["signes"] = " ".join("%s:%+d" % (w, e0["L5"]["signes"][w]) for w in PT)
V["r_202"] = "%.2f" % pts["2.02"]["r"]
Wg, Wd = [pts[w]["W"] for w in PT[:3]], [pts[w]["W"] for w in PT[3:]]
rg, rd = [pts[w]["rec"] for w in PT[:3]], [pts[w]["rec"] for w in PT[3:]]
V["W_g"] = "%.3f a %.3f" % (min(Wg), max(Wg))
V["W_d"] = "%.3f" % min(Wd)
assert "%.3f" % min(Wd) == "%.3f" % max(Wd)
V["rec_g"] = "%.2f a %.2f" % (100 * min(rg), 100 * max(rg))
V["rec_d"] = "%.2f a %.2f" % (100 * min(rd), 100 * max(rd))
assert [pts[w]["r_c"] for w in PT] == [40, 40, 40, 41, 41, 41]
pm17 = [x for w in PT for x in pts[w]["essais"][0]["pas"][1:]]
assert all(pts[w]["essais"][0]["accepte"] and pts[w]["essais"][0]["L"] == 20 for w in PT)
V["pas_m17_max"] = "%.4f" % max(pm17)

# ---------------------------------------------------------------- la reference : bord et limite
V["u5"] = "%.9f" % bal[5]["u_ref"]
V["u5_dep"] = "%.2e" % (bal[5]["u_ref"] - 0.01)
V["g5"] = "%.3e" % bal[5]["Gamma_ref"]
sous = sorted(bal[6]["Gamma_ref"] / x for x in G if x < bal[6]["Gamma_ref"])
assert len(sous) == 5 and sum(1 for x in G if bal[6]["Gamma_ref"] < x < bal[8]["Gamma_ref"]) == 1
V["r_sous_min"], V["r_sous_max"] = "%.1f" % sous[0], "%.1f" % sous[-1]
raf = sum(1 for r in ref["balayage"] if r["raffine"])
assert (raf, len(ref["balayage"])) == (11, 17)
V["o_j06"], V["o_j08"], V["o_min"] = "%.0e" % bal[6]["Gamma_ref"], "%.0e" % bal[8]["Gamma_ref"], "%.0e" % min(G)

# ---------------------------------------------------------------- phrases reprises des notes citees
def plat(chemin):
    return " ".join(open(chemin, encoding="utf-8").read().replace("**", "").split())


CIT = [
    (RECU + "/recu_m2_cert/POUR_MACHINE1_certification_gel_EB_v1_machine2_v1.md", ["21 controles, 2 morsures"]),
    (RECU + "/recu_m2_v2cert/lot_3b388a98d30695e3/POUR_MACHINE1_certification_gel_EB_v2_machine2_v1.md",
     ["11 controles, 0 morsures", "48748 o", "par 18 remplacements a ancre unique"]),
    (RECU + "/recu_m2_sonde/POUR_MACHINE1_certification_sonde_EB_v1_machine2_v1.md", ["13 controles, 3 morsures"]),
    (RECU + "/recu_m2_v2cert/POUR_MACHINE1_certification_sonde_EB_v2_machine2_v1.md",
     ["16 controles, 0 morsures", "Quatre attaques", "Sept cas"]),
    (RECU + "/cert_ref/POUR_MACHINE2_certification_reference_TP_machine1_v1.md",
     ["23 controles, 0 morsure", "171 points", "13 points par raffine, pas 15"]),
    (RECU + "/recu_nuit1/POUR_MACHINE1_resultat_etage1_nuit_EB_machine2_v1.md", ["03h00 -> 04h15"]),
    (RECU + "/recu_nuit1/MANIFEST_lot_machine2_resultat_etage1_nuit_EB_v1.txt", ["279 fichiers de reprise"]),
    (W + "/qualification_EB_pre_enregistrement_v2.md", ["le decompte passe de 540 a 555"]),
    (REF + "/POUR_MACHINE1_reference_TP_machine2_v1.md", ["149 points"]),
    (RECU + "/recu_m2_sonde/POUR_MACHINE1_certification_sonde_EB_v1_machine2_v1.md", ["AU BIT sur G_run a BOCAL4"]),
    (RECU + "/recu_m2_v2cert/POUR_MACHINE1_certification_sonde_EB_v2_machine2_v1.md",
     ["retombe AU BIT sur G_run", "6 mordues sur 6, base saine, 4 refus sur 4"]),
    (RECU + "/recu_nuit1/POUR_MACHINE1_resultat_etage1_nuit_EB_machine2_v1.md",
     ["ce qui manque est la LONGUEUR du plateau", "Je ne tire de cela aucune correction"]),
    (W + "/lot/note_machine1_piste0_etape0_v1.md", ["36 pieces au canon et a la taille"]),
    (W + "/qualification_EB_pre_enregistrement_v2.md", ["quatre demandes"]),
]
for chemin, phrases in CIT:
    t = plat(chemin)
    for ph in phrases:
        assert ph in t, "phrase absente de %s : %s" % (os.path.basename(chemin), ph)
for d, _, fs in os.walk(RECU + "/recu_nuit1"):          # la detention de 7b64... n'est attestee nulle part
    for f in fs:
        assert b"7b64b1b7d86c0591" not in open(os.path.join(d, f), "rb").read()

# ---------------------------------------------------------------- fumee (D-QEB-1) et rejeu ponctuel
fu = open(W + "/lot_sonde/fumee/fumee_reelle_39_20.log", encoding="utf-8").read()
m = re.search(r"rapport - 1 = (\S+) ;", fu)
V["fumee_ecart"] = m.group(1)
rj = open(REJEU, encoding="ascii").read()
assert rj.rstrip().endswith("-- FIN rejeu_ponctuel_TP_machine1_v1 --") and rj.count("\nTP j") == 6
V["rejeu_pire"] = re.search(r"pire ecart relatif m1/m2 sur les six : (\S+)", rj).group(1)
V["rejeu_plat"] = re.search(r"plateforme : (.*)", rj).group(1)

# ================================================================= LE TEXTE
OUT = []


def T(*lignes):
    for l in lignes:
        OUT.extend(l.format(**V).split("\n"))


def P(txt, ind=2, suite=None):
    suite = ind if suite is None else suite
    t = " ".join(txt.split()).format(**V)
    for ponct in (":", ";", "?"):                    # pas de ponctuation double en tete de ligne
        t = t.replace(" " + ponct, "\x00" + ponct)
    OUT.extend(l.replace("\x00", " ") for l in textwrap.wrap(
        t, width=99, initial_indent=" " * ind, subsequent_indent=" " * suite,
        break_long_words=False, break_on_hyphens=False))


def PIECE(nom, cle, desc=""):
    OUT.append("    %s  %s" % (nom, V[cle]))
    if desc:
        P(desc, ind=8)


T("JOURNAL DELTA nn -- LA QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS) REND \"NON CONCLUANT",
  "D'INSTRUMENT\" : A L'ETAGE 1 DU GEL v2, JOUE LE 12/11 SUR BOCAL4, LE TEMOIN POSITIF (JUMEAU H+,",
  "LARGEUR CONNUE PAR ROTATION COMPLEXE) TIENT A L'ABSORBEUR LONG (PLATEAU, ACCORD A {pc_j06_G30} ET",
  "{pc_j08_G30} POUR CENT) ET NE TIENT PAS A L'ABSORBEUR COURT (PAS DE PLATEAU DE CINQ VALEURS), AUX DEUX",
  "COUPLAGES RETENUS ; LE GEL EXIGE LES DEUX ; L'ETAGE 2 N'EST PAS JOUE, LE FANTOME N'EST PAS LU,",
  "RIEN N'EST DIT DES LARGEURS DE M17 ; L'ECHELLE EN eta DU GEL NE COUVRE LE PLATEAU DU TEMOIN QUE",
  "PAR SON BORD FORT -- DEFAUT DE CONCEPTION DE LA PLUME (MACHINE 1), VERSE ; LE TEMOIN NEGATIF",
  "N'EST PAS JOUABLE A TAILLE REELLE ; SOUS CE GEL, LE CHANTIER S'ARRETE ICI",
  "(redaction machine 1, contreseing machine 2, depot operateur, 2026-11-12) -- PROJET, VERSION 1",
  "=======================================================================")
P("""S'insere apres le delta 93 (2ec6775, journal_delta_93_constante_A_mesure_v2.md {c_acte93}).
Numero pris au depot (E18) ; "nn" dans le corps. Rien de ce qui est cite n'est edite (PB-1) ; les
pieces se citent par leur canon (convention B, sha256 NFC+LF, 16 hex), les lots par leur ligne
CANON. Ce delta ne prend aucun numero de serie, ne recommande aucun delta, n'adopte aucune regle.
Les nombres mesures et les canons de ce texte ne sont pas tapes : ils sont poses par
ecrire_acte_qualification_EB_machine1_v1.py depuis les pieces de nn.1, et les statuts sont ceux
que rend la feuille de lecture certifiee, rejouee a l'ecriture.""", ind=0)
T("", "nn.0 POSITION EN TROIS PHRASES")
P("""La manche M17 (deltas 80 a 83) a lu six largeurs quantiques par l'estimateur E-B -- Gamma_LS,
absorbeur complexe, lu a eta0/8 -- et la piste (0) demandait si cette largeur est une largeur
sortante intrinseque ou si elle depend de la facon d'absorber ; l'etape 0, lecture du run sans
aucun calcul neuf, a montre que les pieces du run ne le tranchent pas (nn.2), d'ou un banc de
qualification : gel v2, sonde, feuille de lecture et banc qui tue de machine 1, certifies par
machine 2 ; reference du temoin positif de machine 2, par rotation complexe, certifiee par
machine 1. La nuit du 12/11 a joue l'etage 1 : le temoin positif tient a G30 et ne tient pas a
G20, aux deux couplages retenus ; la feuille rend {verdict1}, la cascade {cascade}, et l'etage
2 n'est pas joue -- le fantome n'est pas lu, il n'est ni qualifie ni disqualifie. Ce que la nuit
apprend hors verdict, ecrit ici comme lecture apres coup et rien de plus : au bord fort de
l'echelle l'absorbeur rend la largeur connue a {km2_max} pour cent pres, aux deux longueurs et aux
deux couplages, et au barreau k = 3 -- l'indice auquel M17 lit ses points -- le meme instrument
rend {k3_min} a {k3_max} fois cette largeur selon la longueur et le couplage ; l'echelle du gel,
posee autour du reglage de M17, ne couvrait le plateau du temoin que par son bord, et c'est la
plume du gel qui l'a posee ainsi.""")

T("", "nn.1 PIECES CITEES (convention B ; \"au registre\" = dans l'arbre a 2ec6775, delta 93 ; detention",
  "     declaree en fin de section)",
  "  Au registre :")
PIECE("scripts/m17_chaine_v17.py", "c_moteur", "le moteur v17 (G-Q1)")
PIECE("gels/m17_pre_enregistrement_quantique_v12_b2.md", "c_gel_m17", "le gel de M17")
PIECE("journal/manche_m17_v17_MANIFEST_machine2.txt", "c_man_run",
      "manifeste du run M17, 36 lignes ; des 36 pieces, seul l'assemblage est au registre")
T("  L'etape 0 (machine 1, classe 3, zero run ; lot {c_lot_e0}) :")
PIECE("lecture_predeclaree_piste0_etape0_machine1_v1.md", "c_predecl",
      "ecrite et empreintee avant l'ouverture des points")
PIECE("lecture_piste0_etape0_machine1_v2.json", "c_e0_json", "la lecture ; source des nombres de nn.2")
PIECE("note_machine1_piste0_etape0_v1.md", "c_note_e0")
T("  Le gel :")
PIECE("qualification_EB_pre_enregistrement_v1.md", "c_gel_v1",
      """NON CERTIFIE en l'etat : machine 2, lot {c_lot_cert_gel1}, note {c_n_m2_gel1}, 21 controles,
      2 morsures de description, quatre demandes""")
PIECE("qualification_EB_pre_enregistrement_v2.md", "c_gel_v2",
      """LE GEL DE CE CHANTIER ; = v1 + 18 remplacements a ancre unique (construction {c_constr_gel}),
      lot {c_lot_gel2}, note {c_n_m1_gel2} ; c'est LE tour de correction de sa section 12 ; CERTIFIE
      par machine 2, lot {c_lot_cert_gel2}, note {c_n_m2_gel2}, 11 controles, 0 morsure, sous deux
      reserves de lecture R-1 et R-2, levees ensuite par le code de la sonde""")
PIECE("estimation_TP_wkb_machine1_v1.py", "c_wkb", "estimation de plume, non opposable")
T("  L'instrument (machine 1) :")
PIECE("sonde_qualification_EB_machine1_v1.py", "c_sonde_v1", "NON CERTIFIEE (D-1, D-2)")
PIECE("sonde_qualification_EB_machine1_v2.py", "c_sonde_v2", "CERTIFIEE ; elle mesure et ne juge pas")
PIECE("banc_qui_tue_qualification_EB_machine1_v1.py", "c_banc_v1", "NON CERTIFIE (D-3)")
PIECE("banc_qui_tue_qualification_EB_machine1_v2.py", "c_banc_v2",
      "CERTIFIE ; six mutations, quatre temoins de refus")
PIECE("lecture_qualification_EB_machine1_v1.py", "c_lecture",
      "CERTIFIEE des le v1, inchangee a l'octet ; elle juge et ne mesure pas")
PIECE("construction_sonde_banc_v2_machine1_v1.py", "c_constr_sonde",
      "construit les v2 depuis les v1 par remplacements a ancre unique")
P("""Les v1 : lot {c_lot_sonde1}, note {c_n_m1_sonde1} ; machine 2, lot {c_lot_cert_sonde1}, note
{c_n_m2_sonde1}, 13 controles, 3 morsures de code -- la feuille certifiee, la sonde et le banc
refuses. Les v2 : lot {c_lot_sonde2}, note {c_n_m1_sonde2} ; machine 2, lot {c_lot_cert_sonde2},
note {c_n_m2_sonde2}, 16 controles, 0 morsure -- certifies.""", ind=4)
T("  La reference du temoin positif (machine 2) :")
PIECE("reference_TP_rotation_complexe_machine2_v1.py", "c_ref_script",
      "aucun absorbeur ; premier jet {c_ref_jet}, conserve (nn.8)")
PIECE("tp_retenus_machine2_v1.json", "c_ref_liste",
      "la liste (j, g), sans aucune largeur : seule piece de la reference que lit la sonde")
PIECE("tp_reference_machine2_v1.json", "c_ref_table", "la table : seule la feuille de lecture l'ouvre")
PIECE("tp_reference_machine2_v1_calculs.json", "c_ref_calculs", "les points bruts")
P("""Lot {c_lot_ref}, note {c_n_m2_ref}. CERTIFIEE par machine 1 : lot {c_lot_cert_ref}, note
{c_n_m1_ref}, 23 controles, 0 morsure, la formule recodee de zero.""", ind=4)
T("  La nuit (machine 2, BOCAL4 ; lot {c_lot_nuit}) :")
PIECE("nuit_EB_etage1/sonde_etage1.json", "c_nuit_json", "la sortie de la sonde ; source des nombres de nn.5 et nn.6")
PIECE("nuit_EB_etage1/sonde_etage1.log", "c_nuit_log")
PIECE("nuit_EB_etage1/console_etage1.log", "c_nuit_console", "code de sortie et heure de fin")
PIECE("nuit_EB_etage1/verdict_etage1.json", "c_nuit_verdict", "le verdict de la feuille, joue par machine 2")
PIECE("nuit_EB_etage1/lecture_etage1.log", "c_nuit_lecture")
PIECE("POUR_MACHINE1_resultat_etage1_nuit_EB_machine2_v1.md", "c_n_m2_nuit")
P("""Detention. Tout ce qui precede est detenu par les deux machines a la date de l'acte, par les
lots echanges (nn.12), sauf : les 279 fichiers de reprise de la nuit, a machine 2 seule, leur
contenu utile etant consolide dans sonde_etage1.json ; et la certification de la reference par
machine 1 (lot {c_lot_cert_ref}), transmise par l'operateur, dont aucune piece de machine 2 ne
porte encore le canon -- au contresignataire de dire s'il la detient. Le run M17 : original a
BOCAL4, copie de machine 1 par l'archive de transport (48748 o, hors manifeste, ni ouverte ni
comptee par la sonde : G-Q2). Rien de ce chantier n'est au registre.""")

T("", "nn.2 CE QUI A MENE AU BANC : L'ETAPE 0 (lecture a zero run des pieces de M17, classe 3)")
P("""Machine 1 a lu les six points f070 du run sous une lecture pre-declaree, 36 pieces sur 36 au
canon du manifeste. Largeurs lues par M17 a eta0/8, de w2 = 1.95 a 2.05 : {grun} ; etendue E_run =
ln(max / min) = {E_run}.""")
P("""L-1 (coherence, non aveugle) TIENT : le budget d'absorbeur des portes du run (translation, N +
p, dernier pas de descente, residu) vaut au plus {B_max} pour un seuil de 0.05. La structure en w2
n'est pas faite par l'absorbeur A L'ECHELLE DES PORTES -- cinq couches, un facteur 8 en eta -- et
cette lecture ne dit rien d'un plateau.""", ind=4, suite=8)
P("""L-2 (aveugle, annoncee 0.5) NE TIENT PAS, L-3 (aveugle, 0.6) TIENT : aucun indicateur d'identite
ni d'absorbeur hors plage a 2.05 ; le pic est sans signature sur ce que le run a stocke.""", ind=4, suite=8)
P("""L-4 (aveugle, 0.4 qu'elle tienne) NE TIENT PAS : rho(Gamma_LS, largeur ponderee) = {rho} contre
29/35, et la largeur ponderee vaut {q_min} a {q_max} fois Gamma_LS. Les deux definitions du taux
portees par le run n'ordonnent pas la grille de la meme facon.""", ind=4, suite=8)
P("""L-5 (aveugle, 0.6) NE TIENT PAS : le signe du dernier pas de descente est mele ({signes} ; 0 =
non defini) ; a 2.02 le rapport des pas vaut {r_202} et Richardson n'est pas defini. Les six
points ne sont pas au meme endroit de leur trajectoire en eta.""", ind=4, suite=8)
P("""Constate hors lectures : deux familles. A gauche de la resonance (1.95, 1.97, 1.98) : poids
total {W_g}, recouvrement de l'etat retenu {rec_g} pour cent, r_c = 40 ; a droite (2.02, 2.03,
2.05) : poids total {W_d}, recouvrement {rec_d} pour cent, r_c = 41.""", ind=4, suite=8)
P("""Ce que l'etape 0 ne pouvait pas dire, et qu'elle avait ecrit avant de lire : ni l'existence
d'un plateau en eta, ni l'effet de la forme, de la longueur ou de la position de l'absorbeur, ni
la justesse de l'instrument sur une largeur connue. C'est la question du banc.""")

T("", "nn.3 LE BANC, TEL QUE GELE (gel v2 {c_gel_v2} ; rappel, le gel fait foi)")
P("""QUESTION : Gamma_LS est-elle independante de la force, de la forme, de la longueur et de la
position de l'absorbeur ? ECHELLE : eta_k = eta0 * 2^(-k), k = -2 a 12, quinze valeurs ; eta0 =
|w2 - 2| aux points, 0.05 au temoin ; M17 lit a k = 3. GEOMETRIES : G20 (N = r_c + 20), G30 (N =
r_c + 30), GT (absorbeur translate de 10) ; formes F1 (native), F2, F3. PLATEAU : une fenetre de
cinq valeurs lisibles a k consecutifs dont le maximum ne depasse pas 21/20 du minimum, en
rationnels exacts ; ACCORD : |ln| <= tau = 0.05 ; lisible : etat suivi par continuite
(recouvrement >= 0.90) et largeur au-dessus du plancher 1e-12.""")
P("""TEMOIN POSITIF : le jumeau H+ du moteur (potentiel x^5, w2 = 39/20), etat du vide ; couplages
g_j = 0.05 * 2^(j/8) ; reference par rotation complexe, a la plume de machine 2 ; RETENUS : les
deux g_j dont la largeur de reference est la plus proche de 1e-10 et de 1e-8, sous u_ref <= 0.01.
TP TIENT si, a chaque g retenu, il y a PLATEAU a G20 ET a G30 et |ln(Gamma_pl / Gamma_ref)| <=
tau + u_ref aux deux. TEMOIN NEGATIF : au point 1.95, un etat loge dans l'absorbeur, qui DOIT
rendre PAS DE PLATEAU ; trois candidats ; trois non lisibles : TN NON JOUE, consigne au verdict.
PLANCHER : |Gamma(H+)| <= 1e-12 aux trente (point, configuration).""")
P("""DECOMPTE : 180 + 180 + 90 + 30 + 60 + 15 = 555 decompositions, dont 105 a l'etage 1 (temoin
positif 60, temoin negatif 15, plancher 30) et 450 a l'etage 2 (les six points). CASCADE, premier
match : 1. NON CONCLUANT D'INSTRUMENT si une garde mord, si le TP ne tient pas ou si le TN rend
PLATEAU -- et alors l'etage 2 n'est pas joue ; 2. ESTIMATEUR QUALIFIE ; 3. QUALIFIE PAR POINT ; 4.
NON QUALIFIE ; 5. NON LISIBLE. GARDE-FOU (section 12, propose par la plume sous le veto de
l'operateur) : un gel, UN tour de correction, un run, un acte ; si le TP ne qualifie pas
l'instrument apres ce tour, on l'ecrit et on s'arrete ; aucun rejeu des donnees du fantome sous
d'autres seuils.""")

T("", "nn.4 CE QUI A ETE JOUE, DANS L'ORDRE, ET E19")
P("""11/11 : etape 0 (machine 1). Gel v1, parti en deux pieces a plat ; machine 2 ne le certifie
pas (E-EB-1, E-EB-2, M-1 a M-4) ; gel v2, tout pris ; machine 2 le certifie. Sonde, feuille et
banc v1 ; machine 2 certifie la feuille, refuse la sonde et le banc sur trois morsures de code
demontrees par rejeu (D-1, D-2, D-3) ; sonde v2 et banc v2 ; machine 2 les certifie apres les
avoir attaques au-dela du banc (quatre attaques de reprise, sept cas de porte). Reference du
temoin par machine 2, onze couplages raffines sur dix-sept, retenus j = 6 et j = 8 ; machine 1 la
certifie, formule recodee sans lire le script de machine 2, table recalculee des points bruts.""")
P("""12/11 : etage 1 sur BOCAL4 ({plat}), de 03h00 (note de machine 2) a {fin} (journal de console),
code de sortie {code} ; {joues} decompositions jouees et {tn_sautes} sautees sur 105, environ
{dur60} s l'une a N = 60 et {dur70} s a N = 70. Lecture par la feuille certifiee, jouee par machine
2 : {verdict1}. L'etage 2 n'est pas lance : la sonde le refuse sans verdict TIENT.""")
P("""Machine 1, a reception : la feuille certifiee rejouee sur la sortie de machine 2 rend le meme
verdict, les memes motifs et le meme detail, a l'egalite du JSON. Hors du perimetre de rejeu
declare au gel, non opposable : six decompositions du temoin (j = 6 et 8, G20, k = -2, 1, 3)
rejouees par un code ecrit pour cela, sans la sonde ni son suivi, sur l'autre plateforme
({rejeu_plat}) : pire ecart relatif a la sonde de machine 2 {rejeu_pire} (journal {c_rejeu}). Le
point 1.95 sur l'echelle entiere, que le gel donnait a rejouer a machine 1, n'est PAS joue :
c'est de la matiere de l'etage 2.""")
P("""E19. Le run de la nuit est joue apres certification croisee du gel, de la sonde, du banc, de la
feuille et de la reference : tenue des deux cotes pour le run. Ce qui a ete calcule avant, et
declare : par machine 2, un essai de formule a un point de l'echelle du temoin (g_8, nomme au gel
v2) et une decomposition d'ancrage au point 1.95 (F1, G20, k = 3), jouee sous la sonde v1 puis
sous la v2, qui retombe au bit sur la largeur du run a BOCAL4 et dont seul le gamma de l'etat
d'ancrage est imprime ; par machine 1, la meme decomposition (ecart au run {fumee_ecart}, autre
plateforme), dont l'impression est la faute D-QEB-1 de nn.8.""")

T("", "nn.5 L'ETAGE 1, AU CHIFFRE (feuille {c_lecture} sur la table {c_ref_table})")
P("""Gardes : G-Q1 moteur au canon ; G-Q2 run 36 au canon et a la taille == 36 lignes du manifeste ;
G-Q3 forme native == moteur, six points sur six ; G-Q5 plancher, {n_plancher} valeurs, max
|Gamma(H+)| = {plancher} contre 1e-12 ; G-Q7 selftest de la feuille, {selftest} ; G-Q10 comptes :
temoin positif {tp_joues} joues, plancher {pl_joues} joues, temoin negatif {tn_joues} joues +
{tn_sautes} sautes == 15 ; selection des couplages : sonde, reference et regle du gel rejouee sur
la table rendent {selection}. Aucune garde ne mord.""")
T("  LE TEMOIN POSITIF :", "{bloc_tp}")
P("""LE TEMOIN NEGATIF : candidats {tn_cands} au point 1.95, (F1, G20). A k = 3, origine du suivi :
Gamma = {tn_g3}. A k = 2 et k = 4 aucun des trois n'est suivi : recouvrements {tn_ov_min} a
{tn_ov_max}, sous le seuil 0.90 ; les douze autres k sont sautes. La feuille lit AUCUNE FENETRE
aux trois et rend TN NON JOUE, consigne au verdict comme le gel le prevoit, sans motif (seul "TN
rend PLATEAU" en leve un).""")
P("""VERDICT DE L'ETAGE 1 : {verdict1}, motifs {motifs}. CASCADE (gel, section 9, rang 1 ; fonction
cascade de la feuille certifiee, appelee a l'ecriture de cet acte sur le verdict de l'etage 1 --
machine 2 ne l'avait pas emise, la commande de l'etage 2 n'ayant pas lieu d'etre jouee) :
{cascade}. Le fantome n'est pas lu.""")
P("""Ce que le gel demande a l'acte dans ce cas (section 13), le meilleur etalement atteint au
temoin : a G30, {etal_j06_G30} (j = 6) et {etal_j08_G30} (j = 8), sous le seuil 0.05, avec un
accord a la reference de {pc_j06_G30} et {pc_j08_G30} pour cent ; a G20, sur la meilleure fenetre
de cinq, {etal_j06_G20} et {etal_j08_G20}.""")

T("", "nn.6 LECTURES APRES COUP DU TEMOIN (aucune n'est pre-enregistree ; aucune n'est un verdict)",
  "  Gamma / Gamma_ref par barreau (Gamma_ref = {gref_j06} a j = 6, {gref_j08} a j = 8 ; \"-\" : sous le",
  "  plancher 1e-12, etat suivi) :",
  "{bloc_tab}")
P("""Lectures de machine 1. Machine 2, dans sa note de la nuit ({c_n_m2_nuit}, section 4), lit de
meme le bord fort et la longueur des paliers, et n'en tire aucune correction.""")
P("""(a) LE BORD FORT. Au barreau le plus fort, k = -2 (eta = 0.2), les quatre trajectoires rendent
la reference a {km2_max} pour cent pres au pire, pour une incertitude de reference de {uref_j06_pc}
pour cent a j = 6. Deux methodes de principe different -- rotation complexe sans absorbeur
(script de machine 2), absorbeur du moteur (sonde de machine 1) -- s'accordent la sur une largeur de {o_j06} et une
de {o_j08}.""", ind=2, suite=6)
P("""(b) LA LONGUEUR DES PALIERS. Plus longue suite de valeurs consecutives a 5 pour cent pres :""",
  ind=2, suite=6)
T("{bloc_pal}")
P("""Toutes commencent au premier barreau de l'echelle : l'echelle ne dit pas si elles continuent
au-dela, du cote fort. A G20 il manque une valeur (j = 6) ou deux (j = 8) pour faire la fenetre de
cinq du gel.""", ind=6)
P("""(c) HORS PALIER. Une fois le palier quitte, la largeur lue est divisee par deux a chaque
barreau (rapports {asym_min} a {asym_max} de k = 8 a 12) : elle est proportionnelle a eta, elle
mesure l'absorbeur et plus le temoin. Au barreau k = 3, Gamma / Gamma_ref vaut {k3_liste} (j = 6
G20, G30 ; j = 8 G20, G30) ; a j = 6, G30, la chute est precedee d'une bosse qui monte a {bosse}
fois la reference (k = {bosse_k}). Rien dans une valeur isolee ne signale l'erreur ; seule la
trajectoire en eta la montre.""", ind=2, suite=6)
P("""(d) LE CRITERE DE DESCENTE DE M17, APPLIQUE AU TEMOIN. Le moteur accepte un point si les deux
derniers des trois pas de descente (eta0 -> eta0/2 -> eta0/4 -> eta0/8, soit k = 0 a 3 ; pas =
|Gamma_k - Gamma_(k-1)| / Gamma_(k-1)) sont sous tau_LS = 0.05, a L = 20 puis a L = 30. Aux six
points de M17 ces deux pas valent au plus {pas_m17_max}. Au temoin, a la meme position :""",
  ind=2, suite=6)
T("{bloc_pas}")
P("""Le critere de M17 aurait donc ARRETE le temoin aux deux longueurs, et n'aurait pas lu la
valeur fausse. Glisse le long de l'echelle (deux pas consecutifs sous 0.05), il n'accepte au
temoin que :""", ind=6)
T("{bloc_gl}")
P("""soit des valeurs a {gl_max} pour cent de la reference au pire. Sur ce temoin, la porte de M17 et
la reference disent la meme chose : la ou la porte passe la largeur est juste a quelques pour
cent, la ou la largeur est fausse la porte refuse. C'est une lecture de quatre trajectoires d'UN
systeme a barriere ; le fantome n'en a pas (gel, section 14), et la porte de M17 n'y est pas
qualifiee pour autant.""", ind=6)
P("""(e) CE QUE LE VERDICT TRANCHE ET NE TRANCHE PAS. La regle du gel, appliquee sans la toucher,
rend {verdict1}, et l'acte ne le discute pas. Mais elle ne distingue pas "le palier de G20 est
plus court que cinq barreaux" de "le palier de G20 est coupe par le bout de l'echelle" : les
valeurs a 5 pour cent sont au bord fort, et l'echelle a deux barreaux plus forts que eta0 pour
douze plus faibles. L'acte ne dit donc pas que l'instrument est faux a G20 ; il dit que le banc,
tel que gele, ne pouvait pas le montrer juste. C'est le defaut D-QEB-2 de nn.8.""", ind=2, suite=6)
P("""(f) LA LIMITE DEJA DECLAREE A LA CERTIFICATION DE LA REFERENCE (O-D). Le temoin le plus bas est
a {gref_j06} ; cinq des six largeurs lues par M17 sont en dessous, d'un facteur {r_sous_min} a
{r_sous_max}. Meme tenu, ce temoin aurait qualifie la chaine de calcul a {o_j06} et {o_j08}, pas a
{o_min}.""", ind=2, suite=6)

T("", "nn.7 ANNONCES (gel, section 11 ; lecture pre-declaree de l'etape 0)")
P("""A-1 (verdict) : l'issue, NON CONCLUANT D'INSTRUMENT, etait annoncee a 0.1 ; la plume avait mis
0.9 sur une lecture du fantome (QUALIFIE PAR POINT 0.5, ESTIMATEUR QUALIFIE 0.3, NON QUALIFIE
0.1). Comptee, non tenue. A-2 et A-3 : non jugeables, l'etage 2 n'etant pas joue. A-4 et A-5 :
non jugeables non plus, et de toute facon non aveugles (D-QEB-1) -- la ligne de machine 2 est
reprise telle quelle : "A-4 et A-5 : non aveugles (D-QEB-1), comptees, non creditees comme
annonces aveugles ; A-1, A-2, A-3 non touchees". Etape 0 : L-3 (0.6) tenue ; L-5 (0.6) et L-2
(0.5) non tenues ; L-4 (annoncee a 0.4 de tenir) non tenue.""")

T("", "nn.8 DEFAUTS ET ERRATA (numeros de chantier ; numeros de serie au depot, E18)")
P("""D-QEB-2 (m1, gel, conception ; NOUVEAU). L'echelle en eta a ete posee autour du reglage de
M17 et prolongee vers l'absorbeur faible, de k = -2 a 12, sans avoir ete reglee sur le temoin.
Au temoin, les valeurs justes occupent le bord fort ; le critere de cinq valeurs etait hors
d'atteinte a G20, sauf palier prolonge du cote que l'echelle n'echantillonne pas. Le temoin
positif n'avait tenu nulle part avant la nuit : au pre-vol, a geometrie reduite, il rendait PAS
DE PLATEAU (etalements {pv_e20} a G20 et {pv_e30} a G30) et le plancher mordait, ce que les deux
machines ont lu comme l'effet attendu de la geometrie reduite, non opposable ; aucun essai du
temoin a taille reelle n'a precede le gel de l'echelle. Ce defaut n'excuse pas le verdict : il dit pourquoi
le verdict ne tranche pas.""", ind=2, suite=4)
P("""D-QEB-3 (m1, gel, conception ; NOUVEAU). Le temoin negatif n'est pas jouable a taille reelle
: un etat loge dans l'absorbeur change trop d'un barreau a l'autre pour un suivi a 0.90
(recouvrements {tn_ov_min} a {tn_ov_max}). Au pre-vol, a geometrie reduite, il jouait son role
(candidat {tn_prevol} ; journal {c_prevol_tn}, non opposable). Consequence : le banc n'a PAS
montre a taille reelle que son critere de plateau mord sur un etat d'absorbeur ; seule la mutation
M-1 du banc qui tue le montre, sur une serie fabriquee.""", ind=2, suite=4)
P("""D-QEB-1 (m1, procedure E19). L'essai de fumee a taille reelle de machine 1 a imprime les
largeurs et les conditionnements de dix etats au point 1.95, k = 3 -- l'etat retenu et neuf
voisins, matiere de l'etage 2 -- avant certification (journal {c_fumee}, joint tel quel au lot {c_lot_sonde1}). N'atteint pas le
verdict ; atteint le statut de A-4 et A-5 (nn.7).""", ind=2, suite=4)
P("""D-1, D-2, D-3 (m1, sonde et banc v1 ; trouves par m2). Reprise par fichier sans identite : un
etage 1 reel reprenait un pre-vol et l'ecrivait comme reel ; un etage 2 reel franchissait la
porte sous un verdict de pre-vol ; le banc lancait la sonde par python -I et echouait a BOCAL4,
ou numpy vit en paquet utilisateur. Leves au v2, certifies.""", ind=2, suite=4)
P("""E-EB-1, E-EB-2, M-1 a M-4 (m1, gel v1 ; trouves par m2). Critere de plateau insatisfaisable en
flottants a la borne, repris en rationnels exacts ; temoin negatif absent du decompte, 540 devenu
555 ; quatre demandes de description. Tout pris au v2. Faute de transit de m1 : le gel v1 parti
en deux pieces a plat, sans manifeste.""", ind=2, suite=4)
P("""D-P0-1 a D-P0-4 (m1, etape 0). Trois traitements fautifs d'une valeur non finie dans le script
de lecture, corriges en v2 par hunks nommes, les cinq lectures inchangees ; l'ensemble de
reference de la regle HORS PLAGE melait les deux familles et la regle etait sans puissance :
laisse tel qu'ecrit.""", ind=2, suite=4)
P("""Autres, de m1 : l'echelle de couplage du temoin d'abord placee de tete, fausse d'un facteur
trois, corrigee par le calcul avant le gel et declaree au gel ; un attendu faux dans l'audit de
la reference (171 points attendus, 149 consommes par les definitions), premier jet et journal
joints.""", ind=2, suite=4)
P("""De m2, sur ses propres pieces : premier jet du script de reference, une egalite exacte
departagee par l'arrondi flottant a j = 12 ; corrige, j = 12 seul bouge, la liste des retenus ne
change pas, premier jet conserve. O-A : "la grille complete" de sa note vaut treize points par
couplage raffine, pas quinze ; rien de ce qui manque n'est lu ; le mot est corrige ici, pas le
calcul. O-C : j = 5 est exclu des retenus pour un depassement de {u5_dep} du seuil de u_ref
(u_ref = {u5}, Gamma_ref {g5}), par un seul point de bruit dense ; liste non modifiee, le fichier
certifie fait foi. Faute de transit de m2 : sa certification du gel v2, ecrite, n'etait pas
partie ; jointe ensuite au lot {c_lot_cert_sonde2}.""", ind=2, suite=4)
P("""Retraits : aucun. E19 : nn.4.""", ind=2, suite=4)

T("", "nn.9 REGLES CANDIDATES SOUS (X) -- revue ECHUE depuis le 28/09 ; aucune n'est prise ici")
P("""19  (m1, d'apres D-QEB-2) L'echelle d'un instrument se regle sur son temoin positif, a taille
reelle, avant le gel, par un run qui ne lit rien de l'objet ; le gel fige ensuite l'echelle et
le run de jugement est un autre run.""", ind=2, suite=6)
P("""20  (m1, d'apres D-QEB-1) Un essai de fumee a taille reelle n'imprime que ce que le gel connait
deja ; toute autre valeur de l'objet reste dans le fichier, non lue.""", ind=2, suite=6)
P("""21  (m1, d'apres D-1 et D-2 de m2) Un fichier repris porte l'identite de ce qui l'a produit --
script, moteur, gel, geometrie, mode -- et la reprise refuse sur tout ecart ; le banc qui tue
porte un temoin de ce refus.""", ind=2, suite=6)
P("""22  (m1, d'apres D-3 de m2) Un banc lance un script comme l'operateur le lance sur la machine
qui joue, pas comme la machine qui ecrit.""", ind=2, suite=6)
P("""Les dix-huit precedentes (huit du 90, quatre du 91, une du 92, trois du 93) attendent la meme
revue.""")

T("", "nn.10 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI")
P("""(i)   les numeros de serie de nn.8 (E18) ;""", ind=2, suite=6)
P("""(ii)  la revue (X), echue : vingt-deux candidates ;""", ind=2, suite=6)
P("""(iii) le depot des lots de ce chantier (nn.12) : rien n'en est au registre ;""", ind=2, suite=6)
P("""(iv)  la suite de la piste (0). Le garde-fou du gel etait propose sous le veto de l'operateur ;
aucun veto n'a ete pose ; l'acte l'applique a ce gel : pas de v3, pas de second run sous lui,
aucun rejeu sous d'autres seuils. Une reprise ne serait donc pas un tour de correction mais un
NOUVEAU gel, c'est-a-dire une decision de l'operateur qui deroge a "on s'arrete". Machine 1
a dit a l'operateur le 12/11 les trois conditions qu'elle y mettrait : cet acte d'abord ; une seule difference au gel, l'echelle prolongee du cote de l'absorbeur fort, gelee et
certifiee avant tout run ; et dernier essai. Ce qui la laisse possible sans biais de lecture : le
fantome n'a pas ete lu, hors les dix largeurs de D-QEB-1. L'acte ne la recommande pas et ne
l'ecarte pas ;""", ind=2, suite=6)
P("""(v)   le statut des largeurs de M17 : inchange par cet acte. Elles ne sont ni qualifiees ni
reclassees ; toute phrase qui porte un Gamma garde le statut qu'elle avait, celui d'une largeur
lue par un instrument sans temoin tenu ;""", ind=2, suite=6)
P("""(vi)  la suite du programme, telle qu'au 93 (nn.9 (v)) : inchangee.""", ind=2, suite=6)

T("", "nn.11 CONSEQUENCES POUR LE REGISTRE")
P("""Aucun verdict de manche ne change. Le gel E-B v2 ({c_gel_v2}) entre au registre comme JOUE,
verdict {cascade} ; le gel v1, la sonde v1 et le banc v1 y entrent comme NON CERTIFIES, avec les
certifications qui les refusent, pour que les corrections restent lisibles ; la sonde v2, le banc
v2 et la feuille v1, certifies ; la reference de machine 2 et sa certification ; le lot de la
nuit ; l'etape 0. Le perimetre s'ENUMERE depuis les citations de cet acte par la feuille de
perimetre du contresignataire et ne s'ecrit pas a la main (E-92-1).""")

T("", "nn.12 LE CANAL")
P("""Lots echanges depuis le delta 93 (canons), tous des 11 et 12/11. Machine 1 -- etape 0
{c_lot_e0} ; gel v2 {c_lot_gel2} ; sonde, feuille et banc v1 {c_lot_sonde1} ; sonde et banc v2
{c_lot_sonde2} ; certification de la reference {c_lot_cert_ref}. Machine 2 -- certification du gel
v1 {c_lot_cert_gel1} ; du gel v2 {c_lot_cert_gel2} ; de la sonde v1 {c_lot_cert_sonde1} ; de la
sonde v2 {c_lot_cert_sonde2} ; reference du temoin {c_lot_ref} ; resultat de la nuit
{c_lot_nuit}. Deux lots sont arrives deux fois a machine 1, verifies identiques a l'octet, sans
effet. Le registre est a 2ec6775, releve par machine 1 le 12/11. Le conteneur de machine 1 est
reinitialise a chaque conversation (rejeux depuis les lots et le clone).""")

T("", "nn.13 CE QUE CE DELTA NE FAIT PAS")
P("""Il ne qualifie pas Gamma_LS et ne la disqualifie pas. Il ne dit rien des six largeurs de M17,
de leur rang ni du verdict de la manche. Il ne fait pas des lectures de nn.6 un resultat : elles
ne sont pas pre-enregistrees, et (d) ne qualifie pas la porte de M17. Il ne dit pas que
l'instrument est faux a G20 ; il ne dit pas qu'il y est juste. Il ne rejoue rien du fantome, sous
ces seuils ni sous d'autres. Il n'ouvre ni v3 ni nouveau gel. Il ne prend aucun numero, n'adopte
aucune regle, ne recommande aucun delta, n'edite aucune piece citee (PB-1), ne depose ni ZIP ni
MANIFEST.sha256.""")

T("", "nn.14 PIECES DE CE DELTA (lot machine 1 ; canon = convention B du manifeste)",
  "  journal_delta_nn_qualification_EB_v1.md              cet acte",
  "  ecrire_acte_qualification_EB_machine1_v1.py          le script qui pose nombres et canons",
  "  rejeu_ponctuel_TP_machine1_v1.py / .log              six decompositions du temoin, non opposable",
  "  releve_acte_qualification_EB_machine1_v1.py / .log   controle de sortie, pas un contreseing",
  "  note_machine1_acte_qualification_EB_v1.md            la note d'accompagnement",
  "  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.",
  "", "-- FIN journal_delta_nn_qualification_EB_v1 --")

texte = "\n".join(OUT) + "\n"
o = texte.encode("ascii")
assert o.count(b"%") == 0, "un signe pour cent dans l'acte"
assert "{" not in texte and "}" not in texte
lmax = max(len(l) for l in OUT)
assert lmax <= 100, "ligne de %d caracteres : %r" % (lmax, [l for l in OUT if len(l) > 100][:3])
assert not any(l != l.rstrip() for l in OUT)
open(SORTIE, "wb").write(o)
print("acte : %s ; canon %s ; %d o ; %d lignes ; plus longue ligne %d ; %d valeurs posees" % (
    os.path.basename(SORTIE), cB(SORTIE), len(o), len(OUT), lmax, len(V)))
