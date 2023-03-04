import serial
import time


ser = serial.Serial('/dev/ttyACM0', 9600)
message = int(1)
print("here")
ser.write(bytes([message]))
print("There")
time.sleep(0.5)

print("No shot")
incoming = ser.readline()
print(incoming)

ser.close()


