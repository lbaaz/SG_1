# Reception machine 1 du lot de certification machine 2 (09/09/2026) : canon = convention B du manifeste,
# neuf pieces contre le manifeste, ASCII/LF, empreinte certifiee, numero annonce. Puis etat du registre
# sur clone frais : HEAD, fichiers delta 87/88, plafond.
import hashlib, unicodedata, re, os, sys, subprocess
U = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads'
CLONE = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/SG_1_frais'
def convB(b): return hashlib.sha256(unicodedata.normalize('NFC', b.decode('utf-8').replace('\r\n', '\n')).encode()).hexdigest()[:16]
man = open(f'{U}/MANIFEST_lot_machine2_certification_acte_P4_v1.txt', 'rb').read()
print(f"MANIFEST_lot_machine2_certification_acte_P4_v1.txt : B {convB(man)} = brut {hashlib.sha256(man).hexdigest()[:16]} ; {len(man)} o ; ascii {all(x<128 for x in man)} ; CR {man.count(b'\r')}  -> CANON DU LOT")
att = {}
for l in man.decode().splitlines():
    m = re.match(r'^([0-9a-f]{16})\s+(\d+)\s+(\S+)$', l.strip())
    if m: att[m.group(3)] = (m.group(1), int(m.group(2)))
ok = 0
for f, (e, n) in att.items():
    b = open(f'{U}/{f}', 'rb').read(); B = convB(b); good = (B == e and len(b) == n); ok += good
    print(f"  {f:<46} B={B} attendu {e} {len(b):6d}/{n} o ascii={all(x<128 for x in b)} CR={b.count(b'\r')} -> {'OK' if good else 'ECART'}")
print(f"pieces : {ok}/{len(att)} conformes ; annoncees 9 ; verifiees + absentes + ecarts = {ok} + 0 + {len(att)-ok} = {len(att)} lignes")
c = open(f'{U}/CERTIFICATION_machine2_acte_P4_v1.md').read()
print(f"certification : piece certifiee 0f8e283fa9499f96 citee {c.count('0f8e283fa9499f96')} fois ; canon lot m1 710498cdc372ed02 cite : {'710498cdc372ed02' in c} ; 'sous le numero 88' (insensible a la casse) : {'sous le numero 88' in c.lower()} ; 'TREIZE' : {'TREIZE' in c}")
print("\nREGISTRE (clone frais) :")
def git(*a): return subprocess.run(['git', '-C', CLONE] + list(a), capture_output=True, text=True).stdout.strip()
print(f"  HEAD {git('rev-parse', '--short', 'HEAD')} : {git('log', '-1', '--format=%s')[:100]}")
fics = git('ls-files').split('\n')
for n in ('87', '88'):
    print(f"  fichiers delta_{n} : {[f for f in fics if f'delta_{n}' in f or f'delta{n}' in f]}")
nums = sorted({int(x) for f in fics for x in re.findall(r'delta[_ -]?(\d+)', f, re.I)})
print(f"  plafond : {nums[-1]} ; premier libre : {nums[-1]+1}")
for f in ('journal/journal_delta_87_sequence_R3_v1.md', 'journal/journal_delta_nn_sequence_R3_v1.md', 'journal/NOTE_DERIVATION_delta87_machine2_v1.md'):
    p = os.path.join(CLONE, f)
    if os.path.exists(p): print(f"  {convB(open(p,'rb').read())}  {f}")
