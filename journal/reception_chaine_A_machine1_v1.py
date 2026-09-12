# Reception machine 1 des lots m2 'provenance_borne_et_transit_v1' et 'chaine_constante_A_v1' (09/09) :
# brut du ZIP, canon = convention B du manifeste, pieces contre manifeste (deux formats de ligne : 'brut B octets fichier'
# ou 'B octets fichier'), fins de ligne. Canons annonces : chaine a4c35a2ee691c9a7 / ZIP 6d26323f2b6627a6 ; provenance : non annonce.
import hashlib, unicodedata, zipfile, io, re, os, sys
U = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads'
def B(b): return hashlib.sha256(unicodedata.normalize('NFC', b.decode('utf-8').replace('\r\n', '\n')).encode()).hexdigest()[:16]
def brut(b): return hashlib.sha256(b).hexdigest()[:16]
ANN = {'lot_machine2_2026-09-09_provenance_borne_et_transit_v1.zip': (None, None), 'lot_machine2_2026-09-09_chaine_constante_A_v1.zip': ('a4c35a2ee691c9a7', '6d26323f2b6627a6')}
for nom, (ac, az) in ANN.items():
    b = open(f'{U}/{nom}', 'rb').read(); Z = zipfile.ZipFile(io.BytesIO(b)); mem = {n: Z.read(n) for n in Z.namelist() if not n.endswith('/')}
    d = nom[:-4]; os.makedirs(d, exist_ok=True)
    for n, c in mem.items(): open(os.path.join(d, os.path.basename(n)), 'wb').write(c)
    man = mem[[n for n in mem if os.path.basename(n).upper().startswith('MANIFEST')][0]]
    att = {}
    for l in man.decode().splitlines():
        m = re.match(r'^([0-9a-f]{16})\s+([0-9a-f]{16})\s+(\d+)\s+(\S+)', l.strip())
        if m: att[m.group(4)] = ({m.group(1), m.group(2)}, int(m.group(3))); continue
        m = re.match(r'^([0-9a-f]{16})\s+(\d+)\s+(\S+)', l.strip())
        if m: att[m.group(3)] = ({m.group(1)}, int(m.group(2)))
    ok = 0; crlf = []
    for f, (es, n) in att.items():
        k = next((x for x in mem if os.path.basename(x) == f), None); c = mem[k] if k else b''
        g = bool(k) and (B(c) in es or brut(c) in es) and len(c) == n; ok += g
        if k and b'\r' in c: crlf.append((f, c.count(b'\r'), B(c), brut(c)))
        print(f"  {f:<52} B={B(c) if k else '---'} brut={brut(c) if k else '---'} {len(c):7d}/{n} -> {'OK' if g else 'ECART'}")
    zb = brut(b); cn = B(man)
    print(f"{nom} : ZIP brut {zb} {'= annonce' if az == zb else ('!= annonce ' + str(az) if az else 'non annonce')} {len(b)} o ; CANON {cn} {'= annonce' if ac == cn else ('!= annonce' if ac else 'non annonce')} ; pieces {ok}/{len(att)} ; membres - 1 = {len(mem) - 1} ; CRLF : {crlf}\n")
