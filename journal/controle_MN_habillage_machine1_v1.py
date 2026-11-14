# Controle hors chaine (machine 1, 13/11/2026) : la survie P(t) de |0,0> dans le modele
# H = n1 - sqrt(2) n2 + (lam/2) x^2 y^2 (Maiezza-Nesti 2610.10040 ; meme forme que GSTZ eq. 56)
# est-elle, a petit couplage, l'habillage perturbatif du premier ordre ?
import numpy as np, sys
w1, w2 = 1.0, np.sqrt(2.0)
def x2(N, w):
    a = np.diag(np.sqrt(np.arange(1, N)), 1)
    x = (a + a.T) / np.sqrt(2.0 * w)
    return x @ x
def survie(lam, N, ts):
    X2, Y2 = x2(N + 2, w1)[:N, :N], x2(N + 2, w2)[:N, :N]   # x^2 exact sur le bloc N (pas d'effet de bord)
    n = np.arange(N)
    H0 = (w1 * n)[:, None] - (w2 * n)[None, :]
    H = np.diag(H0.ravel()) + 0.5 * lam * np.kron(X2, Y2)
    E, V = np.linalg.eigh(H)
    c2 = V[0, :] ** 2                                         # |<v_i|0,0>|^2
    return np.abs((c2[None, :] * np.exp(-1j * np.outer(ts, E))).sum(axis=1)) ** 2
# premier ordre : etats admis depuis |0,0> par x^2 y^2
el = {"(2,0)": (0.5 * (np.sqrt(2) / (2 * w1)) * (1 / (2 * w2)), 2 * w1),
      "(0,2)": (0.5 * (1 / (2 * w1)) * (np.sqrt(2) / (2 * w2)), -2 * w2),
      "(2,2)": (0.5 * (np.sqrt(2) / (2 * w1)) * (np.sqrt(2) / (2 * w2)), 2 * w1 - 2 * w2)}
print("premier ordre : etat, V/lam, DeltaE, |c|^2/lam^2, periode")
for k, (v, dE) in el.items():
    print("  %s  %.5f  %+.5f  %.5f  %.3f" % (k, v, dE, (v / dE) ** 2, 2 * np.pi / abs(dE)))
var = sum(v * v for v, _ in el.values())
print("variance de V dans |0,0> = %.5f lam^2 (= 1/16 : %s)" % (var, abs(var - 1 / 16) < 1e-12))
eps = sum((v / dE) ** 2 for v, dE in el.values())
print("somme |c|^2 = %.5f lam^2 ; creux attendu 1 - P ~ 2*eps + 2*|c22|^2 = %.4f lam^2 (+/- %.4f)" % (
    eps, 2 * eps + 2 * (el["(2,2)"][0] / el["(2,2)"][1]) ** 2,
    2 * ((el["(2,0)"][0] / el["(2,0)"][1]) ** 2 + (el["(0,2)"][0] / el["(0,2)"][1]) ** 2)))
ts = np.linspace(0.0, 120.0, 12001)
print()
print("lam   N   (1-P)/(lam^2 t^2) a t=0.05   min P sur [0,120]   (1-minP)/lam^2   borne MN 1-0.2l^2-2.1l^3   periode dominante")
for lam in (0.02, 0.05, 0.10, 0.15):
    for N in (30, 40):
        P = survie(lam, N, ts)
        i = np.searchsorted(ts, 0.05)
        ct = (1 - P[i]) / (lam ** 2 * ts[i] ** 2)
        m = P.min()
        f = np.fft.rfftfreq(len(ts), ts[1] - ts[0])
        S = np.abs(np.fft.rfft(P - P.mean()))
        per = 1.0 / f[1:][np.argmax(S[1:])]
        print("%.2f  %d   %.5f                    %.6f           %.4f            %.6f                 %.2f" % (
            lam, N, ct, m, (1 - m) / lam ** 2, 1 - 0.2 * lam ** 2 - 2.1 * lam ** 3, per))
