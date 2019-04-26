REM --------------------------------
REM ---------- Img Resize ----------
REM --------------------------------

REM --------------------------------
REM ----- Extensions supported -----
REM ------------ .jpg --------------
REM ------ Not Yet supported -------
REM ----- .png, .jpeg, other ? -----

REM GATA Project specific resize !

REM Absolute path to image folder
FOLDER="/media/alexandre/8628ADC128ADB11B/Cours/Machine_Learning/ML-Projet-GATA/dataset"

REM Max height
WIDTH=300

REM Max width
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