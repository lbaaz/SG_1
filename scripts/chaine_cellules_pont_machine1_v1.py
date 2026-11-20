# -*- coding: ascii -*-
"""CE QUE LA CHAINE SEULE PREDIT AUX CELLULES DU GEL "PONT" -- machine 1, v1, 2026-11-17. Aucune 2D.
Par cellule (w2, m) : couplage ecrit (recalcule et compare a celui qui est passe), barriere, e_bord, geometrie du lecteur,
plateau de la largeur au vide (ordre 3, regle du bloc depose) et, aux douze ecarts, le lisse d'ordre 3, son etendue, et
le pas de l'ordre 2 a l'ordre 3.
Usage : python3 -I -B chaine_cellules_pont_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte>
                      <bloc chaine du pont> <sortie.json> <nom=w2:m:g> [<nom=w2:m:g> ...]     (w2 en fraction)"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, BLOC_P, SORTIE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
assert M.P == 5 and tuple(M.CANAL) == (2, 1) and M.W1 == 1
for bloc in (BLOC2, BLOC3, BLOC_A, BLOC_P):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
out = {"ecarts": list(ECARTS_PONT), "cellules": {}}
for arg in sys.argv[7:]:
    nom, reste = arg.split("="); w2s, ms, g_txt = reste.split(":"); w2 = F(w2s); m = int(ms)
    assert couplage_pont(w2, m) == g_txt, "couplage ecrit : %s contre %s" % (couplage_pont(w2, m), g_txt)
    ch = chaine_pont(w2, m, g_txt)
    pl = plateau_adapte(ch["tb"], ch["t3"], 3)
    r3, e3 = ln_rho_pont(ch, ECARTS_PONT, 3); r2, e2 = ln_rho_pont(ch, ECARTS_PONT, 2)
    c = {"w2": w2s, "m": m, "g": g_txt, "delta": ch["delta"], "m_bord": ch["m_bord"], "e_bord": ch["e_bord"],
         "r_c": 2 * (ch["m_bord"] + max(8, ch["m_bord"])) + 2, "ln_G3": pl["ln_G"], "etendue_vide": pl["etendue"],
         "ln_rho3": r3, "etendue_rho3": e3, "ln_rho2": r2, "pas_2_3": [a - b for a, b in zip(r2, r3)]}
    out["cellules"][nom] = c
    print("%-4s w2 = %-9s m = %d g = %s  m_bord %d  e_bord %.4f  r_c %d  G3* = %.4e (etendue %.4f)  etendue du lisse <= %.4f  |pas| <= %.4f"
          % (nom, w2s, m, g_txt, c["m_bord"], c["e_bord"], c["r_c"], math.exp(c["ln_G3"]), c["etendue_vide"], max(e3),
             max(abs(v) for v in c["pas_2_3"])), flush=True)
    print("     ln rho_3 |delta| : %s" % " ".join("%.2f" % (v + math.log(abs(ch["delta"]))) for v in r3))
    print("     pas 2 -> 3       : %s" % " ".join("%+.4f" % v for v in c["pas_2_3"]))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
print("ecrit : %s" % SORTIE)
