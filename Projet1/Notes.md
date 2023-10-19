'''
Son numéro de téléphone : 02 40 37 15 78
Son nom d’utilisateur GitHub: M0ustach3

Il faudra voir avec Didier Lime pour le rendu de mi projet.

Pour vendredi prochain :
Une présentation rapide (~15mn) sur les différentes technologies existantes en réseau 

'''

# Projet 1

Points à aborder :
- TCP: Pour communiquer les informations entre les ordinateurs. Des poignées de mains et confirmations sont effectuées entre les extrémités d'envoie et de la reception pour garantir l'intégrité et la séquence.
- DNS: Une alternative du nom de domaine.
- UDP: Une convention de communiquer l'info rapide sans garantir l'intégrité et la séquence.
- HTTP: Une convention de hypertexte pour communiquer les pages, les videos...
- NAT: partager IP commun.
- les pare-feux: Contrôler le réseau pour se defendre de la violence malveillante.


Le modèle OSI : 
7 couches formant des briques s’ajoutant les unes sur les autres (voir photo).

La plupart du temps les ports ne dépassent pas 1000 donc critère intéressant.
Problème potentiel de données chiffrées.
Le NAT n’est utilisé qu’en IPv4 et centrale n’en utilise pas.
La signature d’un paquet s’appelle l’IOC (à creuser).
Certaines plages d’IP sont réservées en publique et ne sont donc utilisées qu’en local.
Éduroam utilise FreeRadius (à creuser aussi).
Il existe des bases de données d’ensemble de paquets malveillants et non malveillants, à nous de les trouver.
Il existe aussi des bases de malware et d’URL problématiques, potentiellement par le même site/entreprise que la base précédente.
Un problème à régler sera la taille des donnés extraites et comment la réduire.

+ apprendre à utiliser WireShark
