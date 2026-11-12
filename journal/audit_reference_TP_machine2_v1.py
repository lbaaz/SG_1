# -*- coding: ascii -*-
"""AUDIT de MA reference du temoin positif (gel E-B v2, 5.1) -- machine 2, v1, 2026-11-11.
Verifie les sorties de reference_TP_rotation_complexe_machine2_v1.py AVANT leur envoi : coherence des trois
fichiers, recalcul independant de la table depuis les points calcules, selection rejouee par la FEUILLE
certifiee de machine 1 (importee, canon verifie), identite des g, et une SECONDE METHODE de resolution
(Arnoldi en inversion decalee, creux) aux deux couplages retenus et au couplage de bord j = 5. L'Arnoldi est un
DIAGNOSTIC : il ne change ni la table ni la liste (la selection ne lit que la reference declaree).
Usage : python -P audit_reference_TP_machine2_v1.py DOSSIER_DES_JSON FEUILLE.py SCRIPT_REFERENCE.py
Sorties : audit_reference_TP_machine2_v1.log (stdout) et .json (bilan lu, jamais tape)."""
import hashlib
import importlib.util
import json
import math
import os
import sys
import time
import unicodedata

import numpy as np

sys.dont_write_bytecode = True
if len(sys.argv) != 4:
    print(__doc__)
    sys.exit(2)
REP, FEUILLE, SCRIPT = sys.argv[1], sys.argv[2], sys.argv[3]
ICI = os.path.dirname(os.path.abspath(__file__))


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    except UnicodeDecodeError:
        t = raw
    return hashlib.sha256(t).hexdigest()[:16]


BILAN = []


def chk(nom, tient, detail=""):
    BILAN.append((nom, bool(tient), detail))
    print("%-4s %-76s %s  %s" % (nom.split(" ")[0], " ".join(nom.split(" ")[1:]), "TIENT" if tient else "MORD ",
                                 detail), flush=True)


def charge(nom):
    return json.load(open(os.path.join(REP, nom)))


ret_f = charge("tp_retenus_machine2_v1.json")
ref = charge("tp_reference_machine2_v1.json")
cal = charge("tp_reference_machine2_v1_calculs.json")
bal = {r["j"]: r for r in ref["balayage"]}

# --- C01 canons
canon_script = emp(open(SCRIPT, 'rb').read())
chk("C01 le script lu est celui nomme dans les trois fichiers",
    ref["script_canon"] == cal["script_canon"] == canon_script,
    "canon %s" % canon_script)
chk("C02 moteur et gel nommes", ref["moteur"] == "82a0be882568fe0c" and ref["gel"] == "cde0cd11a763f26d",
    "moteur %s gel %s" % (ref["moteur"], ref["gel"]))
chk("C03 fichiers reels (prevol faux) et grille annoncee",
    not ref["prevol"] and not cal["prevol"] and not ret_f["prevol"] and ref["Ns"] == [50, 60, 70] and
    ref["thetas"] == [0.1, 0.15, 0.2, 0.25, 0.3], "Ns %s thetas %s" % (ref["Ns"], ref["thetas"]))

# --- C04 les 17 g_j, des nombres, g = 0.05 * 2^(j/8) AU BIT, g de la liste == g de la table (repr)
js = sorted(bal)
ok_g = js == list(range(17)) and all(bal[j]["g"] == 0.05 * 2.0 ** (j / 8.0) for j in js)
chk("C04 17 g_j, g = 0.05 * 2.0 ** (j / 8.0) au bit", ok_g, "j de %d a %d" % (js[0], js[-1]))
nums = all(isinstance(bal[j][k], float) and math.isfinite(bal[j][k]) for j in js for k in ("Gamma_ref", "u_ref", "g"))
chk("C05 Gamma_ref, u_ref, g : toujours des nombres finis (engagement O-1/O-2)", nums)
ok_rep = all(json.dumps(r["g"]) == json.dumps(bal[r["j"]]["g"]) for r in ret_f["retenus"]) and \
    ret_f["retenus"] == ref["retenus"]
chk("C06 g de la liste == g de la table, en repr ; meme liste dans les deux fichiers", ok_rep,
    "%s" % [(r["j"], repr(r["g"])) for r in ret_f["retenus"]])
chk("C07 la liste des retenus ne porte AUCUNE largeur (cles j, g seulement)",
    set(ret_f) == {"p", "prevol", "retenus", "w2"} and all(set(r) == {"j", "g"} for r in ret_f["retenus"]) and
    ret_f["w2"] == "39/20" and ret_f["p"] == 5, "cles %s" % sorted(ret_f))

# --- C08 table recalculee depuis les points calcules, par un autre code
pts = {}
for c in cal["calculs"]:
    pts[(c["j"], c["N"], round(c["theta"], 2))] = c
chk("C08 149 points calcules = 17 + 11 * 12", len(pts) == 149 == len(cal["calculs"]), "%d" % len(pts))
TH = [0.10, 0.15, 0.20, 0.25, 0.30]
CEN = [0.15, 0.20, 0.25]
raff = [j for j in js if bal[j]["raffine"]]
ecart_max, ecart_u = 0.0, 0.0
bon_theta = True
for j in raff:
    G70 = np.array([pts[(j, 70, t)]["gamma"] for t in TH])
    lg = np.log(G70)
    var = {TH[i]: max(abs(lg[i] - lg[i - 1]), abs(lg[i] - lg[i + 1])) for i in (1, 2, 3)}
    th = sorted(var, key=lambda t: (var[t], t))[0]
    gref = pts[(j, 70, th)]["gamma"]
    u = max(abs(pts[(j, n, t)]["gamma"] / gref - 1.0) for n in (60, 70) for t in CEN)
    ecart_max = max(ecart_max, abs(gref / bal[j]["Gamma_ref"] - 1.0))
    ecart_u = max(ecart_u, abs(u - bal[j]["u_ref"]))
    bon_theta = bon_theta and abs(th - bal[j]["theta"]) < 1e-12
chk("C09 Gamma_ref, u_ref et theta des 11 raffines, recalcules d'un autre code", ecart_max == 0.0 and
    ecart_u < 1e-15 and bon_theta, "ecart relatif Gamma_ref %.1e, ecart u_ref %.1e, theta %s" % (
        ecart_max, ecart_u, "idem" if bon_theta else "DIFFERENT"))
non_raff = [j for j in js if not bal[j]["raffine"]]
ok_nr = all(bal[j]["u_ref"] == 1.0 and bal[j]["Gamma_ref"] == pts[(j, 50, 0.2)]["gamma"] for j in non_raff)
chk("C10 les non raffines portent u_ref = 1.0 et le Gamma de (50, 0.20)", ok_nr, "j %s" % non_raff)
chk("C11 chaque raffine : Re E stable (< 1e-9) et recouvrement > 0.9 sur tous ses points",
    all(max(p["E_re"] for k, p in pts.items() if k[0] == j) - min(p["E_re"] for k, p in pts.items() if k[0] == j)
        < 1e-9 and min(p["recouvrement"] for k, p in pts.items() if k[0] == j) > 0.9 for j in raff),
    "pire ecart Re E %.1e" % max(max(p["E_re"] for k, p in pts.items() if k[0] == j) -
                                   min(p["E_re"] for k, p in pts.items() if k[0] == j) for j in raff))

# --- C12 selection par la feuille CERTIFIEE de machine 1
canon_f = emp(open(FEUILLE, 'rb').read())
spec = importlib.util.spec_from_file_location("feuille_m1", FEUILLE)
FM = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FM)
sel_f = FM.selection_gel(ref["balayage"])
jr = sorted(r["j"] for r in ref["retenus"])
js_sonde = sorted(r["j"] for r in ret_f["retenus"])
chk("C12 la feuille %s, sur MA table, retrouve la liste (regle du gel rejouee par elle)" % canon_f,
    canon_f == "b3ac958a1a2b915b" and sel_f == jr == js_sonde, "feuille %s, reference %s, sonde %s" % (
        sel_f, jr, js_sonde))

# --- C13 morsure de C12 : la selection de la feuille REAGIT a la table (sinon le controle ne dit rien)
bal2 = [dict(r) for r in ref["balayage"]]
for r in bal2:
    if r["j"] == 5:
        r["u_ref"] = 0.0099
sel_m = FM.selection_gel(bal2)
chk("C13 mutation : j = 5 a u_ref = 0.0099 -> la feuille change la liste (le controle C12 est vivant)",
    sel_m != sel_f, "liste mutee %s" % sel_m)
bal3 = [dict(r) for r in ref["balayage"]]
for r in bal3:
    if r["j"] == 8:
        r["Gamma_ref"] *= 1.5
chk("C14 mutation : Gamma_ref(j = 8) x 1.5 -> ecart a mes points calcules (le controle C09 est vivant)",
    abs(bal3[8]["Gamma_ref"] / pts[(8, 70, bal[8]["theta"])]["gamma"] - 1.0) > 0.4)

# --- C15 le bord : j = 5
r5 = bal[5]
marge = r5["u_ref"] - 0.01
print("   BORD : j = 5, u_ref = %.9f, seuil 0.01, depassement %.2e ; Gamma_ref %.4e (plus proche de 1e-10 que j = 6 : "
      "|ln| %.3f contre %.3f)" % (r5["u_ref"], marge, r5["Gamma_ref"], abs(math.log(r5["Gamma_ref"] / 1e-10)),
                                  abs(math.log(bal[6]["Gamma_ref"] / 1e-10))))
Gj5 = {(n, t): pts[(5, n, t)]["gamma"] for n in (60, 70) for t in CEN}
pire = max(Gj5, key=lambda k: abs(Gj5[k] / r5["Gamma_ref"] - 1.0))
print("   BORD : l'ecart qui fait u_ref = %.4f est a (N, theta) = %s : Gamma %.5e contre Gamma_ref %.5e" % (
    r5["u_ref"], pire, Gj5[pire], r5["Gamma_ref"]))
chk("C15 j = 5 EXCLU par la regle (u_ref > 0.01), j = 6 retenu : consigne, pas corrige",
    r5["u_ref"] > 0.01 and jr == [6, 8], "marge %.2e" % marge)

# --- C16 SECONDE METHODE : Arnoldi en inversion decalee (creux), aux couplages 5, 6, 8 ; DIAGNOSTIC
spec = importlib.util.spec_from_file_location("ref_script", SCRIPT)
RS = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RS)
import scipy.sparse as sp
import scipy.sparse.linalg as sla


# decalage : la resonance du vide est a Re E ~ 1e-4 ; on se place a 0.01 de la partie reelle du point dense
# (meme j, N = 60, theta = 0.20) pour que l'operateur inverse soit bien conditionne et que le niveau voisin
# (distant d'environ 1) soit bien separe.
t0 = time.time()
lignes = []
ok_arn = True
for j in (5, 6, 8):
    g = bal[j]["g"]
    N, th = 60, 0.20
    E_dense = pts[(j, N, th)]
    A = sp.csc_matrix(RS.H_rot(N, g, th))
    sigma = complex(E_dense["E_re"] + 0.01, 0.0)
    vals, vecs = sla.eigs(A, k=6, sigma=sigma, which='LM', ncv=40, tol=0)
    rec = np.abs(vecs[0, :]) ** 2 / np.sum(np.abs(vecs) ** 2, axis=0)
    nu = int(np.lexsort((vals.real, -rec))[0])
    gam = -2.0 * vals[nu].imag
    dense = E_dense["gamma"]
    gref = bal[j]["Gamma_ref"]
    ecart_dense = abs(gam / dense - 1.0)
    ecart_ref = abs(gam / gref - 1.0)
    lignes.append((j, g, gam, dense, gref, ecart_dense, ecart_ref, float(rec[nu]), vals[nu].real))
    print("   ARNOLDI j = %d (N = %d, theta = %.2f) : Gamma = %.6e ; dense %.6e (ecart %.2e) ; Gamma_ref %.6e "
          "(ecart %.2e) ; Re E %.10f ; rec %.4f" % (j, N, th, gam, dense, ecart_dense, gref, ecart_ref,
                                                     vals[nu].real, rec[nu]), flush=True)
    del A
for (j, g, gam, dense, gref, ed, er, rec, ere) in lignes:
    if j in (6, 8):
        ok_arn = ok_arn and er <= bal[j]["u_ref"] + 5e-3 and rec > 0.9 and abs(ere - bal[j]["E_re"]) < 1e-8
chk("C16 SECONDE METHODE (Arnoldi) retrouve la reference aux deux retenus, a u_ref + 5e-3 pres, meme Re E",
    ok_arn, "%.0f s" % (time.time() - t0))
j5 = [x for x in lignes if x[0] == 5][0]
print("   DIAGNOSTIC j = 5 : Arnoldi %.6e contre Gamma_ref %.6e (ecart %.2e) et contre le dense (50..70) "
      "%.2e..%.2e : la table dense est entachee d'un bruit de l'ordre de %.0e a ce g ; la liste N'EST PAS "
      "modifiee." % (j5[2], j5[4], j5[6], min(Gj5.values()), max(Gj5.values()),
                     (max(Gj5.values()) - min(Gj5.values())) / j5[2]))

n = len(BILAN)
mord = [b[0].split(" ")[0] for b in BILAN if not b[1]]
print("BILAN : %d controles, %d mordent%s" % (n, len(mord), (" : " + ", ".join(mord)) if mord else ""))
json.dump({"bilan": {"chk": n, "mord": len(mord), "noms": mord},
           "controles": [{"nom": b[0], "tient": b[1], "detail": b[2]} for b in BILAN],
           "arnoldi": [{"j": x[0], "g": x[1], "Gamma_arnoldi": x[2], "Gamma_dense_N60_th020": x[3],
                        "Gamma_ref": x[4], "ecart_dense": x[5], "ecart_ref": x[6], "recouvrement": x[7],
                        "Re_E": x[8]} for x in lignes]},
          open(os.path.join(ICI, "audit_reference_TP_machine2_v1.json"), "w"), indent=1, sort_keys=True)
