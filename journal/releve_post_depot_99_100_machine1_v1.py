# Releve de machine 1 APRES les depots des deltas 99 et 100, sur clone neuf. Hors chaine, aucun calcul de physique.
# Lit le registre, ne l'ecrit pas ; n'execute aucune piece du registre ni d'un lot recu.
# Arguments : <clone> <base> <tete99> <tete100> <acte ter v1> <acte loi v1> <acte loi v2>
#             <manifeste lot m2 contreseing v1> <dossier extrait de ce lot> <sortie.json> <manifeste de lot (m1 ou m2)> ...
import sys, os, re, json, hashlib, unicodedata, subprocess
clone, base, t99, t100, a_ter, a_v1, a_v2, man_m2, dir_m2, sortie = sys.argv[1:11]
mans_m1 = sys.argv[11:]
ATTENDUS = {"ter": "751165a3eee613d9", "v1": "a3f7d5d6809dcfe5", "v2": "b205b14cdfc23ba3"}
def brut(b): return hashlib.sha256(b).hexdigest()[:16]
def cB(b):
    try: t = unicodedata.normalize("NFC", b.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    except UnicodeDecodeError: return None, None
    e = t.encode("utf-8"); return hashlib.sha256(e).hexdigest()[:16], len(e)
def git(*a): return subprocess.run(["git", "-C", clone] + list(a), capture_output=True, text=True, check=True).stdout
res = {}; mord = []
def chk(code, bon, texte):
    res[code] = {"tient": bool(bon), "texte": texte}
    if not bon: mord.append(code)
    print("%-5s %s %s" % (code, "TIENT" if bon else "MORD ", texte))
def note(code, texte):
    res[code] = {"note": texte}; print("%-5s NOTE  %s" % (code, texte))

# index du clone
idx_B = {}; idx_brut = {}; par_chemin = {}
for d, ds, fs in os.walk(clone):
    if ".git" in ds: ds.remove(".git")
    for f in fs:
        p = os.path.join(d, f); r = os.path.relpath(p, clone).replace(os.sep, "/")
        b = open(p, "rb").read(); e, tb = cB(b); br = brut(b)
        par_chemin[r] = (e, br, tb, len(b))
        if e: idx_B.setdefault(e, []).append(r)
        idx_brut.setdefault(br, []).append(r)

# D01-D02 : la suite des commits
tete = git("rev-parse", "--short=7", "HEAD").strip()
p100 = git("rev-parse", "--short=7", t100 + "^").strip(); p99 = git("rev-parse", "--short=7", t99 + "^").strip()
n100 = git("rev-list", "--count", t99 + ".." + t100).strip(); n99 = git("rev-list", "--count", base + ".." + t99).strip()
chk("D01", tete == t100 and p100 == t99 and p99 == base and n99 == "1" and n100 == "1",
    "tete %s ; %s <- %s <- %s ; un commit par delta (%s, %s)" % (tete, base, t99, t100, n99, n100))
def statuts(a, b):
    l = [x.split("\t") for x in git("diff", "--name-status", a, b).splitlines()]
    return l
s99 = statuts(base, t99); s100 = statuts(t99, t100)
chk("D02", all(x[0] == "A" for x in s99 + s100) and len(s99) == 210 and len(s100) == 277,
    "delta 99 : %d fichiers, tous ajoutes ; delta 100 : %d, tous ajoutes ; aucun fichier anterieur modifie ni retire" % (len(s99), len(s100)))
propre = git("status", "--porcelain").strip() == ""
chk("D03", propre, "clone neuf sans modification locale")

# D04 : les manifestes de depot
def manifeste_depot(rel):
    t = open(os.path.join(clone, rel), "rb").read().decode("utf-8")
    lignes = []
    for l in t.splitlines():
        c = l.split()
        if len(c) >= 5 and re.fullmatch(r"[0-9a-f]{16}", c[1] or "") and re.fullmatch(r"[0-9a-f]{16}", c[2] or "") and c[3].isdigit() and c[4].isdigit():
            lignes.append((c[0], c[1], c[2], int(c[3]), int(c[4])))
    m = re.search(r"pieces : (\d+)", t)
    return lignes, int(m.group(1)) if m else None
for num, rel, ajout in (("99", "journal/MANIFEST_DEPOT_delta99_machine2_v1.txt", s99), ("100", "journal/MANIFEST_DEPOT_delta100_machine2_v2.txt", s100)):
    lig, annonce = manifeste_depot(rel)
    bons = [x for x in lig if par_chemin.get(x[0]) == (x[1], x[2], x[3], x[4])]
    mauvais = [x[0] for x in lig if par_chemin.get(x[0]) != (x[1], x[2], x[3], x[4])]
    ajoutes = set(x[1] for x in ajout); listes = set(x[0] for x in lig)
    hors = sorted(ajoutes - listes); manquent = sorted(listes - ajoutes)
    chk("D04_" + num, len(lig) == annonce and not mauvais and not manquent,
        "manifeste de depot %s : %d lignes (annonce %s), %d au chemin, au canon, a l'empreinte brute et aux deux tailles ; en ecart : %s ; listees mais pas ajoutees par ce commit : %s"
        % (num, len(lig), annonce, len(bons), mauvais, manquent))
    note("D05_" + num, "ajoutes par le commit %s hors des lignes du manifeste (%d) : %s" % (num, len(hors), hors))

# D06 : les actes, octet pour octet contre mes originaux
for cle, rel, mien in (("ter", "journal/journal_delta_99_qualification_EB_ter_v1.md", a_ter),
                       ("v2", "journal/journal_delta_100_loi_largeur_ordre3_v2.md", a_v2),
                       ("v1", "journal/journal_delta_100_loi_largeur_ordre3_v1.md", a_v1)):
    br = open(os.path.join(clone, rel), "rb").read(); bm = open(mien, "rb").read()
    chk("D06_" + cle, br == bm and cB(br)[0] == ATTENDUS[cle] and cB(bm)[0] == ATTENDUS[cle],
        "%s : %d octets, identique octet pour octet a mon original (%s), canon %s (attendu %s)" % (rel, len(br), os.path.basename(mien), cB(br)[0], ATTENDUS[cle]))

# D07 : le perimetre des citations des deux actes deposes
def perimetre(cle, mien):
    t = open(mien, "rb").read().decode("utf-8")
    cit = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])", t)))
    res_f = [c for c in cit if c in idx_B]; non = [c for c in cit if c not in idx_B]
    return cit, res_f, non
perim = {}
for cle, mien in (("ter", a_ter), ("v2", a_v2)):
    cit, ok, non = perimetre(cle, mien); perim[cle] = {"citees": len(cit), "resolues": len(ok), "non_resolues": non}
    note("D07_" + cle, "acte %s : %d empreintes distinctes citees, %d resolues au registre par canon (fichier ou manifeste de lot), non resolues : %s" % (cle, len(cit), len(ok), non))

# D08 : les lots (les miens et deux de machine 2), piece par piece, par canon
lots = {}
for man in mans_m1:
    mb = open(man, "rb").read(); canon = cB(mb)[0]
    pcs = []
    for l in mb.decode("utf-8").splitlines():
        c = l.split()
        if len(c) == 5 and len(c[0]) == 16 and len(c[1]) == 16 and c[2].isdigit(): pcs.append((c[4], c[0], c[1]))
    auB = [p for p in pcs if p[1] in idx_B]; aubrut = [p for p in pcs if p[2] in idx_brut]
    abs_ = [p[0] for p in pcs if p[1] not in idx_B]
    autre_brut = [(p[0], idx_B[p[1]]) for p in pcs if p[1] in idx_B and p[2] not in idx_brut]
    lots[canon] = {"manifeste": os.path.basename(man), "pieces": len(pcs), "au_registre_par_canon": len(auB), "a_l_empreinte_brute": len(aubrut),
                   "manifeste_au_registre": canon in idx_B, "absentes": abs_, "au_canon_autre_brut": autre_brut}
    note("D08", "lot %s (%s) : %d pieces, %d au registre par canon, %d a l'empreinte brute ; manifeste au registre : %s ; absentes : %s"
         % (canon, os.path.basename(man).replace("MANIFEST_lot_", "").replace(".txt", ""), len(pcs), len(auB), len(aubrut), "oui" if canon in idx_B else "non", abs_))
    if autre_brut: note("D08b", "lot %s : au registre par canon mais sous d'autres octets que les miens : %s" % (canon, autre_brut))

# D09 : la normalisation CRLF -> LF du contreseing v1 de machine 2
mb = open(man_m2, "rb").read(); canon_m2 = cB(mb)[0]
diff_brut = []; pcs = 0; auB = 0; lf_ok = 0
for l in mb.decode("utf-8").splitlines():
    c = l.split()
    if len(c) == 5 and len(c[0]) == 16 and len(c[1]) == 16 and c[2].isdigit():
        pcs += 1
        if c[0] in idx_B:
            auB += 1
            if c[1] not in idx_brut:
                b = open(os.path.join(dir_m2, c[4]), "rb").read()
                lf = b.replace(b"\r\n", b"\n")
                ok = brut(lf) in idx_brut and b.count(b"\r\n") > 0
                lf_ok += ok
                diff_brut.append((c[4], b.count(b"\r\n"), "LF = registre" if ok else "AUTRE"))
chk("D09", auB == pcs and len(diff_brut) == lf_ok,
    "lot de machine 2 %s : %d pieces, %d au registre par canon ; %d different a l'empreinte brute, et pour chacune mes octets passes de CRLF en LF sont ceux du registre : %s"
    % (canon_m2, pcs, auB, len(diff_brut), diff_brut))

# D10 : gels et blocs par canon
for nom, canon in (("gel ter", "432319b9feb34b82"), ("gel loi partie 1", "b56ca5cb2dd25da1"), ("gel loi partie 2", "543d8b33e5c9afb8"),
                   ("bloc d'ordre 3", "534ba246aa3b8973"), ("bloc d'ordre 2", "7cd5977bc27bebc1"), ("feuille d'ordre 3", "facd3ceeec07d3bf"),
                   ("table des points", "35fa7b73f2b7f8eb"), ("verdict d'ordre 3", "87e9221cfc5f8f9b")):
    chk("D10", canon in idx_B, "%s %s au registre : %s" % (nom, canon, idx_B.get(canon)))

# D11 : le precedent du delta 98 -- le lot d'acte de machine 1 (manifeste et pieces) est au registre
PRECEDENT = "da1c2668d317b9d5"
chk("D11_98", PRECEDENT in idx_B, "precedent : le manifeste de mon lot d'acte du delta 98 (%s) est au registre : %s" % (PRECEDENT, idx_B.get(PRECEDENT)))
for canon, delta in (("26b3912297b31713", "99"), ("d9250297bf7d2f77", "100"), ("0a5741ff95e7136c", "100")):
    L = lots[canon]
    chk("D11_" + canon[:4], L["manifeste_au_registre"] and not L["absentes"],
        "delta %s : mon lot d'acte %s -- manifeste au registre : %s ; pieces au registre %d sur %d ; absentes : %d"
        % (delta, canon, "oui" if L["manifeste_au_registre"] else "non", L["au_registre_par_canon"], L["pieces"], len(L["absentes"])))
    cite = sorted(r for r, v in par_chemin.items() if canon.encode() in open(os.path.join(clone, r), "rb").read())
    note("D11n", "le canon %s est nomme par %d fichiers du registre et n'y repond a aucun" % (canon, len(cite)))
    lots[canon]["nomme_par"] = cite
# D12 : second niveau -- les empreintes citees par les gels deposes
for nom, canon in (("gel ter", "432319b9feb34b82"), ("gel loi partie 1", "b56ca5cb2dd25da1"), ("gel loi partie 2", "543d8b33e5c9afb8")):
    t = open(os.path.join(clone, idx_B[canon][0]), "rb").read().decode("utf-8")
    cit = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])", t)))
    non = [c for c in cit if c not in idx_B]
    perim[nom] = {"citees": len(cit), "non_resolues": non}
    note("D12", "%s %s : %d empreintes distinctes citees, non resolues au registre : %s" % (nom, canon, len(cit), non))

print("RELEVE APRES DEPOT : %d controles, %d mordent : %s" % (sum(1 for v in res.values() if "tient" in v) , len(mord), mord))
json.dump({"tete": tete, "controles": res, "perimetre": perim, "lots": lots, "mordent": mord}, open(sortie, "w"), indent=1, ensure_ascii=True, sort_keys=True)
