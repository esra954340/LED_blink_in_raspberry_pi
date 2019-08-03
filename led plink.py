import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

while True:
    GPIO.setup(3,GPIO.HIGH)
    GPIO.setup(22,GPIO.LOW)
    time.sleep(1)
    print(" red led on")
    GPIO.setup(3,GPIO.LOW)
    GPIO.setup(22,GPIO.HIGH)
    print("red led off")
    time.sleep(1)
     
