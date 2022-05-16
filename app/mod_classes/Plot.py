### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Plot.py
### Date        : 07/04/2022
### Description : Classe qui créer des plots (vue radar) selon les données captées par le lidar
import time

#MatPlotLib

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


# Autres librairies
import numpy as np
import io
import cv2


#Constantes
DMAX = 2000
IMIN = 0
IMAX = 50
class Radar(object):

    #Constructeur
    #Brief: Initialise le plot avec la forme et les lignes. Instantie le lidar
    def __init__(self):
       #INIT matplotlib
        plt.ion()
        self.fig = plt.figure(figsize=(3,3))
        ax = plt.subplot(111, projection='polar')
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        self.line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                               cmap=plt.cm.jet, lw=0)
        ax.set_rmax(DMAX)
        ax.grid(True)

    #Brief: Lance une lecture des points avec le lidar, et mets les points sur le plot.
    #Return: le plot avec les points dedans
    def CreatePlot(self,scans):

        for scan in scans:
            
            #Insertion des points
            offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
            self.line.set_offsets(offsets)

        self.fig.savefig("static/img/plot.jpg")
        radar = cv2.imread("static/img/plot.jpg")
        radar = cv2.imencode('.jpg', radar)[1]
        return radar.tobytes()
        