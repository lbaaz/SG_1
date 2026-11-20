# -*- coding: ascii -*-
"""FEUILLE DE LECTURE DES BOITES FERMEES, gel "pont" -- machine 1, v1, 2026-11-17.
Des sorties de sonde_boite_fermee_pont_machine1_v1.py (une ligne JSON par boite) et de la chaine seule, par boite :
  PART d'un niveau, en unites de |delta| :  y = c^2 / (w0 rho_3(x) |delta|) ,
      c^2 : poids du site (0, 0), premiere lecture par partition ; w0 : poids du site (0, 0) dans le niveau-vide de la
      boite ; rho_3(x) : lisse d'ordre 3 de la chaine a l'ecart x du niveau (mediane des dix-huit ln rho, calcul direct
      a cet ecart, bloc chaine du pont) ;
  SOMME : S = (somme des y) / 7.95 , 7.95 etant la largeur de la fenetre 0.05 < x < 8 en |delta| ;
  COMPTE : n, le nombre de niveaux de la fenetre ; COMPTE LIBRE : le nombre de sites (a, b), a < N, b < N, dont l'energie
      libre - a + w2 b tombe dans la meme fenetre comptee depuis 0, en fractions exactes ;
  PARTICIPATION : (somme des y)^2 / somme des y^2.
Le COMPTE d'une boite est VALIDE si son niveau-vide est suivi (poids du site (0, 0) >= 0.5 et residu <= 1e-9), si ses
deux lectures debordent la fenetre et trouvent les memes niveaux (energies a 1e-9 pres). Une boite est LISIBLE si son compte est valide et si les niveaux non fiables portent au plus 5 pour cent de
la somme des y.
Ne juge rien. Avec --contre : confrontation, cote par cote, aux boites publiees par machine 2 (meme point).
Usage : python3 -I -B lecture_boites_pont_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte>
                      <bloc chaine du pont> <sortie.json> <boites.jsonl> [<boites.jsonl> ...] [--contre <m2.jsonl> ...]"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, BLOC_P, SORTIE = sys.argv[1:7]
reste = sys.argv[7:]; CONTRE = []
if "--contre" in reste:
    i = reste.index("--contre"); CONTRE = reste[i + 1:]; reste = reste[:i]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in (BLOC2, BLOC3, BLOC_A, BLOC_P):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
X_LO, X_HI, PART_NON_FIABLE_MAX = F(1, 20), F(8), 0.05; LARGEUR = float(X_HI - X_LO)

def compte_libre(N, w2):
    d = w2 - 2; n = 0
    for b in range(N):
        for a in range(N):
            x = -(-a + w2 * b) / d
            if X_LO < x < X_HI: n += 1
    return n

boites = []
for f in reste:
    for ligne in open(f, encoding="ascii"):
        if ligne.strip(): boites.append(json.loads(ligne))
cellules = {}
for b in boites: cellules.setdefault((b["w2"], b["m"], b["g"]), []).append(b)
out = {"largeur": LARGEUR, "cellules": []}
for (w2s, m, g_txt), bs in sorted(cellules.items()):
    w2 = F(w2s); assert couplage_pont(w2, m) == g_txt
    ch = chaine_pont(w2, m, g_txt); AD = abs(ch["delta"]); recs = []
    print("CELLULE w2 = %s, m = %d, g = %s : %d boites" % (w2s, m, g_txt, len(bs)))
    print("   cote   w0          n  libre  fiables  S        participation  part non fiable  lisible")
    for b in sorted(bs, key=lambda r: r["cote"]):
        xs = [v["x"] for v in b["niveaux"]]
        lr, _ = ln_rho_pont(ch, xs, 3) if xs else ([], [])
        y = [v["c2_a"] / (b["w0"] * math.exp(l) * AD) for v, l in zip(b["niveaux"], lr)]
        tot = sum(y); nf = sum(yy for yy, v in zip(y, b["niveaux"]) if not v["fiable"])
        compte_valide = bool(b["w0"] >= 0.5 and b["residu_vide"] <= 1e-9 and b["couverte_a"] and b["couverte_b"] and b["listes_identiques"])
        lisible = bool(compte_valide and tot > 0 and nf / tot <= PART_NON_FIABLE_MAX)
        r = {"cote": b["cote"], "w0": b["w0"], "n": b["n"], "libre": compte_libre(b["cote"], w2), "fiables": b["fiables"],
             "S": tot / LARGEUR, "participation": (tot * tot / sum(yy * yy for yy in y)) if y else None,
             "part_non_fiable": (nf / tot) if tot > 0 else None, "lisible": lisible, "compte_valide": compte_valide,
             "x": xs, "y": y}
        recs.append(r)
        print("   %-5d  %.8f  %-2d %-5d  %-7d  %.4f   %-13s  %-15s  %s" % (r["cote"], r["w0"], r["n"], r["libre"], r["fiables"], r["S"],
              "%.3f" % r["participation"] if y else "-", "%.4f" % r["part_non_fiable"] if tot > 0 else "-", "oui" if lisible else "NON"))
    out["cellules"].append({"w2": w2s, "m": m, "g": g_txt, "delta": ch["delta"], "boites": recs})

if CONTRE:
    ref = {}
    for f in CONTRE:
        for ligne in open(f, encoding="ascii"):
            if ligne.strip():
                r = json.loads(ligne); ref[(r.get("barreaux", 3), r["cote"])] = r
    print("CONFRONTATION aux boites de machine 2 (meme w2, meme profondeur, meme cote) :")
    conf = []
    for c in out["cellules"]:
        for r in c["boites"]:
            q = ref.get((c["m"], r["cote"]))
            if q is None: continue
            memes = (q["n"] == r["n"]); dx = dy = dyf = None
            if memes and r["n"]:
                xo = sorted(-v["off"] for v in q["niveaux"]); xm = sorted(r["x"])
                dx = max(abs(u - v) for u, v in zip(xo, xm))
                yo = [v["y1"] for v in sorted(q["niveaux"], key=lambda v: -v["off"])]; ym = [yy for _, yy in sorted(zip(r["x"], r["y"]))]
                fo = [v["fiable"] for v in sorted(q["niveaux"], key=lambda v: -v["off"])]
                dy = max(abs(u / v - 1.0) for u, v in zip(ym, yo)); dyf = max([abs(u / v - 1.0) for u, v, f in zip(ym, yo, fo) if f] or [0.0])
            conf.append({"m": c["m"], "cote": r["cote"], "n_m2": q["n"], "n_m1": r["n"], "ecart_x_max": dx, "ecart_y_max": dy,
                         "ecart_y_max_fiables_m2": dyf, "S_m2": q["somme"], "S_m1": r["S"], "w0_m2": q["w0"], "w0_m1": r["w0"]})
            print("   m = %d cote %d : niveaux %d contre %d ; ecart max sur x %s ; sur y %s (ses fiables : %s) ; S %.4f contre %.4f ; w0 %.2e"
                  % (c["m"], r["cote"], r["n"], q["n"], "-" if dx is None else "%.1e" % dx, "-" if dy is None else "%.2e" % dy,
                     "-" if dyf is None else "%.2e" % dyf, r["S"], q["somme"], abs(r["w0"] - q["w0"])))
    out["confrontation"] = conf
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s" % SORTIE)
