# Re-derivation machine 1 du volet D depuis les t_exp bruts a T = 6400 (run_R4_voletD_machine2_v2.json 58e79a822583b401)
# contre le JSON P-4 depose (e66549fd72f4239b) : grilles identiques au repr, t_exp <= 1600 identiques, indices a 400/1600/6400.
import json, sys
import numpy as np
V2 = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/cs/run_R4_voletD_machine2_v2.json'
P4 = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/P4/lot_machine2_2026-09-02_P4_run_v4/mesures_P4_jumeau_machine2_v1.json'
D = json.load(open(V2)); P = json.load(open(P4))
print("cles d'un resultat v2 :", list(D['resultats'][0].keys()))
for r in D['resultats']:
    g = next(x for x in P['grilles'] if x['colonne'] == r['colonne'] and x['grille'] == r['grille'])
    sR = np.array([float(x) for x in r['grille_repr']]); sP = np.array([float(x) for x in g['grille_repr']])
    tR = np.array(r['t_exp'], float); tP = np.array(g['t_exp'], float)
    same_grid = bool(np.array_equal(sR, sP)); same_t1600 = bool(np.array_equal(np.where(tR <= 1600, tR, -1.0), tP))
    def first(T): e = (tR > 0) & (tR <= T); return (int(np.argmax(e)), float(sR[int(np.argmax(e))])) if e.any() else (None, None)
    i4, s4 = first(400); i16, s16 = first(1600); i64, s64 = first(6400)
    nE = int((tR > 0).sum()); print(f"  {r['colonne']} {r['grille']} : grille == P-4 : {same_grid} ; t_exp<=1600 == P-4 : {same_t1600} ; i400={i4} i1600={i16} i6400={i64} -> deplacement 1600->6400 : {i64 - i16} noeud ; s*(6400)={s64:.10f} ; explosifs a 6400 : {nE}/96 (a 1600 : {int(((tR>0)&(tR<=1600)).sum())})")
