import asyncio

async def pumpcontrol():
    while True:
        print ("Turn on Pump")
        await asyncio.sleep(3)
        print ("Turn off Pump")
        await asyncio.sleep(3)

async def pumpcontrol2():
    while True:
        print ("Turn on Pump 2")
        await asyncio.sleep(4)
        print ("Turn off Pump 2")
        await asyncio.sleep(4)

loop= asyncio.get_event_loop()