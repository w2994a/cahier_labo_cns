# <span style="font-family:Comic Sans MS">Cahier de laboratoire (genoscope)</span>

<!-- vscode-markdown-toc -->
* 1. [Semaine du 9/09/2021 au 22/10/2021](#Semainedu9092021au22102021)
* 2. [Semaine du 28/10/2021 au 23/12/2021](#Semainedu28102021au23122021)
* 3. [Semaine du 20/01/2022 au 04/02/2022](#Semainedu20012022au04022022)
* 4. [Semaine du 07/02/2022 au ??/??/2022](#Semainedu07022022au2022)

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
    * -h : donne l'usage du programme
    * -p : indique le second fichier FASTQ si paired
    * -l : donne la longueur de chaque reads
    * -n : donne le nombre de chacunes des bases de chaque reads (A, T, C, G, N si inconnu)
    * -t : donne le taux de CG dans chaque reads
    * -q : donne le minimum, le maximum et la moyenne de la qualité de chaque reads

    <mark><span style="color:red"> rq : ajouter code corriger sur github</span><mark>
1. Apprentisage de l'utilisation des modules et du lancement de jobs sur les clusters de calculs.


---
##  2. <a name='Semainedu28102021au23122021'></a>Semaine du 28/10/2021 au 23/12/2021

1. Test du soft bcl2fastq  
Test du temps de calcul de bcl2fstq et de la taille mémoire utiliser en fonction des paramètre -r (coeurs alloués en lecture), -p (coeurs alloués pour le processus), -w (coeurs alloués en écriture). (cf fichier )
1. lecture de la doc de bcl-convert  
Lecture de la doc cd bcl-convert, ayant pour objectif de déterminer les différences d'utilisation entre bcl2fasq et bcl-convert.  
1. test de bcl-convert, pour tenter de reproduire les mêmes résultats que bcl2fastq.  

    * cf. rapport du benchmark entre bcl2fastq et bcl-convert.

    * Les sorties de bcl-convert sont différentes dde bcl2fastq et il est impossible de reproduire la même arborescence obtenu avec bcl2fastq. Il faut donc soit adapter les workflow qui utilisaient ces sorties ou bien créer un worflow qui ce chargera de créer la même arborescence de bcl2fastq. Néaimoins si la seconde méthodes est priviligier il y aura quand des adaptation à faire car le format des fichier de sortie (notament ceux des stats) sont différents.

##  3. <a name='Semainedu20012022au04022022'></a>Semaine du 20/01/2022 au 04/02/2022

1. Préparation du diapo et de la soutenance pour le 24/01/2022 (20 et 21/01/2022)
1. Rédaction du rapport de 5 pages pour le 03/02/2022.

##  4. <a name='Semainedu07022022au2022'></a>Semaine du 07/02/2022 au 25/02/2022

1. Test de bcl-convert avec d'autres paramètres + en utilisant l'option du nombre de tâches effecturer en parallèle
1. préparation de la présentation des tests et des changement à effectuer entre bcl2fastq et bcl-convert à l'équipe (présentation au groupe _production_ prévue pour la semaine du 21/02/2022)
1. Création du ticket JIRA pour le changement de bcl2fastq vers bcl-convert
1. Tableaux et graphiques de comparaison des nouveux tests effectuer de bcl-convert sur inti  
1. choix des paramètres de bcl-convert pour la mise en production  

## Semaine du 14/03/2022 au ??/??/2022

### Info utile pour le dev du pipeline

toutes les lib utile pour les dev sont dans :  

```shell
/env/ig/soft/rdbioseq/
```

Répartit en plusieurs packages :  

1. `dbtools` ==> contient toutes les fontions concernant la data base ngl.
1. ...  

### Structure des fichiers du pipeline

RG  
|———— Pipeline  
|&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;|  
|&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;|———— addRun.pl ==> script pour la création d'un run.  
|  
|———— Treatements  
|&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;|  
|&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;|———— RunCreation.pm ==> vide.  
|  
|  
|———— DBconnectors  
|&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;|  
|&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;&#x202F;|———— RunCreation.pm ==> package pour la création d'un run.  

### Écriture du pipeline NGS-RG pour les séquençeurs MGI
#### Début du pipeline MGI [étapes 1 et 2] (14/03/2022 - 25/03/2022)

1. Création du run dans NGL : ( ~/workdir/DEV_NGS_RG_MGI/RG/MGI/DBconnectors/RunCreation.pm )
    * Creation d'un run : ok
    * mise à jour du run dans l'état IW-RG : ok ( dbFactory::updateRunStateMGI(run_name, state_code) )

1. Création des lanes dans NGL : ~/workdir/DEV_NGS_RG_MGI/RG/MGI/DBconnectors/LaneCreation.pm )  
    * utiliser dbFactory::createLaneMGI(run_name, lane_number)

Création des 2 premières étapes du pipeline NGS-RG de MGI. Le Premier permet de créer dans NGL un run en fonction de son nom (ex : 220322_MUSHU_F00001324). Le second permet de créer les lanes de la flowcell à partir d'un fichier excel contenant les informations suivantes :  

|Lane|Projet|Sample|Barcode|  
|---|---|---|---|  
|# lane|ID Projet|ID_sample|Liste des barcodes de cette échatillon|  

Il peut y avoir plusieur fois le même numéros de lane, par contre l'ID de l'échantillon doit être unique dans le fichier excel. Pour pouvoir créer les lanes du run, on parse ce fichier excel pour récupérer le numéro de la lane, l'ID de l'échantillon (pas besoin de récupérer l'ID du projet, celui-ci est contenu dans l'ID de l'échantillon), et la liste des barcodes utilisés pour cette échantillon.  

Flowcell pour les tests du pipeline : **F300001324**
descripteurs des traitement ngsrg dans ngl : http://appuat.genoscope.cns.fr:9004/descriptions/treatments/home

#### Mise à jour des run avec le traitement "ngsrg" [étapes 3] (28/03/2022 - ??/??/2022)  

Concernant cette étapes il faut récupérer les information nécessaire à la mise à jour des run avec le traintement "ngsrg".  

1. Récupération des infos du run :  
    * position de la flowcell ==> _flowcellPosition_ = **Flowcell Pos** dans `BioInfo.csv` du rep L01  
    * Version ==> _recipeVersion_ = **Recipe Version** dans `SummaryTable.csv` du rep L01  
    * nombre de cycles ==> _nbCycle_ = **CycleNumber** dans `BioInfo.csv` du rep L01  
    * nombre de cycle pour le read 1 ==> nbCycleRead1* = **Read1 Cycles** dans `BioInfo.csv` du rep L01  
    * nombre de cycle pour le read 2 ==>  nbCycleRead2* = **Read2 Cycles** dans `BioInfo.csv` du rep L01  
    * nombre de cycle pour le read index 1 ==> nbCycleReadIndex1* = **Barcode** dans `BioInfo.csv` du rep L01  
    * nombre de cycle pour le read index 2 ==> nbCycleReadIndex2* = **Dual Barcode** dans `BioInfo.csv` du rep L01  
    * nombre de reads ==> _nbReads_ Somme de la colonne 3 des fichiers : `SequenceStat.txt` de toutes les pistes  
    * nombre de bases ==> _nbReads_ * _nbCycle_  
    * version du basecaller ==> _basecallerVersion_ = **ISW Version** dans le fichier `BioInfo.csv` du rep L01

1. Mettre ces infos dans NGL :



TO DO :

* Inclure les infos avec RunQualityControl.pm dans NGL  
* Inclure des mylog dans RunQualityContol.pm  
* Créer le .pm dans DBconnectors pour la partie NGL :  
    * Voir si utilisation d'une fonction similaire à `insertRunTreatment` de nglbi.pm




#### Mise à jour des lanes avec le traitement "ngsrg" [étapes 4] (30/03/2022)

Recupération des information concernant les lanes et mise à jour de ces dernières dans NGL.

1. Récupération des infos des lanes :
    * 
    code: "ngsrg",
    typeCode: "ngsrg-mgi",
    categoryCode: "ngsrg",
    default: {
        nbCycleRead1 => "Read1 Cycles" dans le fichier "BioInfo.csv" du rep L01
        nbCycleRead2 => "Read2 Cycles" dans le fichier "BioInfo.csv" du rep L01
        nbCycleReadIndex1 => "Barcode" dans le fichier "BioInfo.csv" du rep L01
        nbCycleReadIndex2 => "Dual Barcode" dans le fichier "BioInfo.csv" du rep L01
        nbReads => somme des nombres de la colonne 3 du fichier "SequenceStat.txt"
        nbBases => nbReads x (nbCycleRead1 + nbCycleRead2)
        percentDemulLoss => (nbReads - nombre de reads attribués à un barcode attendu) / nbReads) x100
        percentESR => "ESR(%)" dans le fichier "summaryTable.csv"
        percentQ30 => "Q30(%)" dans le fichier "summaryTable.csv"
        percentQ20
        percentQ10
        percentN
        recoverValue => "RecoverValue(AVG)" dans le fichier "summaryTable.csv"
        percentChipProductivity => "ChipProductivity(%)" dans le fichier "summaryTable.csv"
        percentRunon1 => "Runon1(%)" dans le fichier "summaryTable.csv"
        percentRunon2 => "Runon2(%)" dans le fichier "summaryTable.csv"
        percentLag1 => "Lag1(%)" dans le fichier "summaryTable.csv"
        percentLag2 => "Lag2(%)" dans le fichier "summaryTable.csv"
        percentErrors
