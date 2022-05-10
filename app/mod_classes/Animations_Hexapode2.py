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

sys.path.append("../")

from Gyroscope import Gyroscope
from Patte import Patte

class Animations(object):

    def __init__(self):

        self.gyro=Gyroscope()


        # Instantiation des Pattes
        self.patteAvG=Patte("Gauche", "Avant")
        self.patteAvD=Patte("Droite", "Avant")
        self.patteMG=Patte("Gauche", "Milieu")
        self.patteMD=Patte("Droite", "Milieu")
        self.patteArG=Patte("Gauche", "Arriere")
        self.patteArD=Patte("Droite", "Arriere")
        self.pattes=[self.patteAvG, self.patteAvD, self.patteMG, self.patteMD, self.patteArG, self.patteArD]
        
        for item in self.pattes:
            item.WithoutForce()
        



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

        angles=self.gyro.get_angle()

        print(angles["x"])
        #Etape 1 baisser les tibias et légère force sur les pointes
        #Tibias Gauche

        self.patteAvG.Baisser_Tibia(1,40)
        self.patteMG.Baisser_Tibia(1,40)        
        self.patteArG.Baisser_Tibia(1,40)
        
        #Tibias Droite
        # self.tavd.throttle=-1
        # self.tmd.throttle=-1
        # self.tard.throttle=-1

        self.patteAvD.Baisser_Tibia(1,-100)
        self.patteAvD.Tibia.throttle=0
        self.patteMD.Baisser_Tibia(1,-100)
        self.patteMD.Tibia.throttle=0
        self.patteArD.Baisser_Tibia(1,-100)
        self.patteArD.Tibia.throttle=0
            

        # self.pavg.throttle=-0.1
        # self.pmg.throttle=-0.1
        # self.parg.throttle=-0.1
        # self.pavd.throttle=0.1
        # self.pmd.throttle=0.1
        # self.pard.throttle=0.1

        self.patteAvD.Baisser_Pointe(15,10)
        self.patteMD.Baisser_Pointe(15,10)
        self.patteArD.Baisser_Pointe(15,10)
        self.patteAvG.Baisser_Pointe(15,-10)
        self.patteMG.Baisser_Pointe(15,-10)
        self.patteArG.Baisser_Pointe(15,-10)

        time.sleep(1.5) #50 degrés vers le bas

        # self.targ.throttle=1
        # self.tavg.throttle=1
        # self.tmg.throttle=1

        self.patteArG.Baisser_Tibia(15,100)
        self.patteMG.Baisser_Tibia(15,100)
        self.patteAvG.Baisser_Tibia(15,100)

        # self.tavd.throttle=-0.1
        # self.tmd.throttle=-0.1
        # self.tard.throttle=-0.1

        self.patteAvD.Baisser_Tibia(15,-10)
        self.patteMD.Baisser_Tibia(15,-10)
        self.patteArD.Baisser_Tibia(15,-10)

        # self.pavg.throttle=-1
        # self.pmg.throttle=-1
        # self.parg.throttle=-1

        self.patteAvG.Baisser_Pointe(15,-100)
        self.patteMG.Baisser_Pointe(15,-100)
        self.patteArG.Baisser_Pointe(15,-100)

        while angles != self.gyro.get_angle():
            print("Angles de départ: ", angles, "\nAngles de maintenant : ",self.gyro.get_angle())
        #Maintiens
        # self.tavg.throttle=0.1
        # self.tmg.throttle=0.1
        # self.targ.throttle=0.1
        # self.tavd.throttle=-0.1
        # self.tmd.throttle=-0.1
        # self.tard.throttle=-0.1

        self.patteAvG.Tibia.StayWithForce("+")
        self.patteMG.Tibia.StayWithForce("+")
        self.patteArG.Tibia.StayWithForce("+")
        self.patteAvD.Tibia.StayWithForce("-")
        self.patteMD.Tibia.StayWithForce("-")
        self.patteArD.Tibia.StayWithForce("-")

        time.sleep(1)

        # #Etape 3 baisser les tibias Droite et mettre une légère force sur les pointes

        # time.sleep(0.003*50) #50 degrés vers le bas

        # self.tavd.throttle=-0.4
        # self.tmd.throttle=-0.4
        # self.tard.throttle=-0.4

        # self.tavg.throttle=0.3
        # self.tmg.throttle=0.3
        # self.targ.throttle=0.3

    def Avance(self):
        angles=self.gyro.get_angle()
        #Maintiens
        self.tavg.throttle=0.1
        self.tmg.throttle=0.2
        self.targ.throttle=0.2
        self.tavd.throttle=-0.1
        self.tmd.throttle=-0.1
        self.tard.throttle=-0.1

        #Lever la patte avant gauche

        self.tavg.throttle=-1
        self.pavg.throttle=1
        time.sleep(0.003*50) #50 degrés vers le haut
        self.tavg.throttle=0
        self.pavg.throttle=0

        self.havg.throttle=-1
        time.sleep(0.003*20) #20 degrés vers l'avant
        self.havg.throttle=0
        self.pavg.throttle=-1
        time.sleep(0.003*180) #50 degrés vers le bas
        self.pavg.throttle=-0.1

        self.tavg.throttle=1
        while angles["x"] < self.gyro.get_angle()["x"] and angles["y"] < self.gyro.get_angle()["y"]:
            print("Angle de départ: ", angles["x"], "\nAngles de maintenant : ",self.gyro.get_angle())
        self.tavg.throttle=0.1


    # def Init4(self):
    #     #Etape 1 baisser les tibias et légère force sur les pointes
    #     #Tibias Gauche

    #     self.tavg.throttle=0.7
    #     #Tibias Droite
    #     self.tavd.throttle=-1

    #     #Pointes
    #     self.pavg.throttle=-0.1
    #     self.pavd.throttle=0.1

    #     time.sleep(5) #50 degrés vers le bas




    #     #Maintiens
    #     self.tavg.throttle=0.1
    #     self.tavd.throttle=-0.1

    #     #Pointes
    #     self.parg.throttle=-0.1
    #     self.pard.throttle=0.1

    #     #Tibias Arrière
    #     self.targ.throttle=0.7
    #     self.tard.throttle=-1
    #     time.sleep(5)

    #     self.targ.throttle=0.1
    #     self.tard.throttle=-0.1

    #self.pcaD.deinit()
    #self.pcaG.deinit()