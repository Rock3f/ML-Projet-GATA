# ML-Projet-GATA
Guillaume Fourny, Antoine Gosset, Tanguy Badier, Alexandre Desvallées

## Objectif :

Créer une application permettant d'identifier les personnes de la classe à partir d'une photo

## Jalons :

### Collecter un jeu de données ( commencer par nous 4 ) 18/04

### Isoler les visages sur les photos en carré 19/04

### Apprentissage par supervision 25/04

### Prediction sur un jeu de test 26/04

### Ajouter les autres membres de la classe au jeu de donnée 26/04

### Optionnels 02/05
  Ajouter une interface graphique 
  Faire à partir d'image en temps réel (webcam) 
  
## Installation du projet

### Clonage du projet sur votre machine

  git clone https://github.com/Rock3f/ML-Projet-GATA.git

### Installation des paquets

Pour installer les paquets liés au projet, vous devez au préalable disposer d'un environnement python fonctionnel. 

Note pour Windows :

 - Avec Anaconda3, la librairie Dlib nous a posé des soucis lors de son installation. Or sans cette librairie vous ne pourrez pas lancer le programme.
 - Le fichier Batch n'est pas encore terminé, vous ne pourrez donc pas avoir l'option dans le menu et devrez utiliser le resize des images via Python - OpenCV (voir ci-après)

Une fois votre environnement python installé, veillez à avoir l'assistant pip d'installé. Vous pourrez utiliser les commandes ci-dessous pour récupérer le nécessaire :
  pip install CMake
  pip install face_recognition
  pip install pickle
  pip install opencv-python
  pip install imutils

## Paramètrage des images

:exclamation: Important :exclamation:

Vous pouvez modifier votre variable FOLDER présente dans le script, par défaut, nous l'avons paramétré sur le projet pour prendre en compte les dossier dataset ET test

### Par défaut avec Python - OpenCV

Nous mettons à disposition une option dans le menu du programme pour faire un resize de vos images (pour gagner en temps de performance) en position 4 

### Via Script Shell/Batch - ImageMagick

:warning: Cette option est désactivée par défaut, vous avez besoin de décommenter la ligne :warning:

Nous mettons à disposition un script shell/batch pour resize vos images afin de permettre aux ordinateurs moins puissants de pouvoir exécuter rapidement le programme de reconnaissance.

Vous devez également modifier le chemin dans votre code Python à votre script shell/batch si vous voulez l'utiliser.

Pour plus d'informations, vous pouvez vous référer au "ConfigScript.md"