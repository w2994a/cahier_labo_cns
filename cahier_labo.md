# <span style="font-family:Comic Sans MS">Cahier de laboratoire (genoscope)</span>

<!-- vscode-markdown-toc -->
* 1. [Semaine du 9/09/2021 au 22/10/2021](#Semainedu9092021au22102021)
* 2. [Semaine du 28/10/2021 au 5/11/2021](#Semainedu28102021au5112021)
	* 2.1. [Différences d'utilisation entre bcl2fastq et bcl-convert](#Diffrencesdutilisationentrebcl2fastqetbcl-convert)
	* 2.2. [Résultats test bcl2fastq](#Rsultatstestbcl2fastq)
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
##  2. <a name='Semainedu28102021au5112021'></a>Semaine du 28/10/2021 au 5/11/2021

1. Test du soft bcl2fastq  
Test du temps de calcul de bcl2fstq et de la taille mémoire utiliser en fonction des paramètre -r (coeurs alloués en lecture), -p (coeurs alloués pour le processus), -w (coeurs alloués en écriture).
1. lecture de la doc de bcl-convert  
Lecture de la doc cd bcl-convert, ayant pour objectif de déterminer les différences d'utilisation entre bcl2fasq et bcl-convert.  

###  2.1. <a name='Diffrencesdutilisationentrebcl2fastqetbcl-convert'></a>Différences d'utilisation entre bcl2fastq et bcl-convert

__bcl2fastq :__  
Les options utilisés en ligne de commande sont :  
`--inputdir` ==> path des fichier BCL  
`--min-log-level` ==>  
`--barcode-mismatches` ==> nombre de mismatches acceptés sur les index  
`--runfolder-dir` ==> path du répertoire où le run à été effectué  
`--output-dir` ==> path du répertoire de sortie des fichiers générés par bcl2fastq (dont les FASTQ)  
`--use-base-mask` ==> indique le nobre de bases pris en compte pour les index  
`-r` ==> nombre de coeurs alloués en lecture (fichiers BCL)  
`-p` ==> nombre de coeurs alloués pour le processus de bcl2fastq  
`-w` ==> nombre de coeurs alloués en ecriture (FASTQ)  

Les autres options de bcl2fasq sont dans les fishier SampleSheet (seul le format V1 est accepté):  
`Lane`  
`Sample_ID`  
`Sample_name`  
`Sample_plate`  
`Sample_well`  
`I7_index_ID`
`index`  
`ìndex2`  
`Sample_Project`  
`Description`  

__diférences entre bcl2fastq et bcl-convert :__  


###  2.2. <a name='Rsultatstestbcl2fastq'></a>Résultats test bcl2fastq
| bcl2fastq||||||||
|---|---|---|---|---|---|---|---|
|MELISSE||||JARVIS|
|param utilisé|temps (s)|% temps cpu|mémoire utilisé (kb)|param utilisé|temps (s)|% temps cpu|mémoire utilisé (kb)|
|r2 p2 w2|0:53.01|172|2094712|r4 p16 w4|2:45:24|1322|11032040|
|r2 p4 w2|0:29.02|312|2325300|r8 p16 w8|2:45:25|1339|11149476|
|r4 p4 w4|0:27.27|297|2344384|r4 p14 w4||||
|r4 p8 r4|0:17.82|513|2368428|r8 p14 w4|2:43:15|1325|11099508|
|r4 p12 w4|0:07.78|559|2358444|r4 p12 w4||||
|r4 p12 w4|0:05.77|796|2381180|r8 p12 w8|3:21:32|1078|10504408|
|||||r4 p8 w4||||
|||||R8 p8 w8||||  

###  2.3. <a name='Rsultatsdebcl-convert'></a>Résultats de bcl-convert


