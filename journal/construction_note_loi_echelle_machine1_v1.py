# -*- coding: utf-8 -*-
"""CONSTRUCTION DE LA NOTE « loi d'échelle » -- machine 1, v1, 2026-11-16. Hors chaîne.
Tous les nombres de la note sont lus dans les JSON des scripts du lot ; aucun n'est tapé. Les empreintes
(convention B) des pièces sont recalculées ici. Un jeton @@...@@ non remplacé, ou non utilisé, arrête le script.
Usage : python3 -I construction_note_loi_echelle_machine1_v1.py <dossier du lot> <registre> <sortie.md>"""
import sys, os, json, math, hashlib, unicodedata, re
LOT, REG, SORTIE = sys.argv[1:4]

def canon(path):
    b = open(path, "rb").read()
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        return hashlib.sha256(b).hexdigest()[:16]          # binaire : empreinte brute
    t = unicodedata.normalize("NFC", t).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def fr(x, nd=3, signe=False):
    s = ("%+.*f" if signe else "%.*f") % (nd, x)
    return s.replace(".", ",").replace("-", "−")

def sci(x, nd=2):
    m, e = ("%.*e" % (nd, x)).split("e")
    return "%s × 10^%d" % (m.replace(".", ","), int(e))

J = lambda nom: json.load(open(os.path.join(LOT, nom)))
CT, SP, FP, CA, LC, SV = J("phi_echelle_controle_v1.json"), J("superposition_v1.json"), J("forme_phi_v1.json"), J("carte_v1.json"), J("lecture_carte_v1.json"), J("sonde_vide_v1.json")
ST = json.load(open(os.path.join(REG, "journal", "structure_en_delta_v1.json")))
CL = J("controle_limite_v1.json")
V = {}

# --- section 2 : contrôles de Phi ---
c = CT["controles"]
V["n_ctl"] = str(len(c))
V["ctl_fc_mp_tous"] = sci(CT["pire_ecart_fc_mp"], 1)
prof = [x for x in c if x["ln_Phi_fc"] < -13.0]
V["ctl_fc_mp_prof"] = sci(max(abs(x["ln_Phi_fc"] - x["ln_Phi_mp"]) for x in prof), 1); V["n_ctl_prof"] = str(len(prof))
V["ctl_plus_profond"] = fr(-min(x["ln_Phi_fc"] for x in c), 1)
fl = [x for x in c if x["ln_Phi_flux"] == x["ln_Phi_flux"] and x["ln_Phi_fc"] > -46.0]
V["ctl_fc_flux"] = sci(max(abs(x["ln_Phi_fc"] - x["ln_Phi_flux"]) for x in fl), 1)
casse = [x for x in c if x["ln_Phi_flux"] == x["ln_Phi_flux"] and abs(x["ln_Phi_fc"] - x["ln_Phi_flux"]) > 0.01]
V["flux_casse_des"] = fr(-max(x["ln_Phi_fc"] for x in casse), 1)
V["ctl_signe"] = sci(CT["pire_ecart_signe"], 1) if CT["pire_ecart_signe"] > 0 else "0"
s62 = [s for s in ST["series"] if (s["n1"], s["n2"], s["kappa"]) == (6, 2, 0.30)][0]
gm = [l for l in s62["lignes"] if abs(abs(l["delta"]) - 0.0125) < 1e-9]
phi62 = math.exp([x for x in c if (x["n1"], x["n2"], x["kappa"]) == (6, 2, 0.30)][0]["ln_Phi_mp"])
V["phi62"] = sci(phi62, 4); V["g1_moins"] = sci([l for l in gm if l["delta"] < 0][0]["G1_sur_delta"], 4); V["g1_plus"] = sci([l for l in gm if l["delta"] > 0][0]["G1_sur_delta"], 4)
V["phi62_ecart_moy"] = sci(abs(phi62 / (0.5 * (gm[0]["G1_sur_delta"] + gm[1]["G1_sur_delta"])) - 1.0), 1)

petits = [x for x in CL["points"] if abs(x["delta"]) < 2e-4]; coef = [x["ecart"] / x["delta"] for x in CL["points"]]
V["lim_pire"] = sci(CL["pire_a_1e-4"], 1); V["lim_n"] = str(len(set((x["n1"], x["n2"]) for x in CL["points"])))
V["lim_coef_min"] = fr(min(coef), 2, True); V["lim_coef_max"] = fr(max(coef), 2, True)
par_etat = {}
for x in CL["points"]:
    par_etat.setdefault((x["n1"], x["n2"]), []).append(x["ecart"] / x["delta"])
V["lim_coef_disp"] = sci(max(max(v) - min(v) for v in par_etat.values()), 0)

# --- section 3 : superposition ---
E = SP["etats"]; D = [e for e in E if e["domaine"]]; H = [e for e in E if not e["domaine"]]
dom = SP["domaine"]; var = SP["variante"]
V["n_dom"] = str(dom["n"]); V["n_dom_100"] = str(sum(1 for e in D if e["source"] == "delta100")); V["n_dom_98"] = str(sum(1 for e in D if e["source"] == "delta98"))
V["n_juges_100"] = str(sum(1 for e in E if e["source"] == "delta100")); V["n_juges_98"] = str(sum(1 for e in E if e["source"] == "delta98"))
V["decades"] = fr(dom["decades"], 2); V["g_min"] = sci(min(e["Gamma_pl"] / abs(e["delta"]) for e in D)); V["g_max"] = sci(max(e["Gamma_pl"] / abs(e["delta"]) for e in D))
V["decades_plancher"] = fr(-math.log10(min(e["Gamma_pl"] / abs(e["delta"]) for e in D)), 1)
V["kappa_min"] = fr(min(e["kappa"] for e in D), 3); V["kappa_max"] = fr(max(e["kappa"] for e in D), 3)
V["delta_min"] = fr(min(abs(e["delta"]) for e in D), 3); V["delta_max"] = fr(max(abs(e["delta"]) for e in D), 3)
V["mb_min"] = str(min(e["m_bord"] for e in D)); V["mb_max"] = str(max(e["m_bord"] for e in D))
V["pente"] = fr(dom["pente"], 4)
xs = [e["ln_Phi"] for e in D]; ys = [e["ln_G_sur_delta"] for e in D]; mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys)); syy = sum((y - my) ** 2 for y in ys)
V["corr"] = fr(sxy / math.sqrt(sxx * syy), 4); V["sigma_droite"] = fr(math.sqrt(sum((y - my - dom["pente"] * (x - mx)) ** 2 for x, y in zip(xs, ys)) / len(xs)), 3)
V["r_med"] = fr(dom["r_abs_mediane"]); V["r_max"] = fr(dom["r_abs_max"]); V["r_max_facteur"] = fr(math.exp(dom["r_abs_max"]), 2)
rel = sorted(abs(e["r"] / e["ln_G_sur_delta"]) for e in D)
V["rel_med"] = fr(100 * rel[len(rel) // 2], 1); V["rel_max"] = fr(100 * rel[-1], 1)
sg = dom["signes"]; V["sg_neg"] = "%d sur %d" % (sg[0], sg[1]); V["sg_pos"] = "%d sur %d" % (sg[2], sg[3]); V["sg_tot"] = "%d états sur %d" % (sg[0] + sg[2], sg[1] + sg[3])
q3 = sorted(abs(e["r"] - e["r_chaine3"]) for e in D); V["q3_med"] = fr(q3[len(q3) // 2]); V["q3_max"] = fr(q3[-1])
V["stab_phi_med"] = fr(sorted(e["stab_Phi"] for e in D)[len(D) // 2], 4); V["stab_phi_max"] = fr(max(e["stab_Phi"] for e in D), 3)
V["rs_med"] = fr(var["r_abs_mediane"]); V["rs_max"] = fr(var["r_abs_max"]); V["rs_max_facteur"] = fr(math.exp(var["r_abs_max"]), 2)
em = var["etendue_mediane"]; V["et_neg_k"] = fr(em["neg_kappa"]); V["et_neg_e"] = fr(em["neg_etoile"]); V["et_pos_k"] = fr(em["pos_kappa"]); V["et_pos_e"] = fr(em["pos_etoile"])
V["rho_min"] = fr(100 * (min(e["rho"] for e in D) - 1.0), 2, True); V["rho_max"] = fr(100 * (max(e["rho"] for e in D) - 1.0), 2, True)
V["n_hors"] = str(len(H)); V["hors_med"] = fr(sorted(abs(e["r"]) for e in H)[len(H) // 2]); V["hors_max"] = fr(max(abs(e["r"]) for e in H))
V["ecart_kappa"] = sci(SP["controles"]["ecart_kappa"], 1) if SP["controles"]["ecart_kappa"] > 0 else "0"; V["sp_arith"] = sci(SP["controles"]["pire_arith"], 1)
lignes = ["| pièce | id | facteur | δ | états | r : min ; médiane ; max | r* : min ; médiane ; max |", "|---|---|---|---|---|---|---|"]
for x in SP["resume"]:
    lignes.append("| %s | %s | %s | %s | %d | %s ; %s ; %s | %s ; %s ; %s |" % (
        "delta 100" if x["source"] == "delta100" else "delta 98", x["id"], x["facteur"] or "—", fr(x["delta"], 3, True), x["etats"],
        fr(x["r"][0], 3, True), fr(x["r"][1], 3, True), fr(x["r"][2], 3, True), fr(x["r_etoile"][0], 3, True), fr(x["r_etoile"][1], 3, True), fr(x["r_etoile"][2], 3, True)))
V["table_superposition"] = "\n".join(lignes)

# --- section 4 : forme de Phi ---
V["I2"] = fr(2 * FP["I"], 6); V["Xc"] = fr(FP["X_c"], 6); V["M0_nu"] = fr(FP["M0_sur_nu0"], 5); V["M0_dg"] = fr(FP["M0_sur_delta_sur_g_puissance_2_3"], 5)
V["cst_nu"] = fr(FP["constante_en_nu0"], 4); V["cst_dg"] = fr(FP["constante_en_delta_sur_g"], 4)
B = FP["B"]
def ligB(n1, n2, M0):
    return [x for x in B if (x["n1"], x["n2"], x["M0"]) == (n1, n2, M0)][0]
lignes = ["| étiquette | c_L dérivé | pente mesurée au dernier doublement | d_L (lu à 4096 barreaux) | −ln Φ / (B M0) à 16 ; 4096 | erreur de la forme à trois termes à M0 = 16 ; 64 ; 1024 |", "|---|---|---|---|---|---|"]
dL = {}
for (n1, n2) in ((0, 0), (2, 1), (6, 2), (10, 3)):
    f = ligB(n1, n2, 4096); dL[(n1, n2)] = -f["reste3"]
    lignes.append("| (%d, %d) | %s | %s | %s | %s ; %s | %s ; %s ; %s |" % (n1, n2, fr(f["c_L"], 4), fr(-f["pente_par_doublement"], 4), fr(-f["reste3"], 3, True),
                  fr(ligB(n1, n2, 16)["rapport"], 3), fr(f["rapport"], 4),
                  fr(abs(ligB(n1, n2, 16)["reste3"] - f["reste3"]), 3), fr(abs(ligB(n1, n2, 64)["reste3"] - f["reste3"]), 3), fr(abs(ligB(n1, n2, 1024)["reste3"] - f["reste3"]), 4)))
V["table_B"] = "\n".join(lignes)
V["d00"] = fr(dL[(0, 0)], 3)
V["err00_4"] = fr(abs(ligB(0, 0, 4)["reste3"] - ligB(0, 0, 4096)["reste3"]), 3); V["err00_16"] = fr(abs(ligB(0, 0, 16)["reste3"] - ligB(0, 0, 4096)["reste3"]), 3)
V["err62_16"] = fr(abs(ligB(6, 2, 16)["reste3"] - ligB(6, 2, 4096)["reste3"]), 2); V["err103_16"] = fr(abs(ligB(10, 3, 16)["reste3"] - ligB(10, 3, 4096)["reste3"]), 2)
V["rap62_16"] = fr(ligB(6, 2, 16)["rapport"], 2); V["rap103_16"] = fr(ligB(10, 3, 16)["rapport"], 2); V["rap00_4096"] = fr(ligB(0, 0, 4096)["rapport"], 4)
C = FP["C"]
def ligC(n1, n2, k):
    return [x for x in C if (x["n1"], x["n2"]) == (n1, n2) and abs(x["kappa"] - k) < 1e-12][0]
lignes = ["| étiquette | κ | m_bord | −ln Φ | exposant local p | pente d ln Φ / d ln κ |", "|---|---|---|---|---|---|"]
for (n1, n2, ks) in ((0, 0, (0.03, 0.01, 0.001, 0.0001)), (6, 2, (0.30, 0.15, 0.10, 0.03, 0.001, 0.0001)), (10, 3, (0.40, 0.22, 0.10, 0.03, 0.001, 0.0001))):
    for k in ks:
        x = ligC(n1, n2, k)
        lignes.append("| (%d, %d) | %s | %d | %s | %s | %s |" % (n1, n2, ("%g" % k).replace(".", ","), x["m_bord"], fr(x["moins_ln_Phi"], 1), fr(x["p"], 3), fr(x["pente"], 1)))
V["table_C"] = "\n".join(lignes)
joue = [x["p"] for x in C if (x["n1"], x["n2"]) in ((6, 2), (10, 3)) and 0.0995 <= x["kappa"] <= 0.49]
V["p_joue_min"] = fr(min(joue), 2); V["p_joue_max"] = fr(max(joue), 2)
V["p_1e3_00"] = fr(ligC(0, 0, 0.001)["p"], 3); V["p_1e4_103"] = fr(ligC(10, 3, 0.0001)["p"], 3)
V["L_1e3_00"] = fr(ligC(0, 0, 0.001)["moins_ln_Phi"], 0)
V["dec_1e3_00"] = fr(ligC(0, 0, 0.001)["moins_ln_Phi"] / math.log(10), 0)
V["g_min_coef"] = fr((FP["M0_sur_delta_sur_g_puissance_2_3"] / 0.7) ** 1.5, 2)
V["g_min_035"] = sci((FP["M0_sur_delta_sur_g_puissance_2_3"] / 0.7) ** 1.5 * 0.035 ** 2.5, 1)
V["exp_max_coef"] = fr(2 * FP["I"] * 0.7, 2)

# --- section 5 : fraction du seuil ---
Fw = FP["F_wkb"]; Dd = FP["D"]
def chaine(f, j):
    nu = 5.241482788417793 * 2 ** j
    x = [y for y in Dd if abs(y["f"] - f) < 1e-9 and abs(y["nu0"] - nu) < 1e-6][0]
    return x
lignes = ["| f | F(f), intégrale | points tournants x = m / ν0* | chaîne, ν0* = 5,24 (κ) | ν0* = 41,9 (κ) | ν0* = 335 (κ) |", "|---|---|---|---|---|---|"]
for f in (0.0, 0.30, 0.50, 0.60, 0.70, 0.75, 0.80, 0.85, 1.00):
    w = Fw["%.2f" % f]
    cell = []
    for j in (0, 3, 6):
        x = chaine(f, j)
        cell.append("vide (%s)" % fr(x["kappa"], 2) if x["vide"] else "%s (%s)%s" % (fr(x["F"], 3), fr(x["kappa"], 3 if x["kappa"] < 0.1 else 2), "" if x["kappa"] < 0.5 else " †"))
    lignes.append("| %s | %s | %s | %s | %s | %s |" % (fr(f, 2), fr(w["F"], 4) if w else "pas de barrière", ("%s ; %s" % (fr(w["x_in"], 3), fr(w["x_out"], 3))) if w else "—", cell[0], cell[1], cell[2]))
V["table_D"] = "\n".join(lignes)
V["F0"] = fr(Fw["0.00"]["F"], 3); V["F05"] = fr(Fw["0.50"]["F"], 3); V["F07"] = fr(Fw["0.70"]["F"], 3); V["F08"] = fr(Fw["0.80"]["F"], 2); V["F085"] = fr(Fw["0.85"]["F"], 3)
V["F03"] = fr(Fw["0.30"]["F"], 3); V["ch03"] = fr(chaine(0.30, 6)["F"], 3); V["ch05"] = fr(chaine(0.50, 6)["F"], 3)
c07 = chaine(0.70, 0); V["ch07_camp"] = fr(c07["F"], 3); V["k07_camp"] = fr(c07["kappa"], 2)
V["ecart07_pc"] = fr(100 * (Fw["0.70"]["F"] / c07["F"] - 1.0), 1); V["ecart07_ln"] = fr((Fw["0.70"]["F"] - c07["F"]) * c07["nu0"], 2); V["ecart07_fact"] = fr(math.exp((Fw["0.70"]["F"] - c07["F"]) * c07["nu0"]), 1)
disp = [abs(y["F"] / Fw["%.2f" % y["f"]]["F"] - 1.0) for y in Dd if (not y["vide"]) and y["kappa"] > 0.5 and y["f"] in (0.5, 0.6, 0.7, 0.75) and y["nu0"] > 40]
V["disp_grand_kappa"] = fr(100 * max(disp), 0)

# --- section E : profondeur dans le domaine garde ---
lignes = ["| \\|δ\\| | étiquette | e = 0,3 : m_bord ; ν0* ; décades | e = 0,7 : m_bord ; ν0* ; décades |", "|---|---|---|---|"]
for x in FP["E"]:
    a, b = x["e_0.3"], x["e_0.7"]
    lignes.append("| %s | (%d, %d) | %d ; %s ; %s | %d ; %s ; %s |" % (fr(x["delta"], 3), x["n1"], x["n2"], a["m_bord"], fr(a["nu0"], 2), fr(a["decades"], 1), b["m_bord"], fr(b["nu0"], 2), fr(b["decades"], 1)))
V["table_E"] = "\n".join(lignes)
e035 = [x for x in FP["E"] if abs(x["delta"] - 0.035) < 1e-9]
V["dec035_min"] = fr(min(x["e_0.7"]["decades"] for x in e035), 0); V["dec035_max"] = fr(max(x["e_0.7"]["decades"] for x in e035), 0)

# --- section 6 : carte ---
cp = LC["comptes"]; V["n_carte"] = str(cp["points"]); V["n_carte_calc"] = str(cp["calcules"]); V["n_carte_non"] = str(cp["non_calcules"]); V["n_flux"] = str(cp["voie_flux"]); V["n_mp"] = str(cp["voie_mp"])
V["ctl_mat"] = "0" if max(CA["controles"]["matrice_contre_blocs"]) == 0.0 else sci(max(CA["controles"]["matrice_contre_blocs"]), 1); V["ctl_mp_flux"] = sci(CA["controles"]["mp_contre_flux"], 1)
MS = sorted(set(p["m_cible"] for p in CA["points"])); ES = [0.15, 0.3, 0.5, 0.7, 1.0]
for cle, nom in (("0,0", "table_carte_00"), ("6,2", "table_carte_62")):
    T = LC["tables"][cle]
    lignes = ["| barreaux | −ln Φ | " + " | ".join("e = %s" % fr(e, 2) for e in ES) + " |", "|---|---|" + "---|" * len(ES)]
    n1, n2 = [int(z) for z in cle.split(",")]
    for m in MS:
        lp = [p for p in CA["points"] if p["n1"] == n1 and p["n2"] == n2 and p["m_cible"] == m and not p["vide"]][0]["ln_Phi"]
        cells = []
        for e in ES:
            deux = []
            for sgn in (-1, 1):
                q = [x for x in T if x["m_cible"] == m and abs(x["e_cible"] - e) < 1e-9 and x["signe"] == sgn]
                deux.append("—" if not q else fr(q[0]["r3"], 3, True) + ("\\*" if q[0]["instable"] else ""))
            cells.append("%s ; %s" % (deux[0], deux[1]))
        lignes.append("| %d | %s | %s |" % (m, fr(-lp, 1), " | ".join(cells)))
    V[nom] = "\n".join(lignes)
V["n_inst"] = str(LC["instables"]["n"]); V["inst_mb_max"] = str(LC["instables"]["m_bord_max"]); V["inst_d_min"] = fr(LC["instables"]["delta_abs_min"], 4)
V["n_stab"] = str(LC["stables"]["n"]); V["stab_e_max"] = fr(LC["stables"]["e_bord_max"], 2); V["stab_d_max"] = fr(LC["stables"]["delta_abs_max"], 3)
b00, b62 = LC["bornes"]["0,0_m24_e1.0"], LC["bornes"]["6,2_m24_e1.0"]
V["n_long"] = str(b00["n"] + b62["n"]); V["r3_long_00"] = fr(abs(b00["pire_r3"]), 3); V["r3_long_62"] = fr(abs(b62["pire_r3"]), 3)
V["r32_long"] = fr(max(b00["pire_r3_moins_r2"], b62["pire_r3_moins_r2"]), 3)
def r3de(cle, m, e, sgn):
    return [x for x in LC["tables"][cle] if x["m_cible"] == m and abs(x["e_cible"] - e) < 1e-9 and x["signe"] == sgn][0]["r3"]
V["c62_12"] = fr(r3de("6,2", 12, 0.7, 1), 3, True); V["c62_64"] = fr(r3de("6,2", 64, 0.7, 1), 3, True)
V["c00_64m"] = fr(r3de("0,0", 64, 0.7, -1), 3, True); V["c00_64p"] = fr(r3de("0,0", 64, 0.7, 1), 3, True)
V["c00_48m"] = fr(r3de("0,0", 48, 0.7, -1), 3, True); V["c00_48p"] = fr(r3de("0,0", 48, 0.7, 1), 3, True)
V["lnphi_64_00"] = fr(-[p for p in CA["points"] if p["n1"] == 0 and p["m_cible"] == 64 and not p["vide"]][0]["ln_Phi"], 0)
V["stable_00"] = " ; ".join("%s barreaux : %s" % (m, ("aucun" if LC["stable_jusqu_a"]["0,0"][str(m)] is None else fr(LC["stable_jusqu_a"]["0,0"][str(m)], 3))) for m in MS)
V["stable_62"] = " ; ".join("%s barreaux : %s" % (m, ("aucun" if LC["stable_jusqu_a"]["6,2"][str(m)] is None else fr(LC["stable_jusqu_a"]["6,2"][str(m)], 3))) for m in MS)

# --- section 7 : le vide ---
lignes = ["| barreaux | κ | ν0* | Γ / \\|δ\\| (loi d'échelle) | forme fermée − chaîne (ln) | plus grand \\|r3\\| aux six δ | stabilité d'ordre 3 : min ; max |", "|---|---|---|---|---|---|---|"]
for m in (2, 3, 4, 5, 6):
    P = [p for p in SV["points"] if p["m_cible"] == m and not p["vide"]]
    lignes.append("| %d | %s | %s | %s | %s | %s | %s ; %s |" % (m, fr(P[0]["kappa"], 4), fr(P[0]["nu0"], 2), sci(math.exp(P[0]["ln_Phi"])), fr(P[0]["forme_fermee"] - P[0]["ln_Phi"], 3, True),
                  fr(max(abs(p["r3"]) for p in P), 3), fr(min(p["stab3"] for p in P), 3), fr(max(p["stab3"] for p in P), 3)))
V["table_vide"] = "\n".join(lignes)
P4 = [p for p in SV["points"] if p["m_cible"] in (3, 4, 5) and not p["vide"]]
V["vide_r3_max"] = fr(max(abs(p["r3"]) for p in P4), 3); V["vide_stab_max"] = fr(max(p["stab3"] for p in P4), 2)
V["vide_ff_max"] = fr(max(abs(p["forme_fermee"] - p["ln_Phi"]) for p in P4), 3)
V["vide_g_min"] = sci(min(p["g"] for p in P4), 1); V["vide_g_max"] = sci(max(p["g"] for p in P4), 1)
V["gabs_min"] = sci(min(e["Gamma_pl"] for e in E), 1)
V["vide_abs_3"] = sci(0.02 * math.exp([p for p in P4 if p["m_cible"] == 3][0]["ln_Phi"]), 1); V["vide_abs_5"] = sci(0.02 * math.exp([p for p in P4 if p["m_cible"] == 5][0]["ln_Phi"]), 1)
V["vide_G3"] = sci(math.exp([p for p in P4 if p["m_cible"] == 3][0]["ln_Phi"]), 1); V["vide_G5"] = sci(math.exp([p for p in P4 if p["m_cible"] == 5][0]["ln_Phi"]), 1)

# --- pièces ---
REGISTRE = ["scripts/m17_chaine_v17.py", "scripts/chaine_ordre2_bloc_machine1_v1.py", "scripts/ordre3_bloc_machine1_v1.py", "journal/lot_54ccae1713f92bc9__verdict_ordre3.json",
            "journal/ordre3_par_etat_v1.json", "journal/etape1_etalon_v1.json", "journal/structure_en_delta_v1.json", "journal/verdict_ter.json"]
V["pieces_registre"] = "\n".join("    %s  %s" % (canon(os.path.join(REG, p)), p) for p in REGISTRE)
DU_LOT = ["phi_echelle_machine1_v1.py", "phi_echelle_machine1_v1.log", "phi_echelle_controle_v1.json", "superposition_machine1_v1.py", "superposition_machine1_v1.log", "superposition_v1.json",
          "forme_phi_machine1_v1.py", "forme_phi_machine1_v1.log", "forme_phi_v1.json", "carte_machine1_v1.py", "carte_machine1_v1.log", "carte_v1.json",
          "lecture_carte_machine1_v1.py", "lecture_carte_machine1_v1.log", "lecture_carte_v1.json", "sonde_vide_machine1_v1.py", "sonde_vide_machine1_v1.log", "sonde_vide_v1.json",
          "controle_limite_machine1_v1.py", "controle_limite_machine1_v1.log", "controle_limite_v1.json",
          "figure_superposition_machine1_v1.py", "figure_superposition_loi_echelle_v1.png", "canon_fichiers_v1.py"]
V["pieces_lot"] = "\n".join("    %s  %s" % (canon(os.path.join(LOT, p)), p) for p in DU_LOT)

gabarit = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gabarit_note_loi_echelle_machine1_v1.md"), encoding="utf-8").read()
jetons = set(re.findall(r"@@([A-Za-z0-9_]+)@@", gabarit))
manquants = sorted(jetons - set(V)); inutiles = sorted(set(V) - jetons)
if manquants or inutiles:
    sys.exit("jetons sans valeur : %s ; valeurs sans jeton : %s" % (manquants, inutiles))
texte = gabarit
for k, v in V.items():
    texte = texte.replace("@@%s@@" % k, v)
assert "@@" not in texte
texte = unicodedata.normalize("NFC", texte)
open(SORTIE, "w", encoding="utf-8", newline="\n").write(texte)
print("note écrite : %s ; %d jetons ; empreinte B : %s ; %d octets" % (SORTIE, len(V), canon(SORTIE), os.path.getsize(SORTIE)))
