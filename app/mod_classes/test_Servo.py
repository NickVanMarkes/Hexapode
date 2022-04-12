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
pca = PCA9685(i2c, address=65)

MAXPULSE=1890

pca.frequency = 50

# Create all servo objects, specifying pin number, min and max values.

#Patte Avant Gauche
servo0 = servo.ContinuousServo(pca.channels[0], min_pulse=1300, max_pulse=MAXPULSE)
servo1 = servo.ContinuousServo(pca.channels[1], min_pulse=1300, max_pulse=MAXPULSE)
servo2 = servo.ContinuousServo(pca.channels[2], min_pulse=1300, max_pulse=MAXPULSE)

#Patte Milieu Gauche
#Pointe
servo4 = servo.ContinuousServo(pca.channels[4], min_pulse=1300, max_pulse=MAXPULSE)
#Tibia
servo5 = servo.ContinuousServo(pca.channels[5], min_pulse=1300, max_pulse=MAXPULSE)
#Hanche
servo6 = servo.ContinuousServo(pca.channels[6], min_pulse=1300, max_pulse=MAXPULSE)

#Patte Arriere Gauche
servo13 = servo.ContinuousServo(pca.channels[13], min_pulse=1300, max_pulse=MAXPULSE)
servo14 = servo.ContinuousServo(pca.channels[14], min_pulse=1300, max_pulse=MAXPULSE)
servo15 = servo.ContinuousServo(pca.channels[15], min_pulse=1300, max_pulse=MAXPULSE)

#Patte Avant Droite

#Patte Milieu Droite

#Patte Arriere Droite
## We sleep in the loops to give the servo time to move into position.
servo0.throttle=0
servo1.throttle=0
servo2.throttle=0

servo4.throttle=0
servo6.throttle = 0.0
servo13.throttle = 0.0
servo14.throttle = 0.0
servo15.throttle = 0.0

#- = vers le bas
# #+ = vers le haut
while True:
    angle=int(input("Entrez l'angle de la pointe : "))
    if(angle>0):
        servo4.throttle = -1.0
        servo2.throttle = -1.0
    elif(angle<0):
        servo4.throttle = 1.0
        servo2.throttle = 1.0
    else:
        servo4.throttle = 0.0
        servo2.throttle=0.0
    time.sleep(0.003*abs(angle))
    servo4.throttle=0.0
    servo2.throttle=0.0
    
    angle5=int(input("Entrez l'angle du Tibia : "))
    if(angle5>0):
        servo5.throttle = -1.0
        servo1.throttle = -1.0
    elif(angle5<0):
        servo5.throttle = 1.0
        servo1.throttle = 1.0
    else:
        servo5.throttle = 0.0
        servo1.throttle=0.0
    time.sleep(0.003*abs(angle5))
    if(angle5>0):
        servo5.throttle = -0.5
        servo1.throttle = -0.5
    elif(angle5<0):
        servo5.throttle = 0.5
        servo1.throttle = 0.5
    else:
        servo5.throttle = 0.0
        servo1.throttle=0.0
    


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