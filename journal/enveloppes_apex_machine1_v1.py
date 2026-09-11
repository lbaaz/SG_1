# Relecture des enveloppes des sondes m2 (sonde_apex_machine2_v1.json, balayage_s0_p7_machine2_v1.json, lot 6f6387f416854fec) :
# premier maximum, maxima locaux, periode de modulation, et test de la loi 1/eps A CELLULE FIXEE (le seul test non circulaire).
import json, sys, numpy as np
R = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/runR4'
g = 0.05
def eps(p, w2, s0): return g*s0**(p-2)/(w2*w2-1)
def lire(r, T, tag):
    env = np.array(r['env']); n = len(env); tr = T/n; t = (np.arange(n)+1)*tr
    loc = [i for i in range(1, n-1) if env[i] > env[i-1] and env[i] >= env[i+1] and env[i] > 1.05*env.min()]
    e = eps(r['p'], r['w2'], r['s0']); tm = [int(t[i]) for i in loc]
    per = (np.diff(tm).mean() if len(tm) >= 2 else None)
    print(f"  {tag:<22} eps={e:.2e}  env[min,max]=[{env.min():.3f},{env.max():.3f}]  maxima locaux a t={tm[:8]}  premier apex t={tm[0] if tm else None}  periode~{per if per is None else round(per)}  eps*periode={'' if per is None else round(e*per,3)}  champ t_apex m2={r.get('t_apex')}")
    return e, tm, per
S = json.load(open(f'{R}/sonde_apex_machine2_v1.json')); Bz = json.load(open(f'{R}/balayage_s0_p7_machine2_v1.json'))
print("SONDE p = 5, cellule 5|1.50 (3:2 EXACTE, piegee : a + b = 5 = p) -- tranches de 50 sur T = 3000")
res = [lire(r, r['T'], f"5|1.50|{r['sgn']:+d} s0={r['s0']}") for r in S['p5']]
(e1, t1, P1), (e2, t2, P2) = res[0], res[1]
print(f"  test 1/eps a cellule fixee (+1, s0 0.2 -> 0.3) : eps x {e2/e1:.3f} ; periode {P1:.0f} -> {P2:.0f}, rapport {P1/P2:.2f} (resolution +-50 par tranche) ; exposant {np.log(P1/P2)/np.log(e2/e1):.2f} (1/eps = 1.00)")
print("\nBALAYAGE 7|2.50|+1 (5:2 EXACTE piegee, 2:1 desaccordee de -0.5) -- tranches de 50 sur T = 3000")
for r in Bz['resultats']: lire(r, Bz['T'], f"7|2.50|+1 s0={r['s0']}")
print("  premier apex : 0.65 -> 2450, 0.80 -> 1050, 1.00 -> <= 50 (l enveloppe part de son maximum) ; eps x 2.8 puis x 3.1 : pas une loi 1/eps unique ; deux regimes au moins.")
