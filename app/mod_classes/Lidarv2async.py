import os
import asyncio
from math import cos, sin, pi, floor
from socket import timeout
import time
from adafruit_rplidar import RPLidar, RPLidarException

#Constants
PORT_NAME = '/dev/ttyUSB0'
max_distance = 0
scans=[]
class Lidarasync(object):
    _instances = {}
    def __new__(cls):
        """  brief       : Je rends la classe en tant que singleton
              param-type  : None
              return-type : instance 
        """ 
        if cls not in cls._instances:
            cls._instances[cls] = super(Lidarasync, cls).__new__(cls)
        return cls._instances[cls]


    def __init__ (self):
        """  brief       : Constructeur de la classe RPLidar
              param-type  : None
              return-type : Lidar 
        """ 
        
        self.lidar=None
        self.shorterScan=1000
        self.scans=[]
        self.increment=0
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
        """  brief       : Function to get the data
              param-type  : None
              return-type : List(list(int,int,int))
        """ 
        if len(self.scans)>0:
            return self.scans
        else:
            return []
    

    def DoScan(self):
        """  brief       : Function to scan with the lidar
              param-type  : None
              return-type : None
        """
        
        self.shorterScan=1000
        self.scans=[]
        self.lidar.connect()
        try:
            for scan in self.lidar.iter_scans():
                self.scans.append(scan)
                #Get shorter distance
                for meas in scan:
                    if meas[2] < self.shorterScan:
                        self.shorterScan = meas[2]
                #Stop when we have 2 scans
                if len(self.scans) >= 2:             
                    break
            self.lidar.stop()
            #self.lidar.stop_motor()
            self.lidar.disconnect()
            print('Stoping.')

        except KeyboardInterrupt:
            self.lidar.stop()
            self.lidar.stop_motor()
            self.lidar.disconnect()
            print('Stoping.')
        except RPLidarException as ex:
            print(ex)
            self.lidar.stop()
            self.lidar.stop_motor()
            self.lidar.connect()
            print('Stoping.')

    def IncrementTest(self):
        """  brief       : Function to increment the test
        """
        self.increment+=1
        print("Increment: ",self.increment)