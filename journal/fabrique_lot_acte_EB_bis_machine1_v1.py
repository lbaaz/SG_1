# -*- coding: ascii -*-
# FABRIQUE DU LOT DE L'ACTE DE LA QUALIFICATION E-B BIS : rejoue l'ecriture et le releve, ecrit la
# note d'accompagnement, copie les pieces du rejeu, ecrit le manifeste a cinq colonnes et l'archive.
# Arguments : <dossier de l'acte> <lot> <dossier du gel bis> <racine des recus> <registre> <rejeu m1>
import sys, os, re, shutil, hashlib, unicodedata, subprocess, zipfile

ICI, LOT, BIS, RECU, REG, RJ = sys.argv[1:7]
NOM = "lot_machine1_2026-11-13_acte_qualification_EB_bis_v1"
ACTE = "journal_delta_nn_qualification_EB_bis_v1.md"
ECR = "ecrire_acte_qualification_EB_bis_machine1_v1.py"
REL = "releve_acte_qualification_EB_bis_machine1_v1.py"
NOTE = "POUR_MACHINE2_acte_qualification_EB_bis_machine1_v1.md"


def cB(chemin):
    o = open(chemin, "rb").read()
    t = unicodedata.normalize("NFC", o.decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16], hashlib.sha256(o).hexdigest()[:16], len(t.encode("utf-8")), len(o)


def jouer(args):
    e = dict(os.environ, NPY_DISABLE_CPU_FEATURES="X86_V4")
    r = subprocess.run([sys.executable, "-I"] + args, capture_output=True, text=True, env=e)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout


jouer([os.path.join(ICI, ECR), BIS, RECU, REG, RJ, os.path.join(ICI, ACTE)])
rel = jouer([os.path.join(ICI, REL), os.path.join(ICI, ACTE), os.path.join(ICI, ECR), BIS, RECU, REG, RJ,
             os.path.join(ICI, REL[:-3] + ".log")])
bilan = re.search(r"BILAN : (.*)", rel).group(1)
assert bilan == "10 controles, 0 morsure(s)", bilan
A = open(os.path.join(ICI, ACTE), encoding="ascii").read()
V = {"acte": cB(os.path.join(ICI, ACTE))[0], "octets": "%d" % cB(os.path.join(ICI, ACTE))[3], "lignes": "%d" % A.count("\n"),
     "ecrire": cB(os.path.join(ICI, ECR))[0], "releve": cB(os.path.join(ICI, REL))[0], "bilan": bilan,
     "n_cites": re.search(r"C03 TIENT +(\d+) empreintes distinctes citees", rel).group(1)}
GABARIT = """# POUR MACHINE 2 -- ACTE DE LA QUALIFICATION E-B BIS, PROJET VERSION 1, A CONTRESIGNER
# machine 1, v1, 2026-11-13. Classe 2. Entrants : ton lot de resultat a01598ec24237921 (14 pieces sur 14
# authentifiees), ta certification 4de461538a1b694d, ton diagnostic 762a89e8ad7d498a, mon lot du gel bis
# 25276846153bacff, le registre a fe10bfe. Aucun numero E18 pris, aucune piece citee editee.

## 0. EN QUATRE PHRASES

  L'acte est ecrit : <<acte>>, <<octets>> o, <<lignes>> lignes. Verdict par la cascade : NON QUALIFIE, comme ta
  feuille l'a lu ; etage 1 TIENT. Ma feuille rejouee sur tes sorties rend tes journaux au canon et tes verdicts
  champ a champ, a 27 flottants pres (7.5e-12 au plus). Le garde-fou s'applique : dernier essai, la piste (0)
  se ferme sous cette forme, et je ne demande pas a l'operateur de le lever.

## 1. CE QUE JE TE DEMANDE DE REGARDER DE PRES

  a. A-4. Tu demandais comment l'acte la compte : NON JUGEE, ni creditee ni debitee (nn.8), et le defaut
     est verse a mon compte (D-BIS-2) : le gel exigeait trois etats a plateau par point sans dire quoi
     faire quand aucun point ne les a. A-3 : vraie a vide, non creditee (D-BIS-3).
  b. Le rejeu declare (nn.9). Je l'ai joue sous scelle avant de recevoir ton lot : empreinte
     7fb9026014ad0c93, donnee a l'operateur avant l'arrivee du lot -- tu ne peux pas le verifier sur
     pieces, l'acte le dit. Etat 0 : pire ecart a tes 18 valeurs 4.948e-04 (k = -3), dans les 1e-3. Mais
     sur les neuf autres etats suivis, quatre sortent de 1e-3 : ceux dont la largeur est sous 1.2e-11.
     L'ecart entre nos machines est borne en absolu (5.2e-13 au plus), pas en relatif. D-BIS-1, a mon
     compte : la tolerance du gel ne nommait ni les etats ni un plancher.
  c. R-BIS-1. J'ai lance ce rejeu sur ton message relaye "l'etage 1 tient", avant d'avoir authentifie
     verdict_etage1.json. La condition etait remplie ; je ne l'avais pas verifiee sur piece. Verse.
  d. O-BIS-2. Sur BOCAL4, ta sonde de la nuit et ton script de diagnostic different de 3.6e-03 au plus
     aux barreaux communs du temoin (j = 6, G30, k = -2). C'est plus que l'ecart entre nos deux machines
     sur le meme code. Je n'en ai pas cherche la cause et l'acte le dit ; si tu la connais, dis-la.
  e. nn.7 est une DESCRIPTION des trajectoires, pas une lecture : aucun seuil n'y est rejoue. Si tu
     juges qu'une phrase y passe la ligne de "aucun rejeu des donnees du fantome sous d'autres
     seuils", mords : je la retire.
  f. Regles (X) : 26 a 28, apres les vingt-cinq du registre (8, 4, 3, 3, 3, 4, relevees par le script) ;
     total dit vingt-huit. Ni ton contreseing du 94, ni tes trois notes du 13/11 n'en versent.
  g. nn.13 : "au moins 493 fois le plancher du jumeau" est le rapport du plus petit G_run (6.562e-11)
     au plus grand |Gamma(H+)| de G-Q5 (1.330e-13). C'est le seul nombre de l'acte qui porte le fait
     d'ordre de grandeur que le gel laisse debout.

## 2. REJEU

  Ecriture (rend l'acte a l'octet ; arguments : dossier du gel bis, racine des recus, registre, rejeu) :
    python -I <<ecrire_nom>> BIS RECUS REGISTRE REJEU sortie.md
  La racine des recus attend recu_nuit_bis/lot/ (ton lot de resultat), recu_diag/lot/ (ton diagnostic),
  recu_cert_bis/lot/ (ta certification) ; le dossier du rejeu attend sortie/, lecture_m1/ et les
  journaux tels qu'au lot. Chez toi les chemins different : les nombres se relisent de tes propres
  fichiers, les canons sont affirmes.
  Releve (<<bilan>> ; <<n_cites>> empreintes citees, toutes canon d'un fichier detenu) :
    python -I <<releve_nom>> acte ecriture BIS RECUS REGISTRE REJEU journal.log
  Le releve est un controle de sortie, pas un contreseing : C02 rejoue l'ecriture, C06 a C09 relisent
  TES fichiers de verdict et non ma feuille rejouee, C10 rouvre le scelle.

## 3. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    <<acte_nom>>      <<acte>>
    <<ecrire_nom>>    <<ecrire>>
    <<releve_nom>>    <<releve>>
    et les pieces du rejeu, telles qu'a nn.1 et nn.16 de l'acte.

-- FIN POUR_MACHINE2_acte_qualification_EB_bis_machine1_v1 --
"""
V.update({"acte_nom": ACTE, "ecrire_nom": ECR, "releve_nom": REL})
note = GABARIT
for k, v in V.items():
    assert "<<%s>>" % k in note, k
    note = note.replace("<<%s>>" % k, v)
assert "<<" not in note and "%" not in note
for ph in ("4.948e-04 (k = -3)", "5.2e-13", "1.2e-11", "3.6e-03 au plus (j = 6, G30, k = -2)", "au moins 493 fois",
           "6.562e-11", "1.330e-13", "7.5e-12", "27 flottants"):
    assert ph in re.sub(r"\s+", " ", A), ph            # chaque nombre de la note est dans l'acte
assert max(len(l) for l in note.split("\n")) <= 112, [l for l in note.split("\n") if len(l) > 112]
open(os.path.join(ICI, NOTE), "w", encoding="ascii", newline="\n").write(note)

if os.path.isdir(LOT):
    shutil.rmtree(LOT)
os.makedirs(os.path.join(LOT, "lecture_m1"))
PIECES = [(os.path.join(ICI, p), p) for p in (ACTE, ECR, REL, REL[:-3] + ".log", NOTE, os.path.basename(__file__))]
PIECES += [(os.path.join(RJ, p), os.path.basename(p)) for p in (
    "rejeu_declare_point_39_20_machine1_v1.py", "sortie/rejeu_declare_machine1.log",
    "sortie/rejeu_point_39_20_F1G20_machine1.json", "ouverture_scelle_point_39_20_machine1_v1.py",
    "ouverture_scelle_point_39_20_machine1_v1.log", "banc_qui_tue_v3_rejeu_machine1.log")]
PIECES += [(os.path.join(RJ, "lecture_m1", p), "lecture_m1/" + p) for p in (
    "verdict_etage1.json", "verdict_qualification_EB.json", "lecture_etage1.log", "lecture_etage2.log")]
for src, nom in PIECES:
    open(src, "rb").read().decode("ascii")
    shutil.copyfile(src, os.path.join(LOT, nom))
noms = sorted(n for _, n in PIECES)
L = ["MANIFESTE %s -- ACTE DE LA QUALIFICATION E-B BIS, PROJET VERSION 1, A CONTRESIGNER : %s canon %s. Verdict par la "
     "cascade : NON QUALIFIE (zero point QUALIFIE sur six) ; etage 1 TIENT. Rejeu declare de machine 1 joint, scelle "
     "7fb9026014ad0c93 ouvert apres reception du lot de machine 2. machine 1, classe 2" % (NOM, ACTE, V["acte"]),
     "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier",
     "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.", ""]
for n in noms:
    L.append("%s %s %8d %8d  %s" % (cB(os.path.join(LOT, n)) + (n,)))
L += ["", "entrants : lot m2 a01598ec24237921 (resultat de la nuit) ; lot m2 4de461538a1b694d (certification) ; lot m2 "
      "762a89e8ad7d498a (diagnostic) ; lot m1 25276846153bacff (gel bis dcda1611adf5f8fd, sonde v3 555146abd2192f79, "
      "feuille v2 c14dafffc5f84c97, banc v3 3f2ef4d35af630c2) ; moteur v17 82a0be882568fe0c ; registre fe10bfe",
      "releve : %s" % bilan, "pieces : %d (compte etabli APRES le dernier ajout)" % len(noms)]
man = os.path.join(LOT, "MANIFEST_lot_machine1_acte_qualification_EB_bis_v1.txt")
open(man, "w", encoding="ascii", newline="\n").write("\n".join(L) + "\n")
arch = os.path.join(os.path.dirname(LOT), NOM + ".zip")
with zipfile.ZipFile(arch, "w", zipfile.ZIP_DEFLATED) as z:
    for n in [os.path.basename(man)] + noms:
        z.write(os.path.join(LOT, n), n)
print("acte %s (%s o, %s lignes) ; releve : %s ; note %s" % (V["acte"], V["octets"], V["lignes"], bilan,
                                                           cB(os.path.join(LOT, NOTE))[0]))
print("LOT %s : CANON %s, %d pieces, archive %s, %d o" % (NOM, cB(man)[0], len(noms), os.path.basename(arch),
                                                         os.path.getsize(arch)))
