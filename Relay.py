import RPi.GPIO as GPIO
import asyncio

GPIO.setmode(GPIO.BCM)

#relay 1
GPIO.setup (21, GPIO.OUT)

#relay 2
GPIO.setup (26, GPIO.OUT)

pump1 = 21
pump2 = 26

async def pump_1():
    while True:
        GPIO.output (pump1, GPIO.HIGH)
        print ("Turn on Pump")
        await asyncio.sleep(10)
        GPIO.output (pump1, GPIO.LOW)
        print ("Turn off Pump")
        await asyncio.sleep(10)
        
        
async def pump_2():
    while True:
        GPIO.output (pump2, GPIO.HIGH)
        print ("Turn on Pump 2")
        await asyncio.sleep(5)
        GPIO.output (pump2, GPIO.LOW)
        print ("Turn off Pump 2")
        await asyncio.sleep(5)

async def main():
    task1 = asyncio.create_task(pump_1())
    task2 = asyncio.create_task(pump_2())
    await task2
    loop = asyncio.get_event_loop()
    
asyncio.run(main())
GPIO.cleanup()


