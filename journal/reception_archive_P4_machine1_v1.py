# Reception machine 1 de l'archive P-4 (m2 -> m1, 08/09/2026) : quatre pieces de transmission (convention B),
# sept lots (sha256 brut du ZIP, canon = convention B du manifeste interne, taille, pieces contre manifeste),
# 26 empreintes nommees, ZIP imbrique du gel. Aucune piece n'est lue avant ce controle.
import hashlib, unicodedata, zipfile, io, os, re, json, sys
U = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads'   # dossier des douze fichiers recus
def convB(b):
    try: return hashlib.sha256(unicodedata.normalize('NFC', b.decode('utf-8').replace('\r\n', '\n')).encode()).hexdigest()[:16]
    except Exception: return None
def brut(b): return hashlib.sha256(b).hexdigest()[:16]
def asc(b): return all(x < 128 for x in b)
att = {'POUR_MACHINE1_archive_P4_sept_lots_machine2_v1.md': ('909bef4ce6cbd9c3', 7610), 'controle_archive_P4_machine2_v2.log': ('a7c412962bb43d52', 10484),
       'controle_archive_P4_machine2_v2.py': ('a71b8a344e71733d', 9446), 'spec_lots_P4_machine1_v1.json': ('8fb9e813713c6283', 3534)}
print("== PIECES DE TRANSMISSION (convention B annoncee au MANIFEST_ARCHIVE_P4_machine2_v1.txt) ==")
n_ok = 0
for f, (e, n) in att.items():
    b = open(f'{U}/{f}', 'rb').read(); B = convB(b); ok = (B == e and len(b) == n); n_ok += ok
    print(f"  {f:<52} B={B} attendu {e} {len(b):6d}/{n} o ascii={asc(b)} CR={b.count(b'\r')} -> {'OK' if ok else 'ECART'}")
mb = open(f'{U}/MANIFEST_ARCHIVE_P4_machine2_v1.txt', 'rb').read()
print(f"  MANIFEST_ARCHIVE_P4_machine2_v1.txt : B={convB(mb)} (= brut {brut(mb)}) {len(mb)} o ascii={asc(mb)} CR={mb.count(b'\r')} ; aucune empreinte annoncee pour lui-meme")
print(f"  transmission : {n_ok}/4 conformes")
lots = [("lot_machine1_2026-09-02_P4_instrument_v1.zip", "5107783aa32d1fd5", "db6054ad58e4ff44", 45806, 11), ("lot_machine1_2026-09-02_P4_lecture_gel_v3.zip", "ae763220c01bf2e8", "fcaa79169534cbea", 7400, 3),
        ("lot_machine1_2026-09-02_P4_reponse_v2.zip", "f1907286e1eb7759", "d1ff9faa6e020094", 26527, 8), ("lot_machine1_2026-09-02_P4_resultat_v4.zip", "70a43a513f9e0782", "f1d646d9feca7437", 45309, 9),
        ("lot_machine2_2026-09-02_P4_addendum_v3.zip", "c1e8a4b553b47d44", "81ddb80ef0433b15", 47129, 6), ("lot_machine2_2026-09-02_P4_controle_v2.zip", "ad2b0440e6f2f768", "f0f304d0351d592b", 18326, 6),
        ("lot_machine2_2026-09-02_P4_run_v4.zip", "0c86a9cf625bf3d1", "3bcac78e23a1d077", 48010, 7)]
LIG = re.compile(r"^([0-9a-f]{16})\s+(?:([0-9a-f]{16})|\(zip[^)]*\))?\s*(\d+)\s+(\S+)"); EXT = re.compile(r"\.(md|py|json|log|txt|npz|npy|zip|mermaid|csv|png)$")
print("\n== LES SEPT LOTS (brut du ZIP, canon interne, taille, pieces contre leur propre manifeste) ==")
tot_ok = 0; vues = {}; pieces = []
for nom, ez, ec, en, ep in lots:
    b = open(f'{U}/{nom}', 'rb').read(); zb = brut(b); Z = zipfile.ZipFile(io.BytesIO(b)); mem = {n: Z.read(n) for n in Z.namelist() if not n.endswith('/')}
    mans = [n for n in mem if os.path.basename(n).upper().startswith('MANIFEST')]; canon = convB(mem[mans[0]])
    cont = cit = ok = ecart = 0; voie = {'B': 0, 'brut': 0, 'deux': 0}
    for Ln in mem[mans[0]].decode('utf-8', 'replace').replace('\r\n', '\n').split('\n'):
        m = LIG.match(Ln.strip())
        if not m: continue
        e1, e2, taille, f = m.group(1), m.group(2), int(m.group(3)), m.group(4)
        if not EXT.search(f): continue
        cle = next((k for k in mem if os.path.basename(k) == os.path.basename(f)), None)
        if cle is None: cit += 1; continue
        cont += 1; bb = mem[cle]; vB, vb = convB(bb), brut(bb); attn = {x for x in (e1, e2) if x}; mB, mb_ = vB in attn, vb in attn
        if (mB or mb_) and len(bb) == taille: ok += 1; voie['deux' if (mB and mb_) else ('B' if mB else 'brut')] += 1
        else: ecart += 1; print(f"      ECART {f}: attendu {attn} /{taille} ; B={vB} brut={vb} /{len(bb)}")
    for n, c in mem.items():
        pieces.append((nom, os.path.basename(n), convB(c), brut(c), len(c), c.count(b'\r'), asc(c)))
        for e, v in ((convB(c), 'B'), (brut(c), 'brut')):
            if e: vues.setdefault(e, (nom, os.path.basename(n), v))
        if n.lower().endswith('.zip'):
            ZI = zipfile.ZipFile(io.BytesIO(c))
            for inn in ZI.namelist():
                if inn.endswith('/'): continue
                ib = ZI.read(inn); pieces.append((nom + ' :: ' + os.path.basename(n), os.path.basename(inn), convB(ib), brut(ib), len(ib), ib.count(b'\r'), asc(ib)))
                for e, v in ((convB(ib), 'B'), (brut(ib), 'brut')):
                    if e: vues.setdefault(e, (nom, os.path.basename(n) + '::' + os.path.basename(inn), v))
    st = (zb == ez and canon == ec and len(b) == en and (len(mem) - 1) == ep and ecart == 0 and cont == len(mem) - 1); tot_ok += st
    print(f"  {nom:<46} brut {zb} {'=' if zb == ez else '!='} annonce ; canon {canon} {'=' if canon == ec else '!='} annonce ; {len(b)} o ; pieces {len(mem)-1}/{ep} ; manifeste : {cont} contenues ({ok} ok, {ecart} ecart), {cit} citees ; voies B/brut/deux {voie['B']}/{voie['brut']}/{voie['deux']} -> {'OK' if st else 'ECART'}")
print(f"  lots conformes : {tot_ok}/7")
spec = json.load(open(f'{U}/spec_lots_P4_machine1_v1.json'))
print("\n== LES 26 EMPREINTES NOMMEES PAR MACHINE 1 (spec 8fb9e813713c6283) ==")
tot = tr = 0
for lot in spec['lots']:
    for e, role in (lot.get('empreintes_attendues') or {}).items():
        tot += 1; v = vues.get(e); tr += v is not None; print(f"  {'TROUVEE' if v else 'ABSENTE'} {e} {role[:34]:<34} -> {v[1][:58] if v else '---'} ({v[2] if v else ''})")
    for f in lot.get('fichiers_attendus', []):
        pres = any(p[1] == f for p in pieces); tot += 1; tr += pres; print(f"  {'PRESENT' if pres else 'ABSENT '} (par son nom)   {f}")
print(f"  nommees {tot}, retrouvees {tr}, manquantes {tot - tr}")
g1 = [p for p in pieces if p[1] == 'gel_P4_temoin_classique_machine2_v1.md']
print(f"\n  gel : {len(g1)} exemplaires (en clair et imbrique), empreintes B {sorted(set(p[2] for p in g1))}, brut {sorted(set(p[3] for p in g1))}, ascii {all(p[6] for p in g1)}, CR {sorted(set(p[5] for p in g1))}")
print("\n== TOUTES LES PIECES (lot ; fichier ; B ; brut ; octets ; CR ; ascii) ==")
for p in pieces: print(f"  {p[0][:62]:<62} {p[1]:<48} {p[2]} {p[3]} {p[4]:7d} {p[5]:4d} {str(p[6])}")
print(f"  total pieces (manifestes compris, ZIP imbrique deplie) : {len(pieces)}")
