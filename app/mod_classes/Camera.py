### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Camera.py
### Date        : 04/04/2022
### Description : Classe qui récupère le flux vidéo de la caméra et qui la retourne.

# import the necessary packages
import cv2

class VideoCamera(object):
    
    #Constructeur
    #Brief: Trouve la caméra et Capture le flux vidéo
    def __init__(self):
       # capturing video
       self.video = cv2.VideoCapture(cv2.CAP_V4L2)
    
    #destructeur
    #Brief: Se déconnecte de la caméra
    def __del__(self):
        # releasing camera
        self.video.release()
    
    #Brief: Fonction qui permet de récupérer le flux vidéo
    #Retourne: Chaîne de bytes
    def get_frame(self):
       # extracting frames
        ret, frame = self.video.read()
        #frame=cv2.resize(frame,(1280,720))                    
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()