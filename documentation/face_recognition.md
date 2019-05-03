La librairie face_recognition que nous utilisons est disponible [ici](https://github.com/ageitgey/face_recognition).

Cette librairie permet d'identifier des visages présents sur une image. Elles est basé sur plusieurs librairies notemment numpy que nous avons exploré en cours.

Fonctionnement de la libraire

La librairie analyse l'image et retourne l'emplacement des traits du visage c'est à dire :
- La position des yeux
- La position de la bouche
- La position du nez
- Le contour du visage

Chaque trait est contitué de plusieurs point permettant de connaître la forme et l'aspect de ces traits.

Les fonctions appelés dans notre code : </br>

  ## face_recognition.face_locations(img, number_of_times_to_upsample, model) : </br>
 
   Retourne un tableau avec les coordonnées des différents rectangles des visages humain reconnus
   - param img: L'image analysée (as a numpy array)
   - param number_of_times_to_upsample: Nombre de fois où l'image sera bouclé afin de reconnaitre les images. Plus le nombre est grand, moins le nombre de visage trouvé" est faible
   - param model: Quel modèle utilisé. Deux types de modèle hog (moins précis mais plus rapide) et cnn (model en deeplearning). par défaut "HOG"
  -------------------------------------------------------------------------- 
  Méthodes utilisées : _rect_to_css(face.rect), _trim_css_to_bounds(_rect_to_css(face.rect), img.shape), _raw_face_locations(img,number_of_times_to_upsample, model)
    
   
  ## face_recognition.face_encodings(face_image, known_face_locations, num_jitters): </br>
  A partir d'une image, retourne les 128 dimensions encodées de chaque visage 
  - param face_image: Image contenant les visages à reconnaitre
  - param known_face_locations: Optionel - Coordonnées des visages si elles sont connus.
  - param num_jitters: Nombre de fois ou on boucle lors du calcul de l'encodage. Plus la valeur est élevé, plus l'algo est précise et lente (i.e. 100 is 100x slower)
  - return: une liste de 128 dimension contenant l'encodage des visages (une dimension pour chaque visage)  
  -------------------------------------------------------------------------- </br>
  Méthodes utilisées : _raw_face_landmarks(face_image, known_face_locations, model="small"), face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)
  
  ## face_recognition.compare_faces(): </br>
  Comparaison de la liste des visages situés dans le modèle avec l'image passée en paramètre
  - param known_face_encodings: liste des visages encodées
  - param face_encoding_to_check: Visage encodé à reconnaître
  - param tolerance: Différence entre chaque visages pour que l'on considère que c'est une réussite. Plus la valeur est petite, plus la comparaison est stricte. Les meilleurs perfomances sont constatées avec une valeur en 0.6.
  - return: une liste de booléen qui indique quels visages ont été rencontrés
  -------------------------------------------------------------------------- </br>
  Méthodes utilisées :
  -------------------------------------------------------------------------- </br>
  -------------------------------------------------------------------------- </br>
