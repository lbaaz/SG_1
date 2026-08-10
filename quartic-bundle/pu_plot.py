# pu_plot.py -- figure de reference benin/malin (reconstruction du meme jour, cf. README)
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
w1, w2 = 1.0, np.sqrt(2.0); g = 0.05
P2, W2 = w1*w1 + w2*w2, (w1*w2)**2
def f(y):
    q1,q2,p1,p2 = y
    return np.array([q2, p2, W2*q1 - g*q1**3, -p1 - P2*q2])
def traj(s, T, dt=0.006, blow=1e4):
    y=np.array([s,0.0,0.0,s]); ts=[0.0]; xs=[s]
    for i in range(int(T/dt)):
        k1=f(y); k2=f(y+0.5*dt*k1); k3=f(y+0.5*dt*k2); k4=f(y+dt*k3)
        y=y+(dt/6.0)*(k1+2*k2+2*k3+k4); ts.append((i+1)*dt); xs.append(y[0])
        if np.max(np.abs(y))>blow: break
    return np.array(ts), np.array(xs)
bg='#0f1117'; fig,ax=plt.subplots(1,2,figsize=(12.5,4.4)); fig.patch.set_facecolor(bg)
for a in ax:
    a.set_facecolor(bg); a.tick_params(colors='#999'); a.grid(alpha=0.15)
    [sp.set_color('#555') for sp in a.spines.values()]
t,x=traj(0.7,400); ax[0].plot(t,x,color='#4ec9b0',lw=0.7)
ax[0].set_title("s=0.7 : BENIN -- battements bornes, pour toujours",color='#e8e8e8',fontsize=10.5)
t,x=traj(1.5,40); ax[1].plot(t,x,color='#f48771',lw=1.0)
ax[1].set_title(f"s=1.5 : MALIN -- blow-up a t~{t[-1]:.0f}",color='#e8e8e8',fontsize=10.5)
for a in ax: a.set_xlabel("t",color='#bbb'); a.set_ylabel("x(t)",color='#bbb')
fig.suptitle("Le fantome en bocal : l'ile benigne et l'ocean (PU quartique, (1,v2), g=0.05)",color='#f0f0f0',fontsize=12)
plt.tight_layout(); plt.savefig('pu_benin_malin.png',dpi=130,facecolor=bg,bbox_inches='tight')
print("figure : pu_benin_malin.png")
