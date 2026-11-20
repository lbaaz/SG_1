# -*- coding: ascii -*-
"""RELEVE de la seconde partie du gel "pont" contre ses pieces -- machine 1, v1, 2026-11-17. Onze controles ; aucune 2D.
Recalcule depuis les pieces (et non depuis le script de construction) ce que le texte affirme, et cherche chaque nombre
dans le texte. Code de sortie 0 si aucun controle ne mord.
Usage : python3 -I -B ce_script <gel.md> <dossier du lot a plat> <clone du registre> <dossier extrait du lot de machine 2>
                                <manifeste du lot de machine 2> <table commune.json>"""
import sys, os, re, json, math, hashlib, unicodedata, subprocess, tempfile
GEL, D, CLONE, LOT_M2, MAN_M2, COMMUNE = [a.rstrip("/") for a in sys.argv[1:7]]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
brut = open(GEL, "rb").read(); T = brut.decode("utf-8"); LG = T.split("\n"); mord = []
def controle(nom, fautes):
    print("%s : %s" % (nom, "OK" if not fautes else "MORD -- " + " | ".join(str(f) for f in fautes[:4])));
    if fautes: mord.append(nom)
def manque(chaines): return [c for c in chaines if c not in T]
def section(n):
    i = [k for k, l in enumerate(LG) if re.match(r"^%d\. " % n, l)][0]
    j = [k for k, l in enumerate(LG) if k > i and (re.match(r"^\d+\. ", l) or l.startswith("-- FIN"))][0]
    return "\n".join(LG[i:j])
def J(nom): return json.load(open(D + "/" + nom))
# R01 forme
f = []
try: brut.decode("ascii")
except UnicodeDecodeError: f.append("non ASCII")
f += ["ligne de %d colonnes" % len(l) for l in LG if len(l) > 100][:2] + (["signe pour cent"] if "%" in T else [])
f += ["espace en fin de ligne"] * any(l != l.rstrip() for l in LG)
f += ["fin absente"] * (not T.endswith("-- FIN gel_pont_partie2_instrument_enonces_pre_enregistrement_v1 --\n"))
controle("R01 forme (ASCII, 100 colonnes, sans signe pour cent, ligne de fin)", f)
# R02 pieces
s15 = section(15); pcs = re.findall(r"^    ([0-9a-f]{16})  (\S+)$", s15, re.M); f = []
for c, n in pcs:
    if not os.path.isfile(D + "/" + n): f.append("absente : " + n)
    elif canon(D + "/" + n) != c: f.append("canon : " + n)
f += ["compte %d" % len(pcs)] * (len(pcs) != 75) + ["doublon"] * (len(set(n for _, n in pcs)) != len(pcs))
controle("R02 les %d pieces de la section 15 : presentes, canons recalcules" % len(pcs), f)
# R03 sources
s1 = section(1); f = []
for b in ("m17_chaine_v17.py", "chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py", "sonde_lecteur_gel_loi_machine1_v1.py"):
    if "%s  scripts/%s" % (canon(CLONE + "/scripts/" + b), b) not in s1: f.append(b)
tete = subprocess.run(["git", "-C", CLONE, "rev-parse", "--short=7", "HEAD"], capture_output=True, text=True).stdout.strip()
f += ["tete"] * (("tete %s " % tete) not in s1) + ["lot de machine 2"] * ((canon(MAN_M2) + "  lot de machine 2") not in s1)
f += ["note de machine 2"] * ((canon(LOT_M2 + "/POUR_MACHINE1_certification_gel_pont_partie1_machine2_v1.md") + "  POUR_MACHINE1") not in s1)
f += ["table commune"] * ((canon(COMMUNE) + "  table_commune_pont_v1.json") not in s1)
controle("R03 sources : blocs du registre, tete, lot et note de machine 2, table commune", f)
# R04 tirage
s2 = section(2); f = []; graine = re.search(r"certification de machine 2 : (\d+)\.", s2)
tc = json.load(open(COMMUNE))["creneaux"]; attendu = []
if not graine: f.append("graine illisible")
else:
    g = graine.group(1)
    for s in ("MG", "PG"):
        cands = tc[s]["candidats"]; pris = None
        for r in range(5):
            h = hashlib.sha256(("%s|%s|%d" % (g, s, r)).encode("ascii")).hexdigest(); num = int(h, 16) % len(cands)
            if cands[num]["eligible"]:
                pris = (r, h, num, cands[num]); break
        if pris is None: f.append("pas de w2 pour " + s); continue
        r, h, num, c = pris
        if 'creneau %s, rang %d : sha256("%s|%s|%d") = %s... ; modulo %d = %d' % (s, r, g, s, r, h[:16], len(cands), num) not in s2: f.append("rang " + s)
        if "-> w2 = %s (" % c["w2"] not in s2: f.append("w2 " + s)
        attendu += [("%s%d" % (s, x["m"]), c["w2"], x["m"], x["g"]) for x in c["cellules"]]
    for nom, w2, m, gg in attendu:
        if not re.search(r"^    %s\s+w2 = %s\s+m = %d  g = %s$" % (nom, re.escape(w2), m, re.escape(gg)), s2, re.M): f.append("cellule " + nom)
    lt = open(D + "/tirage_pont_graine_456823_machine1_v1.log").read()
    f += ["journal du tirage"] * any(not re.search(r"^  %s\s+w2 = %s\s+m = %d g = %s$" % (n, re.escape(w), m, re.escape(x)), lt, re.M) for n, w, m, x in attendu)
controle("R04 tirage : hachages, modulos, les six cellules contre la table commune et le journal", f)
# R05 table de la chaine
CH = J("chaine_cellules_pont_v1.json"); X = CH["ecarts"]; C = CH["cellules"]; NOMS = [a[0] for a in attendu] or ["MG3", "MG4", "MG5", "PG3", "PG4", "PG5"]
att = []
for n in NOMS:
    c = C[n]; att.append("    %-7s  %d       %.4f   %d    %.4e   %.4f    %.4f        %.4f" % (n, c["m_bord"], c["e_bord"], c["r_c"], math.exp(c["ln_G3"]),
                         c["etendue_vide"], max(c["etendue_rho3"]), max(abs(v) for v in c["pas_2_3"])))
for i, x in enumerate(X):
    att.append("    %-5s  " % ("%g" % x) + "  ".join("%7.2f" % (C[n]["ln_rho3"][i] + math.log(abs(C[n]["delta"]))) for n in NOMS))
    att.append("    %-5s  " % ("%g" % x) + "  ".join("%+7.4f" % C[n]["pas_2_3"][i] for n in NOMS))
f = manque(att); f += ["cellule " + n for n, w2, m, g in attendu if (C[n]["w2"], C[n]["m"], C[n]["g"]) != (w2, m, g)]
controle("R05 section 4 : %d lignes de table recalculees depuis chaine_cellules_pont_v1.json" % len(att), f)
# R06 table de la qualification de la densite
LD = {m: J("lecture_densite_2d_SA%d_v1.json" % m) for m in (3, 4, 5)}
att = ["    %-5s  " % ("%g" % x) + "   ".join("%+.4f  %+.4f" % (LD[m]["par_x"][i]["ln_R3"], LD[m]["par_x"][i]["ln_R2"]) for m in (3, 4, 5)) for i, x in enumerate(X)]
att.append("Plus grand |ln R3| : %.4f, %.4f, %.4f." % tuple(max(abs(p["ln_R3"]) for p in LD[m]["par_x"]) for m in (3, 4, 5)))
controle("R06 section 6 : table des ln R3 et ln R2 recalculee depuis les trois lectures de densite", manque(att))
# R07 constantes du texte contre les scripts
s7 = section(7); s5 = section(5); V = open(D + "/verdict_pont_machine1_v1.py").read(); SB = open(D + "/sonde_boite_fermee_pont_machine1_v1.py").read()
LB_ = open(D + "/lecture_boites_pont_machine1_v1.py").read(); LDs = open(D + "/lecture_densite_2d_pont_machine1_v1.py").read(); f = []
pv = [('UN = (180, 189); DEUX = (291, 300); MIN_BOITES = 8', V), ("TOL_L, MIN_ECARTS, X_L2 = 0.05, 10, 5.0", V), ("S_CELLULE, S_GROUPE = (0.85, 1.15), (0.80, 1.20)", V),
      ("C_REDUIT, C_RAPPORT = (0.33, 0.55), (1.25, 1.85)", V), ("X_LO, X_HI, S_A, S_B, K_DEPART, K_MAX, TOL_FIABLE, TOL_LISTE, ELARGI = 0.05, 8.0, 2.5, 5.5, 24, 768, 0.02, 1e-9, 6", SB),
      ("X_LO, X_HI, PART_NON_FIABLE_MAX = F(1, 20), F(8), 0.05", LB_), ("K_MIN, K_MAX, TAU, SEUIL_ABS = -3, 8, Fraction(1, 20), 0.02", LDs)]
f += ["constante de script : " + a[:40] for a, src in pv if a not in src]
pt = ["au moins 10 de ses 12 ecarts", "|ln R3(x)| <= 0.05", "ecart lisible x >= 5", "au moins 8 boites lisibles", "est dans [0.85, 1.15]", "est dans [0.80,",
      "au moins 8 boites de compte valide", "est dans [0.33, 0.55]", "est dans [1.25, 1.85]", "au moins quatre cellules sont lisibles"]
f += ["enonce : " + a for a in pt if a not in " ".join(s7.split())]
p5 = ["groupe UN = 180 a 189, groupe DEUX = 291 a", "de 24 a 768", "s'accordent a 2 pour cent", "au plus 5 pour cent", "(energies a 1e-9 pres)", "est <= 1.05",
      "est <= 0.02", "E_v - 2.5 delta et E_v - 5.5 delta", "0.05 < x < 8"]
f += ["instrument : " + a for a in p5 if a not in " ".join(s5.split())]
controle("R07 constantes des sections 5 et 7 contre les scripts (%d + %d + %d)" % (len(pv), len(pt), len(p5)), f)
# R08 qualification des boites
rep = [c for c in J("lecture_boites_repetition_v1.json")["cellules"] if c["m"] == 3][0]; un = [b for b in rep["boites"] if 180 <= b["cote"] <= 189]
S = [b["S"] for b in un]; mo = sum(S) / len(S); sd = math.sqrt(sum((s - mo) ** 2 for s in S) / (len(S) - 1)); nm = sum(b["n"] for b in un) / len(un)
b5 = json.loads(open(D + "/boite_SA5_300_v1.jsonl").readline()); niv = min(b5["niveaux"], key=lambda v: abs(v["x"] - 6.699))
conf = J("lecture_boites_qualification_v1.json")["confrontation"]
att = [": TIENT : %.4f +- %.4f. U3" % (mo, sd / math.sqrt(len(S))), "et %.4f +- %.4f sur les dix boites" % (mo, sd / math.sqrt(len(S))), "n moyen %.1f (de %d a %d)" % (nm, min(b["n"] for b in un), max(b["n"] for b in un)), ": TIENT : %.4f. U4" % sd,
       "elles s'accordent a %.1e pres" % abs(niv["c2_b"] / niv["c2_a"] - 1.0), "egaux a %.1e |delta| pres" % max(c["ecart_x_max"] for c in conf),
       "Compte reduit n / (cote x 7.95 x |delta|) : %.3f" % (nm / (184.5 * 7.95 * 0.02))]
controle("R08 section 6 : groupe UN, niveau non fiable de machine 2, confrontation, recalcules", [a for a in att if " ".join(a.split()) not in " ".join(T.split())])
# R09 reserve R1
B = J("controle_details_R1_v1.json")["B"]; em = B["ecart_relatif_max_par_profondeur"]; ch = B["cellules_dont_l_etendue_change_de_plus_de_5e-5"]
att = ["bloc de %.1e au plus a 3 barreaux, %.1e a 4, %.1e a 5" % (em["3"], em["4"], em["5"]), "dans %d cellules (%d a 4 barreaux, %d a 5)" % (ch["3"] + ch["4"] + ch["5"], ch["4"], ch["5"]),
       "ainsi lue : %.4f, pour un seuil de 0.02" % B["plus_grande_etendue_en_double"]]
controle("R09 section 3 : nombres de la reserve R1 recalcules", [a for a in att if a not in " ".join(T.split())] + ["une decision change"] * (B["decisions_iii_qui_changent"] != 0))
# R10 coherence des annonces
s11 = section(11); f = []
for fam in ("L", "L2", "S", "C"):
    m = re.search(r"^    \(%s\)\s+((?:\d\.\d\d\s+){6})(\d\.\d\d)$" % fam, s11, re.M)
    if not m: f.append("ligne (%s) illisible" % fam); continue
    cel = [float(v) for v in m.group(1).split()]
    if float(m.group(2)) > min(cel) + 1e-12: f.append("(%s) : la famille est annoncee plus probable que sa cellule la moins probable" % fam)
m4 = re.search(r"Les quatre familles tenues : (\d\.\d+)\.", s11)
f += ["quatre familles"] * (not m4 or float(m4.group(1)) > 0.40)
controle("R10 annonces : aucune famille plus probable que sa cellule la moins probable", f)
# R11 la feuille de verdict, rejouee en repetition sur les pieces
with tempfile.TemporaryDirectory() as tmp:
    r = subprocess.run([sys.executable, "-I", "-B", D + "/verdict_pont_machine1_v1.py", D + "/chaine_cellules_pont_v1.json", D + "/lecture_boites_repetition_v1.json", tmp + "/v.json",
                        "--repetition", "180", "189", "291", "300", "1"] + ["SA%d=%s/lecture_densite_2d_SA%d_v1.json" % (m, D, m) for m in (3, 4, 5)], capture_output=True, text=True)
    f = []
    if r.returncode != 0: f.append("la feuille echoue")
    else:
        v = json.load(open(tmp + "/v.json")); a = v["cellules"]["SA3"]
        att = ["(L) %s, pire ln R3 %+.4f ; (S) %s, %.4f +- %.4f ; (C) %s, comptes reduits %.3f et %.3f, rapport %.3f" % (a["L"]["verdict"], a["L"]["pire_ln_R3"], a["S"]["verdict"],
               a["S"]["moyenne"], a["S"]["erreur"], a["C"]["verdict"], a["C"]["compte_reduit"]["UN"], a["C"]["compte_reduit"]["DEUX"], a["C"]["rapport"]),
               "A 4 et 5 barreaux : (L) %s et %s." % (v["cellules"]["SA4"]["L"]["verdict"], v["cellules"]["SA5"]["L"]["verdict"])]
        f += [x for x in att if x not in " ".join(T.split())]
        f += ["sortie deposee differente"] * (json.dumps(v, sort_keys=True) != json.dumps(J("repetition_verdict_v1.json"), sort_keys=True))
controle("R11 repetition du verdict rejouee : memes verdicts que le texte et que la piece", f)
print("RELEVE : %d controles ; %s" % (11, "0 morsure" if not mord else "%d MORSURE(S) : %s" % (len(mord), ", ".join(m.split()[0] for m in mord))))
sys.exit(1 if mord else 0)
