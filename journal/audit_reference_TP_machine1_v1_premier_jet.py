# -*- coding: ascii -*-
# AUDIT m1 DE LA REFERENCE DU TEMOIN POSITIF DE m2 (lot a6c9daf3f3da3e41).
# Arguments : <dossier du lot m2> <feuille de lecture m1> <sortie json>.
# Ne joue aucune decomposition : relit, recalcule la table depuis les 149
# points bruts par un code ecrit ici, et fait juger par la feuille certifiee.
import sys, os, json, math, hashlib, unicodedata, importlib.util, copy

D, FEUILLE, SORTIE = sys.argv[1:4]
R = []


def cB(o):
    t = unicodedata.normalize("NFC", o.decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def ctl(nom, ok, detail=""):
    R.append({"nom": nom, "tient": bool(ok), "detail": detail})
    print("%-5s %s%s" % ("OK" if ok else "MORD", nom, (" : " + detail) if detail else ""))


def lire(n):
    return json.load(open(os.path.join(D, n)))


ret, tab, cal = lire("tp_retenus_machine2_v1.json"), lire("tp_reference_machine2_v1.json"), lire("tp_reference_machine2_v1_calculs.json")
bal = tab["balayage"]
THETAS, CENTRAUX, NS = [0.10, 0.15, 0.20, 0.25, 0.30], [0.15, 0.20, 0.25], [50, 60, 70]

# C01 canons des pieces citees
att = {"reference_TP_rotation_complexe_machine2_v1.py": "5fd3a1897ca0442a", "tp_retenus_machine2_v1.json": "69b3bab3bb8480b7", "tp_reference_machine2_v1.json": "4d51dd58ef456fe9", "tp_reference_machine2_v1_calculs.json": "fe25da36c3ad27fd"}
ctl("C01 canons des quatre pieces de la reference", all(cB(open(os.path.join(D, f), "rb").read()) == c for f, c in att.items()))
ctl("C02 en-tetes : gel, moteur, canon du script, w2, p, prevol faux",
    tab["gel"] == "cde0cd11a763f26d" and tab["moteur"] == "82a0be882568fe0c" and tab["script_canon"] == att["reference_TP_rotation_complexe_machine2_v1.py"]
    and tab["w2"] == ret["w2"] == "39/20" and tab["p"] == ret["p"] == 5 and tab["prevol"] is False and ret["prevol"] is False)
# C03 la liste ne porte aucune largeur
def cles(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            acc.add(k); cles(v, acc)
    elif isinstance(o, list):
        for v in o: cles(v, acc)
    return acc
kr = cles(ret, set())
ctl("C03 la liste des retenus ne porte que j et g", kr == {"p", "prevol", "retenus", "w2", "j", "g"}, "cles %s" % sorted(kr))
# C04 echelle exacte, g identique dans les deux fichiers
ech = [0.05 * 2.0 ** (j / 8.0) for j in range(17)]
ctl("C04 dix-sept lignes, j = 0..16, g_j == 0.05 * 2^(j/8) au bit", [r["j"] for r in bal] == list(range(17)) and all(r["g"] == ech[r["j"]] for r in bal))
ctl("C05 g des retenus == g de la table == echelle, au bit ; table.retenus == liste", all(x["g"] == bal[x["j"]]["g"] == ech[x["j"]] for x in ret["retenus"]) and tab["retenus"] == ret["retenus"])
# C06 des nombres partout
num = lambda v: isinstance(v, float) and math.isfinite(v)
ctl("C06 Gamma_ref et u_ref : un nombre fini a chaque ligne ; non raffine -> u_ref = 1.0",
    all(num(r["Gamma_ref"]) and num(r["u_ref"]) for r in bal) and all(r["u_ref"] == 1.0 for r in bal if not r["raffine"]),
    "raffines %s" % [r["j"] for r in bal if r["raffine"]])
# C07 les 149 points
P = {}
for c in cal["calculs"]:
    P[(c["j"], c["N"], c["theta"])] = c
raff = [r["j"] for r in bal if r["raffine"]]
attendu = {(j, 50, 0.2) for j in range(17)} | {(j, n, t) for j in raff for n in NS for t in THETAS}
ctl("C07 points bruts : 17 grossiers + grille complete des raffines, sans doublon", len(cal["calculs"]) == len(P) == len(attendu) == 149 and set(P) == attendu,
    "%d points, %d raffines x 15 + 17 - %d communs" % (len(P), len(raff), len(raff)))
# C08 la table recalculee depuis les points bruts (lectures L-1, L-2 de m2, code m1)
ecarts, th_diff = [], []
for j in raff:
    G = {t: P[(j, 70, t)]["gamma"] for t in THETAS}
    LG = {t: math.log(G[t]) for t in THETAS}
    var = {t: max(abs(LG[t] - LG[THETAS[THETAS.index(t) - 1]]), abs(LG[t] - LG[THETAS[THETAS.index(t) + 1]])) for t in CENTRAUX}
    th = sorted(CENTRAUX, key=lambda t: (var[t], t))[0]
    gref = G[th]
    u = max(abs(P[(j, n, t)]["gamma"] / gref - 1.0) for n in (60, 70) for t in CENTRAUX)
    r = bal[j]
    if th != r["theta"]: th_diff.append(j)
    ecarts.append(max(abs(gref - r["Gamma_ref"]) / gref, abs(u - r["u_ref"])))
ctl("C08 Gamma_ref, u_ref et theta des %d raffines recalcules des points bruts" % len(raff), not th_diff and max(ecarts) == 0.0, "ecart max %.1e ; theta differents %s" % (max(ecarts), th_diff))
ctl("C09 non raffines : Gamma_ref == Gamma(N = 50, theta = 0.20) du point brut, hors [1e-12, 1e-6]",
    all(r["Gamma_ref"] == P[(r["j"], 50, 0.2)]["gamma"] and not (1e-12 <= r["Gamma_ref"] <= 1e-6) for r in bal if not r["raffine"])
    and all(1e-12 <= P[(j, 50, 0.2)]["gamma"] <= 1e-6 for j in raff))
ctl("C10 aucune ligne raffinee ne porte de motif d'exclusion ajoute", not [r["j"] for r in bal if "motifs" in r])
# C11 selection : regle du gel ecrite ici, et par la feuille certifiee
cand = [r for r in bal if 1e-11 <= r["Gamma_ref"] <= 1e-7 and r["u_ref"] <= 0.01]
sel = sorted(set(min(cand, key=lambda r: (abs(math.log(r["Gamma_ref"] / x)), r["j"]))["j"] for x in (1e-10, 1e-8)))
ctl("C11 selection rejouee par un code ecrit ici == liste", sel == [x["j"] for x in ret["retenus"]] == [6, 8], "candidats %s -> %s" % ([r["j"] for r in cand], sel))
ctl("C12 canon de la feuille de lecture certifiee", cB(open(FEUILLE, "rb").read()) == "b3ac958a1a2b915b")
spec = importlib.util.spec_from_file_location("lecture_qeb", FEUILLE)
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
L.dire.f = open(os.devnull, "w")
ctl("C13 selection_gel de la feuille certifiee sur la table == liste", L.selection_gel(bal) == [6, 8])
# C14 la feuille juge un etage 1 synthetique sur la VRAIE table, sans erreur
def traj(G):
    return {str(k): {"etats": [{"suivi": True, "gamma": (G if 0 <= k <= 8 else G * 2.0 ** (-abs(k)))}]} for k in range(-2, 13)}
def s1_synth(f6=1.0, f8=1.0):
    return {"GQ3": {n: True for n in L.POINTS}, "GQ5": {n: {c: 1e-14 for c in "abcde"} for n in L.POINTS}, "GQ10": True,
            "TP": {"j%02d" % x["j"]: {"j": x["j"], "g": x["g"], "traj": {c: traj(bal[x["j"]]["Gamma_ref"] * (f6 if x["j"] == 6 else f8)) for c in ("F1G20", "F1G30")}} for x in ret["retenus"]},
            "TN": {"candidats": [[50, 25]], "traj": {str(k): {"etats": [{"suivi": True, "gamma": 5.0 * 2.0 ** (-k)}]} for k in range(-2, 13)}}}
so = sys.stdout; sys.stdout = open(os.devnull, "w")
try:
    v_ok = L.juger_etage1(s1_synth(), tab)
    v_ko = L.juger_etage1(s1_synth(f6=1.06), tab)
    t2 = copy.deepcopy(tab); t2["retenus"] = [{"j": 5, "g": bal[5]["g"]}, {"j": 8, "g": 0.1}]
    v_sel = L.juger_etage1(s1_synth(), t2)
finally:
    sys.stdout = so
ctl("C14 la feuille lit la vraie table : etage 1 synthetique a Gamma_ref -> TIENT", v_ok[0] == "TIENT", "%s %s" % (v_ok[0], v_ok[1]))
ctl("C15 controle vivant : une largeur a j = 6 fausse de 6 pour cent -> NE TIENT PAS", v_ko[0] == "NE TIENT PAS" and any("j06" in m for m in v_ko[1]), "%s" % v_ko[1])
ctl("C16 controle vivant : une liste [5, 8] contre cette table -> NE TIENT PAS", v_sel[0] == "NE TIENT PAS", "%s" % v_sel[1][:1])
# C17 le bord j = 5
r5 = bal[5]
pire = max(((n, t) for n in (60, 70) for t in CENTRAUX), key=lambda p: abs(P[(5, p[0], p[1])]["gamma"] / r5["Gamma_ref"] - 1.0))
ctl("C17 bord j = 5 : u_ref depasse 0.01 de moins de 1e-4, par un seul point", 0.0 < r5["u_ref"] - 0.01 < 1e-4,
    "u_ref = %.9f, depassement %.2e, point (N = %d, theta = %.2f) ; second plus grand ecart %.2e" % (
        r5["u_ref"], r5["u_ref"] - 0.01, pire[0], pire[1],
        sorted(abs(P[(5, n, t)]["gamma"] / r5["Gamma_ref"] - 1.0) for n in (60, 70) for t in CENTRAUX)[-2]))
ctl("C18 sans j = 5 le plus proche de 1e-10 est j = 6 ; avec lui ce serait j = 5",
    min(cand, key=lambda r: abs(math.log(r["Gamma_ref"] / 1e-10)))["j"] == 6 and min(cand + [r5], key=lambda r: abs(math.log(r["Gamma_ref"] / 1e-10)))["j"] == 5)
# C19 stabilite des deux retenus, relue des points bruts
for j in (6, 8):
    pts = [P[(j, n, t)] for n in NS for t in THETAS]
    g = [p["gamma"] for p in pts]; e = [p["E_re"] for p in pts]; rc = [p["recouvrement"] for p in pts]
    ctl("C19 j = %d : 15 points, Gamma a moins de 1 pour cent, Re E stable, etat du vide" % j,
        max(g) / min(g) - 1.0 < 0.01 and max(e) - min(e) < 1e-10 and min(rc) > 0.5,
        "Gamma %.4e a %.4e (etalement %.1e) ; Re E etalement %.1e ; recouvrement %.3f a %.3f" % (min(g), max(g), max(g) / min(g) - 1.0, max(e) - min(e), min(rc), max(rc)))
print("AUDIT m1 : %d controles, %d morsures" % (len(R), sum(1 for r in R if not r["tient"])))
json.dump({"controles": R, "table": [{"j": r["j"], "g": r["g"], "Gamma_ref": r["Gamma_ref"], "u_ref": r["u_ref"], "raffine": r["raffine"]} for r in bal]}, open(SORTIE, "w"), indent=1, sort_keys=True)
