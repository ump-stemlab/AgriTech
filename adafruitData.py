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
    flow_feed=aio.feeds('flow-rate')
    main_pump=aio.feeds('main-pump-state')

except RequestError:
    temperature_feed = aio.create_feed(Feed(name='ambient'))
    pressure_feed = aio.create_feed(Feed(name='pressure'))
    humidity_feed = aio.create_feed(Feed(name='humidity'))
    flow_feed = aio.create_feed(Feed(name='flow-rate'))
    main_pump = aio.create_feed(Feed(name='main-pump-state'))


    
async def Send_data():
    while True:
        aio.send(temperature_feed.key, vdata.ambient_temperature)
        print('Temperature=\t' + str(vdata.ambient_temperature))
        aio.send(pressure_feed.key, int(vdata.pressure))
        print('Pressure=\t' + str(int(vdata.pressure)))
        aio.send(humidity_feed.key, int(vdata.humidity))
        print('Humidity=\t' + str(vdata.humidity))
        aio.send(flow_feed.key, int(vdata.flow))
        print('Flow=\t' + str(vdata.flow))
        aio.send(main_pump.key, int(vdata.main_pump_state))
        print('Main Pump=\t' + str(vdata.main_pump_state))
        print('Data sent')
        await asyncio.sleep(10)
        
loop= asyncio.get_event_loop()

