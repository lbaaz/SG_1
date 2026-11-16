# -*- coding: ascii -*-
"""LES DIX-HUIT VARIANTES AUX ETATS DEJA JOUES -- machine 1, v1, 2026-11-16. Hors chaine, classe 3, APRES COUP. Aucun 2D.
Verifie, par le bloc du gel "largeur du vide" (chaine_adaptee_bloc_machine1_v1.py) et sans lire les sorties de machine 2,
deux constats de sa certification (section 4) sur les etats du domaine des deltas 98 et 100 :
 (1) combien d'etats ont AU MOINS UNE des dix-huit variantes de l'absorbeur adapte hors de la tolerance rappelee de E1
     (0.05 si e_bord < 0.3, 0.10 sinon), et combien de couples (etat, variante) ;
 (2) le signe du residu ln(G3* / Gamma_plateau) (mediane des dix-huit) compare au signe de delta.
Les etats, leurs couplages et la largeur de plateau 2D sont LUS dans superposition_v1.json (lot 408b8a595cad0040).
Ce n'est PAS un rejeu d'un gel : aucun verdict n'est touche.
Usage : python3 -I -B verifie_variantes_joues_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <superposition.json> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, SUPER, SORTIE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
E = [e for e in json.load(open(SUPER))["etats"] if e["domaine"]]
out = []
for e in E:
    _cache.clear()
    w2 = F(e["w2"]); sites = M.barriere(float(e["n1"]), float(e["n2"]), w2, e["g"], True)
    tb = tables_ordre2(float(e["n1"]), float(e["n2"]), w2, e["g"], sites, M_facteur=4); t3 = tables_ordre3(float(e["n1"]), float(e["n2"]), w2, e["g"], tb)
    pl = plateau_adapte(tb, t3, 3); lp = math.log(e["Gamma_pl"])
    T = 0.05 if e["e_bord"] < 0.3 else 0.10
    q = [v - lp for v in pl["valeurs"]]
    out.append({"source": e["source"], "id": e["id"], "rang": e["rang"], "n1": e["n1"], "n2": e["n2"], "delta": e["delta"], "tolerance_E1": T,
                "q_mediane": pl["ln_G"] - lp, "etendue": pl["etendue"], "q_variantes": q, "variantes_hors": sum(1 for x in q if abs(x) > T)})
n = len(out); hors = [r for r in out if r["variantes_hors"] > 0]
print("etats du domaine : %d" % n)
print("(1) etats dont la MEDIANE est hors de la tolerance rappelee de E1 : %d" % sum(1 for r in out if abs(r["q_mediane"]) > r["tolerance_E1"]))
print("    etats dont AU MOINS UNE variante est hors de la tolerance : %d ; couples (etat, variante) hors : %d" % (len(hors), sum(r["variantes_hors"] for r in hors)))
par = {}
for r in hors:
    k = (r["source"], r["id"], r["delta"]); a = par.setdefault(k, {"etats": 0, "couples": 0, "pire": 0.0, "T": r["tolerance_E1"]})
    a["etats"] += 1; a["couples"] += r["variantes_hors"]; a["pire"] = max(a["pire"], max(abs(x) for x in r["q_variantes"]))
for k in sorted(par, key=lambda k: k[2]):
    a = par[k]; print("    %s %s (delta %+.3f) : %d etats, %d couples, pire |ln q| d'une variante %.4f pour une tolerance de %.2f (%.1f fois)" % (k[0], k[1], k[2], a["etats"], a["couples"], a["pire"], a["T"], a["pire"] / a["T"]))
neg = [r for r in out if r["delta"] < 0]; pos = [r for r in out if r["delta"] > 0]
print("(2) residu (mediane) du signe de delta : %d etats sur %d" % (sum(1 for r in out if r["q_mediane"] * r["delta"] > 0), n))
print("    delta < 0 : %d etats, residu negatif a %d, le moins negatif %+.4f" % (len(neg), sum(1 for r in neg if r["q_mediane"] < 0), max(r["q_mediane"] for r in neg)))
print("    delta > 0 : %d etats, residu positif a %d, le moins positif %+.4f" % (len(pos), sum(1 for r in pos if r["q_mediane"] > 0), min(r["q_mediane"] for r in pos)))
cel = {}
for r in out:
    cel.setdefault((r["delta"], r["source"], r["id"]), []).append(abs(r["q_mediane"]))
print("    mediane de |residu| par cellule, par delta croissant :")
for k in sorted(cel):
    v = sorted(cel[k]); m = v[len(v) // 2] if len(v) % 2 else 0.5 * (v[len(v) // 2 - 1] + v[len(v) // 2])
    print("      %+.3f %-8s %-3s %2d etats  %.4f" % (k[0], k[1], k[2], len(v), m))
json.dump({"etats": out}, open(SORTIE, "w"), indent=1, sort_keys=True)
