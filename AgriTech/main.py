import asyncio
from time import sleep
import flowmeter
import BME280test
import adafruitData
import Relay


try:
    asyncio.ensure_future(flowmeter.flowcount()) #Flow meter measurement
    asyncio.ensure_future(BME280test.checkTemp())
    asyncio.ensure_future(adafruitData.Send_data())
    asyncio.ensure_future(Relay.main_pump())
    flowmeter.loop.run_forever()
    BME280test.loop.run_forever()
    adafruitData.loop.run_forever()
    Relay.loop.run_forever()
    

except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    flowmeter.loop.close()
    BME280test.loop.close()
    adafruitData.loop.close()
    Relay.loop.close()
    