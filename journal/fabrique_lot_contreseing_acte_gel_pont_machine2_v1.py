# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'CONTRESEING DE L'ACTE DU RUN DU GEL PONT' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-18. Meme squelette que fabrique_lot_resultats_run_gel_pont_machine2_v1.py (non edite).
Aucune 2D, aucun depot. Le lot porte mon releve de l'acte et sa contre-epreuve (tous les passages), ton releve rejoue sur mon poste, les journaux d'authentification.
Usage : py -3.11 -I fabrique_lot_contreseing_acte_gel_pont_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; la note est ASCII et nomme le canon de CHAQUE piece ; les blocs que la note recopie sont LUS dans les journaux ; les nombres qu'elle cite d'elle-meme sont relus dans le journal qui les porte ;
aucune fuite de vie privee (noms, lettres de lecteur avec barre ET antislash, adresses) ; les chemins de disque des journaux sont remplaces par <chemin> dans les octets du zip ; CRLF -> LF ; canon B inchange par la seule normalisation LF ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
L18 = 'livraison_18a_acte_gel_pont/'
CS = L18 + 'contreseing/'
NOM = 'lot_machine2_2026-11-18_contreseing_acte_gel_pont_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_gel_pont_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_gel_pont_machine2_v1.md'
GAB = 'POUR_MACHINE1_contreseing_acte_gel_pont_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_contreseing_acte_gel_pont_machine2_v1.py'
arrets = []
PIECES = [L18 + 'authentification_envoi_machine2_v1.log']
for d, _, fs in os.walk(os.path.join(ICI, CS)):
    for f in fs:
        rel = os.path.relpath(os.path.join(d, f), ICI).replace(os.sep, '/')
        if not rel.endswith('gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md'):       # la copie posee pour son releve redouble sa piece : non portee
            PIECES.append(rel)
PIECES = sorted(PIECES) + [SELF]
for p in PIECES[:-1] + [GAB]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


MASQUE = re.compile(rb'(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s"\']*')
CONT = {}
nmask = 0
for p in PIECES:
    brut = open(os.path.join(ICI, p), 'rb').read()
    if b'\r\n' in brut:
        lf = brut.replace(b'\r\n', b'\n')
        if emp(lf)[0] != emp(brut)[0]:
            arrets.append('le canon B change a la normalisation LF : %s' % p)
        brut = lf
    if p.endswith('.log') and MASQUE.search(brut):
        brut = MASQUE.sub(b'<chemin>', brut)
        nmask += 1
    CONT[p] = brut
nb_lf = sum(1 for p in PIECES if open(os.path.join(ICI, p), 'rb').read() != CONT[p])


def lit(p):
    return CONT[p].decode('utf-8')


TERMES = [''.join(p) for p in (('ba', 'zil'), ('le', 'beau'), ('gm', 'ail'), ('hot', 'mail'), ('Us', 'ers\\'), ('Us', 'ers/'), ('App', 'Data'), ('.cla', 'ude\\'), ('.cla', 'ude/'), ('Down', 'loads'), ('PANIER', 'CLIENT'))]


def fuites(nom, octets):
    t = octets.decode('latin-1').lower()
    out = [(nom, w) for w in TERMES if w.lower() in t]
    out += [(nom, m) for m in re.findall(r'(?<![a-z0-9])[a-z]:[\\/]', t)]
    out += [(nom, m) for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', t)]
    return out


note = open(os.path.join(ICI, GAB), encoding='ascii', newline='').read()
if '\r' in note:
    arrets.append('le gabarit a des CRLF')
log = lambda n: lit(CS + n)
rel_log, ce_log = log('releve_contreseing_acte_pont_machine2_v1.log'), log('contre_epreuve_releve_contreseing_pont_machine2_v1.log')
m1_rel, m1_ce = log('releve_acte_m1_rejoue_sur_mon_poste_machine2_v1.log'), log('contre_epreuve_releve_m1_rejouee_sur_mon_poste_machine2_v1.log')
auth = lit(L18 + 'authentification_envoi_machine2_v1.log')
ind = lambda ls, n=3: '\n'.join(' ' * n + l for l in ls)
note = note.replace('@@AUTH@@', ind([l for l in auth.split('\n') if l.startswith(('CANON du manifeste', 'MORSURES'))]))
note = note.replace('@@RELEVE@@', ind([l for l in rel_log.split('\n') if l.startswith(('R', ' ')) and l.strip()]))
note = note.replace('@@CE@@', ind([l for l in ce_log.split('\n') if l.startswith(('copie intacte', 'CONTRE-EPREUVE'))]))
note = note.replace('@@RELEVEM1@@', ind([l for l in m1_rel.split('\n') if l.startswith('RELEVE DE')] + [l for l in m1_ce.split('\n') if l.startswith('CONTRE-EPREUVE')]))
note = note.replace('@@NMASK@@', str(nmask))
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(CONT[p])[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
CHAMPS = CS + 'champs_au_dessus_de_1e12_machine2_v1.log'
NOMBRES = [(CS + 'releve_contreseing_acte_pont_machine2_v1.log', 'RELEVE DE MON CONTRESEING : 16 controles ; 0 morsure(s)'),
           (CS + 'contre_epreuve_releve_contreseing_pont_machine2_v1.log', 'CONTRE-EPREUVE DE MON RELEVE : 30 alterations, 30 mordues sur le controle vise ; copie intacte sans morsure'),
           (CS + 'contre_epreuve_releve_m1_rejouee_sur_mon_poste_machine2_v1.log', "CONTRE-EPREUVE DE L'ACTE : 20 alterations, 20 mordues"),
           (CS + 'releve_acte_m1_rejoue_sur_mon_poste_machine2_v1.log', "RELEVE DE L'ACTE : 10 controles ; 0 morsure"),
           (L18 + 'authentification_envoi_machine2_v1.log', 'MORSURES : 0'),
           (CS + 'releve_contreseing_acte_pont_machine2_v1.log', '1.26e-09'),
           (CS + 'releve_contreseing_acte_pont_machine2_v1.log', '6211 nombres, 1.44e-11'),
           (CHAMPS, '6211 nombres compares ; champs au-dessus de 1e-12 : 3'), (CHAMPS, 'plus grand ecart 6.16e-12'), (CHAMPS, 'plus grand ecart 5.42e-12'),
           (CS + 'contre_epreuve_releve_contreseing_pont_machine2_v1_second_passage_29_sur_30.log', 'les cellules tombees de (L)                : NON MORDUE par R03'),
           (CS + 'releve_contreseing_acte_pont_machine2_v1_second_passage_R13_mord_regex.log', 'R13 nn.6 : (Q4)'),
           (CS + 'releve_acte_m1_rejoue_sur_mon_poste_machine2_v1_premier_passage_A02_mord_nom_de_fichier.log', 'A02 les 29 pieces de nn.12, canons recalcules : MORD')]
SANS_NOTE = {'6211 nombres compares ; champs au-dessus de 1e-12 : 3', 'les cellules tombees de (L)                : NON MORDUE par R03', 'R13 nn.6 : (Q4)', 'A02 les 29 pieces de nn.12, canons recalcules : MORD'}
for j, s in NOMBRES:
    if norm(s) not in norm(lit(j)):
        arrets.append('la piece %s ne porte pas %r' % (j, s))
    if s not in SANS_NOTE and norm(s) not in norm(note):
        arrets.append('la note ne porte pas %r' % s)
for s_ in ('1.26e-09', '6211 nombres', '1.44e-11', '1743 niveaux', '11185 s', '0.05024', '9b980dffc71552d5', 'daf56d624e87e8e5', 'e7fb283dd2ee517c', 'JE CONTRESIGNE'):
    if s_ not in note:
        arrets.append('la note ne porte pas %r' % s_)
if '@@' in note:
    arrets.append('marque non remplacee dans la note')
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for p in PIECES:
    if p != SELF and emp(CONT[p])[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for p in PIECES:
    for f in fuites(p, CONT[p]):
        arrets.append('FUITE de vie privee : %s' % (f,))
for f in fuites(NOTE, note.encode('ascii')):
    arrets.append('FUITE de vie privee : %s' % (f,))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
CONT_NOTE = note.encode('ascii')

lignes = [
    'MANIFESTE %s -- LE CONTRESEING par machine 2 de l\'acte du run du gel "pont" (journal_delta_nn_pont_v1.md, canon e7fb283dd2ee517c, lot de machine 1 daf56d624e87e8e5) : mon releve et sa contre-epreuve (tous les passages), '
    'ton releve rejoue sur mon poste, l\'authentification. AUCUNE 2D ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : l'acte de machine 1 (lot daf56d624e87e8e5) ; mon lot de resultats 9b980dffc71552d5 ; le gel en deux parties (735ce41be200c5cd, 428ac47649de31f3) et son rectificatif (9e25019f3b9bdf04) ; le registre public en tete 2988237\n")
lignes.append('pieces : %d (compte etabli APRES le dernier ajout) ; %d portees en LF ; %d journaux dont des chemins de disque ont ete masques\n' % (len(PIECES) + 1, nb_lf, nmask))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    z.writestr(NOTE, CONT_NOTE)
    for p in PIECES:
        z.writestr(p, CONT[p])
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read(), NOTE: CONT_NOTE}
    attendu.update(CONT)
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets ; %d portees en LF ; %d journaux masques' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP), nb_lf, nmask))
