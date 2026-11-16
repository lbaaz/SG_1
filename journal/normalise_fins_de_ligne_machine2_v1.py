# -*- coding: ascii -*-
"""NORMALISE LES FINS DE LIGNE de trois scripts de mon contreseing de la v1 de l'acte de la loi (lot bbb74a8df7697397), machine 2, 2026-11-16, avant le depot du delta 100.
Cause : ces trois fichiers ont ete retouches par l'outil d'edition de mon poste Windows, qui y a pose des fins de ligne CRLF ; la feuille de perimetre du depot exige B == brut (ASCII/LF) et a MORDU sur eux (essai conserve
hors depot : essai_rate_perimetre_delta100/). La convention B (sha256 de l'UTF-8 NFC, CRLF -> LF) rend l'empreinte B de chaque fichier IDENTIQUE avant et apres : seule change l'empreinte BRUTE. Le contenu, lui, ne change pas d'un octet
hors les fins de ligne ; le ZIP scelle du lot bbb74a8df7697397 porte, lui, les octets d'origine, et son manifeste donne les deux empreintes.
Le script lit chaque fichier, verifie qu'il est ASCII, remplace CRLF par LF (rien d'autre), verifie que l'empreinte B n'a pas bouge, ecrit, relit, et PRINT avant/apres. Usage (depuis BOCAL4) :
py -3.11 -P DEPOT_delta100/normalise_fins_de_ligne_machine2_v1.py <fichier> [<fichier> ...]"""
import hashlib
import sys
import unicodedata


def emp(raw):
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
    return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16]


ok = True
for f in sys.argv[1:]:
    raw = open(f, 'rb').read()
    avant = emp(raw)
    if any(b > 127 for b in raw):
        print('ARRET : %s n\'est pas ASCII' % f)
        sys.exit(1)
    n = raw.count(b'\r\n')
    if raw.count(b'\r') != n:
        print('ARRET : %s porte des retours chariot hors CRLF' % f)
        sys.exit(1)
    neuf = raw.replace(b'\r\n', b'\n')
    open(f, 'wb').write(neuf)
    apres = emp(open(f, 'rb').read())
    bon = avant[0] == apres[0] and apres[0] == apres[1]
    ok = ok and bon
    print('%-95s CRLF %4d -> 0 ; B %s -> %s ; brut %s -> %s ; %s' % (f, n, avant[0], apres[0], avant[1], apres[1], 'B INCHANGE, B == brut' if bon else 'MORD'))
sys.exit(0 if ok else 1)
