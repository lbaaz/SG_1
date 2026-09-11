# Lecture machine 1 du run 'periode de libration' (lot m2 09bb0eee8f817a1e) contre le gel f8face8b95486d02 (ma prediction) :
# periodes re-derivees des enveloppes du JSON, bandes recalculees, verdict par le falsifieur tel qu ecrit.
import json, sys, numpy as np
J = json.load(open(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/runP/run_periode_libration_machine2_v1.json'))
g, p, D = 0.05, 5, 1.25; lo, hi = 0.26, 0.34
print(f"gel cite {J['gel']} ; moteur {J['moteur']} ; tranche {J['tranche']} ; bande C_P {J['C_P_bande']}")
hors = 0
for r in J['resultats']:
    s0 = r['s0']; e = g*s0**(p-2)/D
    env = np.array(r['env']); n = len(env); tr = J['tranche']; t = (np.arange(n)+1)*tr
    loc = [i for i in range(1, n-1) if env[i] > env[i-1] and env[i] >= env[i+1] and env[i] > 1.05*env.min()]
    tm = [int(t[i]) for i in loc]; P = float(np.diff(tm).mean()) if len(tm) >= 2 else None
    b = (lo/e, hi/e); dans = (P is not None) and (b[0] <= P <= b[1]); hors += (not dans)
    print(f"  s0={s0} eps={e:.4e} T={n*tr:.0f} maxima {tm} -> periode {P} ; bande [{b[0]:.0f}, {b[1]:.0f}] -> {'DANS' if dans else 'HORS'} ; C_P = {e*P:.4f} ; premier apex {tm[0] if tm else None} (predit {0.30/(2*e):.0f}, ecart {abs(tm[0]-0.30/(2*e)):.0f}) ; nb de maxima {len(tm)} -> periode {'sur UN intervalle' if len(tm)==2 else 'sur '+str(len(tm)-1)+' intervalles'} ; explose {r['explose']}")
print(f"  verdict par le falsifieur (hors bande aux DEUX s0) : {'FALSIFIEE' if hors == 2 else 'TENUE'} ; hors bande {hors}/2")
