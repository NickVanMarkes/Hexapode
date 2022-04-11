### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : mod_classes/Lidar.py
### Date        : 07/04/2022
### Description : Classe qui récupère les données du lidar, et qui les retournes si besoin.

#packages
from adafruit_rplidar import RPLidar, RPLidarException



#Constantes
PORT_NAME = '/dev/ttyUSB0'
DMAX = 2000
IMIN = 0
IMAX = 50
NBSCANSMAX = 1

#Variables de classe
scans=[]

class Lidar():
    
    #Constructeur
    def __init__(self):
        self.lidar=None
        self.run()

    #fonction qui permet de connecter le lidar, et préviens en cas de problème
    def init(self):
        try:
            lidar = RPLidar(None, PORT_NAME, timeout=3, logging=False)
            #lidar.logging = True
            lidar.stop()            
        except Exception as e:
            print("init-Exception " + str(e))
            return None
        except RPLidarException as le:
            print("init-Lidar Exception " + str(le))
            return None
        return lidar

    #fonction qui permet d'arrêter le lidar, et le déconnecter proprement
    def reset(self,ld):
        try:
            #ld.stop_motor()
            ld.stop()
            ld.disconnect()
        except Exception as e:
            print("reset-Exception " + str(e))
            return False
        except RPLidarException as le:
            print("reset-Lidar Exception " + str(le))
            return False

    #fonction qui récupère les données du lidar
    def loop(self,ld, iter=2):
        scans.clear()
        
        try:
            for scan in ld.iter_scans(iter):
                scans.append(scan)
                if len(scans) > NBSCANSMAX:
                    self.reset(ld)
                    self.lidar=None
                    break
            return True
        except RPLidarException as le:
            print("loop-Lidar Exception " + str(le))
            return False
        except Exception as e:
            print("loop-Exception " + str(e))
            return False

    #fonction qui permet à un programme externe de récupérer les données récupérées auparavant
    def Get_Scans(self):
        if scans != None:
            return scans

    #fonction qui aide en cas de problème avec le lidar
    def CanDoLoop(self,lidar):
        try:
            if self.loop(lidar)== False:
                self.reset(lidar)
                #lidar=self.init()
        except KeyboardInterrupt:
            self.reset(lidar)
            print("program aborted requested")
                
    #fonction qui démare le lidar, et lance l'acquisition de données
    def run(self):
        self.lidar=self.init()
        if self.lidar is None:
            print("Program fails to initialize")
            exit(-1)

        print("Start")
        self.CanDoLoop(self.lidar)