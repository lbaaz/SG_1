# -*- coding: ascii -*-
# RELEVE DE L'ACTE E-B BIS, PROJET v2 -- controle de sortie de machine 1, PAS un contreseing.
# Arguments : <v1> <v2> <racine /home/claude> <journal>
import sys, os, re, hashlib, unicodedata, difflib
V1, V2, R, JOURNAL = sys.argv[1:5]
F = open(JOURNAL, "w", encoding="ascii", newline="\n"); BILAN = []
def dire(s):
    print(s); F.write(s + "\n")
def B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def chk(nom, ok, detail):
    BILAN.append(ok); dire("%s  %s  %s" % (nom, "TIENT" if ok else "MORD ", detail))
a = open(V1, encoding="ascii").read(); b = open(V2, encoding="ascii").read()
chk("C01", B(V1) == "c396a00095a0b9e3", "canon de la v1 lue : %s" % B(V1))
lg = [l for l in b.split("\n") if len(l) > 100]
chk("C02", all(ord(c) < 128 for c in b) and "%" not in b and not lg and b.rstrip("\n").endswith(
    "-- FIN journal_delta_nn_qualification_EB_bis_v2 --") and b.count("-- PROJET, VERSION 2\n") == 1,
    "ASCII, sans pour cent, 100 colonnes, ligne de version et ligne de fin de la v2 ; %d lignes" % (len(b.split("\n")) - 1))
la, lb = a.split("\n"), b.split("\n")
ops = [o for o in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes() if o[0] != "equal"]
moins = sum(o[2] - o[1] for o in ops); plus = sum(o[4] - o[3] for o in ops)
sections = []
for o in ops:
    s = "tete"
    for l in la[:o[1] + 1]:
        m = re.match(r"(nn\.\d+) ", l)
        if m: s = m.group(1)
    sections.append(s)
chk("C03", len(ops) == 8 and moins == 9 and plus == 28 and sections == ["tete", "nn.4", "nn.7", "nn.10", "nn.14", "nn.16", "nn.16", "nn.16"],
    "la v2 ne differe de la v1 qu'en %d endroits (-%d +%d lignes), sections %s" % (len(ops), moins, plus, " ".join(sections)))
attendu = {
 "2b211d51fb8eb3f0": B(R + "/lecture_nem/MANIFEST_lot_machine1_chaine_EA_par_etat_v1.txt"),
 "e58d01567a46b86a": B(R + "/lecture_nem/MANIFEST_lot_machine1_envoi_chaine_et_lectures_v1.txt"),
 "05f8eed219631f63": B(R + "/recu_contreseing_bis/MANIFEST_recu.txt"),
 "df01461fc9b2b099": B(R + "/recu_rejeu_chaine/MANIFEST_recu.txt"),
 "c396a00095a0b9e3": B(V1),
 "ff93d708547f8ec0": B(R + "/acte_bis/MANIFEST_lot_machine1_acte_qualification_EB_bis_v1.txt"),
}
neuves = sorted(set(re.findall(r"\b[0-9a-f]{16}\b", b)) - set(re.findall(r"\b[0-9a-f]{16}\b", a)))
chk("C04", neuves == sorted(attendu) and all(k == v for k, v in attendu.items()),
    "empreintes nouvelles citees par la v2 : %d, toutes recalculees de pieces detenues : %s" % (len(neuves), " ".join(neuves)))
src = open(R + "/lecture_nem/comparaison_par_etat_machine1_v1.py", encoding="utf-8").read()
chk("C05", "max |Gamma(H+)| = 1.330e-13" in a and src.count("1.33e-12") >= 1 and "1.330e-13 (nn.5)" in b,
    "le plancher 1.330e-13 est en nn.5 de la v1 ; le script du lot 2b211d51 seuille a 1.33e-12 (dix planchers)")
e1 = open(R + "/recu_contreseing_bis/lot/experience_O_BIS_2/experience_O_BIS_2.log", encoding="utf-8").read()
e2 = open(R + "/recu_contreseing_bis/lot/experience_O_BIS_2/experience_O_BIS_2_threads.log", encoding="utf-8").read()
so = open(R + "/recu_nuit_bis/lot/nuit_EB_bis/sortie/sonde_etage1.json", encoding="utf-8").read()
di = open(R + "/recu_diag/lot/diagnostic_TP_echelle_forte/diag_G30.json", encoding="utf-8").read()
d16 = re.search(r"A voie du diagnostic.*gamma = (\S+)", e1).group(1)
d4 = re.search(r"\('openblas', 4\)\] : gamma = (\S+)", e2).group(1)
d2 = re.search(r"\('openblas', 2\)\] : gamma = (\S+)", e2).group(1)
ok = (d16[:14] == "5.398020792141" and "5.39802079214111e-10" in so and d4[:14] == "5.378534999046"
      and "5.378534999046463e-10" in di and d2[:14] not in (d16[:14], d4[:14]))
chk("C06", ok, "O-BIS-2 : defaut %s = sonde de la nuit a 13 chiffres ; 4 fils %s = diagnostic a 13 chiffres ; 2 fils %s, autre" % (d16, d4, d2))
chk("C07", B(V2) == sys.argv[5] if len(sys.argv) > 5 else True, "canon de la v2 : %s" % B(V2))
dire("BILAN : %d controles, %d morsures" % (len(BILAN), BILAN.count(False)))
