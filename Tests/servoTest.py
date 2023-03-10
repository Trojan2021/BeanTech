import RPi.GPIO as GPIO

import time
import sys

GPIO.setmode(GPIO.BCM)

# pos = sys.argv[2]

# Set the GPIO pin to use for the servo
servo_pin = int(sys.argv[1])

# Set the PWM frequency to 50 Hz
pwm_frequency = 50

# Set the duty cycle range (in percent) for the servo motor
duty_cycle_min = 2
duty_cycle_max = 12

# Setup the GPIO pin as a PWM output
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, pwm_frequency)

# Start the PWM output with a 0% duty cycle
pwm.start(0)

# Define a function to set the servo position
def set_servo_position(angle):
    duty_cycle = ((angle / 180) * (duty_cycle_max - duty_cycle_min)) + duty_cycle_min
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

# Set the servo position to 0 degrees (minimum position)
set_servo_position(180)
time.sleep(2)
set_servo_position(0)
time.sleep(2)


# Cleanup the GPIO pins
pwm.stop()
GPIO.cleanup()
