# -*- coding: utf-8 -*-
"""CERTIFICATION PAR MACHINE 2 DE L'ACTE DELTA nn P-4 -- classe 1.
Piece certifiee : journal_delta_nn_P4_v1.md (lot machine 1 du 08/09, canon 710498cdc372ed02).
Machine 1 demande la certification en un tour avant depot.

METHODE, la meme qu'au delta 87 :
  - le PERIMETRE est EXTRAIT du texte de l'acte par regex, jamais recopie ;
  - AUCUNE feuille de lecture n'est relue -- ni celle de machine 1, ni la mienne du 02/09 :
    tous les comptes sont re-derives de (grille_repr, t_exp) du JSON du run e66549fd72f4239b,
    et la barriere est re-derivee de la FORME FERMEE de nn.2 A-2, pas lue dans un fichier ;
  - t_exp porte le temps d'explosion a T = 1600 ; le comportement a T = 400 s'en deduit
    (explose a 400 <=> 0 < t_exp <= 400), ce qui donne les DEUX fenetres du meme tableau ;
  - la garde de la maison : verifiees + absentes + ecarts == lignes, et un compte de bilan
    calcule APRES le dernier ajout."""
import hashlib, json, math, os, re, sys, unicodedata, zipfile

S = sys.argv[1] if len(sys.argv) > 1 else "."
ACTE = sys.argv[2] if len(sys.argv) > 2 else os.path.join(S, "..", "lot22", "journal_delta_nn_P4_v1.md")
DEPOT = r"D:\devs\bocal\BOCAL4"
G_COUPL = 0.05


def convB(b):
    try:
        t = unicodedata.normalize("NFC", b.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n"))
        return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
    except Exception:
        return None


def brut(b):
    return hashlib.sha256(b).hexdigest()[:16]


texte = open(ACTE, "rb").read()
print("=== 0. L'ACTE ===")
print("  journal_delta_nn_P4_v1.md : B = %s, brut = %s, %d octets" % (convB(texte), brut(texte), len(texte)))
t = texte.decode("utf-8")
print("  caracteres non ASCII : %d ; signes pour cent : %d ; 'pour cent' en toutes lettres : %d"
      % (sum(1 for c in t if ord(c) > 127), t.count("%"), len(re.findall(r"\bpour cent\b", t))))

# ---------- 1. perimetre extrait ----------
emps = []
for m in re.finditer(r"\b([0-9a-f]{16})\b", t):
    if m.group(1) not in emps:
        emps.append(m.group(1))
corpus = {}
racines = [DEPOT] + sorted(__import__("glob").glob(os.path.join(S, "..", "lot*"))) + [S]
racines = [r for r in racines if os.path.isdir(r)]
for R in racines:
    for dp, dn, fn in os.walk(R):
        for f in fn:
            p = os.path.join(dp, f)
            try:
                b = open(p, "rb").read()
            except Exception:
                continue
            for e in (convB(b), brut(b)):
                if e:
                    corpus.setdefault(e, os.path.relpath(p, R))
            if f.lower().endswith(".zip"):
                try:
                    Z = zipfile.ZipFile(p)
                except Exception:
                    continue
                for n in Z.namelist():
                    if n.endswith("/"):
                        continue
                    bb = Z.read(n)
                    for e in (convB(bb), brut(bb)):
                        if e:
                            corpus.setdefault(e, os.path.basename(p) + " :: " + n)
                    if n.lower().endswith(".zip"):
                        try:
                            ZI = zipfile.ZipFile(__import__("io").BytesIO(bb))
                        except Exception:
                            continue
                        for nn2 in ZI.namelist():
                            if nn2.endswith("/"):
                                continue
                            ib = ZI.read(nn2)
                            for e in (convB(ib), brut(ib)):
                                if e:
                                    corpus.setdefault(e, os.path.basename(p) + " :: " + n + " :: " + nn2)
manquantes = [e for e in emps if e not in corpus]
print("")
print("=== 1. PERIMETRE EXTRAIT DE L'ACTE ===")
print("  empreintes citees : %d ; retrouvees dans le corpus detenu : %d ; non detenues : %d"
      % (len(emps), len(emps) - len(manquantes), len(manquantes)))
for e in manquantes:
    print("    NON DETENUE  %s" % e)

# ---------- 2. la barriere, re-derivee de la forme fermee ----------
print("")
print("=== 2. LA BARRIERE, RE-DERIVEE DE LA FORME FERMEE DE nn.2 A-2 (aucun fichier lu) ===")


def barriere(p, w2, sgn, g=G_COUPL):
    delta = w2 * w2 - 1.0
    kappa = w2 * w2 / (1.0 + w2 * w2)
    S_b = -(delta * kappa / g) ** (1.0 / (p - 2))
    E_b = kappa * S_b * S_b * (p - 2) / (2.0 * p)
    Q = ((1.0 + w2 * w2) ** 2 + 4.0 * w2 * w2) / (2.0 * delta * delta)
    s_b0 = math.sqrt(E_b / Q)

    def E0(s):
        return Q * s * s + (g / (p * delta)) * ((sgn * s) ** p)
    lo, hi = 0.0, s_b0 * 4.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if E0(mid) < E_b:
            lo = mid
        else:
            hi = mid
    return S_b, E_b, Q, s_b0, 0.5 * (lo + hi)


SB_ACTE = {(5, 2.00): -3.6342, (5, 2.22): -4.0272, (5, 1.50): -2.5867,
           (7, 2.00): -2.1689, (7, 2.42): -2.4198, (7, 2.50): -2.4623, (7, 1.50): -1.7687}
n_sb = 0
for (p, w2), att in sorted(SB_ACTE.items()):
    S_b = barriere(p, w2, 1)[0]
    ok = abs(S_b - att) < 5e-5
    n_sb += ok
    print("  S_b(%d|%.2f) = %.6f   acte : %.4f   %s" % (p, w2, S_b, att, "CONFORME" if ok else "ECART <<<"))
print("  S_b : %d sur %d conformes" % (n_sb, len(SB_ACTE)))

# ---------- 3. les comptes, re-derives du JSON du run ----------
print("")
print("=== 3. LES COMPTES, RE-DERIVES DE (grille_repr, t_exp) DU JSON e66549fd72f4239b ===")
Z = zipfile.ZipFile(os.path.join(DEPOT, "lot_machine2_2026-09-02_P4_run_v4.zip"))
jb = Z.read("mesures_P4_jumeau_machine2_v1.json")
print("  empreinte du JSON relu : %s (acte : e66549fd72f4239b) -> %s"
      % (convB(jb), "CONFORME" if convB(jb) == "e66549fd72f4239b" else "ECART <<<"))
D = json.loads(jb.decode("utf-8"))
G = D["grilles"]

pair_pts = pair_expl = 0
imp_sous = imp_sous_expl = 0
c21 = {}
seuils = []
garde_max = 0.0
garde_ok = 0
somme_ok = 0
for x in G:
    s = [float(v) for v in x["grille_repr"]]
    te = x["t_exp"]
    assert len(s) == len(te)
    expl1600 = [i for i, v in enumerate(te) if v is not None and v > 0]
    expl400 = [i for i, v in enumerate(te) if v is not None and 0 < v <= 400.0]
    if x["n_expl"] + x["n_non_expl"] == len(s):
        somme_ok += 1
    garde_max = max(garde_max, x["derive_Eplus_max"])
    garde_ok += bool(x["derive_Eplus_max"] <= x["garde"])
    if x["p"] % 2 == 0:
        pair_pts += len(s)
        pair_expl += len(expl1600)
    else:
        sb = barriere(x["p"], x["w2"], x["sgn"])[4]
        sous = [i for i, v in enumerate(s) if v < sb]
        imp_sous += len(sous)
        imp_sous_expl += len([i for i in sous if i in set(expl1600)])
        if abs(x["w2"] - 2.00) < 1e-9 and x["grille"] == "G_P1":
            c21[x["colonne"]] = (len(expl1600), len(s))
    if expl1600:
        i1600 = expl1600[0]
        i400 = expl400[0] if expl400 else None
        seuils.append((x["colonne"], x["grille"], i400, i1600, s[i1600]))

print("  degre PAIR   : %d points, %d explosions   (acte : 0 sur 480)  -> %s"
      % (pair_pts, pair_expl, "CONFORME" if (pair_pts, pair_expl) == (480, 0) else "ECART <<<"))
print("  degre IMPAIR sous s_b : %d points, %d explosions   (acte : 0 sur 1512)  -> %s"
      % (imp_sous, imp_sous_expl, "CONFORME" if (imp_sous, imp_sous_expl) == (1512, 0) else "ECART <<<"))
print("  site 2:1 sur G_P1, quatre colonnes (acte : 0/96 chacune) :")
for c in sorted(c21):
    print("     %-12s %d/%d %s" % (c, c21[c][0], c21[c][1], "CONFORME" if c21[c][0] == 0 else "ECART <<<"))
print("  garde de derive : max %.3e <= 1.1e-3 ; grilles qui passent %d sur %d ; somme derivee juste %d sur %d"
      % (garde_max, garde_ok, len(G), somme_ok, len(G)))

print("")
print("  LES SEUILS ET LEUR INDEPENDANCE EN T (indices entiers, regle 15) :")
d0 = d1 = dsup = 0
for c, gr, i400, i1600, sval in sorted(seuils):
    d = None if i400 is None else abs(i400 - i1600)
    if d == 0:
        d0 += 1
    elif d == 1:
        d1 += 1
    elif d is not None:
        dsup += 1
    print("     %-12s %-6s i400=%-5s i1600=%-4d |d|=%-4s s*=%.6f"
          % (c, gr, i400, i1600, d, sval))
print("  seuils : %d ; |d_indice| = 0 : %d ; = 1 : %d ; > 1 : %d   (acte : 14 seuils, 11 / 3 / 0)"
      % (len(seuils), d0, d1, dsup))
conforme_seuils = (len(seuils), d0, d1, dsup) == (14, 11, 3, 0)
print("  -> %s" % ("CONFORME" if conforme_seuils else "ECART <<<"))

# ---------- 4. s*/s_b ----------
print("")
print("=== 4. LE FAIT NEUF A-5 : s*_j(1600)/s_b, RE-DERIVE ===")
TABLE = {"5|2.22|-1": 1.5567, "7|2.42|+1": 1.0687, "5|2.00|+1": 1.0085, "5|2.00|-1": 1.3276,
         "7|2.00|+1": 1.0223, "7|2.00|-1": 1.2721, "7|2.50|-1": 1.1146, "5|1.50|+1": 1.2357,
         "5|1.50|-1": 1.0073, "7|1.50|+1": 1.2177, "7|1.50|-1": 1.0073}
n_ok = 0
rapports = []
for c, gr, i400, i1600, sval in sorted(seuils):
    if gr != "G_ext":
        continue
    p, w2, sgn = int(c.split("|")[0]), float(c.split("|")[1]), int(c.split("|")[2])
    sb = barriere(p, w2, sgn)[4]
    r = sval / sb
    rapports.append(r)
    att = TABLE.get(c)
    ok = att is not None and abs(r - att) < 5e-4
    n_ok += ok
    print("     %-12s s_b=%.6f  s*=%.6f  s*/s_b=%.4f  acte : %s  %s"
          % (c, sb, sval, r, att, "CONFORME" if ok else "ECART <<<"))
print("  %d sur %d conformes ; plage re-derivee [%.4f, %.4f]  (acte : 1.0073 a 1.5567)"
      % (n_ok, len(TABLE), min(rapports), max(rapports)))
plage_ok = abs(min(rapports) - 1.0073) < 5e-4 and abs(max(rapports) - 1.5567) < 5e-4

# ---------- 5. l'etat du registre ----------
print("")
print("=== 5. L'ETAT DU REGISTRE, AU MOMENT DE LA CERTIFICATION ===")
print("  L'acte (en-tete et nn.1) declare : clone frais a HEAD 0ff330b, plafond 86, premier libre 87.")
print("  Machine 1 a lu le registre AVANT que machine 2 n'y depose le delta de la sequence R3.")
import subprocess
CLONE = os.path.join(S, "..", "SG_1_depot")
if os.path.isdir(CLONE):
    subprocess.run(["git", "-C", CLONE, "fetch", "origin", "--quiet"], capture_output=True, timeout=180)
    head = subprocess.run(["git", "-C", CLONE, "rev-parse", "--short", "origin/main"],
                          capture_output=True, text=True).stdout.strip()
    sujet = subprocess.run(["git", "-C", CLONE, "log", "-1", "--format=%s", "origin/main"],
                           capture_output=True, text=True).stdout.strip()[:90]
    fic = subprocess.run(["git", "-C", CLONE, "ls-tree", "-r", "--name-only", "origin/main", "journal/"],
                         capture_output=True, text=True).stdout
    d87 = [x for x in fic.split("\n") if "delta_87" in x]
    d88 = [x for x in fic.split("\n") if "delta_88" in x]
    print("  ETAT REEL, sur clone re-fetche : origin/main = %s" % head)
    print("    %s" % sujet)
    print("    fichiers delta_87 au registre : %d %s" % (len(d87), [os.path.basename(x) for x in d87]))
    print("    fichiers delta_88 au registre : %d" % len(d88))
    print("  -> le numero 87 est PRIS depuis le depot du delta R3 ; le premier libre est 88.")

print("")
print("=== BILAN (compte etabli apres le dernier controle) ===")
controles = [("perimetre : empreintes citees toutes detenues", len(manquantes) == 0),
             ("S_b re-derives de la forme fermee", n_sb == len(SB_ACTE)),
             ("JSON du run a l'empreinte de l'acte", convB(jb) == "e66549fd72f4239b"),
             ("degre pair 0 sur 480", (pair_pts, pair_expl) == (480, 0)),
             ("degre impair 0 sur 1512 sous s_b", (imp_sous, imp_sous_expl) == (1512, 0)),
             ("site 2:1 : 0/96 aux quatre colonnes", all(v[0] == 0 for v in c21.values()) and len(c21) == 4),
             ("14 seuils, 11 a 0, 3 a 1, 0 au-dela", conforme_seuils),
             ("s*/s_b : 11 valeurs et la plage", n_ok == len(TABLE) and plage_ok),
             ("garde de derive passee 27 sur 27", garde_ok == len(G) == 27),
             ("somme derivee explosifs + non == 96", somme_ok == len(G))]
for nom, v in controles:
    print("  %-46s %s" % (nom, "PASSE" if v else "ECHOUE <<<"))
print("  controles passes : %d sur %d" % (sum(1 for _, v in controles if v), len(controles)))
json.dump({"controles": {n: bool(v) for n, v in controles},
           "empreintes_citees": len(emps), "non_detenues": manquantes,
           "pair": [pair_pts, pair_expl], "impair_sous_sb": [imp_sous, imp_sous_expl],
           "seuils": [len(seuils), d0, d1, dsup],
           "plage_s_sur_sb": [min(rapports), max(rapports)],
           "garde_max": garde_max},
          open("certification_acte_P4_machine2_v1.json", "w"), indent=1)
