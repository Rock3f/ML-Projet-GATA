#!/usr/bin/env bash
# Purpose: batch image resizer
# Source: https://guides.wp-bullet.com
# Author: Mike

# --------------------------------
# ---------- Img Resize ----------
# --------------------------------

# --------------------------------
# ----- Extensions supported -----
# ------------ .jpg --------------
# ------ Not Yet supported -------
# ----- .png, .jpeg, other ? -----

# Original link tutorial : https://guides.wp-bullet.com/batch-resize-images-using-linux-command-line-and-imagemagick/

# GATA Project specific resize !

# Absolute path to image folder
FOLDER="/media/alexandre/8628ADC128ADB11B/Cours/Machine_Learning/ML-Projet-GATA/dataset"


# Max height
WIDTH=300

# Max width
HEIGHT=400

# Par défaut, on va utiliser des images en .jpg
# Resize png or jpg to either height or width, keeps proportions using imagemagick
#find ${FOLDER} -iname '*.jpg' -o -iname '*.png' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;

# Resize png to either height or width, keeps proportions using imagemagick
#find ${FOLDER} -iname '*.png' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;

# Resize jpg only to either height or width, keeps proportions using imagemagick
find ${FOLDER} -iname '*.jpg' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;

# Alternative
#mogrify -path ${FOLDER} -resize ${WIDTH}x${HEIGHT}% *.png -verbose
