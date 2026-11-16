# -*- coding: ascii -*-
"""LE PROCEDE DU LECTEUR CREUX SUR UNE BARRIERE PROFONDE -- machine 1, v1, 2026-11-16. Hors chaine, classe 3.
AUCUN CALCUL 2D, aucune largeur du systeme a fantome 2D. On donne a la routine DEPOSEE du lecteur (lire_etat : iteration
inverse creuse a decalage fixe, largeur par le flux 2 eta <W>) une matrice dont la largeur est connue par une autre
arithmetique : la chaine tridiagonale de la limite pour l'etat (0, 0), rangee dans une "boite" de N x N sites (les sites
en trop sont decouples), sous l'absorbeur de la chaine deposee. Reference : la fraction continue en logarithme de
phi_echelle (elle-meme controlee contre le pole exact en precision arbitraire).
Question : la double precision limite-t-elle la profondeur que ce procede lit ?
Usage : python3 -I procede_lecteur_profond_machine1_v1.py <moteur> <sonde_lecteur_gel_loi.py> <phi_echelle.py> <carte.py>
        <bloc 2> <bloc 3> <sortie.json>"""
import sys, math, json, hashlib, unicodedata, importlib.util
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
MOTEUR, SONDE, PHI, CARTE, BLOC2, BLOC3, SORTIE = sys.argv[1:8]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
if canon_B(SONDE) != "d5cc48f48e37af99":
    raise SystemExit("REFUS : canon de la sonde du lecteur")
sauv = list(sys.argv); sys.argv = [CARTE, MOTEUR, BLOC2, BLOC3, PHI, "/dev/null"]
spec = importlib.util.spec_from_file_location("carte", CARTE); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C); sys.argv = sauv
PH, M = C.PH, C.M
src = open(SONDE, encoding="ascii").read(); i0 = src.index("# --- LECTEUR CREUX"); i1 = src.index("# --- fin du bloc ---", i0)
exec(compile(src[i0:i1], "bloc_lecteur_depose", "exec"))
out = []
print(" barreaux  kappa        sites   ln Phi (fraction continue)   ln Phi (procede du lecteur)   ecart        iterations  residu     poids du site 0")
for mc in (4, 8, 16, 32, 64, 128):
    k = C.kappa_pour_m_bord(0, 0, mc)[0]
    f = PH.phi_fc(k, 0, 0); rg = PH.reglage(k, 0, 0)
    Mh, cap = rg["Mh"], rg["debut_cap"]
    N = int(math.ceil(math.sqrt(Mh + 1))); n = N * N
    t0 = PH.tau(0, 0, 0); T = [k * PH.tau(0, 0, m) / t0 for m in range(Mh)]
    I = list(range(Mh)) + list(range(1, Mh + 1)); Jc = list(range(1, Mh + 1)) + list(range(Mh))
    H0 = sp.csc_matrix((T + T, (I, Jc)), shape=(n, n), dtype=float)
    diag = np.array([float(m) for m in range(Mh + 1)] + [1.0e6 + j for j in range(n - Mh - 1)])
    W = np.zeros(n)
    for m in range(cap + 1, Mh + 1):
        W[m] = PH.EF * (m - cap) ** 2
    r, x = lire_etat(H0, diag, W, 1.0, N, (0, 0), f["E"])
    lg = math.log(r["gamma"]) if r["gamma"] and r["gamma"] > 0 else float("nan")
    out.append({"m_cible": mc, "kappa": k, "sites": Mh + 1, "ln_Phi_fc": f["ln_Phi"], "ln_Phi_lecteur": lg, "ecart": lg - f["ln_Phi"], "suivi": r["suivi"], "iterations": r["iterations"],
                "residu": r["residu"], "poids_site": r["poids_site"], "decalage_repris": r["decalage_repris"]})
    print("  %4d    %.4e   %5d   %+.10f           %+.10f            %+.1e     %2d        %.1e    %.6f%s" % (mc, k, Mh + 1, f["ln_Phi"], lg, lg - f["ln_Phi"], r["iterations"], r["residu"], r["poids_site"], "" if r["suivi"] else "  NON SUIVI"))
pire = max(abs(o["ecart"]) for o in out)
print("plus grand ecart : %.1e ; plus petite largeur lue : exp(%.1f)" % (pire, min(o["ln_Phi_lecteur"] for o in out)))
json.dump({"points": out, "pire_ecart": pire}, open(SORTIE, "w"), indent=1, sort_keys=True)
