# OPTION (b) DU DEPOT, NON RETENUE PAR LA CERTIFICATION, A LA MAIN DE QUI DEPOSE : derivation mecanique
# \bnn\b -> 88 de l'acte certifie (meme geste qu'aux deltas 86 et 87), avec les gardes du delta 87.
# Ne tourne que si la source rend 0f8e283fa9499f96. Ecrit le derive dans le dossier courant et rend son empreinte.
import hashlib, re, sys, unicodedata
SRC = sys.argv[1] if len(sys.argv) > 1 else 'journal_delta_88_P4_v1.md'
b = open(SRC, 'rb').read()
def convB(x): return hashlib.sha256(unicodedata.normalize('NFC', x.decode('utf-8').replace('\r\n', '\n')).encode()).hexdigest()[:16]
assert convB(b) == '0f8e283fa9499f96', convB(b)
t = b.decode('ascii')
d = re.sub(r'\bnn\b', '88', t)
lt, ld = t.split('\n'), d.split('\n')
assert len(lt) == len(ld)
mod = [i + 1 for i, (a, c) in enumerate(zip(lt, ld)) if a != c]
for i in mod: assert re.sub(r'\bnn\b', '88', lt[i - 1]) == ld[i - 1]
for w in ('donnees', 'annonce', 'connexite', 'colonne', 'bonne', 'nommees', 'personne', 'inconnue'):
    assert t.count(w) == d.count(w), w
occ = len(re.findall(r'\bnn\b', t))
assert 'journal_delta_nn_P4_v1' in d and all(ord(ch) < 128 for ch in d) and '%' not in d
open('journal_delta_88_P4_v1_DERIVE_option_b.md', 'w', newline='\n').write(d)
print(f"source {SRC} : 0f8e283fa9499f96, {len(b)} o, {len(lt)} lignes")
print(f"regle \\bnn\\b -> 88 : {occ} occurrences, {len(mod)} lignes modifiees (lignes {mod[:12]}{'...' if len(mod) > 12 else ''}) ; longueur {len(d.encode())} o ; le nom de fichier journal_delta_nn_P4_v1 reste intact (nn entre underscores)")
print(f"derive : journal_delta_88_P4_v1_DERIVE_option_b.md  B = {convB(d.encode())}  -- NON certifie tel quel : la certification porte sur 0f8e283fa9499f96")
