import sys
import time

import keyboard
import RPi.GPIO as GPIO
import serial

# Desired temp for Room 1
# TODO this needs to be updated to include the website. These numbers will be coming from there now
desiredTemp = float(sys.argv[1])

# Define the serial port and baud rate for the arduino
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

# Setup proper board type
GPIO.setmode(GPIO.BCM)


# Set the GPIO pin values
# TODO
r1AcPin = 22
r2AcPin = 0
r3AcPin = 0
r4AcPin = 0
r1HeatPin = 23
r2HeatPin = 0
r3HeatPin = 0
r4HeatPin = 0

# GPIO setup
GPIO.setup(r1AcPin, GPIO.OUT)
GPIO.setup(r2AcPin, GPIO.OUT)
GPIO.setup(r3AcPin, GPIO.OUT)
GPIO.setup(r4AcPin, GPIO.OUT)
GPIO.setup(r1HeatPin, GPIO.OUT)
GPIO.setup(r2HeatPin, GPIO.OUT)
GPIO.setup(r3HeatPin, GPIO.OUT)
GPIO.setup(r4HeatPin, GPIO.OUT)


# SERVO CONTROL
# Windows and middle flap

# Set the GPIO pin values
# TODO
r1wPin = 27
r2wPin = 21
r3wPin = 0
r4wPin = 0
r12wPin = 0
r23wPin = 0
r34wPin = 0
r41wPin = 0

# Set the PWM frequency to 50 Hz
pwm_frequency = 50

# Set the duty cycle range (in percent) for the servo motor
duty_cycle_min = 2
duty_cycle_max = 12

# Setup the GPIO pin as a PWM output
GPIO.setup(r1wPin, GPIO.OUT)
GPIO.setup(r2wPin, GPIO.OUT)
GPIO.setup(r3wPin, GPIO.OUT)
GPIO.setup(r4wPin, GPIO.OUT)
GPIO.setup(r12wPin, GPIO.OUT)
GPIO.setup(r23wPin, GPIO.OUT)
GPIO.setup(r34wPin, GPIO.OUT)
GPIO.setup(r41wPin, GPIO.OUT)
r1wpwm = GPIO.PWM(r1wPin, pwm_frequency)
r2wpwm = GPIO.PWM(r2wPin, pwm_frequency)
r3wpwm = GPIO.PWM(r3wPin, pwm_frequency)
r4wpwm = GPIO.PWM(r4wPin, pwm_frequency)
r12wpwm = GPIO.PWM(r12wPin, pwm_frequency)
r23wpwm = GPIO.PWM(r23wPin, pwm_frequency)
r34wpwm = GPIO.PWM(r34wPin, pwm_frequency)
r41wpwm = GPIO.PWM(r41wPin, pwm_frequency)

# Start the PWM output with a 0% duty cycle
r1wpwm.start(0)
r2wpwm.start(0)
r3wpwm.start(0)
r4wpwm.start(0)
r12wpwm.start(0)
r23wpwm.start(0)
r34wpwm.start(0)
r41wpwm.start(0)


# Function to set the servo position
def set_servo_position(pwm, angle):
    duty_cycle = ((angle / 180) * (duty_cycle_max - duty_cycle_min)) + duty_cycle_min
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)


# Variables
# For state variables, True is open/on
r1w = False
r2w = False
r3w = False
r4w = False
# Interior windows connecting rooms
r12w = False
r23w = False
r34w = False
r41w = False
# Interior fans (True is counter-clockwise, False is clockwise)
r12Fan = False
r23Fan = False
r34Fan = False
r41Fan = False
# Room heaters
r1Heat = False
r2Heat = False
r3Heat = False
r4Heat = False
# Room air conditioning
r1Ac = False
r2Ac = False
r3Ac = False
r4Ac = False


stop_loop = False

# This is here to grab and dump the first set of date
# In testing, sometimes this data was causing errors
try:
    data = ser.readline().decode("utf-8").rstrip()
except UnicodeDecodeError as e:
    pass

while not stop_loop:
    # TODO acCheck = int(acVar.get())
    # TODO heatCheck = int(heatVar.get())
    # TODO room = int(roomSelect.get())
    # TODO DesiredTemp = int(desiredTemp.get())
    Room1Temp = 999
    Room2Temp = 999
    Room3Temp = 999
    Room4Temp = 999
    OutsideTemp = 999
    # Exterior windows
    r1w = False
    r2w = False
    r3w = False
    r4w = False
    # Interior windows connecting rooms
    r12w = False
    r23w = False
    r34w = False
    r41w = False
    # Interior fans (True is counter-clockwise, False is clockwise)
    r12Fan = False
    r23Fan = False
    r34Fan = False
    r41Fan = False
    # Room heaters
    r1Heat = False
    r2Heat = False
    r3Heat = False
    r4Heat = False
    # Room air conditioning
    r1Ac = False
    r2Ac = False
    r3Ac = False
    r4Ac = False

    try:
        data = ser.readline().decode("utf-8").rstrip()
        values = data.split(",")
        # Arduino Order: Room1Temp, Room2Temp, Room3Temp, Room4Temp
        Room1Temp = float(values[0])
        Room2Temp = float(values[1])
        Room3Temp = float(values[2])
        Room4Temp = float(values[3])
        OutsideTemp = float(values[4])

    except UnicodeDecodeError as e:
        pass

    if room == 1:
        # Heater
        if heatCheck and Room1Temp < DesiredTemp:
            r1Heat = True
        # Interior Window Forward
        if (Room2Temp > Room1Temp and Room1Temp < DesiredTemp) or (
            Room2Temp < Room1Temp and Room1Temp > DesiredTemp
        ):
            r12w = True
            r12Fan = False
        # Interior Window Backward
        if (Room4Temp > Room1Temp and Room1Temp < DesiredTemp) or (
            Room4Temp < Room1Temp and Room1Temp > DesiredTemp
        ):
            r41w = True
            r41Fan = True
        # AC
        if acCheck and Room1Temp > DesiredTemp:
            r1Ac = True
        # Outside Windows Cooling
        if OutsideTemp < Room1Temp and Room1Temp > DesiredTemp:
            r1w = True
        # Outside Windows Heating
        if OutsideTemp > Room1Temp and Room1Temp < DesiredTemp:
            r1w = True

    elif room == 2:
        # Heater
        if heatCheck and Room2Temp < DesiredTemp:
            r2Heat = True
        # Interior Window Froward
        if (Room3Temp > Room2Temp and Room2Temp < DesiredTemp) or (
            Room3Temp < Room2Temp and Room2Temp > DesiredTemp
        ):
            r23w = True
            r23Fan = False
        # Interior Window Backward
        if (Room1Temp > Room2Temp and Room2Temp < DesiredTemp) or (
            Room1Temp < Room2Temp and Room2Temp > DesiredTemp
        ):
            r12w = True
            r12Fan = True
        # AC
        if acCheck and Room2Temp > DesiredTemp:
            r2Ac = True
        # Outside Windows Cooling
        if OutsideTemp < Room2Temp and Room2Temp > DesiredTemp:
            r2w = True
        # Outside Windows Heating
        if OutsideTemp > Room2Temp and Room2Temp < DesiredTemp:
            r2w = True

    elif room == 3:
        # Heater
        if heatCheck and Room3Temp < DesiredTemp:
            r3Heat = True
        # Interior Window Forward
        if (Room4Temp > Room3Temp and Room3Temp < DesiredTemp) or (
            Room4Temp < Room3Temp and Room3Temp > DesiredTemp
        ):
            r34w = True
            r34Fan = False
        # Interior Window Backward
        if (Room2Temp > Room3Temp and Room3Temp < DesiredTemp) or (
            Room2Temp < Room3Temp and Room3Temp > DesiredTemp
        ):
            r23w = True
            r23Fan = True
        # AC
        if acCheck and Room3Temp > DesiredTemp:
            r3Ac = True
        # Outside Windows Cooling
        if OutsideTemp < Room3Temp and Room3Temp > DesiredTemp:
            r3w = True
        # Outside Windows Heating
        if OutsideTemp > Room3Temp and Room3Temp < DesiredTemp:
            r3w = True

    elif room == 4:
        # Heater
        if heatCheck and Room4Temp < DesiredTemp:
            r4Heat = True
        # Interior Window Forward
        if (Room1Temp > Room4Temp and Room4Temp < DesiredTemp) or (
            Room1Temp < Room4Temp and Room4Temp > DesiredTemp
        ):
            r41w = True
            r41Fan = False
        # Interior Window Backward
        if (Room3Temp > Room4Temp and Room4Temp < DesiredTemp) or (
            Room3Temp < Room4Temp and Room4Temp > DesiredTemp
        ):
            r34w = True
            r34Fan = True
        # AC
        if acCheck and Room4Temp > DesiredTemp:
            r4Ac = True
        # Outside Windows Cooling
        if OutsideTemp < Room4Temp and Room4Temp > DesiredTemp:
            r4w = True
        # Outside Windows Heating
        if OutsideTemp > Room4Temp and Room4Temp < DesiredTemp:
            r4w = True

    # Servos for exterior windows
    if r1w:
        set_servo_position(r1wpwm, 180)
    else:
        set_servo_position(r1wpwm, 0)
    if r2w:
        set_servo_position(r2wpwm, 180)
    else:
        set_servo_position(r2wpwm, 0)
    if r3w:
        set_servo_position(r3wpwm, 180)
    else:
        set_servo_position(r3wpwm, 0)
    if r4w:
        set_servo_position(r4wpwm, 180)
    else:
        set_servo_position(r4wpwm, 0)

    # Servos for interior windows
    if r12w:
        set_servo_position(r12wpwm, 180)
        # TODO Turn on fan and control direction
    else:
        set_servo_position(r12wpwm, 0)
        # TODO turn off fan
    if r23w:
        set_servo_position(r23wpwm, 180)
    else:
        set_servo_position(r23wpwm, 0)
    if r34w:
        set_servo_position(r34wpwm, 180)
    else:
        set_servo_position(r34wpwm, 0)
    if r41w:
        set_servo_position(r41wpwm, 180)
    else:
        set_servo_position(r41wpwm, 0)

    # Air Conditioning
    if r1Ac:
        GPIO.output(r1AcPin, 1)
    else:
        GPIO.output(r1AcPin, 0)
    if r2Ac:
        GPIO.output(r2AcPin, 1)
    else:
        GPIO.output(r2AcPin, 0)
    if r3Ac:
        GPIO.output(r3AcPin, 1)
    else:
        GPIO.output(r3AcPin, 0)
    if r4Ac:
        GPIO.output(r4AcPin, 1)
    else:
        GPIO.output(r4AcPin, 0)

    # Heating
    if r1Heat:
        GPIO.output(r1HeatPin, 1)
    else:
        GPIO.output(r1HeatPin, 0)
    if r2Heat:
        GPIO.output(r2HeatPin, 1)
    else:
        GPIO.output(r2HeatPin, 0)
    if r3Heat:
        GPIO.output(r3HeatPin, 1)
    else:
        GPIO.output(r3HeatPin, 0)
    if r4Heat:
        GPIO.output(r4HeatPin, 1)
    else:
        GPIO.output(r4HeatPin, 0)

    time.sleep(1)


# Cleanup the GPIO pins
r1wpwm.stop()
r2wpwm.stop()
r3wpwm.stop()
r4wpwm.stop()
r12wpwm.stop()
r23wpwm.stop()
r34wpwm.stop()
r41wpwm.stop()
GPIO.cleanup()
ser.close()
