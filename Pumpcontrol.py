
import RPi.GPIO as GPIO
import time

GPIO.cleanup

in1 = 24
in2 = 23
enA = 25
in3 = 14 
in4 = 15
enB = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.HIGH)

pA= GPIO.PWM(enA, 500)
pB= GPIO.PWM(enB, 500)
pA.start(0)
pB.start(0)

while True:
# initial value to final value, with increment of 5
    for dc in range(0, 101, 10):
        pA.ChangeDutyCycle(dc)
        pB.ChangeDutyCycle(dc)
        time.sleep(5)
    
    for dc in range (100, -1, -10):
        pA.ChangeDutyCycle(dc)
        pB.ChangeDutyCycle(dc)
        time.sleep(5)

