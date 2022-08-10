import asyncio
import time
import vdata

# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError

# loop timeout, in seconds.
LOOP_DELAY = 10

#Adafuit IO Username and Key
ADAFRUIT_IO_USERNAME = 'umpstemlab'
ADAFRUIT_IO_KEY = 'Yaio_zCup0319HtRZTly8U34SwC8oNNkD'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    temperature_feed = aio.feeds('Ambient_temp')
    pressure_feed = aio.feeds('Air_pressure')
    humidity_feed = aio.feeds('humidity')

except RequestError:
    temperature_feed = aio.create_feed(Feed(name='Ambient_temp'))
    pressure_feed = aio.create_feed(Feed(name='Air_pressure'))
    humidity_feed = aio.create_feed(Feed(name='humidity'))

time.sleep(1)

async def Send_data():
    while True:
        aio.send(temperature_feed.key, vdata.ambient_temperature)
        aio.send(pressure_feed.key, int(vdata.pressure))
        aio.send(humidity_feed.key, int(vdata.humidity))
        await asyncio.wait(30)

