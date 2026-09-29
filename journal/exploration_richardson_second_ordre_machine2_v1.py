"""exploration_richardson_second_ordre_machine2_v1.py -- machine 2, 2026-09-13.

EXPLORATOIRE, NON PRE-DECLAREE AU SENS DE LA LECTURE 99080e4822bf0108 :
cette piece est nee APRES la section 5 de derivation_second_ordre_machine2_v1
(log 2409f40ed2a61c61), qui a montre (obs - pred)/disp_91 ~ 1.0 aux douze
points p = 4, 5. Hypothese : cet exces est l'erreur de l'integrateur RK4 au
pas dt_2b, que la jumelle G-dt (dt_2b/2, meme trajectoire) mesure.

REGLE DE LECTURE, ECRITE ICI AVANT EXECUTION (donc dans l'empreinte) :
  lnA_R = lnA(dt/2) + (lnA(dt/2) - lnA(dt)) / (2^q - 1), q = 4 (ordre du
          schema) ; la sensibilite q = 3 et q = 5 se CONSIGNE.
  obs_R = lnA_R - ln(K/g)/(p-2)
  pred  = biais C4 (derivation v1, JSON b70fca94d72822ad, decalage 0.0)
  EXPLIQUE  au degre p si obs_R/pred est dans [0.8, 1.2] aux SIX points ;
  NON       sinon. p = 7 se lit a part : les modes libres y sont a tau^2.3
            (C3), un NON a p = 7 seul n'infirme pas le premier ordre, il
            designe les modes libres -- a CONSIGNER, pas a conclure.
  Test negatif de la regle : pred = 0 -> EXPLIQUE ne doit pas pouvoir sortir
  (obs_R/0 infini) ; pred x 2 doit rendre NON aux degres ou EXPLIQUE sort.
Portee : lecture de conception, a posteriori, non opposable (N-70).
"""
import hashlib
import json
import math
import os
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RUN91 = os.path.join(ICI, "out_run_delta91", "alpha_v13", "resultats_alpha.json")
DERIV = os.path.join(ICI, "derivation_second_ordre_machine2_v1.json")
DERIV_B = "b70fca94d72822ad"
LOG = os.path.join(ICI, "exploration_richardson_second_ordre_machine2_v1.log")
DEGRES, W2S, CS = (4, 5, 7), ("1.73", "2.27", "2.80"), ("1.05", "1.20")
G = 0.05
K = {4: 120.0, 5: 3640 / 81, 7: 9576 / 625}
lignes, bilan = [], {"chk": 0, "mord": []}


def out(s=""):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=""):
    bilan["chk"] += 1
    if not cond:
        bilan["mord"].append(nom)
    out("  [chk %s] %s%s" % ("PASSE" if cond else "MORD ", nom, (" -- " + detail) if detail else ""))


def B(ch):
    t = open(ch, encoding="utf-8", newline="").read()
    return hashlib.sha256(unicodedata.normalize("NFC", t.replace("\r\n", "\n")).encode()).hexdigest()[:16]


out("EXPLORATION RICHARDSON -- machine 2 -- NON PRE-DECLAREE (voir docstring)")
chk("derivation v1 a son empreinte", B(DERIV) == DERIV_B, B(DERIV))
run, der = json.load(open(RUN91, encoding="utf-8")), json.load(open(DERIV, encoding="utf-8"))
out("  run 91 convention B %s" % B(RUN91))


def lire(pred_mult):
    etats = {}
    for p in DEGRES:
        lnAK = math.log(K[p] / G) / (p - 2)
        ok = True
        for w2 in W2S:
            pred = pred_mult * der["C4"]["%d|%s" % (p, w2)]["0.0"]["biais_lnA"]
            for c in CS:
                cle = "%d|%s|%s" % (p, w2, c)
                a1, a2 = run["plan"][cle]["ajustement"], run["G_dt"][cle]["ajustement"]
                r = {}
                for q in (3, 4, 5):
                    lnR = a2["lnA_II"] + (a2["lnA_II"] - a1["lnA_II"]) / (2 ** q - 1)
                    r[q] = (lnR - lnAK) / pred if pred != 0 else math.inf
                ok = ok and 0.8 <= r[4] <= 1.2
                if pred_mult == 1:
                    obs = a1["lnA_II"] - lnAK
                    out("  %s  obs(dt) %.4e  obs(dt/2) %.4e  obs_R %.4e  pred %.4e  obs_R/pred q=3 %.4f  q=4 %.4f  q=5 %.4f"
                        % (cle, obs, a2["lnA_II"] - lnAK, r[4] * pred, pred, r[3], r[4], r[5]))
        etats[p] = "EXPLIQUE" if ok else "NON"
    return etats


out()
out("LECTURE (pred du premier ordre)")
e1 = lire(1)
for p in DEGRES:
    out("  p = %d : %s" % (p, e1[p]))
out()
out("TESTS NEGATIFS DE LA REGLE")
e0, e2 = lire(0), lire(2)
chk("pred = 0 -> aucun EXPLIQUE", all(v == "NON" for v in e0.values()), str(e0))
chk("pred x 2 -> NON la ou EXPLIQUE est sorti", all(e2[p] == "NON" for p in DEGRES if e1[p] == "EXPLIQUE"), str(e2))
out()
out("BILAN : %d controles, %d mordent %s" % (bilan["chk"], len(bilan["mord"]), bilan["mord"]))
with open(LOG, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lignes) + "\n")
print("log convention B %s ; script convention B %s" % (B(LOG), B(os.path.abspath(__file__))))
