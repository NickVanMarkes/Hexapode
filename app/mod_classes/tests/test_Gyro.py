import sys


sys.path.append("../")

from Gyroscope import Gyroscope

test = Gyroscope()
# while True:
    # angle=test.get_angle()
    # if angle["x"]!=test.get_angle()["x"]:
        # print(angle["x"])
while True:
    
    accel=test.get_acceleration()
    if accel["y"]!=test.get_acceleration()["y"]:
        print(accel["y"])
