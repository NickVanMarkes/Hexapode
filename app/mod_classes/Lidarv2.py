import os
from math import cos, sin, pi, floor
import time
from adafruit_rplidar import RPLidar

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3.0)

# used to scale data to fit on the screen
max_distance = 0
Begin=0
End=0
scans=[]
def process_data(data):
    End=time.time()
    print("Time to process data: ")
    print(End-Begin)
    print(len(scans))
   
        
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
          break
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