import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

entered = sys.argv[1]

# Set the GPIO pin to use
pin1 = 23
pin2 = 25
pin3 = 13
pin4 = 19

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

GPIO.output(pin1, int(entered))
GPIO.output(pin2, int(entered))
GPIO.output(pin3, int(entered))
GPIO.output(pin4, int(entered))

time.sleep(2000)

GPIO.cleanup()