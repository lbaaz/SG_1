# Lecture machine 1 du run P2 a 8|2.00|+1 (lot m2 19edb2ba80f357f1) contre ma piece opposable prediction_P2_p8_machine1_v1.json (8250dc0a2719ea8c) :
# periodes re-derivees des enveloppes brutes, bandes, verdict par le falsifieur ; la version NAIVE (sans correction d'action) confrontee aux memes bandes.
import json, sys, numpy as np
J = json.load(open(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/p8/run_P2_p8_machine2_v1.json'))
G = json.load(open(sys.argv[2] if len(sys.argv) > 2 else '/home/claude/vB_rep/prediction_P2_p8_machine1_v1.json'))
print("cles :", list(J.keys())[:14])
cols = J.get('colonnes') or J.get('resultats') or J.get('P2', {}).get('colonnes')
if isinstance(cols, dict): cols = list(cols.values())
hors = 0; naive_hors = 0; tr = J.get('tranche', 10.0)
for c in cols:
    s = c['s']; pred = next(r for r in G['predictions'] if abs(r['s'] - s) < 1e-9); env = np.array(c['env']); n = len(env); t = (np.arange(n)+1)*tr
    loc = [i for i in range(1, n-1) if env[i] > env[i-1] and env[i] >= env[i+1] and env[i] > 1.03*env.min()]
    tm = [t[i] for i in loc]; P = float(np.mean(np.diff(tm))) if len(tm) >= 2 else None
    lo, hi = pred['bande']; dans = P is not None and lo <= P <= hi; hors += (not dans); nd = lo <= pred['periode_naive'] <= hi; naive_hors += (not nd)
    print(f"  s={s:.2f} : maxima {len(tm)} ; periode re-derivee {P:.2f} ; corrigee predite {pred['periode_predite']:.1f} (ecart {100*(P/pred['periode_predite']-1):+.2f} pc) ; naive {pred['periode_naive']:.1f} (ecart {100*(P/pred['periode_naive']-1):+.1f} pc) ; bande [{lo:.0f}, {hi:.0f}] -> corrigee {'DANS' if dans else 'HORS'}, naive {'DANS' if nd else 'HORS'} ; profondeur {env.min()/env.max():.4f} (annoncee {G['profondeur_annoncee']:.4f}) ; explose {c.get('explose')}")
print(f"  verdict (hors bande a DEUX des trois s) : corrigee {'FALSIFIEE' if hors >= 2 else 'TENUE'} ({hors}/3 hors) ; naive {'FALSIFIEE' if naive_hors >= 2 else 'TENUE'} ({naive_hors}/3 hors)")
