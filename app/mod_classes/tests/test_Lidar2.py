import sys
import time
import asyncio


sys.path.append("../")

from Lidarv2async import Lidarasync

lidar=Lidarasync()
lidar.scans=[]
#lidar.DoScan()

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    task3 = asyncio.create_task(lidar.DoScan())

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    await task3

    print(f"finished at {time.strftime('%X')}")
    print(task3)

asyncio.run(main())