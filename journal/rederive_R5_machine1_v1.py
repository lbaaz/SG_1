# Re-derivation machine 1 de la lecture R5 (lot m2 efb384ec6db3003b) : rangs, rho de Spearman en fractions exactes,
# p par enumeration des 720 permutations, depuis les valeurs du log m2 (r_gen du gel b5e0b5230b08d767, Gamma des points M17 v17) ;
# et controle des deux Gamma_LS citees au registre (delta 82 : 6.562e-11 a 2.02, 2.661e-09 a 2.05).
from fractions import Fraction
from itertools import permutations
import json, sys
J = json.load(open(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/R5/lecture_R5_PD2_machine2_v1.json'))
w2 = J['cellules']; rgen = J['r_gen']
G = {'Gamma_LS (H)': [2.162327e-10, 1.297614e-10, 8.442079e-11, 6.562453e-11, 9.007655e-11, 2.661393e-09],
     'Gamma_pondere (H)': [9.891569e-04, 4.837834e-04, 3.539536e-04, 5.703013e-06, 8.606365e-06, 1.358705e-05],
     'Gamma_c (EA)': [6.146984e-09, 6.102981e-09, 5.237754e-09, 1.444547e-08, 2.814418e-08, 7.791260e-08]}
def rangs(v): 
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0]*len(v)
    for k, i in enumerate(o): r[i] = k + 1
    return r
n = len(w2); rm = rangs([-x for x in rgen]); assert rm == J['resultats']['Gamma_LS (H)']['rangs_mrgen']
def rho(ra, rb): d2 = sum((a - b)**2 for a, b in zip(ra, rb)); return Fraction(1) - Fraction(6 * d2, n * (n*n - 1)), d2
# p exacte : proportion des 720 permutations des rangs de Gamma dont rho >= rho observe
def p_exact(r_obs):
    tot = 0; ok = 0
    for perm in permutations(range(1, n + 1)):
        tot += 1; ok += (rho(rm, list(perm))[0] >= r_obs)
    return Fraction(ok, tot)
print(f"n = {n} ; cellules {w2} ; rangs -r_gen {rm} ; seuils : 5/7 = {5/7:.6f} (n=7), 29/35 = {29/35:.6f} (n=6)")
for k, v in G.items():
    rg = rangs(v); r, d2 = rho(rm, rg); p = p_exact(r); att = J['resultats'][k]
    print(f"  {k:<18} rangs {rg}  rho = {r} = {float(r):+.6f}  d2 = {d2}  p = {p} = {float(p):.5f}  -> {'TENUE' if r >= Fraction(29,35) else 'NON TENUE'} a 29/35, {'TENUE' if r >= Fraction(5,7) else 'NON TENUE'} a 5/7 ; m2 : rho {att['rho']} d2 {att['d2']} p {att['p']} {att['verdict']} -> {'CONCORDE' if (str(r) == att['rho'] and d2 == att['d2'] and str(p) == att['p']) else 'ECART'}")
print("registre (delta 82) : Gamma_LS(2.02) = 6.562e-11, Gamma_LS(2.05) = 2.661e-09 :", abs(G['Gamma_LS (H)'][3] - 6.562e-11) < 1e-14, abs(G['Gamma_LS (H)'][5] - 2.661e-09) < 1e-12)
