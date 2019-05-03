Cette librairie est disponible [ici](https://github.com/ageitgey/face_recognition_models) et est utilisé par la librairie face_recognition.

Ce model va permettre de définir les points correspondant aux traits du visage. Par la suite nous pourrons comparer les points identifiés par le model afin de définir s'il s'agit de la même personne ou non. 


## Les fonctions appelés dans le code face_recognition_models :

 ### pose_predictor_model_location() : </br>

  Retourne resource_filename(__name__, "models/shape_predictor_68_face_landmarks.dat"). Ce fichier n'est pas consultable car il s'agit d'un fichier DAT créé par un programme dont nous n'avons pas connaissance.

 ### pose_predictor_five_point_model_location() : </br>

  Retourne resource_filename(__name__, "models/shape_predictor_5_face_landmarks.dat"). Non consultable.

 ### face_recognition_model_location() : </br>

  Retourne resource_filename(__name__, "models/dlib_face_recognition_resnet_model_v1.dat"). Non consultable.

 ### cnn_face_detector_model_location() : </br>

  retourne resource_filename(__name__, "models/mmod_human_face_detector.dat"). Non consultatble.