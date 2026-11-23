# controle_pole_court_machine1_v1.py -- machine 1, 2026-11-22
# CONTROLE INDEPENDANT de l'epreuve "pole court" (lot 2d69195af996cc0f de machine 2), par un code NEUF :
# les elements de x^5 sont reconstruits ici de zero (puissances de matrices de position), SANS mon module
# de la 21h (forme_energie_fixee_machine1_v1.py), que machine 2 a importe pour batir ses boites. Rien du
# lot de machine 2 n'est execute ni importe ; ses JSON ne sont lus qu'a la partie 3, pour comparer.
# Modele : H = -n1 + w2 n2 + (g / 5) x^5, x = (q1 + q2) / sqrt(w2^2 - 1), q_i = (a_i + a_i^+) / sqrt(2 w_i),
# w1 = 1. Echelle 2:1 : sites (2 m, m). Hors chaine, classe 3, aucun verdict.
# Parties :
#   1  (une dimension) sauts de l'echelle par mes elements neufs, contre la forme close de tau_m
#   2  (une dimension) chaine du PREMIER ordre coupee au site m_c, absorbeur court : Gamma / g
#   3  (deux dimensions) les huit boites de l'epreuve, memes points sacrifies, memes douze absorbeurs :
#      rejeu, puis comparaison a ses JSON. Aucune autre boite, aucun autre point.
# Usage : python3 -I controle_pole_court_machine1_v1.py 12
#         python3 -I controle_pole_court_machine1_v1.py 3 <indice de boite 0 a 3> <g> <dossier de sortie> <dossier de ses JSON>
import sys, math, json, os, time
import numpy as np

W2 = 2.0
P = 5

def tau_close(m):
    return (11.0 * m + 9.0) * (m + 1.0) * math.sqrt(2.0 * m + 1.0) / (36.0 * math.sqrt(6.0))

def puissances_q(nmax, w):
    # elements exacts de q^k, k = 0 a P, entre etats de Fock 0..nmax : matrice de taille nmax + 1 + P,
    # restreinte ensuite (aucun etat intermediaire ne depasse la taille tant que k <= P)
    n = nmax + 1 + P
    a = np.zeros((n, n))
    for i in range(1, n):
        a[i - 1, i] = math.sqrt(i)
    q = (a + a.T) / math.sqrt(2.0 * w)
    out, cur = [np.eye(n)], np.eye(n)
    for k in range(1, P + 1):
        cur = cur @ q
        out.append(cur.copy())
    return [m[:nmax + 1, :nmax + 1] for m in out]

def element_x5_sur_5(q1p, q2p, a2, b2, a1, b1):
    # < a2, b2 | x^5 / 5 | a1, b1 >
    s = 0.0
    for k in range(P + 1):
        s += math.comb(P, k) * q1p[k][a2, a1] * q2p[P - k][b2, b1]
    return s / (W2 * W2 - 1.0) ** (P / 2.0) / P

def pole(A, i0):
    # A symetrique complexe ; poids biorthogonal du niveau j au site i0 : r_j(i0)^2 / (r_j^T r_j)
    val, vec = np.linalg.eig(A)
    nr = np.einsum("ij,ij->j", vec, vec)
    w = vec[i0, :] ** 2 / nr
    j = int(np.argmax(np.abs(w)))
    res = float(np.linalg.norm(A @ vec[:, j] - val[j] * vec[:, j]) / np.linalg.norm(vec[:, j]))
    return val[j], w[j], complex(np.sum(w)), res

def W_abs(a, m, m0, mc):
    return a * tau_close(m) * ((m - m0) / float(mc - m0)) ** 2 if m0 < m <= mc else 0.0

def partie_1():
    print("=== PARTIE 1 (une dimension) : sauts de l'echelle par mes elements neufs, contre la forme close")
    mmax = 30
    q1p, q2p = puissances_q(2 * mmax + 2, 1.0), puissances_q(mmax + 1, W2)
    pire = 0.0
    for m in range(mmax + 1):
        t = element_x5_sur_5(q1p, q2p, 2 * m + 2, m + 1, 2 * m, m)
        pire = max(pire, abs(t / tau_close(m) - 1.0))
        if m <= 4:
            print("   tau_%d : elements neufs %.12f ; forme close %.12f" % (m, t, tau_close(m)))
    print("ecart relatif maximal, m = 0 a %d : %.1e" % (mmax, pire))
    # l'echelle ne se couple pas a elle-meme autrement qu'au premier voisin, a w2 = 2 ?
    autres = 0.0
    for m in range(mmax):
        for dm in (2, 3):
            if m + dm <= mmax:
                autres = max(autres, abs(element_x5_sur_5(q1p, q2p, 2 * (m + dm), m + dm, 2 * m, m)))
    print("plus grand element direct entre sites d'echelle a deux ou trois crans : %.1e" % autres)

def partie_2():
    print()
    print("=== PARTIE 2 (une dimension) : chaine du PREMIER ordre coupee au site m_c, absorbeur court")
    print("    diagonale nulle (w2 = 2), sauts tau_m, terme -i W_m ; Gamma / g ; colonnes m0 = 2, 3, 4")
    out = {}
    for a in (2.0, 4.0, 0.5, 1.0):
        for mc in (10, 11, 12, 13):
            lig = []
            for m0 in (2, 3, 4):
                A = np.zeros((mc + 1, mc + 1), dtype=complex)
                for m in range(mc):
                    A[m, m + 1] = A[m + 1, m] = tau_close(m)
                for m in range(mc + 1):
                    A[m, m] = -1j * W_abs(a, m, m0, mc)
                E, w, somme, res = pole(A, 0)
                assert abs(somme - 1.0) < 1e-9 and res < 1e-9
                out[(a, mc, m0)] = -2.0 * E.imag
                lig.append(-2.0 * E.imag)
            print("   a = %.1f m_c = %d : %s" % (a, mc, " ".join("%.5f" % v for v in lig)))
    fort = [v for (a, mc, m0), v in out.items() if a in (2.0, 4.0)]
    print("absorbeur fort (24 cas, premier ordre) : de %.5f a %.5f ; moyenne %.5f" % (min(fort), max(fort), sum(fort) / len(fort)))
    json.dump({"%.1f|%d|%d" % k: v for k, v in out.items()}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "journaux", "chaine_premier_ordre_pole_court.json"), "w"), indent=1, sort_keys=True)

def partie_3(ib, gs, sortie, dossier_m2):
    BOITES = ((34, 24, 10), (34, 24, 11), (40, 28, 12), (40, 28, 13))
    TAILLES = (868, 869, 1181, 1182)
    n1max, n2max, mc = BOITES[ib]
    g = float(gs)
    t0 = time.time()
    q1p, q2p = puissances_q(n1max, 1.0), puissances_q(n2max, W2)
    # V = x^5 / 5 sur le produit (n1, n2), par produits de Kronecker
    d1, d2 = n1max + 1, n2max + 1
    V = np.zeros((d1 * d2, d1 * d2))
    for k in range(P + 1):
        V += math.comb(P, k) * np.kron(q1p[k], q2p[P - k])
    V /= (W2 * W2 - 1.0) ** (P / 2.0) * P
    garde, idx = [], {}
    for n1 in range(d1):
        for n2 in range(d2):
            if n1 == 2 * n2 and n2 > mc:
                continue  # sites d'echelle au-dela de la coupe : retires
            idx[(n1, n2)] = len(garde)
            garde.append(n1 * d2 + n2)
    n = len(garde)
    assert n == TAILLES[ib], (n, TAILLES[ib])
    garde = np.array(garde)
    H = g * V[np.ix_(garde, garde)]
    for (n1, n2), i in idx.items():
        H[i, i] += -1.0 * n1 + W2 * n2
    assert np.max(np.abs(H - H.T)) < 1e-12
    lad = [idx[(2 * m, m)] for m in range(mc + 1)]
    e0 = idx[(0, 0)]
    print("=== PARTIE 3 (deux dimensions) : boite %d, (%d, %d, %d), %d etats, g = %.0e" % (ib, n1max, n2max, mc, n, g), flush=True)
    ref = json.load(open(os.path.join(dossier_m2, "pole_court_b%d_g%s.json" % (ib, gs))))
    assert ref["taille"] == n and ref["m_coupe"] == mc and ref["g"] == g
    refc = {(c["a"], c["m0"]): c for c in ref["cas"]}
    cas, pire_g, pire_r, pire_p = [], 0.0, 0.0, 0.0
    for a in (0.5, 1.0, 2.0, 4.0):
        for m0 in (2, 3, 4):
            A = H.astype(complex)
            for m in range(m0 + 1, mc + 1):
                A[lad[m], lad[m]] += -1j * g * W_abs(a, m, m0, mc)
            E, w, somme, res = pole(A, e0)
            gam, re, pw = -2.0 * E.imag / g, E.real / g, abs(w)
            r = refc[(a, m0)]
            dg, dr, dp = abs(gam - r["gamma_sur_g"]), abs(re - r["re_sur_g"]), abs(pw - r["poids_abs"])
            pire_g, pire_r, pire_p = max(pire_g, dg), max(pire_r, dr), max(pire_p, dp)
            cas.append({"a": a, "m0": m0, "gamma_sur_g": gam, "re_sur_g": re, "poids_abs": pw, "somme_moins_1": abs(somme - 1.0), "residu": res, "ecart_gamma_a_m2": dg, "ecart_re_a_m2": dr, "ecart_poids_a_m2": dp})
            print("   a = %.1f m0 = %d : Gamma / g = %.9f ; Re E / g = %+.9f ; poids %.7f ; |somme - 1| %.1e ; residu %.1e ; ecarts a machine 2 : %.1e %.1e %.1e (%.0f s)" % (a, m0, gam, re, pw, abs(somme - 1.0), res, dg, dr, dp, time.time() - t0), flush=True)
    print("boite %d g = %s : 12 cas ; plus grand ecart a machine 2 : Gamma / g %.1e ; Re E / g %.1e ; poids %.1e" % (ib, gs, pire_g, pire_r, pire_p), flush=True)
    os.makedirs(sortie, exist_ok=True)
    json.dump({"boite": ib, "taille": n, "m_coupe": mc, "g": g, "cas": cas, "pire_ecart_gamma": pire_g, "pire_ecart_re": pire_r, "pire_ecart_poids": pire_p}, open(os.path.join(sortie, "rejeu_m1_b%d_g%s.json" % (ib, gs)), "w"), indent=1, sort_keys=True)

if sys.argv[1] == "12":
    partie_1()
    partie_2()
elif sys.argv[1] == "3":
    partie_3(int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5])
