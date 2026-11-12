# -*- coding: ascii -*-
# RELEVE DE L'ACTE journal_delta_nn_qualification_EB_v2.md PAR SA PLUME (machine 1).
# v2 = releve_acte_qualification_EB_machine1_v1.py (52e62eefe85e7d1a) + les hunks de
# construction_acte_v2_machine1_v1.py : le nom du v2, et C09, le controle qui manquait.
# Ce n'est pas un contreseing : c'est le controle de sortie de la redaction, par
# un code qui ne charge NI le script d'ecriture NI la feuille de lecture.
# Arguments : <acte> <sonde_etage1.json> <tp_reference.json> <script d'ecriture>
#             <registre> <journal> <racine de recherche> [<racine> ...]
import sys, os, re, json, hashlib, unicodedata, subprocess, tempfile
from fractions import Fraction

acte, nuit, table, ecrire, reg, journal = sys.argv[1:7]
racines = sys.argv[7:]
F = open(journal, "w", encoding="ascii", newline="\n")
BILAN = []


def dire(s):
    print(s, flush=True)
    F.write(s + "\n")


def controle(nom, ok, detail):
    BILAN.append(ok)
    dire("%s %-7s %s" % (nom, "TIENT" if ok else "MORD", detail))


def cB(octets):
    t = unicodedata.normalize("NFC", octets.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


brut = open(acte, "rb").read()
txt = brut.decode("ascii")
lignes = txt.split("\n")
dire("acte %s : canon %s, %d o, %d lignes" % (os.path.basename(acte), cB(brut), len(brut), len(lignes) - 1))

# C01 -- forme
ok = (txt.startswith("JOURNAL DELTA nn -- ") and txt.endswith("-- FIN journal_delta_nn_qualification_EB_v2 --\n")
      and "%" not in txt and "\r" not in txt and "\t" not in txt
      and max(len(l) for l in lignes) <= 100 and not any(l != l.rstrip() for l in lignes))
controle("C01", ok, "ASCII, LF, zero signe pour cent, titre, terminateur, %d colonnes au plus, aucune fin de ligne"
         " blanche" % max(len(l) for l in lignes))

# C02 -- sections nn.0 a nn.14 presentes, dans l'ordre, une fois
secs = [int(m) for m in re.findall(r"(?m)^nn\.(\d+) [A-Z]", txt)]
controle("C02", secs == list(range(15)), "sections %s" % secs)

# C03 -- toute empreinte de 16 hex citee est le canon B d'une piece detenue
index, n = {}, 0
for r in racines:
    for d, sub, fs in os.walk(r):
        sub[:] = [x for x in sub if x not in (".git", "__pycache__")]
        for f in fs:
            p = os.path.join(d, f)
            n += 1
            try:
                index.setdefault(cB(open(p, "rb").read()), []).append(p)
            except UnicodeDecodeError:
                pass
cites = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])", txt)))
non = [c for c in cites if c not in index]
controle("C03", not non, "%d empreintes distinctes citees, %d resolues en convention B sur %d fichiers parcourus ;"
         " non resolues : %s" % (len(cites), len(cites) - len(non), n, non))

# C04 -- le tableau Gamma / Gamma_ref, recalcule des fichiers bruts
s1 = json.load(open(nuit))
ref = {r["j"]: r for r in json.load(open(table))["balayage"]}


def serie(j, cfg):
    tr = s1["TP"]["j%02d" % j]["traj"]["F1" + cfg]
    out = {}
    for k in range(-2, 13):
        e = tr[str(k)]["etats"][0]
        out[k] = e["gamma"] if (e.get("suivi") and e.get("gamma") is not None and e["gamma"] > 1e-12) else None
    return out


attendu, lu = [], []
for a, b in ((-2, 6), (6, 13)):
    for j in (6, 8):
        for cfg in ("G20", "G30"):
            s = serie(j, cfg)
            attendu.append([("%.3f" % (s[k] / ref[j]["Gamma_ref"])) if s[k] is not None else "-" for k in range(a, b)])
rows = re.findall(r"(?m)^    j = (\d)  (G[23]0)       ?(.*)$", txt)
lu = [r[2].split() for r in rows]
controle("C04", lu == attendu and len(lu) == 8, "tableau de nn.6 : %d lignes, %d valeurs, identiques au recalcul" % (
    len(lu), sum(len(x) for x in lu)))

# C05 -- plateau du gel recalcule en rationnels exacts, contre le bloc de nn.5
ok, det = True, []
for j in (6, 8):
    for cfg in ("G20", "G30"):
        s = serie(j, cfg)
        best = None
        for k0 in range(-2, 9):
            v = [s[k] for k in range(k0, k0 + 5)]
            if any(x is None for x in v):
                continue
            mx, mn = Fraction(max(v)), Fraction(min(v))
            cand = (not (mx <= (1 + Fraction(1, 20)) * mn), mx / mn, k0)
            if best is None or cand < best:
                best = cand
        plat = not best[0]
        etal = "%.4f" % (float(best[1]) - 1.0)
        m = re.search(r"(?m)^  j = %d, .*\n(?:.*\n)?    %s : (PLATEAU|PAS DE PLATEAU).*etalement ([0-9.]+)" % (j, cfg), txt)
        bon = bool(m) and (m.group(1) == "PLATEAU") == plat and m.group(2) == etal
        ok = ok and bon
        det.append("j%d %s %s %s" % (j, cfg, "PLATEAU" if plat else "PAS DE PLATEAU", etal))
controle("C05", ok, " ; ".join(det))

# C06 -- le verdict ecrit est celui de la piece de machine 2
vm2 = json.load(open(os.path.join(os.path.dirname(nuit), "verdict_etage1.json")))
ok = ("VERDICT DE L'ETAGE 1 : %s, motifs %s." % (vm2["etage1"], " ; ".join("'%s'" % x for x in vm2["motifs"]))) in " ".join(txt.split())
controle("C06", ok, "verdict et motifs de verdict_etage1.json retrouves mot pour mot")

# C07 -- le registre est bien a la tete citee
tete = subprocess.run(["git", "-C", reg, "rev-parse", "--short=7", "HEAD"], capture_output=True, text=True).stdout.strip()
dist = subprocess.run(["git", "-C", reg, "rev-parse", "--short=7", "origin/main"], capture_output=True, text=True).stdout.strip()
controle("C07", tete == dist == "2ec6775" and txt.count("2ec6775") >= 3, "clone %s, origin/main %s" % (tete, dist))

# C08 -- l'ecriture est deterministe : rejouee dans un dossier neuf, meme octets
with tempfile.TemporaryDirectory() as d:
    sortie = os.path.join(d, "acte.md")
    args = [a for a in os.environ["ARGS_ECRIRE"].split("|")]
    r = subprocess.run([sys.executable, "-I", ecrire] + args + [sortie], capture_output=True, text=True)
    meme = r.returncode == 0 and open(sortie, "rb").read() == brut
controle("C08", meme, "script d'ecriture %s rejoue : acte identique a l'octet" % cB(open(ecrire, "rb").read()))



# C09 -- numeros et comptes des regles candidates sous (X), releves au registre (E-nn-1 a E-nn-3)
def regles(nom, debut, fin):
    t = open(os.path.join(reg, "journal", nom), encoding="utf-8").read()
    return [int(x) for x in re.findall(r"(?m)^  (\d{1,2})[. ] ", t.split(debut, 1)[1].split(fin, 1)[0])]


anc = [regles(nom, "\nnn.8 REGLES CANDIDATES", "\nnn.9 ") for nom in (
    "journal_delta_90_constante_A_v2.md", "journal_delta_91_constante_A_run_v2.md",
    "journal_delta_92_constante_A_second_ordre_v1.md", "journal_delta_93_constante_A_mesure_v2.md")]
anc.append(regles("POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md", "## 6. VERSE SOUS (X)", "## 7."))
deja = [x for l in anc for x in l]
neufs = [int(x) for x in re.findall(r"(?m)^  (\d{2}) \(m1", txt.split("\nnn.9 REGLES CANDIDATES", 1)[1].split("\nnn.10 ", 1)[0])]
MOTS = {"une": 1, "deux": 2, "trois": 3, "quatre": 4, "six": 6, "huit": 8, "dix-huit": 18, "vingt et une": 21,
        "vingt-deux": 22, "vingt-cinq": 25}
aplat = " ".join(txt.split())
par = re.search(r"Les ([a-z -]+?) precedentes \(([^)]*)\)", aplat)
somme = sum(MOTS[w] for w in re.findall(r"\b(huit|quatre|une|trois|deux|six)\b", par.group(2)))
dit = re.search(r"la revue \(X\), echue : ([a-z-]+) candidates", aplat).group(1)
ok = (deja == list(range(1, len(deja) + 1)) and neufs == list(range(len(deja) + 1, len(deja) + 1 + len(neufs)))
      and MOTS[par.group(1)] == somme == len(deja) and MOTS[dit] == len(deja) + len(neufs))
controle("C09", ok, "regles (X) : %d au registre (par piece %s) ; l'acte numerote %s, annonce '%s precedentes' pour une"
         " parenthese qui somme a %d, et '%s candidates'" % (len(deja), [len(l) for l in anc], neufs, par.group(1), somme, dit))

dire("BILAN : %d controles, %d morsure(s)" % (len(BILAN), BILAN.count(False)))
dire("-- FIN releve_acte_qualification_EB_machine1_v2 --")
sys.exit(0 if all(BILAN) else 1)
