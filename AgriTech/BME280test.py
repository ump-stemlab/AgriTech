import bme280
import smbus2
from time import sleep
import asyncio,vdata

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

async def checkTemp():
    while True:
        bme280_data = bme280.sample(bus,address)
        vdata.humidity  = bme280_data.humidity
        vdata.pressure  = bme280_data.pressure
        vdata.ambient_temperature = bme280_data.temperature
        #print(vdata.humidity, vdata.pressure, vdata.ambient_temperature)
        await asyncio.sleep(5)
    
loop= asyncio.get_event_loop()