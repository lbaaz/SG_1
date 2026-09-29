# LECTURE MACHINE 1 DU DOSSIER DE CONCEPTION "SECOND ORDRE" (machine 2, 13/09) -- ET CLOTURE DU DELTA 91
# machine 1, v1, 13/09/2026 (nuit). Classe C (lecture de conception ; rien d'opposable, aucun gel).
# PB-1 : rien d'edite. Les pieces de machine 2 sont rejouees ici, pas relues seulement.

## 0. EN QUATRE PHRASES

La derivation est rejouee sur machine 1 (levier X86_V4) : 93/93, le JSON de sortie est
IDENTIQUE AU BIT (b70fca94d72822ad), le log ne differe que par la ligne de plateforme et le
fichier du run ; l'exploration Richardson rejoue a l'identique. Ma projection du matin
(residuel en delta' x plancher, gains 1e+03 a 1e+04) etait FAUSSE et je la retire : les modes
libres de la linearisation autour de la solution auto-semblable ont des exposants complexes
de partie reelle alpha + 3/2, entre tau^2 et tau^4, et a p = 7 leur amplitude, libre, est du
meme ordre que le terme c1 -- c'est le resultat du dossier, et il est derive. Une faute de
citation est versee (D-SO-1) : le JSON du run v13 de BOCAL4 n'est pas au registre. Le delta 91
est clos (releve sur clone frais 729f9a9).

## 1. CE QUE J'AI VERIFIE MOI-MEME, HORS DU REJEU

  c1 A LA MAIN : dans x = A tau^-alpha (1 + c1 tau^2), le coefficient de tau^(-alpha-2) est
    c1 P2 + (1+w2^2) alpha(alpha+1) - (p-1) K c1, avec P2 = alpha(alpha+1)(alpha-1)(alpha-2)
    (derivee quatrieme de tau^(2-alpha)) et (p-1) K du developpement de u^(p-1) : c1 =
    (1+w2^2) alpha(alpha+1)/((p-1)K - P2). A p = 4 : P2 = 0, K = 120, c1 = (1+w2^2)/60 ; le
    terme c1 tau_dom'^2 = delta'/60, sans w2, 1/3 du plancher v7 = delta'/20. Concorde.
  MODES LIBRES, UNE LIGNE DE PLUS : le polynome m(m-1)(m-2)(m-3) - (p-1)K, m = beta - alpha,
    est symetrique par m -> 3 - m ; ses racines vont donc par paires (m, 3 - m) : (6, -3) a
    p = 4 -- d'ou beta = 8 et beta = -1 -- et la paire complexe a Re m = 3/2 EXACTEMENT,
    d'ou Re beta = alpha + 3/2 a tout degre. Ce n'est pas un fait numerique, c'est la
    symetrie du polynome ; a porter tel quel dans le gel v8.
  DISPERSION, AU TEXTE DE L'INSTRUMENT (v13 l.225-230) : dispersion_lnA(p) est le max sur
    les six points de (max - min) de lnA_II sur les trois grilles {(dt_2, k=2), (dt_2/2, k=2),
    (dt_2, k=4)}. C'est donc, par definition, la sensibilite de l'ajustement au pas et a la
    fenetre -- l'erreur d'integrateur, pas une dispersion physique. F2 est juste et, mieux,
    elle est definitionnelle : Richardson sur la jumelle retire ce que la "dispersion" mesure.
  LE 2 POUR CENT A p = 4 ET 5 : je le lis comme machine 2, sous la meme reserve d'ordre
    (q = 4 suppose ; q = 3 et 5 donnent 0.73 et 1.13). Avec p_obs = 3.9 a 3.98 au temoin,
    q = 4 est fonde, mais sur une autre grandeur : le troisieme niveau (Q2) est du.

## 2. D-SO-1 (machine 2 ; citation ; non bloquant ; numero propose)

  Le dossier cite out_run_delta91/alpha_v13/resultats_alpha.json b2c5f8cc47c6e611 "au registre,
  729f9a9". Au clone frais 729f9a9, le registre porte les JSON du run v12 (journal/
  lot_41208ad7ac1293cc__resultats_alpha.json edec88c7a9f3faf2, __resultats_temoin.json
  8d4c76d38726baf1) et AUCUN fichier de canon b2c5f8cc : le run v13 de BOCAL4 n'est ni
  depose ni transmis. Mon rejeu lit le v12 depose a sa place -- la section 5 (lecture a
  posteriori) rend les MEMES nombres a tous les points, le v13 n'ayant change que le 9bis --
  substitution declaree, sans effet. Le JSON v13 doit etre transmis ou depose avant
  d'ancrer quoi que ce soit ; une piece se cite par le canon d'un fichier tenu.

## 3. MA PLUME SUR Q1-Q5 (arbitrages operateur ; le gel v8 est a ma plume, il n'est pas ecrit)

  Q1  OUI a la seconde voie : le terme c1 tau^2, coefficient DERIVE et fixe, entre dans le
      modele de l'ajustement II ; plus de projection, plus de sensibilite de grille (1.3 pour
      cent). Le facteur 0.6727 disparait avec elle.
  Q2  OUI, et c'est une condition : un troisieme niveau (dt_2b/4) par point pour MESURER
      l'ordre q avant Richardson ; sans lui la tolerance d'instrument a p = 4, 5 n'est pas
      1e-8 mais l'ambiguite d'ordre, 3e-8. Cout negligeable (un etage 2b de plus).
  Q3  (iii) morte, d'accord, a consigner. Pour (i) contre (ii) : Q5 d'abord, puis le gel
      choisit. Ma reserve sur (i) : sur la fenetre [tau_CAP', 1.5 tau_dom'] le logarithme de
      tau court sur ~2.7, soit 1.2 periode de cos(2.9 ln tau) a p = 7 -- deux parametres
      libres (amplitude, phase) contre un terme tau^2 a coefficient fixe, la separation est
      possible mais marginale : le fit DOIT rendre son conditionnement, et le test negatif
      (frequence fausse -> pas d'amelioration) est obligatoire. (ii) est la voie sure : la
      tolerance de modele a p = 7 se MESURE sur l'ecart entre les deux c a (p, w2) fixe
      (7|1.73 : 0.14 contre 0.82 de pred), c'est une tolerance tiree des donnees, declaree
      avant le run suivant -- gain ~10 sur le plancher, pas 1.8e+03.
  Q4  OUI, P-A a deux regimes ecrit tel quel : instrument-limite a p = 4 et 5 (Richardson a
      ordre mesure), modele-limite a p = 7 (tolerance (ii)) sauf si (i) tient a Q5.
  Q5  OUI, premier geste, le moins cher. ET J'AJOUTE CE QUE LE 91 NE PEUT PAS DONNER, une
      prediction EN AVEUGLE pour le gel v8 : le biais du premier ordre est proportionnel a
      delta' (c1 tau_dom'^2 = delta' x constante de degre). A l'echelle du gel, n = 19
      (delta' = 1/36100, branche 5 au pre-vol de machine 1, a confirmer sur BOCAL4), la
      prediction du biais projete vaut biais(91) x 441/361 = 3.106e-07 (p = 4) et 3.213e-07
      (p = 5), a lire sur l'ecart P-A corrige par Richardson a ordre mesure, tolerance le
      residu de Richardson (~6e-9 a p = 4, ~5e-9 a p = 5, soit 2 pour cent). C'est un test
      que les series deposees ne contiennent pas, il ne coute qu'un run, et il tranche si le
      premier ordre est le terme ou seulement un terme. A p = 7 la meme prediction (2.930e-07)
      ne se lit qu'a la tolerance (ii).

## 4. CLOTURE DU DELTA 91

  Clone frais 729f9a9, plafond 91, 788 fichiers. L'acte depose est la v2
  (journal_delta_91_constante_A_run_v2.md, 035e19806db14910) : diff contre la v1 certifiee
  = H1 mot pour mot (le texte de ma certification), la ligne de version, le paragraphe de
  lignee, la ligne FIN ; aucun nombre ne change ; ma certification vaut pour la v2. Manifeste
  de depot v1 : 103 lignes sur 104 retrouvees au bit, la 104e etant l'acte v1 remplace par
  la v2. Perimetre rejoue avec la v2 au nouveau HEAD : 26 citations, 26 au registre, 0 non
  resolue ; les deux MORD sont ses assertions d'avant depot, attendus (comme au 90). Le lot
  435302fae671f4f8 est au registre. La reserve est close.

## 5. PIECES

  m1_rejeu_derivation_second_ordre.log / .json (JSON identique au bit a b70fca94d72822ad)
  m1_rejeu_exploration_richardson.log ; releve_perimetre_delta91_v2_HEAD_729f9a9_machine1.log

-- FIN note_machine1_lecture_second_ordre_v1 --
