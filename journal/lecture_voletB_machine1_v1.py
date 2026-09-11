# Lecture machine 1 du run du volet B (lot m2 579cf0a6bed9ac76) contre ma piece opposable D2_prediction_P_D1_5_machine1_v1.json (9537d740be94bf91) :
# P2 : periodes re-derivees des enveloppes brutes, bandes, verdict ; P1 : seuils, ratio, ensemble explosif ; parite : identite, versee.
import json, sys, math, numpy as np
J = json.load(open(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/vB/run_R4_voletB_machine2_v1.json'))
G = json.load(open(sys.argv[2] if len(sys.argv) > 2 else '/home/claude/D2/D2_prediction_P_D1_5_machine1_v1.json'))
print(f"d2 cite {J['d2']} (attendu 9537d740be94bf91) ; moteur {J['moteur']} ; gardes mordues {J['n_gardes_mordues']}/{len(J['gardes'])}")
print("\n=== P2 : periode de l'enveloppe sous le seuil ===")
p, w2, g = 6, 2.0, 0.05; D = w2*w2-1; da = 87.766204
hors = 0; per = {}
for col in J['P2']['colonnes']:
    ks = [k for k in col if not isinstance(col[k], (list, dict))]
    env = np.array(col['env']) if 'env' in col else None
    s = col['s']; tr = J['P2']['tranche']; pred = next(r for r in G['P2']['predictions'] if abs(r['s'] - s) < 1e-9)
    if env is not None:
        n = len(env); t = (np.arange(n)+1)*tr
        loc = [i for i in range(1, n-1) if env[i] > env[i-1] and env[i] >= env[i+1] and env[i] > 1.03*env.min()]
        tm = [t[i] for i in loc]; P = float(np.mean(np.diff(tm))) if len(tm) >= 2 else None
    else: P = col.get('periode'); tm = []
    lo, hi = pred['bande']; dans = P is not None and lo <= P <= hi; hors += (not dans)
    a_eff = math.pi*p*D/(g*P*s**4) if P else None
    per[s] = (P, a_eff)
    print(f"  s={s:.2f} : maxima {len(tm)} ; periode re-derivee {P:.1f} ; predite {pred['periode_enveloppe_predite']:.1f} bande [{lo:.0f},{hi:.0f}] -> {'DANS' if dans else 'HORS'} ; a' effectif = {a_eff:.2f} (derive 87.77 ; rapport {a_eff/da:.4f}) ; env min/max = {env.min():.4f}/{env.max():.4f} = {env.min()/s:.3f} s / {env.max()/s:.3f} s (derive 2.024 / 2.333, rapport {env.min()/env.max():.3f} vs 0.868) ; champs m2 : {{ {', '.join(f'{k}={col[k]}' for k in ks if k not in ('s',))} }}")
print(f"  verdict P2 (hors bande a DEUX des trois s) : {'FALSIFIEE' if hors >= 2 else 'TENUE'} ; hors {hors}/3")
print("\n=== P1 : ile ===")
for sg, c in J['P1']['colonnes'].items():
    ks = {k: c[k] for k in c if not isinstance(c[k], (list, dict))}
    print(f"  sgn {sg} : {ks}")
    if 't_exp' in c and 'grille_repr' in c:
        sgr = np.array([float(x) for x in c['grille_repr']]); t = np.array(c['t_exp'], float)
        for T in (400, 1600):
            e = (t > 0) & (t <= T); idx = np.where(e)[0]
            comps = np.split(idx, np.where(np.diff(idx) != 1)[0] + 1) if len(idx) else []
            print(f"     T={T} : premier explosif noeud {int(np.argmax(e)) if e.any() else None} s*={sgr[int(np.argmax(e))]:.6f} ; explosifs {int(e.sum())}/96 ; composantes contigues {len(comps)} ({'INTERVALLE' if len(comps)==1 else 'ILOTS'})")
print("  ratios m2 :", J['P1']['ratios'], "; parite_pas :", J['P1']['parite_pas'])
