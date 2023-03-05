import serial
import cv2

ser = serial.Serial('/dev/ttyACM0', 9600)

count = 0
try:
    data = ser.readline().decode('utf-8').rstrip()
except UnicodeDecodeError as e:
    pass
while count < 1000:
    try:
        data = ser.readline().decode('utf-8').rstrip()
        values = data.split(",")
        Room1temp = float(values[0])
        Room2temp = float(values[1]) - 3.4
        Room1Light = int(values[2])
        Room2Light = int(values[3])
        Rotary = int(values[4])
        print("Value 1:", Room1temp)
        print("Value 2:", Room2temp)
        print("Value 3:", Room1Light)
        print("Value 4:", Room2Light)
        print("Value 5:", Rotary)
        
        
    except UnicodeDecodeError as e:
        #print(f"UnicodeDecodeError: {e}")
        pass
    count += 1 

ser.close()
