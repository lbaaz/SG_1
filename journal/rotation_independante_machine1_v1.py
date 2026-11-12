# -*- coding: ascii -*-
# ROTATION COMPLEXE INDEPENDANTE -- machine 1, v1. Ecrite depuis la formule du
# gel E-B v2 (5.1) AVANT de lire le script de reference de m2. N'emprunte au
# moteur que lambdas() et, pour la garde, H_2D. Sert a certifier la reference.
import sys, math, cmath, time, importlib.util
from fractions import Fraction
import numpy as np


def moteur(chemin):
    spec = importlib.util.spec_from_file_location("moteur_m17", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def abaisseur(n):
    return np.diag(np.sqrt(np.arange(1.0, n)), 1)


def h_rot(N, w1, w2, g, theta, l1, l2, phase_x=5):
    ne = N + 5                                # x^5 exact dans le bloc N x N
    a = abaisseur(ne)
    q = a + a.T
    ie = np.eye(ne)
    x = l1 * np.kron(q, ie) + l2 * np.kron(ie, q)
    x2 = x @ x
    x5 = x2 @ x2 @ x
    idx = np.array([i * ne + j for i in range(N) for j in range(N)])
    x5 = x5[np.ix_(idx, idx)]
    b = abaisseur(N)
    n = np.diag(np.arange(float(N)))
    s2 = b @ b + b.T @ b.T
    i1 = np.eye(N)
    c, s = math.cos(2.0 * theta), math.sin(2.0 * theta)
    h = (w1 * (c * np.kron(n, i1) + 0.5j * s * np.kron(s2, i1))
         + w2 * (c * np.kron(i1, n) + 0.5j * s * np.kron(i1, s2))
         + 0.5 * (w1 + w2) * (c - 1.0) * np.eye(N * N)
         + cmath.exp(1j * phase_x * theta) * (g / 5.0) * x5)
    return h


def largeur(h):
    vals, vecs = np.linalg.eig(h)
    r = np.abs(vecs[0, :])
    j = int(np.argmax(r))
    return float(-2.0 * vals[j].imag), float(vals[j].real), float(r[j] * r[j])


if __name__ == "__main__":
    M = moteur(sys.argv[1])
    w2f = Fraction(39, 20)
    _, l1, l2 = M.lambdas(w2f)
    w1, w2 = 1.0, float(w2f)
    print("lambdas du moteur : %.15f %.15f ; 1/sqrt(2 Delta w_i) : %.15f %.15f" % (
        l1, l2, 1 / math.sqrt(2 * (w2 * w2 - 1) * w1), 1 / math.sqrt(2 * (w2 * w2 - 1) * w2)))
    # (a) garde : H(theta = 0) == H_2D du moteur, jumeau H+
    for N in (14, 22):
        ref = M.H_2D(N, w2f, 0.10, +1, "x5", 0.0, None)[0]
        h = h_rot(N, w1, w2, 0.10, 0.0, l1, l2)
        print("(a) N = %d : max|H_rot(0) - H_2D| = %.3e ; max|H| = %.2f ; max|H - H^T| a theta = 0.2 : %.2e" % (
            N, float(np.max(np.abs(h - ref))), float(np.max(np.abs(ref))),
            float(np.max(np.abs(h_rot(N, w1, w2, 0.10, 0.2, l1, l2) - h_rot(N, w1, w2, 0.10, 0.2, l1, l2).T)))))
    # (c) la phase fausse doit mordre, la bonne etre stationnaire (N = 30)
    for ph in (5, 4):
        G = [largeur(h_rot(30, w1, w2, 0.10, t, l1, l2, ph))[0] for t in (0.15, 0.20, 0.25)]
        print("(c) N = 30, phase e^{%d i theta} : Gamma = %s" % (ph, ["%.4e" % x for x in G]))
    # (b) points demandes : "j,N,theta" ...
    for spec in sys.argv[2:]:
        j, N, th = spec.split(",")
        g = 0.05 * 2.0 ** (int(j) / 8.0)
        t0 = time.time()
        G, e, r = largeur(h_rot(int(N), w1, w2, g, float(th), l1, l2))
        print("(b) j = %s g = %r N = %s theta = %s : Gamma = %.6e Re E = %.9e recouvrement %.4f (%.0f s)" % (
            j, g, N, th, G, e, r, time.time() - t0), flush=True)
