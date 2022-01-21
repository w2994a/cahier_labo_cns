# <span style="font-family:Comic Sans MS">Cahier de laboratoire (genoscope)</span>

<!-- vscode-markdown-toc -->
* 1. [Semaine du 9/09/2021 au 22/10/2021](#Semainedu9092021au22102021)
* 2. [Semaine du 28/10/2021 au 23/12/2021](#Semainedu28102021au23122021)
* 3. [Semaine du 20/01/2022 au ??/??/2022](#Semainedu20012022au2022)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

---
---
##  1. <a name='Semainedu9092021au22102021'></a>Semaine du 9/09/2021 au 22/10/2021

1. Apprentisage du langage Perl
1. Codage d'un petit programme Perl qui réalise quelques statistiques simple sur un fichier FASTQ  
Le programme prend en argument un fichier FASTQ. Les options du programme (au moins une parmis : h, n, t, q, l):
    - -h : donne l'usage du programme
    - -p : indique le second fichier FASTQ si paired
    - -l : donne la longueur de chaque reads
    - -n : donne le nombre de chacunes des bases de chaque reads (A, T, C, G, N si inconnu)
    - -t : donne le taux de CG dans chaque reads
    - -q : donne le minimum, le maximum et la moyenne de la qualité de chaque reads
    
    <mark><span style="color:red"> rq : ajouter code corriger sur github</span><mark>
1. Apprentisage de l'utilisation des modules et du lancement de jobs sur les clusters de calculs.


---
##  2. <a name='Semainedu28102021au23122021'></a>Semaine du 28/10/2021 au 23/12/2021

1. Test du soft bcl2fastq  
Test du temps de calcul de bcl2fstq et de la taille mémoire utiliser en fonction des paramètre -r (coeurs alloués en lecture), -p (coeurs alloués pour le processus), -w (coeurs alloués en écriture). (cf fichier )
1. lecture de la doc de bcl-convert  
Lecture de la doc cd bcl-convert, ayant pour objectif de déterminer les différences d'utilisation entre bcl2fasq et bcl-convert.  
1. test de bcl-convert, pour tenter de reproduire les mêmes résultats que bcl2fastq.
	- cf. rapport du benchmark entre bcl2fastq et bcl-convert.
	- Les sorties de bcl-convert sont différentes dde bcl2fastq et il est impossible de reproduire la même arborescence obtenu avec bcl2fastq. Il faut donc soit adapter les workflow qui utilisaient ces sorties ou bien créer un worflow qui ce chargera de créer la même arborescence de bcl2fastq. Néaimoins si la seconde méthodes est priviligier il y aura quand des adaptation à faire car le format des fichier de sortie (notament ceux des stats) sont différents.

##  3. <a name='Semainedu20012022au2022'></a>Semaine du 20/01/2022 au ??/??/2022

1. Préparation du diapo et de la soutenance pour le 24/01/2022 (20 et 21/01/2022)
1. Rédaction du rapport de 5 pages pour le 03/02/2022.
