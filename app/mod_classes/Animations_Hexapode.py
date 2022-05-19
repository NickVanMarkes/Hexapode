### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : app/mod_classes/Animations_Hexapode.py
### Date        : 03/05/2022
### Description : Classe qui contient les animations du hexapode.

import sys
import time

from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from simple_pid import PID

sys.path.append("../")

from Gyroscope import Gyroscope

class Animations(object):

    def __init__(self):
        """  brief       : Initialisation des servomoteurs et du gyroscope.
             param-type  : None
             return-type : None 
        """

        self.i2c = busio.I2C(SCL, SDA)

        self.gyro=Gyroscope()

        # Création des instances des différents modules PCA9685
        self.pcaG = PCA9685(self.i2c, address=65)
        self.pcaD = PCA9685(self.i2c, address=66)

        self.MAXPULSE=1890
        self.MARGEDIFFERENCE=0.5

        self.pcaG.frequency = 50
        self.pcaD.frequency = 50

        # Instantiation des servomoteurs

        #Patte Avant Gauche
        #Hanche
        self.havg = servo.ContinuousServo(self.pcaG.channels[0], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.tavg = servo.ContinuousServo(self.pcaG.channels[1], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Pointe
        self.pavg = servo.ContinuousServo(self.pcaG.channels[2], min_pulse=1300, max_pulse=self.MAXPULSE)

        #Patte Milieu Gauche
        #Pointe
        self.pmg = servo.ContinuousServo(self.pcaG.channels[4], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.tmg = servo.ContinuousServo(self.pcaG.channels[5], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.hmg = servo.ContinuousServo(self.pcaG.channels[6], min_pulse=1300, max_pulse=self.MAXPULSE)

        #Patte Arriere Gauche
        #Hanche
        self.harg = servo.ContinuousServo(self.pcaG.channels[12], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.targ = servo.ContinuousServo(self.pcaG.channels[13], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Pointe
        self.parg = servo.ContinuousServo(self.pcaG.channels[15], min_pulse=1300, max_pulse=self.MAXPULSE)

        #Patte Avant Droite
        #Pointe
        self.pavd = servo.ContinuousServo(self.pcaD.channels[15], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.tavd = servo.ContinuousServo(self.pcaD.channels[14], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.havd = servo.ContinuousServo(self.pcaD.channels[13], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Patte Milieu Droite
        #Pointe
        self.pmd = servo.ContinuousServo(self.pcaD.channels[4], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.tmd = servo.ContinuousServo(self.pcaD.channels[5], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.hmd = servo.ContinuousServo(self.pcaD.channels[6], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Patte Arriere Droite
        #Pointe
        self.pard = servo.ContinuousServo(self.pcaD.channels[0], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.tard = servo.ContinuousServo(self.pcaD.channels[1], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.hard = servo.ContinuousServo(self.pcaD.channels[2], min_pulse=1300, max_pulse=self.MAXPULSE)

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

        self.initAngles=self.gyro.get_angle()

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
        self.tavg.throttle=1
        self.tmg.throttle=1
        self.targ.throttle=1
        time.sleep(3) #40 degrés vers le haut
        self.tavg.throttle=0.1
        self.tmg.throttle=0.1
        self.targ.throttle=0.1

    def Init2(self):
        """  brief       : Animation faisant lever le robot, depuis l'état initial.
             param-type  : None
             return-type : None 
        """
        print(self.initAngles["y"])
        #Etape 1 baisser les tibias et légère force sur les pointes
        #Tibias Gauche

        self.tavg.throttle=0.4
        self.tmg.throttle=0.4
        self.targ.throttle=0.4
        #Tibias Droite
        self.tavd.throttle=-1
        self.tmd.throttle=-1
        self.tard.throttle=-1

        self.pavg.throttle=-0.1
        self.pmg.throttle=-0.1
        self.parg.throttle=-0.1
        self.pavd.throttle=0.1
        self.pmd.throttle=0.1
        self.pard.throttle=0.1

        time.sleep(2)

        self.targ.throttle=1
        self.tavg.throttle=1
        self.tmg.throttle=1
        self.tavd.throttle=-0.1
        self.tmd.throttle=-0.1
        self.tard.throttle=-0.1

        self.pavg.throttle=-0.5
        self.pmg.throttle=-0.5
        self.parg.throttle=-0.5
        time.sleep(3)
            
        #Maintiens
        self.tavg.throttle=0.2
        self.tmg.throttle=0.2
        self.targ.throttle=0.2
        self.tavd.throttle=-0.2
        self.tmd.throttle=-0.2
        self.tard.throttle=-0.2

    def Avance(self):
        """  brief       : Animation permettant au robot d'avancer.
             param-type  : None
             return-type : None 
        """

        print("AVANCE")
        print("===========================================================")
        #PATTE AVANT GAUCHE
        print("Lever les pattes")
        self.tavg.throttle=-1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.tavg.throttle=0

        print("Tourner les hanches")
        self.havg.throttle=-1
        time.sleep(0.003*40) #30 degrés vers l'avant
        self.havg.throttle=0
        time.sleep(0.003*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.pavg.throttle=-0.1

        print("baisser les pattes")
        self.tavg.throttle=1
        time.sleep(2)
        self.tavg.throttle=0.2


        # Patte Milieu Gauche
        print("Lever les pattes")
        self.tmg.throttle=-1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.tmg.throttle=0

        print("Tourner les hanches")
        self.hmg.throttle=-1
        time.sleep(0.003*40) #30 degrés vers l'avant
        self.hmg.throttle=0

        time.sleep(0.003*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.pmg.throttle=-0.1

        print("baisser les pattes")
        self.tmg.throttle=1
        time.sleep(2)
        self.tmg.throttle=0.2

        # Patte Arrière Gauche
        print("Lever les pattes")
        self.targ.throttle=-1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.targ.throttle=0

        print("Tourner les hanches")
        self.harg.throttle=-1
        time.sleep(0.003*40) #30 degrés vers l'avant
        self.harg.throttle=0

        time.sleep(0.003*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.parg.throttle=-0.1

        print("baisser les pattes")
        self.targ.throttle=1
        time.sleep(2)
        self.targ.throttle=0.2

        # Patte Avant Droit
        print("Lever les pattes")
        self.tavd.throttle=1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.tavd.throttle=0

        print("Tourner les hanches")
        self.havd.throttle=1
        time.sleep(0.003*40) #30 degrés vers l'avant
        self.havd.throttle=0

        time.sleep(0.003*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.pavd.throttle=0.1

        print("baisser les pattes")
        self.tavd.throttle=-1
        time.sleep(2)
        self.tavd.throttle=-0.2

        # Patte Milieu Droit
        print("Lever les pattes")
        self.tmd.throttle=1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.tmd.throttle=0

        print("Tourner les hanches")
        self.hmd.throttle=1
        time.sleep(0.003*40) #30 degrés vers l'avant
        self.hmd.throttle=0

        time.sleep(0.003*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.pmd.throttle=0.1

        print("baisser les pattes")
        self.tmd.throttle=-1
        time.sleep(2)
        self.tmd.throttle=-0.2

        # Patte Arrière Droit
        print("Lever les pattes")
        self.tard.throttle=1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.tard.throttle=0

        print("Tourner les hanches")
        self.hard.throttle=1
        time.sleep(0.003*40) #30 degrés vers l'avant
        self.hard.throttle=0

        time.sleep(0.003*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.pard.throttle=0.1

        print("baisser les pattes")
        self.tard.throttle=-1
        time.sleep(2)
        self.tard.throttle=-0.2

        self.havd.throttle=-1
        self.hmd.throttle=-1
        self.hard.throttle=-1
        self.havg.throttle=1
        self.hmg.throttle=1
        self.harg.throttle=1
        time.sleep(0.003*90) #90 degrés vers l'arrière
        self.havd.throttle=-0
        self.hmd.throttle=-0
        self.hard.throttle=-0
        self.havg.throttle=0
        self.hmg.throttle=0
        self.harg.throttle=0


        self.Maintiens()

    def Maintiens(self):
        """  brief       : Fonction qui permet au robot de rester droit grâce aux PID et au gyroscope.
             param-type  : None
             return-type : None 
        """
        print("MAINTIENS")
        print("===========================================================")
        pidy=PID(0.1,0.1,0.1,setpoint=self.initAngles["y"])
        pidx=PID(0.5,0.5,0.5,setpoint=self.initAngles["x"])
        pidy.sample_time=0.5
        pidx.sample_time=0.5
        memooutputy=0
        memooutputx=0
        isnotplatx=True
        isnotplaty=True

        while isnotplaty:
            angles=self.gyro.get_angle()

            #Axe Y
            outputy=pidy(angles["y"])

            if outputy!=memooutputy:
                print("Output Y : ",outputy)
                memooutputy=outputy
            
        
            if outputy<0:
                self.targ.throttle=1
                self.tmg.throttle=1
                self.tavg.throttle=1
                self.tard.throttle=-0.05
                self.tmd.throttle=-0.05
                self.tavd.throttle=-0.05
                isnotplaty=True
            elif outputy<0.05 and outputy>-0.05:
                self.targ.throttle=0.2
                self.tmg.throttle=0.2
                self.tavg.throttle=0.2
                self.tard.throttle=-0.2
                self.tmd.throttle=-0.2
                self.tavd.throttle=-0.2
                isnotplaty=False
            elif outputy>0:
                self.tard.throttle=-1
                self.tmd.throttle=-1
                self.tavd.throttle=-1
                self.targ.throttle=0.05
                self.tmg.throttle=0.05
                self.tavg.throttle=0.05
                isnotplaty=True

            #Axe X
        print(self.initAngles["x"])
        print(self.initAngles["y"])
        print(self.gyro.get_angle()["y"])
        
        while isnotplatx:
            angles=self.gyro.get_angle()
            
            outputx=pidx(angles["x"])
            if outputx!=memooutputx:
                print("Angle de X: ",angles["x"])
                print("Output X : ",outputx)
                print(outputx-self.initAngles["x"])
                memooutputx=outputx
            difference=outputx-self.initAngles["x"]
            
            self.pavg.throttle=-0.2
            self.parg.throttle=-0.1
            self.pavd.throttle=0.1
            self.pard.throttle=0.1

            if difference<-self.MARGEDIFFERENCE:
                self.targ.throttle=0.1
                self.tard.throttle=-0.1
                self.tavg.throttle=1
                self.tavd.throttle=-1
                isnotplatx=True
            elif difference<self.MARGEDIFFERENCE and difference>-self.MARGEDIFFERENCE:
                self.targ.throttle=0.2
                self.tmg.throttle=0.2
                self.tavg.throttle=0.2
                self.tard.throttle=-0.2
                self.tmd.throttle=-0.2
                self.tavd.throttle=-0.2
                isnotplatx=False
            elif difference>self.MARGEDIFFERENCE:
                self.tavg.throttle=-0.1
                self.tavd.throttle=0.1
                self.targ.throttle=1
                self.tard.throttle=-1
                isnotplatx=True

    #self.pcaD.deinit()
    #self.pcaG.deinit()