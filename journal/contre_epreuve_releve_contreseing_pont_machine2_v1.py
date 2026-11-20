# -*- coding: ascii -*-
"""CONTRE-EPREUVE de MON releve de contreseing de l'acte du pont (releve_contreseing_acte_pont_machine2_v1.py) -- machine 2, 2026-11-18. Une alteration a la fois sur une COPIE de l'acte, chacune appliquee exactement une fois ;
le releve doit mordre sur le controle VISE. La copie intacte ne doit pas mordre. Le releve est copie (octet pour octet) dans un dossier temporaire neuf, pour que son JSON de sortie n'ecrase pas le mien.
Usage : py -3.11 -P contre_epreuve_releve_contreseing_pont_machine2_v1.py <releve.py> <acte.md> <dossier du run> <dossier lot_m1 de l'acte> <racine> <dossier temporaire NEUF>"""
import os
import shutil
import subprocess
import sys

RELEVE, ACTE, RUN, LOTA, RAC, TMP = sys.argv[1:7]
os.makedirs(TMP)
T0 = open(ACTE, 'rb').read().decode('ascii')
sc = os.path.join(TMP, 'releve_copie.py')
shutil.copyfile(RELEVE, sc)
assert open(sc, 'rb').read() == open(RELEVE, 'rb').read()
ALT = [
    ('une lettre accentuee', 'R01', 'nn.0 POSITION', 'nn.0 POSITION ' + chr(233)),
    ('une ligne trop longue', 'R01', 'nn.0 POSITION', 'nn.0 POSITION ' + 'x' * 100),
    ('la ligne de verdict', 'R02', 'VERDICT : (S) TENUE, (C) TENUE, (L) TOMBEE', 'VERDICT : (S) TENUE, (C) TENUE, (L) TENUE'),
    ('le pire ln R3 de MG3 (nn.3)', 'R03', '-0.0502 a x = 8            1.00', '-0.0501 a x = 8            1.00'),
    ('la part de tolerance de MG5', 'R03', 'x = 8            1.49', 'x = 8            1.48'),
    ('un compte reduit de PG4', 'R03', '0.449               0.441   1.576', '0.448               0.441   1.576'),
    ('les cellules tombees de (L)', 'R03', 'FAMILLE (L), le lisse : TOMBEE ; cellules lisibles 6 sur 6 ; tombees : MG3 MG4 MG5', 'FAMILLE (L), le lisse : TOMBEE ; cellules lisibles 6 sur 6 ; tombees : MG4 MG5'),
    ('le nombre de niveaux', 'R04', '1743 niveaux', '1744 niveaux'),
    ('la plus grande etendue', 'R04', 'entre absorbeurs\n  0.0034', 'entre absorbeurs\n  0.0035'),
    ('un ln R3 de la table (PG3 a x = 8)', 'R05', '-0.0089  +0.0025', '-0.0088  +0.0025'),
    ('un ln R2 de la table (PG5 a x = 8)', 'R05', '+0.0564', '+0.0565'),
    ('la liste hors tolerance', 'R06', 'MG5 a x = 7 et 8', 'MG5 a x = 8'),
    ('la borne a 4 |delta|', 'R06', 'il reste sous 0.0136', 'il reste sous 0.0130'),
    ('la chute de MG3', 'R06', '0.05024 pour 0.05', '0.05023 pour 0.05'),
    ('un ecart-type de groupe', 'R07', '0.090 / 0.072', '0.091 / 0.072'),
    ('la moyenne de groupe la plus loin de 1', 'R07', 'la\n  moyenne de groupe la plus loin de 1 vaut 0.9339', 'la\n  moyenne de groupe la plus loin de 1 vaut 0.9340'),
    ('l\'exces de (Q1) en erreurs', 'R08', 'soit -0.67 erreur', 'soit -0.66 erreur'),
    ('(Q3) de MG3', 'R08', 'MG3      1.0107              0.9946', 'MG3      1.0108              0.9946'),
    ('le regard apres lecture de MG3', 'R08', 'MG3 0.27 ;', 'MG3 0.28 ;'),
    ('une annonce du gel (L MG4)', 'R09', '0.80 TOMBE', '0.81 TOMBE'),
    ('le nombre d\'annonces contre le run', 'R09', 'Sur 24 annonces, 5 vont contre le run', 'Sur 24 annonces, 4 vont contre le run'),
    ('un canon de lot (gel partie 1)', 'R10', '55612644fc4ca279', '55612644fc4ca27a'),
    ('la duree du run', 'R10', 'huit de front, 11185 s', 'huit de front, 11184 s'),
    ('un canon de piece (journal du run)', 'R11', '229e47bceac1a1f7', '229e47bceac1a1f8'),
    ('le nombre de nombres rejoues', 'R12', '6211 nombres', '6212 nombres'),
    ('l\'ecart de la table de la chaine', 'R12', 'a 1.3e-09', 'a 1.4e-09'),
    ('(Q4) de MG3, absorbeur C', 'R13', '+0.00195', '+0.00196'),
    ('l\'ancienne tolerance', 'R14', 'les cellules MG3 MG4 MG5 tombent, les memes', 'les cellules MG4 MG5 tombent, les memes'),
    ('le nombre de la limite de MG3', 'R15', 'MG3 tombe pour 0.00024 de trop', 'MG3 tombe pour 0.00025 de trop'),
    ('une citation du gel', 'R16', '(L2) TOMBEE : l\'ordre 3 n\'ameliore pas', '(L2) TOMBEE : l\'ordre 3 n\'aggrave pas'),
]


def passe(texte, nom):
    p = os.path.join(TMP, nom)
    open(p, 'wb').write(texte.encode('utf-8'))      # utf-8 : l'alteration d'une lettre accentuee doit pouvoir s'ecrire
    r = subprocess.run([sys.executable, '-P', sc, p, RUN, LOTA, RAC], capture_output=True, text=True)
    mord = [l.split()[0] for l in r.stdout.split('\n') if ' : MORD' in l]
    return r.returncode, mord, r.stdout, r.stderr


rc, mord, out, err = passe(T0, 'intact.md')
print('copie intacte : %s' % ('0 morsure' if rc == 0 and not mord else 'MORSURE %s ; stderr %s' % (mord, err[-200:])))
intact_ok = (rc == 0 and not mord)
bad = 0 if intact_ok else 1
mordues = 0
for nom, cible, a, b in ALT:
    n = T0.count(a)
    if n != 1:
        print('%-42s : ALTERATION NON APPLICABLE (%d occurrences de %r)' % (nom, n, a[:40]))
        bad += 1
        continue
    rc, mord, out, err = passe(T0.replace(a, b), 'alteree.md')
    ok = cible in mord
    mordues += ok
    bad += (not ok)
    print('%-42s : %s par %s%s' % (nom, 'MORDUE' if ok else 'NON MORDUE', cible, '' if len(mord) == 1 and ok else ' (mordent : %s)' % (' '.join(mord) or 'aucun, stderr ' + err[-120:].replace('\n', ' '))))
print('CONTRE-EPREUVE DE MON RELEVE : %d alterations, %d mordues sur le controle vise ; copie intacte %s' % (len(ALT), mordues, 'sans morsure' if intact_ok else 'AVEC MORSURE'))
sys.exit(1 if bad else 0)
