import RPi.GPIO as GPIO
import time
import serial
import sys


# Desired temp for Room 1
desiredTemp = sys.argv[1]

# Define the serial port and baud rate.
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

# Setup proper board type
GPIO.setmode(GPIO.BCM)


# ON OFF CONTROLS
# Air conditioning, heaters, and middle fan power

# Set the GPIO pin values
r1ac = 22
r1h1 = 23
r1h2 = 25
r2h1 = 5
r2h2 = 12
mfp = 17

# GPIO setup
GPIO.setup(r1ac, GPIO.OUT)
GPIO.setup(r1h1, GPIO.OUT)
GPIO.setup(r1h2, GPIO.OUT)
GPIO.setup(r2h1, GPIO.OUT)
GPIO.setup(r2h2, GPIO.OUT)
GPIO.setup(mfp, GPIO.OUT)



# SERVO CONTROL
# Windows and middle flap

# Set the GPIO pin values
r1w = 27
r2w = 4
mfs = 18

# Set the PWM frequency to 50 Hz
pwm_frequency = 50

# Set the duty cycle range (in percent) for the servo motor
duty_cycle_min = 2
duty_cycle_max = 12

# Setup the GPIO pin as a PWM output
GPIO.setup(r1w, GPIO.OUT)
GPIO.setup(r2w, GPIO.OUT)
GPIO.setup(mfs, GPIO.OUT)
r1wpwm = GPIO.PWM(r1w, pwm_frequency)
r2wpwm = GPIO.PWM(r2w, pwm_frequency)
mfspwm = GPIO.PWM(mfs, pwm_frequency)

# Start the PWM output with a 0% duty cycle
r1wpwm.start(0)
r2wpwm.start(0)
mfspwm.start(0)

# Function to set the servo position
def set_servo_position(pwm, angle):
    duty_cycle = ((angle / 180) * (duty_cycle_max - duty_cycle_min)) + duty_cycle_min
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    
while True:
    pass



# Cleanup the GPIO pins
r1wpwm.stop()
r2wpwm.stop()
mfspwm.stop()
GPIO.cleanup()