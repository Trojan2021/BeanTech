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
        values = data.split(",")
        value1 = float(values[0])
        value2 = float(values[1])
        value3 = int(values[2])
        value4 = int(values[3])
        value5 = int(values[4])
        print("Value 1:", value1)
        print("Value 2:", value2)
        print("Value 3:", value3)
        print("Value 4:", value4)
        print("Value 5:", value5)
        
        
    except UnicodeDecodeError as e:
        #print(f"UnicodeDecodeError: {e}")
        pass
    count += 1   
ser.close()
