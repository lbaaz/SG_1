# -*- coding: ascii -*-
"""LECTURE DE L'ELIGIBILITE DES CELLULES CANDIDATES -- machine 1, v1, 2026-11-15. Arithmetique sur les sorties de
eligibilite_creneaux_machine1_v1.py ; aucun calcul de chaine ni de 2D ici.
Classement d'une etiquette : celui de lecture_carte_machine1_v1.py (da84e6de4fdfd23b), fonction lire, recopiee.
Eligibilite d'une cellule des creneaux N et P (regle COMMUNE) : boite N <= 74, au moins 8 etats jugeables parmi les 14
etiquettes predites, dont au moins 5 dans le domaine.
Eligibilite d'une cellule des creneaux BN et BP (regle DE BORD) : boite N <= 74, au moins 8 etats jugeables, dont au moins
2 dans le domaine et au moins 2 hors du domaine.
Un w2 candidat est ELIGIBLE si toutes ses cellules le sont (cinq pour N et P, une pour BN et BP).
Usage : python3 -I lecture_eligibilite_machine1_v1.py <sortie.json> <eligibilite_*.json> [<eligibilite_*.json> ...]"""
import sys, json, math
from fractions import Fraction as F
SORTIE = sys.argv[1]; ENTREES = sys.argv[2:]
PLANCHER10 = 1.33e-12; E_MAX = 0.7; STAB_MAX = 0.05; N_ETATS = 14; N_COUT = 74; JUG_MIN = 8; DOM_MIN = 5; BORD_MIN = 2
ORDRE = ("N", "P", "BN", "BP"); N_ATTENDU = {"N": 9, "P": 18, "BN": 8, "BP": 9}; F_ATTENDUS = {"N": 5, "P": 5, "BN": 1, "BP": 1}

def lire(e):
    """Classement d'une etiquette par la chaine seule (texte de lecture_carte_machine1_v1.py, sans les marques discriminantes)."""
    if e["vide"]:
        return {"jug": False, "dom": False, "G": None}
    dans = e["e_bord"] < E_MAX and e["stab3"] is not None and e["stab3"] <= STAB_MAX
    G = e["G3"] if dans else e["G2"][2]
    jug = bool(e["stable1"] and e["stable2"] and G > PLANCHER10)
    return {"jug": jug, "dom": bool(jug and dans), "G": G}

cells = []
for f in ENTREES:
    cells += json.load(open(f))["cellules"]
par = {}
for c in cells:
    es = [e for e in c["etats"] if e["rang_predit"] is not None and e["rang_predit"] < N_ETATS]; assert len(es) == N_ETATS
    ls = [lire(e) for e in es]; nj = sum(l["jug"] for l in ls); nd = sum(l["dom"] for l in ls); s = c["id"]
    if s in ("N", "P"):
        el = bool(c["N"] <= N_COUT and nj >= JUG_MIN and nd >= DOM_MIN)
    else:
        el = bool(c["N"] <= N_COUT and nj >= JUG_MIN and nd >= BORD_MIN and nj - nd >= BORD_MIN)
    Gs = [l["G"] for l in ls if l["jug"]]
    par.setdefault(s, {}).setdefault(c["w2"], []).append({"creneau": s, "w2": c["w2"], "facteur": c["facteur"], "g": c["g"], "graine": c["graine"], "N": c["N"],
        "n_jug": nj, "n_dom": nd, "n_hors": nj - nd, "eligible": el, "etiquettes": [[e["n1"], e["n2"], int(l["jug"]), int(l["dom"])] for e, l in zip(es, ls)],
        "lgG_min": math.log10(min(Gs)) if Gs else None, "lgG_max": math.log10(max(Gs)) if Gs else None})
out = {"reglage": {"plancher10": PLANCHER10, "e_max": E_MAX, "stab_max": STAB_MAX, "n_etats": N_ETATS, "N_cout": N_COUT, "jug_min": JUG_MIN, "dom_min": DOM_MIN, "bord_min": BORD_MIN},
       "creneaux": {}, "cellules": []}
tot = 0
for s in ORDRE:
    assert len(par[s]) == N_ATTENDU[s] and all(len(v) == F_ATTENDUS[s] for v in par[s].values()), s
    print("CRENEAU %s : %d w2 candidats, %d facteur(s) ; par cellule : boite, jugeables/dans le domaine%s" % (s, len(par[s]), F_ATTENDUS[s], "/hors domaine" if s in ("BN", "BP") else ""))
    liste = []
    for w in sorted(par[s], key=lambda x: F(x)):
        v = sorted(par[s][w], key=lambda r: F(r["facteur"])); ok = all(r["eligible"] for r in v); liste.append({"w2": w, "eligible": ok})
        if s in ("N", "P"):
            det = "   ".join("x%-3s %2d %2d/%2d%s" % (r["facteur"], r["N"], r["n_jug"], r["n_dom"], "" if r["eligible"] else "!") for r in v)
        else:
            det = "   ".join("x%-3s %2d %2d/%2d/%2d%s" % (r["facteur"], r["N"], r["n_jug"], r["n_dom"], r["n_hors"], "" if r["eligible"] else "!") for r in v)
        print("  %-10s delta %+.3f   %s   %s" % (w, float(F(w)) - 2.0, det, "ELIGIBLE" if ok else "INELIGIBLE"))
        out["cellules"] += v; tot += len(v)
    out["creneaux"][s] = {"candidats": liste, "n": len(liste), "n_eligibles": sum(l["eligible"] for l in liste)}
    print("  -> %d w2 eligibles sur %d" % (out["creneaux"][s]["n_eligibles"], len(liste)))
print("TOTAL : %d cellules, %d eligibles ; w2 candidats : %d, eligibles : %d" % (tot, sum(r["eligible"] for r in out["cellules"]), sum(c["n"] for c in out["creneaux"].values()),
      sum(c["n_eligibles"] for c in out["creneaux"].values())))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
