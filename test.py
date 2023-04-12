import requests
import json

acResponse = requests.get('http://localhost:5000/acOnOff')
acOnOff = acResponse.text
print("AC: " + acOnOff)

heatResponse = requests.get('http://localhost:5000/heatOnOff')
heatOnOff = heatResponse.text
print("Heat: " + heatOnOff)

inputResponse = requests.get('http://localhost:5000/input')
li = json.loads(inputResponse.text)
print("Desired: " + li[0])
print("Room: " + li[1])

def runSim():
    acCheck = int(acOnOff)
    heatCheck = int(heatOnOff)
    room = int(li[1])
    DesiredTemp = int(li[0])
    
    Room1Temp = 75
    Room2Temp = 60
    Room3Temp = 71
    Room4Temp = 80
    OutsideTemp = 72
    
    #Room1Temp = int(room1Temp.get())
    #Room2Temp = int(room2Temp.get())
    #Room3Temp = int(room3Temp.get())
    #Room4Temp = int(room4Temp.get())
    #OutsideTemp = int(outsideTemp.get())
    
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
            
    print(f"\n\n\nRoom 1 Window: {r1w}")
    print(f"Room 2 Window: {r2w}")
    print(f"Room 3 Window: {r3w}")
    print(f"Room 4 Window: {r4w}")

    print(f"Room 1-2 Window: {r12w}")
    print(f"Room 2-3 Window: {r23w}")
    print(f"Room 3-4 Window: {r34w}")
    print(f"Room 4-1 Window: {r41w}")

    print(f"Room 1-2 Fan: {r12Fan}")
    print(f"Room 2-3 Fan: {r23Fan}")
    print(f"Room 3-4 Fan: {r34Fan}")
    print(f"Room 4-1 Fan: {r41Fan}")

    print(f"Room 1 Heat: {r1Heat}")
    print(f"Room 2 Heat: {r2Heat}")
    print(f"Room 3 Heat: {r3Heat}")
    print(f"Room 4 Heat: {r4Heat}")

    print(f"Room 1 AC: {r1Ac}")
    print(f"Room 2 AC: {r2Ac}")
    print(f"Room 3 AC: {r3Ac}")
    print(f"Room 4 AC: {r4Ac}")
    
runSim()

