# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pcaG = PCA9685(i2c, address=65)
pcaD = PCA9685(i2c, address=66)

MAXPULSE=1890

pcaG.frequency = 50
pcaD.frequency = 50

# Create all servo objects, specifying pin number, min and max values.

#Patte Avant Gauche
#Hanche
havg = servo.ContinuousServo(pcaG.channels[0], min_pulse=1300, max_pulse=MAXPULSE)
#Tibia
tavg = servo.ContinuousServo(pcaG.channels[1], min_pulse=1300, max_pulse=MAXPULSE)
#Pointe
pavg = servo.ContinuousServo(pcaG.channels[2], min_pulse=1300, max_pulse=MAXPULSE)

#Patte Milieu Gauche
#Pointe
pmg = servo.ContinuousServo(pcaG.channels[4], min_pulse=1300, max_pulse=MAXPULSE)
#Tibia
tmg = servo.ContinuousServo(pcaG.channels[5], min_pulse=1300, max_pulse=MAXPULSE)
#Hanche
hmg = servo.ContinuousServo(pcaG.channels[6], min_pulse=1300, max_pulse=MAXPULSE)

#Patte Arriere Gauche
#Hanche
harg = servo.ContinuousServo(pcaG.channels[12], min_pulse=1300, max_pulse=MAXPULSE)
#Tibia
targ = servo.ContinuousServo(pcaG.channels[13], min_pulse=1300, max_pulse=MAXPULSE)
#Pointe
parg = servo.ContinuousServo(pcaG.channels[15], min_pulse=1300, max_pulse=MAXPULSE)

#Patte Avant Droite
#Pointe
pavd = servo.ContinuousServo(pcaD.channels[0], min_pulse=1300, max_pulse=MAXPULSE)
#Tibia
tavd = servo.ContinuousServo(pcaD.channels[1], min_pulse=1300, max_pulse=MAXPULSE)
#Hanche
havd = servo.ContinuousServo(pcaD.channels[2], min_pulse=1300, max_pulse=MAXPULSE)
#Patte Milieu Droite
#Pointe
pmd = servo.ContinuousServo(pcaD.channels[4], min_pulse=1300, max_pulse=MAXPULSE)
#Tibia
tmd = servo.ContinuousServo(pcaD.channels[5], min_pulse=1300, max_pulse=MAXPULSE)
#Hanche
hmd = servo.ContinuousServo(pcaD.channels[6], min_pulse=1300, max_pulse=MAXPULSE)
#Patte Arriere Droite
#Pointe
pard = servo.ContinuousServo(pcaD.channels[15], min_pulse=1300, max_pulse=MAXPULSE)
#Tibia
tard = servo.ContinuousServo(pcaD.channels[14], min_pulse=1300, max_pulse=MAXPULSE)
#Hanche
hard = servo.ContinuousServo(pcaD.channels[13], min_pulse=1300, max_pulse=MAXPULSE)
## We sleep in the loops to give the servo time to move into position.
#Hanches à 0
havg.throttle=0
havd.throttle=0
hmd.throttle=0
hmg.throttle=0
harg.throttle=0
hard.throttle=0

#Pointes à 0
pavg.throttle=0
pavd.throttle=0
pmg.throttle=0
pmd.throttle=0
parg.throttle=0
pard.throttle=0

#Tibias à 0
tavg.throttle=0
tavd.throttle=0
tmg.throttle=0
tmd.throttle=0
targ.throttle=0
tard.throttle=0

#- = vers le bas
# #+ = vers le haut
while True:
    angle=int(input("Entrez l'angle de la pointe : "))
    if(angle>0):
        pavg.throttle=-1
        pavd.throttle=1
        pmg.throttle=-1
        pmd.throttle=1
        parg.throttle=-1
        pard.throttle=1
    elif(angle<0):
        pavg.throttle=1
        pavd.throttle=-1
        pmg.throttle=1
        pmd.throttle=-1
        parg.throttle=1
        pard.throttle=-1
    else:
        pavg.throttle=0
        pavd.throttle=0
        pmg.throttle=0
        pmd.throttle=0
        parg.throttle=0
        pard.throttle=0
    time.sleep(0.003*abs(angle))
    pavg.throttle=0
    pavd.throttle=0
    pmg.throttle=0
    pmd.throttle=0
    parg.throttle=0
    pard.throttle=0
    
    angle5=int(input("Entrez l'angle du Tibia : "))
    if(angle5<0): #Monte
        tavg.throttle=-1
        tavd.throttle=1
        tmg.throttle=-1
        tmd.throttle=1
        targ.throttle=-1
        tard.throttle=1
    elif(angle5>0): #descends
        tavg.throttle=1
        tavd.throttle=-1
        tmg.throttle=1
        tmd.throttle=-1
        targ.throttle=1
        tard.throttle=-1
    else:
        tavg.throttle=0
        tavd.throttle=0
        tmg.throttle=0
        tmd.throttle=0
        targ.throttle=0
        tard.throttle=0
    time.sleep(0.003*abs(angle5))
    if(angle5>0):
        tavg.throttle=-0.2
        tavd.throttle=0.2
        tmg.throttle=-0.2
        tmd.throttle=0.2
        targ.throttle=-0.2
        tard.throttle=0.2
    elif(angle5<0):
        tavg.throttle=0.2
        tavd.throttle=-0.2
        tmg.throttle=0.2
        tmd.throttle=-0.2
        targ.throttle=0.2
        tard.throttle=-0.2
    else:
        tavg.throttle=0
        tavd.throttle=0
        tmg.throttle=0
        tmd.throttle=0
        targ.throttle=0
        tard.throttle=0
    


#i=10
#flag=True
#while True:
#    if flag:
#        i+=1
#        servo4.throttle = -0.5
#    else:
#        i-=1
#        servo4.throttle = 0.5
#
#    if(i>=40):
#        flag=not flag
#        
#    elif(i<=10):
#        flag=not flag
#    time.sleep(0.003*abs(1))
#    servo4.throttle=0.0

#- = vers le haut
#+ = vers le bas
#servo5.throttle = -1.0
#angle5=40
#time.sleep(0.003*angle5)
#servo5.throttle=0.0



    

pca.deinit()