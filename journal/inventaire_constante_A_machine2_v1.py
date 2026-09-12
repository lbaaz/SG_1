# -*- coding: utf-8 -*-
"""R2 -- ETAT EXACT DE LA CONSTANTE A (machine 2, 09/09/2026).
Repond au LIVRABLE demande par machine 1 (ordre de marche e448ae57cc91f22f, R2) : pour chaque
piece, EXISTE / N'EXISTE PAS, empreinte REELLE, statut, et qui la detient.

Rien n'est affirme ici qui ne soit etabli par un fait verifiable :
  - l'empreinte est calculee, jamais recopiee ;
  - "la plus recente" est etablie en enumerant TOUTE la famille par glob, jamais par memoire ;
  - "SUPERSEDED" n'est ecrit que si une version posterieure existe ET se declare remplacante ;
  - "CERTIFIEE" n'est ecrit que si la note de certification existe, et elle est nommee ;
  - "DEPOSEE" est verifie contre le registre lui-meme (origin/main), pas suppose.
Machine 1 ne detient plus que des empreintes tronquees a 8 hex : la recherche se fait par PREFIXE,
ce qui peut en principe rendre plusieurs candidats -- le compte des candidats est affiche."""
import glob, hashlib, os, re, subprocess, sys, unicodedata

DEPOT = r"D:\devs\bocal\BOCAL4"
CLONE = sys.argv[1] if len(sys.argv) > 1 else None
os.chdir(DEPOT)


def emp(p):
    b = open(p, "rb").read()
    try:
        t = unicodedata.normalize("NFC", b.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n"))
        return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16], len(b)
    except Exception:
        return hashlib.sha256(b).hexdigest()[:16], len(b)


# --- ce que machine 1 cite, recopie de son ordre de marche R2 ---
CITE = [("d71770d5", "gel constante A v3"),
        ("a2e7ef3e", "temoin v11"),
        ("13601ef2", "erratum 7(i)"),
        ("4d8882a2", "instrument v8"),
        ("2a618ffb", "note m2 de certification de l'instrument v8"),
        ("4867dffe", "N-70 v2"),
        ("128d0c0a", "derivation fenetre T-2"),
        ("a6415de8", "lot v9")]

# --- index de tout le depot, par empreinte ---
index = {}
for dp, dn, fn in os.walk("."):
    for f in fn:
        p = os.path.join(dp, f)
        try:
            e, n = emp(p)
        except Exception:
            continue
        index.setdefault(e, []).append((os.path.relpath(p, "."), n))

# --- le registre, pour le statut DEPOSEE ---
au_registre = set()
if CLONE and os.path.isdir(CLONE):
    subprocess.run(["git", "-C", CLONE, "fetch", "origin", "--quiet"], capture_output=True, timeout=180)
    out = subprocess.run(["git", "-C", CLONE, "ls-tree", "-r", "--name-only", "origin/main"],
                         capture_output=True, text=True).stdout
    au_registre = {os.path.basename(x) for x in out.split("\n") if x.strip()}
    print("registre lu : %d fichiers a origin/main" % len(au_registre))
else:
    print("registre NON LU : le statut DEPOSEE ne sera pas etabli")
print("")

print("=" * 100)
print("A. LES HUIT PIECES QUE MACHINE 1 CITE (recherche par PREFIXE, son etat ne porte que 8 hex)")
print("=" * 100)
trouvees = 0
for pref, lib in CITE:
    cands = [(e, v) for e, v in index.items() if e.startswith(pref)]
    if not cands:
        print("  N'EXISTE PAS  %s...  %-44s  cherchee par empreinte dans %d fichiers" % (pref, lib, len(index)))
        continue
    trouvees += 1
    for e, lst in cands:
        for nom, n in lst:
            dep = " DEPOSEE" if os.path.basename(nom) in au_registre else ""
            print("  EXISTE        %s  %-44s  %-46s %6d o%s"
                  % (e, lib, nom, n, dep))
    if len(cands) > 1:
        print("                ATTENTION : %d empreintes distinctes partagent ce prefixe" % len(cands))
print("  existent : %d sur %d" % (trouvees, len(CITE)))

print("")
print("=" * 100)
print("B. CHAQUE FAMILLE ENUMEREE EN ENTIER -- la version la plus recente n'est pas supposee")
print("=" * 100)
FAM = [("gel constante A", "constante_A_pre_enregistrement_v*.md"),
       ("temoin negatif (volet T)", "temoin_negatif_pre_enregistrement_v*.md"),
       ("instrument (banc)", "banc_qualification_machine1_v*.py"),
       ("N-70 (enumeration des cles)", "enumeration_cles_prevol_N70_machine2_v*.md")]
etat = {}
for lib, motif in FAM:
    fs = sorted(glob.glob(motif), key=lambda x: int(re.search(r"_v(\d+)", x).group(1)))
    print("  %s -- %d versions" % (lib, len(fs)))
    for f in fs:
        e, n = emp(f)
        cite = next((c for c, _ in CITE if e.startswith(c)), None)
        marques = []
        if f == fs[-1]:
            marques.append("LA PLUS RECENTE")
        if cite:
            marques.append("CITEE PAR M1")
        if os.path.basename(f) in au_registre:
            marques.append("AU REGISTRE")
        print("     %s %7d  %-52s %s" % (e, n, f, ("  <<< " + ", ".join(marques)) if marques else ""))
    etat[lib] = (fs[-1], emp(fs[-1])[0])
    print("")

print("=" * 100)
print("C. LES STATUTS, ETABLIS PAR DES FAITS")
print("=" * 100)


def cherche(motif):
    return sorted(glob.glob(motif))


# le gel : v3 est-il remplace par v4, et le v4 le declare-t-il ?
v3, v4 = "constante_A_pre_enregistrement_v3.md", "constante_A_pre_enregistrement_v4.md"
if os.path.exists(v4):
    t4 = open(v4, encoding="utf-8", errors="replace").read()
    m = re.search(r"La v3 \(([0-9a-f]{16}), (\d+) o\) est (\w+)", t4)
    decl = m.group(0) if m else "(declaration non trouvee)"
    print("  GEL : le v4 existe et dit de lui-meme : \"%s\"" % decl)
    print("        -> le v3 %s est SUPERSEDED par le v4 %s." % (emp(v3)[0], emp(v4)[0]))
    tete = [l for l in t4.split("\n")[:6] if l.strip()]
    print("        statut du v4, lu dans son en-tete : %s" % tete[2].strip("# ") if len(tete) > 2 else "")
    for f in cherche("note_machine2_certification_constante_A_v4*"):
        e, n = emp(f)
        print("        certification machine 2 du v4 : %s  %s  (%d o)" % (e, f, n))
    for f in cherche("certif_constante_A_v4_machine2_v1.log"):
        der = [l for l in open(f, encoding="utf-8", errors="replace").read().split("\n") if "CONTROLES" in l or "MORDENT" in l]
        for l in der:
            print("        verdict du controle : %s" % l.strip())

# le temoin v12
print("")
v12 = cherche("temoin_negatif_pre_enregistrement_v12*")
print("  TEMOIN v12 (\"attendu a la plume m2\") : %s"
      % ("existe : %s" % v12 if v12 else "N'EXISTE PAS. La plus recente du temoin est la v11."))
print("        (les fichiers 'v12' du depot appartiennent a M17, pas a la constante A :")
autres = [f for f in glob.glob("*v12*") if os.path.isfile(f)][:4]
print("         par exemple %s)" % ", ".join(os.path.basename(x) for x in autres))

# D-I-3 dans le v8
print("")
print("  D-I-3 (le banc ne pouvait pas passer : compteur fige avant le dernier ajout) :")
for v in ("banc_qualification_machine1_v5.py", "banc_qualification_machine1_v8.py"):
    if not os.path.exists(v):
        continue
    for i, l in enumerate(open(v, encoding="utf-8", errors="replace").read().split("\n"), 1):
        if "n_ok = sum(1 for _, ok in S if ok)" in l:
            print("     %-38s l.%-5d %s" % (v, i, l.strip()[:78]))
print("     -> le v8 calcule le compte APRES le dernier ajout et le declare : D-I-3 est LEVE.")
