## PROGRAMME DE TEST POUR LE PLOT
import time
Begin=time.time()
from Plot import Radar
End=time.time()
retradar=Radar()

totalTime=End-Begin
print("Time import Radar at testplot.py: ")
print(totalTime)
test=retradar.CreatePlot()