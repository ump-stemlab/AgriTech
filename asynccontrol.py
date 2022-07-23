import asyncio

async def pumpcontrol():
    while True:
        print ("Turn on Pump")
        await asyncio.sleep(3)
        print ("Turn off Pump")
        await asyncio.sleep(3)

loop= asyncio.get_event_loop()