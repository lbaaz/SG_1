# LECTURE PRE-DECLAREE Q5 -- LES MODES LIBRES S'AJUSTENT-ILS SUR LES SERIES DU 91 ?
# machine 2, 2026-09-13 (soir), APRES accord Q5 des deux machines (note machine 1
# c8390c986806649b) et "go" de l'operateur ; AVANT tout ajustement sur une serie.
# Classe C, detenteur machine 2. Lecture de conception, a posteriori, NON opposable (N-70).

## 0. CE QUE JE SAIS DEJA -- DECLARE

Du run 91 : les lnA_II du JSON (cellules plan, G_dt, G_k) et, par l'exploration Richardson
(28f599270bcce9ea), obs_R - ln(K/g)/(p-2) aux 18 points : a p = 7 ils vont de 3.3e-08 a
2.85e-07 (ecart max-min ~2.5e-07) ; a p = 4 et 5 ils tiennent a +/- 6e-09 du biais c1.
Des series : le format (t x1 x2, %.17g, en-tete) et rien d'autre. Aucun ajustement fait.

## 1. LES MODELES (tous derives ; aucun coefficient ajuste hors ceux nommes)

Sur la fenetre de point fixe de l'instrument (indices de `ajuster_point_fixe` du v13), y =
ln|x1 + x2|, tau = t* - t, s = tau / tau_dom'(w2), alpha = 4/(p-2), t* minimise par
`_minimiser_1d` de l'instrument sur ses bornes :

  M1   y + alpha ln tau - c1 tau^2 = lnA                         (c1 DERIVE, dossier C2)
  M2   ... = lnA + s^b [a cos(w ln s) + c sin(w ln s)]           (b = alpha + 3/2, w DERIVE C3)
  M2-  idem a w/2      M2+  idem a 2w       (FREQUENCES FAUSSES : tests negatifs, m1 3.Q3)

Par point : lnA_R = lnA(dt/2) + (lnA(dt/2) - lnA(dt))/15 (q = 4 SUPPOSE -- Q2 non disponible).
Par degre : S_M(p) = max - min des six lnA_R. **A est universelle (ni w2 ni c) : S ne
contient pas K.** L'ecart a K se CONSIGNE et n'entre dans AUCUN verdict.

## 2. CONTROLES QUI PEUVENT MORDRE

  C0  controle positif de lecture : `ajuster_point_fixe` du v13 sur chaque serie dt2_k2,
      dt2s2_k2, dt2_k4 rend le lnA_II du JSON (cellules plan, G_dt, G_k) a 1e-13 pres,
      aux 54 series. MORD sinon -> je ne lis pas les series que le run a ajustees, rien
      d'autre ne se lit.
  C0b M1 a c1 = 0 rend lnA_II de l'instrument a 1e-12 pres (mon ajustement = le sien).
  C0c conditionnement de M2 CONSIGNE par point (colonnes normalisees) ; un lstsq de rang < 3
      MORD.

## 3. LA REGLE DE LECTURE (ecrite avant)

  Q5-a  a p = 7 :  S_M2(7) <= S_M1(7) / 3
  Q5-b  a p = 7 :  S_M2-(7) > S_M1(7) / 3  ET  S_M2+(7) > S_M1(7) / 3
                   (une frequence fausse ne doit PAS rendre le meme gain)
  Q5-c  a p = 4 et 5 : S_M2(p) <= 2 S_M1(p)  (M2 ne detruit pas ce qui tient)

  (i) TIENT A p = 7          si Q5-a et Q5-b
  (i) NON SPECIFIQUE         si Q5-a sans Q5-b (le gain est celui de deux parametres de plus)
  (i) NE TIENT PAS           si Q5-a echoue -> voie (ii) (tolerance mesuree), comme m1 le propose
  Q5-c echoue                -> (i) se restreint a p = 7 et le gel le dit

  PORTEE : six points par degre, q suppose, un seul run, sur BOCAL4 ; un TIENT ici autorise
  seulement a PREDIRE (i) au gel v8, il ne le valide pas.

-- FIN lecture_predeclaree_Q5_modes_libres_machine2_v1 --
