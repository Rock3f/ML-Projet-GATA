from imutils import paths
import face_recognition
import pickle
import cv2
import os


def main():
	#Variables de définition du path vers le dataset, nom du fichier d'encodage, et de la méthode de détection
	path_dataset = "dataset"
	path_encoding = "encodings.pickle"
	detection_method = "cnn"

	# Récupération du path vers notre dataset d'images
	print("Quantifier les images du dataset ...")
	image_paths = list(paths.list_images(path_dataset))

	# initialisation des variables de stockages
	known_encodings = []
	known_names = []

	# Boucle sur l'ensemble des images dsu dataset
	for (i, image_path) in enumerate(image_paths):
		# Extraction du nom de la personne
		print("Processus d'extraction de l'image {}/{}".format(i + 1, len(image_paths)))
		name = image_path.split(os.path.sep)[-2]

		# Chargment des images et conversion en RGB (OpenCV ordering)
		image = cv2.imread(image_path)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# Détection de chaque visage par coordonnées(x, y)
		# correspondant à chaque visage sur une image
		boxes = face_recognition.face_locations(rgb, model=detection_method)

		# Récupération de la version encodée de l'ensemble des visages
		encodings = face_recognition.face_encodings(rgb, boxes)

		# Boucle au travers l'ensemble de l'encodage
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			known_encodings.append(encoding)
			known_names.append(name)

	# Création d'un dump encodings + names
	print("[Serialisation des différents encodings...")
	data = {"encodings": known_encodings, "names": known_names}
	f = open(path_encoding, "wb")
	f.write(pickle.dumps(data))
	f.close()

if __name__ == "__main__":
	main()