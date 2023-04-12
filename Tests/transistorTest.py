import RPi.GPIO as GPIO
import time
import sys

# Pin definition
controlPin = int(sys.argv[1])

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(controlPin, GPIO.OUT)

# Main program loop
while True:
    # Turn on the transistor (active high)
    GPIO.output(controlPin, GPIO.HIGH)
    # Wait for some time