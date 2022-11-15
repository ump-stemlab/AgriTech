from Adafruit_IO import Client, Feed, RequestError

global humidity, pressure, ambient_temperature,flow,main_pump_state,pumpflow

ADAFRUIT_IO_USERNAME = 'umpstemlab'
ADAFRUIT_IO_KEY = 'aio_ljdE77FrzrvUQ7RxRnW9I7HTKoEI'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    temperature_feed = aio.feeds('ambient')

except RequestError:
    temperature_feed = aio.create_feed(Feed(name='ambient'))
    
try:
    pressure_feed = aio.feeds('pressure')
    
except RequestError:
    pressure_feed = aio.create_feed(Feed(name='pressure'))
    
try:
    humidity_feed = aio.feeds('humidity')
    
except RequestError:
    humidity_feed = aio.create_feed(Feed(name='humidity'))

try:
    flow_feed=aio.feeds('flow-rate')
    
except RequestError:
    flow_feed = aio.create_feed(Feed(name='flow-rate'))

try:
    main_pump=aio.feeds('main-pump-state')
    
except RequestError:
    main_pump = aio.create_feed(Feed(name='main-pump-state'))