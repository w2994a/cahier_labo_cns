% Présentation Alternance
% William Amory \newline M1 BI-IPFB Université de Paris
% 24/01/2022

# CEA - Genoscope  
## CEA - Genoscope
### CEA (Commissariat à l'énergie atomique et aux énergies)  
- créé le 18 octobre 1945 par Charles de Gaulle   
- 20 000 Salariés  
- 4 directions opérationnelles et 9 directions fonctionnelles  


### Genoscope (Centre National de Séquençage)
- 250 salariés  
- Créé en 1996  
    - Participation **projet Génome humain** (Séquençage du chromosome 14 humain)  
    - Développer programmes de génomiques en France  
    - Plus grand centre de séquençage français et européen 

## Organigrame CEA - Genoscope - LBGB
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{img/organigramme.jpg}
    \caption{\tiny{Organigramme situant l'équipe du \emph{Laboratoire de Bioinformatique pour la Génomique et la Biodiversité (LBGB)} au sein du genoscope et du CEA}}
    \label{fig-organigramme}
\end{figure}

# Contexte
## LBGB (Laboratoire de Bioinformatique pour la Génomique et la Biodiversité)
### missions  
- Veille technologique  
- Contrôle qualité  
- Assemblage  
- Annotation  
- Visualisation  

### Plusieurs équiques  
- Production  
- Annotation  
- Assemblage
- Evaluation des technologies de séquençage  

## LBGB (Production)
### Missions
- Veille technologique  
- Evaluation de nouveaux outils  
- developper, tester et maintenir les codes  
- Répondre au besoin des équipes de recherche et de production
- Mise en place de pipeline automatisés  
    - génération des FATSQ  
    - Contrôle qualité  
    - Analyses biologiques

## LBGB - Workflow NGS 
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{img/Workflow.png}
    \caption{\tiny{Workflow de génération, de controle qualité et d'analyse biologique des FASTQ}}
    \label{fig-worklow}
\end{figure}

## LBGB - MGI
\begin{block}{Arrivé de séquenceurs MGI}
    \begin{itemize}
        \item 2 DNBSEQ-G400  
        \item 1 DNBSEQ-T7  
    \end{itemize}
\end{block}

\begin{center}
    \includegraphics[width=0.4\textwidth]{img/MGI_G400.jpg}
    \includegraphics[width=0.4\textwidth]{img/MGI_T7.jpg}
\end{center}
<cite>https://en.mgi-tech.com/products/</cite>

##  La technologie MGI
\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\textwidth]{img/MGI_vs_Illumina.png}
    \caption{\tiny{Différences entre Illumina et MGI de technologie NGL}}
    \label{fig-Illu-vs-MGI}
\end{figure}

##  La technologie MGI
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{img/Techno_MGI.png}
    \caption{\tiny{Schéma techno MGI}}
    \label{fig-techno-MGI}
\end{figure}



# Objectifs
## Développement d'un pipeline automatique pour MGI
### Objectifs du pipline  
- Générer les fichiers FASTQ à partir des *Bases Calls*  
- Mise à jour de la base de données NGL  
- Analyses des FASTQ générés  
- Rennomage et déplacement des fichiers en fonction des projets  
- Mise à jour de l'état d'un run  

## Développement d'un pipeline automatique pour MGI
### Comment ?    
- Déterminer les outils et methodes nécessaires  
    - utilisation de nouveaux outils ?  
    - utisation d'outils et méthodes existant pour Illumina ?  
    - création de nouvelles méthodes pour MGI ?  
- Ecriture du pipeline  
    - déterminer de l'ordre d'utilisation des outils et méthodes  
    - choix du langage de programation (Perl)  


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

## Test de 2 software de génération de FASTQ (bcl2fastq et bcl-convert)
## bcl2fastq vs bcl-convert (Temps total)
\begin{minipage}{0.45\textwidth}
    \begin{figure}[H]
        \centering
        \includegraphics[width=1\textwidth]{img/barplot_cum_bcl-convert1.png}
        \caption{\tiny{Temps total de génération \newline des FASTQ pour bcl2fastq}}
        \label{fig-total-time-illu}
    \end{figure}
\end{minipage} 
\hfill
\begin{minipage}{0.5\textwidth}
    \begin{figure}[H]
        \centering
        \includegraphics[width=0.95\textwidth]{img/barplot_cum_bcl2fastq1.png}
        \caption{\tiny{Temps total de génération \newline des FASTQ pour bcl-convert}}
        \label{fig-total-time-mgi}
    \end{figure}
\end{minipage} 

## bcl2fastq vs bcl-convert (Temps cpu)
\begin{minipage}{0.45\textwidth}
    \begin{figure}[H]
        \centering
        \includegraphics[width=1\textwidth]{img/barplot_cum_bcl-convert2.png}
        \caption{\tiny{Temps cpu de génération des \newline FASTQ pour bcl2fastq}}
        \label{fig-total-time-illu}
    \end{figure}
\end{minipage} 
\hfill
\begin{minipage}{0.5\textwidth}
    \begin{figure}[H]
        \centering
        \includegraphics[width=0.95\textwidth]{img/barplot_cum_bcl2fastq2.png}
        \caption{\tiny{Temps cpu de génération des \newline FASTQ pour bcl-convert}}
        \label{fig-total-time-mgi}
    \end{figure}
\end{minipage} 

## bcl2fastq vs bcl-convert (Pourcentage d'utilisation cpu)
\begin{minipage}{0.45\textwidth}
    \begin{figure}[H]
        \centering
        \includegraphics[width=1\textwidth]{img/barplot_cum_bcl-convert3.png}
        \caption{\tiny{Pourcentage d'ulisation cpu pour \newline la génération des FASTQ pour bcl2fastq}}
        \label{fig-total-time-illu}
    \end{figure}
\end{minipage} 
\hfill
\begin{minipage}{0.5\textwidth}
    \begin{figure}[H]
        \centering
        \includegraphics[width=0.95\textwidth]{img/barplot_cum_bcl2fastq3.png}
        \caption{\tiny{Pourcentage d'ulisation cpu pour \newline la génération des FASTQ pour bcl-convert}}
        \label{fig-total-time-mgi}
    \end{figure}
\end{minipage} 

# Perspective
## Perspective
### Détermination de la Migration de bcl2fastq vers bcl-convert    
- Mise à jour du pipeline de génération des FASTQ  
- Prise en charge des sorties de bcl-convert pour les autres pipelines  

### Worflow MGI  
- Automatisation total du workflow