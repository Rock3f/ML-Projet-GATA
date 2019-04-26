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
# Directory get all the current folder then split on the last 7 characters 
DIRECTORY=$(cd `dirname $0` && pwd)
# Absolute path to image folder
FOLDER="${DIRECTORY::${#DIRECTORY}-7}"
echo $FOLDER

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
find "${FOLDER}" -iname '*.jpg' -exec convert \{} -verbose -resize $WIDTHx$HEIGHT\> \{} \;

# Alternative
#mogrify -path ${FOLDER} -resize ${WIDTH}x${HEIGHT}% *.png -verbose