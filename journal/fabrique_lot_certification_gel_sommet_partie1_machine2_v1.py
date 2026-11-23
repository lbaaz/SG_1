# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'CERTIFICATION DU GEL SOMMET, PARTIE 1' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-22. Derive de fabrique_lot_Q2_signe_machine2_v1.py (non edite).
Contenu : ma certification (a) a (e) de la premiere partie du gel "sommet" (piece 1e5039cade55d13f, lot 3ba4618d7976c6ea) : ma table des 560 cellules, son recoupement et la table commune, mon tirage de demonstration, mon balayage de virginite, la robustesse de ses choix neufs, ses chiffres de la section 7 refaits.
Classe 3 sauf ce que la note certifie ; aucun calcul 2D, aucun gel, aucun depot.
Usage : py -3.11 -I fabrique_lot_certification_gel_sommet_partie1_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; la note est ASCII et nomme le canon de CHAQUE piece ; les blocs recopies sont LUS dans les journaux ; les nombres cites sont relus dans le journal qui les porte ;
aucune fuite de vie privee ; chemins de disque masques ; CRLF -> LF ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-22_certification_gel_sommet_partie1_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_sommet_partie1_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_sommet_partie1_machine2_v1.md'
GAB = 'POUR_MACHINE1_certification_gel_sommet_partie1_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_certification_gel_sommet_partie1_machine2_v1.py'
C = 'certif_gel_sommet_partie1_machine2/'
L = {n: C + n for n in ('table_eligibilite_sommet_machine2_v1.log', 'recoupe_tables_sommet_machine2_v1.log', 'compare_tirage_sommet_m1_machine2_v1.log', 'autotest_regle_rangs_sommet_machine2_v1.log',
                         'balayage_virginite_sommet_machine2_v1.log', 'robustesse_sommet_machine2_v1.log', 'verifie_chiffres_section7_machine2_v1.log', 'tirage_demonstration_sommet_machine2_v1.log')}
PIECES = [C + 'table_eligibilite_sommet_machine2_v1.py', L['table_eligibilite_sommet_machine2_v1.log'], C + 'table_machine2_sommet_v1.json', C + 'detail_machine2_sommet_v1.json',
          C + 'recoupe_tables_sommet_machine2_v1.py', L['recoupe_tables_sommet_machine2_v1.log'], C + 'table_commune_sommet_machine2_v1.json',
          C + 'tirage_sommet_machine2_v1.py', L['tirage_demonstration_sommet_machine2_v1.log'], C + 'compare_tirage_sommet_m1_machine2_v1.py', L['compare_tirage_sommet_m1_machine2_v1.log'],
          C + 'autotest_regle_rangs_sommet_machine2_v1.py', L['autotest_regle_rangs_sommet_machine2_v1.log'],
          C + 'balayage_virginite_sommet_machine2_v1.py', L['balayage_virginite_sommet_machine2_v1.log'],
          C + 'robustesse_sommet_machine2_v1.py', L['robustesse_sommet_machine2_v1.log'], C + 'verifie_chiffres_section7_machine2_v1.py', L['verifie_chiffres_section7_machine2_v1.log'],
          'livraison_22i_Q2_notee_gel_sommet_partie1/authentification_lots_machine2_v2.log', SELF]
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


def lignes(p):
    return [l for l in lit(p).split('\n') if l.strip()]


def bloc_tab():
    ls = lignes(L['table_eligibilite_sommet_machine2_v1.log'])
    i = [k for k, l in enumerate(ls) if l.startswith('w2 eligibles :')]
    return ls[i[0]:] if i else []


def bloc_bal():
    ls = lignes(L['balayage_virginite_sommet_machine2_v1.log'])
    i3 = [k for k, l in enumerate(ls) if l.startswith('(3) VALEURS DISTINCTES')]
    if not i3:
        return []
    sortie = ls[:i3[0] + 1]
    for l in ls[i3[0] + 1:]:
        m = re.search(r'=\s+([0-9]+\.[0-9]+)\s+\(', l)
        if m and 1.9945 <= float(m.group(1)) <= 2.0055:
            sortie.append(l)
    sortie.append('    [... les autres valeurs distinctes de w2 (1.25 a 1.99, 2.005 a 2.019) sont dans le journal joint ...]')
    sortie += [l for l in ls if l.startswith('VALEURS CANDIDATES VUES')]
    return sortie


ind = lambda ls: '\n'.join(('    ' + l) if l else '' for l in ls)
note = open(os.path.join(ICI, GAB), encoding='ascii', newline='').read()
if '\r' in note:
    arrets.append('le gabarit a des CRLF')
BLOCS = (('@@TAB@@', bloc_tab()), ('@@REC@@', lignes(L['recoupe_tables_sommet_machine2_v1.log'])), ('@@TIR@@', lignes(L['compare_tirage_sommet_m1_machine2_v1.log'])),
         ('@@AUT@@', lignes(L['autotest_regle_rangs_sommet_machine2_v1.log'])), ('@@BAL@@', bloc_bal()), ('@@ROB@@', lignes(L['robustesse_sommet_machine2_v1.log'])),
         ('@@S7@@', lignes(L['verifie_chiffres_section7_machine2_v1.log'])))
for marque, bloc in BLOCS:
    if not bloc:
        arrets.append('bloc vide : %s' % marque)
    note = note.replace(marque, ind(bloc))
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(CONT[p])[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
LOGS = ' '.join(norm(lit(p)) for p in L.values())
NOMBRES = [('w2 eligibles : 80 sur 80 ; cellules : 560 sur 560', '80 w2 eligibles sur 80, 560 cellules sur 560'),
           ('ecart |ln Gamma_flux - ln Gamma_eig| maximal : 1.63e-07', '1.63e-07'),
           ('second plus grand poids du site 0 (parmi les etats propres), maximum sur les 560 cellules x 18 variantes : 0.0192', '0.0192'),
           ('couplages ecrits dont l ecriture depend de |delta| calcule en flottant ou en exact : 0', '0 couplage ecrit different sur 560'),
           ('DESACCORDS (trois nombres ecrits, kappa, m_bord, eligibilite, w2) : 0', '0 desaccord'),
           ('plus grands ecarts entre ses nombres et les miens : e_bord 1.08e-19 ; etendue 2.17e-11 ; ln du plateau G3 2.28e-11 ; poids du site 0 8.62e-13', 'e_bord 1.08e-19, etendue 2.17e-11, ln du plateau 2.28e-11, poids du site 0 8.62e-13'),
           ('TABLE COMMUNE : 80 w2 eligibles sur 80 ; cellules eligibles 560 sur 560', 'Elle est jointe (table_commune_sommet_machine2_v1.json)'),
           ('(3) cellules : miennes 56 ; siennes 56 ; identiques (kappa, g, eta0, r_c, chaines) : 56 sur 56', '56 sur 56 identiques'),
           ('AUTOTEST : TIENT (5 sur 5)', '5 sur 5'),
           ('avec M_facteur = 4 : 0 aboutissent, 60 echouent (KeyError)', 'echoue (KeyError) aux 60'),
           ('plus grand |ln Gamma(M_facteur 5) - ln Gamma(M_facteur 6)| sur les dix-huit variantes : 0.00e+00', 'identiques a 0.0 pres'),
           ('etendue : minimum 0.0003, mediane 0.0025, maximum 0.0037 sur 560 cellules', 'de 0.0003 a 0.0037'),
           ('seuil 0.0035 : 7 cellules et 7 w2 sur 80 seraient retires', '0.0035 retirerait 7 w2'),
           ('seuil 0.0033 : 55 cellules et 50 w2 sur 80 seraient retires', '0.0033 en retirerait 50'),
           ('plus grand e_bord sur les 560 cellules : 0.0010 (garde : 0.7 : 714 fois de marge)', '714 fois de marge'),
           ('plus grand ecart entre ma formule et la valeur du moteur : 1.08e-19', '1.08e-19 pres aux 160'),
           ('280 paires ; ln[Phi(delta < 0) / Phi(delta > 0)] de -0.00007 a +0.00051', '(de -0.00007 a +0.00051)'),
           ('cellules a barriere vide : 400', '400 cellules a barriere vide'),
           ('50 cellules, jusqu a 2.33 fois', 'jusqu\'a 2.33 fois'), ('42 cellules, jusqu a 0.163 fois', 'jusqu\'a 0.163 fois'),
           ('eta0 / g de 3.8883 a 3.9027', '3.8883 a 3.9027'),
           ('VALEURS CANDIDATES VUES COMME w2 DANS UN JSON : 0', 'zero cle JSON')]
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
for cle in ('3ba4618d7976c6ea', '1e5039cade55d13f', '82a0be882568fe0c', '7cd5977bc27bebc1', '534ba246aa3b8973', '77ce2a6c7e867011', '882f55d07d03dfff'):
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

lg = [
    'MANIFESTE %s -- CERTIFICATION (a) A (e) DE LA PREMIERE PARTIE DU GEL "SOMMET" (piece 1e5039cade55d13f, lot 3ba4618d7976c6ea) : ma table des 560 cellules, son recoupement avec la sienne et la table commune, mon tirage de demonstration et son autotest, mon balayage de virginite, '
    'la robustesse de ses choix neufs, ses chiffres de la section 7 refaits. AUCUN CALCUL 2D ; aucun gel ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lg.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lg.append("\nentrants : son enveloppe 22i (lot 3ba4618d7976c6ea) : la piece de gel 1e5039cade55d13f, sa table JSON 77ce2a6c7e867011 et son detail 882f55d07d03dfff (lus APRES ma table) ; le registre public en tete 055be58 : moteur 82a0be882568fe0c, blocs 7cd5977bc27bebc1 et 534ba246aa3b8973 ; mes lots c58c2b3f533c516b (Q) et 295b2b1549b076c2 (Q2)\n")
lg.append('pieces : %d (compte etabli APRES le dernier ajout) ; %d portees en LF ; %d pieces dont des chemins de disque ont ete masques\n' % (len(PIECES) + 1, nb_lf, nmask))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lg)
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
