### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Camera.py
### Date        : 04/04/2022
### Description : Classe qui récupère le flux vidéo de la caméra et qui la retourne.

# import the necessary packages
import cv2

class VideoCamera(object):
    __color = (0, 0, 0)
    __increment = 0
    wait1frame=True

    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 480
    COLORGREEN=(0,255,0)
    COLORRED=(0,0,255)
    MAX8BIT=255
    MIN_ANGLE_VUE= 327
    MAX_ANGLE_VUE= 31
    MAX_DISTANCE=2000
    GRID_END = 130
    GRID_BEGIN = 116
    GRID_WIDTH = 10
    zone={}
    translator={}
    _memozone={}
    reseter=0

    
    
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
        self.QRCodeActivated=False

        # Initialisation du dictionnaire de zones
        value = 0
        for i in range(327,360):
            self.translator[str(i)]=value
            value+=1
        for i in range(0,32):
            self.translator[str(i)]=value
            value+=1
    
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
        cv2.line(self.rotated, (0, self.GRID_END), (self.IMAGE_WIDTH, 130), self.COLORGREEN, 1)
        cv2.line(self.rotated, (0, self.GRID_BEGIN), (self.IMAGE_WIDTH, 116), self.COLORGREEN, 1)
        # cv2.line(rotated, (int(self.IMAGE_WIDTH/2),0), (int(self.IMAGE_WIDTH/2), self.IMAGE_HEIGHT), (255, 0, 0), 1)
        
        for i in range(0,self.IMAGE_WIDTH,self.GRID_WIDTH):
            cv2.line(self.rotated, (i, int(self.IMAGE_HEIGHT-350)), (i, self.IMAGE_HEIGHT-364), self.COLORGREEN, 1)


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
                # calcul of the color by the distance
                self.__increment= int((self.MAX8BIT*self.zone[key])/self.MAX_DISTANCE)
                self.start_point = ((key*self.GRID_WIDTH), self.GRID_BEGIN)
                self.end_point = (((key*self.GRID_WIDTH)+self.GRID_WIDTH), self.GRID_END)
                self.__color = (0, 0+ self.__increment, self.MAX8BIT - self.__increment)
                
                self.rotated = cv2.rectangle(self.rotated, self.start_point, self.end_point, self.__color, self.thickness)
        else:
            for key in self.zone:
                self.__increment= int((self.MAX8BIT*self.zone[key])/self.MAX_DISTANCE)
                self.start_point = ((key*self.GRID_WIDTH), self.GRID_BEGIN)
                self.end_point = (((key*self.GRID_WIDTH)+self.GRID_WIDTH), self.GRID_END)
                self.__color = (0, 0+ self.__increment, self.MAX8BIT - self.__increment)
                self.rotated = cv2.rectangle(self.rotated, self.start_point, self.end_point, self.__color, self.thickness)

        if self.reseter==100:
            self.zone={}
            self.scans=[]
            self.reseter=0

        self.reseter+=1
               
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
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if len(img)>0:
            if self.QRCodeActivated:
                decoder=cv2.QRCodeDetector()
                data,points,_=decoder.detectAndDecode(img)
                if data=="target":
                    if points is not None:
                        points=points[0]
    
                        for i in range(len(points)):
                            pt1=[int(val)for val in points[i]]
                            pt2=[int(val)for val in points[(i+1)%len(points)]]
                            cv2.line(self.rotated,tuple(pt1),tuple(pt2),(self.MAX8BIT,0,0),1)
        return self.rotated
