### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Camera.py
### Date        : 04/04/2022
### Description : Classe qui récupère le flux vidéo de la caméra et qui la retourne.

# import the necessary packages
import cv2
import numpy as np

class VideoCamera(object):
    __color = (0, 0, 0)
    __increment = 0
    __up_down = 0
    wait1frame=True

    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 480
    MIN_ANGLE_VUE= 340
    MAX_ANGLE_VUE= 38
    MAX_DISTANCE=2000
    GRID_END = 130
    GRID_BEGIN = 116
    GRID_WIDTH = 11
    zone={}
    translator={
            "340":0,
            "341":1,
            "342":2,
            "343":3,
            "344":4,
            "345":5,
            "346":6,
            "347":7,
            "348":8,
            "349":9,
            "350":10,
            "351":11,
            "352":12,
            "353":13,
            "354":14,
            "355":15,
            "356":16,
            "357":17,
            "358":18,
            "359":19,
            "0":20,
            "1":21,
            "2":22,
            "3":23,
            "4":24,
            "5":25,
            "6":26,
            "7":27,
            "8":28,
            "9":29,
            "10":30,
            "11":31,
            "12":32,
            "13":33,
            "14":34,
            "15":35,
            "16":36,
            "17":37,
            "18":38,
            "19":39,
            "20":40,
            "21":41,
            "22":42,
            "23":43,
            "24":44,
            "25":45,
            "26":46,
            "27":47,
            "28":48,
            "29":49,
            "30":50,
            "31":51,
            "32":52,
            "33":53,
            "34":54,
            "35":55,
            "36":56,
            "37":57,
            "38":58
        }
    _memozone={}

    
    
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
    
    def get_frame(self,scans):
        """  brief       : capture du flux vidéo de la caméra et retourne le flux vidéo
             param-type  : None
             return-type : bytes 
        """ 
       # extracting frames
        ret, frame = self.video.read()
        rotated=cv2.rotate(frame,cv2.ROTATE_180)

        # #Draw grid on the frame
        cv2.line(rotated, (0, self.GRID_END), (self.IMAGE_WIDTH, 130), (0, 255, 0), 1)
        cv2.line(rotated, (0, self.GRID_BEGIN), (self.IMAGE_WIDTH, 116), (0, 255, 0), 1)
        
        for i in range(0,self.IMAGE_WIDTH,self.GRID_WIDTH):
            cv2.line(rotated, (i, int(self.IMAGE_HEIGHT-350)), (i, self.IMAGE_HEIGHT-364), (0, 255, 0), 1)


        self.scans = scans

        #print(self.scans)
        

        # Start coordinate, here (5, 5)
        # represents the top left corner of rectangle
        self.start_point = (0, 116)
        
        # Ending coordinate, here (220, 220)
        # represents the bottom right corner of rectangle
        self.end_point = (11, 123)
        
        # Line thickness of 1 px
        self.thickness = 1
        if self.scans!=[]:
            for scan in self.scans:
                for meas in scan:
                    if meas[1]>=self.MIN_ANGLE_VUE or meas[1]<=self.MAX_ANGLE_VUE and  meas[2]<self.MAX_DISTANCE:
                        self.zone[self.translator[str(int(meas[1]))]]=meas[2]
            for key in self.zone:
                self.__increment= int((255*self.zone[key])/self.MAX_DISTANCE)
                self.start_point = ((key*self.GRID_WIDTH), self.GRID_BEGIN)
                self.end_point = (((key*self.GRID_WIDTH)+self.GRID_WIDTH), self.GRID_END)
                self.__color = (0, 0+ self.__increment, 255 - self.__increment)
                rotated = cv2.rectangle(rotated, self.start_point, self.end_point, self.__color, self.thickness)
        else:
            for key in self.zone:
                self.__increment= int((255*self.zone[key])/self.MAX_DISTANCE)
                self.start_point = ((key*self.GRID_WIDTH), self.GRID_BEGIN)
                self.end_point = (((key*self.GRID_WIDTH)+self.GRID_WIDTH), self.GRID_END)
                self.__color = (0, 0+ self.__increment, 255 - self.__increment)
                rotated = cv2.rectangle(rotated, self.start_point, self.end_point, self.__color, self.thickness)


               
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', rotated)
        return jpeg.tobytes()