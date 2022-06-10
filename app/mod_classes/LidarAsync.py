### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : app/mod_classes/LidarAsync.py
### Date        : 03/05/2022
### Description : Classe qui contrôle le lidar, préparée pour faire du multithreading.

from adafruit_rplidar import RPLidar, RPLidarException

#Constants
PORT_NAME = '/dev/ttyUSB0'

class Lidarasync(object):
    _instances = {}
    def __new__(cls):
        """  brief: Je rends la classe en tant que singleton.
             
             parameters  :
                 None
             
             returns :
                instance
        """ 
        if cls not in cls._instances:
            cls._instances[cls] = super(Lidarasync, cls).__new__(cls)
        return cls._instances[cls]

    def __init__ (self):
        """  brief: Constructeur de la classe Lidar, initialise les valeurs et le lidar.
             
             parameters  :
                 None
             
             returns :
                lidar
        """ 
        
        self.lidar=None
        self.shorterScan=2000
        self.scans=[]
        # Setup the RPLidar
        try:
            self.lidar = RPLidar(None,PORT_NAME,timeout=3.0)
        except:
            print("No lidar found")
            return

    @property
    def ShorterScan(self):
        return self.shorterScan

    def Get_Data(self):
        """  brief: Fonction permettant de récupérer les données du lidar.
             
             parameters  :
                 None
             
             returns :
                list(list(float,float,float))
        """ 
        if len(self.scans)>0:
            result= self.scans
        else:
            result= []
        
        return result
    

    def DoScan(self):
        """  brief: Fonction effectuant le scan avec le lidar.
             
             parameters  :
                 None
             
             returns :
                None
        """ 
        self.scans=[]
        self.lidar.connect()
        try:
            for scan in self.lidar.iter_scans():
                self.scans.append(scan)
                #Get shorter distance
                self.shorterScan=1200
                for meas in scan:
                    if meas[2] < self.shorterScan:
                        self.shorterScan = meas[2]
                            
                #Stop when we have 2 scans
                if len(self.scans) >= 2:             
                    break
            self.StopLidar(withmotor=False)
            #print('Stoping, scan completed.')
        except RPLidarException as ex:
            print(ex)
            self.StopLidar()
            print('Stoping RPLidarException.')

    def StartLidar(self):
        """  brief: Fonction qui permet de démarrer le moteur du lidar.
             
             parameters  :
                 None
             
             returns :
                None
        """ 
        self.lidar.start_motor()
    
    def StopLidar(self,withmotor=True):
        """  brief: Fonction permettant d'arrêter le lidar, et le déconnecte.
             
             parameters  :
                 bool
             
             returns :
                None
        """ 
        if withmotor:
            self.lidar.stop_motor()
        self.lidar.stop()
        self.lidar.disconnect()