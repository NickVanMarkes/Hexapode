### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Camera.py
### Date        : 04/04/2022
### Description : Classe qui récupère le flux vidéo de la caméra et qui la retourne.

# import the necessary packages
import cv2
import numpy as np

class VideoCamera(object):

    
    
    def __init__(self):
        """  brief       : Initialisation de la caméra et du flux vidéo
             param-type  : None
             return-type : None 
        """ 
       # capturing video
        self.video = cv2.VideoCapture(cv2.CAP_V4L2)

    
    def __del__(self):
        """  brief       : Arrêt de la saisie de la caméra
             param-type  : None
             return-type : None 
        """ 
        # releasing camera
        self.video.release()
    
    def get_frame(self):
        """  brief       : capture du flux vidéo de la caméra et retourne le flux vidéo
             param-type  : None
             return-type : bytes 
        """ 
       # extracting frames
        ret, frame = self.video.read()
        rotated=cv2.rotate(frame,cv2.ROTATE_180)

        #Draw grid on the frame
        cv2.line(rotated, (0, 130), (640, 130), (0, 255, 0), 1)
        cv2.line(rotated, (0, 123), (640, 123), (0, 255, 0), 1)
        cv2.line(rotated, (0, 116), (640, 116), (0, 255, 0), 1)
        
        for i in range(0,640,11):
            cv2.line(rotated, (i, 480-349), (i, 480-364), (0, 255, 0), 1)

        #frame=cv2.resize(frame,(1280,720))                    
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', rotated)
        return jpeg.tobytes()