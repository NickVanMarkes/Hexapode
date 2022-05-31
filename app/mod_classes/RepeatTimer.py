### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : app/mod_classes/RepeatTimer.py
### Date        : 03/05/2022
### Description : Classe qui permet de faire des répétitions de fonction en multithreading.

from threading import Timer

class RepeatTimer(Timer):
    def run(self):
        """  brief: fonction qui permet de faire du mutlithreading avec un Timer.
             
             parameters  :
                 None
             
             returns :
                None
        """
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)