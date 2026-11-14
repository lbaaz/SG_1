# -*- coding: ascii -*-
# ECRIT L'ACTE DE LA QUALIFICATION E-B BIS (journal_delta_nn_qualification_EB_bis_v1.md).
# Aucun nombre MESURE et aucun canon n'est tape : les nombres sont relus des pieces
# citees, les statuts sont ceux que rend la feuille de lecture certifiee v2
# (c14dafffc5f84c97) rejouee ici sur les sorties de machine 2, et chaque canon tape est
# un ATTENDU affirme contre le canon recalcule du fichier. Le texte (prose, seuils du
# gel, noms) est de la plume.
# Arguments : <dossier du gel bis m1> <racine des recus> <clone du registre>
#             <dossier du rejeu m1> <sortie>
import sys, os, json, re, math, hashlib, unicodedata, importlib.util, textwrap
from fractions import Fraction

BIS, RECU, REG, RJ, SORTIE = sys.argv[1:6]
V = {}


def cB(chemin):
    o = open(chemin, "rb").read()
    t = unicodedata.normalize("NFC", o.decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


LOTN = RECU + "/recu_nuit_bis/lot"
NUIT = LOTN + "/nuit_EB_bis"
SO = NUIT + "/sortie"
JR = REG + "/journal/"
PIECES = [  # (cle, chemin, canon attendu ou None)
    ("moteur", REG + "/scripts/m17_chaine_v17.py", "82a0be882568fe0c"),
    ("man_run", JR + "manche_m17_v17_MANIFEST_machine2.txt", "4aecd0e2b23bc818"),
    ("acte94", JR + "journal_delta_94_qualification_EB_v2.md", "569ccbd0d1adb927"),
    ("gel_v2", REG + "/gels/qualification_EB_pre_enregistrement_v2.md", "cde0cd11a763f26d"),
    ("ref_table", JR + "tp_reference_machine2_v1.json", "4d51dd58ef456fe9"),
    ("ref_liste", JR + "tp_retenus_machine2_v1.json", "69b3bab3bb8480b7"),
    ("gel_bis", BIS + "/qualification_EB_bis_pre_enregistrement_v1.md", "dcda1611adf5f8fd"),
    ("sonde", BIS + "/sonde_qualification_EB_machine1_v3.py", "555146abd2192f79"),
    ("feuille", BIS + "/lecture_qualification_EB_machine1_v2.py", "c14dafffc5f84c97"),
    ("banc", BIS + "/banc_qui_tue_qualification_EB_machine1_v3.py", "3f2ef4d35af630c2"),
    ("essai", BIS + "/essai_feuille_v2_series_etendues_machine1_v1.log", None),
    ("n_m1_gel", BIS + "/POUR_MACHINE2_gel_EB_bis_machine1_v1.md", "09f239071bb2ba23"),
    ("lot_gel", BIS + "/lot/MANIFEST_lot_machine1_gel_EB_bis_v1.txt", "25276846153bacff"),
    ("lot_diag", RECU + "/recu_diag/lot/MANIFEST_lot_machine2_diagnostic_TP_echelle_forte_v1.txt",
     "762a89e8ad7d498a"),
    ("n_m2_diag", RECU + "/recu_diag/lot/POUR_MACHINE1_diagnostic_TP_echelle_forte_machine2_v1.md",
     "7e856dbdd51ea14f"),
    ("lot_cert", RECU + "/recu_cert_bis/lot/MANIFEST_lot_machine2_certification_gel_EB_bis_v1.txt",
     "4de461538a1b694d"),
    ("n_m2_cert", RECU + "/recu_cert_bis/lot/POUR_MACHINE1_certification_gel_EB_bis_machine2_v1.md",
     "62beaa7971ce4544"),
    ("lot_nuit", LOTN + "/MANIFEST_lot_machine2_resultat_nuit_EB_bis_v1.txt", "a01598ec24237921"),
    ("n_m2_nuit", LOTN + "/POUR_MACHINE1_resultat_nuit_EB_bis_machine2_v1.md", "7fb7c0534c744911"),
    ("s1", SO + "/sonde_etage1.json", "1ae4b5b2f9ff0e70"),
    ("s1_log", SO + "/sonde_etage1.log", "4908daa89d914382"),
    ("v1", SO + "/verdict_etage1.json", "f7694c58bdbd11a4"),
    ("l1_log", SO + "/lecture_etage1.log", "85e7939fc556b0e8"),
    ("s2", SO + "/sonde_etage2.json", "c110c6286157b025"),
    ("s2_log", SO + "/sonde_etage2.log", "1c53c8c28ab5ab95"),
    ("v2", SO + "/verdict_qualification_EB.json", "63bca8c997bde7c0"),
    ("l2_log", SO + "/lecture_etage2.log", "e316a1e8caffd058"),
    ("console", NUIT + "/console_nuit.log", "efcc91c332e008ea"),
    ("pilote", NUIT + "/lancer_nuit_EB_bis_machine2_v1.py", "7dc2197de3401886"),
    ("m2_lect_log", NUIT + "/lecture_resultat_machine2_v1.log", "4f471482c721e5b6"),
    ("m2_lect", LOTN + "/lecture_resultat_nuit_EB_bis_machine2_v1.py", "37579efadcaf862b"),
    # le rejeu declare de machine 1
    ("rj_pilote", RJ + "/rejeu_declare_point_39_20_machine1_v1.py", "4c9243a624a8686d"),
    ("rj_scelle", RJ + "/sortie/rejeu_point_39_20_F1G20_machine1.json", "7fb9026014ad0c93"),
    ("rj_log", RJ + "/sortie/rejeu_declare_machine1.log", "e9fd2a0309846c06"),
    ("rj_ouv", RJ + "/ouverture_scelle_point_39_20_machine1_v1.py", None),
    ("rj_ouv_log", RJ + "/ouverture_scelle_point_39_20_machine1_v1.log", None),
    ("rj_banc", RJ + "/banc_qui_tue_v3_rejeu_machine1.log", None),
    ("rj_l1", RJ + "/lecture_m1/lecture_etage1.log", "85e7939fc556b0e8"),
    ("rj_l2", RJ + "/lecture_m1/lecture_etage2.log", "e316a1e8caffd058"),
    ("rj_v1", RJ + "/lecture_m1/verdict_etage1.json", None),
    ("rj_v2", RJ + "/lecture_m1/verdict_qualification_EB.json", None),
]
for cle, chemin, att in PIECES:
    c = cB(chemin)
    assert att is None or c == att, "canon : %s rend %s, attendu %s" % (chemin, c, att)
    V["c_" + cle] = c
print("canons relus : %d, dont %d affirmes contre un attendu" % (
    len(PIECES), sum(1 for p in PIECES if p[2])))

# ---------------------------------------------------------------- les deux etages, par la feuille certifiee
s1 = json.load(open(SO + "/sonde_etage1.json"))
v1m2 = json.load(open(SO + "/verdict_etage1.json"))
s2 = json.load(open(SO + "/sonde_etage2.json"))
v2m2 = json.load(open(SO + "/verdict_qualification_EB.json"))
ref = json.load(open(JR + "tp_reference_machine2_v1.json"))
spec = importlib.util.spec_from_file_location("lec", BIS + "/lecture_qualification_EB_machine1_v2.py")
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
so = sys.stdout
sys.stdout = open(os.devnull, "w")
try:
    verdict1, motifs, det1 = L.juger_etage1(s1, ref)
    okst, TS = L.selftest()
    jg = L.selection_gel(ref["balayage"])
    verdict2, det2 = L.juger_etage2(v1m2, s2)
finally:
    sys.stdout = so


def ecarts(a, b, chemin=""):
    """Compare deux arbres JSON : rend (nombre d'ecarts non flottants, liste des ecarts relatifs flottants)."""
    nf, fl = 0, []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                nf += 1
            else:
                x, y = ecarts(a[k], b[k], chemin + "/" + str(k))
                nf += x
                fl += y
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for x_, y_ in zip(a, b):
            x, y = ecarts(x_, y_, chemin)
            nf += x
            fl += y
    elif a != b:
        if isinstance(a, float) and isinstance(b, float) and b != 0.0:
            fl.append(abs(a / b - 1.0))
        else:
            nf += 1
    return nf, fl


assert verdict1 == v1m2["etage1"] == "TIENT" and motifs == v1m2["motifs"] == []
assert verdict2 == v2m2["verdict"] == "NON QUALIFIE"
e1 = ecarts(det1, v1m2["detail"])
e2 = ecarts(det2, v2m2["detail"])
assert e1[0] == 0 and e2[0] == 0 and max(e1[1] + e2[1] + [0.0]) < 1e-9, (e1[0], e2[0])
rv1 = json.load(open(RJ + "/lecture_m1/verdict_etage1.json"))
rv2 = json.load(open(RJ + "/lecture_m1/verdict_qualification_EB.json"))
f1, f2 = ecarts(rv1, v1m2), ecarts(rv2, v2m2)
assert f1[0] == 0 and f2[0] == 0
V["fl_n1"], V["fl_n2"] = "%d" % len(f1[1]), "%d" % len(f2[1])
V["fl_n"] = "%d" % (len(f1[1]) + len(f2[1]))
V["fl_pire"] = "%.1e" % max(f1[1] + f2[1])
assert s1["gel"] == s2["gel"] == V["c_gel_bis"] and s1["moteur"] == s2["moteur"] == V["c_moteur"]
assert s1["prevol"] is False and s2["prevol"] is False and s1["mutation"] is None and s2["mutation"] is None
assert s1["GQ10"] is True and s2["GQ10"] is True
assert v1m2["canon_sonde_etage1"] == V["c_s1"] and v1m2["canon_reference"] == V["c_ref_table"]
assert all(s1["GQ3"].values()) and len(s1["GQ3"]) == 6
assert okst
V["selftest"] = "%d tenus sur %d" % (sum(1 for x in TS if x[1]), len(TS))
js = sorted(v["j"] for v in s1["TP"].values())
assert js == sorted(r["j"] for r in ref["retenus"]) == jg == [6, 8]
V["cascade"] = L.cascade(v1m2, s2, det2["points"])
assert V["cascade"] == "NON QUALIFIE"
pf = s2["plateforme"]
assert pf == s1["plateforme"] and pf["temoin_lecture"] == "CR"
V["plat"] = "%s %s, python %s, numpy %s" % (pf["systeme"], pf["machine"], pf["python"], pf["numpy"])
for tp_ in s1["TP"].values():
    for cfg_ in ("F1G20", "F1G30"):
        for rec in tp_["traj"][cfg_].values():
            assert rec["identite_reprise"]["sonde"] == V["c_sonde"]
V["cascade_1"] = verdict1

# ---------------------------------------------------------------- etage 1
def fenetres(ser):
    out = []
    for k0 in range(L.K_MIN, L.K_MAX - 3):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(x is None for x in v):
            continue
        mx, mn = Fraction(max(v)), Fraction(min(v))
        out.append((k0, mx <= (1 + L.TAU) * mn, float(mx / mn) - 1.0))
    return out


LIGNES_TP, min4, pire_ln = [], None, 0.0
for cle in ("j06", "j08"):
    d = det1["TP"][cle]
    g = s1["TP"][cle]["g"]
    LIGNES_TP.append("  j = %d, g = %.5f, Gamma_ref %.4e, u_ref %.1e" % (int(cle[1:]), g, d["Gamma_ref"], d["u_ref"]))
    for cfg in ("F1G20", "F1G30"):
        q = d[cfg]
        assert q["statut"] == "PLATEAU" and q["tient"] is True
        f = fenetres(L.serie(s1["TP"][cle]["traj"][cfg], 0))
        pk = [k for k, ok, _ in f if ok]
        assert pk and max(pk) < 4
        m4 = min(e for k, ok, e in f if k >= 4)
        min4 = m4 if min4 is None else min(min4, m4)
        pire_ln = max(pire_ln, q["ecart_ln"])
        LIGNES_TP.append("    %s : PLATEAU, k0 = %2d, etalement %.4f, Gamma_pl %.4e, |ln| %.4f contre %.4f :"
                         " TIENT" % (cfg[2:], q["k0"], q["etalement"], q["Gamma_pl"], q["ecart_ln"],
                                     L.TAU_F + d["u_ref"]))
        LIGNES_TP.append("          fenetres a PLATEAU : k0 = %s" % ", ".join("%d" % k for k in pk))
V["tp_pire_ln"] = "%.4f" % pire_ln
V["tp_pire_pc"] = "%.2f" % (100.0 * (math.exp(pire_ln) - 1.0))
V["tp_min4"] = "%.1f" % min4
assert det1["TN"] == "NON JOUE"
V["tn_cands"] = ", ".join("[%d, %d]" % tuple(c) for c in s1["TN"]["candidats"])
pl = [abs(x) for d in s1["GQ5"].values() for x in d.values()]
V["plancher"], V["n_plancher"] = "%.3e" % max(pl), "%d" % len(pl)
c1 = s1["comptes"]
assert (c1["TP"]["joues"], c1["TN"]["joues"], c1["TN"]["sautes"], c1["plancher"]["joues"]) == (72, 3, 15, 30)
assert sum(x["repris"] for x in c1.values()) == 0
V["hors"] = ", ".join(s1.get("hors_manifeste") or ["rien"])
con = open(NUIT + "/console_nuit.log", encoding="utf-8").read()
d1 = int(re.search(r"FIN etage1 code=0 duree=(\d+) s", con).group(1))
d2 = int(re.search(r"FIN etage2 code=0 duree=(\d+) s", con).group(1))
V["d1"], V["d2"] = "%d h %02d" % (d1 // 3600, round(d1 % 3600 / 60.0)), "%d h %02d" % (d2 // 3600, round(d2 % 3600 / 60.0))
V["debut"] = re.search(r"2026-11-13 (\d\d):(\d\d):\d\d DEBUT etage1", con).expand(r"\1h\2")
V["fin1"] = re.search(r"2026-11-13 (\d\d):(\d\d):\d\d FIN etage1", con).expand(r"\1h\2")
V["fin2"] = re.search(r"2026-11-13 (\d\d):(\d\d):\d\d FIN etage2", con).expand(r"\1h\2")
assert "VERDICT ETAGE 1 : TIENT" in con and "VERDICT DE LA QUALIFICATION : NON QUALIFIE" in con
assert "ARRET" not in con

# ---------------------------------------------------------------- etage 2
c2 = s2["comptes"]
assert (c2["F1"]["joues"], c2["F1"]["repris"], c2["formes"]["joues"], c2["translation"]["joues"],
        c2["ouverture"]["joues"]) == (210, 6, 216, 108, 6)
assert sum(x["sautes"] for x in c2.values()) == 0
assert all(x["au_bit"] is True and x["rapport"] == 1.0 for x in s2["GQ4"].values()) and len(s2["GQ4"]) == 6
NOMS = {"39_20": "1.95", "197_100": "1.97", "99_50": "1.98", "101_50": "2.02", "203_100": "2.03", "41_20": "2.05"}
for n in L.POINTS:
    assert abs(float(Fraction(s2["points"][n]["w2"])) - float(NOMS[n])) < 1e-12
ns = nt = 0
ovmin = idmin = 1.0
for n in L.POINTS:
    for cfg, d in s2["points"][n]["cfg"].items():
        idmin = min(idmin, d["identite"])
        for r in d["traj"].values():
            e = r["etats"][0]
            nt += 1
            ns += bool(e["suivi"])
            if e.get("ov") is not None:
                ovmin = min(ovmin, e["ov"])
assert ns == nt == 540
V["ov_min"], V["id_min"] = "%.9f" % ovmin, "%.4f" % idmin
PTS = det2["points"]
assert all(PTS[n]["statut"] == "NON QUALIFIE" and not PTS[n]["non_lisibles"] for n in L.POINTS)
CODE = {"PLATEAU": "PL", "PAS DE PLATEAU": "--"}
TAB = ["  w2    G_run      F1G20          F1G30          F2G20          F3G20          F1GT           echecs"]
npl = {c: 0 for c in L.REQUIS}
proches = []
for n in L.POINTS:
    cel = []
    for c in L.REQUIS:
        q = PTS[n]["plateaux"][c]
        npl[c] += q["statut"] == "PLATEAU"
        cel.append("%s %.4f %2d" % (CODE[q["statut"]], q["etalement"], q["k0"]))
        if q["statut"] == "PAS DE PLATEAU" and q["etalement"] < 0.06:
            proches.append((q["etalement"], "%s a %s en %s" % ("%.4f" % q["etalement"], NOMS[n], c)))
    TAB.append("  %s  %.3e  %s   %d" % (NOMS[n], s2["points"][n]["G_run"], "   ".join(cel), len(PTS[n]["echecs"])))
V["npl"] = ", ".join("%s %d" % (c, npl[c]) for c in L.REQUIS)
V["proches"] = " ; ".join(t for _, t in sorted(proches))
V["n_proches"] = "%d" % len(proches)
GPL = []
for n in L.POINTS:
    t = ["%s %.3e" % (c, PTS[n]["plateaux"][c]["Gamma_pl"]) for c in L.REQUIS if PTS[n]["plateaux"][c]["statut"] == "PLATEAU"]
    GPL.append("  %s  %s" % (NOMS[n], " ; ".join(t)))
p195 = PTS["39_20"]
assert [n for n in L.POINTS if PTS[n]["plateaux"]["F1G20"]["statut"] == "PLATEAU"] == ["39_20"]
assert p195["M17_sur_plateau"] is True and p195["plateaux"]["F1G20"]["k0"] == 0
assert sorted(e.split(" (")[0] for e in p195["echecs"]) == ["pas de plateau a F2G20", "pas de plateau a F3G20"]
V["e_ln"] = "%.4f" % abs(math.log(s2["points"]["39_20"]["G_run"] / p195["plateaux"]["F1G20"]["Gamma_pl"]))
V["b_ln"] = "%.4f" % p195["plateaux"]["F1G30"]["ecart_ln_F1G20"]
V["d_ln"] = "%.4f" % p195["plateaux"]["F1GT"]["ecart_ln_F1G20"]
V["f2_195"] = "%.4f" % p195["plateaux"]["F2G20"]["etalement"]
V["f3_195"] = "%.4f" % p195["plateaux"]["F3G20"]["etalement"]
V["e_run"] = "%.4f" % det2["E_run"]
assert V["e_run"] == L.E_RUN_GEL
TE = det2["T_etats"]
assert all(TE[n]["S_w"] is None for n in L.POINTS) and det2["mediane_S_w"] is None
V["te_npl"] = ", ".join("%s %d" % (NOMS[n], TE[n]["n_plateaux"]) for n in L.POINTS)
V["te_somme"] = "%.0e" % max(TE[n]["somme_c_ecart"] for n in L.POINTS)
kap = [k for n in L.POINTS for k in TE[n]["kappa"]]
V["kap_n"], V["kap_min"], V["kap_max"] = "%d" % len(kap), "%.7f" % min(kap), "%.5f" % max(kap)
V["kap_ecart"] = "%.0e" % (max(kap) - 1.0)
ANN = det2["annonces"]
assert ANN == v2m2["detail"]["annonces"]
assert (ANN["A-1"], ANN["A-2 (2.02 non qualifie)"], ANN["A-3 (droite >= gauche)"],
        ANN["A-4 (fluctuation d'etat dominante)"], ANN["A-5 (kappa gauche > droite)"]) == (
            "NON QUALIFIE", True, True, None, False)
gmin = min(s2["points"][n]["G_run"] for n in L.POINTS)
gmax = max(s2["points"][n]["G_run"] for n in L.POINTS)
V["g_min"], V["g_max"] = "%.3e" % gmin, "%.3e" % gmax
V["rap_plancher"] = "%d" % int(gmin / max(pl))          # arrondi vers le bas

# ---------------------------------------------------------------- lectures apres coup (description)
R = {n: {c: {k: (v / s2["points"][n]["G_run"]) for k, v in L.serie(s2["points"][n]["cfg"][c]["traj"], 0).items()
             if v is not None} for c in L.REQUIS} for n in L.POINTS}
w = max((max(abs(R[n]["F1G20"][k] / R[n]["F1G30"][k] - 1.0) for k in range(-5, 3)), NOMS[n]) for n in L.POINTS)
V["g20g30"], V["g20g30_pt"] = "%.4f" % w[0], w[1]
w4 = [abs(R[n]["F1G20"][4] / R[n]["F1G30"][4] - 1.0) for n in L.POINTS]
V["g20g30_k4_min"], V["g20g30_k4_max"] = "%.3f" % min(w4), "%.3f" % max(w4)


def bornes(ks, cfgs=None):
    x = [(R[n][c][k], NOMS[n], c, k) for n in L.POINTS for c in (cfgs or L.REQUIS) for k in ks if k in R[n][c]]
    return min(x), max(x)


a, b = bornes(range(1, 4))
V["c13_min"], V["c13_max"] = "%.2f" % a[0], "%.2f" % b[0]
V["c13_bande"] = "%.2f" % max(1.0 - a[0], b[0] - 1.0)
a, b = bornes(range(0, 4))
V["c03_min"], V["c03_max"], V["c03_max_ou"] = "%.2f" % a[0], "%.2f" % b[0], "%s en %s, k = %d" % b[1:]
a, b = bornes(range(-5, 0))
V["fort_min"], V["fort_min_ou"] = "%.2f" % a[0], "%s en %s, k = %d" % a[1:]
V["fort_max"], V["fort_max_ou"] = "%.2f" % b[0], "%s en %s, k = %d" % b[1:]
a, b = bornes(range(-5, 0), ["F1G20", "F1G30", "F3G20"])
V["fort13_max"] = "%.2f" % b[0]
a, b = bornes(range(-5, 0), ["F2G20", "F1GT"])
V["fort2t_min"] = "%.2f" % a[0]
a, b = bornes(range(5, 13))
V["faible_max"], V["faible_max_ou"] = "%.2f" % b[0], "%s en %s, k = %d" % b[1:]
k0s = sorted({PTS[n]["plateaux"][c]["k0"] for n in L.POINTS for c in L.REQUIS})
V["k0_min"], V["k0_max"] = "%d" % k0s[0], "%d" % k0s[-1]

# ---------------------------------------------------------------- le rejeu declare, ouvert
A = json.load(open(RJ + "/sortie/rejeu_point_39_20_F1G20_machine1.json"))["traj"]
B = s2["points"]["39_20"]["cfg"]["F1G20"]["traj"]
pire0, k_pire0, abs0, absmax = 0.0, None, 0.0, 0.0
hors, g3 = {}, [e["gamma"] for e in B["3"]["etats"]]
for k in range(-5, 13):
    ea, eb = A[str(k)]["etats"], B[str(k)]["etats"]
    assert len(ea) == len(eb) == 10 and A[str(k)]["eta"] == B[str(k)]["eta"]
    for t in range(10):
        assert ea[t]["suivi"] is True and eb[t]["suivi"] is True
        assert abs(ea[t]["E_re"] - eb[t]["E_re"]) < 1e-11
        e = abs(ea[t]["gamma"] / eb[t]["gamma"] - 1.0)
        absmax = max(absmax, abs(ea[t]["gamma"] - eb[t]["gamma"]))
        if t == 0:
            abs0 = max(abs0, abs(ea[t]["gamma"] - eb[t]["gamma"]))
            if e > pire0:
                pire0, k_pire0 = e, k
        elif e > 1e-3:
            hors.setdefault(t, []).append(eb[t]["gamma"])
assert pire0 <= 1e-3
V["rj_pire0"], V["rj_k0"], V["rj_abs0"] = "%.3e" % pire0, "%d" % k_pire0, "%.1e" % abs0
V["rj_absmax"] = "%.1e" % absmax
V["rj_tiennent"] = "%d" % (9 - len(hors))
V["rj_hors"] = "%d" % len(hors)
V["rj_hors_detail"] = " ; ".join("etat %d, %d barreaux sur 18, ou Gamma va de %.0e a %.0e" % (
    t, len(hors[t]), min(hors[t]), max(hors[t])) for t in sorted(hors))
V["rj_gmin"], V["rj_gmax"] = "%.0e" % min(g3), "%.0e" % max(g3)
_m = max(max(v) for v in hors.values())
_e = math.floor(math.log10(_m))
V["rj_hors_max"] = "%.1fe%+03d" % (math.ceil(_m / 10.0 ** _e * 10.0) / 10.0, _e)      # arrondi vers le haut
assert float(V["rj_hors_max"]) >= _m
V["rj_ancrage"] = "%.3e" % abs(A["3"]["etats"][0]["gamma"] / s2["points"]["39_20"]["G_run"] - 1.0)
rjl = open(RJ + "/sortie/rejeu_declare_machine1.log", encoding="ascii").read()
assert rjl.count("-- FIN (barreaux") == 5 and "SCELLE : rejeu_point_39_20_F1G20_machine1.json canon " + V["c_rj_scelle"] in rjl
V["rj_plat"] = "Linux x86_64, python 3.13.18, numpy 2.5.3, levier X86_V4"
assert '"numpy": "2.5.3"' in rjl and '"python": "3.13.18"' in rjl and '"NPY_DISABLE_CPU_FEATURES": "X86_V4"' in rjl
ouv = open(RJ + "/ouverture_scelle_point_39_20_machine1_v1.log", encoding="ascii").read()
assert "pire ecart relatif, etat 0 : %s (k = %s) ; tolerance 1e-3 : TIENT" % (V["rj_pire0"], V["rj_k0"]) in ouv
bq = open(RJ + "/banc_qui_tue_v3_rejeu_machine1.log", encoding="ascii").read()
assert "banc qui tue : 6 mordues == 6 attendues ; base saine ; temoins hors gel : 4 refus == 4 attendus : PASSE" in bq
# la sonde contre le diagnostic, meme machine (O-BIS-2)
pd, ou = 0.0, None
for geom in ("G20", "G30"):
    for r in json.load(open(RECU + "/recu_diag/lot/diagnostic_TP_echelle_forte/diag_%s.json" % geom)):
        tr = s1["TP"]["j%02d" % r["j"]]["traj"]["F1" + geom]
        if str(r["k"]) in tr:
            e = abs(tr[str(r["k"])]["etats"][0]["gamma"] / r["gamma"] - 1.0)
            if e > pd:
                pd, ou = e, "j = %d, %s, k = %d" % (r["j"], geom, r["k"])
V["diag_pire"], V["diag_ou"] = "%.1e" % pd, ou
es = open(BIS + "/essai_feuille_v2_series_etendues_machine1_v1.log", encoding="ascii").read()
V["essai_pire"] = "%.4f" % max(float(x) for x in re.findall(r"\|ln\| = (\d\.\d+) contre", es))

# ---------------------------------------------------------------- phrases reprises des pieces citees
def plat(chemin):
    return " ".join(open(chemin, encoding="utf-8").read().split())


GEL = plat(BIS + "/qualification_EB_bis_pre_enregistrement_v1.md")
for ph in ("et c'est le DERNIER ESSAI de la piste (0) sous cette forme",
           "ni troisieme gel, ni autre echelle, ni autre temoin",
           "L'operateur peut lever ce garde-fou ; les machines, non",
           "NON QUALIFIE : toute phrase portant un Gamma depuis juillet est reclassee ; reste le fait d'ordre de"
           " grandeur \"le fantome fuit, le jumeau non\", et seulement si le TP a tenu",
           "compare a BOCAL4 a 1e-3", "au moins trois, sinon non lu",
           "Aucun rejeu des donnees du fantome sous d'autres seuils"):
    assert ph in GEL, ph
NM2 = plat(LOTN + "/POUR_MACHINE1_resultat_nuit_EB_bis_machine2_v1.md")
for ph in ("540 decompositions", "A toi de dire comment l'acte le compte",
           "le j = 5 a l'echelle etendue (~30 min) que j'avais propose reste non joue"):
    assert ph in NM2, ph
NC = plat(RECU + "/recu_cert_bis/lot/POUR_MACHINE1_certification_gel_EB_bis_machine2_v1.md")
assert "28 controles, 0 morsure" in open(RECU + "/recu_cert_bis/lot/MANIFEST_lot_machine2_certification_gel_EB_bis_v1.txt",
                                         encoding="utf-8").read()

# ---------------------------------------------------------------- les regles candidates sous (X), RELEVEES AU REGISTRE
def numeros(chemin, debut, fin, motif=r"(?m)^  (\d{1,2})[. ] "):
    sec = open(chemin, encoding="utf-8").read().split(debut, 1)[1].split(fin, 1)[0]
    return [int(x) for x in re.findall(motif, sec)]


XR = [("du 90", numeros(JR + "journal_delta_90_constante_A_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("du 91", numeros(JR + "journal_delta_91_constante_A_run_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("du 92", numeros(JR + "journal_delta_92_constante_A_second_ordre_v1.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("de l'acte 93", numeros(JR + "journal_delta_93_constante_A_mesure_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 ")),
      ("du contreseing du 93 par machine 2",
       numeros(JR + "POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md", "## 6. VERSE SOUS (X)", "## 7.")),
      ("du 94", numeros(JR + "journal_delta_94_qualification_EB_v2.md", "\nnn.9 REGLES CANDIDATES", "\nnn.10 ",
                        r"(?m)^  (\d{2}) \(m[12]"))]
assert [n for _, l in XR for n in l] == list(range(1, 26)), XR
NOMBRE = {3: "trois", 4: "quatre", 8: "huit", 25: "vingt-cinq", 28: "vingt-huit"}
n_prec = sum(len(l) for _, l in XR)
V["x_prec"] = NOMBRE[n_prec]
V["x_detail"] = ", ".join("%s %s" % (NOMBRE[len(l)], d) for d, l in XR)
V["x1"], V["x2"], V["x3"] = ["%d" % (n_prec + i) for i in (1, 2, 3)]
V["x_total"] = NOMBRE[n_prec + 3]
for f in ("POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v1.md",
          "POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v2.md"):
    assert "VERSE SOUS (X)" not in open(JR + f, encoding="utf-8").read()
for f in (RECU + "/recu_diag/lot/POUR_MACHINE1_diagnostic_TP_echelle_forte_machine2_v1.md",
          RECU + "/recu_cert_bis/lot/POUR_MACHINE1_certification_gel_EB_bis_machine2_v1.md",
          LOTN + "/POUR_MACHINE1_resultat_nuit_EB_bis_machine2_v1.md"):
    assert "(X)" not in open(f, encoding="utf-8").read()

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


TITRE = """JOURNAL DELTA nn -- LA QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS), REPRISE SOUS LE GEL BIS,
REND "NON QUALIFIE" : A L'ETAGE 1, JOUE LA NUIT DU 13/11 SUR BOCAL4, LE TEMOIN POSITIF (JUMEAU H+, LARGEUR
CONNUE) TIENT AUX QUATRE CONFIGURATIONS, A {tp_pire_pc} POUR CENT AU PIRE ; L'ETAGE 2 SE JOUE EN ENTIER,
540 DECOMPOSITIONS, TOUTES GARDES TENUES ; AUCUN DES SIX POINTS DU FANTOME N'EST QUALIFIE : UN SEUL (1.95)
A UN PLATEAU A L'ABSORBEUR COURT, ET IL ECHOUE SOUS LES DEUX FORMES DE REMPLACEMENT ; LES LARGEURS LUES PAR
M17 NE SONT PAS, AU SENS DU GEL, DES LARGEURS INDEPENDANTES DE L'ABSORBEUR ; TOUTE PHRASE PORTANT UN Gamma
DEPUIS JUILLET EST RECLASSEE ; RESTE LE FAIT D'ORDRE DE GRANDEUR "LE FANTOME FUIT, LE JUMEAU NON" ; C'ETAIT
LE DERNIER ESSAI : LA PISTE (0) SE FERME SOUS CETTE FORME"""
P(TITRE, ind=0)
T("(redaction machine 1, contreseing machine 2, depot operateur, 2026-11-13) -- PROJET, VERSION 1",
  "=======================================================================")

T("", "nn.0 POSITION EN TROIS PHRASES")
P("""L'instrument sait mesurer une largeur connue : sur le jumeau H+, la sonde certifiee rend la largeur de
reference a {tp_pire_pc} pour cent au pire, sur un palier qui commence au bord fort de l'echelle, aux deux
couplages et aux deux longueurs d'absorbeur. Le meme instrument, sur le fantome, ne rend pas une largeur
independante de l'absorbeur au sens gele : cinq points sur six n'ont pas de plateau de cinq valeurs a
l'absorbeur court, et le sixieme perd le sien des qu'on change la forme de l'absorbeur ; verdict de la
cascade : {cascade}, zero point QUALIFIE sur six, zero NON LISIBLE. Le gel dit ce que cela engage et
l'acte ne fait que l'ecrire : les Gamma cites depuis juillet sont reclasses, le fait d'ordre de grandeur
reste parce que le temoin a tenu, et la piste (0) se ferme sous cette forme, sauf decision de l'operateur.""")

T("", "nn.1 PIECES CITEES (convention B ; \"au registre\" = dans l'arbre a fe10bfe, delta 94)")
T("  Au registre")
PIECE("gels/qualification_EB_pre_enregistrement_v2.md", "c_gel_v2", "le gel v2, joue le 12/11 (delta 94)")
PIECE("journal/journal_delta_94_qualification_EB_v2.md", "c_acte94", "l'acte 94 : NON CONCLUANT D'INSTRUMENT")
PIECE("scripts/m17_chaine_v17.py", "c_moteur", "le moteur")
PIECE("journal/manche_m17_v17_MANIFEST_machine2.txt", "c_man_run", "le manifeste du run de M17 (36 lignes)")
PIECE("journal/tp_reference_machine2_v1.json", "c_ref_table", "la table de reference du temoin (machine 2)")
PIECE("journal/tp_retenus_machine2_v1.json", "c_ref_liste", "les couplages retenus, j = 6 et j = 8")
T("  Lot de machine 2 du 13/11, diagnostic du temoin aux barreaux forts (hors gel, non opposable)")
PIECE("MANIFEST_lot_machine2_diagnostic_TP_echelle_forte_v1.txt", "c_lot_diag")
PIECE("POUR_MACHINE1_diagnostic_TP_echelle_forte_machine2_v1.md", "c_n_m2_diag")
T("  Lot de machine 1 du 13/11, gel bis et instrument")
PIECE("MANIFEST_lot_machine1_gel_EB_bis_v1.txt", "c_lot_gel")
PIECE("qualification_EB_bis_pre_enregistrement_v1.md", "c_gel_bis", "LE GEL BIS ; il fait foi")
PIECE("sonde_qualification_EB_machine1_v3.py", "c_sonde", "la sonde : elle mesure et ne juge pas")
PIECE("lecture_qualification_EB_machine1_v2.py", "c_feuille", "la feuille : elle juge et ne mesure pas")
PIECE("banc_qui_tue_qualification_EB_machine1_v3.py", "c_banc")
PIECE("essai_feuille_v2_series_etendues_machine1_v1.log", "c_essai", "essai a blanc, non opposable (nn.10, O-BIS-2)")
PIECE("POUR_MACHINE2_gel_EB_bis_machine1_v1.md", "c_n_m1_gel")
T("  Lot de machine 2 du 13/11, certification du gel bis et de l'instrument")
PIECE("MANIFEST_lot_machine2_certification_gel_EB_bis_v1.txt", "c_lot_cert", "28 controles, 0 morsure ; CERTIFIE")
PIECE("POUR_MACHINE1_certification_gel_EB_bis_machine2_v1.md", "c_n_m2_cert")
T("  Lot de machine 2 du 13/11, resultat de la nuit (14 pieces, authentifiees une a une par machine 1)")
PIECE("MANIFEST_lot_machine2_resultat_nuit_EB_bis_v1.txt", "c_lot_nuit")
PIECE("POUR_MACHINE1_resultat_nuit_EB_bis_machine2_v1.md", "c_n_m2_nuit")
PIECE("nuit_EB_bis/sortie/sonde_etage1.json", "c_s1", "source des nombres de nn.5")
PIECE("nuit_EB_bis/sortie/sonde_etage1.log", "c_s1_log")
PIECE("nuit_EB_bis/sortie/verdict_etage1.json", "c_v1")
PIECE("nuit_EB_bis/sortie/lecture_etage1.log", "c_l1_log")
PIECE("nuit_EB_bis/sortie/sonde_etage2.json", "c_s2", "source des nombres de nn.6 et nn.7")
PIECE("nuit_EB_bis/sortie/sonde_etage2.log", "c_s2_log")
PIECE("nuit_EB_bis/sortie/verdict_qualification_EB.json", "c_v2")
PIECE("nuit_EB_bis/sortie/lecture_etage2.log", "c_l2_log")
PIECE("nuit_EB_bis/console_nuit.log", "c_console", "le journal du pilote : heures et codes de sortie")
PIECE("nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py", "c_pilote")
PIECE("lecture_resultat_nuit_EB_bis_machine2_v1.py", "c_m2_lect", "lecture des JSON par machine 2 ; ne mesure rien")
PIECE("nuit_EB_bis/lecture_resultat_machine2_v1.log", "c_m2_lect_log")
T("  Pieces de machine 1 jointes a ce delta (nn.9)")
PIECE("rejeu_declare_point_39_20_machine1_v1.py", "c_rj_pilote")
PIECE("rejeu_point_39_20_F1G20_machine1.json", "c_rj_scelle", "le rejeu SCELLE")
PIECE("rejeu_declare_machine1.log", "c_rj_log")
PIECE("ouverture_scelle_point_39_20_machine1_v1.py", "c_rj_ouv")
PIECE("ouverture_scelle_point_39_20_machine1_v1.log", "c_rj_ouv_log")
PIECE("banc_qui_tue_v3_rejeu_machine1.log", "c_rj_banc")
PIECE("lecture_m1/verdict_etage1.json", "c_rj_v1", "la feuille rejouee par machine 1 sur les sorties de machine 2")
PIECE("lecture_m1/verdict_qualification_EB.json", "c_rj_v2")

T("", "nn.2 CE QUI A MENE AU GEL BIS")
P("""L'acte 94 ({c_acte94}) a rendu NON CONCLUANT D'INSTRUMENT sous le gel v2 : le temoin tenait a
l'absorbeur long et pas au court, faute d'un plateau de cinq valeurs dans l'echelle k = -2 a 12 ; cause
versee, D-QEB-2, l'echelle ne couvrait le palier du temoin que par son bord fort. Le 13/11, machine 2 a
joue hors gel un diagnostic du temoin seul aux barreaux k = -6 a -2 (lot {c_lot_diag}, non opposable) :
le palier du temoin se prolonge du cote fort aux deux longueurs. La reprise est une decision de
l'operateur ; machine 1 y avait mis trois conditions au 94, nn.10 (iv) : l'acte d'abord, une seule difference de fond,
dernier essai. Le gel bis ({c_gel_bis}) est ce nouveau gel : sa seule difference de fond avec le v2 est
l'echelle, etendue a k = -5 a 12, dix-huit valeurs ; le temoin y est declare REGLE (section 4) et non
plus aveugle ; j = 5 n'est pas ajoute.""")

T("", "nn.3 LE BANC, TEL QUE GELE (rappel ; le gel fait foi)")
P("""Estimateur : Gamma_LS = -2 Im E sous potentiel absorbant -i eta W ; echelle eta_k = eta0 2^(-k), k =
-5 a 12 ; M17 lit a k = 3. PLATEAU : une fenetre de cinq valeurs lisibles a k consecutifs dont le plus
grand rapport max / min ne depasse pas 21/20 ; fenetre retenue : le plus petit rapport ; Gamma_pl :
moyenne geometrique. Configurations : F1 (forme native), F2, F3 (formes de remplacement), G20 et G30
(longueur d'absorbeur), GT (bord translate). Etage 1 : le temoin positif (jumeau H+, x^5, w2 = 39/20,
j = 6 et j = 8, reference par rotation complexe) doit avoir un PLATEAU en accord avec sa reference a G20
ET a G30 ; le temoin negatif est attendu NON JOUE ; plancher du jumeau sous 1e-12. Etage 2, ouvert
seulement si l'etage 1 tient : aux six points de M17, les epreuves (a) a (d) de la section 6 et la
consigne (e). Cascade : section 9. Decomptes geles : 120 decompositions a l'etage 1, 540 a l'etage 2.""")

T("", "nn.4 CE QUI A ETE JOUE, DANS L'ORDRE, ET E19")
P("""13/11, avant le gel bis : le diagnostic de machine 2 (hors gel). Puis : lot du gel bis et de
l'instrument par machine 1 ({c_lot_gel}) ; certification par machine 2 ({c_lot_cert} : 28 controles, 0
morsure, les quatre pieces reconstruites au bit depuis les constructions de machine 1) ; feu vert ecrit
de l'operateur, selon le manifeste de machine 2. Aucun run n'a precede la certification croisee (E19).""")
P("""Le run : pilote {c_pilote} sur BOCAL4 ({plat}), lance a {debut} ; etage 1 fini a {fin1} (duree
{d1}), code 0 ; la feuille lit TIENT ; le pilote ouvre l'etage 2 sans intervention ; etage 2 fini a
{fin2} (duree {d2}), code 0 ; la feuille lit {cascade}. Aucun arret, aucune reprise d'un processus.
Machine 2 declare n'avoir lance aucun calcul pendant le run.""")
P("""Machine 1, pendant et apres le run : le rejeu declare au gel (nn.9), lance le 13/11 au matin sur
le relais par l'operateur du message de machine 2 "l'etage 1 tient", avant la reception du lot (R-BIS-1,
nn.10) ; puis, lot recu et authentifie ({c_lot_nuit}, 14 pieces sur 14), le rejeu de la feuille sur les
sorties de machine 2 et l'ouverture du scelle. Machine 1 a aussi joue pendant le run un calcul hors
chaine sans rapport avec ces donnees (une note de litterature, non jointe, non citee). Rien d'autre.""")

T("", "nn.5 L'ETAGE 1, AU CHIFFRE (feuille {c_feuille} sur la table {c_ref_table})")
P("""Gardes : G-Q1 moteur au canon ; G-Q2 36 pieces du run au canon et a la taille, hors manifeste dans
le dossier de BOCAL4 : {hors}, ni ouvert ni compte ; G-Q3 six matrices a taille reelle identiques a celles
du moteur ; G-Q5 plancher : {n_plancher} valeurs, max |Gamma(H+)| = {plancher} contre 1e-12 ; G-Q7
selftest {selftest} ; G-Q10 : temoin positif 72 joues, plancher 30, temoin negatif 3 joues et 15 sautes,
soit 120. Selection du temoin : j = 6 et j = 8 cote sonde, cote table, et par la regle du gel rejouee.""")
T("  Temoin positif (etat du vide, forme F1) :")
OUT.extend(LIGNES_TP)
P("""Les quatre tiennent ; pire ecart a la reference : |ln| = {tp_pire_ln}. Consigne du gel (5.2) :
aucune fenetre de depart k0 >= 4 ne rend PLATEAU au temoin -- TENUE ; le plus petit etalement d'une telle
fenetre vaut {tp_min4}, contre 0.05. Temoin negatif : candidats {tn_cands}, AUCUNE FENETRE ; NON JOUE,
comme le gel l'attend ; il ne leve aucun motif. VERDICT DE L'ETAGE 1 : {cascade_1}, motifs : aucun.""")

T("", "nn.6 L'ETAGE 2, AU CHIFFRE, ET LE VERDICT (feuille {c_feuille})")
P("""Gardes : G-Q4, ancrage a k = 3 en (F1, G20) : Gamma == G_run AU BIT aux six points ; G-Q10 : F1 210
joues et 6 repris (les six de l'ouverture), formes 216, translation 108, soit 540 decompositions sans une
perdue ; l'etat 0 est SUIVI aux 540 barreaux, plus petit recouvrement lu {ov_min} ; identite {id_min} aux
trente couples (point, configuration).""")
T("  Par point et par configuration : statut (PL = PLATEAU, -- = PAS DE PLATEAU), etalement de la",
  "  meilleure fenetre (seuil 0.05), depart k0 de cette fenetre ; derniere colonne : nombre d'echecs.")
OUT.extend(TAB)
T("  Gamma_pl, la ou un plateau existe :")
OUT.extend(GPL)
P("""Nombre de PLATEAU sur six points : {npl}. Les six points sont NON QUALIFIES, aucun n'est NON
LISIBLE : chaque configuration a des fenetres lisibles, et l'echec est partout "pas de plateau" ; aucun
accord (b), (c) ou (d) n'echoue, parce qu'ils ne se jouent que la ou (F1, G20) a un plateau.""")
P("""Le point 1.95 est le seul a avoir un PLATEAU a (F1, G20). Il tient (a), (b) -- accord G30 / G20 :
|ln| = {b_ln} -- et (d) -- accord GT / G20 : |ln| = {d_ln} -- contre 0.05 ; il echoue sur (c) seul : pas
de plateau sous F2 (meilleur etalement {f2_195}) ni sous F3 ({f3_195}). Consigne 6 (e), lisible a ce seul
point : |ln(G_run / Gamma_pl)| = {e_ln} contre 0.05, "M17 a lu sur le plateau" ; la fenetre retenue part
de k0 = 0 et contient k = 3.""")
P("""T-etats (section 7, sans effet sur le verdict) : E_run = {e_run}, comme au gel ; somme des c_nu a
{te_somme} pres de 1 aux six points ; nombre d'etats a plateau parmi les dix, par point : {te_npl} ; il en
faut trois pour lire S_w : S_w lu a zero point sur six, mediane non lue, lecture non rendue. Les {kap_n}
kappa lus vont de {kap_min} a {kap_max}.""")
P("""VERDICT, par la cascade de la section 9 : {cascade} -- zero point QUALIFIE et au moins un NON
QUALIFIE. Machine 1 a rejoue la feuille certifiee sur les sorties de machine 2 : memes verdicts, memes
statuts (nn.9).""")

T("", "nn.7 CE QUE LES TRAJECTOIRES MONTRENT (description apres coup ; rien ici n'est un verdict, aucun",
  "     seuil n'est rejoue)")
P("""Toutes les valeurs sont Gamma(k) / G_run de l'etat 0, relues de la sortie de la sonde. Machine 2
en donne une lecture voisine dans sa note (section 5), sans en tirer de motif.""")
P("""(a) Au centre, k = 1 a 3, les cinq configurations rendent entre {c13_min} et {c13_max} fois G_run
aux six points ; de k = 0 a 3, entre {c03_min} et {c03_max} (le plus haut : {c03_max_ou}).""", ind=2, suite=6)
P("""(b) Du cote fort, k = -5 a -1, la valeur depend de la FORME de l'absorbeur : F1 et F3 montent
jusqu'a {fort13_max} fois G_run, F2 et la translation descendent jusqu'a {fort2t_min}, selon le point ; sur
l'ensemble,
de {fort_min} ({fort_min_ou}) a {fort_max} ({fort_max_ou}). C'est la que le temoin, lui, est plat.""",
  ind=2, suite=6)
P("""(c) Du cote faible, k >= 5, la valeur chute (elle se divise a peu pres par deux a chaque barreau)
ou fait une bosse, jusqu'a {faible_max} fois G_run ({faible_max_ou}) ; l'etat reste suivi a ces
barreaux, ce n'est pas un saut de suivi.""", ind=2, suite=6)
P("""(d) G20 et G30 coincident a {g20g30} pres de k = -5 a k = 2 aux six points (pire : {g20g30_pt}) et
se separent ensuite : a k = 4, de {g20g30_k4_min} a {g20g30_k4_max}. G30 a un plateau a cinq points,
G20 a un seul.""", ind=2, suite=6)
P("""(e) Les fenetres retenues partent de k0 = {k0_min} a {k0_max}. Etalements hors plateau a moins
de 0.06 : {n_proches} -- {proches}.""", ind=2, suite=6)
P("""Ce que cela decrit, sans le juger : sur trois barreaux centraux les cinq absorbeurs rendent G_run a
{c13_bande} pres ; cette zone est bordee d'un cote par une dependance a la forme et de l'autre par la
chute ; le critere gele demande cinq valeurs a 0.05 pres dans chacune des cinq configurations, et ne les
trouve ensemble a aucun point. Le gel interdit de relire ces donnees sous d'autres seuils (section 12) :
cette description n'est pas une seconde lecture.""")

T("", "nn.8 ANNONCES DE LA PLUME (gel bis, section 11), COMPTEES")
P("""A-1, le verdict. Annonce : QUALIFIE PAR POINT 0.50, NON QUALIFIE 0.27, ESTIMATEUR QUALIFIE 0.13, NON
CONCLUANT D'INSTRUMENT 0.07, NON LISIBLE 0.03. Rendu : NON QUALIFIE. L'issue donnee pour la plus probable
ne s'est pas produite ; celle qui s'est produite etait annoncee a 0.27.""", ind=2, suite=6)
P("""A-2 (0.6), 2.02 n'est pas QUALIFIE : vrai.""", ind=2, suite=6)
P("""A-3 (0.5), la famille de droite compte au moins autant de QUALIFIES que celle de gauche : vrai, SANS
CONTENU -- zero contre zero ; l'acte ne la credite pas (D-BIS-3).""", ind=2, suite=6)
P("""A-4 (0.7, non aveugle), fluctuation d'etat dominante : NON JUGEE -- S_w lu a zero point sur six, la
feuille rend None ; ni creditee ni debitee (D-BIS-2).""", ind=2, suite=6)
P("""A-5 (0.6, non aveugle), kappa de gauche plus grand que kappa de droite : faux, tel que la feuille le
calcule ; les kappa sont tous a moins de {kap_ecart} de 1.""", ind=2, suite=6)
P("""A-6 (0.93, non aveugle, temoin regle), le temoin tient : vrai, aux quatre configurations.""", ind=2, suite=6)
P("""A-7 (0.7), a (F1, G20), tout point qui a un PLATEAU a une fenetre qui ne commence pas avant k = -1 :
vrai sur UN point (1.95, k0 = 0) ; un compte a n = 1.""", ind=2, suite=6)
P("""A-8 (0.55), la consigne 6 (e) tient a tout point qui a un PLATEAU a (F1, G20) : vrai sur le meme UN
point (|ln| = {e_ln}).""", ind=2, suite=6)
P("""Bilan : sur les quatre annonces aveugles a contenu (A-1, A-2, A-7, A-8), trois vraies dont deux sur un
seul point, et l'annonce principale manquee. A-1 a A-5 sont rendues par la feuille ; A-6 a A-8 sont
comptees dans les JSON (verdict_etage1.json ; detail.points.<n>.plateaux.F1G20.k0 et M17_sur_plateau),
pas tapees.""")

T("", "nn.9 LE REJEU DE MACHINE 1 (perimetre declare au gel, section 12)")
P("""Selftest de la feuille : {selftest}. Banc qui tue : 6 mordues == 6 attendues, base saine, 4 refus
== 4 attendus, PASSE. Point 1.95 en (F1, G20) sur l'echelle entiere : 18 decompositions par la sonde
certifiee, appelee par un pilote qui n'affiche aucune largeur ({c_rj_pilote}), sur {rj_plat} ; dix
etats suivis a chacun des 18 barreaux ; ancrage a k = 3 contre G_run : ecart relatif {rj_ancrage}.""")
P("""SCELLE : le resultat ({c_rj_scelle}) a ete ecrit sans etre lu, et son empreinte donnee a l'operateur
avant la reception du lot de machine 2, selon la conversation de l'operateur avec machine 1 ; machine 2
ne peut pas le verifier sur pieces. OUVERTURE, lot recu : etat 0, celui que la feuille juge, pire ecart
relatif a BOCAL4 {rj_pire0} (k = {rj_k0}), contre 1e-3 : TIENT ; plus grand ecart absolu {rj_abs0}. Sur
les neuf autres etats suivis, {rj_tiennent} tiennent a 1e-3 a tous les barreaux et {rj_hors} non :
{rj_hors_detail}. Les energies reelles concordent a 1e-11 pres aux 180 couples (etat, barreau) : ce
sont les memes etats. Aucune largeur au-dessus de {rj_hors_max} ne sort de la tolerance. Le plus grand
ecart absolu sur Gamma, tous etats confondus, vaut {rj_absmax}, pour des largeurs qui vont a k = 3 de
{rj_gmin} a {rj_gmax} : l'ecart entre machines est borne en ABSOLU, a quelques fois le plancher du
jumeau ({plancher}), et la tolerance relative du gel ne dit pas sur quoi elle porte (D-BIS-1).""")
P("""La feuille, rejouee par machine 1 sur les sorties de machine 2 : journaux des deux etages
IDENTIQUES au canon ({c_l1_log}, {c_l2_log}) ; fichiers de verdict egaux champ a champ, statuts et
verdicts compris, sauf {fl_n} flottants ({fl_n1} a l'etage 1, {fl_n2} a l'etage 2) qui different d'au plus
{fl_pire} en relatif (O-BIS-1).""")

T("", "nn.10 DEFAUTS, ERRATA ET OBSERVATIONS (numeros de chantier ; numeros de serie au depot, E18)")
P("""D-BIS-1 (m1, gel bis, section 12). La tolerance du rejeu, "compare a BOCAL4 a 1e-3", ne nomme ni les
etats sur lesquels elle porte ni de plancher absolu. Elle tient sur l'etat juge ; elle ne peut pas tenir
sur un etat dont la largeur est a moins de mille fois le bruit entre machines. Sans effet sur le verdict.""",
  ind=2, suite=4)
P("""D-BIS-2 (m1, gel bis, section 7). La lecture des T-etats exige trois etats a plateau par point ; aucun
point n'en a plus de deux. Le gel ne disait pas ce que l'acte compte d'A-4 dans ce cas ; l'acte la compte
NON JUGEE. Sans effet sur le verdict (la section 7 n'en a pas).""", ind=2, suite=4)
P("""D-BIS-3 (m1, gel bis, section 11). A-3 est vraie a vide quand aucun point n'est qualifie ; une
annonce doit pouvoir etre fausse dans chaque issue de la cascade.""", ind=2, suite=4)
P("""R-BIS-1 (m1, ordre). Le gel ouvre le rejeu de machine 1 "seulement APRES un etage 1 qui tient".
Machine 1 l'a lance sur un message relaye, avant d'avoir authentifie verdict_etage1.json ; le fichier,
authentifie ensuite, dit TIENT. La condition etait remplie ; machine 1 ne l'avait pas verifiee sur piece
au moment de lancer. Sans effet sur les nombres.""", ind=2, suite=4)
P("""O-BIS-1 (m1). Les fichiers de verdict de la feuille ne sont pas reproductibles au bit d'une
plateforme a l'autre : moyennes geometriques et logarithmes passent par la bibliotheque mathematique.
Les journaux, arrondis, le sont. Aucun statut n'en depend.""", ind=2, suite=4)
P("""O-BIS-2 (m1). Sur BOCAL4, aux barreaux communs k = -5 a -2 du temoin, la sonde et le script du
diagnostic different de {diag_pire} au plus ({diag_ou}) -- plus que l'ecart entre machines sur le meme
code. Cause non recherchee. L'essai a blanc de machine 1 joint au lot du gel bis, fait sur les valeurs
du diagnostic, donnait |ln| <= {essai_pire} ; le run donne {tp_pire_ln}. Sans effet : le seuil est a
plus de 0.05.""", ind=2, suite=4)
P("""O-BIS-3 (m2, declare). Le dossier du run de BOCAL4 contient un fichier hors manifeste ({hors}) ; la
garde G-Q2 le nomme et ne l'ouvre pas.""", ind=2, suite=4)
P("""Defauts de machine 2 releves par machine 1 : aucun. Retraits : aucun.""", ind=2, suite=4)

T("", "nn.11 REGLES CANDIDATES SOUS (X) -- revue ECHUE depuis le 28/09 ; aucune n'est prise ici")
P("""{x1} (m1, d'apres D-BIS-1) La tolerance d'un rejeu entre machines se declare avec ce sur quoi elle
porte et avec son plancher absolu ; une tolerance relative seule ne vaut que loin du bruit du solveur.""",
  ind=2, suite=6)
P("""{x2} (m1, d'apres D-BIS-2 et D-BIS-3) Une lecture ou une annonce dont la condition peut ne pas se
realiser dit, au gel, ce que l'acte en compte quand elle ne se realise pas ; une annonce doit pouvoir
etre fausse dans chaque issue.""", ind=2, suite=6)
P("""{x3} (m1, d'apres R-BIS-1) Un rejeu se scelle par son empreinte avant que la machine qui rejoue ne
recoive les valeurs de l'autre, et ne se lance que sur une piece authentifiee ; l'acte dit qui a vu
quoi, et quand.""", ind=2, suite=6)
P("""Les {x_prec} precedentes ({x_detail}) attendent la meme revue.""")

T("", "nn.12 A ARBITRER PAR L'OPERATEUR, NON PRIS ICI")
P("""(i)   les numeros de serie de nn.10 (E18) ;""", ind=2, suite=6)
P("""(ii)  la revue (X), echue : {x_total} candidates ;""", ind=2, suite=6)
P("""(iii) le depot des lots de ce chantier (nn.14) : rien n'en est au registre ;""", ind=2, suite=6)
P("""(iv)  le garde-fou. Le gel dit : "et c'est le DERNIER ESSAI de la piste (0) sous cette forme", "ni
troisieme gel, ni autre echelle, ni autre temoin", "L'operateur peut lever ce garde-fou ; les machines,
non". Machine 1 ne demande pas qu'il soit leve. Le j = 5 a l'echelle etendue que machine 2 avait propose
reste non joue ;""", ind=2, suite=6)
P("""(v)   le reclassement. Le gel, section 13 : "toute phrase portant un Gamma depuis juillet est
reclassee ; reste le fait d'ordre de grandeur "le fantome fuit, le jumeau non", et seulement si le TP a
tenu". Le TP a tenu. L'inventaire des phrases concernees, piece par piece, n'est pas fait ici ; aucune
piece deposee n'est editee (PB-1) : le reclassement est un statut que ce delta porte, pas une
correction des actes ;""", ind=2, suite=6)
P("""(vi)  la suite de la branche quantique : aucune n'est proposee par cet acte.""", ind=2, suite=6)

T("", "nn.13 CONSEQUENCES POUR LE REGISTRE")
P("""Aucun verdict de manche n'est reecrit. Le gel bis ({c_gel_bis}) entre au registre comme JOUE,
verdict {cascade} ; la sonde v3, la feuille v2 et le banc v3, certifies ; le diagnostic de machine 2,
hors gel ; la certification ; le lot de la nuit ; le rejeu de machine 1. A partir de ce delta, une
largeur Gamma citee depuis juillet se lit comme une valeur rendue sous un absorbeur donne, bonne a
l'ordre de grandeur, et non comme une largeur intrinseque. Ce qui porte le fait d'ordre de grandeur dans
ce run : aux six points, G_run va de {g_min} a {g_max}, soit au moins {rap_plancher} fois le plancher du
jumeau aux memes geometries ({plancher}). Le perimetre s'ENUMERE depuis les citations de cet acte par
la feuille de perimetre du contresignataire et ne s'ecrit pas a la main (E-92-1).""")

T("", "nn.14 LE CANAL")
P("""Lots echanges depuis le delta 94 (canons), tous du 13/11. Machine 2 -- diagnostic {c_lot_diag} ;
certification du gel bis {c_lot_cert} ; resultat de la nuit {c_lot_nuit}. Machine 1 -- gel bis et
instrument {c_lot_gel} ; cet acte. Le lot de certification est arrive deux fois a machine 1, verifie
identique a l'octet, sans effet. Le registre est a fe10bfe, releve par machine 1 le 13/11. Le conteneur
de machine 1 a tenu du 12 au 13/11 ; les rejeux se refont depuis les lots et le clone.""")

T("", "nn.15 CE QUE CE DELTA NE FAIT PAS")
P("""Il ne dit pas que le fantome ne fuit pas, ni qu'il fuit a un taux donne. Il ne dit pas que les
valeurs de M17 sont fausses : il dit qu'elles ne sont pas qualifiees comme independantes de l'absorbeur
sous le critere gele. Il ne fait pas de nn.7 un resultat et ne relit rien sous d'autres seuils. Il ne
dit rien de l'unitarite, de l'auto-adjonction ni de la dynamique du systeme ferme : l'absorbeur ne
mesure qu'un taux sortant. Il ne dit rien d'autres degres, d'autres resonances, d'autres fractions que
ceux de la section 14 du gel. Il n'ouvre ni troisieme gel ni autre chantier. Il ne prend aucun numero,
n'adopte aucune regle, ne recommande aucun delta, n'edite aucune piece citee (PB-1), ne depose ni ZIP
ni MANIFEST.sha256.""")

T("", "nn.16 PIECES DE CE DELTA (lot machine 1 ; canon = convention B du manifeste)",
  "  journal_delta_nn_qualification_EB_bis_v1.md           cet acte",
  "  ecrire_acte_qualification_EB_bis_machine1_v1.py       le script qui pose nombres et canons",
  "  releve_acte_qualification_EB_bis_machine1_v1.py / .log  controle de sortie, pas un contreseing",
  "  rejeu_declare_point_39_20_machine1_v1.py              le pilote du rejeu declare",
  "  rejeu_declare_machine1.log, rejeu_point_39_20_F1G20_machine1.json   le journal et le scelle",
  "  ouverture_scelle_point_39_20_machine1_v1.py / .log    la comparaison a BOCAL4",
  "  banc_qui_tue_v3_rejeu_machine1.log                    le banc rejoue",
  "  lecture_m1/ (deux verdicts, deux journaux)            la feuille rejouee sur les sorties de m2",
  "  POUR_MACHINE2_acte_qualification_EB_bis_machine1_v1.md  la note d'accompagnement",
  "  fabrique_lot_acte_EB_bis_machine1_v1.py               la fabrique du lot",
  "  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.",
  "", "-- FIN journal_delta_nn_qualification_EB_bis_v1 --")

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
