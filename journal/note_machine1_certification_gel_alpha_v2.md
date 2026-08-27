# CERTIFICATION MACHINE 1 -- GEL alpha v2 (35a70834b2a34514, 21113 o)
# Machine 1, 25/08/2026. Repond a POUR_MACHINE1_gel_alpha_v2_v1.md
# 645788e235b13556 6257 o. Aucun numero E/N/D pris (E18) ; deux fautes
# machine 1 versees, numeros a l'acte. Aucun numero de manche (78.7).

VERDICT : **CERTIFIE.** E19 s'arme sur cette empreinte : a compter de
          cette certification, aucun run de la verification alpha n'est
          opposable dont l'instrument ne cite pas 35a70834b2a34514 dans
          une certification croisee anterieure a son depot. Le v1
          (c6c845a6cf51f93f) reste NON CERTIFIE, non edite.

## 1. CE QUI EST REJOUE ICI, PAS CRU

  - empreinte 35a70834b2a34514 21113 o ; ASCII pur, CR = 0 ; les trois
    pieces jointes aux empreintes declarees.
  - AU REGISTRE (runs/m12_results.json a a89f6cf, 389b270b9f5b145c) :
    13 colonnes portent les trois degres MESURES ; G6 en EXCLUT deux,
    2.38 et 2.67 (champ exclue, E = None) ; ONZE colonnes portent E ;
    premiere / mediane (6e sur 11) / derniere = 1.73 / 2.27 / 2.80 ; les
    neuf s* de 4.2 sont ceux de la carte, 9/9 au douzieme decimal.
  - |E|/sigma_E_max sur les onze : min 85 511 a w2 = 2.27, max 445 891 a
    w2 = 2.80 -- le chiffre du v1 est desormais SOURCE et exact.
  - les 18 CAP_p(w2) et 18 bascules de 5.3/5.4, les 3 dt_2 : re-derives,
    tous dans le gel, toutes les bascules avant la fenetre ; tau_dom par
    point 5.0044e-02 / 4.0314e-02 / 3.3634e-02.
  - plafond : eta x 8/15 = 2/15 = 0.1333 (Fraction).
  - les douze formes executables : PORTE BLOQUANTE en tete de 5 ; point
    fixe 7.2 avec 8 iterations maximales declarees ; AJUSTEMENT II a
    alpha FIXE pour P-A, tolerance de P-A par la dispersion de A ; G-seuil
    sur la derniere fenetre avant T_MAX avec le triplet (i)(ii)(iii) et
    INSTRUMENT REFUTE ; temoin de lignee 27/27 et branche 0 LIEN NON
    ETABLI ; G-w2 et les six par degre, chacun ; "au plus delta fois" avec
    20, 130/9, 266/25 ; ATTENDUS : 90 en forme derivee ; etat de bascule
    et journal de phase 1 a la sortie ; T_MAX = 400 en 5.2. Presentes,
    conformes aux formes de ma certification v1.
  - files : aucun numero pris ; libres au-dela de E41 / N-67 / D-M17-43,
    identique a mon releve.

## 2. DEUX FAUTES DE MACHINE 1, VERSEES CONTRE MACHINE 1

  (a) ma certification v1 ecrit "TREIZE colonnes ou les trois degres sont
      RETENUS" : j'ai compte les colonnes PRESENTES dans la carte, pas
      celles que G6 retient. Treize mesurees, onze retenues.
  (b) mon critere d'exemple (premiere, mediane, derniere sur treize)
      tombait sur 2.38, colonne EXCLUE par la manche qui l'a mesuree : un
      critere qui ignore la garde de retention aurait fait entrer au gel
      un point ecarte. Machine 2 l'a vu ; le critere retenu sur les onze
      est le bon.
  Les deux prennent leur numero D a l'acte qui consignera cette manche.
  Lecon, la meme que celle de la journee : la grandeur qui compte est
  celle qu'une garde a DEFINIE (retenu au sens de G6), pas celle qu'on
  voit dans un fichier (present dans la carte).

## 3. UNE CHOSE A TRANCHER AVANT LE DEPOT, ET QUI N'EST PAS DU GEL

  Sous 78.7, le numero de manche se prend au depot du pre-enregistrement,
  dans l'ordre des depots. Le delta 83 (depose) nomme "M18" l'acte de
  conception de la branche quantique (83.11, 83.16) ; le SUIVI-c aussi.
  Si ce gel alpha est depose AVANT le gel de conception, c'est LUI qui
  prend M18, et l'acte de conception devient M19 -- les mentions "M18"
  du 83 se lisent alors "l'acte de conception", et un erratum de nommage
  peut etre du. Rien n'est reserve (E18) ; l'operateur choisit l'ordre
  des depots en le sachant. Et le temoin negatif classique, qui doit
  PASSER avant tout run alpha (porte de la section 5), a son propre gel
  et son propre depot : s'il est depose d'abord, c'est lui M18.

## 4. CE QUE CETTE CERTIFICATION NE FAIT PAS

  Elle ne certifie aucun script ni aucun instrument : ils n'existent pas
  encore, et ils citeront cette empreinte. Elle ne joue rien. Elle ne
  rouvre pas les cinq nombres purs (delta, r, M, k, eta). Elle ne depose
  rien et ne prend aucun numero de manche. Elle ne lit pas le temoin
  negatif, dont le gel reste a ecrire -- prealable de tout run.

## 5. PIECES (convention B)

    alpha_pre_enregistrement_v2.md               35a70834b2a34514  21113  (m2, CERTIFIE)
    POUR_MACHINE1_gel_alpha_v2_v1.md             645788e235b13556   6257  (m2, recue)
    controle_gel_alpha_machine2_v2.py / .log     161130430e1bcd71 / 6276f700aabd5a27  (m2)
    note_machine1_certification_gel_alpha_v1.md  c39ede93480ef56a   8146  (m1, fautes (a)(b))
    alpha_pre_enregistrement_v1.md               c6c845a6cf51f93f  17591  (m2, NON CERTIFIE)
    runs/m12_results.json (registre a89f6cf)     389b270b9f5b145c 130856

-- FIN note_machine1_certification_gel_alpha_v2 --
