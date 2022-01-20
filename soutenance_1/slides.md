% Présentation Alternance
% William Amory \newline M1 BI-IPFB Université de Paris
% 24/01/2022

# CEA - Genoscope  
## CEA - Genoscope
### CEA (Commissariat à l'énergie atomique et aux énergies)
- ???? Salarié  
- ??? de labo  
- créé en ????  

### Genoscope (centre national de séquençage)
- ???? salarié  
- Créé en ????  
    - Séquençage du chromosome 14 humain pour le projet ????  
    - Plus grand centre de séquençge français et européen 

## Organigrame CEA - Genoscope - LBGB

# Contexte
## LBGB ( Laboratoire de Bioinformatique pour la Génomique et la Biodiversité)
### Arrivé de séquenceurs MGI  
- 2 DNBSEQ-G400  
- 1 DNBSEQ-T7  

## Workflow NGS 
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{img/Workflow.png}
    \caption{Workflow de génération, de controle qualité et d'analyse biologique des FASTQ}
    \label{fig-worklow}
\end{figure}
##  La technologie MGI
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\textwidth]{img/MGI_vs_Illumina.png}
    \caption{Différences entre Illumina et MGI de technologie NGL}
    \label{fig-Illu-vs-MGI}
\end{figure}
##  La technologie MGI
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{img/Techno_MGI.png}
    \caption{Schéma techno MGI}
    \label{fig-techno-MGI}
\end{figure}

# Objectifs
## Développement d'un pipeline automatique pour MGI
### Détermination des outils bioinformatique  
### Quels méthodes et outils pour le pipline


## Test de 2 software de génération de FASTQ
## Apprentissage du Perl
### Pouquoi ?  
- Raison historique du laboratoire  
- Toutes les librairies et modules utilisés sont en Perl  
- Worflow d'Illumina écrit en Perl  

### Réalisation  
- Programme effectuant des analyses statistiques élémentaires  
    - compter le taux de GC  
    - moyene de la qualité de chaque read   
    - ect ...  
- Lecture des modules utilisé dans le workflow d'illumina  

# Perspective