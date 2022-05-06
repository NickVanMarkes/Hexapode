### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : app/mod_classes/Patte.py
### Date        : 06/05/2022
### Description : Classe qui contrôle les pattes de l'hexapode.

from mod_classes.Motor import ServoMoteur

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

    def Lever_Pointe (self,Angle, Force) -> None:
        """  brief       : Lève la pointe de la patte
             param-type  : Angle (int)
                           Force (int) Pourcentage
             return-type : None 
        """ 
        self.Pointe.set_angle_rel(Angle,Force)

    def Lever_Tibia (self,Angle, Force) -> None:
        """  brief       :  Lève le tibia de la patte
             param-type  :  Angle (int)
                            Force (int) Pourcentage
             return-type :  None
        """
        self.Tibia.set_angle_rel(Angle,Force)
        if Force<0:
            self.Tibia.stay_with_force("-")
        else:
            self.Tibia.stay_with_force("+")

    def Baisser_Pointe (self,Angle,Force) -> None:
        """  brief       : Baisse la pointe de la patte
             param-type  : Angle (int)
                            Force (int) Pourcentage
             return-type : None
        """
        #Faire animation pour baisser la pointe

    def Baisser_Tibia (self,Angle, Force) -> None:
        """  brief       : Baisse le tibia de la patte
                param-type  : Angle (int)
                                Force (int) Pourcentage
                return-type : None
        """
        #Faire animation pour baisser le tibia

    def Tourner (self,Angle, Force) -> None:
        """  brief       : Tourne la patte
             param-type  : Angle (int)
                            Force (int) Pourcentage
             return-type : None
        """
        #Faire animation pour tourner la patte

