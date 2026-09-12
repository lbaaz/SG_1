#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LE LOT DE RE-LIVRAISON -- assemblage. machine 2, v2, 12/09/2026.

Le conteneur de machine 1 est reinitialise : elle ne detient plus le fond. Sa note
`a37c86b0e9b80833` section 6 donne la liste. Cette feuille l'ASSEMBLE.

POURQUOI UNE v2 (la v1 n'a jamais ete emise ; son log mordant est garde comme trace) :
  -- le premier jeu de la v1 lisait les manifestes par un motif de COLONNES et versait
     ZERO piece pour quatre lots, en silence (aucun controle ne le voyait) ;
  -- la v1 corrigee (jetons de 16 hex + nom de fichier, sans presumer du format) a MORDU
     sur 2 controles / 9 : elle lisait TOUTE ligne portant un jeton et un nom comme une
     piece du lot. Or un manifeste porte DEUX sortes de lignes : les lignes de TABLE
     (elles commencent par un jeton hex : une piece DU lot, a cote de son manifeste) et
     les lignes de CITATION (entrants, prose : une piece d'un AUTRE lot, qui vit
     ailleurs au poste). Les cinq morsures etaient cinq citations lues comme des pieces.
  -- ici : une piece de TABLE se resout A COTE du manifeste, canon dans SA ligne ; une
     CITATION se resout PAR CANON N'IMPORTE OU AU POSTE (D-ACA-5), et si sa ligne ne
     porte pas son canon, elle est dite CITEE PAR NOM SEUL -- declaree, jamais tue.
  -- et un premier jeu de CETTE v2 a passe 11/11 en PERDANT UNE PIECE EN SILENCE : la
     prose d'un manifeste citait sa propre garde AVANT la table, la passe unique marquait
     le nom comme vu, et la ligne de table etait sautee (table 3 pour un lot qui declare
     4). Corrige en DEUX PASSES (table d'abord, citations ensuite) et, surtout, par le
     controle qui aurait mordu : le compte de table EGALE le `pieces : N` ecrit dans le
     manifeste -- le compte attendu se lit A LA SOURCE, il ne se devine pas.

Les regles nees du jour, appliquees :
  -- RESOLUTION PAR CANON, JAMAIS PAR NOM (`D-ACA-5`).
  -- CHAQUE PIECE EST VERIFIEE CONTRE LE MANIFESTE DE SON LOT avant d'entrer.
  -- DEUX VERBES (`D-ACA-7`) : `chk` mesure et compte, `note` porte la prose.
  -- LE COMPTE EST ETABLI APRES LE DERNIER AJOUT.
  -- LES LIGNES DE PROVENANCE PARLENT DE CE LOT-CI (`D-ACA-6`).
  -- CE QUI NE RESOUT PAS EST NOMME, jamais tu.

L'ARBRE EST PRESERVE : le zip reproduit les chemins relatifs a BOCAL4, pour que les
feuilles (qui lisent en relatif) se rejouent apres un simple depliage.
PB-1 : aucune piece n'est editee ; tout est lu et copie tel quel.
Cette feuille et son log sont livres A COTE du zip (le log s'ecrit apres lui).
"""
import hashlib, os, re, sys, unicodedata, zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
ZIP = os.path.join(RAC, 'lot_machine2_2026-09-12_RELIVRAISON_v1.zip')
MAN = 'MANIFEST_lot_machine2_RELIVRAISON_v1.txt'
OK = []


def chk(n, c, d=''):
    """MESURE. Compte au bilan. Sa condition n'est jamais une constante."""
    OK.append((n, bool(c)))
    print('  [%s] %-52s %s' % ('PASSE' if c else 'MORD ', n[:52], d))


def note(n, d=''):
    print('  [ note] %-52s %s' % (n[:52], d))


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8'))
        t = t.replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
        return (hashlib.sha256(t).hexdigest()[:16],
                hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw))
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return (h, h, len(raw), len(raw))


_EMP = {}


def emp_de(p):
    if p not in _EMP:
        _EMP[p] = emp(open(p, 'rb').read())
    return _EMP[p]


def rel(p):
    return os.path.relpath(p, RAC).replace('\\', '/')


# --------------------------------------------------------------------
# CE QUE SA SECTION 6 DEMANDE, PAR CANON. Le nom n'est jamais la cle.
# --------------------------------------------------------------------
LOTS = [
    ('d5ace962a3a6e413', 'gel constante A v5 (machine 1)'),
    ('13d2973b0e143a20', 'ma certification du v5, 104/104'),
    ('a4c35a2ee691c9a7', 'la chaine, 8 pieces (porte le banc v8 CERTIFIE)'),
    ('7883311c6e363b02', 'tenaille v1 + comparaison a trois'),
    ('2b155abffbe4f6ff', 'geste (2) m1 -- convergence dt 7|1.73'),
    ('117bcfaa1f283059', 'geste (2) m1 -- cause de l ecart'),
    ('5ea2fa8d7457a125', 'geste (2) m1 -- reponse cas durs'),
    ('ca5456d3b11df0be', 'geste (2) m1 -- reponse globale (ses deux JSON)'),
    ('4cb991ce22ca35d0', 'geste (2) m1 -- cloture'),
    ('1859bbc126bb52c7', 'geste (2) m1 -- erratum de cloture'),
    ('eb7fb1cefbf2cec4', 'geste (2) m2 -- rejeu convergence'),
    ('f9e1c1922e32220d', 'geste (2) m2 -- cas durs'),
    ('3675daba802cbc6c', 'geste (2) m2 -- reponse globale'),
    ('cd70cda556d60380', 'geste (2) m2 -- cloture'),
    ('e3b707c589e9d1d8', 'm2 -- acte constante A v1'),
    ('56378e0f371f9681', 'm2 -- reponse a sa lecture'),
    ('1985ad4eea984bf5', 'm2 -- reponse R-G2-5'),
    ('5c84c48e9a9c72eb', 'm2 -- cloture du tour'),
    ('b228e0f5a0197494', 'm1 -- lecture de l ouverture + SUIVI 28b'),
    ('25b6f78bdf2ddcff', 'm1 -- lecture de la reponse + R-G2-5 v1'),
    ('990a8fe5cec6ef87', 'm1 -- R-G2-5 v2 + garde chk constante'),
]

# Le FOND : ce que les feuilles LISENT et qui ne vit dans aucun lot.
FOND = [
    'm2_v8_prevol_temoin_resultats.json',
    'm2_v8_prevol_temoin.log',
    'prevol_temoin_v8_machine1.log',
    os.path.join('registre', 'runs', 'run_temoin_delta85', 'resultats_temoin.json'),
    os.path.join('registre', 'runs', 'run_alpha_delta85', 'resultats_alpha.json'),
    'banc_qualification_machine1_v3.py',
    'banc_qualification_machine1_v8.py',
    'm2_run_temoin_reel.log',
    'm2_run_alpha_reel.log',
]

# =====================================================================
print("\n1. RESOLUTION DES 21 LOTS -- PAR CANON, PAS PAR NOM (D-ACA-5)")
# =====================================================================
# Un seul balayage du poste : index par NOM de tout fichier (hors __pycache__ et .git du
# clone de registre) ; les canons sont calcules a la demande, jamais deux fois.
par_nom, index, n_txt = {}, {}, 0
for d, dn, fs in os.walk(RAC):
    dn[:] = [x for x in dn if x not in ('__pycache__', '.git')]
    for f in fs:
        p = os.path.join(d, f)
        par_nom.setdefault(f, []).append(p)
        if f.endswith('.txt'):
            n_txt += 1
            try:
                index.setdefault(emp_de(p)[0], p)
            except OSError:
                continue
resolus = [(h, l, index[h]) for h, l in LOTS if h in index]
absents = [(h, l) for h, l in LOTS if h not in index]
chk('les %d lots demandes resolvent tous par canon' % len(LOTS), not absents,
    '%d manifestes balayes ; absents : %s'
    % (n_txt, ','.join(h for h, _ in absents) or 'aucun'))
note('rappel de forme', 'un des 21 ne vivait QUE dans un zip -- installe avant ce jeu')

# =====================================================================
print("\n2. LES PIECES DE CHAQUE LOT -- TABLE A COTE DU MANIFESTE, CITATIONS PAR CANON")
# =====================================================================
HEX = re.compile(r'\b[0-9a-f]{16}\b')
NOM = re.compile(r'[\w.\-+@]+\.(?:md|py|log|json|txt|zip|csv|npz|png)\b')
TABLE = re.compile(r'^[0-9a-f]{16}\s')
PIECES = re.compile(r'^pieces\s*:\s*(\d+)\b', re.M)
retenues, ecarts, introuvables, vides, faux_comptes, sans_compte = [], [], [], [], [], []
cit_canon, cit_nom, cit_perdues = [], [], []
for h, lib, chemin in resolus:
    d = os.path.dirname(chemin)
    retenues.append(rel(chemin))
    texte = open(chemin, encoding='utf-8').read()
    lignes_m = [(l, HEX.findall(l), NOM.findall(l)) for l in texte.split('\n')]
    lignes_m = [(l, j, n) for l, j, n in lignes_m if j and n]
    n_tab, n_cit, vus = 0, 0, set()
    # PASSE 1 -- LIGNES DE TABLE : une piece DU lot. Elle vit a cote de son manifeste et
    # son canon est dans SA ligne. Sinon : ecart ou introuvable, et c'est une morsure.
    # La table passe AVANT les citations : une piece du lot citee dans la prose du meme
    # manifeste reste une piece du lot.
    for l, jetons, noms in lignes_m:
        if not TABLE.match(l):
            continue
        nom = noms[0]
        if nom in vus:
            continue
        p = os.path.join(d, nom)
        if not os.path.exists(p):
            introuvables.append('%s : %s' % (h, nom))
            continue
        e = emp_de(p)
        if e[0] not in jetons and e[1] not in jetons:
            ecarts.append('%s : %s' % (h, nom))
            continue
        vus.add(nom)
        n_tab += 1
        retenues.append(rel(p))
    # PASSE 2 -- LIGNES DE CITATION : une piece d'un AUTRE lot. Elle se resout PAR CANON,
    # n'importe ou au poste. Si sa ligne ne porte pas son canon, elle est citee PAR NOM
    # SEUL : declaree, et couverte ou non par un homonyme au poste.
    for l, jetons, noms in lignes_m:
        if TABLE.match(l):
            continue
        for nom in dict.fromkeys(noms):
            if nom == os.path.basename(chemin) or nom in vus:
                continue
            cands = [p for p in par_nom.get(nom, [])
                     if emp_de(p)[0] in jetons or emp_de(p)[1] in jetons]
            vus.add(nom)
            if cands:
                n_cit += 1
                retenues.append(rel(cands[0]))
                cit_canon.append('%s : %s' % (h, nom))
            elif nom in par_nom:
                cit_nom.append('%s : %s' % (h, nom))
            else:
                cit_perdues.append('%s : %s' % (h, nom))
    if not n_tab:
        vides.append(h)
    # LE COMPTE ATTENDU SE LIT A LA SOURCE : la ligne `pieces : N` du manifeste.
    m = PIECES.search(texte)
    attendu = int(m.group(1)) if m else None
    if attendu is None:
        sans_compte.append(h)
    elif attendu != n_tab:
        faux_comptes.append('%s : table %d, declare %d' % (h, n_tab, attendu))
    print('   %-16s %-40s table %2d / declare %-4s citations resolues %2d'
          % (h, lib[:40], n_tab, attendu if attendu is not None else '?', n_cit))
# LE CONTROLE QUI MANQUAIT AU PREMIER JEU : rien ne pouvait voir qu'un lot versait ZERO
# piece. Mordrait si un seul lot n'apportait que son manifeste.
chk('chaque lot verse au moins une piece de table', not vides, ','.join(vides) or '0 lot vide')
# LE CONTROLE QUI MANQUAIT AU PREMIER JEU DE LA v2 : le compte de table egale le compte
# que le manifeste DECLARE. Mordrait sur une piece de table perdue en silence.
chk('le compte de table egale le `pieces : N` de chaque manifeste', not faux_comptes,
    '; '.join(faux_comptes) or '21 lots au compte declare')
chk('chaque manifeste declare son compte `pieces : N`', not sans_compte,
    ','.join(sans_compte) or '0 sans compte')
chk('aucune piece de table ne s ecarte de son manifeste', not ecarts,
    ','.join(ecarts[:4]) or '0 ecart')
chk('aucune piece de table n est introuvable a cote', not introuvables,
    ','.join(introuvables[:4]) or '0 introuvable')
chk('%d citations resolues par canon au poste' % len(cit_canon), bool(cit_canon),
    '; '.join(cit_canon))
# Une citation par nom seul n'est pas verifiable par canon : on le dit. Elle MORD si le
# nom n'existe nulle part au poste (une piece dont les manifestes parlent et que
# personne n'a) ; sinon elle est declaree, avec sa couverture par le perimetre retenu.
chk('aucune citation par nom seul sans homonyme au poste', not cit_perdues,
    ','.join(cit_perdues[:4]) or '0 perdue')

# =====================================================================
print("\n3. LE FOND -- CE QUE LES FEUILLES LISENT ET QUI N EST DANS AUCUN LOT")
# =====================================================================
manque = [f for f in FOND if not os.path.exists(os.path.join(RAC, f))]
for f in FOND:
    p = os.path.join(RAC, f)
    if os.path.exists(p):
        retenues.append(rel(p))
        print('   %-16s %8d o  %s' % (emp_de(p)[0], os.path.getsize(p), rel(p)))
chk('les %d pieces de fond sont au poste' % len(FOND), not manque,
    ','.join(manque) or '0 manquante')

retenues = sorted(set(retenues))
bases = set(os.path.basename(r) for r in retenues)
couvertes = [c for c in cit_nom if c.split(' : ')[1] in bases]
non_couv = [c for c in cit_nom if c.split(' : ')[1] not in bases]
note('%d citations par nom seul, couvertes par un homonyme retenu' % len(couvertes),
     '; '.join(couvertes))
note('%d citations par nom seul, homonyme au poste NON retenu' % len(non_couv),
     '; '.join(non_couv) or 'aucune')

# =====================================================================
print("\n4. LE ZIP -- ARBRE PRESERVE, POUR QUE LES FEUILLES SE REJOUENT")
# =====================================================================
doublons = len(retenues) != len(set(x.lower() for x in retenues))
chk('aucun doublon de chemin dans le perimetre', not doublons, '%d chemins' % len(retenues))
lignes = [emp_de(os.path.join(RAC, r)) + (r,) for r in retenues]

corps = ("MANIFESTE lot_machine2_2026-09-12_RELIVRAISON_v1 -- LE FOND ENTIER, RE-EMIS A "
         "MACHINE 1 (conteneur reinitialise) ; machine 2, classe 3\n"
         "OBJET : sa note a37c86b0e9b80833 section 6. Elle ne detient plus le fond ; sans "
         "lui, aucune mesure n'est possible d'aucun cote. Ce lot le rend ENTIER.\n"
         "RESOLUTION PAR CANON, JAMAIS PAR NOM (D-ACA-5) : les 21 lots demandes ont ete "
         "retrouves en recalculant le canon de tous les manifestes du poste. Un d'entre "
         "eux (4cb991ce22ca35d0) ne vivait QUE dans son zip, jamais extrait -- il est "
         "installe et joint ; fait verse, un balayage de disque ne voit pas une piece "
         "restee dans une archive.\n"
         "DEUX SORTES DE LIGNES DANS UN MANIFESTE : les lignes de TABLE (une piece DU lot, "
         "verifiee A COTE de son manifeste, canon dans sa ligne, B ou brut) et les lignes "
         "de CITATION (entrants, prose : une piece d'un AUTRE lot, resolue par CANON "
         "n'importe ou au poste). Aucune piece n'entre sur son nom. Les citations dont la "
         "ligne ne porte pas le canon sont dites CITEES PAR NOM SEUL et declarees dans le "
         "log de la feuille d'assemblage.\n"
         "L'ARBRE EST PRESERVE : les chemins sont relatifs a BOCAL4, pour que derivation "
         "v3, relecture v1 et R-G2-5 v2 se rejouent apres un simple depliage, sans "
         "reecrire une ligne.\n"
         "PB-1 : aucune piece n'est editee ; tout est copie tel quel, y compris les octets "
         "CRLF des .log de ce poste.\n"
         "colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  "
         "octets_bruts  chemin (relatif a BOCAL4)\n"
         "Le CANON du lot est l'empreinte de CE manifeste ; il ne se porte pas lui-meme.\n\n")
for B, br, oB, obr, r in lignes:
    corps += "%s %s %9d %9d  %s\n" % (B, br, oB, obr, r)
corps += ("\nentrants : les 21 lots de sa section 6 et des trois tours du jour, tous "
          "resolus par CANON au poste ; le fond lu en place (pre-vols, journaux, runs du "
          "registre, bancs v3 et v8, captures du delta 85)\n")
corps += "pieces : %d (compte etabli APRES le dernier ajout)\n" % len(lignes)
corps += ("bilan de la feuille d'assemblage : assemblage_relivraison_machine2_v2.py et "
          "son .log, livres A COTE du zip (le log s'ecrit apres lui) ; la v1 et son log "
          "mordant (7/9) sont gardes au poste comme trace et ne sont pas emis\n")

open(os.path.join(ICI, MAN), 'w', encoding='utf-8', newline='\n').write(corps)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(ICI, MAN), MAN)
    for r in retenues:
        z.write(os.path.join(RAC, r), r)

# Relecture du zip : on ne croit pas l'ecriture, on la relit.
with zipfile.ZipFile(ZIP) as z:
    dedans = [i.filename for i in z.infolist()]
    faux = [r for r in retenues if z.read(r) != open(os.path.join(RAC, r), 'rb').read()]
chk('le zip porte le manifeste plus les %d pieces' % len(retenues),
    len(dedans) == len(retenues) + 1, '%d entrees' % len(dedans))
chk('chaque piece du zip est BIT-IDENTIQUE a celle du poste', not faux,
    ','.join(faux[:3]) or '0 ecart sur %d' % len(retenues))

cn = emp(open(os.path.join(ICI, MAN), 'rb').read())[0]
chk('le manifeste ne se porte pas lui-meme', cn not in corps, cn)

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('CANON DU LOT : %s   ZIP brut %s   %d pieces, %.1f Mo'
      % (cn, hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()[:16],
         len(retenues), os.path.getsize(ZIP) / 1048576.0))
print('=====================================================================')
sys.exit(0 if k == n else 1)
