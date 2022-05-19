### Author      : Nicolas Oliveira
### Project     : The Big Bug
### File        : app/mod_classes/RepeatTimer.py
### Date        : 03/05/2022
### Description : Classe qui permet de faire des répétitions de fonction en multithreading.

from threading import Timer

class RepeatTimer(Timer):
    def run(self):
        
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)