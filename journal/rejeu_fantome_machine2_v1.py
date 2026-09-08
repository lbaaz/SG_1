# -*- coding: utf-8 -*-
"""REJEU DU FANTOME PAR MACHINE 2, pour la certification de l'acte P-4.
L'acte fonde A-4 et sa phrase externe sur des references fantomes re-derivees par machine 1
(rejeu, 14/14). Machine 2 ne les croit pas davantage : elle les rejoue elle-meme, sur les MEMES
valeurs de grille (grille_repr du JSON du run) et avec l'instrument certifie a eta = +1, qui EST
le moteur depose au bit.
t_exp = idx * DT donne les deux fenetres du meme calcul : explose a T <=> 0 < t_exp <= T."""
import importlib.util, json, math, os, sys, time, zipfile
import numpy as np

DEPOT = r"D:\devs\bocal\BOCAL4"
INST = r"C:\Users\bazil\AppData\Local\Temp\claude\d--devs-bocal\c05caab7-d368-4b5e-a48a-79643f7042ff\scratchpad\P4inst"
sys.path.insert(0, INST)
from integrer_jumeau_machine1_v1 import integrer_jumeau

spec = importlib.util.spec_from_file_location("m9", os.path.join(DEPOT, "m9_replication_v1.py"))
m9 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m9)

Z = zipfile.ZipFile(os.path.join(DEPOT, "lot_machine2_2026-09-02_P4_run_v4.zip"))
D = json.loads(Z.read("mesures_P4_jumeau_machine2_v1.json").decode("utf-8"))
CIBLES = ["5|2.00|+1", "5|2.00|-1", "7|2.00|+1", "7|2.00|-1"]
ATT = {"5|2.00|+1": (10, 43, 0.379198, 0.237766, -0.4668),
       "5|2.00|-1": (10, 43, 0.378468, 0.237308, -0.4668),
       "7|2.00|+1": (10, 30, 0.397186, 0.299320, -0.2829),
       "7|2.00|-1": (10, 30, 0.396752, 0.298993, -0.2829)}
PAS = math.log(1.15 / 0.3) / 95

print("=== REJEU FANTOME (eta = +1) SUR LES QUATRE COLONNES 2:1, GRILLE G_P1, T = 1600 ===")
print("  pas de G_P1 re-derive : ln(1.15/0.3)/95 = %.9f   (acte : 0.014145)" % PAS)
print("")
res = {}
n_ok = 0
for x in D["grilles"]:
    if x["colonne"] not in CIBLES or x["grille"] != "G_P1":
        continue
    s = np.array([float(v) for v in x["grille_repr"]], float)
    m9.P = x["p"]
    t0 = time.time()
    expl, idx = integrer_jumeau(m9, x["w2"], s, sgn=x["sgn"], t_max=1600.0, eta=+1.0)
    t_exp = np.where(idx >= 0, idx * m9.DT, -1.0)
    e400 = [i for i, v in enumerate(t_exp) if 0 < v <= 400.0]
    e1600 = [i for i, v in enumerate(t_exp) if v > 0]
    s400 = s[e400[0]] if e400 else None
    s1600 = s[e1600[0]] if e1600 else None
    dln = math.log(s1600 / s400) if (s400 and s1600) else None
    a = ATT[x["colonne"]]
    ok = (len(e400) == a[0] and len(e1600) == a[1]
          and abs(s400 - a[2]) < 5e-6 and abs(s1600 - a[3]) < 5e-6 and abs(dln - a[4]) < 5e-5)
    n_ok += ok
    pas_dln = dln / PAS
    print("  %-12s  jumeau du JSON 0/96 ; FANTOME rejoue : %2d/96 a T=400 -> %2d/96 a T=1600"
          % (x["colonne"], len(e400), len(e1600)))
    print("                s*_f(400) = %.6f   s*_f(1600) = %.6f   dln = %+.4f = %.1f pas   [%.0f s]"
          % (s400, s1600, dln, pas_dln, time.time() - t0))
    print("                acte      : %2d -> %2d, %.6f -> %.6f, dln %+.4f   -> %s"
          % (a[0], a[1], a[2], a[3], a[4], "CONFORME" if ok else "ECART <<<"))
    res[x["colonne"]] = dict(e400=len(e400), e1600=len(e1600), s400=s400, s1600=s1600,
                             dln=dln, pas=pas_dln, conforme=bool(ok))
print("")
print("  colonnes rejouees : %d ; conformes a l'acte : %d" % (len(res), n_ok))
p5 = [v["pas"] for k, v in res.items() if k.startswith("5|")]
p7 = [v["pas"] for k, v in res.items() if k.startswith("7|")]
print("  dln en pas de grille : degre 5 -> %.1f et %.1f ; degre 7 -> %.1f et %.1f"
      % (p5[0], p5[1], p7[0], p7[1]))
print("  l'acte annonce -33.0 et -20.0 pas EXACTEMENT : %s"
      % ("CONFORME" if all(abs(round(v) - v) < 0.06 for v in p5 + p7)
         and abs(round(p5[0]) + 33) < 0.5 and abs(round(p7[0]) + 20) < 0.5 else "A REGARDER"))
json.dump(res, open("rejeu_fantome_machine2_v1.json", "w"), indent=1)
