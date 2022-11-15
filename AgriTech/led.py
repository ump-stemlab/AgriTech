import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

G=17

GPIO.setup(G,GPIO.OUT)

GPIO.output(G,GPIO.LOW)
time.sleep(1)