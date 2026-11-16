# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'certification du gel loi de la largeur ordre 3, premiere partie, ma table, la table commune' -- manifeste + ZIP. 2026-11-15. Derive de
fabrique_lot_evaluateur_tirage_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_certification_gel_loi_partie1_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; les bilans des quatre passages LUS dans leurs JSON (second passage : 9 controles, 0 morsure ; premier passage : C08 seul ; copie mutee : 9 sur 9) ; mon journal
d'eligibilite lu (152 cellules, 0 difference, 2128 drapeaux, 0 desaccord, table commune) ; mes tirages lus ; ma table et la table commune relues (format de la section 5, comptes 9, 18, 8, 9) ; le gel et le
lot de machine 1 RECALCULES depuis les fichiers recus ; le moteur, le bloc d'ordre 2 et mon script de tirage recalcules ; les chiffres de la note presents ; les canons de CHAQUE piece nommes dans la note ; note
ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-15_certification_gel_loi_partie1_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_loi_partie1_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_loi_partie1_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_loi_partie1_machine2_v1.py'
D = 'controle_carte_machine2/'
V = D + 'verification_gel_loi_partie1_machine2_v1'
REG = r'C:/Users/bazil/AppData/Local/Temp/claude/75adcc7f3c1d08bf/7d33635e-8345-4a2c-a69e-f6a51f9d8fa7/scratchpad/reg_neuf98/scripts/'
LIV = 'livraison_15g_gel_loi_partie1/'
PIECES = [D + x for x in ('eligibilite_gel_loi_machine2_v1.py', 'eligibilite_gel_loi_machine2_v1.log', 'eligibilite_machine2_v1.json', 'table_commune_machine2_v1.json',
                          'tirage_gel_loi_machine2_v1.py', 'tirage_demonstration_machine2_v1.py', 'tirage_demonstration_machine2_v1.log', 'tirage_complet_machine2_v1.py',
                          'tirage_complet_machine2_v1_essai.log', 'tirage_complet_machine2_v1_demonstration.log')] + \
         [V + x for x in ('.py', '.log', '.json', '_premier_jet.py', '_premier_passage.log', '_premier_passage.json')] + \
         [D + 'mutation_gel_loi_partie1_contre_epreuve_machine2_v1.py', V + '_sur_gel_mute.log', V + '_sur_gel_mute.json'] + [SELF]
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


for p in PIECES + [NOTE, LIV + 'MANIFEST_lot_machine1_gel_loi_partie1_regle_tirage_v1.txt', LIV + 'lot_m1/gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md']:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
nn = re.sub(r'\s+', ' ', note)
v2 = json.load(open(os.path.join(ICI, V + '.json'), encoding='ascii'))
v1 = json.load(open(os.path.join(ICI, V + '_premier_passage.json'), encoding='ascii'))
vm = json.load(open(os.path.join(ICI, V + '_sur_gel_mute.json'), encoding='ascii'))
if len(v2['controles']) != 9 or v2['bilan']['ids'] != [] or v2['canon'] != 'b56ca5cb2dd25da1':
    arrets.append('second passage : %d controles, mordent %s, canon %s (attendu 9, aucun, b56ca5cb2dd25da1)' % (len(v2['controles']), v2['bilan']['ids'], v2['canon']))
if len(v1['controles']) != 9 or v1['bilan']['ids'] != ['C08']:
    arrets.append('premier passage : mordent %s (attendu C08 seul)' % v1['bilan']['ids'])
if len(vm['controles']) != 9 or vm['bilan']['mord'] != 9 or vm['canon'] == 'b56ca5cb2dd25da1':
    arrets.append('copie mutee : %d mordent (attendu 9), canon %s' % (vm['bilan']['mord'], vm['canon']))
le, lt, lc = lit(D + 'eligibilite_gel_loi_machine2_v1.log'), lit(D + 'tirage_demonstration_machine2_v1.log'), lit(D + 'tirage_complet_machine2_v1_demonstration.log')
for nom, lg, xs in (
        ('eligibilite', le, ('creneau N  :  9 w2 eligibles sur  9', 'creneau P  : 18 w2 eligibles sur 18', 'creneau BN :  7 w2 eligibles sur  8   INELIGIBLES : 1.916', 'creneau BP :  9 w2 eligibles sur  9',
                             'cellules de la table de machine 1 : 152 ; cellules ou nos tables different (boite, comptes, un drapeau, ou l eligibilite) : 0',
                             'boites differentes : 0 ; comptes jugeables / domaine differents : 0 ; drapeaux d etiquette (jugeable, domaine) differents : 0 sur 2128',
                             'desaccords sur l eligibilite d un w2 candidat (moi, machine 1) : 0', 'TABLE COMMUNE : N 9 / 9 ; P 18 / 18 ; BN 7 / 8 ; BP 9 / 9', 'cellules eligibles DE PEU (un compte au seuil) : 0')),
        ('tirage demonstration', lt, ('TIRAGE SUR LA GRAINE DE DEMONSTRATION : TIENT, les huit lignes sont identiques', 'RETROUVE')),
        ('tirage complet', lc, ('N1  w2 = 387/200 (1.935) facteur 3/4', 'P1  w2 = 256/125 (2.048) facteur 3/4', 'BN  w2 = 959/500 (1.918) facteur 1', 'BP  w2 = 2069/1000 (2.069) facteur 1')),
        ('essai du tirage complet', lit(D + 'tirage_complet_machine2_v1_essai.log'), ('ESSAI : TIENT (determinisme, douze cellules, rang suivant, arret sans candidat)',))):
    for x in xs:
        if x not in lg:
            arrets.append('journal %s : %r absent' % (nom, x))
mt = json.load(open(os.path.join(ICI, D + 'eligibilite_machine2_v1.json'), encoding='ascii'))
tc = json.load(open(os.path.join(ICI, D + 'table_commune_machine2_v1.json'), encoding='ascii'))
for nom, tab in (('ma table', mt), ('table commune', tc)):
    n = {s: (len(tab['creneaux'][s]['candidats']), sum(1 for c in tab['creneaux'][s]['candidats'] if c['eligible'])) for s in ('N', 'P', 'BN', 'BP')}
    if n != {'N': (9, 9), 'P': (18, 18), 'BN': (8, 7), 'BP': (9, 9)} or not all(re.fullmatch(r'\d+/\d+', c['w2']) for s in tab['creneaux'] for c in tab['creneaux'][s]['candidats']):
        arrets.append('%s : comptes ou format faux %s' % (nom, n))
if len(mt['cellules']) != 152:
    arrets.append('ma table : %d cellules (attendu 152)' % len(mt['cellules']))
for x in ('596a45bf6d4f97d7', 'b56ca5cb2dd25da1', 'CERTIFIE TEL QUEL', 'A ZERO MORSURE', '2128', '1.916', '4b2a1d038c89c813', 'OK go on gel', 'E19', '152', 'TABLE COMMUNE', 'onze endroits', '9 controles',
          'premier jet', 'C08', '548fb2ba8793ecfe', '658e3a89bcfa9368', 'M-8', 'Reprends', 'ne certifie pas', 'ne joue rien', 'je n\'ai pas la graine' if False else 'Je n\'ai pas recu la graine'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
man1 = open(os.path.join(ICI, LIV + 'MANIFEST_lot_machine1_gel_loi_partie1_regle_tirage_v1.txt'), 'rb').read()
if emp(man1)[0] != '596a45bf6d4f97d7':
    arrets.append('le lot de machine 1 n a plus le canon 596a45bf6d4f97d7 : %s' % emp(man1)[0])
if emp(open(os.path.join(ICI, LIV + 'lot_m1/gel_loi_ordre3_partie1_regle_tirage_pre_enregistrement_v1.md'), 'rb').read())[0] != 'b56ca5cb2dd25da1':
    arrets.append('le gel n a plus le canon b56ca5cb2dd25da1')
for nom, p, att in (('moteur', REG + 'm17_chaine_v17.py', '82a0be882568fe0c'), ('bloc d ordre 2', REG + 'chaine_ordre2_bloc_machine1_v1.py', '7cd5977bc27bebc1')):
    if emp(open(p, 'rb').read())[0] != att:
        arrets.append('canon %s : %s, attendu %s' % (nom, emp(open(p, 'rb').read())[0], att))
if emp(open(os.path.join(ICI, D + 'tirage_gel_loi_machine2_v1.py'), 'rb').read())[0] != 'c3128f277ef97d26':
    arrets.append('mon script de tirage n est plus celui du lot 658e3a89bcfa9368 (c3128f277ef97d26)')
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION DE MACHINE 2 DU GEL "LOI DE LA LARGEUR, ORDRE 3", PREMIERE PARTIE (b56ca5cb2dd25da1, lot de machine 1 596a45bf6d4f97d7) : CERTIFIE TEL QUEL, A ZERO MORSURE (9 controles ; '
    'premier passage : une morsure, la mienne, C08 ; contre-epreuve sur une copie mutee : 9 sur 9) ; MA TABLE des 152 cellules candidates, par ma chaine, identique a celle de machine 1 (0 difference sur '
    '2128 drapeaux) ; LA TABLE COMMUNE : N 9/9, P 18/18, BN 7/8 (1.916 ineligible), BP 9/9 ; mon tirage (graine de demonstration, rangs, table commune) identique au sien. 1D seulement, aucune largeur 2D ; '
    'aucune graine recue, aucun point tire. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : gel b56ca5cb2dd25da1 ; lot de machine 1 596a45bf6d4f97d7 ; mon lot reponse a la carte 548fb2ba8793ecfe ; mon lot evaluateur et tirage 658e3a89bcfa9368 ; mon lot ordre 3 889fe9b4c1c1c60a ; '
              'moteur 82a0be882568fe0c ; bloc d ordre 2 7cd5977bc27bebc1 ; note de la carte 1f6cfb5f9472b1b4\n')
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
