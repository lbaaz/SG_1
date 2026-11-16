# -*- coding: utf-8 -*-
"""Construit la note hors chaine de la reprise de la piste (0) : chaque nombre est calcule ici depuis les sorties.
Usage : python3 -I construction_note_piste0_reprise_machine1_v1.py <dossier du chantier> <gabarit> <sortie.md> <clone du registre>"""
import sys, os, json, math, re, hashlib, unicodedata
D, GABARIT, SORTIE, CLONE = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def fr(x, n=4):
    return ("%.*f" % (n, x)).replace(".", ",")
ORDRE = ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"]
NOM = {"39_20": "1,95", "197_100": "1,97", "99_50": "1,98", "101_50": "2,02", "203_100": "2,03", "41_20": "2,05"}
P = {}
for f in ("exploration_v1.json", "exploration_v1b.json"):
    P.update(json.load(open(os.path.join(D, f)))["points"])
assert sorted(P) == sorted(ORDRE), sorted(P)
CH = json.load(open(os.path.join(D, "chaine_sans_boite_v1.json")))
KS = list(range(-5, 15))
def fenetre(vals, ks=None):              # regle du gel bis : meilleure fenetre de cinq k consecutifs
    ks = KS if ks is None else ks
    best = None
    for i in range(len(ks) - 4):
        f = [vals[k] for k in ks[i:i + 5]]
        e = max(f) / min(f)
        if best is None or e < best[0]:
            best = (e, ks[i], math.exp(sum(math.log(x) for x in f) / 5.0))
    return best[0] - 1.0, best[1], best[2]
def suite(vals, tol):                    # plus longue suite de k consecutifs tenant dans tol
    best = (0, None)
    for i in range(len(KS)):
        for j in range(i, len(KS)):
            f = [vals[k] for k in KS[i:j + 1]]
            if max(f) / min(f) - 1.0 <= tol:
                if j - i + 1 > best[0]: best = (j - i + 1, KS[i])
            else:
                break
    return best
def traj(nom, cle):
    c = P[nom]["cfg"][cle]; G = P[nom]["G_run"]
    return {k: c["traj"][str(k)]["gamma"] / G for k in KS}
V = {}
# --- tableau 1 : cinq absorbeurs longs ---
LONGS = [("F2_r+0_L60", "F2, 60"), ("F2_r+0_L80", "F2, 80"), ("F1_r+0_L80", "F1, 80"), ("F3_r+0_L60", "F3, 60"), ("F1_r+10_L60", "F1 translaté, 60")]
lignes = []; pire_etal = {c: 0.0 for c, _ in LONGS}; ecart_cfg = []; m17 = []; chaine = []; n05 = {c: [] for c, _ in LONGS}; gel98 = []
for nom in ORDRE:
    cells = []; vals = []
    for cle, _ in LONGS:
        e, k0, v = fenetre(traj(nom, cle)); s = suite(traj(nom, cle), 0.005)
        pire_etal[cle] = max(pire_etal[cle], e); n05[cle].append(s[0]); vals.append(v)
        cells.append("%s (%s %%, %d)" % (fr(v), fr(100 * e, 2), s[0]))
    ref = vals[1]                                            # F2 a 80 couches
    ecart_cfg.append(max(vals) / min(vals) - 1.0); m17.append(1.0 / ref)
    chaine.append(CH[nom]["plateau"] / (ref * P[nom]["G_run"])); gel98.append(CH[nom]["lecture_du_gel_98"] / CH[nom]["plateau"])
    lignes.append("| %s | %s | %s | %s |" % (NOM[nom], " | ".join(cells), fr(1.0 / ref), fr(chaine[-1])))
V["tableau1"] = "\n".join(lignes)
for cle, _ in LONGS:
    assert pire_etal[cle] <= 0.05, (cle, pire_etal[cle])       # tous a PLATEAU au sens du gel bis
V["pire_etal_F2_60"] = fr(100 * pire_etal["F2_r+0_L60"], 2); V["pire_etal_F2_80"] = fr(100 * pire_etal["F2_r+0_L80"], 2)
V["pire_etal_F1_80"] = fr(100 * pire_etal["F1_r+0_L80"], 2); V["pire_etal_F3_60"] = fr(100 * pire_etal["F3_r+0_L60"], 2)
V["pire_etal_FT_60"] = fr(100 * pire_etal["F1_r+10_L60"], 2)
V["pire_etal_tous"] = fr(100 * max(pire_etal.values()), 2)
V["n05_F2_60_min"] = min(n05["F2_r+0_L60"]); V["n05_F2_60_max"] = max(n05["F2_r+0_L60"])
V["n05_F2_80_min"] = min(n05["F2_r+0_L80"]); V["n05_F2_80_max"] = max(n05["F2_r+0_L80"])
V["n05_F1_80_min"] = min(n05["F1_r+0_L80"]); V["n05_F1_80_max"] = max(n05["F1_r+0_L80"])
V["ecart_cfg_max"] = fr(100 * max(ecart_cfg), 2); V["ecart_cfg_min"] = fr(100 * min(ecart_cfg), 2)
V["m17_min"] = fr(min(m17)); V["m17_max"] = fr(max(m17))
V["m17_ecart_max"] = fr(100 * max(abs(x - 1.0) for x in m17), 1)
V["chaine_min"] = fr(min(chaine)); V["chaine_max"] = fr(max(chaine))
V["gel98_min"] = fr(100 * (min(gel98) - 1.0), 2); V["gel98_max"] = fr(100 * (max(gel98) - 1.0), 2)
V["chaine_etal_max"] = fr(100 * max(CH[n]["etalement"] for n in ORDRE), 2)
# --- tableau 2 : la longueur, critere du gel bis (etalement de la meilleure fenetre, seuil 5 %) ---
lignes = []; nb = {}
for forme in ("F1", "F2", "F3"):
    for L in (20, 30, 40, 60, 80):
        cle = "%s_r+0_L%d" % (forme, L)
        if cle not in P[ORDRE[0]]["cfg"]:
            continue
        es = [fenetre(traj(nom, cle), list(range(-5, 13)))[0] for nom in ORDRE]      # echelle du gel bis : k = -5 a 12
        nb[cle] = sum(e <= 0.05 for e in es)
        lignes.append("| %s | %d | %s | %d sur 6 |" % (forme, L, " | ".join(fr(100 * e, 2) for e in es), nb[cle]))
V["tableau2"] = "\n".join(lignes)
assert nb["F1_r+0_L20"] == 1 and nb["F1_r+0_L30"] == 5 and nb["F2_r+0_L20"] == 1, nb    # ce que la nuit bis a rendu
for cle in ("F1_r+0_L40", "F1_r+0_L60", "F1_r+0_L80", "F2_r+0_L40", "F2_r+0_L60", "F2_r+0_L80", "F3_r+0_L40", "F3_r+0_L60"):
    V["nb_" + cle.replace("_r+0_", "_")] = nb[cle]
V["nb_F2_L30"] = nb["F2_r+0_L30"]; V["nb_F3_L30"] = nb["F3_r+0_L30"]
# --- cote fort : les trajectoires F1 ne dependent pas de la longueur ; bord ramene vers l'etat ---
co = 0.0
for nom in ORDRE:
    for k in range(-5, 3):
        v = [traj(nom, "F1_r+0_L%d" % L)[k] for L in (20, 30, 40, 60, 80)]
        co = max(co, max(v) / min(v) - 1.0)
V["coinc_F1"] = fr(100 * co, 2)
assert co < 0.005, co
rm = [max(traj(nom, "F1_r-20_L60").values()) for nom in ORDRE]
V["rm20_min"] = fr(min(rm), 1); V["rm20_max"] = fr(max(rm), 1)
rm10 = [fenetre(traj(nom, "F1_r-10_L50"))[0] for nom in ORDRE]
V["rm10_min"] = fr(100 * min(rm10), 1); V["rm10_max"] = fr(100 * max(rm10), 1); V["rm10_nb"] = sum(e <= 0.05 for e in rm10)
assert V["rm10_nb"] == 1
# --- le lecteur : validation ---
t = open(os.path.join(D, "validation_lecteur_creux_v1.log")).read()
m = re.search(r"VALIDATION : (\d+) lectures, pire ecart relatif ([0-9.e+-]+)", t); V["val_n"] = int(m.group(1)); V["val_pire"] = fr(100 * float(m.group(2)), 2)
assert "ecart max a H_2D du moteur (N = 60) : 0.000e+00" in t
dE = max(float(x) for x in re.findall(r"max \|dE_re\| ([0-9.e+-]+)", t)); V["val_dE"] = "%.0e" % dE
assert dE < 3e-13
n = 0; pire = 0.0; res = 0.0
for nom in ORDRE:
    for cle, c in P[nom]["cfg"].items():
        for k, r in c["traj"].items():
            n += 1; res = max(res, r["residu"])
            if r["gamma"] > 1e-13: pire = max(pire, abs(r["gamma_im"] / r["gamma"] - 1.0))
V["expl_n"] = n; V["expl_flux_im"] = "%.0e" % pire; V["expl_residu"] = "%.0e" % res
assert pire < 1e-9 and res < 1e-13
# --- le temoin ---
t = open(os.path.join(D, "temoin_absorbeurs_longs_v1.log")).read()
tem = {}
for bloc in t.split("=== ")[1:]:
    j = bloc[:3]
    for forme, L in (("F1", 60), ("F2", 60), ("F1", 80), ("F2", 80)):
        m = re.search(r"%s L%d \(N \d+\) / reference, k=-5\.\.12 : ([0-9. ]+)" % (forme, L), bloc)
        v = [float(x) for x in m.group(1).split()]
        s = 0
        for x in v:                                   # barreaux consecutifs, depuis k = -5, a moins de 0.5 % de la reference
            if abs(x - 1.0) <= 0.005: s += 1
            else: break
        tem[(j, forme, L)] = (s, max(abs(x - 1.0) for x in v[:s]))
V["tem_n_min"] = min(x[0] for x in tem.values()); V["tem_n_max"] = max(x[0] for x in tem.values())
V["tem_ecart"] = fr(100 * max(x[1] for x in tem.values()), 2)
assert V["tem_n_min"] >= 5
# --- l'emulation par la chaine (voie essayee d'abord) ---
E = json.load(open(os.path.join(D, "emulation_v1.json")))["points"]
CFG5 = ["F1G20", "F1G30", "F2G20", "F3G20", "F1GT"]
def etal(nom, ks, corr):
    v = []
    for c in CFG5:
        for k in ks:
            t_ = E[nom]["cfg"][c]["traj"][str(k)]
            v.append(t_["g2D"] / t_["o2b"] if corr else t_["g2D"])
    return max(v) / min(v) - 1.0
cent = ["197_100", "99_50", "101_50", "203_100"]; bords = ["39_20", "41_20"]
V["emu_brut_min"] = fr(100 * min(etal(n, (0, 1, 2), False) for n in cent), 1); V["emu_brut_max"] = fr(100 * max(etal(n, (0, 1, 2), False) for n in cent), 1)
V["emu_corr_min"] = fr(100 * min(etal(n, (0, 1, 2), True) for n in cent), 1); V["emu_corr_max"] = fr(100 * max(etal(n, (0, 1, 2), True) for n in cent), 1)
V["emu_bord_brut"] = " et ".join(fr(100 * etal(n, (0, 1, 2), False), 1) for n in bords); V["emu_bord_corr"] = " et ".join(fr(100 * etal(n, (0, 1, 2), True), 1) for n in bords)
acc = 0
for nom in ORDRE:
    for c in CFG5:
        tr = E[nom]["cfg"][c]["traj"]
        def pl(cle):
            best = min(max(tr[str(k)][cle] for k in range(k0, k0 + 5)) / min(tr[str(k)][cle] for k in range(k0, k0 + 5)) for k0 in range(-5, 9))
            return best - 1.0 <= 0.05
        acc += pl("g2D") == pl("o2b")
V["emu_accord"] = acc
assert acc == 19
t = open(os.path.join(D, "lecture_hors_echantillon_v1.log")).read()
m = re.search(r"retenus : (\d+)", t); V["he_n"] = int(m.group(1))
m2_ = re.search(r"tous\s+n=\s*\d+ k=2 contre k=3 : \|brut\| med ([0-9.]+) .*? reste o2b med ([0-9.]+)", t)
m4_ = re.search(r"tous\s+n=\s*\d+ k=4 contre k=3 : \|brut\| med ([0-9.]+) .*? reste o2b med ([0-9.]+)", t)
V["he_brut2"] = fr(100 * float(m2_.group(1)), 1); V["he_reste2"] = fr(100 * float(m2_.group(2)), 1)
V["he_brut4"] = fr(100 * float(m4_.group(1)), 1); V["he_reste4"] = fr(100 * float(m4_.group(2)), 1)
# --- pieces ---
PIECES = ["lecteur_2D_creux_machine1_v1.py", "lecteur_2D_creux_machine1_v2.py", "validation_lecteur_creux_machine1_v1.py", "validation_lecteur_creux_v1.log",
          "exploration_absorbeurs_machine1_v1.py", "exploration_v1.json", "exploration_v1b.json", "lecture_exploration_machine1_v1.py",
          "temoin_absorbeurs_longs_machine1_v1.py", "temoin_absorbeurs_longs_v1.log", "chaine_sans_boite_machine1_v1.py", "chaine_sans_boite_v1.json",
          "chaine_longue_plateau_machine1_v1.py", "chaine_longue_plateau_v1.log", "emulation_absorbeur_machine1_v1.py", "emulation_v1.json",
          "lecture_emulation_machine1_v1.py", "lecture_corrigee_machine1_v1.py", "plateaux_emulation_machine1_v1.py",
          "emulation_hors_echantillon_machine1_v1.py", "emulation_hors_echantillon_v1.json", "lecture_hors_echantillon_machine1_v1.py", "lecture_hors_echantillon_v1.log",
          "construction_note_piste0_reprise_machine1_v1.py", "note_piste0_reprise_gabarit.txt"]
V["pieces"] = "\n".join("    %s  %s" % (canon(os.path.join(D, p)) if p != "construction_note_piste0_reprise_machine1_v1.py" else "(ce script)      ", p) for p in PIECES)
SOURCES = [("scripts/m17_chaine_v17.py", "le moteur"), ("gels/qualification_EB_bis_pre_enregistrement_v1.md", "le gel bis"),
           ("journal/journal_delta_95_qualification_EB_bis_v2.md", "l'acte 95 (nuit bis : NON QUALIFIÉ)"),
           ("journal/lot_a01598ec24237921__sonde_etage2.json", "la sortie de la sonde certifiée, étage 2 de la nuit bis"),
           ("journal/lot_a01598ec24237921__sonde_etage1.json", "idem, étage 1 (témoin)"),
           ("journal/tp_reference_machine2_v1.json", "la référence du témoin, par rotation complexe (machine 2)"),
           ("gels/gel_ordre2_chaine_EA_pre_enregistrement_v1.md", "le gel de la chaîne d'ordre 2"),
           ("journal/journal_delta_98_ordre2_chaine_EA_v1.md", "l'acte 98"),
           ("journal/sonde_ordre2.json", "la sortie de la sonde du delta 98"), ("journal/sonde_domaine_G1.json", "idem, delta 97"),
           ("journal/sonde_chaine_par_etat.json", "idem, delta 96")]
V["sources"] = "\n".join("    %s  %s — %s" % (canon(os.path.join(CLONE, p)), p, quoi) for p, quoi in SOURCES)
assert canon(os.path.join(CLONE, "scripts/m17_chaine_v17.py")) == "82a0be882568fe0c"
assert canon(os.path.join(CLONE, "journal/journal_delta_98_ordre2_chaine_EA_v1.md")) == "c2f3e5c9102dc1a7"
g = open(GABARIT, encoding="utf-8").read()
manquants = set(re.findall(r"\{\{(\w+)\}\}", g)) - set(V)
assert not manquants, manquants
out = re.sub(r"\{\{(\w+)\}\}", lambda m: str(V[m.group(1)]), g)
open(SORTIE, "w", encoding="utf-8", newline="\n").write(out)
print("ecrit", SORTIE, canon(SORTIE), len(out.splitlines()), "lignes")
for k in sorted(V):
    if k not in ("tableau1", "tableau2", "pieces"): print("  %-20s %s" % (k, V[k]))
