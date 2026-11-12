# -*- coding: ascii -*-
# Estimation de plume, NON OPPOSABLE : action WKB 1D du jumeau H+ (p = 5,
# w2 = 39/20) le long de u = q1 + q2, pour placer l'echelle de couplage du
# temoin positif du gel de qualification E-B. Ne lit aucun artefact.
import math
w1, w2 = 1.0, 1.95
D = w2 * w2 - w1 * w1
k = w1 * w1 * w2 * w2 / (w1 * w1 + w2 * w2)
m = (w2 ** 4 + w1 ** 4) / (w1 * w1 + w2 * w2) ** 2
om = math.sqrt(k / m)


def action(g, E0):
    gp = g / (5.0 * D ** 2.5)
    U = lambda u: 0.5 * k * u * u - gp * u ** 5
    us = (k / (5.0 * gp)) ** (1.0 / 3.0)
    if E0 >= U(us):
        return float("nan"), U(us)
    lo, hi = 0.0, us
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if U(mid) < E0 else (lo, mid)
    a = hi
    lo, hi = us, 3.0 * us
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if U(mid) > E0 else (lo, mid)
    b = lo
    n = 20000
    s = sum(math.sqrt(max(0.0, 2.0 * m * (U(a + (b - a) * (i + 0.5) / n) - E0)))
            for i in range(n))
    return 2.0 * s * (b - a) / n, U(us)


print("Delta %.4f  k_eff %.4f  m_eff %.4f  omega_eff %.4f" % (D, k, m, om))
print(" j      g       E_b        S     (om/2pi) exp(-S)")
dans = []
for j in range(17):
    g = 0.05 * 2.0 ** (j / 8.0)
    s, eb = action(g, 0.5 * om)
    G = om / (2.0 * math.pi) * math.exp(-s)
    f = 1e-11 <= G <= 1e-7
    if f:
        dans.append(j)
    print("%2d  %.5f  %7.3f  %8.3f   %.2e %s" % (j, g, eb, s, G,
                                                 "<-- fenetre" if f else ""))
print("j dans la fenetre [1e-11, 1e-7] : %s (%d sur 17)" % (dans, len(dans)))
