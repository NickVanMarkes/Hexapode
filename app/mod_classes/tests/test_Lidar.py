import sys
import time


sys.path.append("../")

from LidarAsync import Lidarasync
from RepeatTimer import RepeatTimer

#Test du singleton
lidar=Lidarasync()
lidar2=Lidarasync()

print("Est-ce la même instance? ",lidar is lidar2)
result=[]

print("==========================================================")
print("Sans thread")
print("==========================================================")
#Scan réussi
lidar.DoScan()

result=lidar.Get_Data()
print(len(result))

print(lidar.ShorterScan)

print("==========================================================")
print("Avec thread")
print("==========================================================")

#Répétition du scan toutes les secondes
thread=RepeatTimer(0.05,lidar.DoScan)
#lancement du thread
thread.start()
resultwithoutdoubles=[] 
while len(resultwithoutdoubles)<10:
     
     #Ajout des valeurs dans notre liste
    if(result!=lidar.Get_Data()):
        result+=lidar.Get_Data().copy()
    #Retire les doublons
    for scans in result:
        if scans not in resultwithoutdoubles:
            resultwithoutdoubles.append(scans)
    time.sleep(0.05) #Attendre 0.05 secondes



thread.cancel()

if result is []:
    print("No data")