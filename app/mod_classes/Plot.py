### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Plot.py
### Date        : 07/04/2022
### Description : Classe qui créer des plots (vue radar) selon les données captées par le lidar

#MatPlotLib

import matplotlib.pyplot as plt
import matplotlib

# Autres librairies
import numpy as np
import cv2


#Constantes

class Radar(object):
    DMAX = 2000
    IMIN = 0
    IMAX = 50
    COLORS=[(1, 0.2, 0.3), (1, 0.8, 0), (0.1, 0.5, 0.1)]  # near -> mid -> far
    CMAP_NAME="distance_warning"
    def __init__(self):
        """  brief: Constructeur de la classe Radar, créer la base de l'image.
             
             parameters  :
                 None
             
             returns :
                None
        """ 

       #INIT matplotlib
        plt.ion()
        self.fig = plt.figure(figsize=(3,3))
        plt.axes([0,0,1,1])
        ax = plt.subplot(111, projection='polar')
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        cmap = matplotlib.colors.LinearSegmentedColormap.from_list(self.CMAP_NAME, self.COLORS)
        self.line = ax.scatter([0, 0], [0, 0], s=5, c=[self.IMIN, self.IMAX],
                               cmap=cmap, lw=0)
        ax.set_rmax(self.DMAX)
        ax.grid(True)

    def CreatePlot(self,scans):
        """  brief: Grâce aux obstacles détéctés avec le lidar, et mets les points sur le plot.
             
             parameters  :
                 list
             
             returns :
                bytes
        """ 

        for scan in scans:
            #Insertion des points
            offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
            self.line.set_offsets(offsets)
            intens = np.array([int(100*meas[2]/self.DMAX) for meas in scan])
            self.line.set_array(intens)

        self.fig.savefig("static/img/plot.png", transparent=True)
        radar=cv2.imread("static/img/plot.png", cv2.IMREAD_UNCHANGED)
        radar = cv2.imencode('.png', radar)[1]
        radar_encode= np.array(radar)
        return radar_encode.tobytes()