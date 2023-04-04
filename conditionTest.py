# This file is made to test scenarios

# Is a simple GUI to set sensor values and then test how the
# system reacts to different scenarios.

import tkinter as tk


def runSim():
    # print(f"{heatVar.get()}\n{acVar.get()}")
    acCheck = acVar.get()
    heatState = heatVar.get()
    room = int(roomSelect.get())
    r1w = False
    r2w = False
    r3w = False
    r4w = False
    r12w = False
    r23w = False
    r34w = False
    r41w = False
    acState = False

    # Make sure AC is on
    if acCheck:
        # The user wants to cool room 1
        if room == 1:
            if room1Temp.get() > desiredTemp.get():
                acState = True
        elif room == 2:
            if room2Temp.get() > desiredTemp.get():
                acState = True
        elif room == 3:
            if room3Temp.get() > desiredTemp.get():
                acState = True
        elif room == 4:
            if room4Temp.get() > desiredTemp.get():
                acState = True
        else:
            print("Error: Invalid room number!")
    else:
        # No AC
        if room == 1:
            # TODO: Open windows and turn on fans
            pass
        elif room == 2:
            pass
        elif room == 3:
            pass
        elif room == 4:
            pass
        else:
            print("Error: Invalid room number!")

    if heatState:
        pass

    print(f"AC State: {acState}")
    print(f"Heat State: {heatState}")
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

room3Label = tk.Label(root, text="Room 2 Temp")
room3Label.grid(row=rowCount, column=0)

room3Temp = tk.Entry(root)
room3Temp.grid(row=rowCount, column=1)

rowCount += 1

room4Label = tk.Label(root, text="Room 2 Temp")
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
