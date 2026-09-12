# -*- coding: ascii -*-
# Meme test que mesure_ufuncs_cr (power x**6, x**(-0.8), exp) sous une autre version de numpy, meme OS, meme CPU.
import os, sys, math, io, contextlib, re, numpy as np
from fractions import Fraction
import mpmath
mpmath.mp.prec = 200
def cr(v):
    v = mpmath.mpf(v)
    if v == 0: return 0.0
    s = -1 if v < 0 else 1; v = abs(v)
    return s * float(Fraction(int(v.man)) * (Fraction(2) ** int(v.exp)))
buf = io.StringIO()
with contextlib.redirect_stdout(buf): np.show_runtime()
m = re.search(r"'found': \[(.*?)\]", buf.getvalue(), re.S)
print("numpy %s ; python %s ; NPY_DISABLE_CPU_FEATURES=%r ; dispatch found : %s" % (np.__version__, sys.version.split()[0], os.environ.get("NPY_DISABLE_CPU_FEATURES", ""), (m.group(1) if m else "?").replace("\n", " ")))
rng = np.random.default_rng(20260912); N = 20000
x = np.exp(rng.uniform(-3, 8, N))
for nom, fn, ref in (("power x**6", lambda a: a ** 6, lambda t: mpmath.mpf(t) ** 6),
                     ("power x**(-0.8)", lambda a: a ** (-0.8), lambda t: mpmath.mpf(t) ** mpmath.mpf(-0.8)),
                     ("exp", np.exp, mpmath.exp)):
    xs = x if nom != "exp" else rng.uniform(-20, 20, N)
    ys = np.asarray(fn(xs), float)
    ncr = sum(1 for a, b in zip(xs.tolist(), ys.tolist()) if cr(ref(a)) != b)
    npy = sum(1 for a, b in zip(xs.tolist(), ys.tolist()) if (a ** 6 if nom == "power x**6" else (a ** (-0.8) if nom.endswith("0.8)") else math.exp(a))) != b)
    print("  %-18s non-CR %5d / %d = %.2f pour cent ; differe du pow/exp de Python (glibc) sur %d" % (nom, ncr, N, 100.0 * ncr / N, npy))
