# -*- coding: ascii -*-
"""FABRIQUE DU LOT de certification de machine 2 : gel 'largeur du vide', PREMIERE PARTIE (b57c9ccdd3946261) + lecture de la note sur le vide -- manifeste + ZIP. 2026-11-16.
Meme squelette que fabrique_lot_reponse_releve_depot_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_certification_gel_vide_partie1_machine2_v1.py
Gardes AVANT ecriture : chaque nombre que la note cite est RELU dans un journal (authentifications a 0 morsure, recoupe des tables a 0 desaccord, tirage, balayages, faisabilite,
rejeu, robustesse) ; mon journal de tirage rejoue = le journal de m1, ligne a ligne ; la note est ASCII (verifie AVANT d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ;
ZIP relu bit-identique."""
import glob
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_certification_gel_vide_partie1_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_vide_partie1_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_vide_partie1_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_vide_partie1_machine2_v1.py'
C = 'certif_gel_vide_partie1_machine2/'
R = 'rejeu_vide_machine2/'
L16E = 'livraison_16e_vide_etape_sans_run/'
L16F = 'livraison_16f_gel_vide_partie1/'
M1_DEMO = L16F + 'ext/x_gel_vide_partie1_regle_tirage/lot_machine1_2026-11-16_gel_vide_partie1_regle_tirage_v1/tirage_vide_machine1_v1_demonstration.log'
PIECES = [
    # authentification de ce que m1 a livre
    L16E + 'authentifie_lot_vide_m1_machine2_v1.py', L16E + 'authentifie_lot_vide_m1_machine2_v1.log',
    L16F + 'authentifie_lots_gel_vide_machine2_v1.py', L16F + 'authentifie_lots_gel_vide_machine2_v1.log',
    # ma table, le recoupement, la table commune
    C + 'table_eligibilite_vide_machine2_v1.py', C + 'table_eligibilite_vide_machine2_v1.log', C + 'table_machine2_vide_v1.json', C + 'detail_machine2_vide_v1.json',
    C + 'recoupe_tables_vide_machine2_v1.py', C + 'recoupe_tables_vide_machine2_v1.log', C + 'table_commune_vide_machine2_v1.json',
    C + 'controle_kappa_m_machine2_v1.py', C + 'controle_kappa_m_machine2_v1.log',
    # tirage
    C + 'tirage_demonstration_machine2_v1.py', C + 'tirage_demonstration_machine2_v1.log', C + 'tirage_m1_autotest_rejoue_machine2.log', C + 'tirage_m1_demonstration_rejouee_machine2.log',
    # balayages E19
    C + 'balayage_E19_vide_machine2_v1.py', C + 'balayage_E19_vide_machine2_v1.log', C + 'balayage_E19_vide_machine2_v1_premier_passage.log',
    C + 'triage_E19_contexte_machine2_v1.py', C + 'triage_E19_contexte_machine2_v1.log',
    C + 'balayage_etat_00_machine2_v1.py', C + 'balayage_etat_00_machine2_v1.log',
    # boites (e) et petit delta (M-6)
    C + 'derive_faisabilite_machine2_v1.py', C + 'faisabilite_profondeur_jumeau_machine2_v1.py', C + 'faisabilite_profondeur_jumeau_machine2_v1.diff',
    C + 'faisabilite_profondeur_jumeau_machine2_v1.log', C + 'faisabilite_profondeur_jumeau_machine2_v1.json',
    C + 'faisabilite_profondeur_jumeau_machine2_v1_premier_passage_memoire_0.log', C + 'faisabilite_profondeur_jumeau_machine2_v1_premier_passage.json',
    C + 'derive_petit_delta_machine2_v1.py',
    C + 'faisabilite_petit_delta_w2_1_9995_machine2_v1.py', C + 'faisabilite_petit_delta_w2_1_9995_machine2_v1.diff', C + 'faisabilite_petit_delta_w2_1_9995_machine2_v1.log', C + 'faisabilite_petit_delta_w2_1_9995_machine2_v1.json',
    C + 'faisabilite_petit_delta_w2_2_0005_machine2_v1.py', C + 'faisabilite_petit_delta_w2_2_0005_machine2_v1.diff', C + 'faisabilite_petit_delta_w2_2_0005_machine2_v1.log', C + 'faisabilite_petit_delta_w2_2_0005_machine2_v1.json',
    # rejeu et lecture de la note du vide
    R + 'rejeu_vide_machine2_v1.py', R + 'console_rejeu.log', R + 'compare_rejeu_machine2_v1.py', R + 'compare_rejeu_machine2_v1.log',
    R + 'verifie_phi_profond_machine2_v1.py', R + 'verifie_phi_profond_machine2_v1.log',
    R + 'recompte_titres_machine2_v1.py', R + 'recompte_titres_machine2_v1.log',
    R + 'analyse_biais_joues_machine2_v1.py', R + 'analyse_biais_joues_machine2_v1.log',
    R + 'robustesse_variantes_joues_machine2_v1.py', R + 'robustesse_variantes_joues_machine2_v1.log',
] + sorted(os.path.relpath(p, ICI).replace(os.sep, '/') for p in glob.glob(os.path.join(ICI, 'rejeu_vide_machine2', 'sortie', '*')) if os.path.isfile(p)) + [SELF]
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def lit(p):
    return open(os.path.join(ICI, p), encoding='utf-8', errors='replace').read().replace('\r\n', '\n')


def exige(p, *morceaux):
    t = lit(p)
    for m in morceaux:
        if m not in t:
            arrets.append('journal %s : %r absent' % (p.split('/')[-1], m))


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
# gardes : les nombres de la note sont dans les journaux
exige(L16E + 'authentifie_lot_vide_m1_machine2_v1.log', 'CANON du manifeste (calcule, non annonce) : c5d8fd0313217569', 'MORSURES : 0', 'note a plat == note du lot (octets) : True')
exige(L16F + 'authentifie_lots_gel_vide_machine2_v1.log', 'CANON du manifeste (calcule) : 879ea2e51c7d7f4f', 'CANON du manifeste (calcule) : 408b8a595cad0040 ; annonce : 408b8a595cad0040',
      'md a plat == md du lot (octets) : True ; canon b57c9ccdd3946261', 'section 13 : pieces citees avec canon : 27', 'morsures section 13 : 0', 'lot du vide de l enveloppe == lot deja recu (octets) : True', 'MORSURES TOTAL : 0')
exige(C + 'table_eligibilite_vide_machine2_v1.log', 'creneau MG : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27', 'creneau MP : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27',
      'creneau PP : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27', 'creneau PG : 9 w2 eligibles sur 9 ; cellules profondes retenues : 27 sur 27',
      'X entier == X flottant partout : True', 'couplages ecrits dont l ecriture depend de |delta| calcule en flottant ou en exact : 0', 'etendue max 0.0093')
exige(C + 'recoupe_tables_vide_machine2_v1.log', 'cellules comparees : 252', 'DESACCORDS (couplage, m_bord, eligibilite, w2) : 0', 'e_bord 5.55e-17', 'etendue 1.59e-08', 'ln du plateau de Gamma 1.33e-08')
exige(C + 'controle_kappa_m_machine2_v1.log', '-0.16 %', '2.92e-08', '1.25e-06', '3.63e-03')
exige(C + 'tirage_demonstration_machine2_v1.log', 'EXEMPLE DU GEL RETROUVE : True', 'MG : rang 0, w2 = 1.987', 'MP : rang 0, w2 = 1.993', 'PP : rang 0, w2 = 2.006', 'PG : rang 0, w2 = 2.017')
exige(C + 'tirage_m1_autotest_rejoue_machine2.log', 'AUTOTEST : TIENT')
if lit(C + 'tirage_m1_demonstration_rejouee_machine2.log') != lit(M1_DEMO):
    arrets.append('mon rejeu de ton tirage --demonstration n\'est pas, caractere pour caractere, ton journal')
exige(C + 'balayage_E19_vide_machine2_v1.log', 'fichiers texte lus : 10543 ; zips ouverts : 287 ; membres texte de zips lus : 3224 ; erreurs de lecture : 0', 'fichiers avec au moins une ecriture d un w2 candidat : 237',
      'LIGNES OU LE JETON FIGURE AVEC "w2"/"omega" : 22 ligne(s)')
exige(C + 'triage_E19_contexte_machine2_v1.log', 'fichiers texte : 3790 ; jetons : 98 , dont mantisses en notation scientifique : 19 ; isoles : 79', 'valeurs isolees dont la ligne parle de w2 ou omega : 0',
      'fichiers distincts portant une valeur isolee : 35')
exige(C + 'balayage_etat_00_machine2_v1.log', 'fichiers portant une etiquette (0, 0) : 43')
exige(C + 'faisabilite_profondeur_jumeau_machine2_v1.log', 'memoire max 411 Mo', 'memoire max 538 Mo', 'memoire max 662 Mo', '3.91e-56', '1.90e-78', '1.02e-100')
if lit(C + 'faisabilite_profondeur_jumeau_machine2_v1.log').count('6 lectures, 6 suivies') != 3:
    arrets.append('faisabilite : les trois geometries ne sont pas 6 sur 6')
exige(C + 'faisabilite_profondeur_jumeau_machine2_v1_premier_passage_memoire_0.log', 'memoire max 0 Mo')
for n in ('1_9995', '2_0005'):
    j = C + 'faisabilite_petit_delta_w2_%s_machine2_v1.log' % n
    exige(j, 'memoire max 662 Mo')
    if lit(j).count('6 lectures, 6 suivies') != 3:
        arrets.append('petit delta %s : les trois geometries ne sont pas 6 sur 6' % n)
exige(R + 'compare_rejeu_machine2_v1.log', 'DESACCORDS DE STRUCTURE TOTAL : 0', '4.33e-16', '1.69e-07')
exige(R + 'console_rejeu.log', 'FIN DU REJEU : 0 job(s) en echec')
exige(R + 'verifie_phi_profond_machine2_v1.log', 'ma regle de barriere rend m_bord = nombre de barreaux aux 6 points : True', 'plus grand |mon - fc| : 1.14e-13', 'plus grand |mon - lecteur| : 7.11e-15')
exige(R + 'recompte_titres_machine2_v1.log', 'adapte < depose : 168 sur 185', 'delta>0 71/81 ; delta<0 7/104', 'hors tolerance E1 : adapte 0, depose 0', 'etendue adaptee : mediane 0.021 ; 9e decile 0.064 ; max 0.33')
exige(R + 'robustesse_variantes_joues_machine2_v1.log', 'etats ou AU MOINS UNE des 18 variantes sort de la tolerance E1 : 14', 'etats ou la MEDIANE des variantes sort de la tolerance : 0',
      'etats ou la regle deposee sort de la tolerance : 0', 'BP rang  3 : deposee +0.0996 ; variantes de +0.0684 a +0.1221')
note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note):
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for x in ('879ea2e51c7d7f4f', '408b8a595cad0040', 'c5d8fd0313217569', 'b57c9ccdd3946261', '1.987, 1.993, 2.006, 2.017', '252 cellules sur 252', '14 ont AU MOINS UNE', '662 Mo'):
    if x not in re.sub(r'\s+', ' ', note):
        arrets.append('la note ne porte pas %r' % x)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION de machine 2 de la PREMIERE PARTIE du gel "largeur du vide" (b57c9ccdd3946261) : ma table des 252 cellules (identique a celle de machine 1), la table commune, mon tirage, mon balayage, '
    'les boites jusqu\'a N = 166 ; l\'authentification des trois lots de l\'enveloppe 16f ; mon rejeu de la note sur le vide et ce que j\'y ai trouve en plus. Aucune 2D du systeme a fantome, aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le gel partie 1 b57c9ccdd3946261 (lot 879ea2e51c7d7f4f) ; la note sur la loi d'echelle (lot 408b8a595cad0040) ; la note sur le vide (lot c5d8fd0313217569) ; le registre en tete dee73bd (lu, non ecrit)\n")
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
