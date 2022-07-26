import asyncio
from time import sleep
import asynccontrol
import flowmeter


try:
    asyncio.ensure_future(asynccontrol.pumpcontrol())
    #asyncio.ensure_future(flowmeter.flowcount()) #Flow meter measurement
    asynccontrol.loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    asynccontrol.loop.close()
    
    #test again again
    #test test