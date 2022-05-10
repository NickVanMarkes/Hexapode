### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : app/mod_classes/Patte.py
### Date        : 06/05/2022
### Description : Classe qui contrôle les pattes de l'hexapode.

from Motor import ServoMoteur

class Patte(object):

    def __init__ (self,Cote,Position) -> None:
        """  brief       : Constructeur de la classe
                 param-type  : Cote (str)
                               Position (str)
                 return-type : type 
        """ 
        if Cote=="Gauche":
            if Position=="Avant":
                self.Pointe=ServoMoteur(Cote,2)
                self.Tibia=ServoMoteur(Cote,1)
                self.Hanche=ServoMoteur(Cote,0)
            elif Position=="Milieu":
                self.Pointe=ServoMoteur(Cote,4)
                self.Tibia=ServoMoteur(Cote,5)
                self.Hanche=ServoMoteur(Cote,6)
            elif Position=="Arriere":
                self.Pointe=ServoMoteur(Cote,15)
                self.Tibia=ServoMoteur(Cote,13)
                self.Hanche=ServoMoteur(Cote,12)
        elif Cote=="Droite":
            if Position=="Avant":
                self.Pointe=ServoMoteur(Cote,15)
                self.Tibia=ServoMoteur(Cote,14)
                self.Hanche=ServoMoteur(Cote,13)
            elif Position=="Milieu":
                self.Pointe=ServoMoteur(Cote,4)
                self.Tibia=ServoMoteur(Cote,5)
                self.Hanche=ServoMoteur(Cote,6)
            elif Position=="Arriere":
                self.Pointe=ServoMoteur(Cote,0)
                self.Tibia=ServoMoteur(Cote,1)
                self.Hanche=ServoMoteur(Cote,2)
        self.servos=[self.Pointe,self.Tibia,self.Hanche]

    def Lever_Pointe (self,Angle, Force) -> None:
        """  brief       : Lève la pointe de la patte
             param-type  : Angle (int)
                           Force (int) Pourcentage
             return-type : None 
        """ 
        self.Pointe.SetAngleRel(Angle,Force)
        if Force<0:
            self.Pointe.StayWithForce("-")
        else:
            self.Pointe.StayWithForce("+")

    def Lever_Tibia (self,Angle, Force) -> None:
        """  brief       :  Lève le tibia de la patte
             param-type  :  Angle (int)
                            Force (int) Pourcentage
             return-type :  None
        """
        self.Tibia.SetAngleRel(Angle,Force)
        if Force<0:
            self.Tibia.StayWithForce("-")
        else:
            self.Tibia.StayWithForce("+")

    def Baisser_Pointe (self,Angle,Force) -> None:
        """  brief       : Baisse la pointe de la patte
             param-type  : Angle (int)
                            Force (int) Pourcentage
             return-type : None
        """
        self.Pointe.SetAngleRel(Angle,Force)
        if Force<0:
            self.Pointe.StayWithForce("-")
        else:
            self.Pointe.StayWithForce("+")

    def Baisser_Tibia (self,Angle, Force) -> None:
        """  brief       : Baisse le tibia de la patte
                param-type  : Angle (int)
                                Force (int) Pourcentage
                return-type : None
        """
        self.Tibia.SetAngleRel(Angle,Force)
        if Force<0:
            self.Tibia.StayWithForce("-")
        else:
            self.Tibia.StayWithForce("+")

    def Tourner (self,Angle, Force) -> None:
        """  brief       : Tourne la patte
             param-type  : Angle (int)
                            Force (int) Pourcentage
             return-type : None
        """
        self.Hanche.SetAngleRel(Angle,Force)
        if Force<0:
            self.Hanche.StayWithForce("-")
        else:
            self.Hanche.StayWithForce("+")
    def WithoutForce(self) -> None:
        """  brief       : Désactive les moteurs
             param-type  : None
             return-type : None
        """
        self.Pointe.WithoutForce()
        self.Tibia.WithoutForce()
        self.Hanche.WithoutForce()

