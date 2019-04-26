from imutils import paths
import face_recognition
import pickle
import cv2
import os
import numpy as np

def get_RGB(source):
    return cv2.cvtColor(source, cv2.COLOR_BGR2RGB)

def reconnaissance_image(encodings, image, detection_method): 
	#Chargement du fichier .pickle (dataset)
	print("Chargement du dataset Dump")
	data = pickle.loads(open(encodings, "rb").read())

	# load the input image and convert it from BGR to RGB
	image = cv2.imread(image)
	rgb = get_RGB(image)	

	# Detection des coordonnées (x,y) de chaque visage sur l'image 
	print("Reconnaissances des visages")
	boxes = face_recognition.face_locations(rgb, model=detection_method)
	#Encodage des visages
	encodings = face_recognition.face_encodings(rgb, boxes)

	# Initialisation du tableau de variable
	names = []

	# Boucle sur l'ensemble des visages détectés 
	for encoding in encodings:
		# Comparaison des visages
		matches = face_recognition.compare_faces(encodings,encoding)
		name = "Non reconnu"

		# Si le visage correspond
		if True in matches:
			# Récupération des index de tous les visages qui correspondent
			# et Création d'un dictionnaire permettant de compter le nombre totale de visages reconnus 
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# Boucle sur l'ensemble des index correspondant et mise à jour d'un compteur par nom
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# Récupération du nom dont le compteur est la plus grande valeur
			#Il s'agit ici d'avoir le nom dont la probabilité est la plus grande
			name = max(counts, key=counts.get)
		
		# Mise à jour de la liste de noms
		names.append(name)

	# Boucle sur l'ensemble des visage reconnu
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# Dessine un rectangle et le nom sur le visage reconnu
		cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)

	print("Affichage de l'image")
	print ("<-- Veuillez changer de fenêtre -->")
	# show the output image
	cv2.imshow("Image", image)

	print("Après avoir vu votre belle image, appuyer sur n'importe quelle touche")
	cv2.waitKey(0)

def load_model(path_dataset, path_encoding, detection_method ) :

	# Récupération du path vers notre dataset d'images
	print("Recupération des informations concernant les images du dataset ...")
	image_paths = list(paths.list_images(path_dataset))
	print(image_paths)

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
		rgb = get_RGB(image)

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

#Redimensionne les images d'un dossier
def resize_img(path) :

	#Pour chaque image du dossier et des sous-dossier
	for root, dirs, files in os.walk(path):
		for file in files:
			#Charge l'image
			img = cv2.imread("%s\\%s" %(root, file), cv2.IMREAD_UNCHANGED)
			#Définition d'une taille standard
			max_width = 400
			#Calcul le pourcentage entre la dimension standard et la dimension actuelle de l'image
			scale_percent = int(img.shape[1]) / max_width
			#Si l'image est plus large que la dimension standard
			if int(img.shape[1] > 400) :
				#Définie la largeur au format standard
				width = int(img.shape[1] * scale_percent / 100)
				#Définie la hauteur en conservant les proportions
				height = int(img.shape[0] * scale_percent / 100)
				dim = (width, height)
				#Redimensionne l'image 
				resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
				#Enregistre l'image modifiée au même endroit pour éviter les doublons
				cv2.imwrite("%s\\%s" %(root, file) ,resized);



def main():
	print("------------------------------------------------")
	print()
	print("Initialisation de l'interface")
	print("Récupération des variables")
	#Variables de définition du path vers le dataset, nom du fichier d'encodage, et de la méthode de détection
	path_dataset = "dataset"
	path_encoding = "encodings.pickle"
	detection_method = "cnn"
	menuItems = np.array(["Charger le modèle de données", "Reconnaissance de l'image", "Redimensionner les images", "Quitter"])
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
			path_image = input("Saisissez l'URI de l'image de test : ")
			reconnaissance_image(path_encoding, path_image, detection_method)
		elif choice == 3:
			path_folder = input("Saisissez l'URI du dossier contenant les images : ")
			resize_img(path_folder)
		elif choice == 4:
			print("Fermeture de l'application...")
			break

if __name__ == "__main__":
	main()