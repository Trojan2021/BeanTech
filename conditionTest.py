# This file is made to test scenarios

# Is a simple GUI to set sensor values and then test how the
# system reacts to different scenarios.

import tkinter as tk


def runSim():
    # print(f"{heatVar.get()}\n{acVar.get()}")
    acCheck = acVar.get()
    heatCheck = heatVar.get()
    room = int(roomSelect.get())
    r1w = False
    r2w = False
    r3w = False
    r4w = False
    r12w = False
    r23w = False
    r34w = False
    r41w = False
    r12Fan = False
    r23Fan = False
    r34Fan = False
    r41Fan = False
    r1Heat = False
    r2Heat = False
    r3Heat = False
    r4Heat = False
    r1Ac = False
    r2Ac = False
    r3Ac = False
    r4Ac = False
    r1OutW = False
    r2OutW = False
    r3OutW = False
    r4OutW = False
    heatState = False


    if room == 1:
        # Get room 1 warmer
        if room1Temp.get() < desiredTemp:
            # Heater
            if heatCheck and room1Temp.get() < desiredTemp:
                r1Heat = True
            # Interior Window
            if room2Temp.get() > room1Temp.get() and room1Temp.get() < desiredTemp: # Work on thinking about when the heater should be on or the AC
                r12w = True
                r12Fan = False
            # Interior Window
            if room4Temp.get() > room1Temp.get():
                r41w = True
                r41Fan = True
            # AC
            if acCheck and room1Temp.get() > desiredTemp:
                r1Ac = True
            # Outside Windows Cooling
            if outsideTemp.get() < room1Temp.get() and room1Temp.get() > desiredTemp:
                r1OutW = True
            # Outside Windows Heating
            if outsideTemp.get() > room1Temp.get() and room1Temp.get() < desiredTemp:
                r1OutW = True

    if room == 2:
        # Get room 2 warmer
        if room2Temp.get() < desiredTemp:
            # Heater
            if heatCheck and room2Temp.get() < desiredTemp:
                r2Heat = True
            # Interior Window
            if room2Temp.get() > room3Temp.get() and room2:
                r12w = True
                r12Fan = False
            # Interior Window
            if room4Temp.get() > room1Temp.get():
                r41w = True
                r41Fan = True
            # AC
            if acCheck and room2Temp.get() > desiredTemp:
                r1Ac = True
            # Outside Windows Cooling
            if outsideTemp.get() < room2Temp.get() and room2Temp.get() > desiredTemp:
                r1OutW = True
            # Outside Windows Heating
            if outsideTemp.get() > room2Temp.get() and room2Temp.get() < desiredTemp:
                r1OutW = True


    print(f"AC State: {acState}")
    print(f"Room 1 Heat State: {r1Heat}")
    print(f"Room 2 Heat State: {r2Heat}")
    print(f"Room 3 Heat State: {r3Heat}")
    print(f"Room 4 Heat State: {r4Heat}")
    print(f"Room 1 Window: {r1w}")
    print(f"Room 2 Window: {r2w}")
    print(f"Room 3 Window: {r3w}")
    print(f"Room 4 Window: {r4w}")
    print(f"Room 1-2 Window: {r12w}")
    print(f"Room 2-3 Window: {r23w}")
    print(f"Room 3-4 Window: {r34w}")
    print(f"Room 4-1 Window: {r41w}")


root = tk.Tk()
root.title("Scenario Test")

rowCount = 0

outsideLabel = tk.Label(root, text="Outside Temp:")
outsideLabel.grid(row=0, column=0)

outsideTemp = tk.Entry(root)
outsideTemp.grid(row=0, column=1)

rowCount += 1

room1Label = tk.Label(root, text="Room 1 Temp")
room1Label.grid(row=rowCount, column=0)

room1Temp = tk.Entry(root)
room1Temp.grid(row=rowCount, column=1)

rowCount += 1

room2Label = tk.Label(root, text="Room 2 Temp")
room2Label.grid(row=rowCount, column=0)

room2Temp = tk.Entry(root)
room2Temp.grid(row=rowCount, column=1)

rowCount += 1

room3Label = tk.Label(root, text="Room 3 Temp")
room3Label.grid(row=rowCount, column=0)

room3Temp = tk.Entry(root)
room3Temp.grid(row=rowCount, column=1)

rowCount += 1

room4Label = tk.Label(root, text="Room 4 Temp")
room4Label.grid(row=rowCount, column=0)

room4Temp = tk.Entry(root)
room4Temp.grid(row=rowCount, column=1)

rowCount += 1

heatVar = tk.IntVar()
heatCheck = tk.Checkbutton(root, text="Heater", variable=heatVar)
heatCheck.grid(row=rowCount, column=0)

acVar = tk.IntVar()
acCheck = tk.Checkbutton(root, text="AC", variable=acVar)
acCheck.grid(row=rowCount, column=1)

rowCount += 1

roomSelLabel = tk.Label(root, text="Room Selection")
roomSelLabel.grid(row=rowCount, column=0)

roomSelect = tk.Entry(root)
roomSelect.grid(row=rowCount, column=1)

rowCount += 1

desiredTempLabel = tk.Label(root, text="Desired Temp")
desiredTempLabel.grid(row=rowCount, column=0)

desiredTemp = tk.Entry(root)
desiredTemp.grid(row=rowCount, column=1)

rowCount += 1

button = tk.Button(root, text="Run Simulation", command=runSim)
button.grid(row=rowCount, column=0)

root.mainloop()
