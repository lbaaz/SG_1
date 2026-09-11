# D2 -- LE SITE 2:1 A DEGRE PAIR AU PREMIER ORDRE (classe 3, zero run). Machine 1, 11/09/2026.
# Hamiltonien moyenne au premier ordre pres de 2:1 (angle retrograde, phi = 2 theta1 + theta2 ; a degre pair seuls les
# harmoniques a j + k PAIR existent : la 2:1 n'entre que par (4,2) = cos(2 phi), admise ssi p >= 6) :
#   h(J2, phi) = (2 - w2) J2 - (g/(p Delta)) [ a(J2) + b(J2) cos(2 phi) ],  J1 = I + 2 J2 (I conserve),
#   a = <S^p> (moyenne sur les deux angles : shift de frequence du premier ordre, absent a degre impair),
#   b = coefficient de cos(4 theta1 + 2 theta2) dans S^p,   S = X cos theta1 + Y cos theta2, X^2 = 2J1, Y^2 = 2J2/w2.
# A la resonance exacte : phi' = -(g/(p Delta)) [a' + b' cos 2phi] (derivees le long du canal), J2' = -(2g/(p Delta)) b sin 2phi.
# Si a' > b' partout, phi' garde un signe : la phase tourne, J2 oscille, AUCUN transport : ile au premier ordre (seuil vrai,
# hors du premier ordre). Si b' > a', un point fixe existe (cos 2phi = -a'/b') : capture possible, transport, canal direct
# (nombres de fenetre, comme a degre impair). Le rapport r = b'/a' est un nombre pur le long du canal.
import numpy as np, json
from math import comb
def coeffs(p, w2):
    """rend (a(X2,Y2), b(X2,Y2)) comme polynomes en X2 = 2J1, Y2 = 2J2/w2 : listes de (coef, m/2, n/2)."""
    A = []; B = []
    for m in range(0, p+1, 2):
        n = p - m
        if n % 2: continue
        A.append((comb(p, m) * comb(m, m//2) / 2**m * comb(n, n//2) / 2**n, m//2, n//2))
        if m >= 4 and n >= 2:
            B.append((comb(p, m) * 2.0**(1-m) * comb(m, (m-4)//2) * 2.0**(1-n) * comb(n, (n-2)//2) * 0.5, m//2, n//2))
    return A, B
def ev(P, X2, Y2): return sum(c * X2**i * Y2**j for c, i, j in P)
def dev(P, X2, Y2, w2):   # derivee le long du canal : dX2/dJ2 = 4 (J1 = I + 2J2), dY2/dJ2 = 2/w2
    return sum(c * (i * X2**(i-1) * Y2**j * 4 + j * X2**i * Y2**(j-1) * 2/w2) for c, i, j in P)
w2 = 2.0; Delta = w2*w2 - 1; g = 0.05
out = {}
print(f"{'p':>3} {'b/a (J0)':>9} {'b\'/a\' (J0)':>11} {'b\'/a\' canal J2 x4':>18} {'b\'/a\' J2->inf':>14}   regime au premier ordre")
for p in (4, 6, 8, 10, 12, 14):
    A, B = coeffs(p, w2)
    # condition initiale de la campagne (normalisee par s^2) : X2 = (1+w2^2)^2/Delta^2, Y2 = (2/w2) * 2 w2 / Delta^2 ... : J1 = (1+w2^2)^2/(2 Delta^2), J2 = 2 w2/Delta^2
    J1 = (1 + w2*w2)**2 / (2*Delta*Delta); J2 = 2*w2/(Delta*Delta); I = J1 - 2*J2
    def r_at(J2v):
        X2 = 2*(I + 2*J2v); Y2 = 2*J2v/w2; da, db = dev(A, X2, Y2, w2), dev(B, X2, Y2, w2); return db/da if da else float('nan')
    X2, Y2 = 2*J1, 2*J2/w2
    ra = ev(B, X2, Y2)/ev(A, X2, Y2) if B else 0.0
    r0, r4, rinf = r_at(J2), r_at(4*J2), r_at(1e6)
    regime = 'PAS de terme resonant (4,2) : ile pure' if not B else ('ILE (a\' > b\' partout) : pas de transport au premier ordre' if max(r0, r4, rinf) < 1 else 'CAPTURE POSSIBLE : canal direct au premier ordre')
    print(f"{p:>3} {ra:9.4f} {r0:11.4f} {r4:18.4f} {rinf:14.4f}   {regime}")
    out[p] = dict(b_sur_a_J0=ra, r0=r0, r4=r4, rinf=rinf, regime=regime, a=A, b=B)
json.dump(out, open('D2_premier_ordre_2_1_pair_machine1_v1.json', 'w'), indent=1)
print("\nRappel des nombres archives a 2:1 : p = 4 ile, s*(400) = 2.63449 (T-independant, delta 86 A-7 i) ; p impairs 5, 7, 9, 11 : canal direct, nombres de fenetre.")
