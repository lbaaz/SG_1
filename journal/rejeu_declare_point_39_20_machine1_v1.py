# -*- coding: ascii -*-
# REJEU DECLARE DE MACHINE 1 (gel E-B bis dcda1611adf5f8fd, section 12) : le
# point 1.95 (39_20) en (F1, G20) sur l'echelle entiere, 18 decompositions,
# avec le levier NPY_DISABLE_CPU_FEATURES. Ce pilote ne calcule rien lui-meme :
# il charge la SONDE CERTIFIEE v3 (555146abd2192f79) et appelle ses fonctions
# pour cette seule trajectoire, comme le fait son etage 2.
# SOUS SCELLE : aucune largeur n'est affichee ni ecrite au journal ; elles
# vont au disque, et seules les empreintes sortent. La comparaison a BOCAL4
# (1e-3) se fera a la reception du lot de machine 2.
# Arguments : <sonde> <moteur> <run> <manifeste> <sortie> <nombre de barreaux>
import sys, os, json, hashlib, unicodedata, importlib.util

sonde, moteur, run, manifeste, sortie, n = sys.argv[1:7]
n = int(n)


def cB(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


assert cB(sonde) == "555146abd2192f79", "canon de la sonde"
spec = importlib.util.spec_from_file_location("sonde_v3", sonde)
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)
os.makedirs(sortie, exist_ok=True)
S.dire.f = open(os.path.join(sortie, "rejeu_declare_machine1.log"), "a")
S.dire("=" * 74)
S.dire("REJEU DECLARE m1 -- point 39_20, F1G20 -- barreaux demandes : %d sur %d"
       % (n, len(S.K_ECH)))
S.CTX.update({"etage": 2, "prevol": False, "mutation": None, "sonde": cB(sonde)})
S.ligne_plateforme()
M = S.charger_moteur(moteur)
S.authentifier_run(run, manifeste)
p = S.parametres(run, False)["39_20"]
forme, r_c, N, L = S.geometrie("F1G20", p["r0"], False)
S.dire("point 39_20 : w2 = %s, N = %d, r_c = %d, L = %d, eta0 = %r" % (
    p["w2"], N, r_c, L, p["eta0"]))
sysm = S.Systeme(M, N, p["w2"], p["g"], -1)
psi = S.cible(M, ("graine",), N, p["s"], p["w2"])
rep = os.path.join(sortie, "reprise", "PT_39_20_F1G20")
recs, vects = S.trajectoire(
    sysm, S.absorbeur(forme, r_c, N, L), p["eta0"], rep, "F1",
    S.choisir_graine(psi, S.K_ETATS, None, extras=True), ks=S.K_ECH[:n],
    meta={"forme": forme, "r_c": r_c, "L": L, "s": p["s"],
          "cibles": "graine %d" % S.K_ETATS})
S.dire("comptes : %s" % json.dumps(S.COMPTES, sort_keys=True))
S.dire("durees (s) : %s" % " ".join("k=%d:%s" % (k, recs[k].get("duree_s"))
                                    for k in S.K_ECH[:n]))
g3 = recs[3]["etats"][0]["gamma"]
S.dire("G-Q4 (ancrage, valeur deja publique de M17) : au bit %s ; rapport - 1 = %+.3e"
       % (g3 == p["G_run"], g3 / p["G_run"] - 1.0))
if n == len(S.K_ECH):
    f = os.path.join(sortie, "rejeu_point_39_20_F1G20_machine1.json")
    json.dump({"point": "39_20", "cfg": "F1G20", "forme": forme, "r_c": r_c,
               "N": N, "L": L, "w2": str(p["w2"]), "g": p["g"],
               "eta0": p["eta0"], "traj": {str(k): recs[k] for k in S.K_ECH}},
              open(f, "w"), indent=1, sort_keys=True)
    S.dire("SCELLE : %s canon %s" % (os.path.basename(f), cB(f)))
    S.dire("etats suivis par barreau : %s" % " ".join(
        "k=%d:%d" % (k, sum(1 for e in recs[k]["etats"] if e["suivi"]))
        for k in sorted(S.K_ECH)))
S.dire("-- FIN (barreaux %d) --" % n)
