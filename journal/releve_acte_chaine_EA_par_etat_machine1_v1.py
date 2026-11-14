# -*- coding: ascii -*-
# RELEVE DE L'ACTE DE LA CHAINE E-A PAR ETAT -- controle de sortie de machine 1, PAS un contreseing.
# Il relit l'acte contre des pieces que le script d'ecriture n'a PAS lues pour ces nombres : le journal de lecture
# rendu par machine 2, son journal de la garde G-1, sa note de resultat. Arguments : <acte> <recu> <gel_chaine> <journal>
import sys, os, re, hashlib, unicodedata
ACTE, RECU, GEL, JOURNAL = sys.argv[1:5]
F = open(JOURNAL, "w", encoding="ascii", newline="\n"); BILAN = []
def dire(x):
    print(x); F.write(x + "\n")
def chk(nom, ok, detail):
    BILAN.append(bool(ok)); dire("%s  %s  %s" % (nom, "TIENT" if ok else "MORD ", detail))
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def lire(p):
    return open(p, encoding="utf-8").read().replace("\r\n", "\n")
a = lire(ACTE)
LR = RECU + "/lots/lot_machine2_2026-11-14_resultat_chaine_EA_par_etat_v1/"
LC = RECU + "/lots/lot_machine2_2026-11-14_certification_gel_chaine_EA_par_etat_v1/"
chk("C01", all(ord(c) < 128 for c in a) and "%" not in a and max(len(l) for l in a.split("\n")) <= 100
    and a.rstrip("\n").endswith("-- FIN journal_delta_nn_chaine_EA_par_etat_v1 --"),
    "ASCII, sans pour cent, 100 colonnes, ligne de fin ; %d lignes, canon %s" % (len(a.split("\n")) - 1, B(ACTE)))
# C02 : le tableau de nn.4 contre le journal de lecture rendu par machine 2
vus = 0; manque = []
for l in lire(LR + "chaine_EA_par_etat/sortie/lecture_chaine_par_etat.log").split("\n"):
    m = re.match(r"\s+(\w\d) (\w+)\s+w2=(\d+)/(\d+) x(\d+)/(\d+) : (.+?)\s+(\d+) etats juges, q de ([\d.]+) a ([\d.]+), mediane ([\d.]+) ; "
                 r"premier juge \((\d+),(\d+)\) q = ([\d.]+)", l)
    if not m:
        continue
    pid, role, wn, wd, fn, fd, st, n, q0, q1, qm, n1, n2, qp = m.groups()
    fac = "1" if fn == fd else "%s/%s" % (fn, fd)
    ligne = "  %-5s  %-6s  %.2f  x%-5s  %-12s  %2d     %-7s  %-7s  %-7s  (%s,%s) q = %s" % (
        pid, role, int(wn) / int(wd), fac, st, int(n), q0, q1, qm, n1, n2, qp)
    vus += 1
    if ligne not in a:
        manque.append(pid)
chk("C02", vus == 12 and not manque, "les 12 lignes du tableau nn.4 se recomposent du journal de machine 2 ; absentes : %s" % manque)
# C03 : la table de la garde G-1 contre le journal de machine 2
vus = 0; manque = []
for l in lire(LC + "chaine_EA_par_etat/garde_G1_domaine_machine2_v1.log").split("\n"):
    m = re.match(r"([JTA]\d)\s+w2=\S+\s+x\S+\s+D1=([\d.]+) .* c_max=([\d.]+) .* -> (.+)$", l)
    if m:
        vus += 1
        if not re.search(r"  %s     %s  %s  %-15s  \S" % (m.group(1), m.group(2), m.group(3), m.group(4).strip()), a):
            manque.append(m.group(1))
chk("C03", vus == 12 and not manque, "les 12 lignes de la garde G-1 (nn.7) sont celles du journal de machine 2 ; absentes : %s" % manque)
# C04 : les annonces contre la note de machine 2
note = lire(LR + "POUR_MACHINE1_resultat_chaine_EA_par_etat_machine2_v1.md")
ok = True; det = []
for k in range(1, 9):
    m2 = re.search(r"A-%d \([\d.]+\)\s+.*?: (REALISEE|VRAIE|FAUSSE)" % k, note)
    m1 = re.search(r"  A-%d  \([\d.]+\)  .*?(REALISEE|VRAIE|FAUSSE)" % k, a)
    ok = ok and m1 is not None and m2 is not None and m1.group(1) == m2.group(1); det.append(m1.group(1) if m1 else "?")
chk("C04", ok and det.count("FAUSSE") == 1 and det[3] == "FAUSSE", "les huit annonces ont le sort que machine 2 leur donne : %s" % " ".join(det))
# C05 : les empreintes citees se resolvent
cites = sorted(set(re.findall(r"\b[0-9a-f]{16}\b", a)))
connus = set()
for racine, _, fs in list(os.walk(RECU)) + list(os.walk(GEL)) + list(os.walk(os.path.dirname(os.path.abspath(ACTE)))) + \
        list(os.walk("/home/claude/acte_bis_v2")) + list(os.walk("/home/claude/reponse_chaine")) + list(os.walk("/home/claude/lecture_nem")):
    for f in fs:
        if f.endswith((".zip", ".pyc")):
            continue
        try:
            connus.add(B(os.path.join(racine, f)))
        except Exception:
            pass
connus.add(B("/home/claude/lbaaz/sg_1/scripts/m17_chaine_v17.py"))
nr = [x for x in cites if x not in connus]
chk("C05", not nr, "%d empreintes citees, toutes recalculees de pieces detenues ; non resolues : %s" % (len(cites), nr))
# C06 : comptes
chk("C06", "131 etats juges sur 168" in a and "chacun des 44 etats" in a and "131 etats juges" in note,
    "131 etats juges sur 168 (note de machine 2 : 131) ; 44 aux quatre points FACTEUR 2")
chk("C07", "VERDICT DE TA FEUILLE = TENU EN PARTIE" in note and "VERDICT : TENU EN PARTIE" in a, "le verdict de l'acte est celui de la note de machine 2")
dire("BILAN : %d controles, %d morsures" % (len(BILAN), BILAN.count(False)))
