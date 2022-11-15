import asyncio
import time
import vdata

# import Adafruit IO REST client
from Adafruit_IO import Client, Feed, RequestError


#Adafuit IO Username and Key
ADAFRUIT_IO_USERNAME = 'umpstemlab'
ADAFRUIT_IO_KEY = 'aio_ljdE77FrzrvUQ7RxRnW9I7HTKoEI'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
data_send=15


    
async def Send_data():
    curr_pump_state=vdata.main_pump_state
    aio.send(vdata.main_pump.key, int(vdata.main_pump_state))
    while True:
        print('Temperature\t=' + str(vdata.ambient_temperature))
        print('Pressure\t=' + str(int(vdata.pressure)))
        print('Humidity\t=' + str(vdata.humidity))
        print('Pump Flowrate\t=' + str(vdata.pumpflow))
        print('Main Pump\t=' + str(vdata.main_pump_state))
        aio.send(vdata.temperature_feed.key, vdata.ambient_temperature)
        aio.send(vdata.pressure_feed.key, int(vdata.pressure))
        aio.send(vdata.humidity_feed.key, int(vdata.humidity))
        aio.send(vdata.flow_feed.key, int(vdata.pumpflow))
        print('Data sent')
        
        for x in range (0,data_send*2,1):
            if curr_pump_state != vdata.main_pump_state:
                curr_pump_state = vdata.main_pump_state
                aio.send(vdata.main_pump.key, int(vdata.main_pump_state))
                print("Pump set to " +str(vdata.main_pump_state))
            await asyncio.sleep(0.5)
            
loop= asyncio.get_event_loop()

