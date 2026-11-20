# -*- coding: ascii -*-
"""FEUILLE DE LECTURE DE LA DENSITE 2D, gel "pont" -- machine 1, v1, 2026-11-17.
Pour UNE cellule : des sorties de sonde_densite_2d_pont_machine1_v1.py aux quatre absorbeurs A, B, C, D, et de la chaine
(chaine_cellules_pont_machine1_v1.py), le rapport
    R_o(x) = rho_2D(x) / (w0 rho_o(x)) ,  o = 3 ou 2 ,
aux douze ecarts. rho_2D(x) : par absorbeur, la routine de PLATEAU deposee du lecteur (fenetre de cinq barreaux
consecutifs, parmi k = -3 a 8, de plus petit rapport max / min ; PLATEAU si ce rapport est <= 1.05 ; valeur = moyenne
geometrique des cinq), appliquee a rho lue par le flux ; puis la MEDIANE des quatre ln rho. L'ecart est LISIBLE si les
quatre absorbeurs ont un plateau et si l'etendue de leurs quatre ln rho est <= 0.02. w0 : mediane, sur les quatre
absorbeurs, de la mediane sur les barreaux suivis du poids du site (0, 0) dans l'etat-vide.
A cote, sans jugement : le plateau de la largeur du vide par absorbeur, contre le plateau de la chaine d'ordre 3.
Derivee de lecture_lisse_hors_vide_machine1_v1.py (c115412d3ca07517). Ne juge rien.
Usage : python3 -I -B lecture_densite_2d_pont_machine1_v1.py <chaine_cellules.json> <nom de la cellule> <sortie.json>
                      <sonde A.json> <sonde B.json> <sonde C.json> <sonde D.json>"""
import sys, json, math
from fractions import Fraction
CHAINE, NOM, SORTIE = sys.argv[1:4]; FICHIERS = sys.argv[4:8]
K_MIN, K_MAX, TAU, SEUIL_ABS = -3, 8, Fraction(1, 20), 0.02
def plateau(ser):                      # recopie de la routine deposee du lecteur (lecture_lecteur_gel_loi_machine1_v1.py)
    best = None
    for k0 in range(K_MIN, K_MAX - 3):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(x is None or not x > 0 for x in v): continue
        mx, mn = Fraction(max(v)), Fraction(min(v)); ok = mx <= (1 + TAU) * mn; cand = (not ok, mx / mn, k0)
        if best is None or cand < best[0]: best = (cand, v, ok)
    if best is None: return {"statut": "AUCUNE FENETRE"}
    (_, rapport, k0), v, ok = best
    return {"statut": "PLATEAU" if ok else "PAS DE PLATEAU", "k0": k0, "etalement": float(rapport) - 1.0,
            "val": math.exp(sum(math.log(x) for x in v) / 5.0)}
def mediane(v):
    s = sorted(v); n = len(s); return s[n // 2] if n % 2 else 0.5 * (s[n // 2 - 1] + s[n // 2])
CH = json.load(open(CHAINE))["cellules"][NOM]; X = json.load(open(CHAINE))["ecarts"]
d2 = {}
for f in FICHIERS:
    s = json.load(open(f))
    assert s["w2"] == CH["w2"] and s["m"] == CH["m"] and s["g"] == CH["g"] and s["X"] == X and s["r_c"] == CH["r_c"], f
    d2[s["absorbeur"]] = {int(k): v for k, v in s["k"].items()}
ABSN = ["A", "B", "C", "D"]; assert sorted(d2) == ABSN
out = {"cellule": NOM, "w2": CH["w2"], "m": CH["m"], "g": CH["g"], "X": X, "par_x": [], "vide": {}}
print("CELLULE %s : w2 = %s, m = %d, g = %s" % (NOM, CH["w2"], CH["m"], CH["g"]))
w0s = []
for a in ABSN:
    suivis = [v for v in d2[a].values() if v["suivi"]]
    p = plateau({k: (v["gamma_vide"] if v["suivi"] else None) for k, v in d2[a].items()})
    w = mediane([v["w0"] for v in suivis]) if suivis else None; w0s.append(w)
    ecart = (CH["ln_G3"] - math.log(p["val"])) if p["statut"] == "PLATEAU" else None
    out["vide"][a] = {"plateau": p, "w0": w, "barreaux_suivis": len(suivis), "ln_chaine3_sur_2d": ecart}
    print("  vide, absorbeur %s : %d barreaux suivis sur %d ; %s%s" % (a, len(suivis), len(d2[a]), p["statut"],
          "" if ecart is None else " k0 = %d, etalement %.4f, Gamma %.5e ; ln(chaine d'ordre 3 / 2D) = %+.5f" % (p["k0"], p["etalement"], p["val"], ecart)))
if any(w is None for w in w0s): raise SystemExit("ILLISIBLE : un absorbeur n'a aucun barreau suivi")
w0 = mediane(w0s); out["w0"] = w0
print("  w0 = %.8f" % w0)
print("     x   plateaux  k0 (A B C D)  etalement max  etendue entre absorbeurs  ln rho_2D     ln R3      ln R2     lisible")
for i, x in enumerate(X):
    P = {a: plateau({k: (v["rho_flux"][i] if v["suivi"] else None) for k, v in d2[a].items()}) for a in ABSN}
    tous = all(P[a]["statut"] == "PLATEAU" for a in ABSN)
    rec = {"x": x, "plateaux": P, "lisible": False}
    if tous:
        lg = [math.log(P[a]["val"]) for a in ABSN]; med = mediane(lg); et = max(lg) - min(lg)
        rec.update({"ln_rho_2d": med, "etendue_absorbeurs": et, "lisible": bool(et <= SEUIL_ABS),
                    "ln_R3": med - math.log(w0) - CH["ln_rho3"][i], "ln_R2": med - math.log(w0) - CH["ln_rho2"][i]})
        print("  %5.2f    %s     %s     %.4f         %.4f                    %9.4f   %+.4f    %+.4f    %s"
              % (x, "".join("P" if P[a]["statut"] == "PLATEAU" else "-" for a in ABSN), " ".join("%2d" % P[a]["k0"] for a in ABSN),
                 max(P[a]["etalement"] for a in ABSN), et, med, rec["ln_R3"], rec["ln_R2"], "oui" if rec["lisible"] else "NON"))
    else:
        print("  %5.2f    %s     pas de plateau aux quatre absorbeurs                                                  NON"
              % (x, "".join("P" if P[a]["statut"] == "PLATEAU" else "-" for a in ABSN)))
    out["par_x"].append(rec)
lis = [r for r in out["par_x"] if r["lisible"]]
out["ecarts_lisibles"] = len(lis)
out["ln_R3_max_abs"] = max(abs(r["ln_R3"]) for r in lis) if lis else None
out["etendue_absorbeurs_max"] = max(r["etendue_absorbeurs"] for r in lis) if lis else None
print("  %d ecarts lisibles sur %d%s" % (len(lis), len(X), "" if not lis else " ; plus grand |ln R3| lisible %.4f ; plus grande etendue entre absorbeurs %.4f"
      % (out["ln_R3_max_abs"], out["etendue_absorbeurs_max"])))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
