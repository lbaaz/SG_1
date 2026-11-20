# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'CERTIFICATION DU GEL PONT, PREMIERE PARTIE' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-17. Meme squelette que fabrique_lot_grandes_boites_machine2_v1.py (non edite).
Aucune 2D a un w2 candidat ; aucun depot ; aucune graine n'existe.
Usage : py -3.11 -I fabrique_lot_certification_gel_pont_partie1_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; chaque nombre cite par la note est RELU dans le journal qui le porte (et doit etre dans la note) ; les deux journaux de mutations sont INSERES tels quels
dans la note ; la note est ASCII (verifie AVANT d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ; aucune fuite de vie privee (identifiant du poste, prenom, nom, messagerie,
chemins personnels, lecteurs de disque) ; LF dans les .py et .md ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'certif_gel_pont_partie1_machine2/'
NOM = 'lot_machine2_2026-11-17_certification_gel_pont_partie1_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_pont_partie1_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_pont_partie1_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_pont_partie1_machine2_v1.py'
PIECES = [D + n for n in (
    'authentifie_envoi_m1_machine2_v1.py', 'authentification_enveloppe_m1_17a_machine2_v1.log',
    'controles_rapides_machine2_v1.py', 'controles_rapides_machine2_v1.log',
    'eligibilite_pont_machine2_v1.py', 'eligibilite_pont_machine2_v1.log', 'table_eligibilite_pont_machine2_v1.json', 'details_eligibilite_pont_machine2_v1.json', 'cache_gamma_hp_pont_machine2_v1.json',
    'verification_finale_reference_machine2_v1.log', 'eligibilite_pont_machine2_v1_premier_passage_gamma_double.log', 'table_eligibilite_pont_machine2_v1_premier_passage_gamma_double.json', 'details_eligibilite_pont_machine2_v1_premier_passage_gamma_double.json',
    'compare_passages_gamma_machine2_v1.py', 'compare_passages_gamma_machine2_v1.log',
    'confronte_tables_pont_machine2_v1.py', 'confrontation_tables_pont_machine2_v1.log', 'table_commune_pont_v1.json', 'canon_table_commune_machine2_v1.py', 'canon_table_commune_pont_machine2_v1.log',
    'confronte_synthese_section7_machine2_v1.py', 'confrontation_synthese_section7_machine2_v1.log', 'confrontation_synthese_section7_machine2_v1_premier_passage_rho_sans_delta.log', 'matrice_mutations_synthese_machine2_v1.log',
    'marges_pont_machine2_v1.py', 'marges_pont_machine2_v1.log', 'verif_rho_precision_machine2_v1.py', 'verif_rho_precision_machine2_v1.log', 'robustesse_g_machine2_v1.py', 'robustesse_g_machine2_v1.log',
    'matrice_mutations_pont_machine2_v1.py', 'matrice_mutations_pont_machine2_v1.log',
    'tirage_pont_machine2_v1.py', 'tirage_pont_machine2_v1_demonstration.log', 'differentiel_tirage_machine2_v1.py', 'differentiel_tirage_machine2_v1.log', 'matrice_mutations_tirage_machine2_v1.log',
    'balayage_virginite_pont_machine2_v1.py', 'balayage_virginite_pont_machine2_v1.log', 'balayage_virginite_anciennes_sessions_machine2_v1.log',
    'contexte_touches_machine2_v1.py', 'contexte_touches_machine2_v1.log', 'triage_virginite_machine2_v1.py', 'triage_virginite_machine2_v1.log', 'triage_virginite_anciennes_sessions_machine2_v1.log',
    'rejeu_scripts_m1/compare_rejeu_json_machine2_v1.py', 'rejeu_scripts_m1/compare_rejeu_json_machine2_v1.log', 'rejeu_scripts_m1/compare_journaux_rejeu_machine2_v1.py', 'rejeu_scripts_m1/compare_journaux_rejeu_machine2_v1.log',
    'rejeu_scripts_m1/eligibilite_pont_MG_PG_rejeu_m2.json', 'rejeu_scripts_m1/eligibilite_pont_MG_PG_rejeu_m2.log', 'rejeu_scripts_m1/essai_avx512.json', 'rejeu_scripts_m1/essai_avx2_avx512.json',
    'rejeu_scripts_m1/essai_tout_sauf_sse.json', 'rejeu_scripts_m1/diff_log_levier.txt', 'rejeu_scripts_m1/diff_log_sans_levier.txt', 'rejeu_scripts_m1/tirage_autotest_rejeu_m2.log',
    'rejeu_scripts_m1/tirage_demo_rejeu_m2_sa_table.log', 'rejeu_scripts_m1/tirage_demo_rejeu_m2_table_commune.log',
    'faisabilite/boite300_4barreaux.jsonl', 'faisabilite/boite300_4barreaux.log', 'faisabilite/boite300_5barreaux.jsonl', 'faisabilite/boite300_5barreaux.log',
    'faisabilite/faisabilite_niveaux_non_fiables_machine2_v1.log', 'faisabilite/pic_memoire_boites300.txt', 'faisabilite/temps_factorisation_absorbeur_machine2_v1.py', 'faisabilite/temps_factorisation_absorbeur_machine2_v1.log')] + [SELF]
NOMBRES = [
    ('authentification_enveloppe_m1_17a_machine2_v1.log', 'CANON du manifeste : 55612644fc4ca279 | canon(s) annonce(s) par l ENVOI : [\'55612644fc4ca279\']'),
    ('authentification_enveloppe_m1_17a_machine2_v1.log', 'MORSURES : 0'),
    ('controles_rapides_machine2_v1.log', 'sha256("DEMONSTRATION|MG|0") = 8254e7d473dd8e66... ; modulo 8 = 5 -> w2 = 1.987'),
    ('controles_rapides_machine2_v1.log', 'MG : 8 w2 : 1.981 1.983 1.984 1.985 1.986 1.987 1.988 1.989 | identique a la liste du gel : True'),
    ('controles_rapides_machine2_v1.log', 'm = 3 : g = 5.53067e-03'),
    ('controles_rapides_machine2_v1.log', '(3/8)^5 = 0.0074 (gel : 0.0074)'),
    ('controles_rapides_machine2_v1.log', 'canon de mon lot (manifeste) : dce7431e7a8b4a8c (gel : dce7431e7a8b4a8c)'),
    ('confrontation_tables_pont_machine2_v1.log', '48 cellules : moi 48, lui 48 ; memes cles : True'),
    ('confrontation_tables_pont_machine2_v1.log', '2. COUPLAGES ECRITS : 0 cellules avec un g different'),
    ('confrontation_tables_pont_machine2_v1.log', '3. ELIGIBILITE PAR CELLULE : 0 cellules ou nos eligibilites different'),
    ('confrontation_tables_pont_machine2_v1.log', '144 nombres sur 144 identiques a 4 decimales'),
    ('confrontation_tables_pont_machine2_v1.log', '6. TABLE COMMUNE : MG : 5 eligibles sur 8 ; PG : 8 eligibles sur 8'),
    ('confrontation_tables_pont_machine2_v1.log', 'MG eligibles : 397/200 993/500 1987/1000 497/250 1989/1000'),
    ('canon_table_commune_pont_machine2_v1.log', 'canon B de ma table commune (octets du fichier) : 0c10ddbf2813d809 ; canon B du sous-ensemble de la sienne : 0c10ddbf2813d809'),
    ('canon_table_commune_pont_machine2_v1.log', 'serialisation (indent=1, cles triees, LF) de son sous-ensemble == octets de mon fichier : True'),
    ('verification_finale_reference_machine2_v1.log', 'eligibilite_pont_machine2_v1.log identique : True'),
    ('confrontation_synthese_section7_machine2_v1.log', '48 nombres de synthese sur 48 identiques a la precision imprimee par le gel'),
    ('confrontation_synthese_section7_machine2_v1_premier_passage_rho_sans_delta.log', '36 nombres de synthese sur 48 identiques a la precision imprimee par le gel'),
    ('matrice_mutations_synthese_machine2_v1.log', 'e_bord_sans_sigma            44 nombres de synthese sur 48 identiques a la precision imprimee par le gel'),
    ('compare_passages_gamma_machine2_v1.log', 'cellules dont l etendue au vide change de plus de 5e-5 entre double precision et precision etendue : 20 sur 48, toutes a 4/5 barreaux'),
    ('compare_passages_gamma_machine2_v1.log', 'tables d eligibilite (section 5) identiques entre les deux passages : True'),
    ('marges_pont_machine2_v1.log', 'ecarte 6 cellule(s)'),
    ('marges_pont_machine2_v1.log', 'w2 ecartes : 1.981 1.983 1.984'),
    ('marges_pont_machine2_v1.log', 'ecart relatif maximal de Gamma lu en double precision (-2 Im E) a la precision etendue : 6.84e-03'),
    ('verif_rho_precision_machine2_v1.log', '144 lectures comparees ; plus grande erreur relative : directe en double precision 2.51e-15 ; flux 2.68e-15'),
    ('robustesse_g_machine2_v1.log', 'couplage ecrit different entre |float(w2) - 2.0| et float(|w2 - 2|) : 0 ; entre X(w2) en Fraction et en float : 0'),
    ('differentiel_tirage_machine2_v1.log', '(a) table commune : 200000 graines ; desaccords : 0 ; PAS DE GEL : 1531 (0.0077)'),
    ('differentiel_tirage_machine2_v1.log', '(b) 300 tables aleatoires x 200 graines = 60000 tirages ; desaccords : 0 ; PAS DE GEL : 12926 (0.215)'),
    ('balayage_virginite_pont_machine2_v1.log', 'fichiers lus (zips deplies) : 27694 ; octets : 1080969808'),
    ('balayage_virginite_pont_machine2_v1.log', 'fichiers touches : 288'),
    ('balayage_virginite_anciennes_sessions_machine2_v1.log', 'fichiers lus (zips deplies) : 49824 ; octets : 1262092427'),
    ('balayage_virginite_anciennes_sessions_machine2_v1.log', 'fichiers touches : 439'),
    ('triage_virginite_machine2_v1.log', 'fichiers touches classes : A (gel du vide, 1D) 117 ; B (present gel, present lot, mes certifications du pont) 31 ; C (coincidences numeriques) 98 ; D (explorations anciennes 1D / lots certifies) 42'),
    ('triage_virginite_anciennes_sessions_machine2_v1.log', 'fichiers touches classes : A (gel du vide, 1D) 46 ; B (present gel, present lot, mes certifications du pont) 0 ; C (coincidences numeriques) 236 ; D (explorations anciennes 1D / lots certifies) 157'),
    ('triage_virginite_anciennes_sessions_machine2_v1.log', 'NON CLASSES : 0'),
    ('rejeu_scripts_m1/compare_rejeu_json_machine2_v1.log', 'champs non flottants differents : 0 ; flottants : 2098 compares, 1982 differents, plus grand ecart relatif 9.03e-07'),
    ('rejeu_scripts_m1/compare_journaux_rejeu_machine2_v1.log', 'tirage_pont_machine1_v1_autotest.log contre tirage_autotest_rejeu_m2.log : octets identiques False ; aux fins de ligne pres True ; lignes differentes 0 dont hors durees et nom de fichier 0'),
    ('faisabilite/pic_memoire_boites300.txt', 'duree totale des deux boites en parallele : 157 s ; pic de memoire des processus python (somme) : 1,92 Go'),
    ('faisabilite/boite300_4barreaux.log', '300 90000 0.99958770 19 19 1.0423 5.769 40/40 104'),
    ('faisabilite/boite300_5barreaux.log', '300 90000 0.99974240 19 18 1.1123 7.661 80/40 151'),
    ('faisabilite/faisabilite_niveaux_non_fiables_machine2_v1.log', 'NON FIABLE : ecart au vide -6.699 |delta| ; y1 = 5.313e-02 ; y2 = 5.453e-02 ; ecart relatif 2.6 pour cent'),
    ('faisabilite/temps_factorisation_absorbeur_machine2_v1.log', '104 10816 1.4 2.9 0.02 110'),
    ('faisabilite/temps_factorisation_absorbeur_machine2_v1.log', '128 16384 2.2 9.0 0.03 217'),
    ('faisabilite/temps_factorisation_absorbeur_machine2_v1.log', '158 24964 3.3 21.5 0.03 388'),
]
INSERTIONS = {'@@MUTATIONS@@': 'matrice_mutations_pont_machine2_v1.log', '@@MUTATIONS_TIRAGE@@': 'matrice_mutations_tirage_machine2_v1.log', '@@MUTATIONS_SYNTHESE@@': 'matrice_mutations_synthese_machine2_v1.log'}
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


TERMES = [''.join(p) for p in (('ba', 'zil'), ('le', 'beau'), ('gm', 'ail'), ('hot', 'mail'), ('Us', 'ers\\'), ('Us', 'ers/'), ('App', 'Data'), ('.cla', 'ude\\'), ('.cla', 'ude/'), ('Down', 'loads'))]


def fuites(nom, octets):
    t = octets.decode('latin-1').lower()
    out = [(nom, w) for w in TERMES if w.lower() in t]
    out += [(nom, m) for m in re.findall(r'(?<![a-z0-9])[a-z]:[\\/]', t)]
    out += [(nom, m) for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', t)]
    return out


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
note = lit(NOTE)
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
for ph, j in INSERTIONS.items():
    if ph in note:
        bloc = '\n'.join('    ' + l.rstrip() for l in lit(D + j).replace('\r\n', '\n').split('\n') if l.strip())
        note = note.replace(ph, bloc)
nn = norm(note)
for j, s in NOMBRES:
    if norm(s) not in norm(lit(D + j)):
        arrets.append('le journal %s ne porte pas %r' % (j, s))
    if norm(s) not in nn:
        arrets.append('la note ne porte pas %r' % s)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
elif not arrets:
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for p in PIECES + [NOTE]:
    brut = open(os.path.join(ICI, p), 'rb').read()
    for f in fuites(p, brut):
        arrets.append('FUITE de vie privee : %s' % (f,))
    if b'\r' in brut and p.endswith(('.py', '.md', '.json')):
        arrets.append('fins de ligne CRLF dans %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION par machine 2 du gel "pont", premiere partie (regle de tirage et d\'eligibilite, canon 735ce41be200c5cd, lot de machine 1 55612644fc4ca279) : ma table des 48 cellules ecrite depuis le texte seul, '
    'sa confrontation a celle de machine 1, la table commune, le tirage (differentiel, mutations), le balayage de virginite, le rejeu de ses scripts, la faisabilite sur BOCAL4. AUCUNE 2D a un w2 candidat ; aucun depot ; aucune graine. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le lot de machine 1 lot_machine1_2026-11-17_gel_pont_partie1_regle_tirage_v1 (55612644fc4ca279, authentifie, 66 pieces, 0 morsure) ; le registre public en tete 2988237 (clone frais sur D:, lu, non ecrit)\n")
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
