# Complements re-derives pour l'acte : marges d'energie (addendum 4), E0(s_max)/E_b et points au-dessus de s_b
# sur G_P1 (gel 3.4), s_ii (condition (ii)), s_CAP pair, s_lin/s_b (attente m1, hors gel) et DANS/HORS,
# excursions lineaires (lecture candidate 5.2 et predictions gelees de la jambe S).
import json, math, sys
import numpy as np
from scipy.optimize import brentq
BASE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/P4'
G = 0.05; W1 = 1.0; CAP = 1e4
R = json.load(open('rederive_P4_acte_machine1_v1.json'))
D = json.load(open(BASE + '/lot_machine2_2026-09-02_P4_run_v4/mesures_P4_jumeau_machine2_v1.json'))
DM1 = json.load(open(BASE + '/lot_machine1_2026-09-02_P4_instrument_v1/derivation_barriere_machine1_v1.json'))
REP = json.load(open(BASE + '/lot_machine1_2026-09-02_P4_reponse_v2/reprises_P4_machine1_v1.json'))
SII = []
def Q_(w2): d = w2*w2-1; return ((1+w2*w2)**2 + 4*w2*w2)/(2*d*d)
def E0(p, w2, sgn, s): d = w2*w2-1; return Q_(w2)*s*s + (G/(p*d))*(sgn*s)**p
imp = [r for r in R['grilles'] if r['p'] % 2 == 1]
cols = []
for r in imp:
    if r['grille'] == 'G_P1': cols.append(r['colonne'])
print("MARGES (dernier point sous s_b sur G_P1 U G_ext ; marge = 1 - E0(s_dernier)/E_b) :")
marges = {}
for c in cols:
    gg = [g for g in D['grilles'] if g['colonne'] == c]
    p, w2, sgn = gg[0]['p'], gg[0]['w2'], gg[0]['sgn']
    r = next(x for x in imp if x['colonne'] == c); s_b, E_b = r['s_b'], r['E_b']
    pts = np.concatenate([np.array([float(x) for x in g['grille_repr']]) for g in gg]); pts = pts[pts < s_b]
    s_last = pts.max(); marge = 1 - E0(p, w2, sgn, s_last)/E_b
    marges[c] = (s_last, marge)
    gP1 = np.array([float(x) for x in next(g for g in gg if g['grille'] == 'G_P1')['grille_repr']])
    au_dessus = int((gP1 >= s_b).sum()); ratio_E = E0(p, w2, sgn, gP1[-1])/E_b
    d = w2*w2-1; s_ii = (2*Q_(w2)/G)**(1.0/(p-2))
    print(f"  {c:<10} s_dernier={s_last:.6f} marge={100*marge:.4f} pour-cent  marge/10={marge/10:.3e}  | G_P1 : {au_dessus:>2} pts >= s_b, E0(s_max)/E_b={ratio_E:.4f}, s_b/s_max={s_b/gP1[-1]:.3f} | s_ii={s_ii:.4f} s_ii/s_b={s_ii/s_b:.2f}")
mmin = min(marges.items(), key=lambda kv: kv[1][1]); print(f"  marge minimale : {100*mmin[1][1]:.4f} pour-cent a {mmin[0]} ; /10 = {mmin[1][1]/10:.4e} ; garde gelee 1.1e-3 majore : {all(v[1]/10 >= 1.1e-3 for v in marges.values())}")
print("\nPLAFOND PAIR s_CAP (borne sqrt(2 E0) = CAP, E_j pair normalisation m2 : E0 = Q s^2 + g s^p/(p delta)) :")
for c in ['4|2.22|+1', '4|2.00|+1', '4|3.00|+1']:
    g = next(x for x in D['grilles'] if x['colonne'] == c); p, w2, sgn = g['p'], g['w2'], g['sgn']
    s_cap = brentq(lambda s: 2*E0(p, w2, sgn, s) - CAP*CAP, 1.0, 1e5); sref = g['s_ref']
    print(f"  {c:<10} s_CAP={s_cap:.2f}  = {s_cap/(1.15*sref):.1f} x haut de grille G_P1 (1.15 s_ref = {1.15*sref:.4f}) ; sans le terme (g/p)s^p : {CAP/math.sqrt(2*Q_(w2)):.0f}")
print("\nATTENTE m1 (hors gel) s_b <= s* <= s_lin : s_lin/s_b lu dans la derivation m1 80e8280603673992, s*(1600) G_ext re-derive :")
n_dans = n_hors = 0
for c in cols:
    r = next(x for x in imp if x['colonne'] == c and x['grille'] == 'G_ext')
    p_, w2_, sg_ = c.split('|'); cle_m1 = f"{p_}|{float(w2_)!r}|{sg_}"
    dm = next((x for x in DM1['colonnes'] if x['cle'] == cle_m1), None)
    if dm is not None: s_lin = dm['s_lin']
    else: s_lin = REP['b'][cle_m1]['s_lin']   # les deux colonnes ajoutees (reprises 9539f6b4c826fd4e, b)
    rl = s_lin / r['s_b']; rj = r['ratio_s1600_sur_s_b']; dans = rj <= rl
    # condition (ii), normalisation m1 (Q_m1 = delta Q_m2) : s_ii = (2 Q_m1 / g)^(1/(p-2))
    pc, wc = r['p'], r['w2']; Qm1 = (wc*wc-1)*Q_(wc); s_ii_m1 = (2*Qm1/G)**(1.0/(pc-2)); SII.append((c, s_ii_m1, s_ii_m1/r['s_b']))
    n_dans += dans; n_hors += (not dans)
    print(f"  {c:<10} s*_j/s_b={rj:.4f}  s_lin/s_b={rl:.4f}  {'DANS' if dans else 'HORS'}")
print(f"  DANS {n_dans} / HORS {n_hors}")
print("\nCONDITION (ii) (normalisation m1) : " + " ; ".join(f"{c} s_ii={v:.4f} ({q:.2f} s_b)" for c, v, q in SII) + f" ; min/max du rapport {min(q for _,_,q in SII):.2f} / {max(q for _,_,q in SII):.2f}")
print("\nEXCURSION LINEAIRE x_lin(t)/s = sgn [(1+w2^2) cos t - 2 cos(w2 t)]/delta, minimum sur [0, 400] (pas 1e-4 puis affinage) :")
def exc(w2, sgn):
    d = w2*w2-1; t = np.arange(0, 400.0+1e-9, 1e-4); x = sgn*((1+w2*w2)*np.cos(t) - 2*np.cos(w2*t))/d
    i = int(np.argmin(x)); tt = np.linspace(t[max(i-1,0)], t[min(i+1,len(t)-1)], 20001); xx = sgn*((1+w2*w2)*np.cos(tt) - 2*np.cos(w2*tt))/d
    return float(xx.min())
paires = {'2:1 (w2=2.00)': 2.00, '3:2 (w2=1.50)': 1.50, '2.22': 2.22, '2.42': 2.42, '2.50': 2.50}
ex = {}
for nom, w2 in paires.items():
    ex[w2] = (exc(w2, +1), exc(w2, -1)); print(f"  w2={nom:<14} +1 : {ex[w2][0]:+.4f} s   -1 : {ex[w2][1]:+.4f} s   |rapport| = {ex[w2][0]/ex[w2][1]:.4f}")
print("  regle lue (candidate) : le signe a la plus grande excursion colle a la barriere ; sur les paires jouees : 2:1 -> +1 ; 3:2 -> -1")
json.dump(dict(marges={k: dict(s_dernier=v[0], marge=v[1]) for k, v in marges.items()}, excursions={str(k): dict(plus=v[0], moins=v[1]) for k, v in ex.items()}), open('rederive_complements_acte_machine1_v1.json', 'w'), indent=1)
