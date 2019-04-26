from imutils import paths
import face_recognition
import pickle
import cv2
import os
import numpy as np

def getRGB(source):
    return cv2.cvtColor(source, cv2.COLOR_BGR2RGB)

def load_model(path_dataset, path_encoding, detection_method ) :

	# Récupération du path vers notre dataset d'images
	print("Recupération des informations concernant les images du dataset ...")
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
		rgb = getRGB(image)

		# Détection de chaque visage par coordonnées(x, y)
		# correspondant à chaque visage sur une image
		boxes = face_recognition.face_locations(rgb, model=detection_method)

		# Récupération de la version encodée de l'ensemble des visages
		encodings = face_recognition.face_encodings(rgb, boxes)

		# Boucle au travers l'ensemble des encodages
		for encoding in encodings:
			# Ajout d'un tuple encoding + name à note modèle
			known_encodings.append(encoding)
			known_names.append(name)

	# Création d'un dump encodings + names
	print("[Serialisation des différents encodings...")
	data = {"encodings": known_encodings, "names": known_names}
	f = open(path_encoding, "wb")
	f.write(pickle.dumps(data))
	f.close()

	print("Chargement du modele termine")

#Affichage du menu
def display_menu(options):
	# affichage des options suivant le tableau d'options passé en paramètre
	for i in range(len(options)):
		print("{:d}. {:s}".format(i+1, options[i]))
	
	choice = 0
	#Attente de la réponse utilisateur
	#Si l'élément envoyé par l'utilisateur n'est pas dans le tableau alors l'utilisateur est prompté de nouveau
	while not(np.any(choice == np.arange(len(options))+1)):
		choice = input_number("Choississez une option du menu : ")
	
	return choice

#Conversion du message en float
def input_number(message) :
	while True : 
		try:
			num = float(input(message))
			break
		except ValueError :
			pass
	return num

def main():
	print("------------------------------------------------")
	print()
	print("Initialisation de l'interface")
	print("Récupération des variables")
	#Variables de définition du path vers le dataset, nom du fichier d'encodage, et de la méthode de détection
	path_dataset = "dataset"
	path_encoding = "encodings.pickle"
	detection_method = "cnn"
	menuItems = np.array(["Charger le modèle de données", "Quitter"])
	print()
	print("------------------------------------------------")
	print()

	#Affichage du menu jusqu'à ce que l'option quitter soit saisie
	#Nécessite de trouver une autre solution qu'une boucle infinie ! 
	while True : 
		choice = display_menu(menuItems)

		if choice == 1:
			load_model(path_dataset,path_encoding,detection_method)
		elif choice == 2:
			print("Fermeture de l'application...")
			break

if __name__ == "__main__":
	main()