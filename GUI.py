import tkinter as tk
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

# Sample values
Room1temp = 25.5
Room2temp = 26.8
Room1Light = 50
Room2Light = 80
Rotary = 0.5


# Create the main window
root = tk.Tk()

root.geometry("400x300")

# Create labels
room1_label = tk.Label(root, text="Room 1 temperature:")
room2_label = tk.Label(root, text="Room 2 temperature:")
room1_light_label = tk.Label(root, text="Room 1 light:")
room2_light_label = tk.Label(root, text="Room 2 light:")
rotary_label = tk.Label(root, text="Rotary:")
room1_temp_val = tk.Label(root, text=Room1temp)
room2_temp_val = tk.Label(root, text=Room2temp)
room1_light_val = tk.Label(root, text=Room1Light)
room2_light_val = tk.Label(root, text=Room2Light)
rotary_val = tk.Label(root, text=Rotary)

# Organize labels in a grid layout
room1_label.grid(row=0, column=0)
room2_label.grid(row=1, column=0)
room1_light_label.grid(row=2, column=0)
room2_light_label.grid(row=3, column=0)
rotary_label.grid(row=4, column=0)
room1_temp_val.grid(row=0, column=1)
room2_temp_val.grid(row=1, column=1)
room1_light_val.grid(row=2, column=1)
room2_light_val.grid(row=3, column=1)
rotary_val.grid(row=4, column=1)

def update_gui():
    try:
        data = ser.readline().decode('utf-8').rstrip()
        values = data.split(",")
        Room1temp = float(values[0])
        Room2temp = float(values[1])
        Room1Light = int(values[2])
        Room2Light = int(values[3])
        Rotary = int(values[4])
        
        # Update the label text with the new values
        room1_temp_val.config(text=Room1temp)
        room2_temp_val.config(text=Room2temp)
        room1_light_val.config(text=Room1Light)
        room2_light_val.config(text=Room2Light)
        rotary_val.config(text="N")
        
    except UnicodeDecodeError as e:
        #print(f"UnicodeDecodeError: {e}")
        pass
    
    # Schedule the next update after 1 second
    root.after(1000, update_gui)


def on_closing():
    ser.close()
    root.destroy()

update_gui()

# Start the main loop
root.mainloop()
