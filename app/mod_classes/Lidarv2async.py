import os
import asyncio
from math import cos, sin, pi, floor
from socket import timeout
import time
from adafruit_rplidar import RPLidar

#Constants
PORT_NAME = '/dev/ttyUSB0'
# used to scale data to fit on the screen
max_distance = 0
Begin=0
End=0
scans=[]
class Lidarasync(object):

    def __init__ (self):
        """  brief       : Constructeur de la classe RPLidar
              param-type  : None
              return-type : Lidar 
        """ 
        # Setup the RPLidar
        self.lidar=None
        self.scans=[]
        self.lidar = RPLidar(None, PORT_NAME,timeout=3.0)

    def __del__ (self) -> None:
        """  brief       : Destructeur de l'objet RPLidar
              param-type  : None
              return-type : None 
        """ 
        self.lidar.stop()
        self.lidar.stop_motor()
        self.lidar.disconnect()
        self.lidar=None
        print('Stoping.')


    async def process_data(self):
        """  brief       : Function to process the data
              param-type  : None
              return-type : List(list(int,int,int))
        """ 
        End=time.time()
        print("Time to process data: ")
        print(End-Begin)
        return await self.scans
    
    # async def Get_Data(self):
    #     """  brief       : Function to get the data
    #           param-type  : None
    #           return-type : List(list(int,int,int))
    #     """
    #     return await self.process_data()

    def DoScan(self):
        """  brief       : Function to scan with the lidar
              param-type  : None
              return-type : List(list(int,int,int))
        """
        scan_data = [0]*400
        scans.clear()

        try:
            global Begin
            Begin=time.time()
            for scan in self.lidar.iter_scans():
                scans.append(scan)

                if len(scans) >= 2:             
                  self.process_data(scan_data)
                  break
            self.lidar.stop()
            self.lidar.stop_motor()
            self.lidar.disconnect()
            print('Stoping.')

        except KeyboardInterrupt:
            self.lidar.stop()
            self.lidar.stop_motor()
            self.lidar.disconnect()
            print('Stoping.')