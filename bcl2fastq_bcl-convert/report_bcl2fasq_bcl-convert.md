 # <span style="font-family:Comic Sans MS">Benchmark entre bcl2fastq et bcl-convert </span>

<!-- vscode-markdown-toc -->
* 1. [Différences d'utilisation entre bcl2fastq et bcl-convert](#Diffrencesdutilisationentrebcl2fastqetbcl-convert)
* 2. [Résultats test bcl2fastq (variation du paramètre p avec r = 4 et w = 4)](#Rsultatstestbcl2fastqvariationduparamtrepavecr4etw4)
	* 2.1. [Tableau des performance de bcl2fastq](#Tableaudesperformancedebcl2fastq)
	* 2.2. [Graphiques des performances de bcl2fastq](#Graphiquesdesperformancesdebcl2fastq)
		* 2.2.1. [Temps total](#Tempstotal)
		* 2.2.2. [Temps cpu](#Tempscpu)
* 3. [Résultats test bcl2fastq (variation du paramètre r et w avec p = 12)](#Rsultatstestbcl2fastqvariationduparamtreretwavecp12)
	* 3.1. [Tableau des performance de bcl2fastq](#Tableaudesperformancedebcl2fastq-1)
	* 3.2. [Graphiques des performances de bcl2fastq](#Graphiquesdesperformancesdebcl2fastq-1)
		* 3.2.1. [Temps total](#Tempstotal-1)
		* 3.2.2. [Temps cpu](#Tempscpu-1)
* 4. [Résultats test bcl2fastq (variation du paramètre p, r et w)](#Rsultatstestbcl2fastqvariationduparamtrepretw)
	* 4.1. [Tableau des performance de bcl2fastq](#Tableaudesperformancedebcl2fastq-1)
	* 4.2. [Graphiques des performances de bcl2fastq](#Graphiquesdesperformancesdebcl2fastq-1)
		* 4.2.1. [Temps total](#Tempstotal-1)
		* 4.2.2. [Temps cpu](#Tempscpu-1)
* 5. [Résultats test bcl2fastq (variation du paramètre r et w avec p = 8)](#Rsultatstestbcl2fastqvariationduparamtreretwavecp8)
	* 5.1. [Tableau des performance de bcl2fastq](#Tableaudesperformancedebcl2fastq-1)
	* 5.2. [Graphiques des performances de bcl2fastq](#Graphiquesdesperformancesdebcl2fastq-1)
		* 5.2.1. [Temps total](#Tempstotal-1)
		* 5.2.2. [Temps cpu](#Tempscpu-1)
* 6. [Tableau récapitulatif des résultats obtenus pour bcl2fastq](#Tableaurcapitulatifdesrsultatsobtenuspourbcl2fastq)
	* 6.1. [MELISSE](#MELISSE)
	* 6.2. [JARVIS](#JARVIS)
* 7. [Résultats de bcl-convert](#Rsultatsdebcl-convert)

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
`-d` ==> nombre de coeurs alloués pour le démultipléxage  

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
`--bcl-sampleproject-subdirectories` ==> création de sous-répertoires Sample_ Project comme spécifié dans la SampleSheet  
`--bcl-num-decompression-threads` ==> nombre de coeurs alloués en lecture (fichiers BCL)  
`--bcl-num-conversion-threads` ==> nombre de coeurs alloués pour le processus de bcl2fastq  
`--bcl-num-compression-threads` ==> nombre de coeurs alloués en ecriture (FASTQ)  
`--bcl-num-parallel-tiles` ==>  nombre de tâche effectuer en parallèle  

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
| `-r` | `--bcl-num-decompression-threads` | même utilisation |
| `-p` | `--bcl-num-conversion-threads` | même utilisation |
| `-w` | `--bcl-num-compression-threads` | même utilisation |
| None | `--bcl-num-parallel-tiles` | spécifier le nombre de tâche à efectuer en parallèle
---
---

##  2. <a name='Rsultatstestbcl2fastqvariationduparamtrepavecr4etw4'></a>Résultats test bcl2fastq (variation du paramètre p avec r = 4 et w = 4)

###  2.1. <a name='Tableaudesperformancedebcl2fastq'></a>Tableau des performance de bcl2fastq

| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (h) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 w4 r4 | 00:00:12.47 | 40.38 | 80.95 | 2.346448 |
| p8 w4 r4 | 00:00:07.59 | 43.18 | 71.12 | 2.361540 |
| p12 w4 r4 | 00:00:06.45 | 43.21 | 55.75 | 2.386592 |
| p16 w4 r4 | 00:00:11.31 | 62.62 | 34.56 | 2.365040 |
| JARVIS |
| param utilisé | temps écoulé (h) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 w4 r4 | 10:48:31 + 11:35:17 | 154644.12 + 161789.16 | 99.25 + 96.75 | 12.459632 + 26.311436 |
| p8 w4 r4 | 05:48:32 + 06:13:34  | 165298.55 + 170323.1 | 98.75 + 94.88 | 12.226456 + 29.826448 |
| p12 w4 r4 | 04:04:10 + 04:36:05 | 172296.87 + 182714.38 | 98.00 + 91.83 | 10.649516 + 35.187044 |
| p16 w4 r4 | 02:58:41 + 05:51:39 | 167139.05 + 314416.25 | 97.38 + 93.13 | 11.353516 + 43.053008 |


###  2.2. <a name='Graphiquesdesperformancesdebcl2fastq'></a>Graphiques des performances de bcl2fastq

####  2.2.1. <a name='Tempstotal'></a>Temps total
![](img/temps_total1.png "") 

####  2.2.2. <a name='Tempscpu'></a>Temps cpu
![](img/temps_cpu1.png "")  

#### Barplot cummulé des deux run de JARVIS (NovaSeq 6000)
![](img/barplot_cum_jarvis1.png "")

##  3. <a name='Rsultatstestbcl2fastqvariationduparamtreretwavecp12'></a>Résultats test bcl2fastq (variation du paramètre r et w avec p = 12)  
###  3.1. <a name='Tableaudesperformancedebcl2fastq-1'></a>Tableau des performance de bcl2fastq
| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (h) | temps cpu (s) |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p12 r4 w4 | 00:00:08.58 | 57.98 | 56.25 | 2.360844 |
| p12 r8 w8 | 00:00:18.38 | 58.11 | 26.33 | 2.354396 |
| p12 r12 w12 | 00:00:07.51 | 57.26 | 63.50 | 2.359704 |
| JARVIS |
| param utilisé | temps écoulé (h) | temps cpu (s) |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p12 r4 w4 | 04:04:10 + 04:36:05 | 172296.87 + 182714.38 | 98.00 + 91.83 | 10.649516 +  35.187044 |
| p12 r8 w8 | 03:57:35 + 04:38:53 | 168491.81 + 187202.29 | 98.42 + 93.17 | 12.122880 + 37.427376 |
| p12 r12 w12 | 04:01:35 + 04:34:25 | 171504.55 + 183624.04 | 98.58 + 92.92 | 11.171612 + 38.953616 |  

###  3.2. <a name='Graphiquesdesperformancesdebcl2fastq-1'></a>Graphiques des performances de bcl2fastq

####  3.2.1. <a name='Tempstotal-1'></a>Temps total
![](img/temps_total2.png "") 

####  3.2.2. <a name='Tempscpu-1'></a>Temps cpu
![](img/temps_cpu2.png "")  

#### Barplot cummulé des deux run de JARVIS (NovaSeq 6000)
![](img/barplot_cum_jarvis2.png "")

##  4. <a name='Rsultatstestbcl2fastqvariationduparamtrepretw'></a>Résultats test bcl2fastq (variation du paramètre p, r et w)

###  4.1. <a name='Tableaudesperformancedebcl2fastq-1'></a>Tableau des performance de bcl2fastq

| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (h) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 r4 w4 | 00:00:12.47 | 40.38 | 80.95 | 2.346448 |
| p8 r8 w8 | 00:00:34.75 | 51.98 | 18.63 | 1.869064 |
| p12 r12 w12 | 00:00:07.51 | 57.30 | 63.50 | 2.359704 |
| p16 r16 w16 | 00:00:08.02 | 60.47 | 49.19 | 2.360132 |
| JARVIS |
| param utilisé | temps écoulé (h) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p4 r4 w4 | 10:21:47 + 16:42:32 | 148369.72 + 215649.95 | 99.20 + 89.50 | 10.226312 + 22.814680 |
| p8 r8 w8 | 05:40:55 + 06:51:09 | 160477.90 + 174911.9 | 98.00 + 88.63 | 10.509808 + 30.503808 |
| p12 r12 w12 | 04:01:35 + 04:34:25 | 171504.55 + 183624.04 | 98.58 + 92.92 | 11.171612 + 38.953616 |
| p16 r16 w16 | 03:24:32 + 03:40:24 | 165158.86 + 181473.41 | 84.06 + 85.75 | 11.793640 + 44.042212 |


###  4.2. <a name='Graphiquesdesperformancesdebcl2fastq-1'></a>Graphiques des performances de bcl2fastq

####  4.2.1. <a name='Tempstotal-1'></a>Temps total
![](img/temps_total3.png "") 

####  4.2.2. <a name='Tempscpu-1'></a>Temps cpu
![](img/temps_cpu3.png "") 

#### Barplot cummulé des deux run de JARVIS (NovaSeq 6000)
![](img/barplot_cum_jarvis3.png "")

##  5. <a name='Rsultatstestbcl2fastqvariationduparamtreretwavecp8'></a>Résultats test bcl2fastq (variation du paramètre r et w avec p = 8)

###  5.1. <a name='Tableaudesperformancedebcl2fastq-1'></a>Tableau des performance de bcl2fastq

| bcl2fastq ||||||
|---|---|---|---|---|---|
| MELISSE |
| param utilisé | temps écoulé (h) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p8 r2 w2 | 00:00:36.49 | 53.16 | 18.13 | 1.872452 |
| p8 r4 w4 | 00:00:07.59 | 43.18 | 71.00 | 2.361540 |
| p8 r6 w6 | 00:00:08.55 | 50.79 | 74.25 | 2.346620 |
| p8 r8 w8 | 00:00:34.75 | 51.98 | 18.63 | 1.869064 |
| JARVIS |
| param utilisé | temps écoulé (h) | temps cpu |  utilisation cpu (%) |mémoire utilisé (Gb) |
| p8 r2 w2 | 05:56:38 + 06:50:56 | 167567.71 + 188531.43 | 97.88 + 95.5 | 10.172972 + 27.979624 |
| p8 r4 w4 | 05:48:32 + 06:13:34 | 165298.55 + 170323.10 | 98.75 + 94.88 | 12.226456 + 29.826448 |
| p8 r6 w6 | 05:54:49 + 06:31:55 | 167594.55 + 180114.75 | 98.38 + 95.63 | 10.559480 + 30.853492 |
| p8 r8 w8 | 05:40:55 + 06:51:09 | 160477.90 + 174911.90 | 98.0 + 88.63 | 10.509808 + 30.503808 |



###  5.2. <a name='Graphiquesdesperformancesdebcl2fastq-1'></a>Graphiques des performances de bcl2fastq

####  5.2.1. <a name='Tempstotal-1'></a>Temps total
![](img/temps_total4.png "") 

####  5.2.2. <a name='Tempscpu-1'></a>Temps cpu
![](img/temps_cpu4.png "")  

#### Barplot cummulé des deux run de JARVIS (NovaSeq 6000)
![](img/barplot_cum_jarvis4.png "")

---

##  6. <a name='Tableaurcapitulatifdesrsultatsobtenuspourbcl2fastq'></a>Tableau récapitulatif des résultats obtenus pour bcl2fastq
###  6.1. <a name='MELISSE'></a>MELISSE

|type run|param utilisé|temps écoulé (h : m : s)|temps cpu (h : m : s)| utilisation cpu (%)|mémoire utilisé (Gb)|
| --- | --- | --- | --- | --- | --- |
|MELISSE|p4 r4 w4|00:00:12.47|00:00:40|80.95|2.346448|
|MELISSE|p8 r4 w4|<span style="color: green">00:00:07.59</span>|00:00:43|71.12|2.36154|
|MELISSE|p12 r4 w4|<span style="color: green">00:00:06.45</span>|00:00:43|55.75|2.386592|
|MELISSE|p16 r4 w4|00:00:11.31|00:01:02|34.56|2.36504|
|MELISSE|p12 r4 w4|<span style="color: green">00:00:08.58</span>|00:00:57|56.25|2.360844|
|MELISSE|p12 r8 w8|00:00:18.38|00:00:58|26.33|2.354396|
|MELISSE|r12 w12|<span style="color: green">00:00:07.51</span>|00:00:57|63.5|2.359704|
|MELISSE|p4 r4 w4|00:00:12.47|00:00:40|80.95|2.346448|
|MELISSE|p8 r8 w8|00:00:34.75|00:00:51|18.63|1.869064|
|MELISSE|p12 r12 w12|<span style="color: green">00:00:07.51|00:00:57|63.5|2.359704|
|MELISSE|p16 r16 w16|<span style="color: green">00:00:08.02</span>|00:01:03|49.19|2.360132|
|MELISSE|p8 r2 w2|00:00:36.49|00:00:53|18.13|1.872452|
|MELISSE|p8 r4 w4|<span style="color: green">00:00:07.59</span>|00:00:43|71.0|2.36154|
|MELISSE|p8 r6 w6|<span style="color: green">00:00:08.55</span>|00:00:50|74.25|2.34662|
|MELISSE|p8 r8 w8|00:00:34.75|00:00:51|18.63|1.869064|  

###  6.2. <a name='JARVIS'></a>JARVIS

| type run | param utilisé | temps écoulé (h : m : s) | temps cpu (h : m : s) |  utilisation cpu (%) | mémoire utilisé (Gb) | 
| --- | --- | --- | --- | --- | --- |
| JARVIS|p4 r4 w4|<span style="color: red">22:23:48</span>|87:53:53|98.0|38.771068|
|JARVIS|p8 r4 w4|<span style="color: red">12:02:06</span>|93:13:41|96.82|42.052904|
|JARVIS|p12 r4 w4|<span style="color: yellow">08:40:15</span>|98:36:51|94.91|45.83656|
|JARVIS|p16 r4 w4|<span style="color: yellow">08:49:20</span>|133:45:55|95.3|54.406524|
|JARVIS|p12 r4 w4|<span style="color: yellow">08:40:15</span>|98:36:51|94.9|45.83656|
|JARVIS|p12 r8 w8|<span style="color: green">07:42:28</span>|98:48:14|95.8|49.550256|
|JARVIS|p12 r12 w12|<span style="color: yellow">08:36:00</span>|98:38:48|95.75|50.125228|
|JARVIS|p4 r4 w4|<span style="color: red">27:04:19</span>|101:06:59|94.35|33.040992|
|JARVIS|p8 r8 w8|<span style="color: red">12:32:08</span>|93:09:49|93.32|41.013616|
|JARVIS|p12 r12 w12|<span style="color: yellow">08:35:00</span>|98:38:48|95.75|50.125228|
|JARVIS|p16 r16 w16|<span style="color: green">07:04:56</span>|96:17:12|84.91|55.835852|
|JARVIS|p8 r2 w2|<span style="color: red">12:47:34</span>|98:54:59|96.69|38.152596|
|JARVIS|p8 r4 w4|<span style="color: red">12:02:06</span>|93:13:41|96.82|42.052904|
|JARVIS|p8 r6 w6|<span style="color: red">12:37:44</span>|96:35:09|97.01|41.412972|
|JARVIS|p8 r8 w8|<span style="color: red">12:32:04</span>|93:09:49|93.32|41.013616|

---
---

##  7. <a name='Rsultatsdebcl-convert'></a>Résultats de bcl-convert

