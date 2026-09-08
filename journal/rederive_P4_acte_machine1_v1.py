# Re-derivation machine 1 pour l'acte delta P-4 : chaque nombre de l'acte est
# recalcule ici depuis (grille_repr, t_exp) du JSON e66549fd72f4239b et depuis
# la forme fermee de la barriere, sans croire aucun champ de lecture du JSON.
import json, math, sys
import numpy as np
from scipy.optimize import brentq
BASE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/P4'   # racine ou les sept lots sont extraits (un dossier par lot)
J = BASE + '/lot_machine2_2026-09-02_P4_run_v4/mesures_P4_jumeau_machine2_v1.json'
D = json.load(open(J))
G, W1 = 0.05, 1.0
def barriere(p, w2, sgn):
    delta = w2*w2 - W1*W1
    if p % 2 == 0: return None, None, None, None
    kappa = w2*w2/(1+w2*w2)
    S_b = -(delta*kappa/G)**(1.0/(p-2))
    E_b = kappa*S_b*S_b*(p-2)/(2*p)
    Q = ((1+w2*w2)**2 + 4*w2*w2)/(2*delta*delta)
    E0 = lambda s: Q*s*s + (G/(p*delta))*(sgn*s)**p
    # plus petit s > 0 tel que E0(s) = E_b (E0 croissant sur [0, s] pour sgn=+1 ; pour sgn=-1, la
    # premiere racine est sous le maximum local, cherchee dans [0, s_max_local])
    if sgn > 0: hi = 10.0
    else:
        s_ml = (2*Q*delta/(G*(p-1)))**(1.0/(p-2)) * 1.0  # d/ds [Q s^2 - g s^p/(p delta)] = 0 -> s^(p-2) = 2 Q delta / (g (p-1))
        hi = s_ml
    s_b = brentq(lambda s: E0(s) - E_b, 1e-12, hi, xtol=1e-15, rtol=1e-15, maxiter=500)
    s_b0 = math.sqrt(E_b/Q)
    return s_b, s_b0, E_b, S_b
out = {'grilles': [], 'comptes': {}}
pas_P1 = math.log(1.15/0.3)/95; pas_ext = math.log(4.0)/95
tot_pair = tot_pair_expl = 0; tot_sous = tot_sous_expl = 0
seuils = []; ulp = 0; npts = 0; exact = 0
for g in D['grilles']:
    p, w2, sgn, T = g['p'], g['w2'], g['sgn'], g['T']
    s = np.array([float(x) for x in g['grille_repr']]); t = np.array(g['t_exp'], float)
    assert len(s) == 96 and len(t) == 96 and np.all(np.diff(s) > 0)
    expl1600 = (t >= 0) & (t <= 1600.0); expl400 = (t >= 0) & (t <= 400.0)
    assert np.all(expl400 <= expl1600)
    n_expl = int(expl1600.sum()); n_non = 96 - n_expl
    i400 = int(np.argmax(expl400)) if expl400.any() else None
    i1600 = int(np.argmax(expl1600)) if expl1600.any() else None
    s400 = float(s[i400]) if i400 is not None else None
    s1600 = float(s[i1600]) if i1600 is not None else None
    dln = (math.log(s1600/s400) if (s400 and s1600) else None)
    s_b, s_b0, E_b, S_b = barriere(p, w2, sgn)
    # grille attendue
    if g['grille'] == 'G_P1':
        s_ref = g['s_ref']; att = s_ref*np.logspace(math.log10(0.3), math.log10(1.15), 96); pas = pas_P1
    elif p % 2 == 1:
        att = s_b0*np.logspace(math.log10(0.5), math.log10(2.0), 96); pas = pas_ext
    else:
        att = np.logspace(math.log10(1.15*g['s_ref']), math.log10(6.0), 96); pas = math.log(6.0/(1.15*g['s_ref']))/95
    rel = np.abs(s/att - 1); npts += 96; exact += int((s == att).sum()); ulp += int(((s != att) & (rel < 5e-16)).sum())
    assert rel.max() < 5e-16, (g['colonne'], g['grille'], rel.max())
    d_idx = (i1600 - i400) if (i400 is not None) else None
    rec = dict(colonne=g['colonne'], grille=g['grille'], p=p, w2=w2, sgn=sgn, n_expl=n_expl, n_non=n_non,
               somme=f"{n_expl} + {n_non} == 96", i400=i400, i1600=i1600, s400=s400, s1600=s1600, dln=dln,
               d_indice=d_idx, pas=pas, s_b=s_b, s_b0=s_b0, E_b=E_b, S_b=S_b,
               s_b_json=g['s_b'], s_b0_json=g['s_b0'], E_b_json=g['E_b'],
               n_expl_json=g['n_expl'], s400_json=g['s_400'], s1600_json=g['s_1600'],
               derive=g['derive_Eplus_max'], garde=g['garde'])
    if p % 2 == 0:
        tot_pair += 96; tot_pair_expl += n_expl; rec['pts_sous_s_b'] = None
    else:
        sous = s < s_b; rec['pts_sous_s_b'] = int(sous.sum()); rec['expl_sous_s_b'] = int((sous & expl1600).sum())
        rec['pts_sous_s_b_json'] = g['pts_sous_s_b']; rec['expl_sous_s_b_json'] = g['explosifs_sous_s_b']
        tot_sous += int(sous.sum()); tot_sous_expl += int((sous & expl1600).sum())
        rec['premier_pt_au_dessus_explose'] = (bool(expl1600[int(sous.sum())]) if sous.sum() < 96 else None)
        rec['ratio_s1600_sur_s_b'] = (s1600/s_b if s1600 else None)
        rec['pas_au_dessus_s_b'] = (math.log(s1600/s_b)/pas if s1600 else None)
    if s1600 is not None: seuils.append(rec)
    out['grilles'].append(rec)
# verification champ a champ contre le JSON (sans y croire : on compte les ecarts)
ecarts = []
for r in out['grilles']:
    for a, b in (('n_expl', 'n_expl_json'), ('s400', 's400_json'), ('s1600', 's1600_json')):
        if r[a] != r[b] and not (r[a] is None and r[b] is None): ecarts.append((r['colonne'], r['grille'], a, r[a], r[b]))
    if r['p'] % 2 == 1:
        if abs(r['s_b'] - r['s_b_json']) > 1e-12 or abs(r['s_b0'] - r['s_b0_json']) > 1e-12 or abs(r['E_b'] - r['E_b_json']) > 1e-12: ecarts.append((r['colonne'], r['grille'], 's_b/s_b0/E_b', r['s_b'], r['s_b_json']))
        if r['pts_sous_s_b'] != r['pts_sous_s_b_json'] or r['expl_sous_s_b'] != r['expl_sous_s_b_json']: ecarts.append((r['colonne'], r['grille'], 'sous s_b', r['pts_sous_s_b'], r['pts_sous_s_b_json']))
n_imp = sum(1 for r in out['grilles'] if r['p'] % 2 == 1); n_pair = 27 - n_imp
out['comptes'] = dict(grilles=len(out['grilles']), impaires=n_imp, paires=n_pair, points_pairs=tot_pair, explosifs_pairs=tot_pair_expl,
                      points_sous_s_b=tot_sous, explosifs_sous_s_b=tot_sous_expl, seuils=len(seuils),
                      d0=sum(1 for r in seuils if r['d_indice'] == 0), d1=sum(1 for r in seuils if abs(r['d_indice']) == 1),
                      dplus=sum(1 for r in seuils if abs(r['d_indice']) > 1), points_grille=npts, exacts=exact, a_1ulp=ulp,
                      derive_max=max(r['derive'] for r in out['grilles']), garde=D['meta']['garde_derive'],
                      grilles_sous_garde=sum(1 for r in out['grilles'] if r['derive'] <= D['meta']['garde_derive']),
                      ecarts_json=len(ecarts), pas_P1=pas_P1, pas_ext=pas_ext)
json.dump(out, open('rederive_P4_acte_machine1_v1.json', 'w'), indent=1)
C = out['comptes']
print("COMPTES (re-derives depuis grille_repr et t_exp, s_b depuis la forme fermee) :")
for k, v in C.items(): print(f"  {k:<20} {v}")
print("ECARTS au JSON :", ecarts if ecarts else "aucun")
print("\nSEUILS (premier s explosif de la grille a T ; indices ; d_indice ; s*/s_b ; pas au-dessus de s_b) :")
print(f"  {'colonne':<10} {'grille':<5} {'i400':>4} {'i1600':>5} {'s*(400)':>10} {'s*(1600)':>10} {'dln':>11} {'d_i':>3} {'s_b(sgn)':>10} {'s*/s_b':>7} {'pas>s_b':>7} {'1er>s_b expl':>12}")
for r in seuils:
    print(f"  {r['colonne']:<10} {r['grille']:<5} {r['i400']:>4} {r['i1600']:>5} {r['s400']:>10.6f} {r['s1600']:>10.6f} {r['dln']:>+11.8f} {r['d_indice']:>3} {r['s_b']:>10.6f} {r['ratio_s1600_sur_s_b']:>7.4f} {r['pas_au_dessus_s_b']:>7.2f} {str(r['premier_pt_au_dessus_explose']):>12}")
print("\nCOLONNES IMPAIRES : s_b(sgn), s_b0, S_b, E_b (forme fermee m1) et sous/sur s_b par grille :")
for r in out['grilles']:
    if r['p'] % 2 == 1:
        print(f"  {r['colonne']:<10} {r['grille']:<5} s_b={r['s_b']:.6f} s_b0={r['s_b0']:.6f} S_b={r['S_b']:.4f} E_b={r['E_b']:.6f} sous={r['pts_sous_s_b']:>2} expl_sous={r['expl_sous_s_b']} n_expl={r['n_expl']:>2} derive={r['derive']:.2e}")
print("\nPAIRES :")
for r in out['grilles']:
    if r['p'] % 2 == 0: print(f"  {r['colonne']:<10} {r['grille']:<5} n_expl={r['n_expl']} derive={r['derive']:.2e}")
