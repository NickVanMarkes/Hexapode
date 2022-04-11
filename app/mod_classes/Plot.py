### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Plot.py
### Date        : 07/04/2022
### Description : Classe qui créer des plots (vue radar) selon les données captées par le lidar
import time

#MatPlotLib

Begin=time.time()
import matplotlib.pyplot as plt
End=time.time()
print("Time to import matplotlib in Plot.py :")
print(End-Begin)
Begin=time.time()
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
End=time.time()
print("Time to import matplotlib.backend in Plot.py :")
print(End-Begin)

BeginLidar=time.time()
# Lidar pour les données
from Lidar import Lidar
EndLidar=time.time()
print("Time to import Lidar in Plot.py :")
print(EndLidar-BeginLidar)

# Autres librairies
import numpy as np
import io


#Constantes
DMAX = 2000
IMIN = 0
IMAX = 50
class Radar(object):

    #Constructeur
    #Brief: Initialise le plot avec la forme et les lignes. Instantie le lidar
    def __init__(self):
        # Get Lidar
        self.lidar=Lidar()
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
    def CreatePlot(self):
        self.lidar.run()
        scans=self.lidar.Get_Scans()

        for scan in scans:
            
            #Insertion des points
            offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
            self.line.set_offsets(offsets)
            #intens = np.array([meas[0] for meas in scan])
            #self.line.set_array(intens)


        buf= io.BytesIO()
        FigureCanvas(self.fig).print_png(buf)
        self.fig.savefig("plot.png")
        return self.fig