import sys


sys.path.append("../")

from Gyroscope import Gyroscope

test = Gyroscope()
# while True:
    # angle=test.get_angle()
    # if angle["x"]!=test.get_angle()["x"]:
        # print(angle["x"])
while True:
    
    gyro=test.get_angle()
    if gyro["z"]!=test.get_angle()["z"]:
        print(gyro["z"])
