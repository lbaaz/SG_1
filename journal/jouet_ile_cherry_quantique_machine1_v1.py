# Jouet hors chaine (classe 3) : ile de la forme normale resonante desaccordee, version quantique.
# H = nu*I + mu*I^(p/2)*cos(phi), I = hbar*k  ->  matrice de Jacobi semi-infinie
#   diag a_k = nu*hbar*k ; hors-diag b_k = (mu/2)*(hbar*(k+1))^(p/2)
# Prediction WKB (derivee a la main) : Gamma ~ exp(-2*c_p*I1/hbar), I1=(nu/mu)^(2/(p-2)), c_3=1, c_4=pi/2.
import sys, numpy as np

def largeur(hbar, p, nu, mu, I0, Imax, eta, forme):
    N = int(round(Imax / hbar))
    k = np.arange(N)
    a = (nu * hbar * k).astype(complex)
    b = 0.5 * mu * (hbar * (k[:-1] + 1.0)) ** (p / 2.0)
    x = np.clip((hbar * k - I0) / (Imax - I0), 0.0, None)
    a = a - 1j * eta * x ** forme
    H = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
    w, v = np.linalg.eig(H)
    poids = np.abs(v[0, :]) ** 2 / np.sum(np.abs(v) ** 2, axis=0)
    j = int(np.argmax(poids))
    return -2.0 * w[j].imag, w[j].real, poids[j]

def palier(hbar, p, nu, mu, I0, Imax, forme):
    etas = [2.0 ** e for e in range(-2, 9)]
    g = np.array([largeur(hbar, p, nu, mu, I0, Imax, e, forme)[0] for e in etas])
    best = None
    for i in range(len(g) - 4):
        f = g[i:i + 5]
        if np.all(f > 0):
            r = f.max() / f.min()
            if best is None or r < best[0]:
                best = (r, float(np.exp(np.mean(np.log(f)))), etas[i])
    return best

for p, cp in ((3, 1.0), (4, np.pi / 2)):
    nu = mu = 1.0
    I1 = (nu / mu) ** (2.0 / (p - 2))
    print(f"--- p = {p} ; I1 = {I1:.3f} ; pente WKB attendue de ln Gamma en 1/hbar : {-2*cp*I1:.4f}")
    xs, ys = [], []
    for hbar in (0.20, 0.16, 0.13, 0.11, 0.095, 0.085):
        lignes = []
        for (I0, Imax, forme) in ((4.0, 12.0, 2), (5.0, 14.0, 2), (4.0, 12.0, 3), (3.0, 10.0, 4)):
            lignes.append(palier(hbar, p, nu, mu, I0, Imax, forme))
        gs = np.array([l[1] for l in lignes]); et = max(l[0] for l in lignes)
        xs.append(1 / hbar); ys.append(np.log(np.exp(np.mean(np.log(gs)))))
        print(f"hbar={hbar:.3f}  Gamma_pl (4 absorbeurs) = " + " ".join(f"{x:.4e}" for x in gs)
              + f"  max/min entre absorbeurs = {gs.max()/gs.min():.4f}  pire etalement interne = {et:.4f}")
    xs, ys = np.array(xs), np.array(ys)
    for (i, j) in ((0, 5), (2, 5), (3, 5)):
        print(f"pente entre hbar={1/xs[i]:.3f} et {1/xs[j]:.3f} : {(ys[j]-ys[i])/(xs[j]-xs[i]):.4f}")

# Cercle limite : somme partielle de |u_k|^2 pour les deux solutions de la recurrence a E fixe.
print("--- cercle limite ? sommes partielles de |u_k|^2 (E = 0.3, nu = mu = 1, hbar = 0.1)")
for p in (2, 3, 4):
    hbar = 0.1; E = 0.3
    K = 10 ** 6
    k = np.arange(K + 1)
    b = 0.5 * (hbar * (k + 1.0)) ** (p / 2.0)
    a = hbar * k
    for depart in ((1.0, 0.0), (0.0, 1.0)):
        u0, u1 = depart; s = u0 * u0 + u1 * u1; sorties = []
        for n in range(1, K):
            u2 = ((E - a[n]) * u1 - b[n - 1] * u0) / b[n]
            u0, u1 = u1, u2; s += u2 * u2
            if n + 1 in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6 - 1):
                sorties.append(s)
        print(f"p={p} depart={depart} : " + "  ".join(f"{x:.5f}" for x in sorties))
