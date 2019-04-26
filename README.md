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

### Installation des paquets

TODO

### Pamètrage des images

  Nous mettons à disposition un script shell/batch pour resize vos images afin de permettre aux ordinateurs moins puissants de pouvoir exécuter rapidement le programme de reconnaissance.
  Veuillez noter que nous nous sommes basés sur un tutoriel sur internet, vous trouverez les références dans les commentaires du script.

  :exclamation: Important :exclamation:

Vous devez impérativement modifier votre variable FOLDER présente dans le script :

![alt text](https://raw.github.com/Rock3f/ML-Projet-GATA/master/.assets/BatchResize_InitConfig.png)

Vous devez également modifier le chemin dans votre code Python à votre script shell/batch si vous voulez l'utiliser
