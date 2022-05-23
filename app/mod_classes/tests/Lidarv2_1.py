import os
import asyncio
from math import cos, sin, pi, floor
import time
from rplidar import RPLidar, RPLidarException

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(PORT_NAME, timeout=3.0)
lidar.start_motor()

# used to scale data to fit on the screen
max_distance = 0
Begin=0
End=0
scans=[]
def process_data(data):
    End=time.time()
    print("Time to process data: ")
    print(End-Begin)
    pass

scan_data = [0]*400
scans.clear()

try:
    Begin=time.time()
    for scan in lidar.iter_scans():
        scans.append(scan)
        
        if len(scans) >= 2:
            #for (_, angle, distance) in scan:
            #    scan_data[min([359, floor(angle)])] = distance                
          process_data(scan_data)
        #   lidar.clear_input()
        #   break
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    print('Stoping.')
    print(scans[1])
    print(len(scans[0])+len(scans[1]))

except KeyboardInterrupt:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    print('Stoping.')
except RPLidarException as le :
    print('RPLidar exception :', str(le))
    process_data(scan_data)