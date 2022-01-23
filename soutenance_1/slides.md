% Gestion informatique des données de séquençage
% William Amory \newline M1 BI-IPFB Université de Paris \newline \newline sous la responsabilité de Frédérick Gavory \newline \newline \includegraphics[height=1cm]{img/genoscope_logo.png} \newline \newline \includegraphics[height=1.5cm]{img/cea.jpg}
% 24/01/2022

## Gestion informatique des données de séquençage
\tableofcontents

# CEA - Genoscope  
## CEA - Genoscope
### CEA (Commissariat à l'énergie atomique et aux énergies)  
- créé le 18 octobre 1945 par Charles de Gaulle   
- 20 000 Salariés  
- 4 directions opérationnelles et 9 directions fonctionnelles  


### Genoscope (Centre National de Séquençage)  
- Créé en 1996 - 250 salariés   
    - Participation **projet Génome humain** (Séquençage du chromosome 14 humain)  
    - Développer programmes de génomiques en France  
    - Plus grand centre de séquençage français  
    - **France génomique**
    - **Projet Tara Océans** - étude des écosystèmes marins planctoniques

## Organigrame CEA - Genoscope - LBGB
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\textwidth]{img/organigramme.jpg}
    \caption{\tiny{Organigramme situant l'équipe du \emph{Laboratoire de Bioinformatique pour la Génomique} \newline \emph{et la Biodiversité (LBGB)} au sein du genoscope et du CEA}}
    \label{fig-organigramme}
\end{figure}

# Contexte
## LBGB (Laboratoire de Bioinformatique pour la Génomique et la Biodiversité)
### missions  
- Veille technologique  
- Contrôle qualité des fichiers de séquences   
- Assemblage des séquences et des génomes  
- Annotation des séquences et des génomes  
- Visualisation  

### Plusieurs groupes de travail  
- **Production**  
- Annotation  
- Assemblage
- Evaluation des technologies de séquençage  

## LBGB (Production)
### Missions
- Veille technologique  
- Evaluation de nouveaux outils  
- developper, tester et maintenir les codes  
- Répondre aux besoins des équipes de recherches et de productions
- Mise en place de pipelines automatisés  
    - génération des fichiers de séquences  
    - Contrôle qualité des fichiers de séquences  
    - Analyses biologiques

## LBGB - Workflow NGS 
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{img/Workflow.png}
    \caption{\tiny{Workflow de génération, de controle qualité et d'analyse biologique des FASTQ}}
    \label{fig-worklow}
\end{figure}
<cite>https://www.genoscope.cns.fr/rdbioseq/</cite>

## LBGB - MGI
\begin{block}{Arrivée des séquenceurs MGI}
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
    \caption{\tiny{Différences entre Illumina et MGI de technologie NGL \newline J. Patterson \& all. (2019). Impact of sequencing depth and technology on de novo RNA-Seq assembly. \newline BMC Genomics. 20. 10.1186/s12864-019-5965-x.}}
    \label{fig-Illu-vs-MGI}
\end{figure}

##  La technologie MGI
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{img/Techno_MGI.png}
    \caption{\tiny{Schéma techno MGI}}
    \label{fig-techno-MGI}
\end{figure}
<cite>https://en.mgi-tech.com/products/</cite>


# Objectifs
## Développement d'un pipeline automatique pour MGI
### Objectifs du pipeline  
- développement NGS-RG et NGS-QC pour MGI  
- Distribution des FASTQ par projets
- Trie des FASTQ par echantillons, technologies et runs  
- Mise à jour de la base de données de références (NGL)  
    - création des entrées runs et readset  
    - stockage des métriques et analyses correspondantes  
- Nettoyage des FASTQ générés
- Analyses des FASTQ générés     

## Développement d'un pipeline automatique pour MGI
### Comment ?    
- Déterminer les outils et methodes nécessaires    
    - utisation d'outils et méthodes existants pour Illumina ?  
    - utilisation de nouveaux outils et méthodes ?  
- Ecriture du pipeline  
    - déterminer l'ordre d'utilisation des outils et méthodes   

## Autres objectifs de la missions
### Evaluation d'outils  
- pour les pipelines :
  - Illumina  
  - MGI  
  - Oxford Nanopore  
- Mise en place des outils pertinents
- Remplacement ou arrêt des outils non pertinents  

### codage d'outils 
- maintenir les pipelines  
- distributions des résultats d'analyses par projet, échantillon/run  
- Mettre à jour la base de données (NGL)

## Apprentissage du Perl
### Pourquoi ?  
- Raison historique du laboratoire  
- Toutes les librairies et modules utilisés sont en Perl  
- Worflow d'Illumina écrit en Perl  

### Réalisation  
- Programme effectuant des analyses statistiques élémentaires  
    - taux de GC  
    - moyene de la qualité de chaque read   
    - ect ...  
- Utilisation des modules utilisés dans le workflow d'illumina  

## Test de 2 software de génération de FASTQ (bcl2fastq et bcl-convert)
permettent la génération des FASTQ et de réaliser le démultiplexage  

\begin{block}{Comparaison des performances}
    \begin{itemize}
        \item Recherche des meilleurs paramètres pour bcl2fastq
        \begin{itemize}
        \item Nombre de threads lecture/décompression \emph{Bases Calls} (\textbf{r})
        \item Nombre de threads Génération FASTQ (\textbf{p})
        \item Nombre de threads écriture/compression FASTQ (\textbf{w})
        \end{itemize}
        \item Comparaison des performances entres les 2 soft
        \item Choix de changement de soft
    \end{itemize}
\end{block}
## bcl2fastq vs bcl-convert (Temps total)  
\begin{figure}[H]
    \centering
    \includegraphics[width=1\textwidth]{img/barplot_total_time_comp.png}
    \caption{Temps total de génération des FASTQ pour bcl2fastq \newline et bcl-convert}
    \label{fig-total-time}
\end{figure}  

## bcl2fastq vs bcl-convert (Temps cpu)  
\begin{figure}[H]
    \centering
    \includegraphics[width=1\textwidth]{img/barplot_cpu_time_comp.png}
    \caption{Temps cpu de génération des FASTQ pour bcl2fastq \newline et bcl-convert}
    \label{fig-cpu-time}
\end{figure}  

## bcl2fastq vs bcl-convert (Pourcentage d'utilisation cpu)  
\begin{figure}[H]
    \centering
    \includegraphics[width=1\textwidth]{img/barplot_pourcnetage_cpu_comp.png}
    \caption{Pourcentage d'ulisation cpu pour la génération des \newline FASTQ pour bcl2fastq et bcl-convert}
    \label{fig-pourcentage-cpu}
\end{figure}  

# Perspective
## Perspective
### Détermination de la Migration de bcl2fastq vers bcl-convert    
- Mise à jour du pipeline de génération des FASTQ  
- Prise en charge des sorties de bcl-convert pour les autres pipelines  
- Discussion avec les équipes LIS et LS

### Worflow MGI  
- Automatisation total du workflow

## Perspective
### Evaluation d'autres outils  
- outils d'assignation taxonomique  
- outils de *filtering*, *trimming*  
- intégration d'outils des autres groupes de travails dans les pipelines
  - outils de *mapping*, assemblage, *scafold* ...


## Bibliographie
\begin{itemize}
\footnotesize{
	\item[•] Impact of sequencing depth and technology on de novo RNA-Seq assembly, Patterson. 2022-01-23, BMC Genomics. \href{https://doi.org/10.1186/s12864-019-5965-x}{10.1186/s12864-019-5965-x}
	\item[•] bcl2fastq2 Conversion Software v2.20 Software Guide (\href{https://emea.support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/bcl2fastq/bcl2fastq2-v2-20-software-guide-15051736-03.pdf}{15051736}). 2019, Illumina, Inc.
    \item[•] BCL Convert Software Guide v3.7.5 (\href{https://emea.support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/bcl_convert/bcl-convert-v3-7-5-software-guide-1000000163594-00.pdf}{1000000163594}). 2021, Illumina, Inc.
    \item[•] perl - The Perl 5 language interpreter - Perldoc Browser. 2022-01-23, \href{https://perldoc.perl.org/perl}{https://perldoc.perl.org/perl}
    \item[•] The Comprehensive Perl Archive Network. 2022-01-23, \href{https://www.cpan.org/}{www.cpan.org}}
\end{itemize}

##
\begin{center}
\begin{figure}[H]
    \includegraphics[width=0.5\textwidth]{img/genoscope_logo.png}
\end{figure}

\huge\textbf{Merci de votre attention}
\newline
  
\begin{figure}[H]
\includegraphics[width=0.2\textwidth]{img/cea.jpg}
\end{figure} 
\end{center}