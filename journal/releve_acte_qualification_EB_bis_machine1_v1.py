# -*- coding: ascii -*-
# RELEVE DE L'ACTE DE LA QUALIFICATION E-B BIS -- controle de sortie de machine 1, PAS un contreseing.
# Chaque controle relit sa source par un chemin qui n'est pas celui du script d'ecriture quand c'est
# possible (les fichiers de verdict de machine 2, pas la feuille rejouee).
# Arguments : <acte> <script d'ecriture> <dossier du gel bis> <racine des recus> <registre> <rejeu m1> <journal>
import sys, os, re, json, math, hashlib, unicodedata, subprocess, tempfile
ACTE, ECRIRE, BIS, RECU, REG, RJ, JOURNAL = sys.argv[1:8]
F = open(JOURNAL, "w", encoding="ascii", newline="\n")
BILAN = []


def dire(s):
    print(s)
    F.write(s + "\n")


def cB(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def controle(nom, ok, detail):
    BILAN.append(ok)
    dire("%s %s  %s" % (nom, "TIENT" if ok else "MORD ", detail))


o = open(ACTE, "rb").read()
A = o.decode("ascii")
LG = A.split("\n")
N = re.sub(r"\s+", " ", A)
dire("RELEVE de %s, canon %s, %d o, %d lignes" % (os.path.basename(ACTE), cB(ACTE), len(o), A.count("\n")))
SO = RECU + "/recu_nuit_bis/lot/nuit_EB_bis/sortie/"
v1 = json.load(open(SO + "verdict_etage1.json"))
v2 = json.load(open(SO + "verdict_qualification_EB.json"))
s1 = json.load(open(SO + "sonde_etage1.json"))
s2 = json.load(open(SO + "sonde_etage2.json"))

# C01 forme
controle("C01", b"%" not in o and max(len(l) for l in LG) <= 100 and not any(l != l.rstrip() for l in LG)
         and A.rstrip().endswith("-- FIN journal_delta_nn_qualification_EB_bis_v1 --"),
         "ASCII, aucun signe pour cent, plus longue ligne %d, pas d'espace en fin de ligne, ligne de FIN" % max(len(l) for l in LG))
# C02 determinisme : le script d'ecriture rejoue rend l'acte a l'octet
tmp = os.path.join(tempfile.mkdtemp(), "acte.md")
r = subprocess.run([sys.executable, "-I", ECRIRE, BIS, RECU, REG, RJ, tmp], capture_output=True, text=True)
controle("C02", r.returncode == 0 and open(tmp, "rb").read() == o, "le script d'ecriture %s rejoue rend l'acte a l'octet" % cB(ECRIRE))
# C03 toute empreinte citee est le canon d'un fichier detenu
canons = {}
for racine in (BIS, RECU + "/recu_diag", RECU + "/recu_cert_bis", RECU + "/recu_nuit_bis", RJ, REG + "/journal",
               REG + "/gels", REG + "/scripts"):
    for d, _, fs in os.walk(racine):
        if "__pycache__" in d or "/.git" in d or "/reprise" in d:
            continue
        for f in fs:
            if f.endswith((".npy", ".zip", ".pyc", ".png")):
                continue
            try:
                canons.setdefault(cB(os.path.join(d, f)), f)
            except UnicodeDecodeError:
                pass
cites = sorted(set(re.findall(r"\b[0-9a-f]{16}\b", A)))
orph = [c for c in cites if c not in canons]
controle("C03", not orph, "%d empreintes distinctes citees, toutes canon d'un fichier detenu ; orphelines : %s" % (len(cites), orph))
# C04 regles (X)
def numeros(chemin, debut, fin, motif=r"(?m)^  (\d{1,2})[. ] "):
    sec = open(chemin, encoding="utf-8").read().split(debut, 1)[1].split(fin, 1)[0]
    return [int(x) for x in re.findall(motif, sec)]
J = REG + "/journal/"
par = [numeros(J + "journal_delta_90_constante_A_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 "),
       numeros(J + "journal_delta_91_constante_A_run_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 "),
       numeros(J + "journal_delta_92_constante_A_second_ordre_v1.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 "),
       numeros(J + "journal_delta_93_constante_A_mesure_v2.md", "\nnn.8 REGLES CANDIDATES", "\nnn.9 "),
       numeros(J + "POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md", "## 6. VERSE SOUS (X)", "## 7."),
       numeros(J + "journal_delta_94_qualification_EB_v2.md", "\nnn.9 REGLES CANDIDATES", "\nnn.10 ", r"(?m)^  (\d{2}) \(m[12]")]
anciens = [n for l in par for n in l]
neufs = [int(x) for x in re.findall(r"(?m)^  (\d{2}) \(m1", A.split("nn.11 REGLES CANDIDATES")[1].split("nn.12 ")[0])]
MOT = {"une": 1, "deux": 2, "trois": 3, "quatre": 4, "huit": 8}
pa = re.search(r"Les vingt-cinq precedentes \(([^)]*)\)", N)
somme = sum(MOT[w] for w in re.findall(r"\b(huit|quatre|une|trois|deux)\b", pa.group(1))) if pa else -1
controle("C04", anciens == list(range(1, 26)) and neufs == [26, 27, 28] and somme == 25
         and "la revue (X), echue : vingt-huit candidates" in N,
         "regles (X) : %d au registre (par piece %s) ; neuves %s ; parenthese sommee a %d ; total dit vingt-huit" % (
             len(anciens), [len(l) for l in par], neufs, somme))
# C05 verdicts
controle("C05", v1["etage1"] == "TIENT" and v2["verdict"] == "NON QUALIFIE" and "VERDICT DE L'ETAGE 1 : TIENT" in N
         and "VERDICT, par la cascade de la section 9 : NON QUALIFIE" in N and v1["prevol"] is False and v2["prevol"] is False,
         "etage 1 %s, verdict %s, relus des fichiers de machine 2 et retrouves dans l'acte" % (v1["etage1"], v2["verdict"]))
# C06 la table de l'etage 2, depuis le verdict de machine 2
NOMS = {"39_20": "1.95", "197_100": "1.97", "99_50": "1.98", "101_50": "2.02", "203_100": "2.03", "41_20": "2.05"}
ORD = ["F1G20", "F1G30", "F2G20", "F3G20", "F1GT"]
manq = []
for n, w in NOMS.items():
    p = v2["detail"]["points"][n]
    cel = ["%s %.4f %2d" % ({"PLATEAU": "PL", "PAS DE PLATEAU": "--"}[p["plateaux"][c]["statut"]], p["plateaux"][c]["etalement"],
                            p["plateaux"][c]["k0"]) for c in ORD]
    l = "  %s  %.3e  %s   %d" % (w, s2["points"][n]["G_run"], "   ".join(cel), len(p["echecs"]))
    if l not in LG or p["statut"] != "NON QUALIFIE":
        manq.append(w)
controle("C06", not manq, "six lignes de la table de nn.6 recalculees du verdict de machine 2 ; manquantes : %s" % manq)
# C07 le temoin
manq = []
for cle in ("j06", "j08"):
    for cfg in ("F1G20", "F1G30"):
        q = v1["detail"]["TP"][cle][cfg]
        l = "    %s : PLATEAU, k0 = %2d, etalement %.4f, Gamma_pl %.4e, |ln| %.4f contre %.4f : TIENT" % (
            cfg[2:], q["k0"], q["etalement"], q["Gamma_pl"], q["ecart_ln"], 0.05 + v1["detail"]["TP"][cle]["u_ref"])
        if l not in LG or not q["tient"]:
            manq.append(cle + cfg)
controle("C07", not manq and v1["detail"]["TN"] == "NON JOUE", "quatre lignes du temoin positif ; TN %s ; manquantes : %s" % (v1["detail"]["TN"], manq))
# C08 decomptes
c1, c2 = s1["comptes"], s2["comptes"]
n1 = c1["TP"]["joues"] + c1["TN"]["joues"] + c1["TN"]["sautes"] + c1["plancher"]["joues"]
n2 = c2["F1"]["joues"] + c2["formes"]["joues"] + c2["translation"]["joues"] + c2["ouverture"]["joues"]
controle("C08", n1 == 120 and n2 == 540 and "soit 120" in N and "soit 540 decompositions" in N,
         "etage 1 : %d ; etage 2 : %d" % (n1, n2))
# C09 annonces
a = v2["detail"]["annonces"]
pl = [n for n in NOMS if v2["detail"]["points"][n]["plateaux"]["F1G20"]["statut"] == "PLATEAU"]
ok = (a["A-1"] == "NON QUALIFIE" and a["A-2 (2.02 non qualifie)"] is True and a["A-3 (droite >= gauche)"] is True
      and a["A-4 (fluctuation d'etat dominante)"] is None and a["A-5 (kappa gauche > droite)"] is False
      and pl == ["39_20"] and v2["detail"]["points"]["39_20"]["plateaux"]["F1G20"]["k0"] == 0
      and v2["detail"]["points"]["39_20"]["M17_sur_plateau"] is True
      and all(x in N for x in ("Rendu : NON QUALIFIE", "2.02 n'est pas QUALIFIE : vrai", "NON JUGEE", "faux, tel que la feuille",
                               "vrai sur UN point (1.95, k0 = 0)", "vrai sur le meme UN point")))
controle("C09", ok, "A-1 a A-5 relues du verdict de machine 2, A-7 et A-8 comptees (plateau a F1G20 : %s)" % pl)
# C10 le scelle
X = json.load(open(RJ + "/sortie/rejeu_point_39_20_F1G20_machine1.json"))["traj"]
Y = s2["points"]["39_20"]["cfg"]["F1G20"]["traj"]
pire = max((abs(X[str(k)]["etats"][0]["gamma"] / Y[str(k)]["etats"][0]["gamma"] - 1.0), k) for k in range(-5, 13))
controle("C10", cB(RJ + "/sortie/rejeu_point_39_20_F1G20_machine1.json") == "7fb9026014ad0c93" and pire[0] <= 1e-3
         and ("pire ecart relatif a BOCAL4 %.3e (k = %d)" % pire) in N,
         "scelle 7fb9026014ad0c93 ; etat 0, pire ecart %.3e a k = %d, retrouve dans l'acte" % pire)
dire("BILAN : %d controles, %d morsure(s)" % (len(BILAN), BILAN.count(False)))
sys.exit(0 if all(BILAN) else 1)
