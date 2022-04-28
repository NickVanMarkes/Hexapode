import sys
import time
import asyncio
import threading


sys.path.append("../")

from Lidarv2async import Lidarasync

lidar=Lidarasync()
lidar.scans=[]
#lidar.DoScan()

#thread = threading.Thread(target=lidar.DoScan)
#thread.start()

async def main():
    array=[]
    array.append(lidar.DoScan())
    print("".join(await asyncio.gather(*array)))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


#result = asyncio.gather(lidar.DoScan())