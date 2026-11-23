# -*- coding: ascii -*-
"""OU SONT TOMBEES LES FENETRES DU LECTEUR AU RUN DU GEL "LARGEUR DU VIDE" (delta 102), aux cellules de 3 barreaux --
machine 1, v1, 2026-11-22. Hors chaine, classe 3. AUCUN CALCUL : lecture des sorties DEPOSEES du run (registre public,
tete 055be58, journal/sonde_vide_<cellule>.json), comme des donnees. Sert a comparer, APRES COUP, ce que le mandataire a
une dimension annoncait pour ces cellules (note sur le vide, 2.3 : F2 de k = -2 a +3, F1 de k = +1 a +6) a ce que la 2D
a rendu ; et a donner |d| / g et Gamma_pl / g a ces cellules.
Regle de plateau : celle de la feuille deposee (cinq barreaux consecutifs, max <= 1.05 min ; plus petit rapport, puis
plus petit k).
Usage : python3 -I fenetres_vide_delta102_machine1_v1.py <dossier journal du clone du registre>"""
import sys, os, json
DOS = sys.argv[1]
def plateau(ser):
    best = None
    for k0 in range(-3, 5):
        v = [ser[k] for k in range(k0, k0 + 5)]
        r = max(v) / min(v)
        if best is None or r < best[0] - 1e-15:
            best = (r, k0)
    return best
print("cellule  w2          g            |d| / g  eta0 / g  fenetres k0 (A B C D)   Gamma_pl (A)   Gamma_pl / g   Gamma_pl / |d|")
tout = []
for cel in ("MG3", "MP3", "PP3", "PG3"):
    s = json.load(open(os.path.join(DOS, "sonde_vide_%s.json" % cel)))
    c = s["cellule"]; g = float(c["g"]); eta0 = float(c["eta0"])
    assert s["prevol"] is False and s["fantome"]["signe"] == -1 and s["fantome"]["site"] == [0, 0]
    k0s, val = {}, {}
    for a in "ABCD":
        tr = s["fantome"]["traj"][a]
        assert all(tr[k]["suivi"] for k in tr) and len(tr) == 12
        ser = {int(k): float(tr[k]["gamma"]) for k in tr}
        r, k0 = plateau(ser); assert r <= 1.05
        k0s[a] = k0; val[a] = ser[k0]
    tout.append(k0s)
    print("%-7s  %-10s  %.5e  %.3f    %.3f     %+d %+d %+d %+d             %.5e    %.4e     %.4e" % (
        cel, c["w2"], g, eta0 / g, eta0 / g, k0s["A"], k0s["B"], k0s["C"], k0s["D"], val["A"], val["A"] / g, val["A"] / eta0))
for a in "ABCD":
    v = sorted(set(k[a] for k in tout))
    print("absorbeur %s : fenetres retenues k0 dans %s sur 4 cellules" % (a, v))
