# spotcheck_reformulation.py -- test point par point de la forme equivalente de la loi de seuil
# Le long de la famille de CI (s,0,0,s) : A2 = -2s/Delta, donc K = C eps^2 (w1+w2)
# equivaut a g*A2^2*(w1+w2) = 4C (aveugle au detuning). Si C=1/4 : g*A2*^2 = 1/(w1+w2).
import numpy as np
d=np.load('bocal_paysage.npz')
om=None; sst=None
for k in d.files:
    a=d[k]
    if a.ndim==1 and a.size>=8:
        if om is None and a.min()>1.0 and a.max()<=4.0: om=a; continue
        if sst is None: sst=a
g=0.05; mask=np.isfinite(sst)
print("Spot-check : chaque point doit donner g*A2^2*(1+w2) = 4C  (= 1 si C = 1/4)")
print(f"  {'w2':<8}{'s*':<8}{'C_pt':<9}{'gA2^2(1+w2)':<13}{'zone'}")
rows=[]
for w2v,sv in zip(om[mask],sst[mask]):
    eps=w2v-1.0; Delta=w2v**2-1.0
    C=g*sv*sv/(eps*eps*(1.0+w2v)); q=g*(2.0*sv/Delta)**2*(1.0+w2v)
    zone="BORD-G" if 1.25<=w2v<=1.5 else ("BORD-D" if 2.75<=w2v<=3.25 else ("vallee" if 1.75<=w2v<=2.6 else "-"))
    rows.append((w2v,sv,C,q,zone))
    if zone!="-": print(f"  {w2v:<8.3f}{sv:<8.2f}{C:<9.3f}{q:<13.3f}{zone}")
print("\n  points-phares A/B (raideur appariee) :")
ph=[]
for w2v,sv in [(np.sqrt(2.0),1.27),(2.85,8.10),(3.00,9.58)]:
    eps=w2v-1.0; Delta=w2v**2-1.0
    C=g*sv*sv/(eps*eps*(1.0+w2v)); q=g*(2.0*sv/Delta)**2*(1.0+w2v)
    ph.append((w2v,sv,C,q)); print(f"  w2={w2v:.3f}  s*={sv:.2f}  C_pt={C:.3f}  gA2^2(1+w2)={q:.3f}")
stats={}
for lo,hi,name in [(1.25,1.5,'gauche'),(2.75,3.25,'droit')]:
    m=mask&(om>=lo)&(om<=hi)
    C=g*sst[m]**2/((om[m]-1)**2*(1+om[m])); stats[name]=(C.mean(),C.std(),int(m.sum()))
    print(f"\n  BORD {name.upper()}: C = {C.mean():.3f} +/- {C.std():.3f}  (n={m.sum()}, min {C.min():.3f}, max {C.max():.3f})")
print("\n  Lecture : bord droit = instrument de precision (biais premiere-cellule + derive ~10 pct a resoudre) ;")
print("           bord gauche limite par la resolution (quantification Delta_s = 0.2 sur s* ~ 1-1.8).")
np.savez('spotcheck_reformulation.npz',rows=np.array([(a,b,c,dd) for a,b,c,dd,_ in rows]),phares=np.array(ph),
         gauche=stats['gauche'],droit=stats['droit'])
