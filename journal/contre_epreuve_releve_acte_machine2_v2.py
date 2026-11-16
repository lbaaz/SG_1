# -*- coding: ascii -*-
"""CONTRE-EPREUVE de mon releve du contreseing de la VERSION 2 (derivee de contre_epreuve_releve_acte_machine2_v1.py, NON EDITEE ; diff joint) -- machine 2, 2026-11-16. On corrompt une COPIE de l'acte (UNE chose a la fois, texte unique asserte, retours a la ligne tolerees), on relance
releve_contreseing_acte_gel_loi_machine2_v2.py sur chaque copie ; le releve doit MORDRE, et sur le controle attendu (qui ne mordait pas sur l'acte tel quel). Un releve qui ne mord pas sur une corruption ne certifie rien.
Une 'correction' fait l'inverse : un controle qui mord sur l'acte tel quel doit cesser de mordre quand on corrige le texte.
Usage : py -3.11 -P contre_epreuve_releve_acte_machine2_v1.py <acte.md> <dossier de travail (neuf)> <sortie.json> <controles qui mordent sur l'acte tel quel, separes par des virgules>"""
import json
import os
import re
import subprocess
import sys

ACTE, TRAV, SORTIE, BASE = sys.argv[1:5]
BASE = set(x for x in BASE.split(',') if x)
os.makedirs(TRAV, exist_ok=False)
raw = open(ACTE, encoding='ascii', newline='').read().replace('\r\n', '\n')
MUT = [  # (nom, texte, remplacement, genre, controle)
    ('M01 tableau : |ln q3| de N1 0.0740 -> 0.0840', '|ln q3| 0.0740 marge +0.0260', '|ln q3| 0.0840 marge +0.0260', 'corruption', 'R05N1'),
    ('M02 chronologie : 19 appels -> 18', '19 appels, tous au code 0', '18 appels, tous au code 0', 'corruption', 'R03a'),
    ('M03 chronologie : duree 6166 -> 6176 s', 'duree totale 6166 s ; 19', 'duree totale 6176 s ; 19', 'corruption', 'R03a'),
    ('M04 empreinte du verdict d ordre 3 : dernier chiffre', '87e9221cfc5f8f9b verdict d\'ordre 3 du run', '87e9221cfc5f8f9c verdict d\'ordre 3 du run', 'corruption', 'R02a'),
    ('M05 BP : 0.099617 -> 0.099717', 'vaut 0.099617 pour T = 0.10', 'vaut 0.099717 pour T = 0.10', 'corruption', 'R07d'),
    ('M06 delta > 0 : 784 -> 774', 'ln q3 / delta^3 atteint 784', 'ln q3 / delta^3 atteint 774', 'corruption', 'R10b'),
    ('M07 delta > 0 : 15 etats sur 62 -> 14', 'ancien maximum a 15 etats sur 62', 'ancien maximum a 14 etats sur 62', 'corruption', 'R10b'),
    ('M08 signes : 58 sur 60 -> 59', 'negatif a 58 etats sur 60', 'negatif a 59 etats sur 60', 'corruption', 'R09a'),
    ('M09 annonce A-6 BN : 0.65 -> 0.55', 'BN tient (annonce 0.65)', 'BN tient (annonce 0.55)', 'corruption', 'R11a'),
    ('M10 phrase autorisee : 0.05 pres -> 0.06 pres', 'a 0.05 pres en logarithme (e_bord < 0.3)', 'a 0.06 pres en logarithme (e_bord < 0.3)', 'corruption', 'R12a'),
    ('M11 rejeu : 1.6e-09 -> 1.7e-09 sur ln q3', '141 etats juges : 1.6e-09 sur ln q3', '141 etats juges : 1.7e-09 sur ln q3', 'corruption', 'R14a'),
    ('M12 lecteur : plateau 142 -> 143 sur 144', 'sur le plateau a 142 etats sur 144', 'sur le plateau a 143 etats sur 144', 'corruption', 'R04a'),
    ('M13 O-1 : 0.16338 -> 0.16438', 'Le plus grand est 0.16338', 'Le plus grand est 0.16438', 'corruption', 'R13a'),
    ('M14 E1 lignes : 117 etats -> 116', 'Aux dix cellules de ligne, 117 etats', 'Aux dix cellules de ligne, 116 etats', 'corruption', 'R07a'),
    ('M15 etiquettes : 132 -> 133', 'Etiquettes : 132 des 144', 'Etiquettes : 133 des 144', 'corruption', 'R09d'),
    ('M16 hors domaine : e_bord 0.489 -> 0.499', 'de e_bord 0.489 a 0.711', 'de e_bord 0.499 a 0.711', 'corruption', 'R09b'),
    ('M17 exclus : N5 rang 13 -> 14', 'N3 rang 12, N5 rang 13, BN rang 13', 'N3 rang 12, N5 rang 14, BN rang 13', 'corruption', 'R06a'),
    ('M18 garde e_bord : BP rang 5 -> 6', 'a e_bord = 0.7 (BP rang 5)', 'a e_bord = 0.7 (BP rang 6)', 'corruption', 'R07e'),
    ('M19 au-dela de 0.603 : N1 rang 1 -> 2', '(N1 rang 1, N1 rang 3, BP rang 1', '(N1 rang 2, N1 rang 3, BP rang 1', 'corruption', 'R10g'),
    ('M20 lecteur rejoue : 7.3e-15 -> 7.4e-15', 'plus grand ecart relatif : 7.3e-15', 'plus grand ecart relatif : 7.4e-15', 'corruption', 'R14b'),
    ('M21 attente de P1 : 0.0336 -> 0.0236', '0.0336 a P1 pour une attente de 0.0211', '0.0236 a P1 pour une attente de 0.0211', 'corruption', 'R10d'),
    ('M22 deltas : -0.065 -> -0.055', 'delta = -0.065, cinq a delta = +0.035', 'delta = -0.055, cinq a delta = +0.035', 'corruption', 'R15a'),
    ('M23 P1 P2 : 13 predits -> 14', '(12 et 13 predits dans le domaine)', '(12 et 14 predits dans le domaine)', 'corruption', 'R15b'),
    ('M24 aux cellules : N4 ln q2 0.0747 -> 0.0847', '|ln q3| 0.0208 marge +0.0422 |ln q2| 0.0747', '|ln q3| 0.0208 marge +0.0422 |ln q2| 0.0847', 'corruption', 'R05N4'),
    ('M25 canon du lot de resultat : 54ccae1713f92bc9 -> ...c', '54ccae1713f92bc9 lot de machine 2 : resultat du run', '54ccae1713f92bca lot de machine 2 : resultat du run', 'corruption', 'R02a'),
    ("M27 rien regle apres lecture : phrase alteree", "Aucun seuil, aucune garde, aucune tolerance n'a ete regle apres lecture", "Un seuil, aucune garde, aucune tolerance n'a ete regle apres lecture", 'corruption', 'R12c'),
    ("M28 precision sur BP : 0.0026 -> 0.0025 (mon propre arrondi de la v1, faux : le rang 1 est a +0.002524)", 'sont a moins de 0.0026 de la tolerance', 'sont a moins de 0.0025 de la tolerance', 'corruption', 'R16a'),
    ('M29 precision sur BP : 6.2 fois la marge -> 6.9', 'soit 6.2 fois la marge', 'soit 6.9 fois la marge', 'corruption', 'R16a'),
    ('M30 feu vert : 00 h 54 -> 01 h 00', 'le 16/11 a 00 h 54 (heure', 'le 16/11 a 01 h 00 (heure', 'corruption', 'R16b'),
    ('M31 retouches : 67 tenus -> 66', '68 controles, 67 tenus, une morsure de description. Trois retouches', '68 controles, 66 tenus, une morsure de description. Trois retouches', 'corruption', 'R16c'),
    ('M32 hors du diff annonce : un mot ajoute en nn.0', 'Ce delta rend le run unique du gel', 'Ce delta rend le run unique, joue, du gel', 'corruption', 'R17'),
    ('M33 hors du diff annonce : un mot ajoute en nn.7', 'Annonces (gel, section 10). A-1', 'Annonces (gel, section 10, relues). A-1', 'corruption', 'R17'),
]


def flex(a):
    return r'\s+'.join(re.escape(w) for w in a.split())


procs = []
base = os.path.join(TRAV, 'base')
os.makedirs(base)
open(os.path.join(base, 'acte.md'), 'w', encoding='ascii', newline='\n').write(raw)
procs.append(('base', None, base, 'reference', subprocess.Popen([sys.executable, '-P', 'releve_contreseing_acte_gel_loi_machine2_v2.py', os.path.join(base, 'acte.md'), os.path.join(base, 'sortie.json')],
                                                              stdout=open(os.path.join(base, 'releve.log'), 'w'), stderr=subprocess.STDOUT)))
for nom, a, b, genre, att in MUT:
    n = len(re.findall(flex(a), raw))
    assert n == 1, '%s : texte trouve %d fois : %r' % (nom, n, a)
    d = os.path.join(TRAV, nom[:3])
    os.makedirs(d)
    g = os.path.join(d, 'acte_mute.md')
    open(g, 'w', encoding='ascii', newline='\n').write(re.sub(flex(a), lambda m: b, raw))
    procs.append((nom, att, d, genre, subprocess.Popen([sys.executable, '-P', 'releve_contreseing_acte_gel_loi_machine2_v2.py', g, os.path.join(d, 'sortie.json')],
                                                       stdout=open(os.path.join(d, 'releve.log'), 'w'), stderr=subprocess.STDOUT)))
res = []
for nom, att, d, genre, p in procs:
    code = p.wait()
    txt = open(os.path.join(d, 'releve.log')).read()
    mordus = sorted(set(l.split()[0] for l in txt.split('\n') if len(l.split()) > 1 and l.split()[1] == 'MORD'))
    complet = 'RELEVE DU CONTRESEING' in txt
    if genre == 'reference':
        print('%-72s mordent %s %s' % (nom, mordus, 'COMPLET' if complet else 'INCOMPLET'), flush=True)
        res.append({'mutation': nom, 'genre': genre, 'controles_qui_mordent': mordus, 'tient': complet and set(mordus) == BASE})
        continue
    if genre == 'corruption':
        ok = complet and att in mordus and att not in BASE
        verdict = 'MORD COMME ATTENDU' if ok else 'MUET OU AUTRE'
    else:
        ok = complet and att in BASE and att not in mordus and set(mordus) == BASE - {att}
        verdict = 'CESSE DE MORDRE COMME ATTENDU' if ok else 'INCHANGE OU AUTRE'
    res.append({'mutation': nom, 'genre': genre, 'attendu': att, 'code': code, 'controles_qui_mordent': mordus, 'tient': ok})
    print('%-72s attendu %-6s -> mordent %-22s %s' % (nom, att, mordus, verdict), flush=True)
print('CONTRE-EPREUVE : %d essais, %d comme attendu' % (len(res), sum(r['tient'] for r in res)))
json.dump(res, open(SORTIE, 'w'), indent=1)
sys.exit(0 if all(r['tient'] for r in res) else 1)
