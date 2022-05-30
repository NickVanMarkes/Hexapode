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

class Animations(object):

    WAITTIME = 0.003
    SENSHORAIREPLEINEFORCE = -1
    SENSANTIHORAIREPLEINEFORCE = 1
    WITHOUTFORCE=0
    def __init__(self, gyroscope):
        """  brief       : Initialisation des servomoteurs et du gyroscope.
             parameters  : Gyroscope
             returns : None 
        """

        self.i2c = busio.I2C(SCL, SDA)

        self.gyro=gyroscope

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
        self.HancheAvantGauche = servo.ContinuousServo(self.pcaG.channels[0], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.TibiaAvantGauche = servo.ContinuousServo(self.pcaG.channels[1], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Pointe
        self.PointeAvantGauche = servo.ContinuousServo(self.pcaG.channels[2], min_pulse=1300, max_pulse=self.MAXPULSE)

        #Patte Milieu Gauche
        #Pointe
        self.PointeMilieuGauche = servo.ContinuousServo(self.pcaG.channels[4], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.TibiaMilieuGauche = servo.ContinuousServo(self.pcaG.channels[5], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.HancheMilieuGauche = servo.ContinuousServo(self.pcaG.channels[6], min_pulse=1300, max_pulse=self.MAXPULSE)

        #Patte Arriere Gauche
        #Hanche
        self.HancheArriereGauche = servo.ContinuousServo(self.pcaG.channels[12], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.TibiaArriereGauche = servo.ContinuousServo(self.pcaG.channels[13], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Pointe
        self.PointeArriereGauche = servo.ContinuousServo(self.pcaG.channels[15], min_pulse=1300, max_pulse=self.MAXPULSE)

        #Patte Avant Droite
        #Pointe
        self.PointeAvantDroit = servo.ContinuousServo(self.pcaD.channels[15], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.TibiaAvantDroit = servo.ContinuousServo(self.pcaD.channels[14], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.HancheAvantDroit = servo.ContinuousServo(self.pcaD.channels[13], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Patte Milieu Droite
        #Pointe
        self.PointeMilieuDroit = servo.ContinuousServo(self.pcaD.channels[4], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.TibiaMilieuDroit = servo.ContinuousServo(self.pcaD.channels[5], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.HancheMilieuDroit = servo.ContinuousServo(self.pcaD.channels[6], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Patte Arriere Droite
        #Pointe
        self.PointeArriereDroit = servo.ContinuousServo(self.pcaD.channels[0], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Tibia
        self.TibiaArriereDroit = servo.ContinuousServo(self.pcaD.channels[1], min_pulse=1300, max_pulse=self.MAXPULSE)
        #Hanche
        self.HancheArriereDroit = servo.ContinuousServo(self.pcaD.channels[2], min_pulse=1300, max_pulse=self.MAXPULSE)

        #Hanches à 0
        self.HancheAvantGauche.throttle=self.WITHOUTFORCE
        self.HancheAvantDroit.throttle=self.WITHOUTFORCE
        self.HancheMilieuDroit.throttle=self.WITHOUTFORCE
        self.HancheMilieuGauche.throttle=self.WITHOUTFORCE
        self.HancheArriereGauche.throttle=self.WITHOUTFORCE
        self.HancheArriereDroit.throttle=self.WITHOUTFORCE

        #Pointes à 0
        self.PointeAvantGauche.throttle=self.WITHOUTFORCE
        self.PointeAvantDroit.throttle=self.WITHOUTFORCE
        self.PointeMilieuGauche.throttle=self.WITHOUTFORCE
        self.PointeMilieuDroit.throttle=self.WITHOUTFORCE
        self.PointeArriereGauche.throttle=self.WITHOUTFORCE
        self.PointeArriereDroit.throttle=self.WITHOUTFORCE

        #Tibias à 0
        self.TibiaAvantGauche.throttle=self.WITHOUTFORCE
        self.TibiaAvantDroit.throttle=self.WITHOUTFORCE
        self.TibiaMilieuGauche.throttle=self.WITHOUTFORCE
        self.TibiaMilieuDroit.throttle=self.WITHOUTFORCE
        self.TibiaArriereGauche.throttle=self.WITHOUTFORCE
        self.TibiaArriereDroit.throttle=self.WITHOUTFORCE

        self.initAngles=self.gyro.get_angle()

    def Init(self):

        #Etape 1 lever les pattes
        #Pointes
        self.PointeAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.PointeAvantDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.PointeMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.PointeMilieuDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.PointeArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.PointeArriereDroit.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le haut
        self.PointeAvantGauche.throttle=self.WITHOUTFORCE
        self.PointeAvantDroit.throttle=self.WITHOUTFORCE
        self.PointeMilieuGauche.throttle=self.WITHOUTFORCE
        self.PointeMilieuDroit.throttle=self.WITHOUTFORCE
        self.PointeArriereGauche.throttle=self.WITHOUTFORCE
        self.PointeArriereDroit.throttle=self.WITHOUTFORCE

        #Etape 2 baisser les tibias Gauche et mettre une légère force sur les pointes
        #Tibias
        #Gauche
        self.TibiaAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE

        #Pointes
        self.PointeAvantGauche.throttle=-0.05
        self.PointeMilieuGauche.throttle=-0.05
        self.PointeArriereGauche.throttle=-0.05

        time.sleep(self.WAITTIME*50) #50 degrés vers le bas
        #Maintiens
        self.TibiaAvantGauche.throttle=0.2
        self.TibiaMilieuGauche.throttle=0.2
        self.TibiaArriereGauche.throttle=0.2
        time.sleep(1)

        #Etape 3 baisser les tibias Droite et mettre une légère force sur les pointes
        #Tibia Droite
        self.TibiaAvantDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.TibiaMilieuDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.TibiaArriereDroit.throttle=self.SENSHORAIREPLEINEFORCE
        #Pointes Droite
        self.PointeAvantDroit.throttle=0.05
        self.PointeMilieuDroit.throttle=0.05
        self.PointeArriereDroit.throttle=0.05
        #Pointes Gauche
        self.PointeAvantGauche.throttle=self.WITHOUTFORCE
        self.PointeMilieuGauche.throttle=self.WITHOUTFORCE
        self.PointeArriereGauche.throttle=self.WITHOUTFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le bas

        self.TibiaAvantDroit.throttle=-0.4
        self.TibiaMilieuDroit.throttle=-0.4
        self.TibiaArriereDroit.throttle=-0.4

        self.TibiaAvantGauche.throttle=0.3
        self.TibiaMilieuGauche.throttle=0.3
        self.TibiaArriereGauche.throttle=0.3
        time.sleep(1)
        #Etape 4 baisser les pointes Gauche et les tibias Gauche
        #Pointes Gauche
        self.PointeAvantGauche.throttle=self.SENSHORAIREPLEINEFORCE
        self.PointeMilieuGauche.throttle=self.SENSHORAIREPLEINEFORCE
        self.PointeArriereGauche.throttle=self.SENSHORAIREPLEINEFORCE
        #Tibia Gauche
        self.TibiaAvantGauche.throttle=0.8
        self.TibiaMilieuGauche.throttle=0.8
        self.TibiaArriereGauche.throttle=0.8

        self.TibiaAvantDroit.throttle=-0.05
        self.TibiaMilieuDroit.throttle=-0.05
        self.TibiaArriereDroit.throttle=-0.05

        self.PointeAvantDroit.throttle=self.WITHOUTFORCE
        self.PointeMilieuDroit.throttle=self.WITHOUTFORCE
        self.PointeArriereDroit.throttle=self.WITHOUTFORCE
        time.sleep(2)
        self.TibiaAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(3) #40 degrés vers le haut
        self.TibiaAvantGauche.throttle=0.1
        self.TibiaMilieuGauche.throttle=0.1
        self.TibiaArriereGauche.throttle=0.1

    def Init2(self):
        """  brief       : Animation faisant lever le robot, depuis l'état initial.
             parameters  : None
             returns : None 
        """
        print(self.initAngles["y"])
        #Etape 1 baisser les tibias et légère force sur les pointes
        #Tibias Gauche

        self.TibiaAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        #Tibias Droite
        self.TibiaAvantDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.TibiaMilieuDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.TibiaArriereDroit.throttle=self.SENSHORAIREPLEINEFORCE

        self.PointeAvantGauche.throttle=-0.1
        self.PointeMilieuGauche.throttle=-0.1
        self.PointeArriereGauche.throttle=-0.1
        self.PointeAvantDroit.throttle=0.1
        self.PointeMilieuDroit.throttle=0.1
        self.PointeArriereDroit.throttle=0.1

        time.sleep(2)

        self.TibiaArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.TibiaAvantDroit.throttle=-0.1
        self.TibiaMilieuDroit.throttle=-0.1
        self.TibiaArriereDroit.throttle=-0.1

        self.PointeAvantGauche.throttle=-0.5
        self.PointeMilieuGauche.throttle=-0.5
        self.PointeArriereGauche.throttle=-0.5
        time.sleep(3)
            
        #Maintiens
        self.TibiaAvantGauche.throttle=0.2
        self.TibiaMilieuGauche.throttle=0.2
        self.TibiaArriereGauche.throttle=0.2
        self.TibiaAvantDroit.throttle=-0.2
        self.TibiaMilieuDroit.throttle=-0.2
        self.TibiaArriereDroit.throttle=-0.2

    def Avance(self):
        """  brief       : Animation permettant au robot d'avancer.
             parameters  : None
             returns : None 
        """

        print("AVANCE")
        print("===========================================================")
        #PATTE AVANT GAUCHE
        print("Lever les pattes")
        self.TibiaAvantGauche.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le haut
        self.TibiaAvantGauche.throttle=self.WITHOUTFORCE

        print("Tourner les hanches")
        self.HancheAvantGauche.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*40) #30 degrés vers l'avant
        self.HancheAvantGauche.throttle=self.WITHOUTFORCE
        time.sleep(self.WAITTIME*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.PointeAvantGauche.throttle=-0.1

        print("baisser les pattes")
        self.TibiaAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(2)
        self.TibiaAvantGauche.throttle=0.1


        # Patte Milieu Gauche
        print("Lever les pattes")
        self.TibiaMilieuGauche.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le haut
        self.TibiaMilieuGauche.throttle=self.WITHOUTFORCE

        print("Tourner les hanches")
        self.HancheMilieuGauche.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*40) #30 degrés vers l'avant
        self.HancheMilieuGauche.throttle=self.WITHOUTFORCE

        time.sleep(self.WAITTIME*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.PointeMilieuGauche.throttle=-0.1

        print("baisser les pattes")
        self.TibiaMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(2)
        self.TibiaMilieuGauche.throttle=0.1

        # Patte Arrière Gauche
        print("Lever les pattes")
        self.TibiaArriereGauche.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le haut
        self.TibiaArriereGauche.throttle=self.WITHOUTFORCE

        print("Tourner les hanches")
        self.HancheArriereGauche.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*40) #30 degrés vers l'avant
        self.HancheArriereGauche.throttle=self.WITHOUTFORCE

        time.sleep(self.WAITTIME*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.PointeArriereGauche.throttle=-0.1

        print("baisser les pattes")
        self.TibiaArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(2)
        self.TibiaArriereGauche.throttle=0.2

        # Patte Avant Droit
        print("Lever les pattes")
        self.TibiaAvantDroit.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le haut
        self.TibiaAvantDroit.throttle=self.WITHOUTFORCE

        print("Tourner les hanches")
        self.HancheAvantDroit.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*40) #30 degrés vers l'avant
        self.HancheAvantDroit.throttle=self.WITHOUTFORCE

        time.sleep(self.WAITTIME*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.PointeAvantDroit.throttle=0.1

        print("baisser les pattes")
        self.TibiaAvantDroit.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(2)
        self.TibiaAvantDroit.throttle=-0.1

        # Patte Milieu Droit
        print("Lever les pattes")
        self.TibiaMilieuDroit.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le haut
        self.TibiaMilieuDroit.throttle=self.WITHOUTFORCE

        print("Tourner les hanches")
        self.HancheMilieuDroit.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*40) #30 degrés vers l'avant
        self.HancheMilieuDroit.throttle=self.WITHOUTFORCE

        time.sleep(self.WAITTIME*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.PointeMilieuDroit.throttle=0.1

        print("baisser les pattes")
        self.TibiaMilieuDroit.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(2)
        self.TibiaMilieuDroit.throttle=-0.2

        # Patte Arrière Droit
        print("Lever les pattes")
        self.TibiaArriereDroit.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*50) #50 degrés vers le haut
        self.TibiaArriereDroit.throttle=self.WITHOUTFORCE

        print("Tourner les hanches")
        self.HancheArriereDroit.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*40) #30 degrés vers l'avant
        self.HancheArriereDroit.throttle=self.WITHOUTFORCE

        time.sleep(self.WAITTIME*180) #180 degrés vers le bas
        print("Mettre un peu de force sur les pointes")
        self.PointeArriereDroit.throttle=0.1

        print("baisser les pattes")
        self.TibiaArriereDroit.throttle=self.SENSHORAIREPLEINEFORCE
        time.sleep(2)
        self.TibiaArriereDroit.throttle=-0.2

        self.HancheAvantDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.HancheMilieuDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.HancheArriereDroit.throttle=self.SENSHORAIREPLEINEFORCE
        self.HancheAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.HancheMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        self.HancheArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
        time.sleep(self.WAITTIME*90) #90 degrés vers l'arrière
        self.HancheAvantDroit.throttle=-self.WITHOUTFORCE
        self.HancheMilieuDroit.throttle=-self.WITHOUTFORCE
        self.HancheArriereDroit.throttle=-self.WITHOUTFORCE
        self.HancheAvantGauche.throttle=self.WITHOUTFORCE
        self.HancheMilieuGauche.throttle=self.WITHOUTFORCE
        self.HancheArriereGauche.throttle=self.WITHOUTFORCE


        self.Maintiens()

    def Maintiens(self):
        """  brief       : Fonction qui permet au robot de rester droit grâce aux PID et au gyroscope.
             parameters  : None
             returns : None 
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
                self.TibiaArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
                self.TibiaMilieuGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
                self.TibiaAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
                self.TibiaArriereDroit.throttle=-0.05
                self.TibiaMilieuDroit.throttle=-0.05
                self.TibiaAvantDroit.throttle=-0.05
                isnotplaty=True
            elif outputy<0.05 and outputy>-0.05:
                self.TibiaArriereGauche.throttle=0.2
                self.TibiaMilieuGauche.throttle=0.2
                self.TibiaAvantGauche.throttle=0.2
                self.TibiaArriereDroit.throttle=-0.2
                self.TibiaMilieuDroit.throttle=-0.2
                self.TibiaAvantDroit.throttle=-0.2
                isnotplaty=False
            elif outputy>0:
                self.TibiaArriereDroit.throttle=self.SENSHORAIREPLEINEFORCE
                self.TibiaMilieuDroit.throttle=self.SENSHORAIREPLEINEFORCE
                self.TibiaAvantDroit.throttle=self.SENSHORAIREPLEINEFORCE
                self.TibiaArriereGauche.throttle=0.05
                self.TibiaMilieuGauche.throttle=0.05
                self.TibiaAvantGauche.throttle=0.05
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
            
            self.PointeAvantGauche.throttle=-0.2
            self.PointeArriereGauche.throttle=-0.1
            self.PointeAvantDroit.throttle=0.1
            self.PointeArriereDroit.throttle=0.1

            if difference<-self.MARGEDIFFERENCE:
                self.TibiaArriereGauche.throttle=0.1
                self.TibiaArriereDroit.throttle=-0.1
                self.TibiaAvantGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
                self.TibiaAvantDroit.throttle=self.SENSHORAIREPLEINEFORCE
                isnotplatx=True
            elif difference<self.MARGEDIFFERENCE and difference>-self.MARGEDIFFERENCE:
                self.TibiaArriereGauche.throttle=0.2
                self.TibiaMilieuGauche.throttle=0.2
                self.TibiaAvantGauche.throttle=0.2
                self.TibiaArriereDroit.throttle=-0.2
                self.TibiaMilieuDroit.throttle=-0.2
                self.TibiaAvantDroit.throttle=-0.2
                isnotplatx=False
            elif difference>self.MARGEDIFFERENCE:
                self.TibiaAvantGauche.throttle=-0.1
                self.TibiaAvantDroit.throttle=0.1
                self.TibiaArriereGauche.throttle=self.SENSANTIHORAIREPLEINEFORCE
                self.TibiaArriereDroit.throttle=self.SENSHORAIREPLEINEFORCE
                isnotplatx=True

    #self.pcaD.deinit()
    #self.pcaG.deinit()