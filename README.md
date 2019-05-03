# ML-Projet-GATA
Guillaume Fourny, Antoine Gosset, Tanguy Badier, Alexandre Desvallées

## Objectif :

Créer une application permettant d'identifier les personnes de la classe à partir d'une photo

## Jalons :

- Collecter un jeu de données ( commencer par nous 4 ) 18/04

- Isoler les visages sur les photos en carré 19/04

- Apprentissage par supervision 25/04

- Prediction sur un jeu de test 26/04

- Ajouter les autres membres de la classe au jeu de donnée 26/04

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

### Par défaut avec Python - OpenCV

Nous mettons à disposition une option dans le menu du programme pour faire un resize de vos images (pour gagner en temps de performance) en position 4 

### Via Script Shell/Batch - ImageMagick

:warning: Cette option est désactivée par défaut, vous avez besoin de décommenter la ligne :warning:

Nous mettons à disposition un script shell/batch pour resize vos images afin de permettre aux ordinateurs moins puissants de pouvoir exécuter rapidement le programme de reconnaissance.

:exclamation: Important :exclamation:

Vous pouvez modifier votre variable FOLDER présente dans le script, par défaut, nous l'avons paramétré sur le projet pour prendre en compte les dossier dataset ET test

Vous devez également modifier dans votre code Python le chemin à votre script shell/batch si vous voulez l'utiliser.

Pour plus d'informations, vous pouvez vous référer au "ConfigScript.md"

## Contenu du programme de reconnaissance faciale

Pour utiliser face_recognition vous avez besoin de charger votre modèle de données pour que l'algorithme puisse interprêter les images et vous fournir un résultat. Ci-après, un petit tutorial de notre petit programme

### Navigation

Pour naviguer dans l'application, vous devez rentrer dans votre terminal quelle fonctionnalité vous voulez utiliser puis appuyer sur Entrée.

Pour sortir d'une fonctionnalité, vous avez besoin d'appuyer sur une touche.

![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/MenuProgramme.png)

### Première étape : le resize de vos images

Pour gagner en temps de traitement pour la seconde étape, vous aurez besoin de formater vos images à un format plus petit pour limiter les consommations en CPU de vos machines et donc limiter le temps de traitement.

Pour ce faire, **avant de lancer votre programme**, vous aurez besoin au préalable de mettre dans un répertoire les photo où vous retrouvez une seule personne. 

![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/dataset1.png)
![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/dataset2.png)

Une fois cela fait, vous pouvez déposer une image de test dans le répertoire de test.

![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/test1.png)

Vous pourrez alors par la suite lancer le programme et saisir le 4 dans votre console pour lancer le resize automatique de vos images.

**Attention au format qui doit être pour le moment .jpg pour que le programme le prenne en compte**

Dans le cas contraire, vous aurez un message dans la console pour vous prévenir que votre image n'a pas été prise en compte à cause d'un mauvais format.

### Seconde étape : le chargement du modèle

Pour que face_recognition puisse apprendre puis exploiter les données, vous devez charger le modèle de données. Vous avez besoin de charger une première fois le modèle de données.
Lancez alors la commande 3 dans votre terminal.

![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/imgModele1.png)
![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/imgModele2.png)

### Comment utiliser la reconnaissance par image

Lancez la commande 1 dans votre terminal.

![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/recoImg1.png)
![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/recoImg2.png)

### Comment utiliser la reconnaissance par webcam

Lancez la commande 2 dans votre terminal.

![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/recoWebcam1.png)
![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/recoWebcam2.png)
