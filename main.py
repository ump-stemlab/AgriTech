import asyncio
from time import sleep
import asynccontrol


try:
    asyncio.ensure_future(asynccontrol.pumpcontrol())
    asynccontrol.loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    asynccontrol.loop.close()

while 1:
    print("Test print")
    sleep(2)