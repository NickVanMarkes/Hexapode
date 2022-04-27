import sys
from syncer import sync
import asyncio
from concurrent.futures import ThreadPoolExecutor

sys.path.append("../")

from Lidarv2async import Lidarasync

lidar=Lidarasync()

#Scan réussi
lidar.DoScan()
scans=[]



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
result = asyncio.gather(lidar.Get_Data())

print(result)

print(lidar.shorterScan)


if scans is None:
    print("No data")

