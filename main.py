import asyncio
from time import sleep
import asynccontrol


try:
    asyncio.ensure_future(asynccontrol.pumpcontrol())
    asyncio.ensure_future(asynccontrol.pumpcontrol2())
    asynccontrol.loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    asynccontrol.loop.close()

#Tunjuk Zul