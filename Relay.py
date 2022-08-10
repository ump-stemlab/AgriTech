import RPi.GPIO as GPIO
import asyncio
import vdata

GPIO.setmode(GPIO.BCM)

#relay 1
GPIO.setup (21, GPIO.OUT)

#relay 2
GPIO.setup (26, GPIO.OUT)

pump1 = 21
pump2 = 26

async def main_pump():
    while True:
        GPIO.output (pump1, GPIO.HIGH)
        print ("Turn on Pump")
        vdata.main_pump_state=1
        await asyncio.sleep(10)
        GPIO.output (pump1, GPIO.LOW)
        print ("Turn off Pump")
        vdata.main_pump_state=0
        await asyncio.sleep(10)
        
        
# async def pump_2():
#     while True:
#         GPIO.output (pump2, GPIO.HIGH)
#         print ("Turn on Pump 2")
#         await asyncio.sleep(5)
#         GPIO.output (pump2, GPIO.LOW)
#         print ("Turn off Pump 2")
#         await asyncio.sleep(5)

loop= asyncio.get_event_loop()


