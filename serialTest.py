import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

count = 0
ser.readline().decode('utf-8').rstrip()
while count < 100:
    data = ser.readline().decode('utf-8').rstrip()
    print(data)
    count += 1   
ser.close()


