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
Test du temps de calcul de bcl2fstq et de la taille mémoire utiliser en fonction des paramètre -r (coeurs alloués en lecture), -p (coeurs alloués pour le processus), -w (coeurs alloués en écriture).
1. lecture de la doc de bcl-convert  
Lecture de la doc cd bcl-convert, ayant pour objectif de déterminer les différences d'utilisation entre bcl2fasq et bcl-convert.  

###  2.1. <a name='Diffrencesdutilisationentrebcl2fastqetbcl-convert'></a>Différences d'utilisation entre bcl2fastq et bcl-convert

__bcl2fastq :__  
Options utilisées en ligne de commande :  
`--inputdir` ==> path des fichier BCL  
`--min-log-level` ==>  
`--barcode-mismatches` ==> nombre de mismatches acceptés sur les index  
`--runfolder-dir` ==> path du répertoire où le run à été effectué  
`--output-dir` ==> path du répertoire de sortie des fichiers générés par bcl2fastq (dont les FASTQ)  
`--use-base-mask` ==> indique le nobre de bases pris en compte pour les index  
`-r` ==> nombre de coeurs alloués en lecture (fichiers BCL)  
`-p` ==> nombre de coeurs alloués pour le processus de bcl2fastq  
`-w` ==> nombre de coeurs alloués en ecriture (FASTQ)  

Autres options :  
`--sample-sheet` ==> path de la sample sheet (par défaut : <`runfolder-dir`>/SampleSheet.csv)  

Options de bcl2fasq dans les fichiers SampleSheet (seul le format V1 est accepté) :  
Data section :  
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


__bcl-convert :__  
Option utilisées en ligne de commande :  
`--bcl-input-directory` ==> path du répertoire où le run à été effectué   
`--output-directory` ==> path du répertoire de sortie des fichiers générés par bcl-convert. cette option est obligatoire et le répertoire spécifié ne doit pas exister. (si le répertoire existe alors il faut utiliser `--force` / `-f` en plus)  
`--sample-sheet` ==> path de la sample sheet (oblgatoire, par défaut : <`--bcl-input-directory`>/SampleSheet.csv)  
Option non mentionnées dans la doc de bcl-convert :  
`-r` ==> nombre de coeurs alloués en lecture (fichiers BCL)  
`-p` ==> nombre de coeurs alloués pour le processus de bcl2fastq  
`-w` ==> nombre de coeurs alloués en ecriture (FASTQ)

Option de bcl-convert dans les fichiers SampleSheet (formats V1 et V2 acceptés) :  
Data section (comme pour bcl2fastq):  
`Lane`  
`Sample_ID`  
`index`  
`ìndex2`  
`Sample_Project`  
Settings section :  
`BarcodeMismatchesIndex1`  
`BarcodeMismatchesIndex2` 
`OverrideCycles` 

__Différence utilisation en ligne de commande :__  
| bcl2fastq | bcl-convert | changement utilisation |
|---|---|---|
| `--inputdir` | None | Inpossible de spécifier le path des BaseCalls |
| `--min-log-level` ? | ? | ? |
| `--barcode-mismatches` | None | À mettre dans la Sample Sheet (dans la partie settings ==> `BarcodeMismatchesIndex1` / `BarcodeMismatchesIndex2`)| 
| `--runfolder-dir` | `--bcl-input-directory` | même utilisation  |
| `--output-dir` | `--output-directory` | même utilisation, mais devient obligatoire (utiliser `--force`/`-f` si le rep de sortie existe déjà) |
| `--sample-sheet` | `--sample-sheet` | même utilisation |
| `--use-base-mask` | None | À mettre dans la Sample Sheet (dans la partie settings ==> `OverrideCycles`) |
| `-r` | ? | même utilisation ? |
| `-p` | ? | même utilisation ? |
| `-w` | ? | même utilisation ? |

###  2.2. <a name='Rsultatstestbcl2fastqvariationduparamtrepr4etw4'></a>Résultats test bcl2fastq (variation du paramètre p, r = 4 et w = 4)

####  2.2.1. <a name='Tableaudesperformancedebcl2fastq'></a>Tableau des performance de bcl2fastq

| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (s) | temps utilisateur (s) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 | 0:12.47 | 38.27 | 2.11 | 80.95 | 2.346448 |
| p8 | 0:07.59 | 40.22 | 2.96 | 71.12 | 2.361540 |
| p12 | 0:06.45 | 40.31 | 2.90 | 55.75 | 2.386592 |
| p16 | 0:11.31 | 60.38 | 2.24 | 34.56 | 2.365040 |
| JARVIS |
| param utilisé | temps écoulé (s) | temps utilisateur (s) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 | ? | ? | ? | ? | ? |
| p8 | ? | ? | ? | ? | ? |
| p12 | 4:04:10 + 4:36:05 | 169691.13 + 181498.04 | 2605.74 + 1216.34 | 98.00 + 91.83 | 10.649516 + 35.187044 |
| p16 | 2:58:41 + 5:51:39 | 166134.80 + 312672.50 | 1004.25 + 1743.75 | 97.38 + 93.13 | 11.353516 + 43.053008|

Relancer les job pour p = 4 et 8 avec une limite de temps de 16h au lieu de 8h.  
Comment ne pas tuer un job quand on quitte le terminal ?
####  2.2.2. <a name='Graphiquesdesperformancesdebcl2fastq'></a>Graphiques des performances de bcl2fastq

![perf_melisse](img/temps_melisse_bcl2fastq.png "Histogramme du temps total en fonction du temps (Melisse)")

###  2.3. <a name='Rsultatsdebcl-convert'></a>Résultats de bcl-convert


