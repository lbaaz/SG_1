# -*- coding: ascii -*-
"""CONTRE-EPREUVE de ma verification des nombres -- machine 2, 2026-11-16. On corrompt le gel (copie, UNE chose a la fois, texte unique asserte), on relance verification_nombres_gel_machine2_v1.py sur chaque
copie ; le verificateur doit MORDRE, et sur le controle attendu. Un verificateur qui ne mord pas sur une corruption ne certifie rien.
Usage : py -3.11 -P contre_epreuve_nombres_gel_machine2_v1.py <gel.md> <dossier de travail (neuf)> <sortie.json> -- <arguments du verificateur apres le gel : table, retro, table retro, depot, feuille ter, ref ancres> <moteur> <bloc2> <script3>"""
import json
import os
import subprocess
import sys

GEL, TRAV, SORTIE = sys.argv[1:4]
i = sys.argv.index('--')
TABLE, RETRO, TRETRO, DEPOT, FTER, REFANC, MOTEUR, BLOC2, SCRIPT3 = sys.argv[i + 1:i + 10]
os.makedirs(TRAV, exist_ok=False)
gel = open(GEL, encoding='ascii').read()
MUT = [
    ('G01 section 3 : boite de N1 68 -> 69', 'N = 68   predits 11 / 11 /  0', 'N = 69   predits 11 / 11 /  0', 'N01'),
    ('G02 section 4.5 : 131 etats -> 132', 'retrouve les 131 etats de la note', 'retrouve les 132 etats de la note', 'N02'),
    ('G03 E-1 : 83 etats juges -> 84', 'aux 83 etats juges de e_bord < 0.7', 'aux 84 etats juges de e_bord < 0.7', 'N03'),
    ('G04 7.1 : plus grand de la classe [0.5, 0.7[ 0.0604 -> 0.0704', 'mediane 0.0385   plus grand 0.0604', 'mediane 0.0385   plus grand 0.0704', 'N04'),
    ('G05 7.1 : ln q3 de l ancre A2 +0.0374 -> +0.0474', 'ln q3 = +0.0374 et +0.0373', 'ln q3 = +0.0474 et +0.0373', 'N05'),
    ('G06 7.2 : k le plus grand 3.24 -> 3.34', 'vaut de 0.55 a 3.24, mediane 1.99', 'vaut de 0.55 a 3.34, mediane 1.99', 'N06'),
    ('G07 7.3 : plus grand e_bord vu 0.603 -> 0.653', "n'a e_bord au-dessus de\n    0.603.", "n'a e_bord au-dessus de\n    0.653.", 'N07'),
    ('G08 7.3 : marge de N1 1.15 -> 1.25', 'attente 0.0866  marge 1.15', 'attente 0.0866  marge 1.25', 'N08'),
    ('G09 7.3 : 3 etats a N1 -> 2 (et 5 -> 4)', '5 etats predits du domaine sont au-dela (3 a N1, 2 a BP)', '4 etats predits du domaine sont au-dela (2 a N1, 2 a BP)', 'N09'),
    ('G10 7.3 : l ordre 2 plus pres a 4 etats sur 11 -> 5', 'que l\'ordre 3 a 4 etats sur 11 : E2 y tomberait', 'que l\'ordre 3 a 5 etats sur 11 : E2 y tomberait', 'N10'),
    ('G11 section 6 : |ln(G3/G2)| de la ligne P jusqu a 0.019 -> 0.029', 'vaut de 0.014 a 0.019, du niveau', 'vaut de 0.014 a 0.029, du niveau', 'N11'),
    ('G12 section 12 : 149 etats -> 150', 'predisent 149 etats au-dessus', 'predisent 150 etats au-dessus', 'N12'),
    ('G13 section 3 : delta de BN -0.076 -> -0.086', 'BN  w2 = 481/250   delta -0.076', 'BN  w2 = 481/250   delta -0.086', 'N01'),
    ('G14 7.3 : e_bord maximal de BP 0.636 -> 0.736', 'e_bord 0.347 a 0.636', 'e_bord 0.347 a 0.736', 'N08'),
]
procs = []
for nom, a, b, att in MUT:
    assert gel.count(a) == 1, '%s : texte trouve %d fois : %r' % (nom, gel.count(a), a)
    d = os.path.join(TRAV, nom[:3])
    os.makedirs(d)
    g = os.path.join(d, 'gel_mute.md')
    open(g, 'w', encoding='ascii', newline='\n').write(gel.replace(a, b))
    log = open(os.path.join(d, 'verification.log'), 'w')
    p = subprocess.Popen([sys.executable, '-P', 'verification_nombres_gel_machine2_v1.py', MOTEUR, BLOC2, SCRIPT3, g, TABLE, RETRO, TRETRO, DEPOT, FTER, REFANC, os.path.join(d, 'sortie.json')],
                         stdout=log, stderr=subprocess.STDOUT, env=dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1'))
    procs.append((nom, att, d, p))
res = []
for nom, att, d, p in procs:
    code = p.wait()
    txt = open(os.path.join(d, 'verification.log')).read()
    mordus = sorted(set(l.split()[0] for l in txt.split('\n') if len(l.split()) > 1 and l.split()[1] == 'MORD'))
    ok = code != 0 and att in mordus
    res.append({'mutation': nom, 'attendu': att, 'code': code, 'controles_qui_mordent': mordus, 'tient': ok})
    print('%-72s attendu %-4s -> mordent %-14s %s' % (nom, att, mordus, 'MORD COMME ATTENDU' if ok else 'MUET OU AUTRE'), flush=True)
print('CONTRE-EPREUVE : %d corruptions, %d mordues comme attendu' % (len(res), sum(r['tient'] for r in res)))
json.dump(res, open(SORTIE, 'w'), indent=1)
sys.exit(0 if all(r['tient'] for r in res) else 1)
