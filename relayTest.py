import RPi.GPIO as GPIO
import time

pin_number = 17

# Set the mode of the GPIO library to BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin as an output
GPIO.setup(pin_number, GPIO.OUT)

count = 0

while count < 5:
    # Set the state of the GPIO pin to HIGH
    GPIO.output(pin_number, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin_number, GPIO.HIGH)
    time.sleep(0.5)
    count += 1
    
GPIO.cleanup()
    
    
