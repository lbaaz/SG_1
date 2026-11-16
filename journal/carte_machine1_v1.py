# -*- coding: ascii -*-
"""CARTE DES CORRECTIONS A LA LOI D'ECHELLE -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. Aucun calcul 2D.
Question : dans le plan (longueur de barriere m_bord, desaccord au bout e = m_bord |delta|), de combien la chaine
complete (ordres 2 et 3, blocs deposes, appeles tels quels pour leurs tables) s'ecarte-t-elle de la loi d'echelle
|delta| Phi(kappa) ?   r2 = ln(Gamma_2 / (|delta| Phi)),   r3 = ln(Gamma_3 / (|delta| Phi)).
Les w2 parcourus ne sont pas des points de la campagne ; aucune largeur 2D n'y est lue ni predite.
Largeur des chaines d'ordre 2 et 3 : la diagonalisation dense du bloc (flux) tant que Gamma / |delta| > 1e-15 ;
en dessous, quotient de Rayleigh complexe en precision arbitraire sur la MEME matrice (meme etat, choisi en double).
Usage : python3 -I carte_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <phi_echelle.py> <sortie.json> [rapide]"""
import sys, math, json, time, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, PHI, SORTIE = sys.argv[1:6]
RAPIDE = len(sys.argv) > 6
spec = importlib.util.spec_from_file_location("phi_echelle", PHI); PH = importlib.util.module_from_spec(spec); spec.loader.exec_module(PH)
M = PH.charger(MOTEUR)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    c = (k, l, n1, n2, w2)
    if c not in _cache:
        _cache[c] = _brut(p, k, l, n1, n2, w2)
    return _cache[c]
M.X_saut_reel = _X
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
EF = 0.0625
SEUIL_FLUX = 1e-15

def matrice(tb, t3, ef, ordre, recul=0):
    """La matrice que construisent gamma_chaine_ordre2 (ordre = 2) et gamma_chaine_ordre3 (ordre = 3) des blocs deposes."""
    d, Mh, m_min = tb["d"], tb["Mh"], tb["m_min"]
    eta_c = abs(d) * ef
    cap = tb["m2_bord"] + tb["b_M"] // 2 + recul
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > cap:
            Wd[i] = eta_c * (m - cap) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0)
            H[i, i + 1] = x; H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
        if ordre == 3 and m + 3 <= Mh:
            H[i, i + 3] = t3["W3"][m]; H[i + 3, i] = t3["W3"][m]
        if ordre == 3 and m + 5 <= Mh:
            H[i, i + 5] = t3["W5"][m]; H[i + 5, i] = t3["W5"][m]
    return H, Wd, -m_min

def resoudre_bande(lignes, second, b):
    """Elimination de Gauss a pivot partiel sur une matrice bande (lignes : dictionnaires colonne -> valeur)."""
    n = len(lignes); L = [dict(r) for r in lignes]; x = list(second)
    for k in range(n):
        p = max(range(k, min(n, k + b + 1)), key=lambda i: abs(L[i].get(k, 0)))
        if p != k:
            L[k], L[p] = L[p], L[k]; x[k], x[p] = x[p], x[k]
        piv = L[k][k]
        for i in range(k + 1, min(n, k + b + 1)):
            f = L[i].get(k, 0)
            if f != 0:
                f = f / piv
                for c, v in L[k].items():
                    if c > k:
                        L[i][c] = L[i].get(c, 0) - f * v
                del L[i][k]; x[i] -= f * x[k]
    for k in range(n - 1, -1, -1):
        s = x[k]
        for c, v in L[k].items():
            if c > k:
                s -= v * x[c]
        x[k] = s / L[k][k]
    return x

def largeur_mp(H, psi0, mu0, chiffres, b=5):
    """Valeur propre complexe de H (symetrique complexe) voisine de mu0, par quotient de Rayleigh bilineaire."""
    mp.mp.dps = chiffres
    n = H.shape[0]
    lignes = [{j: mp.mpc(H[i, j]) for j in range(max(0, i - b), min(n, i + b + 1)) if (H[i, j] != 0 or j == i)} for i in range(n)]
    psi = [mp.mpc(z) for z in psi0]; mu = mp.mpc(mu0.real, 0)
    def quotient(v):
        num = mp.mpc(0); den = mp.mpc(0)
        for i in range(n):
            s = mp.mpc(0)
            for j, a in lignes[i].items():
                s += a * v[j]
            num += v[i] * s; den += v[i] * v[i]
        return num / den
    mu = quotient(psi)
    for it in range(12):
        dec = [dict(r) for r in lignes]
        for i in range(n):
            dec[i][i] = dec[i][i] - mu
        y = resoudre_bande(dec, psi, b)
        nrm = max(abs(z) for z in y)
        psi = [z / nrm for z in y]
        nouveau = quotient(psi)
        ecart = abs(nouveau - mu); mu = nouveau
        if ecart < mp.mpf(10) ** (-(chiffres - 12)):
            break
    else:
        raise RuntimeError("largeur_mp : pas de convergence")
    return float(-2 * mu.imag), it + 1

def largeur(H, Wd, i0, d_abs, ln_phi):
    val, vec = np.linalg.eig(H)
    recs = np.abs(vec[i0, :]) ** 2
    nu = np.lexsort((val.real, -recs))[0]
    psi2 = np.abs(vec[:, nu]) ** 2
    flux = float(2.0 * (Wd @ psi2) / psi2.sum())
    if flux / d_abs > SEUIL_FLUX:
        return flux, "flux", float(recs[nu])
    chiffres = int(-ln_phi / math.log(10.0)) + 60
    G, it = largeur_mp(H, vec[:, nu], val[nu], chiffres)
    return G, "mp%d" % it, float(recs[nu])

def kappa_pour_m_bord(n1, n2, m_cible):
    """Milieu geometrique de l'intervalle de kappa dont la barriere (regle du moteur, a la limite) finit a m_cible."""
    def mb(k):
        rg = PH.reglage(k, n1, n2)
        return 0 if rg is None else rg["m_bord"]
    lo, hi = 1e-7, 2.0
    # plus grand kappa avec m_bord >= m_cible
    a, b = lo, hi
    for _ in range(80):
        c = math.sqrt(a * b)
        if mb(c) >= m_cible: a = c
        else: b = c
    k_haut = a
    a, b = lo, hi
    for _ in range(80):                 # plus petit kappa avec m_bord <= m_cible
        c = math.sqrt(a * b)
        if mb(c) <= m_cible: b = c
        else: a = c
    k_bas = b
    return math.sqrt(k_bas * k_haut), k_bas, k_haut

def point(n1, n2, kappa, delta):
    w2 = F(2) + F(delta).limit_denominator(10 ** 7); d = float(w2) - 2.0
    tau0 = M.X_saut_reel(M.P, M.CANAL[0], M.CANAL[1], float(n1), float(n2), w2) / M.P
    g = kappa * abs(d) / tau0
    f = PH.phi_fc(kappa, n1, n2)
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    if not sites or f is None:
        return {"n1": n1, "n2": n2, "kappa": kappa, "delta": d, "g": g, "vide": True, "motif": "barriere vide"}
    if sites[-1][0] > 3 * f["m_bord"] + 8:
        # avec Sigma2, la regle du moteur ne trouve plus de fin a la barriere : hors de tout domaine, non calcule
        return {"n1": n1, "n2": n2, "kappa": kappa, "delta": d, "g": g, "vide": True, "motif": "barriere du moteur sans fin (m_bord %d contre %d a la limite)" % (sites[-1][0], f["m_bord"])}
    tb = tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=4); t3 = tables_ordre3(float(n1), float(n2), w2, g, tb)
    mbd = tb["m2_bord"]; e_bord = abs(mbd * d + tb["S"][mbd] - tb["S"][0])
    out = {"n1": n1, "n2": n2, "kappa": kappa, "delta": d, "g": g, "vide": False, "m_bord": mbd, "m_bord_limite": f["m_bord"], "e_bord": e_bord,
           "ln_Phi": f["ln_Phi"], "n_sites": tb["Mh"] - tb["m_min"] + 1}
    H2, Wd, i0 = matrice(tb, t3, EF, 2); G2, voie2, rec2 = largeur(H2, Wd, i0, abs(d), f["ln_Phi"])
    H3, Wd, i0 = matrice(tb, t3, EF, 3); G3, voie3, rec3 = largeur(H3, Wd, i0, abs(d), f["ln_Phi"])
    var = []
    for (ef, recul) in ((2 * EF, 0), (EF / 2, 0), (EF, 4)):
        Hv, Wv, iv = matrice(tb, t3, ef, 3, recul); var.append(largeur(Hv, Wv, iv, abs(d), f["ln_Phi"])[0])
    ok = G3 > 0 and all(x > 0 for x in var)
    out.update({"G2": G2, "G3": G3, "voie2": voie2, "voie3": voie3, "recouvrement3": rec3,
                "r2": math.log(G2 / abs(d)) - f["ln_Phi"] if G2 > 0 else None, "r3": math.log(G3 / abs(d)) - f["ln_Phi"] if G3 > 0 else None,
                "stab3": max(abs(math.log(x / G3)) for x in var) if ok else None})
    return out

if __name__ == "__main__":
    out = {"reglage": {"ef": EF, "M_facteur": 4, "seuil_flux": SEUIL_FLUX}, "controles": {}, "points": []}
    # --- controle 1 : ma matrice redonne les largeurs des blocs deposes ---
    w2 = F(387, 200); g = 0.0016696740862707378; n1, n2 = 9.0, 3.0            # N1 rang 0 du delta 100
    sites = M.barriere(n1, n2, w2, g, True); tb = tables_ordre2(n1, n2, w2, g, sites, M_facteur=4); t3 = tables_ordre3(n1, n2, w2, g, tb)
    ref2 = gamma_chaine_ordre2(tb, EF)["Gamma_flux"]; ref3 = gamma_chaine_ordre3(tb, t3, EF)["Gamma_flux"]
    H2, Wd, i0 = matrice(tb, t3, EF, 2); H3, Wd3, i03 = matrice(tb, t3, EF, 3)
    a2 = largeur(H2, Wd, i0, 0.065, -23.0)[0]; a3 = largeur(H3, Wd3, i03, 0.065, -23.0)[0]
    out["controles"]["matrice_contre_blocs"] = [abs(a2 / ref2 - 1.0), abs(a3 / ref3 - 1.0)]
    print("controle 1 : ma matrice contre les blocs deposes (N1 rang 0) : ecarts relatifs %.1e (ordre 2), %.1e (ordre 3) ; G3 = %.16e (feuille du run : 1.1371927892733262e-10)" % (
        out["controles"]["matrice_contre_blocs"][0], out["controles"]["matrice_contre_blocs"][1], a3))
    # --- controle 2 : la voie de precision arbitraire redonne le flux la ou les deux existent ---
    val, vec = np.linalg.eig(H3); recs = np.abs(vec[i03, :]) ** 2; nu = np.lexsort((val.real, -recs))[0]
    Gmp, it = largeur_mp(H3, vec[:, nu], val[nu], 60)
    out["controles"]["mp_contre_flux"] = abs(Gmp / ref3 - 1.0)
    print("controle 2 : precision arbitraire contre flux, meme matrice : ecart relatif %.1e (%d iterations)" % (out["controles"]["mp_contre_flux"], it))
    # --- la carte ---
    M_CIBLES = (4, 8, 16) if RAPIDE else (4, 6, 8, 12, 16, 24, 32, 48, 64)
    E_CIBLES = (0.3, 0.7) if RAPIDE else (0.075, 0.15, 0.3, 0.5, 0.7, 1.0)
    for (n1, n2) in ((0, 0), (6, 2)):
        print(); print("etiquette (%d, %d)" % (n1, n2))
        print("  m_cible  kappa       e_cible  delta       m_bord  e_bord   -ln Phi     r2         r3         stab3     voie")
        for mc in M_CIBLES:
            k, kb, kh = kappa_pour_m_bord(n1, n2, mc)
            for ec in E_CIBLES:
                for sg in (-1, 1):
                    t0 = time.time(); _cache.clear()
                    p = point(n1, n2, k, sg * ec / mc); p.update({"m_cible": mc, "e_cible": ec, "kappa_bas": kb, "kappa_haut": kh, "duree_s": round(time.time() - t0, 1)})
                    out["points"].append(p)
                    if p["vide"]:
                        print("  %4d    %.4e   %.3f   %+.5f   %s" % (mc, k, ec, p["delta"], p["motif"]), flush=True); continue
                    print("  %4d    %.4e   %.3f   %+.5f   %4d   %.3f   %9.3f   %s   %s   %s   %s  (%.0f s)" % (
                        mc, k, ec, p["delta"], p["m_bord"], p["e_bord"], -p["ln_Phi"],
                        ("%+.4f" % p["r2"]) if p["r2"] is not None else "   -   ", ("%+.4f" % p["r3"]) if p["r3"] is not None else "   -   ",
                        ("%.4f" % p["stab3"]) if p["stab3"] is not None else "  -   ", p["voie3"], p["duree_s"]), flush=True)
            json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
