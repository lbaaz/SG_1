# -*- coding: ascii -*-
# Mesure : quelles ufuncs numpy de cette plateforme ne rendent PAS le double correctement arrondi,
# avec et sans le niveau de dispatch X86_V4 (a lancer deux fois, la variable dans l'environnement).
import os, sys, math, numpy as np
from fractions import Fraction
import mpmath
mpmath.mp.prec = 200
def to_double_cr(v):                       # mpf -> double correctement arrondi via Fraction
    v = mpmath.mpf(v)
    if v == 0: return 0.0
    s = -1 if v < 0 else 1
    v = abs(v)
    m, e = v.man, v.exp                    # |v| = m * 2**e exactement (man est sans signe)
    return s * float(Fraction(int(m)) * (Fraction(2) ** int(e)))
rng = np.random.default_rng(20260912)
N = 20000
tests = {}
x_pos = np.exp(rng.uniform(-3, 8, N))                       # bases > 0 (amplitudes de la campagne, 0.05 .. 3000)
tests["power x**6 (entier)"]     = (lambda a: a ** 6,                      x_pos, lambda x: mpmath.mpf(x) ** 6)
tests["power x**(-0.8)"]         = (lambda a: a ** (-0.8),                 x_pos, lambda x: mpmath.mpf(x) ** mpmath.mpf(-0.8))
tests["power (-x)**6 == x**6 ?"] = (lambda a: (-a) ** 6,                   x_pos, lambda x: mpmath.mpf(x) ** 6)
tests["sqrt"]                    = (np.sqrt,                                x_pos, mpmath.sqrt)
tests["exp"]                     = (np.exp,      rng.uniform(-20, 20, N),          mpmath.exp)
tests["log"]                     = (np.log,                                 x_pos, mpmath.log)
tests["log2"]                    = (np.log2,                                x_pos, lambda x: mpmath.log(x, 2))
tests["log10"]                   = (np.log10,                               x_pos, mpmath.log10)
tests["sin"]                     = (np.sin,      rng.uniform(-50, 50, N),          mpmath.sin)
tests["cos"]                     = (np.cos,      rng.uniform(-50, 50, N),          mpmath.cos)
tests["tan"]                     = (np.tan,      rng.uniform(-1.5, 1.5, N),        mpmath.tan)
tests["arctan"]                  = (np.arctan,   rng.uniform(-50, 50, N),          mpmath.atan)
tests["tanh"]                    = (np.tanh,     rng.uniform(-5, 5, N),            mpmath.tanh)
tests["expm1"]                   = (np.expm1,    rng.uniform(-2, 2, N),            mpmath.expm1)
tests["log1p"]                   = (np.log1p,    rng.uniform(-0.5, 5, N),          lambda x: mpmath.log1p(x))
tests["cbrt"]                    = (np.cbrt,                                x_pos, mpmath.cbrt)
tests["arctan2(y,1.7)"]          = (lambda a: np.arctan2(a, 1.7), rng.uniform(-5, 5, N), lambda y: mpmath.atan2(y, 1.7))
print("variable NPY_DISABLE_CPU_FEATURES = %r" % os.environ.get("NPY_DISABLE_CPU_FEATURES", ""))
print("%-26s %8s %8s %8s  %s" % ("ufunc (tableau)", "non-CR", "sur N", "p.cent", "biais (nb -1ulp / +1ulp / autres)"))
for nom, (fn, xs, ref) in tests.items():
    ys = np.asarray(fn(xs), dtype=float)
    ncr = 0; moins = plus = autres = 0
    for x, y in zip(xs.tolist(), ys.tolist()):
        c = to_double_cr(ref(x))
        if c != y:
            ncr += 1
            d = (y - c) / math.ulp(c) if c != 0 else float("nan")
            if d == -1: moins += 1
            elif d == 1: plus += 1
            else: autres += 1
    print("%-26s %8d %8d %8.2f  %d / %d / %d" % (nom, ncr, N, 100.0 * ncr / N, moins, plus, autres))
# le meme x ** 6 par le pow scalaire de la libm (Python) : reference de comparaison
ncr = sum(1 for x in x_pos.tolist() if to_double_cr(mpmath.mpf(x) ** 6) != x ** 6)
print("%-26s %8d %8d %8.2f  (pow de la libm par Python, meme entrees)" % ("python x**6 (libm)", ncr, N, 100.0 * ncr / N))
ncr = sum(1 for x in x_pos.tolist() if to_double_cr(mpmath.log(x)) != math.log(x))
print("%-26s %8d %8d %8.2f  (log de la libm par Python, meme entrees)" % ("math.log (libm)", ncr, N, 100.0 * ncr / N))
