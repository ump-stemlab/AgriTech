import asyncio
import time
import vdata

# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError


#Adafuit IO Username and Key
ADAFRUIT_IO_USERNAME = 'umpstemlab'
ADAFRUIT_IO_KEY = 'aio_zCup0319HtRZTly8U34SwC8oNNkD'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    temperature_feed = aio.feeds('ambient')
    pressure_feed = aio.feeds('pressure')
    humidity_feed = aio.feeds('humidity')

except RequestError:
    temperature_feed = aio.create_feed(Feed(name='ambient'))
    pressure_feed = aio.create_feed(Feed(name='pressure'))
    humidity_feed = aio.create_feed(Feed(name='humidity'))


    
async def Send_data():
    while True:
        aio.send(temperature_feed.key, vdata.ambient_temperature)
        print('Temperature' + str(vdata.ambient_temperature))
        aio.send(pressure_feed.key, int(vdata.pressure))
        print('Pressure' + str(int(vdata.pressure)))
        aio.send(humidity_feed.key, int(vdata.humidity))
        print('Pressure' + str(vdata.humidity))
        print('Data sent')
        await asyncio.sleep(10)
        
loop= asyncio.get_event_loop()

