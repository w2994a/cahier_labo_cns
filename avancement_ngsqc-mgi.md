# Avancement NGS-QC MGI

Les conf sont dans : /env/ig/atelier/cns/mgi/DEV_MGI/TEST_DISPATCH/conf/  
- mgi.conf : conf de la fdr
- isoprod_mgi.conf : conf des variables d'environement

chaque traitement est divisé en deux partie (Treatments, DBConnectors)

Pour tester les chacun des traitements individuellement il faut utiliser les subroutines de la librairie : src/perl/lib/Qc/Mgi/Pipeline/NgsQcMgi.pm ou le prog de test : /env/ig/atelier/cns/mgi/DEV_MGI/TEST_DISPATCH/TestNgsQcMgi.pl

il prend argument :
- le nom du traitement à tester  
- l'objet contenant les info du readset (/env/ig/atelier/cns/mgi/DEV_MGI/TEST_DISPATCH/ReadsetMgi-<codeReadset>.data)  

Tous les traiments fonctionnaient, sauf le traitement FileManagement de la lib src/perl/lib/Qc/MgI/Treatments/FileManagement.pm que j'était en train de débeuguer.  


