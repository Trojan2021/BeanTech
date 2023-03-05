import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

entered = 1

# Set the GPIO pin to use
pin1 = int(sys.argv[1])

GPIO.setup(pin1, GPIO.OUT)


GPIO.output(pin1, entered)

time.sleep(3)

GPIO.cleanup()