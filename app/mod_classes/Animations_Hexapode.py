# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

class Animations(object):

    def __init__(self):
        self.i2c = busio.I2C(SCL, SDA)

        # Create a simple PCA9685 class instance.
        self.pcaG = PCA9685(self.i2c, address=65)
        self.pcaD = PCA9685(self.i2c, address=66)

        MAXPULSE=1890

        self.pcaG.frequency = 50
        self.pcaD.frequency = 50

        # Create all servo objects, specifying pin number, min and max values.

        #Patte Avant Gauche
        #Hanche
        self.havg = servo.ContinuousServo(self.pcaG.channels[0], min_pulse=1300, max_pulse=MAXPULSE)
        #Tibia
        self.tavg = servo.ContinuousServo(self.pcaG.channels[1], min_pulse=1300, max_pulse=MAXPULSE)
        #Pointe
        self.pavg = servo.ContinuousServo(self.pcaG.channels[2], min_pulse=1300, max_pulse=MAXPULSE)

        #Patte Milieu Gauche
        #Pointe
        self.pmg = servo.ContinuousServo(self.pcaG.channels[4], min_pulse=1300, max_pulse=MAXPULSE)
        #Tibia
        self.tmg = servo.ContinuousServo(self.pcaG.channels[5], min_pulse=1300, max_pulse=MAXPULSE)
        #Hanche
        self.hmg = servo.ContinuousServo(self.pcaG.channels[6], min_pulse=1300, max_pulse=MAXPULSE)

        #Patte Arriere Gauche
        #Hanche
        self.harg = servo.ContinuousServo(self.pcaG.channels[12], min_pulse=1300, max_pulse=MAXPULSE)
        #Tibia
        self.targ = servo.ContinuousServo(self.pcaG.channels[13], min_pulse=1300, max_pulse=MAXPULSE)
        #Pointe
        self.parg = servo.ContinuousServo(self.pcaG.channels[15], min_pulse=1300, max_pulse=MAXPULSE)

        #Patte Avant Droite
        #Pointe
        self.pavd = servo.ContinuousServo(self.pcaD.channels[0], min_pulse=1300, max_pulse=MAXPULSE)
        #Tibia
        self.tavd = servo.ContinuousServo(self.pcaD.channels[1], min_pulse=1300, max_pulse=MAXPULSE)
        #Hanche
        self.havd = servo.ContinuousServo(self.pcaD.channels[2], min_pulse=1300, max_pulse=MAXPULSE)
        #Patte Milieu Droite
        #Pointe
        self.pmd = servo.ContinuousServo(self.pcaD.channels[4], min_pulse=1300, max_pulse=MAXPULSE)
        #Tibia
        self.tmd = servo.ContinuousServo(self.pcaD.channels[5], min_pulse=1300, max_pulse=MAXPULSE)
        #Hanche
        self.hmd = servo.ContinuousServo(self.pcaD.channels[6], min_pulse=1300, max_pulse=MAXPULSE)
        #Patte Arriere Droite
        #Pointe
        self.pard = servo.ContinuousServo(self.pcaD.channels[15], min_pulse=1300, max_pulse=MAXPULSE)
        #Tibia
        self.tard = servo.ContinuousServo(self.pcaD.channels[14], min_pulse=1300, max_pulse=MAXPULSE)
        #Hanche
        self.hard = servo.ContinuousServo(self.pcaD.channels[13], min_pulse=1300, max_pulse=MAXPULSE)
        ## We sleep in the loops to give the servo time to move into position.
        #Hanches à 0
        self.havg.throttle=0
        self.havd.throttle=0
        self.hmd.throttle=0
        self.hmg.throttle=0
        self.harg.throttle=0
        self.hard.throttle=0

        #Pointes à 0
        self.pavg.throttle=0
        self.pavd.throttle=0
        self.pmg.throttle=0
        self.pmd.throttle=0
        self.parg.throttle=0
        self.pard.throttle=0

        #Tibias à 0
        self.tavg.throttle=0
        self.tavd.throttle=0
        self.tmg.throttle=0
        self.tmd.throttle=0
        self.targ.throttle=0
        self.tard.throttle=0



    def Init(self):

        #Etape 1 lever les pattes
        #Pointes
        self.pavg.throttle=1
        self.pavd.throttle=-1
        self.pmg.throttle=1
        self.pmd.throttle=-1
        self.parg.throttle=1
        self.pard.throttle=-1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.pavg.throttle=0
        self.pavd.throttle=0
        self.pmg.throttle=0
        self.pmd.throttle=0
        self.parg.throttle=0
        self.pard.throttle=0

        #Etape 2 baisser les tibias Gauche et mettre une légère force sur les pointes
        #Tibias
        #Gauche
        self.tavg.throttle=1
        self.tmg.throttle=1
        self.targ.throttle=1

        #Pointes
        self.pavg.throttle=-0.05
        self.pmg.throttle=-0.05
        self.parg.throttle=-0.05

        time.sleep(0.003*50) #50 degrés vers le bas
        #Maintiens
        self.tavg.throttle=0.2
        self.tmg.throttle=0.2
        self.targ.throttle=0.2
        time.sleep(1)

        #Etape 3 baisser les tibias Droite et mettre une légère force sur les pointes
        #Tibia Droite
        self.tavd.throttle=-1
        self.tmd.throttle=-1
        self.tard.throttle=-1
        #Pointes Droite
        self.pavd.throttle=0.05
        self.pmd.throttle=0.05
        self.pard.throttle=0.05
        #Pointes Gauche
        self.pavg.throttle=0
        self.pmg.throttle=0
        self.parg.throttle=0
        time.sleep(0.003*50) #50 degrés vers le bas

        self.tavd.throttle=-0.4
        self.tmd.throttle=-0.4
        self.tard.throttle=-0.4

        self.tavg.throttle=0.3
        self.tmg.throttle=0.3
        self.targ.throttle=0.3
        time.sleep(1)
        #Etape 4 baisser les pointes Gauche et les tibias Gauche
        #Pointes Gauche
        self.pavg.throttle=-1
        self.pmg.throttle=-1
        self.parg.throttle=-1
        #Tibia Gauche
        self.tavg.throttle=0.8
        self.tmg.throttle=0.8
        self.targ.throttle=0.8

        self.tavd.throttle=-0.05
        self.tmd.throttle=-0.05
        self.tard.throttle=-0.05

        self.pavd.throttle=0
        self.pmd.throttle=0
        self.pard.throttle=0
        time.sleep(2)
        i=1
        while i<0.1:
            self.tavg.throttle=i
            self.tmg.throttle=i
            self.targ.throttle=i
            i=i-0.05
    #self.pcaD.deinit()
    #self.pcaG.deinit()