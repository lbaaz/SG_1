# FANTOME (eta = +1) sur les 7 autres colonnes impaires et les 2 paires ayant une G_P1 (T = 1600) :
# re-derivation des references fantomes s*_f(400), s*_f(1600) de la table du gel, pour les rapports cites a l'acte.
import sys, json, time, math
import numpy as np
BASE = sys.argv[1]   # racine des lots extraits ; puis les colonnes a jouer
sys.path.insert(0, BASE + '/lot_machine1_2026-09-02_P4_instrument_v1')
from charge_moteur import charger
from integrer_jumeau_machine1_v1 import integrer_jumeau
m = charger()
D = json.load(open(BASE + '/lot_machine2_2026-09-02_P4_run_v4/mesures_P4_jumeau_machine2_v1.json'))
cols = sys.argv[2:]
pasP1 = math.log(1.15/0.3)/95
try: out = json.load(open('fantome_reste_acte_machine1_v1.json'))
except Exception: out = []
for col in cols:
    g = next(g for g in D['grilles'] if g['colonne'] == col and g['grille'] == 'G_P1'); m.P = g['p']
    grille = np.array([float(x) for x in g['grille_repr']]); t0 = time.time()
    e, idx = integrer_jumeau(m, g['w2'], grille, g['sgn'], t_max=1600.0, eta=+1.0)
    tex = np.where(idx >= 0, idx * m.DT, -1.0)
    def sT(Tq):
        ok = (tex > 0) & (tex <= Tq); return (float(grille[ok].min()), int(ok.sum()), int(np.argmax(ok))) if ok.any() else (None, 0, None)
    s400, n400, i400 = sT(400.0); s1600, n1600, i1600 = sT(1600.0)
    dln = (math.log(s1600/s400) if (s400 and s1600) else None)
    out.append(dict(colonne=col, grille='G_P1', n_expl_400=n400, n_expl_1600=n1600, s_f_400=s400, s_f_1600=s1600, i400=i400, i1600=i1600, dln=dln, pas=(dln/pasP1 if dln is not None else None), jumeau_n_expl_1600=g['n_expl'], jumeau_s1600=g['s_1600'], duree=round(time.time()-t0,1)))
    print(f"FANTOME {col} G_P1 eta=+1 : {n400}/96 a T=400, {n1600}/96 a T=1600 ; s*_f(400)={s400} (i={i400}) s*_f(1600)={s1600} (i={i1600}) ; dln={dln} ; jumeau meme grille {g['n_expl']}/96, s*_j(1600)={g['s_1600']} ({time.time()-t0:.0f} s)")
json.dump(out, open('fantome_reste_acte_machine1_v1.json', 'w'), indent=1)
