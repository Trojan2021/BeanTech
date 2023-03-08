import RPi.GPIO as GPIO
import time

# Pin definition
controlPin = 17

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(controlPin, GPIO.OUT)

# Main program loop
while True:
    # Turn on the transistor (active high)
    GPIO.output(controlPin, GPIO.HIGH)
    # Wait for some time
    time.sleep(5)
    # Turn off the transistor
    GPIO.output(controlPin, GPIO.LOW)
    # Wait for some time
    time.sleep(5)