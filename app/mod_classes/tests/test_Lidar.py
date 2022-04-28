import sys
from syncer import sync
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial

sys.path.append("../")

from Lidarv2async import Lidarasync

lidar=Lidarasync()
lidar2=Lidarasync()

print("Est-ce la même instance? ",lidar is lidar2)
result=[]
#print("Sans thread")
##Scan réussi
#lidar.DoScan()
#
#result=lidar.Get_Data()
#print(len(result))
#
#print(lidar.shorterScan)
#
#time.sleep(5)

# def synchronize_async_helper(to_await):
#     async_response = []

#     async def run_and_capture_result():
#         r = await to_await
#         async_response.append(r)

#     loop = asyncio.get_event_loop()
#     coroutine = run_and_capture_result()
#     loop.run_until_complete(coroutine)
#     return async_response[0]

# result = synchronize_async_helper(lidar.Get_Data())
print("==========================================================")
print("Avec thread")
lidar.scans=[]
#thread=threading.Thread(target=lidar.DoScan)
#thread.start()
#thread.join()
thread=threading.Timer(1,lidar.DoScan)
#thread = threading.Thread(target=lidar.DoScan)
thread.start()
#thread.run()
while len(result)<16:
    
    if(result!=lidar.Get_Data()):
        #print(lidar.Get_Data())
        result=lidar.Get_Data().copy()
    print("Éléments dans les scans: ",len(result))
    time.sleep(0.3)

for scan in result:
    print(scan, "\n")



#thread.cancel()
if result is []:
    print("No data")