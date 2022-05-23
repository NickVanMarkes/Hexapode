## PROGRAMME DE TEST POUR LE PLOT
import time
Begin=time.time()
from Plot import Radar
End=time.time()
retradar=Radar()

totalTime=End-Begin
print("Time import Radar at testplot.py: ")
print(totalTime)

Begin=0
End=0
Begin=time.time()
for i in range(10):
    test=retradar.CreatePlot()
End=time.time()
print("Time to make 10 plots")
print(End-Begin)

