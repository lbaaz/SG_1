# m15_certification_croisee_v4.py -- machine 2, 2026-08-10
# Certification croisee du GEL v4 (m15_pre_enregistrement_v4.md, 35022c5c),
# livre au delta 53. INDEPENDANT du script de patch : extractions re-faites
# a ancres STRUCTURELLES (colonne 0, regle 12), diff v3->v4 juge PAR HUNK,
# invariants recomptes, definition E29 re-appliquee (pas seulement heritee).
# Le rejeu bit-identique du script machine 1 est un fait SEPARE, consigne
# au log de session (PYTHONUTF8=1 requis sur Windows, voir note).
import difflib, hashlib, sys, unicodedata

ECHECS = []
def check(nom, ok, detail=""):
    print(f"{'OK  ' if ok else 'ECHEC'} {nom}" + (f" -- {detail}" if detail else ""))
    if not ok: ECHECS.append(nom)

def lis(nom, sha16):
    b = open(nom, 'rb').read()
    h = hashlib.sha256(b).hexdigest()[:16]
    check(f"empreinte {nom}", h == sha16, f"{h} attendu {sha16}")
    return b.decode('utf-8')

print("== 1. SOURCES ET LIVRAISON (empreintes re-derivees) ==")
v3   = lis('m15_pre_enregistrement_v3.md',      'e41f4da3685e6d1b')
v4   = lis('m15_pre_enregistrement_v4.md',      '35022c5c0784cb82')
cert = lis('m15_certification_croisee_v3.md',   '8081a0325e0821de')
err3 = lis('m15_erratum_grossiere_mordue_v3.md','16c6d86e389da2a9')
err2 = lis('m15_erratum_grossiere_mordue_v2.md','f4a3508b84d40cb6')

print("== 2. EXTRACTION INDEPENDANTE (regle declaree du script, re-appliquee) ==")
# Regle declaree : bloc = src[find(deb) : find(fin, apres deb)], debut unique.
# Mon ajout structurel : le debut est en COLONNE 0 (precede d'un '\n').
# La fin N-15 ('\n---\n') n'est PAS unique dans la source (separateur de
# sections, 10 occurrences) : la regle est "premiere apres debut" --
# deterministe sur source gelee par empreinte ; DECLARE, voir note.
def bloc_source(src, deb, fin, nom):
    check(f"{nom} : ancre debut unique et colonne 0",
          src.count(deb) == 1 and src.count('\n' + deb) == 1)
    i = src.find(deb)
    j = src.find(fin, i)
    check(f"{nom} : ancre fin presente apres debut", j > i,
          f"premiere occurrence de {fin!r} apres debut (occurrences source : {src.count(fin)})")
    return src[i:j]

e29_src = bloc_source(err3, '3. CORRECTION', '4. MOTIVATION', 'E29.3')
n13_src = bloc_source(cert, '### N-13', '### N-14', 'N-13')
n15_src = bloc_source(cert, '### N-15', '\n---\n',  'N-15')

def bloc_v4(marq):
    deb, fin = f'<<<DEBUT EXTRAIT {marq}>>>\n', f'<<<FIN EXTRAIT {marq}>>>'
    check(f"marqueurs {marq} uniques", v4.count(deb) == 1 and v4.count(fin) == 1)
    i = v4.find(deb) + len(deb)
    return v4[i:v4.find(fin, i)]

for marq, src_bloc, n_attendu in (('E29.3', e29_src, 709),
                                  ('N-13',  n13_src, 1109),
                                  ('N-15',  n15_src, 2111)):
    porte = bloc_v4(marq)
    check(f"{marq} : BYTE-VERBATIM v4 == source", porte == src_bloc,
          f"v4 {len(porte)} car., source {len(src_bloc)} car.")
    check(f"{marq} : compte annonce delta 53", len(porte) == n_attendu,
          f"{len(porte)} attendu {n_attendu}")
    check(f"{marq} : N-14 absent de l'extrait", '### N-14' not in porte)

print("== 3. DEFINITION E29 RE-APPLIQUEE (pas seulement heritee ; M2-a) ==")
for temoin in ('passe GROSSIERE', '[LO0, 0.90', 'explosion_sous_LO0_0.90s',
               'gros_explosifs', 'b_fond = 3/96', 'k_min = 3', 'n_eff = 24'):
    check(f"E29.3 porte '{temoin}'", temoin in e29_src)
check("E29.3 : ASCII pur", all(ord(c) < 128 for c in e29_src))

print("== 4. RESERVE DELTA 51 : v3 erratum vs v2 contre-signee ==")
# annonce : sections 1-7 bit-identiques a la v2 f4a3508b.
def sections_1_7(t):
    a = '\n1. '
    check("ancre '1. ' unique", t.count(a) == 1)
    i = t.find(a) + 1
    j = t.find('\n7. ', i)
    k = t.find('\n=== FIN', j)
    return t[i:k]
check("erratum v3 sections 1-7 == v2 (bit)", sections_1_7(err3) == sections_1_7(err2))

print("== 5. DIFF v3 -> v4 PAR HUNK (chaque bloc contigu = un patch declare) ==")
sm = difflib.SequenceMatcher(None, v3.splitlines(True), v4.splitlines(True), autojunk=False)
hunks = [op for op in sm.get_opcodes() if op[0] != 'equal']
temoins_hunk = [
    ('A+B en-tete', ('hors PORTAGE v4', 'v4 HERITAGE, machine 1, 2026-08-09')),
    ('C mot N-13',  ('appliquait la marge ABSOLUE',)),
    ('D chiffre N-15', ('marge 1.117 contre', 'P(n_disc >= 1) = 0.399', '1.025')),
    ('E PORTAGE',   ('PORTAGE v4 (HERITAGE)', '<<<DEBUT EXTRAIT E29.3>>>')),
]
print(f"   hunks non-egaux : {len(hunks)}")
restants = list(hunks)
for nom, marqs in temoins_hunk:
    attr = [h for h in restants
            if all(m in ''.join(v4.splitlines(True)[h[3]:h[4]]) for m in marqs)]
    check(f"hunk '{nom}' : present et unique", len(attr) == 1, f"{len(attr)} hunk(s)")
    for h in attr: restants.remove(h)
check("aucun hunk clandestin", len(restants) == 0,
      f"{len(restants)} hunk(s) hors patchs declares")

print("== 6. ANCIENS ABSENTS, NOUVEAUX UNIQUES (patchs A-D) ==")
paires = [
    ("A", "bloc ASCII, canonique NFC+LF ;",
          "bloc ASCII hors PORTAGE v4 (extraits NFC verbatim de source), canonique NFC+LF ;"),
    ("B", "version v3, machine 1, 2026-08-07)",
          "version v4 HERITAGE, machine 1, 2026-08-09)"),
    # ancien C = la PARENTHESE REELLE de la v3 (ancre dynamique du script) ;
    # la citation du delta 53 est ABREGEE : le texte reel porte en plus
    # "elle range 2.42, 2.45 et 2.55 sous 5:2." -- DECLARE, voir note.
    ("C", v3[v3.find("(Lecture argmin"):v3.find(")", v3.find("(Lecture argmin")) + 1],
          "appliquait la marge ABSOLUE -- meme mot, pas la meme regle ; ensemble F identique"),
    ("D", "moins profonde que le seuil (COURBURES",
          "CHIFFRE N-15 : marge 1.117 contre 1 sur le seul indice mesure"),
]
for nom, ancien, nouveau in paires:
    check(f"patch {nom} : ancien present 1x en v3", v3.count(ancien) == 1)
    check(f"patch {nom} : ancien absent de v4",     ancien not in v4)
    check(f"patch {nom} : nouveau present 1x en v4", v4.count(nouveau) == 1)
    check(f"patch {nom} : nouveau absent de v3",     nouveau not in v3)

check("clause retiree par C ('2.42, 2.45 et 2.55 sous 5:2') survit en P4.2",
      "2.42, 2.45 et 2.55 sous 5:2" in n13_src)

print("== 7. INVARIANTS DE SORTIE (recomptes) ==")
TERM = "\n=== FIN DU GEL M15 ===\n"
check("terminateur exactement 1x", v4.count(TERM) == 1)
check("terminateur en derniere ligne", v4.endswith(TERM))
check("v4 NFC", unicodedata.is_normalized('NFC', v4))
check("LF final unique", v4.endswith("\n") and not v4.endswith("\n\n"))
hors = v4
for marq in ('N-13', 'N-15'):
    deb, fin = f'<<<DEBUT EXTRAIT {marq}>>>\n', f'<<<FIN EXTRAIT {marq}>>>'
    i = hors.find(deb) + len(deb); j = hors.find(fin, i)
    hors = hors[:i] + hors[j:]
check("ASCII partout hors extraits NFC (N-13, N-15)",
      all(ord(c) < 128 for c in hors),
      "les seuls caracteres non-ASCII de v4 vivent dans les deux extraits declares")

print()
if ECHECS:
    print(f"VERDICT : {len(ECHECS)} ECHEC(S) :", *ECHECS, sep='\n  '); sys.exit(1)
print("VERDICT : 0 echec. Gel v4 35022c5c0784cb82 : controles machine 2 passes.")
