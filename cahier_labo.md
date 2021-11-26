# <span style="font-family:Comic Sans MS">Cahier de laboratoire (genoscope)</span>

<!-- vscode-markdown-toc -->
* 1. [Semaine du 9/09/2021 au 22/10/2021](#Semainedu9092021au22102021)
* 2. [Semaine du 28/10/2021 au 18/11/2021](#Semainedu28102021au18112021)
	* 2.1. [Différences d'utilisation entre bcl2fastq et bcl-convert](#Diffrencesdutilisationentrebcl2fastqetbcl-convert)
	* 2.2. [Résultats test bcl2fastq (variation du paramètre p, r = 4 et w = 4)](#Rsultatstestbcl2fastqvariationduparamtrepr4etw4)
		* 2.2.1. [Tableau des performance de bcl2fastq](#Tableaudesperformancedebcl2fastq)
		* 2.2.2. [Graphiques des performances de bcl2fastq](#Graphiquesdesperformancesdebcl2fastq)
	* 2.3. [Résultats de bcl-convert](#Rsultatsdebcl-convert)

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
##  2. <a name='Semainedu28102021au18112021'></a>Semaine du 28/10/2021 au 18/11/2021

1. Test du soft bcl2fastq  
Test du temps de calcul de bcl2fstq et de la taille mémoire utiliser en fonction des paramètre -r (coeurs alloués en lecture), -p (coeurs alloués pour le processus), -w (coeurs alloués en écriture). (cf fichier )
1. lecture de la doc de bcl-convert  
Lecture de la doc cd bcl-convert, ayant pour objectif de déterminer les différences d'utilisation entre bcl2fasq et bcl-convert.