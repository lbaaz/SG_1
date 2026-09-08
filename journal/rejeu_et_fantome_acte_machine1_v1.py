# (a) REJEU jumeau (eta = -1) sur les valeurs de grille du JSON m2 : t_exp au bit ?
# (b) FANTOME (eta = +1, moteur depose au signe d'origine) sur les quatre colonnes 2:1, G_P1, T = 1600 :
#     re-derivation des references 10/96, 43/96, 30/96 et des s*_f(400), s*_f(1600) cites par le gel.
import sys, json, time, math, hashlib
import numpy as np
BASE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/P4'
sys.path.insert(0, BASE + '/lot_machine1_2026-09-02_P4_instrument_v1')   # charge_moteur.py : chemin du moteur a substituer cote BOCAL4
from charge_moteur import charger
from integrer_jumeau_machine1_v1 import integrer_jumeau
h = hashlib.sha256(open(BASE + '/lot_machine1_2026-09-02_P4_instrument_v1/integrer_jumeau_machine1_v1.py','rb').read()).hexdigest()[:16]
assert h == '171a02edfbc23864', h
m = charger()
D = json.load(open(BASE + '/lot_machine2_2026-09-02_P4_run_v4/mesures_P4_jumeau_machine2_v1.json'))
print(f"moteur c8ed357b120352c4 charge ; instrument {h} ; numpy {np.__version__} ; DT={m.DT} CAP={m.CAP} G_REF={m.G_REF} W1={m.W1}")
def trouve(col, gr): return next(g for g in D['grilles'] if g['colonne'] == col and g['grille'] == gr)
out = {'rejeu': [], 'fantome': []}
for col, gr in [('7|1.50|-1', 'G_ext'), ('5|1.50|+1', 'G_ext')]:
    g = trouve(col, gr); m.P = g['p']; grille = np.array([float(x) for x in g['grille_repr']]); t0 = time.time()
    e, idx = integrer_jumeau(m, g['w2'], grille, g['sgn'], t_max=1600.0, eta=-1.0)
    tex = np.where(idx >= 0, idx * m.DT, -1.0); ref = np.array(g['t_exp'], float)
    ident = bool(np.array_equal(tex, ref)); n = int(e.sum())
    out['rejeu'].append(dict(colonne=col, grille=gr, t_exp_au_bit=ident, n_expl_m1=n, n_expl_json=g['n_expl'], duree=round(time.time()-t0,1)))
    print(f"REJEU {col} {gr} eta=-1 T=1600 : t_exp au bit {ident} ; explosifs m1 {n} / json {g['n_expl']} ({time.time()-t0:.0f} s)")
pasP1 = math.log(1.15/0.3)/95
for col in ['5|2.00|+1', '5|2.00|-1', '7|2.00|+1', '7|2.00|-1']:
    g = trouve(col, 'G_P1'); m.P = g['p']; grille = np.array([float(x) for x in g['grille_repr']]); t0 = time.time()
    e, idx = integrer_jumeau(m, g['w2'], grille, g['sgn'], t_max=1600.0, eta=+1.0)
    tex = np.where(idx >= 0, idx * m.DT, -1.0)
    def sT(Tq):
        ok = (tex > 0) & (tex <= Tq); return (float(grille[ok].min()), int(ok.sum()), int(np.argmax(ok))) if ok.any() else (None, 0, None)
    s400, n400, i400 = sT(400.0); s1600, n1600, i1600 = sT(1600.0)
    dln = math.log(s1600/s400); jum = g['n_expl']
    out['fantome'].append(dict(colonne=col, grille='G_P1', n_expl_400=n400, n_expl_1600=n1600, s_f_400=s400, s_f_1600=s1600, i400=i400, i1600=i1600, dln=dln, pas=dln/pasP1, jumeau_n_expl_1600=jum, duree=round(time.time()-t0,1)))
    print(f"FANTOME {col} G_P1 eta=+1 : {n400}/96 a T=400, {n1600}/96 a T=1600 ; s*_f(400)={s400:.6f} (i={i400}) s*_f(1600)={s1600:.6f} (i={i1600}) ; dln={dln:+.4f} = {dln/pasP1:.1f} pas ; jumeau meme grille {jum}/96 ({time.time()-t0:.0f} s)")
json.dump(out, open('rejeu_et_fantome_acte_machine1_v1.json', 'w'), indent=1)
