import json
import time

import requests
import RPi.GPIO as GPIO
import serial
from adafruit_servokit import ServoKit

# Amount of servos
servoCount = 12

# Define the servo controller
pca = ServoKit(channels=16)

# Make each of the servos
for i in range(servoCount):
    pca.servo[i].set_pulse_width_range(500, 2500)


# Define the serial port and baud rate for the arduino
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

# Setup proper board type
GPIO.setmode(GPIO.BCM)


# Set the GPIO pin values
AcPin = 5
r1HeatPin = 17
r2HeatPin = 27
r3HeatPin = 22

# GPIO setup
GPIO.setup(AcPin, GPIO.OUT)
GPIO.setup(r1HeatPin, GPIO.OUT)
GPIO.setup(r2HeatPin, GPIO.OUT)
GPIO.setup(r3HeatPin, GPIO.OUT)


# Set the GPIO pin values for interior
r12fPin = 18
r23fPin = 23
r34fPin = 24
r41fPin = 25


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
# Room air conditioning
Ac = False


stop_loop = False

# This is here to grab and dump the first set of date
# In testing, sometimes this data was causing errors
try:
    data = ser.readline().decode("utf-8").rstrip()
except UnicodeDecodeError:
    pass

while not stop_loop:
    acResponse = requests.get("http://localhost:5000/acOnOff")
    acOnOff = acResponse.text
    acCheck = int(acOnOff)

    heatResponse = requests.get("http://localhost:5000/heatOnOff")
    heatOnOff = heatResponse.text
    heatCheck = int(heatOnOff)

    inputResponse = requests.get("http://localhost:5000/input")
    li = json.loads(inputResponse.text)
    room = int(li[1])
    DesiredTemp = int(li[0])

    Room1Temp = float("inf")
    Room2Temp = float("inf")
    Room3Temp = float("inf")
    Room4Temp = float("inf")
    OutsideTemp = float("inf")

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
    # Room air conditioning
    Ac = False

    try:
        data = ser.readline().decode("utf-8").rstrip()
        values = data.split(",")
        # Arduino Order: Room1Temp, Room2Temp, Room3Temp, Room4Temp
        Room1Temp = float(values[0])
        Room2Temp = float(values[1])
        Room3Temp = float(values[2])
        Room4Temp = float(values[3])
        OutsideTemp = float(values[4])

        requests.post("http://localhost:5000/room1", json={"room1temp": Room1Temp})
        requests.post("http://localhost:5000/room2", json={"room2temp": Room2Temp})
        requests.post("http://localhost:5000/room3", json={"room3temp": Room3Temp})
        requests.post("http://localhost:5000/room4", json={"room4temp": Room4Temp})
        requests.post("http://localhost:5000/outside", json={"outside": OutsideTemp})

    except UnicodeDecodeError:
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
            Ac = True
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
            Ac = True
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
            Ac = True
        # Outside Windows Cooling
        if OutsideTemp < Room3Temp and Room3Temp > DesiredTemp:
            r3w = True
        # Outside Windows Heating
        if OutsideTemp > Room3Temp and Room3Temp < DesiredTemp:
            r3w = True

    elif room == 4:
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
            Ac = True
        # Outside Windows Cooling
        if OutsideTemp < Room4Temp and Room4Temp > DesiredTemp:
            r4w = True
        # Outside Windows Heating
        if OutsideTemp > Room4Temp and Room4Temp < DesiredTemp:
            r4w = True

    # Servos for exterior windows
    if r1w:
        pca.servo[0].angle = 0
        pca.servo[1].angle = 180
    else:
        pca.servo[0].angle = 180
        pca.servo[1].angle = 0
    if r2w:
        pca.servo[2].angle = 0
        pca.servo[3].angle = 0
    else:
        pca.servo[2].angle = 180
        pca.servo[3].angle = 180
    if r3w:
        pca.servo[4].angle = 180
        pca.servo[5].angle = 120
    else:
        pca.servo[4].angle = 30
        pca.servo[5].angle = 0
    if r4w:
        pca.servo[6].angle = 0
        pca.servo[7].angle = 0
    else:
        pca.servo[6].angle = 180
        pca.servo[7].angle = 180

    # Servos for interior windows
    if r12w:
        pca.servo[8].angle = 90
        if r12Fan:
            GPIO.output(r12fPin, 1)
    else:
        pca.servo[8].angle = 0
        GPIO.output(r12fPin, 0)
    if r23w:
        pca.servo[9].angle = 90
        if r23Fan:
            GPIO.output(r23fPin, 1)
    else:
        pca.servo[9].angle = 0
        GPIO.output(r23fPin, 0)
    if r34w:
        pca.servo[10].angle = 90
        if r34Fan:
            GPIO.output(r34fPin, 1)
    else:
        pca.servo[10].angle = 0
        GPIO.output(r34fPin, 0)
    if r41w:
        pca.servo[11].angle = 90
        if r41Fan:
            GPIO.output(r41fPin, 1)
    else:
        pca.servo[11].angle = 0
        GPIO.output(r41fPin, 0)

    # Air Conditioning
    if Ac:
        GPIO.output(AcPin, 1)
    else:
        GPIO.output(AcPin, 0)

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

    time.sleep(1)


# Cleanup the GPIO pins
GPIO.cleanup()
ser.close()
