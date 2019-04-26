from imutils import paths
from imutils.video import VideoStream
import imutils
import face_recognition
import pickle
import cv2
import os
import numpy as np
import subprocess
import time

def get_RGB(source):
    return cv2.cvtColor(source, cv2.COLOR_BGR2RGB)

def reconnaissance_image(encodings, image, detection_method): 
	#Chargement du fichier .pickle (dataset)
	print("Chargement du dataset Dump")
	data = pickle.loads(open(encodings, "rb").read())

	# load the input image and convert it from BGR to RGB
	image = cv2.imread(image)
	rgb = get_RGB(image)	

	# Detection des coordonnees (x,y) de chaque visage sur l'image 
	print("Reconnaissances des visages")
	boxes = face_recognition.face_locations(rgb, model=detection_method)
	#Encodage des visages
	encodings = face_recognition.face_encodings(rgb, boxes)

	# Initialisation du tableau de variable
	names = []

	# Boucle sur l'ensemble des visages detectes 
	for encoding in encodings:
		# Comparaison des visages
		matches = face_recognition.compare_faces(data["encodings"],encoding)
		name = "Non reconnu"

		# Si le visage correspond
		if True in matches:
			# Recuperation des index de tous les visages qui correspondent
			# et Creation d'un dictionnaire permettant de compter le nombre totale de visages reconnus 
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# Boucle sur l'ensemble des index correspondant et mise a jour d'un compteur par nom
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# Recuperation du nom dont le compteur est la plus grande valeur
			#Il s'agit ici d'avoir le nom dont la probabilite est la plus grande
			name = max(counts, key=counts.get)
		
		# Mise a jour de la liste de noms
		names.append(name)

	font_scale = 0.7
	font = cv2.FONT_HERSHEY_SIMPLEX

	# Boucle sur l'ensemble des visage reconnu
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# Dessine un rectangle et le nom sur le visage reconnu
		cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

		#Mise en place de la coordonée Y du label du nom
		y = top - 15 if top - 15 > 15 else top + 15
		#Récupération de la taille en hauteur et longeur du texte
		(text_width, text_height) = cv2.getTextSize(name, font, fontScale=font_scale, thickness=1)[0]
		#Mise à jour des coordonées suivant la taille du texte
		box_coords = ((left, y), (left + text_width - 2, y - text_height - 2))
		#Affichage du texte et du fond de couleur
		cv2.rectangle(image, box_coords[0], box_coords[1], (0,0,0), cv2.FILLED)
		cv2.putText(image, name, (left, y), font, fontScale=font_scale, color=(255,255,255), thickness=1)

	print("Affichage de l'image")
	print ("<-- Veuillez changer de fenetre -->")
	# Affichage de l'image
	cv2.imshow("Image", image)

	print("Apres avoir vu votre belle image, appuyer sur n'importe quelle touche (dans l'image)")
	cv2.waitKey(0)

def reconnaissance_cam(encodings, detection_method) : 
	#Chargement du dataset
	print("Chargement du dataset...")
	data = pickle.loads(open(encodings, "rb").read())

	# Activation  du flux video via la webcam
	print("Démarrage de la webcam...")
	vs = VideoStream(src=0).start()
	#Warmup pour activation de la camera
	time.sleep(2.0)

	# Boucle sur les différentes frames du flux video
	while True:
		#Obtention de la frame en cours de la video
		frame = vs.read()
		
		# Conversion de la couleur et resizing de l'image
		#Plus l'image est petite, plus les fps sont élevés
		rgb = get_RGB(frame)
		rgb = imutils.resize(frame, width=300)
		r = frame.shape[1] / float(rgb.shape[1])

		# Detection des coordonnees (x,y) de chaque visage sur l'image
		boxes = face_recognition.face_locations(rgb,model=detection_method)
		encodings = face_recognition.face_encodings(rgb, boxes)
		
		names = []

		# Boucle sur l'ensemble des visages detectes 
		for encoding in encodings:
			# Comparaison des visages
			matches = face_recognition.compare_faces(data["encodings"], encoding)
			name = "Non Reconnu"

			# Si le visage correspond
			if True in matches:
				# Recuperation des index de tous les visages qui correspondent
				# et Creation d'un dictionnaire permettant de compter le nombre totale de visages reconnus 
				matched_idxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}

				# Boucle sur l'ensemble des index correspondant et mise a jour d'un compteur par nom
				for i in matched_idxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				# Recuperation du nom dont le compteur est la plus grande valeur
				#Il s'agit ici d'avoir le nom dont la probabilite est la plus grande
				name = max(counts, key=counts.get)
			
			# Mise a jour de la liste de noms
			names.append(name)

		font_scale = 0.7
		font = cv2.FONT_HERSHEY_SIMPLEX

		# Boucle sur l'ensemble des visage reconnu
		for ((top, right, bottom, left), name) in zip(boxes, names):
			# Modifications des coordonnées détectés
			top = int(top * r)
			right = int(right * r)
			bottom = int(bottom * r)
			left = int(left * r)

			# Affichage des carrés autour des visages + noms
			cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			#Récupération de la taille en hauteur et longeur du texte
			(text_width, text_height) = cv2.getTextSize(name, font, fontScale=font_scale, thickness=1)[0]
			#Mise à jour des coordonées suivant la taille du texte
			box_coords = ((left, y), (left + text_width - 2, y - text_height - 2))
			#Affichage du texte et du fond de couleur
			cv2.rectangle(frame, box_coords[0], box_coords[1], (0,0,0), cv2.FILLED)
			cv2.putText(frame, name, (left, y), font, fontScale=font_scale, color=(255,255,255), thickness=1)

		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# Lorsque la touche 'q' est ajouté alors quitte le processus
		if key == ord("q"):
			break

	# Suppression des fenêtres OpenCV (images, photos, videos..)
	cv2.destroyAllWindows()
	vs.stop()

def load_model(path_dataset, path_encoding, detection_method ) :

	# Recuperation du path vers notre dataset d'images
	print("Recuperation des informations concernant les images du dataset ...")
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

		# Detection de chaque visage par coordonnees(x, y)
		# correspondant a chaque visage sur une image
		boxes = face_recognition.face_locations(rgb, model=detection_method)

		# Recuperation de la version encodee de l'ensemble des visages
		encodings = face_recognition.face_encodings(rgb, boxes)

		# Boucle au travers l'ensemble des encodages
		for encoding in encodings:
			# Ajout d'un tuple encoding + name a note modele
			known_encodings.append(encoding)
			known_names.append(name)

	# Creation d'un dump encodings + names
	print("[Serialisation des differents encodings...")
	data = {"encodings": known_encodings, "names": known_names}
	f = open(path_encoding, "wb")
	f.write(pickle.dumps(data))
	f.close()

	print("Chargement du modele termine")

#Affichage du menu
def display_menu(options):
	# affichage des options suivant le tableau d'options passe en parametre
	for i in range(len(options)):
		print("{:d}. {:s}".format(i+1, options[i]))
	
	choice = 0
	#Attente de la reponse utilisateur
	#Si l'element envoye par l'utilisateur n'est pas dans le tableau alors l'utilisateur est prompte de nouveau
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
	print("Recuperation des variables")
	#Variables de definition du path vers le dataset, nom du fichier d'encodage, et de la methode de detection
	path_dataset = "dataset"
	path_encoding = "encodings.pickle"
	detection_method = "cnn"
	menuItems = np.array(["Charger le modele de donnees", "Reconnaissance de l'image", "Reconnaissance via Camera", "Changer le format des images", "Quitter"])
	print()
	print("------------------------------------------------")
	print()

	#Affichage du menu jusqu'a ce que l'option quitter soit saisie
	#Necessite de trouver une autre solution qu'une boucle infinie ! 
	while True : 
		choice = display_menu(menuItems)

		if choice == 1:
			load_model(path_dataset,path_encoding,detection_method)
		elif choice == 2:
			path_image = input("Saisissez l'URI de l'image de test : ")
			reconnaissance_image(path_encoding, path_image, detection_method)

			# Suppression des fenêtres OpenCV (images, photos, videos..)
			cv2.destroyAllWindows()
		
		elif choice == 3:
			reconnaissance_cam(path_encoding, detection_method)
		elif choice == 4:	
			path_folder = input("Saisissez l'URI du dossier contenant les images : ")
			resize_img(path_folder)
			
			#Version de resize avec Bash
			#Si vous souhaitez utiliser la fonctionnalité de resizing via le bash, il est nécessaire de commenter
			#la ligne dont la méthode est resize_img
			#Décommenter la ligne si vous souhaitez réaliser le formatage des images via le bash
			#subprocess.call(['./scripts/shell-image-resize.sh'])
		elif choice == 5:
			print("Fermeture de l'application...")
			break

if __name__ == "__main__":
	main()