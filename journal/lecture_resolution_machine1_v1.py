# Lecture machine 1 de la resolution m2 (lot 9b1d89d71774ea38) : periodes re-derivees des enveloppes a T = 4 x borne haute, bandes du gel f8face8b95486d02.
import json, sys, numpy as np
J = json.load(open(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/corr/resolution_periodes_machine2_v1.json'))
g, p, D = 0.05, 5, 1.25; lo, hi = 0.26, 0.34
print("cles :", list(J.keys())[:10])
res = J.get('resultats', J.get('cellules', []))
rows = []
for r in (res if isinstance(res, list) else list(res.values())):
    s0 = r['s0']; e = g*s0**(p-2)/D
    for tag in ('env_long', 'env_4x', 'env'):
        if tag in r: env = np.array(r[tag]); break
    else: env = None
    tr = r.get('tranche', 50); 
    if env is None: print(f"  s0={s0} : pas d enveloppe au JSON, cles {list(r.keys())}"); continue
    n = len(env); t = (np.arange(n)+1)*tr
    loc = [i for i in range(1, n-1) if env[i] > env[i-1] and env[i] >= env[i+1] and env[i] > 1.05*env.min()]
    tm = [int(t[i]) for i in loc]; P = float(np.diff(tm).mean()) if len(tm) >= 2 else None; inc = tr/max(1, len(tm)-1) if len(tm) >= 2 else None
    b = (lo/e, hi/e); resolu = P is not None and (b[0] <= P - inc and P + inc <= b[1])
    print(f"  s0={s0} eps={e:.4e} T={n*tr:.0f} maxima {tm} -> periode {P:.0f} +- {inc:.0f} ; bande [{b[0]:.0f}, {b[1]:.0f}] -> {'DANS, RESOLU' if resolu else ('DANS' if b[0] <= P <= b[1] else 'HORS')} ; C_P = {e*P:.4f}")
    rows.append((s0, e, P))
rows += [(0.20, g*0.2**3/D, 1000.0), (0.30, g*0.3**3/D, 260.0)]
rows.sort(); x = np.log([r[1] for r in rows]); y = np.log([r[2] for r in rows])
print(f"  C_P par s0 : {[(r[0], round(r[1]*r[2],4)) for r in rows]} ; pente ln P / ln eps sur {len(rows)} points : {np.polyfit(x, y, 1)[0]:.3f}")
