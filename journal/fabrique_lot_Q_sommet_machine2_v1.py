# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'Q SOMMET' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-22. Derive de fabrique_lot_pole_court_machine2_v1.py (non edite).
Contenu : la QUALIFICATION "Q" du lecteur creux au sommet (sa 22g, section 8) jouee aux cinq points sacrifies, ses attendus Q-1 a Q-5 ecrits avant, ma lecture a la lettre ; le releve de convergence ; mes verifications de sa note (eta0, rejeu de 96 cas, d'apres-coup) ; ma demolition de l'esquisse du gel "sommet".
Classe 3 : aucun gel, aucun depot, aucun verdict.
Usage : py -3.11 -I fabrique_lot_Q_sommet_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; la note est ASCII et nomme le canon de CHAQUE piece ; les blocs recopies sont LUS dans les journaux ; les nombres cites sont relus dans le journal qui les porte ;
aucune fuite de vie privee ; chemins de disque masques ; CRLF -> LF ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-22_Q_sommet_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_Q_sommet_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_Q_sommet_demolition_machine2_v1.md'
GAB = 'POUR_MACHINE1_Q_sommet_demolition_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_Q_sommet_machine2_v1.py'
C = 'certif_relecteur_machine2/'
EP_LOG, ETA_LOG, CV_LOG = C + 'epreuve_Q_sommet_machine2_v1.log', C + 'eta0_Q_machine2_v1.log', C + 'releve_convergence_Q_machine2_v1.log'
RJ_LOG, AC_LOG = C + 'verifie_rejeu_m1_pole_court_machine2_v1.log', C + 'verifie_apres_coup_m1_machine2_v1.log'
SO = C + 'Q_sorties/'
IDS = ['Qa', 'Qc', 'Qd', 'Qe', 'Qf']
JSON_Q = [SO + 'lect2D_%s_%s.json' % (i, q) for i in IDS for q in ('fantome', 'jumeau')]
LOGS_Q = [SO + 'log_%s_%s.txt' % (i, q) for i in IDS for q in ('fantome', 'jumeau')]
PIECES = [C + 'epreuve_Q_sommet_machine2_v1.py', EP_LOG, C + 'epreuve_Q_sommet_machine2_v1_premier_passage_R1_geometrie_mal_lue.log',
          C + 'eta0_Q_machine2_v1.py', ETA_LOG, C + 'releve_convergence_Q_machine2_v1.py', CV_LOG,
          C + 'jobs_Q_machine2_v1.txt', C + 'lance_Q_machine2_v1.out', C + 'lance_lect2D_machine2_v3_abs.sh', C + 'lecteur_2D_pilote_machine2_v1.py', SO + 'debut.txt'] + JSON_Q + LOGS_Q + [
          C + 'verifie_rejeu_m1_pole_court_machine2_v1.py', RJ_LOG, C + 'verifie_apres_coup_m1_machine2_v1.py', AC_LOG, SELF]
arrets = []
for p in PIECES + [GAB]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if len(set(PIECES)) != len(PIECES):
    arrets.append('doublon dans la liste des pieces')
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
    if p.endswith(('.log', '.md', '.txt', '.out')) and MASQUE.search(brut):
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


ind = lambda ls: '\n'.join(('    ' + l) if l else '' for l in ls)
note = open(os.path.join(ICI, GAB), encoding='ascii', newline='').read()
if '\r' in note:
    arrets.append('le gabarit a des CRLF')
for marque, chemin in (('@@EP@@', EP_LOG), ('@@CV@@', CV_LOG), ('@@ETA@@', ETA_LOG), ('@@RJ@@', RJ_LOG), ('@@AC@@', AC_LOG)):
    bloc = [l for l in lit(chemin).split('\n') if l.strip()]
    if not bloc:
        arrets.append('bloc vide : %s' % marque)
    note = note.replace(marque, ind(bloc))
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(CONT[p])[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
LOGS = ' '.join(norm(lit(p)) for p in (EP_LOG, ETA_LOG, CV_LOG, RJ_LOG, AC_LOG))
NOMBRES = [('statut QUALIFIE', 'QUALIFIES par la feuille deposee'),
           ('Q-f 0.00008', '0.00008'),
           ('Q-4 fenetres retenues dans les listes de sa note : 19 sur 20', 'Q-4 : 19 SUR 20'),
           ('Q-5 |ln[(Gamma_pl / g)(Q-d) / (Gamma_pl / g)(Q-a)]| = 0.00001', 'Q-5 : 0.00001 pour 0.005'),
           ('-> NON REALISE', "N'EST REALISE NULLE PART"),
           ('/ t_0 = 0.533315', '0.533315'), ('/ t_0 = 0.533314', '0.533314'), ('/ t_0 = 0.533308', '0.533308'),
           ('Gamma_pl(A) / g = 0.040309', '0.040309 g'), ('Gamma_pl(A) / g = 0.019430', '0.019430 g'),
           ('(= 1.45e-36 Gamma_pl)', '1.45e-36 Gamma_pl'),
           ('poids du site (0, 0) mini dans la fenetre de A : 0.8988', '0.8988'),
           ('1.040 1.135 1.256 1.318', '1.040 a k = 5, 1.318 a k = 8'),
           ('1.013 1.098 1.091 0.714', '1.098 a k = 6, 0.714 a k = 8'),
           ('0.971 0.884 0.797 0.758', '0.758'), ('0.990 0.940 0.847 0.615', '0.615'), ('0.944 0.714 0.421 0.221', '0.221'),
           ('lectures suivies : 477 sur 480', '477 lectures suivies sur 480'), ('0.7531 .. 0.9247', '0.7531'),
           ('plus grand ecart relatif entre mes eta0 (six chiffres) et les siens : 0.0e+00', 'ecart relatif 0 aux cinq points'),
           ('plus grand ecart sur gamma_sur_g : 5.48e-11', '5.48e-11'),
           ('0.5 5e-04 4.48e-04', '4.48e-04'), ('0.5 1e-03 1.65e-03', '1.65e-03'), ('2.0 1e-03 2.43e-05', '2.43e-05'), ('4.0 1e-03 7.99e-06', '7.99e-06'),
           ('de 3.60 a 4.12', '3.60 a 4.12'), ('de 4.12 a 4.48', '4.12 a 4.48'),
           ('coupes paires : 2D - C1 : 12 negatifs, 0 positifs', '12 negatifs aux coupes paires')]
for sj, sn in NOMBRES:
    if norm(sj) not in LOGS:
        arrets.append('le journal ne porte pas %r' % sj)
    if norm(sn) not in norm(note):
        arrets.append('la note ne porte pas %r' % sn)
if '@@' in note:
    arrets.append('marque non remplacee dans la note')
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for p in PIECES:
    if p != SELF and emp(CONT[p])[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for cle in ('423ec0fd24240977', '82a0be882568fe0c', 'd5cc48f48e37af99', '83701094e6a2b965', '47a84eae6052f006'):
    if cle not in note:
        arrets.append('la note ne cite pas le canon %s' % cle)
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
    'MANIFESTE %s -- QUALIFICATION "Q" DU LECTEUR CREUX AU SOMMET (sa 22g, section 8) jouee aux cinq points sacrifies (w2 = 2 a g = 2.5e-04, 1e-03, 2e-03 ; w2 = 20001/10000 a g = 3e-04, 1.5e-04), ses attendus Q-1 a Q-5 ecrits avant et lus a la lettre ; releve de convergence ; mes verifications de sa note (eta0, rejeu de 96 cas, d\'apres-coup) ; ma demolition de l\'esquisse du gel "sommet". '
    'HORS CHAINE, classe 3, non certifie ; aucun gel ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : son enveloppe 22g (lot 423ec0fd24240977), lue comme donnees (ses JSON de rejeu et sa chaine du premier ordre) ; le registre public en tete 055be58 : moteur 82a0be882568fe0c, bloc LECTEUR CREUX d5cc48f48e37af99, feuille 83701094e6a2b965 ; mon pilote 47a84eae6052f006 ; mon lot 2d69195af996cc0f\n")
lignes.append('pieces : %d (compte etabli APRES le dernier ajout) ; %d portees en LF ; %d pieces dont des chemins de disque ont ete masques\n' % (len(PIECES) + 1, nb_lf, nmask))
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
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets ; %d portees en LF ; %d masquees' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP), nb_lf, nmask))
