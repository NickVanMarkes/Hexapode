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
    wait1frame=True

    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 480
    MIN_ANGLE_VUE= 327
    MAX_ANGLE_VUE= 31
    MAX_DISTANCE=2000
    GRID_END = 130
    GRID_BEGIN = 116
    GRID_WIDTH = 10
    zone={}
    translator={
            "327":0,
            "328":1,
            "329":2,
            "330":3,
            "331":4,
            "332":5,
            "333":6,
            "334":7,
            "335":8,
            "336":9,
            "337":10,
            "338":11,
            "339":12,
            "340":13,
            "341":14,
            "342":15,
            "343":16,
            "344":17,
            "345":18,
            "346":19,
            "347":20,
            "348":21,
            "349":22,
            "350":23,
            "351":24,
            "352":25,
            "353":26,
            "354":27,
            "355":28,
            "356":29,
            "357":30,
            "358":31,
            "359":32,
            "0":33,
            "1":34,
            "2":35,
            "3":36,
            "4":37,
            "5":38,
            "6":39,
            "7":40,
            "8":41,
            "9":42,
            "10":43,
            "11":44,
            "12":45,
            "13":46,
            "14":47,
            "15":48,
            "16":49,
            "17":50,
            "18":51,
            "19":52,
            "20":53,
            "21":54,
            "22":55,
            "23":56,
            "24":57,
            "25":58,
            "26":59,
            "27":60,
            "28":61,
            "29":62,
            "30":63,
            "31":64,
        }
    _memozone={}

    
    
    def __init__(self):
        """  brief: Initialisation de la caméra et du flux vidéo.
             
             parameters  :
                 None
             
             returns :
                None
        """  
       # capturing video
        self.video = cv2.VideoCapture(cv2.CAP_V4L2)
        self.frame=None
        self.rotated=None

    
    def __del__(self):
        """  brief: Arrêt de la saisie de la caméra.
             
             parameters  :
                 None
             
             returns :
                None
        """ 
        # releasing camera
        self.video.release()
    
    def get_frame(self,scans):
        """  brief: Capture du flux vidéo de la caméra et retourne le flux vidéo.
             
             parameters  :
                 list[int]
             
             returns :
                bytes
        """ 
       # extracting frames
        ret, self.frame = self.video.read()
        self.rotated=cv2.rotate(self.frame,cv2.ROTATE_180)

        # #Draw grid on the frame
        cv2.line(self.rotated, (0, self.GRID_END), (self.IMAGE_WIDTH, 130), (0, 255, 0), 1)
        cv2.line(self.rotated, (0, self.GRID_BEGIN), (self.IMAGE_WIDTH, 116), (0, 255, 0), 1)
        # cv2.line(rotated, (int(self.IMAGE_WIDTH/2),0), (int(self.IMAGE_WIDTH/2), self.IMAGE_HEIGHT), (255, 0, 0), 1)
        
        for i in range(0,self.IMAGE_WIDTH,self.GRID_WIDTH):
            cv2.line(self.rotated, (i, int(self.IMAGE_HEIGHT-350)), (i, self.IMAGE_HEIGHT-364), (0, 255, 0), 1)


        self.scans = scans        

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
                    if meas[1]>=self.MIN_ANGLE_VUE or meas[1]<=self.MAX_ANGLE_VUE:
                        self.zone[self.translator[str(int(meas[1]))]]=meas[2]
            
            for key in self.zone:
                self.__increment= int((255*self.zone[key])/self.MAX_DISTANCE)
                self.start_point = ((key*self.GRID_WIDTH), self.GRID_BEGIN)
                self.end_point = (((key*self.GRID_WIDTH)+self.GRID_WIDTH), self.GRID_END)
                self.__color = (0, 0+ self.__increment, 255 - self.__increment)
                self.rotated = cv2.rectangle(self.rotated, self.start_point, self.end_point, self.__color, self.thickness)
        else:
            for key in self.zone:
                self.__increment= int((255*self.zone[key])/self.MAX_DISTANCE)
                self.start_point = ((key*self.GRID_WIDTH), self.GRID_BEGIN)
                self.end_point = (((key*self.GRID_WIDTH)+self.GRID_WIDTH), self.GRID_END)
                self.__color = (0, 0+ self.__increment, 255 - self.__increment)
                self.rotated = cv2.rectangle(self.rotated, self.start_point, self.end_point, self.__color, self.thickness)

               
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', self.QRCodeDetect())
        return jpeg.tobytes()

    def QRCodeDetect(self):
        """  brief: Detecte les QR Code dans une image.
             
             parameters  :
                 None
             
             returns :
                Image
        """
        img=self.rotated
        decoder=cv2.QRCodeDetector()
        data,points,_=decoder.detectAndDecode(img)
        if points is not None:
            print('Decoded data:', data)
            points=points[0]

            for i in range(len(points)):
                pt1=[int(val)for val in points[i]]
                pt2=[int(val)for val in points[(i+1)%len(points)]]
                cv2.line(img,tuple(pt1),tuple(pt2),(255,0,0),1)
        return img
