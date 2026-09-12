#!/usr/bin/env python3
# -*- coding: ascii -*-
"""DECISION (v) -- LA PIECE, SON OBJET, ET LA QUESTION DE CLAUSE. machine 2, 12/09/2026.

Machine 1 a retrouve `SUIVI_campagne_2026-08-28b.md` et l'a re-emis octet pour octet.
L'objet de (v) est sa SECTION 2. Cette feuille fait trois choses, et aucune sur citation :

  1. AUTHENTIFIE la piece contre l'annonce du GEL COURANT -- pas contre sa parole.
  2. VERIFIE sa section 2 AU POSTE : les deux captures du delta 85 sont-elles vraiment en
     octets CRLF, leur sha256 brut est-il celui qu'elle annonce, et la transformation
     CRLF -> LF reproduit-elle exactement les empreintes citees a l'acte ?
  3. REPOND A SA QUESTION DE CLAUSE, ET ELLE A DEMANDE QU'ON LA VERIFIE "AU TEXTE, PAS
     DEPUIS LA MEMOIRE" : la regle d'ecriture "toute transformation CRLF -> LF est
     declaree a l'application" figure-t-elle au texte qui porte la convention B ? Si oui
     elle est acquise ; sinon elle est la QUATRIEME candidate sous (X).

PB-1 : rien n'est edite. Les captures du delta 85 sont lues, jamais reecrites.
"""
import hashlib, os, re, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-54s %s' % ('PASSE' if c else 'MORD ', n[:54], d))


def emp(p):
    raw = open(p, 'rb').read()
    t = unicodedata.normalize('NFC', raw.decode('utf-8'))
    t = t.replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
    return (hashlib.sha256(raw).hexdigest()[:16],
            hashlib.sha256(t).hexdigest()[:16], raw)


# =====================================================================
print("\n1. LA PIECE -- AUTHENTIFIEE CONTRE LE GEL COURANT, PAS CONTRE SA PAROLE")
# =====================================================================
S28B = P('entrant_machine1_2026-09-12_lecture_acte', 'SUIVI_campagne_2026-08-28b.md')
brut, b, raw = emp(S28B)
chk('le 28b resout a b6d13e6a1559e850', b == 'b6d13e6a1559e850', b)
chk('il fait 5639 octets, ASCII, LF, newline final',
    len(raw) == 5639 and all(c < 128 for c in raw) and b'\r' not in raw
    and raw.endswith(b'\n'), '%d octets, %d CR' % (len(raw), raw.count(b'\r')))
chk('brut == convention B (le fichier est LF)', brut == b, brut)
gel = open(P('entrant_machine1_2026-09-09_constante_A_v5',
             'constante_A_pre_enregistrement_v5.md'), encoding='utf-8').read()
chk('et cette empreinte est CELLE QUE LE GEL COURANT ANNONCE',
    'b6d13e6a1559e850' in gel and 'SUIVI_campagne_2026-08-28b.md' in gel,
    'constante_A_pre_enregistrement_v5.md')
# Mordrait si la piece re-emise ne portait pas l'objet que (v) lui attribue.
txt = raw.decode('ascii')
chk('sa section 2 porte bien le fait de forme de (v)',
    '2. UN FAIT DE FORME, RELEVE' in txt and 'E18' in txt and 'CRLF' in txt,
    'numerotation proposee : E18')

# =====================================================================
print("\n2. SA SECTION 2, VERIFIEE AU POSTE -- LES DEUX CAPTURES DU DELTA 85")
# =====================================================================
CAPTURES = (('m2_run_temoin_reel.log', '3833ba551a390945', '10a7ce5688f515d5'),
            ('m2_run_alpha_reel.log', '717b61caa5921aaa', '0e7e56006d2e200a'))
for nom, ab, an in CAPTURES:
    f = P(nom)
    if not os.path.exists(f):
        chk('%s est au poste' % nom, False, 'ABSENTE')
        continue
    br, bb, r = emp(f)
    chk('%-22s octets CRLF' % nom, r.count(b'\r') > 0, '%d CR' % r.count(b'\r'))
    chk('%-22s sha256 brut == son annonce' % nom, br == ab, br)
    chk('%-22s CRLF->LF reproduit la citation de l acte' % nom, bb == an, bb)
    chk('%-22s et le brut NE la reproduit PAS' % nom, br != an,
        'c est tout le fait de forme')

# =====================================================================
print("\n3. SA QUESTION DE CLAUSE -- REPONDUE AU TEXTE, PAS DEPUIS LA MEMOIRE")
# =====================================================================
# Elle ecrit : la regle est "deja acquise si la clause figure au texte qui porte la
# convention B". On cherche donc la CLAUSE, pas la convention. Issue qui ferait mordre :
# un seul texte la portant -- la regle serait acquise et il n'y aurait rien a verser.
# Les limites de mot ne sont PAS decoratives : sans le \b, "forme a la citation" matche
# a l'interieur de "conforme a la citation" -- ce qui s'est produit au premier jeu, sur
# m17_pre_enregistrement_quantique_v3.md, ou la phrase parle d'un RENOMMAGE. Le controle
# a donc deja mordu une fois, de ma main : l'issue qui le fait mordre est ecrivable.
CLAUSE = re.compile(r'(declar\w+.{0,40}(CRLF|transformation)'
                    r'|(CRLF|transformation).{0,40}declar\w+'
                    r'|\bdeclare sa forme|\bforme a la citation)', re.I)
mds, porteurs, clauses = [], [], []
for d, _, fs in os.walk(RAC):
    if os.sep + 'ACTE_constante_A' in d or 'lecture_acte' in d:
        continue
    for f in fs:
        if not f.endswith('.md'):
            continue
        p = os.path.join(d, f)
        try:
            t = open(p, encoding='utf-8').read()
        except (UnicodeDecodeError, OSError):
            continue
        mds.append(p)
        if 'convention B' in t or 'Convention B' in t:
            porteurs.append(p)
            if CLAUSE.search(t):
                clauses.append(p)
chk('des textes portent bien la convention B', len(porteurs) > 0,
    '%d textes sur %d .md' % (len(porteurs), len(mds)))
chk('AUCUN ne porte la clause de declaration CRLF -> LF', not clauses,
    ','.join(os.path.basename(x) for x in clauses) or '0 texte')
chk('donc la regle d ecriture N EST PAS ACQUISE', not clauses,
    'quatrieme candidate sous (X), revue 28/09')

# =====================================================================
print("\n4. LA PRATIQUE EST DEJA (b) -- ET LA FAUTE A DEJA ETE PAYEE UNE FOIS")
# =====================================================================
man = open(P('ACTE_constante_A', 'MANIFEST_lot_machine2_acte_constante_A_v1.txt'),
           encoding='utf-8').read()
chk('mon propre manifeste porte DEUX empreintes et DEUX tailles',
    'empreinte_brute' in man and 'octets_bruts' in man, 'convention (b) en pratique')
chk('le 28b lui-meme cite ses captures sous les deux formes',
    'brut 3833ba551a390945' in txt and '10a7ce5688f515d5' in txt, 'section 5 du 28b')
# Precedent : la meme faute a deja ete relevee sur le lot P-4, et consignee.
p4 = P('entrant_machine1_2026-09-08_P4', 'note_machine1_reception_controle_m2_P4_v1.md')
prec = open(p4, encoding='utf-8').read() if os.path.exists(p4) else ''
chk('PRECEDENT : la meme faute est deja consignee au lot P-4',
    'octets bruts' in prec and 'Trois pieces sont CRLF' in prec,
    'un manifeste disait "convention B" pour du brut')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('(v) EST TRANCHABLE : objet = section 2 du 28b, VERIFIE au chiffre.')
print('La lecture (b) est la PRATIQUE des deux machines ; le TEXTE ne la porte pas.')
print('=====================================================================')
