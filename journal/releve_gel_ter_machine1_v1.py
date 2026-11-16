# -*- coding: ascii -*-
"""RELEVE du gel ter : controle de sortie de la plume, pas une certification. Chaque nombre et chaque citation du
texte du gel sont refaits ici depuis les pieces, par un code qui n'est ni la construction ni la feuille (la
routine de plateau est reecrite en flottants, avec un controle d'ecart a la borne).
Usage : python3 -I releve_gel_ter_machine1_v1.py <gel.md> <dossier du gel> <dossier de la note> <clone>
        <manifeste du lot de la note>     (code de sortie 0 si aucun controle ne mord)"""
import sys, os, re, json, math, ast, hashlib, unicodedata
GEL, D, DN, CLONE, MAN_NOTE = sys.argv[1:6]
T = open(GEL, "rb").read().decode("utf-8")
U = re.sub(r"\s+", " ", T)
RES = []

def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def ctl(nom, ok, detail=""):
    RES.append((nom, bool(ok), detail)); print("%-4s %s  %s" % (nom, "TIENT" if ok else "MORD ", detail))

def dans(s):
    return re.sub(r"\s+", " ", s) in U

def essai(nom):
    a_ = os.path.join(D, "essai_m1", nom)
    return a_ if os.path.exists(a_) else os.path.join(D, "essai_m1_" + nom)

def med(x):
    x = sorted(x); n = len(x); return x[n // 2] if n % 2 else 0.5 * (x[n // 2 - 1] + x[n // 2])

# R01 forme
lignes = T.split("\n")
try:
    T.encode("ascii"); asc = True
except UnicodeEncodeError:
    asc = False
ctl("R01", asc and "%" not in T and max(len(l) for l in lignes) <= 100 and T.endswith("-- FIN qualification_EB_ter_pre_enregistrement_v1 --\n")
    and "\r" not in T and not any(l != l.rstrip() for l in lignes),
    "ASCII %s ; pour cent %d ; plus longue ligne %d ; ligne de FIN ; pas d'espace en fin de ligne" % (asc, T.count("%"), max(len(l) for l in lignes)))

# R02 empreintes : chaque suite de 16 hex du gel est le canon d'une piece que je tiens
connus = {}
for racine, dossiers, fichiers in os.walk(CLONE):
    if ".git" in racine:
        continue
    for f in fichiers:
        if f.endswith((".md", ".py", ".json", ".txt")):
            try:
                connus.setdefault(canon(os.path.join(racine, f)), os.path.relpath(os.path.join(racine, f), CLONE))
            except Exception:
                pass
for f in os.listdir(D):
    p = os.path.join(D, f)
    if os.path.isfile(p):
        try:
            connus.setdefault(canon(p), "gel/" + f)
        except Exception:
            pass
connus.setdefault(canon(os.path.join(DN, "note/note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md")), "note")
connus.setdefault(canon(MAN_NOTE), "manifeste du lot de la note")
hexs = sorted(set(re.findall(r"(?<![0-9a-f.])[0-9a-f]{16}(?![0-9a-f])", T)))
inconnus = [h for h in hexs if h not in connus]
ctl("R02", not inconnus and len(hexs) >= 14, "%d empreintes citees, non resolues : %s" % (len(hexs), inconnus))

# R03 noms : chaque empreinte nommee porte bien sur la piece nommee
attendus = {"moteur": ("scripts/m17_chaine_v17.py", r"canons du moteur \(([0-9a-f]{16})\)"),
            "depot": ("journal/sonde_ordre2.json", r"du depot \(([0-9a-f]{16})\)"),
            "retenus": ("journal/tp_retenus_machine2_v1.json", r"liste des retenus \(([0-9a-f]{16})\)"),
            "table du temoin": ("journal/tp_reference_machine2_v1.json", r"table du temoin \(([0-9a-f]{16})\)")}
bad = []
for nom, (chemin, motif) in attendus.items():
    m = re.search(motif, U)
    if not m or m.group(1) != canon(os.path.join(CLONE, chemin)):
        bad.append(nom)
for nom, fichier, motif in (("sonde", "sonde_qualification_EB_ter_machine1_v1.py", r"la sonde \(([0-9a-f]{16})\)"),
                            ("bloc", "lecteur_plateau_bloc_machine1_v1.py", r"le bloc du lecteur \(([0-9a-f]{16})\)"),
                            ("feuille", "lecture_qualification_EB_ter_machine1_v1.py", r"la feuille \(([0-9a-f]{16})\)"),
                            ("banc", "banc_feuille_ter_machine1_v1.py", r"banc qui tue \(([0-9a-f]{16})\)"),
                            ("reference des ancres", "reference_ancres_ter_machine1_v1.json", r"reference des ancres \(([0-9a-f]{16})\)")):
    m = re.search(motif, U)
    if not m or m.group(1) != canon(os.path.join(D, fichier)):
        bad.append(nom)
ctl("R03", not bad, "empreintes nommees fausses : %s" % bad)

# R04 citations du gel bis, mot pour mot
BIS = re.sub(r"\s+", " ", open(os.path.join(CLONE, "gels/qualification_EB_bis_pre_enregistrement_v1.md")).read())
cit = ["DERNIER ESSAI", "ni troisieme gel, ni autre echelle, ni autre temoin", "L'operateur peut lever ce garde-fou ; les machines, non",
       "La largeur Gamma_LS que la manche M17 a lue est-elle une largeur SORTANTE INTRINSEQUE -- independante de la force, de la forme, de la longueur et de la position de l'absorbeur -- ou depend-elle de la facon d'absorber ?",
       "le hamiltonien est-il essentiellement auto-adjoint", "largeur sortante stable sous les variations jouees",
       "toute phrase portant un Gamma depuis juillet est reclassee"]
manq = [c for c in cit if not (c in BIS and ('"%s"' % c) in U)]
ctl("R04", not manq, "citations absentes du gel bis ou du gel : %s" % [c[:30] for c in manq])

# R05 les douze points : table refaite du depot
DEP = json.load(open(os.path.join(CLONE, "journal/sonde_ordre2.json"))); P = {p["id"]: p for p in DEP["points"]}
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]
bad = []; nj = 0; etal = []
for i in JUGES:
    p = P[i]; es = [e for e in p["etats"] if (e.get("Gamma_2D") or {}).get("3") is not None and e["Gamma_2D"]["3"] > 1.33e-12]
    nj += len(es); rc = p["r_c"]
    for e in es:
        v = [e["Gamma_2D"][k] for k in ("2", "3", "4")]; etal.append(max(v) / min(v) - 1.0)
    m = re.search(r"^  %s\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+), (\d+), (\d+), (\d+)$" % i, T, re.M)
    if not m or (m.group(1), m.group(2), int(m.group(3)), int(m.group(4))) != (p["w2"], p["facteur"], rc, len(es)) or \
            [int(m.group(j)) for j in (5, 6, 7, 8)] != [rc + 80, rc + 100, rc + 100, rc + 90] or not any(e["rang"] == 0 for e in es):
        bad.append(i)
ctl("R05", not bad and dans("%d etats. Rien d'autre." % nj), "points faux : %s ; etats juges %d" % (bad, nj))

# R06 comptes
seuil = -((-9 * nj) // 10)
ctl("R06", dans("etage 2, %d lectures (%d etats, quatre absorbeurs, douze barreaux)" % (nj * 48, nj)) and dans("(au moins %d)" % seuil)
    and dans("etage 0, 84 lectures ; ancres, 192 ; etage 1, 96 au temoin positif et 96 au temoin negatif"),
    "lectures %d ; seuil des neuf dixiemes %d" % (nj * 48, seuil))

# R07 constantes de la sonde et de la feuille contre le texte
def constantes(chemin):
    out = {}
    for n in ast.parse(open(chemin).read()).body:
        if isinstance(n, ast.Assign):
            try:
                val = ast.literal_eval(n.value)
            except Exception:
                continue
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = val
                elif isinstance(t, ast.Tuple) and isinstance(val, tuple):
                    for a, b in zip(t.elts, val):
                        out[a.id] = b
    return out
CS = constantes(os.path.join(D, "sonde_qualification_EB_ter_machine1_v1.py")); CF = constantes(os.path.join(D, "lecture_qualification_EB_ter_machine1_v1.py"))
src_f = open(os.path.join(D, "lecture_qualification_EB_ter_machine1_v1.py")).read(); src_s = open(os.path.join(D, "sonde_qualification_EB_ter_machine1_v1.py")).read()
ok = (CS.get("ABSORBEURS") == [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]
      and "KS = list(range(-3, 9))" in src_s and CS.get("KS_ETAGE0") == [2, 3, 4] and CS.get("PLANCHER10") == 1.33e-12
      and (CS.get("ITER_MIN"), CS.get("ITER_MAX"), CS.get("TOL_RESIDU"), CS.get("POIDS_MIN")) == (2, 12, 1e-11, 0.5)
      and CS.get("JUGES") == JUGES and CS.get("ANCRES") == ["A1", "A2"] and "TP_W2, TP_RC, TP_ETA0 = F(39, 20), 40, 0.05" in src_s
      and "TAU = Fraction(1, 20)" in src_f and CF.get("TAU_F") == 0.05 and (CF.get("K_MIN"), CF.get("K_MAX")) == (-3, 8)
      and (CF.get("TOL_E0_REL"), CF.get("TOL_E0_ABS")) == (1e-3, 1e-12) and CF.get("TOL_ANCRE") == 1e-6
      and "PART_ETATS = Fraction(9, 10)" in src_f and CF.get("PLANCHER10") == 1.33e-12 and CF.get("JUGES") == JUGES
      and '"absorbeurs": [["A", "F2", 0, 80], ["B", "F2", 0, 100], ["C", "F1", 0, 100], ["D", "F2", 10, 80]],' in src_f
      and 'REGLAGE = {"ks": KS, "ks_etage0": KS_ETAGE0,' in src_f and "KS = list(range(K_MIN, K_MAX + 1))" in src_f
      and '"plancher10": PLANCHER10, "iter_min": 2, "iter_max": 12, "tol_residu": 1e-11, "poids_min": 0.5}' in src_f)
txt = (dans("A : F2, B = r_c, L = 80") and dans("B : F2, B = r_c, L = 100") and dans("C : F1, B = r_c, L = 100") and dans("D : F2, B = r_c + 10, L = 80")
       and dans("(d'un facteur 16/25)")
       and dans("k = -3, -2, ..., 8 : douze valeurs, un facteur 2048") and dans("Au moins 2 iterations, au plus 12")
       and dans("1e-11 fois max(1, |lambda|)") and dans("vaut au moins 0.5") and dans("tau = 0.05") and dans("<= 1e-3 G_dep + 1e-12")
       and dans("<= 1e-6") and dans("neuf dixiemes") and dans("(1 + Fraction(1, 20)) * Fraction(min)") and dans("(1.33e-12)")
       and dans("huit fenetres, de k0 = -3 a k0 = 4") and dans("bord 40, eta0 = 0.05"))
ctl("R07", ok and txt, "constantes des scripts %s ; phrases du gel %s" % (ok, txt))

# R08 le bloc est dans la sonde tel quel ; la feuille porte le canon de la sonde et celui de la reference
bloc = open(os.path.join(D, "lecteur_plateau_bloc_machine1_v1.py")).read().rstrip("\n")
ctl("R08", bloc in src_s and CF.get("CANON_SONDE") == canon(os.path.join(D, "sonde_qualification_EB_ter_machine1_v1.py"))
    and CF.get("CANON_REFERENCE_ANCRES") == canon(os.path.join(D, "reference_ancres_ter_machine1_v1.json"))
    and CF.get("CANON_DEPOT") == canon(os.path.join(CLONE, "journal/sonde_ordre2.json")) and CS.get("CANON_DEPOT") == CF.get("CANON_DEPOT"),
    "bloc tel quel ; canons croises de la sonde, de la reference et du depot")

# R09 selftest et banc : comptes relus des journaux
jb = open(os.path.join(D, "banc_feuille_ter_machine1_v1.log")).read()
m = re.search(r"BANC : (\d+) alterations, (\d+) mordues, 0 survivantes", jb)
js = open(os.path.join(D, "selftest_feuille_ter_machine1_v1.log")).read()
ms = re.search(r"selftest : (\d+) tenus sur (\d+)", js)
ctl("R09", m and ms and m.group(1) == m.group(2) and ms.group(1) == ms.group(2)
    and dans("%s cas tenus sur %s" % (ms.group(1), ms.group(1))) and dans("%s alterations du code de la feuille, %s mordues" % (m.group(1), m.group(1))),
    "selftest %s ; banc %s" % (ms.group(0) if ms else None, m.group(0) if m else None))

# --- routine de plateau du releve (flottants) ---
def fenetre(vals, ks):
    best = None
    for i in range(len(ks) - 4):
        f = [vals.get(k) for k in ks[i:i + 5]]
        if any(x is None for x in f):
            continue
        r = max(f) / min(f)
        if best is None or r < best[0] - 0.0:
            best = (r, ks[i], math.exp(sum(math.log(x) for x in f) / 5.0))
    return best
MARGE = []          # distance a la borne de 1.05 de chaque fenetre retenue : le releve en flottants n'est sur que loin de la borne

# R10 (i) la note
EX = {}
for f in ("exploration_v1.json", "exploration_v1b.json"):
    EX.update(json.load(open(os.path.join(DN, f)))["points"])
KSN = list(range(-5, 15)); pire = 0.0; acc = 0.0; f3 = 0.0
for nom, p in EX.items():
    vals = {}
    for c in ("F2_r+0_L60", "F2_r+0_L80", "F1_r+0_L80", "F3_r+0_L60", "F1_r+10_L60"):
        b = fenetre({k: p["cfg"][c]["traj"][str(k)]["gamma"] for k in KSN}, KSN); pire = max(pire, b[0] - 1.0); vals[c] = b[2]
    acc = max(acc, max(vals.values()) / min(vals.values()) - 1.0); f3 = max(f3, abs(math.log(vals["F3_r+0_L60"] / vals["F1_r+0_L80"])))
ctl("R10", len(EX) == 6 and dans("pire etalement %.4f" % pire) and dans("s'accordent a %.4f pres au pire" % acc) and dans("a %.4f pres au pire (note" % f3),
    "note : pire etalement %.4f, accord %.4f, F3 a 60 contre F1 a 80 : %.4f" % (pire, acc, f3))

# R11 (ii) le reglage, rejuge par le releve
R = {}
for f in ("reglage_p1.json", "reglage_p2.json"):
    R.update(json.load(open(os.path.join(D, f)))["points"])
KS = list(range(-3, 9)); st = {"Q": 0, "N": 0, "L": 0}; et = {x: [] for x in "ABCD"}; ac = {x: [] for x in "BCD"}; dp = []; r0q = 0; nlect = 0; fl = 0.0; pp = []
for pid in ("A1", "A2", "J1", "J2", "J3", "J5", "E4", "H1"):
    q = 0
    for cle, e in R[pid]["etats"].items():
        F_ = {}
        for x in "ABCD":
            ser = {}
            for k in KS:
                r_ = e["cfg"][x][str(k)]; nlect += 1
                ser[k] = r_["gamma"] if (r_["suivi"] and r_["gamma"] is not None and r_["gamma"] > 0 and math.isfinite(r_["gamma"])) else None
                if r_["suivi"]:
                    fl = max(fl, abs(r_["gamma_im"] / r_["gamma"] - 1.0))
            F_[x] = fenetre(ser, KS)
            if F_[x]:
                et[x].append(F_[x][0] - 1.0); MARGE.append(abs(F_[x][0] - 1.05))
        ech = any(F_[x] is not None and F_[x][0] > 1.05 for x in "ABCD"); nl = any(F_[x] is None for x in "ABCD")
        if F_["A"] and F_["A"][0] <= 1.05:
            for x in "BCD":
                if F_[x] and F_[x][0] <= 1.05:
                    a_ = abs(math.log(F_[x][2] / F_["A"][2])); ac[x].append(a_); MARGE.append(abs(a_ - 0.05)); ech = ech or a_ > 0.05
            d_ = abs(math.log(e["G2D"]["3"] / F_["A"][2])); dp.append(d_)
        s_ = "N" if ech else ("L" if nl else "Q"); st[s_] += 1; q += s_ == "Q"
        if e["rang"] == 0 and s_ == "Q":
            r0q += 1
    pp.append("%s %d/%d" % (pid, q, len(R[pid]["etats"])))
n = sum(st.values())
phr = [dans("; %d etats :" % n),
       dans("%d QUALIFIES, %d NON QUALIFIES, %d NON LISIBLES ; etat lu QUALIFIE a %d points sur 8" % (st["Q"], st["N"], st["L"], r0q)),
       dans("par point (QUALIFIES / juges) : %s, %s ;" % (", ".join(pp[:4]), ", ".join(pp[4:])))]
for x in "ABCD":
    phr.append(dans("etalement de la meilleure fenetre sous %s : mediane %.4f, plus grand %.4f" % (x, med(et[x]), max(et[x]))))
for x in "BCD":
    phr.append(dans("accord %s / A, |ln| : mediane %.4f, plus grand %.4f" % (x, med(ac[x]), max(ac[x]))))
phr.append(dans("consigne (e), |ln(G_dep / Gamma_pl(A))| : mediane %.4f, plus grand %.4f ; au-dessus de tau a %d etats sur %d." % (
    med(dp), max(dp), sum(d > 0.05 for d in dp), len(dp))))
phr.append(dans("sur les %d lectures de (ii) elle s'ecarte de 2 eta <W> de %.0e au pire" % (nlect, fl)))
mb = re.search(r"pire ecart relatif au lecteur d'exploration ([0-9.e+-]+) ;", open(os.path.join(D, "essai_bloc_lecteur_v1.log")).read())
phr.append(bool(mb) and dans("concorde a %s pres en relatif" % mb.group(1)))
ctl("R11", all(phr), "reglage : %d etats, %s, rang 0 QUALIFIE a %d ; phrases tenues %d sur %d ; plus petite distance a une borne %.4f" % (
    n, st, r0q, sum(phr), len(phr), min(MARGE)))

# R12 (iii) et (iv) : la sonde du gel sur le conteneur de machine 1
REF = {b["j"]: b for b in json.load(open(os.path.join(CLONE, "journal/tp_reference_machine2_v1.json")))["balayage"]}
s1 = json.load(open(essai("sonde_ter_etage1.json"))); tp = []; okp = True
for t in s1["temoin"]:
    for x in "ABCD":
        b = fenetre({k: t["traj"][x][str(k)]["gamma"] for k in KS}, KS); okp = okp and b[0] <= 1.05
        tp.append(abs(math.log(b[2] / REF[t["j"]]["Gamma_ref"]))); okp = okp and tp[-1] <= 0.05 + REF[t["j"]]["u_ref"]
tn3 = []; okn = True
for t in s1["temoin_negatif"]:
    for x in "ABCD":
        v = [t["traj"][x][str(k)]["gamma"] for k in KS]; tn3.append(t["traj"][x]["3"]["gamma"])
        okn = okn and fenetre(dict(zip(KS, v)), KS)[0] > 1.05 and all(abs(v[i + 1] / v[i] - 0.5) < 2e-3 for i in range(11))
s0 = json.load(open(essai("sonde_ter_etage0.json"))); pa = 0.0; pr = 0.0; n0 = 0; hors = 0
for pt in s0["points"]:
    dep = {e["rang"]: e for e in P[pt["id"]]["etats"]}
    for e in pt["etats"]:
        for k in ("2", "3", "4"):
            r_ = e["traj"]["depot"][k]; gd = dep[e["rang"]]["Gamma_2D"][k]; n0 += 1
            pa = max(pa, abs(r_["gamma"] - gd)); pr = max(pr, abs(r_["gamma"] - gd) / gd) if gd > 1.33e-10 else pr
            hors += not (r_["suivi"] and abs(r_["gamma"] - gd) <= 1e-3 * gd + 1e-12)
ctl("R12", okp and okn and n0 == 84 and hors == 0 and len(tp) == 8 and len(tn3) == 8
    and dans("pire |ln(Gamma_pl / Gamma_ref)| = %.4f" % max(tp)) and dans("vaut %.0e a %.0e a k = 3" % (min(tn3), max(tn3)))
    and dans("pire ecart absolu %.1e, pire ecart relatif au-dessus de mille planchers %.1e" % (pa, pr))
    and s0["sonde_canon"] == s1["sonde_canon"] == canon(os.path.join(D, "sonde_qualification_EB_ter_machine1_v1.py")),
    "TP %d plateaux, pire |ln| %.4f ; TN sans plateau %s ; etage 0 : %d lectures, %d hors, pire absolu %.1e, pire relatif %.1e" % (
        len(tp), max(tp), okn, n0, hors, pa, pr))

# R13 (v) l'etalement des largeurs deposees aux etats juges
ctl("R13", dans("s'ecartent de %.3f en mediane et de %.3f au pire" % (med(etal), max(etal))), "mediane %.3f, max %.3f sur %d etats" % (med(etal), max(etal), len(etal)))

# R14 annonces : identifiants, probabilites, somme de A-1
sec = T.split("## 11. Annonces")[1].split("## 12.")[0]
ids = re.findall(r"^  (A-\d+)\b", sec, re.M)
a1 = sec.split("\n  A-1 ")[1].split("\n  A-2 ")[0]
pr1 = [float(x) for x in re.findall(r" : (0\.\d+)", a1)]
pro = [float(x) for x in re.findall(r"(?<![\d.])(0\.\d+)(?= ?[.;:,)\n])", sec)]
ctl("R14", len(ids) >= 6 and ids == ["A-%d" % (i + 1) for i in range(len(ids))] and abs(sum(pr1) - 1.0) < 1e-9 and len(pr1) == 6,
    "%d annonces ; probabilites de A-1 : %s (somme %.2f)" % (len(ids), pr1, sum(pr1)))

# R15 ouvertures et pieces nommees
piec = ["qualification_EB_ter_pre_enregistrement_v1.md", "sonde_qualification_EB_ter_machine1_v1.py", "lecteur_plateau_bloc_machine1_v1.py",
        "lecture_qualification_EB_ter_machine1_v1.py", "banc_feuille_ter_machine1_v1.py", "reference_ancres_ter_machine1_v1.json"]
ctl("R15", dans('"ouvre" (15/11/2026, 08 h 38)') and dans('"go" (15/11/2026, 10 h 28)') and all(p in T for p in piec)
    and all(os.path.exists(os.path.join(D, p)) for p in piec[1:]) and canon(MAN_NOTE) in T,
    "ouvertures datees ; six pieces nommees presentes")

nb = sum(1 for r in RES if not r[1])
print("RELEVE : %d controles, %d tenus, %d mordent %s" % (len(RES), len(RES) - nb, nb, [r[0] for r in RES if not r[1]]))
sys.exit(0 if nb == 0 else 1)
