# -*- coding: ascii -*-
"""ELIGIBILITE DES CELLULES CANDIDATES DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16.
CHAINE SEULE : aucun calcul 2D, ni dense ni creux. Etat : celui que porte le site (0, 0).
Une CELLULE est un couple (w2, profondeur m). Son couplage est
    g = kappa_m |w2 - 2| P / X_saut_reel(P, 2, 1, 0, 0, w2)     (fonction du moteur),
ARRONDI a six chiffres significatifs : le couplage de la cellule EST le nombre decimal ecrit ("%.5e").
Par cellule : barriere du moteur (avec Sigma2) du site (0, 0) ; tables des blocs d'ordre 2 et 3 deposes (M_facteur 4) ;
plateau et etendue de la chaine d'ordre 3 sous l'absorbeur adapte (bloc chaine_adaptee, dix-huit variantes).
La cellule est ELIGIBLE si la barriere finit au site m, si e_bord < 0.7, si les dix-huit largeurs sont strictement
positives et si leur etendue est <= 0.02. Un w2 est ELIGIBLE si ses quatre cellules LISIBLES (m = 3, 4, 5, 6) le
sont ; une cellule PROFONDE (m = 8, 12, 16) est RETENUE si elle est eligible, et ne decide pas du w2.
Usage : python3 -I eligibilite_vide_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <sortie.json> <creneau> [<creneau> ...]
        python3 -I eligibilite_vide_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <sortie.json> --controle <absorbeur_adapte_v1.json>"""
import sys, math, json, time, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, SORTIE = sys.argv[1:6]
ARGS = sys.argv[6:]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
assert M.P == 5 and tuple(M.CANAL) == (2, 1) and M.W1 == 1
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):                    # memoire des appels : memes valeurs, moins de calcul
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))

CRENEAUX = {"MG": [F(k, 1000) for k in range(1981, 1990)], "MP": [F(k, 1000) for k in range(1991, 2000)],
            "PP": [F(k, 1000) for k in range(2001, 2010)], "PG": [F(k, 1000) for k in range(2011, 2020)]}
ORDRE = ("MG", "MP", "PP", "PG")
KAPPA = {3: "0.0262", 4: "0.0200", 5: "0.0159", 6: "0.0130", 8: "0.00928", 12: "0.00558", 16: "0.00382"}
LISIBLES = (3, 4, 5, 6); PROFONDES = (8, 12, 16)
SEUIL_ETENDUE = 0.02; GARDE_E_BORD = 0.7; M_FACTEUR = 4

def couplage(w2, m):
    """Le couplage de la cellule : le decimal a six chiffres significatifs, et son flottant."""
    brut = float(F(KAPPA[m])) * abs(float(w2) - 2.0) * M.P / _brut(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, w2)
    texte = "%.5e" % brut
    return texte, float(texte)

def cellule(w2, m, g_force=None):
    g_txt, g = couplage(w2, m) if g_force is None else ("%r" % g_force, g_force)
    rec = {"m": m, "kappa": KAPPA[m], "g": g_txt, "lisible": m in LISIBLES}
    sites = M.barriere(0.0, 0.0, w2, g, True)
    if not sites:
        rec.update({"eligible": False, "motif": "barriere vide"}); return rec
    m_bord, e_bord = sites[-1][0], sites[-1][1]
    rec.update({"m_bord": m_bord, "e_bord": e_bord, "r_c": 2 * (m_bord + max(8, m_bord)) + 2})
    rec["N_max"] = rec["r_c"] + 100
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=M_FACTEUR); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    pl = plateau_adapte(tb, t3, 3)
    d = abs(float(w2) - 2.0)
    rec.update({"ln_G3": pl["ln_G"], "ln_G3_sur_delta": None if pl["ln_G"] is None else pl["ln_G"] - math.log(d), "etendue": pl["etendue"],
                "poids_min": pl["poids_min"], "methodes": sorted(set(x[:2] for x in pl["methodes"]))})
    motifs = []
    if m_bord != m: motifs.append("barriere a %d barreaux" % m_bord)
    if not e_bord < GARDE_E_BORD: motifs.append("e_bord %.3f" % e_bord)
    if pl["ln_G"] is None: motifs.append("largeur non positive")
    elif not pl["etendue"] <= SEUIL_ETENDUE: motifs.append("etendue %.4f" % pl["etendue"])
    rec["eligible"] = not motifs
    if motifs: rec["motif"] = " ; ".join(motifs)
    return rec

if ARGS and ARGS[0] == "--controle":
    # Le bloc rend-il ce que la note du vide a calcule ? Points de sa table B a |delta| = 0.02 : w2 = 99/50 et 101/50,
    # qui ne sont pas des candidats (centiemes). Le couplage est celui de la note, non arrondi.
    REF = json.load(open(ARGS[1])); pire = 0.0; n = 0
    print("CONTROLE du bloc contre la piece de la note du vide (w2 = 99/50 et 101/50, non candidats)")
    for b in REF["B"]:
        if abs(abs(b["delta"]) - 0.02) > 1e-12:
            continue
        w2 = F(2) + F(b["delta"]).limit_denominator(10 ** 7)
        sites = M.barriere(0.0, 0.0, w2, b["g"], True)
        tb = tables_ordre2(0.0, 0.0, w2, b["g"], sites, M_facteur=M_FACTEUR); t3 = tables_ordre3(0.0, 0.0, w2, b["g"], tb)
        for o in (2, 3):
            pl = plateau_adapte(tb, t3, o); ref = b["ordres"][str(o)]
            e1 = abs(pl["ln_G"] - math.log(abs(b["delta"])) - ref["plateau"]); e2 = abs(pl["etendue"] - ref["etendue"])
            pire = max(pire, e1, e2); n += 1
            print("  %2d barreaux, w2 = %-6s ordre %d : plateau %+.9f (note %+.9f), etendue %.6f (note %.6f)" % (
                b["m_cible"], w2, o, pl["ln_G"] - math.log(abs(b["delta"])), ref["plateau"], pl["etendue"], ref["etendue"]))
    print("  %d comparaisons, plus grand ecart %.2e" % (n, pire))
    ok = n == 20 and pire < 1e-9
    print("CONTROLE : %s" % ("TIENT" if ok else "NE TIENT PAS"))
    json.dump({"comparaisons": n, "pire_ecart": pire, "tient": ok}, open(SORTIE, "w"), indent=1, sort_keys=True)
    sys.exit(0 if ok else 1)

assert all(s in CRENEAUX for s in ARGS) and ARGS, "creneaux : MG MP PP PG"
out = {"regle": {"kappa": KAPPA, "lisibles": LISIBLES, "profondes": PROFONDES, "seuil_etendue": SEUIL_ETENDUE, "garde_e_bord": GARDE_E_BORD,
                 "M_facteur": M_FACTEUR, "variantes": VARIANTES_ADAPTEES, "seuil_flux": SEUIL_FLUX_ADAPTE, "chiffres": CHIFFRES_ADAPTE},
       "creneaux": {}}
t0 = time.time()
for s in ARGS:
    cands = []
    print("creneau %s : %d w2 candidats" % (s, len(CRENEAUX[s])), flush=True)
    for w2 in CRENEAUX[s]:
        cs = [cellule(w2, m) for m in LISIBLES + PROFONDES]
        el = all(c["eligible"] for c in cs if c["lisible"])
        cands.append({"w2": "%d/%d" % (w2.numerator, w2.denominator), "eligible": el, "cellules": cs})
        print("  %.3f  %s  %s" % (float(w2), "  ".join("m%d %s %s%s" % (c["m"], c["g"], ("%.4f" % c["etendue"]) if c.get("etendue") is not None else "----",
              "" if c["eligible"] else " !") for c in cs), "ELIGIBLE" if el else "INELIGIBLE"), flush=True)
    out["creneaux"][s] = {"candidats": cands}
    print("  -> %d w2 eligibles sur %d ; cellules profondes retenues : %d sur %d ; %.0f s" % (sum(c["eligible"] for c in cands), len(cands),
          sum(x["eligible"] for c in cands for x in c["cellules"] if not x["lisible"]), 3 * len(cands), time.time() - t0), flush=True)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s" % SORTIE)
