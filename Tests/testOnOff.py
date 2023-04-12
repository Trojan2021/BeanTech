import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

entered = 1

# Set the GPIO pin to use
pin1 = int(sys.argv[1])
pin2 = int(sys.argv[2])
pin3 = int(sys.argv[3])

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)


GPIO.output(pin1, entered)
GPIO.output(pin2, entered)
GPIO.output(pin3, entered)

time.sleep(6000)

GPIO.cleanup()