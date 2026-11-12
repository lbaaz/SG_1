# -*- coding: ascii -*-
# SONDE DE QUALIFICATION E-B -- machine 1, v1 -- gel E-B v2 cde0cd11a763f26d
# CLASSE 2. Elle MESURE et ne juge pas : aucune routine de plateau, aucun
# statut, aucun verdict. Elle n'arrete que sur ses gardes d'integrite
# (G-Q1, G-Q2, G-Q3, G-Q4, G-Q6). Le moteur est charge en lecture seule.
# Aucun ** de tableau hors du moteur, sauf le temoin d'arrondi, declare.
import sys, os, json, math, hashlib, unicodedata, argparse, importlib.util
import platform, time
from fractions import Fraction
import numpy as np

CANON_GEL = "cde0cd11a763f26d"
CANON_MOTEUR = "82a0be882568fe0c"
POINTS = ["39_20", "197_100", "99_50", "101_50", "203_100", "41_20"]
K_ECH = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 1, 0, -1, -2]   # ordre declare
SEUIL_SUIVI = 0.90
K_ETATS = 10
TOL_ANCRAGE = 1e-3
CFGS = ["F1G20", "F2G20", "F3G20", "F1G30", "F1GT"]    # groupes par N
COMPTES = {}


def dire(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    if dire.f:
        dire.f.write(s + "\n")
        dire.f.flush()


dire.f = None


def canon_b(octets):
    t = unicodedata.normalize("NFC", octets.decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def arret(code, motif):
    dire("ARRET %s" % motif)
    sys.exit(code)


def compter(famille, quoi):
    c = COMPTES.setdefault(famille, {"joues": 0, "repris": 0, "sautes": 0})
    c[quoi] += 1


def charger_moteur(chemin):
    c = canon_b(open(chemin, "rb").read())
    dire("G-Q1 moteur %s canon %s : %s" % (os.path.basename(chemin), c,
                                         "OK" if c == CANON_MOTEUR else "MORD"))
    if c != CANON_MOTEUR:
        arret(2, "G-Q1 : canon du moteur")
    spec = importlib.util.spec_from_file_location("moteur_m17", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def authentifier_run(dossier, manifeste):
    att = {}
    for l in open(manifeste, "rb").read().decode("utf-8").splitlines():
        ch = l.split()
        if len(ch) == 3 and len(ch[0]) == 16 and ch[2].isdigit():
            att[ch[1]] = (ch[0], int(ch[2]))
    ok = 0
    for nom, (emp, taille) in sorted(att.items()):
        p = os.path.join(dossier, nom)
        if os.path.isfile(p):
            b = open(p, "rb").read()
            ok += int(canon_b(b) == emp and len(b) == taille)
    hors = sorted(set(os.listdir(dossier)) - set(att))
    dire("G-Q2 run : %d au canon et a la taille == %d lignes du manifeste"
         " (attendu 36) ; hors manifeste, ni ouverts ni comptes : %s"
         % (ok, len(att), hors))
    if ok != len(att) or len(att) != 36:
        arret(2, "G-Q2 : dossier du run non authentifie")
    return hors


def ligne_plateforme():
    x = np.array([1765.6704444885254])
    t = float((x ** 6)[0]).hex()          # SEUL ** de tableau : le temoin
    d = {"python": sys.version.split()[0], "numpy": np.__version__,
         "machine": platform.machine(), "systeme": platform.system(),
         "NPY_DISABLE_CPU_FEATURES": os.environ.get(
             "NPY_DISABLE_CPU_FEATURES", ""),
         "temoin_arrondi": t,
         "temoin_lecture": ("CR" if t.endswith("9c6p+64") else
                            "noyau SIMD" if t.endswith("9c5p+64") else "?")}
    dire("plateforme : %s" % json.dumps(d, sort_keys=True))
    return d


def parametres(dossier, prevol):
    P = {}
    for nom in POINTS:
        d = json.load(open(os.path.join(dossier, "pt_%s_f070.json" % nom)))
        P[nom] = {"w2": Fraction(d["w2"]), "g": d["g"], "s": d["graine"]["s"],
                  "r0": 14 if prevol else d["EB"]["r_c"],
                  "eta0": d["EB"]["eta"],
                  "G_run": d["EB"]["Gamma_LS"]["H"]["Gamma_LS"]}
    return P


def geometrie(cfg, r0, prevol):
    l20, l30, dt = (6, 9, 3) if prevol else (20, 30, 10)
    forme = cfg[:2]
    if cfg.endswith("G20"):
        return forme, r0, r0 + l20, l20
    if cfg.endswith("G30"):
        return forme, r0, r0 + l30, l30
    return forme, r0 + dt, r0 + l30, l20          # GT : bord translate


def absorbeur(forme, r_c, N, L, mutation=None):
    w = np.zeros(N * N)
    for a in range(N):
        for b in range(N):
            m = max(a, b)
            if forme == "F1" and m > r_c:
                w[a * N + b] = float((m - r_c) ** 2)
            elif forme == "F2" and m > r_c:
                w[a * N + b] = (m - r_c) ** 4 / L ** 2
            elif forme == "F3" and max(a, 2 * b) > r_c:
                w[a * N + b] = float((max(a, 2 * b) - r_c) ** 2)
    if mutation == "M-5":                 # un element deplace d'une couche
        w[(r_c + 1) * N] = 4.0
    return w


class Systeme:
    """Partie hermitienne du moteur, diagonale absorbee posee en place."""

    def __init__(self, M, N, w2, g, signe):
        self.N, self.w2, self.g, self.signe = N, w2, g, signe
        self.H = M.H_2D(N, w2, g, signe, "x5", 0.0, None)[0]
        self.d0 = self.H.diagonal().copy()

    def decomposer(self, eta, w):
        np.fill_diagonal(self.H, self.d0 + (-1j * eta) * w)
        return np.linalg.eig(self.H)


def cible(M, spec, N, s, w2):
    if spec[0] == "graine":
        return M.graine_coherente(N, s, w2)
    v = np.zeros(N * N)
    v[spec[1] * N + spec[2]] = 1.0        # ("fock", a, b) ; le vide = (0, 0)
    return v


def ordre_ancrage(vals, vecs, psi):
    r = np.abs(vecs.conj().T @ psi)
    r = r * r
    return np.lexsort((vals.real, -r)), r


def trajectoire(sysm, w, eta0, rep, famille, choisir, ks=None):
    """Suit des etats sur l'echelle. choisir(vals, vecs) -> (indices, extras)
    a k = 3. Reprise par fichier (k). Rend {k: enregistrement}."""
    os.makedirs(rep, exist_ok=True)
    recs, vects = {}, {}
    for k in (ks or K_ECH):
        fj = os.path.join(rep, "k_%+03d.json" % k)
        fv = os.path.join(rep, "k_%+03d.npy" % k)
        if os.path.exists(fj) and os.path.exists(fv):
            recs[k] = json.load(open(fj))
            vects[k] = np.load(fv)
            compter(famille, "repris")
            continue
        eta = eta0 * 2.0 ** (-k)
        if eta * 2.0 ** k != eta0:
            arret(2, "G-Q6 : echelle en eta inexacte a k = %d" % k)
        ref = None if k == 3 else (k - 1 if k > 3 else k + 1)
        if ref is not None and not any(e["suivi"] for e in recs[ref]["etats"]):
            recs[k] = {"k": k, "eta": eta, "saute": True, "etats": [
                {"suivi": False, "ov": None} for _ in recs[ref]["etats"]]}
            vects[k] = np.zeros_like(vects[ref])
            compter(famille, "sautes")
        else:
            t0 = time.time()
            vals, vecs = sysm.decomposer(eta, w)
            etats, extras = [], {}
            if ref is None:
                idx, extras = choisir(vals, vecs)
                V = np.array([vecs[:, j] for j in idx])
                for j in idx:
                    etats.append({"suivi": True, "ov": None,
                                  "E_re": float(vals[j].real),
                                  "E_im": float(vals[j].imag),
                                  "gamma": float(-2.0 * vals[j].imag)})
            else:
                V = np.zeros_like(vects[ref])
                for t, e0 in enumerate(recs[ref]["etats"]):
                    if not e0["suivi"]:
                        etats.append({"suivi": False, "ov": None})
                        continue
                    ov = np.abs(vecs.conj().T @ vects[ref][t])
                    j = int(np.argmax(ov))
                    if float(ov[j]) < SEUIL_SUIVI:
                        etats.append({"suivi": False, "ov": float(ov[j])})
                        continue
                    V[t] = vecs[:, j]
                    etats.append({"suivi": True, "ov": float(ov[j]),
                                  "E_re": float(vals[j].real),
                                  "E_im": float(vals[j].imag),
                                  "gamma": float(-2.0 * vals[j].imag)})
            recs[k] = {"k": k, "eta": eta, "saute": False, "etats": etats,
                       "duree_s": round(time.time() - t0, 1)}
            recs[k].update(extras)
            vects[k] = V
            compter(famille, "joues")
        np.save(fv, vects[k])
        json.dump(recs[k], open(fj, "w"), sort_keys=True)
    return recs, vects


def choisir_graine(psi, n, mutation=None, extras=False):
    def f(vals, vecs):
        ordre, r = ordre_ancrage(vals, vecs, psi)
        idx = [int(j) for j in ordre[:n]]
        if mutation == "M-4":
            idx = [int(ordre[1])] + idx[1:]
        x = {"recouvrements": [float(r[j]) for j in idx]}
        if extras:                        # T-etats, gel section 7
            p = vecs.T @ psi
            den = np.sum(vecs * vecs, axis=0)
            c = (p * p) / den
            sc = complex(np.sum(c))
            x.update({"poids_total": float(np.sum(r)),
                      "somme_c_re": sc.real, "somme_c_im": sc.imag,
                      "c_re": [float(c[j].real) for j in idx],
                      "c_im": [float(c[j].imag) for j in idx],
                      "kappa": [float(1.0 / abs(den[j])) for j in idx]})
        return idx, x
    return f


def choisir_cibles(cibles):
    def f(vals, vecs):
        idx, rr = [], []
        for psi in cibles:
            ordre, r = ordre_ancrage(vals, vecs, psi)
            idx.append(int(ordre[0]))
            rr.append(float(r[ordre[0]]))
        return idx, {"recouvrements": rr}
    return f


def bloc_interieur(v, N, r0):
    u = np.array([v[a * N + b] for a in range(r0 + 1) for b in range(r0 + 1)])
    n = float(np.sqrt(np.sum(np.abs(u) * np.abs(u))))
    return u / n if n > 0 else u


def etage1(M, P, a, sortie):
    res = {"etage": 1, "GQ3": {}, "GQ5": {}, "TP": {}, "TN": {}}
    # --- G-Q3 : identite de forme, sans decomposition ---------------------
    for nom in POINTS:
        p = P[nom]
        forme, r_c, N, L = geometrie("F1G20", p["r0"], a.prevol)
        s = Systeme(M, N, p["w2"], p["g"], -1)
        eta = p["eta0"] * 2.0 ** (-3)
        np.fill_diagonal(s.H, s.d0 + (-1j * eta) * absorbeur(
            "F1", r_c, N, L, a.mutation))
        ref = M.H_2D(N, p["w2"], p["g"], -1, "x5", eta, r_c)[0]
        res["GQ3"][nom] = bool(np.array_equal(s.H, ref))
        dire("G-Q3 %-8s N = %d : %s" % (nom, N, "OK" if res["GQ3"][nom]
                                        else "MORD"))
        del s, ref
    if not all(res["GQ3"].values()):
        json.dump(res, open(os.path.join(sortie, "sonde_etage1.json"), "w"),
                  indent=1, sort_keys=True)
        arret(3, "G-Q3 : la forme native n'est pas celle du moteur")
    # --- TP : jumeau H+, etat du vide --------------------------------------
    ret = json.load(open(a.retenus))["retenus"]
    w2tp = Fraction(39, 20)
    for r in ret:
        cle = "j%02d" % r["j"]
        res["TP"][cle] = {"j": r["j"], "g": r["g"], "traj": {}}
        for cfg in ("F1G20", "F1G30"):
            forme, r_c, N, L = geometrie(cfg, 14 if a.prevol else 40, a.prevol)
            s = Systeme(M, N, w2tp, r["g"], +1)
            vide = cible(M, ("fock", 0, 0), N, None, w2tp)
            recs, _ = trajectoire(
                s, absorbeur("F1", r_c, N, L), 0.05,
                os.path.join(sortie, "reprise", "TP_%s_%s" % (cle, cfg)),
                "TP", choisir_cibles([vide]))
            res["TP"][cle]["traj"][cfg] = recs
            dire("TP %s g = %.6f %s : fait" % (cle, r["g"], cfg))
            del s
    # --- TN : trois candidats loges dans l'absorbeur, memes decompositions -
    p = P["39_20"]
    forme, r_c, N, L = geometrie("F1G20", p["r0"], a.prevol)
    pas = 1 if a.prevol else 5
    cands = [r_c + 2 * pas, r_c + 3 * pas, r_c + pas]      # a, a + 5, a - 5
    s = Systeme(M, N, p["w2"], p["g"], -1)
    cibles = [cible(M, ("fock", c, c // 2), N, None, p["w2"]) for c in cands]
    recs, _ = trajectoire(s, absorbeur("F1", r_c, N, L), p["eta0"],
                          os.path.join(sortie, "reprise", "TN"), "TN",
                          choisir_cibles(cibles))
    res["TN"] = {"candidats": [[c, c // 2] for c in cands], "traj": recs}
    dire("TN : fait, candidats %s" % res["TN"]["candidats"])
    del s
    # --- G-Q5 : plancher, jumeau H+ aux geometries des points --------------
    for nom in POINTS:
        p = P[nom]
        res["GQ5"][nom] = {}
        cache = {}
        for cfg in CFGS:
            forme, r_c, N, L = geometrie(cfg, p["r0"], a.prevol)
            if N not in cache:
                cache.clear()
                cache[N] = Systeme(M, N, p["w2"], p["g"], +1)
            psi = cible(M, ("graine",), N, p["s"], p["w2"])
            recs, _ = trajectoire(
                cache[N], absorbeur(forme, r_c, N, L), p["eta0"],
                os.path.join(sortie, "reprise", "PL_%s_%s" % (nom, cfg)),
                "plancher", choisir_graine(psi, 1), ks=[3])
            res["GQ5"][nom][cfg] = recs[3]["etats"][0]["gamma"]
        dire("G-Q5 %-8s : %s" % (nom, " ".join(
            "%s %.2e" % (c, res["GQ5"][nom][c]) for c in CFGS)))
    return res


def etage2(M, P, a, sortie):
    res = {"etage": 2, "GQ4": {}, "points": {}}
    refs = None
    if a.prevol and a.ancrage_ref:
        refs = json.load(open(a.ancrage_ref))
    # --- OUVERTURE : les six (F1, G20, k = 3), puis G-Q4 -------------------
    S3 = {}
    for nom in POINTS:
        p = P[nom]
        forme, r_c, N, L = geometrie("F1G20", p["r0"], a.prevol)
        s = Systeme(M, N, p["w2"], p["g"], -1)
        psi = cible(M, ("graine",), N, p["s"], p["w2"])
        recs, vects = trajectoire(
            s, absorbeur(forme, r_c, N, L), p["eta0"],
            os.path.join(sortie, "reprise", "PT_%s_F1G20" % nom),
            "ouverture",
            choisir_graine(psi, K_ETATS, a.mutation, extras=True), ks=[3])
        g3 = recs[3]["etats"][0]["gamma"]
        G = p["G_run"] if not a.prevol else (refs[nom] if refs else None)
        res["GQ4"][nom] = {"gamma": g3, "reference": G,
                           "rapport": (g3 / G if G else None),
                           "au_bit": (g3 == G if G else None)}
        dire("G-Q4 %-8s gamma %.10e reference %s rapport %s au bit %s" % (
            nom, g3, G, res["GQ4"][nom]["rapport"], res["GQ4"][nom]["au_bit"]))
        S3[nom] = vects[3][0].copy()
        del s
    if a.prevol and not refs:
        json.dump({n: res["GQ4"][n]["gamma"] for n in POINTS}, open(
            os.path.join(sortie, "ancrage_prevol.json"), "w"), sort_keys=True)
    mord = [n for n in POINTS if res["GQ4"][n]["rapport"] is not None
            and abs(res["GQ4"][n]["rapport"] - 1.0) > TOL_ANCRAGE]
    if mord:
        json.dump(res, open(os.path.join(sortie, "sonde_etage2.json"), "w"),
                  indent=1, sort_keys=True)
        arret(3, "G-Q4 : ancrage hors de %g a %s" % (TOL_ANCRAGE, mord))
    # --- LES SIX POINTS ------------------------------------------------------
    for nom in POINTS:
        p = P[nom]
        res["points"][nom] = {"w2": str(p["w2"]), "G_run": p["G_run"],
                              "r0": p["r0"], "eta0": p["eta0"], "cfg": {}}
        cache = {}
        for cfg in CFGS:
            forme, r_c, N, L = geometrie(cfg, p["r0"], a.prevol)
            if N not in cache:
                cache.clear()
                cache[N] = Systeme(M, N, p["w2"], p["g"], -1)
            psi = cible(M, ("graine",), N, p["s"], p["w2"])
            prem = (cfg == "F1G20")
            recs, vects = trajectoire(
                cache[N], absorbeur(forme, r_c, N, L), p["eta0"],
                os.path.join(sortie, "reprise", "PT_%s_%s" % (nom, cfg)),
                {"F1G20": "F1", "F1G30": "F1", "F1GT": "translation"}.get(
                    cfg, "formes"),
                choisir_graine(psi, K_ETATS if prem else 1,
                               a.mutation if prem else None, extras=prem))
            ident = 1.0
            if not prem:
                u = bloc_interieur(S3[nom], geometrie(
                    "F1G20", p["r0"], a.prevol)[2], p["r0"])
                v = bloc_interieur(vects[3][0], N, p["r0"])
                ident = float(abs(np.vdot(u, v)))
            res["points"][nom]["cfg"][cfg] = {
                "forme": forme, "r_c": r_c, "N": N, "L": L,
                "identite": ident, "traj": recs}
            dire("point %-8s %s : fait (identite %.4f)" % (nom, cfg, ident))
    return res


def main():
    ap = argparse.ArgumentParser()
    for x in ("moteur", "run", "manifeste", "sortie"):
        ap.add_argument("--" + x, required=True)
    ap.add_argument("--etage", type=int, required=True, choices=[1, 2])
    ap.add_argument("--retenus")
    ap.add_argument("--verdict1")
    ap.add_argument("--prevol", action="store_true")
    ap.add_argument("--ancrage-ref", dest="ancrage_ref")
    ap.add_argument("--mutation", choices=["M-4", "M-5"])
    a = ap.parse_args()
    os.makedirs(a.sortie, exist_ok=True)
    dire.f = open(os.path.join(a.sortie, "sonde_etage%d.log" % a.etage), "w")
    dire("=" * 74)
    dire("SONDE DE QUALIFICATION E-B v1 -- gel %s -- etage %d%s%s" % (
        CANON_GEL, a.etage, " -- PRE-VOL (geometrie reduite, NON OPPOSABLE)"
        if a.prevol else "", " -- MUTATION %s" % a.mutation if a.mutation
        else ""))
    dire("=" * 74)
    if a.mutation and not a.prevol:
        arret(2, "une mutation ne se joue qu'en pre-vol")
    plat = ligne_plateforme()
    M = charger_moteur(a.moteur)
    hors = authentifier_run(a.run, a.manifeste)
    P = parametres(a.run, a.prevol)
    if a.etage == 1:
        if not a.retenus:
            arret(2, "etage 1 : --retenus manque")
        res = etage1(M, P, a, a.sortie)
        att = {"TP": 60, "TN": 15, "plancher": 30}
        att["TP"] = 30 * len(res["TP"])
    else:
        f1 = os.path.join(a.sortie, "sonde_etage1.json")
        v = json.load(open(a.verdict1)) if a.verdict1 else {}
        if v.get("etage1") != "TIENT" or v.get("canon_sonde_etage1") != \
                canon_b(open(f1, "rb").read()):
            arret(2, "etage 2 refuse : pas de verdict d'etage 1 qui TIENT"
                     " sur ce sonde_etage1.json")
        if v.get("factice") and not a.prevol:
            arret(2, "etage 2 refuse : verdict factice hors pre-vol")
        res = etage2(M, P, a, a.sortie)
        att = {"F1": 180, "formes": 180, "translation": 90, "ouverture": 6}
    ok = True
    for fam in sorted(att):
        c = COMPTES.get(fam, {"joues": 0, "repris": 0, "sautes": 0})
        tot = c["joues"] + c["repris"] + c["sautes"]
        ok = ok and tot == att[fam]
        dire("G-Q10 %-12s joues %d + repris %d + sautes %d == %d attendus : %s"
             % (fam, c["joues"], c["repris"], c["sautes"], att[fam],
                "OK" if tot == att[fam] else "MORD"))
    res.update({"gel": CANON_GEL, "moteur": CANON_MOTEUR, "prevol": a.prevol,
                "mutation": a.mutation, "plateforme": plat,
                "hors_manifeste": hors, "comptes": COMPTES,
                "attendus": att, "GQ10": ok})
    fs = os.path.join(a.sortie, "sonde_etage%d.json" % a.etage)
    json.dump(res, open(fs, "w"), indent=1, sort_keys=True)
    dire("sonde %s canon %s (relu du disque)" % (
        os.path.basename(__file__), canon_b(open(__file__, "rb").read())))
    dire("sortie %s canon %s (relu du disque)" % (
        os.path.basename(fs), canon_b(open(fs, "rb").read())))
    dire("CE QUE CE LOG NE JOUE PAS : aucune routine de plateau, aucun statut,"
         " aucun verdict ; %s" % ("l'etage 2." if a.etage == 1 else
                                  "l'etage 1 (deja juge)."))
    if not ok:
        arret(3, "G-Q10 : comptes")


if __name__ == "__main__":
    main()
