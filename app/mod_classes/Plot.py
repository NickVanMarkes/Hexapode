### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Plot.py
### Date        : 07/04/2022
### Description : Classe qui créer des plots (vue radar) selon les données captées par le lidar

#MatPlotLib

import matplotlib.pyplot as plt

# Autres librairies
import numpy as np
import cv2


#Constantes
DMAX = 2000
IMIN = 0
IMAX = 50
class Radar(object):
    def __init__(self):
        """  brief       : Constructeur de la classe Radar, créer la base de l'image.
             param-type  : None
             return-type : None
        """ 

       #INIT matplotlib
        plt.ion()
        self.fig = plt.figure(figsize=(3,3))
        plt.axes([0,0,1,1])
        ax = plt.subplot(111, projection='polar')
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        self.line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                               cmap=plt.cm.jet, lw=0)
        ax.set_rmax(DMAX)
        ax.grid(True)

    def CreatePlot(self,scans):
        """  brief       : Grâce aux obstacles détéctés avec le lidar, et mets les points sur le plot.
             param-type  : scans (list)
             return-type : Bytes
        """ 

        for scan in scans:
            
            #Insertion des points
            offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
            self.line.set_offsets(offsets)
            intens = np.array([int(100*meas[2]/2000) for meas in scan])
            self.line.set_array(intens)

        self.fig.savefig("static/img/plot.jpg")
        radar = cv2.imread("static/img/plot.jpg")
        radar = cv2.imencode('.jpg', radar)[1]
        return radar.tobytes()
        