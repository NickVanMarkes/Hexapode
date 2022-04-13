### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : Hexapode/app/mod_classes/Gyroscope.py
### Date        : 08/04/2022
### Description : Classe qui permet de récupérer les données du gyroscope, et qui les retournes si besoin.

from mpu6050 import mpu6050

class Gyroscope(object):
    def __init__ (self) -> None:
        """  brief       : Initialisation du module gyroscope
             param-type  : None
             return-type : None 
        """ 
        self.sensor=mpu6050(0x68)

    def get_angle(self) -> dict[str, float]:
        """  brief       : Permet de récupérer les angles du robot
             param-type  : None
             return-type : int 
        """ 
         
        return self.sensor.get_gyro_data()
    
    def get_acceleration (self) -> dict[str, float]:
        """  brief       : Permet de récupérer les accélérations du robot
              param-type  : type
              return-type : type 
        """
        return self.sensor.get_accel_data()