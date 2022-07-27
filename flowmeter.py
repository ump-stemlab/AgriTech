import asyncio
import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR_GPIO = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count, start_counter
count = 0

def countPulse(channel):
   global count, start_counter
   if start_counter == 1:
      count = count+1


GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)

async def flowcount():
    global count, start_counter
    while True:
        start_counter = 1
        await asyncio.sleep(1)
        start_counter = 0
        flow = (count / 7.5) # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
        print("The flow is: %.3f Liter/min" % (flow))
        #publish.single("/Garden.Pi/WaterFlow", flow, hostname=MQTT_SERVER)
        count = 0
        await asyncio.sleep(5)


loop= asyncio.get_event_loop()