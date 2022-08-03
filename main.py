import asyncio
from time import sleep
import asynccontrol
import flowmeter
import Relay
import Pumpcontrol

GPIO.setwarnings(False)			#disable warnings

try:
    asyncio.ensure_future(flowmeter.flowcount()) #Flow meter measurement
    asyncio.ensure_future(Relay.main_pump()) #Pump timer control
    asyncio.ensure_future(Pumpcontrol.pump_1())
    asynccontrol.loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    asynccontrol.loop.close()
