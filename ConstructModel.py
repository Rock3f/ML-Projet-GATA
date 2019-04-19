# USAGE
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os


def main():
	#Variables de définition 
	path_dataset = ""
	path_encoding = ""
	detection_method = "cnn"

if __name__ == "__main__":
	main()

# construct the argument parser and parse the arguments


# grab the paths to the input images in our dataset
print("Quantifier les images du dataset ...")
image_paths = list(paths.list_images(path_dataset))

# initialize the list of known encodings and known names
known_encodings = []
known_names = []

# loop over the image paths
for (i, image_path) in enumerate(image_paths):
	# extract the person name from the image path
	print("Processus d'extraction de l'image {}/{}".format(i + 1, len(image_paths)))
	name = image_path.split(os.path.sep)[-2]

	# load the input image and convert it from RGB (OpenCV ordering)
	# to dlib ordering (RGB)
	image = cv2.imread(image_path)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# detect the (x, y)-coordinates of the bounding boxes
	# corresponding to each face in the input image
	boxes = face_recognition.face_locations(rgb, model=detection_method)

	# compute the facial embedding for the face
	encodings = face_recognition.face_encodings(rgb, boxes)

	# loop over the encodings
	for encoding in encodings:
		# add each encoding + name to our set of known names and
		# encodings
		known_encodings.append(encoding)
		known_names.append(name)

# dump the facial encodings + names to disk
print("[INFO] serializing encodings...")
data = {"encodings": known_encodings, "names": known_names}
f = open(path_encoding, "wb")
f.write(pickle.dumps(data))
f.close()