import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

count = 0
try:
    data = ser.readline().decode('utf-8').rstrip()
except UnicodeDecodeError as e:
    pass
while count < 1000:
    try:
        data = ser.readline().decode('utf-8').rstrip()
        print(data)
        
    except UnicodeDecodeError as e:
        #print(f"UnicodeDecodeError: {e}")
        pass
    count += 1   
ser.close()


