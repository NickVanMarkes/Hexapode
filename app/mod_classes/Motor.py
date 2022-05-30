### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : Hexapode/app/mod_classes/Motor.py
### Date        : 08/04/2022
### Description : Classe qui permet de contrôler les servomoteur du robot hexapode.

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

from board import SCL, SDA
import busio
import time

class ServoMotor(object):

    FREQUENCY = 50
    MINPULSE=1300
    MAXPULSE=1890
    def __init__(self,Channel="Gauche",Position=0) -> None:
        """  brief       : Initialisation du module servomoteur
                parameters  : Channel (str)
                              position (int)
                returns : None
        """
        i2c = busio.I2C(SCL, SDA)
        # Création des instances des différents modules PCA9685
        self.pcaG = PCA9685(i2c, address=65)
        self.pcaD = PCA9685(i2c, address=66)
        self.pcaG.frequency = self.FREQUENCY
        self.pcaD.frequency = self.FREQUENCY
        
        if Channel=="Gauche":
            self.servo=servo.ContinuousServo(self.pcaG.channels[Position], min_pulse=self.MINPULSE, max_pulse=self.MAXPULSE)
        elif Channel=="Droite":
            self.servo=servo.ContinuousServo(self.pcaD.channels[Position], min_pulse=self.MINPULSE, max_pulse=self.MAXPULSE)
    
    
    def SetAngleRel(self,Angle,Force) -> None:
        """  brief       : Permet de définir l'angle du servomoteur, la force est en pourcentage
                parameters  : Angle (int)
                              Force (int)
                returns : None
        """

        self.servo.throttle = Force/100
        time.sleep(0.003*abs(Angle))
    
    def StayWithForce(self,direction="+") -> None:
        """  brief       : Permet de garder le servomoteur avec un peu de force vers le sol
                parameters  : direction (str)
                returns : None
        """
        if direction=="+":
            self.servo.throttle=0.1
        elif direction=="-":
            self.servo.throttle=-0.1
    def WithoutForce(self) -> None:
        """  brief       : Permet de garder le servomoteur sans force
                parameters  : None
                returns : None
        """
        self.servo.throttle=0

#Usage:
#import Motor
#moteur=Motor.ServoMoteur("Gauche",0)
#moteur.set_angle_rel(90,50)
#moteur.stay_with_force(-)

