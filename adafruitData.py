import asyncio
import time
import vdata

# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError


#Adafuit IO Username and Key
ADAFRUIT_IO_USERNAME = 'umpstemlab'
ADAFRUIT_IO_KEY = 'aio_zCup0319HtRZTly8U34SwC8oNNkD'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)



    
async def Send_data():
    while True:
        aio.send(vdata.temperature_feed.key, vdata.ambient_temperature)
        print('Temperature=\t' + str(vdata.ambient_temperature))
        aio.send(vdata.pressure_feed.key, int(vdata.pressure))
        print('Pressure=\t' + str(int(vdata.pressure)))
        aio.send(vdata.humidity_feed.key, int(vdata.humidity))
        print('Humidity=\t' + str(vdata.humidity))
        aio.send(vdata.flow_feed.key, int(vdata.flow))
        print('Flow=\t' + str(vdata.flow))
        aio.send(vdata.main_pump.key, int(vdata.main_pump_state))
        print('Main Pump=\t' + str(vdata.main_pump_state))
        print('Data sent')
        await asyncio.sleep(10)
        
loop= asyncio.get_event_loop()

