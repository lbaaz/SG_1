# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'rejeu de la chaine E-A par etat (hors chaine, classe 3)' -- manifeste + ZIP. 2026-11-13.
Usage : python -P fabrique_lot_rejeu_chaine_EA_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; les journaux de lancement portent six et trois codes 0 ; les chiffres cles de la note
(marges, etat lu, 0.499, 0.115, 1.160 0.865 0.611, predit/run, facteurs 28 a 312, ecarts des predictions) RELUS dans les journaux ;
les canons de CHAQUE piece recalcules et ecrits dans la section 7 de la note (gabarit @@PIECES@@) ; note ASCII ; le manifeste ne se
porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'chaine_EA_rejeu/'
NOM = 'lot_machine2_2026-11-13_rejeu_chaine_EA_par_etat_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_rejeu_chaine_EA_par_etat_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_rejeu_chaine_EA_par_etat_machine2_v1.md'
SELF = 'fabrique_lot_rejeu_chaine_EA_machine2_v1.py'
PTS = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']
PIECES = ([D + 'lancer_rejeu_chaine_EA_machine2_v1.py', D + 'journal_rejeu.log'] + [D + 'point_%s.log' % p for p in PTS] +
          [D + 'lancer_bissection_machine2_v1.py', D + 'journal_bissection.log'] + [D + 'bissection_%s.log' % p for p in ('39_20', '101_50', '41_20')] +
          [D + 'second_ordre_machine2.log', D + 'lire_m17_table_machine2.log', D + 'controle_quanta_machine2_v1.py',
           D + 'controle_quanta_machine2_v1.log', D + 'compare_rejeu_chaine_EA_machine2_v1.py', D + 'compare_rejeu_chaine_EA_machine2_v1.log',
           D + 'predictions_chaine_points_neufs_machine2.log', D + 'compare_predictions_machine2_v1.py',
           D + 'compare_predictions_machine2_v1.log', SELF])
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def lit(p):
    return open(os.path.join(ICI, p), encoding='utf-8', errors='replace').read()


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = lit(NOTE)
if '@@PIECES@@' in note:                       # les canons des pieces entrent dans la section 7 (gabarit)
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
for j, n in (('journal_rejeu.log', 6), ('journal_bissection.log', 3)):
    t = lit(D + j)
    if len(re.findall(r'code=0 ', t)) != n or re.search(r'code=[1-9]', t):
        arrets.append('%s : %d codes 0 attendus' % (j, n))
cmp_ = lit(D + 'compare_rejeu_chaine_EA_machine2_v1.log')
for x in ('1.0338', '1.0129', '1.0026', '1.0308', '1.0190', '1.0043', 'de 0.499 a 1.626 chez moi, de 0.499 a 1.642 chez machine 1',
          'plus grand ecart-type de J sur ces etats : 0.115', "('39/20', '(10,3)', 0.499)", 'complet / resonant : m2 1.160', 'm2 0.865',
          'm2 0.611', 'ecart relatif max 9.41e-04', 'ecart relatif max 1.32e-03', 'plus grand ecart absolu Gamma_2D, tous les etats : 1.00e-13'):
    if x not in cmp_:
        arrets.append('le journal de comparaison ne porte pas %r' % x)
for x in ('1.0338', '0.499', '0.115', '1.160', '0.865', '0.611', '9.4e-04', '1.3e-03'):
    if x not in note:
        arrets.append('la note ne porte pas %s' % x)
q = lit(D + 'controle_quanta_machine2_v1.log')
pr = [float(m.group(1)) for m in re.finditer(r'\s([0-9]\.[0-9]{2})\s*$', q, re.M)]
if pr != [1.00, 1.03, 1.05, 1.10, 1.14, 0.96]:
    arrets.append('predit/run lu %s, la note dit 1.00 1.03 1.05 1.10 1.14 0.96' % pr)
for x in ('28.43', '47.03', '62.04', '220.12', '312.45', '29.28'):
    if x not in lit(D + 'lire_m17_table_machine2.log') or x not in note:
        arrets.append('facteur %s absent du journal ou de la note' % x)
cp = lit(D + 'compare_predictions_machine2_v1.log')
for x in ('36 largeurs, ecart relatif max 8.49e-05', '38 largeurs, ecart relatif max 1.41e-03', 'plus grand ecart absolu : 1.00e-13'):
    if x not in cp:
        arrets.append('le journal des predictions ne porte pas %r' % x)
so = lit(D + 'second_ordre_machine2.log')
if '1.098 -> 0.785' not in so or '0.583 a 1.838' not in so or '0.583 a 1.838' not in note:
    arrets.append('second ordre : 1.098 -> 0.785 ou 0.583 a 1.838 absent du journal ou de la note')
for canon in ('4eaef82543e4f76f', '7cb9dcf62eccf90b', 'b347c0edb9af04d0', '85ba4aba558377c2', '3b09ad4a0cdfc0c4', 'aa74f6fcaeff6a73',
              '2b211d51fb8eb3f0', 'e58d01567a46b86a', '82a0be882568fe0c'):
    if canon not in note:
        arrets.append('la note ne nomme pas le canon %s' % canon)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- REJEU PAR MACHINE 2 DE LA CHAINE E-A CONTRE E-B ETAT PAR ETAT (lots de machine 1 2b211d51fb8eb3f0 et '
    'e58d01567a46b86a ; moteur v17 82a0be882568fe0c). HORS CHAINE, CLASSE 3, NON OPPOSABLE, NON CONTRESIGNE. Memes etats lus aux six '
    'points ; une regle de morsure (borne 0.50) mord a la lettre sur les deux machines ; une phrase de la note mordue ; aucun gel '
    'certifie. machine 2\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 2b211d51fb8eb3f0 (12 pieces) ; lot de machine 1 e58d01567a46b86a (10 pieces) ; moteur v17 '
              '82a0be882568fe0c ; mon dossier du run manche_m17_v17\n')
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % (len(PIECES) + 1))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for p in [NOTE] + PIECES:
        z.write(os.path.join(ICI, p), p)
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for p in [NOTE] + PIECES:
        attendu[p] = open(os.path.join(ICI, p), 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP)))
