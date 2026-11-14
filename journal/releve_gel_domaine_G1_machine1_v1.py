# -*- coding: ascii -*-
# Hors chaine, classe 3, plume machine 1. RELEVE DE CONTROLE du gel "domaine G-1" : chaque nombre du gel est
# relu dans sa source. usage : <dossier du lot> <verdict du run precedent (json)> <sonde precedente (py)>
#                               <essai precedent (json)>
import sys, os, re, json, hashlib, unicodedata, subprocess, tempfile
ICI, VERDICT, SONDE1, ESSAI1 = sys.argv[1:5]
def canon(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
L = lambda n: open(os.path.join(ICI, n), encoding="ascii").read()
gel = L("gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md")
plat = " ".join(gel.split())             # le gel sans ses retours a la ligne, pour y chercher des phrases
mord = []
def C(nom, ok, detail=""):
    print("  %s  %s%s" % ("TIENT" if ok else "MORD ", nom, (" : " + detail) if detail else ""))
    if not ok:
        mord.append(nom)
# C1 les q medians de la section 2 (ii), relus dans le verdict du run precedent
assert canon(VERDICT) == "4fbc5f7115002054", canon(VERDICT)
v = {x["id"]: x for x in json.load(open(VERDICT, encoding="ascii"))["points"]}
med = {k: "%.3f" % v[k]["q_median"] for k in v}
att = "(1.503, 1.505, 1.418)", "1.334 a 2.04, 1.505 a 2.05, 3.735 a 2.10, 18.348 a 2.15", "0.545, 0.758, 0.842 a 1.95"
C("C1 q medians du run precedent", (med["J6"], med["A2"], med["J4"]) == ("1.503", "1.505", "1.418") and
  (med["T2"], med["J2"], med["T4"]) == ("1.334", "3.735", "18.348") and (med["J5"], med["A1"], med["J3"]) == ("0.545", "0.758", "0.842")
  and all(a in plat for a in att), "J6 %s A2 %s J4 %s T2 %s J2 %s T4 %s J5 %s A1 %s J3 %s" % tuple(med[k] for k in "J6 A2 J4 T2 J2 T4 J5 A1 J3".split()))
# C2, C3 la grille de conception
g = {}
for l in L("conception_points_domaine_G1_machine1_v1.log").split("\n"):
    m = re.match(r"(\S+)\s+(\S+)\s+\S+ \(.*?\)\s+(\d+)\s+(\d+)\s+(\d+) \| (\S+) (\S+) (\S+)\s+(EN DOMAINE|HORS DOMAINE)\s+\| \(.*?\) (\S+)\s+(\d+)/32\s+(\d+)$", l)
    if m:
        w2 = eval(m.group(1)) if "/" in m.group(1) else float(m.group(1))
        g[(round(w2, 2), m.group(2))] = {"N": int(m.group(5)), "D1": float(m.group(6)), "c": float(m.group(7)),
                                         "st": m.group(9), "modal": m.group(10), "vides": int(m.group(12))}
C("C2 grille : 156 points lus", len(g) == 156, "%d" % len(g))
C("C2 c_max a 2.05 pour 2/3, 1, 3/2", ("%.4f" % g[(2.05, "2/3")]["c"], "%.4f" % g[(2.05, "1")]["c"], "%.4f" % g[(2.05, "3/2")]["c"])
  == ("0.0635", "0.0510", "0.0381") and "0.0635, 0.0510, 0.0381, le plus grand valant 1.67 fois" in plat
  and "%.2f" % (g[(2.05, "2/3")]["c"] / g[(2.05, "3/2")]["c"]) == "1.67")
C("C3 D1 ne mord jamais, au plus 0.1944", max(x["D1"] for x in g.values()) == 0.1944 and "au plus 0.1944" in plat)
def plage(fac):
    en = sorted(w for (w, f), x in g.items() if f == fac and x["st"] == "EN DOMAINE")
    tous = sorted(w for (w, f) in g if f == fac)
    contigu = all(g[(w, fac)]["st"] == "EN DOMAINE" for w in tous if en[0] <= w <= en[-1])
    return en[0], en[-1], contigu
C("C3 plages EN DOMAINE par facteur", plage("1") == (1.90, 2.09, True) and plage("3/2") == (1.90, 2.12, True) and
  plage("2/3") == (1.92, 2.07, True), "%s %s %s" % (plage("1"), plage("3/2"), plage("2/3")))
v23 = [x["vides"] for (w, f), x in g.items() if f in ("2", "3")]
C("C3 facteurs 2 et 3 : de 10 a 18 sites sans barriere", (min(v23), max(v23)) == (10, 18), "%d a %d" % (min(v23), max(v23)))
n12 = [x["N"] for (w, f), x in g.items() if f == "1/2"]
sous = all(float(x["modal"]) < 1.33e-12 for (w, f), x in g.items() if f == "1/2" and w < 2.0)
C("C3 facteur 1/2 : N de 85 a 93, sous dix planchers sous 2.00", (min(n12), max(n12)) == (85, 93) and sous)
C("C3 hors paires cites : 1.92 x2/3 a 0.0927 EN, 1.89 x3/2 a 0.1017 HORS",
  ("%.4f" % g[(1.92, "2/3")]["c"], g[(1.92, "2/3")]["st"], "%.4f" % g[(1.89, "3/2")]["c"], g[(1.89, "3/2")]["st"])
  == ("0.0927", "EN DOMAINE", "0.1017", "HORS DOMAINE"))
# C4, C5 les points
pts = re.findall(r"^(\w\d) w2=(\S+)\s+x(\S+)\s+g=\S+ Omega_c=\S+\s+D1=(\S+) c_max=(\S+) site=\S+ (EN DOMAINE|HORS DOMAINE)", L("garde_aux_points_machine1_v1.log"), re.M)
joues = {(1.95, "1"), (1.97, "1"), (1.98, "1"), (2.02, "1"), (2.03, "1"), (2.05, "1"), (1.85, "1"), (1.90, "1"), (1.96, "1"),
         (2.04, "1"), (2.10, "1"), (2.15, "1"), (1.95, "3/2"), (1.95, "2/3"), (2.05, "3/2"), (2.05, "2/3")}
neufs = [(round(eval(w), 2), f) for pid, w, f, d1, cm, st in pts if pid[0] in "EH"]
C("C4 douze couples juges, tous distincts, aucun deja joue", len(set(neufs)) == 12 and not (set(neufs) & joues))
C("C5 les six HORS DOMAINE le sont par D2a seule", all(float(d1) <= 0.2 and float(cm) > 0.1 for pid, w, f, d1, cm, st in pts if pid[0] == "H")
  and all(float(d1) <= 0.2 and float(cm) <= 0.1 for pid, w, f, d1, cm, st in pts if pid[0] in "EA"))
C("C5 la garde aux points est celle de la grille a quatre decimales", all(
    "%.4f" % float(cm) == "%.4f" % g[(round(eval(w), 2), f)]["c"] and st == g[(round(eval(w), 2), f)]["st"] for pid, w, f, d1, cm, st in pts))
# C6 les annonces
a1 = re.search(r"A-1  le verdict : (.*?)\n  A-2", gel, re.S).group(1)
probas = [float(x) for x in re.findall(r" (0\.\d+)", a1)]
C("C6 A-1 : cinq issues, somme 1", len(probas) == 5 and abs(sum(probas) - 1.0) < 1e-12, "%s" % probas)
# C7 l'essai aux ancres rend les flottants de l'essai du gel precedent
a = json.load(open(os.path.join(ICI, "sonde_essai_ancres_machine1.json"), encoding="ascii")); b = json.load(open(ESSAI1, encoding="ascii"))
pire, nf = 0.0, 0
for pa, pb in zip(a["points"], b["points"]):
    for ea, eb in zip(pa["etats"], pb["etats"]):
        assert (ea["n1"], ea["n2"]) == (eb["n1"], eb["n2"])
        for x, y in list(zip([ea["Gamma_2D"][k] for k in "234"], [eb["Gamma_2D"][k] for k in "234"])) + \
                list(zip(ea["chaine"]["gammas"] or [], eb["chaine"]["gammas"] or [])):
            pire = max(pire, abs(x - y) / abs(y)); nf += 1
C("C7 essai aux ancres identique a celui du gel precedent", nf == 192 and pire == 0.0, "%d flottants, pire ecart %.1e" % (nf, pire))
# C8 la sonde est la construction appliquee a la sonde certifiee
assert canon(SONDE1) == "acf7e26dedfa8abc"
with tempfile.TemporaryDirectory() as d:
    out = os.path.join(d, "s.py")
    subprocess.run([sys.executable, "-I", os.path.join(ICI, "construction_sonde_domaine_G1_machine1_v1.py"), SONDE1, out],
                   check=True, capture_output=True)
    C("C8 sonde reconstruite par ses cinq hunks", canon(out) == canon(os.path.join(ICI, "sonde_domaine_G1_machine1_v1.py")))
# C9 le gel : forme et canons cites
C("C9 gel ASCII, sans pour cent, 100 colonnes au plus", all(ord(c) < 128 for c in gel) and "%" not in gel and
  max(len(l) for l in gel.split("\n")) <= 100)
cites = re.findall(r"^    (\S+\.(?:py|log|json))  ([0-9a-f]{16})$", gel, re.M)
ok = all(canon(os.path.join(ICI, n)) == c for n, c in cites if os.path.exists(os.path.join(ICI, n)))
C("C9 canons des pieces du lot cites dans le gel", ok and sum(os.path.exists(os.path.join(ICI, n)) for n, c in cites) == 12,
  "%d pieces" % sum(os.path.exists(os.path.join(ICI, n)) for n, c in cites))
C("C9 selftest 74 sur 74 ; banc 59 sur 60", "SELFTEST : 74 cas, 74 tenus" in L("lecture_selftest_machine1.log") and
  "BANC : 60 alterations, 59 mordues, 1 survivantes" in L("banc_feuille_domaine_G1_machine1_v1.log"))
print("RELEVE : %d controles mordent%s" % (len(mord), (" : " + " ; ".join(mord)) if mord else ""))
