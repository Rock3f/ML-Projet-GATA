## (Not Finished) Installation pour Windows - .bat

Vous avez besoin d'installer au préalable l'executable d'ImageMagick pour l'execution du script Batch.
:exclamation: Pensez à noter le chemin d'installation du magick.exe :exclamation:

Une fois cela effectué, vous devez aller modifier dans le projet GATA le fichier batch-image-resize.bat que vous retrouverez dans le dossier script présent à la racine du projet.

Il vous faudra modifier le chemin vers le .exe de magick.exe 

Le script se base sur un déjà existant nommé scale.bat, vous pouvez retrouver le repository Github original dans les commentaires du fichier !

## Installation pour Linux & Mac - .sh

Vous avez besoin d'executer les commandes suivantes dans votre terminal :

### Linux
    sudo apt update
    sudo apt install imagemagick -y
### Mac
    brew update
    brew intall imagemagick

## Notes

Nous avons mis par défaut le chemin vers le projet.
Cela permet d'englober les répertoires de dataset et de test. Cependant, si cela ne vous convient pas, vous pouvez toujours adapter le chemin selon votre convenance !