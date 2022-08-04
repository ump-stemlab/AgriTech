import asyncio
from time import sleep
import flowmeter
import BME280test


try:
#     asyncio.ensure_future(flowmeter.flowcount()) #Flow meter measurement
    asyncio.ensure_future(BME280test.checkTemp())
#     flowmeter.loop.run_forever()
    BME280test.loop.run_forever()

    

except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    BME280test.loop.close()
    