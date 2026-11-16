# -*- coding: utf-8 -*-
"""CONSTRUCTION DE LA NOTE « le vide, étape sans run » -- machine 1, v1, 2026-11-16. Hors chaîne.
Tous les nombres de la note sont lus dans les JSON des scripts du lot ; aucun n'est tapé. Les empreintes
(convention B) des pièces sont recalculées ici. Un jeton @@...@@ sans valeur, ou une valeur sans jeton, arrête le script.
Usage : python3 -I construction_note_vide_machine1_v1.py <dossier du lot> <registre> <note v1 de la loi d'échelle> <sortie.md>"""
import sys, os, json, math, hashlib, unicodedata, re, statistics
LOT, REG, NOTE_V1, SORTIE = sys.argv[1:5]

def canon(path):
    b = open(path, "rb").read()
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        return hashlib.sha256(b).hexdigest()[:16]
    t = unicodedata.normalize("NFC", t).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def fr(x, nd=3, signe=False):
    s = ("%+.*f" if signe else "%.*f") % (nd, x)
    return s.replace(".", ",").replace("-", "−")

def sci(x, nd=1):
    m, e = ("%.*e" % (nd, x)).split("e")
    return "%s × 10^%d" % (m.replace(".", ","), int(e))

J = lambda nom: json.load(open(os.path.join(LOT, nom)))
AA, CJ, TV, MD, CA, AB, PP = J("absorbeur_adapte_v1.json"), J("controle_joues_absorbeur_v1.json"), J("temoin_lecteur_vide_v1.json"), J("mandataire_absorbeur_2D_v1.json"), J("carte_adaptee_v1.json"), J("apres_barriere_v1.json"), J("procede_lecteur_profond_v1.json")
V = {}
med = statistics.median

# --- le témoin sans fantôme ---
cas = TV["cas"]
V["tv_lectures"] = str(sum(c["lectures"] for c in cas)); V["tv_suivies"] = str(sum(c["suivies"] for c in cas))
V["tv_max"] = sci(max(c["plus_grande_largeur"] for c in cas)); V["tv_min"] = sci(min(min(a["gamma"]) for c in cas for a in c["absorbeurs"].values()))
V["tv_duree_min"] = fr(min(c["duree_totale_s"] for c in cas), 0); V["tv_duree_max"] = fr(max(c["duree_totale_s"] for c in cas), 0)
V["tv_N_min"] = str(min(a["N"] for c in cas for a in c["absorbeurs"].values())); V["tv_N_max"] = str(max(a["N"] for c in cas for a in c["absorbeurs"].values()))
lignes = ["| barrière du vide | w2 | g | r_c | boîtes N | lectures suivies | largeur du jumeau : de ... à ... | durée (machine 1) |", "|---|---|---|---|---|---|---|---|"]
for c in cas:
    g_ = [x for a in c["absorbeurs"].values() for x in a["gamma"]]
    lignes.append("| %d barreaux | %s | %s | %d | %d à %d | %d sur %d | %s à %s | %s s |" % (c["m_bord_du_vide"], c["w2"], sci(c["g"], 2), c["r_c"], min(a["N"] for a in c["absorbeurs"].values()),
                  max(a["N"] for a in c["absorbeurs"].values()), c["suivies"], c["lectures"], sci(min(g_)), sci(max(g_)), fr(c["duree_totale_s"], 0)))
V["table_temoin"] = "\n".join(lignes)

# --- le procédé du lecteur sur une chaîne profonde ---
lignes = ["| barreaux | sites | ln Φ, fraction continue | ln Φ, routine du lecteur | écart | itérations |", "|---|---|---|---|---|---|"]
for p in PP["points"]:
    lignes.append("| %d | %d | %s | %s | %s | %d |" % (p["m_cible"], p["sites"], fr(p["ln_Phi_fc"], 6), fr(p["ln_Phi_lecteur"], 6), "0" if p["ecart"] == 0 else sci(abs(p["ecart"])), p["iterations"]))
V["table_procede"] = "\n".join(lignes)
V["pp_pire"] = sci(PP["pire_ecart"]); V["pp_profond"] = fr(-min(p["ln_Phi_lecteur"] for p in PP["points"]), 1)
V["pp_decades"] = fr(-min(p["ln_Phi_lecteur"] for p in PP["points"]) / math.log(10), 0)
V["pp_suivis"] = "%d sur %d" % (sum(1 for p in PP["points"] if p["suivi"]), len(PP["points"]))

# --- le mandataire ---
dep = [c for c in MD["cas"] if c["regle"].startswith("depot")]; sau = [c for c in MD["cas"] if not c["regle"].startswith("depot")]
V["md_dep"] = "%d séries sur %d" % (sum(1 for c in dep if c["plateau"]), len(dep)); V["md_sau"] = "%d sur %d" % (sum(1 for c in sau if c["plateau"]), len(sau))
V["md_dep_r"] = fr(max(abs(x) for c in dep if c["plateau"] for x in c["r_fenetre"]), 4); V["md_sau_r"] = fr(max(abs(x) for c in sau if c["plateau"] for x in c["r_fenetre"]), 3)
V["md_cas"] = str(len(set((c["m_cible"], c["delta"]) for c in MD["cas"])))
f2 = [c["fenetre_k0"] for c in dep if c["absorbeur"] in ("A", "B", "D")]; f1 = [c["fenetre_k0"] for c in dep if c["absorbeur"] == "C"]
V["md_k_F2"] = "k = %s à %s" % (fr(min(f2), 0, True), fr(max(f2) + 4, 0, True)); V["md_k_F1"] = "k = %s à %s" % (fr(min(f1), 0, True), fr(max(f1) + 4, 0, True))
faible = [c["r"][-1] for c in dep if c["absorbeur"] in ("A", "B", "D")]
V["md_k8_min"] = fr(min(faible), 2, True); V["md_k8_max"] = fr(max(faible), 2, True)

# --- diagnostic de la règle déposée ---
lignes = ["| cas | ordre | " + " | ".join("ef = %s" % ("%g" % e).replace(".", ",") for e in AA["A"][0]["ef"]) + " |", "|---|---|" + "---|" * len(AA["A"][0]["ef"])]
for a in AA["A"]:
    lignes.append("| vide, %d barreaux, δ = %s | %d | %s |" % (a["m_cible"], fr(a["delta"], 3, True), a["ordre"], " | ".join(fr(x, 3, True) for x in a["r"])))
V["table_diag"] = "\n".join(lignes)
o1 = [a for a in AA["A"] if a["ordre"] == 1]
V["diag_faible"] = fr(max(a["r"][0] for a in o1), 2, True); V["diag_fort"] = fr(min(a["r"][6] for a in o1), 2, True)
V["diag_ef_faible"] = ("%g" % AA["A"][0]["ef"][0]).replace(".", ","); V["diag_ef_fort"] = ("%g" % AA["A"][0]["ef"][6]).replace(".", ",")

# --- le vide sous l'absorbeur adapté ---
B = AA["B"]
lignes = ["| barreaux | κ | ln Φ* | Φ* − Φ déposée | forme fermée − Φ* | plus grand \\|r3*\\| | plus grand \\|r3* − r2*\\| | étendue d'ordre 3 : max | règle déposée − plateau : de ... à ... | Γ3* / \\|δ\\| |", "|---|---|---|---|---|---|---|---|---|---|"]
par = {}
for b in B:
    par.setdefault(b["m_cible"], []).append(b)
for m in sorted(par):
    L = par[m]; r3 = [b["ordres"]["3"]["plateau"] - b["ln_Phi_etoile"] for b in L]; r2 = [b["ordres"]["2"]["plateau"] - b["ln_Phi_etoile"] for b in L]
    dd = [b["ln_G3_depose"] - b["ordres"]["3"]["plateau"] for b in L]
    lignes.append("| %d | %s | %s | %s | %s | %s | %s | %s | %s à %s | %s |" % (m, fr(L[0]["kappa"], 4), fr(L[0]["ln_Phi_etoile"], 3), fr(L[0]["ln_Phi_etoile"] - L[0]["ln_Phi_deposee"], 3, True),
                  fr(L[0]["forme_fermee"] - L[0]["ln_Phi_etoile"], 3, True), fr(max(abs(x) for x in r3), 3), fr(max(abs(a - b_) for a, b_ in zip(r3, r2)), 4),
                  fr(max(b["ordres"]["3"]["etendue"] for b in L), 4), fr(min(dd), 3, True), fr(max(dd), 3, True), sci(math.exp(L[0]["ln_Phi_etoile"]))))
V["table_vide"] = "\n".join(lignes)
B36 = [b for b in B if 3 <= b["m_cible"] <= 6]; B2 = [b for b in B if b["m_cible"] == 2]
V["vide_et_max"] = fr(max(b["ordres"]["3"]["etendue"] for b in B36), 4); V["vide_et_max_2"] = fr(max(b["ordres"]["3"]["etendue"] for b in B2), 3)
V["vide_r3_max"] = fr(max(abs(b["ordres"]["3"]["plateau"] - b["ln_Phi_etoile"]) for b in B36), 3)
V["vide_r3_pc"] = fr(100 * (math.exp(max(abs(b["ordres"]["3"]["plateau"] - b["ln_Phi_etoile"]) for b in B36)) - 1.0), 1)
V["vide_r32_max"] = fr(max(abs(b["ordres"]["3"]["plateau"] - b["ordres"]["2"]["plateau"]) for b in B36), 4)
V["vide_ff_min"] = fr(min(b["forme_fermee"] - b["ln_Phi_etoile"] for b in B), 3); V["vide_ff_max"] = fr(max(b["forme_fermee"] - b["ln_Phi_etoile"] for b in B), 3)
V["vide_dphi_min"] = fr(min(b["ln_Phi_etoile"] - b["ln_Phi_deposee"] for b in B), 3, True); V["vide_dphi_max"] = fr(max(b["ln_Phi_etoile"] - b["ln_Phi_deposee"] for b in B), 3, True)
V["vide_dep_pire"] = fr(max(abs(b["ln_G3_depose"] - b["ordres"]["3"]["plateau"]) for b in B), 2)
V["vide_et_phi"] = fr(max(b["etendue_Phi_etoile"] for b in B), 4)
V["vide_g_min"] = sci(min(b["g"] for b in B36)); V["vide_g_max"] = sci(max(b["g"] for b in B36))
V["vide_G_max"] = sci(max(b["Gamma3_etoile"] for b in B36)); V["vide_G_min"] = sci(min(b["Gamma3_etoile"] for b in B36))
V["n_var"] = str(len(AA["variantes"]))
Cx = AA["C"]
V["exc_dphi_min"] = fr(min(c["ln_Phi_etoile"] - c["ln_Phi"] for c in Cx), 3, True); V["exc_dphi_max"] = fr(max(c["ln_Phi_etoile"] - c["ln_Phi"] for c in Cx), 3, True); V["exc_n"] = str(len(Cx))
V["exc_et_max"] = fr(max(c["etendue"] for c in Cx), 3)

# --- la carte rejouée ---
P = [p for p in CA["points"] if not p["vide"]]
V["ca_n"] = str(len(P)); V["ca_inst_dep"] = str(sum(1 for p in P if p["instable_depose"])); V["ca_inst_ada"] = str(sum(1 for p in P if p["instable_adapte"]))
V["ca_deja"] = str(sum(1 for p in P if p["instable_adapte"] and p["instable_depose"]))
V["ca_gueris"] = str(sum(1 for p in P if p["instable_depose"] and not p["instable_adapte"])); V["ca_nouveaux"] = str(sum(1 for p in P if p["instable_adapte"] and not p["instable_depose"]))
for cle, lab in (("00", (0, 0)), ("62", (6, 2))):
    L = [p for p in P if (p["n1"], p["n2"]) == lab and p["instable_adapte"]]; S = [p for p in P if (p["n1"], p["n2"]) == lab and not p["instable_adapte"]]
    V["ca_dmin_" + cle] = fr(min(abs(p["delta"]) for p in L), 4); V["ca_n_inst_" + cle] = str(len(L))
prof = [p for p in P if (p["n1"], p["n2"]) == (0, 0) and p["m_cible"] in (8, 12, 16) and abs(p["delta"]) <= 0.02 and not p["instable_adapte"]]
lignes = ["| barreaux | δ | ln Φ* | r3* | étendue | Γ3* / \\|δ\\| | Γ3* |", "|---|---|---|---|---|---|---|"]
for p in sorted(prof, key=lambda p: (p["m_cible"], p["delta"])):
    lg = p["ln_Phi_etoile"] + p["r3_etoile"]
    lignes.append("| %d | %s | %s | %s | %s | %s | %s |" % (p["m_cible"], fr(p["delta"], 4, True), fr(p["ln_Phi_etoile"], 2), fr(p["r3_etoile"], 3, True), fr(p["etendue"], 4), sci(math.exp(lg)), sci(abs(p["delta"]) * math.exp(lg))))
V["table_profond"] = "\n".join(lignes)
V["prof_n"] = str(len(prof)); V["prof_et_max"] = fr(max(p["etendue"] for p in prof), 4); V["prof_r3_max"] = fr(max(abs(p["r3_etoile"]) for p in prof), 3)
V["prof_G_min"] = sci(min(abs(p["delta"]) * math.exp(p["ln_Phi_etoile"] + p["r3_etoile"]) for p in prof))

# --- après la barrière ---
lignes = ["| point | g | ordre 1 : r (étendue) | ordre 2 | ordre 3 | saut > 1 au site | t + T3 change de signe au site | fin de la plus longue variante |", "|---|---|---|---|---|---|---|---|"]
for a in AB["A"]:
    o = a["ordres"]
    lignes.append("| (%d, %d), %d barreaux, δ = %s | %s | %s (%s) | %s (%s) | %s (%s) | %s | %s | %d |" % (a["n1"], a["n2"], a["m_cible"], fr(a["delta"], 4, True), sci(a["g"], 2),
                  fr(o["1"]["r"], 3, True), fr(o["1"]["etendue"], 3), fr(o["2"]["r"], 3, True), fr(o["2"]["etendue"], 3), fr(o["3"]["r"], 3, True), fr(o["3"]["etendue"], 3),
                  a["site_saut_1"], a["site_signe"] if a["site_signe"] is not None else "aucun", a["dernier_site"]))
V["table_apres"] = "\n".join(lignes)
V["ab_n"] = str(len(AB["A"])); V["ab_et12_max"] = fr(max(max(a["ordres"]["1"]["etendue"], a["ordres"]["2"]["etendue"]) for a in AB["A"]), 3)
V["ab_et3_min"] = fr(min(a["ordres"]["3"]["etendue"] for a in AB["A"]), 2); V["ab_et3_max"] = fr(max(a["ordres"]["3"]["etendue"] for a in AB["A"]), 2)
V["ab_signe"] = "%d sur %d" % (sum(1 for a in AB["A"] if a["site_signe"] is not None), len(AB["A"]))
lignes = ["| cas | m_bord | t_s = 0,15 : m_s, r | t_s = 0,30 | t_s = 0,50 | écart entre les trois | sans coupure : r (étendue) | 2D lue | déposée |", "|---|---|---|---|---|---|---|---|---|"]
for b in AB["B"]:
    c = b["coupures"]
    tete, queue = b["cas"].replace("carte ", "").replace("joue ", "joué ").rsplit(" ", 1)
    etiq = tete[tete.index("("):tete.index(")") + 1]
    tete = tete.replace(etiq, etiq.replace(",", ", ")).replace(" (", ", (").replace(") ", "), ")
    nom_cas = tete.lstrip(", ") + ", δ = " + queue.replace(".", ",").replace("-", "−")
    lignes.append("| %s | %d | %s | %s | %s | %s | %s (%s) | %s | %s |" % (nom_cas, b["m_bord"],
                  " | ".join("%d, %s" % (x["m_s"], fr(x["r"], 3, True)) for x in c[:1]), "%d, %s" % (c[1]["m_s"], fr(c[1]["r"], 3, True)), "%d, %s" % (c[2]["m_s"], fr(c[2]["r"], 3, True)),
                  fr(b["ecart"], 3), fr(b["sans_coupure"]["r"], 3, True), fr(b["sans_coupure"]["etendue"], 3),
                  fr(b["r_2D"], 3, True) if b["r_2D"] is not None else "—", fr(b["r_depose"], 3, True) if b["r_depose"] is not None else "—"))
V["table_coupure"] = "\n".join(lignes)
jo = {b["cas"].split()[1]: b for b in AB["B"] if b["cas"].startswith("joue")}
V["cp_N1"] = fr(jo["N1"]["ecart"], 2); V["cp_autres"] = fr(max(jo[k]["ecart"] for k in ("BP", "P1", "C1")), 3)
V["cp_et_max"] = fr(max(x["etendue"] for b in AB["B"] for x in b["coupures"]), 3)

# --- les états joués ---
E = CJ["etats"]
et = sorted(e["etendue"] for e in E); dd = [e["etoile_moins_depose"] for e in E]
V["cj_n"] = str(len(E)); V["cj_et_med"] = fr(med(et), 3); V["cj_et_d9"] = fr(et[int(0.9 * len(et))], 3); V["cj_et_max"] = fr(et[-1], 2)
V["cj_d_med"] = fr(med(dd), 4, True); V["cj_d_min"] = fr(min(dd), 3, True); V["cj_d_max"] = fr(max(dd), 3, True); V["cj_d_neg"] = "%d états sur %d" % (sum(1 for x in dd if x < 0), len(dd))
V["cj_q_dep_med"] = fr(med([abs(e["ln_q3_depose"]) for e in E]), 4); V["cj_q_ada_med"] = fr(med([abs(e["ln_q3_etoile"]) for e in E]), 4)
V["cj_q_dep_max"] = fr(max(abs(e["ln_q3_depose"]) for e in E), 4); V["cj_q_ada_max"] = fr(max(abs(e["ln_q3_etoile"]) for e in E), 4)
V["cj_hors_dep"] = str(sum(1 for e in E if abs(e["ln_q3_depose"]) > e["tolerance_E1"])); V["cj_hors_ada"] = str(sum(1 for e in E if abs(e["ln_q3_etoile"]) > e["tolerance_E1"]))
V["cj_mieux"] = "%d états sur %d" % (sum(1 for e in E if abs(e["ln_q3_etoile"]) < abs(e["ln_q3_depose"])), len(E))
pos = [e for e in E if e["delta"] > 0]; neg = [e for e in E if e["delta"] < 0]
V["cj_mieux_pos"] = "%d sur %d" % (sum(1 for e in pos if abs(e["ln_q3_etoile"]) < abs(e["ln_q3_depose"])), len(pos)); V["cj_mieux_neg"] = "%d sur %d" % (sum(1 for e in neg if abs(e["ln_q3_etoile"]) < abs(e["ln_q3_depose"])), len(neg))
lignes = ["| pièce | id | δ | états | étendue max | adapté − déposé : min ; médiane ; max | \\|ln q3\\| max, déposé | \\|ln q3\\| max, adapté |", "|---|---|---|---|---|---|---|---|"]
for r in CJ["resume"]:
    lignes.append("| %s | %s | %s | %d | %s | %s ; %s ; %s | %s | %s |" % ("delta 100" if r["source"] == "delta100" else "delta 98", r["id"], fr(r["delta"], 3, True), r["etats"], fr(r["etendue_max"], 3),
                  fr(r["diff"][0], 3, True), fr(r["diff"][1], 3, True), fr(r["diff"][2], 3, True), fr(r["q3_depose_max"], 4), fr(r["q3_etoile_max"], 4)))
V["table_joues"] = "\n".join(lignes)
P1 = [r for r in CJ["resume"] if r["id"] == "P1"][0]; V["cj_P1_dep"] = fr(P1["q3_depose_max"], 4); V["cj_P1_ada"] = fr(P1["q3_etoile_max"], 4)
N2 = [r for r in CJ["resume"] if r["id"] == "N2"][0]; V["cj_N2_dep"] = fr(N2["q3_depose_max"], 4); V["cj_N2_ada"] = fr(N2["q3_etoile_max"], 4)
SUP = {(e["source"], e["id"], e["rang"]): e for e in J("superposition_v1.json")["etats"]}
st3 = [SUP[(e["source"], e["id"], e["rang"])]["stab3"] for e in E]
V["cj_stab3_med"] = fr(med(st3), 4)
V["cj_d_sous_deux"] = "%d états sur %d" % (sum(1 for e, x in zip(E, st3) if abs(e["etoile_moins_depose"]) < x and abs(e["etoile_moins_depose"]) < e["etendue"]), len(E))
V["tv_decades"] = "%d" % math.floor(math.log10(min(b["Gamma3_etoile"] for b in B36) / max(c["plus_grande_largeur"] for c in cas)))
V["cj_d_med_abs"] = fr(abs(med(dd)), 4); V["cj_pire_neg"] = "%d sur %d" % (sum(1 for e in neg if abs(e["ln_q3_etoile"]) > abs(e["ln_q3_depose"])), len(neg))

# --- pièces ---
V["canon_note_v1"] = canon(NOTE_V1)
REGISTRE = ["scripts/m17_chaine_v17.py", "scripts/chaine_ordre2_bloc_machine1_v1.py", "scripts/ordre3_bloc_machine1_v1.py", "scripts/sonde_lecteur_gel_loi_machine1_v1.py",
            "scripts/sonde_dense_gel_loi_machine1_v1.py", "scripts/lecture_qualification_EB_ter_machine1_v1.py"]
V["pieces_registre"] = "\n".join("    %s  %s" % (canon(os.path.join(REG, p)), p) for p in REGISTRE)
REPRISES = ["phi_echelle_machine1_v1.py", "carte_machine1_v1.py", "carte_v1.json", "superposition_v1.json", "forme_phi_v1.json", "canon_fichiers_v1.py"]
V["pieces_reprises"] = "\n".join("    %s  %s" % (canon(os.path.join(LOT, p)), p) for p in REPRISES)
DU_LOT = ["absorbeur_adapte_machine1_v1.py", "absorbeur_adapte_machine1_v1.log", "absorbeur_adapte_v1.json", "controle_joues_absorbeur_machine1_v1.py", "controle_joues_absorbeur_machine1_v1.log",
          "controle_joues_absorbeur_v1.json", "carte_adaptee_machine1_v1.py", "carte_adaptee_machine1_v1.log", "carte_adaptee_v1.json", "apres_barriere_machine1_v1.py", "apres_barriere_machine1_v1.log",
          "apres_barriere_v1.json", "temoin_lecteur_vide_machine1_v1.py", "temoin_lecteur_vide_machine1_v1.log", "temoin_lecteur_vide_v1.json", "procede_lecteur_profond_machine1_v1.py",
          "procede_lecteur_profond_machine1_v1.log", "procede_lecteur_profond_v1.json", "mandataire_absorbeur_2D_machine1_v1.py", "mandataire_absorbeur_2D_machine1_v1.log", "mandataire_absorbeur_2D_v1.json"]
V["pieces_lot"] = "\n".join("    %s  %s" % (canon(os.path.join(LOT, p)), p) for p in DU_LOT)

gabarit = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gabarit_note_vide_machine1_v1.md"), encoding="utf-8").read()
jetons = set(re.findall(r"@@([A-Za-z0-9_]+)@@", gabarit))
manquants = sorted(jetons - set(V)); inutiles = sorted(set(V) - jetons)
if manquants or inutiles:
    sys.exit("jetons sans valeur : %s ; valeurs sans jeton : %s" % (manquants, inutiles))
texte = gabarit
for k, v in V.items():
    texte = texte.replace("@@%s@@" % k, v)
assert "@@" not in texte
open(SORTIE, "w", encoding="utf-8", newline="\n").write(unicodedata.normalize("NFC", texte))
print("note écrite : %s ; %d jetons ; empreinte B : %s ; %d octets" % (SORTIE, len(V), canon(SORTIE), os.path.getsize(SORTIE)))
