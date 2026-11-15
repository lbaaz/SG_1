# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1, 2026-11-14. RELEVE DE SORTIE du gel "chaine d'ordre 2" : chaque nombre et chaque
# canon du gel est relu a sa source, par un autre chemin que le script qui l'a pose.
# usage : python3 -I releve_gel_ordre2_machine1_v1.py <gel.md> <dossier du lot> <clone du registre> <note.md> <note.json>
#                                                      <essai precedent.json>
import sys, os, re, json, math, hashlib, unicodedata, subprocess, importlib.util, tempfile, statistics
gel, dos, clone, note, note_json, essai_prec = sys.argv[1:7]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
T = open(gel, encoding="utf-8").read(); L = T.split("\n")
plat = " ".join(T.split())
res = []
def ctl(nom, ok, detail=""):
    res.append(bool(ok)); print("  %s  %s%s" % ("TIENT" if ok else "MORD ", nom, (" : " + detail) if detail else ""))
def dans(*phrases):
    return all(" ".join(p.split()) in plat for p in phrases)

# 1. forme
ctl("R01 forme : ASCII, sans pour-cent, lignes de 100 au plus, ligne de fin",
    all(ord(c) < 128 for c in T) and "%" not in T and max(len(l) for l in L) <= 100
    and L[-2] == "-- FIN gel_ordre2_chaine_EA_pre_enregistrement_v1 --" and L[-1] == "")
# 2. canons : pieces du lot, hors registre, registre
sec1 = T[T.index("1. PIECES CITEES"):T.index("2. CE QUI A MENE ICI")]
paires = re.findall(r"^    (\S+)  ([0-9a-f]{16})$", sec1, re.M)
lot, reg = [], []
for nom, c in paires:
    if nom.startswith(("scripts/", "journal/", "gels/")):
        reg.append((nom, c, B(os.path.join(clone, nom))))
    elif nom.startswith("note_machine1_residuel"):
        lot.append((nom, c, B(note)))
    elif nom == "ordre2_par_etat_v3.json":
        lot.append((nom, c, B(note_json)))
    else:
        p = os.path.join(dos, nom); p = p if os.path.exists(p) else os.path.join(dos, "essai", nom)
        lot.append((nom, c, B(p)))
ctl("R02 canons du lot et hors registre relus (%d)" % len(lot), len(lot) == 21 and all(a == b for _, a, b in lot),
    " ".join(n for n, a, b in lot if a != b))
tete = subprocess.run(["git", "-C", clone, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
propre = subprocess.run(["git", "-C", clone, "status", "--porcelain", "--untracked-files=no"], capture_output=True, text=True).stdout.strip()
ctl("R03 canons du registre relus a la tete %s (%d)" % (tete, len(reg)),
    len(reg) == 8 and all(a == b for _, a, b in reg) and tete == "79e77d2" and propre == "" and T.count("79e77d2") == 2)
tous = set(re.findall(r"(?<![0-9a-f.])[0-9a-f]{16}(?![0-9a-f-])", T))
connus = set(c for _, c in paires) | {"119f4e4dcbb4baba"}
ctl("R04 tout motif de 16 hexadecimaux du gel est un canon connu", tous <= connus, " ".join(sorted(tous - connus)))
# 3. la table de la section 4 contre le journal de la garde, la sonde et la feuille
sec4 = T[T.index("4. LES SEIZE POINTS"):T.index("5. LES ETATS JUGES")]
tab = re.findall(r"^    ([A-Z]\d)  w2 = (\d+/\d+)\s+facteur (\S+)\s+delta ([+-]\d\.\d\d)\s+D1 (\d\.\d{6})  c_max (\d\.\d{6})  (EN DOMAINE|HORS DOMAINE)\s+N (\d+)$", sec4, re.M)
gl = open(os.path.join(dos, "garde_aux_points_ordre2_machine1_v1.log"), encoding="ascii").read()
jl = re.findall(r"^(\S+) w2=(\S+)\s+x(\S+)\s+delta=([+-]\d\.\d\d) g=\S+ Omega_c=\S+\s+D1=(\d\.\d{6}) c_max=(\d\.\d{6}) site=\d+ (EN DOMAINE|HORS DOMAINE)\s+graine=\(.*?\) card=(\d+) r_c=\d+ N=(\d+)$", gl, re.M)
J = dict((x[0], x) for x in jl)
ok = len(tab) == 16 and len(jl) == 16
for (pid, w2, fac, d, d1, cm, st, N) in tab:
    j = J.get(pid)
    ok = ok and j is not None and (w2, fac, d, d1, cm, st, N) == (j[1], j[2], j[3], j[4], j[5], j[6], j[8])
ctl("R05 section 4 : les seize lignes sont celles du journal de la garde", ok)
spec = importlib.util.spec_from_file_location("feuille", os.path.join(dos, "lecture_ordre2_machine1_v1.py"))
Fe = importlib.util.module_from_spec(spec); spec.loader.exec_module(Fe)
def bande_de(d):
    a = abs(float(d)); return "proche" if a <= 0.06 else ("moyenne" if a <= 0.10 else ("lointaine" if a <= 0.12 else None))
role_de = lambda pid: {"C": "juge", "M": "juge", "L": "juge", "A": "ancre", "W": "temoin"}[pid[0]]
fac2 = lambda f: f if "/" in f else f + "/1"
ok = True
for (pid, w2, fac, d, d1, cm, st, N) in tab:
    att = (role_de(pid), w2, fac2(fac), bande_de(d) if role_de(pid) == "juge" else None, st, float(d1), float(cm))
    ok = ok and Fe.ATTENDUS[pid] == att and tuple(Fe.T4[pid][1:5]) + tuple(Fe.T4[pid][6:9]) == att
    ok = ok and abs(eval(w2) - 2.0 - float(d)) < 1e-9
    if role_de(pid) == "juge":
        ok = ok and Fe.T4[pid][5] == dict((b[0], b[1]) for b in Fe.BANDES)[bande_de(d)]
ctl("R06 section 4 contre la feuille : ATTENDUS et la copie du selftest, bandes et bornes", ok and len(Fe.ATTENDUS) == 16 and len(Fe.T4) == 16)
st = open(os.path.join(dos, "sonde_ordre2_machine1_v1.py"), encoding="ascii").read()
sp = re.findall(r'\("([A-Z]\d)", "(juge|ancre|temoin)", F\((\d+), (\d+)\), F\((\d+)(?:, (\d+))?\)\)', st)
ok = [x[0] for x in sp] == [x[0] for x in tab]
for x, t4 in zip(sp, tab):
    ok = ok and x[1] == role_de(t4[0]) and "%s/%s" % (x[2], x[3]) == t4[1] and "%s/%s" % (x[4], x[5] or "1") == fac2(t4[2])
ctl("R07 section 4 contre la sonde : memes points, memes roles, meme ordre, temoins en dernier", ok and len(sp) == 16 and sp[-1][0] == "W2")
# 4. jamais joues
joues = set((1.95, "1/1")) and set()
for f in ("journal/sonde_chaine_par_etat.json", "journal/sonde_domaine_G1.json"):
    for p in json.load(open(os.path.join(clone, f), encoding="ascii"))["points"]:
        joues.add((p["w2"], p["facteur"]))
for w in ("39/20", "197/100", "99/50", "101/50", "203/100", "41/20"):
    joues.add((w, "1/1"))
neufs = [(t[1], fac2(t[2])) for t in tab if role_de(t[0]) != "ancre"]
ctl("R08 les quatorze couples juges et temoins n'ont jamais ete joues ; 3/4, 4/3, 1/2 a aucun w2",
    len(neufs) == 14 and not (set(neufs) & joues) and not any(f in ("3/4", "4/3", "1/2") for _, f in joues) and len(joues) == 28,
    "%d couples joues" % len(joues))
# 5. les nombres de la section 2 contre le tableau de la note
D = json.load(open(note_json, encoding="ascii"))["points"]
dd = [(p, e) for p in D for e in p["etats"] if p["id"] not in ("T3", "T4")]
q2 = [e["q2_bas"] for _, e in dd]; q1 = [e["q1"] for _, e in dd]
ee = [abs(e["dE_2_bas"] - e["dE_2D"]) / abs(e["dE_2D"]) for _, e in dd]
cl = lambda lo, hi: [e["q2_bas"] for p, e in dd if lo - 1e-9 <= abs(p["w2f"] - 2.0) <= hi + 1e-9]
T4q = [e["q2_bas"] for p in D if p["id"] == "T4" for e in p["etats"]]; T3q = sorted(e["q2_bas"] for p in D if p["id"] == "T3" for e in p["etats"])
med = lambda pid, k: statistics.median(e[k] for p in D if p["id"] == pid for e in p["etats"])
ok = (len(dd) == 243 and len(set(p["id"] for p, _ in dd)) == 22 and "%.3f %.3f" % (min(q2), max(q2)) == "0.998 1.512"
      and "%.3f %.2f" % (min(q1), max(q1)) == "0.375 7.00" and "%.2f %.2f" % (100 * statistics.median(ee), 100 * max(ee)) == "0.11 0.50"
      and "%.4f" % max(ee) == "0.0050"
      and (len(cl(0, 0.05)), "%.3f" % max(cl(0, 0.05))) == (88, "1.101") and (len(cl(0.08, 0.10)), "%.3f" % max(cl(0.08, 0.10))) == (118, "1.512")
      and (len(cl(0.11, 0.12)), "%.3f" % max(cl(0.11, 0.12))) == (37, "1.474")
      and "%.2f %.2f" % (min(T4q), max(T4q)) == "1.82 2.69" and len(T3q) == 11 and 1 / 30.0 > T3q[0] > 1 / 32.0 and 1 / 18.0 > T3q[1] > 1 / 20.0 and T3q[2] > 0.25
      and "%.3f %.3f %.3f %.3f" % (med("H6", "q1"), med("H6", "q2_bas"), med("J1", "q1"), med("J1", "q2_bas")) == "0.958 1.229 0.897 1.197")
ok = ok and dans("[0.998 ; 1.512], contre [0.375 ; 7.00]", "0.11 pour cent en mediane, 0.50 au pire", "1.101 pour |delta| <= 0.05 (88 etats)",
                 "1.512 pour |delta| de 0.08 a 0.10 (118 etats)", "1.474 pour |delta| de 0.11 a 0.12 (37 etats)", "de 1.82 a 2.69 a 2.15",
                 "(0.958 contre 1.229 ; 0.897 contre 1.197)", "243 etats juges de 22 points", "note sur les 243 etats : 0.0050")
ctl("R09 section 2 (i), (ii), (v) et section 9 : les nombres de la note, relus dans son tableau", ok)
mieux = sum(1 for p in D if p["id"] not in ("T3", "T4") and max(abs(math.log(e["q2_bas"])) for e in p["etats"]) < max(abs(math.log(e["q1"])) for e in p["etats"]))
pasmed = [p["id"] for p in D if p["id"] not in ("T3", "T4") and statistics.median(abs(math.log(e["q2_bas"])) for e in p["etats"]) >= statistics.median(abs(math.log(e["q1"])) for e in p["etats"])]
ctl("R10 section 2 (v) : au pire etat l'ordre 2 fait mieux aux 22 points ; a la mediane, pas a H6 ni J1", mieux == 22 and sorted(pasmed) == ["H6", "J1"])
# 6. la grille de conception
cg = open(os.path.join(dos, "conception_points_ordre2_machine1_v1.log"), encoding="ascii").read()
lg = [l for l in cg.split("\n") if re.match(r"^\d+/\d+\s", l)]
def loi(w2, fac):
    l = [x for x in lg if x.split()[0] == w2 and x.split()[1] == fac][0]
    return l.split("|")[4].split()
ctl("R11 section 2 (iii) : 168 points candidats ; la loi donne 1.411 au plus a 2.10 x 2/3 et 1.711 a 2.12 x 2/3",
    len(lg) == 168 and loi("21/10", "2/3")[2] == "1.411" and loi("53/25", "2/3")[2] == "1.711"
    and re.findall(r"(\d+) points candidats", T) == ["168", "168"] and dans("1.411 au plus pour 1.512 lu", "jusqu'a 1.711"))
# 7. l'essai du bloc
eb = open(os.path.join(dos, "essai_bloc_machine1_v1.log"), encoding="ascii").read()
ctl("R12 section 2 (iv) et section 1 : les nombres de l'essai du bloc",
    "262 etats ; ecart max du bloc a la note : sur q2 0.0e+00 (relatif), sur dE 0.0e+00 (absolu)" in eb
    and "243 etats hors T3 et T4 : mediane 1.5e-06  p90 5.4e-04  max 1.6e-02" in eb
    and "-2 Im E bouge de mediane 2.7e-05  max 1.7e-01 ; Gamma_flux de mediane 4.2e-10  max 1.7e-05" in eb
    and dans("1.5e-06 en mediane et de 1.6e-02 au pire sur les 243 etats", "-2 Im E bouge jusqu'a 17 pour cent", "Gamma_flux de 1.7e-05 au plus",
             "le bloc redonne les 262 valeurs de la note au bit pres"))
# 8. selftest et banc
sl = open(os.path.join(dos, "lecture_selftest_machine1.log"), encoding="ascii").read().rstrip().split("\n")
bl = open(os.path.join(dos, "banc_feuille_ordre2_machine1_v1.log"), encoding="ascii").read().rstrip().split("\n")
n_st = sum(1 for l in sl if l.startswith("  TIENT"))
ctl("R13 selftest : %d cas tenus, aucun ne mord ; le gel le dit deux fois" % n_st,
    sl[-1] == "SELFTEST : %d cas, %d tenus" % (n_st, n_st) and not any("MORD" in l for l in sl)
    and dans("les %d cas de la feuille" % n_st, "son selftest (%d cas)" % n_st))
nt = sum(1 for l in bl if l.startswith("  T-")); ntm = sum(1 for l in bl if l.startswith("  T-") and " MORD" in l)
nc = sum(1 for l in bl if re.match(r"^  C\d", l)); ncm = sum(1 for l in bl if re.match(r"^  C\d", l) and " MORD" in l)
surv = [l.split()[0] for l in bl if " survit" in l]
ctl("R14 banc : table %d sur %d, code %d sur %d, survivante %s" % (ntm, nt, ncm, nc, " ".join(surv)),
    nt == ntm and nc - ncm == 1 and surv == ["C82b"]
    and dans("la table, %d alterations, %d mordues" % (nt, ntm), "code, %d alterations, %d mordues" % (nc, ncm), "la survivante (C82b)"))
# 9. les references d'ancre
rl = open(os.path.join(dos, "reference_ancres_ordre2_machine1_v1.log"), encoding="ascii").read()
ref = dict((m.group(1), (float(m.group(2)), float(m.group(3)))) for m in re.finditer(r"^(A\d) \(\d,\d\) eta de chaine 0\.0625\s+Gamma_flux = (\S+)\s+-2 Im E = \S+\s+dE = (\S+)", rl, re.M))
p_es = os.path.join(dos, "sonde_essai_ancres_machine1.json")          # a plat dans le lot, sous essai/ chez la plume
es = json.load(open(p_es if os.path.exists(p_es) else os.path.join(dos, "essai", "sonde_essai_ancres_machine1.json"), encoding="ascii"))
ok = True
for pid, ((n1, n2), r2d, ro2, rde) in Fe.ANCRES.items():
    e = [x for p in es["points"] if p["id"] == pid for x in p["etats"] if (x["n1"], x["n2"]) == (n1, n2)]
    ok = ok and ref[pid] == (ro2, rde) and len(e) == 1 and e[0]["chaine2"]["gammas_flux"][2] == ro2 and e[0]["chaine2"]["dE"][2] == rde
    ok = ok and abs(e[0]["Gamma_2D"]["3"] / r2d - 1) < 1e-2 and repr(r2d) in T and repr(ro2) in T and repr(rde) in T
    ok = ok and Fe.TEMOIN_ANCRES[pid] == (n1, n2, r2d, ro2, rde)
ctl("R15 gardes G-4 et G-8 : les references du gel sont celles de la feuille, du journal de reference et de l'essai", ok and len(ref) == 2)
# 10. les constantes de la feuille contre le texte
ok = (Fe.BANDES == (("proche", 1.25, "0.06"), ("moyenne", 1.6, "0.10"), ("lointaine", 2.0, "0.12")) and Fe.PLANCHER == 1.33e-13
      and Fe.DIX_PLANCHERS == 1.33e-12 and Fe.TOL_ENERGIE == 0.01 and Fe.MIN_JUGES == 6 and Fe.MIN_LISIBLES_BANDE == 3 and Fe.TOL_ANCRE == 1e-2
      and Fe.TOL_ANCRE_O2 == 1e-3 and Fe.TOL_ANCRE_DE == 1e-6 and Fe.TOL_GARDE == 5e-5 and Fe.N_ETATS == 14 and Fe.B_LOI == 2.87
      and Fe.SIGMA_J_MAX == 0.2 and Fe.POIDS_SITE_MIN == 0.5 and Fe.SUIVI_MIN == 0.9 and Fe.STABILITE_CIBLE == 2.0 and Fe.ETALEMENT_CHAINE == 2.0
      and Fe.MOTEUR_CANON == "82a0be882568fe0c" and Fe.SONDE_CANON == B(os.path.join(dos, "sonde_ordre2_machine1_v1.py"))
      and Fe.TEMOIN_CANONS == (Fe.MOTEUR_CANON, Fe.SONDE_CANON))
ok = ok and dans("PROCHE |delta| <= 0.06 B = 1.25", "MOYENNE 0.06 < |delta| <= 0.10 B = 1.6", "LOINTAINE 0.10 < |delta| <= 0.12 B = 2",
                 "p = 1.33e-13", "Gamma_2D(3) > 1.33e-12", "un ecart <= 0.01", "moins de 6 etats juges", "moins de 3 de ses 4 points",
                 "a 1e-2 pres en relatif", "Gamma_flux a 1e-3 pres", "dE a 1e-6 pres", "a 5e-5 pres", "exp(2.87 delta^2 m_bord)",
                 "ecart-type de J < 0.2", "poids sur le site (n1, n2) >= 0.5", "recouvrements de suivi >= 0.9", "G-7 la sonde qui a produit le JSON est au canon " + Fe.SONDE_CANON)
ctl("R16 les constantes de la feuille sont celles du texte (bornes, bandes, plancher, tolerances, canons)", ok)
# 11. la sonde se reconstruit
with tempfile.TemporaryDirectory() as tmp:
    out = os.path.join(tmp, "s.py")
    r = subprocess.run([sys.executable, "-I", os.path.join(dos, "construction_sonde_ordre2_machine1_v1.py"), os.path.join(clone, "scripts", "sonde_domaine_G1_machine1_v1.py"),
                        os.path.join(dos, "chaine_ordre2_bloc_machine1_v1.py"), out], capture_output=True, text=True)
    ok = r.returncode == 0 and "hunks appliques : 6" in r.stdout and B(out) == B(os.path.join(dos, "sonde_ordre2_machine1_v1.py"))
ctl("R17 la sonde se reconstruit depuis la sonde du registre : six hunks, meme canon ; le bloc y est tel quel",
    ok and open(os.path.join(dos, "chaine_ordre2_bloc_machine1_v1.py"), encoding="ascii").read() in st and st.count("len(SAUTS_HORS_ECHELLE)") == 1
    and es["reglage"]["ordre2"]["sauts_hors_echelle"] == 34 and dans("les 34 sauts"))
# 12. l'essai aux ancres : les champs de l'essai precedent
def aplat(x, pre=""):
    if isinstance(x, dict):
        for k in sorted(x):
            for y in aplat(x[k], pre + "/" + str(k)): yield y
    elif isinstance(x, list):
        for i, v in enumerate(x):
            for y in aplat(v, pre + "/" + str(i)): yield y
    else:
        yield pre, x
A = dict(aplat(es["points"])); P = dict((k, v) for k, v in aplat(json.load(open(essai_prec, encoding="ascii"))["points"]) if "duree" not in k)
ctl("R18 section 15 : les %d champs de l'essai du gel precedent sont retrouves a l'identique" % len(P),
    len(P) == 737 and all(k in A and A[k] == v for k, v in P.items()) and dans("les 737 champs")
    and es["sonde_canon"] == Fe.SONDE_CANON and es["moteur_canon"] == Fe.MOTEUR_CANON)
# 13. durees, annonces, sources diverses
cout = lambda ids: sum((int(t[7]) / 60.0) ** 6 for t in tab if t[0] in ids)
prec = sum((n / 60.0) ** 6 for n in (61, 61, 55, 55, 60, 54, 74, 74, 62, 72, 72, 60, 60, 61))
d15 = 3028.0 * cout([t[0] for t in tab if t[0] != "W2"]) / prec; dW2 = 3028.0 * cout(["W2"]) / prec
ctl("R19 section 16 : durees a l'echelle N puissance six : %.0f s pour quinze points, %.0f s pour W2" % (d15, dW2),
    abs(d15 / 3100.0 - 1) < 0.05 and abs(dW2 / 1500.0 - 1) < 0.05 and dans("de l'ordre de 3100 secondes", "de 1500 pour W2 seul", "(3028 secondes, sur batterie)"))
a1 = re.search(r"A-1  le verdict : (.*?)\n  A-2", T, re.S).group(1)
ps = [float(x) for x in re.findall(r" (0\.\d\d)(?= ;|\.$)", " " + " ".join(a1.split()))]
ctl("R20 annonce A-1 : six issues, somme %.2f" % sum(ps), len(ps) == 6 and abs(sum(ps) - 1.0) < 1e-9)
jr = open(os.path.join(clone, "journal", "POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md"), encoding="utf-8").read()
acte = open(os.path.join(clone, "journal", "journal_delta_97_domaine_G1_chaine_EA_v1.md"), encoding="utf-8").read()
ctl("R21 sources : le bruit de fils 7.32e-14, les trois regles candidates, la suite 'deriver le residuel', le verdict de l'acte",
    "7.32e-14" in jr and "7.32e-14" in T and all(x in acte for x in ("  (a) (m2, m1)", "  (b) (m2, m1)", "  (c) (m1)", "deriver le residuel", "LA GARDE NE TIENT PAS")))
nt = open(note, encoding="utf-8").read()
ctl("R22 la note : son canon, son statut et sa phrase sur le gel", B(note) == "022d32238a66df6b" and "non\ncertifi" in nt and "Un gel de la cha" in nt)
cp = open(os.path.join(dos, "chaines_aux_points_ordre2_machine1_v1.log"), encoding="ascii").read()
lm4 = [l for l in cp.split("\n") if l.startswith("M4 ")][0]
ctl("R23 les chaines aux seize points : 512 sites, aucune exception ; 0.046 a M4",
    "TOTAL : 512 sites, 0 exceptions" in cp and len(re.findall(r"^[A-Z]\d  ", cp, re.M)) == 16 and lm4.rstrip().endswith("4.6e-02")
    and dans("sur les 512 sites voisins des graines : aucune exception", "donne deja 0.046 a un site voisin de M4"))
def corps(src, nom):
    i = src.index("def %s(" % nom); j = src.index("\ndef ", i + 1)
    return src[i:j].rstrip()
anc = corps(open(os.path.join(clone, "scripts", "lecture_domaine_G1_machine1_v1.py"), encoding="ascii").read(), "motif_exclusion")
neuf = corps(open(os.path.join(dos, "lecture_ordre2_machine1_v1.py"), encoding="ascii").read(), "motif_exclusion")
ctl("R24 section 5 : les neuf premiers criteres de la feuille sont ceux de la feuille du registre, au caractere pres",
    anc.endswith("\n    return None") and neuf.startswith(anc[:-len("\n    return None")]) and neuf.count("return \"") == 12)
print("RELEVE : %d controles, %d tenus" % (len(res), sum(res)))
sys.exit(0 if all(res) else 1)
