import os
import asyncio
from math import cos, sin, pi, floor
from socket import timeout
import time
from adafruit_rplidar import RPLidar

#Constants
PORT_NAME = '/dev/ttyUSB0'
max_distance = 0
scans=[]
class Lidarasync(object):

    def __init__ (self):
        """  brief       : Constructeur de la classe RPLidar
              param-type  : None
              return-type : Lidar 
        """ 
        
        self.lidar=None
        self.shorterScan=1000
        self.scans=[]
        # Setup the RPLidar
        try:
            self.lidar = RPLidar(None,PORT_NAME,timeout=3.0)
            self.lidar.start_motor()
        except:
            print("No lidar found")
            return


    async def Get_Data(self):
        """  brief       : Function to get the data
              param-type  : None
              return-type : List(list(int,int,int))
        """ 
        result= await self.scans[1]
        return result
    

    async def DoScan(self):
        """  brief       : Function to scan with the lidar
              param-type  : None
              return-type : List(list(int,int,int))
        """
        scan_data = [0]*400
        scans.clear()

        try:
            for scan in self.lidar.iter_scans():
                scans.append(scan)
                #Get shorter distance
                if((scan[1][2])<self.shorterScan):
                    self.shorterScan=scan[1][2]
                #Stop when we have 2 scans
                if len(scans) >= 2:             
                    #self.Get_Data(scan_data)
                    self.lidar.stop()
                    self.lidar.stop_motor()
                    self.lidar.disconnect()
                    print('Stoping.')
                    return await scans[1]
                    break
            

        except KeyboardInterrupt:
            self.lidar.stop()
            self.lidar.stop_motor()
            self.lidar.disconnect()
            print('Stoping.')