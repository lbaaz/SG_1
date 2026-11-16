# -*- coding: ascii -*-
"""FONCTION D'ECHELLE Phi(kappa ; n1, n2) -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. Aucun calcul 2D.

Limite delta -> 0 a kappa = t_0 / |delta| fixe de la chaine E-A de l'etat (n1, n2), canal (2, 1) de x^5 :
en unites de |delta|, la chaine du premier ordre devient
    H = s m  +  kappa (tau_m / tau_0) (saut m <-> m + 1),   s = signe de delta,
avec tau_m = X_{2,1}(n1 + 2 m, n2 + m ; w2 = 2) / P (element du moteur, appele tel quel, a w2 = 2 exactement).
Les deplacements Sigma2, le saut au second voisin et l'ordre 3 pesent delta, delta, delta^2 devant elle :
ils sont absents de la limite. Phi = Gamma / |delta| de l'etat de plus grand recouvrement avec le site 0.

Trois arithmetiques pour la meme quantite :
  phi_eig : diagonalisation dense, meme construction que le bloc d'ordre 3 depose (absorbeur, longueur, lecture) ;
  phi_fc  : fraction continue, partie imaginaire suivie en logarithme (aucune soustraction : tient a toute profondeur) ;
  phi_mp  : pole complexe exact de la meme fraction continue en precision arbitraire (controle).
Reglage de la chaine : celui du depot (ef = 0.0625, M_facteur = 4), regle de barriere du moteur.
Usage en module : charger(moteur) puis phi_eig / phi_fc / phi_mp. En script : controle des trois arithmetiques.
  python3 -I phi_echelle_machine1_v1.py <moteur> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np

M = None
EF = 0.0625
M_FACTEUR = 4
W2_LIMITE = F(2)


def charger(chemin_moteur):
    global M
    spec = importlib.util.spec_from_file_location("moteur", chemin_moteur)
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    assert M.P == 5 and tuple(M.CANAL) == (2, 1) and M.W1 == 1
    return M


_TAU = {}


def tau(n1, n2, m, w2=W2_LIMITE):
    """tau_m : saut m -> m + 1 divise par g, aux occupations (n1 + 2 m, n2 + m)."""
    cle = (n1, n2, m, w2)
    if cle not in _TAU:
        c0, c1 = M.CANAL
        a, b = n1 + c0 * m, n2 + c1 * m
        _TAU[cle] = 0.0 if (a < 0 or b < 0) else M.X_saut_reel(M.P, c0, c1, float(a), float(b), w2) / M.P
    return _TAU[cle]


def reglage(kappa, n1, n2, m_plafond=200000, m_facteur=M_FACTEUR, w2=W2_LIMITE):
    """Barriere (regle du moteur, en unites de |delta| : site m >= 1 dans la barriere si m > 2 kappa tau_m / tau_0),
    puis longueur et debut de l'absorbeur comme au depot."""
    t0 = tau(n1, n2, 0, w2)
    sites, neg = [], 0
    for m in range(1, m_plafond + 1):
        tm = kappa * tau(n1, n2, m, w2) / t0
        if m > 2.0 * tm:
            sites.append(m); neg = 0
        else:
            if sites:
                neg += 1
                if neg >= 3:
                    break
            elif m > 8 and 2.0 * tm > 4.0 * m:
                break
    if not sites:
        return None
    m_bord = sites[-1]
    b_M = max(8, m_bord)
    Mh = (m_bord + b_M) * m_facteur
    c0, c1 = M.CANAL
    m_min = -min(int(n1) // c0, int(n2) // c1)
    return {"m_bord": m_bord, "n_sites_barriere": len(sites), "b_M": b_M, "Mh": Mh, "m_min": m_min,
            "debut_cap": m_bord + b_M // 2, "e_bord_sur_delta": float(m_bord)}


def _sauts(kappa, n1, n2, rg, w2=W2_LIMITE):
    t0 = tau(n1, n2, 0, w2)
    return {m: kappa * tau(n1, n2, m, w2) / t0 for m in range(rg["m_min"], rg["Mh"])}


def phi_eig(kappa, n1, n2, s=1, ef=EF, recul=0, m_facteur=M_FACTEUR):
    rg = reglage(kappa, n1, n2, m_facteur=m_facteur)
    if rg is None:
        return None
    T = _sauts(kappa, n1, n2, rg)
    m_min, Mh = rg["m_min"], rg["Mh"]
    cap = rg["debut_cap"] + recul
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = s * m
        if m > cap:
            Wd[i] = ef * (m - cap) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            H[i, i + 1] = T[m]; H[i + 1, i] = T[m]
    val, vec = np.linalg.eig(H)
    recs = np.abs(vec[-m_min, :]) ** 2
    nu = np.lexsort((val.real, -recs))[0]
    psi2 = np.abs(vec[:, nu]) ** 2
    out = dict(rg)
    out.update({"Phi_im": float(-2.0 * val[nu].imag), "Phi_flux": float(2.0 * (Wd @ psi2) / psi2.sum()),
                "E": float(val[nu].real), "recouvrement": float(recs[nu])})
    return out


def _sigma_fc(E, T, rg, s, ef, recul):
    """Parties reelles des self-energies gauche et droite du site 0 a l'energie reelle E, et ln(-Im) de la droite.
    Droite : g_m = 1 / (E - s m + i W_m - T_m^2 g_{m+1}) = u_m - i v_m ; v_m = Y / (X^2 + Y^2) avec
    Y = W_m + T_m^2 v_{m+1} : que des produits et des sommes de termes positifs, suivi en logarithme."""
    m_min, Mh = rg["m_min"], rg["Mh"]
    cap = rg["debut_cap"] + recul
    u, lv = 0.0, None
    for m in range(Mh, 0, -1):
        X = E - s * m - (T[m] ** 2 * u if m < Mh else 0.0)
        W = ef * (m - cap) ** 2 if m > cap else 0.0
        if m < Mh and lv is not None:
            lY2 = 2.0 * math.log(T[m]) + lv
            if W > 0.0:
                lY = math.log(W + math.exp(lY2)) if lY2 > -700.0 else math.log(W)
            else:
                lY = lY2
        else:
            lY = math.log(W) if W > 0.0 else None
        if lY is None:
            u = 1.0 / X; lv = None
        elif lY > -300.0:
            Y = math.exp(lY); den = X * X + Y * Y
            u = X / den; lv = lY - math.log(den)
        else:
            u = 1.0 / X; lv = lY - 2.0 * math.log(abs(X))
    sig_d = T[0] ** 2 * u
    ln_im_d = 2.0 * math.log(T[0]) + lv
    gl = 0.0
    for m in range(m_min, 0):
        gl = 1.0 / (E - s * m - (T[m - 1] ** 2 * gl if m > m_min else 0.0))
    sig_g = (T[-1] ** 2 * gl) if m_min < 0 else 0.0
    return sig_g + sig_d, ln_im_d


def phi_fc(kappa, n1, n2, s=1, ef=EF, recul=0, m_facteur=M_FACTEUR, E0=0.0):
    """ln Phi par la fraction continue. Racine reelle de E - Re Sigma(E) la plus proche de E0 (Newton), poids
    Z = 1 / (1 - d Re Sigma / dE), Phi = 2 Z (-Im Sigma)."""
    rg = reglage(kappa, n1, n2, m_facteur=m_facteur)
    if rg is None:
        return None
    T = _sauts(kappa, n1, n2, rg)
    E, h = E0, 1e-6
    for it in range(200):
        f0 = E - _sigma_fc(E, T, rg, s, ef, recul)[0]
        fp = (E + h - _sigma_fc(E + h, T, rg, s, ef, recul)[0]) - (E - h - _sigma_fc(E - h, T, rg, s, ef, recul)[0])
        fp /= 2.0 * h
        dE = -f0 / fp
        if abs(dE) > 0.2:
            dE = math.copysign(0.2, dE)
        E += dE
        if abs(dE) < 1e-14:
            break
    else:
        raise RuntimeError("phi_fc : Newton n'a pas converge (kappa = %r, etiquette %r)" % (kappa, (n1, n2)))
    sig, lim = _sigma_fc(E, T, rg, s, ef, recul)
    Z = 1.0 / fp
    out = dict(rg)
    out.update({"ln_Phi": math.log(2.0) + math.log(Z) + lim, "E": E, "Z": Z, "iterations": it + 1})
    return out


def phi_mp(kappa, n1, n2, s=1, ef=EF, recul=0, m_facteur=M_FACTEUR, chiffres=None, E0=None):
    """Pole complexe exact de G_00 (fraction continue complexe, precision arbitraire) : Phi = -2 Im E."""
    import mpmath as mp
    rg = reglage(kappa, n1, n2, m_facteur=m_facteur)
    if rg is None:
        return None
    grossier = phi_fc(kappa, n1, n2, s, ef, recul, m_facteur)
    if chiffres is None:
        chiffres = int(-grossier["ln_Phi"] / math.log(10.0)) + 40
    mp.mp.dps = chiffres
    Tf = _sauts(kappa, n1, n2, rg)
    T2 = {m: mp.mpf(Tf[m]) ** 2 for m in Tf}
    m_min, Mh = rg["m_min"], rg["Mh"]
    cap = rg["debut_cap"] + recul
    efm = mp.mpf(ef)

    def D(E):
        g = mp.mpc(0)
        for m in range(Mh, 0, -1):
            h = mp.mpc(s * m, -(efm * (m - cap) ** 2) if m > cap else 0)
            g = 1 / (E - h - (T2[m] * g if m < Mh else 0))
        sd = T2[0] * g
        gl = mp.mpc(0)
        for m in range(m_min, 0):
            gl = 1 / (E - s * m - (T2[m - 1] * gl if m > m_min else 0))
        sg = T2[-1] * gl if m_min < 0 else 0
        return E - sg - sd

    E = mp.mpc(grossier["E"] if E0 is None else E0, -mp.exp(grossier["ln_Phi"]) / 2)
    h = mp.mpf(10) ** (-chiffres // 2)
    for it in range(60):
        d0 = D(E)
        dp = (D(E + h) - D(E - h)) / (2 * h)
        dE = -d0 / dp
        E += dE
        if abs(dE) < mp.mpf(10) ** (-(chiffres - 8)):
            break
    out = dict(rg)
    out.update({"ln_Phi": float(mp.log(-2 * E.imag)), "E": float(E.real), "chiffres": chiffres, "iterations": it + 1})
    return out


if __name__ == "__main__":
    MOTEUR, SORTIE = sys.argv[1:3]
    charger(MOTEUR)
    out = {"reglage": {"ef": EF, "M_facteur": M_FACTEUR, "w2": "2"}, "controles": []}
    print("CONTROLE DES TROIS ARITHMETIQUES (Phi = Gamma / |delta| a la limite delta -> 0, kappa fixe)")
    print(" etiquette  kappa   m_bord  ln Phi (eig, flux)  ln Phi (eig, Im)   ln Phi (fc)        ln Phi (mp)        fc-flux     fc-mp      s=-1 : fc(-)-fc(+)")
    pire_flux, pire_mp, pire_signe = 0.0, 0.0, 0.0
    for (n1, n2) in ((0, 0), (6, 2), (10, 3), (5, 1)):
        for kappa in (0.30, 0.22, 0.15, 0.10, 0.06, 0.03):
            e = phi_eig(kappa, n1, n2)
            if e is None:
                print(" (%2d,%2d)   %.3f   barriere vide" % (n1, n2, kappa)); continue
            f = phi_fc(kappa, n1, n2)
            fm = phi_fc(kappa, n1, n2, s=-1)
            p = phi_mp(kappa, n1, n2)
            lf = math.log(e["Phi_flux"]) if e["Phi_flux"] > 0 else float("nan")
            li = math.log(e["Phi_im"]) if e["Phi_im"] > 0 else float("nan")
            d_flux = f["ln_Phi"] - lf; d_mp = f["ln_Phi"] - p["ln_Phi"]; d_s = fm["ln_Phi"] - f["ln_Phi"]
            fiable = e["Phi_flux"] > 1e-18
            if fiable and not math.isnan(d_flux):
                pire_flux = max(pire_flux, abs(d_flux))
            pire_mp = max(pire_mp, abs(d_mp)); pire_signe = max(pire_signe, abs(d_s))
            out["controles"].append({"n1": n1, "n2": n2, "kappa": kappa, "m_bord": e["m_bord"], "ln_Phi_flux": lf, "ln_Phi_im": li,
                                     "ln_Phi_fc": f["ln_Phi"], "ln_Phi_mp": p["ln_Phi"], "chiffres_mp": p["chiffres"], "E_fc": f["E"], "E_eig": e["E"],
                                     "Z": f["Z"], "recouvrement_eig": e["recouvrement"], "ln_Phi_fc_s_moins": fm["ln_Phi"]})
            print(" (%2d,%2d)   %.3f   %4d    %+17.10f  %+17.10f  %+17.10f  %+17.10f  %+.2e  %+.2e  %+.2e" % (n1, n2, kappa, e["m_bord"], lf, li, f["ln_Phi"], p["ln_Phi"], d_flux, d_mp, d_s))
    out["pire_ecart_fc_flux_au_dessus_de_1e-18"] = pire_flux; out["pire_ecart_fc_mp"] = pire_mp; out["pire_ecart_signe"] = pire_signe
    print("pire |fc - flux| la ou Phi > 1e-18 : %.2e ; pire |fc - mp| : %.2e ; pire |fc(s=-1) - fc(s=+1)| : %.2e" % (pire_flux, pire_mp, pire_signe))
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
