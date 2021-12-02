# <span style="font-family:Comic Sans MS">Benchmark entre bcl2fastq et bcl-convert </span>

<!-- vscode-markdown-toc -->
* 1. [Différences d'utilisation entre bcl2fastq et bcl-convert](#Diffrencesdutilisationentrebcl2fastqetbcl-convert)
* 2. [Résultats test bcl2fastq (variation du paramètre p avec r = 4 et w = 4)](#Rsultatstestbcl2fastqvariationduparamtrepavecr4etw4)
	* 2.1. [Tableau des performance de bcl2fastq](#Tableaudesperformancedebcl2fastq)
	* 2.2. [Graphiques des performances de bcl2fastq](#Graphiquesdesperformancesdebcl2fastq)
* 3. [Résultats test bcl2fastq (variation du paramètre r et w avec p = 12)](#Rsultatstestbcl2fastqvariationduparamtreretwavecp12)
	* 3.1. [Tableau des performance de bcl2fastq](#Tableaudesperformancedebcl2fastq-1)
	* 3.2. [Graphiques des performances de bcl2fastq](#Graphiquesdesperformancesdebcl2fastq-1)
* 4. [Résultats de bcl-convert](#Rsultatsdebcl-convert)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

Ce document à pour objectif de comparer les différences entre le logiciel de "_base calling_" bcl2fastq et BCL convert, qui sont des locgiciels de "_base calling_" conçue par illumina pour leurs séquenceurs.  

---
---

##  1. <a name='Diffrencesdutilisationentrebcl2fastqetbcl-convert'></a>Différences d'utilisation entre bcl2fastq et bcl-convert

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

__Différences d'utilisations en ligne de commande (utilisé actuellement) :__  
| bcl2fastq | bcl-convert | changement utilisation |
|---|---|---|
| `--inputdir` | None | Inpossible de spécifier le path des BaseCalls |
| `--min-log-level` | ? | ? |
| `--barcode-mismatches` | None | À mettre dans la Sample Sheet (dans la partie settings ==> `BarcodeMismatchesIndex1` / `BarcodeMismatchesIndex2`)| 
| `--runfolder-dir` | `--bcl-input-directory` | même utilisation  |
| `--output-dir` | `--output-directory` | même utilisation, mais devient obligatoire (utiliser `--force`/`-f` si le rep de sortie existe déjà) |
| `--sample-sheet` | `--sample-sheet` | même utilisation |
| `--use-base-mask` | None | À mettre dans la Sample Sheet (dans la partie settings ==> `OverrideCycles`) |
| `-r` | ? | même utilisation ? |
| `-p` | ? | même utilisation ? |
| `-w` | ? | même utilisation ? |

---
---

##  2. <a name='Rsultatstestbcl2fastqvariationduparamtrepavecr4etw4'></a>Résultats test bcl2fastq (variation du paramètre p avec r = 4 et w = 4)

###  2.1. <a name='Tableaudesperformancedebcl2fastq'></a>Tableau des performance de bcl2fastq

| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (h) | temps utilisateur (s) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 | 00:00:12.47 | 38.27 | 2.11 | 80.95 | 2.346448 |
| p8 | 00:00:07.59 | 40.22 | 2.96 | 71.12 | 2.361540 |
| p12 | 00:00:06.45 | 40.31 | 2.90 | 55.75 | 2.386592 |
| p16 | 00:00:11.31 | 60.38 | 2.24 | 34.56 | 2.365040 |
| JARVIS |
| param utilisé | temps écoulé (h) | temps utilisateur (s) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 | 10:48:31 + 11:35:17 | 153657.02 + 160546.74 | 987.10 + 1242.42 | 99.25 + 96.75 | 12.459632 + 26.311436 |
| p8 | 5:48:32 + 6:13:34 | 163311.33 + 169181.39 | 1987.22 + 1141.71 | 98.75 + 94.88 | 12.226456 + 29.826448 |
| p12 | 4:04:10 + 4:36:05 | 169691.13 + 181498.04 | 2605.74 + 1216.34 | 98.00 + 91.83 | 10.649516 + 35.187044 |
| p16 | 2:58:41 + 5:51:39 | 166134.80 + 312672.50 | 1004.25 + 1743.75 | 97.38 + 93.13 | 11.353516 + 43.053008 |


###  2.2. <a name='Graphiquesdesperformancesdebcl2fastq'></a>Graphiques des performances de bcl2fastq

![perf_melisse](img/temps_bcl2fastq.png "Histogramme du temps total en fonction du temps (Melisse)")  

##  3. <a name='Rsultatstestbcl2fastqvariationduparamtreretwavecp12'></a>Résultats test bcl2fastq (variation du paramètre r et w avec p = 12)  
###  3.1. <a name='Tableaudesperformancedebcl2fastq-1'></a>Tableau des performance de bcl2fastq
| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (h) | temps utilisateur (s) | temps cpu (s) |  utilisation cpu (%) |mémoire utilisé (Gb) |
| r4 w4 | 00:00:08.58 | 55.72 | 2.26 | 56.25 | 2.360844 |
| r8 w8 | 00:00:18.38 | 55.74 | 2.37 | 26.33 | 2.354396 |
| r12 w12 | 00:00:07.51 | 54.40 | 2.87 | 63.50 | 2.359704 |
| JARVIS |
| param utilisé | temps écoulé (h) | temps utilisateur (s) | temps cpu (s) |  utilisation cpu (%) |mémoire utilisé (Gb) |
| r4 w4 | 4:04:10 + 4:36:05 | 169691.13 + 181498.04 | 2605.74 + 1216.34 | 98.00 + 91.83 | 10.649516 +  35.187044 |
| r8 w8 | 03:57:35 + 04:38:53 | 167379.46 + 185892.51 | 1112.35 + 1309.78 | 98.42 + 93.17 | 12.122880 + 37.427376 |
| r12 w12 | 04:01:35 + 04:34:25 | 170304.54 + 182109.10 | 1200.01 + 1514.94 | 98.58 + 92.92 | 11.171612 + 38.953616 |  

###  3.2. <a name='Graphiquesdesperformancesdebcl2fastq-1'></a>Graphiques des performances de bcl2fastq
![perf_melisse](img/temps2_bcl2fastq.png "Histogramme du temps total en fonction du temps (Melisse)") 

##  2. <a name='Rsultatstestbcl2fastqvariationduparamtrepavecr4etw4'></a>Résultats test bcl2fastq (variation du paramètre p, r et w)

###  2.1. <a name='Tableaudesperformancedebcl2fastq'></a>Tableau des performance de bcl2fastq

| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (h) | temps utilisateur (s) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 r4 w4 | 00:00:12.47 | 38.27 | 2.11 | 80.95 | 2.346448 |
| p8 r8 w8 | 00:00:34.75 | 49.85 | 2.13 | 18.63 | 1.869064 |
| p12 r12 w12 | 00:00:07.51 | 54.40 | 2.90 | 63.50 | 2.359704 |
| p16 r16 w16 | 00:00:08.02 | 59.95 | 3.17 | 49.19 | 2.360132 |
| JARVIS |
| param utilisé | temps écoulé (h) | temps utilisateur (s) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 r4 w4 | 10:21:47 + 16:42:32 | 147372.51 + 214068.47 | 997.21 + 1581.48 | 99.20 + 89.50 | 10.226312 + 22.814680 |
| p8 r8 w8 | 05:40:55 + 6:51:09 | 159463.53 + 171599.59 | 1014.37 + 3312.31 | 98.00 + 88.63 | 10.509808 + 30.503808 |
| p12 r12 w12 | 4:01:35 + 4:34:25 | 170304.54 + 182109.10 | 1200.01 + 1514.94 | 98.58 + 92.92 | 11.171612 + 38.953616 |
| p16 r16 w16 | 3:24:32 + 3:40:24 | 164043.36 + 179308.08 | 1115.50 + 2165.33 | 84.06 + 85.75 | 11.793640 + 44.042212 |


###  2.2. <a name='Graphiquesdesperformancesdebcl2fastq'></a>Graphiques des performances de bcl2fastq

![perf_melisse](img/temps_bcl2fastq.png "Histogramme du temps total en fonction du temps (Melisse)")  

---
---

##  4. <a name='Rsultatsdebcl-convert'></a>Résultats de bcl-convert