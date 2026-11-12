# -*- coding: ascii -*-
# Construit la sonde v2 et le banc qui tue v2 depuis leurs v1, par remplacements
# a ancre unique. Arguments : <sonde v1> <sonde v2> <banc v1> <banc v2>.
# Morsures de m2 (lot 123880c93b810d35) : D-1 reprise sans identite, D-2 porte
# franchie sous un verdict de pre-vol, D-3 banc lance par -I ; O-3 libelle.
import sys, hashlib, unicodedata


def canon_b(o):
    t = unicodedata.normalize("NFC", o.decode("utf-8"))
    return hashlib.sha256(t.replace("\r\n", "\n").encode("utf-8")).hexdigest()[:16]


def appliquer(src, H, nom):
    for etiq, vieux, neuf in H:
        if src.count(vieux) != 1:
            sys.exit("ancre non unique : %s / %s (%d)" % (nom, etiq, src.count(vieux)))
        src = src.replace(vieux, neuf)
        print("%s : applique %s" % (nom, etiq))
    return src


so = open(sys.argv[1], "rb").read()
assert canon_b(so) == "214ea376cbf540a4", "base : ce n'est pas la sonde v1"
bo = open(sys.argv[3], "rb").read()
assert canon_b(bo) == "666e69f11bc1f72c", "base : ce n'est pas le banc v1"

S = []
S.append(("S0 en-tete",
"# SONDE DE QUALIFICATION E-B -- machine 1, v1 -- gel E-B v2 cde0cd11a763f26d\n",
"# SONDE DE QUALIFICATION E-B -- machine 1, v2 -- gel E-B v2 cde0cd11a763f26d\n"
"# v2 = v1 (214ea376cbf540a4) + D-1 (identite de reprise) + D-2 (porte).\n"))
S.append(("S0 banniere",
'    dire("SONDE DE QUALIFICATION E-B v1 -- gel %s -- etage %d%s%s" % (',
'    dire("SONDE DE QUALIFICATION E-B v2 -- gel %s -- etage %d%s%s" % ('))
S.append(("S1 contexte (D-1)",
"COMPTES = {}\n",
"COMPTES = {}\n"
'CTX = {"etage": 0, "prevol": True, "mutation": None, "sonde": "hors main",\n'
'       "moteur": CANON_MOTEUR, "gel": CANON_GEL}\n'))
S.append(("S2 identite (D-1)",
'''def trajectoire(sysm, w, eta0, rep, famille, choisir, ks=None):
    """Suit des etats sur l'echelle. choisir(vals, vecs) -> (indices, extras)
    a k = 3. Reprise par fichier (k). Rend {k: enregistrement}."""
    os.makedirs(rep, exist_ok=True)
''',
'''def trajectoire(sysm, w, eta0, rep, famille, choisir, ks=None, meta=None):
    """Suit des etats sur l'echelle. choisir(vals, vecs) -> (indices, extras)
    a k = 3. Reprise par fichier (k) SOUS IDENTITE (D-1) : un fichier repris
    doit porter la meme identite que le calcul demande, sinon ARRET."""
    os.makedirs(rep, exist_ok=True)
    ident = dict(CTX, trajet=os.path.basename(rep), N=sysm.N,
                 w2=str(sysm.w2), g=sysm.g, signe=sysm.signe, eta0=eta0,
                 **(meta or {}))
'''))
S.append(("S3 refus de reprise (D-1)",
'''            recs[k] = json.load(open(fj))
            vects[k] = np.load(fv)
            compter(famille, "repris")
''',
'''            recs[k] = json.load(open(fj))
            vects[k] = np.load(fv)
            vu = recs[k].get("identite_reprise") or {}
            if vu != ident or vects[k].shape[-1] != sysm.N * sysm.N:
                arret(2, "reprise refusee (D-1) : %s porte une autre"
                         " identite, cles en ecart %s" % (fj, sorted(
                             c for c in set(ident) | set(vu)
                             if vu.get(c) != ident.get(c))))
            compter(famille, "repris")
'''))
S.append(("S4 identite ecrite (D-1)",
'''        json.dump(recs[k], open(fj, "w"), sort_keys=True)
''',
'''        recs[k]["identite_reprise"] = ident
        json.dump(recs[k], open(fj, "w"), sort_keys=True)
'''))
S.append(("S5 meta TP",
'''                "TP", choisir_cibles([vide]))''',
'''                "TP", choisir_cibles([vide]),
                meta={"forme": "F1", "r_c": r_c, "L": L, "cibles": "vide"})'''))
S.append(("S5 meta TN",
'''                          os.path.join(sortie, "reprise", "TN"), "TN",
                          choisir_cibles(cibles))''',
'''                          os.path.join(sortie, "reprise", "TN"), "TN",
                          choisir_cibles(cibles),
                          meta={"forme": "F1", "r_c": r_c, "L": L,
                                "cibles": "fock %s" % cands})'''))
S.append(("S5 meta plancher",
'''                "plancher", choisir_graine(psi, 1), ks=[3])''',
'''                "plancher", choisir_graine(psi, 1), ks=[3],
                meta={"forme": forme, "r_c": r_c, "L": L,
                      "cibles": "graine 1", "s": p["s"]})'''))
S.append(("S5 meta ouverture",
'''            choisir_graine(psi, K_ETATS, a.mutation, extras=True), ks=[3])''',
'''            choisir_graine(psi, K_ETATS, a.mutation, extras=True), ks=[3],
            meta={"forme": forme, "r_c": r_c, "L": L,
                  "cibles": "graine %d" % K_ETATS, "s": p["s"]})'''))
S.append(("S5 meta points",
'''                choisir_graine(psi, K_ETATS if prem else 1,
                               a.mutation if prem else None, extras=prem))''',
'''                choisir_graine(psi, K_ETATS if prem else 1,
                               a.mutation if prem else None, extras=prem),
                meta={"forme": forme, "r_c": r_c, "L": L, "s": p["s"],
                      "cibles": "graine %d" % (K_ETATS if prem else 1)})'''))
S.append(("S6 contexte pose (D-1)",
'''    plat = ligne_plateforme()
''',
'''    CTX.update({"etage": a.etage, "prevol": bool(a.prevol),
                "mutation": a.mutation,
                "sonde": canon_b(open(__file__, "rb").read())})
    plat = ligne_plateforme()
'''))
S.append(("S7 porte (D-2)",
'''        f1 = os.path.join(a.sortie, "sonde_etage1.json")
        v = json.load(open(a.verdict1)) if a.verdict1 else {}
''',
'''        f1 = os.path.join(a.sortie, "sonde_etage1.json")
        if not os.path.exists(f1):
            arret(2, "etage 2 refuse : pas de sonde_etage1.json en sortie")
        v = json.load(open(a.verdict1)) if a.verdict1 else {}
'''))
S.append(("S8 porte (D-2)",
'''            arret(2, "etage 2 refuse : verdict factice hors pre-vol")
''',
'''            arret(2, "etage 2 refuse : verdict factice hors pre-vol")
        s1 = json.load(open(f1))
        drap = [bool(a.prevol), bool(v.get("prevol")), bool(s1.get("prevol"))]
        if len(set(drap)) != 1 or s1.get("mutation"):
            arret(2, "etage 2 refuse (D-2) : pre-vol de la commande, du"
                     " verdict et de sonde_etage1.json = %s ; mutation de"
                     " l'etage 1 = %s" % (drap, s1.get("mutation")))
'''))
s2 = appliquer(so.decode("ascii"), S, "sonde")
open(sys.argv[2], "wb").write(s2.encode("ascii"))

b = bo.decode("ascii")
i0 = b.index("    # --- M-4, M-5 : la sonde reelle en pre-vol, avec mutation")
i1 = b.index('\n\nif __name__ == "__main__":')
assert b.count("    # --- M-4, M-5 : la sonde reelle en pre-vol, avec mutation") == 1
QUEUE = '''    # --- M-4, M-5 : la sonde reelle en pre-vol, avec mutation ----------------
    # D-3 : la sonde se lance par -P et non par -I, qui ecarte les paquets
    # utilisateur (numpy peut y vivre) : comme l'operateur la lance.
    commun = [sys.executable, "-P", a.sonde, "--moteur", a.moteur, "--run",
              a.run, "--manifeste", a.manifeste]

    def lancer(nom, extra, verdict=None, reprise=False):
        d = os.path.join(a.sortie, nom)
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
        shutil.copy(os.path.join(a.prevol, "sonde_etage1.json"), d)
        if reprise:
            shutil.copytree(os.path.join(a.prevol, "reprise"),
                            os.path.join(d, "reprise"))
        if verdict is not None:
            json.dump(verdict, open(os.path.join(d, "v1.json"), "w"))
            extra = extra + ["--verdict1", os.path.join(d, "v1.json")]
        r = subprocess.run(commun + ["--sortie", d] + extra,
                           capture_output=True, text=True)
        return r.returncode, [l for l in r.stdout.splitlines()
                              if l.startswith("ARRET")]
    c1 = S.canon_b(open(os.path.join(a.prevol, "sonde_etage1.json"),
                        "rb").read())
    code, arr = lancer("M4", ["--prevol", "--etage", "2", "--mutation", "M-4",
                              "--ancrage-ref", os.path.join(
                                  a.prevol, "ancrage_prevol.json")],
                       verdict={"etage1": "TIENT", "prevol": True,
                                "factice": True, "canon_sonde_etage1": c1})
    affirmer("M-4", "ancrage sur le deuxieme recouvrement -> G-Q4 mord",
             (code, bool(arr) and arr[0].startswith("ARRET G-Q4")), (3, True))
    code, arr = lancer("M5", ["--prevol", "--etage", "1", "--mutation", "M-5",
                              "--retenus", a.retenus])
    affirmer("M-5", "un element de W_F1 deplace -> G-Q3 mord",
             (code, bool(arr) and arr[0].startswith("ARRET G-Q3")), (3, True))
    # --- temoins hors gel : la porte (D-2) et la reprise (D-1) ---------------
    T = []

    def temoin(nom, vise, code, arr, motif):
        ok = (code == 2 and bool(arr) and motif in arr[0])
        T.append(ok)
        print("%-8s %-60s %s" % (nom, vise, "REFUSE (code 2)" if ok else
                                 "NON REFUSE : code %s, %s" % (code, arr)),
              flush=True)
    code, arr = lancer("PORTE1", ["--prevol", "--etage", "2"], verdict={
        "etage1": "NE TIENT PAS", "prevol": True, "canon_sonde_etage1": c1})
    temoin("PORTE-1", "etage 1 qui ne tient pas -> etage 2 ferme",
           code, arr, "etage 2 refuse")
    code, arr = lancer("PORTE2", ["--etage", "2"], verdict={
        "etage1": "TIENT", "prevol": True, "canon_sonde_etage1": c1})
    temoin("PORTE-2", "etage 2 REEL sous un verdict de pre-vol -> ferme (D-2)",
           code, arr, "(D-2)")
    code, arr = lancer("PORTE3", ["--etage", "2"], verdict={
        "etage1": "TIENT", "prevol": False, "canon_sonde_etage1": c1})
    temoin("PORTE-3", "etage 2 REEL sur un sonde_etage1.json de pre-vol (D-2)",
           code, arr, "(D-2)")
    code, arr = lancer("REPRISE", ["--etage", "1", "--retenus", a.retenus],
                       reprise=True)
    temoin("REPRISE", "etage 1 REEL dans une reprise de pre-vol -> refuse (D-1)",
           code, arr, "reprise refusee (D-1)")
    ok = (sum(R) == 6 and len(R) == 6 and base and all(T) and len(T) == 4)
    print("banc qui tue : %d mordues == 6 attendues ; base %s ; temoins hors"
          " gel : %d refus == 4 attendus : %s" % (
              sum(R), "saine" if base else "MALSAINE", sum(T),
              "PASSE" if ok else "ECHOUE"))
    sys.exit(0 if ok else 1)'''
b2 = b[:i0] + QUEUE + b[i1:]
B = [("B0 en-tete",
"# BANC QUI TUE DE LA QUALIFICATION E-B -- machine 1, v1 -- gel E-B v2\n",
"# BANC QUI TUE DE LA QUALIFICATION E-B -- machine 1, v2 -- gel E-B v2\n"
"# v2 = v1 (666e69f11bc1f72c) + D-3 (-P), temoins de D-1 et D-2, O-3.\n")]
b2 = appliquer(b2, B, "banc")
print("banc : queue remplacee (M-4, M-5, temoins), de l'ancre M-4 a la fin de main")
open(sys.argv[4], "wb").write(b2.encode("ascii"))
print("sonde v2 : canon %s, %d o ; remplacements %d == 14 attendus" % (canon_b(s2.encode()), len(s2), len(S)))
print("banc v2  : canon %s, %d o" % (canon_b(b2.encode()), len(b2)))
assert len(S) == 14
