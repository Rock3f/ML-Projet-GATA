La librairie face_recognition que nous utilisons est disponible [ici](https://github.com/ageitgey/face_recognition).

Cette librairie permet d'identifier des visages présents sur une image. Elles est basé sur plusieurs librairies notemment numpy que nous avons exploré en cours.

Fonctionnement de la libraire

La librairie analyse l'image et retourne l'emplacement des traits du visage c'est à dire :
- La position des yeux
- La position de la bouche
- La position du nez
- Le contour du visage

Chaque trait est contitué de plusieurs point permettant de connaître la forme et l'aspect de ces traits.

Les fonctions appelés dans notre code :
   -------------------------------------------------------------------------- </br>
   -------------------------------------------------------------------------- </br>
  face_recognition.face_locations(img, number_of_times_to_upsample, model) : 
   -------------------------------------------------------------------------- </br>
    Retourne un tableau avec les coordonnées des différents rectangles des visages humain reconnus</br>
      :param img: L'image analysée (as a numpy array)</br>
      :param number_of_times_to_upsample: Nombre de fois où l'image sera bouclé afin de reconnaitre les images. 
                                        Plus le nombre est grand, moins le nombre de visage trouvé" est faible</br>
      :param model: Quel modèle utilisé. Deux types de modèle hog (moins précis mais plus rapide) et cnn (model en    
                    deeplearning). par défaut "HOG": </br>
      :return: Retourne la location des visage via des tuples(top, right, bottom, left) </br>
     -------------------------------------------------------------------------- </br>
     Méthodes utilisées : _rect_to_css(face.rect), _trim_css_to_bounds(_rect_to_css(face.rect), img.shape), 
                          _raw_face_locations(img,number_of_times_to_upsample, model)
    
   -------------------------------------------------------------------------- </br>
   -------------------------------------------------------------------------- </br>    
   </br>
  face_recognition.face_encodings()
  face_recognition.compare_faces()
