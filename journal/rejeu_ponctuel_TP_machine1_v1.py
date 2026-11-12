# -*- coding: ascii -*-
# REJEU PONCTUEL DU TEMOIN POSITIF PAR MACHINE 1 -- hors du perimetre de rejeu
# declare au gel (section 12), NON OPPOSABLE. Six decompositions du JUMEAU H+
# (aucune du fantome) : les deux couplages retenus, geometrie G20 (N = 60,
# r_c = 40), k = -2, 1, 3. Code ecrit ici : il n'emprunte au moteur que H_2D
# (absorbeur natif compris) et ne charge pas la sonde. Etat : plus grand
# recouvrement hermitien avec le vide de Fock, SANS suivi par continuite.
# Arguments : <moteur> <liste des retenus> <sonde_etage1.json de m2> <journal>
import sys, json, time, hashlib, unicodedata, importlib.util, platform
from fractions import Fraction
import numpy as np

moteur, retenus, nuit, journal = sys.argv[1:5]
F = open(journal, "w", encoding="ascii", newline="\n")


def dire(s):
    print(s, flush=True)
    F.write(s + "\n")
    F.flush()


def cB(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


assert cB(moteur) == "82a0be882568fe0c", "canon du moteur"
spec = importlib.util.spec_from_file_location("moteur_m17", moteur)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
x = float(2 ** 64 + 2 ** 12 + 1) * (1.0 + 2.0 ** -52)
dire("plateforme : %s %s, python %s, numpy %s" % (
    platform.system(), platform.machine(), platform.python_version(), np.__version__))
dire("entrants : moteur %s ; liste %s ; sortie de la sonde (m2) %s" % (
    cB(moteur), cB(retenus), cB(nuit)))
s1 = json.load(open(nuit))
N, r_c, w2 = 60, 40, Fraction(39, 20)
pire = 0.0
for r in json.load(open(retenus))["retenus"]:
    cle = "j%02d" % r["j"]
    assert s1["TP"][cle]["g"] == r["g"]
    for k in (-2, 1, 3):
        eta = 0.05 * 2.0 ** (-k)
        t0 = time.time()
        H = M.H_2D(N, w2, r["g"], +1, "x5", eta, r_c)[0]
        vals, vecs = np.linalg.eig(H)
        ov = np.abs(vecs[0, :]) ** 2 / np.sum(np.abs(vecs) ** 2, axis=0)
        i = int(np.argmax(ov))
        gam = float(-2.0 * vals[i].imag)
        m2 = s1["TP"][cle]["traj"]["F1G20"][str(k)]["etats"][0]["gamma"]
        ec = gam / m2 - 1.0
        pire = max(pire, abs(ec))
        dire("TP %s g = %.17g G20 k = %2d eta = %.6g : Gamma m1 = %.10e ; sonde m2 = %.10e ;"
             " m1/m2 - 1 = %+.3e ; recouvrement %.6f ; %.0f s" % (
                 cle, r["g"], k, eta, gam, m2, ec, float(ov[i]), time.time() - t0))
        del H, vals, vecs
dire("pire ecart relatif m1/m2 sur les six : %.3e" % pire)
dire("-- FIN rejeu_ponctuel_TP_machine1_v1 --")
